# Domain, Configure, and Mesh — Black Fox VPN Installer & Android

Ask AI support knowledge for **Black Fox VPN Installer & Android**. Do not invent version numbers. Prefer the product catalog when it is more specific.

## Official product name
Always use this name in bot replies: **Black Fox VPN Installer & Android**

## Add Domain
Three tabs in one feature:

### 1) DNS
Connect Cloudflare or ArvanCloud for the user’s own domain; zone and A records for central or bot webhook. Separate from Black Fox free domains.

### 2) External Proxy
Up to 3 public domains on central panel inbound ports. Needs Full Deploy and panel credentials. Apply to Panel. Not a Free Domain replacement.

### 3) Free Domain
Free Black Fox subdomain on a selected server.

| Mode | Free subdomains per install |
| --- | --- |
| Basic | 0 (disabled) |
| Pro | 3 |
| AI Pro | 5 |

Suffixes: `.ir`, `.store`, `.online`, `.site` — users in Iran should preferably use `.ir`.

Short steps: select server → pick suffix → Get Free Domain from Black Fox → Refresh Domain List if needed → copy from Your Domain.

## Configure Panel and auto domain activation
Configure Panel sets inbound/outbound and relay.

During domain configure, if Pro or AI Pro is active and Free Domain quota remains, a free subdomain is **automatically** activated on that server (central / Exit / Node) and applied to sub-configs.

If quota is exhausted: panel configure still finishes, but sub-config domains are not set.

## Mesh Servers
- View tab: live Topology of Central / Tunnel / Exit / Node and link status
- Deploy / Repair: install Link Monitor Agents on hosts with SSH; monitor WireGuard, GRE, and Reverse Tunnel Stealth-WSS even when the app is closed
- Base failover: WireGuard → GRE → Reverse Tunnel Stealth-WSS
- Optional backup paths and Optimize VPS on the selected link

Prerequisites: servers registered with SSH; Topology usually after deploy or existing links.

## Reply rule
Do not invent facts. If missing from catalog and this file, say you do not know and hand off to support.
