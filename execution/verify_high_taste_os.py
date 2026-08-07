#!/usr/bin/env python3
"""Verify the V4 High-Taste Output OS command surface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "canonical_workflow": ".agent/workflows/high-taste-writing-os.md",
    "alias_workflow": ".agent/workflows/high-taste-os.md",
    "canonical_skill_wrapper": ".agents/skills/source-command-high-taste-writing-os/SKILL.md",
    "alias_skill_wrapper": ".agents/skills/source-command-high-taste-os/SKILL.md",
    "canonical_claude_bridge": ".claude/commands/high-taste-writing-os.md",
    "alias_claude_bridge": ".claude/commands/high-taste-os.md",
    "slash_index": "SLASH_COMMANDS.md",
    "codex_preflight": "execution/codex_operator_preflight.py",
    "compat_preflight": ".codex/tools/codex_orchestration_preflight.py",
    "smoke_artifact": "_active/_archive/2026-08-07-sweep/codex-repeatability/high-taste-os-smoke-practitioner-2026-06-23.md",
}

WORKFLOW_TERMS = [
    "Context Load Packet",
    "V4 golden sample",
    "Reader Contract",
    "Claim/Proof Ledger",
    "Human Wound And Stakes",
    "Taste Evidence Ledger",
    "Orchestration Receipt",
]

ROUTING_QUERIES = [
    "high taste output os remarkable outputs v4 preflight",
    "make this as good as V4 with a remarkable output",
    "consultant-clean flat but structurally sound publish-ready high-taste",
]


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=str(ROOT),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def main() -> int:
    failures: list[str] = []

    for label, rel in REQUIRED_FILES.items():
        if not (ROOT / rel).exists():
            failures.append(f"missing {label}: {rel}")

    workflow = ROOT / ".agent/workflows/high-taste-writing-os.md"
    if workflow.exists():
        content = workflow.read_text(encoding="utf-8", errors="ignore")
        for term in WORKFLOW_TERMS:
            if term not in content:
                failures.append(f"workflow missing term: {term}")

    smoke = ROOT / REQUIRED_FILES["smoke_artifact"]
    if smoke.exists():
        smoke_text = smoke.read_text(encoding="utf-8", errors="ignore")
        for term in (
            "Context Load Packet",
            "Human Wound And Stakes",
            "Taste Evidence Ledger",
            "Orchestration Receipt",
        ):
            if term not in smoke_text:
                failures.append(f"smoke artifact missing term: {term}")

    slash = ROOT / "SLASH_COMMANDS.md"
    if slash.exists():
        text = slash.read_text(encoding="utf-8", errors="ignore")
        for term in ("/high-taste-os", "/high-taste-writing-os", "V4 bar"):
            if term not in text:
                failures.append(f"slash index missing: {term}")

    for query in ROUTING_QUERIES:
        proc = run([sys.executable, "execution/workflow_router.py", "search", query])
        if proc.returncode != 0:
            failures.append(f"workflow_router failed for query: {query}\n{proc.stdout}")
            continue
        first_lines = "\n".join(proc.stdout.splitlines()[:5])
        if "/high-taste-os" not in first_lines and "/high-taste-writing-os" not in first_lines:
            failures.append(f"router did not surface high-taste route near top for: {query}\n{first_lines}")

    binding = run(
        [
            sys.executable,
            "execution/routing_enforcer.py",
            "check",
            "--request",
            "make this as good as V4 with a remarkable output",
            "--workflow",
            "high-taste-writing-os",
        ]
    )
    if binding.returncode != 0:
        failures.append(f"routing_enforcer rejected high-taste-writing-os:\n{binding.stdout}")

    preflight = run(
        [
            sys.executable,
            "execution/codex_operator_preflight.py",
            "generate a remarkable client-facing strategy artifact like V4 high taste output",
            "--json",
        ]
    )
    if preflight.returncode != 0:
        failures.append(f"codex_operator_preflight failed:\n{preflight.stdout}")
    else:
        try:
            payload = json.loads(preflight.stdout)
            owner = payload.get("chosen_path", {}).get("owner")
            if owner not in {"high-taste-writing-os", "high-taste-os"}:
                failures.append(f"preflight chose {owner!r}, expected high-taste-writing-os/high-taste-os")
        except json.JSONDecodeError:
            failures.append(f"codex_operator_preflight returned non-json:\n{preflight.stdout}")

    if failures:
        print("High-Taste OS verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("High-Taste OS verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
