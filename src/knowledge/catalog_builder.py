"""Build product_catalogs/*.json from a folder path or staged uploads via AI."""

from __future__ import annotations

import json
import logging
import re
import shutil
import zipfile
from pathlib import Path
from typing import Any, Awaitable, Callable

logger = logging.getLogger(__name__)

TEXT_EXTS = {".txt", ".md", ".json", ".csv", ".html"}
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

AiChat = Callable[[list[dict[str, str]]], Awaitable[str]]


def catalog_inbox_dir(knowledge_root: Path) -> Path:
    return knowledge_root / "catalog_inbox"


def product_catalogs_dir(knowledge_root: Path) -> Path:
    return knowledge_root / "product_catalogs"


def media_catalogs_dir(project_root: Path) -> Path:
    return project_root / "media" / "catalogs"


def _load_build_prompt(inbox: Path) -> str:
    path = inbox / "_build_prompt.txt"
    if path.is_file():
        return path.read_text(encoding="utf-8")
    return (
        "Build a product catalog JSON. Output ONLY valid JSON with schema_version 1, "
        "product_id, title/short_summary/long_summary/features in fa/en/ru/zh."
    )


def _folder_payload(folder: Path) -> str:
    parts: list[str] = [f"Folder name (product_id hint): {folder.name}"]
    media_names: list[str] = []
    for path in sorted(folder.rglob("*")):
        if not path.is_file():
            continue
        if path.name.startswith("_"):
            continue
        suf = path.suffix.lower()
        rel = str(path.relative_to(folder))
        if suf in TEXT_EXTS:
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if len(text) > 8000:
                text = text[:8000] + "\n…"
            parts.append(f"\n### FILE {rel}\n{text}")
        elif suf in IMAGE_EXTS:
            media_names.append(rel)
        else:
            parts.append(f"\n### FILE {rel} (binary/other, name only)")
    if media_names:
        parts.append("\n### MEDIA FILES\n" + "\n".join(f"- {n}" for n in media_names))
    return "\n".join(parts)


def _extract_json(text: str) -> dict[str, Any] | None:
    raw = (text or "").strip()
    if not raw:
        return None
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    try:
        data = json.loads(raw)
        return data if isinstance(data, dict) else None
    except json.JSONDecodeError:
        m = re.search(r"\{[\s\S]*\}", raw)
        if not m:
            return None
        try:
            data = json.loads(m.group(0))
            return data if isinstance(data, dict) else None
        except json.JSONDecodeError:
            return None


def list_inbox_products(knowledge_root: Path) -> list[Path]:
    inbox = catalog_inbox_dir(knowledge_root)
    if not inbox.is_dir():
        return []
    return [
        p
        for p in sorted(inbox.iterdir())
        if p.is_dir() and not p.name.startswith("_") and not p.name.startswith(".")
    ]


def prepare_work_folder(
    *,
    knowledge_root: Path,
    folder_path: str | None = None,
    staging_dir: Path | None = None,
    product_hint: str = "product",
) -> Path:
    """
    Resolve a readable product folder:
    - absolute/relative path on the bot host, or
    - staging_dir filled by Telegram uploads (may contain zip).
    Copies into catalog_inbox/<product_id>/ as the server copy.
    """
    inbox = catalog_inbox_dir(knowledge_root)
    inbox.mkdir(parents=True, exist_ok=True)

    source: Path | None = None
    if folder_path:
        candidate = Path(folder_path).expanduser()
        if not candidate.is_absolute():
            candidate = (knowledge_root.parent / candidate).resolve()
        if candidate.is_dir():
            source = candidate
        elif candidate.is_file() and candidate.suffix.lower() == ".zip":
            staging = inbox / "_staging_zip"
            if staging.exists():
                shutil.rmtree(staging, ignore_errors=True)
            staging.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(candidate, "r") as zf:
                zf.extractall(staging)
            source = staging
        else:
            raise FileNotFoundError(f"Folder not found: {folder_path}")

    if source is None and staging_dir is not None and staging_dir.is_dir():
        # Expand any zip inside staging
        for zpath in list(staging_dir.glob("*.zip")):
            with zipfile.ZipFile(zpath, "r") as zf:
                zf.extractall(staging_dir)
        source = staging_dir

    if source is None:
        raise FileNotFoundError("No folder path or uploaded files provided")

    product_id = re.sub(r"[^a-zA-Z0-9_-]+", "-", product_hint or source.name).strip("-").lower() or "product"
    dest = inbox / product_id
    if dest.exists():
        shutil.rmtree(dest, ignore_errors=True)
    shutil.copytree(source, dest, dirs_exist_ok=True)
    return dest


