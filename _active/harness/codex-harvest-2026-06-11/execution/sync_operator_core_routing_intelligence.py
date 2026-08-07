#!/usr/bin/env python3
"""Check or align Routing-intelligence Operator Core wrappers."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "routing-intelligence.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-routing-intelligence" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_ROUTING_INTELLIGENCE = Path.home() / ".codex" / "skills" / "routing-intelligence" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-routing-intelligence" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Codex Antigravity/.agent/workflows/routing-intelligence.md"

COMMON_REQUIREMENTS = (
    "read-only routing analytics",
    "routing_intelligence.py scoreboard",
    "misroute",
    "explicitly reports a wrong route",
    "no auto-optimization",
    "Mission mutation",
    "cleanup",
    "real Codex subagents require explicit authorization",
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for Routing-intelligence behavior",
        "read-only analytics by default",
        "python3 execution/routing_intelligence.py scoreboard",
        "python3 execution/routing_intelligence.py utilization",
        "python3 execution/routing_intelligence.py unused",
        "python3 execution/routing_intelligence.py domain-dist",
        "python3 execution/routing_intelligence.py top-combos",
        "python3 execution/routing_intelligence.py underperforming",
        "python3 execution/routing_intelligence.py misroute",
        "Only write routing feedback through `misroute` when the user explicitly reports a wrong route",
        "Do not auto-optimize routes, mutate workflows, sync Notion, mutate Mission, perform cleanup, or mirror global files",
        "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/routing-intelligence.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global Routing-intelligence Analytics",
    ),
    GLOBAL_ROUTING_INTELLIGENCE: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/routing-intelligence/SKILL.md",
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "python execution/routing_intelligence.py",
    "auto-optimize routes by default",
    "auto optimize routes by default",
    "auto-optimize without approval",
    "auto optimize without approval",
    "mutate workflows by default",
    "sync Notion by default",
    "mutate Mission by default",
    "repair Mission by default",
    "write route feedback by default",
)

GLOBAL_AGENTS_BLOCK = f"""## Global Routing-intelligence Analytics

Use the global `routing-intelligence` skill at `/Users/farricecain/.codex/skills/routing-intelligence/SKILL.md`
when the user invokes `/routing-intelligence`, `source-command-routing-intelligence`,
`routing intelligence dashboard`, `routing scoreboard`, or asks for read-only
routing analytics, expert utilization, domain distribution, route feedback, or
underperforming routes.

The canonical Antigravity Routing-intelligence workflow is `{CANONICAL_PATH}`.
Global Routing-intelligence wrappers are thin compatibility wrappers with no
competing behavior contract.

Default behavior: `routing_intelligence.py scoreboard` first for the read-only
analytics dashboard. Focused read-only subcommands may show utilization, unused
experts, domain distribution, top combos, and underperforming routes. `misroute`
writes only when the user explicitly reports a wrong route or asks to record a
correction. Do not perform auto-optimization, workflow mutation, live Notion sync,
Mission mutation, cleanup, destructive action, or real Codex subagents without
explicit authorization. Route repair, drift-audit, and broken-system language to
`/system-audit` or `/autopilot`.

In short: no auto-optimization, no competing behavior contract, and no real
Codex subagents without explicit authorization.
"""

GLOBAL_ROUTING_INTELLIGENCE_TEXT = f"""---
name: routing-intelligence
description: Global thin compatibility wrapper for Antigravity Routing-intelligence analytics; delegates to the canonical project workflow.
---

# Routing-intelligence

## Project Source Of Truth

The canonical Routing-intelligence behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps
`/routing-intelligence`, routing analytics, routing scoreboard, and route
feedback language discoverable anywhere in Codex, but it must not maintain a
competing behavior contract. When the Antigravity project workflow is available
or relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current Routing-intelligence contract:

- `/routing-intelligence` is read-only routing analytics by default
- use `routing_intelligence.py scoreboard` first
- use focused read-only views for utilization, unused experts, domain distribution, top combos, and underperforming routes
- `misroute` writes only when the user explicitly reports a wrong route or asks to record a correction
- no auto-optimization, workflow mutation, live Notion sync, Mission mutation, cleanup, destructive action, or global mirror unless explicitly requested
- repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract

