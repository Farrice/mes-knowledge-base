#!/usr/bin/env python3
"""Compile messy operator intent into a Codex-ready run packet.

The bridge is a companion layer over Autopilot and Virtuoso. It does not
replace routing; it packages the existing launchpad, route, composition, first
action, and verifier evidence into one object a future Codex turn can execute.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXECUTION = ROOT / "execution"
if str(EXECUTION) not in sys.path:
    sys.path.insert(0, str(EXECUTION))

import co_creative_launchpad  # type: ignore  # noqa: E402
import virtuoso_orchestration  # type: ignore  # noqa: E402


MODE_CHOICES = ("auto", "revenue", "creative", "system")
VIRTUOSO_MODE = {
    "auto": None,
    "revenue": "revenue",
    "creative": "creative",
    "system": "build",
}

RAW_BRIDGE_SIGNALS = (
    "/raw-intent-bridge",
    "raw-intent-bridge",
    "intent bridge",
    "raw intent",
    "rough intent",
    "messy context",
    "messy notes",
    "do not know how to ask codex",
    "don't know how to ask codex",
    "how to ask codex",
    "prompt engineer",
    "virtuoso bridge",
    "run packet",
    "translate initially",
    "full capabilities",
    "get the full capabilities",
    "bridge or layer",
    "companion layer",
)

SOURCE_SYSTEM_SIGNALS = (
    "skill",
    "source-to-skill",
    "source to skill",
    "skill system",
    "workflow bridge",
    "companion layer",
    "contract doc",
    "run packet",
    "plugin later",
)

REVENUE_SIGNALS = (
    "money",
    "revenue",
    "offer",
    "client",
    "clients",
    "paid",
    "monetize",
    "first dollar",
    "make income",
)

CREATIVE_SIGNALS = (
    "creative",
    "campaign",
    "content",
    "visual",
    "brand",
    "world-class",
    "world class",
    "taste",
)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def strip_command_prefix(value: str) -> str:
    return re.sub(
        r"^\s*(?:/raw-intent-bridge|raw-intent-bridge|source-command-raw-intent-bridge)\b[:\s-]*",
        "",
        value,
        flags=re.IGNORECASE,
    ).strip() or value.strip()


def has_any(value: str, terms: tuple[str, ...]) -> bool:
    return any(term in value for term in terms)


def is_bridge_intent(raw_intent: str) -> bool:
    q = normalize(raw_intent)
    return has_any(q, RAW_BRIDGE_SIGNALS) or (
        "codex" in q and "intent" in q and ("bridge" in q or "packet" in q)
    )


def route_for_packet(raw_intent: str, mode: str, virtuoso: dict[str, Any]) -> str:
    q = normalize(raw_intent)
    route = str(virtuoso.get("primary_route") or "autopilot")
    if route == "raw-intent-bridge":
        route = "system-audit" if any(term in q for term in ("audit", "repair", "broken", "not working")) else "autopilot"
    if mode == "revenue":
        return route if route in {"first-10k", "revenue-offer-agent", "client-acquire"} else "first-10k"
    if mode == "creative":
        return route if route not in {"plugin-readiness-audit"} else "autopilot"
    if mode == "system" or (is_bridge_intent(raw_intent) and has_any(q, SOURCE_SYSTEM_SIGNALS)):
        return "source-to-skill-system"
    if route == "plugin-readiness-audit" and is_bridge_intent(raw_intent):
        return "source-to-skill-system"
    if has_any(q, REVENUE_SIGNALS):
        return route if route in {"first-10k", "revenue-offer-agent", "client-acquire"} else "first-10k"
    if has_any(q, CREATIVE_SIGNALS):
        return route if route not in {"plugin-readiness-audit"} else "autopilot"
    if is_bridge_intent(raw_intent):
        return "autopilot"
    return route


def support_for_packet(chosen_route: str, virtuoso: dict[str, Any]) -> list[str]:
    gates = [gate for gate in virtuoso.get("support_gates", []) if gate and gate != chosen_route]
    if chosen_route == "source-to-skill-system":
        ordered = [
            "autopilot",
            "virtuoso",
            "extraction-governor-agent",
            "expert-composition-governor",
            "knowledge-librarian",
        ]
    elif chosen_route in {"first-10k", "revenue-offer-agent", "client-acquire"}:
        ordered = [
            "revenue-offer-agent",
            "client-acquire",
            "service-first-productization",
            "publishable-copy-gate",
            "red-team-agent",
        ]
    elif chosen_route in {"campaign", "creative-brief-gen", "content-media-agent", "high-taste-writing-os"}:
        ordered = ["high-taste-writing-os", "publishable-copy-gate", "excellence-gate"]
    else:
        ordered = ["orchestrate", "routing-intelligence", "knowledge-librarian"]

    merged: list[str] = []
    for gate in ordered + gates:
        if gate and gate != chosen_route and gate not in merged:
            merged.append(gate)
    return merged


def owner_for_route(route: str, virtuoso: dict[str, Any]) -> str:
    if route == virtuoso.get("primary_route"):
        return str(virtuoso.get("owner") or route)
    return {
        "source-to-skill-system": "Source To Skill System",
        "autopilot": "Autopilot",
        "first-10k": "First 10K Revenue System",
        "campaign": "Campaign",
        "high-taste-writing-os": "High Taste Writing OS",
    }.get(route, route.replace("-", " ").title())


def composition_slots(chosen_route: str, support_gates: list[str], virtuoso: dict[str, Any]) -> list[dict[str, str]]:
    if chosen_route == virtuoso.get("primary_route") and virtuoso.get("composition_slots"):
        return list(virtuoso["composition_slots"])
    owner = owner_for_route(chosen_route, virtuoso)
    mechanism = f"/{support_gates[0]}" if support_gates else "planned verifier"
    risk_gate = "python3 execution/verify_raw_intent_run_packet.py"
    if "publishable-copy-gate" in support_gates:
        risk_gate = "/publishable-copy-gate"
    elif "routing-intelligence" in support_gates:
        risk_gate = "/routing-intelligence"
    return [
        {
            "slot": "Spine",
            "asset": owner,
            "job": f"Own the final outcome through /{chosen_route}.",
            "evidence": f"chosen_route=/{chosen_route}",
        },
        {
            "slot": "Differentiator",
            "asset": "Raw Intent Virtuoso Bridge",
            "job": "Translate rough operator language into a runnable Codex packet before normal execution.",
            "evidence": "raw intent bridge trigger plus Launchpad packet",
        },
        {
            "slot": "Mechanism",
            "asset": mechanism,
            "job": "Turn packet fields into route, gates, context plan, and first safe action.",
            "evidence": ", ".join(f"/{gate}" for gate in support_gates) or "no support gates",
        },
        {
            "slot": "Craft",
            "asset": "/virtuoso trace",
            "job": "Make the route, composition, plugin surface, and proof visible as one coherent handoff.",
            "evidence": "execution/virtuoso_orchestration.py",
        },
        {
            "slot": "Risk Gate",
            "asset": risk_gate,
            "job": "Prevent generic advice, plugin-first drift, external writes, and unrelated creative-route capture.",
            "evidence": "cold-start fixtures in verify_raw_intent_run_packet.py",
        },
    ]


def context_plan(chosen_route: str, mode: str) -> dict[str, Any]:
    return {
        "hot": [
            "execution/raw_intent_run_packet.py",
            "semantic_libraries/antigravity/primitives/raw-intent-virtuoso-bridge-contract.md",
            "execution/co_creative_launchpad.py",
            "execution/virtuoso_orchestration.py",
            ".agent/workflows/autopilot.md",
        ],
        "on_demand": [
            ".agent/workflows/source-to-skill-system.md",
            ".agents/skills/source-command-virtuoso/SKILL.md",
            "execution/routing_governor.py",
            "execution/workflow_router.py",
            "execution/plugin_readiness_audit.py",
        ],
        "cold": [
            "full migrated command library",
            "plugin marketplace files",
            "global ~/.codex mirrors",
        ],
        "skip": [
            "external writes",
            "plugin marketplace edits",
            "global ~/.codex writes during normal packet runs",
            "real Codex subagents",
            "destructive cleanup",
        ],
        "mode": mode,
        "handoff": f"Use /{chosen_route} with the packet fields; load only the support gate needed for the next step.",
    }


def operator_run_prompt(chosen_route: str, raw_intent: str, mode: str) -> str:
    if chosen_route == "source-to-skill-system":
        return (
            "/source-to-skill-system build this as a Google-local companion layer, "
            "using the Raw Intent Virtuoso Bridge packet and no plugin/global writes: "
            f"{raw_intent}"
        )
    if chosen_route == "autopilot":
        return f"/autopilot compile this raw intent into a run packet, then execute the first safe local action: {raw_intent}"
    if mode in {"revenue", "creative"}:
        return f"/virtuoso --mode {mode} {raw_intent}"
    return f"/{chosen_route} {raw_intent}"


def plugin_packaging_verdict() -> dict[str, str]:
    return {
        "status": "deferred",
        "target": "antigravity-operator-core",
        "reason": "Package only after local cold-start proof passes for revenue, creative, system, and regression fixtures.",
        "next_check": "python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate",
        "v1_boundary": "No plugin marketplace edits, no new plugin, and no unapproved global ~/.codex writes.",
    }


def verification_plan(chosen_route: str, mode: str, virtuoso: dict[str, Any]) -> list[str]:
    checks = [
        "python3 execution/verify_raw_intent_global_skill.py",
        "python3 execution/verify_raw_intent_bridge_command.py",
        "python3 execution/verify_raw_intent_run_packet.py",
        f"python3 execution/routing_governor.py evaluate {json.dumps('raw intent virtuoso bridge ' + chosen_route)}",
        "python3 execution/verify_autopilot_runtime_preflight.py",
        "python3 execution/verify_virtuoso_orchestration.py",
        "python3 execution/verify_google_operator_core.py",
    ]
    for check in virtuoso.get("verification_plan", []):
        if check not in checks:
            checks.append(check)
    if mode == "auto":
        checks.append("python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate")
    return checks


def _goal_spine(intent_text: str) -> dict[str, str]:
    """Match the intent to a standing goal in .agent/cos/goals.json (maestro
    parity with /go Stage 0). Compass, never cage: an ORPHAN flag is one line
    of visibility, execution always proceeds."""
    goals_path = ROOT / ".agent" / "cos" / "goals.json"
    try:
        goals = json.loads(goals_path.read_text()).get("goals", [])
    except (OSError, ValueError):
        return {"serves": "unknown", "note": "goals.json unreadable"}
    q = normalize(intent_text)
    for goal in goals:
        if goal.get("status") != "active":
            continue
        for thread in goal.get("threads", []):
            if thread and thread.replace("-", " ") in q:
                return {"serves": goal["id"], "note": f"thread match: {thread}"}
    for goal in goals:
        if goal.get("status") != "active":
            continue
        tokens = [t for t in re.findall(r"[a-z]{4,}", normalize(goal.get("target", ""))) if t in q]
        if len(tokens) >= 2:
            return {"serves": goal["id"], "note": f"target match: {', '.join(tokens[:3])}"}
    return {"serves": "orphan", "note": "no active goal matched — flag only, execute fully"}


def _log_mission(packet: dict[str, Any]) -> None:
    """Append the compiled mission to .agent/missions.jsonl so /pulse-board and
    COS see Codex missions too (cross-platform operator-console parity)."""
    import datetime
    line = {
        "ts": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "mission": packet["raw_intent"][:160],
        "serves": packet["mission_card"]["serves"],
        "pattern": f"codex-bridge/{packet['chosen_route']}",
        "tier": packet["mission_card"]["tier"],
        "status": "compiled",
        "outcome": "",
        "platform": "codex",
    }
    try:
        with open(ROOT / ".agent" / "missions.jsonl", "a") as fh:
            fh.write(json.dumps(line, ensure_ascii=False) + "\n")
    except OSError:
        pass  # logging must never block a packet compile


def build_packet(raw_intent: str, mode: str = "auto") -> dict[str, Any]:
    if mode not in MODE_CHOICES:
        raise ValueError(f"mode must be one of {', '.join(MODE_CHOICES)}")
    intent_text = strip_command_prefix(raw_intent)
    virtuoso = virtuoso_orchestration.build_virtuoso(
        intent_text,
        mode_bias=VIRTUOSO_MODE[mode],
        trace_only=False,
    )
    chosen_route = route_for_packet(intent_text, mode, virtuoso)
    lane = str(virtuoso.get("preflight_summary", {}).get("lane") or "general")
    support_gates = support_for_packet(chosen_route, virtuoso)
    launchpad = co_creative_launchpad.build_launchpad(
        intent_text,
        route=chosen_route,
        lane=lane,
        risk_reasons=[],
    )
    decision = dict(virtuoso.get("execution_decision") or {})
    if chosen_route != virtuoso.get("primary_route") and decision.get("status") == "Trace only":
        decision["status"] = "Running now"
    decision.setdefault("status", "Running now")
    decision.setdefault("safe_to_run", decision["status"] == "Running now")
    decision.setdefault("approval_needed", "No extra approval needed for local packet compilation.")
    decision.setdefault("risk_reasons", [])
    if decision.get("risk_reasons") == ["co-creative launchpad pause"] and not launchpad["questions_that_change_execution"]:
        decision["risk_reasons"] = []
        decision["safe_to_run"] = True
        decision["status"] = "Running now"

    packet = {
        "schema_version": "raw-intent-run-packet/v1",
        "raw_intent": intent_text,
        "mode": mode,
        "predicted_need": launchpad["predicted_need"],
        "center": launchpad["center"],
        "success_standard": launchpad["success_standard"],
        "constraints": launchpad["constraints"],
        "missing_inputs": launchpad["missing_inputs"],
        "questions_that_change_execution": launchpad["questions_that_change_execution"],
        "chosen_route": chosen_route,
        "route_owner": owner_for_route(chosen_route, virtuoso),
        "support_gates": support_gates,
        "composition_slots": composition_slots(chosen_route, support_gates, virtuoso),
        "context_plan": context_plan(chosen_route, mode),
        "execution_decision": decision,
        "first_safe_action": operator_run_prompt(chosen_route, intent_text, mode),
        "verification_plan": verification_plan(chosen_route, mode, virtuoso),
        "operator_run_prompt": operator_run_prompt(chosen_route, intent_text, mode),
        "mission_card": {
            **_goal_spine(intent_text),
            "tier": "T2 waiting" if launchpad["questions_that_change_execution"] else "T1 auto",
        },
        "plugin_packaging_verdict": plugin_packaging_verdict(),
        "virtuoso_trace": {
            "primary_route": virtuoso.get("primary_route"),
            "owner": virtuoso.get("owner"),
            "meta_intent": virtuoso.get("meta_intent"),
            "support_gates": virtuoso.get("support_gates", []),
            "recommended_stack": virtuoso.get("recommended_stack", {}),
            "execution_decision": virtuoso.get("execution_decision", {}),
        },
    }
    return packet


def fmt_list(values: list[Any]) -> str:
    return ", ".join(str(value) for value in values if str(value)) or "None"


def render_plain(packet: dict[str, Any]) -> str:
    card = packet.get("mission_card", {})
    lines = [
        "## Raw Intent Run Packet",
        f"- **Mode**: {packet['mode']}",
        f"- **Serves**: {card.get('serves', '?')} ({card.get('note', '')}) · **Tier**: {card.get('tier', '?')}",
        f"- **Chosen route**: /{packet['chosen_route']} ({packet['route_owner']})",
        f"- **Predicted need**: {packet['predicted_need']}",
        f"- **Center**: {packet['center']}",
        f"- **What good looks like**: {packet['success_standard']}",
        f"- **Constraints**: {fmt_list(packet['constraints'])}",
        f"- **Missing inputs**: {fmt_list(packet['missing_inputs'])}",
        f"- **Questions that change execution**: {fmt_list(packet['questions_that_change_execution'])}",
        f"- **Support gates**: {fmt_list(['/' + gate for gate in packet['support_gates']])}",
        "",
        "## Context Plan",
        f"- **Hot**: {fmt_list(packet['context_plan']['hot'])}",
        f"- **On demand**: {fmt_list(packet['context_plan']['on_demand'])}",
        f"- **Cold**: {fmt_list(packet['context_plan']['cold'])}",
        f"- **Skip**: {fmt_list(packet['context_plan']['skip'])}",
        f"- **Handoff**: {packet['context_plan']['handoff']}",
        "",
        "## Composition Slots",
    ]
    for slot in packet["composition_slots"]:
        lines.append(f"- **{slot['slot']}**: {slot['asset']} — {slot['job']}")
    decision = packet["execution_decision"]
    verdict = packet["plugin_packaging_verdict"]
    lines.extend(
        [
            "",
            "## Execution",
            f"- **Decision**: {decision.get('status')}",
            f"- **Approval needed**: {decision.get('approval_needed')}",
            f"- **First safe action**: {packet['first_safe_action']}",
            f"- **Operator run prompt**: {packet['operator_run_prompt']}",
            "",
            "## Verification",
            f"- **Checks**: {fmt_list(packet['verification_plan'])}",
            "",
            "## Plugin Packaging",
            f"- **Verdict**: {verdict['status']} for `{verdict['target']}`",
            f"- **Reason**: {verdict['reason']}",
            f"- **Boundary**: {verdict['v1_boundary']}",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile raw intent into a Codex run packet.")
    parser.add_argument("intent", nargs="+", help="Raw intent or messy context.")
    parser.add_argument("--mode", choices=MODE_CHOICES, default="auto")
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--json", action="store_true")
    output.add_argument("--plain", action="store_true")
    args = parser.parse_args()

    packet = build_packet(" ".join(args.intent), mode=args.mode)
    _log_mission(packet)
    if args.json:
        print(json.dumps(packet, indent=2, ensure_ascii=False))
    else:
        print(render_plain(packet))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
