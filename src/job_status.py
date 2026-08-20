"""Lightweight job status markers for health reports."""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def _path(data_dir: Path) -> Path:
    return data_dir / "job_status.json"


def read_job_status(data_dir: Path) -> dict[str, Any]:
    path = _path(data_dir)
    if not path.is_file():
        return {}
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        return raw if isinstance(raw, dict) else {}
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return {}


def record_job(
    data_dir: Path,
    name: str,
    *,
    ok: bool,
    detail: str = "",
) -> None:
    path = _path(data_dir)
    data = read_job_status(data_dir)
    data[name] = {
        "ok": bool(ok),
        "detail": (detail or "")[:500],
        "ts": time.time(),
    }
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(path)
    except OSError as exc:
        logger.warning("job_status write failed: %s", exc)
