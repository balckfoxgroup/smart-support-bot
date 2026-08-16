
<p align="center">
  <img src="docs/assets/logo.jpg" alt="Black Fox VPN Logo" width="96">
</p>

<h1 align="center">Smart Support Bot</h1>


<p align="center">
  <a href="https://foxnext.net">Website</a> •
  <a href="https://foxnext.net/downloads/Black-Fox-Config-Builder.apk">Black-Fox-Config-Builder.apk</a> •
  <a href="https://github.com/balckfoxgroup/blackfox-vpn-installer">Black Fox Vpn Installer</a> •
  <a href="https://github.com/balckfoxgroup/smart-support-bot">Smart Support Bot</a> •
  <a href="https://t.me/blackFoxVPNN">Telegram</a>
</p>

<div dir="rtl">


ربات 🤖 Smart Support Bot به‌ صورت رایگان و متن‌ باز (Open Source) در اختیار عموم قرار گرفته است تا همه بتوانند آزادانه از آن استفاده کنند و در توسعه و بهبود آن مشارکت داشته باشند.

⭐ اگر این پروژه برای شما مفید است، لطفاً با Star ⭐ در GitHub از ادامه این مسیر و توسعه پروژه حمایت کنید. حمایت شما انگیزه‌ای برای ادامه و ساخت پروژه‌های بهتر است.

🦊 همچنین خوشحالیم که به خانواده Black Fox پیوسته‌اید. ❤️
امیدواریم در کنار هم بتوانیم پروژه‌های کاربردی و متن‌باز بیشتری توسعه دهیم.

🚀 در کنار Smart Support Bot، می‌توانید از سایر پروژه‌های Black Fox نیز دیدن کنید و از آن‌ها استفاده کنید.

از همراهی و حمایت شما سپاسگزاریم. 🙏


Open-source multilingual **Telegram Smart Support Bot** from the Black Fox family.  
Build product catalogs, answer with product-scoped Ask AI, teach with screenshots, post news, and reconfigure the bot safely from chat.

⭐ If this project helps you, please **Star** the repository — it motivates more open tools.

---

<a id="english"></a>
## English

### Why Smart Support Bot?

Most Telegram bots are either dumb menus or fragile scripts. **Smart Support Bot** is a full support brain you can run on your own VPS:

- Speaks **4 languages**: Persian (`fa`), English (`en`), Russian (`ru`), Chinese (`zh`)
- Learns your products through **admin Products menu** + JSON catalogs + optional MD guides
- Answers with **Ask AI inside each product** (scoped retrieval — no cross-product leakage)
- Teaches features with a fixed copy pattern: **Design goal** + **Behavior**
- Attaches catalog screenshots only when the question is UI / howto related
- Lets admins change the bot by **chatting with it**
- Protects risky changes with **backup → confirm → auto-restore**

It is free, open source, and designed so anyone can self-host and extend it.

### Highlights (must-try features)

#### 1) Products menu (empty by default)
Fresh installs ship with **no pre-filled products**. In Settings open **Products** (`نام محصولات`):

- Add any number of products (name, emoji, short summary)
- Edit or delete products anytime
- Each product becomes a main-menu key and a `knowledge/product_catalogs/<id>.json` file
- Use **Build / Enrich Catalog** on a product: send photos/files, then build — vision helps when screenshots are the main material
- Each product keeps its own photo folder under `media/catalogs/<product_id>/`

Sample JSON lives under `knowledge/product_catalogs.examples/` (reference). Teaching-copy rules: `knowledge/CATALOG_FEATURE_COPY.md`.

#### 2) Ask AI (inside the product)
Ask AI is **not** a global main-menu dump. Users open a catalog first, then Ask AI:

- Session stores `product_id`
- Catalog RAG + product-prefixed MD guides + photos are filtered to that product
- Local **answer memory** (`data/answer_memory.json`) caches grounded replies (API-independent)
- Weak evidence → honest “not enough info” + handoff to human support (no invented facts)

#### 3) Feature teaching keys (Design goal / Behavior)
Product hubs can expose many educational buttons. Each reply follows:

```text
Design goal: …
Behavior: …
```

Short, educational, user-facing — prefer clear wording over internal file paths.

