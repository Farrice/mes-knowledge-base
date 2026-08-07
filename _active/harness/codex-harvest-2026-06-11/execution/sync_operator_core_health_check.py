#!/usr/bin/env python3
"""Check or align Health-check Operator Core wrappers with source truth."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "health-check.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-health-check" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_HEALTH_CHECK = Path.home() / ".codex" / "skills" / "health-check" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-health-check" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Codex Antigravity/.agent/workflows/health-check.md"

COMMON_REQUIREMENTS = (
    "read-only status",
    "harness_status.py --plain",
    "system_health.py --quick",
    "operator_core_status.py --plain",
    "no report writes",
    "Notion sync",
    "route optimization",
    "Mission mutation",
    "cleanup",
    "verify_mission_activation_contract.py",
    "real Codex subagents require explicit authorization",
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for Health-check behavior",
        "read-only by default",
        "python3 execution/harness_status.py --plain",
        "python3 execution/system_health.py --quick",
        "python3 execution/operator_core_status.py --plain",
        "Do not write reports, sync Notion, optimize routes, mutate Mission, or perform cleanup unless explicitly requested",
        "Mission remains read-only unless `python3 execution/verify_mission_activation_contract.py` fails",
        "Route system-failure or drift-audit language to `/autopilot` or `/system-audit`",
        "Real Codex subagents require explicit authorization",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/health-check.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global Health-check Status",
    ),
    GLOBAL_HEALTH_CHECK: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/health-check/SKILL.md",
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "python execution/system_health.py",
    "/skill-evolution",
    "write reports by default",
    "writes a report by default",
    "auto-optimize",
    "auto optimize",
    "auto-sync",
    "auto sync",
    "live Notion write",
    "mutate Mission by default",
    "repair Mission by default",
)

GLOBAL_AGENTS_BLOCK = f"""## Global Health-check Status

Use the global `health-check` skill at `/Users/farricecain/.codex/skills/health-check/SKILL.md`
when the user invokes `/health-check`, `source-command-health-check`, `health check`,
`run harness status`, or asks for a read-only status view of what is working,
stale, or broken.

The canonical Antigravity Health-check workflow is `{CANONICAL_PATH}`. Global
Health-check wrappers are thin compatibility wrappers with no competing behavior
contract.

Default behavior: `harness_status.py --plain` first for the trust/status
surface, then `system_health.py --quick` for activation health and feedback-loop
readiness, then `operator_core_status.py --plain` for the compact Operator Core
alignment closeout. This is read-only status by default: no report writes, live Notion
sync, route optimization, Mission mutation, cleanup, destructive action, or real
Codex subagents without explicit authorization. Mission remains read-only unless
`verify_mission_activation_contract.py` fails.
"""

GLOBAL_HEALTH_CHECK_TEXT = f"""---
name: health-check
description: Global thin compatibility wrapper for Antigravity Health-check status; delegates to the canonical project workflow.
---

# Health-check

## Project Source Of Truth

The canonical Health-check behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps `/health-check`,
`health check`, and harness status language discoverable anywhere in Codex, but
it must not maintain a competing behavior contract. When the Antigravity project
workflow is available or relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current Health-check contract:

- `/health-check` is read-only status by default
- use `harness_status.py --plain` first
- use `system_health.py --quick` second
- include `operator_core_status.py --plain` as the compact Operator Core alignment closeout
- no report writes, live Notion sync, route optimization, Mission mutation, cleanup, destructive action, or global mirror unless explicitly requested
- Mission remains read-only unless `verify_mission_activation_contract.py` fails
- system-failure or drift-audit language routes to `/autopilot` or `/system-audit`
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract

## Output Contract

Produce a compact status readout: Working, Stale, Broken, latest proof, routing
health, activation health, Operator Core alignment status, and exactly one safe
next move. Do not execute the next move from this wrapper.
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-health-check
description: Global compatibility alias for /health-check; follows the Antigravity status source of truth.
---

# source-command-health-check

This is a compatibility alias for the global Health-check wrapper. When invoked,
load and follow:

