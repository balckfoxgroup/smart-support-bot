<p align="center">
  <img src="docs/assets/logo.jpg" alt="Black Fox VPN Logo" width="96">
</p>

<h1 align="center">Smart Support Bot</h1>

<p align="center">
  <strong>Telegram product support for Black Fox VPN Installer</strong><br>
  Features · Languages · Catalog · Setup · Deploy · Safety
</p>

<p align="center">
  <a href="https://foxnext.net">Website</a> •
  <a href="https://foxnext.net/downloads/Black-Fox-Config-Builder.apk">Black-Fox-Config-Builder.apk</a> •
  <a href="https://github.com/balckfoxgroup/blackfox-vpn-installer">Black Fox Vpn Installer</a> •
  <a href="https://github.com/balckfoxgroup/blackfox-config-builder">Black Fox Config Builder</a> •
  <a href="https://t.me/blackFoxVPNN">Telegram</a>
</p>

<div dir="rtl">

ربات **Smart Support Bot** به‌صورت رایگان و متن‌باز (**Open Source**) در اختیار عموم قرار گرفته است تا همه بتوانند آزادانه از آن استفاده کنند و در توسعه و بهبود آن مشارکت داشته باشند.

⭐ اگر این پروژه برای شما مفید است، لطفاً با **Star ⭐ در GitHub** از ادامه این مسیر و توسعه پروژه حمایت کنید. حمایت شما انگیزه‌ای برای ادامه و ساخت پروژه‌های بهتر است.

🦊 همچنین خوشحالیم که به خانواده **Black Fox** پیوسته‌اید. 💖
امیدواریم در کنار هم بتوانیم پروژه‌های کاربردی و متن‌باز بیشتری توسعه دهیم.

🚀 در کنار Smart Support Bot، می‌توانید از سایر پروژه‌های **Black Fox** نیز دیدن کنید و از آن‌ها استفاده کنید.

**از همراهی و حمایت شما سپاسگزاریم. 🙏**

</div>

---

Async Telegram support bot for **Black Fox VPN Installer** (ops toolkit).
Long polling · aiogram 3 · OpenAI-compatible chat API · local multilingual knowledge.

Not an image/video/codegen bot.

> This is the clean open-source release: no recorded data, no secrets.
> Only the **Contact Creator** card (`knowledge/creator_contact.json`) ships pre-filled.

## Features

- Languages: `fa`, `en`, `ru`, `zh` (Telegram `language_code` + `/lang`)
- Intent match from `AI_BOT_DATABASE` (keyword / sample overlap)
- Low confidence → clarifying question from intent DB
- High confidence / after clarify → LLM with FAQ + KB snippets
- Per-product catalog folders, training notes, and product-scoped operator chat
- Sales nudge (FOMO, no fake prices) → https://foxnext.net · @HiBlackFoxVpn
- User language prefs in `data/users.json` (created on first run)
- **Safe-change watchdog**: backup → apply → healthcheck → 60s admin confirm → keep or auto-restore
  (`/safety_drill`, `/safety_status`; unit `smart-support-bot-watchdog.service`)

## Layout

