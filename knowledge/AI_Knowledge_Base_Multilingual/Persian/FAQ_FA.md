# Black Fox VPN — پرسش‌های متداول (فارسی)

> برای AI / ربات تلگرام / پشتیبانی. شناسهٔ Q با انگلیسی یکی است.
> پاسخ‌های Q001–Q200 بومی‌سازی شده‌اند (بدون روکش انگلیسی).
> دقت: حداکثر ۶ Exit؛ رایگان Basic = Setup Central + Connect SSH + Full Deploy؛ Pro ≠ AI Pro.


### Q001
**سؤال:** نصب‌کننده Black Fox VPN چیست؟
**پاسخ:** Black Fox یک Installer ویندوزی است که با SSH روی VPS شما WireGuard و پنل 3X-UI (Sanaei) را برای زیرساخت VPN چندمکانه خودکار می‌کند؛ کلاینت مصرف‌کنندهٔ وب‌گردی نیست.
**راه‌حل قدم‌به‌قدم:**
1. Setup را از foxnext.net دانلود کنید.
2. نصب کنید و زبان را انتخاب کنید.
3. انجام دهید: Choose Basic, Pro, or AI Assistant Pro on the View tab.
4. انجام دهید: Save central SSH, Connect SSH, then Full Deploy.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q002
**سؤال:** آیا Black Fox فورک رابط کاربری پنل 3X-UI است؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: No — it automates and manages the Sanaei / 3X-UI panel; it is not a panel UI fork. Black Fox installs and configures the real 3X-UI (Sanaei) panel on your central server and drives panel API tasks (inbounds, outbounds, nodes, clients). You still open the panel URL for advanced panel UI work when needed. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Complete Full Deploy.
2. انجام دهید: Use Panel Login Info for URL/user/password.
3. انجام دهید: Open the panel in a browser if you need the native 3X-UI UI.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q003
**سؤال:** محصول از چه پلتفرم‌هایی پشتیبانی می‌کند؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Windows Installer is the full ops app; Android has a companion app with chat/engine packaging differences. Primary product is the Windows desktop Installer (Setup and portable exe). Android builds exist (including a larger release APK that embeds the Go engine). Client WireGuard configs can be imported on Windows/Android/iOS WireGuard apps. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Use Windows for Full Deploy and mesh ops.
2. انجام دهید: Use Android where you need mobile AI/chat or engine-backed features.
3. انجام دهید: Import `.conf` into any WireGuard client for end-user VPN.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q004
**سؤال:** Installer رسمی را از کجا دانلود کنم؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: From foxnext.net (website download and update hosts). Official site is foxnext.net. Setup is typically `Black Fox Vpn-Installer-Setup.exe`. App updates also pull from foxnext.net / blackfoxupdate.ir style hosts configured in runtime. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open http://foxnext.net/ (or /en/).
2. انجام دهید: Use the download/setup page.
3. انجام دهید: Prefer Setup.exe for first install.
4. انجام دهید: For support, confirm you did not use an unofficial mirror.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q005
**سؤال:** تب‌های اصلی برنامه کدام‌اند؟
**پاسخ:** تب‌ها: Operations، Check System، View، Settings، Registration، Contact. Add Domain و Mesh پوشش جدا هستند؛ تب سطح‌بالای Add وجود ندارد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Start on View to pick mode. 2. Use Registration to activate. 3. Use Operations for SSH/deploy. 4. Use Contact for support.
2. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q006
**سؤال:** تب View برای چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Choose Basic / Pro / AI Pro and see topology when ready. View lets you pick the app mode and shows topology after Full Deploy (panel ready) or when links are deployed and a panel client exists. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. تب View را باز کنید.
2. انجام دهید: Select Basic, Pro, or AI Assistant Pro.
3. انجام دهید: After deploy, open Topology when available.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q007
**سؤال:** حالت Basic چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Central SSH, WireGuard + Sanaei panel, up to 6 exits, inbound/outbound setup, client test. Basic covers central in Iran/China/Russia, panel on central, up to six exit servers, configure panel, client test. Keys like Initial Server Setup, Connect SSH, and Full Deploy in Basic are free operations (license still gates full paid feature set after free basics). قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Select Basic on View.
2. انجام دهید: Save central (Iran/China/Russia).
3. Connect SSH را اجرا کنید.
4. Full Deploy را اجرا کنید.
5. انجام دهید: Add Exit Server(s) as needed.
6. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q008
**سؤال:** حالت Pro چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: All Basic plus multi-hop chain, tunnel relay, CDN, subscriptions, nodes (still max 6 exit slots). Pro unlocks multi-hop tunnel chain (Add Tunnel Servers), CDN, subscriptions, nodes, and other Pro ops. Exit capacity remains capped at 6 slots. Dialog text: “This feature requires Pro activation” when a Pro-only feature is locked. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. Pro را فعال کنید.
2. انجام دهید: Switch View to Pro.
3. انجام دهید: Use tunnel chain, CDN, subscription, and node buttons.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q009
**سؤال:** AI Assistant Pro چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: All Pro ops via smart chat, with simultaneous access to manual Pro. AI Assistant Pro (`ai_pro`) provides guided chat that can queue the same operations (Full Deploy, exits, mesh, CDN, diagnose, etc.) with confirmation. Manual Pro remains available. AI chat requires AI Pro unlock and AI quota credit on the hub. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Activate AI Assistant Pro.
2. انجام دهید: Select AI Pro on View.
3. انجام دهید: Use Tasks or free-form chat.
4. انجام دهید: Confirm Yes/No when asked before execution.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q010
**سؤال:** بعد از فعال‌سازی می‌توانم حالت را عوض کنم؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Yes — View mode selection is separate from license unlock, but locked features still need the matching license. You can select Basic/Pro/AI Pro on View. Features still check unlock state (Basic Full / Pro / AI Pro). AI chat is blocked with “AI Assistant Pro activation required…” if not unlocked. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. تب View را باز کنید.
2. انجام دهید: Select the mode you want.
3. انجام دهید: If a button says need activate / need Pro, open Registration.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q011
**سؤال:** کدام عملیات در Basic رایگان است؟
**پاسخ:** بدون License در Basic فقط Setup Central، Connect SSH و Full Deploy رایگان‌اند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Stay in Basic.
2. انجام دهید: Configure central.
3. Connect SSH را اجرا کنید.
4. انجام دهید: Run Full Deploy without paying for those three keys.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q012
**سؤال:** آیا در Basic سرور Central باید در کشورهای خاصی باشد؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Yes — Iran, China, or Russia. Dialog: “Basic mode: central server must be in Iran, China, or Russia.” Pro allows broader central placement (product Pro copy references worldwide/central flexibility vs Basic country rule). قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Choose a VPS in IR/CN/RU for Basic.
2. انجام دهید: Save country correctly in the server form.
3. انجام دهید: If rejected, use a Pro license or change location.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q013
**سؤال:** در Basic چند Exit Server می‌توانم داشته باشم؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Up to 6 exit servers. Basic tooltip and mode description: up to 6 exit servers; Add Exit Server 2 covers slot 2 in Basic and slots 2–6 in Pro flows. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Full Deploy central.
2. انجام دهید: Add Exit Server
3. انجام دهید: 3. Add further exits via Add Exit Server 2 / slots up to 6.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q014
**سؤال:** آیا در Pro تعداد Exit نامحدود است؟
**پاسخ:** خیر. سقف Exit برابر ۶ اسلات است (`MaxExitServers`).
**راه‌حل قدم‌به‌قدم:**
1. Pro را فعال کنید.
2. انجام دهید: Add exits as needed.
3. انجام دهید: Configure Panel for selected exits/nodes.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q015
**سؤال:** Full Deploy چیست؟
**پاسخ:** Full Deploy نصب یک‌مرحله‌ای WireGuard و پنل 3X-UI روی سرور Central است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Save central credentials.
2. انجام دهید: Connect SSH (OK).
3. انجام دهید: Run Full Deploy.
4. انجام دهید: Wait for terminal success.
5. انجام دهید: Open Panel Login Info.
6. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q016
**سؤال:** قبل از Full Deploy چه باید کرد؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Configure/save central server and verify SSH. Dialogs: “Configure central server first.” and Connect SSH to verify login. Without panel credentials after deploy, later ops say “Complete Full Deploy first.” قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Initial / Central Server Setup.
2. Connect SSH را اجرا کنید.
3. انجام دهید: Fix auth errors if any.
4. Full Deploy را اجرا کنید.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q017
**سؤال:** Connect SSH چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Test SSH login to the central server and verify connectivity. Validates username/password or key, host reachability, and stores trust state for host keys. Failures surface as SSH authentication / timeout / host key dialogs. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Save IP, port, user, password or PEM.
2. انجام دهید: Click Connect SSH.
3. انجام دهید: Accept host key only if you trust the VPS.
4. انجام دهید: Proceed when status is OK.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q018
**سؤال:** برنامه چه اطلاعات SSH را می‌پذیرد؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Host/IP, port (usually 22), username (often root), password and/or private key (PEM). Server forms and Factory Reset accept password or private key. Invalid both key and password: “SSH authentication failed” with message that invalid credentials were not saved. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Prefer root or sudo-capable user.
2. انجام دهید: Paste PEM if key auth.
3. انجام دهید: Or password.
4. انجام دهید: Connect SSH to validate.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q019
**سؤال:** Panel Login Info چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Shows saved 3X-UI panel URL, username, and password. Shared across Basic / Pro / AI Pro after deploy. Use it to open the panel and copy credentials. Long values wrap; copy buttons available. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Finish Full Deploy.
2. انجام دهید: Open Panel Login Info.
3. انجام دهید: Copy URL/user/pass.
4. انجام دهید: Log in via browser or continue in-app ops.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q020
**سؤال:** Configure Panel چیست؟
**پاسخ:** Configure Panel مسیریابی inbound/outbound/SOCKS را برای Exit یا Node موجود تعمیر می‌کند؛ نصب پنل روی Central نیست.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Have exits/nodes registered as needed.
2. انجام دهید: Open Configure Panel.
3. انجام دهید: Select targets and ports.
4. انجام دهید: Apply and verify Test Client.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q021
**سؤال:** Test Client / WireGuard چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Shows VLESS link, subscription URL, and WireGuard config for testing. After panel configuration, generate/test client links and `.conf` for import into WireGuard apps. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Configure Panel.
2. انجام دهید: Open Test Client.
3. انجام دهید: Copy VLESS/sub/WG.
4. انجام دهید: Import `.conf` into WireGuard.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q022
**سؤال:** Add Exit Server چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Deploy an exit location (WireGuard + SOCKS outbound) for egress. Exit servers carry traffic out. Slot 1 and additional slots (2–6 Basic, more in Pro). Requires central panel ready. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Full Deploy central.
2. انجام دهید: Enter exit SSH details.
3. انجام دهید: Run Add Exit Server.
4. انجام دهید: Configure Panel to use the exit.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q023
**سؤال:** Add Tunnel Server چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Pro chain hop relay between central and exits. Pro-only multi-hop: register tunnel hops; delete one hop also resets higher-sequence hops to keep the chain intact. Exits using those hops must be deleted first when removing tunnels. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. Pro را فعال کنید.
2. انجام دهید: Add Tunnel Server with hop sequence.
3. انجام دهید: Link exits through the chain.
4. انجام دهید: Deploy mesh/link type as guided.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q024
**سؤال:** Add Node چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Register a node with the central 3X-UI panel. Nodes are panel nodes (not the same as exit egress). Needs central panel login; errors often cite stale panel path/token — re-run Full Deploy or Panel Login Info. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Ensure Full Deploy done.
2. انجام دهید: Enter node SSH/details.
3. انجام دهید: Add Node.
4. انجام دهید: If login fails, refresh panel credentials.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q025
**سؤال:** تفاوت Exit و Node چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Exit = traffic egress VPS; Node = 3X-UI panel node registration. AI chat explicitly asks to confirm Exit vs Node when SSH details are ambiguous. Wrong choice mis-wires routing. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: For country egress use Exit.
2. انجام دهید: For panel node scaling use Node.
3. انجام دهید: Confirm in AI chat or wizard labels.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q026
**سؤال:** Add Domain چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Connect Cloudflare or ArvanCloud and manage DNS from the app. DNS page supports Cloudflare (email + API token) and ArvanCloud (machine user + API key), import zones, create A records for central or bot webhook subdomain. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Add Domain / DNS.
2. انجام دهید: Choose provider.
3. انجام دهید: Connect & Import Zones.
4. انجام دهید: Point A records to central/bot IP.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q027
**سؤال:** Configure CDN چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Configure CDN for domain and panel route (Pro feature family). Monetized Add CDN capability; AI template collects provider, domain/zone, API token/key. Used with domain for panel access over CDN. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. Pro را فعال کنید.
2. انجام دهید: Have domain ready.
3. انجام دهید: Configure CDN with provider details.
4. انجام دهید: Verify panel via domain.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q028
**سؤال:** Add Subscription چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Pro subscription setup for client subscription URLs. Feature `add_subscription` unlocks with Basic Full or Pro tiers per auth rules; used to publish subscription endpoints for clients. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Ensure license allows it.
2. انجام دهید: Run Add Subscription after panel ready.
3. انجام دهید: Share subscription URL from Test Client / panel.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q029
**سؤال:** Proxy Settings چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Proxy for reaching the 3X-UI panel and the internet from restricted networks. SSH Proxy Settings with profiles: none, auto-detect, Iran profile, free country profile; SOCKS5 or HTTP. Save and Test Connection. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Proxy Settings.
2. انجام دهید: Choose mode/type/host/port.
3. انجام دهید: Test Connection.
4. انجام دهید: Save.
5. انجام دهید: Retry panel/AI/hub operations.
6. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q030
**سؤال:** چه زمانی به Proxy نیاز دارم؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: When Direct access to hub, panel, or SSH path fails on filtered networks. Product network pattern prefers Direct first, then program proxy. Iran profile vs free-country profile helps match local filtering. AI chat can guide proxy updates. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Try Direct.
2. انجام دهید: If timeouts, open Proxy Settings.
3. انجام دهید: Enable Iran or free profile as appropriate.
4. انجام دهید: Retest.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q031
**سؤال:** چگونه License را فعال کنم؟
**پاسخ:** تب Registration → Device ID را کپی کنید → کد/claim را وارد و Activate کنید (یا مسیر پرداخت TX در foxnext.net).
**راه‌حل قدم‌به‌قدم:**
1. تب Registration را باز کنید.
2. انجام دهید: Paste code or verify TX.
3. انجام دهید: Wait for success.
4. انجام دهید: Confirm Basic/Pro/AI status badges.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q032
**سؤال:** کد claim چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Website-style code (`PREFIX-CLM-…`) with no Device ID until first unlock binds the PC. PAS help: claim codes match website Activation; Device ID binds on first use in the Windows app. Prefixes include BFXB (Basic), BFXP (Pro), BFXA (AI Pro), BFXQ (AI quota). قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Buy/generate claim code on foxnext.net / PAS.
2. انجام دهید: Open app Registration.
3. انجام دهید: Paste code once on the intended PC.
4. انجام دهید: Do not share after binding.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q033
**سؤال:** کد وابسته به دستگاه (machine-bound) چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Code already tied to a Device ID / fingerprint for a specific PC. PAS can generate machine-bound AI Pro (and related) codes. Verify tool distinguishes claim vs machine-bound vs tier. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Copy Device ID from Registration.
2. انجام دهید: Ask support/PAS for machine-bound code if needed.
3. انجام دهید: Paste on that same PC only.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q034
**سؤال:** Reactivation چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Restore this PC’s prior activation from the server without manually saving the code. Messages: checking previous activation; success; success with code loaded; not found; expired; failed (check internet). Does not invent a new purchase. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Registration on the same device.
2. انجام دهید: Tap Reactivation.
3. انجام دهید: If expired, renew purchase.
4. انجام دهید: If not found, activate with code/TX.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q035
**سؤال:** Device ID / License ID چیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: This PC’s license fingerprint for AI status checks and support. Registration page hint: Device ID is for AI status checks and support. Copy Device ID button available. Used when claiming binds, reactivation lookups, and AI quota checks. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. تب Registration را باز کنید.
2. Device ID را کپی کنید.
3. انجام دهید: Send to support only when asked.
4. انجام دهید: Keep consistent after OS reinstall unless hardware identity changes.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q036
**سؤال:** چرا My Code هنوز موجود نیست؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Activate once, or use Reactivation to load the code from the server. `reg.my_code_empty`: “Not available yet — activate once, or tap Reactivation to load from server.” قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Complete first activation.
2. انجام دهید: Or tap Reactivation.
3. انجام دهید: Then copy activation code if shown.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q037
**سؤال:** پرداخت روی چه شبکه‌ای است؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: USDT on BEP-20 (BSC). Registration tutorial: open wallet, select USDT BEP-20, send exact plan amount to the shown wallet, paste TX HASH / TX ID. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Use BEP-20 only (not TRC20/ERC20).
2. انجام دهید: Send exact amount.
3. انجام دهید: Wait for confirmation.
4. انجام دهید: Paste TX and verify.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q038
**سؤال:** قیمت Basic چقدر است؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Catalog anchors around 19 USDT for 18 months; duration pricing is host-editable. Default amount constant 19 USDT; `license-access.json` lists Basic prices by months (e.g. 12→13.5 … 18→19.0 … 30→30.0 USDT). Live pricing may come from hub — if missing, app asks contacting @HiBlackFoxVpn. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Check foxnext.net Activation for live price/months.
2. انجام دهید: Pay exact amount BEP-20.
3. انجام دهید: Activate in app.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q039
**سؤال:** قیمت Pro چقدر است؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Catalog uses ~33 USDT at 21 months / ~28.5 at 18; anchor 45 at 30 months. Code default `AmountProFull = 33`. Host catalog: Pro 12→20 … 18→28.5, 21→33, 30→45 USDT. Prefer website/live hub pricing. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Confirm months on website.
2. انجام دهید: Pay exact USDT BEP-20.
3. Pro را فعال کنید.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q040
**سؤال:** قیمت AI Assistant Pro چقدر است؟
**پاسخ:** بر اساس رفتار فعلی Black Fox: Catalog ~35–40 USDT mid-duration; anchor 55 at 30 months; includes AI quota flag. Default `AmountAIProFull = 40`. Catalog ai_pro prices 12→24.5 … 18→35, 21→40, 30→55. `includes_ai_quota: true` for AI Pro mode. قیمت و نسخه را اختراع نکنید؛ UI را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Buy AI Pro on foxnext.net.
2. انجام دهید: Activate in app.
3. انجام دهید: Confirm AI quota active before chatting.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q041
**سؤال:** شارژ سهمیه AI با BFXQ چیست؟
**پاسخ:** کدهای شارژ سهمیه AI با پیشوند `BFXQ` (معمولاً claim مثل `BFXQ-CLM-…`) هستند و حالت License را عوض نمی‌کنند. آیتم کاتالوگ `ai_quota` جدا از لایسنس است. PAS می‌تواند claim شارژ بسازد؛ با claim فقط سهمیه اعمال می‌شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: If quota exhausted, buy AI quota / get BFXQ code.
2. انجام دهید: Paste in Registration unlock.
3. انجام دهید: Recheck AI status.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q042
**سؤال:** مدت License چقدر است؟
**پاسخ:** مدت‌ها معمولاً ۱۲ تا ۳۰ ماه طبق کاتالوگ هاب است؛ اگر ماه مشخص نباشد اغلب پیش‌فرض ۱۸ ماه اعمال می‌شود. ماه‌های `license-access.json`: ۱۲،۱۵،۱۸،۲۱،۲۴،۲۷،۳۰. لایسنس منقضی با نشان «منقضی شده» قفل امکانات کامل را می‌بندد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Pick months at purchase.
2. انجام دهید: Note expiry in Registration.
3. انجام دهید: Renew before expiry for uninterrupted Pro/AI.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q043
**سؤال:** آیا یک خرید چند دستگاه را پوشش می‌دهد؟
**پاسخ:** کاتالوگ تا ۳ دستگاه با تخفیف پشتیبانی می‌کند (دستگاه۲ حدود ۲۰٪، دستگاه۳ حدود ۳۰٪). هر claim در اولین Activate به Device ID همان دستگاه bind می‌شود؛ یک claim را روی چند PC بی‌ربط دوباره استفاده نکنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Buy multi-device plan on website if offered.
2. انجام دهید: Activate each PC with its assigned code.
3. انجام دهید: Contact support if device transfer needed.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q044
**سؤال:** اگر TX HASH را دوباره استفاده کنم چه می‌شود؟
**پاسخ:** TX استفاده‌شده هم در کلاینت و هم در هاب رد می‌شود (`tx_already_used` / `tx_already_claimed`). بعد از claim، وارد کردن دوباره TX معمولاً کدها را نشان نمی‌دهد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Do not reuse old TX.
2. انجام دهید: If code already claimed, use Reactivation on bound PC.
3. در صورت نیاز به @HiBlackFoxVpn با Device ID پیام دهید.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q045
**سؤال:** معنی «claim already bound» چیست؟
**پاسخ:** یعنی این کد claim قبلاً به Device ID دیگری وصل شده (`bound_other_device` / `claim_bound`). با همان claim نمی‌توانید PC دوم نامرتبط را باز کنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Use the original PC + Reactivation.
2. انجام دهید: Or purchase another device seat.
3. انجام دهید: Support can help with Device ID evidence.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q046
**سؤال:** کد فعال‌سازی نامعتبر است — چه کار کنم؟
**پاسخ:** پیام «Invalid activation code» معمولاً به‌خاطر غلط املایی، پیشوند سطح اشتباه، کپی ناقص، یا کد نامعتبر است. برای کد machine-bound هم Device ID باید همان دستگاه باشد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Copy code again carefully.
2. انجام دهید: Confirm BFXB/BFXP/BFXA/BFXQ prefix.
3. انجام دهید: Use correct PC.
4. انجام دهید: Ask support to inspect code.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q047
**سؤال:** TX پیدا نشد / در انتظار / مبلغ اشتباه؟
**پاسخ:** منتظر تأیید BEP-20 بمانید؛ مبلغ و آدرس گیرنده باید دقیقاً مطابق صفحه باشد. خطاها: TX پیدا نشد، ناموفق، گیرنده اشتباه، مبلغ کم، توکن غیر USDT-BEP20، یا pending.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Confirm BSC explorer shows success.
2. انجام دهید: Exact USDT amount.
3. انجام دهید: Correct wallet address.
4. انجام دهید: Retry verify.
5. انجام دهید: Contact support with TX if stuck.
6. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q048
**سؤال:** پیام «ابتدا از تب Registration فعال کنید» یعنی چه؟
**پاسخ:** یعنی قابلیت پشت گیت لایسنس است (`dialog.need_activate` / Limited Access). در Basic فقط Setup Central، Connect SSH و Full Deploy بدون لایسنس آزادند؛ بقیه معمولاً نیاز به Activate دارند.
**راه‌حل قدم‌به‌قدم:**
1. تب Registration را باز کنید.
2. انجام دهید: Activate Basic/Pro/AI.
3. انجام دهید: Retry the operation.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q049
**سؤال:** پیام «این قابلیت نیاز به فعال‌سازی Pro دارد» یعنی چه؟
**پاسخ:** قابلیت فقط-Pro است در حالی که لایسنس Basic یا قفل است (`dialog.need_pro`). زنجیره تونل، برخی CDN/Subscription/Nodeها به Pro یا AI Pro نیاز دارند.
**راه‌حل قدم‌به‌قدم:**
1. Pro را فعال کنید.
2. انجام دهید: Switch View to Pro/AI Pro.
3. دوباره تلاش کنید.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q050
**سؤال:** اگر License منقضی شود هنوز می‌توانم از برنامه استفاده کنم؟
**پاسخ:** امکانات کامل لایسنس قفل می‌شود تا تمدید کنید. نشان «License expired» دیده می‌شود. Reactivation هم ممکن است expired برگرداند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Note Device ID.
2. انجام دهید: Purchase renewal on foxnext.net.
3. انجام دهید: Activate or Reactivation.
4. انجام دهید: Confirm badge cleared.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q051
**سؤال:** قیمت زنده سایت کجا تعریف می‌شود؟
**پاسخ:** قیمت زنده در `license-access.json` روی هاب است و بدون rebuild برنامه قابل ویرایش است. اگر هاب در دسترس نباشد، برنامه به ثابت‌های کد fallback می‌کند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Prefer foxnext.net displayed price.
2. انجام دهید: If app says pricing not received, contact @HiBlackFoxVpn.
3. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q052
**سؤال:** Initial Server Setup / Central Server Setup چیست؟
**پاسخ:** Central Server Setup اطلاعات SSH سرور مرکزی را محلی ذخیره می‌کند (IP، احراز هویت، کشور و پیش‌نویس). قبل از Deploy لازم است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open setup central.
2. انجام دهید: Fill IP/port/user/auth/country.
3. انجام دهید: Save.
4. Connect SSH را اجرا کنید.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q053
**سؤال:** چرا هنگام ذخیره نمی‌توانم Host/IP را عوض کنم؟
**پاسخ:** پیام محصول: هنگام ذخیره نمی‌توان Host/IP را عوض کرد؛ برای IP دیگر از جریان سرور جدید استفاده کنید. این از یکپارچگی inventory و شماره chain محافظت می‌کند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Keep IP on edit of credentials.
2. انجام دهید: For a new VPS, use Add/new server flow.
3. انجام دهید: Align chain number with Pro hops.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q054
**سؤال:** Full Deploy تمام شد ولی پنل باز نمی‌شود — بعد چه کنم؟
**پاسخ:** Panel Login Info (URL/path)، Proxy، فایروال را چک کنید و ابزار پنل را دوباره اجرا کنید. اگر credentials نیست → Full Deploy. خطای ورود نود اغلب path/token کهنه است → Full Deploy یا تازه‌سازی Panel Login Info.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Panel Login Info.
2. انجام دهید: Try URL in browser.
3. انجام دهید: Enable Proxy if filtered.
4. انجام دهید: Re-run Full Deploy / install 3X-UI.
5. انجام دهید: Run Diagnostic Center.
6. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q055
**سؤال:** Install WireGuard / Install 3X-UI جداگانه چیست؟
**پاسخ:** می‌توان فقط WireGuard یا فقط پنل Sanaei را روی Central نصب/به‌روز کرد؛ وقتی Full Deploy ناقص مانده مفید است. Settings → Check Update 3X-UI بسته را برای نصب بعدی کش می‌کند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Confirm SSH OK.
2. انجام دهید: Run the needed install button.
3. انجام دهید: Verify Panel Login Info.
4. انجام دهید: Continue Configure Panel.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q056
**سؤال:** Diagnostic Center چیست؟
**پاسخ:** Diagnostic Center بررسی فقط‌خواندنی سلامت SSH، WireGuard، پنل، DNS، CDN و Exitهاست. نتایج OK/Warning/Error را ببینید و برای پشتیبانی Export کنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Check System.
2. انجام دهید: Run Checks.
3. انجام دهید: Fix reported items.
4. انجام دهید: Export logs if contacting support.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q057
**سؤال:** Link Test چیست؟
**پاسخ:** Link Test اتصال را می‌سنجد و WireGuard، GRE یا Reverse Tunnel (Stealth-WSS) را پیشنهاد می‌کند. اعمال نهایی معمولاً از Mesh یا نوع لینک در Add Server است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Ensure servers registered.
2. انجام دهید: Run Link Test (ops/AI).
3. انجام دهید: Apply recommended link type.
4. انجام دهید: Redeploy mesh agents if needed.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q058
**سؤال:** GRE fallback چیست؟
**پاسخ:** اگر تونل WireGuard شکست بخورد، برنامه GRE را پیشنهاد می‌دهد. ترتیب failover مش: WireGuard → GRE → Reverse Tunnel (Stealth-WSS) → پشتیبان‌ها.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: When prompted, choose Yes for GRE if WG blocked.
2. انجام دهید: Or set link type explicitly.
3. انجام دهید: Verify with Link Test / mesh status.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q059
**سؤال:** Reverse Tunnel (Stealth-WSS) چیست؟
**پاسخ:** گزینه تونل معکوس محافظت‌شده در پشته لینک/مش با نام محصول Reverse Tunnel (Stealth-WSS). وقتی مسیر مستقیم WG/GRE ضعیف است استفاده می‌شود و توسط Link Monitor Agent پایش می‌شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Prefer after Link Test recommends it.
2. انجام دهید: Deploy via Mesh / link type.
3. انجام دهید: Keep agents running.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q060
**سؤال:** Mesh / Link Monitor Agent چیست؟
**پاسخ:** ایجنت‌های همیشه روشن روی Central، Tunnel، Exit و Node برای سلامت مسیر و failover. ویزارد Mesh آن‌ها را نصب می‌کند؛ ابزارها هنگام نصب از GitHub روی هر VPS دانلود می‌شوند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Register hosts.
2. انجام دهید: Open Mesh / CDN & Mesh section.
3. انجام دهید: Install agents.
4. انجام دهید: Refresh Status (installed/running).
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q061
**سؤال:** آیا ایجنت‌های Mesh نیاز دارند برنامه Windows باز باشد؟
**پاسخ:** خیر — ایجنت‌ها روی سرور وقتی برنامه Windows بسته است هم کار می‌کنند. برنامه برای نصب/وضعیت/تعمیر است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Deploy agents once.
2. انجام دهید: Close app if desired.
3. انجام دهید: Refresh Status later to verify.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q062
**سؤال:** ایجنت Mesh غایب/متوقف است — چه کنم؟
**پاسخ:** Mesh را دوباره Deploy کنید و Refresh Status بزنید. برچسب‌ها: نصب‌شده/غایب، Running/Stopped/نامشخص. نتیجه: «Mesh agents installed: X ok, Y failed».
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Refresh Status.
2. انجام دهید: Re-run mesh install on failed hosts.
3. انجام دهید: Check SSH to those hosts.
4. انجام دهید: Re-test links.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q063
**سؤال:** Mirza Bot چیست؟
**پاسخ:** ویزارد ربات تلگرام که Mirza را روی میزبان انتخابی نصب می‌کند و اعتبار پنل را پر می‌کند. گزینه‌ها: نصب Mirza، ذخیره ربات دیگر، یا انتقال. توکن بات و ادمین لازم است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Have panel credentials.
2. انجام دهید: Open Add Telegram Bot / Install Mirza.
3. انجام دهید: Enter token/admin.
4. انجام دهید: Install or update with backup.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q064
**سؤال:** می‌توانم Mirza را به سرور دیگری منتقل کنم؟
**پاسخ:** بله — گزینه Move existing bot در انتخابگر هست. قبل از Update/Move پشتیبان توصیه می‌شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Backup Mirza.
2. انجام دهید: Choose move.
3. انجام دهید: Enter destination SSH.
4. انجام دهید: Verify webhook/DNS if used.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q065
**سؤال:** برنامه از چه زبان‌هایی پشتیبانی می‌کند؟
**پاسخ:** چند زبان UI از جمله انگلیسی، فارسی، روسی، عربی، آلمانی، فرانسوی، هندی، ترکی و غیره. انتخاب زبان در شروع؛ Settings → Language روی همه تب‌ها اعمال می‌شود. فارسی RTL است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Settings → Language.
2. انجام دهید: Apply.
3. انجام دهید: Restart UI path if a tab looks stale. NEED_MORE_REVIEW for exact full language list beyond en.go keys if extras load dynamically.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q066
**سؤال:** تفاوت Setup.exe و Portable exe چیست؟
**پاسخ:** Setup زیر LocalAppData\Programs نصب می‌شود؛ Portable با `portable.txt` داده را کنار exe می‌گذارد. برای مشتری معمولاً `Black Fox Vpn-Installer-Setup.exe` پایدارتر است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Prefer Setup for normal users.
2. انجام دهید: Use portable when you must avoid installer.
3. انجام دهید: Do not mix data folders casually.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q067
**سؤال:** Delete History چه می‌کند؟
**پاسخ:** تاریخچه محلی (SSH، لاگ، وضعیت Deploy، CDN محلی و…) را پاک می‌کند؛ سرور ریموت را تغییر نمی‌دهد؛ زبان، حالت و لایسنس می‌ماند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Confirm you have remote access elsewhere.
2. انجام دهید: Run Delete History.
3. انجام دهید: Re-enter servers to continue ops.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q068
**سؤال:** Delete Exit Servers & Node چه می‌کند؟
**پاسخ:** از Exitها WireGuard/microsocks/فایروال را برمی‌دارد و تونل‌های متناظر Central را پاک می‌کند؛ SSH را نگه می‌دارد. می‌توان همه یا یکی را حذف کرد؛ حذف Node در صورت امکان از پنل unregister می‌شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open delete wizard.
2. انجام دهید: Choose Exit or Node.
3. انجام دهید: All or one.
4. انجام دهید: Confirm warning.
5. انجام دهید: Re-add if needed.
6. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q069
**سؤال:** Delete Tunnel Servers چه می‌کند؟
**پاسخ:** نصب hopهای زنجیره Pro را برمی‌دارد؛ حذف یک hop ممکن است hopهای با شماره بالاتر را ریست کند. Exitهایی که هنوز از آن hop استفاده می‌کنند باید اول حذف شوند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Delete dependent exits first.
2. انجام دهید: Delete tunnels (all/one).
3. انجام دهید: Rebuild chain if required.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q070
**سؤال:** DELETE — Reset All Servers چه می‌کند؟
**پاسخ:** WireGuard و پنل را از همه سرورهای پیکربندی‌شده برمی‌دارد و داده Deploy محلی را پاک می‌کند؛ SSH را نگه می‌دارد. با Factory Reset سطح OS فرق دارد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Read confirm body carefully.
2. انجام دهید: Confirm.
3. انجام دهید: Wait for completion.
4. انجام دهید: Full Deploy again to rebuild.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q071
**سؤال:** Factory Reset Server چیست؟
**پاسخ:** ریست مخرب ریموت به‌سوی VPS تازه؛ رمز این عملیات ذخیره نمی‌شود. داده، سرویس‌ها، بسته‌های VPN، تونل، فایروال، کاربران و تنظیمات سفارشی را هدف می‌گیرد. OS نامعتبر fail می‌شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Settings maintenance / Factory Reset.
2. انجام دهید: Enter IP/user/password or PEM.
3. انجام دهید: Confirm warning.
4. انجام دهید: Only on disposable VPS.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q072
**سؤال:** آیا Delete History لایسنس را پاک می‌کند؟
**پاسخ:** خیر — زبان، حالت برنامه و فعال‌سازی لایسنس نگه داشته می‌شوند. توجه: نصب مجدد Windows ممکن است Device ID را عوض کند → Reactivation.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Delete History if cleaning local inventory.
2. انجام دهید: License should remain.
3. انجام دهید: If license missing after Windows reinstall, Reactivation.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q073
**سؤال:** به‌روزرسانی برنامه چگونه کار می‌کند؟
**پاسخ:** Settings → Update BlackFox & Wallet Address؛ در صورت force ممکن است نسخه قدیمی قفل شود و باید Setup جدید از هاب/سایت رسمی نصب شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: When prompted, download latest Setup.
2. انجام دهید: Install over.
3. انجام دهید: Reopen app.
4. انجام دهید: Reactivation if needed.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q074
**سؤال:** Check Update 3X-UI چیست؟
**پاسخ:** آخرین بسته پنل Sanaei را در کش محلی برای نصب‌های بعدی می‌گیرد؛ به‌تنهایی پنل زنده روی سرور را ارتقا نمی‌دهد مگر عملیات نصب/به‌روز را اجرا کنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Settings → packages.
2. انجام دهید: Download if newer.
3. انجام دهید: Next panel install uses cache.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q075
**سؤال:** تفاوت Android و Windows چیست؟
**پاسخ:** Windows سطح کامل عملیات Installer است؛ Android همراه با بسته‌بندی/موتور متفاوت و پرسونای AI مشترک است. برای Full Deploy/Mesh معمولاً Windows را ترجیح دهید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Use Windows for Full Deploy/mesh.
2. انجام دهید: Install full Android APK for engine features.
3. انجام دهید: Same foxnext.net licenses conceptually via Device ID rules on each platform. NEED_MORE_REVIEW for exact Android license parity edge cases.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q076
**سؤال:** چگونه با پشتیبانی تماس بگیرم؟
**پاسخ:** تلگرام `@HiBlackFoxVpn`، سایت foxnext.net، ایمیل support@foxnext.net و کانال `@BlackFoxVPN`. مقادیر زنده را از تب Contact بخوانید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Contact tab or t.me.
2. انجام دهید: Send Device ID + short problem + screenshots/logs.
3. انجام دهید: Do not send passwords in public groups.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q077
**سؤال:** در پیام پشتیبانی چه چیزهایی بفرستم؟
**پاسخ:** Device ID، حالت برنامه، نام عملیات، تکه ترمینال، نوع TX/کد (در چت عمومی رمز کامل ندهید). خروجی Diagnostic مفید است.
**راه‌حل قدم‌به‌قدم:**
1. Device ID را کپی کنید.
2. انجام دهید: Note version from Settings/update.
3. انجام دهید: Attach Diagnostic summary.
4. انجام دهید: Message @HiBlackFoxVpn.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q078
**سؤال:** BlackFox MCP چیست؟
**پاسخ:** پل MCP محلی تا ابزارهای AI بیرونی وقتی برنامه باز است از Black Fox استفاده کنند. Activate MCP، کپی mcp.json، در تنظیمات MCP کلاینت بچسبانید. برنامه باید باز بماند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open BlackFox MCP.
2. انجام دهید: Activate.
3. انجام دهید: Copy mcp.json.
4. انجام دهید: Configure external AI.
5. انجام دهید: Keep Installer running.
6. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q079
**سؤال:** چت AI می‌گوید فعال‌سازی AI Assistant Pro لازم است
**پاسخ:** باید AI Pro را در Registration باز کنید (`view.ai_pro_locked`). فقط Basic یا Pro برای چت AI کافی نیست.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Buy/activate AI Pro.
2. انجام دهید: Reselect AI Pro mode.
3. انجام دهید: Retry chat.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q080
**سؤال:** سهمیه AI تمام شده — چه کنم؟
**پاسخ:** سهمیه تمام شده؛ با BFXQ شارژ کنید یا به پشتیبانی برای تمدید پیام دهید. کدهای `ai.quota.exhausted` / expired / not_found / disabled هم ممکن است.
**راه‌حل قدم‌به‌قدم:**
1. Device ID را کپی کنید.
2. انجام دهید: Buy AI quota (BFXQ) or message @HiBlackFoxVpn.
3. انجام دهید: Activate recharge code.
4. انجام دهید: Retry chat.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q081
**سؤال:** محدودیت پیوست در چت AI چیست؟
**پاسخ:** تا ۳ تصویر و ۵ فایل متنی در هر پیام. بیش از حد با `too_many_images` / `too_many_text_files` رد می‌شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Reduce attachments.
2. انجام دهید: Resend.
3. انجام دهید: Prefer text SSH details when possible.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q082
**سؤال:** آیا AI بدون تأیید عملیات را اجرا می‌کند؟
**پاسخ:** خیر — ابتدا تحلیل، سپس تأیید Yes/No، بعد اجرا. فقط صف‌کردن اکشن کافی نیست؛ باید تأیید شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Review proposed action.
2. انجام دهید: Reply Yes to run.
3. انجام دهید: Wait for “process finished” or failure.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q083
**سؤال:** AI گفت عملیات شروع شد — چقدر صبر کنم؟
**پاسخ:** تا پایان فرایند در ترمینال/وضعیت صبر کنید؛ پنجره busy را بی‌دلیل نبندید. وضعیت‌ها: wait / done / failed.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Keep window open.
2. انجام دهید: Watch terminal.
3. انجام دهید: On failure, read error and retry or Diagnose.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q084
**سؤال:** آیا AI می‌تواند outbound سفارشی v2ray اضافه کند؟
**پاسخ:** بله در AI Pro — JSON outbound را بچسبانید؛ سقف ۱۰ outbound مصنوعی روی پنل. حذف در UI پنل شمارنده AI را ریست نمی‌کند. JSON نامعتبر رد می‌شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Paste one outbound per request.
2. انجام دهید: Confirm apply.
3. انجام دهید: Contact support if need more than 10.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q085
**سؤال:** راهنمای پیش‌فرض پورت inbound در Configure Panel چیست؟
**پاسخ:** راهنمای Configure Panel معمولاً ۴۴۳ VLESS، ۸۰ Trojan، ۸۰۸۰ WireGuard را ذکر می‌کند؛ نصب واقعی را از Panel Login Info / تست کلاینت تأیید کنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Prefer defaults unless you know you need others.
2. انجام دهید: Open firewall for those ports.
3. انجام دهید: Test Client.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q086
**سؤال:** اعتبارنامه پنل Central پیدا نشد؟
**پاسخ:** اول Full Deploy را کامل کنید تا URL/کاربر/رمز/توکن پنل ذخیره شود. بسیاری عملیات به این credentials وابسته‌اند.
**راه‌حل قدم‌به‌قدم:**
1. Full Deploy را اجرا کنید.
2. انجام دهید: Panel Login Info non-empty.
3. انجام دهید: Retry Add Node / proxy panel ops.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q087
**سؤال:** SSH host key عوض شده — امن است؟
**پاسخ:** بعد از ری‌اینستال VPS رایج است؛ فقط اگر به سرور اعتماد دارید Accept کنید. دیالوگ احتمال MITM را هم هشدار می‌دهد؛ Accept کلید ذخیره‌شده را پاک و retry می‌کند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Confirm you reinstalled the VPS or changed keys.
2. انجام دهید: Accept if trusted.
3. انجام دهید: If unexpected, stop and check provider console/IP.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q088
**سؤال:** احراز هویت SSH شکست خورد (کلید و رمز)؟
**پاسخ:** رمز و کلید هر دو نامعتبر/منقضی‌اند؛ مقدار غلط ذخیره نمی‌شود. عنوان: SSH authentication failed.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Reset password in provider panel if needed.
2. انجام دهید: Fix PEM formatting.
3. انجام دهید: Confirm user is allowed SSH.
4. انجام دهید: Connect SSH again.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q089
**سؤال:** رمز لینوکس هنگام SSH منقضی شده؟
**پاسخ:** برنامه جریان Change Linux Password را نشان می‌دهد (رمز فعلی/جدید/تأیید). موفقیت یا mismatch/required/failed.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Enter current and new password.
2. انجام دهید: Confirm match.
3. انجام دهید: Retry Connect SSH.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q090
**سؤال:** علل SSH timeout چیست؟
**پاسخ:** فیلتر شبکه، IP/پورت غلط، فایروال فروشنده، یا نیاز به Proxy. لزوماً رمز اشتباه نیست (`log.ssh_timeout`).
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Ping/port-check from another network if possible.
2. انجام دهید: Verify IP/port.
3. Proxy Settings را امتحان کنید.
4. انجام دهید: Check VPS running in provider UI.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q091
**سؤال:** نمای topology چیست؟
**پاسخ:** نقشه توپولوژی وقتی پنل آماده است یا لینک‌ها Deploy شده و کلاینت پنل وجود دارد. در غیر این صورت `topology_not_ready`.
**راه‌حل قدم‌به‌قدم:**
1. Full Deploy را اجرا کنید.
2. انجام دهید: Add links/exits.
3. انجام دهید: Ensure panel client exists.
4. انجام دهید: Open Topology.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q092
**سؤال:** Add OutBounds چیست؟
**پاسخ:** افزودن outbound روی پنل (دستی یا JSON سفارشی در AI Pro) برای مسیر Exitها و مسیریابی.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Panel must be ready.
2. انجام دهید: Use Configure Panel / Add OutBounds / AI outbound paste.
3. انجام دهید: Test Client.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q093
**سؤال:** آیا Basic همه‌جا می‌تواند از Cloudflare CDN استفاده کند؟
**پاسخ:** CDN در مجموعه قابلیت‌های Pro است؛ Basic روی Central+Exit تمرکز دارد و CDN را مثل Pro باز نمی‌کند.
**راه‌حل قدم‌به‌قدم:**
1. Pro را فعال کنید.
2. انجام دهید: Add Domain.
3. انجام دهید: Configure CDN.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q094
**سؤال:** کدام ارائه‌دهندگان DNS در برنامه پشتیبانی می‌شوند؟
**پاسخ:** Cloudflare (ایمیل + API token با Zone:DNS:Edit) و ArvanCloud (کاربر ماشین + API key). ساب‌دامین وبهوک بات اختیاری و جدا از دامنه پنل است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Create API credentials at provider.
2. انجام دهید: Connect & Import Zones.
3. انجام دهید: Create A records.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q095
**سؤال:** تفاوت DNS وبهوک بات و دامنه پنل؟
**پاسخ:** ساب‌دامین اختیاری برای وبهوک تلگرام بات؛ اگر لازم نیست رد شوید — دامنه پنل نیست.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Decide if Mirza needs webhook domain.
2. انجام دهید: Fill bot subdomain + IP.
3. انجام دهید: Create A → Bot.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q096
**سؤال:** Diagnose & Repair چیست؟
**پاسخ:** بررسی/تعمیر گسترده‌تر (دیسک/ترافیک، پینگ/فیلتر، لینک مش، دامنه/CDN، پارامترهای خراب). به‌صورت Task AI/عملیات؛ فقط وقتی IP یا رمز جدید لازم است می‌پرسد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Register servers first.
2. انجام دهید: Run Diagnose & Repair.
3. انجام دهید: Approve fixes.
4. انجام دهید: Re-test clients.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q097
**سؤال:** اسپینر busy نوار وضعیت یعنی چه؟
**پاسخ:** عملیات طولانی در جریان است؛ صبر کنید تا تمام شود. بستن زودهنگام ناقص‌ماندن کار را هشدار می‌دهد.
**راه‌حل قدم‌به‌قدم:**
1. صبر کنید.
2. انجام دهید: Watch terminal.
3. انجام دهید: Keep Open if prompted.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q098
**سؤال:** می‌توانم عملیات در حال اجرای terminal را متوقف کنم؟
**پاسخ:** بله — دکمه Stop ترمینال با تأیید؛ فرایند فعلی را قطع می‌کند و به‌عنوان توقف کاربر علامت می‌خورد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Click Stop.
2. انجام دهید: Confirm.
3. انجام دهید: Re-run cleanly if needed.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q099
**سؤال:** فایل‌های محلی نصب‌شده کجا ذخیره می‌شوند؟
**پاسخ:** در حالت نصب‌شده معمولاً زیر `%LocalAppData%\Programs\Black Fox Vpn`. در Portable کنار exe (با marker).
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Win+R → `%LocalAppData%\Programs`.
2. انجام دهید: Find Black Fox Vpn.
3. انجام دهید: Do not delete license-critical files casually.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q100
**سؤال:** چگونه Device ID / wallet / TX / کد فعال‌سازی را کپی کنم؟
**پاسخ:** دکمه‌های Copy اختصاصی با پیام موفقیت کلیپ‌بورد برای Device ID، wallet، TX و کد فعال‌سازی.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Click the Copy control.
2. انجام دهید: Paste into notepad/support chat.
3. انجام دهید: Verify no truncation.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q101
**سؤال:** مسیر فعال‌سازی Offline / record-offline چیست؟
**پاسخ:** APIهای هاب می‌توانند کد/TX آفلاین را با پرچم claim_pending ثبت کنند. جزئیات همه دیالوگ‌های offline: در صورت ابهام NEED_MORE_REVIEW.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Prefer online verify.
2. انجام دهید: If offline code issued, activate in app when online.
3. انجام دهید: Support if claim_pending stuck.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q102
**سؤال:** معنی پیشوندهای BFXB / BFXP / BFXA / BFXQ؟
**پاسخ:** BFXB=Basic، BFXP=Pro، BFXA=AI Pro، BFXQ=سهمیه AI. پیشوند اشتباه برای قابلیت هدف unlock را fail می‌کند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Match purchase to prefix.
2. انجام دهید: Paste exact code.
3. انجام دهید: For quota only use BFXQ.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q103
**سؤال:** آیا AI Pro امکانات دستی Pro را هم دارد؟
**پاسخ:** بله — AI Pro عملیات Pro را از چت می‌دهد و دسترسی دستی Pro را همزمان نگه می‌دارد؛ ولی گیت ویژه AI جداست.
**راه‌حل قدم‌به‌قدم:**
1. AI Pro را فعال کنید.
2. انجام دهید: Use AI chat or switch to Pro-style manual ops as allowed.
3. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q104
**سؤال:** آیا باز کردن Pro، AI Assistant Pro را هم می‌دهد؟
**پاسخ:** خیر — unlock معمولی Pro هرگز AI Assistant Pro را باز نمی‌کند (`FeatureAIProFull`).
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Buy AI Pro separately.
2. انجام دهید: Or upgrade path on website if offered (`already_ai_pro` / upgrade reasons on API).
3. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q105
**سؤال:** تفاوت Activation سایت و تأیید TX داخل برنامه؟
**پاسخ:** سایت بعد از پرداخت claim می‌دهد؛ برنامه هم می‌تواند TX را verify کند یا کد را بچسباند. بعد از claim، TX دیگر کد را نشان نمی‌دهد. Bind روی Device ID در Registration است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Pay on foxnext.net.
2. انجام دهید: Receive claim code.
3. انجام دهید: Paste in Windows Registration.
4. انجام دهید: Keep Device ID record.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q106
**سؤال:** PAS Generator چیست؟
**پاسخ:** ابزار داخلی/ادمین برای صدور claim و بررسی TX / وضعیت AI Device ID. مسیر مشتری نیست؛ مشتری foxnext.net + Registration را استفاده می‌کند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Customers: use website/app only.
2. انجام دهید: Support staff: PAS for generate/verify.
3. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q107
**سؤال:** برای Add Exit چه پیش‌نیازهایی لازم است؟
**پاسخ:** Central با Full Deploy/پنل آماده، لایسنس برای add_exit، و SSH به VPS خروج. بدون پنل Central، wiring outbound شکست می‌خورد. قانون کشور Basic مربوط به Central است نه لزوماً کشور Exit.
**راه‌حل قدم‌به‌قدم:**
1. Full Deploy را اجرا کنید.
2. انجام دهید: Activate if locked.
3. انجام دهید: Add Exit with correct SSH.
4. انجام دهید: Configure Panel.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q108
**سؤال:** چرا قبل از بعضی حذف‌های Tunnel باید Exitها پاک شوند؟
**پاسخ:** یکپارچگی زنجیره — Exitهایی که هنوز از hop استفاده می‌کنند باید اول حذف شوند؛ ویزارد حذف تونل این را هشدار می‌دهد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Identify dependent exits.
2. انجام دهید: Delete those exits.
3. انجام دهید: Delete tunnel hops.
4. انجام دهید: Rebuild.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q109
**سؤال:** شماره chain در Pro چیست؟
**پاسخ:** شماره ترتیب hop در تونل چندمرحله‌ای Pro. ذخیره IP که زیر chain دیگر ثبت شده رد می‌شود. حذف یک hop ممکن است شماره بالاتر را ریست کند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Assign consistent chain numbers.
2. انجام دهید: Don’t reuse IP across conflicting chains.
3. انجام دهید: Rebuild after mid-chain deletes.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q110
**سؤال:** نقش Microsocks روی Exitها؟
**پاسخ:** در Deploy خروج، microsocks بخشی از مسیر SOCKS outbound است و هنگام حذف Exit همراه WG/فایروال برداشته می‌شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Let Add Exit install it.
2. انجام دهید: Don’t manually break microsocks.
3. انجام دهید: Use app delete/redeploy to fix.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q111
**سؤال:** نکتهٔ import کلاینت WireGuard؟
**پاسخ:** فایل `.conf` را در اپ WireGuard ویندوز/اندروید/iOS ایمپورت کنید. کلاینت در تب Clients پنل پس از ensure inbound دیده می‌شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Download/copy conf from Test Client.
2. انجام دهید: Import.
3. انجام دهید: Activate tunnel.
4. انجام دهید: Test IP/egress.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q112
**سؤال:** ارجاع پورت پیش‌فرض پنل؟
**پاسخ:** پورت واقعی همان است که Full Deploy در Panel Login Info ذخیره کرده (در تاریخچه اغلب به ۲۰۵۳ اشاره شده). path/token کهنه علت رایج شکست Add Node است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Copy URL from Panel Login Info.
2. انجام دهید: Don’t guess old ports.
3. انجام دهید: Re-sync credentials after panel changes.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q113
**سؤال:** رابطه External Proxy و proxy پنل؟
**پاسخ:** Proxy Settings کمک می‌کند برنامه به پنل/اینترنت/هاب برسد؛ با پروکسی داخل کلاینت VPN کاربر نهایی یکی نیست. پروفایل‌هایی مثل Iran / Free.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Configure Proxy Settings in app.
2. انجام دهید: Test.
3. انجام دهید: Retry Panel Login / AI hub.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q114
**سؤال:** آموزش Registration — پیدا کردن TX HASH؟
**پاسخ:** از تاریخچه Trust Wallet / MetaMask / Binance مقدار TxID را کپی کنید (طبق آموزش Registration).
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open wallet activity.
2. انجام دهید: Open TX details.
3. انجام دهید: Copy hash starting with 0x.
4. انجام دهید: Paste in app.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q115
**سؤال:** کپی System info در Windows؟
**پاسخ:** Win+R → msinfo32 یا دکمه کپی System Info داخل برنامه (در صورت وجود) برای اثرانگشت پشتیبانی.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Prefer in-app Device ID.
2. انجام دهید: Use msinfo32 only if support asks.
3. انجام دهید: Don’t paste unrelated secrets.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q116
**سؤال:** اگر قیمت هاب دریافت نشود چه می‌شود؟
**پاسخ:** اگر مبلغ زنده واکشی نشود، ممکن است به تماس با `@HiBlackFoxVpn` ارجاع داده شوید.
**راه‌حل قدم‌به‌قدم:**
1. اینترنت/Proxy را بررسی کنید.
2. انجام دهید: Retry later.
3. در صورت نیاز به @HiBlackFoxVpn با Device ID پیام دهید.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q117
**سؤال:** آیا blackfoxupdate.ir مرتبط است؟
**پاسخ:** هاب آپدیت در کنار foxnext.net استفاده می‌شود (اول blackfoxupdate.ir سپس foxnext.net). دانلود مشتری را ترجیحاً از foxnext.net بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Allow app update check.
2. انجام دهید: If update fails, try from foxnext.net manually.
3. انجام دهید: NEED_MORE_REVIEW for end-user visible branding of blackfoxupdate.ir.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q118
**سؤال:** دیالوگ Limited Access چیست؟
**پاسخ:** عنوان گیت دسترسی وقتی Activate یا Pro لازم است؛ همراه پیام‌های need_activate / need_pro.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Read body.
2. تب Registration را باز کنید.
3. انجام دهید: Unlock required tier.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q119
**سؤال:** می‌توانم Full Deploy را از چت AI اجرا کنم؟
**پاسخ:** بله — قالب «Full Deploy روی Central» با جزئیات SSH. AI اکشن را صف می‌کند؛ تأیید کنید و منتظر done/failed بمانید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: AI Pro mode.
2. انجام دهید: Pick Full Deploy task or paste template.
3. انجام دهید: Provide SSH.
4. انجام دهید: Confirm Yes.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q120
**سؤال:** آیا AI چت قبلی را ادامه می‌دهد؟
**پاسخ:** هنگام باز شدن ممکن است Continue یا New بپرسد؛ چت ذخیره‌شده روی دستگاه است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Read prompt.
2. انجام دهید: Reply Continue or New.
3. انجام دهید: Proceed.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q121
**سؤال:** Move Central چیست؟
**پاسخ:** جابه‌جایی نقش Central به VPS جدید (قالب AI/عملیات). به SSH مبدأ و مقصد نیاز دارد؛ پرریسک — اول بکاپ بگیرید. جزئیات کامل ویزارد: NEED_MORE_REVIEW.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Backup panel/configs.
2. انجام دهید: Provide both SSH sets.
3. انجام دهید: Run move flow.
4. انجام دهید: Update DNS/CDN to new IP.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q122
**سؤال:** تفاوت Subscription URL و لینک VLESS؟
**پاسخ:** Test Client می‌تواند هر دو را نشان دهد؛ Subscription برای اپ‌هایی است که لیست را به‌روز می‌کشند. VLESS معمولاً لینک تکی inbound است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Configure Panel.
2. انجام دهید: Open Test Client.
3. انجام دهید: Share sub URL to users who need auto-update.
4. انجام دهید: Or share single VLESS for quick test.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q123
**سؤال:** چرا بعد از Deploy توپولوژی خالی است؟
**پاسخ:** تا وقتی پنل آماده نباشد یا لینک/کلاینت نباشد، توپولوژی خالی می‌ماند (`topology_not_ready`).
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Confirm Full Deploy success.
2. انجام دهید: Add at least one link/exit path.
3. انجام دهید: Ensure panel client exists.
4. انجام دهید: Refresh View.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q124
**سؤال:** ابزارهای ایجنت Mesh از کجا دانلود می‌شوند؟
**پاسخ:** ابزار ایجنت هنگام نصب Mesh از GitHub روی همان VPS دانلود می‌شود. VPS فیلترشده ممکن است به Proxy/دسترسی GitHub سمت سرور نیاز داشته باشد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Ensure VPS can reach GitHub.
2. انجام دهید: Retry mesh install.
3. انجام دهید: NEED_MORE_REVIEW for exact repo URLs shown in logs.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q125
**سؤال:** Other CDN چیست؟
**پاسخ:** گزینه CDN برای ارائه‌دهندگان خارج از لیست اصلی در وظایف AI Pro. Diagnose & Repair جدا از پیکربندی CDN است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Choose provider or Other CDN.
2. انجام دهید: Supply API details as requested.
3. انجام دهید: Verify domain.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q126
**سؤال:** Hysteria / پورت‌های خاص؟
**پاسخ:** برخی پورت‌ها در جریان‌ها اعتبارسنجی می‌شوند؛ راهنمای Configure Panel برای inbound WG به ۸۰۸۰ اشاره دارد. جزئیات دقیق Hysteria: NEED_MORE_REVIEW.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Follow form validation.
2. انجام دهید: Don’t force closed ports.
3. انجام دهید: Check Diagnostic.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q127
**سؤال:** می‌توانم کاربر SSH غیر root استفاده کنم؟
**پاسخ:** اگر کاربر sudo برای نصب داشته باشد ممکن است؛ بسیاری اسکریپت‌ها دسترسی سطح بالا فرض می‌کنند. ترجیح root مگر ایمیج را بشناسید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Prefer root.
2. انجام دهید: If non-root, ensure passwordless sudo.
3. انجام دهید: NEED_MORE_REVIEW for full non-root support matrix.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q128
**سؤال:** رمز یا کلید — کدام ترجیح دارد؟
**پاسخ:** هر دو پشتیبانی می‌شوند؛ اگر هر دو fail شوند دیالوگ both_failed می‌آید. روی کلاد اغلب کلید؛ بعد از ریست پنل اغلب رمز.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Use provider-recommended auth.
2. انجام دهید: Paste full PEM including headers.
3. انجام دهید: Test Connect SSH.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q129
**سؤال:** معنی server draft saved چیست؟
**پاسخ:** اعتبارنامه/پیش‌نویس محلی ذخیره شده بدون اتمام Deploy (`server.draft_saved`). برای ادامه ویزارد چندصفحه‌ای مفید است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Save draft.
2. انجام دهید: Continue later.
3. انجام دهید: Connect SSH before Full Deploy.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q130
**سؤال:** عملیات در جریان است — باز هم ببندم؟
**پاسخ:** ترجیح Keep Open؛ Close Anyway کار را ناقص می‌گذارد (`dialog.close_busy_*`).
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Choose Keep Open.
2. انجام دهید: Wait for finish.
3. انجام دهید: Only Close Anyway if stuck and you accept repair later.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q131
**سؤال:** بعد از نصب چگونه زبان برنامه را عوض کنم؟
**پاسخ:** Settings → Language → Apply روی همه تب‌ها. در اولین اجرا هم انتخاب زبان هست.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Settings.
2. انجام دهید: Select language.
3. انجام دهید: Apply.
4. انجام دهید: Confirm labels updated.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q132
**سؤال:** تب Contact چه کانال‌هایی نشان می‌دهد؟
**پاسخ:** پشتیبانی `@HiBlackFoxVpn`، کانال `@BlackFoxVPN`، سایت foxnext.net، ایمیل support@foxnext.net. مقادیر زنده را از Contact بخوانید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Contact.
2. انجام دهید: Tap support for help.
3. انجام دهید: Tap channel for announcements.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q133
**سؤال:** آیا ایمیل مسیر اصلی پشتیبانی است؟
**پاسخ:** مسیر اصلی محصول معمولاً تلگرام پشتیبانی است؛ ایمیل هم هست. برای سرعت Device ID را در تلگرام بفرستید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Message @HiBlackFoxVpn.
2. انجام دهید: Use email if Telegram unavailable.
3. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q134
**سؤال:** «Update BlackFox & Wallet Address» چیست؟
**پاسخ:** اکشن Settings برای تازه‌سازی متادیتای آپدیت و نمایش wallet پرداخت از هاب.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Settings → Updates.
2. انجام دهید: Run update check.
3. انجام دهید: Install if force/min version requires.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q135
**سؤال:** حداقل نسخه اجباری برنامه را قفل کرده — چه کنم؟
**پاسخ:** نسخه حداقل پشتیبانی‌شده را نصب کنید؛ بیلدهای قدیمی ممکن است قفل شوند (`remote.force_*` / MustForceUpdate).
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Download latest Setup from foxnext.net.
2. انجام دهید: Install.
3. انجام دهید: Relaunch.
4. انجام دهید: Reactivation if license UI resets.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q136
**سؤال:** خطای timeout / شبکه سرویس AI؟
**پاسخ:** دوباره تلاش کنید؛ اینترنت/Proxy را چک کنید. پیام‌ها: timeout / could not reach AI service.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Check connectivity.
2. انجام دهید: Configure Proxy if needed.
3. انجام دهید: Resend.
4. انجام دهید: If persistent, support with Device ID.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q137
**سؤال:** AI موقتاً در دسترس نیست؟
**پاسخ:** `ai.disabled` یعنی هاب سرویس AI را خاموش کرده؛ لزوماً مشکل لایسنس محلی نیست.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Wait and retry.
2. انجام دهید: Check foxnext announcements.
3. انجام دهید: Ask @HiBlackFoxVpn.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q138
**سؤال:** برای License سهمیه پیدا نشد؟
**پاسخ:** اول AI Assistant Pro را فعال کنید (`ai.quota.not_found`). با exhausted فرق دارد.
**راه‌حل قدم‌به‌قدم:**
1. AI Pro را فعال کنید.
2. انجام دهید: Or apply BFXQ if only quota missing after AI Pro.
3. انجام دهید: Recheck status.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q139
**سؤال:** آیا Delete All رمزهای SSH را از دیسک پاک می‌کند؟
**پاسخ:** خیر — Reset All SSH را نگه می‌دارد؛ Delete History اعتبارنامه محلی را پاک می‌کند (لایسنس می‌ماند). این دو را قاطی نکنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Choose the delete that matches intent.
2. انجام دهید: Read confirm body.
3. انجام دهید: Proceed.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q140
**سؤال:** آیا Factory Reset دادهٔ پنل را نگه می‌دارد؟
**پاسخ:** خیر — هدف نزدیک‌کردن VPS به حالت اولیه است و برگشت‌ناپذیر. با Reset All (حذف بسته با نگه داشتن SSH) فرق دارد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Use only if you intend to wipe VPS.
2. انجام دهید: Prefer Delete All for app-managed cleanup.
3. انجام دهید: Re-provision after factory reset.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q141
**سؤال:** چگونه failover مش را سریع چک کنم؟
**پاسخ:** وضعیت ایجنت را Refresh کنید؛ بازیابی مسیر معمولاً چند ثانیه خودکار است. ترتیب: WG→GRE→Stealth-WSS→پشتیبان.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Deploy agents.
2. انجام دهید: Refresh Status.
3. انجام دهید: Run Link Test.
4. انجام دهید: Simulate path issue only on test beds.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q142
**سؤال:** دامنهٔ «Install always-on Link Monitor Agents» چیست؟
**پاسخ:** روی میزبان‌های Central، Tunnel، Exit و Node.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Ensure each role has SSH saved.
2. انجام دهید: Run mesh deploy.
3. انجام دهید: Confirm each host Running.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q143
**سؤال:** می‌توانم برنامه را فقط به‌عنوان مدیر بوکمارک پنل استفاده کنم؟
**پاسخ:** طراحی محصول این نیست — کتابخانه عملیاتی Deploy است؛ Panel Login Info فقط بعد از Deploy یک قابلیت است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Deploy central.
2. انجام دهید: Then use panel info/clients.
3. انجام دهید: Or open external panel manually if you already have one (limited integration without saved creds).
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q144
**سؤال:** وضعیت مشترک بین Basic / Pro / AI Pro؟
**پاسخ:** یک Store محلی مشترک برای سرور/پنل بین Basic و Pro و AI Pro — کانفیگ موازی فقط‌AI نیست.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Deploy once.
2. انجام دهید: Switch modes freely for UI.
3. انجام دهید: License still gates features.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q145
**سؤال:** تفاوت Check System و Diagnose & Repair؟
**پاسخ:** Check System تشخیص فقط‌خواندنی است؛ Diagnose & Repair تلاش برای تعمیر است. برای مدرک پشتیبانی اول read-only.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Run Checks.
2. انجام دهید: Export if needed.
3. انجام دهید: Run Diagnose & Repair if appropriate.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q146
**سؤال:** بعد از افزودن Exit تست کلاینت شکست خورد؟
**پاسخ:** دوباره Configure Panel، بررسی outbound/لینک، SSH به Exit و Diagnostic. علل رایج: Deploy ناقص Exit، WG/GRE پایین، تگ outbound ناهماهنگ، فایروال.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Confirm exit deploy success.
2. انجام دهید: Configure Panel.
3. انجام دهید: Link Test.
4. انجام دهید: Test Client again.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q147
**سؤال:** Add Node در ورود به پنل Central شکست می‌خورد؟
**پاسخ:** path یا توکن پنل کهنه — Full Deploy یا Panel Login Info را تازه کنید (`node.err_central_login`).
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Panel Login Info.
2. انجام دهید: Refresh via Full Deploy / panel install.
3. انجام دهید: Retry Add Node.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q148
**سؤال:** ریسک از دست رفتن داده در حالت Portable؟
**پاسخ:** اگر پوشه Portable جابه‌جا/حذف شود ریسک بالاست؛ حالت نصب‌شده از LocalAppData استفاده می‌کند. از پوشه بکاپ بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Keep portable.exe + data together.
2. انجام دهید: Don’t run two copies fighting the same inventory.
3. انجام دهید: Prefer Setup for stability.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q149
**سؤال:** صفحات چندزبانه سایت چه ربطی به برنامه دارند؟
**پاسخ:** سایت foxnext.net صفحات چندزبانه دارد؛ زبان برنامه جداست و از Settings عوض می‌شود.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Browse foxnext.net in your language.
2. انجام دهید: Set app language separately.
3. انجام دهید: Use same support contacts.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q150
**سؤال:** زیرعنوان «Multi-Location VPN Manager» یعنی چه؟
**پاسخ:** یعنی مدیریت Central به‌همراه چند Exit/Tunnel/Node از یک Installer؛ ارزش اصلی اتوماسیون توپولوژی چندمکانه است نه فقط یک VPS.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Full Deploy central.
2. انجام دهید: Add locations.
3. انجام دهید: Configure Panel.
4. انجام دهید: Optional mesh.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q151
**سؤال:** آیا در Factory Reset رمزها ذخیره می‌شوند؟
**پاسخ:** خیر — رمزهای Factory Reset فقط برای همان عملیات‌اند و ذخیره نمی‌شوند؛ برخلاف Save معمولی سرور.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Enter creds for factory reset only.
2. انجام دهید: They won’t be kept.
3. انجام دهید: Re-save server normally if you continue using it.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q152
**سؤال:** معنی «SSH connected but probe output unexpected»؟
**پاسخ:** احراز هویت OK بوده ولی خروجی probe غیرمنتظره است (`log.ssh_probe_unexpected`). ممکن است شل/MOTD عجیب یا دستور مسدود باشد. جزئیات دقیق: NEED_MORE_REVIEW.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Confirm distro is supported Linux.
2. انجام دهید: Retry Connect SSH.
3. انجام دهید: Check provider serial console.
4. انجام دهید: Send log line to support.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q153
**سؤال:** می‌توانم اسکرین‌شات پنل سرور را به چت AI بچسبانم؟
**پاسخ:** بله — تا ۳ تصویر؛ AI چندوجهی است (متن+تصویر) برای جزئیات سرور/ربات و غیره.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Attach clear screenshots.
2. انجام دهید: Add short text.
3. انجام دهید: Confirm extracted details selection.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q154
**سؤال:** AI اشتباه Exit را به‌جای Node تشخیص داد؟
**پاسخ:** رد کنید و با توضیح دوباره بفرستید؛ مسیر reject از شما می‌خواهد هدف را روشن کنید یا Task را انتخاب کنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Reply No.
2. انجام دهید: State Exit or Node clearly.
3. انجام دهید: Resend details or use left-task buttons.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q155
**سؤال:** وضعیت Apply Actions در چت AI چیست؟
**پاسخ:** برنامه اکشن‌های صف‌شده از پاسخ AI را اعمال می‌کند (preparing… applying_actions… finalizing).
**راه‌حل قدم‌به‌قدم:**
1. صبر کنید.
2. انجام دهید: Confirm any Yes/No prompts.
3. انجام دهید: Watch terminal for real deploy results.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q156
**سؤال:** آیا مبلغ USDT همیشه ۱۹/۳۳/۴۰ است؟
**پاسخ:** ۱۹/۳۳/۴۰ لنگر/fallback رایج‌اند؛ کاتالوگ زنده بر اساس ماه فرق دارد. همیشه مبلغ روی صفحه foxnext.net / داخل برنامه را بپردازید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Read on-screen amount.
2. انجام دهید: Pay exactly that on BEP-20.
3. انجام دهید: Don’t assume old chat prices.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q157
**سؤال:** اگر Reactivation بگوید tier mismatch؟
**پاسخ:** رکورد سرور هست ولی با سطح درخواستی جور نیست (`tier_mismatch`). سطح درست را Activate کنید یا با پشتیبانی هم‌تراز کنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Confirm which product you bought.
2. انجام دهید: Try matching activate button.
3. انجام دهید: Message support with Device ID.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q158
**سؤال:** بعد از claim می‌توانم کدها را از TX قدیمی بازیابی کنم؟
**پاسخ:** معمولاً خیر — بعد از claim، TX کد را نشان نمی‌دهد. روی دستگاه bind‌شده Reactivation کنید یا با Device ID به پشتیبانی بروید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Try Reactivation on original PC.
2. انجام دهید: Provide Device ID + TX to @HiBlackFoxVpn.
3. انجام دهید: Do not expect website to reprint claimed codes.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q159
**سؤال:** مسیر پیشنهادی اولین اجرا برای کاربر جدید؟
**پاسخ:** Setup → زبان → Basic → Central → Connect SSH → Full Deploy → Panel Info → در صورت نیاز Exit بعد از Activate. شبکه محدود: Proxy. گیر کردید: `@HiBlackFoxVpn`.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Setup.exe from foxnext.net.
2. انجام دهید: Basic mode.
3. انجام دهید: Central IR/CN/RU.
4. Connect SSH را اجرا کنید.
5. Full Deploy را اجرا کنید.
6. انجام دهید: Test Client.
7. Pro را فعال کنید.
8. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q160
**سؤال:** پشتیبان برای متن دقیق UI به کجا نگاه کند؟
**پاسخ:** برای متن دقیق UI به `internal/i18n/en.go` / `locales/en.json` و `reason_code`های API هاب نگاه کنید. stderr لینوکس ناشناس را NEED_MORE_REVIEW بگذارید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Match screenshot to i18n.
2. انجام دهید: Use Troubleshooting.md for error playbooks.
3. انجام دهید: Escalate with Device ID + logs.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q161
**سؤال:** تعویض حالت View سرورها را پاک می‌کند؟
**پاسخ:** خیر — حالت‌ها یک Store محلی مشترک دارند. عوض کردن View فقط شکل UI و گیت‌ها را عوض می‌کند، سرورها را پاک نمی‌کند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Save work if a wizard is open.
2. انجام دهید: Change mode on View.
3. انجام دهید: Confirm servers still listed under Operations.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q162
**سؤال:** تفاوت Configure Panel و Full Deploy؟
**پاسخ:** Full Deploy روی Central، WG+پنل نصب می‌کند؛ Configure Panel مسیریابی Exit/Node موجود را تعمیر می‌کند و نصب دوباره پنل Central نیست.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Finish Full Deploy first.
2. انجام دهید: Add Exit/Node as needed.
3. انجام دهید: Run Configure Panel.
4. انجام دهید: Use Panel Login Info only to view URL/creds.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q163
**سؤال:** چند Node می‌توانم اضافه کنم؟
**پاسخ:** حداکثر ۶ نود (`MaxNodes`)؛ همان منطق اسلات Exit در Pro.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Unlock Pro.
2. انجام دهید: Open Add Node.
3. انجام دهید: Fill SSH + XUI source.
4. انجام دهید: Stop at six or replace a slot.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q164
**سؤال:** Full Deploy / Add Node از چه منابع XUI استفاده می‌کنند؟
**پاسخ:** Sanaei GitHub، BlackFox Hub، یا بسته Local PC. در Full Deploy و Add Node انتخاب می‌شود. Local برای آفلاین/فیلتر است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Prefer Hub when online.
2. انجام دهید: Use Local if you have a verified package.
3. انجام دهید: GitHub when Hub is blocked (may be slower).
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q165
**سؤال:** Delete History چه چیزهایی را نگه می‌دارد؟
**پاسخ:** تاریخچه محلی را پاک می‌کند؛ زبان، حالت و لایسنس می‌ماند. با Reset All (حذف WG/پنل ریموت با نگه داشتن SSH) فرق دارد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open the delete/history control.
2. انجام دهید: Confirm.
3. انجام دهید: Re-check Registration still unlocked.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q166
**سؤال:** DELETE — Reset All Servers چه می‌کند؟
**پاسخ:** WG/پنل را از سرورهای پیکربندی‌شده برمی‌دارد؛ SSH ذخیره‌شده می‌ماند. بعداً باید دوباره Full Deploy کنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Confirm inventory is correct.
2. انجام دهید: Run Reset All Servers.
3. Connect SSH را اجرا کنید.
4. انجام دهید: Full Deploy again.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q167
**سؤال:** می‌توانم فقط hopهای Tunnel را حذف کنم؟
**پاسخ:** بله — Delete Tunnel Servers فقط hopهای زنجیره Pro را ریست می‌کند و لزوماً Exit/Central را پاک نمی‌کند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Pro mode.
2. انجام دهید: Use Delete Tunnel Servers.
3. انجام دهید: Re-add tunnels if still needed.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q168
**سؤال:** چه پروفایل‌های Proxy وجود دارد؟
**پاسخ:** پروفایل‌هایی مثل None / Auto / Iran / Free در Proxy Settings. سیاست شبکه: اول Direct، شکست → Program Proxy برای SSH، هاب HTTP و API پنل.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Proxy Settings.
2. انجام دهید: Try Auto if Direct fails.
3. انجام دهید: Iran profile when in restricted networks.
4. انجام دهید: Retry Connect SSH / updates.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q169
**سؤال:** بعد از Deploy آدرس پنل را کجا ببینم؟
**پاسخ:** Panel Login Info آدرس/کاربر/رمز ذخیره‌شده را بعد از نصب/همگام موفق پنل نشان می‌دهد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Complete Full Deploy.
2. انجام دهید: Open Panel Login Info.
3. انجام دهید: Copy URL carefully (port + path).
4. انجام دهید: Log in via browser if needed.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q170
**سؤال:** Test Client / WG برای چیست؟
**پاسخ:** دیالوگ تست کلاینت/WireGuard برای اعتبارسنجی بعد از Configure؛ جایگزین Full Deploy نیست.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Ensure panel + exit path ready.
2. انجام دهید: Open Test Client.
3. انجام دهید: Import/test as prompted.
4. انجام دهید: If fail, run Link Test / diagnostics.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q171
**سؤال:** Add Domain چیست؟
**پاسخ:** مدیر DNS پرو برای Cloudflare / ArvanCloud (زون/رکورد؛ وبهوک بات اختیاری). پوشش است نه تب اصلی.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Unlock Pro.
2. انجام دهید: Open Add Domain / DNS Manager.
3. انجام دهید: Enter API credentials.
4. انجام دهید: Create/update records.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q172
**سؤال:** کدام ارائه‌دهندگان CDN در UI هستند؟
**پاسخ:** در UI معمولاً Arvan، Cloudflare و Other CDN. اگر برند چهارم دیدید NEED_MORE_REVIEW — ممکن است کلید داخلی UI نباشد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Pro mode.
2. انجام دهید: Open CDN modal.
3. انجام دهید: Pick Arvan/Cloudflare/Other.
4. انجام دهید: Save; apply via API when available.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q173
**سؤال:** Mesh Servers چیست؟
**پاسخ:** صفحه Pro برای گراف inventory، Deploy ایجنت Link Monitor و وضعیت لینک؛ جدا از شبکه Operations.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Unlock Pro.
2. انجام دهید: Open Mesh Servers.
3. انجام دهید: Deploy agents when prompted.
4. انجام دهید: Read link status; repair via ops if down.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q174
**سؤال:** Add Telegram Bot (Mirza) چیست؟
**پاسخ:** ابزار Pro برای نصب/انتقال Mirza (یا مسیر Other). با ربات پشتیبانی Black Fox فرق دارد؛ خانواده فروش پنل Mirza است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Pro unlock.
2. انجام دهید: Open Add Telegram Bot.
3. انجام دهید: Choose install / other / move.
4. انجام دهید: Supply bot token when asked.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q175
**سؤال:** Move Central Server چیست؟
**پاسخ:** جابه‌جایی نقش Central به VPS دیگر (ابزار Pro). اثر بالا — inventory و credentials پنل باید یکدست بمانند. فیلدهای دقیق ویزارد: NEED_MORE_REVIEW.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Backup panel/creds.
2. انجام دهید: Unlock Pro.
3. انجام دهید: Open Move Central.
4. انجام دهید: Follow wizard; re-verify Panel Login Info.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q176
**سؤال:** BlackFox MCP در Tasks هوش مصنوعی چیست؟
**پاسخ:** فعال‌سازی باینری MCP / mcp.json تا ابزارهای AI بیرونی اکشن‌های Black Fox را صدا بزنند. برای چت داخل برنامه لازم نیست.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: AI Pro unlocked.
2. انجام دهید: Run BlackFox MCP task.
3. انجام دهید: Confirm desktop MCP config.
4. انجام دهید: Use only if integrating external agents.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q177
**سؤال:** تفاوت Diagnose & Repair و Check System؟
**پاسخ:** Check System تب Diagnostics محلی است؛ Diagnose & Repair مسیر Task در AI Pro با تأیید قبل از تغییر.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: For quick local status → Check System.
2. انجام دهید: For guided fix → AI Pro Diagnose & Repair.
3. انجام دهید: Confirm Yes before apply.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q178
**سؤال:** Link Test (AI) چیست؟
**پاسخ:** قالب Task هوش مصنوعی برای تست لینک‌های توپولوژی؛ مکمل Configure Panel و Test Client با تأیید قبل از اجرا.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: AI Pro chat.
2. انجام دهید: Choose Link Test.
3. انجام دهید: Confirm.
4. انجام دهید: Read terminal/status outcome.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q179
**سؤال:** Add OutBounds (AI) چیست؟
**پاسخ:** Task هوش مصنوعی برای پیکربندی outbound پنل؛ ترجیحاً بعد از وجود Exit/Node و با تأیید قبل از Apply.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Ensure central panel ready.
2. انجام دهید: AI task Add OutBounds.
3. انجام دهید: Confirm extracted details.
4. انجام دهید: Verify in panel if needed.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q180
**سؤال:** آیا Factory Reset رمزی که تایپ می‌کنم را ذخیره می‌کند؟
**پاسخ:** خیر — رمزهای واردشده برای Factory Reset فقط همان عملیات‌اند و برای بعد ذخیره نمی‌شوند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Enter creds when asked.
2. انجام دهید: Complete reset.
3. انجام دهید: Re-save SSH normally if you continue.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q181
**سؤال:** زبان برنامه کجا عوض می‌شود؟
**پاسخ:** Settings → اعمال زبان (و انتخابگر اولین اجرا). زبان سایت foxnext.net جدا از کاتالوگ i18n برنامه است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Settings.
2. انجام دهید: Choose language.
3. انجام دهید: Apply.
4. انجام دهید: Confirm labels update (RTL for FA).
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q182
**سؤال:** مدیر بسته 3X-UI در Settings چیست؟
**پاسخ:** بخش Tools برای مدیریت بسته‌های 3X-UI آفلاین/هاب مورد استفاده Deploy و Local PC. برچسب دقیق UI را با Settings فعلی تطبیق دهید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Settings → Tools / packages.
2. انجام دهید: Refresh from hub if online.
3. انجام دهید: Use Local path when offline.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q183
**سؤال:** چه چیزی باعث force update می‌شود؟
**پاسخ:** زیر حداقل نسخه/بیلد پشتیبانی‌شده، یا پرچم force با نسخه جدیدتر ریموت. `version.json` هاب فیدها را می‌راند؛ شماره را اختراع نکنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Allow update dialog.
2. انجام دهید: Download from official hub/site.
3. انجام دهید: Reinstall Setup if portable is stale.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q184
**سؤال:** PAS Generator چیست؟
**پاسخ:** ابزار ادمین جدا (`cmd/pas-generator`) برای گردش PAS. مسیر اصلی مشتری نیست؛ مشتری foxnext.net + Registration را دارد.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Operators only.
2. انجام دهید: Do not ask customers to run PAS Generator unless support instructs.
3. انجام دهید: Customers use Activate / claim codes.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q185
**سؤال:** Config Builder چیست؟
**پاسخ:** APK جدا در `version.json` → `config_builder`. محصول مرتبط است و سورسش در این ریپوی ویندوز نیست؛ با اپ VPN اندروید اصلی قاطی نکنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Download from official hub/site if offered.
2. انجام دهید: Do not expect Installer tabs inside Config Builder.
3. انجام دهید: Support Installer vs Config Builder separately.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q186
**سؤال:** کشورهای رایگان Central در Basic کدام‌اند؟
**پاسخ:** بدون Pro برای Central رایگان: ایران، چین، روسیه (`IsFreeCentralCountry`). کشورهای دیگر معمولاً مسیر Pro می‌خواهند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Basic mode.
2. انجام دهید: Pick IR/CN/RU for free central path.
3. Pro را فعال کنید.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q187
**سؤال:** آیا License پرو چت AI را باز می‌کند؟
**پاسخ:** خیر — چت AI به unlock جداگانه AI Pro و quota نیاز دارد. Pro فقط داشبورد Pro را باز می‌کند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Activate AI Assistant Pro.
2. انجام دهید: Select AI Pro on View.
3. انجام دهید: Confirm quota.
4. انجام دهید: Chat/tasks.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q188
**سؤال:** چه پیشوندهای کدی وجود دارد؟
**پاسخ:** BFXB Basic، BFXP Pro، BFXA AI Pro، BFXQ سهمیه، BFXT تست؛ claimها `-CLM-` دارند. پیشوند اشتباه → unlock غلط یا خطا.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Copy full code.
2. انجام دهید: Paste Activate.
3. انجام دهید: If claim code, ensure unused TX.
4. انجام دهید: Use Reactivation if rebound needed.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q189
**سؤال:** My Code در Registration چیست؟
**پاسخ:** بعد از unlock موفق، کد ذخیره‌شده را نشان می‌دهد؛ برای تیکت مفید است ولی مثل رمز محافظت کنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Activate successfully.
2. انجام دهید: Open My Code.
3. انجام دهید: Share with support only when asked.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q190
**سؤال:** System ID / Device ID چیست؟
**پاسخ:** اثرانگشت ماشین برای bind لایسنس؛ برای Activation سایت و Reactivation لازم است. تعویض سخت‌افزار ممکن است bind را بشکند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Registration tab.
2. Device ID را کپی کنید.
3. انجام دهید: Use on foxnext.net Activation.
4. انجام دهید: Keep for support.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q191
**سؤال:** اگر ماه‌ها مشخص نباشد مدت پیش‌فرض License؟
**پاسخ:** اگر ماه مشخص نباشد اغلب ۱۸ ماه در منطق لایسنس؛ کاتالوگ زنده ۱۲–۳۰ ماه و تخفیف چند دستگاه دارد. مدت روی صفحه را معیار بگیرید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Read purchase page months.
2. انجام دهید: Pay matching amount.
3. انجام دهید: Activate with issued code.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q192
**سؤال:** برنامه از چه هاب‌هایی استفاده می‌کند؟
**پاسخ:** اصلی `blackfoxupdate.ir`، ثانویه `foxnext.net` برای version، runtime-config، license-access، AI و بسته‌ها؛ در فیلتر failover.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Keep internet.
2. انجام دهید: If updates fail, try Proxy.
3. انجام دهید: Confirm official site for downloads.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q193
**سؤال:** راه‌های پشتیبانی از کانفیگ محصول؟
**پاسخ:** شامل `@HiBlackFoxVpn`، `@BlackFoxVpnn`، `@BlackFoxVpn_bot`، `@Black_Fox_Group` از runtime contact. لیست زنده Contact را ترجیح دهید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Contact tab.
2. انجام دهید: Use listed Telegram/email.
3. انجام دهید: Include Device ID in tickets.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q194
**سؤال:** املای GitHub عمومی عمدی است؟
**پاسخ:** هاب ممکن است `github.com/balckfoxgroup/blackfox-vpn-installer` را نشان دهد — همان رشته منتشرشده را استفاده کنید و املا را «درست» نکنید اگر لینک Contact همان است.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Open Contact → GitHub.
2. انجام دهید: Follow the in-app URL.
3. انجام دهید: Don’t invent alternate orgs.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q195
**سؤال:** برای Full Deploy اندروید بهتر است یا Windows؟
**پاسخ:** برای Full Deploy و Mesh از Windows Installer استفاده کنید؛ Android همراه است و workstation اصلی Deploy معمولاً Windows می‌ماند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Deploy from Windows.
2. انجام دهید: Use Android for mobile monitoring/AI where available.
3. انجام دهید: Import WG client configs on any OS WireGuard app.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q196
**سؤال:** دو کپی Portable می‌توانند یک inventory را ایمن شریک شوند؟
**پاسخ:** پرریسک — یک پوشه Portable یا Setup+LocalAppData را ترجیح دهید. دو کپی ممکن است روی یک inventory با هم تداخل کنند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Use one working copy.
2. انجام دهید: Backup portable folder.
3. انجام دهید: Prefer Setup install for stability.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q197
**سؤال:** AI هرگز چه چیزهایی را نباید اختراع کند؟
**پاسخ:** شماره نسخه، قیمت، برند هاستینگ، و stderr لینوکسی که در i18n نیست. هویت: BlackFox AI؛ ابهام را NEED_MORE_REVIEW علامت بزنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Answer from KB.
2. انجام دهید: If unknown, say so.
3. انجام دهید: Ask for screenshot + Device ID.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q198
**سؤال:** اسکرین‌شات‌های آموزش کجا هستند؟
**پاسخ:** پوشه `/Screenshots` با README؛ گرفتن زنده همه دیالوگ‌ها هنوز ناقص است. mode picker، داشبورد Basic/Pro، اندروید و مارکتینگ موجودند.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Pick matching asset from README.
2. انجام دهید: Do not claim a missing dialog screenshot exists.
3. انجام دهید: Request user screenshot when needed.
4. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q199
**سؤال:** چت‌بات برای Deploy گیرکرده چه ترتیبی پیشنهاد دهد؟
**پاسخ:** ترتیب: Proxy → Connect SSH → منبع Full Deploy → Panel Login Info → Configure Panel → Diagnostic. اول Delete/Reset نپرید. گیت رایگان Basic را از لایسنس جدا کنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Verify mode/license.
2. انجام دهید: Proxy if network fails.
3. Connect SSH را اجرا کنید.
4. Full Deploy را اجرا کنید.
5. انجام دهید: Check System / AI Diagnose.
6. انجام دهید: Support if still blocked.
7. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.

### Q200
**سؤال:** فایل اصلی ورود RAG کدام است؟
**پاسخ:** فایل اصلی RAG: `Documentation/AI_Knowledge_Base.md` به‌همراه راهنماها، FAQ، Troubleshooting و `Screenshots/README`. برای ربات چندزبانه از `AI_Knowledge_Base_Multilingual` و `AI_BOT_DATABASE` استفاده کنید.
**راه‌حل قدم‌به‌قدم:**
1. انجام دهید: Load AI_Knowledge_Base.md.
2. انجام دهید: Retrieve FAQ/Troubleshooting for errors.
3. انجام دهید: Cite Feature_List for gates.
4. انجام دهید: Mark NEED_MORE_REVIEW honestly.
5. اگر حل نشد Device ID را به @HiBlackFoxVpn بفرستید.
**خطاهای احتمالی:** خطاهای رایج: need activate/Pro، SSH fail، شکست Full Deploy، AI quota، Proxy، host key. وضعیت و terminal را ببینید؛ در صورت نیاز Device ID + اسکرین به @HiBlackFoxVpn.
