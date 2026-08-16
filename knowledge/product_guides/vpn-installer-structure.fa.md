# نقشه محصول Black Fox VPN Installer & Android

این فایل دانش پشتیبان Ask AI است. وقتی کاتالوگ جزئیات کافی نداد، از اینجا برای توضیح ساده استفاده شود. اعداد نسخه را از خودت نساز.

## نام رسمی
در پاسخ‌ها همیشه بگو: **Black Fox VPN Installer & Android**

## این محصول چیست؟
برنامه Black Fox VPN Installer & Android ابزار نصب و مدیریت زیرساخت VPN روی سرور Linux است؛ کلاینت مصرف‌کننده برای گشت‌وگذار نیست. کار اصلی‌اش اتصال SSH به VPS و اجرای عملیات پنل 3X-UI و WireGuard است.

## تب‌ها و مسیر کلی
- Operations: کار روزانه مثل Connect SSH، Full Deploy، Exit/Node/Tunnel، Domain، CDN، Configure Panel
- Check System: بررسی سلامت و وضعیت
- View: مشاهده Topology و وضعیت لینک‌ها
- Settings: تنظیمات و Factory Reset
- Registration: فعال‌سازی لایسنس Pro / AI Pro
- Contact: ارتباط با سازنده

## ترتیب پیشنهادی راه‌اندازی Central
1. Registration در صورت نیاز به Pro / AI Pro
2. Central Server Setup برای ذخیره Host و Port و User و رمز/کلید
3. Connect SSH برای تست اتصال
4. Full Deploy برای نصب یکجای 3X-UI Sanaei و WireGuard
5. Panel Login Info برای دیدن آدرس و یوزر و رمز و توکن
6. در صورت نیاز Configure Panel برای inbound/outbound و رله
7. Add Exit / Node / Tunnel طبق معماری
8. Domain یا CDN در صورت نیاز عمومی‌سازی دسترسی
9. Mesh و Topology برای پایش و لینک‌ها

## معنی بخش‌های پرتکرار
### Connect SSH
اتصال و تست نشست SSH به سرور مرکزی ذخیره‌شده.

### Full Deploy
نصب یکجای پنل و WireGuard روی سرور مرکزی از مسیرهای مشخص‌شده در برنامه.

### Configure Panel
پیکربندی inbound و outbound و رله برای مرکزی یا Nodeها؛ معمولاً بعد از Deploy و افزودن Exit/Node.

### Panel Login Info
نمایش اطلاعات ورود پنل بعد از نصب.

### Add Exit Servers
افزودن سرور خروجی تا حداکثر ۶ اسلات.

### Add Node Servers
ثبت پنل 3X-UI دیگر به‌عنوان Node تا حداکثر ۶.

### Add Tunnel Servers
هاپ میانی بین مرکزی و Exit در زنجیره چندhop (مد Pro).

### Domain / CDN / Free Domain / External Proxy
روش‌های دامنه و پروکسی برای دسترسی عمومی یا مخفی‌سازی مسیر. جزئیات سهمیه Free Domain (Pro=۳، AI Pro=۵) و فعال‌سازی خودکار در Configure را از فایل `vpn-installer-domain-mesh` و کاتالوگ بخوان.

### Mesh / Topology
Mesh Servers: نمای Topology و Deploy / Repair برای Link Monitor Agent. جزئیات در `vpn-installer-domain-mesh`.

### Terminal / Status Bar
ترمینال برای دستور روی سرور؛ نوار وضعیت برای بازخورد عملیات طولانی.

### Factory Reset
بازنشانی خطرناک تنظیمات محلی برنامه؛ قبل از تأیید پیام هشدار را بخوان.

## مدها
- Basic: هسته رایگان شامل Setup Central و Connect SSH و Full Deploy
- Pro و AI Pro: امکانات پیشرفته‌تر طبق لایسنس؛ جزئیات قیمت فقط از کاتالوگ لایسنس

## قانون پاسخ
اگر در کاتالوگ یا این نقشه چیزی نبود، بگو اطلاعات کافی در منابع محصول نیست و کاربر را به پشتیبانی ارجاع بده. جزئیات ساختگی ننویس.
