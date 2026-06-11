#!/usr/bin/env python3
"""Audit Codex command bridge coverage for the Perception Engineering stack."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

COMMANDS = [
    "psychological-brand-strategy-blueprint",
    "behavioral-value-offer-architecture",
    "psychological-conversion-funnel-design",
    "alchemy-content-relationship-engine",
    "high-stakes-persuasion-copy-protocol",
    "reverse-benchmarking-audit",
    "perception-metric-reframe",
    "asymmetric-bet-evaluator",
    "conspiratorial-reframe-engine",
    "perception-dopamine-engine",
    "insight-perception-sprint",
    "positioning-perception-siege",
    "addictive-perception-content",
    "consumer-perception-alchemy",
    "perception-dominance-campaign",
    "blind-spot-social-engine",
    "behavioral-copy-audit",
    "perception-engineering-productize",
]


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=30,
    )


def check_path(path: Path, label: str, failures: list[str]) -> None:
    if path.exists():
        print(f"ok: {label} -> {path.relative_to(ROOT)}")
        return
    print(f"FAIL: {label} missing -> {path.relative_to(ROOT)}")
    failures.append(f"{label} missing for {path}")


def check_skill_points_to_workflow(command: str, failures: list[str]) -> None:
    skill_path = ROOT / ".agents" / "skills" / f"source-command-{command}" / "SKILL.md"
    if not skill_path.exists():
        return
    content = skill_path.read_text(encoding="utf-8", errors="ignore")
    expected = f".agent/workflows/{command}.md"
    if expected in content:
        print(f"ok: skill route -> {command}")
        return
    print(f"FAIL: skill route missing {expected} -> {skill_path.relative_to(ROOT)}")
    failures.append(f"skill route missing for {command}")


def check_command_menu_show(command: str, failures: list[str]) -> None:
    proc = run(["execution/command_menu.py", "show", command])
    output = proc.stdout + proc.stderr
    if proc.returncode != 0:
        print(f"FAIL: command_menu show failed -> {command}")
        failures.append(f"command_menu show failed for {command}")
        return
    if "Source command: missing" in output or "Codex skill: missing" in output:
        print(f"FAIL: command_menu bridge incomplete -> {command}")
        failures.append(f"command_menu bridge incomplete for {command}")
        return
    print(f"ok: command_menu bridge -> {command}")


def check_search(query: str, expected: str, failures: list[str]) -> None:
    proc = run(["execution/command_menu.py", "search", query])
    output = proc.stdout + proc.stderr
    if proc.returncode != 0:
        print(f"FAIL: command_menu search failed -> {query}")
        failures.append(f"command_menu search failed for {query}")
        return
    if f"/{expected}" not in output:
        print(f"FAIL: search did not surface /{expected} -> {query}")
        failures.append(f"search did not surface {expected}")
        return
    print(f"ok: search surfaces /{expected}")


def main() -> int:
    failures: list[str] = []

    print("# Perception Engineering Bridge Audit")
    for command in COMMANDS:
        print(f"\n## /{command}")
        check_path(ROOT / ".agent" / "workflows" / f"{command}.md", "workflow", failures)
        check_path(ROOT / ".claude" / "commands" / f"{command}.md", "source command", failures)
        check_path(
            ROOT / ".agents" / "skills" / f"source-command-{command}" / "SKILL.md",
            "codex command skill",
            failures,
        )
        check_skill_points_to_workflow(command, failures)
        check_command_menu_show(command, failures)

    print("\n## Search")
    check_search(
        "perception engineering productize product ladder prompt pack playbook intensive",
        "perception-engineering-productize",
        failures,
    )
    check_search(
        "behavioral copy audit perception dominance blind spot social engine",
        "behavioral-copy-audit",
        failures,
    )
    check_search(
        "psychological brand strategy behavioral value offer conversion funnel alchemy content relationship high stakes persuasion asymmetric bet conspiratorial reframe",
        "psychological-brand-strategy-blueprint",
        failures,
    )

    if failures:
        print("\nFAILURES")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\noverall: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
