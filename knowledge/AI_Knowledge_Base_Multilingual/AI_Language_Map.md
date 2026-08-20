# AI Language Map — Black Fox Multilingual Knowledge Brain

> Use this map to route Telegram Bot / AI Assistant retrieval by user language.  
> Canonical product facts: `/Documentation` (English analysis source).  
> Multilingual packs: `/AI_Knowledge_Base_Multilingual`.

---

## 1. Language folders

| Language | Code | Folder | Primary RAG file |
|----------|------|--------|------------------|
| English | `en` | `AI_Knowledge_Base_Multilingual/English/` | `AI_Knowledge_Base_EN.md` |
| Persian (Farsi) | `fa` | `AI_Knowledge_Base_Multilingual/Persian/` | `AI_Knowledge_Base_FA.md` |
| Russian | `ru` | `AI_Knowledge_Base_Multilingual/Russian/` | `AI_Knowledge_Base_RU.md` |
| Simplified Chinese | `zh` / `zh-CN` | `AI_Knowledge_Base_Multilingual/Chinese/` | `AI_Knowledge_Base_ZH.md` |

**Routing rule:** Detect user language → load that folder first → fall back to English only if a topic is marked `NEED_MORE_REVIEW` in the target language.

---

## 2. File roles (same in every language)

| Topic | English | Persian | Russian | Chinese |
|-------|---------|---------|---------|---------|
| Full AI brain (architecture, modes, gates, relationships, AI rules) | `English/AI_Knowledge_Base_EN.md` | `Persian/AI_Knowledge_Base_FA.md` | `Russian/AI_Knowledge_Base_RU.md` | `Chinese/AI_Knowledge_Base_ZH.md` |
| Install + usage + beginner/advanced + problems | `English/User_Guide_EN.md` | `Persian/User_Guide_FA.md` | `Russian/User_Guide_RU.md` | `Chinese/User_Guide_ZH.md` |
| FAQ Q001–Q200 (ID-aligned across languages) | `English/FAQ_EN.md` | `Persian/FAQ_FA.md` | `Russian/FAQ_RU.md` | `Chinese/FAQ_ZH.md` |

---

## 3. Topic → where to look

| User intent examples | Prefer file | FAQ IDs (shared) |
|----------------------|-------------|------------------|
| What is Black Fox? / platforms / download | KB §intro + User Guide §1–3 | Q001–Q004 |
| Modes Basic / Pro / AI Pro | KB §modes + User Guide §6–7 | Q007–Q011, Q103–Q104, Q187 |
| Activate license / Device ID / claim / TX | User Guide + FAQ | Q031–Q050, Q101–Q102, Q188–Q191 |
| Full Deploy / SSH / Panel Login | User Guide §4 + FAQ | Q015–Q019, Q052–Q055, Q086–Q090 |
| Configure Panel vs Full Deploy | KB + FAQ | Q020, Q162 |
| Exit / Tunnel / Node | KB features + FAQ | Q022–Q025, Q107–Q110, Q163 |
| Domain / CDN / DNS | FAQ + Advanced section | Q026–Q028, Q093–Q095, Q171–Q172 |
| Mesh / GRE / Stealth-WSS / Link Test | KB + FAQ | Q057–Q062, Q141–Q142, Q173, Q178 |
| Proxy | FAQ | Q029–Q030, Q168 |
| AI chat / quota / MCP / tasks | KB AI rules + FAQ | Q078–Q084, Q119–Q120, Q153–Q155, Q176–Q179 |
| Deletes / Reset / Factory Reset | User Guide problems + FAQ | Q067–Q072, Q139–Q140, Q165–Q167, Q180 |
| Updates / force update | FAQ | Q073–Q074, Q135, Q183 |
| Support contacts / VPS Partners | KB + FAQ | Q040 (VPS), Q076–Q077, Q132–Q133, Q192–Q194 |
| Screenshots / teaching assets | `Screenshots/README.md` | Q198 |
| Stuck deploy playbook | FAQ + Troubleshooting | Q159, Q199 |

---

## 4. Cross-language FAQ alignment

- Every language FAQ uses the **same IDs** `Q001`…`Q200`.
- Same product facts: max **6** exits/nodes; free Basic = Setup Central + Connect SSH + Full Deploy; **Pro ≠ AI Pro**; tabs = Operations, Check System, View, Settings, Registration, Contact.
- Technical UI labels stay English Title Case in all languages.
- If a localized answer wraps English factual core, the **Question** is fully localized for retrieval (“Как активировать лицензию?”, “如何安装程序؟”, «چگونه License را فعال کنم؟»).

---

## 5. Bot / AI retrieval recipe

1. Detect language (`fa` / `en` / `ru` / `zh`).
2. Search `FAQ_XX.md` by question similarity (native phrasing).
3. If procedural → also pull `User_Guide_XX.md` matching section.
4. If architectural / gating / relationships → `AI_Knowledge_Base_XX.md`.
5. Never invent versions, prices, or VPS brands; VPS only **FoxNext.net → Partners**.
6. Screenshots: `/Screenshots` (language-agnostic assets; captions via this map).

---

## 6. Related English-only deep docs

Still useful as engineer fallback (not required for end-user bot replies):

- `Documentation/Troubleshooting.md`
- `Documentation/Feature_List.md`
- `Documentation/Change_Log.md`
- `Documentation/Product_Overview.md`

---

## 7. Maintenance notes

| Item | Status |
|------|--------|
| EN FAQ format Question/Answer/Steps/Errors | Done (200) |
| FA/RU/ZH questions ID-aligned | Done (200) |
| FAQ answers Q041–Q200 fully localized (FA/RU/ZH) | Done via `_ans_*.py` + `_rebuild_native_faq.py` |
| FAQ answers Q001–Q040 | Partially seeded; some still hybrid EN+wrapper — optional follow-up |
| Live GUI screenshots for every dialog | `NEED_MORE_REVIEW` — see `Screenshots/README.md` |
| Generator script | `AI_Knowledge_Base_Multilingual/_gen_faq_i18n.py` |

When product facts change: update `Documentation/` first, then regenerate `FAQ_EN.md` and re-run `_gen_faq_i18n.py` (and refresh native ANS seeds).
