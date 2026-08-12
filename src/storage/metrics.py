"""Persistent operational metrics for admin bot-stats reports."""

from __future__ import annotations

import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

IRAN_TZ = ZoneInfo("Asia/Tehran")
logger = logging.getLogger(__name__)


def _today_key() -> str:
    return datetime.now(IRAN_TZ).strftime("%Y-%m-%d")


def _empty_day() -> dict[str, Any]:
    return {
        "new_users": 0,
        "conversations": 0,
        "answered": 0,
        "support_referrals": 0,
        "ai_solved": 0,
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
        "spend_usd": 0.0,
        "active_user_ids": [],
    }


class MetricsStore:
    """Async-safe daily counters under data/bot_metrics.json."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._lock = asyncio.Lock()
        self._data: dict[str, Any] = {"days": {}, "lifetime_spend_usd": 0.0}
        self._load()

    def _load(self) -> None:
        if not self.path.is_file():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self._save_sync()
            return
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                days = raw.get("days")
                if not isinstance(days, dict):
                    days = {}
                self._data = {
                    "days": days,
                    "lifetime_spend_usd": float(raw.get("lifetime_spend_usd") or 0.0),
                }
            else:
                self._data = {"days": {}, "lifetime_spend_usd": 0.0}
        except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
            logger.warning("bot_metrics.json unreadable (%s); starting fresh", exc)
            self._data = {"days": {}, "lifetime_spend_usd": 0.0}

    def _save_sync(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        tmp.replace(self.path)

    def _day(self, day: str | None = None) -> dict[str, Any]:
        key = day or _today_key()
        days = self._data.setdefault("days", {})
        row = days.get(key)
        if not isinstance(row, dict):
            row = _empty_day()
            days[key] = row
        for field, default in _empty_day().items():
            row.setdefault(field, default)
        return row

    async def record_new_user(self) -> None:
        async with self._lock:
            day = self._day()
            day["new_users"] = int(day.get("new_users") or 0) + 1
            self._save_sync()

    async def record_conversation(self, user_id: int) -> None:
        async with self._lock:
            day = self._day()
            day["conversations"] = int(day.get("conversations") or 0) + 1
            active = day.get("active_user_ids")
            if not isinstance(active, list):
                active = []
            uid = str(user_id)
            if uid not in active:
                active.append(uid)
            day["active_user_ids"] = active[-5000:]
            self._save_sync()

    async def record_answered(self, *, referred_support: bool, ai_solved: bool) -> None:
        async with self._lock:
            day = self._day()
            day["answered"] = int(day.get("answered") or 0) + 1
            if referred_support:
                day["support_referrals"] = int(day.get("support_referrals") or 0) + 1
            if ai_solved:
                day["ai_solved"] = int(day.get("ai_solved") or 0) + 1
            self._save_sync()

    async def record_token_usage(
        self,
        *,
        prompt_tokens: int,
        completion_tokens: int,
        total_tokens: int,
        spend_usd: float,
    ) -> None:
        async with self._lock:
            day = self._day()
            day["prompt_tokens"] = int(day.get("prompt_tokens") or 0) + max(0, prompt_tokens)
            day["completion_tokens"] = int(day.get("completion_tokens") or 0) + max(
                0, completion_tokens
            )
            day["total_tokens"] = int(day.get("total_tokens") or 0) + max(0, total_tokens)
            spend = max(0.0, float(spend_usd))
            day["spend_usd"] = float(day.get("spend_usd") or 0.0) + spend
            self._data["lifetime_spend_usd"] = float(
                self._data.get("lifetime_spend_usd") or 0.0
            ) + spend
            self._save_sync()

    async def snapshot(self, day: str | None = None) -> dict[str, Any]:
        async with self._lock:
            key = day or _today_key()
            row = dict(self._day(key))
            return {
                "day": key,
                "new_users": int(row.get("new_users") or 0),
                "conversations": int(row.get("conversations") or 0),
                "answered": int(row.get("answered") or 0),
                "support_referrals": int(row.get("support_referrals") or 0),
                "ai_solved": int(row.get("ai_solved") or 0),
                "prompt_tokens": int(row.get("prompt_tokens") or 0),
                "completion_tokens": int(row.get("completion_tokens") or 0),
                "total_tokens": int(row.get("total_tokens") or 0),
                "spend_usd": float(row.get("spend_usd") or 0.0),
                "lifetime_spend_usd": float(self._data.get("lifetime_spend_usd") or 0.0),
                "active_users": len(row.get("active_user_ids") or []),
            }
