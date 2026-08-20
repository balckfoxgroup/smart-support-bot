# AI_BOT_DATABASE — Developer Guide

Structured conversational brain for **Black Fox VPN** Telegram Bot and AI Assistant.

## What’s inside

```
AI_BOT_DATABASE/
├── README.md                          ← this file
├── all_languages_database.json        ← unified DB (all langs flattened)
├── intents_master_multilingual.json   ← nested FA/EN/RU/ZH (editing source)
├── intents/
│   ├── intents_fa.json
│   ├── intents_en.json
│   ├── intents_ru.json
│   └── intents_zh.json
├── _part1_intents.py / _part2_intents.py / _part3_build.py  ← generators
```

Companion markdown (RAG / long answers):

- `AI_Knowledge_Base_Multilingual/`
- `Documentation/`
- `AI_Language_Map.md`

---

## Record schema (per language row)

| Field | Meaning |
|-------|---------|
| `id` | Unique row id: `{intent}_{lang}` |
| `intent` | Machine name, stable across languages (e.g. `activate_license`) |
| `category` | Product area: License, Deploy, Errors, Modes, … |
| `language` | `fa` \| `en` \| `ru` \| `zh` |
| `keywords` | Tokens for keyword / BM25 matching |
| `sample_questions` | ≥20 realistic user phrasings (beginner, pro, short, colloquial, typos-ish) |
| `short_answer` | **Level 1** — fast reply |
| `full_answer` | **Level 2** — complete support answer |
| `steps` | Ordered actions |
| `possible_errors` | Symptoms / dialog titles |
| `solutions` | Fix bullets |
| `related_intents` | Graph edges for follow-ups |
| `priority` | `critical` \| `high` \| `medium` |
| `description` | Intent summary (localized) |
| `expert_guide` | **Level 3** — advanced operator notes |
| `clarifying_questions` | Ask these when user input is incomplete |
| `faq_refs` | Linked FAQ ids (`Q031`, …) |
| `answer_levels` | Explicit `{level1_short, level2_full, level3_expert}` |

Hard product facts are also mirrored in `meta.facts` (free Basic ops, max 6 exits/nodes, Pro ≠ AI Pro, tabs, VPS Partners-only).

---

## How a bot should use this

### 1) Detect language
Use `all_languages_database.json → language_detection_hints` plus Unicode script heuristics.  
Fallback: `en`.

### 2) Load intents
Prefer `intents/intents_{lang}.json`.  
If confidence is low, also search English keywords.

### 3) Rank intent
Score against `sample_questions` + `keywords`.  
If user says only “doesn’t work” / «کار نمیکنه» → force intent `ambiguous_app_broken` and ask its `clarifying_questions`.

### 4) Answer level
- Quick chat / Telegram default → `short_answer` (L1)
- Support mode → `full_answer` + `steps` (L2)
- Power user / after follow-up → `expert_guide` (L3)

### 5) Safety
- Never invent versions, prices, or VPS brands.
- VPS purchase: **FoxNext.net → Partners only**.
- If facts missing → ask clarifying questions; optionally retrieve markdown FAQ by `faq_refs`.

### 6) Optional RAG
After intent match, enrich from:

`AI_Knowledge_Base_Multilingual/{Persian|English|Russian|Chinese}/FAQ_*.md`

---

## Adding a new capability

1. Add a new `add(intent_id=..., ...)` block in `_part1_intents.py` / `_part2_intents.py` / `_part3_build.py` (or extend master JSON carefully).
2. Provide **all four languages** for every localized field.
3. Include ≥20 `sample_questions` per language.
4. Set `related_intents`, `clarifying_questions`, `faq_refs`.
5. Rebuild:

```powershell
python "AI_BOT_DATABASE\_part3_build.py"
```

6. Commit regenerated JSON files.
7. Update `AI_Language_Map.md` if a new topic family appears.

---

## Adding a new language

1. Extend helpers `L()` / `qs()` with the new code (e.g. `tr`).
2. Fill translations for every intent.
3. Emit `intents/intents_tr.json`.
4. Add detection hints in `all_languages_database.json` meta.
5. Add a folder under `AI_Knowledge_Base_Multilingual/`.

Keep **`intent` ids unchanged** so analytics and routing stay stable.

---

## Intent catalog (current families)

- **Product / Install:** `product_what_is`, `download_installer`, `install_setup`, `setup_vs_portable`, `first_run_path`
- **Modes:** `mode_basic`, `mode_pro`, `mode_ai_pro`, `free_ops_basic`
- **License:** `activate_license`, `device_id`, `claim_code`, `reactivation`, `pricing`, `ai_quota`, `need_activate`, `need_pro`
- **Deploy:** `setup_central`, `connect_ssh`, `full_deploy`, `configure_panel`, `panel_login_info`, `add_exit`, `add_tunnel`, `add_node`
- **Network:** `proxy_settings`, `mesh_servers`
- **AI:** `mode_ai_pro`, `ai_chat_locked`, `check_system`
- **Maintenance:** `delete_history`, `reset_all_servers`, `force_update`
- **Errors:** `ssh_auth_failed`, `ssh_timeout`, `ssh_host_key`, `full_deploy_failed`, `panel_unreachable`
- **Support:** `buy_vps`, `contact_support`
- **Meta:** `ambiguous_app_broken`

Exact count is in each file’s `meta.intent_count`.

---

## Quality rules

1. Do not drop important product gates when editing answers.
2. Keep UI labels in English Title Case (`Full Deploy`, `Connect SSH`).
3. Keep FA/EN/RU/ZH **intent-aligned** (same ids and relations).
4. Mark uncertain Linux stderr / wizard fields as needing human review; prefer clarifying questions over guessing.
