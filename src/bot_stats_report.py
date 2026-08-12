"""Build the admin-only Persian bot performance report."""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo

import jdatetime

from src.config import Settings
from src.conversation_analysis_job import TOPIC_RULES, _build_insights, _read_user_messages
from src.storage.metrics import MetricsStore

IRAN_TZ = ZoneInfo("Asia/Tehran")

TOPIC_TITLE_FA: dict[str, str] = {
    "ssh_connectivity": "مشکل اتصال SSH به سرور",
    "full_deploy": "خطا یا ابهام در Full Deploy",
    "exit_server": "افزودن Exit Server",
    "panel_3xui": "تنظیمات پنل 3X-UI",
    "license_activation": "فعال‌سازی License / Pro",
    "wireguard_link": "لینک اشتراک و WireGuard",
    "telegram_bot_usage": "استفاده از ربات تلگرام",
}

TOPIC_STATUS_FA: dict[str, str] = {
    "critical": "بحرانی — نیاز به اقدام فوری",
    "high": "بالا — در حال پیگیری",
    "medium": "متوسط — قابل مدیریت",
    "low": "کم — پایش ادامه دارد",
}


def _education_stats(settings: Settings) -> tuple[int, list[str], list[str]]:
    path = settings.data_dir / "convo_resolution_memory.json"
    if not path.is_file():
        return 0, [], []
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return 0, [], []
    items = raw.get("items") if isinstance(raw, dict) else []
    if not isinstance(items, list):
        return 0, [], []
    today = datetime.now(IRAN_TZ).strftime("%Y-%m-%d")
    topics: list[str] = []
    langs = {"fa", "en", "ru", "zh"}
    count = 0
    for item in items:
        if not isinstance(item, dict):
            continue
        at = str(item.get("at") or "")
        if not at.startswith(today):
            continue
        count += 1
        topic = str(item.get("topic") or "").strip()
        if topic:
            topics.append(TOPIC_TITLE_FA.get(topic, topic))
    # Memory stores one multilingual generation per topic; languages are fixed.
    return count, topics[:8], sorted(langs) if count else []


def _feature_request_hints(messages: list[tuple[str, str]]) -> list[str]:
    keywords = {
        "android": "قابلیت‌های Android",
        "اندروید": "قابلیت‌های Android",
        "mesh": "Mesh / توپولوژی",
        "مش": "Mesh / توپولوژی",
        "full deploy": "Full Deploy",
        "دیپلوی": "Full Deploy",
        "license": "License / فعال‌سازی",
        "لایسنس": "License / فعال‌سازی",
        "exit": "Exit Server",
        "خروجی": "Exit Server",
        "cdn": "Domain / CDN",
        "دامنه": "Domain / CDN",
    }
    hits: Counter[str] = Counter()
    for _, text in messages:
        n = " ".join((text or "").lower().split())
        for key, label in keywords.items():
            if key in n:
                hits[label] += 1
    return [name for name, _ in hits.most_common(4)]


def _catalog_gaps(insights_topics: list[str]) -> list[str]:
    mapping = {
        "ssh_connectivity": "سوال‌های رایج خطای SSH و احراز هویت",
        "full_deploy": "چک‌لیست پیش‌نیاز Full Deploy",
        "exit_server": "تفاوت Add Exit Server با Central Full Deploy",
        "panel_3xui": "تنظیم inbound/outbound و پورت ۴۴۳",
        "license_activation": "تفاوت Basic / Pro / AI Pro و فعال‌سازی",
        "wireguard_link": "ساخت و تست لینک اشتراک / QR",
        "telegram_bot_usage": "نحوه استفاده از منو و Ask AI",
    }
    out: list[str] = []
    for topic in insights_topics:
        label = mapping.get(topic)
        if label and label not in out:
            out.append(label)
    return out[:4]