## Output Contract

Produce a compact analytics readout: overview, expert utilization, domain
distribution, strongest patterns, underperforming routes, and exactly one safe
next move. Do not execute route repairs from this wrapper.
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-routing-intelligence
description: Global compatibility alias for /routing-intelligence; follows the Antigravity routing analytics source of truth.
---

# source-command-routing-intelligence

This is a compatibility alias for the global Routing-intelligence wrapper. When
invoked, load and follow:

`/Users/farricecain/.codex/skills/routing-intelligence/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current Routing-intelligence contract: read-only routing analytics by default,
`routing_intelligence.py scoreboard` first, focused read-only analytics
subcommands, `misroute` writes only when the user explicitly reports a wrong
route or asks to record a correction, no auto-optimization, workflow mutation,
live Notion sync, Mission mutation, cleanup, destructive action, or global
mirror unless explicitly requested, real Codex subagents require explicit
authorization, and no competing behavior contract.

Route repair, drift-audit, and broken-system language to `/system-audit` or
`/autopilot`; keep explicit routing analytics and scoreboard questions on
`/routing-intelligence`.
"""

LOCAL_ALIGNMENT_BLOCK = """## Operator Core Alignment

This project wrapper follows `.agent/workflows/routing-intelligence.md` as the
canonical behavior source. It must stay a thin compatibility wrapper and
preserve:

- read-only routing analytics by default
- `routing_intelligence.py scoreboard` as the first dashboard surface
- focused read-only subcommands for utilization, unused, domain-dist, top-combos, and underperforming
- `misroute` writes only when the user explicitly reports a wrong route or asks to record a correction
- no auto-optimization, workflow mutation, Notion sync, Mission mutation, cleanup, destructive action, or global mirror unless explicitly requested
- repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- no competing behavior contract
"""

WORKFLOW_ALIGNMENT_BLOCK = """## Operator Core Alignment

This workflow is the canonical source of truth for Routing-intelligence behavior.
Global and local Routing-intelligence wrappers must stay thin compatibility
wrappers that point back here, not competing behavior contracts.

Preserve these invariants:

- `/routing-intelligence` is read-only analytics by default.
- Start with `python3 execution/routing_intelligence.py scoreboard` for the dashboard.
- Use subcommands for focused read-only views: utilization, unused, domain-dist, top-combos, and underperforming.
- Only write routing feedback through `misroute` when the user explicitly reports a wrong route or asks to record a correction.
- Do not auto-optimize routes, mutate workflows, sync Notion, mutate Mission, perform cleanup, or mirror global files from `/routing-intelligence`.
- Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`; use `/routing-intelligence` for explicit routing analytics and scoreboard questions.
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
    if "## Global Routing-intelligence Analytics" in text:
        return re.sub(
            r"## Global Routing-intelligence Analytics\n.*?(?=\n## Global Health-check Status|\n## Global End-Session Closeout|\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    return ensure_block(text, GLOBAL_AGENTS_BLOCK, "## Global Health-check Status")


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

    if not GLOBAL_ROUTING_INTELLIGENCE.exists() or read(GLOBAL_ROUTING_INTELLIGENCE) != GLOBAL_ROUTING_INTELLIGENCE_TEXT.rstrip() + "\n":
        write(GLOBAL_ROUTING_INTELLIGENCE, GLOBAL_ROUTING_INTELLIGENCE_TEXT)
        changed.append(str(GLOBAL_ROUTING_INTELLIGENCE))

    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))

    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-routing-intelligence", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global routing-intelligence", GLOBAL_ROUTING_INTELLIGENCE),
        ("global source-command-routing-intelligence", GLOBAL_WRAPPER),
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
                failures.append(f"{label} contains stale Routing-intelligence contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align Routing-intelligence Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global/local Routing-intelligence surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()

    if args.apply:
        changed = apply_alignment()
        print("ROUTING-INTELLIGENCE OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))

    failures = check_alignment()
    if failures:
        print("ROUTING-INTELLIGENCE OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("ROUTING-INTELLIGENCE OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
