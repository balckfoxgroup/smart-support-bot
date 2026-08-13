"""Admin Settings: owner info, destinations, catalog wizard."""

from __future__ import annotations

import logging
import shutil
from pathlib import Path
from typing import Any

from aiogram import F, Router
from aiogram.dispatcher.event.bases import SkipHandler
from aiogram.filters import Filter
from aiogram.types import Message

from src.access import AdminAccess
from src.ai.client import AIClient, AIClientError
from src.ai.persona import apply_owner_info, looks_like_reasoning_leak, strip_reasoning_leak
from src.branding import load_creator_contact
from src.config import Settings
from src.control.audit import AuditLog
from src.control.service import ControlService
from src.custom_buttons import (
    ALLOWED_ACTIONS,
    CustomButton,
    action_catalog_help,
    dispatch_custom_button,
    new_button_id,
)
from src.health_report import build_health_report
from src.knowledge.catalog_builder import build_one_catalog, prepare_work_folder
from src.knowledge.product_catalogs import load_product_catalogs
from src.storage.bot_settings import SLOT_KINDS, TARGET_KEYS, BotSettingsStore
from src.storage.users import UserStore
from src.ui import admin_keyboards as ak
from src.ui import keyboards, texts
from src.utils.chat_dest import validate_destination

logger = logging.getLogger(__name__)

router = Router(name="admin_settings")


class _SettingsButtonFilter(Filter):
    """Match built-in settings labels or runtime custom button labels."""

    def __init__(self, static: set[str] | frozenset[str]) -> None:
        self._static = frozenset(static)

    async def __call__(self, message: Message) -> bool:
        text = (message.text or "").strip()
        if not text:
            return False
        return text in self._static or text in ak.custom_button_labels()


async def _settings_kb(lang: str, store: BotSettingsStore):
    customs = await store.list_custom_buttons(menu="settings")
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

_TARGET_BY_ACTION = {
    "msg_channel": "channel",
    "msg_group": "group",
    "msg_support": "support",
    "msg_account": "support",
    "msg_test": "test",
}

_SLOT_BY_ACTION = {"slot_1": 0, "slot_2": 1, "slot_3": 2}

_OWNER_FIELD_BY_ACTION = {
    "owner_bot_name": "bot_display_name",
    "owner_site": "site_url",
    "owner_channel": "channel",
    "owner_group": "group",
    "owner_support": "support_handle",
}

_ASK_OWNER = {
    "bot_display_name": "ask_owner_bot_name",
    "site_url": "ask_owner_site",
    "channel": "ask_owner_channel",
    "group": "ask_owner_group",
    "support_handle": "ask_owner_support",
}

_EDIT_FIELD_BY_ACTION = {
    "edit_dest": "chat_id",
    "edit_template": "message_template",
    "edit_schedule": "schedule_times",
    "edit_rules": "rules_prompt",
    "edit_slot_kind": "kind",
    "edit_panel_url": "base_url",
    "edit_panel_token": "api_token",
    "edit_panel_port": "required_port",
    "edit_panel_inbound": "inbound_id",
}

_ASK_MSG = {
    "chat_id": "ask_dest",
    "message_template": "ask_template",
    "schedule_times": "ask_schedule",
    "rules_prompt": "ask_rules",
    "kind": "ask_slot_kind",
    "base_url": "ask_panel_url",
    "api_token": "ask_panel_token",
    "required_port": "ask_panel_port",
    "inbound_id": "ask_panel_inbound",
}


def _uid(message: Message) -> int:
    return message.from_user.id if message.from_user else 0


def _fmt_current(lang: str, value: Any, *, secret: bool = False) -> str:
    fa = (lang or "").startswith("fa")
    empty = "—" if fa else "-"
    if secret:
        raw = str(value or "").strip()
        if not raw:
            shown = empty
        elif len(raw) <= 8:
            shown = "••••"
        else:
            shown = raw[:4] + "…" + raw[-2:]
    else:
        shown = str(value).strip() if value is not None and str(value).strip() else empty
        if len(shown) > 600:
            shown = shown[:600] + "…"
    label = "مقدار فعلی" if fa else "Current value"
    return f"{label}: {shown}"


def _ask_with_current(lang: str, ask_key: str, value: Any, *, secret: bool = False) -> str:
    return f"{_fmt_current(lang, value, secret=secret)}\n\n{ak.msg(ask_key, lang)}"


def _ask_dest_key(target_key: str) -> str:
    return {
        "channel": "ask_dest_channel",
        "group": "ask_dest_group",
        "support": "ask_dest_account",
    }.get(target_key, "ask_dest")


def _expect_for_target(target_key: str) -> str | None:
    return {
        "channel": "channel",
        "group": "group",
        "support": "account",
    }.get(target_key)


def _staging_dir(settings: Settings, admin_id: int) -> Path:
    path = settings.data_dir / "catalog_staging" / str(admin_id)
    path.mkdir(parents=True, exist_ok=True)
    return path


async def _lang(users: UserStore, message: Message) -> str:
    uid = _uid(message)
    code = await users.get_lang(
        uid, message.from_user.language_code if message.from_user else None
    )
    return ak.ui_lang(code)


async def _show_settings_hub(
    message: Message, lang: str, bot_settings: BotSettingsStore | None = None
) -> None:
    customs: list = []
    generated: list = []
    if bot_settings is not None:
        customs = await bot_settings.list_custom_buttons(menu="settings")
        try:
            from src.generated.buttons import list_generated_buttons

            generated = list_generated_buttons(menu="settings", refresh=True)
        except Exception:  # noqa: BLE001
            generated = []
        ak.refresh_custom_button_labels(list(customs) + list(generated))
    await message.answer(
        ak.msg("settings_hub", lang),
        reply_markup=ak.settings_hub_keyboard(
            lang, custom_buttons=customs, generated_buttons=generated
        ),
    )


async def _show_messages_hub(message: Message, lang: str) -> None:
    await message.answer(ak.msg("messages_hub", lang), reply_markup=ak.messages_hub_keyboard(lang))


async def _show_owner(message: Message, store: BotSettingsStore, lang: str) -> None:
    owner = await store.get_owner()
    await message.answer(
        store.format_owner_card(owner, lang=lang),
        reply_markup=ak.owner_info_keyboard(lang),
    )


async def _show_target(
    message: Message, store: BotSettingsStore, key: str, lang: str
) -> None:
    target = await store.get_target(key)
    note = ""
    if key == "support" and (lang or "").startswith("fa"):
        note = (
            "\n\nاین بخش فقط برای پیام به اکانت کاربر معمولی است "
            "(نه کانال/گروه). خبر و کانفیگ را در بخش کانال تنظیم کنید."
        )
    elif key == "support":
        note = (
            "\n\nThis section is for normal user-account messages only "
            "(not channel/group). Configure news/config under Channel."
        )
    elif key == "channel" and (lang or "").startswith("fa"):
        note = (
            "\n\nخبر و کانفیگ رایگان اینجا تنظیم می‌شود. "
            "ربات باید در کانال مدیر باشد."
        )
    elif key == "channel":
        note = "\n\nNews and free-config slots live here. Bot must be channel admin."
    elif key == "group" and (lang or "").startswith("fa"):
        note = "\n\nربات باید در گروه مدیر باشد."
    elif key == "group":
        note = "\n\nBot must be an admin in the group."
    await message.answer(
        (store.format_target_card(target, lang=lang) + note)[:3900],
        reply_markup=ak.target_edit_keyboard(lang),
    )


