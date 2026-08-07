#!/usr/bin/env python3
"""Verify Operator Cockpit V2 behavior."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def run(args: list[str], timeout: int = 90) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )


def main() -> int:
    failures: list[str] = []
    intent = (
        "engineering debt and user failure modes are creating bottlenecks; "
        "rebuild the Codex harness as an operator cockpit without limiting the arsenal"
    )

    raw = run(
        [
            sys.executable,
            "execution/operator_cockpit.py",
            "--intent",
            intent,
            "--json",
            "--no-capture",
        ]
    )
    if raw.returncode != 0:
        failures.append(f"operator cockpit json failed: {raw.stdout[:500]}")
        data = {}
    else:
        data = json.loads(raw.stdout)

    if data:
        packet = data.get("preflight", {}).get("intent_confidence_packet", {})
        decision = data.get("preflight", {}).get("execution_decision", {})
        mirror = data.get("global_mirror_checkpoint", {})
        friction = data.get("friction", {})
        route = packet.get("chosen_route")

        if route != "system-audit":
            failures.append(f"expected /system-audit, got /{route}")
        if "operator_cockpit_rebuild" not in packet.get("non_trivial_reason", []):
            failures.append("missing operator_cockpit_rebuild non-trivial reason")
        if decision.get("status") != "Needs judgment":
            failures.append(f"expected Needs judgment, got {decision.get('status')}")
        if packet.get("questions") == []:
            failures.append("confidence packet should include questions for unresolved cockpit work")
        if "Full intelligence arsenal remains available on demand" not in packet.get("arsenal_policy", ""):
            failures.append("arsenal policy did not preserve on-demand access")
        if mirror.get("status") != "proposal-only":
            failures.append("global mirror checkpoint should remain proposal-only")
        if friction.get("enabled") is not False:
            failures.append("--no-capture should disable friction writes")

    plain = run(
        [
            sys.executable,
            "execution/operator_cockpit.py",
            "--intent",
            intent,
            "--plain",
            "--no-capture",
        ]
    )
    if plain.returncode != 0:
        failures.append(f"operator cockpit plain failed: {plain.stdout[:500]}")
    else:
        for snippet in (
            "# Operator Cockpit V2",
            "## Intent Confidence Packet",
            "## Cockpit Status",
            "## Friction Capture",
            "## Retrieval",
            "## Global Mirror Checkpoint",
        ):
            if snippet not in plain.stdout:
                failures.append(f"plain output missing: {snippet}")

    backlog = run(
        [
            sys.executable,
            "execution/artifact_router.py",
            "backlog-map",
            "--json",
        ],
        timeout=120,
    )
    if backlog.returncode != 0:
        failures.append(f"backlog map generation failed: {backlog.stdout[:500]}")
    else:
        result = json.loads(backlog.stdout)
        if not result.get("map_path") or not Path(result["map_path"]).exists():
            failures.append("backlog map path was not created")
        if not result.get("plan_path") or not Path(result["plan_path"]).exists():
            failures.append("backlog plan path was not created")

    if failures:
        print("OPERATOR COCKPIT VERIFICATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("OPERATOR COCKPIT VERIFICATION PASS")
    print("- confidence packet routes cockpit rebuild pressure to /system-audit")
    print("- unresolved non-trivial cockpit work pauses for judgment")
    print("- arsenal policy preserves on-demand intelligence access")
    print("- global mirror remains proposal-only")
    print("- dated backlog map and staged cleanup plan are generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
