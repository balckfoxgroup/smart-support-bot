"""Runtime gates — discovers sealed checker by marker (no fixed module path)."""

from __future__ import annotations

import importlib.util
import logging
import sys
from pathlib import Path
from types import ModuleType

logger = logging.getLogger(__name__)

_MARKER = "TITIL_SEAL_V1"


def _discover(project_root: Path) -> ModuleType:
    root = project_root / "src"
    for path in sorted(root.rglob("*.py")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if _MARKER not in text:
            continue
        spec = importlib.util.spec_from_file_location("_runtime_seal_mod", path)
        if spec is None or spec.loader is None:
            continue
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if not hasattr(mod, "primary") or not hasattr(mod, "start_secondary_thread"):
            continue
        return mod
    logger.error("sealed runtime module missing")
    sys.exit(19)


def run_titil_gate(*, project_root: Path, knowledge_root: Path, data_dir: Path) -> None:
    """Delegate integrity operations to the discovered sealed module."""
    mod = _discover(project_root)
    flag = data_dir / ".runtime" / "tz.ok"
    mod.primary(knowledge_root=knowledge_root, flag_path=flag)
    mod.start_secondary_thread(knowledge_root=knowledge_root, flag_path=flag)