#### 4) Catalog screenshots (smart, not spam)
Ask AI sends related screenshots only when the question is educational / UI and the image is linked to a feature (`slot` / `topics` / `feature_ids`). Download-only questions usually stay text-only. Admins can index new photos from Products.

#### 5) Group & topics
In the community group the bot answers on mention or reply. Topics keep multilingual intros and education separated so private chats stay clean.

#### 6) News discovery & scheduled posts
Optional social/news job finds Iran/internet-related news from **up to 80 sources** and publishes to your channel on a schedule (default `10:00,17:00` Iran time).

Each post is AI-edited into a Telegram-ready format:

- Bold headline with 🚨  
- Short lead paragraph (not a copy of the title)  
- Key points with emojis (🔴 ⚖️ 📊 ⏳) — each point is a complete sentence  
- Source link + Black Fox footer  

#### 7) Nightly free config (optional)
Scheduled free-config delivery via 3X-UI panel API to the configured channel / destination (~21:00 Iran by default).

#### 8) Chat with Bot (admin) — change the bot from Telegram
In the admin settings menu open **Chat with Bot** (`گفتگو با ربات`):

- Reconfigure destinations, templates, owner info, and more in natural language / guided flow  
- Understand uploaded screenshots (vision) for UI/context requests  
- Ask AI to **create real admin buttons** with working code (safe-change watchdog)  
- No SSH required for day-to-day settings  

#### 9) Safe Change / auto-restore
For sensitive updates the independent watchdog:

1. Backs up the working bot  
2. Applies the change  
3. Observes health (~1 minute window)  
4. Asks for confirmation  
5. If confirmation is not approved in time → **automatic restore** to the last good state  

#### 10) More capabilities
- Multilingual menus (`/start`, `/menu`, `/lang`, `/help`) — language stored in `users.json`
- Owner Main Info (site, channel, group, support, bot name)
- Message targets: channel / group / user account / test (up to 3 slots each)
- Conversation analysis drafts for catalog gaps
- Bot statistics + **named user list** for admins
- Contact Creator card (locked open-source credits)

### Languages

| Code | Language |
|------|----------|
| `fa` | فارسی |
| `en` | English |
| `ru` | Русский |
| `zh` | 中文 |

Language is detected from Telegram and can be changed with `/lang`.

### Requirements

- Ubuntu/Debian VPS (root or sudo)
- Python 3.10+
- Telegram bot token (BotFather)
- OpenAI-compatible AI API key
- Your Telegram numeric user id as admin

### Quick install (Linux)

```bash
git clone https://github.com/balckfoxgroup/smart-support-bot.git
cd smart-support-bot
cp .env.example .env
nano .env   # set TELEGRAM_BOT_TOKEN, AI_API_KEY, BOT_ADMIN_IDS
sudo bash deploy/install.sh
```

Install path: `/opt/smart-support-bot`  
Services: `smart-support-bot.service` + `smart-support-bot-watchdog.service`

```bash
systemctl status smart-support-bot.service
journalctl -u smart-support-bot.service -f
```

### After install

1. Open your bot in Telegram  
2. Send `/start` and pick a language  
3. As admin, open settings → **Products** and add your products  
4. Enrich catalogs (JSON / photos / MD guides)  
5. Fill Main Info and message destinations  
6. Invite the bot to your group/channel and grant admin if you post there  

### Project layout

```
smart-support-bot/
├── src/                 # bot runtime (aiogram 3)
├── knowledge/           # FAQ, intents, catalogs, guides, copy rules
├── media/catalogs/      # per-product teaching screenshots
├── deploy/install.sh    # one-shot Linux installer
├── .env.example
└── README.md
```

### Security notes

- Never commit `.env`
- Keep `BOT_ADMIN_IDS` limited to trusted operators
- Watchdog restore protects you from bad admin changes — still review confirms carefully
- Prefer demo/redacted screenshots in public catalogs when possible

### License / family

Part of the **Black Fox** family.  
More projects: https://github.com/balckfoxgroup?tab=repositories

---

<a id="فارسی"></a>
## فارسی

### چرا Smart Support Bot؟

خیلی از ربات‌های تلگرام فقط منوی خشک یا اسکریپت شکننده‌اند. **ربات Smart Support Bot** یک مغز پشتیبانی است که روی سرور خودت اجرا می‌شود:

