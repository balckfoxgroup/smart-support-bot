# -*- coding: utf-8 -*-
"""Build Connection/Server/General trees + Full_Support_Flow + README."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# reuse helpers by importing part A constants pattern
from _build_trees_a import META, T, E, ans, question, action, escalate, end_ok, write  # type: ignore

# ---------------------------------------------------------------------------
# Connection (SSH / hub / proxy — NOT consumer VPN dial)
# ---------------------------------------------------------------------------
CONNECTION = {
    "meta": {
        **META,
        "file": "Connection_Troubleshooting.json",
        "important": "In Black Fox, 'connection' usually means SSH to VPS, hub HTTP, or panel reachability — not a consumer VPN connect toggle.",
    },
    "trees": [
        {
            "id": "connection_problem",
            "category": "Connection",
            "priority": "critical",
            "related_intents": ["connect_ssh", "ssh_timeout", "ssh_auth_failed", "proxy_settings", "panel_unreachable"],
            "title": T("مشکل اتصال (SSH / هاب / پنل)", "Connection problem (SSH / hub / panel)", "Проблема соединения (SSH / хаб / панель)", "连接问题（SSH / Hub / 面板）"),
            "user_problem_examples": E(
                ["وصل نمیشه", "اتصال برقرار نمی‌شود", "SSH قطع", "timeout", "کند / قطع و وصل"],
                ["doesn't connect", "VPN doesn't connect", "SSH fails", "timeout", "slow / drops"],
                ["не подключается", "SSH не коннектится", "timeout", "обрывы", "медленно"],
                ["连不上", "VPN连不上", "SSH失败", "超时", "很慢/掉线"],
            ),
            "entry_node": "q_kind",
            "nodes": {
                "q_kind": question(
                    T("منظور شما از «وصل نمی‌شود» کدام است؟",
                      "When you say it won't connect, which do you mean?",
                      "Когда говорите «не подключается», что именно?",
                      "你说的「连不上」是指哪一种？"),
                    {
                        "ssh": ans("q_ssh_msg", "اتصال SSH به سرور / Connect SSH", "SSH to server / Connect SSH", "SSH к серверу / Connect SSH", "SSH 到服务器 / Connect SSH"),
                        "panel": ans("flow_panel", "باز شدن پنل 3X-UI در مرورگر", "Opening 3X-UI panel in browser", "Открытие панели 3X-UI в браузере", "浏览器打开 3X-UI 面板"),
                        "hub": ans("flow_hub", "آپدیت / فعال‌سازی / AI به اینترنت", "Update / activation / AI online", "Update / активация / AI онлайн", "更新/激活/AI 联网"),
                        "client": ans("flow_client", "کلاینت WireGuard کاربر نهایی", "End-user WireGuard client", "Клиент WireGuard конечного пользователя", "最终用户 WireGuard 客户端"),
                    },
                ),
                "q_ssh_msg": question(
                    T("متن خطا نزدیک به کدام است؟",
                      "Which error text is closest?",
                      "Какой текст ошибки ближе?",
                      "最接近哪条错误原文？"),
                    {
                        "auth": ans("a_auth", "authentication failed / رمز یا کلید", "authentication failed / password or key", "authentication failed / пароль или ключ", "authentication failed / 密码或密钥"),
                        "timeout": ans("a_timeout", "timeout / جواب نمیده", "timeout / no response", "timeout / не отвечает", "timeout / 无响应"),
                        "hostkey": ans("a_hostkey", "host key changed / mismatch", "host key changed / mismatch", "host key changed / mismatch", "host key changed / mismatch"),
                        "other": ans("a_ssh_generic", "سایر / نمی‌دانم", "Other / not sure", "Другое / не знаю", "其他 / 不确定"),
                    },
                ),
                "a_auth": action(
                    1,
                    T("رفع احراز هویت SSH", "Fix SSH authentication", "Исправить SSH authentication", "修复 SSH 认证"),
                    T("رمز را در پنل فروشنده ریست کنید یا PEM کامل (BEGIN/END) بچسبانید. user/port را چک کنید. اول Connect SSH را جدا بزنید.",
                      "Reset password in provider panel or paste full PEM (BEGIN/END). Check user/port. Run Connect SSH alone first.",
                      "Сбросьте пароль у провайдера или вставьте полный PEM (BEGIN/END). Проверьте user/port. Сначала отдельно Connect SSH.",
                      "在商家面板重置密码或粘贴完整 PEM（BEGIN/END）。检查 user/端口。先单独跑 Connect SSH。"),
                    "q_fixed",
                ),
                "a_timeout": action(
                    1,
                    T("رفع SSH timeout", "Fix SSH timeout", "Исправить SSH timeout", "修复 SSH timeout"),
                    T("VPS روشن باشد، IP/پورت درست باشد، فایروال فروشنده SSH را باز کند. سپس Proxy Settings (Auto/Iran).",
                      "Ensure VPS is on, IP/port correct, provider firewall allows SSH. Then Proxy Settings (Auto/Iran).",
                      "VPS включён, IP/порт верны, файрвол провайдера пускает SSH. Затем Proxy Settings (Auto/Iran).",
                      "确保 VPS 开机、IP/端口正确、商家防火墙放行 SSH。然后 Proxy Settings（Auto/Iran）。"),
                    "q_fixed",
                ),
                "a_hostkey": action(
                    1,
                    T("Host key", "Host key", "Host key", "Host key"),
                    T("فقط اگر خودتان VPS را rebuild کرده‌اید Accept کنید؛ وگرنه IP/مالکیت را قبل از Accept بررسی کنید.",
                      "Accept only if you rebuilt the VPS yourself; otherwise verify IP ownership before Accept.",
                      "Accept только если сами пересобрали VPS; иначе проверьте владение IP до Accept.",
                      "仅在您自己重建 VPS 时 Accept；否则 Accept 前核实 IP 归属。"),
                    "q_fixed",
                ),
                "a_ssh_generic": action(
                    1,
                    T("مسیر عمومی SSH", "Generic SSH path", "Общий путь SSH", "通用 SSH 路径"),
                    T("Central را Save کنید → Connect SSH → متن ترمینال را بخوانید → در صورت فیلتر Proxy.",
                      "Save Central → Connect SSH → read terminal → Proxy if filtered.",
                      "Save Central → Connect SSH → читайте terminal → Proxy при фильтрации.",
                      "保存 Central → Connect SSH → 看终端 → 若被过滤开 Proxy。"),
                    "q_fixed",
                ),
                "flow_panel": action(
                    1,
                    T("پنل در مرورگر", "Panel in browser", "Панель в браузере", "浏览器中的面板"),
                    T("Panel Login Info را باز کنید، URL کامل را کپی کنید. Proxy را امتحان کنید. اگر خالی است اول Full Deploy.",
                      "Open Panel Login Info, copy full URL. Try Proxy. If empty, Full Deploy first.",
                      "Откройте Panel Login Info, скопируйте полный URL. Попробуйте Proxy. Если пусто — сначала Full Deploy.",
                      "打开 Panel Login Info，复制完整 URL。尝试 Proxy。若为空先 Full Deploy。"),
                    "q_fixed",
                ),
                "flow_hub": action(
                    1,
                    T("اتصال به هاب", "Hub connectivity", "Связь с хабом", "Hub 连通性"),
                    T("اینترنت پایدار + Proxy Settings. عملیات فعال‌سازی/آپدیت/AI را دوباره امتحان کنید.",
                      "Stable internet + Proxy Settings. Retry activation/update/AI.",
                      "Стабильный интернет + Proxy Settings. Повторите активацию/update/AI.",
                      "稳定网络 + Proxy Settings。重试激活/更新/AI。"),
                    "q_fixed",
                ),
                "flow_client": action(
                    1,
                    T("کلاینت نهایی WireGuard", "End-user WireGuard client", "Клиент WireGuard", "最终用户 WireGuard"),
                    T("Black Fox خودش دکمه «وصل شو و وب‌گردی کن» مصرف‌کننده نیست. از Test Client / پنل کانفیگ WG بگیرید و در اپ WireGuard ایمپورت کنید. اگر Exit ندارید اول لایسنس + Add Exit + Configure Panel.",
                      "Black Fox is not a consumer 'connect & browse' app. Export WG via Test Client/panel and import into a WireGuard app. If no exit yet: license + Add Exit + Configure Panel.",
                      "Black Fox — не клиент «подключись и серфи». Экспортируйте WG через Test Client/панель и импортируйте в WireGuard. Если нет Exit: лицензия + Add Exit + Configure Panel.",
                      "Black Fox 不是「一键连接上网」客户端。通过 Test Client/面板导出 WG 并导入 WireGuard 应用。若还没有 Exit：License + Add Exit + Configure Panel。"),
                    "q_fixed",
                ),
                "q_fixed": question(
                    T("الان مشکل اتصال حل شد؟",
                      "Is the connection issue resolved now?",
                      "Проблема соединения решена?",
                      "连接问题现在解决了吗？"),
                    {
                        "yes": ans("ok", "بله", "Yes", "Да", "是"),
                        "no": ans("ask_more", "خیر", "No", "Нет", "否"),
                        "slow": ans("a_slow", "وصل است ولی کند/قطع می‌شود", "Connected but slow/drops", "Есть связь, но медленно/обрывы", "能连但很慢/掉线"),
                    },
                ),
                "a_slow": action(
                    2,
                    T("پایداری و مسیر", "Stability and path", "Стабильность и путь", "稳定性与路径"),
                    T("Proxy را عوض کنید، سرور/Exit دیگر را تست کنید، Diagnostic Center و در Pro در صورت نیاز Link Test / Mesh.",
                      "Switch Proxy profile, try another server/exit, run Diagnostic Center, and on Pro consider Link Test / Mesh.",
                      "Смените профиль Proxy, другой сервер/Exit, Diagnostic Center, в Pro — Link Test / Mesh.",
                      "更换 Proxy 配置，换服务器/Exit，跑 Diagnostic Center；Pro 下可考虑 Link Test / Mesh。"),
                    "ask_more",
                ),
                "ok": end_ok(T(
                    "اتصال برقرار شد. برای Deploy بعدی ابتدا Connect SSH را سبز نگه دارید.",
                    "Connection OK. Keep Connect SSH healthy before further deploys.",
                    "Соединение OK. Перед дальнейшим deploy держите Connect SSH успешным.",
                    "连接正常。后续部署前保持 Connect SSH 成功。",
                )),
                "ask_more": escalate(
                    [
                        T("نوع اتصال: SSH / پنل / هاب / کلاینت WG", "Connection type: SSH / panel / hub / WG client", "Тип: SSH / панель / хаб / WG-клиент", "类型：SSH / 面板 / Hub / WG 客户端"),
                        T("متن دقیق ترمینال/دیالوگ", "Exact terminal/dialog text", "Точный текст terminal/диалога", "终端/对话框确切原文"),
                        T("آیا Proxy را تست کردید؟", "Did you try Proxy?", "Пробовали Proxy?", "是否试过 Proxy？"),
                        T("Device ID (اگر لایسنس هم درگیر است)", "Device ID if license involved", "Device ID если связана лицензия", "若涉及 License 则提供 Device ID"),
                    ],
                    T("با نوع مشکل + متن خطا + اسکرین به @HiBlackFoxVpn پیام دهید.",
                      "Message @HiBlackFoxVpn with problem type + error text + screenshot.",
                      "Напишите @HiBlackFoxVpn: тип проблемы + текст ошибки + скрин.",
                      "将问题类型 + 错误原文 + 截图发给 @HiBlackFoxVpn。"),
                    ["connect_ssh", "proxy_settings", "panel_unreachable", "contact_support"],
                ),
            },
            "final_solution": T(
                "اتصال در Black Fox = SSH سالم + در صورت نیاز Proxy + پنل قابل‌دسترس؛ کلاینت نهایی جداگانه از اپ WireGuard است.",
                "Connection in Black Fox = healthy SSH + Proxy if needed + reachable panel; end-user clients are separate WireGuard apps.",
                "Соединение в Black Fox = здоровый SSH + Proxy при необходимости + доступная панель; клиенты пользователей — отдельные WireGuard apps.",
                "Black Fox 中的连接 = 健康 SSH + 必要时 Proxy + 面板可达；最终用户客户端是独立的 WireGuard 应用。",
            ),
        }
    ],
}


# ---------------------------------------------------------------------------
# Server
# ---------------------------------------------------------------------------
SERVER = {
    "meta": {**META, "file": "Server_Troubleshooting.json"},
    "trees": [
        {
            "id": "server_problems",
            "category": "Server",
            "priority": "critical",
            "related_intents": ["full_deploy", "panel_unreachable", "panel_login_info", "configure_panel", "add_domain", "mesh_servers"],
            "title": T("مشکلات سرور / پنل / DNS", "Server / panel / DNS problems", "Проблемы сервера / панели / DNS", "服务器 / 面板 / DNS 问题"),
            "user_problem_examples": E(
                ["سرور آفلاین", "پنل باز نمیشه", "DNS", "دامنه", "Full Deploy خراب", "توپولوژی خالی"],
                ["server offline", "panel won't open", "DNS issue", "domain problem", "deploy broken", "empty topology"],
                ["сервер офлайн", "панель не открывается", "проблема DNS", "домен", "deploy сломан", "пустая топология"],
                ["服务器离线", "面板打不开", "DNS问题", "域名问题", "部署坏了", "拓扑为空"],
            ),
            "entry_node": "q_area",
            "nodes": {
                "q_area": question(
                    T("مشکل بیشتر روی کدام بخش است؟",
                      "Which area is the problem mainly about?",
                      "В какой области в основном проблема?",
                      "问题主要在哪一块？"),
                    {
                        "offline": ans("a_offline", "VPS/سرور خاموش یا SSH نیست", "VPS offline / no SSH", "VPS офлайн / нет SSH", "VPS 离线 / 无 SSH"),
                        "panel": ans("a_panel", "پنل 3X-UI", "3X-UI panel", "Панель 3X-UI", "3X-UI 面板"),
                        "dns": ans("a_dns", "دامنه / DNS / CDN", "Domain / DNS / CDN", "Домен / DNS / CDN", "域名 / DNS / CDN"),
                        "deploy": ans("a_deploy", "Full Deploy / نصب روی سرور", "Full Deploy / install on server", "Full Deploy / установка на сервер", "Full Deploy / 服务器安装"),
                        "topo": ans("a_topo", "توپولوژی خالی / لینک", "Empty topology / links", "Пустая топология / линки", "拓扑为空 / 链路"),
                    },
                ),
                "a_offline": action(
                    1,
                    T("سرور آفلاین", "Server offline", "Сервер офлайн", "服务器离线"),
                    T("در پنل فروشنده VPS را روشن کنید، IP عمومی را تأیید کنید، فایروال SSH را باز کنید، سپس Connect SSH.",
                      "Power on VPS in provider panel, confirm public IP, open SSH firewall, then Connect SSH.",
                      "Включите VPS у провайдера, подтвердите публичный IP, откройте SSH в файрволе, затем Connect SSH.",
                      "在商家面板开机 VPS，确认公网 IP，放行 SSH 防火墙，然后 Connect SSH。"),
                    "q_done",
                ),
                "a_panel": action(
                    1,
                    T("پنل در دسترس نیست", "Panel unreachable", "Панель недоступна", "面板不可达"),
                    T("Panel Login Info → URL کامل → مرورگر. Proxy اگر فیلتر است. اگر credentials نیست: Full Deploy. برای routing Exit: Configure Panel (نه به‌جای نصب Central).",
                      "Panel Login Info → full URL → browser. Proxy if filtered. If no credentials: Full Deploy. For exit routing: Configure Panel (not a substitute for central install).",
                      "Panel Login Info → полный URL → браузер. Proxy при фильтре. Если нет credentials: Full Deploy. Для routing Exit: Configure Panel (не замена установки Central).",
                      "Panel Login Info → 完整 URL → 浏览器。若被过滤开 Proxy。无凭据则 Full Deploy。Exit 路由用 Configure Panel（不能替代 Central 安装）。"),
                    "q_done",
                ),
                "a_dns": action(
                    1,
                    T("DNS / Domain / CDN", "DNS / Domain / CDN", "DNS / Domain / CDN", "DNS / Domain / CDN"),
                    T("در Pro از Add Domain رکوردها را چک کنید. CDN origin/CNAME را با پنل جور کنید. Diagnostic مربوط به DNS/CDN را ببینید. Pro لازم است.",
                      "In Pro, verify records via Add Domain. Align CDN origin/CNAME with panel. Check DNS/CDN diagnostics. Pro required.",
                      "В Pro проверьте записи через Add Domain. Согласуйте CDN origin/CNAME с панелью. Смотрите диагностику DNS/CDN. Нужен Pro.",
                      "在 Pro 用 Add Domain 核对记录。CDN origin/CNAME 与面板对齐。查看 DNS/CDN 诊断。需要 Pro。"),
                    "q_done",
                ),
                "a_deploy": action(
                    1,
                    T("شکست نصب روی سرور", "Server install failure", "Сбой установки на сервере", "服务器安装失败"),
                    T("Connect SSH OK → Full Deploy با منبع Hub/Local اگر GitHub بسته است → ترمینال را بخوانید → Diagnostic Center.",
                      "Connect SSH OK → Full Deploy with Hub/Local if GitHub blocked → read terminal → Diagnostic Center.",
                      "Connect SSH OK → Full Deploy с Hub/Local если GitHub закрыт → читайте terminal → Diagnostic Center.",
                      "Connect SSH OK → 若 GitHub 不通用 Hub/Local 做 Full Deploy → 看终端 → Diagnostic Center。"),
                    "q_done",
                ),
                "a_topo": action(
                    1,
                    T("توپولوژی / لینک", "Topology / links", "Топология / линки", "拓扑 / 链路"),
                    T("توپولوژی بعد از Full Deploy (پنل آماده) یا لینک‌های مستقر + کلاینت پنل ظاهر می‌شود. در Pro برای لینک: Mesh / Link Test (WG → GRE → Stealth-WSS).",
                      "Topology appears after Full Deploy (panel ready) or deployed links + panel client. On Pro for links: Mesh / Link Test (WG → GRE → Stealth-WSS).",
                      "Топология появляется после Full Deploy (панель готова) или при линках + клиенте. В Pro: Mesh / Link Test (WG → GRE → Stealth-WSS).",
                      "拓扑在 Full Deploy（面板就绪）或已部署链路 + 面板客户端后出现。Pro 下链路：Mesh / Link Test（WG → GRE → Stealth-WSS）。"),
                    "q_done",
                ),
                "q_done": question(
                    T("مشکل سرور الان برطرف شد؟",
                      "Is the server issue fixed now?",
                      "Проблема сервера сейчас решена?",
                      "服务器问题现在解决了吗？"),
                    {
                        "yes": ans("ok", "بله", "Yes", "Да", "是"),
                        "no": ans("ask_more", "خیر", "No", "Нет", "否"),
                    },
                ),
                "ok": end_ok(T(
                    "سرور/پنل در وضعیت قابل‌استفاده است. قبل از Add Node/Exit از Panel Login Info مطمئن شوید.",
                    "Server/panel usable. Confirm Panel Login Info before Add Node/Exit.",
                    "Сервер/панель работоспособны. Перед Add Node/Exit проверьте Panel Login Info.",
                    "服务器/面板可用。Add Node/Exit 前确认 Panel Login Info。",
                )),
                "ask_more": escalate(
                    [
                        T("IP سرور و نقش: Central/Exit/Node", "Server IP and role: Central/Exit/Node", "IP и роль: Central/Exit/Node", "服务器 IP 与角色：Central/Exit/Node"),
                        T("خروجی Diagnostic Center (در صورت امکان)", "Diagnostic Center export if possible", "Экспорт Diagnostic Center если можно", "如可能导出 Diagnostic Center"),
                        T("اسکرین Panel Login / ترمینال", "Screenshot Panel Login / terminal", "Скрин Panel Login / terminal", "Panel Login / 终端截图"),
                    ],
                    T("جزئیات سرور + لاگ را به @HiBlackFoxVpn بفرستید (رمزها را در چت عمومی کامل نگذارید مگر کانال امن پشتیبانی).",
                      "Send server details + logs to @HiBlackFoxVpn (avoid pasting full passwords in public chats).",
                      "Отправьте детали сервера + логи в @HiBlackFoxVpn (не светите полные пароли в публичных чатах).",
                      "将服务器详情 + 日志发给 @HiBlackFoxVpn（避免在公开聊天粘贴完整密码）。"),
                    ["full_deploy_failed", "panel_unreachable", "contact_support"],
                ),
            },
            "final_solution": T(
                "سلامت سرور = VPS روشن + SSH + Full Deploy موفق + Panel Info درست + در صورت نیاز DNS/CDN/Mesh.",
                "Healthy server = powered VPS + SSH + successful Full Deploy + correct Panel Info + DNS/CDN/Mesh when needed.",
                "Здоровый сервер = VPS включён + SSH + успешный Full Deploy + верный Panel Info + DNS/CDN/Mesh при необходимости.",
                "健康服务器 = VPS 开机 + SSH + Full Deploy 成功 + Panel Info 正确 + 必要时 DNS/CDN/Mesh。",
            ),
        }
    ],
}


# ---------------------------------------------------------------------------
# General errors
# ---------------------------------------------------------------------------
GENERAL = {
    "meta": {**META, "file": "General_Error_Troubleshooting.json"},
    "trees": [
        {
            "id": "general_error",
            "category": "General",
            "priority": "high",
            "related_intents": ["ambiguous_app_broken", "check_system", "contact_support"],
            "title": T("خطاهای عمومی / نامشخص", "General / unclear errors", "Общие / неясные ошибки", "通用 / 不明错误"),
            "user_problem_examples": E(
                ["ارور میده", "کار نمیکنه", "نمی‌دانم چی شده", "پیام عجیب", "همه‌چیز خراب"],
                ["shows an error", "doesn't work", "weird message", "everything broken", "idk what happened"],
                ["ошибка", "не работает", "странное сообщение", "всё сломалось", "не понимаю"],
                ["报错", "不能用", "奇怪提示", "全坏了", "不知道怎么了"],
            ),
            "entry_node": "q_route",
            "nodes": {
                "q_route": question(
                    T("لطفاً بفرمایید مشکل شما کدام است؟",
                      "Please tell me which problem you have:",
                      "Пожалуйста, укажите вашу проблему:",
                      "请选择您的问题类型："),
                    {
                        "install": ans("handoff_install", "۱) برنامه نصب / باز نمی‌شود", "1) Install / won't start", "1) Установка / не запускается", "1) 安装 / 无法启动"),
                        "license": ans("handoff_license", "۲) لایسنس فعال نمی‌شود", "2) License won't activate", "2) Лицензия не активируется", "2) License 无法激活"),
                        "conn": ans("handoff_conn", "۳) اتصال / SSH / پنل", "3) Connection / SSH / panel", "3) Соединение / SSH / панель", "3) 连接 / SSH / 面板"),
                        "update": ans("handoff_update", "۴) آپدیت", "4) Update", "4) Обновление", "4) 更新"),
                        "server": ans("handoff_server", "۵) سرور / Deploy / DNS", "5) Server / Deploy / DNS", "5) Сервер / Deploy / DNS", "5) 服务器 / Deploy / DNS"),
                        "other": ans("a_collect", "۶) سایر", "6) Other", "6) Другое", "6) 其他"),
                    },
                ),
                "handoff_install": {
                    "type": "goto_tree",
                    "target_file": "Installation_Troubleshooting.json",
                    "target_tree": "installation_failed",
                    "message": T("مسیر نصب را شروع می‌کنیم.", "Starting installation troubleshooting.", "Запускаем диагностику установки.", "开始安装排查。"),
                },
                "handoff_license": {
                    "type": "goto_tree",
                    "target_file": "License_Troubleshooting.json",
                    "target_tree": "license_activation_failed",
                    "message": T("مسیر لایسنس را شروع می‌کنیم.", "Starting license troubleshooting.", "Запускаем диагностику лицензии.", "开始 License 排查。"),
                },
                "handoff_conn": {
                    "type": "goto_tree",
                    "target_file": "Connection_Troubleshooting.json",
                    "target_tree": "connection_problem",
                    "message": T("مسیر اتصال را شروع می‌کنیم.", "Starting connection troubleshooting.", "Запускаем диагностику соединения.", "开始连接排查。"),
                },
                "handoff_update": {
                    "type": "goto_tree",
                    "target_file": "Update_Troubleshooting.json",
                    "target_tree": "update_failed",
                    "message": T("مسیر Update را شروع می‌کنیم.", "Starting update troubleshooting.", "Запускаем диагностику обновления.", "开始更新排查。"),
                },
                "handoff_server": {
                    "type": "goto_tree",
                    "target_file": "Server_Troubleshooting.json",
                    "target_tree": "server_problems",
                    "message": T("مسیر سرور را شروع می‌کنیم.", "Starting server troubleshooting.", "Запускаем диагностику сервера.", "开始服务器排查。"),
                },
                "a_collect": action(
                    1,
                    T("جمع‌آوری حداقل شواهد", "Collect minimum evidence", "Сбор минимальных улик", "收集最少证据"),
                    T("Check System را اجرا و در صورت امکان Export کنید. متن دقیق خطا + اسکرین + حالت Basic/Pro/AI + Device ID را آماده کنید.",
                      "Run Check System and export if possible. Prepare exact error text + screenshot + Basic/Pro/AI mode + Device ID.",
                      "Запустите Check System и экспортируйте если можно. Подготовьте точный текст ошибки + скрин + режим + Device ID.",
                      "运行 Check System 并尽量导出。准备确切错误原文 + 截图 + Basic/Pro/AI 模式 + Device ID。"),
                    "ask_more",
                ),
                "ask_more": escalate(
                    [
                        T("متن کامل خطا / اسکرین", "Full error text / screenshot", "Полный текст ошибки / скрин", "完整错误原文 / 截图"),
                        T("مرحله‌ای که خطا افتاد", "Step where it failed", "Шаг, где упало", "出错步骤"),
                        T("Device ID", "Device ID", "Device ID", "Device ID"),
                        T("خروجی Check System", "Check System export", "Экспорт Check System", "Check System 导出"),
                    ],
                    T("با این مدارک به @HiBlackFoxVpn مراجعه کنید تا بدون حدس بررسی شود.",
                      "Contact @HiBlackFoxVpn with this evidence so support can avoid guessing.",
                      "Обратитесь в @HiBlackFoxVpn с этими данными, чтобы не гадать.",
                      "带着这些证据联系 @HiBlackFoxVpn，避免猜测。"),
                    ["ambiguous_app_broken", "check_system", "contact_support"],
                ),
            },
            "final_solution": T(
                "خطای نامشخص را اول دسته‌بندی کنید؛ سپس درخت همان دسته را اجرا کنید.",
                "Classify unclear errors first, then run that category's tree.",
                "Сначала классифицируйте неясную ошибку, затем запустите дерево категории.",
                "先对不明错误分类，再跑对应类别的决策树。",
            ),
        }
    ],
}


# ---------------------------------------------------------------------------
# Full support flow (root)
# ---------------------------------------------------------------------------
FULL = {
    "meta": {
        **META,
        "file": "Full_Support_Flow.json",
        "role": "Root conversation router for Telegram Bot / AI Assistant",
    },
    "entry": {
        "id": "support_root",
        "greeting": T(
            "سلام. من دستیار پشتیبانی Black Fox هستم. لطفاً بفرمایید مشکل شما کدام است؟",
            "Hi — I’m Black Fox support assistant. Which problem do you have?",
            "Здравствуйте. Я помощник поддержки Black Fox. Какая у вас проблема?",
            "你好，我是 Black Fox 支持助手。请问你的问题属于哪一类？",
        ),
        "menu": [
            {
                "key": "1",
                "label": T("برنامه نصب نمی‌شود / باز نمی‌شود", "App won't install / won't start", "Не устанавливается / не запускается", "无法安装 / 无法启动"),
                "goto": {"file": "Installation_Troubleshooting.json", "tree": "installation_failed"},
                "alt_tree": "app_wont_start",
                "ask_followup": T(
                    "نصب است یا اجرا؟ (نصب / اجرا)",
                    "Install or startup? (install / startup)",
                    "Установка или запуск? (install / startup)",
                    "是安装还是启动？（install / startup）",
                ),
            },
            {
                "key": "2",
                "label": T("لایسنس فعال نمی‌شود", "License won't activate", "Лицензия не активируется", "License 无法激活"),
                "goto": {"file": "License_Troubleshooting.json", "tree": "license_activation_failed"},
            },
            {
                "key": "3",
                "label": T("اتصال برقرار نمی‌شود (SSH/پنل/هاب)", "Connection problem (SSH/panel/hub)", "Проблема соединения (SSH/панель/хаб)", "连接问题（SSH/面板/Hub）"),
                "goto": {"file": "Connection_Troubleshooting.json", "tree": "connection_problem"},
            },
            {
                "key": "4",
                "label": T("آپدیت", "Update", "Обновление", "更新"),
                "goto": {"file": "Update_Troubleshooting.json", "tree": "update_failed"},
            },
            {
                "key": "5",
                "label": T("سرور / پنل / DNS / Deploy", "Server / panel / DNS / Deploy", "Сервер / панель / DNS / Deploy", "服务器 / 面板 / DNS / Deploy"),
                "goto": {"file": "Server_Troubleshooting.json", "tree": "server_problems"},
            },
            {
                "key": "6",
                "label": T("سایر / نمی‌دانم", "Other / not sure", "Другое / не уверен", "其他 / 不确定"),
                "goto": {"file": "General_Error_Troubleshooting.json", "tree": "general_error"},
            },
        ],
    },
    "conversation_policy": {
        "max_auto_steps_before_escalate": 5,
        "always_ask_before_destructive": True,
        "never_invent": ["version_numbers", "prices", "hosting_brands"],
        "vps_purchase_only": "FoxNext.net → Partners",
        "human_handoff": "@HiBlackFoxVpn",
        "language_match_user": True,
        "link_intent_db": "AI_BOT_DATABASE/intents/intents_{lang}.json",
        "on_unresolved": T(
            "اگر بعد از مراحل درخت حل نشد: Device ID + اسکرین خطا + مرحله شکست را بفرستید.",
            "If still unresolved after the tree: send Device ID + error screenshot + failing step.",
            "Если не решено после дерева: Device ID + скрин ошибки + шаг сбоя.",
            "若决策树后仍未解决：发送 Device ID + 错误截图 + 失败步骤。",
        ),
    },
    "stage_template": {
        "stage1_first_question": "Use entry.greeting + entry.menu (localized).",
        "stage2_branch": "Load target tree entry_node; ask diagnostic question; follow answers[].next.",
        "stage3_solution": "Execute type=action nodes; present action + solution.",
        "stage4_if_unresolved": "Follow if_unresolved → escalate node; collect ask_for; offer human_handoff.",
    },
}


README = """# Support Decision Tree — Black Fox

