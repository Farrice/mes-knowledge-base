#!/usr/bin/env python3
"""Read-only operating status for the Codex Antigravity harness."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / ".agent"

sys.path.insert(0, str(ROOT / "execution"))

import command_menu  # type: ignore  # noqa: E402
import friction_ledger  # type: ignore  # noqa: E402
import protocol_tracker  # type: ignore  # noqa: E402
import routing_governor  # type: ignore  # noqa: E402
import workflow_router  # type: ignore  # noqa: E402


ROUTING_PROBES = (
    ("control_plane_audit", "audit Autopilot control-plane routing drift", "system-audit"),
    ("end_session_closeout", "end session handoff closeout intelligence", "end-session"),
    ("session_wrap", "wrap this session", "end-session"),
    ("contextual_next_prompts", "three next prompts after final answer", "steering-compass"),
    ("focused_handoff", "prepare a handoff document for a fresh agent to continue this in another conversation", "handoff"),
    ("expert_composition", "expert soup too many agents full arsenal", "expert-composition-governor"),
    ("extraction_governance", "source-command-extraction-governor-agent route this source into reusable capability", "extraction-governor-agent"),
    ("ai_employee_os", "AI employee memory isolation shared integrations", "ai-employee-os"),
)


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except json.JSONDecodeError:
        return {"_error": f"invalid JSON: {path.relative_to(ROOT)}"}


def read_jsonl_count(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8", errors="ignore").splitlines() if line.strip())


def parse_dt(value: str) -> datetime | None:
    if not value:
        return None
    normalized = value.strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        try:
            parsed = datetime.strptime(value.strip(), "%Y-%m-%d %H:%M")
        except ValueError:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def age_label(value: str) -> str:
    parsed = parse_dt(value)
    if not parsed:
        return "unknown"
    delta = datetime.now(timezone.utc) - parsed
    hours = round(delta.total_seconds() / 3600, 1)
    if hours < 48:
        return f"fresh ({hours}h old)"
    days = round(hours / 24, 1)
    return f"stale ({days}d old)"


def route_probe(query: str, expected: str) -> dict[str, Any]:
    workflows = command_menu.build_index()
    menu = [workflow.name for _, workflow in command_menu.search(workflows, query, 8)]
    router = [workflow["name"] for _, workflow in workflow_router.search_workflows(query, 8)]
    decision = routing_governor.evaluate(query, menu, router)
    return {
        "query": query,
        "expected": expected,
        "menu_first": menu[0] if menu else "",
        "router_first": router[0] if router else "",
        "governor": decision.chosen_route,
        "lane": decision.detected_lane,
        "pass": bool(menu and router and menu[0] == expected and router[0] == expected and decision.chosen_route == expected),
    }


def latest_report_path() -> str:
    report_dir = AGENT / "recurring-reports"
    reports = sorted(report_dir.glob("*session-closeout-intelligence.md"))
    return str(reports[-1].relative_to(ROOT)) if reports else ""


def build_status() -> dict[str, Any]:
    intent = read_json(AGENT / "intent-memory" / "current.json")
    cohesion = read_json(AGENT / "system-cohesion-state.json")
    receipt = read_json(AGENT / "run-receipts" / "latest.json")
    routing_data = read_json(AGENT / "routing-intelligence.json")
    friction_summary = friction_ledger.summarize(friction_ledger.read_events())
    protocols = protocol_tracker.audit_protocols()
    probes = {name: route_probe(query, expected) for name, query, expected in ROUTING_PROBES}

    intent_goal = intent.get("active_intent", {}).get("goal", "")
    cohesion_goal = cohesion.get("active_intent", {}).get("goal", "")
    mission = cohesion.get("mission", {}) or intent.get("mission", {})
    weekly = cohesion.get("weekly_platter", {})
    verifier_status = cohesion.get("verifier_status", {})
    routing_decisions = routing_data.get("routing_decisions", [])
    feedback_log = routing_data.get("feedback_log", [])
    feedback_inbox = read_jsonl_count(AGENT / "routing-feedback-inbox.jsonl")
    performance_log = read_jsonl_count(AGENT / "performance-log.jsonl")

    broken = []
    stale = []
    working = []
    if intent_goal and cohesion_goal and intent_goal == cohesion_goal:
        working.append("intent memory and cohesion state agree")
    else:
        broken.append("intent memory and cohesion state do not agree")
    if mission.get("slug"):
        working.append(f"active mission recorded: {mission.get('slug')}")
    else:
        stale.append("no active mission recorded")
    if weekly.get("last_generated_at") and "stale" in age_label(str(weekly.get("last_generated_at"))):
        stale.append("weekly platter timestamp is stale")
    if all(item["pass"] for item in probes.values()):
        working.append("routing probes pass")
    else:
        broken.append("one or more routing probes failed")

    next_move = cohesion.get("next_move", {}).get("action") or intent.get("next_move", {}).get("action") or ""
    if not next_move:
        next_move = "Run /autopilot with raw context; use /system-audit for control-plane repairs."

    return {
        "summary": {
            "status": "broken" if broken else "stale" if stale else "working",
            "working": working,
            "stale": stale,
            "broken": broken,
            "next_move": next_move,
        },
        "intent_memory": {
            "path": ".agent/intent-memory/current.json",
            "updated_at": intent.get("updated_at", ""),
            "age": age_label(str(intent.get("updated_at", ""))),
            "goal": intent_goal,
            "route": intent.get("route", {}).get("chosen_route", ""),
            "next_move": intent.get("next_move", {}).get("action", ""),
        },
        "cohesion_state": {
            "path": ".agent/system-cohesion-state.json",
            "updated_at": cohesion.get("updated_at", ""),
            "age": age_label(str(cohesion.get("updated_at", ""))),
            "goal": cohesion_goal,
            "route": cohesion.get("chosen_route", {}).get("route", ""),
            "support_gates": cohesion.get("support_gates", []),
            "verifier_status": verifier_status,
            "weekly_platter": weekly,
        },
        "mission": {
            "slug": mission.get("slug", ""),
            "state_path": mission.get("state_path", ""),
            "status": mission.get("status", "") or "no active mission",
        },
        "latest_run_receipt": {
            "path": ".agent/run-receipts/latest.json",
            "timestamp": receipt.get("timestamp", ""),
            "age": age_label(str(receipt.get("timestamp", ""))),
            "route": receipt.get("route", ""),
            "status": receipt.get("status", ""),
            "next_action": receipt.get("next_action", ""),
        },
        "friction_ledger": friction_summary,
        "end_session": {
            "latest_report": latest_report_path(),
            "routing_decisions": len(routing_decisions),
            "routing_feedback": len(feedback_log),
            "routing_feedback_inbox": feedback_inbox,
            "performance_log_entries": performance_log,
        },
        "routing_health": probes,
        "protocols": {
            "total": protocols.get("total_protocols"),
            "activated_ever": protocols.get("activated_protocols"),
            "active_recent": protocols.get("active_protocols"),
            "healthy": protocols.get("healthy_protocols"),
            "dormant": protocols.get("dormant_protocols"),
            "cold_source_only": protocols.get("cold_source_only_protocols"),
            "overdue": protocols.get("overdue_protocols"),
            "deprecated": protocols.get("deprecated_protocols"),
        },
    }


def fmt_list(values: list[str]) -> str:
    return ", ".join(values) if values else "none"


def render_plain(status: dict[str, Any]) -> str:
    summary = status["summary"]
    receipt = status["latest_run_receipt"]
    end_session = status["end_session"]
    protocols = status["protocols"]
    probes = status["routing_health"]
    mission = status["mission"]
    lines = [
        "# Harness Status",
        "",
        f"Overall: {summary['status'].upper()}",
        f"Working: {fmt_list(summary['working'])}",
        f"Stale: {fmt_list(summary['stale'])}",
        f"Broken: {fmt_list(summary['broken'])}",
        f"Next move: {summary['next_move']}",
        "",
        "## Current State",
        f"- Intent: {status['intent_memory']['goal'] or 'empty'} ({status['intent_memory']['age']})",
        f"- Route: /{status['cohesion_state']['route'] or status['intent_memory']['route'] or 'none'}",
        f"- Mission: {mission['status']}",
        f"- Weekly platter: {status['cohesion_state']['weekly_platter'].get('status', 'unknown')} ({age_label(str(status['cohesion_state']['weekly_platter'].get('last_generated_at', '')))})",
        "",
        "## Latest Proof",
        f"- Run receipt: /{receipt['route'] or 'none'} / {receipt['status'] or 'unknown'} ({receipt['age']})",
        f"- Run receipt next action: {receipt['next_action'] or 'none'}",
        "- Savant Control Room: python3 execution/savant_control_room.py --plain",
        "- Fast proof: python3 execution/operator_core_fast_proof.py --plain",
        f"- Friction events: {status['friction_ledger']['events']}",
        f"- End-session: {end_session['routing_decisions']} routing decisions, {end_session['routing_feedback']} feedback entries, {end_session['routing_feedback_inbox']} inbox items",
        f"- Latest closeout report: {end_session['latest_report'] or 'none'}",
        "",
        "## Routing Health",
    ]
    for name, probe in probes.items():
        verdict = "PASS" if probe["pass"] else "FAIL"
        lines.append(
            f"- {name}: {verdict} (menu=/{probe['menu_first']}, router=/{probe['router_first']}, governor=/{probe['governor']}, lane={probe['lane']})"
        )
    lines.extend(
        [
            "",
            "## Protocols",
            f"- Total: {protocols['total']}; activated ever: {protocols['activated_ever']}; active recent: {protocols['active_recent']}; healthy: {protocols['healthy']}; dormant: {protocols['dormant']}; overdue: {protocols['overdue']}; cold/source-only: {protocols['cold_source_only']}",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Show a read-only Codex Antigravity harness status.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--plain", action="store_true", help="Print the readable status view.")
    args = parser.parse_args()

    status = build_status()
    if args.json:
        print(json.dumps(status, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print(render_plain(status))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