def copy_media_to_server(folder: Path, *, project_root: Path, product_id: str) -> list[str]:
    """Copy images from folder into media/catalogs/<product_id>/; return relative paths."""
    out_dir = media_catalogs_dir(project_root) / product_id
    out_dir.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for path in sorted(folder.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in IMAGE_EXTS:
            continue
        target = out_dir / path.name
        shutil.copy2(path, target)
        rel = f"media/catalogs/{product_id}/{path.name}"
        copied.append(rel)
    return copied


async def build_one_catalog(
    folder: Path,
    ai_chat: AiChat,
    *,
    knowledge_root: Path,
    project_root: Path,
    extra_sources: str = "",
    reload_fn=None,
) -> str:
    inbox = catalog_inbox_dir(knowledge_root)
    out_dir = product_catalogs_dir(knowledge_root)
    out_dir.mkdir(parents=True, exist_ok=True)
    prompt = _load_build_prompt(inbox)
    payload = _folder_payload(folder)
    if extra_sources.strip():
        payload += "\n\n### OWNER SELECTED SOURCES\n" + extra_sources.strip()
    if len(payload) < 40:
        raise ValueError(f"Folder too empty: {folder}")

    answer = await ai_chat(
        [
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": "Analyze these product materials and produce the catalog JSON.\n\n" + payload,
            },
        ]
    )
    data = _extract_json(answer)
    if not data:
        raise ValueError("AI did not return valid catalog JSON")

    product_id = str(data.get("product_id") or folder.name).strip().lower().replace(" ", "-")
    data["product_id"] = product_id
    data.setdefault("enabled", True)
    data.setdefault("catalog_id", f"user-{product_id}")
    data.setdefault("menu_emoji", "📦")
    data.setdefault("menu_order", 50)

    media_paths = copy_media_to_server(folder, project_root=project_root, product_id=product_id)
    if media_paths:
        data["media"] = [
            {
                "role": "screenshot" if i else "hero",
                "slot": f"{product_id}-{i}",
                "path": p,
                "local_folder": f"media/catalogs/{product_id}",
                "note": "copied from catalog inbox",
            }
            for i, p in enumerate(media_paths)
        ]
    else:
        data.setdefault(
            "media",
            [
                {
                    "role": "hero",
                    "slot": f"{product_id}-hero",
                    "path": "",
                    "local_folder": f"media/catalogs/{product_id}",
                    "note": "no photos in folder",
                }
            ],
        )

    path = out_dir / f"{product_id}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    # Keep a copy inside the inbox folder too
    (folder / f"{product_id}.catalog.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if reload_fn is not None:
        reload_fn()
    logger.info("Wrote catalog %s (+ %s media)", path, len(media_paths))
    return product_id


async def build_catalogs_from_inbox(
    knowledge_root: Path,
    ai_chat: AiChat,
    *,
    reload_fn=None,
    project_root: Path | None = None,
    extra_sources: str = "",
) -> list[str]:
    root = project_root or knowledge_root.parent
    written: list[str] = []
    for folder in list_inbox_products(knowledge_root):
        try:
            pid = await build_one_catalog(
                folder,
                ai_chat,
                knowledge_root=knowledge_root,
                project_root=root,
                extra_sources=extra_sources,
                reload_fn=None,
            )
            written.append(pid)
        except Exception as exc:  # noqa: BLE001
            logger.exception("catalog build failed for %s: %s", folder.name, exc)
    if written and reload_fn is not None:
        reload_fn()
    return written
