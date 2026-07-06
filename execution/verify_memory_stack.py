#!/usr/bin/env python3
"""Verify the interpreter and memory-stack runtime deps are correctly pinned.

Wave 1 (interpreter pinning): hooks and scripts were quietly falling back to
whatever `python3` resolved on PATH instead of the project `.venv`, so a
missing `google-genai` (used by memory/embedding paths) or `PyYAML` would
fail silently in one shell and not another. This verifier is the cheap,
deterministic check that the *active* interpreter has what memory_facade.py
and its dependents actually need, then exercises memory_facade.py itself
with a trivial query to confirm the facade runs end-to-end.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEMORY_FACADE = ROOT / "execution" / "memory_facade.py"


def fail(message: str) -> int:
    print("MEMORY STACK VERIFICATION FAIL")
    print(f"- {message}")
    return 1


def check_genai_import() -> str:
    import google.genai  # noqa: F401

    return "google.genai import ok"


def check_yaml_import() -> str:
    import yaml  # noqa: F401

    return "yaml import ok"


def check_memory_facade_smoke() -> str:
    if not MEMORY_FACADE.exists():
        raise RuntimeError(f"missing {MEMORY_FACADE}")

    proc = subprocess.run(
        [sys.executable, str(MEMORY_FACADE), "verify memory stack smoke test", "--top", "1", "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=30,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"memory_facade.py exited {proc.returncode}: {(proc.stderr or proc.stdout).strip()[:300]}"
        )
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"memory_facade.py did not emit valid JSON: {exc}") from exc

    if "result_count" not in payload or "by_source" not in payload:
        raise RuntimeError(f"memory_facade.py JSON missing expected keys: {sorted(payload.keys())}")

    return f"memory_facade.py smoke call ok (result_count={payload['result_count']})"


def main() -> int:
    print(f"sys.executable: {sys.executable}")

    checks = [
        ("genai_import", check_genai_import),
        ("yaml_import", check_yaml_import),
        ("memory_facade_smoke", check_memory_facade_smoke),
    ]

    receipts: list[str] = []
    for name, func in checks:
        try:
            receipts.append(f"{name}: {func()}")
        except Exception as exc:  # noqa: BLE001 - verifier aggregates a clear failure reason.
            return fail(f"{name}: {exc}")

    print("MEMORY STACK VERIFICATION PASS")
    for receipt in receipts:
        print(f"- {receipt}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
