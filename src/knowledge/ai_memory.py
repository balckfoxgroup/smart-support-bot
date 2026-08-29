"""Persistent operator + user teaching for Ask AI (survives agent/API swap)."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)

GLOBAL_ID = "_global"

_BEH_MARK = "<!-- BEGIN BEHAVIOR -->"
_BEH_END = "<!-- END BEHAVIOR -->"
_FACT_MARK = "<!-- BEGIN FACTS -->"
_FACT_END = "<!-- END FACTS -->"
_LEARN_MARK = "<!-- BEGIN LEARNED -->"
_LEARN_END = "<!-- END LEARNED -->"
_CAT_MARK = "<!-- BEGIN CATALOG -->"
_CAT_END = "<!-- END CATALOG -->"

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
    catalog: str = ""
    learned: list[tuple[str, str]] = field(default_factory=list)


def _safe_pid(product_id: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", (product_id or "").strip()).strip("-") or "product"


def memory_md_path(knowledge_root: Path, product_id: str) -> Path:
    return knowledge_root / "product_guides" / f"{_safe_pid(product_id)}-ai-memory.md"


def behavior_md_path(knowledge_root: Path, product_id: str) -> Path:
    return knowledge_root / "product_guides" / f"{_safe_pid(product_id)}-AI_BEHAVIOR.md"


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
    catalog = _split_marked(raw, _CAT_MARK, _CAT_END).strip()
    mem.behavior = [ln[2:].strip() for ln in beh.splitlines() if ln.strip().startswith("- ")]
    mem.facts = [ln[2:].strip() for ln in facts.splitlines() if ln.strip().startswith("- ")]
    mem.catalog = "" if catalog in {"(none yet)", "- (none yet)"} else catalog
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
    catalog = mem.catalog.strip() or "(none yet)"
    return (
        f"# AI memory for {product_id}\n\n"
        "This file survives agent/API changes. Ask AI must read it first.\n"
        "Behavior rules (from Chat with AI) override the default short/dry tone.\n"
        "Catalog teaching is only about catalog photos/facts and how to teach users from the catalog.\n"
        "If a learned Q matches the user, use that answer. Else use Operator facts, then catalog teaching, then the catalog.\n\n"
        "## Behavior rules\n"
        f"{_BEH_MARK}\n{beh}\n{_BEH_END}\n\n"
        "## Operator facts\n"
        f"{_FACT_MARK}\n{facts}\n{_FACT_END}\n\n"
        "## Catalog teaching\n"
        f"{_CAT_MARK}\n{catalog}\n{_CAT_END}\n\n"
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


def write_product_behavior_md(knowledge_root: Path, product_id: str) -> Path:
    """Write this product's AI_BEHAVIOR.md immediately (no other products)."""
    pid = (product_id or "").strip()
    mem = load_ai_memory(knowledge_root, pid)
    path = behavior_md_path(knowledge_root, pid)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [x for x in mem.behavior if x]
    facts = [x for x in mem.facts if x]
    path.write_text(
        f"# AI_BEHAVIOR for {pid}\n\n"
        "This file is only for this product. Do not use another catalog.\n\n"
        "## Behavior\n"
        + ("\n".join(f"- {x}" for x in lines) if lines else "- (none yet)")
        + "\n\n## Product teaching\n"
        + ("\n".join(f"- {x}" for x in facts) if facts else "- (none yet)")
        + "\n",
        encoding="utf-8",
    )
    return path


def append_operator_teaching(
    knowledge_root: Path,
    product_id: str,
    text: str,
    *,
    kind: str | None = None,
    all_products: bool = False,
) -> list[str]:
    """Store teaching on the chosen product(s) only. Returns target ids."""
    decided = kind or ("behavior" if is_behavior_text(text) else "fact")
    targets: list[str] = []
    if all_products:
        try:
            from src.knowledge.product_catalogs import get_product_catalogs

            targets = [c.product_id for c in get_product_catalogs()]
        except Exception:  # noqa: BLE001
            targets = []
    else:
        pid = (product_id or "").strip()
        if pid and pid != GLOBAL_ID:
            targets = [pid]
    if not targets:
        return []
    for target in targets:
        mem = load_ai_memory(knowledge_root, target)
        if decided == "behavior":
            mem.behavior = _dedupe_append(mem.behavior, text, limit=40)
        else:
            mem.facts = _dedupe_append(mem.facts, text, limit=50)
        save_ai_memory(knowledge_root, target, mem)
        write_product_behavior_md(knowledge_root, target)
    return targets


def catalog_training_md_path(knowledge_root: Path, product_id: str) -> Path:
    return knowledge_root / "product_guides" / f"{_safe_pid(product_id)}-catalog-training.md"


