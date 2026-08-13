"""AI codegen for admin buttons, validated and applied via safe-change watchdog."""

from __future__ import annotations

import ast
import logging
import re
import secrets
from typing import Any

from src.generated.buttons import (
    build_registry_json,
    current_registry_buttons,
)
from src.safety.api import request_safe_change

logger = logging.getLogger(__name__)

_ALLOWED_IMPORT_ROOTS = frozenset(
    {
        "asyncio",
        "json",
        "logging",
        "re",
        "math",
        "datetime",
        "typing",
        "dataclasses",
        "collections",
        "functools",
        "itertools",
        "aiogram",
        "src",
    }
)

_FORBIDDEN_NAMES = frozenset(
    {
        "eval",
        "exec",
        "compile",
        "__import__",
        "open",
        "input",
        "breakpoint",
        "exit",
        "quit",
        "os",
        "sys",
        "subprocess",
        "socket",
        "pathlib",
        "shutil",
        "pickle",
        "ctypes",
        "multiprocessing",
        "importlib",
    }
)

_MAX_SOURCE_CHARS = 12_000


def new_generated_id() -> str:
    return "btn_" + secrets.token_hex(3)


def extract_python_block(text: str) -> str:
    raw = (text or "").strip()
    if not raw:
        return ""
    fence = re.search(r"```(?:python)?\s*([\s\S]*?)```", raw, flags=re.IGNORECASE)
    if fence:
        return fence.group(1).strip()
    # If model returned bare code
    if "async def run(" in raw or "def run(" in raw:
        return raw
    return ""


def validate_generated_button_source(source: str, *, button_id: str) -> tuple[bool, str]:
    src = (source or "").strip()
    if not src:
        return False, "empty source"
    if len(src) > _MAX_SOURCE_CHARS:
        return False, "source too large"
    try:
        tree = ast.parse(src)
    except SyntaxError as exc:
        return False, f"syntax error: {exc}"

    has_run = False
    for node in tree.body:
        if isinstance(node, (ast.AsyncFunctionDef, ast.FunctionDef)) and node.name == "run":
            has_run = True
            break
    if not has_run:
        return False, "missing async def run(...)"

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names: list[str] = []
            if isinstance(node, ast.Import):
                names = [a.name.split(".")[0] for a in node.names]
            else:
                mod = (node.module or "").split(".")[0] if node.module else ""
                if mod:
                    names = [mod]
                # relative imports not allowed
                if getattr(node, "level", 0):
                    return False, "relative imports are not allowed"
            for name in names:
                if name not in _ALLOWED_IMPORT_ROOTS:
                    return False, f"import not allowed: {name}"
        if isinstance(node, ast.Name) and node.id in _FORBIDDEN_NAMES:
            return False, f"forbidden name: {node.id}"
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            if node.value.id in {"os", "sys", "subprocess"}:
                return False, f"forbidden attribute root: {node.value.id}"
        if isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Name) and fn.id in _FORBIDDEN_NAMES:
                return False, f"forbidden call: {fn.id}"

    # Soft contract checks
    if "LABEL_FA" not in src and "label_fa" not in src.lower():
        # allow if BUTTON_ID present; labels come from registry
        pass
    if button_id and f'BUTTON_ID = "{button_id}"' not in src and f"BUTTON_ID = '{button_id}'" not in src:
        # inject later if missing
        pass
    return True, "ok"


def ensure_button_constants(source: str, *, button_id: str, label_fa: str, label_en: str) -> str:
    src = source.strip() + "\n"
    if "BUTTON_ID" not in src:
        src = f'BUTTON_ID = "{button_id}"\n' + src
    if "LABEL_FA" not in src:
        src = f'LABEL_FA = {label_fa!r}\n' + src
    if "LABEL_EN" not in src:
        src = f'LABEL_EN = {label_en!r}\n' + src
    return src


def codegen_system_prompt() -> str:
    return (
        "You write ONE Python module for a Smart Support Bot admin settings button.\n"
        "Return ONLY a python code block.\n"
        "Contract:\n"
        "- Define BUTTON_ID, LABEL_FA, LABEL_EN constants.\n"
        "- Define: async def run(message, *, lang, settings, bot_settings):\n"
        "- You may import from: aiogram, asyncio, json, logging, re, datetime, typing,\n"
        "  src.health_report, src.storage.bot_settings, src.ui.admin_keyboards, src.branding.\n"
        "- Forbidden: os, sys, subprocess, eval, exec, open, socket, pathlib write, network scrape,\n"
        "  reading .env, changing creator contact, deleting files.\n"
        "- Keep it short and useful. Reply to the admin with message.answer(...).\n"
        "- Persian UI text must start sentences with Persian words when lang is fa.\n"
    )


