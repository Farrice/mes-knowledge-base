#!/usr/bin/env python3
"""Compatibility wrapper for the V4 Codex orchestration preflight.

The durable local implementation lives at execution/codex_operator_preflight.py.
This file exists because V4 replay prompts and older Codex guidance reference
.codex/tools/codex_orchestration_preflight.py directly.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]


def _run_preflight(intent: str) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, "execution/codex_operator_preflight.py", intent, "--json"],
        cwd=str(REPO_ROOT),
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        return {
            "schema_version": "codex-orchestration-preflight/v1",
            "error": proc.stderr.strip() or proc.stdout.strip() or "preflight failed",
            "intent_lock": {"raw_intent": intent},
        }
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {
            "schema_version": "codex-orchestration-preflight/v1",
            "error": "preflight returned non-json",
            "stdout": proc.stdout,
            "intent_lock": {"raw_intent": intent},
        }


def _md(payload: dict[str, Any], mode: str) -> str:
    intent = payload.get("intent_lock", {}).get("raw_intent", "")
    chosen = payload.get("chosen_path", {})
    decision = payload.get("execution_decision", {})
    route_candidates = payload.get("route_candidates", [])
    receipt = payload.get("orchestration_receipt", {})
    verification = payload.get("verification_plan", [])
    gates = payload.get("manual_gate_checklist", [])

    lines = [
        "# Context Load Packet",
        "",
        f"Intent: {intent}",
        f"Mode: {mode}",
        f"Owner workflow: /{chosen.get('owner', 'unknown')}",
        f"Execution decision: {decision.get('status', 'unknown')} - {decision.get('reason', '')}",
        "",
        "## Route Proof",
    ]
    if route_candidates:
        for item in route_candidates[:5]:
            lines.append(
                f"- /{item.get('route')}: {item.get('score')} via {item.get('source')} {item.get('matched') or ''}".rstrip()
            )
    else:
        lines.append("- No route candidates returned.")

    lines.extend(["", "## Manual Gates"])
    for gate in gates:
        lines.append(f"- {gate.get('gate')}: {gate.get('status')} - {gate.get('check')}")

    lines.extend(["", "## Verification Plan"])
    for check in verification:
        lines.append(f"- {check}")

    lines.extend(
        [
            "",
            "## Orchestration Receipt Required",
            f"- platform: {receipt.get('platform', 'codex')}",
            f"- workspace: {receipt.get('workspace', str(REPO_ROOT))}",
            "- files_loaded: owner SKILL.md + genius.md + workflow/contract before expert-domain output",
            "- patterns_extracted: concrete mechanics, not expert names",
            "- verifier_results: route, fact/prose as applicable, finalize status",
        ]
    )
    if payload.get("error"):
        lines.extend(["", f"Warning: {payload['error']}"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Codex orchestration preflight compatibility wrapper")
    parser.add_argument("--intent", required=True)
    parser.add_argument("--mode", choices=["deliverable", "system", "research"], default="deliverable")
    parser.add_argument("--format", choices=["md", "json"], default="md")
    args = parser.parse_args()

    payload = _run_preflight(args.intent)
    payload["compat_mode"] = args.mode

    if args.format == "json":
        print(json.dumps(payload, indent=2))
    else:
        print(_md(payload, args.mode), end="")
    return 0 if "error" not in payload else 1


if __name__ == "__main__":
    raise SystemExit(main())
