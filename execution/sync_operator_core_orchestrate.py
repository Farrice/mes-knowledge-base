#!/usr/bin/env python3
"""Check or align Orchestrate Operator Core wrappers with source truth."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "orchestrate.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-orchestrate" / "SKILL.md"
GLOBAL_ORCHESTRATE = Path.home() / ".codex" / "skills" / "orchestrate" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-orchestrate" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Google Antigravity/.agent/workflows/orchestrate.md"

COMMON_REQUIREMENTS = (
    "menu-only backend",
    "must not execute",
    "mutate files",
    "choose on Farrice's behalf",
    "execution intent routes through `/autopilot`",
    "real Codex subagents require explicit authorization",
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for Orchestrate behavior",
        "/orchestrate` is a menu-only backend",
        "must not execute",
        "mutate files",
        "choose on Farrice's behalf",
        "safe-run execution after trace",
        "Real Codex subagents require explicit authorization",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/orchestrate.md",
        "canonical behavior source",
    ),
    GLOBAL_ORCHESTRATE: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "canonical project workflow",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "plan-first approval checkpoint",
    "Plan First Always",
    "approval checkpoint for meaningful work",
    "plan-first checkpoint",
)

GLOBAL_ORCHESTRATE_TEXT = f"""---
name: orchestrate
description: Global thin compatibility wrapper for the Antigravity Orchestrate execution menu; delegates to the canonical project workflow and stays menu-only.
---

# Orchestrate

## Project Source Of Truth

The canonical Orchestrate behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps `/orchestrate` and
`orchestrate` discoverable anywhere in Codex, but it must not maintain a
competing behavior contract. When the Antigravity project workflow is available
or relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current Orchestrate contract:

- `/orchestrate` is a menu-only backend
- it must not execute, mutate files, choose on Farrice's behalf, or continue into implementation
- execution intent routes through `/autopilot`
- raw intent, chosen-route execution, and safe workspace-local work belong to `/autopilot`
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract

## Output Contract

Produce a ranked Execution Menu with concrete paths, exact commands, expert or
skill stack, recommended stack, deliverables, effort, verification criteria, and
the suggested first prompt or command. Stop there.
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-orchestrate
description: Global compatibility alias for /orchestrate; follows the Antigravity menu-only source of truth.
---

# source-command-orchestrate

This is a compatibility alias for the global Orchestrate wrapper. When invoked,
load and follow:

`/Users/farricecain/.codex/skills/orchestrate/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current Orchestrate contract: menu-only backend, must not execute or mutate
files, must not choose on Farrice's behalf, execution intent routes through
`/autopilot`, real Codex subagents require explicit authorization, and no
competing behavior contract.

When blocked or when the user wants execution, route to `/autopilot` instead of
continuing from `/orchestrate`.
"""

LOCAL_ALIGNMENT_BLOCK = """## Operator Core Alignment

This project wrapper follows `.agent/workflows/orchestrate.md` as the canonical behavior source. It must stay a thin compatibility wrapper and preserve:

- menu-only backend behavior
- must not execute, mutate files, or choose on Farrice's behalf
- execution intent routes through `/autopilot`
- real Codex subagents require explicit authorization
- no competing behavior contract
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
    return text.replace(anchor, anchor.rstrip() + "\n\n" + block.rstrip() + "\n", 1)


def align_workflow(text: str) -> str:
    text = text.replace(
        "a decision-complete plan, route them to `/autopilot`",
        "safe-run execution after trace, route them to `/autopilot`",
    )
    text = text.replace(
        "route choice, and a plan-first checkpoint",
        "route choice, and safe-run execution after trace",
    )
    text = text.replace(
        "3. Do not spawn real Codex subagents unless the user explicitly requested delegated agent work.",
        "3. Real Codex subagents require explicit authorization; do not spawn them unless the user explicitly requested delegated agent work.",
    )
    block = """## Operator Core Alignment

This workflow is the canonical source of truth for Orchestrate behavior. Global
and local Orchestrate wrappers must stay thin compatibility wrappers that point
back here, not competing behavior contracts.

Preserve these invariants:

- `/orchestrate` is a menu-only backend.
- It must not execute, mutate files, choose on Farrice's behalf, or continue into implementation.
- It routes raw intent, chosen-route execution, and safe workspace-local work through `/autopilot`.
- Real Codex subagents require explicit authorization.
- The output stops at ranked options, verification criteria, and suggested first prompts or commands.
"""
    return ensure_block(text, block, "Menu-only boundary:")


def align_local_wrapper(text: str) -> str:
    text = text.replace(
        "Do not use this skill when the user wants the system to choose and begin work. Route that through `source-command-autopilot`, which now produces a plan-first approval checkpoint for meaningful work.",
        "Do not use this skill when the user wants the system to choose and begin work. Route that through `source-command-autopilot`, which owns intent lock, route choice, and safe-run execution after trace.",
    )
    return ensure_block(text, LOCAL_ALIGNMENT_BLOCK, "## Command Template")


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

    if not GLOBAL_ORCHESTRATE.exists() or read(GLOBAL_ORCHESTRATE) != GLOBAL_ORCHESTRATE_TEXT.rstrip() + "\n":
        write(GLOBAL_ORCHESTRATE, GLOBAL_ORCHESTRATE_TEXT)
        changed.append(str(GLOBAL_ORCHESTRATE))

    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))

    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-orchestrate", LOCAL_WRAPPER),
        ("global orchestrate", GLOBAL_ORCHESTRATE),
        ("global source-command-orchestrate", GLOBAL_WRAPPER),
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
                failures.append(f"{label} contains stale Orchestrate contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align Orchestrate Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global/local Orchestrate surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()

    if args.apply:
        changed = apply_alignment()
        print("ORCHESTRATE OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))

    failures = check_alignment()
    if failures:
        print("ORCHESTRATE OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("ORCHESTRATE OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
