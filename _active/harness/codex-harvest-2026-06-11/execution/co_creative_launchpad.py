#!/usr/bin/env python3
"""Deterministic co-creative launchpad packet builder.

The launchpad is a shared intent layer, not a new command surface. It predicts
the likely need, names the flashlight center and edges, asks only questions that
change execution, and hands the packet to Autopilot/Virtuoso routing.
"""

from __future__ import annotations

import argparse
import json
import re
from typing import Any, Iterable


ACTION_TERMS = (
    "build",
    "create",
    "make",
    "write",
    "draft",
    "design",
    "repair",
    "audit",
    "extract",
    "turn",
    "implement",
    "ship",
    "use",
    "verify",
    "check",
    "run",
)

SOURCE_TERMS = (
    "youtube",
    "video",
    "transcript",
    "source",
    "source material",
    "source-to-skill",
    "source to skill",
    "source-to-system",
    "source to system",
    "extract",
    "harvest",
)

LAUNCHPAD_TERMS = (
    "co-creative",
    "cocreative",
    "launchpad",
    "launching pad",
    "raw intent",
    "better questions",
    "intent alignment",
    "align intent",
    "apex before build",
    "before build",
    "before execution",
    "senior partner",
    "flashlight",
    "what good looks like",
)

SYSTEM_TERMS = (
    "system",
    "harness",
    "workflow",
    "command",
    "skill",
    "agent",
    "autopilot",
    "virtuoso",
    "routing",
    "orchestration",
)

OPERATOR_COCKPIT_TERMS = (
    "operator cockpit",
    "cockpit-first",
    "cockpit first",
    "v2 operating cockpit",
    "engineering debt",
    "user failure mode",
    "user failure modes",
    "bottleneck",
    "bottlenecks",
    "safeguards are not working",
    "safeguards not working",
    "ambiguous hoping you would catch",
    "catch all my intentions",
    "intent better",
    "conversational flow",
    "claude code",
    "claude catches my intent",
    "rebuild and enhancement",
    "rebuild and enhance",
    "smarter routing",
    "do not limit the arsenal",
    "don't limit the arsenal",
    "access to all the intelligence",
    "find what i need",
    "random numbers and letters",
    "can't find anything",
    "cannot find anything",
    "organization system",
)

RISK_TERMS = (
    "publish",
    "send",
    "dm",
    "outreach",
    "delete",
    "wipe",
    "global",
    "~/.codex",
    "google antigravity",
    "paid",
    "buy",
    "purchase",
    "connector write",
)

TASTE_TERMS = (
    "taste",
    "voice",
    "style",
    "brand",
    "creative direction",
    "creative brief",
    "creative concept",
    "world-class",
    "world class",
    "top 1%",
    "excellent",
    "excellence",
    "sophisticated",
)


def normalize(query: str) -> str:
    return re.sub(r"\s+", " ", query.lower()).strip()


def has_any(query: str, terms: Iterable[str]) -> bool:
    return any(term in query for term in terms)


def word_count(query: str) -> int:
    return len(re.findall(r"[a-z0-9][a-z0-9-]*", query.lower()))


def infer_predicted_need(query: str, route: str = "", lane: str = "") -> str:
    q = normalize(query)
    if has_any(q, OPERATOR_COCKPIT_TERMS):
        return (
            "Rebuild the operator loop so raw conversational intent becomes a "
            "confidence packet, one owner, full-arsenal access on demand, local "
            "friction capture, retrieval proof, and a clear next action."
        )
    if has_any(q, SOURCE_TERMS) and has_any(q, SYSTEM_TERMS):
        return (
            "Turn source material into an operating improvement without creating "
            "a duplicate mega-skill or losing source boundaries."
        )
    if has_any(q, LAUNCHPAD_TERMS):
        return (
            "Create a stronger shared starting point before execution: predicted "
            "intent, center, edges, quality bar, route, and proof."
        )
    if lane == "system-failure" or "broken" in q:
        return "Diagnose the control-plane failure, choose one repair owner, and prove the behavior changed."
    if has_any(q, TASTE_TERMS):
        return "Convert taste and quality ambition into concrete acceptance criteria before producing work."
    if route:
        return f"Route the request through /{route} with enough intent clarity to act safely."
    return "Clarify the outcome enough to choose the right route and first safe action."


def infer_center(query: str, route: str = "", lane: str = "") -> str:
    q = normalize(query)
    if has_any(q, OPERATOR_COCKPIT_TERMS):
        return "A chat-first and command-backed operating cockpit that asks before meaningful work and preserves full arsenal access."
    if has_any(q, LAUNCHPAD_TERMS):
        return "A cohesive co-creative launchpad that improves every meaningful start before building."
    if has_any(q, SOURCE_TERMS) and has_any(q, SYSTEM_TERMS):
        return "A source-grounded companion OS layer that improves future runs."
    if "research" in q:
        return "A source-led answer with claims, confidence, and unresolved gaps separated."
    if has_any(q, TASTE_TERMS):
        return "A result that matches Farrice's taste bar, not merely a technically complete output."
    if route:
        return f"The /{route} outcome, with proof and handoff included."
    return "The concrete outcome implied by the request."


