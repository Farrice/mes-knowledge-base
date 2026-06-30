#!/usr/bin/env python3
"""Verify plugin readiness can run in stdout/read-only mode."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "deliverables" / "plugin-readiness"


def snapshot() -> set[str]:
    if not OUTPUT_DIR.exists():
        return set()
    return {str(path.relative_to(ROOT)) for path in OUTPUT_DIR.rglob("*") if path.is_file()}


def main() -> int:
    before = snapshot()
    result = subprocess.run(
        [sys.executable, "execution/plugin_readiness_audit.py", "--stdout", "--all-bundles"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stdout)
    after = snapshot()
    if before != after:
        created = sorted(after - before)
        raise AssertionError("stdout mode created files: " + ", ".join(created))
    if "Scorecard write skipped" not in result.stdout:
        raise AssertionError("stdout mode did not confirm skipped write")
    print("PLUGIN READINESS STDOUT VERIFICATION PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
