#!/usr/bin/env python3
"""Verify the High-Taste Writing OS bridge and routing integration."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "workflow": ROOT / ".agent" / "workflows" / "high-taste-writing-os.md",
    "codex_skill": ROOT / ".agents" / "skills" / "source-command-high-taste-writing-os" / "SKILL.md",
    "source_command": ROOT / ".claude" / "commands" / "high-taste-writing-os.md",
    "primitive": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "high-taste-writing-os-contract.md",
    "writing_agent": ROOT / "agents" / "writing-agent" / "AGENT.md",
    "writing_workflow": ROOT / ".agent" / "workflows" / "writing-agent.md",
    "copy_agent": ROOT / "agents" / "copywriting-agent" / "AGENT.md",
    "copy_workflow": ROOT / ".agent" / "workflows" / "copywriting-agent.md",
    "publishable_gate": ROOT / ".agent" / "workflows" / "publishable-copy-gate.md",
    "autopilot": ROOT / ".agent" / "workflows" / "autopilot.md",
    "orchestrate": ROOT / ".agent" / "workflows" / "orchestrate.md",
}

WORKFLOW_TERMS = [
    "One composer, many scalpels",
    "Reader Contract",
    "Quality Baseline",
    "Material Ledger",
    "Architecture Map",
    "Composed Draft",
    "Scalpel Passes",
    "Taste Evidence Ledger",
    "No 9+ score without live market/user proof",
]

INTEGRATION_TERMS = [
    "/high-taste-writing-os",
    "Taste Evidence Ledger",
]

ROUTING_QUERIES = [
    "generic flat AI slop poor flow high taste writing",
    "copy is structurally sound but not compelling",
    "make writing agents better high taste perspective shifting content",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def run(args: list[str]) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"{' '.join(args)} failed:\n{result.stdout}")
    return result.stdout


def main() -> int:
    failures: list[str] = []

    for label, path in FILES.items():
        if not path.exists():
            failures.append(f"missing {label}: {path.relative_to(ROOT)}")

    if FILES["workflow"].exists():
        content = read(FILES["workflow"])
        for term in WORKFLOW_TERMS:
            if term not in content:
                failures.append(f"workflow missing term: {term}")

    for label in [
        "writing_agent",
        "writing_workflow",
        "copy_agent",
        "copy_workflow",
        "publishable_gate",
        "autopilot",
        "orchestrate",
    ]:
        if not FILES[label].exists():
            continue
        content = read(FILES[label])
        for term in INTEGRATION_TERMS[:1]:
            if term not in content:
                failures.append(f"{label} missing integration term: {term}")

    combined_skill = read(FILES["codex_skill"]) if FILES["codex_skill"].exists() else ""
    if "generic/flat/AI slop/poorly flowing" not in combined_skill:
        failures.append("codex skill missing user-trigger language")

    for query in ROUTING_QUERIES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        combined = menu + "\n" + router
        if "/high-taste-writing-os" not in combined:
            failures.append(f"routing query did not surface /high-taste-writing-os: {query}")

    if failures:
        print("High-Taste Writing OS verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("High-Taste Writing OS verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
