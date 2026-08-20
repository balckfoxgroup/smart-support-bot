"""Search local license catalog + official website pages for support answers."""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any

import httpx

from src.ai.persona import SITE_URL, SUPPORT_HANDLE, wants_sales_nudge
from src.config import Settings

logger = logging.getLogger(__name__)

_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")

_SITE_PATHS = (
    "/",
    "/en/",
    "/fa/",
    "/download/",
    "/en/download/",
)


class CatalogSiteSearch:
    """Load license-access.json and optionally fetch foxnext.net text snippets."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._catalog: dict[str, Any] = {}
        self._site_cache: dict[str, str] = {}

    def load(self) -> None:
        path = self.settings.knowledge_root / "license-access.json"
        if not path.is_file():
            logger.warning("license-access.json missing at %s", path)
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                self._catalog = data
                logger.info("License catalog loaded (%s)", path.name)
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("Cannot load catalog: %s", exc)

    def catalog_snippet(self, query: str, *, lang: str = "en") -> str:
        if not self._catalog:
            return ""
        q = (query or "").lower()
        price_ask = wants_sales_nudge(query, None) or any(
            w in q for w in ("قیمت", "price", "buy", "خرید", "license", "لایسنس", "usdt")
        )
        if not price_ask and not any(
            w in q for w in ("catalog", "کاتالوگ", "mode", "مد", "basic", "pro", "ai pro")
        ):
            # Still allow a short mode list when comparing modes
            if "mode" not in q and "مد" not in q:
                return ""

        modes = self._catalog.get("license_modes") or {}
        lines: list[str] = [
            "Official license catalog (authoritative for prices when present):",
            f"currency={self._catalog.get('currency', 'USDT')}",
            f"updated_at={self._catalog.get('updated_at', '')}",
        ]
        for key in ("basic", "pro", "ai_pro"):
            mode = modes.get(key)
            if not isinstance(mode, dict) or not mode.get("enabled", True):
                continue
            prices = mode.get("prices") or {}
            price_bits = ", ".join(f"{m}m={p}" for m, p in sorted(prices.items(), key=lambda x: int(x[0])))
            lines.append(
                f"- {key}: visible={mode.get('site_visible')} "
                f"anchor_30={mode.get('anchor_30_usdt')} "
                f"min={mode.get('min_price_usdt')} prices=[{price_bits}]"
            )
            if mode.get("includes_ai_quota"):
                lines.append(f"  note: {key} includes AI quota flag in catalog")
        multi = self._catalog.get("multi_device") or {}
        if multi:
            lines.append(
                f"- multi_device max={multi.get('max_devices')} discounts={multi.get('discounts')}"
            )
        lines.append(f"Purchase/site: {SITE_URL} — support account: {SUPPORT_HANDLE}")
        return "\n".join(lines)

    async def site_snippet(self, query: str, *, limit: int = 3500) -> str:
        """Fetch a few official pages and keep text overlapping the query."""
        q_tokens = {t for t in re.findall(r"[\w\u0600-\u06ff]+", (query or "").lower()) if len(t) > 2}
        blocks: list[str] = []
        async with httpx.AsyncClient(timeout=12.0, follow_redirects=True) as client:
            for path in _SITE_PATHS:
                url = SITE_URL.rstrip("/") + path
                text = await self._fetch_text(client, url)
                if not text:
                    continue
                score = sum(1 for t in q_tokens if t in text.lower()) if q_tokens else 1
                if score <= 0 and q_tokens:
                    continue
                snippet = text[:1800]
                blocks.append(f"### {url}\n{snippet}")
                if sum(len(b) for b in blocks) >= limit:
                    break
        if not blocks:
            return ""
        return "Official site excerpts:\n" + "\n\n".join(blocks)[:limit]

    async def _fetch_text(self, client: httpx.AsyncClient, url: str) -> str:
        if url in self._site_cache:
            return self._site_cache[url]
        try:
            resp = await client.get(url, headers={"User-Agent": "BlackFoxAgentBot/1.0"})
            if resp.status_code >= 400:
                return ""
            raw = resp.text
        except Exception as exc:
            logger.info("site fetch fail %s: %s", url, exc)
            return ""
        text = _TAG_RE.sub(" ", raw)
        text = _WS_RE.sub(" ", text).strip()
        self._site_cache[url] = text
        return text


def unsure_handoff(lang: str) -> str:
    messages = {
        "fa": (
            f"اطلاعات کافی در دانش فعلی ندارم. لطفاً به اکانت پشتیبانی پیام دهید: {SUPPORT_HANDLE}"
        ),
        "en": (
            f"I don’t have enough confirmed information for that. Please message the support account: {SUPPORT_HANDLE}"
        ),
        "ru": (
            f"Недостаточно подтверждённых данных. Напишите в поддержку: {SUPPORT_HANDLE}"
        ),
        "zh": (
            f"当前没有足够确认信息。请联系支持账号：{SUPPORT_HANDLE}"
        ),
    }
    return messages.get(lang, messages["en"])


def looks_unsure(answer: str) -> bool:
    t = (answer or "").lower()
    markers = (
        "i don't know",
        "i do not know",
        "i'm not sure",
        "i am not sure",
        "not sure",
        "no information",
        "cannot confirm",
        "نمی‌دانم",
        "نمیدانم",
        "اطلاعات کافی",
        "مطمئن نیستم",
        "не знаю",
        "не уверен",
        "不知道",
        "不确定",
        "没有足够",
    )
    return any(m in t for m in markers)
