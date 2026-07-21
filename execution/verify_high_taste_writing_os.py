#!/usr/bin/env python3
"""Verify the High-Taste Writing OS bridge and routing integration."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# NOTE (2026-07-21): fork-era operator agents (agents/writing-agent,
# agents/copywriting-agent + their workflows) were deliberately NOT installed
# on the canonical repo (765e9db12 restored only operator-autopilot; Farrice
# 2026-06-30 "canonical-fit, retire the sprawl"). Pins updated to the files
# that carry the behavior here.
FILES = {
    "workflow": ROOT / ".agent" / "workflows" / "high-taste-writing-os.md",
    "codex_skill": ROOT / ".agents" / "skills" / "source-command-high-taste-writing-os" / "SKILL.md",
    "source_command": ROOT / ".claude" / "commands" / "high-taste-writing-os.md",
    "primitive": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "high-taste-writing-os-contract.md",
    "publishable_gate": ROOT / ".agent" / "workflows" / "publishable-copy-gate.md",
    "orchestrate": ROOT / ".agent" / "workflows" / "orchestrate.md",
}

# Anchors track the V4 rewrite's stable headings/rules, not old prose:
# composer ownership, reader contract, golden-sample baseline, proof ledger,
# architecture map, single compose pass, bounded support lanes, taste
# evidence, and the no-unproven-9+ rule.
WORKFLOW_TERMS = [
    "One composer",
    "Reader Contract",
    "Golden Standard",
    "Proof Ledger",
    "Architecture Map",
    "Compose Once",
    "Bounded Support Lanes",
    "Taste Evidence Ledger",
    "No 9+",
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

    # Integration surface after the deliberate autopilot rewrite: autopilot is
    # a thin front door; the high-taste wrap binding lives in the publishable
    # copy gate ("wrap the owner with /high-taste-writing-os") and orchestrate.
    for label in [
        "publishable_gate",
        "orchestrate",
    ]:
        if not FILES[label].exists():
            continue
        content = read(FILES[label])
        for term in INTEGRATION_TERMS[:1]:
            if term not in content:
                failures.append(f"{label} missing integration term: {term}")

    combined_skill = read(FILES["codex_skill"]) if FILES["codex_skill"].exists() else ""
    # Trigger vocabulary anchors (skill description reworded in the V4 pass;
    # the behavior is that flat/generic/uncompelling work triggers the OS).
    for trigger_term in ("flat", "generic", "compelling"):
        if trigger_term not in combined_skill:
            failures.append(f"codex skill missing user-trigger language: {trigger_term}")

    for query in ROUTING_QUERIES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        combined = menu + "\n" + router
        # The workflow's own Behavior Proof accepts either family surface:
        # /high-taste-os (wrapper) or /high-taste-writing-os (owner).
        if "/high-taste-writing-os" not in combined and "/high-taste-os" not in combined:
            failures.append(f"routing query did not surface the high-taste OS: {query}")

    if failures:
        print("High-Taste Writing OS verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("High-Taste Writing OS verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
