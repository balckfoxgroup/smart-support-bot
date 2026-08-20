"""Local answer memory — API-independent learning from grounded replies.

Stores topic → source links (+ optional answer text) on disk under data/.
Survives model/API changes because nothing is kept only in the cloud provider.
"""

from __future__ import annotations

import hashlib
import json
import logging
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.knowledge.catalog_rag import expand_query, _norm, _tokens

logger = logging.getLogger(__name__)

MAX_ENTRIES = 500
MIN_ANSWER_LEN = 80


@dataclass(slots=True)
class MemoryHit:
    topic_key: str
    answer: str
    unit_ids: list[str]
    source: str
    score: float
    hits: int


def _topic_key(query: str) -> str:
    expanded = expand_query(query)
    toks = sorted(set(t for t in _tokens(expanded) if len(t) >= 3))
    blob = " ".join(toks[:24]) or _norm(query)[:80]
    return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:16]


class AnswerMemoryStore:
    """JSON-backed memory shared across users; independent of AI provider."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._data: dict[str, Any] = {"version": 1, "entries": []}
        self._load()

    def _load(self) -> None:
        if not self.path.is_file():
            return
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("answer memory load failed: %s", exc)
            return
        if isinstance(raw, dict) and isinstance(raw.get("entries"), list):
            self._data = raw

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        tmp.replace(self.path)

    def lookup(self, query: str, *, lang: str) -> MemoryHit | None:
        q_norm = _norm(query)
        q_exp = expand_query(query)
        q_key = _topic_key(query)
        q_toks = set(_tokens(q_exp))
        best: MemoryHit | None = None
        for row in self._data.get("entries") or []:
            if not isinstance(row, dict):
                continue
            if str(row.get("lang") or "") not in {lang, "", "en"}:
                # Prefer same language; still allow en as weak fallback later
                pass
            answer = str(row.get("answer") or "").strip()
            if len(answer) < MIN_ANSWER_LEN:
                continue
            score = 0.0
            if str(row.get("topic_key") or "") == q_key:
                score += 12.0
            prev_q = _norm(str(row.get("query_norm") or ""))
            if prev_q and (prev_q in q_norm or q_norm in prev_q):
                score += 8.0
            prev_toks = set(_tokens(str(row.get("query_expanded") or prev_q)))
            if q_toks and prev_toks:
                overlap = len(q_toks & prev_toks) / max(1, len(q_toks))
                score += overlap * 10.0
                if overlap >= 0.45:
                    score += 2.0
            # Same feature units → stronger paraphrase match
            row_units = {str(x) for x in (row.get("unit_ids") or []) if x}
            if row_units and any(u.startswith("feature:") for u in row_units):
                # Soft boost when query expands to same aliases already stored
                prev_exp = _norm(str(row.get("query_expanded") or ""))
                if prev_exp and any(t in prev_exp for t in q_toks if len(t) >= 4):
                    score += 1.5
            # Same-lang boost
            if str(row.get("lang") or "") == lang:
                score += 2.0
            if score < 10.0:
                continue
            hit = MemoryHit(
                topic_key=str(row.get("topic_key") or q_key),
                answer=answer,
                unit_ids=[str(x) for x in (row.get("unit_ids") or []) if x],
                source=str(row.get("source") or "memory"),
                score=score,
                hits=int(row.get("hits") or 0),
            )
            if best is None or hit.score > best.score:
                best = hit
        return best

    def remember(
        self,
        *,
        query: str,
        lang: str,
        answer: str,
        unit_ids: list[str],
        source: str,
        grounded: bool,
    ) -> bool:
        """Store only grounded, complete answers (catalog/MD backed)."""
        if not grounded:
            return False
        text = (answer or "").strip()
        if len(text) < MIN_ANSWER_LEN:
            return False
        # Reject unsure / error-like replies
        low = text.lower()
        bad = (
            "اطلاعات کافی",
            "نمی‌دانم",
            "نمیدانم",
            "i don't know",
            "i do not know",
            "ai is temporarily",
            "پاسخ ai در دسترس نیست",
            "temporarily unavailable",
        )
        if any(b in low for b in bad):
            return False
        if text.endswith(("…", "...")) and len(text) < 200:
            return False

        key = _topic_key(query)
        entries: list[dict[str, Any]] = list(self._data.get("entries") or [])
        now = int(time.time())
        for row in entries:
            if not isinstance(row, dict):
                continue
            if str(row.get("topic_key")) == key and str(row.get("lang")) == lang:
                row["answer"] = text
                row["query_norm"] = _norm(query)
                row["query_expanded"] = expand_query(query)
                row["unit_ids"] = list(dict.fromkeys(unit_ids))[:12]
                row["source"] = source
                row["hits"] = int(row.get("hits") or 0) + 1
                row["updated_at"] = now
                self._data["entries"] = entries
                self._save()
                return True

        entries.append(
            {
                "topic_key": key,
                "lang": lang,
                "query_norm": _norm(query),
                "query_expanded": expand_query(query),
                "unit_ids": list(dict.fromkeys(unit_ids))[:12],
                "source": source,
                "answer": text,
                "hits": 1,
                "created_at": now,
                "updated_at": now,
            }
        )
        # Cap size — drop oldest by updated_at
        if len(entries) > MAX_ENTRIES:
            entries.sort(key=lambda r: int(r.get("updated_at") or 0), reverse=True)
            entries = entries[:MAX_ENTRIES]
        self._data["entries"] = entries
        self._save()
        return True

    def touch_hit(self, topic_key: str, lang: str) -> None:
        for row in self._data.get("entries") or []:
            if (
                isinstance(row, dict)
                and str(row.get("topic_key")) == topic_key
                and str(row.get("lang")) == lang
            ):
                row["hits"] = int(row.get("hits") or 0) + 1
                row["updated_at"] = int(time.time())
                self._save()
                return