- پشتیبانی از **۴ زبان**: فارسی، انگلیسی، روسی، چینی
- ساخت و مدیریت **محصولات** با کاتالوگ JSON و راهنمای MD و عکس
- پاسخ با **سوال از AI داخل هر محصول** (جداسازی دانش — بدون نشت بین محصولات)
- آموزش فیچرها با ساختار ثابت: **هدف طراحی** + **عملکرد**
- ارسال اسکرین فقط وقتی سؤال آموزشی یا مرتبط با UI باشد
- تغییر تنظیمات از داخل تلگرام با **گفتگو با ربات**
- محافظت از تغییرات حساس با **بکاپ ← تأیید ← بازگردانی خودکار**

کاملاً رایگان و متن‌باز است تا همه بتوانند نصب کنند و توسعه بدهند.

### قابلیت‌های مهم (حتماً امتحان کنید)

#### ۱) منوی محصولات (پیش‌فرض خالی)
نصب تازه **بدون محصول ازپیش‌تعریف‌شده** است. در تنظیمات گزینه **نام محصولات** را باز کنید:

- هر تعداد محصول اضافه کنید (نام، ایموجی، خلاصه کوتاه)
- هر وقت بخواهید ویرایش یا حذف کنید
- هر محصول یک کلید در منوی اصلی و یک فایل `knowledge/product_catalogs/<id>.json` می‌شود
- با **ساخت/تکمیل کاتالوگ** روی همان محصول، عکس و فایل بفرستید
- هر محصول پوشه عکس جدا در `media/catalogs/<product_id>/` دارد

نمونه JSON در `knowledge/product_catalogs.examples/` است. قانون نگارش کلیدهای آموزشی: `knowledge/CATALOG_FEATURE_COPY.md`.

#### ۲) سوال از AI (داخل محصول)
Ask AI روی منوی اصلی باز نیست. کاربر اول کاتالوگ را باز می‌کند، بعد سوال از AI:

- شناسه محصول در نشست ذخیره می‌شود
- RAG کاتالوگ و MD با پیشوند همان محصول و عکس‌ها فیلتر می‌شوند
- **حافظه پاسخ محلی** (`data/answer_memory.json`) جواب‌های grounded را نگه می‌دارد (وابسته به یک API خاص نیست)
- اگر مدرک کافی نباشد، حدس نمی‌زند و به پشتیبانی انسانی ارجاع می‌دهد

#### ۳) کلیدهای آموزشی (هدف طراحی / عملکرد)
داخل هاب هر محصول می‌توانید کلیدهای آموزشی زیاد بگذارید. هر پاسخ این ساختار را دارد:

```text
هدف طراحی: …
عملکرد: …
```

کوتاه، آموزشی و کاربرمحور — مسیر فایل داخلی را بی‌دلیل نشان ندهید.

#### ۴) عکس آموزشی کاتالوگ (بدون اسپم)
Ask AI فقط وقتی سؤال آموزشی یا مرتبط با UI باشد و اسکرین به فیچر وصل باشد عکس می‌فرستد. سؤال‌هایی مثل «از کجا دانلود کنم» معمولاً بدون عکس جواب داده می‌شوند. ادمین از Products می‌تواند عکس جدید ایندکس کند.

#### ۵) گروه و تاپیک‌ها
در گروه، وقتی ربات منشن یا ریپلای شود جواب می‌دهد. تاپیک‌ها برای معرفی و آموزش چندزبانه استفاده می‌شوند تا چت خصوصی همه کاربران شلوغ نشود.

#### ۶) جستجو و انتشار خبر
جاب اختیاری خبر، اخبار مرتبط را از **تا ۸۰ منبع** پیدا می‌کند و طبق زمان‌بندی (پیش‌فرض `10:00` و `17:00` به وقت ایران) در کانال منتشر می‌کند.

هر پست با AI به قالب تلگرامی ادیت می‌شود:

- تیتر بولد با 🚨  
- لید کوتاه (تکرار عین تیتر نیست)  
- نکات کلیدی با ایموجی (🔴 ⚖️ 📊 ⏳) — هر نکته جملهٔ کامل  
- لینک منبع + برند Black Fox  

#### ۷) کانفیگ شبانه (اختیاری)
ارسال زمان‌بندی‌شده کانفیگ رایگان از API پنل 3X-UI به مقصد تنظیم‌شده (پیش‌فرض حدود ۲۱:۰۰ ایران).

