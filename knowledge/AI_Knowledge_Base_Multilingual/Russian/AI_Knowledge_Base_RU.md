# Black Fox VPN — база знаний ИИ (русский)

> Для AI Assistant, Telegram Bot и поддержки.  
> Не выдумывайте версии, цены и хостеров. VPS только через **FoxNext.net → Partners**. Неизвестное: `NEED_MORE_REVIEW`.  
> UI-подписи оставляйте на английском Title Case: Full Deploy, Connect SSH, Registration.

---

## 1. Введение

**Black Fox Vpn** — операционный **Installer** для Windows (есть Android-компаньон). Через **SSH** ставит **WireGuard** и панель **3X-UI (Sanaei)** на ваш Linux VPS и помогает собрать multi-location VPN.

Это **не** потребительский VPN-клиент «подключись и серфи».

Сайт/хабы: `foxnext.net`, `blackfoxupdate.ir` · поддержка: Contact / `@HiBlackFoxVpn`

---

## 2. Архитектура

```
UI → общее локальное хранилище (Basic/Pro/AI Pro)
   → SSH + скрипты + Panel API
   → хабы: blackfoxupdate.ir → foxnext.net
Сеть: Direct, затем Program Proxy
```

Роли: Central · Exit (макс. 6) · Tunnel · Node (макс. 6) · Mesh  
**Configure Panel ≠ установка панели на Central** (для Central — Full Deploy).

---

## 3. Режимы и License

`basic` | `pro` | `ai_pro`

- Basic без License: только Setup Central, Connect SSH, Full Deploy  
- Pro: tunnels, nodes, Domain, CDN, Mesh, Mirza, Move Central…  
- AI Pro: те же операции через чат; **отдельно от Pro**; нужен quota  

Коды: BFXB / BFXP / BFXA / BFXQ · claim с `-CLM-`  
В Basic центральный сервер обычно IR/CN/RU.

---

## 4. Возможности

Setup Central · Connect SSH · Full Deploy · Exit · Tunnel · Node · Configure Panel · Domain/DNS · CDN · Mesh · Telegram Bot (Mirza) · Move Central · Proxy · Panel Login Info · Test Client · Registration · Check System · Deletes/Reset · AI Tasks

Источники 3X-UI: Sanaei GitHub / BlackFox Hub / Local PC  
Типы линков: WireGuard · GRE · Reverse Tunnel (Stealth-WSS)

---

## 5. Вкладки

Operations · Check System · View · Settings · Registration · Contact  
Оверлеи: Add Domain, Mesh Servers

---

## 6. Для начинающих

Установка с foxnext.net → язык → BASIC → Setup → Connect SSH → Full Deploy → Panel Login Info → License перед Exit.

---

## 7. Для профессионалов

Порядок Pro: Tunnel → Exit → Configure Panel → Node → Domain → CDN → Mesh → Bot.  
AI Pro: BFXA + quota; подтверждайте действия; Check System ≠ Diagnose & Repair.

---

## 8–9. Проблемы и ошибки

Need activate → Registration  
AI locked → AI Pro + quota  
SSH fail → credentials + Proxy  
Full Deploy fail → другой source + terminal  
Configure Panel fail → сначала Exit/Node  

Эскалация: `@HiBlackFoxVpn` + Device ID + скриншот

---

## 10. Связи разделов

Общий store между режимами · успех Full Deploy открывает Panel Login Info · удаление tunnel hop влияет на цепочку · Pro не открывает AI.

---

## Правила AI

Только продукт Black Fox · язык пользователя · не обсуждать версии · VPS только Partners · подтверждение перед опасными действиями · имя: BlackFox AI
