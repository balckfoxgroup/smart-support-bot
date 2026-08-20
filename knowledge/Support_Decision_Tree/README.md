# Support Decision Tree — Black Fox

Interactive troubleshooting flows for **AI Assistant** and **Telegram Bot**.

These trees do **not** replace `AI_BOT_DATABASE` intents — they **orchestrate** them with questions, branches, and escalation.

## Files

| File | Purpose |
|------|---------|
| `Full_Support_Flow.json` | Root menu / router |
| `Installation_Troubleshooting.json` | Install + won't start |
| `License_Troubleshooting.json` | Activation / Device ID / claim / hub |
| `Update_Troubleshooting.json` | Force update / download / hub |
| `Connection_Troubleshooting.json` | SSH / panel / hub / WG client clarification |
| `Server_Troubleshooting.json` | Offline VPS / panel / DNS / deploy / topology |
| `General_Error_Troubleshooting.json` | Ambiguous errors → route to a tree |
| `_build_trees_a.py` / `_build_trees_b.py` | Generators |

## Node types

- `question` — ask user; `answers.{key}.next` chooses next node
- `action` — give step solution; then `next` or `if_unresolved`
- `resolved` — success end (`final_solution`)
- `escalate` — collect `ask_for`, hand off to human / richer intent
- `goto_tree` — jump to another file/tree id

All user-facing strings are objects: `{ "fa", "en", "ru", "zh" }`.

## How the AI should run a tree

1. Detect language (`fa|en|ru|zh`).
2. Start at `Full_Support_Flow.json` → show localized menu.
3. Open the target file + `entry_node`.
4. Loop:
   - If `question`: ask `text[lang]`, map user reply to an answer key, go `next`.
   - If `action`: show `action` + `solution`, ask “Did this fix it?” → yes/`resolved` or `if_unresolved`.
   - If `goto_tree`: load that tree.
   - If `escalate`: ask for checklist items, then `@HiBlackFoxVpn`.
5. Optionally enrich answers via related `related_intents` in `AI_BOT_DATABASE`.

### Stage mapping (required product behavior)

| Stage | Behavior |
|-------|----------|
| 1 | First question = root menu (or tree `entry_node`) |
| 2 | Branch on user answer |
| 3 | Provide stepwise solution (`action` nodes) |
| 4 | If unresolved → collect evidence (`escalate.ask_for`) |

## Link to Intent Database

- Trees diagnose and sequence.
- Intents provide dense FAQ answers / keywords.
- Example: SSH auth failure tree step → also retrieve intent `ssh_auth_failed`.

Field `related_intents` on each tree lists primary intent ids.

## Product-specific notes

- “Connection” is **not** a consumer VPN toggle. Clarify SSH vs panel vs hub vs end-user WireGuard client.
- Free Basic ops without license: Setup Central + Connect SSH + Full Deploy only.
- Pro ≠ AI Pro.
- Never invent versions/prices; VPS only via FoxNext Partners.

## Adding a new problem

1. Add a tree object in the matching generator section (or JSON file).
2. Provide FA/EN/RU/ZH for all texts and answer labels.
3. Set `entry_node`, wire `next` ids, include an `escalate` path.
4. Add `related_intents`.
5. Register in `Full_Support_Flow.json` menu if it is a top-level category.
6. Rebuild:

```powershell
python Support_Decision_Tree\_build_trees_a.py
python Support_Decision_Tree\_build_trees_b.py
```

## Success criteria

Before human handoff, the bot should have asked clarifying questions, tried stepwise fixes, and collected Device ID + screenshot when still failing.
