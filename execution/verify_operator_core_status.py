#!/usr/bin/env python3
"""Verify the compact Operator Core status dashboard."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXPECTED_ROUTES = (
    "autopilot",
    "orchestrate",
    "end-session",
    "health-check",
    "routing-intelligence",
    "knowledge-librarian",
    "self-evolve",
    "skill-anneal",
    "source-to-skill-system",
    "system-audit",
    "repeatability-spine",
    "expert-composition-governor",
    "extraction-governor-agent",
    "ai-employee-os",
)


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
    raw = run([sys.executable, "execution/operator_core_status.py", "--json", "--strict"])
    data = json.loads(raw)
    if data["summary"]["status"] != "PASS":
        raise AssertionError(f"dashboard status was {data['summary']['status']}")
    routes = tuple(surface["route"] for surface in data["surfaces"])
    if routes != EXPECTED_ROUTES:
        raise AssertionError(f"dashboard routes mismatch: {routes}")
    for surface in data["surfaces"]:
        if surface["sync"]["status"] != "PASS":
            raise AssertionError(f"sync failed for /{surface['route']}")
        if surface["verifier"]["status"] != "PASS":
            raise AssertionError(f"verifier failed for /{surface['route']}")
        if not all(surface["wrappers"].values()):
            raise AssertionError(f"missing wrapper for /{surface['route']}: {surface['missing']}")

    plain = run([sys.executable, "execution/operator_core_status.py", "--plain"])
    for snippet in (
        "# Operator Core Status",
        "Overall: PASS",
        "/autopilot",
        "/orchestrate",
        "/end-session",
        "/health-check",
        "/routing-intelligence",
        "/knowledge-librarian",
        "/self-evolve",
        "/skill-anneal",
        "/source-to-skill-system",
        "/system-audit",
        "/repeatability-spine",
        "/expert-composition-governor",
        "/extraction-governor-agent",
        "/ai-employee-os",
        "Aligned: 14/14",
        "Next audit candidate: /excellence-evaluation-lab",
    ):
        if snippet not in plain:
            raise AssertionError(f"plain dashboard missing: {snippet}")

    print("OPERATOR CORE STATUS VERIFICATION PASS")
    print("- dashboard JSON strict pass")
    print("- plain dashboard contains all aligned surfaces")
    print("- next audit candidate is /excellence-evaluation-lab")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
