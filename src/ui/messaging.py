"""Helpers to answer with optional photo + caption (Telegram limit 1024)."""

from __future__ import annotations

from pathlib import Path

from aiogram.types import FSInputFile, Message, ReplyKeyboardMarkup

CAPTION_LIMIT = 1000


async def answer_with_media(
    message: Message,
    text: str,
    *,
    image: Path | None = None,
    images: list[Path] | None = None,
    reply_markup: ReplyKeyboardMarkup | None = None,
) -> None:
    """Send photo+caption when image exists; otherwise plain text.

    If caption would exceed Telegram limits, send photo then a separate text.
    Multiple images: first carries caption/text flow; extras are photos only.
    """
    body = (text or "").strip()
    paths: list[Path] = []
    for p in list(images or []) + ([image] if image is not None else []):
        if p is None:
            continue
        try:
            resolved = p if p.is_file() else None
        except OSError:
            resolved = None
        if resolved is None:
            continue
        key = str(resolved)
        if any(str(x) == key for x in paths):
            continue
        paths.append(resolved)

    if not paths:
        await message.answer(body or "…", reply_markup=reply_markup)
        return

    first, *rest = paths
    photo = FSInputFile(str(first))
    if len(body) <= CAPTION_LIMIT:
        await message.answer_photo(
            photo,
            caption=body or None,
            reply_markup=reply_markup if not rest else None,
        )
    else:
        await message.answer_photo(photo)
        await message.answer(body, reply_markup=reply_markup if not rest else None)

    for idx, extra in enumerate(rest):
        is_last = idx == len(rest) - 1
        await message.answer_photo(
            FSInputFile(str(extra)),
            reply_markup=reply_markup if is_last else None,
        )
