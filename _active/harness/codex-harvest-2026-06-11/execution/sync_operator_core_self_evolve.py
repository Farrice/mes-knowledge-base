#!/usr/bin/env python3
"""Check or align Self-evolve Operator Core wrappers."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "self-evolve.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-self-evolve" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_SELF_EVOLVE = Path.home() / ".codex" / "skills" / "self-evolve" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-self-evolve" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Codex Antigravity/.agent/workflows/self-evolve.md"

COMMON_REQUIREMENTS = (
    "mutation-gated measured evolution",
    "queue-only diagnosis",
    "complete goal packet",
    "Evolution Council Verdict",
    "baseline",
    "search set",
    "measurable stop condition",
    "turn cap",
    "proof artifact",
    "no-regression check",
    "local, reversible",
    "human checkpoint",
    "verify_mission_activation_contract.py",
    "real Codex subagents require explicit authorization",
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for Self-evolve behavior",
        "mutation-gated measured evolution",
        "Incomplete or vague goal packets produce a queue-only diagnosis",
        "Mutation requires a complete goal packet, Evolution Council Verdict, baseline, search set, measurable stop condition, turn cap, proof artifact, and no-regression check",
        "Permitted side effects must be local, reversible, and inside `/Users/farricecain/Codex Antigravity`",
        "Stop at a human checkpoint for global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or scope expansion",
        "Do not mutate Mission unless `verify_mission_activation_contract.py` fails and the user explicitly approves Mission repair",
        "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/self-evolve.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global Self-evolve Evolution",
    ),
    GLOBAL_SELF_EVOLVE: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/self-evolve/SKILL.md",
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "improve this by editing immediately",
    "mutate by default",
    "global mirror by default",
    "external action by default",
    "delete without approval",
    "destructive cleanup by default",
    "mutate Mission by default",
    "repair Mission by default",
)

GLOBAL_AGENTS_BLOCK = f"""## Global Self-evolve Evolution

Use the global `self-evolve` skill at `/Users/farricecain/.codex/skills/self-evolve/SKILL.md`
when the user invokes `/self-evolve`, `source-command-self-evolve`, or asks for
feedback-backed workflow evolution, regression-aware improvement, performance
log evolution, recurring mistake reduction, or measured evolution without bloat.

The canonical Antigravity Self-evolve workflow is `{CANONICAL_PATH}`. Global
Self-evolve wrappers are thin compatibility wrappers with no competing behavior
contract.

Default behavior: mutation-gated measured evolution. Incomplete or vague goal
packets produce queue-only diagnosis and missing fields. Mutation requires a
complete goal packet, Evolution Council Verdict, baseline, search set,
measurable stop condition, turn cap, proof artifact, and no-regression check.
Side effects must be local, reversible, and inside
`/Users/farricecain/Codex Antigravity`. Stop at a human checkpoint for global
mirrors, external actions, broad archive/delete, destructive cleanup, new
dependencies, failed validation, scope expansion, or Mission repair unless
`verify_mission_activation_contract.py` fails and Farrice explicitly approves.
Real Codex subagents require explicit authorization.
"""

GLOBAL_SELF_EVOLVE_TEXT = f"""---
name: self-evolve
description: Global thin compatibility wrapper for Antigravity Self-evolve; delegates to the canonical project workflow.
---

# Self-evolve

## Project Source Of Truth

The canonical Self-evolve behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps `/self-evolve`,
feedback-backed evolution, regression-aware improvement, and performance-log
evolution discoverable anywhere in Codex, but it must not maintain a competing
behavior contract. When the Antigravity project workflow is available or
relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current Self-evolve contract:

- mutation-gated measured evolution, not casual improvement
- incomplete or vague goal packets produce queue-only diagnosis and missing fields
- mutation requires a complete goal packet, Evolution Council Verdict, baseline, search set, measurable stop condition, turn cap, proof artifact, and no-regression check
- side effects must be local, reversible, and inside `/Users/farricecain/Codex Antigravity`
- human checkpoint for global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, scope expansion, or Mission repair
- no Mission mutation unless `verify_mission_activation_contract.py` fails and Farrice explicitly approves Mission repair
- repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-self-evolve
description: Global compatibility alias for /self-evolve; follows the Antigravity evolution source of truth.
---

# source-command-self-evolve

This is a compatibility alias for the global Self-evolve wrapper. When invoked,
load and follow:

`/Users/farricecain/.codex/skills/self-evolve/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current Self-evolve contract: mutation-gated measured evolution, queue-only
diagnosis for incomplete or vague goal packets, complete goal packet, Evolution
Council Verdict, baseline, search set, measurable stop condition, turn cap,
proof artifact, no-regression check, local and reversible side effects, human
checkpoint for risky changes, no Mission mutation unless
`verify_mission_activation_contract.py` fails and Farrice explicitly approves,
real Codex subagents require explicit authorization, and no competing behavior
contract.

In short: side effects must be local, reversible, and bounded by the canonical
workflow.

Route repair, drift-audit, and broken-system language to `/system-audit` or
`/autopilot`; keep explicit measured evolution questions on `/self-evolve`.
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


def align_global_agents(text: str) -> str:
    if "## Global Self-evolve Evolution" in text:
        return re.sub(
            r"## Global Self-evolve Evolution\n.*?(?=\n## Global Knowledge-librarian Pulse|\n## Global Routing-intelligence Analytics|\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    anchor = "## Global Knowledge-librarian Pulse"
    if anchor in text:
        return text.replace(anchor, GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n" + anchor, 1)
    return text.rstrip() + "\n\n" + GLOBAL_AGENTS_BLOCK.rstrip() + "\n"


def apply_alignment() -> list[str]:
    changed: list[str] = []

    original_agents = read(GLOBAL_AGENTS)
    updated_agents = align_global_agents(original_agents)
    if updated_agents != original_agents:
        write(GLOBAL_AGENTS, updated_agents)
        changed.append(str(GLOBAL_AGENTS))

    if not GLOBAL_SELF_EVOLVE.exists() or read(GLOBAL_SELF_EVOLVE) != GLOBAL_SELF_EVOLVE_TEXT.rstrip() + "\n":
        write(GLOBAL_SELF_EVOLVE, GLOBAL_SELF_EVOLVE_TEXT)
        changed.append(str(GLOBAL_SELF_EVOLVE))

    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))

    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-self-evolve", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global self-evolve", GLOBAL_SELF_EVOLVE),
        ("global source-command-self-evolve", GLOBAL_WRAPPER),
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
                failures.append(f"{label} contains stale Self-evolve contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align Self-evolve Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global Self-evolve surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()

    if args.apply:
        changed = apply_alignment()
        print("SELF-EVOLVE OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))

    failures = check_alignment()
    if failures:
        print("SELF-EVOLVE OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("SELF-EVOLVE OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