`/Users/farricecain/.codex/skills/health-check/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current Health-check contract: read-only status by default,
`harness_status.py --plain` first, `system_health.py --quick` second,
`operator_core_status.py --plain` as the compact Operator Core alignment
closeout, no report
writes, live Notion sync, route optimization, Mission mutation, cleanup, or
destructive action unless explicitly requested, Mission remains read-only unless
`verify_mission_activation_contract.py` fails, real Codex subagents require
explicit authorization, and no competing behavior contract.

Route system-failure or drift-audit language to `/autopilot` or
`/system-audit`; keep explicit status and health questions on `/health-check`.
"""

LOCAL_ALIGNMENT_BLOCK = """## Operator Core Alignment

This project wrapper follows `.agent/workflows/health-check.md` as the canonical behavior source. It must stay a thin compatibility wrapper and preserve:

- read-only status by default
- `harness_status.py --plain` as the first trust/status surface
- `system_health.py --quick` as the activation and feedback-loop detail layer
- `operator_core_status.py --plain` as the compact Operator Core alignment closeout
- no report writes, Notion sync, route optimization, Mission mutation, cleanup, or destructive action unless explicitly requested
- Mission remains read-only unless `verify_mission_activation_contract.py` fails
- system-failure or drift-audit language routes to `/autopilot` or `/system-audit`
- real Codex subagents require explicit authorization
- no competing behavior contract
"""

WORKFLOW_ALIGNMENT_BLOCK = """## Operator Core Alignment

This workflow is the canonical source of truth for Health-check behavior. Global
and local Health-check wrappers must stay thin compatibility wrappers that point
back here, not competing behavior contracts.

Preserve these invariants:

- `/health-check` is read-only by default.
- Start with `python3 execution/harness_status.py --plain` for the trust/status surface.
- Then run `python3 execution/system_health.py --quick` for activation and feedback-loop detail.
- Include `python3 execution/operator_core_status.py --plain` as the compact Operator Core alignment closeout.
- Do not write reports, sync Notion, optimize routes, mutate Mission, or perform cleanup unless explicitly requested.
- Mission remains read-only unless `python3 execution/verify_mission_activation_contract.py` fails.
- Route system-failure or drift-audit language to `/autopilot` or `/system-audit`; use `/health-check` for explicit status and health questions.
- Real Codex subagents require explicit authorization.
"""


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def ensure_block(text: str, block: str, anchor: str) -> str:
    heading = block.splitlines()[0]
    if heading in text:
        return text
    if anchor not in text:
        return text.rstrip() + "\n\n" + block.rstrip() + "\n"
    return text.replace(anchor, block.rstrip() + "\n\n" + anchor, 1)


def align_workflow(text: str) -> str:
    return ensure_block(text, WORKFLOW_ALIGNMENT_BLOCK, "## Usage")


def align_local_wrapper(text: str) -> str:
    return ensure_block(text, LOCAL_ALIGNMENT_BLOCK, "## Command Template")


def align_global_agents(text: str) -> str:
    if "## Global Health-check Status" in text:
        return re.sub(
            r"## Global Health-check Status\n.*?(?=\n## Global End-Session Closeout|\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    return ensure_block(text, GLOBAL_AGENTS_BLOCK, "## Global End-Session Closeout")


def apply_alignment() -> list[str]:
    changed: list[str] = []

    original_workflow = read(PROJECT_WORKFLOW)
    updated_workflow = align_workflow(original_workflow)
    if updated_workflow != original_workflow:
        write(PROJECT_WORKFLOW, updated_workflow)
        changed.append(str(PROJECT_WORKFLOW.relative_to(ROOT)))

    original_local = read(LOCAL_WRAPPER)
    updated_local = align_local_wrapper(original_local)
    if updated_local != original_local:
        write(LOCAL_WRAPPER, updated_local)
        changed.append(str(LOCAL_WRAPPER.relative_to(ROOT)))

    original_agents = read(GLOBAL_AGENTS)
    updated_agents = align_global_agents(original_agents)
    if updated_agents != original_agents:
        write(GLOBAL_AGENTS, updated_agents)
        changed.append(str(GLOBAL_AGENTS))

    if not GLOBAL_HEALTH_CHECK.exists() or read(GLOBAL_HEALTH_CHECK) != GLOBAL_HEALTH_CHECK_TEXT.rstrip() + "\n":
        write(GLOBAL_HEALTH_CHECK, GLOBAL_HEALTH_CHECK_TEXT)
        changed.append(str(GLOBAL_HEALTH_CHECK))

    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))

    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-health-check", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global health-check", GLOBAL_HEALTH_CHECK),
        ("global source-command-health-check", GLOBAL_WRAPPER),
    ):
        if not path.exists():
            failures.append(f"{label} missing: {path}")
            continue
        text = read(path)
        normalized = normalize(text)
        for snippet in PATH_REQUIREMENTS[path]:
            if normalize(snippet) not in normalized:
                failures.append(f"{label} missing: {snippet}")
        for snippet in FORBIDDEN:
            if snippet.lower() in text.lower():
                failures.append(f"{label} contains stale Health-check contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align Health-check Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global/local Health-check surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()

    if args.apply:
        changed = apply_alignment()
        print("HEALTH-CHECK OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))

    failures = check_alignment()
    if failures:
        print("HEALTH-CHECK OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("HEALTH-CHECK OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