def infer_edges(query: str, risk_reasons: Iterable[str] = ()) -> list[str]:
    q = normalize(query)
    edges: list[str] = []
    if has_any(q, OPERATOR_COCKPIT_TERMS):
        edges.append("Do not shrink or delete the intelligence arsenal; make it available on demand through smarter routing.")
        edges.append("Pause meaningful mutation until the confidence packet has answered its execution-changing questions.")
        edges.append("Keep retrieval and local organization visible so outputs are findable outside chat.")
    if has_any(q, SOURCE_TERMS):
        edges.append("Preserve source truth; mark unavailable evidence instead of inventing examples.")
    if has_any(q, SYSTEM_TERMS):
        edges.append("Extend the existing control plane instead of adding a competing front door.")
    if has_any(q, TASTE_TERMS):
        edges.append("Turn taste language into acceptance criteria before drafting or building.")
    if has_any(q, RISK_TERMS) or list(risk_reasons):
        edges.append("Stop before external, paid, destructive, global, public, connector-write, or real-subagent action.")
    if not edges:
        edges.append("State assumptions and keep the first action local, reversible, and verifiable.")
    return edges


def infer_success_standard(query: str, route: str = "") -> str:
    q = normalize(query)
    if has_any(q, OPERATOR_COCKPIT_TERMS):
        return (
            "Future non-trivial starts produce a confidence packet, route to "
            "/system-audit for cockpit/control-plane repair, suppress irrelevant "
            "expert stacks, capture local friction, name a retrieval home, and "
            "pause before meaningful work when questions remain."
        )
    if has_any(q, LAUNCHPAD_TERMS):
        return (
            "Future raw-intent starts show predicted need, center, edges, only "
            "execution-changing questions, chosen route, proof plan, and a safe first action."
        )
    if has_any(q, SOURCE_TERMS) and has_any(q, SYSTEM_TERMS):
        return "The build includes source evidence, route fit, contract fields, validation, and behavior-changing proof."
    if has_any(q, TASTE_TERMS):
        return "The output can be judged against explicit quality criteria, not vague excellence language."
    if route:
        return f"/{route} produces the requested artifact or action and verifies it."
    return "The next route can act without guessing the real objective."


def missing_inputs(query: str) -> list[str]:
    q = normalize(query)
    missing: list[str] = []
    if has_any(q, OPERATOR_COCKPIT_TERMS):
        if not any(term in q for term in ("implement", "approved", "success", "prove", "quality", "bar", "standard", "verify")):
            missing.append("operator_success_standard")
        if not any(term in q for term in ("local", "global", "~/.codex", "workspace")):
            missing.append("scope_boundary")
        if not any(term in q for term in ("capture", "friction", "failure", "retrieval", "organization", "files")):
            missing.append("failure_capture_policy")
    if not has_any(q, ACTION_TERMS) and word_count(q) < 8:
        missing.append("deliverable")
    if not any(term in q for term in ("for ", "audience", "client", "user", "customer", "reader", "prospect", "farrice")):
        missing.append("audience")
    if not any(term in q for term in ("done", "success", "good", "prove", "quality", "bar", "standard", "verify")):
        missing.append("success_standard")
    if has_any(q, SOURCE_TERMS) and not any(term in q for term in ("url", "http", "transcript", "file", "provided", "local")):
        missing.append("source_pointer")
    return missing


def questions_for(missing: list[str], query: str) -> list[str]:
    q = normalize(query)
    questions: list[str] = []
    if "operator_success_standard" in missing:
        questions.append("What must the cockpit prove before it is trusted for real builds?")
    if "scope_boundary" in missing:
        questions.append("Should this change stay workspace-local first, or include a separate global mirror approval packet?")
    if "failure_capture_policy" in missing:
        questions.append("Which failures should Codex capture automatically instead of asking you to log them?")
    if "deliverable" in missing:
        questions.append("What concrete artifact or action should exist when this is done?")
    if "audience" in missing and has_any(q, TASTE_TERMS):
        questions.append("Who will judge or consume the result?")
    if "success_standard" in missing and (has_any(q, TASTE_TERMS) or has_any(q, LAUNCHPAD_TERMS)):
        questions.append("What would make this excellent enough to keep using?")
    if "source_pointer" in missing:
        questions.append("What source file, transcript, URL, or local package should ground the build?")
    return questions[:3]


def route_bias(query: str, route: str = "", lane: str = "") -> dict[str, Any]:
    q = normalize(query)
    if has_any(q, OPERATOR_COCKPIT_TERMS):
        primary = "system-audit"
        support = ["autopilot", "health-check", "routing-intelligence", "expert-composition-governor", "self-evolve", "artifact-router"]
        reason = "Operator-cockpit and control-plane repair belongs to /system-audit with bounded support gates."
    elif has_any(q, SOURCE_TERMS) and has_any(q, SYSTEM_TERMS):
        primary = "source-to-skill-system"
        support = ["extraction-governor-agent", "autopilot"]
        reason = "Source-to-system intent should build a connected companion layer after source triage."
    elif has_any(q, LAUNCHPAD_TERMS) or "raw" in q or "intent" in q:
        primary = "autopilot"
        support = ["align", "virtuoso"]
        reason = "Raw intent and launchpad work belongs in the front-door intent layer."
    else:
        primary = route or "autopilot"
        support = []
        reason = "Use the chosen route unless the launchpad finds a risk or execution-changing ambiguity."
    return {
        "primary": primary,
        "support": support,
        "reason": reason,
        "detected_lane": lane or "unknown",
    }


