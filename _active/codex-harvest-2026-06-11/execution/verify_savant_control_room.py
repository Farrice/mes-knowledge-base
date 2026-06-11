#!/usr/bin/env python3
"""Verify the Savant Control Room cockpit."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def run(args: list[str]) -> str:
    completed = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(f"Command failed: {' '.join(args)}\n{completed.stdout}")
    return completed.stdout


def main() -> int:
    raw = run([sys.executable, "execution/savant_control_room.py", "--json"])
    data = json.loads(raw)
    for key in (
        "summary",
        "fast_proof",
        "harness",
        "routing_intelligence",
        "capability_graph",
        "plugin_readiness",
        "recommended_sequence",
        "boundaries",
    ):
        if key not in data:
            raise AssertionError(f"control room missing key: {key}")
    if data["summary"]["overall"] not in {"PASS", "STALE"}:
        raise AssertionError(f"control room overall status was {data['summary']['overall']}")
    if not data["summary"]["safe_to_use"]:
        raise AssertionError("control room says harness is not safe to use")
    if "ai-employee-os" not in data["plugin_readiness"]["scores"]:
        raise AssertionError("control room plugin readiness missing ai-employee-os")

    plain = run([sys.executable, "execution/savant_control_room.py", "--plain"])
    for snippet in (
        "# Savant Control Room",
        "## Fast Proof",
        "## Routing Intelligence",
        "## Recommended Sequence",
        "Global mirror: requires explicit approval",
    ):
        if snippet not in plain:
            raise AssertionError(f"control room plain output missing: {snippet}")

    print("SAVANT CONTROL ROOM VERIFICATION PASS")
    print("- control room JSON is parseable")
    print("- fast proof, routing intelligence, capability, and boundary sections present")
    print("- /ai-employee-os is included in Operator Core readiness scoring")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
