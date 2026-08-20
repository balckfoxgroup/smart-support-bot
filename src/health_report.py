"""Build admin health / status report text."""

from __future__ import annotations

import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from src.config import Settings
from src.job_status import read_job_status
from src.safety.state import heartbeat_age_seconds, read_heartbeat
from src.storage.bot_settings import BotSettingsStore

IRAN_TZ = ZoneInfo("Asia/Tehran")


def _ago(ts: float | None, lang: str) -> str:
    if not ts:
        return "—" if lang != "fa" else "—"
    age = max(0, int(time.time() - float(ts)))
    if age < 60:
        return f"{age}s" if lang != "fa" else f"{age} ثانیه پیش"
    if age < 3600:
        m = age // 60
        return f"{m}m" if lang != "fa" else f"{m} دقیقه پیش"
    h = age // 3600
    return f"{h}h" if lang != "fa" else f"{h} ساعت پیش"


def _job_line(data: dict[str, Any], key: str, title_fa: str, title_en: str, lang: str) -> str:
    row = data.get(key) if isinstance(data.get(key), dict) else None
    title = title_fa if lang == "fa" else title_en
    if not row:
        return f"• {title}: {'هنوز اجرا نشده' if lang == 'fa' else 'not run yet'}"
    ok = bool(row.get("ok"))
    mark = "✅" if ok else "❌"
    when = _ago(row.get("ts"), lang)
    detail = str(row.get("detail") or "").strip()
    extra = f" — {detail}" if detail else ""
    return f"• {title}: {mark} ({when}){extra}"


async def build_health_report(
    settings: Settings,
    bot_settings: BotSettingsStore,
    *,
    lang: str = "fa",
) -> str:
    fa = (lang or "").startswith("fa")
    now = datetime.now(IRAN_TZ).strftime("%Y-%m-%d %H:%M")
    age = heartbeat_age_seconds()
    hb = read_heartbeat() or {}
    if age is None:
        hb_line = "ربات: ❌ بدون heartbeat" if fa else "Bot: ❌ no heartbeat"
    elif age <= 45:
        hb_line = f"ربات: ✅ آنلاین (heartbeat {_ago(time.time() - age, lang)})" if fa else f"Bot: ✅ online (heartbeat {_ago(time.time() - age, lang)})"
    elif age <= 180:
        hb_line = f"ربات: ⚠️ کند (heartbeat قدیمی {_ago(time.time() - age, lang)})" if fa else f"Bot: ⚠️ slow (stale heartbeat {_ago(time.time() - age, lang)})"
    else:
        hb_line = f"ربات: ❌ احتمالاً آفلاین (heartbeat {_ago(time.time() - age, lang)})" if fa else f"Bot: ❌ likely offline (heartbeat {_ago(time.time() - age, lang)})"

    jobs = read_job_status(settings.data_dir)
    health_cfg = await bot_settings.get_health_settings()
    lines = [
        "🩺 وضعیت سلامت ربات" if fa else "🩺 Bot Health Status",
        f"{'زمان ایران' if fa else 'Iran time'}: {now}",
        "",
        hb_line,
        f"{'PID'}: {hb.get('pid', '—')}",
        "",
        "جاب‌ها:" if fa else "Jobs:",
        _job_line(jobs, "social_news", "خبر / Social", "News / Social", "fa" if fa else "en"),
        _job_line(jobs, "nightly_config", "کانفیگ شبانه", "Nightly config", "fa" if fa else "en"),
        _job_line(jobs, "convo_analysis", "تحلیل مکالمه", "Conversation analysis", "fa" if fa else "en"),
        _job_line(jobs, "health_report", "گزارش سلامت", "Health report", "fa" if fa else "en"),
        "",
    ]
    if fa:
        lines.append(
            f"گزارش روزانه: {'فعال' if health_cfg.get('enabled') else 'خاموش'} "
            f"({health_cfg.get('times') or '09:00'})"
        )
    else:
        lines.append(
            f"Daily report: {'on' if health_cfg.get('enabled') else 'off'} "
            f"({health_cfg.get('times') or '09:00'})"
        )
    return "\n".join(lines)
