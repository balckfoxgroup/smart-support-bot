"""Bot-side API: request a safe change and record admin confirm/reject."""

from __future__ import annotations

import os
import time
from typing import Any

from src.safety.paths import (
    CONFIRM_SECONDS_DEFAULT,
    DEFAULT_SUPPORT_CHAT_ID,
    OBSERVE_SECONDS_DEFAULT,
)
from src.safety.state import (
    clear_decision,
    load_pending,
    new_change_id,
    read_heartbeat,
    read_request,
    write_decision,
    write_request,
)


def resolve_support_chat_id(explicit: str | int | None = None) -> str:
    """Confirm prompts always go to support (not the triggering operator by default)."""
    if explicit is not None and str(explicit).strip():
        return str(explicit).strip()
    for key in (
        "SAFETY_CONFIRM_CHAT_ID",
        "CONVO_ANALYSIS_CHAT_ID",
        "NIGHTLY_SUPPORT_CHAT_ID",
    ):
        val = (os.getenv(key) or "").strip()
        if val:
            return val
    return DEFAULT_SUPPORT_CHAT_ID


def request_safe_change(
    *,
    description: str,
    admin_chat_id: str | int | None = None,
    files: dict[str, str] | None = None,
    marker_only: bool = False,
    confirm_seconds: int = CONFIRM_SECONDS_DEFAULT,
    observe_seconds: int = OBSERVE_SECONDS_DEFAULT,
) -> dict[str, Any]:
    """Queue a change for the independent watchdog.

    ``files`` maps paths relative to install root → full text content.
    ``marker_only`` writes a harmless drill marker under data/ (not restored away).
    Confirm messages are sent to the support chat after ``observe_seconds``.
    """
    existing = read_request()
    pending = load_pending()
    if existing and existing.get("status") not in {"done", "cancelled", "consumed"}:
        return {"ok": False, "error": "A safety request is already queued."}
    if pending and pending.status in {
        "ready_to_apply",
        "applying",
        "observing",
        "awaiting_confirm",
        "restoring",
    }:
        return {
            "ok": False,
            "error": f"Pending change already active ({pending.change_id}, {pending.status}).",
        }

    change_id = new_change_id()
    support_chat = resolve_support_chat_id(admin_chat_id)
    payload = {
        "change_id": change_id,
        "description": description.strip() or "safe change",
        "admin_chat_id": support_chat,
        "files": files or {},
        "marker_only": bool(marker_only),
        "confirm_seconds": int(confirm_seconds),
        "observe_seconds": int(observe_seconds),
        "created_at": time.time(),
        "status": "queued",
    }
    write_request(payload)
    clear_decision()
    return {"ok": True, "change_id": change_id, "payload": payload}


def confirm_change(change_id: str, *, by_user_id: int | None = None) -> dict[str, Any]:
    pending = load_pending()
    if not pending or pending.change_id != change_id:
        return {"ok": False, "error": "No matching pending change."}
    if pending.status != "awaiting_confirm":
        return {"ok": False, "error": f"Change not awaiting confirm ({pending.status})."}
    write_decision(change_id, "confirm", by_user_id=by_user_id)
    return {"ok": True, "change_id": change_id, "decision": "confirm"}


def reject_change(change_id: str, *, by_user_id: int | None = None) -> dict[str, Any]:
    pending = load_pending()
    if not pending or pending.change_id != change_id:
        return {"ok": False, "error": "No matching pending change."}
    write_decision(change_id, "reject", by_user_id=by_user_id)
    return {"ok": True, "change_id": change_id, "decision": "reject"}


def safety_status() -> dict[str, Any]:
    pending = load_pending()
    return {
        "pending": pending.to_dict() if pending else None,
        "request": read_request(),
        "heartbeat": read_heartbeat(),
        "support_chat_id": resolve_support_chat_id(),
    }