def write_catalog_training_md(knowledge_root: Path, product_id: str, text: str) -> Path:
    """Write catalog teaching into a product-scoped markdown file for Ask AI."""
    pid = (product_id or "").strip()
    path = catalog_training_md_path(knowledge_root, pid)
    path.parent.mkdir(parents=True, exist_ok=True)
    body = (text or "").strip()
    path.write_text(
        f"# Catalog training for {pid}\n\n"
        "Use only for this product catalog. Do not mix other products.\n\n"
        + (body if body else "(none yet)")
        + "\n",
        encoding="utf-8",
    )
    return path


def set_catalog_teaching(knowledge_root: Path, product_id: str, text: str) -> None:
    """Replace catalog-only teaching (edit or clear)."""
    mem = load_ai_memory(knowledge_root, product_id)
    mem.catalog = (text or "").strip()
    save_ai_memory(knowledge_root, product_id, mem)
    write_catalog_training_md(knowledge_root, product_id, mem.catalog)


def get_catalog_training(knowledge_root: Path, product_id: str) -> str:
    """Source of truth: product JSON ai_training_text. Markdown is cache only."""
    pid = (product_id or "").strip()
    if not pid:
        return ""
    from src.knowledge.product_catalogs import load_product_raw

    raw = load_product_raw(knowledge_root, pid) or {}
    train = str(raw.get("ai_training_text") or "").strip()
    if train:
        return train
    return load_ai_memory(knowledge_root, pid).catalog.strip()


def replace_catalog_training(knowledge_root: Path, product_id: str, text: str) -> str:
    """Replace catalog teaching in JSON; markdown is write-through cache."""
    pid = (product_id or "").strip()
    combined = (text or "").strip()
    from src.knowledge.product_catalogs import load_product_raw, save_product_raw

    raw = load_product_raw(knowledge_root, pid) or {}
    raw["ai_training_text"] = combined
    save_product_raw(knowledge_root, pid, raw)
    set_catalog_teaching(knowledge_root, pid, combined)
    return combined


def append_catalog_training(knowledge_root: Path, product_id: str, new_text: str) -> str:
    """Append new catalog teaching to the product JSON. Returns full text."""
    pid = (product_id or "").strip()
    add = (new_text or "").strip()
    prev = get_catalog_training(knowledge_root, pid)
    combined = (prev + "\n\n" + add).strip() if prev and add else (add or prev)
    return replace_catalog_training(knowledge_root, pid, combined)


def catalog_teaching_text(knowledge_root: Path, product_id: str) -> str:
    return get_catalog_training(knowledge_root, product_id)


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
    """Copy catalog JSON training into memory if the catalog slot is empty."""
    pid = (product_id or "").strip()
    if not pid:
        return
    mem = load_ai_memory(knowledge_root, pid)
    try:
        from src.knowledge.product_catalogs import load_product_raw
    except Exception:  # noqa: BLE001
        return
    raw = load_product_raw(knowledge_root, pid) or {}
    train = str(raw.get("ai_training_text") or "").strip()
    if train and not mem.catalog:
        mem.catalog = train
        save_ai_memory(knowledge_root, pid, mem)
        write_catalog_training_md(knowledge_root, pid, train)


def behavior_rules_text(knowledge_root: Path, product_id: str | None = None) -> str:
    pid = (product_id or "").strip()
    if not pid or pid == GLOBAL_ID:
        return ""
    rules = [x.strip() for x in load_ai_memory(knowledge_root, pid).behavior if x.strip()]
    return "\n".join(f"- {x}" for x in rules)


def product_memory_has_content(knowledge_root: Path, product_id: str | None) -> bool:
    pid = (product_id or "").strip()
    if not pid:
        return False
    mem = load_ai_memory(knowledge_root, pid)
    return bool(mem.behavior or mem.facts or mem.catalog or mem.learned)


def memory_prompt_block(
    knowledge_root: Path, product_id: str | None = None, *, limit: int = 4500
) -> str:
    pid = (product_id or "").strip()
    if not pid or pid == GLOBAL_ID:
        return ""
    parts: list[str] = [
        f"### Operator AI memory for product_id={pid} ONLY\n"
        "Do not use another product catalog. If this file and this product catalog "
        "lack the fact, say you do not know. Never invent."
    ]
    mem_path = memory_md_path(knowledge_root, pid)
    beh_path = behavior_md_path(knowledge_root, pid)
    train_path = catalog_training_md_path(knowledge_root, pid)
    for path in (beh_path, mem_path, train_path):
        if not path.is_file():
            continue
        try:
            raw = path.read_text(encoding="utf-8").strip()
        except OSError:
            continue
        if raw:
            parts.append(raw)
    return "\n\n".join(parts)[:limit] if len(parts) > 1 else ""
