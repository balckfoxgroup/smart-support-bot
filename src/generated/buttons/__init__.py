"""AI-generated admin button handlers (loaded from registry.json)."""

from __future__ import annotations

import importlib
import json
import logging
import re
from pathlib import Path
from types import ModuleType
from typing import Any

logger = logging.getLogger(__name__)

_DIR = Path(__file__).resolve().parent
_REGISTRY_PATH = _DIR / "registry.json"

_cache_buttons: list[dict[str, Any]] | None = None
_cache_modules: dict[str, ModuleType] = {}


def registry_path() -> Path:
    return _REGISTRY_PATH


def _read_registry() -> dict[str, Any]:
    if not _REGISTRY_PATH.is_file():
        return {"buttons": []}
    try:
        raw = json.loads(_REGISTRY_PATH.read_text(encoding="utf-8"))
        if isinstance(raw, dict):
            raw.setdefault("buttons", [])
            return raw
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        logger.warning("generated buttons registry unreadable: %s", exc)
    return {"buttons": []}


def list_generated_buttons(*, menu: str | None = "settings", refresh: bool = False) -> list[dict[str, Any]]:
    global _cache_buttons
    if refresh or _cache_buttons is None:
        data = _read_registry()
        items = data.get("buttons") if isinstance(data.get("buttons"), list) else []
        out: list[dict[str, Any]] = []
        for item in items:
            if not isinstance(item, dict):
                continue
            if not item.get("enabled", True):
                continue
            if menu and str(item.get("menu") or "settings") != menu:
                continue
            out.append(dict(item))
        out.sort(key=lambda b: (int(b.get("order") or 100), str(b.get("id") or "")))
        _cache_buttons = out
    return list(_cache_buttons or [])


def find_generated_by_label(label: str) -> dict[str, Any] | None:
    needle = (label or "").strip()
    if not needle:
        return None
    for item in list_generated_buttons(menu=None, refresh=False):
        labels = {
            str(item.get("label_fa") or "").strip(),
            str(item.get("label_en") or "").strip(),
        }
        if needle in labels:
            return item
    # refresh once in case registry changed after restart without cache clear
    for item in list_generated_buttons(menu=None, refresh=True):
        labels = {
            str(item.get("label_fa") or "").strip(),
            str(item.get("label_en") or "").strip(),
        }
        if needle in labels:
            return item
    return None


def all_generated_labels() -> set[str]:
    labels: set[str] = set()
    for item in list_generated_buttons(menu=None, refresh=False):
        for key in ("label_fa", "label_en"):
            val = str(item.get(key) or "").strip()
            if val:
                labels.add(val)
    return labels


def _load_module(module_name: str) -> ModuleType | None:
    if module_name in _cache_modules:
        return _cache_modules[module_name]
    if not re.fullmatch(r"btn_[a-zA-Z0-9_]+", module_name or ""):
        logger.warning("reject generated module name: %s", module_name)
        return None
    try:
        mod = importlib.import_module(f"src.generated.buttons.{module_name}")
    except Exception as exc:  # noqa: BLE001
        logger.exception("failed to import generated button %s: %s", module_name, exc)
        return None
    _cache_modules[module_name] = mod
    return mod


def preload_all() -> int:
    """Import all registered modules at startup (fail soft)."""
    n = 0
    for item in list_generated_buttons(menu=None, refresh=True):
        mod_name = str(item.get("module") or item.get("id") or "").strip()
        if _load_module(mod_name):
            n += 1
    return n


async def dispatch_generated(
    message,
    button: dict[str, Any],
    *,
    lang: str,
    settings,
    bot_settings,
) -> bool:
    mod_name = str(button.get("module") or button.get("id") or "").strip()
    mod = _load_module(mod_name)
    if mod is None:
        return False
    run = getattr(mod, "run", None)
    if not callable(run):
        return False
    await run(message, lang=lang, settings=settings, bot_settings=bot_settings)
    return True


def build_registry_json(buttons: list[dict[str, Any]]) -> str:
    payload = {"buttons": buttons}
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def current_registry_buttons() -> list[dict[str, Any]]:
    data = _read_registry()
    items = data.get("buttons") if isinstance(data.get("buttons"), list) else []
    return [dict(x) for x in items if isinstance(x, dict)]