def pause_or_run(
    *,
    query: str,
    missing: list[str],
    risk_reasons: Iterable[str] = (),
    clarity_score: int | None = None,
) -> dict[str, Any]:
    q = normalize(query)
    risks = list(risk_reasons)
    if risks or has_any(q, RISK_TERMS):
        return {
            "decision": "block_for_risk",
            "reason": "Risk-gated action detected before local execution.",
            "requires_pause": True,
        }
    operator_missing = {
        "operator_success_standard",
        "scope_boundary",
        "failure_capture_policy",
    } & set(missing)
    if has_any(q, OPERATOR_COCKPIT_TERMS) and operator_missing:
        return {
            "decision": "pause_for_judgment",
            "reason": "V2 cockpit or operator-friction work needs the confidence packet answered before meaningful mutation.",
            "requires_pause": True,
        }
    if "deliverable" in missing and word_count(q) < 8:
        return {
            "decision": "pause_for_judgment",
            "reason": "The requested outcome is too underspecified to choose a safe first action.",
            "requires_pause": True,
        }
    if has_any(q, TASTE_TERMS) and "success_standard" in missing:
        return {
            "decision": "pause_for_judgment",
            "reason": "Taste-heavy work needs an explicit quality bar before execution.",
            "requires_pause": True,
        }
    if clarity_score is not None and clarity_score < 60:
        return {
            "decision": "pause_for_judgment",
            "reason": "Clarity is below the launch threshold.",
            "requires_pause": True,
        }
    return {
        "decision": "run_with_assumptions",
        "reason": "No execution-changing ambiguity detected; state assumptions and proceed locally.",
        "requires_pause": False,
    }


def build_launchpad(
    query: str,
    *,
    route: str = "",
    lane: str = "",
    risk_reasons: Iterable[str] = (),
    clarity_score: int | None = None,
) -> dict[str, Any]:
    missing = missing_inputs(query)
    questions = questions_for(missing, query)
    pause = pause_or_run(
        query=query,
        missing=missing,
        risk_reasons=risk_reasons,
        clarity_score=clarity_score,
    )
    bias = route_bias(query, route, lane)
    center = infer_center(query, route, lane)
    success = infer_success_standard(query, route)
    constraints = infer_edges(query, risk_reasons)
    return {
        "schema_version": "co-creative-launchpad/v1",
        "predicted_need": infer_predicted_need(query, route, lane),
        "center": center,
        "edges": constraints,
        "success_standard": success,
        "constraints": constraints,
        "missing_inputs": missing,
        "questions_that_change_execution": questions,
        "route_bias": bias,
        "pause_or_run": pause,
        "handoff": {
            "summary": f"Optimize for: {center}",
            "route": bias["primary"],
            "quality_bar": success,
            "source_boundary": (
                "Use public/local source evidence only; private member examples are unavailable unless supplied."
                if has_any(normalize(query), SOURCE_TERMS)
                else "No special source boundary detected."
            ),
            "questions": questions,
        },
    }


def render_launchpad(packet: dict[str, Any]) -> str:
    route = packet["route_bias"]
    pause = packet["pause_or_run"]
    lines = [
        "## Co-Creative Launchpad",
        f"- **Predicted need**: {packet['predicted_need']}",
        f"- **Center**: {packet['center']}",
        f"- **Edges**: {', '.join(packet['edges']) or 'None'}",
        f"- **What good looks like**: {packet['success_standard']}",
        f"- **Missing inputs**: {', '.join(packet['missing_inputs']) or 'None'}",
        f"- **Questions that change execution**: {', '.join(packet['questions_that_change_execution']) or 'None'}",
        f"- **Route bias**: /{route['primary']} ({route['reason']})",
        f"- **Pause or run**: {pause['decision']} - {pause['reason']}",
        f"- **Handoff**: {packet['handoff']['summary']}",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a co-creative launchpad packet.")
    parser.add_argument("query", nargs="+", help="Raw prompt or context.")
    parser.add_argument("--route", default="", help="Already selected route, if known.")
    parser.add_argument("--lane", default="", help="Detected routing lane, if known.")
    parser.add_argument("--clarity-score", type=int, default=None)
    parser.add_argument("--risk", action="append", default=[], help="Risk reason; may be repeated.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    packet = build_launchpad(
        " ".join(args.query),
        route=args.route,
        lane=args.lane,
        risk_reasons=args.risk,
        clarity_score=args.clarity_score,
    )
    if args.json:
        print(json.dumps(packet, indent=2, ensure_ascii=False))
    else:
        print(render_launchpad(packet))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
