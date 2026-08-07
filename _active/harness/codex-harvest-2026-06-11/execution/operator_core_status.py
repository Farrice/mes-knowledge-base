#!/usr/bin/env python3
"""Read-only Operator Core wrapper-alignment dashboard."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Surface:
    name: str
    route: str
    canonical: Path
    local_wrapper: Path
    global_skill: Path | None
    global_wrapper: Path | None
    sync_command: tuple[str, ...] | None
    verifier_command: tuple[str, ...]
    role: str
    scope: str = "global-local"


SURFACES = (
    Surface(
        name="Autopilot",
        route="autopilot",
        canonical=ROOT / ".agent" / "workflows" / "autopilot.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-autopilot" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "autopilot" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-autopilot" / "SKILL.md",
        sync_command=("execution/sync_global_operator_core.py", "--check"),
        verifier_command=("execution/verify_global_autopilot_source_truth.py",),
        role="front door",
    ),
    Surface(
        name="Orchestrate",
        route="orchestrate",
        canonical=ROOT / ".agent" / "workflows" / "orchestrate.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-orchestrate" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "orchestrate" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-orchestrate" / "SKILL.md",
        sync_command=("execution/sync_operator_core_orchestrate.py", "--check"),
        verifier_command=("execution/verify_operator_core_orchestrate.py",),
        role="menu backend",
    ),
    Surface(
        name="End-session",
        route="end-session",
        canonical=ROOT / ".agent" / "workflows" / "end-session.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-end-session" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "end-session" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-end-session" / "SKILL.md",
        sync_command=("execution/sync_operator_core_end_session.py", "--check"),
        verifier_command=("execution/verify_operator_core_end_session.py",),
        role="closeout",
    ),
    Surface(
        name="Health-check",
        route="health-check",
        canonical=ROOT / ".agent" / "workflows" / "health-check.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-health-check" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "health-check" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-health-check" / "SKILL.md",
        sync_command=("execution/sync_operator_core_health_check.py", "--check"),
        verifier_command=("execution/verify_operator_core_health_check.py",),
        role="read-only status",
    ),
    Surface(
        name="Routing-intelligence",
        route="routing-intelligence",
        canonical=ROOT / ".agent" / "workflows" / "routing-intelligence.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-routing-intelligence" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "routing-intelligence" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-routing-intelligence" / "SKILL.md",
        sync_command=("execution/sync_operator_core_routing_intelligence.py", "--check"),
        verifier_command=("execution/verify_operator_core_routing_intelligence.py",),
        role="routing analytics",
    ),
    Surface(
        name="Knowledge-librarian",
        route="knowledge-librarian",
        canonical=ROOT / ".agent" / "workflows" / "knowledge-librarian.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-knowledge-librarian" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "knowledge-librarian" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-knowledge-librarian" / "SKILL.md",
        sync_command=("execution/sync_operator_core_knowledge_librarian.py", "--check"),
        verifier_command=("execution/verify_operator_core_knowledge_librarian.py",),
        role="library pulse",
    ),
    Surface(
        name="Self-evolve",
        route="self-evolve",
        canonical=ROOT / ".agent" / "workflows" / "self-evolve.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-self-evolve" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "self-evolve" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-self-evolve" / "SKILL.md",
        sync_command=("execution/sync_operator_core_self_evolve.py", "--check"),
        verifier_command=("execution/verify_operator_core_self_evolve.py",),
        role="measured evolution",
    ),
    Surface(
        name="Skill-anneal",
        route="skill-anneal",
        canonical=ROOT / ".agent" / "workflows" / "skill-anneal.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-skill-anneal" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "skill-anneal" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-skill-anneal" / "SKILL.md",
        sync_command=("execution/sync_operator_core_skill_anneal.py", "--check"),
        verifier_command=("execution/verify_operator_core_skill_anneal.py",),
        role="prompt annealing",
    ),
    Surface(
        name="Source-to-skill-system",
        route="source-to-skill-system",
        canonical=ROOT / ".agent" / "workflows" / "source-to-skill-system.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-source-to-skill-system" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "source-to-skill-system" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-source-to-skill-system" / "SKILL.md",
        sync_command=("execution/sync_operator_core_source_to_skill_system.py", "--check"),
        verifier_command=("execution/verify_operator_core_source_to_skill_system.py",),
        role="source-to-system",
    ),
    Surface(
        name="System-audit",
        route="system-audit",
        canonical=ROOT / ".agent" / "workflows" / "system-audit.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-system-audit" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "system-audit" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-system-audit" / "SKILL.md",
        sync_command=("execution/sync_operator_core_system_audit.py", "--check"),
        verifier_command=("execution/verify_operator_core_system_audit.py",),
        role="control-plane repair",
    ),
    Surface(
        name="Repeatability-spine",
        route="repeatability-spine",
        canonical=ROOT / ".agent" / "workflows" / "repeatability-spine.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-repeatability-spine" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "repeatability-spine" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-repeatability-spine" / "SKILL.md",
        sync_command=("execution/sync_operator_core_repeatability_spine.py", "--check"),
        verifier_command=("execution/verify_operator_core_repeatability_spine.py",),
        role="regression repair",
    ),
    Surface(
        name="Expert-composition-governor",
        route="expert-composition-governor",
        canonical=ROOT / ".agent" / "workflows" / "expert-composition-governor.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-expert-composition-governor" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "expert-composition-governor" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-expert-composition-governor" / "SKILL.md",
        sync_command=("execution/sync_operator_core_expert_composition_governor.py", "--check"),
        verifier_command=("execution/verify_operator_core_expert_composition_governor.py",),
        role="composition gate",
    ),
    Surface(
        name="Extraction-governor-agent",
        route="extraction-governor-agent",
        canonical=ROOT / ".agent" / "workflows" / "extraction-governor-agent.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-extraction-governor-agent" / "SKILL.md",
        global_skill=Path.home() / ".codex" / "skills" / "extraction-governor-agent" / "SKILL.md",
        global_wrapper=Path.home() / ".codex" / "skills" / "source-command-extraction-governor-agent" / "SKILL.md",
        sync_command=("execution/sync_operator_core_extraction_governor_agent.py", "--check"),
        verifier_command=("execution/verify_operator_core_extraction_governor_agent.py",),
        role="source triage",
    ),
    Surface(
        name="AI Employee OS",
        route="ai-employee-os",
        canonical=ROOT / ".agent" / "workflows" / "ai-employee-os.md",
        local_wrapper=ROOT / ".agents" / "skills" / "source-command-ai-employee-os" / "SKILL.md",
        global_skill=None,
        global_wrapper=None,
        sync_command=None,
        verifier_command=("execution/verify_operator_core_ai_employee_os.py", "--skip-skill-validation"),
        role="company-agent operating layer",
        scope="workspace-local",
    ),
)

NEXT_AUDIT_CANDIDATE = {
    "route": "excellence-evaluation-lab",
    "reason": "AI Employee OS now has local Operator Core proof; next leverage is golden-task evaluation and regression preservation.",
}


def run_command(command: tuple[str, ...]) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, *command],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return {
        "command": " ".join(command),
        "status": "PASS" if completed.returncode == 0 else "FAIL",
        "returncode": completed.returncode,
        "output_tail": "\n".join(completed.stdout.strip().splitlines()[-8:]),
    }


def skipped_command(label: str) -> dict[str, Any]:
    return {
        "command": label,
        "status": "PASS",
        "returncode": 0,
        "output_tail": "not required for workspace-local surface",
    }


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def rel_optional(path: Path | None) -> str:
    if path is None:
        return "not-required"
    return rel(path)


def wrapper_status(surface: Surface) -> dict[str, bool]:
    return {
        "canonical": surface.canonical.exists(),
        "local_wrapper": surface.local_wrapper.exists(),
        "global_skill": True if surface.global_skill is None else surface.global_skill.exists(),
        "global_wrapper": True if surface.global_wrapper is None else surface.global_wrapper.exists(),
    }


def inspect_surface(surface: Surface, run_checks: bool = False) -> dict[str, Any]:
    wrappers = wrapper_status(surface)
    if run_checks:
        sync = skipped_command("workspace-local; no global sync") if surface.sync_command is None else run_command(surface.sync_command)
        verifier = run_command(surface.verifier_command)
    else:
        sync = skipped_command("fast snapshot; use --full to run sync subprocesses")
        verifier = skipped_command("fast snapshot; use --full to run verifier subprocesses")
    missing = [name for name, present in wrappers.items() if not present]
    status = "PASS" if not missing and sync["status"] == "PASS" and verifier["status"] == "PASS" else "FAIL"
    return {
        "name": surface.name,
        "route": surface.route,
        "role": surface.role,
        "scope": surface.scope,
        "status": status,
        "canonical": rel(surface.canonical),
        "local_wrapper": rel(surface.local_wrapper),
        "global_skill": rel_optional(surface.global_skill),
        "global_wrapper": rel_optional(surface.global_wrapper),
        "wrappers": wrappers,
        "missing": missing,
        "sync": sync,
        "verifier": verifier,
    }


def build_dashboard(run_checks: bool = False) -> dict[str, Any]:
    surfaces = [inspect_surface(surface, run_checks=run_checks) for surface in SURFACES]
    failing = [surface for surface in surfaces if surface["status"] != "PASS"]
    return {
        "summary": {
            "status": "PASS" if not failing else "FAIL",
            "aligned": len(surfaces) - len(failing),
            "total": len(surfaces),
            "failing": [surface["route"] for surface in failing],
            "next_audit_candidate": NEXT_AUDIT_CANDIDATE,
            "mode": "full" if run_checks else "fast-snapshot",
        },
        "surfaces": surfaces,
    }


def render_plain(dashboard: dict[str, Any]) -> str:
    summary = dashboard["summary"]
    lines = [
        "# Operator Core Status",
        "",
        f"Overall: {summary['status']}",
        f"Aligned: {summary['aligned']}/{summary['total']}",
        f"Mode: {summary['mode']}",
        f"Next audit candidate: /{summary['next_audit_candidate']['route']} - {summary['next_audit_candidate']['reason']}",
        "",
        "| Surface | Role | Sync | Verifier | Wrappers | Canonical |",
        "|---|---|---|---|---|---|",
    ]
    for surface in dashboard["surfaces"]:
        wrappers = surface["wrappers"]
        wrapper_label = "ok" if all(wrappers.values()) else "missing " + ", ".join(surface["missing"])
        if surface["scope"] == "workspace-local" and wrapper_label == "ok":
            wrapper_label = "workspace-local ok"
        lines.append(
            "| /{route} | {role} | {sync} | {verifier} | {wrappers} | {canonical} |".format(
                route=surface["route"],
                role=surface["role"],
                sync=surface["sync"]["status"],
                verifier=surface["verifier"]["status"],
                wrappers=wrapper_label,
                canonical=surface["canonical"],
            )
        )
    if summary["failing"]:
        lines.extend(["", "## Failures"])
        for surface in dashboard["surfaces"]:
            if surface["status"] == "PASS":
                continue
            lines.append(f"- /{surface['route']}: sync={surface['sync']['status']}, verifier={surface['verifier']['status']}, missing={', '.join(surface['missing']) or 'none'}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Show Operator Core wrapper alignment status.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--plain", action="store_true", help="Print readable dashboard.")
    parser.add_argument("--full", action="store_true", help="Run per-surface sync and verifier subprocesses.")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero when any surface fails.")
    args = parser.parse_args()

    dashboard = build_dashboard(run_checks=args.full)
    if args.json:
        print(json.dumps(dashboard, indent=2, sort_keys=True))
    else:
        print(render_plain(dashboard))
    return 1 if args.strict and dashboard["summary"]["status"] != "PASS" else 0


if __name__ == "__main__":
    raise SystemExit(main())
