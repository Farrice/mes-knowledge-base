#!/usr/bin/env python3
"""Check or align System-audit Operator Core wrappers."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "system-audit.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-system-audit" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_SYSTEM_AUDIT = Path.home() / ".codex" / "skills" / "system-audit" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-system-audit" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Google Antigravity/.agent/workflows/system-audit.md"

COMMON_REQUIREMENTS = (
    "control-plane audit and repair",
    "read-only proof first",
    "structural health",
    "firing behavior",
    "severity-ranked",
    "verifier-backed",
    "workspace-local by default",
    "global `~/.codex` edits require explicit approval",
    "verify_mission_activation_contract.py",
    "real Codex subagents require explicit authorization",
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for System-audit behavior",
        "control-plane audit and repair route",
        "Run read-only proof first",
        "Distinguish structural health from firing behavior",
        "Repairs must be severity-ranked, verifier-backed, and workspace-local by default",
        "Global `~/.codex` edits require explicit approval",
        "Mission remains untouched unless `verify_mission_activation_contract.py` fails and Farrice explicitly approves Mission repair",
        "Route normal status reads to `/health-check`, routing analytics to `/routing-intelligence`, and raw intent or broad broken-harness triage to `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/system-audit.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global System-audit Control Plane",
    ),
    GLOBAL_SYSTEM_AUDIT: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/system-audit/SKILL.md",
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "delete by default",
    "destructive cleanup by default",
    "global edit by default",
    "connector write by default",
    "publish by default",
    "mutate Mission by default",
    "repair Mission by default",
)

GLOBAL_AGENTS_BLOCK = f"""## Global System-audit Control Plane

Use the global `system-audit` skill at `/Users/farricecain/.codex/skills/system-audit/SKILL.md`
when the user invokes `/system-audit`, `source-command-system-audit`, or asks for
a control-plane audit of broken, drifted, cluttered, duplicated, slow, or
not-firing harness behavior.

The canonical Antigravity System-audit workflow is `{CANONICAL_PATH}`. Global
System-audit wrappers are thin compatibility wrappers with no competing
behavior contract.

Default behavior: control-plane audit and repair with read-only proof first.
Distinguish structural health from firing behavior. Repairs must be
severity-ranked, verifier-backed, and workspace-local by default. Global
global `~/.codex` edits require explicit approval. External writes, publishing,
connector writes, destructive cleanup, broad archive/delete, and Mission
mutation require explicit approval and proof. Mission remains untouched unless
`verify_mission_activation_contract.py` fails and Farrice explicitly approves
Mission repair. Real Codex subagents require explicit authorization.
"""

GLOBAL_SYSTEM_AUDIT_TEXT = f"""---
name: system-audit
description: Global thin compatibility wrapper for Antigravity System-audit; delegates to the canonical project workflow.
---

# System-audit

## Project Source Of Truth

The canonical System-audit behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps `/system-audit`,
control-plane audit, not-firing harness, routing drift, and proof-path repair
language discoverable anywhere in Codex, but it must not maintain a competing
behavior contract. When the Antigravity project workflow is available or
relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current System-audit contract:

- control-plane audit and repair for broken, drifted, cluttered, or not-firing harness behavior
- read-only proof first across routing, bridge, activation, telemetry, cohesion, and verifier checks
- structural health is distinct from firing behavior
- repairs are severity-ranked, verifier-backed, and workspace-local by default
- global `~/.codex` edits require explicit approval
- external writes, publishing, connector writes, destructive cleanup, broad archive/delete, and Mission mutation require explicit approval and proof
- Mission remains untouched unless `verify_mission_activation_contract.py` fails and Farrice explicitly approves Mission repair
- status reads route to `/health-check`, routing analytics to `/routing-intelligence`, raw/broad triage to `/autopilot`
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-system-audit
description: Global compatibility alias for /system-audit; follows the Antigravity control-plane audit source of truth.
---

# source-command-system-audit

This is a compatibility alias for the global System-audit wrapper. When invoked,
load and follow:

`/Users/farricecain/.codex/skills/system-audit/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current System-audit contract: control-plane audit and repair, read-only proof
first, structural health versus firing behavior, severity-ranked and
verifier-backed repairs, workspace-local by default, global `~/.codex` edits
require explicit approval, Mission remains untouched unless
`verify_mission_activation_contract.py` fails and Farrice explicitly approves,
real Codex subagents require explicit authorization, and no competing behavior
contract.
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
    if "## Global System-audit Control Plane" in text:
        return re.sub(
            r"## Global System-audit Control Plane\n.*?(?=\n## Global Source-to-skill-system Builder|\n## Global Skill-anneal Prompt Repair|\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    anchor = "## Global Source-to-skill-system Builder"
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
    if not GLOBAL_SYSTEM_AUDIT.exists() or read(GLOBAL_SYSTEM_AUDIT) != GLOBAL_SYSTEM_AUDIT_TEXT.rstrip() + "\n":
        write(GLOBAL_SYSTEM_AUDIT, GLOBAL_SYSTEM_AUDIT_TEXT)
        changed.append(str(GLOBAL_SYSTEM_AUDIT))
    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))
    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-system-audit", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global system-audit", GLOBAL_SYSTEM_AUDIT),
        ("global source-command-system-audit", GLOBAL_WRAPPER),
    ):
        if not path.exists():
            failures.append(f"{label} missing: {path}")
            continue
        text = read(path)
        normalized = normalize(text).lower()
        for snippet in PATH_REQUIREMENTS[path]:
            if normalize(snippet).lower() not in normalized:
                failures.append(f"{label} missing: {snippet}")
        for snippet in FORBIDDEN:
            if snippet.lower() in text.lower():
                failures.append(f"{label} contains stale System-audit contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align System-audit Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global System-audit surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()
    if args.apply:
        changed = apply_alignment()
        print("SYSTEM-AUDIT OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))
    failures = check_alignment()
    if failures:
        print("SYSTEM-AUDIT OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("SYSTEM-AUDIT OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
