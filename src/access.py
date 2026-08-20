"""Admin role access: full (settings) vs stats-only."""

from __future__ import annotations

from typing import Literal

from src.config import Settings
from src.storage.bot_settings import BotSettingsStore

Role = Literal["full", "stats", ""]

ROLE_FULL = "full"
ROLE_STATS = "stats"


class AdminAccess:
    """Env BOT_ADMIN_IDS are always full; extra admins live in bot_settings.json."""

    def __init__(self, settings: Settings, bot_settings: BotSettingsStore) -> None:
        self.settings = settings
        self.bot_settings = bot_settings

    async def role(self, user_id: int) -> Role:
        uid = int(user_id or 0)
        if not uid:
            return ""
        if uid in self.settings.bot_admin_ids:
            return ROLE_FULL
        stored = await self.bot_settings.get_admin_role(uid)
        if stored in (ROLE_FULL, ROLE_STATS):
            return stored  # type: ignore[return-value]
        return ""

    async def is_admin(self, user_id: int) -> bool:
        return bool(await self.role(user_id))

    async def can_stats(self, user_id: int) -> bool:
        return (await self.role(user_id)) in (ROLE_FULL, ROLE_STATS)

    async def can_settings(self, user_id: int) -> bool:
        return (await self.role(user_id)) == ROLE_FULL

    async def can_news_report(self, user_id: int) -> bool:
        """News post report in Stats: owner (BOT_ADMIN) + optional میدان IDs only."""
        uid = int(user_id or 0)
        if not uid:
            return False
        if uid in self.settings.bot_admin_ids:
            return True
        return uid in getattr(self.settings, "news_report_admin_ids", frozenset())
