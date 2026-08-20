"""Admin handlers for safe-change confirm/reject and drills."""

from __future__ import annotations

import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from src.config import Settings, is_bot_admin
from src.safety.api import (
    confirm_change,
    reject_change,
    request_safe_change,
    resolve_support_chat_id,
    safety_status,
)
from src.safety.paths import CONFIRM_SECONDS_DEFAULT, OBSERVE_SECONDS_DEFAULT
from src.storage.users import UserStore

logger = logging.getLogger(__name__)

router = Router(name="safety")


def setup_safety_router(users: UserStore, *, settings: Settings) -> Router:
    def _uid(message: Message | CallbackQuery) -> int:
        u = message.from_user
        return u.id if u else 0

    @router.callback_query(F.data.startswith("sf_ok:") | F.data.startswith("sf_no:"))
    async def on_safety_callback(query: CallbackQuery) -> None:
        uid = _uid(query)
        if not uid or not is_bot_admin(settings, uid):
            await query.answer("Admin only", show_alert=True)
            return
        data = query.data or ""
        try:
            action, change_id = data.split(":", 1)
        except ValueError:
            await query.answer("Bad callback", show_alert=True)
            return
        if action == "sf_ok":
            result = confirm_change(change_id, by_user_id=uid)
            if result.get("ok"):
                await query.answer("تأیید ثبت شد")
                if query.message:
                    await query.message.edit_text(
                        f"✅ تأیید شما ثبت شد. Watchdog تغییرات را نگه می‌دارد.\nchange: {change_id}"
                    )
            else:
                await query.answer(str(result.get("error") or "failed"), show_alert=True)
            return
        if action == "sf_no":
            result = reject_change(change_id, by_user_id=uid)
            if result.get("ok"):
                await query.answer("رد ثبت شد — در حال برگشت")
                if query.message:
                    await query.message.edit_text(
                        f"⏪ رد شد. Watchdog در حال Restore است.\nchange: {change_id}"
                    )
            else:
                await query.answer(str(result.get("error") or "failed"), show_alert=True)

    @router.message(Command("safety_status"))
    async def cmd_safety_status(message: Message) -> None:
        uid = _uid(message)
        if not uid or not is_bot_admin(settings, uid):
            await message.answer("Admin only.")
            return
        st = safety_status()
        pending = st.get("pending")
        req = st.get("request")
        hb = st.get("heartbeat")
        lines = ["🛡 Safety Status"]
        if pending:
            lines.append(
                f"pending: {pending.get('change_id')} / {pending.get('status')}\n"
                f"desc: {pending.get('description')}\n"
                f"observe_s={pending.get('observe_seconds')} confirm_s={pending.get('confirm_seconds')}"
            )
        else:
            lines.append("pending: (none)")
        if req:
            lines.append(f"request: {req.get('change_id')} / {req.get('status')}")
        else:
            lines.append("request: (none)")
        lines.append(f"support_chat: {st.get('support_chat_id')}")
        if hb:
            lines.append(f"heartbeat: ts={hb.get('ts')} status={hb.get('status')}")
        else:
            lines.append("heartbeat: (none)")
        await message.answer("\n".join(lines), disable_notification=True)

    @router.message(Command("safety_drill"))
    async def cmd_safety_drill(message: Message) -> None:
        """Queue a harmless marker change to exercise backup/confirm/rollback."""
        uid = _uid(message)
        if not uid or not is_bot_admin(settings, uid):
            await message.answer("Admin only.")
            return
        support_chat = resolve_support_chat_id()
        result = request_safe_change(
            description="Safety drill (marker only) — تأیید پشتیبانی یا rollback خودکار",
            admin_chat_id=support_chat,
            marker_only=True,
            observe_seconds=OBSERVE_SECONDS_DEFAULT,
            confirm_seconds=CONFIRM_SECONDS_DEFAULT,
        )
        if not result.get("ok"):
            await message.answer(f"❌ {result.get('error')}", disable_notification=True)
            return
        await message.answer(
            "🛡 Safety drill صف شد.\n"
            f"change: {result.get('change_id')}\n"
            f"پشتیبانی: {support_chat}\n"
            f"بعد از اعمال: {OBSERVE_SECONDS_DEFAULT}ث چک → سپس پیام تأیید "
            f"(مهلت {CONFIRM_SECONDS_DEFAULT}ث).",
            disable_notification=True,
        )

    return router
