# -*- coding: utf-8 -*-
"""Native FA/RU/ZH answers for FAQ Q121–Q160."""
A = {
"Q121": {
"fa": "جابه‌جایی نقش Central به VPS جدید (قالب AI/عملیات). به SSH مبدأ و مقصد نیاز دارد؛ پرریسک — اول بکاپ بگیرید. جزئیات کامل ویزارد: NEED_MORE_REVIEW.",
"ru": "Перенос роли Central на новый VPS (шаблон AI/ops). Нужны SSH источника и назначения; высокий риск — сначала backup. Полные поля мастера: NEED_MORE_REVIEW.",
"zh": "将 Central 角色迁到新 VPS（AI/运维模板）。需要源与目标 SSH；高风险——先备份。向导完整字段：NEED_MORE_REVIEW。",
},
"Q122": {
"fa": "Test Client می‌تواند هر دو را نشان دهد؛ Subscription برای اپ‌هایی است که لیست را به‌روز می‌کشند. VLESS معمولاً لینک تکی inbound است.",
"ru": "Test Client может показать оба; Subscription — для приложений, которые тянут обновляемый список. VLESS обычно одиночная inbound-ссылка.",
"zh": "Test Client 可显示两者；Subscription 供会拉取更新列表的客户端。VLESS 通常是单条 inbound 链接。",
},
"Q123": {
"fa": "تا وقتی پنل آماده نباشد یا لینک/کلاینت نباشد، توپولوژی خالی می‌ماند (`topology_not_ready`).",
"ru": "Пока панель не готова или нет линков/клиента, топология пустая (`topology_not_ready`).",
"zh": "面板未就绪或缺少链路/客户端时拓扑为空（`topology_not_ready`）。",
},
"Q124": {
"fa": "ابزار ایجنت هنگام نصب Mesh از GitHub روی همان VPS دانلود می‌شود. VPS فیلترشده ممکن است به Proxy/دسترسی GitHub سمت سرور نیاز داشته باشد.",
"ru": "Инструменты агента при установке Mesh качаются с GitHub на сам VPS. На фильтрованном VPS может понадобиться proxy/доступ к GitHub на сервере.",
"zh": "Mesh 安装时代理工具从 GitHub 下载到该 VPS。受限 VPS 可能需要服务器侧 Proxy/访问 GitHub。",
},
"Q125": {
"fa": "گزینه CDN برای ارائه‌دهندگان خارج از لیست اصلی در وظایف AI Pro. Diagnose & Repair جدا از پیکربندی CDN است.",
"ru": "Опция CDN для провайдеров вне основного списка в AI Pro задачах. Diagnose & Repair — отдельная задача от настройки CDN.",
"zh": "AI Pro 任务中用于主列表之外提供商的 CDN 选项。Diagnose & Repair 与 CDN 配置是不同任务。",
},
"Q126": {
"fa": "برخی پورت‌ها در جریان‌ها اعتبارسنجی می‌شوند؛ راهنمای Configure Panel برای inbound WG به ۸۰۸۰ اشاره دارد. جزئیات دقیق Hysteria: NEED_MORE_REVIEW.",
"ru": "Некоторые порты валидируются во флоу; подсказка Configure Panel для WG inbound упоминает 8080. Точные строки Hysteria: NEED_MORE_REVIEW.",
"zh": "部分端口会在流程中校验；Configure Panel 对 WG inbound 提示提到 8080。Hysteria 精确文案：NEED_MORE_REVIEW。",
},
"Q127": {
"fa": "اگر کاربر sudo برای نصب داشته باشد ممکن است؛ بسیاری اسکریپت‌ها دسترسی سطح بالا فرض می‌کنند. ترجیح root مگر ایمیج را بشناسید.",
"ru": "Возможно, если есть sudo для установок; многие скрипты предполагают привилегии. Предпочтительнее root, если не знаете образ.",
"zh": "若用户具备安装所需 sudo 则可能；多数脚本假定高权限。除非熟悉镜像，否则推荐 root。",
},
"Q128": {
"fa": "هر دو پشتیبانی می‌شوند؛ اگر هر دو fail شوند دیالوگ both_failed می‌آید. روی کلاد اغلب کلید؛ بعد از ریست پنل اغلب رمز.",
"ru": "Поддерживаются оба; если оба падают — диалог both_failed. На облаке чаще ключ; после сброса панели чаще пароль.",
"zh": "两者都支持；若都失败会出现 both_failed。云镜像常用密钥；面板重置后常用密码。",
},
"Q129": {
"fa": "اعتبارنامه/پیش‌نویس محلی ذخیره شده بدون اتمام Deploy (`server.draft_saved`). برای ادامه ویزارد چندصفحه‌ای مفید است.",
"ru": "Локально сохранены credentials/черновик без завершения Deploy (`server.draft_saved`). Удобно перед продолжением многостраничного мастера.",
"zh": "本地已保存凭据/草稿但尚未完成 Deploy（`server.draft_saved`）。便于继续多页向导。",
},
"Q130": {
"fa": "ترجیح Keep Open؛ Close Anyway کار را ناقص می‌گذارد (`dialog.close_busy_*`).",
"ru": "Лучше Keep Open; Close Anyway оставляет работу незавершённой (`dialog.close_busy_*`).",
"zh": "建议 Keep Open；Close Anyway 会使工作未完成（`dialog.close_busy_*`）。",
},
"Q131": {
"fa": "Settings → Language → Apply روی همه تب‌ها. در اولین اجرا هم انتخاب زبان هست.",
"ru": "Settings → Language → Apply на все вкладки. На первом запуске тоже есть выбор языка.",
"zh": "Settings → Language → Apply 作用于全部标签。首次运行也有语言选择。",
},
"Q132": {
"fa": "پشتیبانی `@HiBlackFoxVpn`، کانال `@BlackFoxVPN`، سایت foxnext.net، ایمیل support@foxnext.net. مقادیر زنده را از Contact بخوانید.",
"ru": "Поддержка `@HiBlackFoxVpn`, канал `@BlackFoxVPN`, сайт foxnext.net, email support@foxnext.net. Смотрите живые значения Contact.",
"zh": "支持 `@HiBlackFoxVpn`、频道 `@BlackFoxVPN`、网站 foxnext.net、邮箱 support@foxnext.net。以 Contact 实时值为准。",
},
"Q133": {
"fa": "مسیر اصلی محصول معمولاً تلگرام پشتیبانی است؛ ایمیل هم هست. برای سرعت Device ID را در تلگرام بفرستید.",
"ru": "Основной канал в продукте обычно Telegram поддержки; email тоже есть. Для скорости пришлите Device ID в Telegram.",
"zh": "产品内主通道通常是支持 Telegram；也有邮箱。为求速度请在 Telegram 发送 Device ID。",
},
"Q134": {
"fa": "اکشن Settings برای تازه‌سازی متادیتای آپدیت و نمایش wallet پرداخت از هاب.",
"ru": "Действие Settings для обновления метаданных update и отображения payment wallet с хаба.",
"zh": "Settings 操作，用于从 Hub 刷新更新元数据与支付 wallet 显示。",
},
"Q135": {
"fa": "نسخه حداقل پشتیبانی‌شده را نصب کنید؛ بیلدهای قدیمی ممکن است قفل شوند (`remote.force_*` / MustForceUpdate).",
"ru": "Установите релиз не ниже минимума; старые сборки могут блокироваться (`remote.force_*` / MustForceUpdate).",
"zh": "安装不低于最低支持版本的发布包；过旧构建可能被强制挡住（`remote.force_*` / MustForceUpdate）。",
},
"Q136": {
"fa": "دوباره تلاش کنید؛ اینترنت/Proxy را چک کنید. پیام‌ها: timeout / could not reach AI service.",
"ru": "Повторите; проверьте интернет/Proxy. Сообщения: timeout / could not reach AI service.",
"zh": "请重试；检查网络/Proxy。提示包括 timeout / could not reach AI service。",
},
"Q137": {
"fa": "`ai.disabled` یعنی هاب سرویس AI را خاموش کرده؛ لزوماً مشکل لایسنس محلی نیست.",
"ru": "`ai.disabled` — хаб отключил AI; это не обязательно локальная лицензия.",
"zh": "`ai.disabled` 表示 Hub 关闭了 AI 服务；不一定是本地 License 问题。",
},
"Q138": {
"fa": "اول AI Assistant Pro را فعال کنید (`ai.quota.not_found`). با exhausted فرق دارد.",
"ru": "Сначала активируйте AI Assistant Pro (`ai.quota.not_found`). Это не то же самое, что exhausted.",
"zh": "请先激活 AI Assistant Pro（`ai.quota.not_found`）。这与 exhausted（用尽）不同。",
},
"Q139": {
"fa": "خیر — Reset All SSH را نگه می‌دارد؛ Delete History اعتبارنامه محلی را پاک می‌کند (لایسنس می‌ماند). این دو را قاطی نکنید.",
"ru": "Нет — Reset All сохраняет SSH; Delete History чистит локальные credentials (лицензия остаётся). Не путайте.",
"zh": "不会——Reset All 保留 SSH；Delete History 清除本地凭据（保留 License）。勿混淆。",
},
"Q140": {
"fa": "خیر — هدف نزدیک‌کردن VPS به حالت اولیه است و برگشت‌ناپذیر. با Reset All (حذف بسته با نگه داشتن SSH) فرق دارد.",
"ru": "Нет — цель приблизить VPS к исходному состоянию, необратимо. Отличается от Reset All (снятие пакетов с сохранением SSH).",
"zh": "不会——目标是把 VPS 推向初始状态且不可逆。不同于 Reset All（清软件但保留 SSH）。",
},
"Q141": {
"fa": "وضعیت ایجنت را Refresh کنید؛ بازیابی مسیر معمولاً چند ثانیه خودکار است. ترتیب: WG→GRE→Stealth-WSS→پشتیبان.",
"ru": "Обновите статус агентов; восстановление пути обычно автоматическое за секунды. Порядок: WG→GRE→Stealth-WSS→backups.",
"zh": "刷新代理状态；路径恢复通常数秒内自动。顺序：WG→GRE→Stealth-WSS→备份。",
},
"Q142": {
"fa": "روی میزبان‌های Central، Tunnel، Exit و Node.",
"ru": "На хостах Central, Tunnel, Exit и Node.",
"zh": "安装在 Central、Tunnel、Exit 与 Node 主机上。",
},
"Q143": {
"fa": "طراحی محصول این نیست — کتابخانه عملیاتی Deploy است؛ Panel Login Info فقط بعد از Deploy یک قابلیت است.",
"ru": "Так не задумано — это operational deploy library; Panel Login Info лишь одна функция после Deploy.",
"zh": "并非设计目标——它是运维部署工具库；Panel Login Info 只是部署后的一项功能。",
},
"Q144": {
"fa": "یک Store محلی مشترک برای سرور/پنل بین Basic و Pro و AI Pro — کانفیگ موازی فقط‌AI نیست.",
"ru": "Одно общее локальное хранилище серверов/панели для Basic/Pro/AI Pro — без параллельного AI-only конфига.",
"zh": "Basic/Pro/AI Pro 共用同一本地服务器/面板存储——没有并行的仅 AI 配置。",
},
"Q145": {
"fa": "Check System تشخیص فقط‌خواندنی است؛ Diagnose & Repair تلاش برای تعمیر است. برای مدرک پشتیبانی اول read-only.",
"ru": "Check System — только диагностика; Diagnose & Repair пытается чинить. Для доказательств поддержке сначала read-only.",
"zh": "Check System 为只读诊断；Diagnose & Repair 尝试修复。给支持举证时先用只读。",
},
"Q146": {
"fa": "دوباره Configure Panel، بررسی outbound/لینک، SSH به Exit و Diagnostic. علل رایج: Deploy ناقص Exit، WG/GRE پایین، تگ outbound ناهماهنگ، فایروال.",
"ru": "Снова Configure Panel, проверьте outbound/линк, SSH на Exit и Diagnostic. Частые причины: неполный Exit deploy, WG/GRE down, mismatch тега outbound, файрвол.",
"zh": "重跑 Configure Panel，检查 outbound/链路、SSH 到 Exit 与 Diagnostic。常见原因：Exit 部署不完整、WG/GRE 未起、outbound 标签不匹配、防火墙。",
},
"Q147": {
"fa": "path یا توکن پنل کهنه — Full Deploy یا Panel Login Info را تازه کنید (`node.err_central_login`).",
"ru": "Устаревший path/token панели — обновите Full Deploy или Panel Login Info (`node.err_central_login`).",
"zh": "面板 path/令牌过期——重跑 Full Deploy 或刷新 Panel Login Info（`node.err_central_login`）。",
},
"Q148": {
"fa": "اگر پوشه Portable جابه‌جا/حذف شود ریسک بالاست؛ حالت نصب‌شده از LocalAppData استفاده می‌کند. از پوشه بکاپ بگیرید.",
"ru": "Высокий риск при переносе/удалении portable-папки; installed mode использует LocalAppData. Делайте backup папки.",
"zh": "移动/删除 Portable 文件夹风险高；安装模式用 LocalAppData。请备份该文件夹。",
},
"Q149": {
"fa": "سایت foxnext.net صفحات چندزبانه دارد؛ زبان برنامه جداست و از Settings عوض می‌شود.",
"ru": "У foxnext.net есть мультиязычные страницы; язык приложения отдельный и меняется в Settings.",
"zh": "foxnext.net 有多语言页面；应用语言独立，在 Settings 中更改。",
},
"Q150": {
"fa": "یعنی مدیریت Central به‌همراه چند Exit/Tunnel/Node از یک Installer؛ ارزش اصلی اتوماسیون توپولوژی چندمکانه است نه فقط یک VPS.",
"ru": "Означает управление Central плюс несколькими Exit/Tunnel/Node из одного Installer; ценность — автоматизация multi-location топологии, не один VPS.",
"zh": "指用同一 Installer 管理 Central 与多个 Exit/Tunnel/Node；核心价值是多地域拓扑自动化，而非单台 VPS。",
},
"Q151": {
"fa": "خیر — رمزهای Factory Reset فقط برای همان عملیات‌اند و ذخیره نمی‌شوند؛ برخلاف Save معمولی سرور.",
"ru": "Нет — пароли Factory Reset только для этой операции и не сохраняются; в отличие от обычного Save сервера.",
"zh": "不会——Factory Reset 密码仅用于该次操作且不保存；不同于普通服务器 Save。",
},
"Q152": {
"fa": "احراز هویت OK بوده ولی خروجی probe غیرمنتظره است (`log.ssh_probe_unexpected`). ممکن است شل/MOTD عجیب یا دستور مسدود باشد. جزئیات دقیق: NEED_MORE_REVIEW.",
"ru": "Auth прошёл, но вывод probe неожиданный (`log.ssh_probe_unexpected`). Возможны необычный shell/MOTD или блокировка команд. Точные детали: NEED_MORE_REVIEW.",
"zh": "认证成功但 probe 输出异常（`log.ssh_probe_unexpected`）。可能是异常 shell/MOTD 或命令被拦。精确细节：NEED_MORE_REVIEW。",
},
"Q153": {
"fa": "بله — تا ۳ تصویر؛ AI چندوجهی است (متن+تصویر) برای جزئیات سرور/ربات و غیره.",
"ru": "Да — до 3 изображений; AI мультимодальный (текст+фото) для деталей сервера/бота и т.п.",
"zh": "可以——最多 3 张图；AI 多模态（文本+图像），用于服务器/机器人等信息。",
},
"Q154": {
"fa": "رد کنید و با توضیح دوباره بفرستید؛ مسیر reject از شما می‌خواهد هدف را روشن کنید یا Task را انتخاب کنید.",
"ru": "Отклоните и перешлите с уточнением; reject-путь просит прояснить цель или выбрать Task.",
"zh": "拒绝并澄清后重发；拒绝路径会要求说明用途或改选 Task。",
},
"Q155": {
"fa": "برنامه اکشن‌های صف‌شده از پاسخ AI را اعمال می‌کند (preparing… applying_actions… finalizing).",
"ru": "Приложение применяет поставленные в очередь действия из ответа AI (preparing… applying_actions… finalizing).",
"zh": "应用正在落实 AI 回复中排队的动作（preparing… applying_actions… finalizing）。",
},
"Q156": {
"fa": "۱۹/۳۳/۴۰ لنگر/fallback رایج‌اند؛ کاتالوگ زنده بر اساس ماه فرق دارد. همیشه مبلغ روی صفحه foxnext.net / داخل برنامه را بپردازید.",
"ru": "19/33/40 — распространённые якоря/fallback; live-каталог по месяцам отличается. Всегда платите сумму на экране foxnext.net / в приложении.",
"zh": "19/33/40 是常见锚点/回退；按月的实时目录可能不同。务必支付 foxnext.net/应用内显示金额。",
},
"Q157": {
"fa": "رکورد سرور هست ولی با سطح درخواستی جور نیست (`tier_mismatch`). سطح درست را Activate کنید یا با پشتیبانی هم‌تراز کنید.",
"ru": "Запись на сервере есть, но не совпадает с запрошенным тарифом (`tier_mismatch`). Активируйте верный тариф или согласуйте с поддержкой.",
"zh": "服务器有记录但与请求层级不符（`tier_mismatch`）。激活正确层级或联系支持对齐。",
},
"Q158": {
"fa": "معمولاً خیر — بعد از claim، TX کد را نشان نمی‌دهد. روی دستگاه bind‌شده Reactivation کنید یا با Device ID به پشتیبانی بروید.",
"ru": "Обычно нет — после claim TX больше не показывает коды. На привязанном устройстве Reactivation или поддержка с Device ID.",
"zh": "通常不行——claim 后 TX 不再显示代码。在已绑定设备用 Reactivation，或带 Device ID 找支持。",
},
"Q159": {
"fa": "Setup → زبان → Basic → Central → Connect SSH → Full Deploy → Panel Info → در صورت نیاز Exit بعد از Activate. شبکه محدود: Proxy. گیر کردید: `@HiBlackFoxVpn`.",
"ru": "Setup → язык → Basic → Central → Connect SSH → Full Deploy → Panel Info → при необходимости Exit после Activate. При фильтрации: Proxy. Если застряли: `@HiBlackFoxVpn`.",
"zh": "Setup → 语言 → Basic → Central → Connect SSH → Full Deploy → Panel Info → 需要时 Activate 后再加 Exit。受限网络用 Proxy。卡住联系 `@HiBlackFoxVpn`。",
},
"Q160": {
"fa": "برای متن دقیق UI به `internal/i18n/en.go` / `locales/en.json` و `reason_code`های API هاب نگاه کنید. stderr لینوکس ناشناس را NEED_MORE_REVIEW بگذارید.",
"ru": "Точные UI-строки — в `internal/i18n/en.go` / `locales/en.json` и `reason_code` API хаба. Неизвестный Linux stderr помечайте NEED_MORE_REVIEW.",
"zh": "精确 UI 文案见 `internal/i18n/en.go` / `locales/en.json` 与 Hub API 的 `reason_code`。未知 Linux stderr 标 NEED_MORE_REVIEW。",
},
}
