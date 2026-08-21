"""Reload in-memory knowledge after catalog / product files change."""

from __future__ import annotations

import logging
from collections.abc import Callable

logger = logging.getLogger(__name__)

_hooks: list[Callable[[], None]] = []


def register_knowledge_reload(fn: Callable[[], None]) -> None:
    if fn not in _hooks:
        _hooks.append(fn)


def notify_knowledge_changed() -> None:
    """Tell the running bot to refresh catalogs, FAQ index, and intents."""
    for fn in list(_hooks):
        try:
            fn()
        except Exception:  # noqa: BLE001
            logger.exception("knowledge reload hook failed")
