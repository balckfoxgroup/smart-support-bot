"""Control Service: test / activate / failover — independent of any single Agent."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from typing import Any

import aiohttp

from src.config import Settings
from src.control.audit import AuditLog
from src.control.models import AgentRecord
from src.control.registry import AgentRegistry
from src.control.secrets import mask_api_key

logger = logging.getLogger(__name__)

TEST_PROMPT = "Reply with exactly: PONG"


@dataclass(slots=True)
class ChatResult:
    text: str
    agent: AgentRecord
    usage_tokens: int = 0
    spend_usd: float = 0.0
    failed_over: bool = False
    error_class: str = ""


def classify_error(exc: BaseException | str, status: int | None = None) -> str:
    text = str(exc).lower()
    if status == 401 or "401" in text or "unauthorized" in text:
        return "unauthorized"
    if status == 403 or "403" in text or "forbidden" in text:
        return "forbidden"
    if status == 429 or "rate limit" in text or "too many requests" in text:
        return "rate_limit"
    if "timeout" in text or "timed out" in text:
        return "timeout"
    if "token" in text and ("limit" in text or "quota" in text or "exceed" in text):
        return "token_limit"
    if "model" in text and ("not found" in text or "unavailable" in text):
        return "model_unavailable"
    if "network" in text or "dns" in text or "connection" in text:
        return "network_error"
    if status and status >= 500:
        return "provider_error"
    if status and status >= 400:
        return "api_error"
    return "api_error"


class ControlService:
    """Bot Control Layer — always available even when Agents are down."""

    def __init__(
        self,
        settings: Settings,
        registry: AgentRegistry,
        audit: AuditLog,
    ) -> None:
        self.settings = settings
        self.registry = registry
        self.audit = audit
        self._session: aiohttp.ClientSession | None = None

    async def start(self) -> None:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()

    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()
        self._session = None

    def _spend(self, tokens: int) -> float:
        rate = float(self.settings.ai_usd_per_million_tokens)
        return (max(0, tokens) / 1_000_000.0) * rate

    def usage_warning(self, agent: AgentRecord, *, lang: str = "en") -> str | None:
        if agent.budget_usd <= 0:
            return None
        pct = (agent.spend_usd / agent.budget_usd) * 100.0
        fa = (lang or "").startswith("fa")
        if pct >= 100:
            return (
                "🚨 ایجنت در دسترس نیست — در حال سوییچ به پشتیبان"
                if fa
                else "🚨 Agent unavailable — switching to backup"
            )
        if pct >= 80:
            return (
                f"⚠️ مصرف اعتبار ایجنت بالای ۸۰٪ است ({pct:.0f}٪)"
                if fa
                else f"⚠️ Agent token usage is above 80% ({pct:.0f}%)"
            )
        return None

    async def _raw_chat(
        self,
        agent: AgentRecord,
        messages: list[dict[str, Any]],
        *,
        temperature: float | None = None,
        max_tokens: int | None = None,
        timeout_override: float | None = None,
        allow_reasoning_fallback: bool = False,
        _retry_empty: bool = True,
    ) -> tuple[str, int]:
        await self.start()
        assert self._session is not None
        api_key = self.registry.decrypt_key(agent)
        if not api_key:
            raise RuntimeError("API key missing or undecryptable")
        base = agent.api_endpoint.rstrip("/")
        url = f"{base}/chat/completions"
        payload: dict[str, Any] = {
            "model": agent.model,
            "messages": messages,
            "temperature": agent.temperature if temperature is None else temperature,
            "max_tokens": agent.max_tokens if max_tokens is None else max_tokens,
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        total = float(
            timeout_override
            if timeout_override is not None
            else (agent.timeout_seconds or 60)
        )
        # Keep connect/read snappy so failover does not hang for a full minute.
        timeout = aiohttp.ClientTimeout(total=total, connect=min(8.0, total), sock_read=total)
        try:
            async with self._session.post(
                url, json=payload, headers=headers, timeout=timeout
            ) as resp:
                body = await resp.json(content_type=None)
                if resp.status >= 400:
                    detail = body if isinstance(body, dict) else {"raw": str(body)[:200]}
                    err = detail.get("error", detail)
                    raise RuntimeError(f"HTTP {resp.status}: {err}")
        except aiohttp.ClientError as exc:
            raise RuntimeError(f"Network error: {type(exc).__name__}") from exc

        usage_raw = body.get("usage") if isinstance(body, dict) else None
        tokens = 0
        if isinstance(usage_raw, dict):
            tokens = int(usage_raw.get("total_tokens") or 0)
            if not tokens:
                tokens = int(usage_raw.get("prompt_tokens") or 0) + int(
                    usage_raw.get("completion_tokens") or 0
                )

        try:
            message = body["choices"][0]["message"]
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError("Unexpected AI response shape") from exc

        content = message.get("content") if isinstance(message, dict) else None
        if isinstance(content, str) and content.strip():
            return content.strip(), tokens

        reasoning = None
        if isinstance(message, dict):
            reasoning = message.get("reasoning_content") or message.get("reasoning")
        has_reasoning = isinstance(reasoning, str) and bool(reasoning.strip())

        # Connectivity probes may accept any non-empty model output.
        if allow_reasoning_fallback and has_reasoning:
            return reasoning.strip(), tokens

        if has_reasoning:
            from src.ai.persona import salvage_reply_from_reasoning

            salvaged = salvage_reply_from_reasoning(reasoning)
            if salvaged:
                logger.warning(
                    "Control AI empty content; salvaged reply from reasoning agent=%s (%s chars)",
                    agent.name,
                    len(salvaged),
                )
                return salvaged, tokens

        used_max = int(payload.get("max_tokens") or agent.max_tokens or 1024)
        if has_reasoning and _retry_empty and used_max < 8192:
            bump = min(8192, max(used_max * 2, used_max + 2048))
            logger.warning(
                "Control AI empty content with reasoning; retry max_tokens=%s agent=%s",
                bump,
                agent.name,
            )
            retry_messages = list(messages) + [
                {
                    "role": "user",
                    "content": (
                        "IMPORTANT: Put the final Telegram reply in the content field only. "
                        "Do not leave content empty. No chain-of-thought."
                    ),
                }
            ]
            return await self._raw_chat(
                agent,
                retry_messages,
                temperature=temperature,
                max_tokens=bump,
                timeout_override=timeout_override,
                allow_reasoning_fallback=False,
                _retry_empty=False,
            )

        if has_reasoning:
            logger.error(
                "Control AI refused reasoning leak for agent=%s",
                agent.name,
            )
        raise RuntimeError("AI returned empty content")

    async def test_agent(
        self,
        agent_id: str,
        *,
        admin_id: int | None = None,
        lang: str = "en",
    ) -> tuple[bool, str]:
        fa = (lang or "").startswith("fa")
        agent = await self.registry.get_agent(agent_id)
        if not agent:
            return False, ("❌ ایجنت پیدا نشد." if fa else "❌ Agent not found")
        try:
            # Fast connectivity probe — short timeout; enough tokens for reasoning models.
            text, tokens = await self._raw_chat(
                agent,
                [{"role": "user", "content": TEST_PROMPT}],
                max_tokens=min(256, max(64, agent.max_tokens)),
                temperature=0,
                timeout_override=min(18.0, float(agent.timeout_seconds or 60)),
                allow_reasoning_fallback=True,
            )
            await self.registry.record_result(
                agent.id, ok=True, tokens=tokens, spend_usd=self._spend(tokens)
            )
            await self.audit.write(
                "test_agent_ok",
                admin_id=admin_id,
                detail=f"Test OK for {agent.name}",
                meta={"agent_id": agent.id},
            )
            if fa:
                return True, (
                    f"✅ اتصال موفق بود\n"
                    f"نام ایجنت: {agent.name}\n"
                    f"پاسخ تست: {text[:120]}"
                )
            return True, f"✅ Connection successful\nAgent: {agent.name}\nReply: {text[:120]}"
        except Exception as exc:  # noqa: BLE001 — control plane must never crash
            err_class = classify_error(exc)
            safe = re.sub(r"sk-[A-Za-z0-9_-]+", "sk-••••", str(exc))[:200]
            await self.registry.record_result(
                agent.id, ok=False, error=safe, error_class=err_class
            )
            await self.audit.write(
                "test_agent_fail",
                admin_id=admin_id,
                detail=f"Test FAIL for {agent.name}: {err_class}",
                meta={"agent_id": agent.id, "error_class": err_class},
            )
            if fa:
                return False, (
                    f"❌ اتصال ناموفق بود\n"
                    f"علت: {err_class}\n"
                    f"جزئیات: {safe}"
                )
            return False, f"❌ Connection failed\nReason: {err_class}\nDetail: {safe}"

    async def activate_agent(
        self,
        agent_id: str,
        *,
        admin_id: int | None = None,
        require_test: bool = True,
        as_preferred_primary: bool = True,
        lang: str = "en",
    ) -> tuple[bool, str]:
        fa = (lang or "").startswith("fa")
        agent = await self.registry.get_agent(agent_id)
        if not agent:
            return False, ("❌ ایجنت پیدا نشد." if fa else "❌ Agent not found")
        if not agent.enabled:
            return False, ("❌ این ایجنت غیرفعال است." if fa else "❌ Agent is disabled")
        prev = await self.registry.get_active()
        if require_test:
            ok, msg = await self.test_agent(agent_id, admin_id=admin_id, lang=lang)
            if not ok:
                keep = (
                    "ایجنت فعال قبلی بدون تغییر ماند."
                    if fa
                    else "Previous active agent kept."
                )
                return False, f"{msg}\n\n{keep}"
        activated = await self.registry.set_active(
            agent_id, as_preferred_primary=as_preferred_primary
        )
        if not activated:
            return False, (
                "❌ فعال‌سازی ایجنت انجام نشد."
                if fa
                else "❌ Failed to set active agent"
            )
        await self.audit.write(
            "activate_agent",
            admin_id=admin_id,
            detail=(
                f"Admin changed active agent from "
                f"{prev.name if prev else 'none'} to {activated.name}"
            ),
            meta={
                "from": prev.id if prev else None,
                "to": activated.id,
            },
        )
        if fa:
            return True, (
                f"✅ ایجنت با موفقیت فعال شد\n"
                f"ایجنت فعال: {activated.name}"
            )
        return True, f"✅ Agent Activated Successfully\nActive: {activated.name}"

    async def failover_chain(self) -> list[AgentRecord]:
        agents = await self.registry.list_agents()
        return [
            a
            for a in agents
            if a.enabled and a.role in {"primary", "secondary", "backup"}
        ]

    async def chat_with_failover(
        self,
        messages: list[dict[str, Any]],
        *,
        prefer_agent_id: str | None = None,
        allow_failover: bool = True,
        admin_id: int | None = None,
        timeout_override: float | None = None,
        max_tokens_override: int | None = None,
    ) -> ChatResult:
        ordered: list[AgentRecord] = []
        if prefer_agent_id:
            pref = await self.registry.get_agent(prefer_agent_id)
            if pref and pref.enabled:
                ordered.append(pref)
        active = await self.registry.get_active()
        if active and all(a.id != active.id for a in ordered):
            ordered.append(active)
        if allow_failover:
            for a in await self.failover_chain():
                if all(x.id != a.id for x in ordered):
                    warn = self.usage_warning(a)
                    if warn and "unavailable" in warn:
                        continue
                    # Skip agents already known hard-down to avoid long waits
                    if a.status == "down" and a.last_error_class in {
                        "unauthorized",
                        "forbidden",
                        "token_limit",
                        "model_unavailable",
                    }:
                        continue
                    ordered.append(a)

        if not ordered:
            raise RuntimeError("No agents available in registry")

        last_err = "unknown"
        last_class = "api_error"
        for idx, agent in enumerate(ordered):
            try:
                # Prefer a bounded timeout so admin chat stays responsive.
                to = timeout_override
                if to is None:
                    to = min(45.0, float(agent.timeout_seconds or 60))
                text, tokens = await self._raw_chat(
                    agent,
                    messages,
                    timeout_override=to,
                    max_tokens=max_tokens_override,
                )
                spend = self._spend(tokens)
                await self.registry.record_result(
                    agent.id, ok=True, tokens=tokens, spend_usd=spend
                )
                failed_over = idx > 0
                if failed_over:
                    await self.registry.set_active(agent.id, as_preferred_primary=False)
                    await self.audit.write(
                        "failover",
                        admin_id=admin_id,
                        detail=f"Failover activated {agent.name}",
                        meta={"agent_id": agent.id, "reason": last_class},
                    )
                return ChatResult(
                    text=text,
                    agent=agent,
                    usage_tokens=tokens,
                    spend_usd=spend,
                    failed_over=failed_over,
                    error_class="",
                )
            except Exception as exc:  # noqa: BLE001
                last_class = classify_error(exc)
                last_err = re.sub(r"sk-[A-Za-z0-9_-]+", "sk-••••", str(exc))[:200]
                await self.registry.record_result(
                    agent.id, ok=False, error=last_err, error_class=last_class
                )
                if not allow_failover:
                    break
                continue

        raise RuntimeError(f"All agents failed ({last_class}): {last_err}")

    async def return_to_primary(
        self, *, admin_id: int | None = None, lang: str = "en"
    ) -> tuple[bool, str]:
        fa = (lang or "").startswith("fa")
        primary = await self.registry.get_preferred_primary()
        if not primary:
            for a in await self.registry.list_agents():
                if a.role == "primary" and a.enabled:
                    primary = a
                    break
        if not primary:
            return False, (
                "❌ ایجنت اصلی ترجیحی تنظیم نشده است."
                if fa
                else "❌ No preferred primary configured"
            )
        return await self.activate_agent(
            primary.id,
            admin_id=admin_id,
            require_test=True,
            as_preferred_primary=True,
            lang=lang,
        )

    def format_agent_card(self, agent: AgentRecord, *, lang: str = "en") -> str:
        fa = (lang or "").startswith("fa")
        masked = self.registry.mask_key(agent)
        remaining = None
        usage_pct = None
        if agent.budget_usd > 0:
            remaining = max(0.0, agent.budget_usd - agent.spend_usd)
            usage_pct = (agent.spend_usd / agent.budget_usd) * 100.0
        warn = self.usage_warning(agent, lang=lang)
        yes, no_ = ("بله", "خیر") if fa else ("Yes", "No")
        if fa:
            lines = [
                f"🤖 نام ایجنت: {agent.name}",
                f"شناسه: {agent.id}",
                f"ارائه‌دهنده: {agent.provider}",
                f"مدل: {agent.model}",
                f"آدرس API: {agent.api_endpoint}",
                f"وضعیت کلید: {masked}",
                f"مصرف توکن: {agent.total_tokens} توکن (${agent.spend_usd:.4f})",
            ]
            if remaining is not None and usage_pct is not None:
                lines.append(
                    f"اعتبار باقی‌مانده: ${remaining:.4f} ({usage_pct:.0f}٪ مصرف‌شده)"
                )
            lines.extend(
                [
                    f"وضعیت: {agent.status}",
                    f"آخرین اتصال: {agent.last_connection or '-'}",
                    f"آخرین خطا: {agent.last_error or '-'}",
                    f"فعالِ فعلی: {yes if agent.active else no_}",
                    f"فعال‌بودن: {yes if agent.enabled else no_}",
                    f"نقش: {agent.role}",
                    f"اولویت: {agent.priority}",
                    f"دما / سقف توکن: {agent.temperature} / {agent.max_tokens}",
                ]
            )
        else:
            lines = [
                f"🤖 {agent.name}",
                f"ID: {agent.id}",
                f"Provider: {agent.provider}",
                f"Model: {agent.model}",
                f"API Endpoint: {agent.api_endpoint}",
                f"API Key Status: {masked}",
                f"Token Usage: {agent.total_tokens} tokens (${agent.spend_usd:.4f})",
            ]
            if remaining is not None and usage_pct is not None:
                lines.append(f"Remaining Credits: ${remaining:.4f} ({usage_pct:.0f}% used)")
            lines.extend(
                [
                    f"Status: {agent.status}",
                    f"Last Connection: {agent.last_connection or '-'}",
                    f"Last Error: {agent.last_error or '-'}",
                    f"Active: {yes if agent.active else no_}",
                    f"Enabled: {yes if agent.enabled else no_}",
                    f"Role: {agent.role}",
                    f"Priority: {agent.priority}",
                    f"Temp / MaxTokens: {agent.temperature} / {agent.max_tokens}",
                ]
            )
        if warn:
            lines.append(warn)
        return "\n".join(lines)

    def format_control_home(
        self,
        agents: list[AgentRecord],
        active: AgentRecord | None,
        *,
        lang: str = "en",
    ) -> str:
        fa = (lang or "").startswith("fa")
        if fa:
            lines = [
                "🛠 مرکز کنترل ایجنت و API",
                "",
                "این پنل از مدل فعال مستقل است.",
                "حتی اگر ایجنت فعلی قطع باشد می‌توانید ایجنت اضافه یا عوض کنید.",
                "",
            ]
        else:
            lines = [
                "🛠 Change Agent & API — Control Center",
                "",
                "This panel is independent of the active LLM.",
                "You can add/switch agents even if the current Agent is down.",
                "",
            ]
        if active:
            lines.append("—— ایجنت فعال ——" if fa else "—— Active Agent ——")
            lines.append(self.format_agent_card(active, lang=lang))
            lines.append("")
        lines.append(
            f"تعداد ایجنت‌های ثبت‌شده: {len(agents)}"
            if fa
            else f"Registered agents: {len(agents)}"
        )
        for a in agents[:12]:
            flag = "🟢" if a.active else ("⚪" if a.enabled else "⛔")
            lines.append(
                f"{flag} [{a.role}] {a.name} — {a.model} — prio {a.priority} — {a.status}"
            )
        lines.append("")
        lines.append(
            "یک گزینه را از کیبورد انتخاب کنید."
            if fa
            else "Choose an action from the keyboard."
        )
        return "\n".join(lines)
