# دامنه، پیکربندی و Mesh — Black Fox VPN Installer & Android

دانش پشتیبان Ask AI برای برنامه **Black Fox VPN Installer & Android**. اعداد نسخه را از خودت نساز. اگر جزئیات در کاتالوگ دقیق‌تر بود، کاتالوگ را ترجیح بده.

## نام رسمی محصول
در پاسخ‌های ربات همیشه از این نام استفاده کن: **Black Fox VPN Installer & Android**

## Add Domain
سه تب در یک بخش:

### ۱) DNS
اتصال Cloudflare یا ArvanCloud برای دامنه اختصاصی خود کاربر؛ زون و رکورد A برای سرور مرکزی یا وبهوک بات. جدا از دامنه رایگان Black Fox است.

### ۲) External Proxy
تا ۳ دامنه عمومی روی پورت inbound پنل مرکزی. پیش‌نیاز: Full Deploy و اعتبارنامه پنل. با Apply to Panel اعمال می‌شود. جایگزین Free Domain نیست.

### ۳) Free Domain
ساب‌دامین رایگان Black Fox روی سرور انتخابی.

| مد | سهمیه ساب‌دامین رایگان در هر نصب |
| --- | --- |
| Basic | ۰ (غیرفعال) |
| Pro | ۳ |
| AI Pro | ۵ |

پسوندها: `.ir` ، `.store` ، `.online` ، `.site` — برای کاربران ایران ترجیحاً `.ir`.

مراحل کوتاه: انتخاب سرور → انتخاب پسوند → Get Free Domain from Black Fox → در صورت نیاز Refresh Domain List → کپی آدرس از Your Domain.

## Configure Panel و فعال‌سازی خودکار دامنه
Configure Panel برای inbound/outbound و رله است.

هنگام پیکربندی دامنه، اگر مد Pro یا AI Pro فعال باشد و سهمیه Free Domain باقی باشد، ساب‌دامین رایگان به‌صورت **خودکار** روی همان سرور (مرکزی / Exit / Node) فعال می‌شود و روی ساب‌کانفیگ‌ها ست می‌گردد.

اگر سهمیه تمام شده باشد: پیکربندی پنل تمام می‌شود، ولی دامنه روی ساب‌کانفیگ‌ها ست نمی‌شود.

## Mesh Servers
- تب View: Topology زنده Central / Tunnel / Exit / Node و وضعیت لینک‌ها
- تب Deploy / Repair: نصب Link Monitor Agent روی میزبان‌های دارای SSH؛ پایش WireGuard و GRE و Reverse Tunnel Stealth-WSS حتی با بسته بودن برنامه
- ترتیب failover پایه: WireGuard → GRE → Reverse Tunnel Stealth-WSS
- مسیرهای پشتیبان اختیاری و Optimize VPS روی لینک انتخابی

پیش‌نیاز: ثبت سرورها با SSH؛ برای Topology معمولاً بعد از Deploy یا لینک‌های مستقر.

## قانون پاسخ
جزئیات ساختگی ننویس. اگر در کاتالوگ یا این فایل نبود، بگو اطلاعات کافی نیست و به پشتیبانی ارجاع بده.
