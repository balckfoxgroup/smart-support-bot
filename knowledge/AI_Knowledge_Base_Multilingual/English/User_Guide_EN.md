# Black Fox VPN — User Guide (English)

> Audience: customers, Telegram Bot, AI Assistant.  
> Fact basis: current product docs in `/Documentation`.  
> Rules: do not invent versions, prices, or VPS brands. Buy VPS only via **FoxNext.net → Partners**. Mark unknowns as `NEED_MORE_REVIEW`.

---

## 1. Product introduction

**Black Fox Vpn** is a Windows **Installer / operations toolkit** (Android companion available). It automates building multi-location VPN infrastructure on **your Linux VPS** using **SSH**, **WireGuard**, and the **Sanaei 3X-UI Panel**.

It is **not** a consumer “connect phone and browse” VPN client.

**Hubs / site:** `foxnext.net`, `blackfoxupdate.ir`  
**Support:** Contact tab / `@HiBlackFoxVpn`

---

## 2. Features overview

| Area | What it does |
|------|----------------|
| Setup Central | Save central VPS SSH locally |
| Connect SSH | Verify SSH login (free in Basic) |
| Full Deploy | Install WireGuard + 3X-UI on central (free in Basic) |
| Exit Servers | Egress locations — **max 6 slots** (needs license) |
| Tunnel Servers | Pro multi-hop relays |
| Node Servers | Remote 3X-UI nodes on central — **max 6** |
| Configure Panel | Repair inbound/outbound/SOCKS for existing exit/node (**not** central install) |
| Domain / DNS | Cloudflare / ArvanCloud manager (Pro) |
| CDN | Arvan / Cloudflare / Other (Pro) |
| Mesh Servers | Link Monitor agents / link status (Pro) |
| Telegram Bot | Mirza install / other / move (Pro) |
| Move Central | Migrate central role (Pro) |
| Proxy Settings | Direct first, then Program Proxy |
| Panel Login Info / Test Client | Credentials + client checks |
| AI Assistant Pro | Chat + Tasks for the same ops (separate unlock + quota) |
| Registration | Device ID, Activate, Reactivation, My Code |
| Check System | Diagnostic Center |
| Deletes / Reset | History, exits/nodes/tunnels, Reset All Servers, Factory Reset (Pro) |

---

## 3. Install guide

1. Download **Black Fox Vpn-Installer-Setup.exe** from **foxnext.net** (prefer official site).
2. Run Setup (or use portable folder carefully).
3. Splash appears (saved language is applied).
4. First run: choose **Language** → Continue.
5. Mode picker: **SELECT BASIC** / **PRO** / **AI ASSISTANT PRO**.
6. Main window opens (usually **Operations**).

---

## 4. Usage guide (recommended first path)

1. **Operations → Central Server Setup** — enter IP, port, user, password or key → Save.
2. **Connect SSH** — wait for success.
3. **Full Deploy** — choose 3X-UI source: Sanaei GitHub / BlackFox Hub / Local PC.
4. Open **Panel Login Info** — copy URL / user / password.
5. Optional **Test Client**.
6. When you need exits: **Registration** → copy **Device ID** → activate **Basic** (`BFXB` / claim) → **Add Exit Server** → **Configure Panel**.

---

## 5. Pages / tabs

| Tab | Purpose |
|-----|---------|
| **Operations** | Deploy buttons + terminal/status (or AI chat in AI Pro) |
| **Check System** | Read-only diagnostics / export log |
| **View** | Switch Basic / Pro / AI Pro; topology when ready |
| **Settings** | Language, Updates, Packages, Factory Reset (Pro UI) |
| **Registration** | Device ID, Activate, Reactivation, My Code |
| **Contact** | Website, email, Telegram links from hub config |

**Overlays:** Add Domain (DNS Manager), Mesh Servers.

---

## 6. Beginner guide

1. Use **Basic** mode first.
2. Central in Basic free path should be **Iran / China / Russia**.
3. Always **Connect SSH** before **Full Deploy**.
4. Do not expect the app itself to be your phone VPN client.
5. Activate license before Exit / Configure Panel.
6. If hubs/SSH fail: **Proxy Settings**.

---

## 7. Advanced guide (Pro / AI Pro)

**Order:** Central → SSH → Full Deploy → optional Tunnels → Exits (1–6) → Configure Panel → Nodes → Domain → CDN → Mesh → Mirza Bot → Move Central only when migrating.

**AI Assistant Pro**
1. Unlock **AI Pro** (`BFXA`) + AI quota (`BFXQ` recharges).
2. Pro alone does **not** unlock AI chat.
3. Prefer **Tasks**; confirm Yes/No before mutating actions.
4. Diagnostics tab ≠ AI **Diagnose & Repair**.

**Link types (product names):** WireGuard (default), GRE fallback, Reverse Tunnel (Stealth-WSS).

---

## 8. Common problems

| Problem | Likely cause | First fix |
|---------|--------------|-----------|
| Need activate on Exit | No Basic/Pro license | Registration |
| AI locked | No AI Pro / no quota | Activate AI Pro + recharge |
| SSH fail | Creds / firewall / network | Recheck Setup Central; Proxy |
| Full Deploy fail | Source / network / OS | Retry Hub or Local PC; read terminal |
| Configure Panel errors | No exit/node yet | Add exit/node first |
| Topology empty | Deploy/client not ready | Finish Full Deploy |

---

## 9. Error solutions (support playbook)

1. Read **status bar** + **terminal**.
2. Confirm mode + license gates.
3. Try **Proxy Settings** if hub/SSH blocked.
4. Re-run **Connect SSH** then the failed op.
5. Use **Check System**; export log.
6. Contact **@HiBlackFoxVpn** with **Device ID** + screenshot.

Destructive ops: **Delete History** (local only), **Reset All Servers** (remote WG/panel wipe, SSH kept), **Factory Reset** (Pro — strong confirm).

---

## 10. Cross-feature relationships

| If you… | Then… |
|---------|--------|
| Full Deploy succeeds | Panel Login Info works in all modes (shared store) |
| Add Exit/Node | Configure Panel / Mesh / deletes become relevant |
| Delete tunnel hop | Higher hops may reset; remove dependent exits first |
| Switch View mode | Same servers; different UI/gates |
| Unlock Pro only | AI still locked until AI Pro + quota |

---

## License code families

`BFXB` Basic · `BFXP` Pro · `BFXA` AI Pro · `BFXQ` AI quota · claim codes contain `-CLM-`

---

## NEED_MORE_REVIEW

Live capture of every wizard field, some Linux stderr strings, hub build drift vs local AppBuild.
