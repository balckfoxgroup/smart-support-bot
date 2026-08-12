"""Minimal persistent user preferences (language)."""

from __future__ import annotations

import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from src.config import DEFAULT_LANG, normalize_lang

logger = logging.getLogger(__name__)
IRAN_TZ = ZoneInfo("Asia/Tehran")


class UserStore:
    """Async-safe wrapper around data/users.json."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._lock = asyncio.Lock()
        self._data: dict[str, Any] = {"users": {}}
        self._load()

    def _load(self) -> None:
        if not self.path.is_file():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self._save_sync()
            return
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            if isinstance(raw, dict) and isinstance(raw.get("users"), dict):
                self._data = raw
            else:
                self._data = {"users": {}}
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("users.json unreadable (%s); starting fresh", exc)
            self._data = {"users": {}}

    def _save_sync(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        tmp.replace(self.path)

    def _get_user(self, user_id: int) -> dict[str, Any]:
        key = str(user_id)
        users = self._data.setdefault("users", {})
        entry = users.get(key)
        return entry if isinstance(entry, dict) else {}

    async def has_lang(self, user_id: int) -> bool:
        """True only when the user explicitly chose a language."""
        async with self._lock:
            user = self._get_user(user_id)
            return bool(user.get("lang_chosen"))

    async def get_lang(
        self, user_id: int, telegram_language_code: str | None = None
    ) -> str:
        """Return stored language if chosen; otherwise a Telegram hint for picker chrome."""
        async with self._lock:
            user = self._get_user(user_id)
            if user.get("lang_chosen") and user.get("lang"):
                return normalize_lang(str(user["lang"]))
        return normalize_lang(telegram_language_code) or DEFAULT_LANG

    async def set_lang(self, user_id: int, lang: str) -> tuple[str, bool]:
        """Persist language and mark lang_chosen=True. Returns (lang, is_new_user)."""
        normalized = normalize_lang(lang)
        key = str(user_id)
        async with self._lock:
            users = self._data.setdefault("users", {})
            prior = users.get(key)
            entry = dict(prior) if isinstance(prior, dict) else {}
            is_new = not bool(entry.get("first_seen"))
            entry["lang"] = normalized
            entry["lang_chosen"] = True
            if is_new:
                entry["first_seen"] = datetime.now(IRAN_TZ).isoformat()
            users[key] = entry
            self._save_sync()
        return normalized, is_new

    async def clear_lang(self, user_id: int) -> None:
        """Reset language choice (testing / admin)."""
        key = str(user_id)
        async with self._lock:
            users = self._data.setdefault("users", {})
            users.pop(key, None)
            self._save_sync()

    async def is_ask_ai(self, user_id: int) -> bool:
        """True while user is in free-text Ask AI mode."""
        async with self._lock:
            return bool(self._get_user(user_id).get("ask_ai"))

    async def set_ask_ai(self, user_id: int, enabled: bool) -> None:
        key = str(user_id)
        async with self._lock:
            users = self._data.setdefault("users", {})
            entry = dict(self._get_user(user_id))
            entry["ask_ai"] = bool(enabled)
            if not enabled:
                entry["chat_history"] = []
            users[key] = entry
            self._save_sync()

    async def get_chat_history(self, user_id: int) -> list[dict[str, str]]:
        async with self._lock:
            hist = self._get_user(user_id).get("chat_history") or []
            if not isinstance(hist, list):
                return []
            out: list[dict[str, str]] = []
            for item in hist:
                if isinstance(item, dict) and item.get("role") and item.get("content"):
                    out.append(
                        {"role": str(item["role"]), "content": str(item["content"])}
                    )
            return out

    async def set_group_invited(self, user_id: int, invited: bool = True) -> None:
        key = str(user_id)
        async with self._lock:
            users = self._data.setdefault("users", {})
            entry = dict(self._get_user(user_id))
            entry["group_invited"] = bool(invited)
            users[key] = entry
            self._save_sync()

    async def was_group_invited(self, user_id: int) -> bool:
        async with self._lock:
            return bool(self._get_user(user_id).get("group_invited"))

    async def append_chat(
        self, user_id: int, role: str, content: str, *, limit: int = 8
    ) -> None:
        key = str(user_id)
        text = (content or "").strip()
        if not text:
            return
        async with self._lock:
            users = self._data.setdefault("users", {})
            entry = dict(self._get_user(user_id))
            hist = entry.get("chat_history")
            if not isinstance(hist, list):
                hist = []
            hist = list(hist)
            hist.append({"role": role, "content": text[:2000]})
            entry["chat_history"] = hist[-limit:]
            users[key] = entry
            self._save_sync()
