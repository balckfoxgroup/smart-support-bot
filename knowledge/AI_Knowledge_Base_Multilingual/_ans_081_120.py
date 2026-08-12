# -*- coding: utf-8 -*-
"""Native FA/RU/ZH answers for FAQ Q081–Q120."""
A = {
"Q081": {
"fa": "تا ۳ تصویر و ۵ فایل متنی در هر پیام. بیش از حد با `too_many_images` / `too_many_text_files` رد می‌شود.",
"ru": "До 3 изображений и 5 текстовых файлов на сообщение. Лишнее отклоняется (`too_many_images` / `too_many_text_files`).",
"zh": "每条消息最多 3 张图、5 个文本文件。超出返回 `too_many_images` / `too_many_text_files`。",
},
"Q082": {
"fa": "خیر — ابتدا تحلیل، سپس تأیید Yes/No، بعد اجرا. فقط صف‌کردن اکشن کافی نیست؛ باید تأیید شود.",
"ru": "Нет — сначала анализ, затем подтверждение Yes/No, потом выполнение. Одна постановка в очередь без подтверждения не запускает.",
"zh": "不会——先分析，再 Yes/No 确认，然后执行。仅入队不等于执行。",
},
"Q083": {
"fa": "تا پایان فرایند در ترمینال/وضعیت صبر کنید؛ پنجره busy را بی‌دلیل نبندید. وضعیت‌ها: wait / done / failed.",
"ru": "Дождитесь завершения в terminal/статусе; не закрывайте busy-окно без нужды. Статусы: wait / done / failed.",
"zh": "等待终端/状态完成；勿随意关闭 busy 窗口。状态含 wait / done / failed。",
},
"Q084": {
"fa": "بله در AI Pro — JSON outbound را بچسبانید؛ سقف ۱۰ outbound مصنوعی روی پنل. حذف در UI پنل شمارنده AI را ریست نمی‌کند. JSON نامعتبر رد می‌شود.",
"ru": "Да в AI Pro — вставьте outbound JSON; максимум 10 AI-outbound на панели. Удаление в UI панели не сбрасывает счётчик AI. Невалидный JSON отклоняется.",
"zh": "可以（AI Pro）——粘贴 outbound JSON；面板上 AI outbound 最多 10 条。在面板 UI 删除不会重置 AI 计数器。无效 JSON 会被拒绝。",
},
"Q085": {
"fa": "راهنمای Configure Panel معمولاً ۴۴۳ VLESS، ۸۰ Trojan، ۸۰۸۰ WireGuard را ذکر می‌کند؛ نصب واقعی را از Panel Login Info / تست کلاینت تأیید کنید.",
"ru": "Подсказка Configure Panel обычно: 443 VLESS, 80 Trojan, 8080 WireGuard; фактические порты сверьте в Panel Login Info / client test.",
"zh": "Configure Panel 提示通常为 443 VLESS、80 Trojan、8080 WireGuard；以 Panel Login Info / 客户端测试的实际端口为准。",
},
"Q086": {
"fa": "اول Full Deploy را کامل کنید تا URL/کاربر/رمز/توکن پنل ذخیره شود. بسیاری عملیات به این credentials وابسته‌اند.",
"ru": "Сначала завершите Full Deploy, чтобы сохранились URL/логин/пароль/токен панели. Многие операции зависят от этих credentials.",
"zh": "请先完成 Full Deploy 以保存面板 URL/用户/密码/令牌。许多操作依赖这些凭据。",
},
"Q087": {
"fa": "بعد از ری‌اینستال VPS رایج است؛ فقط اگر به سرور اعتماد دارید Accept کنید. دیالوگ احتمال MITM را هم هشدار می‌دهد؛ Accept کلید ذخیره‌شده را پاک و retry می‌کند.",
"ru": "Часто после переустановки VPS; Accept только если доверяете серверу. Диалог предупреждает о возможном MITM; Accept очищает ключ и делает retry.",
"zh": "常见于 VPS 重装后；仅在信任该服务器时 Accept。对话框也会提示可能 MITM；Accept 会清除已存密钥并重试。",
},
"Q088": {
"fa": "رمز و کلید هر دو نامعتبر/منقضی‌اند؛ مقدار غلط ذخیره نمی‌شود. عنوان: SSH authentication failed.",
"ru": "И пароль, и ключ неверны/истекли; неверное не сохраняется. Заголовок: SSH authentication failed.",
"zh": "密码与密钥均无效/过期；错误值不会保存。标题：SSH authentication failed。",
},
"Q089": {
"fa": "برنامه جریان Change Linux Password را نشان می‌دهد (رمز فعلی/جدید/تأیید). موفقیت یا mismatch/required/failed.",
"ru": "Приложение показывает Change Linux Password (текущий/новый/подтверждение). Успех или mismatch/required/failed.",
"zh": "应用会进入 Change Linux Password（当前/新/确认）。结果为成功或 mismatch/required/failed。",
},
"Q090": {
"fa": "فیلتر شبکه، IP/پورت غلط، فایروال فروشنده، یا نیاز به Proxy. لزوماً رمز اشتباه نیست (`log.ssh_timeout`).",
"ru": "Фильтр сети, неверный IP/порт, файрвол провайдера или нужен Proxy. Не обязательно неверный пароль (`log.ssh_timeout`).",
"zh": "网络过滤、错误 IP/端口、商家防火墙或需要 Proxy。不一定是密码错误（`log.ssh_timeout`）。",
},
"Q091": {
"fa": "نقشه توپولوژی وقتی پنل آماده است یا لینک‌ها Deploy شده و کلاینت پنل وجود دارد. در غیر این صورت `topology_not_ready`.",
"ru": "Карта топологии появляется при готовой панели или задеплоенных линках + клиенте панели. Иначе `topology_not_ready`.",
"zh": "面板就绪，或链路已部署且存在面板客户端时显示拓扑；否则 `topology_not_ready`。",
},
"Q092": {
"fa": "افزودن outbound روی پنل (دستی یا JSON سفارشی در AI Pro) برای مسیر Exitها و مسیریابی.",
"ru": "Добавление outbound на панели (вручную или кастомный JSON в AI Pro) для Exit и маршрутизации.",
"zh": "在面板添加 outbound（手动或在 AI Pro 粘贴自定义 JSON），用于 Exit 与路由。",
},
"Q093": {
"fa": "CDN در مجموعه قابلیت‌های Pro است؛ Basic روی Central+Exit تمرکز دارد و CDN را مثل Pro باز نمی‌کند.",
"ru": "CDN входит в набор Pro; Basic фокусируется на Central+Exit и не позиционирует CDN как Pro.",
"zh": "CDN 属于 Pro 能力集；Basic 聚焦 Central+Exit，不会像 Pro 那样开放 CDN。",
},
"Q094": {
"fa": "Cloudflare (ایمیل + API token با Zone:DNS:Edit) و ArvanCloud (کاربر ماشین + API key). ساب‌دامین وبهوک بات اختیاری و جدا از دامنه پنل است.",
"ru": "Cloudflare (email + API token Zone:DNS:Edit) и ArvanCloud (machine user + API key). Опциональный bot webhook subdomain отдельно от панели.",
"zh": "Cloudflare（邮箱 + Zone:DNS:Edit 的 API token）与 ArvanCloud（机器用户 + API key）。可选 bot webhook 子域与面板域名分开。",
},
"Q095": {
"fa": "ساب‌دامین اختیاری برای وبهوک تلگرام بات؛ اگر لازم نیست رد شوید — دامنه پنل نیست.",
"ru": "Опциональный subdomain для Telegram bot webhook; если не нужен — пропустите; это не домен панели.",
"zh": "可选的 Telegram bot webhook 子域；不需要就跳过——不是面板域名。",
},
"Q096": {
"fa": "بررسی/تعمیر گسترده‌تر (دیسک/ترافیک، پینگ/فیلتر، لینک مش، دامنه/CDN، پارامترهای خراب). به‌صورت Task AI/عملیات؛ فقط وقتی IP یا رمز جدید لازم است می‌پرسد.",
"ru": "Более широкая проверка/починка (диск/трафик, ping/фильтр, mesh-линки, DNS/CDN, битые параметры). Как AI task/ops; спрашивает только если нужны новый IP или секрет.",
"zh": "更广的检查/修复（磁盘/流量、ping/过滤、Mesh 链路、域名/CDN、损坏参数）。作为 AI 任务/运维；仅在需要新 IP 或密钥时询问。",
},
"Q097": {
"fa": "عملیات طولانی در جریان است؛ صبر کنید تا تمام شود. بستن زودهنگام ناقص‌ماندن کار را هشدار می‌دهد.",
"ru": "Идёт длинная операция; дождитесь завершения. Раннее закрытие предупреждает о незавершённой работе.",
"zh": "长操作进行中；请等待完成。过早关闭会提示工作未完成。",
},
"Q098": {
"fa": "بله — دکمه Stop ترمینال با تأیید؛ فرایند فعلی را قطع می‌کند و به‌عنوان توقف کاربر علامت می‌خورد.",
"ru": "Да — Terminal Stop с подтверждением; прерывает текущий процесс и помечает остановку пользователем.",
"zh": "可以——终端 Stop 需确认；会中断当前进程并标记为用户停止。",
},
"Q099": {
"fa": "در حالت نصب‌شده معمولاً زیر `%LocalAppData%\\Programs\\Black Fox Vpn`. در Portable کنار exe (با marker).",
"ru": "В установленном режиме обычно `%LocalAppData%\\Programs\\Black Fox Vpn`. В Portable — рядом с exe (с marker).",
"zh": "已安装模式通常在 `%LocalAppData%\\Programs\\Black Fox Vpn`。Portable 则在 exe 旁（有 marker）。",
},
"Q100": {
"fa": "دکمه‌های Copy اختصاصی با پیام موفقیت کلیپ‌بورد برای Device ID، wallet، TX و کد فعال‌سازی.",
"ru": "Отдельные кнопки Copy с тостом успеха буфера для Device ID, wallet, TX и кода активации.",
"zh": "专用 Copy 按钮，成功复制 Device ID、wallet、TX 与激活码时有提示。",
},
"Q101": {
"fa": "APIهای هاب می‌توانند کد/TX آفلاین را با پرچم claim_pending ثبت کنند. جزئیات همه دیالوگ‌های offline: در صورت ابهام NEED_MORE_REVIEW.",
"ru": "API хаба могут записывать offline-коды/TX с флагами claim_pending. Не все offline-диалоги сверены — при сомнении NEED_MORE_REVIEW.",
"zh": "Hub API 可用 claim_pending 记录离线代码/TX。并非所有离线对话框都已逐字核对——存疑标 NEED_MORE_REVIEW。",
},
"Q102": {
"fa": "BFXB=Basic، BFXP=Pro، BFXA=AI Pro، BFXQ=سهمیه AI. پیشوند اشتباه برای قابلیت هدف unlock را fail می‌کند.",
"ru": "BFXB=Basic, BFXP=Pro, BFXA=AI Pro, BFXQ=AI quota. Неверный префикс для целевой функции ломает unlock.",
"zh": "BFXB=Basic，BFXP=Pro，BFXA=AI Pro，BFXQ=AI quota。目标功能前缀错误会导致解锁失败。",
},
"Q103": {
"fa": "بله — AI Pro عملیات Pro را از چت می‌دهد و دسترسی دستی Pro را همزمان نگه می‌دارد؛ ولی گیت ویژه AI جداست.",
"ru": "Да — AI Pro даёт операции Pro через чат и одновременный ручной Pro; отдельный AI-gate всё равно нужен.",
"zh": "是——AI Pro 可通过聊天执行 Pro 操作并同时保留手动 Pro；但 AI 专用门控仍独立。",
},
"Q104": {
"fa": "خیر — unlock معمولی Pro هرگز AI Assistant Pro را باز نمی‌کند (`FeatureAIProFull`).",
"ru": "Нет — обычный Pro unlock никогда не выдаёт AI Assistant Pro (`FeatureAIProFull`).",
"zh": "不能——普通 Pro 解锁绝不会授予 AI Assistant Pro（`FeatureAIProFull`）。",
},
"Q105": {
"fa": "سایت بعد از پرداخت claim می‌دهد؛ برنامه هم می‌تواند TX را verify کند یا کد را بچسباند. بعد از claim، TX دیگر کد را نشان نمی‌دهد. Bind روی Device ID در Registration است.",
"ru": "Сайт выдаёт claim после оплаты; приложение может проверить TX или принять код. После claim TX больше не показывает коды. Привязка Device ID — в Registration.",
"zh": "网站付款后发 claim；应用也可验证 TX 或粘贴代码。claim 后 TX 不再显示代码。Device ID 绑定在 Registration。",
},
"Q106": {
"fa": "ابزار داخلی/ادمین برای صدور claim و بررسی TX / وضعیت AI Device ID. مسیر مشتری نیست؛ مشتری foxnext.net + Registration را استفاده می‌کند.",
"ru": "Внутренний/админ-инструмент для выдачи claim и проверки TX / AI Device ID. Не клиентский путь; клиенты — foxnext.net + Registration.",
"zh": "内部/管理员工具，用于签发 claim 与检查 TX / AI Device ID。非客户主路径；客户用 foxnext.net + Registration。",
},
"Q107": {
"fa": "Central با Full Deploy/پنل آماده، لایسنس برای add_exit، و SSH به VPS خروج. بدون پنل Central، wiring outbound شکست می‌خورد. قانون کشور Basic مربوط به Central است نه لزوماً کشور Exit.",
"ru": "Central с Full Deploy/готовой панелью, лицензия на add_exit и SSH на Exit VPS. Без панели Central outbound wiring падает. Страновое правило Basic — для Central, не обязательно для Exit.",
"zh": "Central 已 Full Deploy/面板就绪、具备 add_exit 许可，并能 SSH 到 Exit VPS。无 Central 面板则 outbound 接线失败。Basic 国家规则针对 Central，不一定限制 Exit 国家。",
},
"Q108": {
"fa": "یکپارچگی زنجیره — Exitهایی که هنوز از hop استفاده می‌کنند باید اول حذف شوند؛ ویزارد حذف تونل این را هشدار می‌دهد.",
"ru": "Целостность цепочки — Exit, которые ещё используют hop, нужно удалить сначала; мастер удаления туннеля предупреждает.",
"zh": "链路完整性——仍使用该 hop 的 Exit 须先删除；删除隧道向导会明确警告。",
},
"Q109": {
"fa": "شماره ترتیب hop در تونل چندمرحله‌ای Pro. ذخیره IP که زیر chain دیگر ثبت شده رد می‌شود. حذف یک hop ممکن است شماره بالاتر را ریست کند.",
"ru": "Порядковый номер hop в multi-hop Pro. Сохранение IP, уже лежащего под другим chain number, отклоняется. Удаление hop может сбросить старшие номера.",
"zh": "Pro 多跳隧道中 hop 的序号。若 IP 已登记在其他 chain number 下则拒绝保存。删除 hop 可能重置更高序号。",
},
"Q110": {
"fa": "در Deploy خروج، microsocks بخشی از مسیر SOCKS outbound است و هنگام حذف Exit همراه WG/فایروال برداشته می‌شود.",
"ru": "При deploy Exit microsocks — часть SOCKS outbound пути; при удалении Exit снимается вместе с WG/файрволом.",
"zh": "部署 Exit 时 microsocks 是 SOCKS outbound 路径的一部分；删除 Exit 时与 WG/防火墙一并移除。",
},
"Q111": {
"fa": "فایل `.conf` را در اپ WireGuard ویندوز/اندروید/iOS ایمپورت کنید. کلاینت در تب Clients پنل پس از ensure inbound دیده می‌شود.",
"ru": "Импортируйте `.conf` в приложение WireGuard на Windows/Android/iOS. Клиент появляется во вкладке Clients панели после ensure inbound.",
"zh": "将 `.conf` 导入 Windows/Android/iOS 的 WireGuard 应用。ensure inbound 后可在面板 Clients 看到客户端。",
},
"Q112": {
"fa": "پورت واقعی همان است که Full Deploy در Panel Login Info ذخیره کرده (در تاریخچه اغلب به ۲۰۵۳ اشاره شده). path/token کهنه علت رایج شکست Add Node است.",
"ru": "Реальный порт — тот, что Full Deploy сохранил в Panel Login Info (в истории часто 2053). Устаревший path/token — частая причина сбоя Add Node.",
"zh": "实际端口以 Full Deploy 写入 Panel Login Info 的为准（历史常提到 2053）。过期 path/token 是 Add Node 失败常见原因。",
},
"Q113": {
"fa": "Proxy Settings کمک می‌کند برنامه به پنل/اینترنت/هاب برسد؛ با پروکسی داخل کلاینت VPN کاربر نهایی یکی نیست. پروفایل‌هایی مثل Iran / Free.",
"ru": "Proxy Settings помогает приложению достучаться до панели/интернета/хаба; это не proxy внутри VPN-клиента пользователя. Профили вроде Iran / Free.",
"zh": "Proxy Settings 帮助应用访问面板/互联网/Hub；不是最终用户 VPN 客户端内部代理。含 Iran / Free 等配置。",
},
"Q114": {
"fa": "از تاریخچه Trust Wallet / MetaMask / Binance مقدار TxID را کپی کنید (طبق آموزش Registration).",
"ru": "Скопируйте TxID из истории Trust Wallet / MetaMask / Binance (как в туториале Registration).",
"zh": "从 Trust Wallet / MetaMask / Binance 历史复制 TxID（见 Registration 教程）。",
},
"Q115": {
"fa": "Win+R → msinfo32 یا دکمه کپی System Info داخل برنامه (در صورت وجود) برای اثرانگشت پشتیبانی.",
"ru": "Win+R → msinfo32 или кнопка copy system info в приложении (если есть) для отпечатка поддержки.",
"zh": "Win+R → msinfo32，或应用内复制 System Info（若有），用于支持指纹。",
},
"Q116": {
"fa": "اگر مبلغ زنده واکشی نشود، ممکن است به تماس با `@HiBlackFoxVpn` ارجاع داده شوید.",
"ru": "Если live-сумма не загрузилась, UI может отправить к `@HiBlackFoxVpn`.",
"zh": "若无法获取实时金额，界面可能引导联系 `@HiBlackFoxVpn`。",
},
"Q117": {
"fa": "هاب آپدیت در کنار foxnext.net استفاده می‌شود (اول blackfoxupdate.ir سپس foxnext.net). دانلود مشتری را ترجیحاً از foxnext.net بگیرید.",
"ru": "Хаб обновлений рядом с foxnext.net (сначала blackfoxupdate.ir, затем foxnext.net). Клиентские загрузки лучше с foxnext.net.",
"zh": "更新 Hub 与 foxnext.net 并用（先 blackfoxupdate.ir 再 foxnext.net）。客户下载仍优先 foxnext.net。",
},
"Q118": {
"fa": "عنوان گیت دسترسی وقتی Activate یا Pro لازم است؛ همراه پیام‌های need_activate / need_pro.",
"ru": "Заголовок ограничения доступа, когда нужны Activate или Pro; рядом с need_activate / need_pro.",
"zh": "需要 Activate 或 Pro 时的访问限制标题；与 need_activate / need_pro 成对出现。",
},
"Q119": {
"fa": "بله — قالب «Full Deploy روی Central» با جزئیات SSH. AI اکشن را صف می‌کند؛ تأیید کنید و منتظر done/failed بمانید.",
"ru": "Да — шаблон «Full Deploy на Central» с SSH-деталями. AI ставит действие в очередь; подтвердите и ждите done/failed.",
"zh": "可以——模板“在 Central 上 Full Deploy”并附 SSH 详情。AI 会入队；确认后等待 done/failed。",
},
"Q120": {
"fa": "هنگام باز شدن ممکن است Continue یا New بپرسد؛ چت ذخیره‌شده روی دستگاه است.",
"ru": "При открытии может спросить Continue или New; сохранённый чат на устройстве.",
"zh": "打开时可能询问 Continue 或 New；聊天保存在本机。",
},
}
