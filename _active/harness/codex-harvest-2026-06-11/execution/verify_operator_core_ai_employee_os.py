#!/usr/bin/env python3
"""Verify the local Operator Core hardening contract for /ai-employee-os."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
EXECUTION = ROOT / "execution"
sys.path.insert(0, str(EXECUTION))

import command_menu  # type: ignore  # noqa: E402
import routing_governor  # type: ignore  # noqa: E402
import workflow_router  # type: ignore  # noqa: E402


AI_EMPLOYEE_QUERY = "AI employee memory isolation shared integrations"
COMPANY_AGENT_QUERY = "company agent proactive workflow suggestions"
LEAKAGE_QUERY = "audit this agent for memory leakage"

REQUIRED_PATHS = {
    "workflow": ROOT / ".agent" / "workflows" / "ai-employee-os.md",
    "local_skill": ROOT / ".agents" / "skills" / "source-command-ai-employee-os" / "SKILL.md",
    "source_command": ROOT / ".claude" / "commands" / "ai-employee-os.md",
    "contract": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "ai-employee-operating-contract.md",
    "source_skill": ROOT / "skills" / "fryderyk-wiatrowski-ai-employee-os" / "SKILL.md",
    "evidence_map": ROOT / "extractions" / "video-context" / "ohKt066uFhg" / "evidence-map.md",
    "uncertainty_report": ROOT / "extractions" / "video-context" / "ohKt066uFhg" / "uncertainty-report.md",
}

WORKFLOW_SNIPPETS = (
    "semantic_libraries/antigravity/primitives/ai-employee-operating-contract.md",
    "skills/fryderyk-wiatrowski-ai-employee-os/SKILL.md",
    "extractions/video-context/ohKt066uFhg/evidence-map.md",
    "context/access map",
    "Integration map",
    "Event semantics",
    "Trust ladder",
    "Regression guard",
    "Human checkpoint",
    "Validation",
    "Cold-Start Proof",
)

LOCAL_SKILL_SNIPPETS = (
    "Read and execute the workflow at `.agent/workflows/ai-employee-os.md`",
    "memory-isolated",
    "shared integration",
    "proactive workflow",
    "model/personality regression",
)

CONTRACT_SNIPPETS = (
    "An AI employee earns scope",
    "Context map",
    "Memory policy",
    "Integration map",
    "Event ledger",
    "Proactivity ladder",
    "Trust/personality guard",
    "Rollout stage",
)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def command_menu_first(query: str) -> str:
    matches = command_menu.search(command_menu.build_index(), query, 8)
    return matches[0][1].name if matches else ""


def workflow_router_first(query: str) -> str:
    matches = workflow_router.search_workflows(query, 8)
    return str(matches[0][1]["name"]) if matches else ""


def governor_decision(query: str) -> routing_governor.GovernorDecision:
    menu_routes = [item[1].name for item in command_menu.search(command_menu.build_index(), query, 8)]
    workflow_routes = [str(item[1]["name"]) for item in workflow_router.search_workflows(query, 8)]
    return routing_governor.evaluate(query, menu_routes, workflow_routes)


def run_validate_skill(skill_name: str) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, "execution/validate_skill.py", skill_name],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return {
        "skill": skill_name,
        "status": "PASS" if completed.returncode == 0 else "FAIL",
        "returncode": completed.returncode,
        "output_tail": "\n".join(completed.stdout.strip().splitlines()[-6:]),
    }


def inspect_ai_employee_os(run_skill_validation: bool = False) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    for label, path in REQUIRED_PATHS.items():
        checks.append(
            {
                "name": f"path:{label}",
                "status": "PASS" if path.exists() else "FAIL",
                "detail": str(path.relative_to(ROOT)),
            }
        )

    workflow = read_text(REQUIRED_PATHS["workflow"])
    local_skill = read_text(REQUIRED_PATHS["local_skill"])
    contract = read_text(REQUIRED_PATHS["contract"])

    for snippet in WORKFLOW_SNIPPETS:
        checks.append(
            {
                "name": f"workflow_snippet:{snippet}",
                "status": "PASS" if snippet in workflow else "FAIL",
                "detail": "workflow source truth includes required AI employee contract language",
            }
        )

    for snippet in LOCAL_SKILL_SNIPPETS:
        checks.append(
            {
                "name": f"local_skill_snippet:{snippet}",
                "status": "PASS" if snippet in local_skill else "FAIL",
                "detail": "local command wrapper stays thin and discoverable",
            }
        )

    for snippet in CONTRACT_SNIPPETS:
        checks.append(
            {
                "name": f"contract_snippet:{snippet}",
                "status": "PASS" if snippet in contract else "FAIL",
                "detail": "semantic primitive preserves employee safety contract",
            }
        )

    routing_checks = (
        ("command_menu", AI_EMPLOYEE_QUERY, command_menu_first(AI_EMPLOYEE_QUERY), "ai-employee-os"),
        ("workflow_router", COMPANY_AGENT_QUERY, workflow_router_first(COMPANY_AGENT_QUERY), "ai-employee-os"),
    )
    for label, query, actual, expected in routing_checks:
        checks.append(
            {
                "name": f"routing:{label}",
                "status": "PASS" if actual == expected else "FAIL",
                "detail": f"{query!r} -> /{actual or 'none'}",
            }
        )

    decision = governor_decision(LEAKAGE_QUERY)
    checks.append(
        {
            "name": "routing:governor_lane",
            "status": "PASS" if decision.detected_lane == "ai-employee-os" else "FAIL",
            "detail": f"lane={decision.detected_lane}; route=/{decision.chosen_route}",
        }
    )
    checks.append(
        {
            "name": "routing:governor_route",
            "status": "PASS" if decision.chosen_route == "ai-employee-os" else "FAIL",
            "detail": f"lane={decision.detected_lane}; route=/{decision.chosen_route}",
        }
    )

    validations: list[dict[str, Any]] = []
    if run_skill_validation:
        validations = [
            run_validate_skill("source-command-ai-employee-os"),
            run_validate_skill("fryderyk-wiatrowski-ai-employee-os"),
        ]
        for validation in validations:
            checks.append(
                {
                    "name": f"validate_skill:{validation['skill']}",
                    "status": validation["status"],
                    "detail": validation["output_tail"],
                }
            )

    failures = [check for check in checks if check["status"] != "PASS"]
    return {
        "summary": {
            "status": "PASS" if not failures else "FAIL",
            "checks": len(checks),
            "failures": len(failures),
            "scope": "workspace-local",
            "global_mirror": "not_required_without_explicit_approval",
        },
        "checks": checks,
        "validations": validations,
    }


def render_plain(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# AI Employee OS Operator Core Verification",
        "",
        f"Overall: {summary['status']}",
        f"Scope: {summary['scope']}",
        f"Global mirror: {summary['global_mirror']}",
        f"Checks: {summary['checks']} total; {summary['failures']} failing",
        "",
        "## Checks",
    ]
    for check in report["checks"]:
        lines.append(f"- {check['status']}: {check['name']} ({check['detail']})")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify local /ai-employee-os Operator Core hardening.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--skip-skill-validation", action="store_true", help="Skip validate_skill subprocess checks.")
    args = parser.parse_args()

    report = inspect_ai_employee_os(run_skill_validation=not args.skip_skill_validation)
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_plain(report))
    return 0 if report["summary"]["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
