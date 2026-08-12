"""Minimal Telegram Bot API helper for the watchdog (no aiogram dependency)."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any


def _call(token: str, method: str, payload: dict[str, Any], timeout: float = 30.0) -> dict[str, Any]:
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            body = json.loads(raw)
        except json.JSONDecodeError:
            body = {"ok": False, "description": raw or str(exc)}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "description": str(exc)}
    return body if isinstance(body, dict) else {"ok": False, "description": "bad response"}


def get_me(token: str) -> dict[str, Any]:
    return _call(token, "getMe", {})


def send_message(
    token: str,
    chat_id: str | int,
    text: str,
    *,
    reply_markup: dict[str, Any] | None = None,
    disable_notification: bool = True,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "chat_id": chat_id,
        "text": text[:3900],
        "disable_notification": disable_notification,
    }
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup
    return _call(token, "sendMessage", payload)


def edit_message_text(
    token: str,
    chat_id: str | int,
    message_id: int,
    text: str,
) -> dict[str, Any]:
    return _call(
        token,
        "editMessageText",
        {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text[:3900],
        },
    )


def confirm_keyboard(change_id: str) -> dict[str, Any]:
    return {
        "inline_keyboard": [
            [
                {"text": "✅ بله — تأیید", "callback_data": f"sf_ok:{change_id}"},
                {"text": "❌ خیر — برگشت", "callback_data": f"sf_no:{change_id}"},
            ]
        ]
    }
