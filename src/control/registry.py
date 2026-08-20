"""Persistent Agent + API Registry (independent of active LLM)."""

from __future__ import annotations

import asyncio
import json
import logging
from copy import deepcopy
from pathlib import Path
from typing import Any

from src.config import Settings
from src.control.models import AgentRecord, ApiProviderRecord, _utcnow, new_id
from src.control.secrets import decrypt_secret, encrypt_secret, mask_api_key

logger = logging.getLogger(__name__)


class AgentRegistry:
    """JSON-backed registry under data/agent_registry.json."""

    def __init__(self, path: Path, *, master_secret: str) -> None:
        self.path = path
        self._master = master_secret
        self._lock = asyncio.Lock()
        self._data: dict[str, Any] = {
            "agents": {},
            "apis": {},
            "active_agent_id": None,
            "preferred_primary_id": None,
            "admin_sessions": {},
            "version": 1,
        }
        self._load()

    def _load(self) -> None:
        if not self.path.is_file():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self._save_sync()
            return
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                self._data.update(raw)
                self._data.setdefault("agents", {})
                self._data.setdefault("apis", {})
                self._data.setdefault("admin_sessions", {})
        except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
            logger.warning("agent_registry.json unreadable (%s); starting fresh", exc)

    def _save_sync(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(self._data, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(self.path)

    def bootstrap_from_settings(self, settings: Settings) -> bool:
        """Seed Primary from .env if registry empty. Returns True if seeded."""
        agents = self._data.get("agents") or {}
        if agents:
            return False
        agent = AgentRecord(
            id=new_id("agt"),
            name=f"Env Primary ({settings.ai_model})",
            provider="openai-compatible",
            model=settings.ai_model,
            api_endpoint=settings.ai_base_url.rstrip("/"),
            api_key_enc=encrypt_secret(settings.ai_api_key, self._master),
            system_prompt="",
            max_tokens=settings.ai_max_tokens,
            temperature=settings.ai_temperature,
            timeout_seconds=settings.ai_timeout_seconds,
            retry_count=2,
            priority=10,
            role="primary",
            enabled=True,
            active=True,
            status="unknown",
            budget_usd=float(settings.ai_budget_usd),
        )
        self._data["agents"] = {agent.id: agent.to_storage()}
        self._data["active_agent_id"] = agent.id
        self._data["preferred_primary_id"] = agent.id
        api = ApiProviderRecord(
            id=new_id("api"),
            provider_name="Env Primary API",
            api_endpoint=settings.ai_base_url.rstrip("/"),
            api_key_enc=encrypt_secret(settings.ai_api_key, self._master),
            model=settings.ai_model,
            status="unknown",
            priority=10,
            enabled=True,
        )
        self._data["apis"] = {api.id: api.to_storage()}
        self._save_sync()
        return True

    def _agent(self, agent_id: str) -> AgentRecord | None:
        raw = (self._data.get("agents") or {}).get(agent_id)
        if not isinstance(raw, dict):
            return None
        return AgentRecord.from_storage(raw)

    def _put_agent(self, agent: AgentRecord) -> None:
        agents = self._data.setdefault("agents", {})
        agent.updated_at = _utcnow()
        agents[agent.id] = agent.to_storage()

    async def list_agents(self) -> list[AgentRecord]:
        async with self._lock:
            items = [AgentRecord.from_storage(v) for v in (self._data.get("agents") or {}).values()]
            items.sort(key=lambda a: (a.priority, a.name.lower()))
            return items

    async def get_agent(self, agent_id: str) -> AgentRecord | None:
        async with self._lock:
            return self._agent(agent_id)

    async def get_active(self) -> AgentRecord | None:
        async with self._lock:
            aid = self._data.get("active_agent_id")
            if aid:
                a = self._agent(str(aid))
                if a and a.enabled:
                    return a
            # Fallback: lowest priority enabled non-support
            candidates = [
                AgentRecord.from_storage(v)
                for v in (self._data.get("agents") or {}).values()
                if isinstance(v, dict)
            ]
            candidates = [c for c in candidates if c.enabled and c.role != "support"]
            candidates.sort(key=lambda a: a.priority)
            return candidates[0] if candidates else None

    async def get_preferred_primary(self) -> AgentRecord | None:
        async with self._lock:
            pid = self._data.get("preferred_primary_id")
            if pid:
                return self._agent(str(pid))
            return None

    def decrypt_key(self, agent: AgentRecord) -> str:
        # Works for persisted and ephemeral AgentRecord (uses api_key_enc field).
        return decrypt_secret(agent.api_key_enc, self._master)

    def mask_key(self, agent: AgentRecord) -> str:
        return mask_api_key(self.decrypt_key(agent))

    async def add_agent(
        self,
        *,
        name: str,
        provider: str,
        model: str,
        api_endpoint: str,
        api_key: str,
        system_prompt: str = "",
        max_tokens: int = 2048,
        temperature: float = 0.4,
        timeout_seconds: float = 45.0,
        retry_count: int = 1,
        priority: int = 100,
        role: str = "secondary",
        budget_usd: float = 0.0,
    ) -> AgentRecord:
        async with self._lock:
            agent = AgentRecord(
                id=new_id("agt"),
                name=name.strip() or "Unnamed Agent",
                provider=provider.strip() or "openai-compatible",
                model=model.strip(),
                api_endpoint=api_endpoint.rstrip("/"),
                api_key_enc=encrypt_secret(api_key.strip(), self._master),
                system_prompt=system_prompt,
                max_tokens=int(max_tokens),
                temperature=float(temperature),
                timeout_seconds=float(timeout_seconds),
                retry_count=int(retry_count),
                priority=int(priority),
                role=role if role in {"primary", "secondary", "backup", "support"} else "secondary",
                enabled=True,
                active=False,
                budget_usd=float(budget_usd or 0.0),
            )
            self._put_agent(agent)
            self._save_sync()
            return agent

    async def update_agent(self, agent_id: str, **fields: Any) -> AgentRecord | None:
        async with self._lock:
            agent = self._agent(agent_id)
            if not agent:
                return None
            if "api_key" in fields:
                key = str(fields.pop("api_key") or "").strip()
                if key:
                    agent.api_key_enc = encrypt_secret(key, self._master)
            for k, v in fields.items():
                if hasattr(agent, k) and k not in {"id", "api_key_enc", "created_at"}:
                    setattr(agent, k, v)
            if "api_endpoint" in fields and fields["api_endpoint"]:
                agent.api_endpoint = str(fields["api_endpoint"]).rstrip("/")
            self._put_agent(agent)
            self._save_sync()
            return agent

    async def delete_agent(self, agent_id: str) -> bool:
        async with self._lock:
            agents = self._data.setdefault("agents", {})
            if agent_id not in agents:
                return False
            del agents[agent_id]
            if self._data.get("active_agent_id") == agent_id:
                self._data["active_agent_id"] = None
            if self._data.get("preferred_primary_id") == agent_id:
                self._data["preferred_primary_id"] = None
            self._save_sync()
            return True

    async def set_active(self, agent_id: str, *, as_preferred_primary: bool = False) -> AgentRecord | None:
        async with self._lock:
            agent = self._agent(agent_id)
            if not agent or not agent.enabled:
                return None
            for raw in (self._data.get("agents") or {}).values():
                if isinstance(raw, dict):
                    raw["active"] = False
            agent.active = True
            agent.status = agent.status if agent.status != "down" else "healthy"
            self._put_agent(agent)
            self._data["active_agent_id"] = agent.id
            if as_preferred_primary or agent.role == "primary":
                self._data["preferred_primary_id"] = agent.id
            self._save_sync()
            return agent

    async def record_result(
        self,
        agent_id: str,
        *,
        ok: bool,
        error: str = "",
        error_class: str = "",
        tokens: int = 0,
        spend_usd: float = 0.0,
    ) -> None:
        async with self._lock:
            agent = self._agent(agent_id)
            if not agent:
                return
            agent.total_requests += 1
            if ok:
                agent.success_count += 1
                agent.status = "healthy"
                agent.last_connection = _utcnow()
                agent.last_error = ""
                agent.last_error_class = ""
            else:
                agent.error_count += 1
                agent.status = "down" if error_class in {
                    "unauthorized",
                    "forbidden",
                    "token_limit",
                    "model_unavailable",
                } else "degraded"
                agent.last_error = (error or "")[:300]
                agent.last_error_class = error_class
            agent.total_tokens += max(0, tokens)
            agent.spend_usd += max(0.0, spend_usd)
            self._put_agent(agent)
            self._save_sync()

    # --- API providers ---

    async def list_apis(self) -> list[ApiProviderRecord]:
        async with self._lock:
            items = [
                ApiProviderRecord.from_storage(v)
                for v in (self._data.get("apis") or {}).values()
                if isinstance(v, dict)
            ]
            items.sort(key=lambda a: (a.priority, a.provider_name.lower()))
            return items

    async def get_api(self, api_id: str) -> ApiProviderRecord | None:
        async with self._lock:
            raw = (self._data.get("apis") or {}).get(api_id)
            if not isinstance(raw, dict):
                return None
            return ApiProviderRecord.from_storage(raw)

    def decrypt_api_key(self, api: ApiProviderRecord) -> str:
        return decrypt_secret(api.api_key_enc, self._master)

    async def add_api(
        self,
        *,
        provider_name: str,
        api_endpoint: str,
        api_key: str,
        model: str = "",
        priority: int = 100,
    ) -> ApiProviderRecord:
        async with self._lock:
            api = ApiProviderRecord(
                id=new_id("api"),
                provider_name=provider_name.strip() or "API",
                api_endpoint=api_endpoint.rstrip("/"),
                api_key_enc=encrypt_secret(api_key.strip(), self._master),
                model=model.strip(),
                priority=int(priority),
                enabled=True,
                status="unknown",
            )
            apis = self._data.setdefault("apis", {})
            apis[api.id] = api.to_storage()
            self._save_sync()
            return api

    async def update_api(self, api_id: str, **fields: Any) -> ApiProviderRecord | None:
        async with self._lock:
            raw = (self._data.get("apis") or {}).get(api_id)
            if not isinstance(raw, dict):
                return None
            api = ApiProviderRecord.from_storage(raw)
            if "api_key" in fields:
                key = str(fields.pop("api_key") or "").strip()
                if key:
                    api.api_key_enc = encrypt_secret(key, self._master)
            for k, v in fields.items():
                if hasattr(api, k) and k not in {"id", "api_key_enc", "created_at"}:
                    setattr(api, k, v)
            api.updated_at = _utcnow()
            self._data["apis"][api.id] = api.to_storage()
            self._save_sync()
            return api

    async def delete_api(self, api_id: str) -> bool:
        async with self._lock:
            apis = self._data.setdefault("apis", {})
            if api_id not in apis:
                return False
            del apis[api_id]
            self._save_sync()
            return True

    # --- Admin UI session (FSM-like persistence without depending on LLM) ---

    async def get_session(self, admin_id: int) -> dict[str, Any]:
        async with self._lock:
            sess = (self._data.get("admin_sessions") or {}).get(str(admin_id))
            return deepcopy(sess) if isinstance(sess, dict) else {}

    async def set_session(self, admin_id: int, session: dict[str, Any]) -> None:
        async with self._lock:
            sessions = self._data.setdefault("admin_sessions", {})
            # Never persist raw API keys in session drafts longer than needed —
            # caller should clear after save. Still scrub known secret fields on write.
            clean = deepcopy(session)
            for k in list(clean.keys()):
                if "key" in k.lower() and k not in {"api_key_draft"}:
                    # keep api_key_draft only while adding; wipe others
                    if k != "api_key_draft":
                        clean.pop(k, None)
            sessions[str(admin_id)] = clean
            self._save_sync()

    async def clear_session(self, admin_id: int) -> None:
        async with self._lock:
            sessions = self._data.setdefault("admin_sessions", {})
            sessions.pop(str(admin_id), None)
            self._save_sync()