def build_codegen_user_prompt(
    *,
    admin_request: str,
    button_id: str,
    label_fa: str,
    label_en: str,
    lang: str,
) -> str:
    return (
        f"Admin language: {lang}\n"
        f"BUTTON_ID must be: {button_id}\n"
        f"LABEL_FA must be: {label_fa}\n"
        f"LABEL_EN must be: {label_en}\n"
        f"Admin wants this button to do:\n{admin_request}\n"
    )


def queue_generated_button_add(
    *,
    button_id: str,
    label_fa: str,
    label_en: str,
    source: str,
    description: str,
    menu: str = "settings",
    order: int = 50,
    admin_chat_id: str | int | None = None,
) -> dict[str, Any]:
    ok, detail = validate_generated_button_source(source, button_id=button_id)
    if not ok:
        return {"ok": False, "error": detail}
    source = ensure_button_constants(
        source, button_id=button_id, label_fa=label_fa, label_en=label_en
    )
    ok, detail = validate_generated_button_source(source, button_id=button_id)
    if not ok:
        return {"ok": False, "error": detail}

    buttons = current_registry_buttons()
    # replace same id/labels
    kept: list[dict[str, Any]] = []
    for item in buttons:
        if str(item.get("id") or "") == button_id:
            continue
        labs = {str(item.get("label_fa") or "").strip(), str(item.get("label_en") or "").strip()}
        if label_fa in labs or label_en in labs:
            continue
        kept.append(item)
    kept.append(
        {
            "id": button_id,
            "module": button_id,
            "menu": menu or "settings",
            "label_fa": label_fa,
            "label_en": label_en or label_fa,
            "enabled": True,
            "order": int(order),
            "kind": "generated",
        }
    )
    files = {
        f"src/generated/buttons/{button_id}.py": source if source.endswith("\n") else source + "\n",
        "src/generated/buttons/registry.json": build_registry_json(kept),
        "src/generated/buttons/__init__.py": _loader_source(),
        "src/generated/__init__.py": '"""Package marker for AI-generated safe-change modules."""\n',
    }

    return request_safe_change(
        description=description or f"Add generated button {button_id}",
        files=files,
        admin_chat_id=admin_chat_id,
        observe_seconds=60,
        confirm_seconds=30,
    )


def queue_generated_button_remove(
    *,
    button_id: str = "",
    label: str = "",
    description: str = "",
    admin_chat_id: str | int | None = None,
) -> dict[str, Any]:
    buttons = current_registry_buttons()
    bid = (button_id or "").strip()
    lab = (label or "").strip()
    kept: list[dict[str, Any]] = []
    removed: dict[str, Any] | None = None
    for item in buttons:
        hit = False
        if bid and str(item.get("id") or "") == bid:
            hit = True
        labs = {str(item.get("label_fa") or "").strip(), str(item.get("label_en") or "").strip()}
        if lab and lab in labs:
            hit = True
        if hit and removed is None:
            removed = item
            continue
        kept.append(item)
    if removed is None:
        return {"ok": False, "error": "generated button not found"}
    rid = str(removed.get("id") or "")
    # Keep module file as a disabled stub so path stays valid; registry drives visibility.
    stub = (
        f'BUTTON_ID = "{rid}"\n'
        f'LABEL_FA = {str(removed.get("label_fa") or "")!r}\n'
        f'LABEL_EN = {str(removed.get("label_en") or "")!r}\n'
        "ENABLED = False\n\n"
        "async def run(message, *, lang, settings, bot_settings):\n"
        "    await message.answer('این کلید حذف شده است.' if str(lang).startswith('fa') "
        "else 'This button was removed.')\n"
    )
    files = {
        "src/generated/buttons/registry.json": build_registry_json(kept),
        f"src/generated/buttons/{rid}.py": stub,
        "src/generated/buttons/__init__.py": _loader_source(),
    }
    return request_safe_change(
        description=description or f"Remove generated button {rid}",
        files=files,
        admin_chat_id=admin_chat_id,
        observe_seconds=60,
        confirm_seconds=30,
    )


def _loader_source() -> str:
    path = (
        __import__("pathlib").Path(__file__).resolve().parent
        / "generated"
        / "buttons"
        / "__init__.py"
    )
    return path.read_text(encoding="utf-8")


def guess_labels_from_request(text: str) -> tuple[str, str]:
    """Best-effort label extraction from admin free text."""
    chunk = text
    for cue in (
        "کلید بساز",
        "دکمه بساز",
        "اضافه کردن کلید",
        "add button",
        "create button",
    ):
        if cue in chunk:
            chunk = chunk.split(cue, 1)[-1].strip(" :-")
            break
    # drop action= tokens for label
    parts = []
    for part in chunk.replace("—", " ").split():
        if "=" in part:
            continue
        parts.append(part)
    label = " ".join(parts).strip().strip("\"'«»")
    if not label:
        label = "کلید سفارشی"
    if len(label) > 40:
        label = label[:40].rstrip()
    return label, label
