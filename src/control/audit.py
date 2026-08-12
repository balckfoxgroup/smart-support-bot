"""Append-only audit log for Control Plane actions."""

from __future__ import annotations

import asyncio
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def _utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


class AuditLog:
    """Persists control events to data/control_audit.jsonl (no secrets)."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._lock = asyncio.Lock()
        self.path.parent.mkdir(parents=True, exist_ok=True)

    async def write(
        self,
        action: str,
        *,
        admin_id: int | None = None,
        detail: str = "",
        meta: dict[str, Any] | None = None,
    ) -> None:
        # Never accept keys that look like secrets
        safe_meta = {}
        for k, v in (meta or {}).items():
            lk = str(k).lower()
            if any(x in lk for x in ("key", "token", "secret", "password", "authorization")):
                continue
            safe_meta[k] = v
        line = {
            "at": _utcnow(),
            "action": action,
            "admin_id": admin_id,
            "detail": detail[:500],
            "meta": safe_meta,
        }
        async with self._lock:
            with self.path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(line, ensure_ascii=False) + "\n")

    async def tail(self, limit: int = 20) -> list[dict[str, Any]]:
        if not self.path.is_file():
            return []
        async with self._lock:
            try:
                lines = self.path.read_text(encoding="utf-8").splitlines()
            except OSError:
                return []
        out: list[dict[str, Any]] = []
        for raw in lines[-max(1, limit) :]:
            try:
                row = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if isinstance(row, dict):
                out.append(row)
        return out

    def format_tail(self, rows: list[dict[str, Any]]) -> str:
        if not rows:
            return "No audit events yet."
        lines = ["📜 Audit Log (latest)", ""]
        for row in rows:
            who = row.get("admin_id") or "system"
            lines.append(
                f"{row.get('at', '?')} — admin={who} — {row.get('action')} — {row.get('detail', '')}"
            )
        return "\n".join(lines)
