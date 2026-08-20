"""Data models for Agent Registry / API Management."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


def _utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def new_id(prefix: str = "agt") -> str:
    return f"{prefix}_{uuid4().hex[:12]}"


@dataclass
class AgentRecord:
    id: str
    name: str
    provider: str
    model: str
    api_endpoint: str
    api_key_enc: str = ""
    system_prompt: str = ""
    max_tokens: int = 2048
    temperature: float = 0.4
    timeout_seconds: float = 45.0
    retry_count: int = 1
    priority: int = 100  # lower = higher priority
    role: str = "primary"  # primary | secondary | backup | support
    enabled: bool = True
    active: bool = False
    status: str = "unknown"  # unknown | healthy | degraded | down
    last_connection: str = ""
    last_error: str = ""
    last_error_class: str = ""
    total_requests: int = 0
    error_count: int = 0
    success_count: int = 0
    total_tokens: int = 0
    spend_usd: float = 0.0
    budget_usd: float = 0.0
    created_at: str = field(default_factory=_utcnow)
    updated_at: str = field(default_factory=_utcnow)

    def to_public_dict(self, *, masked_key: str) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "provider": self.provider,
            "model": self.model,
            "api_endpoint": self.api_endpoint,
            "api_key_status": masked_key,
            "system_prompt_chars": len(self.system_prompt or ""),
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "timeout_seconds": self.timeout_seconds,
            "retry_count": self.retry_count,
            "priority": self.priority,
            "role": self.role,
            "enabled": self.enabled,
            "active": self.active,
            "status": self.status,
            "last_connection": self.last_connection or "-",
            "last_error": self.last_error or "-",
            "total_requests": self.total_requests,
            "error_count": self.error_count,
            "success_count": self.success_count,
            "total_tokens": self.total_tokens,
            "spend_usd": round(self.spend_usd, 4),
            "budget_usd": self.budget_usd,
        }

    def to_storage(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_storage(cls, raw: dict[str, Any]) -> AgentRecord:
        known = set(cls.__dataclass_fields__)
        data = {k: v for k, v in raw.items() if k in known}
        return cls(**data)  # type: ignore[arg-type]


@dataclass
class ApiProviderRecord:
    id: str
    provider_name: str
    api_endpoint: str
    api_key_enc: str = ""
    model: str = ""
    status: str = "unknown"
    priority: int = 100
    enabled: bool = True
    usage_tokens: int = 0
    error_count: int = 0
    last_successful_request: str = ""
    created_at: str = field(default_factory=_utcnow)
    updated_at: str = field(default_factory=_utcnow)

    def to_storage(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_storage(cls, raw: dict[str, Any]) -> ApiProviderRecord:
        known = set(cls.__dataclass_fields__)
        data = {k: v for k, v in raw.items() if k in known}
        return cls(**data)  # type: ignore[arg-type]
