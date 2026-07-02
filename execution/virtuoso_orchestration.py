#!/usr/bin/env python3
"""Virtuoso orchestration composer for the Antigravity harness.

This layer does not replace Autopilot, Orchestrate, routing intelligence, or
expert composition. It composes their current evidence into one operational
trace so complex work shows route, owner, stack, delegation, tools, and proof in
one place.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXECUTION = ROOT / "execution"
sys.path.insert(0, str(EXECUTION))

import autopilot_runtime_preflight  # type: ignore  # noqa: E402
import codex_dynamic_workflow  # type: ignore  # noqa: E402
import plugin_readiness_audit  # type: ignore  # noqa: E402
import routing_intelligence  # type: ignore  # noqa: E402
import subagent_readiness  # type: ignore  # noqa: E402


OPERATOR_CORE_ROUTES = (
    "autopilot",
    "mission",
    "orchestrate",
    "extraction-governor-agent",
    "knowledge-librarian",
    "health-check",
    "routing-intelligence",
    "self-evolve",
)

REFERENCED_DEPENDENCIES = (
    "system-audit",
    "expert-composition-governor",
    "source-to-skill-system",
)

DELEGATION_SIGNALS = (
    "subagent",
    "subagents",
    "parallel agents",
    "delegate",
    "delegation",
    "swarm",
    "full arsenal",
    "council",
)

MODE_BIASES = {
    "revenue": "revenue first-dollar first-client monetization paid-proof service-first",
    "creative": "creative high-taste content design copy originality craft",
    "research": "deep research os research current sources social listening market intelligence fact verification evidence synthesis source ledger",
    "build": "build implementation workflow command skill system validation",
    "audit": "audit system proof verifier risk diagnosis",
    "repair": "repair regression repeatability failure preservation no-regression",
}


def _fmt_route(route: str) -> str:
    return f"/{route}" if route and not route.startswith("/") else route


def _stack_items(stack: dict[str, Any]) -> list[str]:
    items = stack.get("stack") or []
    return [str(item) for item in items if str(item).strip()]


def _best_mechanism(gates: list[str], route: str) -> str:
    for gate in gates:
        if gate and gate != route:
            return _fmt_route(gate)
    return "planned verifiers"


def _risk_gate(gates: list[str], verifiers: list[str]) -> str:
    for candidate in ("red-team-agent", "ground-truth-agent", "publishable-copy-gate", "routing-intelligence"):
        if candidate in gates:
            return _fmt_route(candidate)
    return verifiers[0] if verifiers else "verification plan"


def biased_query(query: str, mode_bias: str | None) -> str:
    if not mode_bias:
        return query
    bias = MODE_BIASES.get(mode_bias, "")
    return f"{bias}. Objective: {query}" if bias else query


def build_composition_slots(preflight: dict[str, Any]) -> list[dict[str, str]]:
    """Assign bounded expert-composition slots from the chosen route evidence."""
    chosen = preflight["chosen_path"]
    trace = preflight["trace"]
    stack = _stack_items(trace["recommended_stack"])
    route = chosen["primary_route"]
    gates = list(chosen.get("support_gates", []))
    verifiers = list(trace.get("verification_planned", []))

    differentiator = "No extra stack; keep owner-led path"
    if stack:
        differentiator = " + ".join(stack)

    return [
        {
            "slot": "Spine",
            "asset": chosen["owner"],
            "job": f"Own the final outcome through {_fmt_route(route)}.",
            "evidence": f"primary_route={_fmt_route(route)}",
        },
        {
            "slot": "Differentiator",
            "asset": differentiator,
            "job": "Add the non-obvious compound advantage only if it changes the output.",
            "evidence": trace["recommended_stack"].get("evidence_source") or trace["recommended_stack"].get("skip_reason", ""),
        },
        {
            "slot": "Mechanism",
            "asset": _best_mechanism(gates, route),
            "job": "Operationalize the route through the strongest support gate.",
            "evidence": ", ".join(_fmt_route(gate) for gate in gates) or "no support gates",
        },
        {
            "slot": "Craft",
            "asset": "owner integration pass",
            "job": "Make the final output read or behave as one system, not stitched parts.",
            "evidence": "Expert Composition Contract: one owner, bounded specialists, integration pass",
        },
        {
            "slot": "Risk Gate",
            "asset": _risk_gate(gates, verifiers),
            "job": "Catch broken trust, weak claims, overclaiming, or regression before closeout.",
            "evidence": ", ".join(verifiers) or "no verifiers planned",
        },
    ]


def wants_delegation(query: str, delegate_intent: bool) -> bool:
    lowered = query.lower()
    return delegate_intent or any(signal in lowered for signal in DELEGATION_SIGNALS)


def candidate_matches_query(slug: str, query: str) -> bool:
    lowered = query.lower()
    rules = {
        "deep-research": ("research", "current", "latest", "market", "source", "deep"),
        "fact-verifier": ("fact", "verify", "claim", "accuracy", "source", "truth"),
        "competitive-intel": ("competitor", "market", "pricing", "positioning", "category"),
        "icp-deep-canvasser": ("icp", "audience", "buyer", "customer", "avatar"),
        "adversarial-reviewer": ("risk", "red team", "critique", "adversarial", "break", "audit"),
        "prose-doctor": ("write", "copy", "voice", "prose", "draft", "content"),
        "content-finalizer": ("content", "publish", "final", "post", "newsletter", "copy"),
    }
    return any(term in lowered for term in rules.get(slug, ()))


def build_subagent_candidates(query: str, delegate_intent: bool) -> dict[str, Any]:
    matrix = subagent_readiness.build_matrix()
    delegation_requested = wants_delegation(query, delegate_intent)
    items = []
    for item in matrix.get("items", []):
        slug = item.get("slug", "")
        matched = delegation_requested or candidate_matches_query(slug, query)
        items.append(
            {
                "slug": slug,
                "readiness": item.get("readiness", ""),
                "spec_path": item.get("spec_path", ""),
                "selected_for_packet": bool(matched and item.get("readiness") == "ready-for-approved-delegation"),
                "activation_boundary": item.get("activation_boundary", ""),
                "input_contract": item.get("input_contract", ""),
                "output_contract": item.get("output_contract", ""),
            }
        )

    selected = [item["slug"] for item in items if item["selected_for_packet"]]
    if delegation_requested:
        decision = "subagent-first packet planning; real workers still require explicit authorization"
    else:
        decision = "main-thread orchestration; subagent packets available if explicitly authorized"

    return {
        "decision": decision,
        "real_subagents_spawned": False,
        "integration_owner": matrix.get("integration_owner", "main Codex thread"),
        "selected": selected,
        "items": items,
        "delegation_receipt_template": matrix.get("delegation_receipt_template", {}),
    }


def build_plugin_tool_surface(preflight: dict[str, Any]) -> dict[str, Any]:
    route_counts = plugin_readiness_audit.routing_counts()
    operator_scores = [plugin_readiness_audit.score_candidate(name, route_counts) for name in OPERATOR_CORE_ROUTES]
    dependency_scores = [plugin_readiness_audit.score_candidate(name, route_counts) for name in REFERENCED_DEPENDENCIES]
    avg = round(sum(score.total for score in operator_scores) / len(operator_scores), 1)

    def row(score: Any) -> dict[str, Any]:
        return {
            "route": score.name,
            "total": score.total,
            "decision": score.decision,
            "workflow": score.workflow_exists,
            "command": score.command_exists,
            "hot_skill": score.codex_skill_exists,
            "routing_count": score.routing_count,
        }

    return {
        "plugin_name": "antigravity-operator-core",
        "operator_core_average": avg,
        "recommendation": "package candidate" if avg >= 80 else "harden first",
        "bundled_routes": [row(score) for score in operator_scores],
        "referenced_dependencies": [row(score) for score in dependency_scores],
        "tool_clusters": preflight["trace"].get("tool_clusters", []),
        "tool_matches": preflight["trace"].get("tool_matches", []),
        "policy": "Package the mature operator core; keep dependent workflows referenced until readiness proof justifies bundling.",
    }


def build_routing_log(preflight: dict[str, Any], log_routing: bool) -> dict[str, Any]:
    chosen = preflight["chosen_path"]
    trace = preflight["trace"]
    stack = trace["recommended_stack"]
    stack_items = _stack_items(stack)
    ensemble = bool(stack_items)
    pairing = " + ".join(stack_items)
    experts = stack_items or [chosen["owner"]]
    domain = trace["governor"].get("raw_lane") if trace["governor"].get("lane") == "delegate" else trace["governor"].get("lane")
    domain = domain or trace["governor"].get("lane") or "unknown"

    command = (
        "python3 execution/routing_intelligence.py log "
        f"--request {json.dumps(preflight['query'][:200])} "
        f"--score 5 --domain {json.dumps(domain)} "
        f"--experts {json.dumps(','.join(experts))} "
        f"--tier 3 --mode hybrid --workflow {json.dumps(chosen['primary_route'])}"
        + (f" --ensemble --pairing {json.dumps(pairing)}" if ensemble else "")
    )

    result: dict[str, Any] = {
        "ensemble": ensemble,
        "compound_pairing": pairing,
        "expert_lenses_applied": experts,
        "experts_deployed": experts,
        "workflow_used": chosen["primary_route"],
        "domain_detected": domain,
        "command": command,
        "routing_id": None,
        "logged": False,
    }

    if log_routing:
        result["routing_id"] = routing_intelligence.log_routing_decision(
            request_summary=preflight["query"],
            intent_score=5,
            domain_detected=domain,
            experts_deployed=experts,
            tier_loaded=3,
            mode="hybrid",
            workflow_used=chosen["primary_route"],
            ensemble=ensemble,
            compound_pairing=pairing,
            session_id="virtuoso-orchestration",
        )
        result["logged"] = True
    return result


def build_execution_receipt(
    *,
    preflight: dict[str, Any],
    subagents: dict[str, Any],
    routing: dict[str, Any],
    trace_only: bool,
    mode_bias: str | None,
    workflow_intent: bool = False,
) -> dict[str, Any]:
    trace = preflight["trace"]
    chosen = preflight["chosen_path"]
    executed_scripts = ["execution/virtuoso_orchestration.py"]
    if workflow_intent:
        executed_scripts.append("execution/codex_dynamic_workflow.py plan --no-save")
    if routing.get("logged"):
        executed_scripts.append("execution/routing_intelligence.py log")

    if trace_only:
        status = "trace-only"
    elif workflow_intent:
        status = "workflow-trace"
    else:
        status = "ready-for-safe-local-action"
    selected_route = chosen["primary_route"]
    orchestration_receipt = preflight.get("orchestration_receipt", {})
    return {
        "status": status,
        "mode_bias": mode_bias or "auto",
        "meta_intent": chosen.get("meta_intent", ""),
        "composition_owner": chosen.get("composition_owner", chosen.get("owner", "")),
        "considered_gates": chosen.get("support_gates", []),
        "loaded_context": trace.get("loaded", []),
        "context_sources": trace.get("context_sources", []),
        "selected_workflow": selected_route,
        "executed_workflows": [],
        "executed_scripts": executed_scripts,
        "skipped_gates": trace.get("skipped", []),
        "expert_lenses_applied": routing.get("expert_lenses_applied", []),
        "subagent_packets_prepared": subagents.get("selected", []),
        "real_subagents_spawned": subagents.get("real_subagents_spawned", False),
        "subagent_boundary": orchestration_receipt.get(
            "subagent_boundary",
            "Delegation packets only; real Codex subagents require explicit authorization.",
        ),
        "feedback_hook": orchestration_receipt.get("feedback_hook", ""),
        "external_actions": "blocked unless explicitly approved",
        "approval_gates": [
            "external writes",
            "publishing",
            "outreach or DMs",
            "connector writes",
            "global mirrors",
            "paid/API actions",
            "destructive cleanup",
            "Mission/system memory mutation",
            "real Codex subagents",
        ],
        "receipt_note": (
            "Support gates are considered, not executed. Only items in executed_workflows "
            "or executed_scripts ran during this trace."
        ),
    }


def build_virtuoso(
    query: str,
    delegate_intent: bool = False,
    log_routing: bool = False,
    trace_only: bool = False,
    mode_bias: str | None = None,
    workflow_intent: bool = False,
) -> dict[str, Any]:
    mode = "delegate" if delegate_intent else "auto"
    routed_query = biased_query(query, mode_bias)
    preflight = autopilot_runtime_preflight.build_preflight(routed_query, mode=mode)
    raw_bridge = preflight.get("raw_intent_bridge", {})
    chosen = preflight["chosen_path"]
    trace = preflight["trace"]
    verification = list(trace.get("verification_planned", []))
    if "python3 execution/verify_virtuoso_orchestration.py" not in verification:
        verification.insert(0, "python3 execution/verify_virtuoso_orchestration.py")
    subagents = build_subagent_candidates(query, delegate_intent)
    routing = build_routing_log(preflight, log_routing)
    dynamic_workflow = None
    if workflow_intent:
        manifest = codex_dynamic_workflow.build_manifest(
            query,
            allow_subagents=delegate_intent,
            max_concurrency=4,
        )
        dynamic_workflow = {
            "manifest": manifest,
            "status": codex_dynamic_workflow.status_summary(manifest),
            "receipt_preview": codex_dynamic_workflow.build_receipt(manifest),
            "save_command": (
                "python3 execution/codex_dynamic_workflow.py plan "
                f"{json.dumps(query)} --recipe {manifest['recipe']['id']}"
            ),
            "verify_command": "python3 execution/verify_codex_dynamic_workflow.py",
            "runtime_boundary": codex_dynamic_workflow.REAL_SUBAGENT_BOUNDARY,
        }
        if "python3 execution/verify_codex_dynamic_workflow.py" not in verification:
            verification.insert(0, "python3 execution/verify_codex_dynamic_workflow.py")
    execution = dict(preflight["execution_decision"])
    if trace_only:
        execution = {
            "status": "Trace only",
            "first_action": "Trace only: no local action executed.",
            "approval_needed": "Approve a follow-up run to execute the selected route.",
            "risk_reasons": [],
            "safe_to_run": False,
        }
    elif workflow_intent:
        execution = {
            "status": "Workflow trace",
            "first_action": "Dynamic workflow manifest planned; review or save it before execution.",
            "approval_needed": "Approve saving/resuming the manifest and separately authorize any real Codex subagents.",
            "risk_reasons": ["real subagents remain approval-gated"] if delegate_intent else [],
            "safe_to_run": False,
        }

    result = {
        "schema_version": "virtuoso-orchestration/v1",
        "objective": query,
        "routed_query": routed_query,
        "launchpad": preflight["launchpad"],
        "raw_intent_bridge": raw_bridge,
        "orchestration_receipt": preflight.get("orchestration_receipt", {}),
        "primary_route": chosen["primary_route"],
        "owner": chosen["owner"],
        "meta_intent": chosen.get("meta_intent", ""),
        "composition_owner": chosen.get("composition_owner", chosen["owner"]),
        "support_gates": chosen.get("support_gates", []),
        "recommended_stack": trace["recommended_stack"],
        "composition_slots": build_composition_slots(preflight),
        "subagent_candidates": subagents,
        "dynamic_workflow": dynamic_workflow,
        "plugin_tool_surface": build_plugin_tool_surface(preflight),
        "routing_log": routing,
        "execution_receipt": build_execution_receipt(
            preflight=preflight,
            subagents=subagents,
            routing=routing,
            trace_only=trace_only,
            mode_bias=mode_bias,
            workflow_intent=workflow_intent,
        ),
        "verification_plan": verification,
        "first_action": execution.get("first_action") or trace.get("first_action", ""),
        "execution_decision": execution,
        "preflight_summary": {
            "mode": preflight["mode"],
            "mode_bias": mode_bias or "auto",
            "lane": trace["governor"]["lane"],
            "raw_lane": trace["governor"]["raw_lane"],
            "confidence": trace["governor"]["confidence"],
            "why": chosen["why"],
            "tool_clusters": trace.get("tool_clusters", []),
            "context_sources": trace.get("context_sources", []),
        },
    }
    return result


def render_markdown(data: dict[str, Any]) -> str:
    launchpad = data["launchpad"]
    raw_bridge = data.get("raw_intent_bridge", {})
    stack = data["recommended_stack"]
    stack_text = stack.get("recommended_stack", "No recommended stack")
    stack_detail = stack.get("effect") or stack.get("skip_reason") or stack.get("policy", "")
    delegation = data["subagent_candidates"]
    plugin = data["plugin_tool_surface"]
    routing = data["routing_log"]
    receipt = data["execution_receipt"]
    orchestration_receipt = data.get("orchestration_receipt", {})
    dynamic = data.get("dynamic_workflow")

    lines = [
        "## Virtuoso Trace",
        f"- **Objective**: {data['objective']}",
        f"- **Meta intent**: {data.get('meta_intent') or 'none'}",
        f"- **Route**: {_fmt_route(data['primary_route'])}",
        f"- **Owner**: {data['owner']}",
        f"- **Composition owner**: {data.get('composition_owner') or data['owner']}",
        f"- **Launchpad**: {launchpad['center']} | {launchpad['pause_or_run']['decision']}",
        f"- **Raw Intent Bridge**: {raw_bridge.get('status', 'skipped')} | {raw_bridge.get('preferred_route', data['primary_route'])}",
        f"- **Stack**: {stack_text}; {stack_detail}",
        f"- **Support gates**: {', '.join(_fmt_route(gate) for gate in data['support_gates']) or 'None'}",
        f"- **Delegation**: {delegation['decision']}; selected={', '.join(delegation['selected']) or 'none'}; real_subagents_spawned={delegation['real_subagents_spawned']}",
        f"- **Plugin/tool surface**: {plugin['plugin_name']} avg={plugin['operator_core_average']}; {plugin['recommendation']}; clusters={', '.join(plugin['tool_clusters']) or 'none'}",
        f"- **Routing log**: ensemble={routing['ensemble']}; logged={routing['logged']}; id={routing['routing_id'] or 'not logged'}",
        f"- **First action**: {data['first_action']}",
        "",
        "## Co-Creative Launchpad",
        f"- **Predicted need**: {launchpad['predicted_need']}",
        f"- **Center**: {launchpad['center']}",
        f"- **Edges**: {', '.join(launchpad['edges']) or 'none'}",
        f"- **What good looks like**: {launchpad['success_standard']}",
        f"- **Questions that change execution**: {', '.join(launchpad['questions_that_change_execution']) or 'none'}",
        f"- **Route bias**: /{launchpad['route_bias']['primary']}; {launchpad['route_bias']['reason']}",
        f"- **Pause or run**: {launchpad['pause_or_run']['decision']} - {launchpad['pause_or_run']['reason']}",
        "",
        "## Raw Intent Bridge",
        f"- **Status**: {raw_bridge.get('status', 'skipped')}",
        f"- **Reason**: {raw_bridge.get('reason', 'No raw-intent bridge needed.')}",
        f"- **Preferred route**: {_fmt_route(raw_bridge.get('preferred_route', data['primary_route']))}",
        f"- **Packet compiler**: {raw_bridge.get('packet_command') or 'Not triggered for this request.'}",
        f"- **Contract**: {raw_bridge.get('contract', 'semantic_libraries/antigravity/primitives/raw-intent-virtuoso-bridge-contract.md')}",
        f"- **Plugin packaging**: {raw_bridge.get('plugin_packaging', 'deferred')}",
        "",
    ]

    if dynamic:
        manifest = dynamic["manifest"]
        status = dynamic["status"]
        lines.extend(
            [
                "## Dynamic Workflow Trace",
                "- **Runtime**: `execution/codex_dynamic_workflow.py`",
                f"- **Recipe**: `{manifest['recipe']['id']}` - {manifest['recipe']['purpose']}",
                f"- **Run state**: {status['status']}; current_phase={status['current_phase']}",
                f"- **Max concurrency**: {manifest['max_concurrency']}",
                f"- **Integration owner**: {manifest['final_integration_owner']}",
                f"- **Real subagents spawned**: {status['real_subagents_spawned']}",
                f"- **Boundary**: {dynamic['runtime_boundary']}",
                f"- **Save command**: `{dynamic['save_command']}`",
                f"- **Verify command**: `{dynamic['verify_command']}`",
                "",
                "| # | Phase | Worker packets | Outputs |",
                "|---:|---|---|---|",
            ]
        )
        for phase in manifest["phases"]:
            lines.append(
                f"| {phase['index']} | {phase['name']} | {', '.join(phase['worker_packet_ids'])} | {', '.join(phase['outputs'])} |"
            )
        lines.append("")

    lines.extend(
        [
        "## Orchestration Receipt",
        f"- **Objective**: {orchestration_receipt.get('objective', data['objective'])}",
        f"- **Meta intent**: {orchestration_receipt.get('meta_intent', data.get('meta_intent', 'none'))}",
        f"- **Owner**: {orchestration_receipt.get('owner', data['owner'])}",
        f"- **Composition owner**: {orchestration_receipt.get('composition_owner', data.get('composition_owner', data['owner']))}",
        f"- **Route**: {_fmt_route(orchestration_receipt.get('route', data['primary_route']))}",
        f"- **Support gates**: {', '.join(_fmt_route(gate) for gate in orchestration_receipt.get('support_gates', data['support_gates'])) or 'none'}",
        f"- **Expert lenses**: {', '.join(orchestration_receipt.get('expert_lenses', [])) or 'none'}",
        f"- **Subagent boundary**: {orchestration_receipt.get('subagent_boundary', receipt.get('subagent_boundary', 'approval-gated'))}",
        f"- **Verifier results**: {orchestration_receipt.get('verifier_results', {}).get('status', 'planned')}",
        f"- **Feedback hook**: {orchestration_receipt.get('feedback_hook', receipt.get('feedback_hook', 'routing and friction ledgers'))}",
        "",
        "## Execution Receipt",
        f"- **Status**: {receipt['status']}",
        f"- **Meta intent**: {receipt.get('meta_intent') or 'none'}",
        f"- **Composition owner**: {receipt.get('composition_owner') or 'none'}",
        f"- **Considered gates**: {', '.join(_fmt_route(gate) for gate in receipt['considered_gates']) or 'none'}",
        f"- **Loaded context**: {', '.join(receipt['loaded_context'][:8])}{'...' if len(receipt['loaded_context']) > 8 else ''}",
        f"- **Selected workflow**: {_fmt_route(receipt['selected_workflow'])}",
        f"- **Executed workflows**: {', '.join(_fmt_route(item) for item in receipt['executed_workflows']) or 'none in composer trace'}",
        f"- **Executed scripts**: {', '.join(receipt['executed_scripts'])}",
        f"- **Skipped gates**: {', '.join(_fmt_route(gate) for gate in receipt['skipped_gates']) or 'none'}",
        f"- **Expert lenses applied**: {', '.join(receipt['expert_lenses_applied']) or 'none'}",
        f"- **Subagent packets prepared**: {', '.join(receipt['subagent_packets_prepared']) or 'none'}",
        f"- **Real subagents spawned**: {receipt['real_subagents_spawned']}",
        f"- **Subagent boundary**: {receipt.get('subagent_boundary', 'approval-gated')}",
        f"- **External actions**: {receipt['external_actions']}",
        f"- **Feedback hook**: {receipt.get('feedback_hook') or 'none'}",
        f"- **Receipt note**: {receipt['receipt_note']}",
        "",
        "## Composition Ledger",
        "| Slot | Asset | Job | Evidence |",
        "|---|---|---|---|",
        ]
    )
    for slot in data["composition_slots"]:
        lines.append(f"| {slot['slot']} | {slot['asset']} | {slot['job']} | {slot['evidence']} |")

    lines.extend(
        [
            "",
            "## Delegation Matrix",
            "| Candidate | Selected | Readiness | Boundary | Output |",
            "|---|---:|---|---|---|",
        ]
    )
    for item in delegation["items"]:
        if item["selected_for_packet"] or item["readiness"] == "ready-for-approved-delegation":
            selected = "yes" if item["selected_for_packet"] else "no"
            lines.append(
                f"| `{item['slug']}` | {selected} | {item['readiness']} | {item['activation_boundary']} | {item['output_contract']} |"
            )

    lines.extend(
        [
            "",
            "## Verification",
        ]
    )
    for verifier in data["verification_plan"]:
        lines.append(f"- {verifier}")

    lines.extend(
        [
            "",
            "## Routing Evidence",
            f"- Command: `{routing['command']}`",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compose a Virtuoso orchestration trace over the existing Antigravity routers.")
    parser.add_argument("query", nargs="+", help="Goal or raw context to orchestrate.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--delegate-intent", "--delegate", action="store_true", help="Plan subagent-first packets while keeping real delegation gated.")
    parser.add_argument("--log-routing", "--log", action="store_true", help="Write the resulting routing decision to routing intelligence.")
    parser.add_argument("--trace-only", action="store_true", help="Render the trace and stop without safe-action execution guidance.")
    parser.add_argument("--workflow", action="store_true", help="Attach a Codex Dynamic Workflow manifest trace without spawning workers.")
    parser.add_argument(
        "--mode",
        choices=sorted(MODE_BIASES),
        help="Bias routing toward a domain without bypassing the owner/gate system.",
    )
    args = parser.parse_args()

    query = " ".join(args.query).strip()
    if not query:
        parser.error("query is required")

    data = build_virtuoso(
        query,
        delegate_intent=args.delegate_intent,
        log_routing=args.log_routing,
        trace_only=args.trace_only,
        mode_bias=args.mode,
        workflow_intent=args.workflow,
    )
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(render_markdown(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
