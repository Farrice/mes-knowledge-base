#!/usr/bin/env python3
"""Verify execution-bias and subagent approval boundaries."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8").lower()


def require_text(path: str, needles: list[str]) -> None:
    text = read(path)
    missing = [needle for needle in needles if needle.lower() not in text]
    if missing:
        fail(f"{path} missing boundary language: {', '.join(missing)}")


def preflight(query: str) -> dict:
    proc = run([sys.executable, "execution/codex_operator_preflight.py", query, "--json"])
    if proc.returncode != 0:
        fail(f"preflight failed for {query!r}: {proc.stderr.strip()}")
    return json.loads(proc.stdout)


def check_boundary_language() -> None:
    require_text(
        ".agent/workflows/system-audit.md",
        ["execution bias", "read-only diagnostics", "main thread owns"],
    )
    require_text(
        ".agent/workflows/mission.md",
        ["targeted read-only parallelism", "explicitly asks for parallel agents"],
    )
    require_text(
        ".agent/workflows/autopilot.md",
        [
            "explicit run-specific authorization",
            "read-only diagnostics",
            "no further subagents",
            "main thread owns",
            "add to fan-out list only if farrice has explicitly authorized",
            "run the research angles sequentially in the main thread",
            "worker count, read-only scope, deny list, halt condition, and no further subagents",
        ],
    )
    require_text(
        ".agent/workflows/orchestrate.md",
        ["real codex subagents require explicit authorization"],
    )
    require_text(
        ".agent/workflows/expert-composition-governor.md",
        ["do not spawn real codex subagents unless explicitly authorized"],
    )
    require_text(
        "execution/codex_operator_preflight.py",
        ["subagent_approval_packet_present", "real subagents", "read-only diagnostic subagents"],
    )
    require_text(
        "execution/run_receipt.py",
        ["subagents_requested", "subagent_boundary"],
    )


def check_unapproved_subagents_block() -> None:
    for query in (
        "spawn subagent for this execution bias repair",
        "execution bias repair with parallel agents",
        "delegate to agents for not firing harness repair",
    ):
        data = preflight(query)
        if data["chosen_path"]["owner"] != "system-audit":
            fail(f"{query!r} should route to /system-audit, got /{data['chosen_path']['owner']}")
        if "real subagents" not in data["intent_lock"]["risk_reasons"]:
            fail(f"{query!r} did not flag real subagents risk")
        if data["execution_decision"]["status"] != "Blocked":
            fail(f"{query!r} should be blocked, got {data['execution_decision']['status']}")
        gates = json.dumps(data["manual_gate_checklist"]).lower()
        if "human approval" not in gates or "real subagents" not in gates:
            fail(f"{query!r} missing human approval gate for real subagents")


def check_approved_read_only_subagents_run() -> None:
    query = (
        "execution bias repair authorize read-only diagnostic subagents worker count 2 "
        "scope route probes and verifier review deny list file edits and network writes "
        "halt condition failed verifier no further subagents"
    )
    data = preflight(query)
    if data["chosen_path"]["owner"] != "system-audit":
        fail(f"approved diagnostic query should route to /system-audit, got /{data['chosen_path']['owner']}")
    if "real subagents" in data["intent_lock"]["risk_reasons"]:
        fail("approved diagnostic query still flagged real subagents")
    if data["execution_decision"]["status"] != "Run Locally":
        fail(f"approved diagnostic query should run locally, got {data['execution_decision']['status']}")
    policy = data["local_next_action"]["subagent_policy"].lower()
    if "read-only diagnostic subagents" not in policy or "main thread" not in policy:
        fail("approved diagnostic query missing read-only/main-thread subagent policy")


def check_receipt_boundary() -> None:
    proc = run([sys.executable, "execution/run_receipt.py", "--verify"])
    if proc.returncode != 0:
        fail(f"run receipt verification failed: {proc.stdout or proc.stderr}")


def main() -> int:
    checks = [
        check_boundary_language,
        check_unapproved_subagents_block,
        check_approved_read_only_subagents_run,
        check_receipt_boundary,
    ]
    failures: list[str] = []
    for check in checks:
        try:
            check()
        except Exception as exc:  # noqa: BLE001 - verifier reports all failures.
            failures.append(f"{check.__name__}: {exc}")
    if failures:
        print("SUBAGENT APPROVAL LANGUAGE VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("SUBAGENT APPROVAL LANGUAGE VERIFICATION PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
