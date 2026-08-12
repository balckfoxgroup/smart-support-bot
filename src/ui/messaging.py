"""Helpers to answer with optional photo + caption (Telegram limit 1024)."""

from __future__ import annotations

from pathlib import Path

from aiogram.types import FSInputFile, Message, ReplyKeyboardMarkup

CAPTION_LIMIT = 1000


async def answer_with_media(
    message: Message,
    text: str,
    *,
    image: Path | None,
    reply_markup: ReplyKeyboardMarkup | None = None,
) -> None:
    """Send photo+caption when image exists; otherwise plain text.

    If caption would exceed Telegram limits, send photo then a separate text.
    """
    body = (text or "").strip()
    if image is not None and image.is_file():
        photo = FSInputFile(str(image))
        if len(body) <= CAPTION_LIMIT:
            await message.answer_photo(
                photo,
                caption=body or None,
                reply_markup=reply_markup,
            )
            return
        await message.answer_photo(photo)
        await message.answer(body, reply_markup=reply_markup)
        return

    await message.answer(body or "…", reply_markup=reply_markup)
