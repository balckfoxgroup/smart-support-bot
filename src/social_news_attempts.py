"""Append-only log of social-news publish attempts (for admin Report)."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

IRAN_TZ = ZoneInfo("Asia/Tehran")
logger = logging.getLogger(__name__)

_KEEP_DAYS = 14  # prune file older than this; report UI shows 3 days


def _path(data_dir: Path) -> Path:
    return data_dir / "social_news_attempts.jsonl"


def record_news_attempt(
    data_dir: Path,
    *,
    ok: bool,
    reason: str,
    title: str = "",
    link: str = "",
    target: str = "",
    source: str = "",
) -> None:
    path = _path(data_dir)
    row = {
        "ts": datetime.now(ZoneInfo("UTC")).isoformat(),
        "ok": bool(ok),
        "reason": (reason or "")[:400],
        "title": (title or "")[:200],
        "link": (link or "")[:400],
        "target": (target or "")[:120],
        "source": (source or "")[:120],
    }
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    except OSError as exc:
        logger.warning("social news attempt log write failed: %s", exc)


def _parse_ts(raw: str) -> datetime | None:
    try:
        return datetime.fromisoformat(str(raw).replace("Z", "+00:00"))
    except Exception:
        return None


def load_news_attempts(
    data_dir: Path,
    *,
    days: int = 3,
) -> list[dict[str, Any]]:
    """Return attempts in the last ``days`` (Iran calendar window), newest first."""
    path = _path(data_dir)
    cutoff = datetime.now(ZoneInfo("UTC")) - timedelta(days=max(1, int(days)))
    rows: list[dict[str, Any]] = []
    if path.is_file():
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            lines = []
        keep_lines: list[str] = []
        prune_cut = datetime.now(ZoneInfo("UTC")) - timedelta(days=_KEEP_DAYS)
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(item, dict):
                continue
            ts = _parse_ts(str(item.get("ts") or ""))
            if ts is None:
                continue
            if ts >= prune_cut:
                keep_lines.append(json.dumps(item, ensure_ascii=False))
            if ts >= cutoff:
                rows.append(item)
        # Opportunistic prune
        if path.is_file() and len(keep_lines) < len(lines):
            try:
                tmp = path.with_suffix(".jsonl.tmp")
                tmp.write_text("\n".join(keep_lines) + ("\n" if keep_lines else ""), encoding="utf-8")
                tmp.replace(path)
            except OSError:
                pass
    # Backfill successful posts from publications if attempts log is thin.
    pub = data_dir / "social_news_publications.jsonl"
    if pub.is_file():
        seen_links = {str(r.get("link") or "") for r in rows if r.get("ok")}
        try:
            for line in pub.read_text(encoding="utf-8", errors="replace").splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if not isinstance(item, dict):
                    continue
                ts = _parse_ts(str(item.get("published_at") or ""))
                if ts is None or ts < cutoff:
                    continue
                link = str(item.get("link") or "")
                if link and link in seen_links:
                    continue
                rows.append(
                    {
                        "ts": ts.isoformat(),
                        "ok": True,
                        "reason": "published",
                        "title": str(item.get("title") or ""),
                        "link": link,
                        "target": str(item.get("target") or ""),
                        "source": str(item.get("source") or ""),
                    }
                )
                if link:
                    seen_links.add(link)
        except OSError:
            pass

    def sort_key(row: dict[str, Any]) -> float:
        ts = _parse_ts(str(row.get("ts") or ""))
        return ts.timestamp() if ts else 0.0

    rows.sort(key=sort_key, reverse=True)
    return rows
