"""Daily health status push to admin chat."""

from __future__ import annotations

import asyncio
import logging
from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram import Bot

from src.config import Settings
from src.health_report import build_health_report
from src.job_status import record_job
from src.storage.bot_settings import BotSettingsStore

logger = logging.getLogger(__name__)
IRAN_TZ = ZoneInfo("Asia/Tehran")


def _parse_times(raw: str) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for part in (raw or "").split(","):
        part = part.strip()
        if not part or ":" not in part:
            continue
        try:
            hh, mm = part.split(":", 1)
            out.append((int(hh), int(mm)))
        except ValueError:
            continue
    return out or [(9, 0)]


async def run_health_report_job(
    settings: Settings,
    bot: Bot,
    bot_settings: BotSettingsStore,
) -> None:
    """Send a short health card once per scheduled Iran-time slot."""
    sent_keys: set[str] = set()
    while True:
        try:
            cfg = await bot_settings.get_health_settings()
            if not cfg.get("enabled", True):
                await asyncio.sleep(30)
                continue
            times = _parse_times(str(cfg.get("times") or "09:00"))
            now = datetime.now(IRAN_TZ)
            key = f"{now.date().isoformat()}-{now.hour:02d}:{now.minute:02d}"
            matched = any(now.hour == h and now.minute == m for h, m in times)
            if matched and key not in sent_keys:
                chat = str(cfg.get("chat_id") or "").strip()
                if not chat:
                    # Prefer first env full admin
                    admins = sorted(settings.bot_admin_ids)
                    chat = str(admins[0]) if admins else ""
                if chat:
                    text = await build_health_report(settings, bot_settings, lang="fa")
                    await bot.send_message(chat_id=chat, text=text[:3900])
                    record_job(settings.data_dir, "health_report", ok=True, detail=f"sent to {chat}")
                    sent_keys.add(key)
                    # prune old keys
                    if len(sent_keys) > 40:
                        sent_keys = set(list(sent_keys)[-20:])
                else:
                    record_job(
                        settings.data_dir,
                        "health_report",
                        ok=False,
                        detail="no chat_id / admin",
                    )
                    sent_keys.add(key)
        except Exception:  # noqa: BLE001
            logger.exception("health report job failed")
            record_job(settings.data_dir, "health_report", ok=False, detail="exception")
        await asyncio.sleep(20)
