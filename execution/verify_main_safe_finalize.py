#!/usr/bin/env python3
"""Negative controls for integration-main-safe finalize telemetry."""
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

import chain_runner as cr


def run(root: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(root), *args], check=True,
                   capture_output=True, text=True)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS: {message}")


def main() -> int:
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        run(root, "init", "-b", "main")
        run(root, "config", "user.email", "verify@local")
        run(root, "config", "user.name", "Verifier")
        (root / "README.md").write_text("fixture\n")
        run(root, "add", "README.md")
        run(root, "commit", "-m", "fixture")

        old_root, old_log = cr.PROJECT_ROOT, cr.FINALIZE_RUNTIME_LOG
        try:
            cr.PROJECT_ROOT = root
            cr.FINALIZE_RUNTIME_LOG = root / ".agent" / "finalize-runtime.jsonl"
            check(cr._on_integration_main(), "canonical main checkout selects runtime-only telemetry")
            cr._record_main_runtime_event("test", {"proof": "main stays clean"})
            event = json.loads(cr.FINALIZE_RUNTIME_LOG.read_text().splitlines()[-1])
            check(event["kind"] == "test" and event["proof"] == "main stays clean",
                  "runtime event remains observable in the local ledger")

            run(root, "checkout", "-b", "codex/test-lane")
            check(not cr._on_integration_main(), "authoring lane retains document-update behavior")
        finally:
            cr.PROJECT_ROOT, cr.FINALIZE_RUNTIME_LOG = old_root, old_log

    print("PASS: main-safe finalize suite")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
