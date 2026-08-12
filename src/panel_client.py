"""Minimal 3x-ui panel API client for scheduled subscription creation."""

from __future__ import annotations

import secrets
import json
from dataclasses import dataclass
from urllib.parse import quote, urlencode

import httpx


@dataclass(frozen=True, slots=True)
class CreatedSubscription:
    email: str
    sub_id: str
    sub_link: str
    vless_link: str


class PanelAPIError(RuntimeError):
    """Raised when 3x-ui API returns an error."""


class PanelClient:
    """Token-authenticated client for `/panel/api/*` endpoints."""

    def __init__(self, *, base_url: str, api_token: str, timeout_seconds: float = 45.0) -> None:
        normalized = base_url.rstrip("/")
        if normalized.endswith("/panel"):
            normalized = normalized[: -len("/panel")]
        self._base_url = normalized
        self._api_token = api_token.strip()
        self._timeout_seconds = timeout_seconds
        self._headers = {
            "Authorization": f"Bearer {self._api_token}",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/json",
        }

    async def _call(self, method: str, path: str, payload: dict | None = None) -> dict:
        url = f"{self._base_url}{path}"
        async with httpx.AsyncClient(timeout=self._timeout_seconds, verify=False) as client:
            response = await client.request(method, url, headers=self._headers, json=payload)
        if response.status_code >= 400:
            raise PanelAPIError(f"{method} {path} failed: HTTP {response.status_code} {response.text[:180]}")
        data = response.json()
        if not isinstance(data, dict):
            raise PanelAPIError(f"{method} {path} returned invalid JSON object")
        if not data.get("success", False):
            raise PanelAPIError(str(data.get("msg") or f"{method} {path} failed"))
        return data

    async def get_new_uuid(self) -> str:
        data = await self._call("GET", "/panel/api/server/getNewUUID")
        obj = data.get("obj")
        if not isinstance(obj, dict) or not obj.get("uuid"):
            raise PanelAPIError("Panel did not return uuid")
        return str(obj["uuid"])

    async def resolve_inbound_id(self, preferred_id: int, required_port: int = 443) -> int:
        if preferred_id > 0 and required_port <= 0:
            return preferred_id
        data = await self._call("GET", "/panel/api/inbounds/list")
        obj = data.get("obj")
        if not isinstance(obj, list) or not obj:
            raise PanelAPIError("No inbound found in panel")
        if preferred_id > 0:
            for rec in obj:
                if not isinstance(rec, dict):
                    continue
                if int(rec.get("id") or 0) == preferred_id:
                    if required_port > 0 and int(rec.get("port") or 0) != required_port:
                        raise PanelAPIError(
                            f"Preferred inbound {preferred_id} is not on required port {required_port}"
                        )
                    return preferred_id

        candidates: list[dict] = []
        if required_port > 0:
            for rec in obj:
                if isinstance(rec, dict) and rec.get("enable", False) and int(rec.get("port") or 0) == required_port:
                    candidates.append(rec)
        if not candidates:
            candidates = [rec for rec in obj if isinstance(rec, dict) and rec.get("enable", False)] or [
                rec for rec in obj if isinstance(rec, dict)
            ]
        if not candidates:
            raise PanelAPIError("No inbound candidate found")

        # Prefer an inbound that already contains an "agent-bot" example client.
        for rec in candidates:
            for cl in rec.get("clientStats") or []:
                if "agent-bot" in str((cl or {}).get("email", "")).lower() and isinstance(rec.get("id"), int):
                    return int(rec["id"])
        for rec in candidates:
            if isinstance(rec, dict) and rec.get("enable", False) and isinstance(rec.get("id"), int):
                return int(rec["id"])
        first = candidates[0]
        if isinstance(first, dict) and isinstance(first.get("id"), int):
            return int(first["id"])
        raise PanelAPIError("Unable to detect inbound id")

    @staticmethod
    def _parse_json_field(raw: str | dict | None) -> dict:
        if isinstance(raw, dict):
            return raw
        if isinstance(raw, str) and raw.strip():
            try:
                parsed = json.loads(raw)
                if isinstance(parsed, dict):
                    return parsed
            except json.JSONDecodeError:
                return {}
        return {}

    async def _get_inbound(self, inbound_id: int) -> dict:
        data = await self._call("GET", f"/panel/api/inbounds/get/{inbound_id}")
        obj = data.get("obj")
        if not isinstance(obj, dict):
            raise PanelAPIError("Inbound payload is invalid")
        return obj

    def _build_vless_link(self, *, inbound: dict, client_uuid: str, title: str) -> str:
        stream = self._parse_json_field(inbound.get("streamSettings"))
        network = str(stream.get("network") or "tcp")
        security = str(stream.get("security") or "none")
        host = ""
        for ep in stream.get("externalProxy") or []:
            if isinstance(ep, dict) and str(ep.get("dest", "")).strip():
                host = str(ep["dest"]).strip()
                break
        if not host:
            host = "127.0.0.1"

        port = int(inbound.get("port") or 443)
        query: dict[str, str] = {"type": network, "encryption": "none", "security": security}
        if security == "reality":
            rs = self._parse_json_field(stream.get("realitySettings"))
            rs_settings = self._parse_json_field(rs.get("settings"))
            public_key = str(rs_settings.get("publicKey") or "").strip()
            if public_key:
                query["pbk"] = public_key
            fingerprint = str(rs_settings.get("fingerprint") or "").strip() or "chrome"
            query["fp"] = fingerprint
            server_names = rs.get("serverNames") or []
            if isinstance(server_names, list) and server_names:
                query["sni"] = str(server_names[0])
            short_ids = rs.get("shortIds") or []
            if isinstance(short_ids, list) and short_ids:
                query["sid"] = str(short_ids[0])
            spider_x = str(rs_settings.get("spiderX") or "/")
            query["spx"] = spider_x
        if network == "ws":
            ws = self._parse_json_field(stream.get("wsSettings"))
            path = str(ws.get("path") or "/")
            ws_host = str(ws.get("host") or "")
            query["path"] = path
            if ws_host:
                query["host"] = ws_host

        fragment = quote(title, safe="")
        return f"vless://{client_uuid}@{host}:{port}?{urlencode(query)}#{fragment}"

    async def add_client_10gb(
        self,
        *,
        inbound_id: int,
        required_port: int = 443,
        email_prefix: str = "bf-ai-nightly",
    ) -> CreatedSubscription:
        inbound_id = await self.resolve_inbound_id(inbound_id, required_port=required_port)
        uuid = await self.get_new_uuid()
        suffix = secrets.token_hex(3)
        email = f"{email_prefix}-{suffix}"
        sub_id = secrets.token_hex(8)
        total_bytes = 10 * 1024 * 1024 * 1024

        payload = {
            "client": {
                "email": email,
                "id": uuid,
                "uuid": uuid,
                "subId": sub_id,
                "enable": True,
                "expiryTime": 0,
                "totalGB": total_bytes,
                "limitIp": 0,
                "flow": "",
                "comment": "BlackFox AI nightly auto account",
            },
            "inboundIds": [inbound_id],
        }
        try:
            await self._call("POST", "/panel/api/clients/add", payload)
        except PanelAPIError as exc:
            # Older 3x-ui builds use /panel/api/inbounds/addClient with settings JSON string.
            if "HTTP 404" not in str(exc):
                raise
            legacy_payload = {
                "id": inbound_id,
                "settings": json.dumps(
                    {
                        "clients": [
                            {
                                "id": uuid,
                                "email": email,
                                "enable": True,
                                "expiryTime": 0,
                                "totalGB": total_bytes,
                                "limitIp": 0,
                                "flow": "",
                                "subId": sub_id,
                                "reset": 0,
                                "tgId": "",
                            }
                        ]
                    },
                    ensure_ascii=False,
                ),
            }
            await self._call("POST", "/panel/api/inbounds/addClient", legacy_payload)

        sub_link = ""
        try:
            links_data = await self._call("GET", f"/panel/api/clients/subLinks/{sub_id}")
            obj = links_data.get("obj")
            if isinstance(obj, list) and obj:
                sub_link = str(obj[0]).strip()
        except PanelAPIError:
            sub_link = ""
        if not sub_link:
            sub_link = f"{self._base_url}/sub/{sub_id}"
        inbound = await self._get_inbound(inbound_id)
        vless_link = self._build_vless_link(
            inbound=inbound,
            client_uuid=uuid,
            title=f"@BlackFoxVPNN-{email}-🪧",
        )
        return CreatedSubscription(email=email, sub_id=sub_id, sub_link=sub_link, vless_link=vless_link)

