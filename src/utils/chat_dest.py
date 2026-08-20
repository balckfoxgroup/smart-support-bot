"""Validate Telegram destinations for channel / group / private account."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class DestCheck:
    ok: bool
    chat_id: str
    chat_type: str = ""
    title: str = ""
    detail_fa: str = ""
    detail_en: str = ""
    need_admin: bool = False


def _normalize(raw: str) -> str:
    return (raw or "").strip()


async def validate_destination(
    bot: Any,
    raw: str,
    *,
    expect: str,
) -> DestCheck:
    """
    expect: 'channel' | 'group' | 'account'
    """
    value = _normalize(raw)
    if not value:
        return DestCheck(
            ok=False,
            chat_id="",
            detail_fa="مقدار خالی است.",
            detail_en="Empty value.",
        )

    # Heuristic pre-check without API
    low = value.lower()
    if expect == "channel":
        if value.lstrip("-").isdigit() and not value.startswith("-100"):
            # numeric private-looking id
            pass
    if expect == "account":
        if low.startswith("@") and ("channel" in low or "group" in low):
            return DestCheck(
                ok=False,
                chat_id=value,
                detail_fa="این بخش فقط اکانت کاربر شخصی است، نه کانال/گروه.",
                detail_en="This section accepts only a personal user account.",
            )

    try:
        chat = await bot.get_chat(value)
    except Exception as exc:  # noqa: BLE001
        return DestCheck(
            ok=False,
            chat_id=value,
            detail_fa=f"ربات به این مقصد دسترسی ندارد: {exc}",
            detail_en=f"Bot cannot access this destination: {exc}",
            need_admin=expect in {"channel", "group"},
        )

    ctype = str(getattr(chat, "type", "") or "")
    title = str(getattr(chat, "title", "") or getattr(chat, "full_name", "") or getattr(chat, "username", "") or "")
    username = getattr(chat, "username", None)
    resolved = f"@{username}" if username else str(getattr(chat, "id", value))

    if expect == "channel":
        if ctype != "channel":
            return DestCheck(
                ok=False,
                chat_id=resolved,
                chat_type=ctype,
                title=title,
                detail_fa=f"این مقصد «{ctype or 'نامشخص'}» است؛ فقط کانال مجاز است.",
                detail_en=f"Got «{ctype or 'unknown'}»; only a channel is allowed.",
            )
    elif expect == "group":
        if ctype not in {"group", "supergroup"}:
            return DestCheck(
                ok=False,
                chat_id=resolved,
                chat_type=ctype,
                title=title,
                detail_fa=f"این مقصد «{ctype or 'نامشخص'}» است؛ فقط گروه مجاز است.",
                detail_en=f"Got «{ctype or 'unknown'}»; only a group is allowed.",
            )
    elif expect == "account":
        if ctype != "private":
            return DestCheck(
                ok=False,
                chat_id=resolved,
                chat_type=ctype,
                title=title,
                detail_fa=f"این مقصد «{ctype or 'نامشخص'}» است؛ فقط اکانت کاربر مجاز است.",
                detail_en=f"Got «{ctype or 'unknown'}»; only a private user is allowed.",
            )

    # Admin check for channel/group
    if expect in {"channel", "group"}:
        try:
            me = await bot.get_me()
            member = await bot.get_chat_member(chat.id, me.id)
            status = str(getattr(member, "status", "") or "")
            if status not in {"administrator", "creator"}:
                return DestCheck(
                    ok=False,
                    chat_id=resolved,
                    chat_type=ctype,
                    title=title,
                    detail_fa="ربات در این کانال/گروه ادمین نیست.",
                    detail_en="Bot is not an admin in this channel/group.",
                    need_admin=True,
                )
        except Exception as exc:  # noqa: BLE001
            return DestCheck(
                ok=False,
                chat_id=resolved,
                chat_type=ctype,
                title=title,
                detail_fa=f"نتوانست وضعیت ادمین را چک کند: {exc}",
                detail_en=f"Could not verify admin status: {exc}",
                need_admin=True,
            )

    return DestCheck(ok=True, chat_id=resolved, chat_type=ctype, title=title)
