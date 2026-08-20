"""Custom admin buttons: catalog of runnable actions + dispatcher."""

from __future__ import annotations

import logging
import secrets
from dataclasses import dataclass, field
from typing import Any, Callable, Awaitable

from aiogram.types import Message

from src.branding import load_creator_contact
from src.config import Settings
from src.health_report import build_health_report
from src.storage.bot_settings import TARGET_KEYS, BotSettingsStore

logger = logging.getLogger(__name__)

ALLOWED_MENUS = frozenset({"settings"})
ALLOWED_ACTIONS = frozenset(
    {
        "open_owner",
        "open_messages",
        "open_panel",
        "open_health",
        "open_backup",
        "open_admins",
        "open_creator",
        "open_slot",
        "toggle_slot",
        "send_static_now",
        "run_health_now",
        "show_text",
        "show_owner_card",
        "noop_confirm",
    }
)


@dataclass
class CustomButton:
    id: str
    menu: str = "settings"
    label_fa: str = ""
    label_en: str = ""
    enabled: bool = True
    action: str = "noop_confirm"
    params: dict[str, Any] = field(default_factory=dict)
    order: int = 100

    def labels(self) -> set[str]:
        out = {self.label_fa.strip(), self.label_en.strip()}
        return {x for x in out if x}

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "menu": self.menu,
            "label_fa": self.label_fa,
            "label_en": self.label_en,
            "enabled": self.enabled,
            "action": self.action,
            "params": dict(self.params or {}),
            "order": int(self.order),
        }

    @classmethod
    def from_dict(cls, raw: dict[str, Any] | None) -> CustomButton | None:
        if not isinstance(raw, dict):
            return None
        action = str(raw.get("action") or "").strip()
        if action not in ALLOWED_ACTIONS:
            return None
        menu = str(raw.get("menu") or "settings").strip() or "settings"
        if menu not in ALLOWED_MENUS:
            return None
        label_fa = str(raw.get("label_fa") or "").strip()
        label_en = str(raw.get("label_en") or label_fa).strip()
        if not label_fa and not label_en:
            return None
        bid = str(raw.get("id") or "").strip() or new_button_id()
        params = raw.get("params") if isinstance(raw.get("params"), dict) else {}
        try:
            order = int(raw.get("order") or 100)
        except (TypeError, ValueError):
            order = 100
        return cls(
            id=bid,
            menu=menu,
            label_fa=label_fa or label_en,
            label_en=label_en or label_fa,
            enabled=bool(raw.get("enabled", True)),
            action=action,
            params=dict(params),
            order=order,
        )


def new_button_id() -> str:
    return "cb_" + secrets.token_hex(3)


def action_catalog_help(*, lang: str = "fa") -> str:
    fa = (lang or "").startswith("fa")
    if fa:
        return (
            "عمل‌های مجاز برای کلید سفارشی:\n"
            "• open_owner / open_messages / open_panel / open_health / open_backup / open_admins / open_creator\n"
            "• open_slot (target=channel|group|support|test slot=1..3)\n"
            "• toggle_slot (target=… slot=…)\n"
            "• send_static_now (target=… slot=…) — ارسال متن اسلات\n"
            "• run_health_now — گزارش سلامت الان\n"
            "• show_text (text=…)\n"
            "• show_owner_card\n"
            "• noop_confirm — فقط تأیید"
        )
    return (
        "Allowed custom-button actions:\n"
        "• open_owner / open_messages / open_panel / open_health / open_backup / open_admins / open_creator\n"
        "• open_slot (target=channel|group|support|test slot=1..3)\n"
        "• toggle_slot (target=… slot=…)\n"
        "• send_static_now (target=… slot=…)\n"
        "• run_health_now\n"
        "• show_text (text=…)\n"
        "• show_owner_card\n"
        "• noop_confirm"
    )


DispatchFn = Callable[..., Awaitable[None]]


