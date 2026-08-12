"""Pending change state + heartbeat helpers."""

from __future__ import annotations

import json
import secrets
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from src.safety.paths import (
    CONFIRM_SECONDS_DEFAULT,
    DECISION_PATH,
    HEARTBEAT_PATH,
    OBSERVE_SECONDS_DEFAULT,
    PENDING_PATH,
    REQUEST_PATH,
    SAFETY_ROOT,
)


@dataclass
class PendingChange:
    change_id: str
    description: str
    admin_chat_id: str
    backup_path: str
    status: str
    created_at: float
    confirm_deadline: float | None = None
    observe_until: float | None = None
    confirm_message_id: int | None = None
    files: dict[str, str] | None = None  # relative path → text content
    marker_only: bool = False
    last_error: str = ""
    confirm_seconds: int = CONFIRM_SECONDS_DEFAULT
    observe_seconds: int = OBSERVE_SECONDS_DEFAULT

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> PendingChange:
        return cls(
            change_id=str(raw.get("change_id") or ""),
            description=str(raw.get("description") or ""),
            admin_chat_id=str(raw.get("admin_chat_id") or ""),
            backup_path=str(raw.get("backup_path") or ""),
            status=str(raw.get("status") or ""),
            created_at=float(raw.get("created_at") or 0),
            confirm_deadline=(
                float(raw["confirm_deadline"])
                if raw.get("confirm_deadline") is not None
                else None
            ),
            observe_until=(
                float(raw["observe_until"])
                if raw.get("observe_until") is not None
                else None
            ),
            confirm_message_id=(
                int(raw["confirm_message_id"])
                if raw.get("confirm_message_id") is not None
                else None
            ),
            files=raw.get("files") if isinstance(raw.get("files"), dict) else None,
            marker_only=bool(raw.get("marker_only")),
            last_error=str(raw.get("last_error") or ""),
            confirm_seconds=int(raw.get("confirm_seconds") or CONFIRM_SECONDS_DEFAULT),
            observe_seconds=int(raw.get("observe_seconds") or OBSERVE_SECONDS_DEFAULT),
        )


def ensure_safety_dirs() -> None:
    SAFETY_ROOT.mkdir(parents=True, exist_ok=True)
    (SAFETY_ROOT / "backups").mkdir(parents=True, exist_ok=True)
    (SAFETY_ROOT / "staging").mkdir(parents=True, exist_ok=True)


def new_change_id() -> str:
    return f"chg_{secrets.token_hex(6)}"


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return raw if isinstance(raw, dict) else None


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def load_pending() -> PendingChange | None:
    raw = _read_json(PENDING_PATH)
    if not raw:
        return None
    try:
        return PendingChange.from_dict(raw)
    except Exception:
        return None


def save_pending(pending: PendingChange) -> None:
    ensure_safety_dirs()
    _write_json(PENDING_PATH, pending.to_dict())


def clear_pending() -> None:
    if PENDING_PATH.is_file():
        PENDING_PATH.unlink(missing_ok=True)


def write_heartbeat(*, pid: int, status: str = "ok") -> None:
    HEARTBEAT_PATH.parent.mkdir(parents=True, exist_ok=True)
    _write_json(
        HEARTBEAT_PATH,
        {
            "ts": time.time(),
            "pid": pid,
            "status": status,
        },
    )


def read_heartbeat() -> dict[str, Any] | None:
    return _read_json(HEARTBEAT_PATH)


def heartbeat_age_seconds() -> float | None:
    hb = read_heartbeat()
    if not hb or "ts" not in hb:
        return None
    try:
        return max(0.0, time.time() - float(hb["ts"]))
    except (TypeError, ValueError):
        return None


def write_request(payload: dict[str, Any]) -> None:
    _write_json(REQUEST_PATH, payload)


def read_request() -> dict[str, Any] | None:
    return _read_json(REQUEST_PATH)


def clear_request() -> None:
    if REQUEST_PATH.is_file():
        REQUEST_PATH.unlink(missing_ok=True)


def write_decision(change_id: str, decision: str, *, by_user_id: int | None = None) -> None:
    _write_json(
        DECISION_PATH,
        {
            "change_id": change_id,
            "decision": decision,
            "ts": time.time(),
            "by_user_id": by_user_id,
        },
    )


def read_decision() -> dict[str, Any] | None:
    return _read_json(DECISION_PATH)


def clear_decision() -> None:
    if DECISION_PATH.is_file():
        DECISION_PATH.unlink(missing_ok=True)
