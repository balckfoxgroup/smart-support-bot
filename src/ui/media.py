"""Menu / topic media paths for Telegram photo replies."""

from __future__ import annotations

from pathlib import Path

from src.config import PROJECT_ROOT

MEDIA_DIR = PROJECT_ROOT / "media" / "menu"

# action -> filename (about uses about_{lang}.jpg)
_ACTION_FILE: dict[str, str] = {
    "ask_ai": "ask_ai.jpg",
    "install": "install.png",
    "license": "license.png",
    "connection": "connection.png",
    "update": "update.png",
    "server": "server.png",
    "buy_license": "buy_license.png",
    "buy_vps": "buy_vps.jpg",
    "contact": "welcome.png",
    "lang": "lang.jpg",
    "home": "home.png",
}


def menu_image_path(action: str, lang: str = "en") -> Path | None:
    """Return a local image path for a menu action, if present."""
    if action == "about":
        candidate = MEDIA_DIR / f"about_{lang}.jpg"
        if candidate.is_file():
            return candidate
        fallback = MEDIA_DIR / "about_en.jpg"
        return fallback if fallback.is_file() else None

    name = _ACTION_FILE.get(action)
    if not name:
        return None
    path = MEDIA_DIR / name
    return path if path.is_file() else None


def language_picker_image(lang_hint: str = "en") -> Path | None:
    """Welcome logo first; fallback to localized hero."""
    welcome = MEDIA_DIR / "welcome.png"
    if welcome.is_file():
        return welcome
    return menu_image_path("about", lang_hint) or menu_image_path("lang", lang_hint)


def welcome_image() -> Path | None:
    """Brand image for pre-start /start greeting."""
    for name in ("welcome.png", "group_avatar.jpg"):
        path = MEDIA_DIR / name
        if path.is_file():
            return path
    return None
