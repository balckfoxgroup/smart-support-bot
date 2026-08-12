# -*- coding: utf-8 -*-
"""Native FA/RU/ZH answers for FAQ Q041–Q080."""
A = {
"Q041": {
"fa": "کدهای شارژ سهمیه AI با پیشوند `BFXQ` (معمولاً claim مثل `BFXQ-CLM-…`) هستند و حالت License را عوض نمی‌کنند. آیتم کاتالوگ `ai_quota` جدا از لایسنس است. PAS می‌تواند claim شارژ بسازد؛ با claim فقط سهمیه اعمال می‌شود.",
"ru": "Коды пополнения AI quota с префиксом `BFXQ` (часто claim вроде `BFXQ-CLM-…`) не меняют режим License. Каталог `ai_quota` отделён от лицензии. PAS может выдать claim пополнения; claim добавляет только квоту.",
"zh": "`BFXQ` 前缀的 AI quota 充值码（常为 `BFXQ-CLM-…` 这类 claim）不会改变 License 模式。目录项 `ai_quota` 与许可证分离。PAS 可生成充值 claim；claim 只增加配额。",
},
"Q042": {
"fa": "مدت‌ها معمولاً ۱۲ تا ۳۰ ماه طبق کاتالوگ هاب است؛ اگر ماه مشخص نباشد اغلب پیش‌فرض ۱۸ ماه اعمال می‌شود. ماه‌های `license-access.json`: ۱۲،۱۵،۱۸،۲۱،۲۴،۲۷،۳۰. لایسنس منقضی با نشان «منقضی شده» قفل امکانات کامل را می‌بندد.",
"ru": "Срок обычно 12–30 месяцев по каталогу хаба; если месяцы не указаны, часто применяется 18. Месяцы в `license-access.json`: 12,15,18,21,24,27,30. Истёкшая лицензия блокирует полный функционал.",
"zh": "时长通常按 Hub 目录为 12–30 个月；未指定时常见默认 18 个月。`license-access.json` 月份：12、15、18、21、24、27、30。过期后完整功能会被锁定。",
},
"Q043": {
"fa": "کاتالوگ تا ۳ دستگاه با تخفیف پشتیبانی می‌کند (دستگاه۲ حدود ۲۰٪، دستگاه۳ حدود ۳۰٪). هر claim در اولین Activate به Device ID همان دستگاه bind می‌شود؛ یک claim را روی چند PC بی‌ربط دوباره استفاده نکنید.",
"ru": "Каталог поддерживает до 3 устройств со скидками (device2 ≈20%, device3 ≈30%). Каждый claim при первом Activate привязывается к Device ID — не используйте один claim на разных ПК.",
"zh": "目录最多支持 3 台设备折扣（第2台约20%，第3台约30%）。每个 claim 在首次 Activate 时绑定该机 Device ID；不要把同一 claim 用在无关的多台电脑。",
},
"Q044": {
"fa": "TX استفاده‌شده هم در کلاینت و هم در هاب رد می‌شود (`tx_already_used` / `tx_already_claimed`). بعد از claim، وارد کردن دوباره TX معمولاً کدها را نشان نمی‌دهد.",
"ru": "Уже использованный TX отклоняется и локально, и на хабе (`tx_already_used` / `tx_already_claimed`). После claim повторный ввод TX обычно больше не показывает коды.",
"zh": "已使用的 TX 在本地与 Hub 都会被拒绝（`tx_already_used` / `tx_already_claimed`）。claim 之后再次输入 TX 通常不再显示代码。",
},
"Q045": {
"fa": "یعنی این کد claim قبلاً به Device ID دیگری وصل شده (`bound_other_device` / `claim_bound`). با همان claim نمی‌توانید PC دوم نامرتبط را باز کنید.",
"ru": "Этот claim уже привязан к другому Device ID (`bound_other_device` / `claim_bound`). Тем же claim нельзя открыть второй несвязанный ПК.",
"zh": "表示该 claim 已绑定到另一台设备的 Device ID（`bound_other_device` / `claim_bound`）。同一 claim 无法解锁第二台无关电脑。",
},
"Q046": {
"fa": "پیام «Invalid activation code» معمولاً به‌خاطر غلط املایی، پیشوند سطح اشتباه، کپی ناقص، یا کد نامعتبر است. برای کد machine-bound هم Device ID باید همان دستگاه باشد.",
"ru": "«Invalid activation code» обычно из‑за опечатки, неверного префикса тарифа, обрезанной вставки или мусорного кода. Для machine-bound нужен тот же Device ID.",
"zh": "“Invalid activation code” 通常因拼写错误、层级前缀错误、粘贴不完整或无效代码。设备绑定码还要求 Device ID 为本机。",
},
"Q047": {
"fa": "منتظر تأیید BEP-20 بمانید؛ مبلغ و آدرس گیرنده باید دقیقاً مطابق صفحه باشد. خطاها: TX پیدا نشد، ناموفق، گیرنده اشتباه، مبلغ کم، توکن غیر USDT-BEP20، یا pending.",
"ru": "Дождитесь подтверждения BEP-20; сумма и адрес получателя должны совпадать со страницей. Ошибки: TX не найден, failed, неверный получатель, мало суммы, не USDT BEP-20, pending.",
"zh": "等待 BEP-20 确认；金额与收款地址须与页面完全一致。错误包括：TX 未找到、失败、收款错误、金额不足、非 USDT BEP-20、pending。",
},
"Q048": {
"fa": "یعنی قابلیت پشت گیت لایسنس است (`dialog.need_activate` / Limited Access). در Basic فقط Setup Central، Connect SSH و Full Deploy بدون لایسنس آزادند؛ بقیه معمولاً نیاز به Activate دارند.",
"ru": "Функция закрыта лицензией (`dialog.need_activate` / Limited Access). В Basic без лицензии свободны только Setup Central, Connect SSH и Full Deploy.",
"zh": "表示功能被 License 门控（`dialog.need_activate` / Limited Access）。Basic 无许可证时仅 Setup Central、Connect SSH、Full Deploy 免费。",
},
"Q049": {
"fa": "قابلیت فقط-Pro است در حالی که لایسنس Basic یا قفل است (`dialog.need_pro`). زنجیره تونل، برخی CDN/Subscription/Nodeها به Pro یا AI Pro نیاز دارند.",
"ru": "Функция только для Pro при Basic/locked (`dialog.need_pro`). Туннельная цепочка и часть CDN/Subscription/Node требуют Pro или AI Pro.",
"zh": "在 Basic/锁定状态下使用了仅 Pro 功能（`dialog.need_pro`）。隧道链及部分 CDN/Subscription/Node 需要 Pro 或 AI Pro。",
},
"Q050": {
"fa": "امکانات کامل لایسنس قفل می‌شود تا تمدید کنید. نشان «License expired» دیده می‌شود. Reactivation هم ممکن است expired برگرداند.",
"ru": "Полный функционал лицензии блокируется до продления. Виден бейдж «License expired». Reactivation может вернуть expired.",
"zh": "完整许可功能会锁定直至续期。可见 “License expired”。Reactivation 也可能返回 expired。",
},
"Q051": {
"fa": "قیمت زنده در `license-access.json` روی هاب است و بدون rebuild برنامه قابل ویرایش است. اگر هاب در دسترس نباشد، برنامه به ثابت‌های کد fallback می‌کند.",
"ru": "Живые цены в `license-access.json` на хабе; правка без rebuild приложения. Если хаб недоступен — fallback на константы в коде.",
"zh": "实时价格在 Hub 的 `license-access.json`，改价无需重建应用。Hub 不可用时回退代码常量。",
},
"Q052": {
"fa": "Central Server Setup اطلاعات SSH سرور مرکزی را محلی ذخیره می‌کند (IP، احراز هویت، کشور و پیش‌نویس). قبل از Deploy لازم است.",
"ru": "Central Server Setup сохраняет SSH центрального сервера локально (IP, auth, страна, черновик). Нужно до Deploy.",
"zh": "Central Server Setup 在本地保存中心服务器 SSH（IP、认证、国家、草稿）。Deploy 前必需。",
},
"Q053": {
"fa": "پیام محصول: هنگام ذخیره نمی‌توان Host/IP را عوض کرد؛ برای IP دیگر از جریان سرور جدید استفاده کنید. این از یکپارچگی inventory و شماره chain محافظت می‌کند.",
"ru": "Сообщение продукта: при сохранении нельзя менять Host/IP; для другого IP — новый server flow. Так защищают inventory и номер chain.",
"zh": "产品提示：保存时不能改 Host/IP；换 IP 请走新建服务器流程。用于保护库存与 chain 编号完整性。",
},
"Q054": {
"fa": "Panel Login Info (URL/path)، Proxy، فایروال را چک کنید و ابزار پنل را دوباره اجرا کنید. اگر credentials نیست → Full Deploy. خطای ورود نود اغلب path/token کهنه است → Full Deploy یا تازه‌سازی Panel Login Info.",
"ru": "Проверьте Panel Login Info (URL/path), Proxy, файрвол и повторите panel-операции. Нет credentials → Full Deploy. Ошибка логина ноды часто из‑за устаревшего path/token.",
"zh": "检查 Panel Login Info（URL/path）、Proxy、防火墙并重跑面板相关操作。无凭据 → Full Deploy。节点登录失败常见于过期 path/token。",
},
"Q055": {
"fa": "می‌توان فقط WireGuard یا فقط پنل Sanaei را روی Central نصب/به‌روز کرد؛ وقتی Full Deploy ناقص مانده مفید است. Settings → Check Update 3X-UI بسته را برای نصب بعدی کش می‌کند.",
"ru": "Можно поставить только WireGuard или только панель Sanaei на Central — полезно при частичном Full Deploy. Settings → Check Update 3X-UI кэширует пакет.",
"zh": "可仅在 Central 安装/更新 WireGuard 或仅 Sanaei 面板——Full Deploy 部分成功时有用。Settings → Check Update 3X-UI 会缓存包供下次安装。",
},
"Q056": {
"fa": "Diagnostic Center بررسی فقط‌خواندنی سلامت SSH، WireGuard، پنل، DNS، CDN و Exitهاست. نتایج OK/Warning/Error را ببینید و برای پشتیبانی Export کنید.",
"ru": "Diagnostic Center — только чтение здоровья SSH, WireGuard, панели, DNS, CDN и Exit. Смотрите OK/Warning/Error и экспортируйте для поддержки.",
"zh": "Diagnostic Center 只读检查 SSH、WireGuard、面板、DNS、CDN 与 Exit。查看 OK/Warning/Error，并可导出给支持。",
},
"Q057": {
"fa": "Link Test اتصال را می‌سنجد و WireGuard، GRE یا Reverse Tunnel (Stealth-WSS) را پیشنهاد می‌کند. اعمال نهایی معمولاً از Mesh یا نوع لینک در Add Server است.",
"ru": "Link Test измеряет связность и рекомендует WireGuard, GRE или Reverse Tunnel (Stealth-WSS). Применение — через Mesh или тип линка в Add Server.",
"zh": "Link Test 评估连通性并建议 WireGuard、GRE 或 Reverse Tunnel (Stealth-WSS)。最终应用通常经 Mesh 或 Add Server 的链路类型。",
},
"Q058": {
"fa": "اگر تونل WireGuard شکست بخورد، برنامه GRE را پیشنهاد می‌دهد. ترتیب failover مش: WireGuard → GRE → Reverse Tunnel (Stealth-WSS) → پشتیبان‌ها.",
"ru": "Если WireGuard падает, приложение предлагает GRE. Порядок failover mesh: WireGuard → GRE → Reverse Tunnel (Stealth-WSS) → backups.",
"zh": "若 WireGuard 隧道失败，应用会建议 GRE。Mesh 故障切换顺序：WireGuard → GRE → Reverse Tunnel (Stealth-WSS) → 备份。",
},
"Q059": {
"fa": "گزینه تونل معکوس محافظت‌شده در پشته لینک/مش با نام محصول Reverse Tunnel (Stealth-WSS). وقتی مسیر مستقیم WG/GRE ضعیف است استفاده می‌شود و توسط Link Monitor Agent پایش می‌شود.",
"ru": "Защищённый reverse-туннель в стеке линков/mesh под именем Reverse Tunnel (Stealth-WSS). Когда прямые WG/GRE плохи; мониторит Link Monitor Agent.",
"zh": "链路/Mesh 栈中的受保护反向隧道，产品名 Reverse Tunnel (Stealth-WSS)。在直连 WG/GRE 不佳时使用，并由 Link Monitor Agent 监控。",
},
"Q060": {
"fa": "ایجنت‌های همیشه روشن روی Central، Tunnel، Exit و Node برای سلامت مسیر و failover. ویزارد Mesh آن‌ها را نصب می‌کند؛ ابزارها هنگام نصب از GitHub روی هر VPS دانلود می‌شوند.",
"ru": "Постоянные агенты на Central/Tunnel/Exit/Node для здоровья пути и failover. Мастер Mesh ставит их; инструменты качаются с GitHub на каждый VPS при установке.",
"zh": "运行在 Central/Tunnel/Exit/Node 上的常驻代理，用于路径健康与故障切换。Mesh 向导安装它们；安装时各 VPS 从 GitHub 下载工具。",
},
"Q061": {
"fa": "خیر — ایجنت‌ها روی سرور وقتی برنامه Windows بسته است هم کار می‌کنند. برنامه برای نصب/وضعیت/تعمیر است.",
"ru": "Нет — агенты продолжают работать на серверах при закрытом Windows-приложении. Приложение нужно для установки/статуса/ремонта.",
"zh": "不需要——Windows 应用关闭后代理仍在服务器运行。应用用于安装/状态/修复。",
},
"Q062": {
"fa": "Mesh را دوباره Deploy کنید و Refresh Status بزنید. برچسب‌ها: نصب‌شده/غایب، Running/Stopped/نامشخص. نتیجه: «Mesh agents installed: X ok, Y failed».",
"ru": "Снова Deploy mesh и Refresh Status. Метки: installed/missing, Running/Stopped/unknown. Итог: «Mesh agents installed: X ok, Y failed».",
"zh": "重新 Deploy Mesh 并 Refresh Status。标签：已安装/缺失、Running/Stopped/未知。结果形如 “Mesh agents installed: X ok, Y failed”。",
},
"Q063": {
"fa": "ویزارد ربات تلگرام که Mirza را روی میزبان انتخابی نصب می‌کند و اعتبار پنل را پر می‌کند. گزینه‌ها: نصب Mirza، ذخیره ربات دیگر، یا انتقال. توکن بات و ادمین لازم است.",
"ru": "Мастер Telegram-бота: ставит Mirza на выбранный хост и подставляет credentials панели. Варианты: Install Mirza, другой бот, Move. Нужны bot token и admin.",
"zh": "Telegram 机器人向导：在选定主机安装 Mirza 并预填面板凭据。选项：安装 Mirza、保存其他机器人或迁移。需要 bot token 与管理员。",
},
"Q064": {
"fa": "بله — گزینه Move existing bot در انتخابگر هست. قبل از Update/Move پشتیبان توصیه می‌شود.",
"ru": "Да — в chooser есть Move existing bot. Перед Update/Move рекомендуется backup.",
"zh": "可以——选择器含 Move existing bot。Update/Move 前建议备份。",
},
"Q065": {
"fa": "چند زبان UI از جمله انگلیسی، فارسی، روسی، عربی، آلمانی، فرانسوی، هندی، ترکی و غیره. انتخاب زبان در شروع؛ Settings → Language روی همه تب‌ها اعمال می‌شود. فارسی RTL است.",
"ru": "Много языков UI: английский, фарси, русский, арабский, немецкий, французский, хинди, турецкий и др. Старт + Settings → Language. Персидский — RTL.",
"zh": "多语言 UI：英语、波斯语、俄语、阿拉伯语、德语、法语、印地语、土耳其语等。首次选择；Settings → Language 作用于全部标签。波斯语为 RTL。",
},
"Q066": {
"fa": "Setup زیر LocalAppData\\Programs نصب می‌شود؛ Portable با `portable.txt` داده را کنار exe می‌گذارد. برای مشتری معمولاً `Black Fox Vpn-Installer-Setup.exe` پایدارتر است.",
"ru": "Setup ставится в LocalAppData\\Programs; Portable с `portable.txt` хранит данные рядом с exe. Клиентам обычно лучше Setup.exe.",
"zh": "Setup 安装到 LocalAppData\\Programs；Portable 凭 `portable.txt` 把数据放在 exe 旁。客户通常更推荐 Setup.exe。",
},
"Q067": {
"fa": "تاریخچه محلی (SSH، لاگ، وضعیت Deploy، CDN محلی و…) را پاک می‌کند؛ سرور ریموت را تغییر نمی‌دهد؛ زبان، حالت و لایسنس می‌ماند.",
"ru": "Чистит локальную историю (SSH, логи, deploy-статус, локальный CDN…) без изменения удалённых серверов; язык, режим и лицензия остаются.",
"zh": "清除本地历史（SSH、日志、部署状态、本地 CDN 等），不改远程服务器；保留语言、模式与 License。",
},
"Q068": {
"fa": "از Exitها WireGuard/microsocks/فایروال را برمی‌دارد و تونل‌های متناظر Central را پاک می‌کند؛ SSH را نگه می‌دارد. می‌توان همه یا یکی را حذف کرد؛ حذف Node در صورت امکان از پنل unregister می‌شود.",
"ru": "С Exit снимает WireGuard/microsocks/файрвол и чистит связанные туннели на Central; SSH сохраняет. Можно все или один; Node по возможности unregister с панели.",
"zh": "从 Exit 移除 WireGuard/microsocks/防火墙并清理 Central 对应隧道；保留 SSH。可删全部或单个；Node 尽可能从面板注销。",
},
"Q069": {
"fa": "نصب hopهای زنجیره Pro را برمی‌دارد؛ حذف یک hop ممکن است hopهای با شماره بالاتر را ریست کند. Exitهایی که هنوز از آن hop استفاده می‌کنند باید اول حذف شوند.",
"ru": "Снимает hop’ы Pro-цепочки; удаление одного hop может сбросить старшие номера. Exit, которые ещё используют hop, нужно удалить сначала.",
"zh": "移除 Pro 链路 hop；删除一个 hop 可能重置更高序号。仍依赖该 hop 的 Exit 须先删除。",
},
"Q070": {
"fa": "WireGuard و پنل را از همه سرورهای پیکربندی‌شده برمی‌دارد و داده Deploy محلی را پاک می‌کند؛ SSH را نگه می‌دارد. با Factory Reset سطح OS فرق دارد.",
"ru": "Снимает WireGuard и панель со всех настроенных серверов и чистит локальные deploy-данные; SSH оставляет. Это не Factory Reset ОС.",
"zh": "从所有已配置服务器移除 WireGuard 与面板并清除本地部署数据；保留 SSH。不同于 OS 级 Factory Reset。",
},
"Q071": {
"fa": "ریست مخرب ریموت به‌سوی VPS تازه؛ رمز این عملیات ذخیره نمی‌شود. داده، سرویس‌ها، بسته‌های VPN، تونل، فایروال، کاربران و تنظیمات سفارشی را هدف می‌گیرد. OS نامعتبر fail می‌شود.",
"ru": "Разрушительный remote-сброс к «свежему» VPS; пароль этой операции не хранится. Цель — данные, сервисы, VPN-пакеты, туннели, файрвол, пользователи. Неподдерживаемая ОС падает.",
"zh": "破坏性远程重置趋向全新 VPS；此次操作的密码不保存。针对数据、服务、VPN 包、隧道、防火墙、用户与自定义设置。不支持的系统会失败。",
},
"Q072": {
"fa": "خیر — زبان، حالت برنامه و فعال‌سازی لایسنس نگه داشته می‌شوند. توجه: نصب مجدد Windows ممکن است Device ID را عوض کند → Reactivation.",
"ru": "Нет — язык, режим и активация лицензии сохраняются. Но переустановка Windows может сменить Device ID → Reactivation.",
"zh": "不会——保留语言、模式与 License 激活。但重装 Windows 可能改变 Device ID → 使用 Reactivation。",
},
"Q073": {
"fa": "Settings → Update BlackFox & Wallet Address؛ در صورت force ممکن است نسخه قدیمی قفل شود و باید Setup جدید از هاب/سایت رسمی نصب شود.",
"ru": "Settings → Update BlackFox & Wallet Address; при force старая версия блокируется — ставьте новый Setup с хаба/официального сайта.",
"zh": "Settings → Update BlackFox & Wallet Address；强制更新时旧版会被挡住，需安装官网/Hub 的新 Setup。",
},
"Q074": {
"fa": "آخرین بسته پنل Sanaei را در کش محلی برای نصب‌های بعدی می‌گیرد؛ به‌تنهایی پنل زنده روی سرور را ارتقا نمی‌دهد مگر عملیات نصب/به‌روز را اجرا کنید.",
"ru": "Качает свежий пакет панели Sanaei в локальный кэш для будущих установок; сам по себе живую панель не обновляет без install/update ops.",
"zh": "将最新 Sanaei 面板包下载到本地缓存供日后安装； alone 不会升级服务器上现网面板，除非再跑安装/更新操作。",
},
"Q075": {
"fa": "Windows سطح کامل عملیات Installer است؛ Android همراه با بسته‌بندی/موتور متفاوت و پرسونای AI مشترک است. برای Full Deploy/Mesh معمولاً Windows را ترجیح دهید.",
"ru": "Windows — полная ops-поверхность Installer; Android — компаньон с иной упаковкой/движком и общей AI-персоной. Для Full Deploy/Mesh обычно Windows.",
"zh": "Windows 是完整 Installer 运维面；Android 为配套应用（打包/引擎不同）并共享 AI 人设。Full Deploy/Mesh 通常优先 Windows。",
},
"Q076": {
"fa": "تلگرام `@HiBlackFoxVpn`، سایت foxnext.net، ایمیل support@foxnext.net و کانال `@BlackFoxVPN`. مقادیر زنده را از تب Contact بخوانید.",
"ru": "Telegram `@HiBlackFoxVpn`, сайт foxnext.net, email support@foxnext.net, канал `@BlackFoxVPN`. Смотрите живые значения на вкладке Contact.",
"zh": "Telegram `@HiBlackFoxVpn`、网站 foxnext.net、邮箱 support@foxnext.net、频道 `@BlackFoxVPN`。以 Contact 标签实时值为准。",
},
"Q077": {
"fa": "Device ID، حالت برنامه، نام عملیات، تکه ترمینال، نوع TX/کد (در چت عمومی رمز کامل ندهید). خروجی Diagnostic مفید است.",
"ru": "Device ID, режим приложения, имя операции, фрагмент terminal, тип TX/кода (не светите полный секрет в публичном чате). Полезен Diagnostic export.",
"zh": "提供 Device ID、应用模式、操作名、终端片段、TX/代码类型（公开聊天勿贴完整密钥）。Diagnostic 导出很有用。",
},
"Q078": {
"fa": "پل MCP محلی تا ابزارهای AI بیرونی وقتی برنامه باز است از Black Fox استفاده کنند. Activate MCP، کپی mcp.json، در تنظیمات MCP کلاینت بچسبانید. برنامه باید باز بماند.",
"ru": "Локальный MCP-мост: внешние AI-приложения используют инструменты Black Fox, пока приложение открыто. Activate MCP, скопируйте mcp.json в настройки клиента.",
"zh": "本地 MCP 桥：外部 AI 应用在本程序保持打开时可调用 Black Fox 工具。Activate MCP，复制 mcp.json 到客户端 MCP 设置。",
},
"Q079": {
"fa": "باید AI Pro را در Registration باز کنید (`view.ai_pro_locked`). فقط Basic یا Pro برای چت AI کافی نیست.",
"ru": "Нужно разблокировать AI Pro в Registration (`view.ai_pro_locked`). Одного Basic/Pro для AI-чата недостаточно.",
"zh": "须在 Registration 解锁 AI Pro（`view.ai_pro_locked`）。仅有 Basic/Pro 不足以使用 AI 聊天。",
},
"Q080": {
"fa": "سهمیه تمام شده؛ با BFXQ شارژ کنید یا به پشتیبانی برای تمدید پیام دهید. کدهای `ai.quota.exhausted` / expired / not_found / disabled هم ممکن است.",
"ru": "Квота исчерпана; пополните BFXQ или напишите в поддержку. Возможны `ai.quota.exhausted` / expired / not_found / disabled.",
"zh": "配额已用尽；用 BFXQ 充值或联系支持续期。也可能出现 `ai.quota.exhausted` / expired / not_found / disabled。",
},
}