Interactive troubleshooting flows for **AI Assistant** and **Telegram Bot**.

These trees do **not** replace `AI_BOT_DATABASE` intents — they **orchestrate** them with questions, branches, and escalation.

## Files

| File | Purpose |
|------|---------|
| `Full_Support_Flow.json` | Root menu / router |
| `Installation_Troubleshooting.json` | Install + won't start |
| `License_Troubleshooting.json` | Activation / Device ID / claim / hub |
| `Update_Troubleshooting.json` | Force update / download / hub |
| `Connection_Troubleshooting.json` | SSH / panel / hub / WG client clarification |
| `Server_Troubleshooting.json` | Offline VPS / panel / DNS / deploy / topology |
| `General_Error_Troubleshooting.json` | Ambiguous errors → route to a tree |
| `_build_trees_a.py` / `_build_trees_b.py` | Generators |

## Node types

- `question` — ask user; `answers.{key}.next` chooses next node
- `action` — give step solution; then `next` or `if_unresolved`
- `resolved` — success end (`final_solution`)
- `escalate` — collect `ask_for`, hand off to human / richer intent
- `goto_tree` — jump to another file/tree id

All user-facing strings are objects: `{ "fa", "en", "ru", "zh" }`.

## How the AI should run a tree

1. Detect language (`fa|en|ru|zh`).
2. Start at `Full_Support_Flow.json` → show localized menu.
3. Open the target file + `entry_node`.
4. Loop:
   - If `question`: ask `text[lang]`, map user reply to an answer key, go `next`.
   - If `action`: show `action` + `solution`, ask “Did this fix it?” → yes/`resolved` or `if_unresolved`.
   - If `goto_tree`: load that tree.
   - If `escalate`: ask for checklist items, then `@HiBlackFoxVpn`.
