"""API key masking and Fernet encryption for the Agent Registry."""

from __future__ import annotations

import base64
import hashlib
import logging

from cryptography.fernet import Fernet, InvalidToken

logger = logging.getLogger(__name__)


def mask_api_key(raw: str | None) -> str:
    key = (raw or "").strip()
    if not key:
        return "(empty)"
    if len(key) <= 8:
        return "••••" + key[-2:]
    return f"{key[:3]}••••••••••••{key[-4:]}"


def _fernet_from_secret(secret: str) -> Fernet:
    digest = hashlib.sha256(secret.encode("utf-8")).digest()
    return Fernet(base64.urlsafe_b64encode(digest))


def encrypt_secret(plaintext: str, master_secret: str) -> str:
    if not plaintext:
        return ""
    return _fernet_from_secret(master_secret).encrypt(plaintext.encode("utf-8")).decode("ascii")


def decrypt_secret(ciphertext: str, master_secret: str) -> str:
    if not ciphertext:
        return ""
    try:
        return _fernet_from_secret(master_secret).decrypt(ciphertext.encode("ascii")).decode("utf-8")
    except (InvalidToken, ValueError, TypeError) as exc:
        logger.warning("Failed to decrypt agent secret (re-enter key): %s", type(exc).__name__)
        return ""