async def build_bot_stats_report(settings: Settings, metrics: MetricsStore) -> str:
    snap = await metrics.snapshot()
    now = datetime.now(IRAN_TZ)
    shamsi = jdatetime.datetime.fromgregorian(datetime=now).strftime("%Y/%m/%d - %H:%M")

    spent_today = float(snap["spend_usd"])
    lifetime = float(snap["lifetime_spend_usd"])
    remaining = max(0.0, float(settings.ai_budget_usd) - lifetime)

    messages = _read_user_messages(settings.users_db_path)
    insights = _build_insights(messages)[:2]
    edu_count, edu_topics, edu_langs = _education_stats(settings)

    answered = int(snap["answered"])
    solved = int(snap["ai_solved"])
    success_pct = int(round((solved / answered) * 100)) if answered else 0

    needs_review = [
        TOPIC_TITLE_FA.get(i.topic, i.topic)
        for i in insights
        if i.severity in {"critical", "high"}
    ]
    if not needs_review and insights:
        needs_review = [TOPIC_TITLE_FA.get(insights[0].topic, insights[0].topic)]

    feature_hints = _feature_request_hints(messages)
    catalog_gaps = _catalog_gaps([i.topic for i in insights] or list(TOPIC_RULES.keys())[:2])

    lines: list[str] = [
        "📊 گزارش عملکرد AI",
        "",
        f"📅 تاریخ: {shamsi}",
        "",
        "### Ai Token",
        f"میزان مصرف‌شده از حجم توکن AI امروز: ${spent_today:.4f}",
        f"میزان مصرف‌شده تجمعی: ${lifetime:.4f}",
        f"میزان باقی‌مانده از بودجه توکن: ${remaining:.4f}",
        f"نام ایجنت AI: {settings.ai_model}",
        "",
        "## کاربران:",
        f"- تعداد کاربران جدید: {snap['new_users']}",
        f"- تعداد مکالمات انجام‌شده: {snap['conversations']}",
        f"- تعداد سوالات پاسخ‌داده‌شده: {snap['answered']}",
        f"- تعداد موارد ارجاع‌داده‌شده به پشتیبانی: {snap['support_referrals']}",
        "",
        "## مشکلات کاربران:",
        "",
        "بیشترین مشکلات امروز:",
        "",
    ]

    if not insights:
        lines.extend(
            [
                "1.",
                "نام مشکل: دادهٔ کافی برای شناسایی مشکل پرتکرار ثبت نشده است",
                "تعداد تکرار: 0",
                "تعداد کاربران: 0",
                "وضعیت: پایش ادامه دارد",
                "",
            ]
        )
    else:
        for idx, item in enumerate(insights, start=1):
            lines.extend(
                [
                    f"{idx}.",
                    f"نام مشکل: {TOPIC_TITLE_FA.get(item.topic, item.topic)}",
                    f"تعداد تکرار: {item.occurrences}",
                    f"تعداد کاربران: {item.users}",
                    f"وضعیت: {TOPIC_STATUS_FA.get(item.severity, item.severity)}",
                    "",
                ]
            )

    lines.extend(
        [
            "## آموزش‌های تولیدشده:",
            f"- تعداد آموزش‌های ایجادشده: {edu_count}",
            f"- موضوع آموزش‌ها: {('، '.join(edu_topics) if edu_topics else 'هنوز آموزشی ثبت نشده است')}",
            f"- زبان‌های تولیدشده: {('، '.join(edu_langs) if edu_langs else '-')}",
            "",
            "## عملکرد حل مشکل:",
            f"- تعداد مشکلات حل‌شده توسط AI: {solved}",
            f"- درصد تقریبی موفقیت: {success_pct}%",
            f"- مشکلاتی که نیاز به بررسی بیشتر دارند: {('؛ '.join(needs_review) if needs_review else 'مورد بحرانی ثبت نشده است')}",
            "",
            "## پیشنهادات AI:",
            "",
            "بر اساس تحلیل کاربران پیشنهاد می‌شود:",
            "",
            f"- چه آموزشی ساخته شود؟ {(edu_topics[0] if edu_topics else (TOPIC_TITLE_FA.get(insights[0].topic, insights[0].topic) if insights else 'آموزش شروع کار با Ask AI و مسیرهای اصلی'))}",
            f"- چه بخشی از برنامه نیاز به بهبود دارد؟ {(TOPIC_TITLE_FA.get(insights[0].topic, insights[0].topic) if insights else 'پایداری پاسخ‌گویی و مسیر ارجاع به پشتیبانی')}",
            f"- چه سوالاتی باید به کاتالوگ اضافه شود؟ {(('؛ '.join(catalog_gaps)) if catalog_gaps else 'سوالات پرتکرار نصب، لایسنس و اتصال')}",
            f"- چه قابلیت‌هایی بیشتر درخواست شده‌اند؟ {(('؛ '.join(feature_hints)) if feature_hints else 'هنوز الگوی درخواست قابلیت به‌اندازه کافی تکرار نشده است')}",
        ]
    )
    return "\n".join(lines)
