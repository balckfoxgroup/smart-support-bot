"""One Ask AI turn: text + media from the same retrieval context."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class MediaRef:
    path: str
    product_id: str
    unit_id: str = ""
    feature_ids: list[str] = field(default_factory=list)
    score: float = 0.0

    def as_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "product_id": self.product_id,
            "unit_id": self.unit_id,
            "feature_ids": list(self.feature_ids),
            "score": self.score,
        }

    @classmethod
    def from_dict(cls, raw: dict[str, Any] | None) -> MediaRef | None:
        if not isinstance(raw, dict):
            return None
        path = str(raw.get("path") or "").strip()
        pid = str(raw.get("product_id") or "").strip()
        if not path or not pid:
            return None
        feats = raw.get("feature_ids") if isinstance(raw.get("feature_ids"), list) else []
        return cls(
            path=path,
            product_id=pid,
            unit_id=str(raw.get("unit_id") or ""),
            feature_ids=[str(x).strip() for x in feats if str(x).strip()],
            score=float(raw.get("score") or 0.0),
        )


@dataclass(slots=True)
class ResponseBundle:
    product_id: str
    user_query: str
    answer_text: str = ""
    knowledge_refs: list[str] = field(default_factory=list)
    media_refs: list[MediaRef] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "product_id": self.product_id,
            "user_query": self.user_query,
            "answer_text": (self.answer_text or "")[:500],
            "knowledge_refs": list(self.knowledge_refs),
            "media_refs": [m.as_dict() for m in self.media_refs],
        }

    @classmethod
    def from_dict(cls, raw: dict[str, Any] | None) -> ResponseBundle | None:
        if not isinstance(raw, dict):
            return None
        pid = str(raw.get("product_id") or "").strip()
        if not pid:
            return None
        refs: list[MediaRef] = []
        for item in raw.get("media_refs") or []:
            ref = MediaRef.from_dict(item if isinstance(item, dict) else None)
            if ref:
                refs.append(ref)
        know = raw.get("knowledge_refs") if isinstance(raw.get("knowledge_refs"), list) else []
        return cls(
            product_id=pid,
            user_query=str(raw.get("user_query") or ""),
            answer_text=str(raw.get("answer_text") or ""),
            knowledge_refs=[str(x) for x in know if str(x).strip()],
            media_refs=refs,
        )


def validate_media_for_response(
    media: MediaRef,
    *,
    product_id: str,
    knowledge_refs: list[str] | None = None,
    project_root: Path | None = None,
    min_score: float = 8.0,
) -> bool:
    """Send only if media is same product and tied to this retrieval."""
    pid = (product_id or "").strip()
    if not pid or media.product_id != pid:
        return False
    path = Path(media.path)
    if project_root is not None and not path.is_absolute():
        path = (project_root / media.path).resolve()
    try:
        if not path.is_file():
            return False
    except OSError:
        return False
    know = {k for k in (knowledge_refs or []) if k}
    if media.unit_id and media.unit_id in know:
        return True
    if media.feature_ids and any(
        any(fid in k for k in know) for fid in media.feature_ids
    ):
        return True
    return media.score >= min_score


def existing_media_paths(
    refs: list[MediaRef],
    *,
    product_id: str,
    knowledge_refs: list[str] | None,
    project_root: Path,
    limit: int = 2,
) -> list[Path]:
    out: list[Path] = []
    seen: set[str] = set()
    for ref in refs:
        if not validate_media_for_response(
            ref,
            product_id=product_id,
            knowledge_refs=knowledge_refs,
            project_root=project_root,
        ):
            continue
        path = Path(ref.path)
        if not path.is_absolute():
            path = (project_root / ref.path).resolve()
        key = str(path).lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(path)
        if len(out) >= limit:
            break
    return out