async def dispatch_custom_button(
    message: Message,
    button: CustomButton,
    *,
    lang: str,
    settings: Settings,
    bot_settings: BotSettingsStore,
    show_owner,
    show_messages_hub,
    show_panel,
    show_slot,
    show_settings_hub,
) -> None:
    """Run a catalog action for a custom button. Always performs a real effect."""
    from src.ui import admin_keyboards as ak

    action = button.action
    params = button.params or {}
    fa = (lang or "").startswith("fa")

    if action == "noop_confirm":
        await message.answer(
            ("✅ کلید سفارشی اجرا شد." if fa else "✅ Custom button ran."),
            reply_markup=await _kb_settings(lang, bot_settings),
        )
        return

    if action == "open_owner":
        await bot_settings.set_session(_uid(message), {"mode": "owner"})
        await show_owner(message, bot_settings, lang)
        return

    if action == "open_messages":
        await bot_settings.set_session(_uid(message), {"mode": "messages_hub"})
        await show_messages_hub(message, lang)
        return

    if action == "open_panel":
        await bot_settings.set_session(_uid(message), {"mode": "panel"})
        await show_panel(message, bot_settings, lang)
        return

    if action == "open_health":
        report = await build_health_report(settings, bot_settings, lang=lang)
        await bot_settings.set_session(_uid(message), {"mode": "health"})
        await message.answer(report[:3900], reply_markup=ak.health_keyboard(lang))
        return

    if action == "open_backup":
        await bot_settings.set_session(_uid(message), {"mode": "backup"})
        await message.answer(
            "💾 " + ("پشتیبان تنظیمات" if fa else "Settings backup"),
            reply_markup=ak.backup_keyboard(lang),
        )
        return

    if action == "open_admins":
        env_ids = sorted(settings.bot_admin_ids)
        env_txt = "\n".join(f"• {i} (full/env)" for i in env_ids) or "—"
        extra = await bot_settings.list_extra_admins()
        extra_txt = (
            "\n".join(f"• {uid} ({role})" for uid, role in extra) if extra else "—"
        )
        body = ak.msg("admins_card", lang).format(
            env_admins=env_txt, extra_admins=extra_txt
        )
        await bot_settings.set_session(_uid(message), {"mode": "admins"})
        await message.answer(body, reply_markup=ak.admins_keyboard(lang))
        return

    if action == "open_creator":
        creator = load_creator_contact(settings.knowledge_root)
        await message.answer(
            creator.format_card(lang),
            reply_markup=await _kb_settings(lang, bot_settings),
        )
        return

    if action == "show_owner_card":
        owner = await bot_settings.get_owner()
        await message.answer(
            bot_settings.format_owner_card(owner, lang=lang),
            reply_markup=await _kb_settings(lang, bot_settings),
        )
        return

    if action == "show_text":
        text = str(params.get("text") or "").strip() or (
            "متن خالی است." if fa else "Empty text."
        )
        await message.answer(text[:3900], reply_markup=await _kb_settings(lang, bot_settings))
        return

    if action == "run_health_now":
        report = await build_health_report(settings, bot_settings, lang=lang)
        await message.answer(report[:3900], reply_markup=await _kb_settings(lang, bot_settings))
        return

    if action in {"open_slot", "toggle_slot", "send_static_now"}:
        target = str(params.get("target") or "channel").strip()
        if target not in TARGET_KEYS:
            await message.answer(
                "مقصد نامعتبر." if fa else "Invalid target.",
                reply_markup=await _kb_settings(lang, bot_settings),
            )
            return
        try:
            slot_no = int(params.get("slot") or 1)
        except (TypeError, ValueError):
            slot_no = 1
        if not (1 <= slot_no <= 3):
            slot_no = 1
        idx = slot_no - 1

        if action == "open_slot":
            await bot_settings.set_session(
                _uid(message),
                {"mode": "slot", "target_key": target, "slot_index": idx},
            )
            await show_slot(message, bot_settings, target, idx, lang)
            return

        if action == "toggle_slot":
            t = await bot_settings.get_target(target)
            slot = t.slot(idx)
            new_enabled = not bool(slot.enabled)
            await bot_settings.update_slot(target, idx, enabled=new_enabled)
            state = ("فعال" if new_enabled else "غیرفعال") if fa else ("on" if new_enabled else "off")
            await message.answer(
                (f"اسلات {slot_no} ({target}): {state}" if fa else f"Slot {slot_no} ({target}): {state}"),
                reply_markup=await _kb_settings(lang, bot_settings),
            )
            return

        # send_static_now
        t = await bot_settings.get_target(target)
        slot = t.slot(idx)
        chat_id = (slot.chat_id or t.chat_id or "").strip()
        body = (slot.message_template or "").strip()
        if not chat_id:
            await message.answer(
                "مقصد اسلات خالی است." if fa else "Slot destination is empty.",
                reply_markup=await _kb_settings(lang, bot_settings),
            )
            return
        if not body:
            await message.answer(
                "متن اسلات خالی است." if fa else "Slot message text is empty.",
                reply_markup=await _kb_settings(lang, bot_settings),
            )
            return
        if message.bot is None:
            return
        await message.bot.send_message(chat_id=chat_id, text=body[:3900])
        await message.answer(
            ("✅ پیام ارسال شد." if fa else "✅ Message sent."),
            reply_markup=await _kb_settings(lang, bot_settings),
        )
        return

    await message.answer(
        ("عمل ناشناخته." if fa else "Unknown action."),
        reply_markup=await _kb_settings(lang, bot_settings),
    )


def _uid(message: Message) -> int:
    return message.from_user.id if message.from_user else 0


async def _kb_settings(lang: str, bot_settings: BotSettingsStore):
    from src.ui import admin_keyboards as ak

    customs = await bot_settings.list_custom_buttons(menu="settings")
    generated: list = []
    try:
        from src.generated.buttons import list_generated_buttons

        generated = list_generated_buttons(menu="settings", refresh=True)
    except Exception:  # noqa: BLE001
        generated = []
    ak.refresh_custom_button_labels(list(customs) + list(generated))
    return ak.settings_hub_keyboard(
        lang, custom_buttons=customs, generated_buttons=generated
    )
