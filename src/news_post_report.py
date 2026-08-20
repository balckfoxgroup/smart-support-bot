"""Admin report: why social news posts were sent or skipped (last 3 days)."""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

from src.config import Settings
from src.social_news_attempts import load_news_attempts
from src.storage.bot_settings import BotSettingsStore

IRAN_TZ = ZoneInfo("Asia/Tehran")

_REASON_FA = {
    "published": "ارسال شد",
    "nothing publishable": "خبر قابل‌انتشار پیدا نشد (فیلتر کیفیت/منبع یا تکراری)",
    "slot disabled or no chat": "اسلات خبر خاموش است یا مقصد تنظیم نشده",
    "news slot disabled or no destination": "اسلات خبر خاموش است یا مقصد تنظیم نشده",
}


def _reason_fa(raw: str) -> str:
    text = (raw or "").strip()
    if not text:
        return "علت ثبت نشده"
    low = text.lower()
    for key, fa in _REASON_FA.items():
        if key in low or low == key:
            return fa
    if low.startswith("http"):
        return f"ارسال شد — {text[:120]}"
    if "fail" in low or "error" in low or "exception" in low:
        return f"خطای ارسال: {text[:180]}"
    return text[:220]


def _fmt_iran(ts_raw: str) -> str:
    try:
        dt = datetime.fromisoformat(str(ts_raw).replace("Z", "+00:00"))
        return dt.astimezone(IRAN_TZ).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return "—"


async def build_news_post_report(
    settings: Settings,
    bot_settings: BotSettingsStore | None = None,
    *,
    lang: str = "fa",
    days: int = 3,
) -> str:
    fa = (lang or "").startswith("fa")
    rows = load_news_attempts(settings.data_dir, days=days)
    times = settings.social_news_times
    chat = settings.social_news_chat_id
    if bot_settings is not None:
        times = await bot_settings.effective_social_times(settings)
        chat = await bot_settings.effective_social_chat_id(settings)

    if fa:
        lines = [
            "📋 گزارش پست خبری",
            f"بازه: {days} روز اخیر (ساعت ایران)",
            f"زمان‌بندی: {times or '—'}",
            f"مقصد: {chat or '—'}",
            "",
        ]
    else:
        lines = [
            "📋 News Post Report",
            f"Window: last {days} days (Iran time)",
            f"Schedule: {times or '—'}",
            f"Target: {chat or '—'}",
            "",
        ]

    if not rows:
        lines.append(
            "در این بازه تلاشی ثبت نشده."
            if fa
            else "No attempts recorded in this window."
        )
        return "\n".join(lines)

    for row in rows:
        when = _fmt_iran(str(row.get("ts") or ""))
        ok = bool(row.get("ok"))
        mark = "✅" if ok else "❌"
        reason = _reason_fa(str(row.get("reason") or ""))
        title = str(row.get("title") or "").strip()
        target = str(row.get("target") or "").strip()
        source = str(row.get("source") or "").strip()
        link = str(row.get("link") or "").strip()
        if fa:
            block = [f"{mark} {when}", f"علت: {reason}"]
            if title:
                block.append(f"عنوان: {title[:120]}")
            if source:
                block.append(f"منبع: {source[:80]}")
            if target:
                block.append(f"مقصد: {target}")
            if ok and link:
                block.append(f"لینک: {link[:160]}")
        else:
            block = [f"{mark} {when}", f"Reason: {reason}"]
            if title:
                block.append(f"Title: {title[:120]}")
            if source:
                block.append(f"Source: {source[:80]}")
            if target:
                block.append(f"Target: {target}")
            if ok and link:
                block.append(f"Link: {link[:160]}")
        lines.append("\n".join(block))
        lines.append("")

    return "\n".join(lines).strip()
