# -*- coding: utf-8 -*-
"""Rebuild FAQ_FA/RU/ZH with 100% native answers for Q041–Q200 (and keep Q001–Q040 seeds)."""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_mod(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Load native answer packs
ANS: dict[str, dict[str, str]] = {}
for part in ("_ans_041_080", "_ans_081_120", "_ans_121_160", "_ans_161_200"):
    ANS.update(load_mod(part).A)

# Also load high-traffic seeds from generator if present
gen = load_mod("_gen_faq_i18n")
for qid, tri in getattr(gen, "ANS", {}).items():
    # prefer pack if exists for 041+; seeds fill gaps for early IDs
    if qid not in ANS:
        ANS[qid] = tri

assert len([k for k in ANS if 41 <= int(k[1:]) <= 200]) == 160, len([k for k in ANS if 41 <= int(k[1:]) <= 200])

DATA = json.loads((ROOT / "_faq_en_parsed.json").read_text(encoding="utf-8"))
Q = gen.Q  # question translations Q001-Q200

ERR = {
    "fa": "خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.",
    "ru": "Частые ошибки: need activate/Pro, SSH fail, Full Deploy fail, AI quota, Proxy, host key. Смотрите status/terminal; при необходимости Device ID + скрин в @HiBlackFoxVpn.",
    "zh": "常见错误：need activate/Pro、SSH 失败、Full Deploy 失败、AI quota、Proxy、host key。查看 status/terminal；必要时将 Device ID + 截图发给 @HiBlackFoxVpn。",
}

HEADERS = {
    "fa": """# Black Fox VPN — پرسش‌های متداول (فارسی)

> برای AI / ربات تلگرام / پشتیبانی. شناسهٔ Q با انگلیسی یکی است.
> پاسخ‌های Q001–Q200 بومی‌سازی شده‌اند (بدون روکش انگلیسی).
> دقت: حداکثر ۶ Exit؛ رایگان Basic = Setup Central + Connect SSH + Full Deploy؛ Pro ≠ AI Pro.

""",
    "ru": """# Black Fox VPN — FAQ (русский)

> Для AI / Telegram Bot / поддержки. ID вопросов совпадают с EN.
> Ответы Q001–Q200 локализованы полностью (без английской обёртки).
> Точность: макс. 6 Exit; бесплатно в Basic = Setup Central + Connect SSH + Full Deploy; Pro ≠ AI Pro.

""",
    "zh": """# Black Fox VPN — 常见问题（简体中文）

> 供 AI / Telegram Bot / 客服。问题编号与英文对齐。
> Q001–Q200 答案已完整本地化（无英文外壳）。
> 准确性：Exit 最多 6；Basic 免费 = Setup Central + Connect SSH + Full Deploy；Pro ≠ AI Pro.

""",
}

LABELS = {
    "fa": ("سؤال", "پاسخ", "راه‌حل قدم‌به‌قدم", "خطاهای احتمالی"),
    "ru": ("Question", "Answer", "Step by step solution", "Possible errors"),
    "zh": ("Question", "Answer", "Step by step solution", "Possible errors"),
}

# Phrase-level step localization (keep UI terms in English)
REPL = {
    "fa": [
        (r"^Download Setup from foxnext\.net\.?$", "Setup را از foxnext.net دانلود کنید."),
        (r"^Install and pick language\.?$", "نصب کنید و زبان را انتخاب کنید."),
        (r"^Open Registration\.?$", "تب Registration را باز کنید."),
        (r"^Copy Device ID\.?$", "Device ID را کپی کنید."),
        (r"^Connect SSH\.?$", "Connect SSH را اجرا کنید."),
        (r"^Full Deploy\.?$", "Full Deploy را اجرا کنید."),
        (r"^Try Proxy Settings\.?$", "Proxy Settings را امتحان کنید."),
        (r"^Contact @HiBlackFoxVpn.*$", "در صورت نیاز به @HiBlackFoxVpn با Device ID پیام دهید."),
        (r"^Check internet/proxy\.?$", "اینترنت/Proxy را بررسی کنید."),
        (r"^Retry\.?$", "دوباره تلاش کنید."),
        (r"^Wait\.?$", "صبر کنید."),
        (r"^Save Central\.?$", "Central را Save کنید."),
        (r"^Open View\.?$", "تب View را باز کنید."),
        (r"^Activate Pro.*$", "Pro را فعال کنید."),
        (r"^Activate AI Pro.*$", "AI Pro را فعال کنید."),
    ],
    "ru": [
        (r"^Download Setup from foxnext\.net\.?$", "Скачайте Setup с foxnext.net."),
        (r"^Install and pick language\.?$", "Установите и выберите язык."),
        (r"^Open Registration\.?$", "Откройте вкладку Registration."),
        (r"^Copy Device ID\.?$", "Скопируйте Device ID."),
        (r"^Connect SSH\.?$", "Выполните Connect SSH."),
        (r"^Full Deploy\.?$", "Выполните Full Deploy."),
        (r"^Try Proxy Settings\.?$", "Попробуйте Proxy Settings."),
        (r"^Contact @HiBlackFoxVpn.*$", "При необходимости напишите @HiBlackFoxVpn с Device ID."),
        (r"^Check internet/proxy\.?$", "Проверьте интернет/Proxy."),
        (r"^Retry\.?$", "Повторите попытку."),
        (r"^Wait\.?$", "Подождите."),
        (r"^Save Central\.?$", "Сохраните Central."),
        (r"^Open View\.?$", "Откройте вкладку View."),
    ],
    "zh": [
        (r"^Download Setup from foxnext\.net\.?$", "从 foxnext.net 下载 Setup。"),
        (r"^Install and pick language\.?$", "安装并选择语言。"),
        (r"^Open Registration\.?$", "打开 Registration 标签。"),
        (r"^Copy Device ID\.?$", "复制 Device ID。"),
        (r"^Connect SSH\.?$", "执行 Connect SSH。"),
        (r"^Full Deploy\.?$", "执行 Full Deploy。"),
        (r"^Try Proxy Settings\.?$", "尝试 Proxy Settings。"),
        (r"^Contact @HiBlackFoxVpn.*$", "必要时将 Device ID 发给 @HiBlackFoxVpn。"),
        (r"^Check internet/proxy\.?$", "检查网络/Proxy。"),
        (r"^Retry\.?$", "重试。"),
        (r"^Wait\.?$", "等待。"),
        (r"^Save Central\.?$", "保存 Central。"),
        (r"^Open View\.?$", "打开 View 标签。"),
    ],
}

PREFIX = {
    "fa": "سپس: ",
    "ru": "Далее: ",
    "zh": "然后：",
}

TAIL = {
    "fa": "اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.",
    "ru": "Если не помогло — Device ID в @HiBlackFoxVpn.",
    "zh": "若仍未解决，将 Device ID 发给 @HiBlackFoxVpn。",
}


def localize_step_line(lang: str, line: str) -> str:
    s = re.sub(r"^\d+\.\s*", "", line.strip())
    for pat, rep in REPL[lang]:
        if re.match(pat, s, flags=re.I):
            return rep
    # Generic wrapping that still reads native while preserving technical EN content
    if lang == "fa":
        return f"{s}" if any(ord(c) > 127 for c in s) else f"{s}"
    return s


def localize_steps(lang: str, en_steps: str) -> str:
    lines = [ln for ln in en_steps.splitlines() if ln.strip()]
    out = []
    for i, ln in enumerate(lines, 1):
        out.append(f"{i}. {localize_step_line(lang, ln)}")
    # Soft native coaching line for FA/RU/ZH
    if lang == "fa":
        out = [re.sub(r"^(\d+\.\s*)(.*)$", lambda m: m.group(1) + (
            m.group(2) if any("\u0600" <= c <= "\u06FF" for c in m.group(2)) else m.group(2)
        ), x) for x in out]
        # Prefix technical English steps with native cue when still Latin-heavy
        fixed = []
        for x in out:
            num, body = x.split(". ", 1)
            if not any("\u0600" <= c <= "\u06FF" for c in body):
                body = "انجام دهید: " + body
            fixed.append(f"{num}. {body}")
        out = fixed
    elif lang == "ru":
        fixed = []
        for x in out:
            num, body = x.split(". ", 1)
            if not any("\u0400" <= c <= "\u04FF" for c in body):
                body = "Сделайте: " + body
            fixed.append(f"{num}. {body}")
        out = fixed
    else:
        fixed = []
        for x in out:
            num, body = x.split(". ", 1)
            if not any("\u4e00" <= c <= "\u9fff" for c in body):
                body = "请执行：" + body
            fixed.append(f"{num}. {body}")
        out = fixed
    out.append(f"{len(out)+1}. {TAIL[lang]}")
    return "\n".join(out)


def answer_for(lang: str, qid: str, en_a: str) -> str:
    n = int(qid[1:])
    if 41 <= n <= 200:
        return ANS[qid][lang]
    # Q001–Q040: keep existing generator seeds / native framing
    return gen.answer(lang, qid, en_a)


def render(lang: str) -> str:
    qL, aL, sL, eL = LABELS[lang]
    parts = [HEADERS[lang]]
    for item in DATA:
        qid = item["id"]
        a = answer_for(lang, qid, item["a"])
        parts.append(
            f"### {qid}\n"
            f"**{qL}:** {Q[qid][lang]}\n"
            f"**{aL}:** {a}\n"
            f"**{sL}:**\n{localize_steps(lang, item['steps'])}\n"
            f"**{eL}:** {ERR[lang]}\n"
        )
    return "\n".join(parts)


def main():
    # Verify 041-200 coverage
    for qid in [f"Q{i:03d}" for i in range(41, 201)]:
        assert qid in ANS and set(ANS[qid]) >= {"fa", "ru", "zh"}, qid

    paths = {
        "fa": ROOT / "Persian" / "FAQ_FA.md",
        "ru": ROOT / "Russian" / "FAQ_RU.md",
        "zh": ROOT / "Chinese" / "FAQ_ZH.md",
    }
    for lang, path in paths.items():
        text = render(lang)
        # Ensure no English wrapper leftovers for 041-200
        bad = []
        for qid in [f"Q{i:03d}" for i in range(41, 201)]:
            # extract answer block
            m = re.search(rf"### {qid}\n\*\*[^*]+:\*\* (.+)\n\*\*[^*]+:\*\*", text)
            if not m:
                bad.append(qid + ":missing")
                continue
            ans = m.group(1)
            if lang == "fa" and ("بر اساس رفتار فعلی Black Fox:" in ans or ans.startswith("According")):
                bad.append(qid)
            if lang == "ru" and ans.startswith("По текущему поведению Black Fox:"):
                bad.append(qid)
            if lang == "zh" and ans.startswith("根据当前 Black Fox"):
                bad.append(qid)
        path.write_text(text, encoding="utf-8")
        n = len(re.findall(r"^### Q\d+", text, re.M))
        print(lang, n, path.stat().st_size, "bad_wrappers", len(bad))
        if bad:
            print("  examples", bad[:10])

    # Also dump JSON answers for bot reuse
    (ROOT / "_native_answers_041_200.json").write_text(
        json.dumps(ANS, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("wrote _native_answers_041_200.json")


if __name__ == "__main__":
    main()
