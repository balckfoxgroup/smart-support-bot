"""Catalog RAG: semantic topic retrieval + educational context for Ask AI.

Not a parallel answer system — feeds the existing LLM path with better evidence.
Does not hardcode per-question replies.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.knowledge.product_catalogs import ProductCatalog, get_product_catalogs

logger = logging.getLogger(__name__)

# Concept aliases → boost matching without per-question hardcoding.
# Keys are normalized (lower, ZWNJ stripped). Values are tokens merged into the query.
TOPIC_ALIASES: dict[str, tuple[str, ...]] = {
    "پیکربندی": ("configure", "panel", "configure_panel", "inbound", "outbound", "config"),
    "پیکربندی پنل": ("configure_panel", "configure", "panel", "inbound", "outbound"),
    "کانفیگ": ("configure", "configure_panel", "config", "panel"),
    "کانفیگ پنل": ("configure_panel", "configure", "panel"),
    "configure": ("configure_panel", "panel", "inbound", "outbound"),
    "configuration": ("configure_panel", "configure", "panel"),
    "inbound": ("configure_panel", "inbounds", "panel"),
    "outbound": ("configure_panel", "add_outbounds", "outbounds"),
    "outbounds": ("add_outbounds", "configure_panel"),
    "نصب": ("full_deploy", "deploy", "setup", "install"),
    "دیپلوی": ("full_deploy", "deploy"),
    "فول دیپلوی": ("full_deploy", "deploy", "wireguard", "3x-ui"),
    "full deploy": ("full_deploy", "deploy", "wireguard"),
    "fulldeploy": ("full_deploy", "deploy"),
    "ssh": ("connect_ssh", "central", "setup_central"),
    "اتصال": ("connect_ssh", "ssh", "link"),
    "مش": ("mesh", "topology", "mesh_topology"),
    "توپولوژی": ("topology", "mesh", "view"),
    "دامنه": ("domain", "dns", "cdn", "add_domain", "free_domain"),
    "دامنه رایگان": ("free_domain", "freedns", "subdomain", "pro", "ai pro"),
    "ساب دامین": ("free_domain", "subdomain", "domain"),
    "ساب‌دامین": ("free_domain", "subdomain", "domain"),
    "free domain": ("free_domain", "subdomain", "pro", "ai pro"),
    "add domain": ("add_domain_dns", "external_proxy", "free_domain", "domain"),
    "external proxy": ("external_proxy", "domain", "inbound"),
    "mesh servers": ("mesh_servers", "mesh_topology", "mesh", "link monitor"),
    "مش سرور": ("mesh_servers", "mesh_topology", "mesh"),
    "سی‌دی‌ان": ("cdn", "cloudflare"),
    "cdn": ("cdn", "cloudflare", "domain"),
    "لایسنس": ("registration", "license", "pro"),
    "ریست": ("factory_reset", "reset"),
    "ترمینال": ("terminal",),
    "ربات": ("telegram", "mirza", "smart_support", "agent"),
    "نود": ("add_node_servers", "node"),
    "اگزیت": ("add_exit_servers", "exit"),
    "تونل": ("add_tunnel_servers", "tunnel"),
}

EDU_HINTS = (
    "آموزش",
    "اموزش",
    "چطور",
    "چگونه",
    "توضیح",
    "توضیح بده",
    "راهنما",
    "مراحل",
    "چیست",
    "چی هست",
    "how",
    "what is",
    "explain",
    "tutorial",
    "steps",
)


@dataclass(slots=True)
class CatalogUnit:
    """One searchable knowledge unit (feature or media card)."""

    kind: str  # feature | media | product
    product_id: str
    unit_id: str
    title: str
    body: str
    search_blob: str
    feature_ids: list[str] = field(default_factory=list)
    media_slots: list[str] = field(default_factory=list)
    media_path: str = ""
    score: float = 0.0


@dataclass(slots=True)
class CatalogRetrieval:
    query_expanded: str
    units: list[CatalogUnit]
    media_paths: list[Path]
    is_educational: bool
    insufficient: bool
    prompt_block: str


def _norm(text: str) -> str:
    t = (text or "").strip().lower().replace("‌", "")
    return re.sub(r"\s+", " ", t)


def _tokens(text: str) -> list[str]:
    return [t for t in re.findall(r"[\w\u0600-\u06ff]+", _norm(text)) if len(t) >= 2]


def expand_query(query: str) -> str:
    """Merge alias tokens so Persian teaching phrases map to catalog English ids."""
    q = _norm(query)
    extra: list[str] = []
    # Longer phrases first
    for phrase, aliases in sorted(TOPIC_ALIASES.items(), key=lambda x: -len(x[0])):
        if phrase in q:
            extra.extend(aliases)
    # Also map space-insensitive compact forms
    compact = q.replace(" ", "").replace("-", "").replace("_", "")
    for phrase, aliases in TOPIC_ALIASES.items():
        pcompact = phrase.replace(" ", "").replace("-", "").replace("_", "")
        if len(pcompact) >= 4 and pcompact in compact:
            extra.extend(aliases)
    if not extra:
        return q
    return f"{q} " + " ".join(dict.fromkeys(extra))


def is_educational_question(query: str) -> bool:
    q = _norm(query)
    return any(h in q for h in EDU_HINTS)


def _lang_text(obj: Any, lang: str) -> str:
    if isinstance(obj, dict):
        return str(obj.get(lang) or obj.get("en") or obj.get("fa") or "").strip()
    return str(obj or "").strip()


def _feature_body(feat: dict[str, Any], lang: str) -> str:
    title = _lang_text(feat.get("title"), lang)
    summary = _lang_text(feat.get("summary"), lang)
    howto = _lang_text(feat.get("howto"), lang)
    parts = [p for p in (title, summary, howto) if p]
    return "\n".join(parts)


def build_catalog_units(*, lang: str = "fa") -> list[CatalogUnit]:
    units: list[CatalogUnit] = []
    for cat in get_product_catalogs():
        # Product overview unit
        prod_title = cat.title.get(lang) or cat.title.get("en") or cat.product_id
        prod_body = (
            cat.long_summary.get(lang)
            or cat.short_summary.get(lang)
            or cat.long_summary.get("en")
            or cat.short_summary.get("en")
            or ""
        )
        keywords = " ".join(str(k) for k in (cat.keywords or []))
        units.append(
            CatalogUnit(
                kind="product",
                product_id=cat.product_id,
                unit_id=f"product:{cat.product_id}",
                title=str(prod_title),
                body=str(prod_body),
                search_blob=_norm(
                    f"{cat.product_id} {prod_title} {prod_body} {keywords} "
                    + " ".join(cat.title.values())
                    + " "
                    + " ".join(cat.short_summary.values())
                ),
                feature_ids=[],
                media_slots=[],
            )
        )
        slot_to_feat: dict[str, str] = {}
        for feat in cat.features or []:
            if not isinstance(feat, dict):
                continue
            fid = str(feat.get("id") or "").strip()
            if not fid:
                continue
            title = _lang_text(feat.get("title"), lang)
            body = _feature_body(feat, lang)
            slot = str(feat.get("media_slot") or "").strip()
            related = [
                str(x).strip()
                for x in (feat.get("related_media_slots") or [])
                if str(x).strip()
            ]
            slots = []
            if slot:
                slots.append(slot)
                slot_to_feat[slot] = fid
            for s in related:
                if s not in slots:
                    slots.append(s)
                slot_to_feat.setdefault(s, fid)
            blob = _norm(
                f"{fid} {title} {body} {slot} {' '.join(slots)} "
                + " ".join(str(v) for v in (feat.get("title") or {}).values())
                + " "
                + " ".join(str(v) for v in (feat.get("summary") or {}).values())
            )
            units.append(
                CatalogUnit(
                    kind="feature",
                    product_id=cat.product_id,
                    unit_id=f"feature:{cat.product_id}:{fid}",
                    title=title or fid,
                    body=body,
                    search_blob=blob,
                    feature_ids=[fid],
                    media_slots=slots,
                )
            )

        for media in cat.media or []:
            if not isinstance(media, dict):
                continue
            rel = str(media.get("path") or "").strip().replace("\\", "/")
            if not rel:
                continue
            slot = str(media.get("slot") or "").strip()
            note = str(media.get("note") or "").strip()
            mid = str(media.get("id") or slot or Path(rel).stem).strip()
            title = _lang_text(media.get("title"), lang) or note or slot or mid
            desc = _lang_text(media.get("description"), lang) or note
            topics = media.get("topics") if isinstance(media.get("topics"), list) else []
            feat_ids = (
                media.get("feature_ids")
                if isinstance(media.get("feature_ids"), list)
                else []
            )
            feat_ids_s = [str(x).strip() for x in feat_ids if str(x).strip()]
            if not feat_ids_s and slot in slot_to_feat:
                feat_ids_s = [slot_to_feat[slot]]
            # Derive soft links from slot naming
            soft = slot.replace("-", "_").replace(" ", "_")
            blob = _norm(
                f"{mid} {slot} {note} {title} {desc} {' '.join(map(str, topics))} "
                f"{' '.join(feat_ids_s)} {soft} {rel}"
            )
            units.append(
                CatalogUnit(
                    kind="media",
                    product_id=cat.product_id,
                    unit_id=f"media:{cat.product_id}:{mid}",
                    title=str(title),
                    body=str(desc or note),
                    search_blob=blob,
                    feature_ids=feat_ids_s,
                    media_slots=[slot] if slot else [],
                    media_path=rel,
                )
            )
    return units


def score_unit(query_expanded: str, unit: CatalogUnit) -> float:
    q = _norm(query_expanded)
    tokens = _tokens(q)
    if not tokens:
        return 0.0
    blob = unit.search_blob
    compact_q = q.replace(" ", "").replace("-", "").replace("_", "")
    compact_blob = blob.replace(" ", "").replace("-", "").replace("_", "")
    score = 0.0
    hits = 0
    for tok in tokens:
        if len(tok) < 3:
            continue
        if tok in blob:
            score += 1.6
            hits += 1
        ctok = tok.replace("-", "").replace("_", "")
        if len(ctok) >= 4 and ctok in compact_blob:
            score += 1.2
            hits += 1
    # Coverage: prefer units that match a larger share of meaningful tokens
    meaningful = [t for t in tokens if len(t) >= 3]
    if meaningful:
        cov = hits / max(1, len(meaningful))
        score *= 0.55 + min(1.0, cov)
    # Strong id/title containment
    for fid in unit.feature_ids:
        fcompact = fid.replace("_", "").replace("-", "").lower()
        if fcompact and fcompact in compact_q:
            score += 10.0
    title_c = _norm(unit.title).replace(" ", "")
    if len(title_c) >= 5 and title_c in compact_q:
        score += 6.0
    # Kind weights: features > media cards for text evidence
    if unit.kind == "feature":
        score *= 1.15
    elif unit.kind == "media":
        score *= 0.85
    elif unit.kind == "product":
        score *= 0.7
    return score


def retrieve_catalog_context(
    query: str,
    *,
    lang: str = "fa",
    project_root: Path,
    limit_features: int = 4,
    limit_media: int = 2,
    min_score: float = 4.5,
) -> CatalogRetrieval:
    """Retrieve related catalog sections + only relevant images for a user question."""
    expanded = expand_query(query)
    educational = is_educational_question(query)
    units = build_catalog_units(lang=lang)
    scored: list[CatalogUnit] = []
    for u in units:
        s = score_unit(expanded, u)
        if s < min_score:
            continue
        u.score = s
        scored.append(u)
    scored.sort(key=lambda x: (-x.score, x.unit_id))

    # Prefer feature units for evidence; keep product overview only if strong
    features = [u for u in scored if u.kind == "feature"][:limit_features]
    products = [u for u in scored if u.kind == "product"][:1]
    media_units = [u for u in scored if u.kind == "media"]

    evidence = features or products
    # If educational and we have a weak top hit, still keep it when clearly themed
    if not evidence and scored:
        top = scored[0]
        if top.score >= min_score * 0.85:
            evidence = [top]

    # Related feature ids from evidence → pull linked media
    wanted_feats = {fid for u in evidence for fid in u.feature_ids}
    wanted_slots = {s for u in evidence for s in u.media_slots}

    media_scored: list[tuple[float, CatalogUnit]] = []
    seen_paths: set[str] = set()
    for mu in media_units:
        bonus = mu.score
        if any(f in wanted_feats for f in mu.feature_ids):
            bonus += 8.0
        if any(s in wanted_slots for s in mu.media_slots):
            bonus += 10.0
        if bonus < min_score + 1.0 and not (
            any(f in wanted_feats for f in mu.feature_ids)
            or any(s in wanted_slots for s in mu.media_slots)
        ):
            continue
        if not mu.media_path or mu.media_path in seen_paths:
            continue
        path = (project_root / mu.media_path).resolve()
        if not path.is_file():
            continue
        seen_paths.add(mu.media_path)
        media_scored.append((bonus, mu))

    # Also resolve paths for evidence slots even if media unit scored low
    catalogs = {c.product_id: c for c in get_product_catalogs()}
    for u in evidence:
        cat = catalogs.get(u.product_id)
        if not cat:
            continue
        for media in cat.media or []:
            if not isinstance(media, dict):
                continue
            slot = str(media.get("slot") or "").strip()
            rel = str(media.get("path") or "").strip().replace("\\", "/")
            if not rel or rel in seen_paths:
                continue
            if slot and slot in wanted_slots:
                path = (project_root / rel).resolve()
                if path.is_file():
                    seen_paths.add(rel)
                    media_scored.append(
                        (
                            20.0,
                            CatalogUnit(
                                kind="media",
                                product_id=u.product_id,
                                unit_id=f"media-slot:{slot}",
                                title=slot,
                                body=str(media.get("note") or ""),
                                search_blob=slot,
                                media_slots=[slot],
                                media_path=rel,
                                score=20.0,
                            ),
                        )
                    )

    media_scored.sort(key=lambda x: -x[0])
    media_paths = [
        (project_root / mu.media_path).resolve()
        for _, mu in media_scored[:limit_media]
        if mu.media_path
    ]
    # Deduplicate existing files only
    media_paths = [p for p in media_paths if p.is_file()]

    insufficient = not evidence
    prompt_block = _format_prompt_block(
        evidence=evidence,
        media_units=[m for _, m in media_scored[:limit_media]],
        educational=educational,
        insufficient=insufficient,
        lang=lang,
    )
    return CatalogRetrieval(
        query_expanded=expanded,
        units=evidence,
        media_paths=media_paths,
        is_educational=educational,
        insufficient=insufficient,
        prompt_block=prompt_block,
    )


def _format_prompt_block(
    *,
    evidence: list[CatalogUnit],
    media_units: list[CatalogUnit],
    educational: bool,
    insufficient: bool,
    lang: str,
) -> str:
    lines: list[str] = ["### Catalog evidence (authoritative — do not invent beyond this)"]
    if insufficient:
        lines.append(
            "NO sufficiently related catalog sections were found for this question. "
            "Say clearly that catalog information is insufficient. "
            "Do NOT invent product steps or limits."
        )
        return "\n".join(lines)

    for i, u in enumerate(evidence, 1):
        lines.append(f"\n#### Section {i}: {u.title} [{u.kind}/{u.product_id}]")
        lines.append(u.body or "(no body)")
        if u.feature_ids:
            lines.append(f"feature_ids: {', '.join(u.feature_ids)}")

    if media_units:
        lines.append("\n#### Related teaching screenshots (already selected for Telegram)")
        for m in media_units:
            lines.append(f"- {m.title}: {m.body or m.media_path}")

    lines.append("\n#### Reply style rules")
    if educational or lang.startswith("fa"):
        lines.append(
            "Write like a patient product tutor. Cover: (1) what it is, "
            "(2) what it is for, (3) ordered steps, (4) useful tip/limit if present in evidence. "
            "Do not dump only button names. Finish every sentence completely. "
            "Reply in the user's language. Keep official UI labels in English Title Case."
        )
    else:
        lines.append(
            "Answer completely from evidence. Finish sentences. User language. "
            "Official UI labels stay in English Title Case."
        )
    return "\n".join(lines)


def enrich_media_entry_from_filename(
    filename: str, *, product_id: str, index: int
) -> dict[str, Any]:
    """Heuristic metadata so new uploads are searchable without hand-editing JSON."""
    stem = Path(filename).stem.lower()
    slot = re.sub(r"[^a-z0-9]+", "-", stem).strip("-") or f"{product_id}-{index}"
    topics = [t for t in re.split(r"[-_]+", stem) if len(t) >= 3][:8]
    feature_guess = []
    joined = stem.replace("-", "_")
    for token in topics:
        feature_guess.append(token)
    return {
        "id": slot,
        "role": "screenshot" if index else "hero",
        "slot": slot,
        "path": f"media/catalogs/{product_id}/{Path(filename).name}",
        "local_folder": f"media/catalogs/{product_id}",
        "note": f"auto-indexed from {Path(filename).name}",
        "title": {"fa": slot, "en": slot, "ru": slot, "zh": slot},
        "description": {
            "fa": f"تصویر آموزشی مرتبط با {slot}",
            "en": f"Teaching screenshot for {slot}",
            "ru": f"Teaching screenshot for {slot}",
            "zh": f"Teaching screenshot for {slot}",
        },
        "topics": topics,
        "feature_ids": feature_guess[:3],
        "stage": "guide",
    }