#### ۸) گفتگو با ربات — تغییر ربات از خود تلگرام
در منوی تنظیمات ادمین، گزینه **گفتگو با ربات** را باز کنید:

- مقصد پیام‌ها، قالب‌ها، اطلاعات اصلی و بیشتر را از همان‌جا تغییر دهید  
- عکس/اسکرین‌شات ارسالی را می‌فهمد (vision)  
- می‌توانید بخواهید **کلید ادمین واقعی با کد** بسازد (safe-change)  
- برای کارهای روزمره نیازی به SSH نیست  

#### ۹) تغییر امن و Restore خودکار
برای تغییرات حساس، نگهبان مستقل این کار را می‌کند:

1. از ربات سالم بکاپ می‌گیرد  
2. تغییر را اعمال می‌کند  
3. حدود یک دقیقه سلامت را چک می‌کند  
4. پیام تأیید می‌فرستد  
5. اگر تأیید نشود → **ربات به‌صورت خودکار به حالت قبلی Restore می‌شود**

#### ۱۰) بقیه امکانات
- منوی چندزبانه (`/start` ، `/menu` ، `/lang` ، `/help`) — زبان در `users.json` ذخیره می‌شود
- اطلاعات اصلی مالک (سایت، کانال، گروه، پشتیبانی، نام ربات)
- مقصد پیام: کانال / گروه / اکانت کاربر / تست (هرکدام تا ۳ اسلات)
- تحلیل مکالمات برای پیدا کردن شکاف کاتالوگ
- آمار ربات و **لیست کاربران با نام** برای ادمین
- کارت تماس با سازنده (متن‌باز)

### زبان‌ها

| کد | زبان |
|----|------|
| `fa` | فارسی |
| `en` | English |
| `ru` | Русский |
| `zh` | 中文 |

زبان از تلگرام تشخیص داده می‌شود و با `/lang` عوض می‌شود.

### پیش‌نیاز

- سرور Ubuntu/Debian
- Python 3.10 به بالا
- توکن ربات از BotFather
- کلید API سازگار با OpenAI
- آیدی عددی تلگرام شما به‌عنوان ادمین

### نصب سریع لینوکس

```bash
git clone https://github.com/balckfoxgroup/smart-support-bot.git
cd smart-support-bot
cp .env.example .env
nano .env   # مقدار TELEGRAM_BOT_TOKEN و AI_API_KEY و BOT_ADMIN_IDS
sudo bash deploy/install.sh
```

مسیر نصب: `/opt/smart-support-bot`  
سرویس‌ها: `smart-support-bot.service` و `smart-support-bot-watchdog.service`

```bash
systemctl status smart-support-bot.service
journalctl -u smart-support-bot.service -f
```

### بعد از نصب

1. ربات را در تلگرام باز کنید  
2. دستور `/start` را بفرستید و زبان را انتخاب کنید  
3. با اکانت ادمین وارد تنظیمات شوید → **نام محصولات** و محصول‌ها را بسازید  
4. کاتالوگ را با JSON / عکس / راهنمای MD غنی کنید  
5. اطلاعات اصلی و مقصد پیام‌ها را کامل کنید  
6. ربات را به گروه/کانال اضافه کنید و در صورت نیاز ادمین بدهید  

### امنیت

- فایل `.env` را عمومی نکنید  
- فقط ادمین‌های مطمئن را در `BOT_ADMIN_IDS` بگذارید  
- Restore خودکار جلوی خراب‌کاری را می‌گیرد؛ باز هم پیام تأیید را جدی بگیرید  
- برای کاتالوگ عمومی تا جای ممکن از اسکرین با IP واقعی پرهیز کنید  

### خانواده Black Fox

این پروژه عضو خانواده **Black Fox** است.  
پروژه‌های بیشتر: https://github.com/balckfoxgroup?tab=repositories

از همراهی و Star شما سپاسگزاریم.


### Settings Backup / Health / Admin Roles / News

- Export/Import settings JSON from admin Settings  
- Daily health report + manual Health Status  
- Extra admins: `full` (settings) or `stats` (stats/health only)  
- Channel news: editorial AI posts, up to 80 sources, schedule `10:00,17:00` (Iran), catch-up after restart  
