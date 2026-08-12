"""Load host-editable product catalogs for menu buttons and AI answers."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

SUPPORTED = ("fa", "en", "ru", "zh")


@dataclass(slots=True)
class ProductCatalog:
    product_id: str
    catalog_id: str
    enabled: bool
    menu_order: int
    menu_emoji: str
    title: dict[str, str]
    short_summary: dict[str, str]
    long_summary: dict[str, str]
    features: list[dict[str, Any]] = field(default_factory=list)
    does_not: dict[str, list[str]] = field(default_factory=dict)
    keywords: list[str] = field(default_factory=list)
    media: list[dict[str, Any]] = field(default_factory=list)
    support: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    def label(self, lang: str) -> str:
        title = self.title.get(lang) or self.title.get("en") or self.product_id
        emoji = (self.menu_emoji or "").strip()
        return f"{emoji} {title}".strip() if emoji else title

    def summary(self, lang: str) -> str:
        return (
            self.long_summary.get(lang)
            or self.short_summary.get(lang)
            or self.long_summary.get("en")
            or self.short_summary.get("en")
            or ""
        )

    def menu_body(self, lang: str) -> str:
        # Hub intro: short educational copy (prefer short_summary).
        intro = (
            self.short_summary.get(lang)
            or self.long_summary.get(lang)
            or self.short_summary.get("en")
            or self.long_summary.get("en")
            or ""
        ).strip()
        lines = [f"{self.label(lang)}", "", intro]
        feats = self.features or []
        if feats:
            lines.append("")
            tip = "کلیدها را بزنید تا کوتاه یاد بگیرید:" if lang == "fa" else "Tap a key for a short tip:"
            lines.append(tip)
            for feat in feats[:8]:
                if not isinstance(feat, dict):
                    continue
                title = (feat.get("title") or {}).get(lang) or (feat.get("title") or {}).get("en")
                if title:
                    lines.append(f"• {title}")
        empty_media = [m for m in self.media if isinstance(m, dict) and not str(m.get("path") or "").strip()]
        if empty_media and lang == "fa":
            lines.append("")
            lines.append("عکس‌های محصول به‌زودی اضافه می‌شوند.")
        elif empty_media:
            lines.append("")
            lines.append("Product photos coming soon.")
        return "\n".join(lines).strip()


_CACHE: list[ProductCatalog] = []


def product_catalogs_dir(knowledge_root: Path) -> Path:
    return knowledge_root / "product_catalogs"


def load_product_catalogs(knowledge_root: Path) -> list[ProductCatalog]:
    """Scan knowledge/product_catalogs/*.json and cache enabled products."""
    global _CACHE
    folder = product_catalogs_dir(knowledge_root)
    out: list[ProductCatalog] = []
    if not folder.is_dir():
        logger.warning("product_catalogs folder missing: %s", folder)
        _CACHE = []
        return _CACHE
    for path in sorted(folder.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("Skip catalog %s: %s", path.name, exc)
            continue
        if not isinstance(data, dict) or not data.get("enabled", True):
            continue
        product_id = str(data.get("product_id") or path.stem).strip()
        if not product_id:
            continue
        title = data.get("title") if isinstance(data.get("title"), dict) else {}
        short_summary = data.get("short_summary") if isinstance(data.get("short_summary"), dict) else {}
        long_summary = data.get("long_summary") if isinstance(data.get("long_summary"), dict) else {}
        does_not = data.get("does_not") if isinstance(data.get("does_not"), dict) else {}
        features = data.get("features") if isinstance(data.get("features"), list) else []
        media = data.get("media") if isinstance(data.get("media"), list) else []
        keywords = data.get("keywords") if isinstance(data.get("keywords"), list) else []
        support = data.get("support") if isinstance(data.get("support"), dict) else {}
        out.append(
            ProductCatalog(
                product_id=product_id,
                catalog_id=str(data.get("catalog_id") or product_id),
                enabled=True,
                menu_order=int(data.get("menu_order") or 100),
                menu_emoji=str(data.get("menu_emoji") or ""),
                title={k: str(v) for k, v in title.items()},
                short_summary={k: str(v) for k, v in short_summary.items()},
                long_summary={k: str(v) for k, v in long_summary.items()},
                features=[f for f in features if isinstance(f, dict)],
                does_not={k: [str(x) for x in (v or [])] for k, v in does_not.items() if isinstance(v, list)},
                keywords=[str(k) for k in keywords],
                media=[m for m in media if isinstance(m, dict)],
                support=support,
                raw=data,
            )
        )
    out.sort(key=lambda p: (p.menu_order, p.product_id))
    _CACHE = out
    logger.info("Product catalogs loaded: %s", [p.product_id for p in out])
    return _CACHE


def get_product_catalogs() -> list[ProductCatalog]:
    return list(_CACHE)


def get_product(product_id: str) -> ProductCatalog | None:
    for item in _CACHE:
        if item.product_id == product_id:
            return item
    return None


def product_action_id(product_id: str) -> str:
    return f"product:{product_id}"


def parse_product_action(action: str | None) -> str | None:
    if not action or not action.startswith("product:"):
        return None
    # Ignore feature actions that also start with product: — use product:id only
    rest = action.split(":", 1)[1].strip()
    if not rest or ":" in rest:
        return None
    return rest or None


def feature_action_id(product_id: str, feature_id: str) -> str:
    return f"pfeat:{product_id}:{feature_id}"


def parse_feature_action(action: str | None) -> tuple[str, str] | None:
    if not action or not action.startswith("pfeat:"):
        return None
    parts = action.split(":", 2)
    if len(parts) != 3:
        return None
    _, product_id, feature_id = parts
    product_id = product_id.strip()
    feature_id = feature_id.strip()
    if not product_id or not feature_id:
        return None
    return product_id, feature_id


def feature_label(product: ProductCatalog, feature: dict[str, Any], lang: str) -> str:
    title = (feature.get("title") or {}).get(lang) or (feature.get("title") or {}).get("en") or feature.get("id")
    return str(title)


def feature_body(product: ProductCatalog, feature: dict[str, Any], lang: str) -> str:
    """Short educational reply for a product feature key (1–2 lines)."""
    title = feature_label(product, feature, lang)
    summary = (feature.get("summary") or {}).get(lang) or (feature.get("summary") or {}).get("en") or ""
    summary = str(summary).strip()
    if lang == "fa":
        # Keep replies educational and very concise for Telegram.
        if summary:
            return f"{title}\n{summary}".strip()
        return str(title)
    lines = [str(title)]
    if summary:
        lines.append(summary)
    return "\n".join(lines).strip()


def ai_products_snippet(query: str, *, lang: str = "en", limit_chars: int = 4500) -> str:
    """Build a prompt block from product catalogs matching the query (or all if product ask)."""
    catalogs = get_product_catalogs()
    if not catalogs:
        return ""
    q = (query or "").lower()
    product_ask = any(
        w in q
        for w in (
            "product",
            "محصول",
            "catalog",
            "کاتالوگ",
            "installer",
            "config builder",
            "ربات",
            "bot",
            "what is",
            "چیست",
        )
    )
    scored: list[tuple[int, ProductCatalog]] = []
    for cat in catalogs:
        score = 0
        blob = " ".join(
            [
                cat.product_id,
                cat.catalog_id,
                " ".join(cat.keywords),
                " ".join(cat.title.values()),
                " ".join(cat.short_summary.values()),
            ]
        ).lower()
        for token in re.findall(r"[\w\u0600-\u06ff]+", q):
            if len(token) < 3:
                continue
            if token in blob:
                score += 2
        if product_ask:
            score += 1
        if score > 0:
            scored.append((score, cat))
    if not scored and product_ask:
        scored = [(1, c) for c in catalogs]
    if not scored:
        # Always expose a short index so AI knows which products exist.
        lines = ["Product catalog index:"]
        for cat in catalogs:
            lines.append(f"- {cat.product_id}: {cat.short_summary.get(lang) or cat.short_summary.get('en') or cat.title.get('en')}")
        return "\n".join(lines)[:limit_chars]

    scored.sort(key=lambda x: (-x[0], x[1].menu_order))
    blocks = ["Official product catalogs (authoritative feature facts):"]
    used = 0
    for _, cat in scored:
        body = cat.menu_body(lang)
        chunk = f"### {cat.product_id}\n{body}"
        if used + len(chunk) > limit_chars:
            break
        blocks.append(chunk)
        used += len(chunk)
    return "\n\n".join(blocks)[:limit_chars]
