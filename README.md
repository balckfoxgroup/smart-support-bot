# Smart Support Bot

[English](#english) · [فارسی](#فارسی)

Open-source multilingual **Telegram AI support bot** from the Black Fox family.  
Build product catalogs, answer with Ask AI, search knowledge, post news, and reconfigure the bot safely from chat.

⭐ If this project helps you, please **Star** the repository — it motivates more open tools.

---

<a id="english"></a>
## English

### Why Smart Support Bot?

Most Telegram bots are either dumb menus or fragile scripts. **Smart Support Bot** is a full support brain you can run on your own VPS:

- Speaks **4 languages**: Persian (`fa`), English (`en`), Russian (`ru`), Chinese (`zh`)
- Learns your products through **admin Products menu** + optional AI catalogs
- Answers with **Ask AI** + local knowledge + intent matching
- Lets admins change the bot by **chatting with it**
- Protects risky changes with **backup → confirm → auto-restore**

It is free, open source, and designed so anyone can self-host and extend it.

### Highlights (must-try features)

#### 1) Products menu (empty by default)
Fresh installs ship with **no pre-filled products**. In Settings open **Products** (`نام محصولات`):

- Add any number of products (name, emoji, short summary)
- Edit or delete products anytime
- Each product becomes a main-menu key and a `knowledge/product_catalogs/<id>.json` file
- Use **Build / Enrich Catalog** on a product to attach richer content and photos

Sample JSON lives only under `knowledge/product_catalogs.examples/` (not loaded into the menu).

#### 2) Ask AI everywhere
Private chats, group replies, and menu flows all use the same AI stack:

- Intent matching from multilingual databases
- Knowledge-base retrieval (FAQ + guides)
- Catalog-aware answers
- Fallback to your support account when unsure

#### 3) Search + knowledge
Users and admins benefit from search over knowledge and catalogs. The bot prefers grounded answers over hallucinations.

#### 4) News discovery & scheduled posts
Optional social/news job finds relevant internet news and can publish short posts to your channel/account on a schedule.

#### 5) Chat with Bot (admin) — change the bot from Telegram
In the admin settings menu open **Chat with Bot** (`گفتگو با ربات`):

- Reconfigure destinations, templates, owner info, and more in natural language / guided flow
- No SSH required for day-to-day settings
- Agent control plane can also chat with AI providers for model/API changes

#### 6) Safe Change / auto-restore
For sensitive updates the independent watchdog:

1. Backs up the working bot  
2. Applies the change  
3. Observes health (~1 minute window)  
4. Asks for confirmation  
5. If confirmation is not approved in time → **automatic restore** to the last good state  

This keeps experiments safe.

#### 7) More capabilities
- Multilingual menus (`/start`, `/menu`, `/lang`, `/help`)
- Owner Main Info (site, channel, group, support, bot name)
- Message targets: channel / group / user account / test (up to 3 slots each)
- Nightly free-config delivery via 3X-UI panel API (optional)
- Conversation analysis drafts for support quality
- Bot statistics for admins
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
2. Send `/start`  
3. As admin, open settings → **Products** (`نام محصولات`) and add your products  
4. Optionally enrich catalogs via folder/upload wizard  
5. Fill Main Info, message destinations  
6. Invite the bot to your group/channel and grant admin if you post there  

### Project layout

```
smart-support-bot/
├── src/                 # bot runtime (aiogram 3)
├── knowledge/           # FAQ, intents, catalogs, decision trees
├── deploy/install.sh    # one-shot Linux installer
├── .env.example
└── README.md
```

### Security notes

- Never commit `.env`
- Keep `BOT_ADMIN_IDS` limited to trusted operators
- Watchdog restore protects you from bad admin changes — still review confirms carefully

### License / family

Part of the **Black Fox**  family.  
More projects: https://github.com/balckfoxgroup?tab=repositories

---

<a id="فارسی"></a>
## فارسی

### چرا Smart Support Bot؟

خیلی از ربات‌های تلگرام فقط منوی خشک یا اسکریپت شکننده‌اند. **ربات Smart Support Bot** یک مغز پشتیبانی است که روی سرور خودت اجرا می‌شود:

- پشتیبانی از **۴ زبان**: فارسی، انگلیسی، روسی، چینی
- ساخت و مدیریت **محصولات** از تنظیمات (نصب تازه خالی است)
- پاسخ‌گویی با **سوال از AI** + دانش محلی + تشخیص نیت
- امکان تغییر تنظیمات از داخل خود تلگرام با **گفتگو با ربات**
- محافظت از تغییرات حساس با **بکاپ ← تأیید ← بازگردانی خودکار**

کاملاً رایگان و متن‌باز است تا همه بتوانند نصب کنند و توسعه بدهند.

### قابلیت‌های مهم (حتماً امتحان کنید)

#### ۱) منوی محصولات (پیش‌فرض خالی)
نصب تازه **بدون محصول ازپیش‌تعریف‌شده** است. در تنظیمات گزینه **نام محصولات** را باز کنید:

- هر تعداد محصول اضافه کنید (نام، ایموجی، خلاصه کوتاه)
- هر وقت بخواهید ویرایش یا حذف کنید
- هر محصول یک کلید در منوی اصلی و یک فایل `knowledge/product_catalogs/<id>.json` می‌شود
- با **ساخت/تکمیل کاتالوگ** (یا ویزارد پوشه) محتوا و عکس غنی‌تر وصل کنید

نمونهٔ JSON فقط در `knowledge/product_catalogs.examples/` است و وارد منو نمی‌شود.

#### ۲) استفاده از AI در تمام قسمت‌ها
چت خصوصی، پاسخ گروهی و مسیر منو همگی از یک موتور AI استفاده می‌کنند:

- تشخیص نیت چندزبانه
- بازیابی از پایگاه دانش (FAQ و راهنما)
- پاسخ آگاه از کاتالوگ
- ارجاع به اکانت پشتیبانی وقتی مطمئن نیست

#### ۳) جستجو در دانش و کاتالوگ
جستجو روی دانش و کاتالوگ کمک می‌کند جواب‌ها واقعی و مفید باشند، نه حدس بی‌پایه.

#### ۴) جستجو و انتشار خبر
جاب اختیاری خبر، اخبار مرتبط را پیدا می‌کند و می‌تواند در زمان‌بندی مشخص برای کانال/اکانت شما پست کوتاه بسازد.

#### ۵) گفتگو با ربات — تغییر ربات از خود تلگرام
در منوی تنظیمات ادمین، گزینه **گفتگو با ربات** را باز کنید:

- مقصد پیام‌ها، قالب‌ها، اطلاعات اصلی و بیشتر را از همان‌جا تغییر دهید
- برای کارهای روزمره نیازی به SSH نیست
- برای تعویض مدل/API هم گفتگو با ایجنت در کنترل‌پنل ادمین هست

#### ۶) تغییر امن و Restore خودکار
برای تغییرات حساس، نگهبان مستقل این کار را می‌کند:

1. از ربات سالم بکاپ می‌گیرد  
2. تغییر را اعمال می‌کند  
3. حدود یک دقیقه سلامت را چک می‌کند  
4. پیام تأیید می‌فرستد  
5. اگر تأیید نشود → **ربات به‌صورت خودکار به حالت قبلی Restore می‌شود**

پس آزمایش کردن تنظیمات، کم‌خطرتر است.

#### ۷) بقیه امکانات
- منوی چندزبانه (`/start` ، `/menu` ، `/lang` ، `/help`)
- اطلاعات اصلی مالک (سایت، کانال، گروه، پشتیبانی، نام ربات)
- مقصد پیام: کانال / گروه / اکانت کاربر / تست (هرکدام تا ۳ اسلات)
- ارسال کانفیگ رایگان شبانه از طریق API پنل 3X-UI (اختیاری)
- تحلیل مکالمات برای بهبود پشتیبانی
- آمار ربات برای ادمین
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
2. دستور `/start` را بفرستید  
3. با اکانت ادمین وارد تنظیمات شوید → **نام محصولات** و محصول‌های خود را بسازید  
4. در صورت نیاز کاتالوگ را با ویزارد پوشه/آپلود غنی کنید  
5. اطلاعات اصلی و مقصد پیام‌ها را کامل کنید  
6. ربات را به گروه/کانال اضافه کنید و در صورت نیاز ادمین بدهید  

### امنیت

- فایل `.env` را عمومی نکنید  
- فقط ادمین‌های مطمئن را در `BOT_ADMIN_IDS` بگذارید  
- Restore خودکار جلوی خراب‌کاری را می‌گیرد؛ باز هم پیام تأیید را جدی بگیرید  

### خانواده Black Fox

این پروژه عضو خانواده **Black Fox** است.  
پروژه‌های بیشتر: https://github.com/balckfoxgroup?tab=repositories

از همراهی و Star شما سپاسگزاریم.


### Settings Backup / Health / Admin Roles

- Export/Import settings JSON from admin Settings
- Daily health report + manual Health Status
- Extra admins: `full` (settings) or `stats` (stats/health only)
