"""Persistent operator + user teaching for Ask AI (survives agent/API swap)."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)

_BEH_MARK = "<!-- BEGIN BEHAVIOR -->"
_BEH_END = "<!-- END BEHAVIOR -->"
_FACT_MARK = "<!-- BEGIN FACTS -->"
_FACT_END = "<!-- END FACTS -->"
_LEARN_MARK = "<!-- BEGIN LEARNED -->"
_LEARN_END = "<!-- END LEARNED -->"

_BEHAVIOR_HINTS = (
    "ایموجی",
    "emoji",
    "چند خط",
    "چند سطر",
    "چند خطی",
    "لحن",
    "سبک",
    "رفتار",
    "format",
    "style",
    "وقتی یک کاربر",
    "وقتی کاربر",
    "زمان پاسخ",
    "پیام ها رو",
    "پیام‌ها را",
    "پیامها را",
    "از ایموجی",
    "دوستانه",
    "گرم",
)


@dataclass
class AIMemory:
    behavior: list[str] = field(default_factory=list)
    facts: list[str] = field(default_factory=list)
    learned: list[tuple[str, str]] = field(default_factory=list)


def memory_md_path(knowledge_root: Path, product_id: str) -> Path:
    safe = re.sub(r"[^a-zA-Z0-9._-]+", "-", (product_id or "").strip()).strip("-") or "product"
    return knowledge_root / "product_guides" / f"{safe}-ai-memory.md"


def is_behavior_text(text: str) -> bool:
    q = (text or "").strip().lower().replace("‌", "")
    return any(h in q for h in _BEHAVIOR_HINTS)


def _split_marked(raw: str, start: str, end: str) -> str:
    if start not in raw or end not in raw:
        return ""
    return raw.split(start, 1)[1].split(end, 1)[0]


def load_ai_memory(knowledge_root: Path, product_id: str) -> AIMemory:
    path = memory_md_path(knowledge_root, product_id)
    mem = AIMemory()
    if not path.is_file():
        return mem
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError:
        return mem
    beh = _split_marked(raw, _BEH_MARK, _BEH_END)
    facts = _split_marked(raw, _FACT_MARK, _FACT_END)
    learned = _split_marked(raw, _LEARN_MARK, _LEARN_END)
    mem.behavior = [ln[2:].strip() for ln in beh.splitlines() if ln.strip().startswith("- ")]
    mem.facts = [ln[2:].strip() for ln in facts.splitlines() if ln.strip().startswith("- ")]
    q = ""
    a_lines: list[str] = []
    for line in learned.splitlines():
        if line.startswith("### Q:"):
            if q and a_lines:
                mem.learned.append((q, "\n".join(a_lines).strip()))
            q = line[6:].strip()
            a_lines = []
        elif line.startswith("A:"):
            a_lines = [line[2:].strip()]
        elif q and line.strip():
            a_lines.append(line.strip())
    if q and a_lines:
        mem.learned.append((q, "\n".join(a_lines).strip()))
    return mem


def render_ai_memory_md(product_id: str, mem: AIMemory) -> str:
    beh = "\n".join(f"- {x}" for x in mem.behavior if x) or "- (none yet)"
    facts = "\n".join(f"- {x}" for x in mem.facts if x) or "- (none yet)"
    learned_bits: list[str] = []
    for q, a in mem.learned:
        learned_bits.append(f"### Q: {q}\nA: {a}")
    learned = "\n\n".join(learned_bits) if learned_bits else "(none yet)"
    return (
        f"# AI memory for {product_id}\n\n"
        "This file survives agent/API changes. Ask AI must read it first.\n"
        "Behavior rules override the default short/dry tone.\n"
        "If a learned Q matches the user, use that answer. Else use Operator facts, then the catalog.\n\n"
        "## Behavior rules\n"
        f"{_BEH_MARK}\n{beh}\n{_BEH_END}\n\n"
        "## Operator facts\n"
        f"{_FACT_MARK}\n{facts}\n{_FACT_END}\n\n"
        "## Learned user answers\n"
        f"{_LEARN_MARK}\n{learned}\n{_LEARN_END}\n"
    )


def save_ai_memory(knowledge_root: Path, product_id: str, mem: AIMemory) -> Path:
    path = memory_md_path(knowledge_root, product_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_ai_memory_md(product_id, mem), encoding="utf-8")
    return path


def _dedupe_append(items: list[str], text: str, *, limit: int) -> list[str]:
    t = (text or "").strip()
    if not t:
        return items
    items = [x for x in items if x.strip() != t]
    items.append(t)
    return items[-limit:]


def append_operator_teaching(
    knowledge_root: Path,
    product_id: str,
    text: str,
    *,
    kind: str | None = None,
) -> str:
    """Store operator chat/training. Returns 'behavior' or 'fact'."""
    mem = load_ai_memory(knowledge_root, product_id)
    decided = kind or ("behavior" if is_behavior_text(text) else "fact")
    if decided == "behavior":
        mem.behavior = _dedupe_append(mem.behavior, text, limit=40)
    else:
        mem.facts = _dedupe_append(mem.facts, text, limit=50)
    save_ai_memory(knowledge_root, product_id, mem)
    return decided


def append_learned_answer(
    knowledge_root: Path,
    product_id: str,
    question: str,
    answer: str,
) -> None:
    q = (question or "").strip()
    a = (answer or "").strip()
    if not product_id or len(q) < 4 or len(a) < 40:
        return
    mem = load_ai_memory(knowledge_root, product_id)
    mem.learned = [(qq, aa) for qq, aa in mem.learned if qq != q]
    mem.learned.append((q, a[:1800]))
    mem.learned = mem.learned[-40:]
    save_ai_memory(knowledge_root, product_id, mem)


def seed_memory_from_product(knowledge_root: Path, product_id: str) -> None:
    """Copy older JSON training into the md file once, so a new agent still sees it."""
    pid = (product_id or "").strip()
    if not pid:
        return
    mem = load_ai_memory(knowledge_root, pid)
    if mem.behavior or mem.facts or mem.learned:
        return
    try:
        from src.knowledge.product_catalogs import load_product_raw
    except Exception:  # noqa: BLE001
        return
    raw = load_product_raw(knowledge_root, pid) or {}
    train = str(raw.get("ai_training_text") or "").strip()
    if not train:
        return
    for part in re.split(r"\n{2,}", train):
        if part.strip():
            append_operator_teaching(knowledge_root, pid, part.strip())


def behavior_rules_text(knowledge_root: Path, product_id: str) -> str:
    seed_memory_from_product(knowledge_root, product_id)
    mem = load_ai_memory(knowledge_root, product_id)
    return "\n".join(f"- {x}" for x in mem.behavior if x)


def memory_prompt_block(knowledge_root: Path, product_id: str, *, limit: int = 4500) -> str:
    pid = (product_id or "").strip()
    if not pid:
        return ""
    seed_memory_from_product(knowledge_root, pid)
    path = memory_md_path(knowledge_root, pid)
    if not path.is_file():
        return ""
    try:
        raw = path.read_text(encoding="utf-8").strip()
    except OSError:
        return ""
    header = (
        "### Operator AI memory (CHECK FIRST — before catalog)\n"
        "Follow Behavior rules for tone/format in every Ask AI reply.\n"
        "If Learned user answers contain this question, reuse that answer.\n"
        "If not found here, use the product catalog next.\n\n"
    )
    return (header + raw)[:limit]