async def _show_slot(
    message: Message, store: BotSettingsStore, key: str, slot_index: int, lang: str
) -> None:
    target = await store.get_target(key)
    kb = ak.slot_edit_keyboard(lang)
    # Account section: message-to-user only (no kind switch needed)
    if key == "support":
        from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

        kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=ak.label("edit_dest", lang))],
                [KeyboardButton(text=ak.label("edit_template", lang))],
                [KeyboardButton(text=ak.label("edit_schedule", lang))],
                [KeyboardButton(text=ak.label("edit_rules", lang))],
                [KeyboardButton(text=ak.label("nav_back", lang))],
                [KeyboardButton(text=ak.label("settings_back", lang))],
            ],
            resize_keyboard=True,
            is_persistent=True,
        )
    await message.answer(
        store.format_slot_card(target, slot_index, lang=lang)[:3900],
        reply_markup=kb,
    )


async def _show_panel(message: Message, store: BotSettingsStore, lang: str) -> None:
    panel = await store.get_panel()
    await message.answer(
        store.format_panel_card(panel, lang=lang),
        reply_markup=ak.panel_edit_keyboard(lang),
    )


async def _show_catalog_wizard(
    message: Message, store: BotSettingsStore, uid: int, lang: str
) -> None:
    sess = await store.get_session(uid)
    sources = sess.get("catalog_sources") or {"site": False, "channel": False, "group": False}
    path = sess.get("catalog_path") or ""
    staging = Path(str(sess.get("catalog_staging") or ""))
    files = 0
    if staging.is_dir():
        files = sum(1 for p in staging.rglob("*") if p.is_file())
    body = ak.msg("catalog_wizard_intro", lang)
    body += "\n\n" + ak.msg("catalog_src_toggled", lang).format(
        site=("بله" if sources.get("site") else "خیر")
        if (lang or "").startswith("fa")
        else ("yes" if sources.get("site") else "no"),
        channel=("بله" if sources.get("channel") else "خیر")
        if (lang or "").startswith("fa")
        else ("yes" if sources.get("channel") else "no"),
        group=("بله" if sources.get("group") else "خیر")
        if (lang or "").startswith("fa")
        else ("yes" if sources.get("group") else "no"),
    )
    body += "\n" + _fmt_current(lang, path or ("—" if not files else f"{files} uploaded file(s)"))
    await message.answer(
        body,
        reply_markup=ak.catalog_wizard_keyboard(lang, sources=sources),
    )


