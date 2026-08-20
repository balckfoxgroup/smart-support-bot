# Black Fox VPN — راهنمای کاربر (فارسی)

> برای مشتری، ربات تلگرام و AI. اصطلاحات فنی استاندارد را به انگلیسی نگه دار: License، Server، Panel، VPN، Installer، Update، Configuration، SSH، WireGuard.

---

## ۱. معرفی

Black Fox Vpn یک Installer عملیاتی است که روی VPS لینوکس شما WireGuard و Panel سه‌گانهٔ 3X-UI را با SSH خودکار می‌کند. کلاینت مصرف‌کنندهٔ موبایل برای «فقط وصل شدن» نیست.

سایت: foxnext.net — پشتیبانی: تب Contact / `@HiBlackFoxVpn`

---

## ۲. قابلیت‌ها

نگاه کنید به جدول قابلیت‌ها در `AI_Knowledge_Base_FA.md` بخش ۴. نکات حیاتی:

- بدون License در Basic فقط Setup Central، Connect SSH، Full Deploy
- حداکثر ۶ Exit و ۶ Node
- Configure Panel فقط برای Exit/Node موجود است
- Pro ≠ AI Pro

---

## ۳. نصب

۱. از foxnext.net فایل Setup را دانلود کنید.  
۲. نصب را اجرا کنید.  
۳. زبان را انتخاب کنید.  
۴. حالت Basic / Pro / AI Assistant Pro را انتخاب کنید.  
۵. وارد پنجرهٔ اصلی شوید.

---

## ۴. استفاده روزمره

۱. Operations → Central Server Setup (IP، پورت، کاربر، رمز یا کلید)  
۲. Connect SSH  
۳. Full Deploy (منبع: GitHub / Hub / Local PC)  
۴. Panel Login Info  
۵. در صورت نیاز Test Client  
۶. برای Exit: Registration → Device ID → Activate → Add Exit Server → Configure Panel  

---

## ۵. توضیح صفحات

- **Operations:** عملیات اصلی یا چت AI  
- **Check System:** عیب‌یابی محلی  
- **View:** تعویض حالت و توپولوژی  
- **Settings:** زبان، Update، Packages، Factory Reset  
- **Registration:** فعال‌سازی License  
- **Contact:** راه‌های ارتباط  

---

## ۶. مبتدی

Basic را انتخاب کنید · Central در IR/CN/RU · اول SSH بعد Deploy · قبل از Exit لایسنس بگیرید · در شبکهٔ محدود Proxy Settings را امتحان کنید.

---

## ۷. حرفه‌ای

ترتیب Pro: Tunnel → Exit → Configure Panel → Node → Domain → CDN → Mesh → Bot.  
AI Pro: `BFXA` + quota؛ از Tasks استفاده کنید؛ قبل از اجرا تأیید کنید.

لینک‌ها: WireGuard · GRE · Reverse Tunnel (Stealth-WSS)

---

## ۸–۹. مشکلات و راه‌حل

SSH قطع: Credential، فایروال، Proxy.  
Deploy شکست: منبع دیگر، لاگ terminal.  
AI قفل: فعال‌سازی AI Pro و شارژ.  
نیاز به Activate: تب Registration.

حذف‌ها: Delete History فقط محلی؛ Reset All Servers پنل/WG ریموت را پاک می‌کند ولی SSH را نگه می‌دارد؛ Factory Reset مخرب است (Pro).

---

## ۱۰. ارتباط بخش‌ها

یک Store مشترک بین حالت‌ها · تغییر Panel روی همهٔ حالت‌ها اثر دارد · حذف hop تونل روی زنجیره اثر زنجیره‌ای دارد.