5. Optionally enrich answers via related `related_intents` in `AI_BOT_DATABASE`.

### Stage mapping (required product behavior)

| Stage | Behavior |
|-------|----------|
| 1 | First question = root menu (or tree `entry_node`) |
| 2 | Branch on user answer |
| 3 | Provide stepwise solution (`action` nodes) |
| 4 | If unresolved → collect evidence (`escalate.ask_for`) |

## Link to Intent Database

- Trees diagnose and sequence.
- Intents provide dense FAQ answers / keywords.
- Example: SSH auth failure tree step → also retrieve intent `ssh_auth_failed`.

Field `related_intents` on each tree lists primary intent ids.

## Product-specific notes

- “Connection” is **not** a consumer VPN toggle. Clarify SSH vs panel vs hub vs end-user WireGuard client.
- Free Basic ops without license: Setup Central + Connect SSH + Full Deploy only.
- Pro ≠ AI Pro.
- Never invent versions/prices; VPS only via FoxNext Partners.

## Adding a new problem

1. Add a tree object in the matching generator section (or JSON file).
2. Provide FA/EN/RU/ZH for all texts and answer labels.
3. Set `entry_node`, wire `next` ids, include an `escalate` path.
4. Add `related_intents`.
5. Register in `Full_Support_Flow.json` menu if it is a top-level category.
6. Rebuild:

```powershell
python Support_Decision_Tree\\_build_trees_a.py
python Support_Decision_Tree\\_build_trees_b.py
```

## Success criteria

Before human handoff, the bot should have asked clarifying questions, tried stepwise fixes, and collected Device ID + screenshot when still failing.
"""


def main():
    write("Connection_Troubleshooting.json", CONNECTION)
    write("Server_Troubleshooting.json", SERVER)
    write("General_Error_Troubleshooting.json", GENERAL)
    write("Full_Support_Flow.json", FULL)
    (ROOT / "README.md").write_text(README, encoding="utf-8")
    print("wrote README.md")


if __name__ == "__main__":
    main()