def setup_admin_settings_router(
    users: UserStore,
    *,
    settings: Settings,
    bot_settings: BotSettingsStore,
    audit: AuditLog,
    control: ControlService | None = None,
    ai: AIClient | None = None,
    access: AdminAccess | None = None,
) -> Router:
    access = access or AdminAccess(settings, bot_settings)

    async def _require_settings(message: Message) -> tuple[bool, str]:
        uid = _uid(message)
        lang = await _lang(users, message)
        if not uid or not await access.can_settings(uid):
            if uid and await access.can_stats(uid):
                await message.answer(ak.msg("settings_denied", lang))
            else:
                await message.answer(ak.msg("admin_only", lang))
            return False, lang
        return True, lang

    async def _admins_card(lang: str) -> str:
        env_ids = sorted(settings.bot_admin_ids)
        env_txt = "\n".join(f"• {i} (full/env)" for i in env_ids) or "—"
        extra = await bot_settings.list_extra_admins()
        extra_txt = (
            "\n".join(f"• {uid} ({role})" for uid, role in extra) if extra else "—"
        )
        return ak.msg("admins_card", lang).format(
            env_admins=env_txt,
            extra_admins=extra_txt,
        )

    async def _clear_control(uid: int) -> None:
        if control is not None:
            await control.registry.clear_session(uid)

    async def _save_dest(
        message: Message,
        *,
        uid: int,
        lang: str,
        target_key: str,
        slot_index: int | None,
        value: str,
    ) -> bool:
        expect = _expect_for_target(target_key)
        if expect and message.bot is not None:
            check = await validate_destination(message.bot, value, expect=expect)
            if not check.ok:
                detail = check.detail_fa if (lang or "").startswith("fa") else check.detail_en
                await message.answer(
                    ak.msg("dest_type_mismatch", lang).format(detail=detail),
                    reply_markup=ak.cancel_keyboard(lang),
                )
                if check.need_admin:
                    await message.answer(ak.msg("dest_need_admin", lang))
                return False
            value = check.chat_id or value
        if slot_index is None:
            await bot_settings.update_target(target_key, chat_id=value)
        else:
            await bot_settings.update_slot(target_key, slot_index, chat_id=value)
        return True

    @router.message(F.text.in_(set(texts.MENU_SETTINGS.values()) | ak.texts("settings_hub")))
    async def on_settings_entry(message: Message) -> None:
        ok, lang = await _require_settings(message)
        if not ok:
            return
        uid = _uid(message)
        await users.set_ask_ai(uid, False)
        await bot_settings.clear_session(uid)
        await _clear_control(uid)
        await _show_settings_hub(message, lang, bot_settings)

    button_texts = (
        ak.texts("settings_messages")
        | ak.texts("settings_panel")
        | ak.texts("settings_back")
        | ak.texts("nav_back")
        | ak.texts("owner_info")
        | ak.texts("creator_contact")
        | ak.texts("bot_config_chat")
        | ak.texts("build_catalogs")
        | ak.texts("catalog_src_site")
        | ak.texts("catalog_src_channel")
        | ak.texts("catalog_src_group")
        | ak.texts("catalog_run")
        | ak.texts("owner_bot_name")
        | ak.texts("owner_site")
        | ak.texts("owner_channel")
        | ak.texts("owner_group")
        | ak.texts("owner_support")
        | ak.texts("msg_channel")
        | ak.texts("msg_group")
        | ak.texts("msg_support")
        | ak.texts("msg_account")
        | ak.texts("msg_test")
        | ak.texts("slot_1")
        | ak.texts("slot_2")
        | ak.texts("slot_3")
        | ak.texts("edit_dest")
        | ak.texts("edit_dest_legacy")
        | ak.texts("edit_template")
        | ak.texts("edit_template_legacy")
        | ak.texts("edit_schedule")
        | ak.texts("edit_schedule_legacy")
        | ak.texts("edit_rules")
        | ak.texts("edit_rules_legacy")
        | ak.texts("edit_slot_kind")
        | ak.texts("toggle_slot_enabled")
        | ak.texts("edit_panel_url")
        | ak.texts("edit_panel_url_legacy")
        | ak.texts("edit_panel_token")
        | ak.texts("edit_panel_token_legacy")
        | ak.texts("edit_panel_port")
        | ak.texts("edit_panel_port_legacy")
        | ak.texts("edit_panel_inbound")
        | ak.texts("edit_panel_inbound_legacy")
        | ak.texts("backup_settings")
        | ak.texts("backup_export")
        | ak.texts("backup_import")
        | ak.texts("health_status")
        | ak.texts("health_toggle")
        | ak.texts("health_times")
        | ak.texts("health_chat")
        | ak.texts("manage_admins")
        | ak.texts("admin_role_full")
        | ak.texts("admin_role_stats")
        | ak.texts("admin_remove")
        | ak.texts("cancel")
    )
    # include toggle-prefixed labels
    for src in ("catalog_src_site", "catalog_src_channel", "catalog_src_group"):
        for v in ak.texts(src):
            button_texts |= {f"✅ {v}", f"⬜ {v}"}

    @router.message(_SettingsButtonFilter(button_texts))
    async def on_settings_button(message: Message) -> None:
        uid = _uid(message)
        lang = await _lang(users, message)
        action = ak.resolve_action(message.text)

        # Custom / generated buttons (must run before empty-action return).
        if not action:
            try:
                from src.generated.buttons import dispatch_generated, find_generated_by_label

                gen = find_generated_by_label(message.text or "")
            except Exception:  # noqa: BLE001
                gen = None
            if gen:
                ok, lang = await _require_settings(message)
                if not ok:
                    return
                ran = await dispatch_generated(
                    message,
                    gen,
                    lang=lang,
                    settings=settings,
                    bot_settings=bot_settings,
                )
                if not ran:
                    await message.answer(
                        "اجرای کلید تولیدشده ناموفق بود."
                        if lang.startswith("fa")
                        else "Generated button failed to run."
                    )
                return
            raw_btn = await bot_settings.find_custom_button_by_label(message.text or "")
            if raw_btn:
                ok, lang = await _require_settings(message)
                if not ok:
                    return
                btn = CustomButton.from_dict(raw_btn)
                if btn is None:
                    return
                await dispatch_custom_button(
                    message,
                    btn,
                    lang=lang,
                    settings=settings,
                    bot_settings=bot_settings,
                    show_owner=_show_owner,
                    show_messages_hub=_show_messages_hub,
                    show_panel=_show_panel,
                    show_slot=_show_slot,
                    show_settings_hub=_show_settings_hub,
                )
                return
            return

        # Health report is allowed for stats-only admins too.
        if action == "health_status":
            if not await access.can_stats(uid):
                await message.answer(ak.msg("admin_only", lang))
                return
            report = await build_health_report(settings, bot_settings, lang=lang)
            if await access.can_settings(uid):
                await bot_settings.set_session(uid, {"mode": "health"})
                await message.answer(report[:3900], reply_markup=ak.health_keyboard(lang))
            else:
                await message.answer(report[:3900], reply_markup=ak.stats_hub_keyboard(lang))
            return

        ok, lang = await _require_settings(message)
        if not ok:
            return
        uid = _uid(message)
        await users.set_ask_ai(uid, False)

        if action == "settings_back":
            await bot_settings.clear_session(uid)
            await _clear_control(uid)
            await _show_settings_hub(message, lang, bot_settings)
            return

        if action == "backup_settings":
            await bot_settings.set_session(uid, {"mode": "backup"})
            await message.answer(
                "💾 " + ("پشتیبان تنظیمات" if lang == "fa" else "Settings backup"),
                reply_markup=ak.backup_keyboard(lang),
            )
            return

        if action == "backup_export":
            import json
            from datetime import datetime

            from aiogram.types import BufferedInputFile

            payload = await bot_settings.export_backup()
            raw = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
            name = f"smart-support-bot-settings-{datetime.utcnow().strftime('%Y%m%d-%H%M')}.json"
            await message.answer_document(
                BufferedInputFile(raw, filename=name),
                caption=ak.msg("backup_exported", lang),
                reply_markup=ak.backup_keyboard(lang),
            )
            await audit.write("export_settings_backup", admin_id=uid, detail=name)
            return

        if action == "backup_import":
            await bot_settings.set_session(uid, {"mode": "import_backup"})
            await message.answer(
                ak.msg("ask_backup_import", lang),
                reply_markup=ak.cancel_keyboard(lang),
            )
            return

        if action == "health_toggle":
            cfg = await bot_settings.get_health_settings()
            cfg = await bot_settings.update_health_settings(enabled=not cfg.get("enabled", True))
            state = ("روشن" if cfg.get("enabled") else "خاموش") if lang == "fa" else ("on" if cfg.get("enabled") else "off")
            await message.answer(
                f"{'گزارش روزانه' if lang == 'fa' else 'Daily report'}: {state}",
                reply_markup=ak.health_keyboard(lang),
            )
            return

        if action == "health_times":
            cfg = await bot_settings.get_health_settings()
            await bot_settings.set_session(uid, {"mode": "edit_health", "health_field": "times"})
            await message.answer(
                ak.msg("ask_health_times", lang) + "\n" + _fmt_current(lang, cfg.get("times")),
                reply_markup=ak.cancel_keyboard(lang),
            )
            return

        if action == "health_chat":
            cfg = await bot_settings.get_health_settings()
            await bot_settings.set_session(uid, {"mode": "edit_health", "health_field": "chat_id"})
            await message.answer(
                ak.msg("ask_health_chat", lang) + "\n" + _fmt_current(lang, cfg.get("chat_id") or "—"),
                reply_markup=ak.cancel_keyboard(lang),
            )
            return

        if action == "manage_admins":
            await bot_settings.set_session(uid, {"mode": "admins"})
            await message.answer(await _admins_card(lang), reply_markup=ak.admins_keyboard(lang))
            return

        if action in {"admin_role_full", "admin_role_stats", "admin_remove"}:
            await bot_settings.set_session(
                uid,
                {"mode": "edit_admin", "admin_action": action},
            )
            await message.answer(ak.msg("ask_admin_id", lang), reply_markup=ak.cancel_keyboard(lang))
            return

        if action == "nav_back":
            sess = await bot_settings.get_session(uid)
            mode = str(sess.get("mode") or "")
            target_key = str(sess.get("target_key") or "")
            slot_index = sess.get("slot_index")
            if mode in {"backup", "health", "admins", "catalog_wizard"}:
                await bot_settings.clear_session(uid)
                await _show_settings_hub(message, lang, bot_settings)
                return
            if mode == "catalog_wizard":
                await bot_settings.clear_session(uid)
                await _show_settings_hub(message, lang, bot_settings)
                return
            if mode in {"edit_slot", "scoped_rules_ai"} and target_key in TARGET_KEYS and slot_index is not None:
                await bot_settings.set_session(
                    uid,
                    {"mode": "slot", "target_key": target_key, "slot_index": int(slot_index)},
                )
                await _show_slot(message, bot_settings, target_key, int(slot_index), lang)
                return
            if mode == "slot" and target_key in TARGET_KEYS:
                await bot_settings.set_session(uid, {"mode": "target", "target_key": target_key})
                await _show_target(message, bot_settings, target_key, lang)
                return
            if mode == "edit_target" and target_key in TARGET_KEYS:
                await bot_settings.set_session(uid, {"mode": "target", "target_key": target_key})
                await _show_target(message, bot_settings, target_key, lang)
                return
            if mode in {"edit_owner", "owner"}:
                await bot_settings.set_session(uid, {"mode": "owner"})
                await _show_owner(message, bot_settings, lang)
                return
            if mode == "edit_panel":
                await bot_settings.set_session(uid, {"mode": "panel"})
                await _show_panel(message, bot_settings, lang)
                return
            if mode == "target" and target_key in TARGET_KEYS:
                await bot_settings.set_session(uid, {"mode": "messages_hub"})
                await _show_messages_hub(message, lang)
                return
            if mode in {"panel", "messages_hub", "bot_config_chat", "owner"}:
                await bot_settings.clear_session(uid)
                await _show_settings_hub(message, lang, bot_settings)
                return
            raise SkipHandler()

        if action == "cancel":
            sess = await bot_settings.get_session(uid)
            if not sess or sess.get("mode") in {None, ""}:
                raise SkipHandler()
            target_key = str(sess.get("target_key") or "")
            slot_index = sess.get("slot_index")
            mode = str(sess.get("mode") or "")
            if mode == "catalog_wizard":
                await _show_catalog_wizard(message, bot_settings, uid, lang)
                return
            await bot_settings.clear_session(uid)
            if target_key in TARGET_KEYS and slot_index is not None:
                await bot_settings.set_session(
                    uid,
                    {"mode": "slot", "target_key": target_key, "slot_index": int(slot_index)},
                )
                await _show_slot(message, bot_settings, target_key, int(slot_index), lang)
            elif target_key in TARGET_KEYS:
                await bot_settings.set_session(uid, {"mode": "target", "target_key": target_key})
                await _show_target(message, bot_settings, target_key, lang)
            elif mode in {"panel", "edit_panel"}:
                await bot_settings.set_session(uid, {"mode": "panel"})
                await _show_panel(message, bot_settings, lang)
            elif mode in {"owner", "edit_owner"}:
                await bot_settings.set_session(uid, {"mode": "owner"})
                await _show_owner(message, bot_settings, lang)
            else:
                await _show_settings_hub(message, lang, bot_settings)
            return

        if action == "owner_info":
            await bot_settings.set_session(uid, {"mode": "owner"})
            await message.answer(ak.msg("owner_hub", lang))
            await _show_owner(message, bot_settings, lang)
            return

        if action == "creator_contact":
            creator = load_creator_contact(settings.knowledge_root)
            await message.answer(
                creator.format_card(lang),
                reply_markup=await _settings_kb(lang, bot_settings),
            )
            return

        if action == "bot_config_chat":
            await bot_settings.set_session(uid, {"mode": "bot_config_chat", "history": []})
            await message.answer(
                ak.msg("bot_chat_start", lang),
                reply_markup=ak.cancel_keyboard(lang),
            )
            return

        if action == "build_catalogs":
            staging = _staging_dir(settings, uid)
            if staging.exists():
                shutil.rmtree(staging, ignore_errors=True)
            staging.mkdir(parents=True, exist_ok=True)
            await bot_settings.set_session(
                uid,
                {
                    "mode": "catalog_wizard",
                    "catalog_sources": {"site": False, "channel": False, "group": False},
                    "catalog_path": "",
                    "catalog_staging": str(staging),
                },
            )
            await _show_catalog_wizard(message, bot_settings, uid, lang)
            await message.answer(ak.msg("catalog_ask_path", lang))
            return

        if action in {"catalog_src_site", "catalog_src_channel", "catalog_src_group"}:
            sess = await bot_settings.get_session(uid)
            if sess.get("mode") != "catalog_wizard":
                await _show_settings_hub(message, lang, bot_settings)
                return
            sources = dict(sess.get("catalog_sources") or {})
            key = action.replace("catalog_src_", "")
            sources[key] = not bool(sources.get(key))
            sess["catalog_sources"] = sources
            await bot_settings.set_session(uid, sess)
            await _show_catalog_wizard(message, bot_settings, uid, lang)
            return

        if action == "catalog_run":
            sess = await bot_settings.get_session(uid)
            if sess.get("mode") != "catalog_wizard" or ai is None:
                await _show_settings_hub(message, lang, bot_settings)
                return
            sources = sess.get("catalog_sources") or {}
            folder_path = str(sess.get("catalog_path") or "").strip()
            staging = Path(str(sess.get("catalog_staging") or ""))
            await message.answer(ak.msg("catalog_building", lang))
            try:
                folder = prepare_work_folder(
                    knowledge_root=settings.knowledge_root,
                    folder_path=folder_path or None,
                    staging_dir=staging if staging.is_dir() else None,
                    product_hint=Path(folder_path).name if folder_path else "product",
                )
                owner = await bot_settings.get_owner()
                extras: list[str] = []
                if sources.get("site") and owner.site_url:
                    extras.append(f"Official site: {owner.site_url}")
                if sources.get("channel") and owner.channel:
                    extras.append(f"Official channel: {owner.channel}")
                if sources.get("group") and owner.group:
                    extras.append(f"Official group: {owner.group}")
                pid = await build_one_catalog(
                    folder,
                    ai.chat,
                    knowledge_root=settings.knowledge_root,
                    project_root=settings.project_root,
                    extra_sources="\n".join(extras),
                    reload_fn=lambda: load_product_catalogs(settings.knowledge_root),
                )
            except Exception as exc:  # noqa: BLE001
                logger.exception("catalog wizard failed: %s", exc)
                await message.answer(
                    f"❌ {exc}",
                    reply_markup=ak.catalog_wizard_keyboard(
                        lang, sources=sess.get("catalog_sources") or {}
                    ),
                )
                return
            await message.answer(
                ak.msg("catalog_done", lang).format(ids=pid),
                reply_markup=await _settings_kb(lang, bot_settings),
            )
            await bot_settings.clear_session(uid)
            return

        if action in _OWNER_FIELD_BY_ACTION:
            field = _OWNER_FIELD_BY_ACTION[action]
            owner = await bot_settings.get_owner()
            current = getattr(owner, field, "") or ""
            await bot_settings.set_session(uid, {"mode": "edit_owner", "owner_field": field})
            await message.answer(
                _ask_with_current(lang, _ASK_OWNER[field], current),
                reply_markup=ak.cancel_keyboard(lang),
            )
            return

        if action == "settings_messages":
            await bot_settings.set_session(uid, {"mode": "messages_hub"})
            await _show_messages_hub(message, lang)
            return

        if action == "settings_panel":
            await bot_settings.set_session(uid, {"mode": "panel"})
            await _show_panel(message, bot_settings, lang)
            return

        if action in _TARGET_BY_ACTION:
            key = _TARGET_BY_ACTION[action]
            # Account section: force static slots for user DMs
            if key == "support":
                target = await bot_settings.get_target(key)
                for i, s in enumerate(target.slots):
                    if s.kind != "static":
                        await bot_settings.update_slot(key, i, kind="static")
            await bot_settings.set_session(uid, {"mode": "target", "target_key": key})
            await _show_target(message, bot_settings, key, lang)
            return

        if action in _SLOT_BY_ACTION:
            sess = await bot_settings.get_session(uid)
            key = str(sess.get("target_key") or "")
            if key not in TARGET_KEYS:
                await _show_messages_hub(message, lang)
                return
            idx = _SLOT_BY_ACTION[action]
            await bot_settings.set_session(
                uid, {"mode": "slot", "target_key": key, "slot_index": idx}
            )
            await _show_slot(message, bot_settings, key, idx, lang)
            return

        if action == "toggle_slot_enabled":
            sess = await bot_settings.get_session(uid)
            target_key = str(sess.get("target_key") or "")
            slot_index = sess.get("slot_index")
            if target_key not in TARGET_KEYS or slot_index is None:
                await message.answer(
                    "اول یک اسلات را باز کنید." if lang == "fa" else "Open a slot first.",
                    reply_markup=ak.messages_hub_keyboard(lang),
                )
                return
            idx = int(slot_index)
            target = await bot_settings.get_target(target_key)
            slot = target.slot(idx)
            new_enabled = not bool(slot.enabled)
            await bot_settings.update_slot(target_key, idx, enabled=new_enabled)
            await audit.write(
                "toggle_slot_enabled",
                admin_id=uid,
                detail=f"{target_key}/{idx} -> {new_enabled}",
                meta={"target": target_key, "slot": idx, "enabled": new_enabled},
            )
            state = ("فعال" if new_enabled else "غیرفعال") if lang == "fa" else ("on" if new_enabled else "off")
            await message.answer(
                (f"اسلات {idx + 1}: {state}" if lang == "fa" else f"Slot {idx + 1}: {state}"),
            )
            await _show_slot(message, bot_settings, target_key, idx, lang)
            return

        if action in _EDIT_FIELD_BY_ACTION:
            field = _EDIT_FIELD_BY_ACTION[action]
            sess = await bot_settings.get_session(uid)
            if field in {"base_url", "api_token", "required_port", "inbound_id"}:
                panel = await bot_settings.get_panel()
                if field == "api_token":
                    ask_body = _ask_with_current(
                        lang, _ASK_MSG[field], bot_settings.mask_panel_token(panel)
                    )
                elif field == "base_url":
                    ask_body = _ask_with_current(lang, _ASK_MSG[field], panel.base_url)
                elif field == "required_port":
                    ask_body = _ask_with_current(lang, _ASK_MSG[field], panel.required_port)
                else:
                    ask_body = _ask_with_current(lang, _ASK_MSG[field], panel.inbound_id)
                await bot_settings.set_session(
                    uid, {"mode": "edit_panel", "panel_field": field}
                )
                await message.answer(ask_body, reply_markup=ak.cancel_keyboard(lang))
                return
            target_key = str(sess.get("target_key") or "")
            slot_index = sess.get("slot_index")
            if target_key not in TARGET_KEYS:
                await _show_messages_hub(message, lang)
                return
            if sess.get("mode") == "target" and field == "chat_id":
                target = await bot_settings.get_target(target_key)
                await bot_settings.set_session(
                    uid,
                    {"mode": "edit_target", "target_key": target_key, "field": "chat_id"},
                )
                await message.answer(
                    _ask_with_current(lang, _ask_dest_key(target_key), target.chat_id),
                    reply_markup=ak.cancel_keyboard(lang),
                )
                return
            if slot_index is None and sess.get("mode") == "target":
                await message.answer(
                    "یک اسلات (۱/۲/۳) انتخاب کنید." if lang == "fa" else "Pick a slot (1/2/3).",
                    reply_markup=ak.target_edit_keyboard(lang),
                )
                return
            idx = int(slot_index if slot_index is not None else 0)
            target = await bot_settings.get_target(target_key)
            slot = target.slot(idx)
            if field == "rules_prompt":
                await bot_settings.set_session(
                    uid,
                    {
                        "mode": "scoped_rules_ai",
                        "target_key": target_key,
                        "slot_index": idx,
                        "history": [],
                    },
                )
                await message.answer(
                    _ask_with_current(lang, "scoped_rules_start", slot.rules_prompt),
                    reply_markup=ak.cancel_keyboard(lang),
                )
                await message.answer(
                    _ask_with_current(lang, "ask_rules", slot.rules_prompt),
                    reply_markup=ak.cancel_keyboard(lang),
                )
                return
            if field == "kind" and target_key == "support":
                await message.answer(
                    "این بخش فقط پیام به اکانت کاربر است (نوع ثابت)."
                    if lang == "fa"
                    else "Account section uses static user messages only.",
                )
                return
            current_map = {
                "chat_id": slot.chat_id or target.chat_id,
                "message_template": slot.message_template,
                "schedule_times": slot.schedule_times,
                "kind": slot.kind,
            }
            ask_key = _ask_dest_key(target_key) if field == "chat_id" else _ASK_MSG[field]
            await bot_settings.set_session(
                uid,
                {
                    "mode": "edit_slot",
                    "target_key": target_key,
                    "slot_index": idx,
                    "field": field,
                },
            )
            await message.answer(
                _ask_with_current(lang, ask_key, current_map.get(field, "")),
                reply_markup=ak.cancel_keyboard(lang),
            )
            return

    @router.message(F.chat.type == "private", F.document | F.photo)
    async def on_catalog_upload(message: Message) -> None:
        uid = _uid(message)
        if not await access.can_settings(uid) or not message.bot:
            return
        sess = await bot_settings.get_session(uid)
        lang = await _lang(users, message)

        if sess.get("mode") == "import_backup":
            if not message.document:
                await message.answer(ak.msg("ask_backup_import", lang))
                return
            import json
            from io import BytesIO

            buf = BytesIO()
            await message.bot.download(message.document, destination=buf)
            try:
                payload = json.loads(buf.getvalue().decode("utf-8"))
                applied = await bot_settings.import_backup(payload)
            except Exception as exc:  # noqa: BLE001
                await message.answer(f"❌ {exc}", reply_markup=ak.backup_keyboard(lang))
                return
            apply_owner_info(await bot_settings.get_owner())
            await audit.write(
                "import_settings_backup",
                admin_id=uid,
                detail=",".join(applied),
            )
            await bot_settings.set_session(uid, {"mode": "backup"})
            await message.answer(
                ak.msg("backup_imported", lang).format(
                    sections=", ".join(applied) or "—"
                ),
                reply_markup=ak.backup_keyboard(lang),
            )
            return

        if sess.get("mode") != "catalog_wizard":
            raise SkipHandler()
        staging = Path(str(sess.get("catalog_staging") or _staging_dir(settings, uid)))
        staging.mkdir(parents=True, exist_ok=True)
        try:
            if message.document:
                dest = staging / (message.document.file_name or f"file_{message.document.file_id}")
                await message.bot.download(message.document, destination=dest)
            elif message.photo:
                photo = message.photo[-1]
                dest = staging / f"photo_{photo.file_unique_id}.jpg"
                await message.bot.download(photo, destination=dest)
            else:
                return
        except Exception as exc:  # noqa: BLE001
            await message.answer(f"❌ upload failed: {exc}")
            return
        await message.answer(
            ("✅ فایل دریافت شد." if lang == "fa" else "✅ File received.")
            + "\n"
            + ak.msg("catalog_ask_path", lang),
            reply_markup=ak.catalog_wizard_keyboard(
                lang, sources=sess.get("catalog_sources") or {}
            ),
        )

    @router.message(
        F.chat.type == "private",
        F.text,
        ~F.text.startswith("/"),
        ~F.text.in_(ak.all_admin_control_texts()),
        ~F.text.in_(keyboards.all_menu_button_texts()),
        ~F.text.in_(keyboards.all_lang_button_texts()),
    )
    async def on_settings_text(message: Message) -> None:
        uid = _uid(message)
        if not await access.can_settings(uid):
            return
        lang = await _lang(users, message)
        sess = await bot_settings.get_session(uid)
        mode = sess.get("mode")
        if mode not in {
            "edit_target",
            "edit_panel",
            "edit_slot",
            "edit_owner",
            "edit_health",
            "edit_admin",
            "scoped_rules_ai",
            "bot_config_chat",
            "catalog_wizard",
        }:
            raise SkipHandler()

        text = (message.text or "").strip()
        if not text:
            return

        if mode == "edit_health":
            field = str(sess.get("health_field") or "")
            if field == "times":
                await bot_settings.update_health_settings(times=text)
            elif field == "chat_id":
                await bot_settings.update_health_settings(chat_id=text)
            else:
                await bot_settings.clear_session(uid)
                await _show_settings_hub(message, lang, bot_settings)
                return
            await bot_settings.set_session(uid, {"mode": "health"})
            await message.answer(ak.msg("saved_ok", lang), reply_markup=ak.health_keyboard(lang))
            report = await build_health_report(settings, bot_settings, lang=lang)
            await message.answer(report[:3900], reply_markup=ak.health_keyboard(lang))
            return

        if mode == "edit_admin":
            action = str(sess.get("admin_action") or "")
            try:
                target_id = int(text.replace("@", "").strip())
            except ValueError:
                await message.answer(ak.msg("ask_admin_id", lang), reply_markup=ak.cancel_keyboard(lang))
                return
            if target_id in settings.bot_admin_ids and action == "admin_remove":
                await message.answer(
                    ("ادمین env را از BOT_ADMIN_IDS حذف کنید." if lang == "fa" else "Remove env admins from BOT_ADMIN_IDS."),
                    reply_markup=ak.admins_keyboard(lang),
                )
                return
            if action == "admin_role_full":
                await bot_settings.set_admin_role(target_id, "full")
            elif action == "admin_role_stats":
                await bot_settings.set_admin_role(target_id, "stats")
            elif action == "admin_remove":
                await bot_settings.remove_admin(target_id)
            else:
                await bot_settings.clear_session(uid)
                await _show_settings_hub(message, lang, bot_settings)
                return
            await audit.write(
                "update_admin_role",
                admin_id=uid,
                detail=f"{action}:{target_id}",
            )
            await bot_settings.set_session(uid, {"mode": "admins"})
            await message.answer(ak.msg("saved_ok", lang))
            await message.answer(await _admins_card(lang), reply_markup=ak.admins_keyboard(lang))
            return

        if mode == "catalog_wizard":
            # Treat as folder path on the bot host
            sess["catalog_path"] = text
            await bot_settings.set_session(uid, sess)
            await message.answer(
                ("✅ مسیر ذخیره شد." if lang == "fa" else "✅ Path saved.")
                + "\n"
                + _fmt_current(lang, text),
                reply_markup=ak.catalog_wizard_keyboard(
                    lang, sources=sess.get("catalog_sources") or {}
                ),
            )
            return

        if mode == "edit_owner":
            field = str(sess.get("owner_field") or "")
            if field not in {
                "site_url",
                "channel",
                "group",
                "support_handle",
                "bot_display_name",
            }:
                await bot_settings.clear_session(uid)
                await _show_settings_hub(message, lang, bot_settings)
                return
            owner = await bot_settings.update_owner(**{field: text})
            apply_owner_info(owner)
            if field == "bot_display_name":
                from src.branding import sync_telegram_bot_name

                await sync_telegram_bot_name(message.bot, text)
            await audit.write(
                "update_owner_info",
                admin_id=uid,
                detail=f"Updated owner.{field}",
                meta={"field": field},
            )
            await bot_settings.set_session(uid, {"mode": "owner"})
            await message.answer(ak.msg("saved_ok", lang))
            await _show_owner(message, bot_settings, lang)
            return

        if mode == "edit_target":
            key = str(sess.get("target_key") or "")
            field = str(sess.get("field") or "")
            if key not in TARGET_KEYS or field != "chat_id":
                await bot_settings.clear_session(uid)
                await _show_messages_hub(message, lang)
                return
            ok = await _save_dest(
                message, uid=uid, lang=lang, target_key=key, slot_index=None, value=text
            )
            if not ok:
                return
            updated = await bot_settings.get_target(key)
            await audit.write(
                "update_message_target",
                admin_id=uid,
                detail=f"Updated chat_id for {key}",
                meta={"target": key, "field": "chat_id"},
            )
            await bot_settings.set_session(uid, {"mode": "target", "target_key": key})
            await message.answer(ak.msg("saved_ok", lang))
            await message.answer(
                bot_settings.format_target_card(updated, lang=lang)[:3900],
                reply_markup=ak.target_edit_keyboard(lang),
            )
            return

        if mode == "edit_slot":
            key = str(sess.get("target_key") or "")
            field = str(sess.get("field") or "")
            slot_index = int(sess.get("slot_index") or 0)
            if key not in TARGET_KEYS or field not in {
                "chat_id",
                "message_template",
                "schedule_times",
                "kind",
            }:
                await bot_settings.clear_session(uid)
                await _show_messages_hub(message, lang)
                return
            if field == "chat_id":
                ok = await _save_dest(
                    message,
                    uid=uid,
                    lang=lang,
                    target_key=key,
                    slot_index=slot_index,
                    value=text,
                )
                if not ok:
                    return
            else:
                value: Any = text
                if field == "kind":
                    kind = text.strip().lower()
                    if key == "support":
                        kind = "static"
                    if kind not in SLOT_KINDS:
                        await message.answer(
                            ak.msg("ask_slot_kind", lang),
                            reply_markup=ak.cancel_keyboard(lang),
                        )
                        return
                    value = kind
                await bot_settings.update_slot(key, slot_index, **{field: value})
            updated = await bot_settings.get_target(key)
            await audit.write(
                "update_message_slot",
                admin_id=uid,
                detail=f"Updated {field} for {key} slot {slot_index}",
                meta={"target": key, "slot": slot_index, "field": field},
            )
            await bot_settings.set_session(
                uid, {"mode": "slot", "target_key": key, "slot_index": slot_index}
            )
            await message.answer(ak.msg("saved_ok", lang))
            await _show_slot(message, bot_settings, key, slot_index, lang)
            return

        if mode == "scoped_rules_ai":
            key = str(sess.get("target_key") or "")
            slot_index = int(sess.get("slot_index") or 0)
            if key not in TARGET_KEYS or ai is None:
                await bot_settings.clear_session(uid)
                await _show_messages_hub(message, lang)
                return
            target = await bot_settings.get_target(key)
            slot = target.slot(slot_index)
            new_rules = text
            wants_ai = any(
                w in text.lower()
                for w in ("بساز", "عوض", "تغییر", "rewrite", "change", "update", "make")
            ) or len(text) < 200
            if wants_ai:
                prompt = (
                    f"You edit ONLY the rules_prompt for destination={key} slot={slot_index + 1} "
                    f"(kind={slot.kind}). Do not change creator contact or other bot sections.\n"
                    f"Current rules:\n{slot.rules_prompt or '(empty)'}\n\n"
                    f"Admin request:\n{text}\n\n"
                    "Return ONLY the new rules_prompt text (no markdown, no commentary)."
                )
                try:
                    answer = await ai.chat(
                        [
                            {
                                "role": "system",
                                "content": "You are a settings assistant. Output only the updated rules prompt.",
                            },
                            {"role": "user", "content": prompt},
                        ]
                    )
                    answer = strip_reasoning_leak(answer)
                    if answer and not looks_like_reasoning_leak(answer):
                        new_rules = answer.strip()
                except AIClientError as exc:
                    logger.exception("scoped rules AI failed: %s", exc)
            await bot_settings.update_slot(key, slot_index, rules_prompt=new_rules)
            await audit.write(
                "update_slot_rules_ai",
                admin_id=uid,
                detail=f"Rules updated via AI for {key}/{slot_index}",
                meta={"target": key, "slot": slot_index},
            )
            await bot_settings.set_session(
                uid, {"mode": "slot", "target_key": key, "slot_index": slot_index}
            )
            await message.answer(ak.msg("saved_ok", lang))
            await _show_slot(message, bot_settings, key, slot_index, lang)
            return

        if mode == "bot_config_chat":
            if ai is None:
                await message.answer("AI unavailable.")
                return
            lowered = text.lower()
            if any(k in lowered for k in ("سازنده", "creator_contact", "creator contact")):
                await message.answer(ak.msg("creator_locked", lang))
                return

            # Deterministic UI layout requests (do not depend on model inventing menus).
            # Avoid treating "کلید بساز" as a layout request.
            is_button_mgmt = any(
                x in text
                for x in (
                    "کلید بساز",
                    "دکمه بساز",
                    "حذف کلید",
                    "پاک کردن کلید",
                    "لیست کلید",
                    "add button",
                    "create button",
                    "remove button",
                    "delete button",
                    "list button",
                )
            )
            wants_two_cols = (not is_button_mgmt) and (
                any(
                    x in text
                    for x in ("دو ردیف", "دو ستون", "2 ستون", "2 ردیف", "two row", "two column")
                )
                or (
                    any(x in text for x in ("کوچیک", "کوچک", "compact", "small"))
                    and any(
                        x in text
                        for x in ("کلید", "دکمه", "کیبورد", "تنظیمات", "button", "keyboard")
                    )
                )
            )
            wants_one_col = any(
                x in text for x in ("یک ردیف", "تک ستون", "1 ستون", "one column", "single column")
            )
            if wants_two_cols or wants_one_col:
                cols = 1 if wants_one_col and not wants_two_cols else 2
                ui = await bot_settings.update_ui_settings(settings_columns=cols)
                ak.set_settings_columns(int(ui["settings_columns"]))
                await audit.write(
                    "bot_config_chat_apply",
                    admin_id=uid,
                    detail=f"ui.settings_columns={ui['settings_columns']}",
                )
                await bot_settings.set_session(uid, {"mode": "settings"})
                msg = (
                    f"ظاهر کیبورد تنظیمات روی {ui['settings_columns']} ستون تنظیم شد.\n"
                    "اندازه دقیق دکمه‌ها را تلگرام مشخص می‌کند؛ با دو ستون معمولاً جمع‌وجورتر دیده می‌شوند."
                    if lang.startswith("fa")
                    else (
                        f"Settings keyboard set to {ui['settings_columns']} column(s).\n"
                        "Telegram controls exact button width; two columns usually look more compact."
                    )
                )
                await message.answer(msg, reply_markup=await _settings_kb(lang, bot_settings))
                return

            # Deterministic custom button add/remove/list (Persian + English cues).
            wants_list_buttons = any(
                x in text for x in ("لیست کلید", "کلیدهای سفارشی", "list button", "list custom")
            )
            wants_remove_button = any(
                x in text for x in ("حذف کلید", "پاک کردن کلید", "remove button", "delete button")
            )
            wants_add_button = any(
                x in text
                for x in ("کلید بساز", "دکمه بساز", "اضافه کردن کلید", "add button", "create button")
            )
            if wants_list_buttons:
                from src.generated.buttons import list_generated_buttons

                gen_items = list_generated_buttons(menu="settings", refresh=True)
                cat_items = await bot_settings.list_custom_buttons(menu="settings")
                lines: list[str] = []
                if gen_items:
                    lines.append("—— کلیدهای کدنویسی‌شده (AI) ——" if lang.startswith("fa") else "—— AI-coded buttons ——")
                    for b in gen_items:
                        lines.append(
                            f"• {b.get('id')}: {b.get('label_fa') or b.get('label_en')} [generated]"
                        )
                if cat_items:
                    lines.append("—— کلیدهای کاتالوگ ——" if lang.startswith("fa") else "—— Catalog buttons ——")
                    for b in cat_items:
                        lines.append(
                            f"• {b.get('id')}: {b.get('label_fa') or b.get('label_en')} → {b.get('action')}"
                        )
                if not lines:
                    body = "کلید سفارشی ندارید." if lang.startswith("fa") else "No custom buttons."
                else:
                    body = "\n".join(lines)
                await message.answer(body[:3900], reply_markup=ak.cancel_keyboard(lang))
                return
            if wants_remove_button:
                from src.button_codegen import queue_generated_button_remove
                from src.generated.buttons import list_generated_buttons

                bid = ""
                label = ""
                for token in text.replace("،", " ").split():
                    if token.startswith("id=") or token.startswith("btn_") or token.startswith("cb_"):
                        bid = token.split("=", 1)[-1].strip()
                for cue in ("حذف کلید", "پاک کردن کلید", "remove button", "delete button"):
                    if cue in text:
                        label = text.split(cue, 1)[-1].strip(" :-")
                        break
                # Prefer generated registry removal via safe-change
                gen_hit = None
                for b in list_generated_buttons(menu=None, refresh=True):
                    labs = {str(b.get("label_fa") or "").strip(), str(b.get("label_en") or "").strip()}
                    if (bid and str(b.get("id") or "") == bid) or (label and label in labs):
                        gen_hit = b
                        break
                if gen_hit:
                    result = queue_generated_button_remove(
                        button_id=str(gen_hit.get("id") or ""),
                        label=str(gen_hit.get("label_fa") or ""),
                        description=f"Remove generated button {gen_hit.get('id')}",
                        admin_chat_id=uid,
                    )
                    if not result.get("ok"):
                        await message.answer(
                            f"❌ {result.get('error')}",
                            reply_markup=ak.cancel_keyboard(lang),
                        )
                        return
                    await audit.write(
                        "generated_button_remove_queued",
                        admin_id=uid,
                        detail=str(result.get("change_id")),
                    )
                    await message.answer(
                        (
                            "🛡 حذف کلید در صف safe-change قرار گرفت.\n"
                            f"change: `{result.get('change_id')}`\n"
                            "ربات ری‌استارت می‌شود؛ حدود ۱ دقیقه فرصت چک دارید، بعد پیام تأیید می‌آید."
                            if lang.startswith("fa")
                            else (
                                "🛡 Button removal queued via safe-change.\n"
                                f"change: `{result.get('change_id')}`\n"
                                "Bot will restart; ~1 minute observe, then confirm prompt."
                            )
                        ),
                        reply_markup=ak.cancel_keyboard(lang),
                    )
                    return
                removed = await bot_settings.remove_custom_button(button_id=bid, label=label)
                if not removed:
                    await message.answer(
                        "کلیدی پیدا نشد. id یا متن دکمه را بفرستید."
                        if lang.startswith("fa")
                        else "Button not found. Send id or label.",
                        reply_markup=ak.cancel_keyboard(lang),
                    )
                    return
                await audit.write(
                    "custom_button_remove",
                    admin_id=uid,
                    detail=str(removed.get("id")),
                )
                await bot_settings.set_session(uid, {"mode": "settings"})
                await message.answer(
                    ("✅ کلید حذف شد: " if lang.startswith("fa") else "✅ Removed: ")
                    + str(removed.get("label_fa") or removed.get("id")),
                    reply_markup=await _settings_kb(lang, bot_settings),
                )
                return
            if wants_add_button:
                # Explicit catalog shortcut: action=run_health_now etc.
                has_catalog_action = "action=" in text
                if has_catalog_action:
                    label_fa = ""
                    action_name = "noop_confirm"
                    params: dict[str, Any] = {}
                    chunk = text
                    for cue in ("کلید بساز", "دکمه بساز", "اضافه کردن کلید", "add button", "create button"):
                        if cue in chunk:
                            chunk = chunk.split(cue, 1)[-1].strip(" :-")
                            break
                    parts = chunk.replace("—", " ").replace("–", " ").split()
                    label_bits: list[str] = []
                    for part in parts:
                        if part.startswith("action="):
                            action_name = part.split("=", 1)[1].strip()
                        elif "=" in part and part.split("=", 1)[0] in {
                            "target",
                            "slot",
                            "text",
                            "menu",
                        }:
                            k, v = part.split("=", 1)
                            params[k] = v
                        else:
                            label_bits.append(part)
                    label_fa = " ".join(label_bits).strip().strip("\"'«»")
                    if label_fa and action_name in ALLOWED_ACTIONS:
                        try:
                            created = await bot_settings.add_custom_button(
                                {
                                    "id": new_button_id(),
                                    "menu": str(params.pop("menu", "settings") or "settings"),
                                    "label_fa": label_fa,
                                    "label_en": label_fa,
                                    "enabled": True,
                                    "action": action_name,
                                    "params": params,
                                    "order": 50,
                                }
                            )
                        except ValueError as exc:
                            await message.answer(f"❌ {exc}", reply_markup=ak.cancel_keyboard(lang))
                            return
                        await audit.write(
                            "custom_button_add",
                            admin_id=uid,
                            detail=f"{created.get('id')}:{created.get('action')}",
                        )
                        await bot_settings.set_session(uid, {"mode": "settings"})
                        await message.answer(
                            (
                                "✅ کلید کاتالوگ ساخته شد:\n"
                                if lang.startswith("fa")
                                else "✅ Catalog button created:\n"
                            )
                            + f"{created.get('label_fa')} → {created.get('action')} ({created.get('id')})",
                            reply_markup=await _settings_kb(lang, bot_settings),
                        )
                        return

                # Default: AI writes real Python code → safe-change watchdog (~1 min).
                from src.button_codegen import (
                    build_codegen_user_prompt,
                    codegen_system_prompt,
                    extract_python_block,
                    guess_labels_from_request,
                    new_generated_id,
                    queue_generated_button_add,
                    validate_generated_button_source,
                )

                if ai is None:
                    await message.answer("AI unavailable.", reply_markup=ak.cancel_keyboard(lang))
                    return
                button_id = new_generated_id()
                label_fa, label_en = guess_labels_from_request(text)
                await message.answer(
                    "⏳ در حال کدنویسی کلید با AI…"
                    if lang.startswith("fa")
                    else "⏳ Generating button code with AI…"
                )
                try:
                    answer = await ai.chat(
                        [
                            {"role": "system", "content": codegen_system_prompt()},
                            {
                                "role": "user",
                                "content": build_codegen_user_prompt(
                                    admin_request=text,
                                    button_id=button_id,
                                    label_fa=label_fa,
                                    label_en=label_en,
                                    lang=lang,
                                ),
                            },
                        ]
                    )
                except AIClientError as exc:
                    await message.answer(f"❌ {exc}", reply_markup=ak.cancel_keyboard(lang))
                    return
                source = extract_python_block(strip_reasoning_leak(answer or ""))
                ok_src, detail = validate_generated_button_source(source, button_id=button_id)
                if not ok_src:
                    await message.answer(
                        (
                            f"❌ کد تولیدشده معتبر نبود: {detail}\n"
                            "دوباره با توضیح واضح‌تر بخواهید."
                            if lang.startswith("fa")
                            else f"❌ Invalid generated code: {detail}"
                        ),
                        reply_markup=ak.cancel_keyboard(lang),
                    )
                    return
                result = queue_generated_button_add(
                    button_id=button_id,
                    label_fa=label_fa,
                    label_en=label_en,
                    source=source,
                    description=f"AI button: {label_fa}",
                    admin_chat_id=uid,
                )
                if not result.get("ok"):
                    await message.answer(
                        f"❌ {result.get('error')}",
                        reply_markup=ak.cancel_keyboard(lang),
                    )
                    return
                await audit.write(
                    "generated_button_add_queued",
                    admin_id=uid,
                    detail=f"{button_id}:{result.get('change_id')}",
                )
                await message.answer(
                    (
                        "🛡 کلید با کد AI در صف safe-change قرار گرفت.\n"
                        f"id: `{button_id}`\n"
                        f"change: `{result.get('change_id')}`\n"
                        f"برچسب: {label_fa}\n\n"
                        "ربات ری‌استارت می‌شود، حدود ۱ دقیقه فرصت تست دارید، "
                        "بعد پیام تأیید می‌آید. اگر تأیید نشود، خودکار برمی‌گردد."
                        if lang.startswith("fa")
                        else (
                            "🛡 AI-coded button queued via safe-change.\n"
                            f"id: `{button_id}`\n"
                            f"change: `{result.get('change_id')}`\n"
                            f"label: {label_fa}\n\n"
                            "Bot restarts, ~1 minute observe, then confirm. "
                            "No confirm → auto rollback."
                        )
                    ),
                    reply_markup=ak.cancel_keyboard(lang),
                )
                return

            from src.bot_config_apply import (
                apply_operator_lines,
                build_full_state_brief,
                operator_command_help,
                operator_system_prompt,
                strip_apply_lines,
            )

            state_brief = await build_full_state_brief(bot_settings)
            prompt = (
                f"{operator_system_prompt()}\n"
                f"CURRENT STATE:\n{state_brief}\n\n"
                f"{operator_command_help()}\n"
                f"Admin language hint: {lang}\n"
                f"Admin request: {text}"
            )
            try:
                answer = await ai.chat(
                    [
                        {
                            "role": "system",
                            "content": (
                                "Full settings operator. Edit any existing section via APPLY_*/OPEN_SECTION. "
                                "No fake menus."
                            ),
                        },
                        {"role": "user", "content": prompt},
                    ]
                )
            except AIClientError as exc:
                await message.answer(f"❌ {exc}", reply_markup=ak.cancel_keyboard(lang))
                return
            answer = strip_reasoning_leak(answer)
            result = await apply_operator_lines(
                (answer or "").splitlines(),
                bot_settings=bot_settings,
                message_bot=message.bot,
                allowed_catalog_actions=ALLOWED_ACTIONS,
            )
            clean = strip_apply_lines(answer or "")
            if result.status_dump:
                clean = (
                    (clean + "\n\n—— STATUS ——\n" + result.status_dump)
                    if clean
                    else result.status_dump
                )
            if result.applied:
                clean = (
                    clean
                    + (
                        "\n\n✅ اعمال شد: "
                        if lang.startswith("fa")
                        else "\n\n✅ Applied: "
                    )
                    + ", ".join(result.applied)
                ).strip()
                await audit.write(
                    "bot_config_chat_apply",
                    admin_id=uid,
                    detail=", ".join(result.applied)[:500],
                )
            if result.errors:
                clean = (
                    clean
                    + (
                        "\n⚠️ "
                        if lang.startswith("fa")
                        else "\n⚠ "
                    )
                    + "; ".join(result.errors)
                ).strip()

            # Navigate to requested section when possible.
            if result.open_section:
                sec = result.open_section
                await bot_settings.set_session(uid, {"mode": sec if sec != "account" else "target"})
                if sec == "settings":
                    await _show_settings_hub(message, lang, bot_settings)
                    return
                if sec == "owner":
                    await bot_settings.set_session(uid, {"mode": "owner"})
                    await _show_owner(message, bot_settings, lang)
                    return
                if sec == "messages":
                    await bot_settings.set_session(uid, {"mode": "messages_hub"})
                    await _show_messages_hub(message, lang)
                    return
                if sec == "panel":
                    await bot_settings.set_session(uid, {"mode": "panel"})
                    await _show_panel(message, bot_settings, lang)
                    return
                if sec == "health":
                    from src.health_report import build_health_report as _bhr

                    report = await _bhr(settings, bot_settings, lang=lang)
                    await bot_settings.set_session(uid, {"mode": "health"})
                    await message.answer(
                        ((clean + "\n\n") if clean else "") + report[:3500],
                        reply_markup=ak.health_keyboard(lang),
                    )
                    return
                if sec == "backup":
                    await bot_settings.set_session(uid, {"mode": "backup"})
                    await message.answer(
                        ((clean + "\n\n") if clean else "")
                        + ("💾 پشتیبان تنظیمات" if lang.startswith("fa") else "💾 Settings backup"),
                        reply_markup=ak.backup_keyboard(lang),
                    )
                    return
                if sec == "admins":
                    await bot_settings.set_session(uid, {"mode": "admins"})
                    await message.answer(
                        ((clean + "\n\n") if clean else "") + await _admins_card(lang),
                        reply_markup=ak.admins_keyboard(lang),
                    )
                    return
                if sec in {"channel", "group", "account", "test"}:
                    key = "support" if sec == "account" else sec
                    await bot_settings.set_session(uid, {"mode": "target", "target_key": key})
                    if clean:
                        await message.answer(clean[:3900])
                    await _show_target(message, bot_settings, key, lang)
                    return
                if sec == "creator":
                    creator = load_creator_contact(settings.knowledge_root)
                    await message.answer(
                        ((clean + "\n\n") if clean else "") + creator.format_card(lang),
                        reply_markup=await _settings_kb(lang, bot_settings),
                    )
                    return
                if sec == "control" and control is not None:
                    from src.handlers.admin_control import _show_control_home

                    await users.set_ask_ai(uid, False)
                    await control.registry.set_session(uid, {"mode": "control_home"})
                    if clean:
                        await message.answer(clean[:3900])
                    await _show_control_home(message, control, lang)
                    return

            if result.show_settings_keyboard:
                await bot_settings.set_session(uid, {"mode": "settings"})
                kb = await _settings_kb(lang, bot_settings)
            else:
                kb = ak.cancel_keyboard(lang)
            await message.answer(
                (clean or ak.msg("saved_ok", lang))[:3900],
                reply_markup=kb,
            )
            return

        if mode == "edit_panel":
            field = str(sess.get("panel_field") or "")
            fields: dict[str, Any] = {}
            try:
                if field == "api_token":
                    fields["api_token"] = text
                elif field == "base_url":
                    fields["base_url"] = text
                elif field == "required_port":
                    fields["required_port"] = int(text)
                elif field == "inbound_id":
                    fields["inbound_id"] = int(text)
                else:
                    await message.answer(
                        "فیلد نامعتبر." if lang == "fa" else "Invalid field.",
                        reply_markup=ak.panel_edit_keyboard(lang),
                    )
                    return
            except ValueError:
                await message.answer(
                    "عدد معتبر بفرستید." if lang == "fa" else "Send a valid number.",
                    reply_markup=ak.cancel_keyboard(lang),
                )
                return
            panel = await bot_settings.update_panel(**fields)
            await audit.write(
                "update_panel",
                admin_id=uid,
                detail=f"Updated panel.{field}",
                meta={"field": field},
            )
            await bot_settings.set_session(uid, {"mode": "panel"})
            await message.answer(ak.msg("saved_ok", lang))
            await message.answer(
                bot_settings.format_panel_card(panel, lang=lang),
                reply_markup=ak.panel_edit_keyboard(lang),
            )
            return

    return router
