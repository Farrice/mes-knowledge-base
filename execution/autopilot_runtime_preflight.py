#!/usr/bin/env python3
"""Deterministic Autopilot intent-to-outcome preflight.

This is the live trace layer for the upgraded Autopilot contract. It chooses a
route, classifies the execution posture, attaches outcome recipes/capability
evidence, and prints the run prompt or proof plan before meaningful work.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent.parent
EXECUTION = ROOT / "execution"

sys.path.insert(0, str(EXECUTION))

import command_menu  # type: ignore  # noqa: E402
import co_creative_launchpad  # type: ignore  # noqa: E402
import context_retriever  # type: ignore  # noqa: E402
import expert_router  # type: ignore  # noqa: E402
import protocol_tracker  # type: ignore  # noqa: E402
import recommend_stack  # type: ignore  # noqa: E402
import routing_audit  # type: ignore  # noqa: E402
import routing_governor  # type: ignore  # noqa: E402
import tool_router  # type: ignore  # noqa: E402
import workflow_router  # type: ignore  # noqa: E402
from outcome_recipes import classify_outcome  # type: ignore  # noqa: E402


RUNNING_TEXT = "Running safe workspace-local execution now after this trace."
PLAN_ONLY_TEXT = "Plan only: execution intentionally paused by mode."
RISK_BLOCK_TEXT = "Blocked by risk gate before execution."
JUDGMENT_TEXT = "Needs Farrice judgment before execution."

SAFE_LOCAL_POLICY = (
    "safe workspace-local execution allowed after trace when the work is "
    "non-destructive, additive or reversible, clear enough, and inside Codex Antigravity."
)

DEFAULT_HOT_ROUTES = (
    "autopilot",
    "system-audit",
    "end-session",
    "repeatability-spine",
    "mission",
    "orchestrate",
    "extraction-governor-agent",
    "expert-composition-governor",
    "source-to-skill-system",
    "knowledge-librarian",
    "self-evolve",
    "skill-anneal",
    "routing-intelligence",
    "health-check",
    "artifact-router",
)

OWNER_BY_ROUTE = {
    "autopilot": "Operator Autopilot",
    "system-audit": "System Audit",
    "routing-intelligence": "Routing Intelligence",
    "health-check": "Health Check",
    "mission": "Mission OS",
    "orchestrate": "Antigravity Orchestrator",
    "self-evolve": "Evolution Agent",
    "skill-anneal": "Skill Anneal",
    "repeatability-spine": "Repeatability Spine",
    "expert-composition-governor": "Expert Composition Governor",
    "source-to-skill-system": "Source-To-Skill System",
    "extraction-governor-agent": "Extraction Governor",
    "knowledge-librarian": "Knowledge Librarian",
    "plugin-readiness-audit": "Plugin Readiness Audit",
    "deep-research-os": "Deep Research OS",
    "research-intelligence-agent": "Research Intelligence Agent",
    "kishotenketsu-contrast-storytelling": "Kishotenketsu Contrast Storytelling",
    "first-10k": "First 10K Revenue System",
    "revenue-offer-agent": "Revenue Offer Agent",
    "client-acquire": "Client Acquisition",
}

RAW_INTENT_BRIDGE_SIGNALS = (
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
    "run packet",
    "virtuoso bridge",
    "bridge or layer",
    "companion layer",
    "full capabilities",
    "translate initially",
)

RAW_INTENT_SOURCE_SYSTEM_SIGNALS = (
    "source-to-skill",
    "source to skill",
    "skill system",
    "workflow bridge",
    "companion layer",
    "contract doc",
    "plugin later",
    "plugin phase",
    "plugin packaging",
)

RAW_INTENT_BUILD_SIGNALS = (
    "build",
    "implement",
    "create",
    "add",
    "update",
    "wire",
    "compiler",
)


def is_raw_intent_bridge_query(query: str) -> bool:
    q = query.lower()
    return any(signal in q for signal in RAW_INTENT_BRIDGE_SIGNALS) or (
        "codex" in q and "intent" in q and ("bridge" in q or "packet" in q)
    )


def raw_intent_bridge_route(query: str) -> str | None:
    q = query.lower()
    if not is_raw_intent_bridge_query(query):
        return None
    explicit_system = any(signal in q for signal in RAW_INTENT_SOURCE_SYSTEM_SIGNALS)
    build_bridge = any(signal in q for signal in RAW_INTENT_BUILD_SIGNALS) and (
        "bridge" in q or "run packet" in q or "raw intent" in q
    )
    if explicit_system or build_bridge:
        return "source-to-skill-system"
    return "autopilot"


def raw_intent_bridge_hint(query: str, route: str, gates: list[str], lane: str, recipe_name: str) -> dict[str, Any]:
    q = query.lower()
    triggered = is_raw_intent_bridge_query(query)
    triggered = triggered or (lane in {"front-door-choice", "skill-system"} and ("codex" in q or "intent" in q))
    if not triggered:
        return {
            "status": "skipped",
            "reason": "Request is already specific enough for normal Autopilot routing.",
            "packet_command": "",
            "contract": "semantic_libraries/antigravity/primitives/raw-intent-virtuoso-bridge-contract.md",
            "preferred_route": route,
            "plugin_packaging": "deferred",
        }

    raw_route = raw_intent_bridge_route(query)
    if raw_route:
        preferred = raw_route
    elif recipe_name == "plugin-packaging" and ("raw intent" in q or "bridge" in q or "run packet" in q):
        preferred = "source-to-skill-system"
    elif lane == "revenue":
        preferred = route if route in {"first-10k", "revenue-offer-agent", "client-acquire"} else "first-10k"
    elif lane == "skill-system":
        preferred = "source-to-skill-system"
    elif lane == "front-door-choice":
        preferred = "autopilot"
    else:
        preferred = route if route not in {"plugin-readiness-audit"} else "autopilot"

    mode = "auto"
    if lane == "revenue":
        mode = "revenue"
    elif route in {"campaign", "creative-brief-gen", "content-media-agent", "high-taste-writing-os"}:
        mode = "creative"
    elif preferred == "source-to-skill-system":
        mode = "system"

    return {
        "status": "triggered",
        "reason": "Raw or under-specified Codex intent should be compiled into a run packet before execution.",
        "packet_command": f"python3 execution/raw_intent_run_packet.py {json.dumps(query)} --mode {mode} --plain",
        "contract": "semantic_libraries/antigravity/primitives/raw-intent-virtuoso-bridge-contract.md",
        "preferred_route": preferred,
        "support_gates": gates,
        "plugin_packaging": "deferred until cold-start proof passes",
    }

VERIFIERS_BY_LANE = {
    "system-failure": (
        "python3 execution/verify_autopilot_runtime_preflight.py",
        "python3 execution/verify_system_control_plane.py",
        "python3 execution/verify_autopilot_routing.py",
        "python3 execution/verify_agent_arsenal_routing.py",
    ),
    "expert-composition": (
        "python3 execution/verify_autopilot_runtime_preflight.py",
        "python3 execution/verify_expert_composition_standard.py",
        "python3 execution/verify_agent_arsenal_routing.py",
    ),
    "repeatability": (
        "python3 execution/verify_autopilot_runtime_preflight.py",
        "python3 execution/verify_repeatability_spine.py",
        "python3 execution/verify_autopilot_routing.py",
    ),
    "skill-system": (
        "python3 execution/verify_autopilot_runtime_preflight.py",
        "python3 execution/verify_skill_system_contract.py",
    ),
    "revenue": (
        "python3 execution/verify_autopilot_runtime_preflight.py",
        "python3 execution/verify_autopilot_routing.py",
        "python3 execution/routing_intelligence.py scoreboard",
    ),
    "deep-research-os": (
        "python3 execution/verify_deep_research_os.py",
        "python3 execution/research_router.py --health",
        "python3 execution/research_quality_gate.py validate [final_report.md] --strict --source-ledger [source_ledger.md]",
    ),
    "kishotenketsu-contrast-storytelling": (
        "python3 execution/validate_skill.py lucas-alpay-storytelling",
        "python3 execution/verify_behavior_changing_extraction_contract.py",
        "python3 execution/verify_skill_system_contract.py",
    ),
    "plugin-packaging": (
        "python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate",
        "python3 execution/capability_graph.py --json",
    ),
    "end-session-closeout": (
        "python3 execution/verify_end_session_intelligence.py",
        "python3 execution/verify_system_control_plane.py",
    ),
    "delegate": (
        "python3 execution/subagent_readiness.py --dry-run --json",
        "python3 execution/verify_subagent_readiness.py",
    ),
}

RISK_SIGNALS = {
    "publishing/external": (
        "publish",
        "post this",
        "send",
        "dm",
        "message",
        "outreach",
        "email them",
        "browser write",
        "connector write",
        "google docs",
        "notion write",
    ),
    "paid/budget": ("paid tool", "spend", "buy", "purchase", "apify", "budget", "charge"),
    "global/external-workspace": ("~/.codex", "global", "google antigravity", "back-port", "backport"),
    "destructive": ("delete", "remove all", "wipe", "destructive", "reset", "archive everything"),
}

JUDGMENT_SIGNALS = (
    "taste judgment",
    "my judgment",
    "approve the final",
    "pick between",
    "which one do i like",
    "needs my call",
)

SUBAGENT_SIGNALS = ("subagent", "subagents", "parallel agents", "delegate", "delegated agents")
DYNAMIC_WORKFLOW_SIGNALS = (
    "dynamic workflow",
    "workflow runtime",
    "script-held",
    "manifest-held",
    "many-file",
    "large audit",
    "codebase audit",
    "migration",
    "cross-checked",
    "multi-angle",
    "repeated verification",
)

NON_TRIVIAL_SIGNALS = (
    "build",
    "deploy",
    "implement",
    "repair",
    "audit",
    "rebuild",
    "enhance",
    "client",
    "deliverable",
    "external",
    "publish",
    "system",
    "harness",
    "workflow",
    "workflows",
    "skill",
    "skills",
    "multi-step",
    "multi step",
    "revenue",
    "creative",
    "strategy",
)


def route_names_from_command_menu(query: str, limit: int = 8) -> list[str]:
    workflows = command_menu.build_index()
    return [workflow.name for _, workflow in command_menu.search(workflows, query, limit)]


def route_names_from_workflow_router(query: str, limit: int = 8) -> list[str]:
    return [workflow["name"] for _, workflow in workflow_router.search_workflows(query, limit)]


def expert_candidates(query: str, limit: int = 5) -> list[dict[str, str]]:
    candidates = []
    for score, name, info in expert_router.route(query, top_n=limit):
        candidates.append(
            {
                "name": name,
                "domain": info.get("domain", ""),
                "owns": info.get("owns", ""),
                "use": info.get("use", ""),
                "score": f"{score:.1f}",
            }
        )
    return candidates


def context_sources(query: str, limit: int = 5) -> list[str]:
    try:
        results = context_retriever.retrieve_context(query, top_k=limit)
    except BaseException:
        return ["context_retriever unavailable; use local control-plane files directly"]
    sources = []
    for _, chunk in results[:limit]:
        source = chunk.get("source", "")
        section = chunk.get("section", "")
        label = source if not section else f"{source} :: {section}"
        sources.append(label)
    return sources


def tool_clusters(query: str) -> tuple[list[str], list[str]]:
    clusters, matched = tool_router.select_tools(query)
    matched_labels = [f"{name}:{score}" for name, score, _ in matched]
    return clusters, matched_labels


def normalize_mode(query: str, mode: str = "auto") -> str:
    lowered = query.lower()
    if mode != "auto":
        return mode
    if "--plan" in lowered:
        return "plan"
    if "--menu" in lowered or "show me the menu" in lowered or "menu of options" in lowered:
        return "menu"
    plugin_package_terms = (
        "--package",
        "plugin package",
        "plugin packaging",
        "package as plugin",
        "package into plugin",
        "marketplace package",
        "marketplace packaging",
    )
    if "plugin" in lowered or any(term in lowered for term in plugin_package_terms):
        return "package"
    if "--delegate" in lowered:
        return "delegate"
    if "--run" in lowered:
        return "run"
    return "auto"


def risk_reasons(query: str, mode: str) -> list[str]:
    lowered = query.lower()
    reasons: list[str] = []
    for label, signals in RISK_SIGNALS.items():
        if any(signal in lowered for signal in signals):
            reasons.append(label)
    if any(signal in lowered for signal in SUBAGENT_SIGNALS) and mode != "delegate":
        reasons.append("real subagents require explicit delegation")
    return reasons


def needs_judgment(query: str) -> bool:
    lowered = query.lower()
    return any(signal in lowered for signal in JUDGMENT_SIGNALS)


def needs_dynamic_workflow(query: str, lane: str, recipe_name: str) -> bool:
    lowered = query.lower()
    if any(signal in lowered for signal in DYNAMIC_WORKFLOW_SIGNALS):
        return True
    if recipe_name in {"deep-research-os", "source-to-skill"} and any(term in lowered for term in ("cross-check", "multi", "phases", "proof loop")):
        return True
    if lane in {"system-failure", "skill-system"} and any(term in lowered for term in ("large", "many", "migration", "audit", "runtime")):
        return True
    return False


def non_trivial_reasons(query: str, lane: str, route: str, recipe_name: str) -> list[str]:
    lowered = query.lower()
    reasons: list[str] = []
    if any(signal in lowered for signal in ("build", "deploy", "implement", "create", "ship")):
        reasons.append("build_or_delivery")
    if lane in {"system-failure", "skill-system", "expert-composition", "repeatability"} or route in {
        "system-audit",
        "source-to-skill-system",
        "self-evolve",
        "skill-anneal",
    }:
        reasons.append("system_or_harness_change")
    if any(signal in lowered for signal in ("client", "revenue", "publish", "external", "offer")):
        reasons.append("public_or_business_consequence")
    if any(signal in lowered for signal in ("ambiguous", "intent", "not sure", "which", "what should")):
        reasons.append("ambiguous_intent")
    if needs_dynamic_workflow(query, lane, recipe_name):
        reasons.append("multi_step_or_cross_checked")
    if routing_governor.is_operator_cockpit_rebuild_intent(query):
        reasons.append("operator_cockpit_rebuild")
    if not reasons and any(signal in lowered for signal in NON_TRIVIAL_SIGNALS):
        reasons.append("meaningful_work")
    return list(dict.fromkeys(reasons))


def retrieval_home_for(query: str, route: str, recipe_name: str) -> dict[str, str]:
    lowered = query.lower()
    if routing_governor.is_operator_cockpit_rebuild_intent(query):
        project = "operator-cockpit-v2"
        folder = "06-system"
    elif route == "system-audit" or recipe_name == "system-repair":
        project = "system-audit"
        folder = "06-system"
    elif recipe_name == "source-to-skill":
        project = "source-to-skill-system"
        folder = "06-system"
    elif any(term in lowered for term in ("client", "proposal", "handoff")):
        project = "client-delivery"
        folder = "04-deliverables"
    else:
        project = route or "autopilot"
        folder = "03-working-drafts"
    return {
        "project": project,
        "folder": folder,
        "path": f"_active/{project}/{folder}/",
        "policy": "Project-first home for new artifacts; existing backlog uses a staged map before any moves.",
    }


def read_hot_routes() -> list[str]:
    codex = ROOT / "CODEX.md"
    if not codex.exists():
        return list(DEFAULT_HOT_ROUTES)
    text = codex.read_text(encoding="utf-8", errors="ignore")
    start = text.find("Keep front doors and high-use control routes hot:")
    if start < 0:
        return list(DEFAULT_HOT_ROUTES)
    end = text.find("Keep the broad migrated command library cold", start)
    block = text[start:end] if end > start else text[start:]
    routes = re.findall(r"`/([^`]+)`", block)
    return routes or list(DEFAULT_HOT_ROUTES)


def parse_latest_efficiency_counts() -> dict[str, str]:
    path = ROOT / "deliverables" / "system-efficiency" / "system-efficiency-baseline.md"
    if not path.exists():
        return {"warm": "unknown", "cold": "unknown", "source": "not generated"}
    text = path.read_text(encoding="utf-8", errors="ignore")
    warm = re.search(r"Warm bundle candidates still on disk:\s*(\d+)", text)
    cold = re.search(r"Cold workflow count:\s*(\d+)", text)
    return {
        "warm": warm.group(1) if warm else "unknown",
        "cold": cold.group(1) if cold else "unknown",
        "source": str(path.relative_to(ROOT)),
    }


def parse_routing_audit_counts() -> dict[str, str]:
    try:
        _, summary = routing_audit.build_tiered_routing_report()
        total = int(summary["total"])
        return {
            "fully_routed": f"{summary['legacy_fully_routed']}/{total}",
            "unmeasured": str(summary["legacy_unrouted"]),
            "tiered_compliant": f"{summary['tier_compliant']}/{total}",
            "tiered_noncompliant": str(summary["tier_noncompliant"]),
            "cold_source_only": str(summary["cold_source_only"]),
            "source": "execution/routing_audit.py",
        }
    except BaseException:
        return {
            "fully_routed": "unknown",
            "unmeasured": "unknown",
            "tiered_compliant": "unknown",
            "tiered_noncompliant": "unknown",
            "cold_source_only": "unknown",
            "source": "run routing_audit.py",
        }


def protocol_counts() -> dict[str, Any]:
    try:
        report = protocol_tracker.audit_protocols()
    except BaseException:
        return {
            "activated": "unknown",
            "active": "unknown",
            "healthy": "unknown",
            "dormant": "unknown",
            "cold": "unknown",
            "overdue": "unknown",
            "deprecated": "unknown",
        }
    return {
        "activated": str(report.get("activated_protocols", report.get("active_protocols", "unknown"))),
        "active": str(report.get("active_protocols", "unknown")),
        "healthy": str(report.get("healthy_protocols", "unknown")),
        "dormant": str(report.get("dormant_protocols", "unknown")),
        "cold": str(report.get("cold_source_only_protocols", "unknown")),
        "overdue": str(report.get("overdue_protocols", report.get("zombie_protocols", "unknown"))),
        "deprecated": str(report.get("deprecated_protocols", "unknown")),
    }


def surface_classification() -> dict[str, Any]:
    hot = read_hot_routes()
    efficiency = parse_latest_efficiency_counts()
    routing = parse_routing_audit_counts()
    protocols = protocol_counts()
    workflows = list((ROOT / ".agent" / "workflows").glob("*.md"))
    live_skills = [
        path
        for path in (ROOT / ".agents" / "skills").glob("*")
        if path.is_dir() and (path / "SKILL.md").exists()
    ]
    live_command_wrappers = [path for path in live_skills if path.name.startswith("source-command-")]
    cold_wrappers = list((ROOT / ".agents" / "cold-skills" / "source-command-wrappers").glob("source-command-*"))
    return {
        "hot": hot,
        "hot_count": len(hot),
        "live_skill_count": str(len(live_skills)),
        "live_command_wrapper_count": str(len(live_command_wrappers)),
        "cold_command_wrapper_count": str(sum(1 for path in cold_wrappers if path.is_dir())),
        "warm_count": efficiency["warm"],
        "cold_count": efficiency["cold"],
        "cold_source": efficiency["source"],
        "dormant_protocols": protocols["dormant"],
        "activated_protocols": protocols["activated"],
        "active_protocols": protocols["active"],
        "healthy_protocols": protocols["healthy"],
        "cold_source_only_protocols": protocols["cold"],
        "overdue_protocols": protocols["overdue"],
        "deprecated_protocols": protocols["deprecated"],
        "fully_routed_agents": routing["fully_routed"],
        "unmeasured_agents": routing["unmeasured"],
        "tiered_routing_compliant": routing["tiered_compliant"],
        "tiered_routing_noncompliant": routing["tiered_noncompliant"],
        "cold_source_only_agents": routing["cold_source_only"],
        "routing_source": routing["source"],
        "workflow_count": len(workflows),
        "policy": "Classify before cleanup; do not delete or archive from count alone.",
    }


def clarity_score(query: str, decision: Any) -> int:
    score = 50
    if len(query.split()) >= 6:
        score += 12
    if decision.chosen_route:
        score += 15
    if decision.detected_lane != "general":
        score += 12
    if decision.confidence >= 0.85:
        score += 10
    if any(term in query.lower() for term in ("success", "prove", "verifier", "broken", "repeat", "expert soup")):
        score += 6
    return min(score, 96)


def planned_verifiers(lane: str, recipe: Any) -> list[str]:
    verifiers = list(VERIFIERS_BY_LANE.get(lane, ()))
    for verifier in recipe.verifiers:
        if verifier not in verifiers:
            verifiers.append(verifier)
    if "python3 execution/codex_harness_check.py" not in verifiers:
        verifiers.append("python3 execution/codex_harness_check.py")
    return verifiers


def support_gates(query: str, decision: Any, recipe: Any) -> list[str]:
    gates = list(decision.required_candidates[:5]) if decision.required_candidates else []
    for gate in recipe.support_gates:
        if gate not in gates:
            gates.append(gate)
    if decision.detected_lane == "front-door-choice" or raw_intent_bridge_route(query) == "autopilot":
        for gate in ("autopilot", "orchestrate"):
            if gate not in gates:
                gates.append(gate)
    if decision.detected_lane == "system-failure":
        for gate in ("system-audit", "routing-intelligence", "health-check", "friction-ledger"):
            if gate not in gates:
                gates.append(gate)
    if routing_governor.is_operator_cockpit_rebuild_intent(query):
        for gate in ("expert-composition-governor", "self-evolve", "artifact-router", "friction-ledger"):
            if gate not in gates:
                gates.append(gate)
    if decision.detected_lane == "general" and decision.chosen_route == "autopilot":
        for gate in ("routing-governor", "capability-graph", "run-receipt"):
            if gate not in gates:
                gates.append(gate)
    if any(signal in query.lower() for signal in SUBAGENT_SIGNALS):
        for gate in ("subagent-readiness", "delegation-receipt", "expert-composition-governor"):
            if gate not in gates:
                gates.append(gate)
    if needs_dynamic_workflow(query, decision.detected_lane, recipe.name):
        for gate in ("codex-dynamic-workflow", "run-receipt"):
            if gate not in gates:
                gates.append(gate)
    return gates


def classify_meta_intent(query: str, lane: str, route: str, recipe_name: str) -> str:
    if routing_governor.is_operating_alignment_intent(query):
        return "operating-alignment"
    if lane == "system-failure":
        return "control-plane-repair"
    if lane == "expert-composition":
        return "bounded-expert-composition"
    if lane == "repeatability":
        return "repeatability-repair"
    if lane == "kishotenketsu-contrast-storytelling" or route == "kishotenketsu-contrast-storytelling":
        return "kishotenketsu-contrast-storytelling"
    if recipe_name == "source-to-skill":
        return "source-to-system-build"
    return route or lane or "general"


def build_orchestration_receipt(
    *,
    query: str,
    route: str,
    owner: str,
    gates: list[str],
    stack: dict[str, Any],
    meta_intent: str,
    composition_owner: str,
    verifiers: list[str],
    posture: dict[str, Any],
    launchpad: dict[str, Any],
) -> dict[str, Any]:
    expert_lenses = [str(item) for item in stack.get("stack", []) if str(item).strip()]
    container = dict(launchpad.get("container_decision") or {})
    capability = dict(launchpad.get("capability_move") or {})
    return {
        "objective": query,
        "meta_intent": meta_intent,
        "owner": owner,
        "composition_owner": composition_owner,
        "route": route,
        "support_gates": gates,
        "expert_lenses": expert_lenses,
        "subagent_boundary": "Delegation packets only; real Codex subagents require explicit authorization.",
        "container_decision": container.get("move", "continue"),
        "capability_move": (
            capability.get("recommendation", "Continue here.")
            if capability.get("visible")
            else "Quiet execution; no capability interruption needed."
        ),
        "why_now": launchpad.get("why_now", "No material leverage fork is present."),
        "approval_boundary": launchpad.get(
            "approval_boundary",
            "None for safe, reversible workspace-local work.",
        ),
        "auto_task_creation": False,
        "verifier_results": {
            "status": "planned",
            "planned": verifiers,
            "execution_decision": posture.get("status", ""),
        },
        "feedback_hook": (
            "Use routing_intelligence.py misroute for wrong owners and friction_ledger.py "
            "for weak output, stale recommendation, missing prompt, or verifier failure."
        ),
    }


def build_intent_confidence_packet(
    *,
    query: str,
    route: str,
    owner: str,
    gates: list[str],
    verifiers: list[str],
    score: int,
    launchpad: dict[str, Any],
    posture: dict[str, Any],
    stack: dict[str, Any],
    lane: str,
    recipe_name: str,
) -> dict[str, Any]:
    reasons = non_trivial_reasons(query, lane, route, recipe_name)
    questions = list(launchpad.get("questions_that_change_execution", []))
    arsenal_policy = (
        "Full intelligence arsenal remains available on demand. For system/cockpit "
        "repair, unrelated domain experts are suppressed until /expert-composition-governor "
        "assigns a bounded slot."
    )
    if stack.get("stack"):
        arsenal_policy = (
            "Full intelligence arsenal remains available on demand. Suggested expert lenses "
            "are support evidence only; the chosen workflow owner still integrates the result."
        )
    return {
        "goal": query,
        "audience": "Farrice and the Codex Antigravity operating layer",
        "success_criteria": launchpad.get("success_standard", ""),
        "non_trivial_reason": reasons,
        "confidence": score,
        "questions": questions,
        "chosen_route": route,
        "owner": owner,
        "support_gates": gates,
        "arsenal_policy": arsenal_policy,
        "proof_plan": verifiers,
        "retrieval_home": retrieval_home_for(query, route, recipe_name),
        "pause_or_run": {
            "status": posture.get("status", ""),
            "reason": posture.get("approval_needed", ""),
            "safe_to_run": posture.get("safe_to_run", False),
        },
    }


def choose_effective_route(mode: str, query: str, decision: Any, recipe: Any, menu_routes: list[str]) -> str:
    if mode == "menu":
        return "orchestrate"
    if decision.detected_lane == "deep-research-os" or recipe.name == "deep-research-os":
        return decision.chosen_route or "deep-research-os"
    bridge_route = raw_intent_bridge_route(query)
    if bridge_route:
        return bridge_route
    if mode == "package" or recipe.name == "plugin-packaging":
        return "plugin-readiness-audit"
    if recipe.name == "system-repair" and routing_governor.is_system_audit_query(query):
        return "system-audit"
    return decision.chosen_route or recipe.primary_route or (menu_routes[0] if menu_routes else "autopilot")


def execution_decision(
    query: str,
    mode: str,
    score: int,
    route: str,
    launchpad: dict[str, Any] | None = None,
) -> dict[str, Any]:
    risks = risk_reasons(query, mode)
    if mode == "plan":
        return {
            "status": "Plan only",
            "first_action": PLAN_ONLY_TEXT,
            "approval_needed": "None for planning; approve a later run prompt to execute.",
            "risk_reasons": [],
            "safe_to_run": False,
        }
    if mode == "menu":
        return {
            "status": "Plan only",
            "first_action": "Menu only: route to /orchestrate and stop at ranked options.",
            "approval_needed": "Choose a menu path or reroute through /autopilot --run.",
            "risk_reasons": [],
            "safe_to_run": False,
        }
    if risks:
        return {
            "status": "Blocked by risk",
            "first_action": RISK_BLOCK_TEXT,
            "approval_needed": "Approve the named risk gate before execution: " + ", ".join(risks),
            "risk_reasons": risks,
            "safe_to_run": False,
        }
    if launchpad and launchpad.get("pause_or_run", {}).get("requires_pause"):
        pause = launchpad["pause_or_run"]
        return {
            "status": "Needs judgment",
            "first_action": JUDGMENT_TEXT,
            "approval_needed": pause.get("reason") or "Clarify the launchpad judgment point.",
            "risk_reasons": ["co-creative launchpad pause"],
            "safe_to_run": False,
        }
    if score < 75 or needs_judgment(query):
        return {
            "status": "Needs judgment",
            "first_action": JUDGMENT_TEXT,
            "approval_needed": "Clarify the judgment point or approve the chosen route.",
            "risk_reasons": ["low clarity or taste/judgment gate"],
            "safe_to_run": False,
        }
    return {
        "status": "Running now",
        "first_action": RUNNING_TEXT,
        "approval_needed": "No extra approval needed for safe local work; pause if a risk gate appears mid-run.",
        "risk_reasons": [],
        "safe_to_run": True,
    }


def build_run_prompt(query: str, route: str, gates: list[str], decision: dict[str, Any]) -> str:
    gate_text = ", ".join(f"/{gate}" for gate in gates) or "none"
    return "\n".join(
        [
            "Use Default mode.",
            "",
            f"Run /autopilot --run {query}".strip(),
            f"Primary route: /{route}",
            f"Support gates: {gate_text}",
            f"Execution decision: {decision['status']}",
            f"Stay local to {ROOT}.",
            "Run the planned verifiers and finish with a run receipt.",
            "Pause only if an external, paid, destructive, global, non-current-workspace, or real-subagent gate appears.",
        ]
    )


def build_preflight(query: str, mode: str = "auto") -> dict[str, Any]:
    mode = normalize_mode(query, mode)
    menu_routes = route_names_from_command_menu(query)
    workflow_routes = route_names_from_workflow_router(query)
    decision = routing_governor.evaluate(query, menu_routes, workflow_routes)
    recipe = classify_outcome(query, decision.detected_lane, decision.chosen_route)
    bridge_route = raw_intent_bridge_route(query)
    if mode == "delegate":
        effective_lane = "delegate"
    elif bridge_route == "source-to-skill-system":
        effective_lane = "skill-system"
    elif bridge_route == "autopilot":
        effective_lane = "front-door-choice"
    else:
        effective_lane = "plugin-packaging" if recipe.name == "plugin-packaging" else decision.detected_lane
    if bridge_route == "source-to-skill-system":
        recipe = classify_outcome(query, "skill-system", "source-to-skill-system")
    chosen = choose_effective_route(mode, query, decision, recipe, menu_routes)
    stack = recommend_stack.recommend_stack(query)
    tools, tool_matches = tool_clusters(query)
    experts = expert_candidates(query)
    contexts = context_sources(query)
    classification = surface_classification()
    score = clarity_score(query, decision)
    owner = OWNER_BY_ROUTE.get(chosen, chosen.replace("-", " ").title() if chosen else "None")
    gates = support_gates(query, decision, recipe)
    gates = [gate for gate in gates if gate != chosen]
    verifiers = planned_verifiers(effective_lane, recipe)
    dynamic_workflow_needed = needs_dynamic_workflow(query, effective_lane, recipe.name)
    if dynamic_workflow_needed and "python3 execution/verify_codex_dynamic_workflow.py" not in verifiers:
        verifiers.insert(0, "python3 execution/verify_codex_dynamic_workflow.py")
    risks = risk_reasons(query, mode)
    raw_bridge = raw_intent_bridge_hint(query, chosen, gates, effective_lane, recipe.name)
    if raw_bridge["status"] == "triggered" and "python3 execution/verify_raw_intent_run_packet.py" not in verifiers:
        verifiers.insert(0, "python3 execution/verify_raw_intent_run_packet.py")
    launchpad = co_creative_launchpad.build_launchpad(
        query,
        route=chosen,
        lane=effective_lane,
        risk_reasons=risks,
        clarity_score=score,
    )
    posture = execution_decision(query, mode, score, chosen, launchpad)
    confidence_packet = build_intent_confidence_packet(
        query=query,
        route=chosen,
        owner=owner,
        gates=gates,
        verifiers=verifiers,
        score=score,
        launchpad=launchpad,
        posture=posture,
        stack=stack,
        lane=effective_lane,
        recipe_name=recipe.name,
    )
    meta_intent = classify_meta_intent(query, effective_lane, chosen, recipe.name)
    composition_owner = "System Audit" if meta_intent == "operating-alignment" else owner
    orchestration_receipt = build_orchestration_receipt(
        query=query,
        route=chosen,
        owner=owner,
        gates=gates,
        stack=stack,
        meta_intent=meta_intent,
        composition_owner=composition_owner,
        verifiers=verifiers,
        posture=posture,
        launchpad=launchpad,
    )
    skipped = list(decision.skipped_routes)
    if not skipped:
        seen_skipped = set()
        skipped = []
        for route in (menu_routes + workflow_routes):
            if not route or route == chosen or route in gates or route in seen_skipped:
                continue
            skipped.append(route)
            seen_skipped.add(route)
            if len(skipped) >= 5:
                break

    run_prompt = build_run_prompt(query, chosen, gates, posture)

    return {
        "query": query,
        "mode": mode,
        "intent": {
            "goal": "Compile this request into the best intent-to-outcome route.",
            "deliverable": f"{recipe.artifact}; execution decision and run receipt.",
            "audience": "Farrice and the Codex Antigravity harness.",
            "success_criteria": "Trace appears, one route wins, safe local work runs or a Run Prompt explains the gate, and verifiers are named.",
            "clarity_score": score,
            "confidence": "High" if decision.confidence >= 0.85 else "Medium" if decision.confidence >= 0.7 else "Low",
            "ambiguity_map": "No execution-changing ambiguity detected." if score >= 75 else "Clarify deliverable or approval boundary before execution.",
            "clarifier": "None before execution." if score >= 75 else "What outcome should the run produce?",
        },
        "intent_confidence_packet": confidence_packet,
        "launchpad": launchpad,
        "raw_intent_bridge": raw_bridge,
        "trace": {
            "loaded": [
                "CODEX.md",
                ".agent/workflows/autopilot.md",
                "semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md",
                "semantic_libraries/antigravity/primitives/operating-alignment-contract.md",
                "semantic_libraries/antigravity/primitives/magic-preservation-regression-set.md",
                "execution/autopilot_runtime_preflight.py",
                "execution/co_creative_launchpad.py",
                "execution/outcome_recipes.py",
                "execution/capability_graph.py",
                "execution/harness_status.py",
                "execution/friction_ledger.py",
                "execution/run_receipt.py",
                "execution/subagent_readiness.py",
                "execution/codex_dynamic_workflow.py",
                "execution/command_menu.py",
                "execution/workflow_router.py",
                "execution/routing_governor.py",
                "execution/expert_router.py",
                "execution/recommend_stack.py",
                "execution/tool_router.py",
                "execution/context_retriever.py",
            ],
            "raw_intent_bridge": raw_bridge,
            "candidates": {
                "command_menu": menu_routes,
                "workflow_router": workflow_routes,
                "expert_router": experts,
            },
            "governor": {
                "lane": effective_lane,
                "raw_lane": decision.detected_lane,
                "meta_intent": meta_intent,
                "composition_owner": composition_owner,
                "confidence": decision.confidence,
                "chosen_route": chosen,
                "reason": decision.reason,
            },
            "recommended_stack": stack,
            "owner": owner,
            "support_gates": gates,
            "skipped": skipped,
            "tool_clusters": tools,
            "tool_matches": tool_matches,
            "context_sources": contexts,
            "research_stack": "Use research/ground-truth gates before market claims." if effective_lane == "revenue" else "Skipped: request does not require current external research.",
            "copy_gate": "Trigger /publishable-copy-gate for public or revenue copy." if effective_lane == "revenue" else "Skipped: not public-facing copy.",
            "mission_package": "Skipped: no mission continuation detected; Mission remains read-only unless implicated.",
            "dynamic_workflow": (
                "Escalate through /virtuoso --workflow for a manifest-held phase runner."
                if dynamic_workflow_needed
                else "Skipped: single-thread route is sufficient unless the task expands."
            ),
            "composition": "One owner selected; /expert-composition-governor only when expert-soup intent is detected." if effective_lane != "expert-composition" else "Triggered: one owner plus contribution slots required.",
            "read_only_checks_performed": [
                "command_menu search",
                "workflow_router search",
                "routing_governor evaluate",
                "outcome recipe classify",
                "capability graph policy",
                "expert_router route",
                "recommend_stack",
                "tool_router route",
                "context_retriever search",
            ],
            "verification_planned": verifiers,
            "first_action": posture["first_action"],
        },
        "execution_decision": posture,
        "chosen_path": {
            "mode": mode,
            "meta_intent": meta_intent,
            "primary_route": chosen,
            "owner": owner,
            "composition_owner": composition_owner,
            "support_gates": gates,
            "why": decision.reason,
        },
        "orchestration_receipt": orchestration_receipt,
        "outcome_recipe": {
            "name": recipe.name,
            "primary_route": recipe.primary_route,
            "support_gates": list(recipe.support_gates),
            "artifact": recipe.artifact,
            "plugin_ladder": recipe.plugin_ladder,
        },
        "execution_plan": [
            "Render the Co-Creative Launchpad packet, trace, and execution decision.",
            "Run the chosen route now if the decision is Running now; otherwise use the Run Prompt after approval or judgment.",
            "Run planned verifiers and create a run receipt.",
            "Log any extra-pass, weak-output, missing-prompt, stale-recommendation, or verifier-failure event in the friction ledger.",
        ],
        "run_prompt": run_prompt,
        "run_receipt": {
            "command": (
                f"python3 execution/run_receipt.py --query {json.dumps(query)} "
                f"--route {json.dumps(chosen)} --status {json.dumps(posture['status'])} "
                f"--owner {json.dumps(owner)} --meta-intent {json.dumps(meta_intent)} "
                f"--composition-owner {json.dumps(composition_owner)} "
                f"--support-gates {json.dumps(','.join(gates))} "
                f"--expert-lenses {json.dumps(','.join(orchestration_receipt['expert_lenses']))} "
                f"--subagent-boundary {json.dumps(orchestration_receipt['subagent_boundary'])} "
                f"--container-decision {json.dumps(orchestration_receipt['container_decision'])} "
                f"--capability-move {json.dumps(orchestration_receipt['capability_move'])} "
                f"--why-now {json.dumps(orchestration_receipt['why_now'])} "
                f"--approval-boundary {json.dumps(orchestration_receipt['approval_boundary'])} "
                f"--feedback-hook {json.dumps(orchestration_receipt['feedback_hook'])} "
                "--changed \"[what changed]\" --passed \"[verifiers passed]\" "
                "--failed \"[verifiers failed]\" --judgment \"[judgment needed]\" "
                "--next-action \"[next action]\""
            ),
            "verify": "python3 execution/run_receipt.py --verify",
        },
        "friction_ledger": {
            "command": (
                "python3 execution/friction_ledger.py log --kind [extra-pass|failed-route|weak-output|"
                "missing-prompt|unclear-approval|stale-recommendation|verifier-failure] "
                "--summary \"[what happened]\" --next-action \"[repair route]\""
            ),
            "verify": "python3 execution/friction_ledger.py verify",
        },
        "surface_classification": classification,
        "global_mirror": {
            "status": "deferred",
            "surfaces": [
                "/Users/farricecain/.codex/AGENTS.md",
                "/Users/farricecain/.codex/skills/autopilot/SKILL.md",
                "/Users/farricecain/.codex/skills/source-command-autopilot/SKILL.md",
            ],
            "boundary": "Do not mirror until local proof passes and Farrice explicitly approves global edits.",
        },
    }


def fmt_routes(routes: Iterable[str]) -> str:
    values = [f"/{route}" for route in routes if route]
    return ", ".join(values) if values else "None"


def fmt_list(values: Iterable[str]) -> str:
    items = [str(value) for value in values if value]
    return ", ".join(items) if items else "None"


def render_preflight(data: dict[str, Any]) -> str:
    intent = data["intent"]
    confidence_packet = data["intent_confidence_packet"]
    launchpad = data["launchpad"]
    raw_bridge = data.get("raw_intent_bridge", {})
    trace = data["trace"]
    posture = data["execution_decision"]
    chosen = data["chosen_path"]
    recipe = data["outcome_recipe"]
    classification = data["surface_classification"]
    stack = trace["recommended_stack"]
    candidates = trace["candidates"]
    governor = trace["governor"]
    global_mirror = data["global_mirror"]
    orchestration_receipt = data["orchestration_receipt"]

    expert_names = [f"@{item['name']} ({item['domain']}, score {item['score']})" for item in candidates["expert_router"]]

    lines = [
        "## Intent Lock",
        f"- **Goal interpreted as**: {intent['goal']}",
        f"- **Deliverable**: {intent['deliverable']}",
        f"- **Audience/User**: {intent['audience']}",
        f"- **Success criteria**: {intent['success_criteria']}",
        f"- **Clarity Score**: {intent['clarity_score']}",
        f"- **Confidence**: {intent['confidence']}",
        f"- **Ambiguity Map**: {intent['ambiguity_map']}",
        f"- **Clarifier**: {intent['clarifier']}",
        "",
        "## Intent Confidence Packet",
        f"- **Goal**: {confidence_packet['goal']}",
        f"- **Audience**: {confidence_packet['audience']}",
        f"- **Success criteria**: {confidence_packet['success_criteria']}",
        f"- **Non-trivial reason**: {fmt_list(confidence_packet['non_trivial_reason'])}",
        f"- **Confidence**: {confidence_packet['confidence']}/100",
        f"- **Questions**: {fmt_list(confidence_packet['questions'])}",
        f"- **Chosen route**: /{confidence_packet['chosen_route']}",
        f"- **Owner**: {confidence_packet['owner']}",
        f"- **Support gates**: {fmt_routes(confidence_packet['support_gates'])}",
        f"- **Arsenal policy**: {confidence_packet['arsenal_policy']}",
        f"- **Proof plan**: {fmt_list(confidence_packet['proof_plan'])}",
        f"- **Retrieval home**: {confidence_packet['retrieval_home']['path']} ({confidence_packet['retrieval_home']['policy']})",
        f"- **Pause or run**: {confidence_packet['pause_or_run']['status']} - {confidence_packet['pause_or_run']['reason']}",
        "",
        "## Co-Creative Launchpad",
        f"- **Predicted need**: {launchpad['predicted_need']}",
        f"- **Center**: {launchpad['center']}",
        f"- **Edges**: {fmt_list(launchpad['edges'])}",
        f"- **What good looks like**: {launchpad['success_standard']}",
        f"- **Missing inputs**: {fmt_list(launchpad['missing_inputs'])}",
        f"- **Questions that change execution**: {fmt_list(launchpad['questions_that_change_execution'])}",
        f"- **Route bias**: /{launchpad['route_bias']['primary']}; {launchpad['route_bias']['reason']}",
        f"- **Pause or run**: {launchpad['pause_or_run']['decision']} - {launchpad['pause_or_run']['reason']}",
        f"- **Handoff**: {launchpad['handoff']['summary']}",
        "",
        "## Raw Intent Bridge",
        f"- **Status**: {raw_bridge.get('status', 'skipped')}",
        f"- **Reason**: {raw_bridge.get('reason', 'No raw-intent bridge needed.')}",
        f"- **Preferred route**: /{raw_bridge.get('preferred_route', chosen['primary_route'])}",
        f"- **Packet compiler**: {raw_bridge.get('packet_command') or 'Not triggered for this request.'}",
        f"- **Contract**: {raw_bridge.get('contract', 'semantic_libraries/antigravity/primitives/raw-intent-virtuoso-bridge-contract.md')}",
        f"- **Plugin packaging**: {raw_bridge.get('plugin_packaging', 'deferred')}",
        "",
        "## Autopilot Trace",
        f"- **Loaded**: {fmt_list(trace['loaded'])}",
        f"- **Candidates**: command_menu={fmt_routes(candidates['command_menu'])}; workflow_router={fmt_routes(candidates['workflow_router'])}; expert_router={fmt_list(expert_names)}",
        f"- **Governor**: lane={governor['lane']}; raw_lane={governor['raw_lane']}; meta_intent={governor['meta_intent']}; composition_owner={governor['composition_owner']}; confidence={governor['confidence']:.2f}; chosen=/{governor['chosen_route']}; reason={governor['reason']}",
        f"- **Outcome Recipe**: {recipe['name']} -> /{recipe['primary_route']}; artifact={recipe['artifact']}",
        f"- **Recommended Stack**: {stack['recommended_stack']}; {stack.get('skip_reason') or stack.get('effect') or stack.get('policy')}",
        f"- **Owner**: {trace['owner']}",
        f"- **Support Gates**: {fmt_routes(trace['support_gates'])}",
        f"- **Skipped**: {fmt_routes(trace['skipped'])}",
        f"- **Tool Routing**: clusters={fmt_list(trace['tool_clusters'])}; matches={fmt_list(trace['tool_matches'])}",
        f"- **Context Sources**: {fmt_list(trace['context_sources'])}",
        f"- **Mission Package**: {trace['mission_package']}",
        f"- **Dynamic Workflow**: {trace['dynamic_workflow']}",
        f"- **Composition**: {trace['composition']}",
        f"- **Copy Gate**: {trace['copy_gate']}",
        f"- **Research Stack**: {trace['research_stack']}",
        f"- **Read-only checks performed**: {fmt_list(trace['read_only_checks_performed'])}",
        f"- **Verification planned**: {fmt_list(trace['verification_planned'])}",
        "",
        "## Execution Decision",
        f"- **Status**: {posture['status']}",
        f"- **Safe local policy**: {SAFE_LOCAL_POLICY}",
        f"- **Risk reasons**: {fmt_list(posture['risk_reasons'])}",
        f"- **Approval needed**: {posture['approval_needed']}",
        f"- **First action**: {posture['first_action']}",
        "",
        "## Chosen Path",
        f"- **Mode**: {chosen['mode']}",
        f"- **Meta intent**: {chosen['meta_intent']}",
        f"- **Primary route**: /{chosen['primary_route']}",
        f"- **Owner**: {chosen['owner']}",
        f"- **Composition owner**: {chosen['composition_owner']}",
        f"- **Recommended stack**: {stack['recommended_stack']}; {stack.get('skip_reason') or stack.get('effect') or stack.get('policy')}",
        f"- **Composition**: {trace['composition']}",
        f"- **Support gates**: {fmt_routes(chosen['support_gates'])}",
        f"- **Why this path**: {chosen['why']}",
        "",
        "## Capability Graph",
        f"- **Outcome**: {recipe['name']}",
        f"- **Artifact**: {recipe['artifact']}",
        f"- **Plugin ladder**: {recipe['plugin_ladder']}",
        "- **Refresh command**: python3 execution/capability_graph.py --json",
        "",
        "## Execution Plan",
    ]

    for index, step in enumerate(data["execution_plan"], 1):
        lines.append(f"- **Step {index}**: {step}")

    lines.extend(
        [
            f"- **Verification**: {fmt_list(trace['verification_planned'])}",
            "- **Assumptions**: Workspace-local first; Mission read-only unless implicated; no global mirror without approval.",
            "",
            "## Orchestration Receipt",
            f"- **Objective**: {orchestration_receipt['objective']}",
            f"- **Meta intent**: {orchestration_receipt['meta_intent']}",
            f"- **Owner**: {orchestration_receipt['owner']}",
            f"- **Composition owner**: {orchestration_receipt['composition_owner']}",
            f"- **Route**: /{orchestration_receipt['route']}",
            f"- **Support gates**: {fmt_routes(orchestration_receipt['support_gates'])}",
            f"- **Expert lenses**: {fmt_list(orchestration_receipt['expert_lenses'])}",
            f"- **Subagent boundary**: {orchestration_receipt['subagent_boundary']}",
            f"- **Container decision**: {orchestration_receipt['container_decision']}",
            f"- **Capability move**: {orchestration_receipt['capability_move']}",
            f"- **Why now**: {orchestration_receipt['why_now']}",
            f"- **Approval boundary**: {orchestration_receipt['approval_boundary']}",
            f"- **Automatic task creation**: {orchestration_receipt['auto_task_creation']}",
            f"- **Verifier results**: {orchestration_receipt['verifier_results']['status']}; planned={fmt_list(orchestration_receipt['verifier_results']['planned'])}",
            f"- **Feedback hook**: {orchestration_receipt['feedback_hook']}",
            "",
            "## Run Prompt",
            "```text",
            data["run_prompt"],
            "```",
            "",
            "## Run Receipt",
            f"- **Create**: {data['run_receipt']['command']}",
            f"- **Verify**: {data['run_receipt']['verify']}",
            "",
            "## Friction Ledger",
            f"- **Log if needed**: {data['friction_ledger']['command']}",
            f"- **Verify**: {data['friction_ledger']['verify']}",
            "",
            "## Harness Surface Classification",
            f"- **Ready direct routes**: {classification['hot_count']} routes ({fmt_routes(classification['hot'])})",
            f"- **Live Codex skills**: {classification['live_skill_count']} total; {classification['live_command_wrapper_count']} direct command wrappers; {classification['cold_command_wrapper_count']} on-demand command wrappers",
            f"- **Available-on-demand bundles**: {classification['warm_count']} bundle candidates from {classification['cold_source']}",
            f"- **Indexed workflow library**: {classification['cold_count']} on-demand workflows; total workflows={classification['workflow_count']}",
            f"- **Protocols**: active={classification['active_protocols']}; healthy={classification['healthy_protocols']}; dormant={classification['dormant_protocols']}; source-only={classification['cold_source_only_protocols']}; overdue={classification['overdue_protocols']}; deprecated={classification['deprecated_protocols']}; activated ever={classification['activated_protocols']}",
            f"- **Agent Routing**: legacy fully routed={classification['fully_routed_agents']}; legacy unrouted={classification['unmeasured_agents']}; tiered compliant={classification['tiered_routing_compliant']}; tiered noncompliant={classification['tiered_routing_noncompliant']}; source-only={classification['cold_source_only_agents']} from {classification['routing_source']}",
            "- **Policy**: The arsenal stays accessible on demand; classification controls clutter and proof, not intelligence access.",
            "",
            "## Global Mirror Proposal",
            f"- **Status**: {global_mirror['status']}",
            f"- **Surfaces**: {fmt_list(global_mirror['surfaces'])}",
            f"- **Boundary**: {global_mirror['boundary']}",
            "",
            "## Approval/Risk Gate",
            f"- **Status**: {posture['status']}",
            f"- **Approval needed**: {posture['approval_needed']}",
            "- **Boundary**: no global mirror, Google Antigravity edit, publishing, paid tool, destructive cleanup, or real subagent run without explicit approval.",
        ]
    )

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Autopilot intent-to-outcome runtime preflight.")
    parser.add_argument("query", nargs="+", help="Raw prompt or context to preflight.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable preflight JSON.")
    parser.add_argument("--plan", action="store_true", help="Plan-only mode.")
    parser.add_argument("--menu", action="store_true", help="Menu-only mode.")
    parser.add_argument("--run", action="store_true", help="Force run-mode classification when safe.")
    parser.add_argument("--delegate", action="store_true", help="Delegation explicitly authorized.")
    parser.add_argument("--package", action="store_true", help="Plugin packaging/readiness mode.")
    args = parser.parse_args()

    query = " ".join(args.query).strip()
    if not query:
        parser.error("query is required")

    mode = "auto"
    for flag in ("plan", "menu", "run", "delegate", "package"):
        if getattr(args, flag):
            mode = flag
            break

    data = build_preflight(query, mode)
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(render_preflight(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
