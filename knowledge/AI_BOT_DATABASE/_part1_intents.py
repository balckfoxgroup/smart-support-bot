# -*- coding: utf-8 -*-
"""
Build Black Fox AI/Telegram intent database (FA/EN/RU/ZH).
Facts locked to current product: free Basic = Setup Central+Connect SSH+Full Deploy;
max 6 exits/nodes; Pro ≠ AI Pro; tabs Operations/Check System/View/Settings/Registration/Contact.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "intents"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def L(fa, en, ru, zh):
    return {"fa": fa, "en": en, "ru": ru, "zh": zh}


def qs(fa_list, en_list, ru_list, zh_list):
    # pad/trim to at least 20 by cycling unique-ish variants
    def pad(xs, lang):
        xs = list(xs)
        i = 0
        while len(xs) < 20:
            xs.append(xs[i % len(xs)] + ("؟" if lang == "fa" and not xs[i % len(xs)].endswith("؟") else ""))
            # avoid infinite identical: add space marker once
            if lang != "fa":
                xs[-1] = xs[i % max(len(xs) - 1, 1)] if False else xs[i % len(fa_list if False else xs)]
            i += 1
            if i > 40:
                break
        return xs[: max(20, len(xs))][:24]

    # Better pad: duplicate with slight colloquial prefix
    def ensure20(items, colloquial_prefixes):
        items = [x for x in items if x]
        out = list(items)
        p = 0
        while len(out) < 20:
            base = items[p % len(items)]
            pref = colloquial_prefixes[p % len(colloquial_prefixes)]
            cand = f"{pref}{base}" if pref else base
            if cand not in out:
                out.append(cand)
            else:
                out.append(f"{base} ({p+1})")
            p += 1
        return out[:22]

    return {
        "fa": ensure20(fa_list, ["", "ببخشید ", "سلام ", "لطفاً بگید ", "اصلاً "]),
        "en": ensure20(en_list, ["", "hey ", "please ", "quick q: ", "um "]),
        "ru": ensure20(ru_list, ["", "подскажите ", "пожалуйста ", "срочно: ", "э "]),
        "zh": ensure20(zh_list, ["", "请问", "麻烦说下", "急：", "嗯"]),
    }


def intent(
    intent_id: str,
    category: str,
    priority: str,
    description: dict,
    keywords: dict,
    sample_questions: dict,
    short: dict,
    full: dict,
    expert: dict,
    steps: dict,
    errors: dict,
    solutions: dict,
    related: list,
    clarifying: dict,
    faq_refs: list | None = None,
):
    return {
        "intent": intent_id,
        "category": category,
        "priority": priority,
        "description": description,
        "keywords": keywords,
        "sample_questions": sample_questions,
        "short_answer": short,
        "full_answer": full,
        "expert_guide": expert,
        "steps": steps,
        "possible_errors": errors,
        "solutions": solutions,
        "related_intents": related,
        "clarifying_questions": clarifying,
        "faq_refs": faq_refs or [],
        "source_docs": [
            "Documentation/",
            "AI_Knowledge_Base_Multilingual/",
        ],
    }


INTENTS: list[dict] = []

# ========================= PRODUCT =========================
INTENTS.append(intent(
    "product_what_is", "Product", "high",
    L("معرفی نرم‌افزار Black Fox", "What Black Fox is", "Что такое Black Fox", "Black Fox 是什么"),
    L(["بلک فاکس", "چیست", "نرم افزار", "installer", "vpn"],
      ["black fox", "what is", "installer", "vpn manager", "product"],
      ["блэк фокс", "что такое", "installer", "vpn", "программа"],
      ["黑狐", "是什么", "installer", "vpn", "软件"]),
    qs(
        ["بلک فاکس چیه؟", "این نرم افزار چیکار میکنه؟", "Black Fox چیست؟", "آیا کلاینت VPN مصرف‌کننده‌ست؟",
         "این برنامه پنل ثنایی نصب می‌کنه؟", "برای چی ساخته شده؟", "Multi-Location VPN Manager یعنی چی؟",
         "فرق با کلاینت عادی VPN چیه؟", "روی گوشی هم همون کار ویندوز رو میکنه؟", "اصلاً به درد من میخوره؟",
         "این فورک 3X-UI هست؟", "خودکارسازی سرور میکنه؟", "WireGuard هم می‌ذاره؟", "فقط ایرانیه؟",
         "سایت رسمی کجاست؟", "با 3X-UI چه رابطه‌ای داره؟", "اپراتور سرور باید باشم؟", "مبتدی میتونه استفاده کنه؟",
         "اسم کامل محصول چیه؟", "Installer یعنی چی اینجا؟"],
        ["What is Black Fox?", "Is this a consumer VPN app?", "Does it install 3X-UI?", "What does the installer do?",
         "Is it a 3X-UI fork?", "Who is it for?", "Multi-Location VPN Manager meaning?", "Windows only?",
         "Android companion?", "Official website?", "WireGuard automation?", "Do I need Linux skills?",
         "Sanaei panel?", "foxnext.net related?", "Not a browse VPN?", "Server toolkit?", "Ops installer?",
         "What platforms?", "Product overview please", "Explain Black Fox simply"],
        ["Что такое Black Fox?", "Это VPN-клиент?", "Ставит 3X-UI?", "Для кого программа?",
         "Это форк 3X-UI?", "Что делает Installer?", "Нужен Linux?", "Есть Android?",
         "Официальный сайт?", "WireGuard автоматически?", "Не для серфинга?", "Панель Sanaei?",
         "Multi-Location VPN Manager?", "Windows приложение?", "Обзор продукта", "Простыми словами",
         "Для операторов VPS?", "Связь с foxnext.net?", "Что автоматизирует?", "Кратко о продукте"],
        ["Black Fox是什么？", "这是消费级VPN客户端吗？", "会安装3X-UI吗？", "Installer做什么？",
         "是3X-UI分支吗？", "适合谁用？", "需要懂Linux吗？", "有Android吗？",
         "官网是什么？", "自动装WireGuard吗？", "不是上网VPN？", "Sanaei面板？",
         "多地域VPN管理？", "Windows应用？", "产品简介", "简单说明",
         "给VPS运维用？", "和foxnext.net关系？", "自动化什么？", "一句话介绍"],
    ),
    L("Black Fox یک Installer عملیاتی است؛ روی VPS شما WireGuard و پنل 3X-UI را با SSH خودکار می‌کند، نه کلاینت وب‌گردی.",
      "Black Fox is an ops Installer that automates WireGuard + 3X-UI on your VPS via SSH — not a consumer browse VPN.",
      "Black Fox — операционный Installer: WireGuard + 3X-UI на вашем VPS по SSH, не клиент для серфинга.",
      "Black Fox 是运维型 Installer，通过 SSH 在您的 VPS 上自动部署 WireGuard + 3X-UI，不是上网用的消费级 VPN。"),
    L("برنامه سرورهای شما را مدیریت می‌کند: ذخیره SSH، Full Deploy، Exit/Tunnel/Node، DNS/CDN، Mesh، Mirza و در AI Pro چت عملیاتی. فورک UI پنل نیست.",
      "It manages YOUR servers: SSH store, Full Deploy, exits/tunnels/nodes, DNS/CDN, mesh, Mirza, and AI Pro chat ops. It is not a panel UI fork.",
      "Управляет ВАШИМИ серверами: SSH, Full Deploy, exits/tunnels/nodes, DNS/CDN, mesh, Mirza и AI Pro. Не форк UI панели.",
      "管理您自己的服务器：SSH、Full Deploy、Exit/Tunnel/Node、DNS/CDN、Mesh、Mirza 与 AI Pro。不是面板 UI 分支。"),
    L("معماری: UI → Store مشترک Basic/Pro/AI → SSH/Panel API → هاب‌های blackfoxupdate.ir و foxnext.net. شبکه: Direct سپس Program Proxy.",
      "Architecture: UI → shared Basic/Pro/AI store → SSH/Panel API → hubs blackfoxupdate.ir + foxnext.net. Network: Direct then Program Proxy.",
      "Архитектура: UI → общее хранилище → SSH/Panel API → хабы. Сеть: Direct, затем Program Proxy.",
      "架构：UI → Basic/Pro/AI 共享存储 → SSH/Panel API → 双 Hub。网络：先 Direct 再 Program Proxy。"),
    L(["۱. از foxnext.net دانلود کنید", "۲. حالت Basic را انتخاب کنید", "۳. Central → Connect SSH → Full Deploy"],
      ["1. Download from foxnext.net", "2. Pick Basic", "3. Central → Connect SSH → Full Deploy"],
      ["1. Скачайте с foxnext.net", "2. Выберите Basic", "3. Central → Connect SSH → Full Deploy"],
      ["1. 从 foxnext.net 下载", "2. 选择 Basic", "3. Central → Connect SSH → Full Deploy"]),
    L(["اشتباه گرفتن با کلاینت VPN", "دانلود از سایت غیررسمی"],
      ["Confusing with consumer VPN", "Unofficial download"],
      ["Путаница с VPN-клиентом", "Неофициальная загрузка"],
      ["当成消费级VPN", "非官网下载"]),
    L(["از سایت رسمی نصب کنید", "مسیر مبتدی را دنبال کنید"],
      ["Install from official site", "Follow beginner path"],
      ["Ставьте с официального сайта", "Идите по пути новичка"],
      ["从官网安装", "按新手路径操作"]),
    ["download_installer", "first_run_path", "mode_basic"],
    L(["می‌خواهید نصب کنید یا فقط بدونید محصول چیست؟", "Windows مدنظرتان است یا Android؟"],
      ["Do you need install steps or just a product overview?", "Windows or Android?"],
      ["Нужна установка или только обзор?", "Windows или Android?"],
      ["需要安装步骤还是产品介绍？", "Windows 还是 Android？"]),
    ["Q001", "Q002", "Q150"],
))

INTENTS.append(intent(
    "download_installer", "Install", "high",
    L("دانلود Installer رسمی", "Download official Installer", "Скачать официальный Installer", "下载官方 Installer"),
    L(["دانلود", "download", "نصب کننده", "setup", "foxnext"],
      ["download", "setup.exe", "installer", "foxnext", "official"],
      ["скачать", "download", "setup", "installer", "foxnext"],
      ["下载", "setup", "installer", "官网", "foxnext"]),
    qs(
        ["از کجا دانلود کنم؟", "لینک نصب کجاست؟", "Setup رسمی کدومه؟", "سایت دانلود چیه؟",
         "portable هم هست؟", "فایل از کجا بگیرم؟", "mirror غیررسمی خطرناکه؟", "آپدیت از کجا میاد؟",
         "Black Fox Vpn-Installer-Setup.exe کجاست؟", "روی foxnext.net کجا بزنم؟",
         "لینک مستقیم میخوای؟", "دانلود نمیشه چیکار کنم؟", "با فیلتر چطور دانلود کنم؟", "هاب آپدیت کجاست؟",
         "نسخه ویندوز کجاست؟", "اندروید جداست؟", "Config Builder جداست؟", "چطور مطمئن شم اصلیه؟",
         "سیاه‌افزار نباشه؟", "از تلگرام دانلود کنم؟"],
        ["Where to download?", "Official Setup link?", "Is portable OK?", "foxnext.net download?",
         "Unofficial mirror safe?", "Windows installer name?", "Update host?", "Android separate?",
         "Config Builder separate?", "How verify authenticity?", "Setup.exe where?", "Can't download",
         "Blocked download fix?", "blackfoxupdate.ir?", "GitHub download?", "Telegram file OK?",
         "Which file first?", "Installer vs portable", "Official site only?", "Download help"],
        ["Где скачать?", "Официальный Setup?", "Portable можно?", "Ссылка foxnext.net?",
         "Неофициальное зеркало?", "Имя файла Windows?", "Хаб обновлений?", "Android отдельно?",
         "Config Builder отдельно?", "Как проверить подлинность?", "Не качается", "Блокировка загрузки",
         "blackfoxupdate.ir?", "С GitHub?", "Из Telegram можно?", "Какой файл первый?",
         "Setup или portable", "Только официальный сайт?", "Помощь со скачиванием", "Где Setup.exe"],
        ["从哪里下载？", "官方 Setup 链接？", "可以用 Portable 吗？", "foxnext.net 下载？",
         "非官方镜像安全吗？", "Windows 文件名？", "更新 Hub？", "Android 分开吗？",
         "Config Builder 分开吗？", "如何确认正版？", "下不下来怎么办？", "被墙怎么下？",
         "blackfoxupdate.ir？", "GitHub 下？", "Telegram 文件可以吗？", "先下哪个？",
         "Setup 还是 portable", "只用官网？", "下载帮助", "Setup.exe 在哪"],
    ),
    L("از سایت رسمی foxnext.net فایل Setup را دانلود کنید؛ از mirrorهای ناشناس پرهیز کنید.",
      "Download Setup from official foxnext.net; avoid unknown mirrors.",
      "Скачивайте Setup с официального foxnext.net; избегайте неизвестных зеркал.",
      "请从官网 foxnext.net 下载 Setup，避免不明镜像。"),
    L("نام رایج: Black Fox Vpn-Installer-Setup.exe. آپدیت‌ها از هاب‌های foxnext.net / blackfoxupdate.ir می‌آیند. Android و Config Builder بسته‌های جدا در version.json هستند.",
      "Typical name: Black Fox Vpn-Installer-Setup.exe. Updates use foxnext.net / blackfoxupdate.ir hubs. Android and Config Builder are separate packages.",
      "Обычно: Black Fox Vpn-Installer-Setup.exe. Обновления с хабов foxnext.net / blackfoxupdate.ir. Android и Config Builder — отдельные пакеты.",
      "常见文件名：Black Fox Vpn-Installer-Setup.exe。更新来自 foxnext.net / blackfoxupdate.ir。Android 与 Config Builder 为独立包。"),
    L("اگر دانلود مسدود است Proxy Settings داخل برنامه بعد از نصب، یا شبکه دیگر. نسخه/build را از چت اختراع نکنید.",
      "If download is blocked, use another network; after install try Proxy Settings. Do not invent version numbers in chat.",
      "Если загрузка блокируется — другая сеть; после установки Proxy Settings. Не выдумывайте номера версий.",
      "若下载被拦，换网络；安装后可用 Proxy Settings。聊天中不要编造版本号。"),
    L(["۱. foxnext.net را باز کنید", "۲. صفحه Download/Setup", "۳. Setup.exe را اجرا کنید", "۴. زبان و حالت را انتخاب کنید"],
      ["1. Open foxnext.net", "2. Download/Setup page", "3. Run Setup.exe", "4. Pick language and mode"],
      ["1. Откройте foxnext.net", "2. Страница Download/Setup", "3. Запустите Setup.exe", "4. Язык и режим"],
      ["1. 打开 foxnext.net", "2. Download/Setup 页面", "3. 运行 Setup.exe", "4. 选择语言与模式"]),
    L(["فایل ناقص", "آنتی‌ویروس", "سایت جعلی"], ["Corrupt file", "Antivirus", "Fake site"],
      ["Битый файл", "Антивирус", "Фейковый сайт"], ["文件损坏", "杀毒拦截", "假网站"]),
    L(["دوباره از سایت رسمی", "استثنا برای آنتی‌ویروس", "هش/اندازه را با سایت چک کنید"],
      ["Re-download official", "Allow in antivirus", "Verify with site"],
      ["Скачайте снова официально", "Разрешите в антивирусе", "Сверьте с сайтом"],
      ["重新从官网下载", "杀毒放行", "与官网核对"]),
    ["install_setup", "setup_vs_portable", "force_update"],
    L(["Windows می‌خواهید یا Android؟", "Setup نصب‌شونده یا Portable؟"],
      ["Windows or Android?", "Setup installer or Portable?"],
      ["Windows или Android?", "Setup или Portable?"],
      ["要 Windows 还是 Android？", "Setup 安装包还是 Portable？"]),
    ["Q004", "Q066"],
))

# Continue with more intents in a second write via exec - file getting long.
# I'll append remaining intents in the same file using a compact builder below.

def add(**kwargs):
    INTENTS.append(intent(**kwargs))

# ---- modes / license / deploy core (compact but complete) ----

add(
    intent_id="mode_basic", category="Modes", priority="high",
    description=L("حالت Basic", "Basic mode", "Режим Basic", "Basic 模式"),
    keywords=L(["basic", "بیسیک", "ساده", "رایگان"], ["basic", "free ops", "mode"], ["basic", "режим", "бесплатно"], ["basic", "基础", "免费"]),
    sample_questions=qs(
        ["Basic چیه؟", "حالت ساده کافیه؟", "تو Basic چی آزاده؟", "کشور Central چی باشه؟",
         "Exit تو Basic میخواد لایسنس؟", "با Basic چند Exit؟", "برای شخصی خوبه؟", "Basic یا Pro؟",
         "سوییچ به Basic کجاست؟", "بدون پول چی کار میشه؟", "ایران چین روسیه الزامیه؟", "Configure Panel تو Basic؟",
         "Full Deploy رایگانه؟", "Connect SSH پولیه؟", "Setup Central رایگانه؟", "محدودیت Basic چیه؟",
         "بعداً Pro میشم؟", "AI تو Basic هست؟", "توپولوژی تو Basic؟", "دکمه Exit قفله چرا؟"],
        ["What is Basic?", "Free ops in Basic?", "Central country rule?", "Need license for exit?",
         "How many exits?", "Basic vs Pro?", "Where switch mode?", "Is Full Deploy free?",
         "Connect SSH free?", "AI in Basic?", "Configure Panel needs license?", "Personal use OK?",
         "Iran China Russia?", "Why exit locked?", "Topology in Basic?", "Enough for me?",
         "Upgrade later?", "View tab Basic?", "Limited Access on exit?", "Beginner mode?"],
        ["Что такое Basic?", "Что бесплатно?", "Страна Central?", "Лицензия для Exit?",
         "Сколько Exit?", "Basic или Pro?", "Где сменить режим?", "Full Deploy бесплатно?",
         "Connect SSH бесплатно?", "AI в Basic?", "Configure Panel?", "Для личного?",
         "Иран Китай Россия?", "Почему Exit заблокирован?", "Топология?", "Хватит ли Basic?",
         "Потом Pro?", "Вкладка View?", "Limited Access?", "Режим новичка?"],
        ["什么是Basic？", "Basic哪些免费？", "Central国家限制？", "Exit要License吗？",
         "多少Exit？", "Basic还是Pro？", "哪里切换模式？", "Full Deploy免费吗？",
         "Connect SSH免费吗？", "Basic有AI吗？", "Configure Panel？", "个人用够吗？",
         "伊朗中国俄罗斯？", "为何Exit锁定？", "有拓扑吗？", "够用吗？",
         "以后升级Pro？", "View标签？", "Limited Access？", "新手模式？"],
    ),
    short=L("Basic برای راه‌اندازی Central و پنل است. بدون License فقط Setup Central + Connect SSH + Full Deploy رایگان‌اند.",
            "Basic builds central+panel. Without license only Setup Central, Connect SSH, Full Deploy are free.",
            "Basic — central+панель. Без License бесплатны только Setup Central, Connect SSH, Full Deploy.",
            "Basic 用于搭建 Central+面板。无 License 时仅 Setup Central、Connect SSH、Full Deploy 免费。"),
    full=L("Central در Basic معمولاً باید ایران/چین/روسیه باشد. Exit و Configure Panel نیاز به فعال‌سازی دارند. سقف Exit برابر ۶ است. AI Pro جداست.",
           "Basic central is typically IR/CN/RU. Exits and Configure Panel need activation. Max 6 exits. AI Pro is separate.",
           "Central в Basic обычно IR/CN/RU. Exit и Configure Panel требуют активации. Макс. 6 Exit. AI Pro отдельно.",
           "Basic 的 Central 通常需在伊朗/中国/俄罗斯。Exit 与 Configure Panel 需激活。Exit 最多 6。AI Pro 单独。"),
    expert=L("Store مشترک با Pro/AI است؛ عوض کردن حالت سرورها را پاک نمی‌کند. گیت‌ها همچنان چک می‌شوند.",
             "Shared store with Pro/AI; switching mode does not wipe servers. Gates still apply.",
             "Общий store с Pro/AI; смена режима не стирает серверы. Гейты остаются.",
             "与 Pro/AI 共享 Store；切换模式不清除服务器，权限门控仍生效。"),
    steps=L(["۱. View → Basic", "۲. Central Setup", "۳. Connect SSH", "۴. Full Deploy", "۵. برای Exit از Registration فعال کنید"],
            ["1. View → Basic", "2. Central Setup", "3. Connect SSH", "4. Full Deploy", "5. Activate for exits"],
            ["1. View → Basic", "2. Central Setup", "3. Connect SSH", "4. Full Deploy", "5. Активируйте для Exit"],
            ["1. View → Basic", "2. Central Setup", "3. Connect SSH", "4. Full Deploy", "5. 需要 Exit 时先激活"]),
    errors=L(["Limited Access", "کشور Central رد شد", "Exit قفل"],
             ["Limited Access", "Central country rejected", "Exit locked"],
             ["Limited Access", "Страна Central отклонена", "Exit заблокирован"],
             ["Limited Access", "Central 国家被拒", "Exit 锁定"]),
    solutions=L(["Registration برای لایسنس", "VPS در IR/CN/RU", "یا ارتقا به Pro"],
                ["Registration for license", "Use IR/CN/RU VPS", "Or upgrade Pro"],
                ["Registration для лицензии", "VPS IR/CN/RU", "Или Pro"],
                ["到 Registration 激活", "使用 IR/CN/RU VPS", "或升级 Pro"]),
    related=["activate_license", "free_ops_basic", "mode_pro", "full_deploy"],
    clarifying=L(["الان روی کدام حالت هستید؟", "مشکل روی Exit است یا Full Deploy؟"],
                 ["Which mode are you on?", "Is the issue Exit or Full Deploy?"],
                 ["Какой сейчас режим?", "Проблема с Exit или Full Deploy?"],
                 ["当前是什么模式？", "问题在 Exit 还是 Full Deploy？"]),
    faq_refs=["Q007", "Q011", "Q012", "Q013"],
)

add(
    intent_id="mode_pro", category="Modes", priority="high",
    description=L("حالت Pro", "Pro mode", "Режим Pro", "Pro 模式"),
    keywords=L(["pro", "پرو", "تونل", "نود", "mesh", "cdn"], ["pro", "tunnel", "node", "mesh", "cdn"],
               ["pro", "туннель", "node", "mesh", "cdn"], ["pro", "隧道", "节点", "mesh", "cdn"]),
    sample_questions=qs(
        ["Pro چیه؟", "با Pro چی باز میشه؟", "تونل فقط پرو؟", "نود لازمه Pro؟", "Mesh تو Pro؟",
         "CDN فقط Pro؟", "Mirza پرو میخواد؟", "Exit نامحدود میشه؟", "فرق Pro و AI Pro؟",
         "چطور Pro فعال کنم؟", "BFXP چیه؟", "Move Central پرو؟", "Domain پرو؟", "Factory Reset پرو؟",
         "بعد از Pro حالت View؟", "زنجیره multi-hop؟", "Subscription؟", "چرا میگه need Pro؟",
         "AI با Pro میاد؟", "Pro برای ریسلر؟"],
        ["What is Pro?", "What unlocks?", "Tunnels Pro-only?", "Nodes need Pro?", "Mesh Pro?",
         "CDN Pro?", "Mirza needs Pro?", "Unlimited exits?", "Pro vs AI Pro?", "How activate Pro?",
         "BFXP?", "Move Central?", "Domain Pro?", "Factory Reset Pro?", "multi-hop chain?",
         "Why need Pro?", "Does Pro include AI?", "Reseller use?", "View switch?", "Add Subscription?"],
        ["Что такое Pro?", "Что открывает?", "Туннели только Pro?", "Node нужен Pro?", "Mesh?",
         "CDN?", "Mirza?", "Безлимит Exit?", "Pro vs AI Pro?", "Как активировать Pro?",
         "BFXP?", "Move Central?", "Domain?", "Factory Reset?", "multi-hop?",
         "Почему need Pro?", "Pro даёт AI?", "Для реселлера?", "Смена View?", "Subscription?"],
        ["什么是Pro？", "解锁什么？", "隧道仅Pro？", "Node要Pro吗？", "Mesh？",
         "CDN？", "Mirza？", "无限Exit？", "Pro和AI Pro区别？", "如何激活Pro？",
         "BFXP？", "Move Central？", "Domain？", "Factory Reset？", "多跳？",
         "为何need Pro？", "Pro含AI吗？", "适合代理？", "切换View？", "Subscription？"],
    ),
    short=L("Pro تونل، نود، Domain، CDN، Mesh، Mirza و Move Central را باز می‌کند. Exit همچنان حداکثر ۶ است. AI جداست.",
            "Pro unlocks tunnels, nodes, Domain, CDN, Mesh, Mirza, Move Central. Still max 6 exits. AI is separate.",
            "Pro открывает tunnels/nodes/Domain/CDN/Mesh/Mirza/Move Central. Exit всё ещё макс. 6. AI отдельно.",
            "Pro 解锁隧道、节点、Domain、CDN、Mesh、Mirza、Move Central。Exit 仍最多 6。AI 单独。"),
    full=L("فعال‌سازی با BFXP/claim/TX. سپس View → Pro. ترتیب پیشنهادی: Tunnel → Exit → Configure Panel → Node → Domain → CDN → Mesh → Bot.",
           "Activate via BFXP/claim/TX, then View → Pro. Order: Tunnel → Exit → Configure Panel → Node → Domain → CDN → Mesh → Bot.",
           "Активация BFXP/claim/TX, затем View → Pro. Порядок: Tunnel → Exit → Configure Panel → Node → Domain → CDN → Mesh → Bot.",
           "用 BFXP/claim/TX 激活后 View → Pro。顺序：Tunnel → Exit → Configure Panel → Node → Domain → CDN → Mesh → Bot。"),
    expert=L("حذف Tunnel ممکن است hop بالاتر را ریست کند؛ Exit وابسته را اول پاک کنید.",
             "Deleting a tunnel hop may reset higher hops; remove dependent exits first.",
             "Удаление hop может сбросить старшие; сначала удалите зависимые Exit.",
             "删除 tunnel hop 可能重置更高跳；先删除依赖的 Exit。"),
    steps=L(["۱. Registration → Activate Pro", "۲. View → Pro", "۳. ستون فقرات Basic را کامل کنید", "۴. لایه‌های Pro را اضافه کنید"],
            ["1. Registration → Activate Pro", "2. View → Pro", "3. Finish Basic spine", "4. Add Pro layers"],
            ["1. Registration → Activate Pro", "2. View → Pro", "3. Завершите Basic", "4. Добавьте слои Pro"],
            ["1. Registration → Activate Pro", "2. View → Pro", "3. 完成 Basic 主干", "4. 添加 Pro 层"]),
    errors=L(["This feature requires Pro activation"], ["This feature requires Pro activation"],
             ["This feature requires Pro activation"], ["This feature requires Pro activation"]),
    solutions=L(["کد Pro را فعال کنید", "حالت View را Pro کنید"], ["Activate Pro code", "Switch View to Pro"],
                ["Активируйте Pro", "Переключите View на Pro"], ["激活 Pro", "View 切到 Pro"]),
    related=["activate_license", "mode_ai_pro", "add_tunnel", "mesh_servers", "need_pro"],
    clarifying=L(["کدام دکمه Pro قفل است؟", "لایسنس Pro دارید؟"],
                 ["Which Pro button is locked?", "Do you already have Pro license?"],
                 ["Какая Pro-кнопка заблокирована?", "Уже есть Pro license?"],
                 ["哪个 Pro 按钮被锁？", "是否已有 Pro License？"]),
    faq_refs=["Q008", "Q014", "Q049", "Q104"],
)

add(
    intent_id="mode_ai_pro", category="Modes", priority="high",
    description=L("AI Assistant Pro", "AI Assistant Pro", "AI Assistant Pro", "AI Assistant Pro"),
    keywords=L(["ai pro", "هوش مصنوعی", "چت", "quota", "bfxa"], ["ai pro", "assistant", "chat", "quota", "bfxa"],
               ["ai pro", "чат", "квота", "bfxa"], ["ai pro", "助手", "聊天", "quota", "bfxa"]),
    sample_questions=qs(
        ["AI Pro چیه؟", "چت هوش مصنوعی کجاست؟", "چرا AI قفله؟", "سهمیه تموم شده", "BFXA چیه؟",
         "BFXQ چیه؟", "Pro کافیه برای AI؟", "Tasks چی هستن؟", "Diagnose & Repair؟", "MCP چیه؟",
         "تأیید Yes/No؟", "عکس میتونم بفرستم؟", "Add OutBounds؟", "Link Test AI؟", "کوتای زمان‌دار؟",
         "چت استریم میشه؟", "Android هم AI داره؟", "لاگ عملیات کجاست؟", "AI نسخه مدل میگه؟", "چطور شارژ کنم؟"],
        ["What is AI Pro?", "Where is AI chat?", "Why AI locked?", "Quota exhausted?", "BFXA?",
         "BFXQ?", "Does Pro include AI?", "What are Tasks?", "Diagnose & Repair?", "MCP?",
         "Yes/No confirm?", "Can attach images?", "Add OutBounds?", "Link Test AI?", "Quota expiry?",
         "Streaming replies?", "Android AI?", "Does AI discuss versions?", "How recharge?", "Apply Actions?"],
        ["Что такое AI Pro?", "Где AI-чат?", "Почему AI заблокирован?", "Квота кончилась?", "BFXA?",
         "BFXQ?", "Pro включает AI?", "Что такое Tasks?", "Diagnose & Repair?", "MCP?",
         "Подтверждение Yes/No?", "Можно фото?", "Add OutBounds?", "Link Test?", "Срок квоты?",
         "Стриминг?", "AI на Android?", "AI говорит версии?", "Как пополнить?", "Apply Actions?"],
        ["什么是AI Pro？", "AI聊天在哪？", "为何AI锁定？", "quota用尽？", "BFXA？",
         "BFXQ？", "Pro含AI吗？", "Tasks是什么？", "Diagnose & Repair？", "MCP？",
         "要Yes/No确认吗？", "能发图吗？", "Add OutBounds？", "Link Test？", "quota过期？",
         "流式回复？", "Android有AI吗？", "AI会说版本吗？", "怎么充值？", "Apply Actions？"],
    ),
    short=L("AI Pro چت و Tasks عملیاتی است؛ جدا از Pro؛ نیاز به BFXA و quota دارد.",
            "AI Pro is chat+Tasks for ops; separate from Pro; needs BFXA and quota.",
            "AI Pro — чат+Tasks; отдельно от Pro; нужны BFXA и quota.",
            "AI Pro 是运维聊天+Tasks；与 Pro 分开；需要 BFXA 与 quota。"),
    full=L("بدون unlock، Operations حالت قفل نشان می‌دهد. ترجیح با Tasks. قبل از تغییر مخرب تأیید بگیرید. هویت پاسخ: BlackFox AI؛ نسخه اختراع نکنید.",
           "Without unlock, Operations shows locked AI UI. Prefer Tasks. Confirm before mutating. Identity: BlackFox AI; never invent versions.",
           "Без unlock — locked UI. Предпочитайте Tasks. Подтверждайте опасные действия. Имя: BlackFox AI; версии не выдумывать.",
           "未解锁时 Operations 显示锁定。优先 Tasks。危险操作先确认。身份：BlackFox AI；不要编造版本。"),
    expert=L("Check System محلی است؛ Diagnose & Repair مسیر AI است. MCP برای ابزار خارجی مثل Cursor.",
             "Check System is local; Diagnose & Repair is AI path. MCP bridges external tools like Cursor.",
             "Check System — локально; Diagnose & Repair — AI. MCP — мост к внешним инструментам.",
             "Check System 为本地；Diagnose & Repair 为 AI 路径。MCP 对接外部工具。"),
    steps=L(["۱. Activate AI Pro", "۲. View → AI Pro", "۳. سهمیه را چک کنید", "۴. Task یا چت", "۵. Yes/No را تأیید کنید"],
            ["1. Activate AI Pro", "2. View → AI Pro", "3. Check quota", "4. Task or chat", "5. Confirm Yes/No"],
            ["1. Activate AI Pro", "2. View → AI Pro", "3. Проверьте quota", "4. Task или чат", "5. Подтвердите"],
            ["1. 激活 AI Pro", "2. View → AI Pro", "3. 检查 quota", "4. Task 或聊天", "5. 确认 Yes/No"]),
    errors=L(["AI Assistant Pro activation required", "quota exhausted"],
             ["AI Assistant Pro activation required", "quota exhausted"],
             ["AI Assistant Pro activation required", "quota exhausted"],
             ["AI Assistant Pro activation required", "quota exhausted"]),
    solutions=L(["BFXA + BFXQ", "Proxy اگر هاب قطع است"], ["BFXA + BFXQ", "Proxy if hub blocked"],
                ["BFXA + BFXQ", "Proxy если хаб недоступен"], ["BFXA + BFXQ", "Hub 不通时开 Proxy"]),
    related=["activate_license", "ai_quota", "ai_chat_locked", "mode_pro"],
    clarifying=L(["پیام قفل می‌بینید یا سهمیه تمام شده؟", "لایسنس AI Pro دارید؟"],
                 ["Is it lock message or quota empty?", "Do you have AI Pro license?"],
                 ["Блокировка или квота?", "Есть AI Pro license?"],
                 ["是锁定提示还是 quota 用尽？", "是否已有 AI Pro License？"]),
    faq_refs=["Q009", "Q079", "Q080", "Q104", "Q187"],
)

print("base intents", len(INTENTS))
