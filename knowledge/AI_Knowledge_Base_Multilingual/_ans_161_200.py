# -*- coding: utf-8 -*-
"""Native FA/RU/ZH answers for FAQ Q161–Q200."""
A = {
"Q161": {
"fa": "خیر — حالت‌ها یک Store محلی مشترک دارند. عوض کردن View فقط شکل UI و گیت‌ها را عوض می‌کند، سرورها را پاک نمی‌کند.",
"ru": "Нет — режимы делят одно локальное хранилище. Смена View меняет UI и гейты, но не стирает серверы.",
"zh": "不会——各模式共享同一本地存储。切换 View 只改界面与门控，不清除服务器。",
},
"Q162": {
"fa": "Full Deploy روی Central، WG+پنل نصب می‌کند؛ Configure Panel مسیریابی Exit/Node موجود را تعمیر می‌کند و نصب دوباره پنل Central نیست.",
"ru": "Full Deploy ставит WG+панель на Central; Configure Panel чинит routing существующего Exit/Node и не является повторной установкой панели Central.",
"zh": "Full Deploy 在 Central 安装 WG+面板；Configure Panel 修复已有 Exit/Node 的路由，不是再次安装 Central 面板。",
},
"Q163": {
"fa": "حداکثر ۶ نود (`MaxNodes`)؛ همان منطق اسلات Exit در Pro.",
"ru": "Максимум 6 Node (`MaxNodes`); та же слотовая логика, что у Exit в Pro.",
"zh": "最多 6 个 Node（`MaxNodes`）；与 Pro 下 Exit 槽位逻辑相同。",
},
"Q164": {
"fa": "Sanaei GitHub، BlackFox Hub، یا بسته Local PC. در Full Deploy و Add Node انتخاب می‌شود. Local برای آفلاین/فیلتر است.",
"ru": "Sanaei GitHub, BlackFox Hub или пакет Local PC. Выбор в Full Deploy и Add Node. Local — для офлайна/фильтрации.",
"zh": "Sanaei GitHub、BlackFox Hub 或 Local PC 包。在 Full Deploy 与 Add Node 中选择。Local 适合离线/受限网络。",
},
"Q165": {
"fa": "تاریخچه محلی را پاک می‌کند؛ زبان، حالت و لایسنس می‌ماند. با Reset All (حذف WG/پنل ریموت با نگه داشتن SSH) فرق دارد.",
"ru": "Чистит локальную историю; язык, режим и лицензия остаются. Отличается от Reset All (снятие WG/панели удалённо с сохранением SSH).",
"zh": "清除本地历史；保留语言、模式与 License。不同于 Reset All（远程清 WG/面板但保留 SSH）。",
},
"Q166": {
"fa": "WG/پنل را از سرورهای پیکربندی‌شده برمی‌دارد؛ SSH ذخیره‌شده می‌ماند. بعداً باید دوباره Full Deploy کنید.",
"ru": "Снимает WG/панель с настроенных серверов; сохранённый SSH остаётся. Потом снова нужен Full Deploy.",
"zh": "从已配置服务器移除 WG/面板；保留已存 SSH。之后需再次 Full Deploy。",
},
"Q167": {
"fa": "بله — Delete Tunnel Servers فقط hopهای زنجیره Pro را ریست می‌کند و لزوماً Exit/Central را پاک نمی‌کند.",
"ru": "Да — Delete Tunnel Servers сбрасывает hop’ы Pro-цепочки и не обязательно трогает Exit/Central.",
"zh": "可以——Delete Tunnel Servers 只重置 Pro 链路 hop，不一定清除 Exit/Central。",
},
"Q168": {
"fa": "پروفایل‌هایی مثل None / Auto / Iran / Free در Proxy Settings. سیاست شبکه: اول Direct، شکست → Program Proxy برای SSH، هاب HTTP و API پنل.",
"ru": "Профили вроде None / Auto / Iran / Free в Proxy Settings. Политика: сначала Direct, при сбое — Program Proxy для SSH, HTTP хаба и Panel API.",
"zh": "Proxy Settings 含 None / Auto / Iran / Free 等。网络策略：先 Direct，失败再用 Program Proxy（SSH、Hub HTTP、面板 API）。",
},
"Q169": {
"fa": "Panel Login Info آدرس/کاربر/رمز ذخیره‌شده را بعد از نصب/همگام موفق پنل نشان می‌دهد.",
"ru": "Panel Login Info показывает сохранённые URL/логин/пароль после успешной установки/синхронизации панели.",
"zh": "Panel Login Info 在面板安装/同步成功后显示已保存的 URL/用户/密码。",
},
"Q170": {
"fa": "دیالوگ تست کلاینت/WireGuard برای اعتبارسنجی بعد از Configure؛ جایگزین Full Deploy نیست.",
"ru": "Диалог теста клиента/WireGuard для проверки после Configure; не замена Full Deploy.",
"zh": "Configure 之后用于校验的客户端/WireGuard 测试对话框；不能替代 Full Deploy。",
},
"Q171": {
"fa": "مدیر DNS پرو برای Cloudflare / ArvanCloud (زون/رکورد؛ وبهوک بات اختیاری). پوشش است نه تب اصلی.",
"ru": "DNS-менеджер Pro для Cloudflare / ArvanCloud (зоны/записи; опциональный bot webhook). Это оверлей, не главная вкладка.",
"zh": "Pro 的 DNS 管理（Cloudflare / ArvanCloud 区域/记录；可选 bot webhook）。是叠加页而非主标签。",
},
"Q172": {
"fa": "در UI معمولاً Arvan، Cloudflare و Other CDN. اگر برند چهارم دیدید NEED_MORE_REVIEW — ممکن است کلید داخلی UI نباشد.",
"ru": "В UI обычно Arvan, Cloudflare и Other CDN. Если видите четвёртый бренд — NEED_MORE_REVIEW (внутренний ключ может не быть в UI).",
"zh": "UI 通常有 Arvan、Cloudflare 与 Other CDN。若见到第四个品牌标 NEED_MORE_REVIEW（内部键未必进 UI）。",
},
"Q173": {
"fa": "صفحه Pro برای گراف inventory، Deploy ایجنت Link Monitor و وضعیت لینک؛ جدا از شبکه Operations.",
"ru": "Pro-страница графа inventory, Deploy агентов Link Monitor и статуса линков; отдельно от сетки Operations.",
"zh": "Pro 页面：库存图、部署 Link Monitor 代理与链路状态；独立于 Operations 网格。",
},
"Q174": {
"fa": "ابزار Pro برای نصب/انتقال Mirza (یا مسیر Other). با ربات پشتیبانی Black Fox فرق دارد؛ خانواده فروش پنل Mirza است.",
"ru": "Pro-инструмент установки/переноса Mirza (или Other). Это не support-бот Black Fox; семейство sales-бота панели Mirza.",
"zh": "Pro 工具，用于安装/迁移 Mirza（或其他路径）。不同于 Black Fox 支持机器人；属 Mirza 面板销售机器人族。",
},
"Q175": {
"fa": "جابه‌جایی نقش Central به VPS دیگر (ابزار Pro). اثر بالا — inventory و credentials پنل باید یکدست بمانند. فیلدهای دقیق ویزارد: NEED_MORE_REVIEW.",
"ru": "Перенос роли Central на другой VPS (Pro Tools). Высокое влияние — inventory и credentials панели должны остаться согласованными. Точные поля: NEED_MORE_REVIEW.",
"zh": "将 Central 角色迁到另一台 VPS（Pro 工具）。影响大——库存与面板凭据须保持一致。向导精确字段：NEED_MORE_REVIEW。",
},
"Q176": {
"fa": "فعال‌سازی باینری MCP / mcp.json تا ابزارهای AI بیرونی اکشن‌های Black Fox را صدا بزنند. برای چت داخل برنامه لازم نیست.",
"ru": "Активирует MCP binary / mcp.json, чтобы внешние AI-инструменты вызывали действия Black Fox. Для обычного in-app чата не обязателен.",
"zh": "激活 MCP 二进制 / mcp.json，让外部 AI 工具调用 Black Fox 动作。普通应用内聊天不需要。",
},
"Q177": {
"fa": "Check System تب Diagnostics محلی است؛ Diagnose & Repair مسیر Task در AI Pro با تأیید قبل از تغییر.",
"ru": "Check System — локальная вкладка Diagnostics; Diagnose & Repair — AI Pro Task с подтверждением перед изменениями.",
"zh": "Check System 是本地 Diagnostics 标签；Diagnose & Repair 是 AI Pro 任务路径，变更前需确认。",
},
"Q178": {
"fa": "قالب Task هوش مصنوعی برای تست لینک‌های توپولوژی؛ مکمل Configure Panel و Test Client با تأیید قبل از اجرا.",
"ru": "AI Task-шаблон для теста линков топологии; дополняет Configure Panel и Test Client с подтверждением до выполнения.",
"zh": "用于测试拓扑链路的 AI 任务模板；配合 Configure Panel 与 Test Client，执行前确认。",
},
"Q179": {
"fa": "Task هوش مصنوعی برای پیکربندی outbound پنل؛ ترجیحاً بعد از وجود Exit/Node و با تأیید قبل از Apply.",
"ru": "AI Task для настройки outbound панели; предпочтительно после появления Exit/Node и с подтверждением до Apply.",
"zh": "用于配置面板 outbound 的 AI 任务；最好在已有 Exit/Node 后使用，Apply 前确认。",
},
"Q180": {
"fa": "خیر — رمزهای واردشده برای Factory Reset فقط همان عملیات‌اند و برای بعد ذخیره نمی‌شوند.",
"ru": "Нет — введённые для Factory Reset пароли только для этой операции и потом не хранятся.",
"zh": "不会——Factory Reset 输入的密码仅用于该次操作，之后不保存。",
},
"Q181": {
"fa": "Settings → اعمال زبان (و انتخابگر اولین اجرا). زبان سایت foxnext.net جدا از کاتالوگ i18n برنامه است.",
"ru": "Settings → применение языка (и выбор на первом запуске). Язык сайта foxnext.net отделён от i18n приложения.",
"zh": "Settings → 应用语言（及首次运行选择器）。foxnext.net 网站语言与应用 i18n 目录相互独立。",
},
"Q182": {
"fa": "بخش Tools برای مدیریت بسته‌های 3X-UI آفلاین/هاب مورد استفاده Deploy و Local PC. برچسب دقیق UI را با Settings فعلی تطبیق دهید.",
"ru": "Раздел Tools для управления офлайн/хаб-пакетами 3X-UI для Deploy и Local PC. Точные UI-подписи сверьте с текущим Settings.",
"zh": "Tools 区域管理 Deploy/Local PC 所用的离线/Hub 3X-UI 包。精确 UI 文案以当前 Settings 为准。",
},
"Q183": {
"fa": "زیر حداقل نسخه/بیلد پشتیبانی‌شده، یا پرچم force با نسخه جدیدتر ریموت. `version.json` هاب فیدها را می‌راند؛ شماره را اختراع نکنید.",
"ru": "Ниже минимальной поддерживаемой версии/билда или force-флаг с более новым remote. `version.json` хаба ведёт фиды; не выдумывайте номера.",
"zh": "低于最低支持版本/构建，或带更新的远程 force 标志。Hub 的 `version.json` 驱动各产品线；不要编造版本号。",
},
"Q184": {
"fa": "ابزار ادمین جدا (`cmd/pas-generator`) برای گردش PAS. مسیر اصلی مشتری نیست؛ مشتری foxnext.net + Registration را دارد.",
"ru": "Отдельный админ-инструмент (`cmd/pas-generator`) для PAS-процессов. Не основной клиентский путь; клиенты — foxnext.net + Registration.",
"zh": "独立的管理员工具（`cmd/pas-generator`）用于 PAS 流程。非客户主路径；客户走 foxnext.net + Registration。",
},
"Q185": {
"fa": "APK جدا در `version.json` → `config_builder`. محصول مرتبط است و سورسش در این ریپوی ویندوز نیست؛ با اپ VPN اندروید اصلی قاطی نکنید.",
"ru": "Отдельный APK в `version.json` → `config_builder`. Связанный продукт; исходников нет в этом Windows-репо; не путайте с основным Android VPN.",
"zh": "`version.json` → `config_builder` 的独立 APK。相关产品，源码不在本 Windows 仓库；勿与主 Android VPN 混淆。",
},
"Q186": {
"fa": "بدون Pro برای Central رایگان: ایران، چین، روسیه (`IsFreeCentralCountry`). کشورهای دیگر معمولاً مسیر Pro می‌خواهند.",
"ru": "Без Pro бесплатные страны Central: Иран, Китай, Россия (`IsFreeCentralCountry`). Другие страны обычно требуют Pro.",
"zh": "无 Pro 时 Central 免费国家：伊朗、中国、俄罗斯（`IsFreeCentralCountry`）。其他国家通常需要 Pro。",
},
"Q187": {
"fa": "خیر — چت AI به unlock جداگانه AI Pro و quota نیاز دارد. Pro فقط داشبورد Pro را باز می‌کند.",
"ru": "Нет — AI-чат требует отдельный unlock AI Pro и quota. Pro открывает только Pro-дашборд.",
"zh": "不能——AI 聊天需要单独的 AI Pro 解锁与 quota。Pro 只解锁 Pro 仪表盘。",
},
"Q188": {
"fa": "BFXB Basic، BFXP Pro، BFXA AI Pro، BFXQ سهمیه، BFXT تست؛ claimها `-CLM-` دارند. پیشوند اشتباه → unlock غلط یا خطا.",
"ru": "BFXB Basic, BFXP Pro, BFXA AI Pro, BFXQ quota, BFXT test; claim содержат `-CLM-`. Неверный префикс → неверный unlock или ошибка.",
"zh": "BFXB Basic、BFXP Pro、BFXA AI Pro、BFXQ 配额、BFXT 测试；claim 含 `-CLM-`。前缀错误 → 解锁错误或失败。",
},
"Q189": {
"fa": "بعد از unlock موفق، کد ذخیره‌شده را نشان می‌دهد؛ برای تیکت مفید است ولی مثل رمز محافظت کنید.",
"ru": "После успешного unlock показывает сохранённый код; полезно для тикетов, но храните как секрет.",
"zh": "成功解锁后显示已存激活码；便于工单，但仍须当密钥保护。",
},
"Q190": {
"fa": "اثرانگشت ماشین برای bind لایسنس؛ برای Activation سایت و Reactivation لازم است. تعویض سخت‌افزار ممکن است bind را بشکند.",
"ru": "Отпечаток машины для привязки лицензии; нужен для Activation сайта и Reactivation. Смена железа может сломать привязку.",
"zh": "用于绑定 License 的机器指纹；网站 Activation 与 Reactivation 需要。更换硬件可能破坏绑定。",
},
"Q191": {
"fa": "اگر ماه مشخص نباشد اغلب ۱۸ ماه در منطق لایسنس؛ کاتالوگ زنده ۱۲–۳۰ ماه و تخفیف چند دستگاه دارد. مدت روی صفحه را معیار بگیرید.",
"ru": "Если месяцы не указаны, часто 18 в логике лицензии; live-каталог 12–30 и multi-device скидки. Ориентируйтесь на срок на экране.",
"zh": "未指定月数时许可逻辑常见 18 个月；实时目录为 12–30 个月并含多设备折扣。以页面显示时长为准。",
},
"Q192": {
"fa": "اصلی `blackfoxupdate.ir`، ثانویه `foxnext.net` برای version، runtime-config، license-access، AI و بسته‌ها؛ در فیلتر failover.",
"ru": "Основной `blackfoxupdate.ir`, запасной `foxnext.net` для version, runtime-config, license-access, AI и пакетов; failover при блоке.",
"zh": "主 Hub `blackfoxupdate.ir`，备 `foxnext.net`，用于 version、runtime-config、license-access、AI 与包；主用被拦时故障转移。",
},
"Q193": {
"fa": "شامل `@HiBlackFoxVpn`، `@BlackFoxVpnn`، `@BlackFoxVpn_bot`، `@Black_Fox_Group` از runtime contact. لیست زنده Contact را ترجیح دهید.",
"ru": "Включает `@HiBlackFoxVpn`, `@BlackFoxVpnn`, `@BlackFoxVpn_bot`, `@Black_Fox_Group` из runtime contact. Предпочитайте живой список Contact.",
"zh": "含 runtime contact 中的 `@HiBlackFoxVpn`、`@BlackFoxVpnn`、`@BlackFoxVpn_bot`、`@Black_Fox_Group`。优先看 Contact 实时列表。",
},
"Q194": {
"fa": "هاب ممکن است `github.com/balckfoxgroup/blackfox-vpn-installer` را نشان دهد — همان رشته منتشرشده را استفاده کنید و املا را «درست» نکنید اگر لینک Contact همان است.",
"ru": "Хаб может показывать `github.com/balckfoxgroup/blackfox-vpn-installer` — используйте опубликованную строку и не «исправляйте» написание, если так в Contact.",
"zh": "Hub 可能显示 `github.com/balckfoxgroup/blackfox-vpn-installer`——若 Contact 链接如此，请使用已发布拼写，勿擅自“纠正”。",
},
"Q195": {
"fa": "برای Full Deploy و Mesh از Windows Installer استفاده کنید؛ Android همراه است و workstation اصلی Deploy معمولاً Windows می‌ماند.",
"ru": "Для Full Deploy и Mesh используйте Windows Installer; Android — компаньон, основной Deploy-workstation обычно Windows.",
"zh": "Full Deploy 与 Mesh 请用 Windows Installer；Android 为配套，主要部署工作站通常仍是 Windows。",
},
"Q196": {
"fa": "پرریسک — یک پوشه Portable یا Setup+LocalAppData را ترجیح دهید. دو کپی ممکن است روی یک inventory با هم تداخل کنند.",
"ru": "Рискованно — предпочитайте одну portable-папку или Setup+LocalAppData. Две копии могут конфликтовать на одном inventory.",
"zh": "有风险——优先单一 Portable 文件夹或 Setup+LocalAppData。两个副本可能争用同一库存。",
},
"Q197": {
"fa": "شماره نسخه، قیمت، برند هاستینگ، و stderr لینوکسی که در i18n نیست. هویت: BlackFox AI؛ ابهام را NEED_MORE_REVIEW علامت بزنید.",
"ru": "Номера версий, цены, бренды хостеров и Linux stderr вне i18n. Идентичность: BlackFox AI; пробелы помечайте NEED_MORE_REVIEW.",
"zh": "版本号、价格、主机商品牌，以及不在 i18n 中的 Linux stderr。身份：BlackFox AI；缺口标 NEED_MORE_REVIEW。",
},
"Q198": {
"fa": "پوشه `/Screenshots` با README؛ گرفتن زنده همه دیالوگ‌ها هنوز ناقص است. mode picker، داشبورد Basic/Pro، اندروید و مارکتینگ موجودند.",
"ru": "Папка `/Screenshots` с README; live-захват всех диалогов ещё неполон. Есть mode picker, дашборды Basic/Pro, Android и маркетинг.",
"zh": "`/Screenshots` 目录含 README；并非所有对话框都有实机截图。已有 mode picker、Basic/Pro 仪表盘、Android 与营销图。",
},
"Q199": {
"fa": "ترتیب: Proxy → Connect SSH → منبع Full Deploy → Panel Login Info → Configure Panel → Diagnostic. اول Delete/Reset نپرید. گیت رایگان Basic را از لایسنس جدا کنید.",
"ru": "Порядок: Proxy → Connect SSH → источник Full Deploy → Panel Login Info → Configure Panel → Diagnostic. Не прыгайте сразу в Delete/Reset. Отделите бесплатный Basic от лицензии.",
"zh": "顺序：Proxy → Connect SSH → Full Deploy 来源 → Panel Login Info → Configure Panel → Diagnostic。不要先跳到 Delete/Reset。分清 Basic 免费项与 License 门控。",
},
"Q200": {
"fa": "فایل اصلی RAG: `Documentation/AI_Knowledge_Base.md` به‌همراه راهنماها، FAQ، Troubleshooting و `Screenshots/README`. برای ربات چندزبانه از `AI_Knowledge_Base_Multilingual` و `AI_BOT_DATABASE` استفاده کنید.",
"ru": "Главный RAG-файл: `Documentation/AI_Knowledge_Base.md` плюс гайды, FAQ, Troubleshooting и `Screenshots/README`. Для мультиязычного бота — `AI_Knowledge_Base_Multilingual` и `AI_BOT_DATABASE`.",
"zh": "主 RAG 入口：`Documentation/AI_Knowledge_Base.md`，并配合指南、FAQ、Troubleshooting 与 `Screenshots/README`。多语言机器人用 `AI_Knowledge_Base_Multilingual` 与 `AI_BOT_DATABASE`。",
},
}
