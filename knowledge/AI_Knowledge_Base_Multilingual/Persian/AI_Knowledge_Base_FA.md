# Black Fox VPN — پایگاه دانش هوش مصنوعی (فارسی)

> مخاطب: AI Assistant، ربات تلگرام، پشتیبانی.  
> قوانین: شمارهٔ نسخه، قیمت یا برند هاستینگ اختراع نکن. خرید VPS فقط از **FoxNext.net → Partners / همکاران**. موارد نامشخص: `NEED_MORE_REVIEW`.  
> برچسب‌های UI انگلیسی را Title Case نگه دار: `Full Deploy`, `Connect SSH`, `Registration`.

---

## ۱. معرفی محصول

**Black Fox Vpn** یک **Installer عملیاتی** برای Windows است (نسخهٔ همراه Android هم وجود دارد). روی **VPS لینوکسی شما** با **SSH**، **WireGuard** و پنل **3X-UI (Sanaei)** زیرساخت VPN چندمکانه می‌سازد.

این برنامه **کلاینت مصرف‌کنندهٔ «وصل شو و وب‌گردی کن»** نیست.

**سایت / هاب:** `foxnext.net` ، `blackfoxupdate.ir`  
**پشتیبانی:** تب Contact / `@HiBlackFoxVpn`

---

## ۲. معماری کوتاه

```
UI (Windows / Android)
  → ذخیرهٔ محلی مشترک (Basic / Pro / AI Pro)
  → SSH + اسکریپت‌های سرور + API پنل
  → هاب‌ها: blackfoxupdate.ir سپس foxnext.net
شبکه: اول Direct، در شکست Program Proxy
```

نقش‌ها: **Central** (پنل + WG) · **Exit** (خروج، حداکثر ۶) · **Tunnel** (پر hop) · **Node** (نود پنل، حداکثر ۶) · **Mesh** (لینک بین سرورها)

**Configure Panel ≠ نصب پنل روی Central.** نصب پنل مرکزی با **Full Deploy** است.

---

## ۳. حالت‌ها و License

حالت‌ها: `basic` | `pro` | `ai_pro`

| حالت | نکته |
|------|------|
| Basic | بدون License فقط: Setup Central + Connect SSH + Full Deploy |
| Pro | تونل، نود، Domain، CDN، Mesh، Mirza، Move Central… |
| AI Pro | همان عملیات Pro از طریق چت + Tasks؛ **جدا از Pro**؛ نیاز به سهمیه (quota) |

کدها: `BFXB` Basic · `BFXP` Pro · `BFXA` AI Pro · `BFXQ` شارژ AI · claim با `-CLM-`

در Basic، Central رایگان معمولاً باید در **ایران / چین / روسیه** باشد.

---

## ۴. قابلیت‌ها (خلاصهٔ عملیاتی)

Setup Central · Connect SSH · Full Deploy · Exit (۶ اسلات) · Tunnel · Node · Configure Panel · Domain/DNS · CDN · Mesh · Mirza Bot · Move Central · Proxy · Panel Login Info · Test Client · Registration · Check System · Deletes/Reset · AI Tasks (MCP، OutBounds، Diagnose & Repair، Link Test)

منبع نصب 3X-UI در Full Deploy: Sanaei GitHub / BlackFox Hub / Local PC

انواع لینک: WireGuard · GRE · Reverse Tunnel (Stealth-WSS)

---

## ۵. صفحات و تب‌ها

| تب | کاربرد |
|----|--------|
| Operations | دکمه‌های عملیات / در AI Pro چت |
| Check System | تشخیص سلامت (فقط‌خواندنی) |
| View | تعویض حالت + توپولوژی |
| Settings | زبان، Update، Packages، Factory Reset (Pro) |
| Registration | Device ID، Activate، Reactivation |
| Contact | لینک‌های پشتیبانی |

پوشش‌ها: Add Domain، Mesh Servers

---

## ۶. راهنمای مبتدی

۱. نصب از foxnext.net  
۲. زبان → SELECT BASIC  
۳. Central Server Setup → Connect SSH → Full Deploy  
۴. Panel Login Info  
۵. برای Exit: فعال‌سازی Basic در Registration  

اشتباهات رایج: تصور کلاینت مصرف‌کننده بودن برنامه؛ رد شدن از Connect SSH؛ Exit بدون License؛ انتخاب AI Pro بدون فعال‌سازی.

---

## ۷. راهنمای حرفه‌ای

ترتیب پیشنهادی Pro: Tunnel → Exit → Configure Panel → Node → Domain → CDN → Mesh → Mirza → Move Central فقط هنگام جابه‌جایی.

AI Pro: فعال‌سازی `BFXA` + quota؛ تأیید Yes/No قبل از اعمال؛ تب Check System با Diagnose & Repair فرق دارد.

---

## ۸–۹. مشکلات و خطاها

| نشانه | اقدام اول |
|-------|-----------|
| Need activate | Registration |
| AI قفل | AI Pro + quota |
| SSH fail | بررسی Credential + Proxy |
| Full Deploy fail | تعویض منبع نصب؛ خواندن terminal |
| Configure Panel خطا | اول Exit/Node بساز |

مسیر پشتیبانی: وضعیت + terminal → Proxy در صورت نیاز → Check System → `@HiBlackFoxVpn` با Device ID

---

## ۱۰. ارتباط بین بخش‌ها

Full Deploy موفق → Panel Login Info در همهٔ حالت‌ها (یک Store).  
حذف Tunnel → ممکن است hopهای بالاتر ریست شوند.  
فقط Pro → AI هنوز قفل است.

---

## قوانین پاسخ AI

۱. فقط دربارهٔ Black Fox / عملیات سرور.  
۲. زبان کاربر را رعایت کن.  
۳. نسخه اختراع/بحث نکن؛ هویت: BlackFox AI.  
۴. VPS فقط Partners در FoxNext.  
۵. قبل از تغییر مخرب روی سرور، تأیید بگیر.
