#!/usr/bin/env python3
"""Operator Cockpit V2 for Codex Antigravity.

This command is the chat-first, command-backed surface for meaningful work:
it renders the Intent Confidence Packet, current cockpit status, local
friction capture, retrieval home, proof plan, and global mirror checkpoint.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
EXECUTION = ROOT / "execution"
sys.path.insert(0, str(EXECUTION))

import artifact_router  # type: ignore  # noqa: E402
import autopilot_runtime_preflight as preflight  # type: ignore  # noqa: E402
import friction_ledger  # type: ignore  # noqa: E402
import routing_governor  # type: ignore  # noqa: E402
import savant_control_room  # type: ignore  # noqa: E402


PROJECT = "operator-cockpit-v2"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def ensure_project_home() -> dict[str, Any]:
    project_dir = ROOT / "_active" / PROJECT
    created: list[str] = []
    for folder in artifact_router.STANDARD_PROJECT_DIRS:
        path = project_dir / folder
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(str(path))
    index_path = project_dir / "INDEX.md"
    if not index_path.exists():
        index_path.write_text(
            "# Operator Cockpit V2\n\n"
            "## Purpose\n"
            "Chat-first and command-backed operating cockpit for non-trivial Codex Antigravity work.\n\n"
            "## Use\n"
            "- Run `python3 execution/operator_cockpit.py --intent \"<raw request>\" --plain` before meaningful work.\n"
            "- New system artifacts for this lane live under `06-system/`.\n"
            "- Cleanup and migration plans are staged under `_system/organization/`; no broad moves happen automatically.\n",
            encoding="utf-8",
        )
        created.append(str(index_path))
    return {
        "project": PROJECT,
        "path": str(project_dir),
        "system_path": str(project_dir / "06-system"),
        "created": created,
    }


def latest_backlog_map() -> str:
    backlog_dir = artifact_router.ORG_DIR / "backlog-maps"
    if not backlog_dir.exists():
        return ""
    maps = sorted(backlog_dir.glob("*-backlog-map.md"))
    return str(maps[-1]) if maps else ""


def organization_snapshot(refresh: bool) -> dict[str, Any]:
    if refresh:
        result = artifact_router.write_backlog_map()
        result["refreshed"] = True
        return result
    return {
        "refreshed": False,
        "map_path": latest_backlog_map(),
        "plan_path": "",
        "safe": "",
        "ambiguous": "",
        "blocked": "",
        "skipped": "",
    }


def friction_candidates(intent: str, data: dict[str, Any], room: dict[str, Any]) -> list[dict[str, Any]]:
    lowered = intent.lower()
    packet = data["intent_confidence_packet"]
    route = packet["chosen_route"]
    owner = packet.get("owner", "")
    status = data["execution_decision"]["status"]
    candidates: list[dict[str, Any]] = []

    def add(kind: str, trigger: str, failure_class: str, summary: str, next_action: str) -> None:
        event_id = friction_ledger.stable_event_id(kind, route, trigger, summary)
        candidates.append(
            {
                "event_id": event_id,
                "kind": kind,
                "severity": "P1" if kind in {"misroute", "retrieval-failure"} else "P2",
                "route": route,
                "summary": summary,
                "evidence": intent[:500],
                "next_action": next_action,
                "trigger": trigger,
                "failure_class": failure_class,
                "user_signal": intent[:500],
                "source_session": "operator-cockpit-v2",
                "owner": owner,
                "status": "captured",
            }
        )

    if routing_governor.is_operator_cockpit_rebuild_intent(intent):
        add(
            "user-struggle",
            "operator-cockpit-rebuild-signal",
            "operator-friction",
            "User described engineering debt, unclear intent capture, or cockpit rebuild pressure.",
            "Use /system-audit with the Operator Cockpit V2 confidence packet and proof plan.",
        )
    if any(term in lowered for term in ("can't find", "cannot find", "find what i need", "random numbers", "folders")):
        add(
            "retrieval-failure",
            "retrieval-overload",
            "organization-retrieval",
            "User described local retrieval or file organization failure.",
            "Refresh artifact backlog map and place new work under the project-first home.",
        )
    if status == "Needs judgment":
        add(
            "needs-judgment",
            "confidence-packet-open-questions",
            "unanswered-intent",
            "The v2 confidence packet has unanswered questions before meaningful work.",
            "Pause mutation and answer the packet questions before execution.",
        )
    if room.get("summary", {}).get("harness_status") == "STALE":
        add(
            "stale-recommendation",
            "cockpit-status-stale",
            "stale-proof",
            "Cockpit status is usable but stale.",
            "Run fast proof and refresh only the stale anchor that blocks the chosen route.",
        )
    if route != "system-audit" and routing_governor.is_operating_alignment_intent(intent):
        add(
            "misroute",
            "operating-alignment-wrong-owner",
            "route-owner",
            "Operating-alignment intent did not land on /system-audit.",
            "Repair routing_governor and Autopilot golden prompts for operating-alignment.",
        )
    return candidates


def capture_friction(candidates: list[dict[str, Any]], enabled: bool) -> dict[str, Any]:
    captured: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    if not enabled:
        return {"enabled": False, "captured": captured, "skipped": candidates}
    for event in candidates:
        if friction_ledger.event_exists(event["event_id"]):
            skipped.append({**event, "skip_reason": "already captured"})
            continue
        captured.append(friction_ledger.append_event(event))
    return {"enabled": True, "captured": captured, "skipped": skipped}


def build_cockpit(intent: str, *, capture: bool = True, refresh_organization: bool = False) -> dict[str, Any]:
    project_home = ensure_project_home()
    data = preflight.build_preflight(intent)
    room = savant_control_room.build_control_room()
    org = organization_snapshot(refresh_organization)
    candidates = friction_candidates(intent, data, room)
    friction = capture_friction(candidates, capture)
    return {
        "schema_version": "operator-cockpit/v2",
        "generated_at": now_iso(),
        "intent": intent,
        "project_home": project_home,
        "preflight": data,
        "cockpit_status": {
            "overall": room["summary"]["overall"],
            "safe_to_use": room["summary"]["safe_to_use"],
            "harness_status": room["summary"]["harness_status"],
            "broken": room["summary"]["broken"],
            "stale": room["summary"]["stale"],
            "next_move": room["summary"]["next_move"],
            "routing_feedback": room["routing_intelligence"]["total_feedback"],
            "ensemble_rate": room["routing_intelligence"]["ensemble_rate"],
        },
        "organization": org,
        "friction": friction,
        "global_mirror_checkpoint": {
            "status": "proposal-only",
            "boundary": "No global ~/.codex writes until local proof passes and Farrice explicitly approves the mirror.",
            "candidate_surfaces": [
                "/Users/farricecain/.codex/AGENTS.md",
                "/Users/farricecain/.codex/skills/autopilot/SKILL.md",
                "/Users/farricecain/.codex/skills/source-command-autopilot/SKILL.md",
                "/Users/farricecain/.codex/skills/system-audit/SKILL.md",
                "/Users/farricecain/.codex/skills/source-command-system-audit/SKILL.md",
                "/Users/farricecain/.codex/skills/health-check/SKILL.md",
                "/Users/farricecain/.codex/skills/source-command-health-check/SKILL.md",
            ],
        },
    }


def fmt(values: list[Any]) -> str:
    return ", ".join(str(value) for value in values if value) or "None"


def render_plain(cockpit: dict[str, Any]) -> str:
    packet = cockpit["preflight"]["intent_confidence_packet"]
    decision = cockpit["preflight"]["execution_decision"]
    status = cockpit["cockpit_status"]
    friction = cockpit["friction"]
    org = cockpit["organization"]
    mirror = cockpit["global_mirror_checkpoint"]

    captured = friction.get("captured", [])
    skipped = friction.get("skipped", [])

    lines = [
        "# Operator Cockpit V2",
        "",
        f"Generated: {cockpit['generated_at']}",
        "",
        "## Intent Confidence Packet",
        f"- Goal: {packet['goal']}",
        f"- Audience: {packet['audience']}",
        f"- Success criteria: {packet['success_criteria']}",
        f"- Non-trivial reason: {fmt(packet['non_trivial_reason'])}",
        f"- Confidence: {packet['confidence']}/100",
        f"- Questions: {fmt(packet['questions'])}",
        f"- Chosen route: /{packet['chosen_route']}",
        f"- Support gates: {fmt('/' + gate for gate in packet['support_gates'])}",
        f"- Arsenal policy: {packet['arsenal_policy']}",
        f"- Proof plan: {fmt(packet['proof_plan'])}",
        f"- Retrieval home: {packet['retrieval_home']['path']}",
        f"- Pause or run: {packet['pause_or_run']['status']} - {packet['pause_or_run']['reason']}",
        "",
        "## Cockpit Status",
        f"- Overall: {status['overall']}",
        f"- Safe to use: {'yes' if status['safe_to_use'] else 'no'}",
        f"- Harness: {status['harness_status']}",
        f"- Broken: {fmt(status['broken'])}",
        f"- Stale: {fmt(status['stale'])}",
        f"- Routing feedback entries: {status['routing_feedback']}",
        f"- Ensemble rate: {status['ensemble_rate']}%",
        f"- Recorded next move: {status['next_move'] or 'None'}",
        "",
        "## Friction Capture",
        f"- Enabled: {'yes' if friction['enabled'] else 'no'}",
        f"- Captured now: {len(captured)}",
        f"- Already captured/skipped: {len(skipped)}",
    ]
    for event in captured[:5]:
        lines.append(f"- Captured `{event['event_id']}`: {event['failure_class']} -> {event['next_action']}")
    for event in skipped[:5]:
        if event.get("skip_reason"):
            lines.append(f"- Skipped `{event['event_id']}`: {event['skip_reason']}")

    lines.extend(
        [
            "",
            "## Retrieval",
            f"- Project home: {cockpit['project_home']['path']}",
            f"- System path: {cockpit['project_home']['system_path']}",
            f"- Backlog map: {org.get('map_path') or 'not generated yet'}",
            f"- Cleanup plan: {org.get('plan_path') or 'run with --refresh-organization to generate'}",
            f"- Refreshed this run: {'yes' if org.get('refreshed') else 'no'}",
            "",
            "## Next Action",
            f"- {decision['first_action']}",
            "",
            "## Global Mirror Checkpoint",
            f"- Status: {mirror['status']}",
            f"- Boundary: {mirror['boundary']}",
            f"- Candidate surfaces: {fmt(mirror['candidate_surfaces'])}",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render the Operator Cockpit V2 packet.")
    parser.add_argument("--intent", required=True, help="Raw request or work intent to preflight.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--plain", action="store_true", help="Print readable cockpit output.")
    parser.add_argument("--no-capture", action="store_true", help="Do not append local friction events.")
    parser.add_argument("--refresh-organization", action="store_true", help="Generate a dated backlog map and staged cleanup plan.")
    args = parser.parse_args()

    cockpit = build_cockpit(
        args.intent,
        capture=not args.no_capture,
        refresh_organization=args.refresh_organization,
    )
    if args.json:
        print(json.dumps(cockpit, indent=2, ensure_ascii=False))
    else:
        print(render_plain(cockpit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
