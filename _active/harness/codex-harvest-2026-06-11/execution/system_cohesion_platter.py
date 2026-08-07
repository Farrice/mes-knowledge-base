#!/usr/bin/env python3
"""Build the weekly system-cohesion Silver Platter.

This is a workspace-local collector. It does not introduce a new command
surface for the operator; recurring_ops.py calls it from weekly-system-pulse.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOC_REPORT_DIR = ROOT / "docs" / "pulse-reports" / "system-cohesion"
AGENT_REPORT_DIR = ROOT / ".agent" / "recurring-reports" / "system-cohesion"
METADATA_SUFFIX = ".metadata.json"
SILVER_RENDER_DATA_MAP = (
    ROOT
    / "skills"
    / "mark-kashef-silver-platter-agentic-os"
    / "scripts"
    / "render_data_map.py"
)
SILVER_RENDER_OPPORTUNITIES = (
    ROOT
    / "skills"
    / "mark-kashef-silver-platter-agentic-os"
    / "scripts"
    / "render_opportunities.py"
)
DEFAULT_CHECK_TIMEOUT = 120
CONTROL_PLANE_CHECK_TIMEOUT = 300


@dataclass
class Check:
    label: str
    command: list[str]
    returncode: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0

    @property
    def status(self) -> str:
        return "PASS" if self.ok else "FAIL"

    @property
    def text(self) -> str:
        return self.stdout or self.stderr or "No output."


def run_check(label: str, command: list[str], timeout: int = DEFAULT_CHECK_TIMEOUT) -> Check:
    try:
        proc = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
        return Check(
            label=label,
            command=command,
            returncode=proc.returncode,
            stdout=proc.stdout.strip(),
            stderr=proc.stderr.strip(),
        )
    except FileNotFoundError as exc:
        return Check(label, command, 127, "", str(exc))
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout if isinstance(exc.stdout, str) else ""
        stderr = exc.stderr if isinstance(exc.stderr, str) else ""
        message = stderr.strip() or f"Timed out after {timeout}s: {' '.join(command)}"
        return Check(label, command, 124, stdout.strip(), message)


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def clip(text: str, limit: int = 2200) -> str:
    text = text.strip() or "No output."
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "\n\n[truncated]"


def summarize_findings(checks: list[Check]) -> dict[str, Any]:
    failed = [check for check in checks if not check.ok]
    activation = next((check for check in checks if check.label == "Activation Governor Plan"), None)
    routing = next((check for check in checks if check.label == "Routing Scoreboard"), None)
    health = next((check for check in checks if check.label == "System Health"), None)
    protocol = next((check for check in checks if check.label == "Protocol Audit"), None)
    return {
        "all_passed": not failed,
        "failed_labels": [check.label for check in failed],
        "activation_excerpt": clip(activation.text, 900) if activation else "Activation governor not available yet.",
        "routing_excerpt": clip(routing.text, 900) if routing else "Routing scoreboard not available.",
        "health_excerpt": clip(health.text, 900) if health else "System health not available.",
        "protocol_excerpt": clip(protocol.text, 900) if protocol else "Protocol audit not available.",
    }


def build_data_map(checks: list[Check], generated_at: str) -> dict[str, Any]:
    summary = summarize_findings(checks)
    today = date.today().isoformat()
    pantry = [
        {
            "id": "control-plane-verifiers",
            "tool": "Control-plane verifiers",
            "format": "Python checks",
            "cadence": "weekly-system-pulse",
            "feeds": ["route-health-summary", "validation-summary"],
            "status": "active",
            "explanation": "Proof spine for routing, Autopilot, skill-system, and harness health.",
        },
        {
            "id": "routing-intelligence",
            "tool": "Routing Intelligence",
            "format": ".agent/routing-intelligence.json",
            "cadence": "continuous when routes log usage",
            "feeds": ["misroute-ledger", "activation-summary"],
            "status": "active",
            "explanation": "Shows route usage, feedback, unused experts, and ensemble capture gaps.",
        },
        {
            "id": "protocol-tracker",
            "tool": "Protocol Tracker",
            "format": "directive metadata",
            "cadence": "weekly audit",
            "feeds": ["activation-summary"],
            "status": "active",
            "explanation": "Separates active, dormant, stale, and never-activated protocols.",
        },
        {
            "id": "system-health",
            "tool": "System Health",
            "format": "quick health report",
            "cadence": "daily and weekly",
            "feeds": ["activation-summary", "repair-queue"],
            "status": "active",
            "explanation": "Summarizes blockers such as Skill Evolution thresholds and telemetry gaps.",
        },
        {
            "id": "activation-governor",
            "tool": "Activation Governor",
            "format": "supervised queue",
            "cadence": "daily health and weekly pulse",
            "feeds": ["repair-queue"],
            "status": "active" if any(check.label == "Activation Governor Plan" and check.ok for check in checks) else "missing",
            "explanation": "Turns dormant assets into approval-gated next actions without fake activation.",
        },
    ]
    prep = [
        {
            "id": "route-health-summary",
            "name": "Route Health Summary",
            "sources": ["control-plane-verifiers"],
            "status": "ready" if summary["all_passed"] else "needs-repair",
            "sample_content": "Control-plane checks passed." if summary["all_passed"] else ", ".join(summary["failed_labels"]),
            "explanation": "Keeps front-door routing visible and test-backed.",
        },
        {
            "id": "misroute-ledger",
            "name": "Misroute Ledger",
            "sources": ["routing-intelligence"],
            "status": "ready",
            "sample_content": summary["routing_excerpt"],
            "explanation": "Shows routes that need correction or proof.",
        },
        {
            "id": "activation-summary",
            "name": "Activation Summary",
            "sources": ["routing-intelligence", "protocol-tracker", "system-health", "activation-governor"],
            "status": "ready",
            "sample_content": summary["activation_excerpt"],
            "explanation": "Turns dormant protocols, unused experts, and blocked evolution into a supervised queue.",
        },
        {
            "id": "validation-summary",
            "name": "Validation Summary",
            "sources": ["control-plane-verifiers", "system-health"],
            "status": "ready" if summary["all_passed"] else "needs-repair",
            "sample_content": summary["health_excerpt"],
            "explanation": "Keeps the weekly report tied to proof rather than vibes.",
        },
    ]
    plate = [
        {
            "id": "operator-readout",
            "name": "Operator Readout",
            "reads_from": ["route-health-summary", "activation-summary", "validation-summary"],
            "status": "ready",
            "sample_output": f"Weekly System Cohesion Platter, {today}",
            "explanation": "One scan-first readout for what is firing, what is dormant, and what to fix next.",
        },
        {
            "id": "repair-queue",
            "name": "Repair Queue",
            "reads_from": ["activation-summary", "misroute-ledger"],
            "status": "ready",
            "sample_output": "Ranked workspace-local repair moves with proof commands.",
            "explanation": "Makes the system recommend the next move instead of asking Farrice to remember tools.",
        },
    ]
    opportunities = [
        {
            "surface": "prep/route-health-summary",
            "type": "repair",
            "title": "Keep front-door-choice routing under regression guard",
            "explanation": "The user-bottleneck prompts must keep routing to /autopilot first.",
            "estimated_impact": "High",
            "claude_code_feature": "Verifier",
        },
        {
            "surface": "prep/activation-summary",
            "type": "automation",
            "title": "Promote real activation moves through the governor queue",
            "explanation": "Dormant protocols and unused experts should become supervised work items, not prettier metrics.",
            "estimated_impact": "High",
            "claude_code_feature": "Hook",
        },
        {
            "surface": "plate/operator-readout",
            "type": "summary",
            "title": "Read one weekly cohesion platter instead of checking scattered tools",
            "explanation": "Weekly pulse becomes the coordination layer across routing, audit, activation, and Silver Platter outputs.",
            "estimated_impact": "Medium",
            "claude_code_feature": "Skill",
        },
    ]
    return {
        "business": {
            "name": "Codex Antigravity System",
            "archetype": "internal_operator_system",
            "one_liner": "One workspace-local operating tree for intent, routing, activation, verification, and weekly repair.",
            "stack_summary": "Pantry evidence flows into Prep summaries, then Plate outputs Farrice can act on without choosing from a tool pile.",
            "generated_at": generated_at,
        },
        "pantry": pantry,
        "prep": prep,
        "plate": plate,
        "opportunities": opportunities,
        "recipes": [
            {
                "headline": "Weekly Cohesion Pulse",
                "goal": "Show what fired, what misrouted, what stayed dormant, and what to repair next.",
                "stack": ["weekly-system-pulse", "system-cohesion-platter", "activation-governor"],
                "after": "Run the top repair through /autopilot or Mission OS.",
            }
        ],
        "setup_priority": [
            {
                "title": "route_front_door_choice",
                "title_friendly": "Keep /autopilot as the tool-choice front door",
                "what_to_do": "Run the routing verifiers and protect the two real-world prompts.",
                "working_when": "Both command surfaces and the governor choose /autopilot first.",
            },
            {
                "title": "activation_governor_queue",
                "title_friendly": "Turn activation debt into a supervised queue",
                "what_to_do": "Review activation_governor.py plan output during daily health and weekly pulse.",
                "working_when": "Dormant protocols, unused experts, and Skill Evolution blockers have ranked next actions.",
            },
            {
                "title": "weekly_cohesion_platter",
                "title_friendly": "Read one weekly system-cohesion platter",
                "what_to_do": "Use the weekly pulse report as the operating readout.",
                "working_when": "The report names route health, activation gaps, proof status, and the next move.",
            },
        ],
        "interaction_layer": [
            {
                "entrypoint": "/autopilot",
                "role": "front door",
                "behavior": "intent lock, route choice, support gates, and approval checkpoint",
            },
            {
                "entrypoint": "weekly-system-pulse",
                "role": "recurring spine",
                "behavior": "renders the weekly cohesion platter without a new command to remember",
            },
        ],
    }


def checks_for_run() -> list[Check]:
    checks = [
        run_check(
            "Control Plane",
            [sys.executable, "execution/verify_system_control_plane.py"],
            timeout=CONTROL_PLANE_CHECK_TIMEOUT,
        ),
        run_check("Autopilot Routing", [sys.executable, "execution/verify_autopilot_routing.py"]),
        run_check("System Health", [sys.executable, "execution/system_health.py", "--quick"]),
        run_check("Protocol Audit", [sys.executable, "execution/protocol_tracker.py", "audit"]),
        run_check("Routing Scoreboard", [sys.executable, "execution/routing_intelligence.py", "scoreboard"]),
        run_check("Unused Experts", [sys.executable, "execution/routing_intelligence.py", "unused"]),
        run_check(
            "Silver Platter Workspace Audit",
            [
                sys.executable,
                "skills/mark-kashef-silver-platter-agentic-os/scripts/audit_existing_folder.py",
                str(ROOT),
            ],
        ),
    ]
    if (ROOT / "execution" / "activation_governor.py").exists():
        checks.append(
            run_check(
                "Activation Governor Plan",
                [sys.executable, "execution/activation_governor.py", "plan", "--dry-run"],
            )
        )
    return checks


def render_markdown(checks: list[Check], data_map: dict[str, Any], generated_at: str) -> str:
    summary = summarize_findings(checks)
    failed = summary["failed_labels"]
    next_move = (
        "Fix failed proof checks before expanding the operating tree."
        if failed
        else "Use the activation queue to turn the highest-value dormant asset into a real routed run."
    )
    lines = [
        f"# Weekly System Cohesion Platter, {date.today().isoformat()}",
        "",
        f"**Generated**: {generated_at}",
        "",
        "## Executive Read",
        "",
        (
            "The cohesion spine is healthy at the proof layer."
            if not failed
            else "The cohesion spine found proof failures that should be repaired first."
        ),
        "",
        "## Route Health",
        "",
        "| Check | Status |",
        "|---|---|",
    ]
    for check in checks:
        lines.append(f"| {check.label} | {check.status} |")
    lines.extend(
        [
            "",
            "## Misroutes This Week",
            "",
            clip(summary["routing_excerpt"]),
            "",
            "## Dormant Protocols",
            "",
            clip(summary["protocol_excerpt"]),
            "",
            "## Activation Blockers",
            "",
            clip(summary["activation_excerpt"]),
            "",
            "## Pantry: Evidence Sources",
            "",
        ]
    )
    for item in data_map["pantry"]:
        lines.append(f"- **{item['tool']}**: {item['explanation']}")
    lines.extend(["", "## Prep: Summaries Maintained", ""])
    for item in data_map["prep"]:
        lines.append(f"- **{item['name']}**: {item['explanation']}")
    lines.extend(["", "## Plate: What Farrice Should See", ""])
    for item in data_map["plate"]:
        lines.append(f"- **{item['name']}**: {item['explanation']}")
    lines.extend(["", "## Repair Queue", ""])
    for index, item in enumerate(data_map["setup_priority"], start=1):
        lines.append(f"{index}. **{item['title_friendly']}**: {item['what_to_do']}")
    lines.extend(
        [
            "",
            "## Validation Results",
            "",
        ]
    )
    for check in checks:
        lines.extend(
            [
                f"### {check.label}",
                "",
                f"**Status**: {check.status}",
                "",
                "```text",
                clip(check.text),
                "```",
                "",
            ]
        )
    lines.extend(["## Next Week's One Move", "", next_move, ""])
    return "\n".join(lines)


def write_metadata(report_path: Path, generated_at: str, data_map_path: Path) -> Path:
    metadata = {
        "userFacingSurface": "rendered-conversation-document",
        "sourceRole": "persistence-copy",
        "externalExportRequested": False,
        "generatedAt": generated_at,
        "sourceKind": "system-cohesion-platter",
        "dataMap": rel(data_map_path),
    }
    metadata_path = report_path.with_name(report_path.name + METADATA_SUFFIX)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    return metadata_path


def render_sidecars(data_map_path: Path, html_path: Path, opportunities_path: Path) -> list[Check]:
    checks: list[Check] = []
    if SILVER_RENDER_DATA_MAP.exists():
        checks.append(
            run_check(
                "Render Data Map",
                [sys.executable, str(SILVER_RENDER_DATA_MAP), "--input", str(data_map_path), "--output", str(html_path)],
            )
        )
    if SILVER_RENDER_OPPORTUNITIES.exists():
        checks.append(
            run_check(
                "Render Opportunities",
                [
                    sys.executable,
                    str(SILVER_RENDER_OPPORTUNITIES),
                    "--input",
                    str(data_map_path),
                    "--output",
                    str(opportunities_path),
                ],
            )
        )
    return checks


def run(dry_run: bool = False, json_only: bool = False) -> dict[str, Any]:
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    stamp = date.today().isoformat()
    checks = checks_for_run()
    data_map = build_data_map(checks, generated_at)
    markdown = render_markdown(checks, data_map, generated_at)
    report_path = DOC_REPORT_DIR / f"{stamp}-system-cohesion-platter.md"
    data_map_path = AGENT_REPORT_DIR / f"{stamp}-data_map.json"
    html_path = AGENT_REPORT_DIR / f"{stamp}-data_map.html"
    opportunities_path = AGENT_REPORT_DIR / f"{stamp}-opportunities.md"
    metadata_path = report_path.with_name(report_path.name + METADATA_SUFFIX)
    render_checks: list[Check] = []

    if not dry_run:
        DOC_REPORT_DIR.mkdir(parents=True, exist_ok=True)
        AGENT_REPORT_DIR.mkdir(parents=True, exist_ok=True)
        report_path.write_text(markdown, encoding="utf-8")
        data_map_path.write_text(json.dumps(data_map, indent=2) + "\n", encoding="utf-8")
        metadata_path = write_metadata(report_path, generated_at, data_map_path)
        render_checks = render_sidecars(data_map_path, html_path, opportunities_path)

    result = {
        "status": "pass" if all(check.ok for check in checks + render_checks) else "fail",
        "dry_run": dry_run,
        "generated_at": generated_at,
        "report_path": rel(report_path),
        "metadata_path": rel(metadata_path),
        "data_map_path": rel(data_map_path),
        "html_path": rel(html_path),
        "opportunities_path": rel(opportunities_path),
        "checks": [
            {
                "label": check.label,
                "status": check.status,
                "returncode": check.returncode,
                "command": check.command,
            }
            for check in checks + render_checks
        ],
        "markdown": markdown,
        "data_map": data_map,
    }
    if json_only:
        print(json.dumps({k: v for k, v in result.items() if k not in {"markdown"}}, indent=2))
    else:
        print(markdown)
        mode = "would be written" if dry_run else "written"
        print(f"\nReport {mode}: {report_path}")
        print(f"Data map {mode}: {data_map_path}")
        if not dry_run:
            print(f"Metadata written: {metadata_path}")
            print(f"HTML written: {html_path}")
            print(f"Opportunities written: {opportunities_path}")
    return result


def verify() -> int:
    result = run(dry_run=True, json_only=True)
    failures = []
    required_sections = [
        "## Executive Read",
        "## Route Health",
        "## Activation Blockers",
        "## Pantry: Evidence Sources",
        "## Prep: Summaries Maintained",
        "## Plate: What Farrice Should See",
        "## Repair Queue",
        "## Validation Results",
    ]
    markdown = result.get("markdown", "")
    for section in required_sections:
        if section not in markdown:
            failures.append(f"missing report section: {section}")
    data_map = result.get("data_map", {})
    for key in ("business", "pantry", "prep", "plate", "opportunities", "setup_priority"):
        if not data_map.get(key):
            failures.append(f"missing data_map key: {key}")
    if failures:
        print("System cohesion platter verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("System cohesion platter verification passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the weekly system-cohesion Silver Platter.")
    sub = parser.add_subparsers(dest="command")
    run_parser = sub.add_parser("run", help="Collect signals and render the platter.")
    run_parser.add_argument("--dry-run", action="store_true", help="Print without writing files.")
    run_parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    verify_parser = sub.add_parser("verify", help="Verify report/data-map shape using dry-run collection.")
    verify_parser.add_argument("--json", action="store_true", help="Accepted for script parity; ignored.")
    parser.add_argument("--dry-run", action="store_true", help="Print without writing files.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    if args.command == "verify":
        return verify()
    if args.command == "run":
        run(dry_run=args.dry_run, json_only=args.json)
        return 0
    run(dry_run=args.dry_run, json_only=args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