```
smart-support-bot/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── ai/client.py
│   ├── ai/persona.py
│   ├── knowledge/loader.py
│   ├── knowledge/intents.py
│   ├── handlers/start.py
│   ├── handlers/chat.py
│   └── storage/users.py
├── knowledge/
│   ├── AI_Knowledge_Base_Multilingual/
│   ├── AI_BOT_DATABASE/
│   ├── Support_Decision_Tree/
│   ├── creator_contact.json      # Contact Creator card (pre-filled)
│   ├── social_news_sources.json
│   ├── product_catalogs/
│   └── product_guides/
├── data/.gitkeep                 # runtime files created here on first run
├── media/                        # menu images + catalog images
├── docs/assets/logo.jpg
├── deploy/smart-support-bot.service
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

Windows (PowerShell):

```powershell
cd smart-support-bot
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
# Edit .env: TELEGRAM_BOT_TOKEN, AI_API_KEY, BOT_ADMIN_IDS (your Telegram user id)
python -m src.main
```

Linux:

```bash
cd "/opt/Smart Support Bot"
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env
python -m src.main
```

> **`BOT_ADMIN_IDS` is required** to access the admin/Statistics menus.
> Until you set it, admin-only buttons are simply inaccessible.
> Find your numeric Telegram user id via a bot like `@userinfobot`.

## Environment

| Variable | Required | Default | Notes |
|----------|----------|---------|-------|
| `TELEGRAM_BOT_TOKEN` | yes | — | from @BotFather |
| `AI_API_KEY` | yes | — | OpenAI-compatible key |
| `AI_BASE_URL` | no | `https://ai.nube.sh/api/v1` | |
| `AI_MODEL` | no | `kimi-k2.5` | |
| `AI_TIMEOUT_SECONDS` | no | `60` | |
| `AI_MAX_TOKENS` | no | `4096` | |
| `AI_TEMPERATURE` | no | `0.4` | |
| `INTENT_CONFIDENCE_THRESHOLD` | no | `0.28` | |
| `KNOWLEDGE_SNIPPET_CHARS` | no | `12000` | |
| `LOG_LEVEL` | no | `INFO` | |
| `BOT_ADMIN_IDS` | recommended | — | comma-separated numeric ids; admin menus |
| `AI_BUDGET_USD` | no | `50` | |
| `AI_USD_PER_MILLION_TOKENS` | no | `2.0` | |
| `NIGHTLY_ENABLED` | no | `false` | free config to channel |
| `NIGHTLY_IRAN_TIME` | no | `21:00` | |
| `NIGHTLY_SUPPORT_CHAT_ID` | no | `@HiBlackFoxVpn` | |
| `PANEL_BASE_URL` | when nightly enabled | — | 3x-ui panel |
| `PANEL_API_TOKEN` | when nightly enabled | — | 3x-ui API token |
| `PANEL_INBOUND_ID` | when nightly enabled | `0` | |
| `PANEL_REQUIRED_PORT` | no | `443` | |
| `SOCIAL_NEWS_ENABLED` | no | `true` | verified Iran internet news |
| `SOCIAL_NEWS_CHAT_ID` | no | `@blackFoxVPNN` | |
| `SOCIAL_NEWS_TIMES` | no | `10:00,17:00` | |
| `CONVO_ANALYSIS_ENABLED` | no | `false` | private-chat → drafts |
| `CONVO_ANALYSIS_TIMES` | no | `12:30` | |
| `CONVO_ANALYSIS_CHAT_ID` | when convo enabled | — | numeric id |
| `CONVO_ANALYSIS_TEST_MODE` | no | `true` | |
| `SAFETY_CONFIRM_CHAT_ID` | for safety drills | — | numeric id; confirm prompts |
| `NEWS_REPORT_ADMIN_IDS` | no | — | extra ids for Stats → Report |

Social news: up to **80 sources** (`knowledge/social_news_sources.json`), AI editorial caption (headline + lead + emoji key points), catch-up after restart.

## systemd

```bash
sudo cp deploy/smart-support-bot.service /etc/systemd/system/
sudo cp deploy/smart-support-bot-watchdog.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now smart-support-bot
sudo systemctl enable --now smart-support-bot-watchdog
```

Or use the bundled installer:

```bash
sudo bash deploy/install.sh
```

## Commands

- `/start` — greeting
- `/help` — short help
- `/lang fa|en|ru|zh` — persist language
- `/safety_drill`, `/safety_status` — admin only (safe-change watchdog)

## Safety / product rules

- No invented versions or prices
- VPS only via FoxNext Partners on foxnext.net
- License sales: scarcity framing without fake numbers; link site + @HiBlackFoxVpn

## License & credit

Released free and open source. If it helps you, ⭐ the repo.
🦊 Built by **Black Fox** — https://foxnext.net · @HiBlackFoxVpn
