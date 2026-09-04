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

from control_intent import classify_control_intent


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
    "match claude code",
    "mirror claude code",
    "claude parity",
    "claude-parity",
    "blocking hooks",
    "blocked hooks",
    "wrong defaults",
    "wrong default routing",
    "routing wrong defaults",
    "default settings",
    "default setting",
    "things that are not wired",
    "not wired",
    "should not be wired",
    "shouldn't be wired",
    "wired together",
    "not wired together",
    "should not be wired together",
    "shouldn't be wired together",
    "wiring",
    "hook wiring",
    "route wiring",
    "routing wiring",
    "hooks or routes",
    "hooks and routes",
    "routes and hooks",
    "handcuffed",
    "handcuff",
    "handcuffed and chained",
    "handcuffed and chained together",
    "chained together",
    "chained",
    "things being chained together",
    "routes are being handcuffed",
    "hooks are being handcuffed",
    "should not be chained",
    "shouldn't be chained",
    "full audit or check and repair",
    "audit or check and repair",
    "check and repair",
    "audit and repair",
    "thin wrappers",
    "too many thin wrappers",
    "without breaking my workspace",
    "without breaking claude code",
    "not trying to break anything",
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
    "codex is not working",
    "codex is not working in my workspace",
    "codex not working",
    "codex not working in my workspace",
    "no point in using codex",
    "using codex in my workspace",
    "feels like it is not working",
    "feels like it's not working",
    "not working at all",
    "just not working at all",
    "context issue",
    "context issue and not usable",
    "not usable",
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
    "paid api",
    "paid tool",
    "paid tools",
    "paid research",
    "paid provider",
    "quota-heavy",
    "quota heavy",
    "buy credits",
    "purchase credits",
    "spend $",
    "spend money",
    "connector write",
    "gemini deep research",
    "tavily",
    "apify",
    "contact buyers",
    "interview buyers",
    "buyer interview",
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

TINY_MECHANICAL_TERMS = (
    "tiny edit",
    "mechanical edit",
    "five-minute edit",
    "5-minute edit",
    "one-line edit",
    "one line edit",
    "fix this typo",
    "correct this typo",
    "rename this file",
)

# Adaptive sensemaking vocabulary is intentionally shape-based and advisory.
# It selects a useful inquiry posture; it does not create a new permission or
# evidence gate. More specific signals are evaluated before broad ones.
CREATIVE_EXPLORATION_TERMS = (
    "brainstorm",
    "ideate",
    "explore ideas",
    "explore concepts",
    "creative exploration",
    "fictional",
    "fiction",
    "story concept",
    "visual concept",
    "speculative",
    "imagine",
    "moodboard",
    "rough prototype",
    "sketch a prototype",
)

PRODUCTION_REQUEST_TERMS = (
    "production-ready",
    "production ready",
    "final asset",
    "final version",
    "ship this",
    "ready to publish",
    "complete the asset",
    "implement this plan",
    "approved plan",
)

EXPLICIT_BUILD_DIRECTION_TERMS = (
    "just build",
    "build it now",
    "go straight to the asset",
    "proceed with the build",
    "do not research",
    "don't research",
)

STABLE_ANALYSIS_TERMS = (
    "explain",
    "analyze",
    "analyse",
    "compare",
    "evaluate",
    "technical question",
    "conceptual question",
    "canonical documentation",
    "primary literature",
    "original thinker",
)

CURRENT_WORLD_TERMS = (
    "current",
    "currently",
    "latest",
    "today",
    "right now",
    "time-sensitive",
    "time sensitive",
    "recent",
    "market landscape",
    "competitor landscape",
    "current price",
    "current pricing",
    "current law",
    "current regulation",
)

CURRENT_DECISION_CONTEXT_TERMS = (
    "decision",
    "decide",
    "choose",
    "recommend",
    "whether",
    "claim",
    "market",
    "competitor",
    "price",
    "pricing",
    "law",
    "regulation",
    "policy",
    "schedule",
    "standard",
    "specification",
    "software version",
    "risk",
)

BUYER_BEHAVIOR_TERMS = (
    "buyer pain",
    "buyer problem",
    "buyer problems",
    "customer pain",
    "customer problem",
    "market demand",
    "willingness to pay",
    "will pay",
    "anyone wants",
    "does anyone want",
    "validate demand",
    "market validation",
    "problem interview",
    "buyer interview",
    "interview buyers",
    "observed action",
    "payment behavior",
)

WEAK_EVIDENCE_TERMS = (
    "weak sources",
    "sources are weak",
    "weak and outdated",
    "weak evidence",
    "evidence is weak",
    "conflicting sources",
    "sources conflict",
    "conflicting evidence",
    "evidence conflicts",
    "outdated sources",
    "outdated evidence",
    "insufficient evidence",
    "shallow articles",
    "public articles alone",
)

PAID_OR_PERMISSIONED_INQUIRY_TERMS = (
    "paid research",
    "paid provider",
    "paid api",
    "quota-heavy",
    "quota heavy",
    "gemini deep research",
    "tavily",
    "apify",
    "contact buyers",
    "interview buyers",
    "buyer interview",
    "external interview",
)

ITERATION_REFRAME_TERMS = (
    "two substantive passes",
    "two passes without convergence",
    "we are not converging",
    "this is not converging",
    "third similar revision",
    "third materially similar revision",
    "we keep going back and forth",
    "rejected twice",
    "two rejected",
)

TASTE_CONTINUE_TERMS = (
    "direction is correct",
    "direction is right",
    "right direction",
    "remaining gap is taste",
    "remaining gap is craft",
    "taste only",
    "craft only",
    "keep the direction",
)

DISTINCT_BRANCH_TERMS = (
    "distinct branch",
    "separate branch",
    "research branch",
    "new branch",
    "branch deserves",
    "different objective",
)

DURABLE_BRANCH_TERMS = (
    "own objective",
    "own acceptance criteria",
    "own sources",
    "own next action",
    "retrieval home",
    "durable branch",
)

FRESH_PEN_REJECTION_TERMS = (
    "two rejected",
    "rejected twice",
    "second rejected",
    "two failed revisions",
    "revision rejected again",
)

FRESH_PEN_CONTEXT_TERMS = (
    "heavy context",
    "context fatigue",
    "context is contaminating",
    "context contamination",
    "taste revision",
    "taste-bearing",
    "spiraling",
)

EXPERT_COMPOSITION_TERMS = (
    "more than three experts",
    "four experts",
    "4 experts",
    "many plausible experts",
    "too many experts",
    "expert soup",
    "full arsenal",
)

PARALLEL_WORK_TERMS = (
    "independent workstreams",
    "parallelizable work",
    "parallel workstreams",
    "run in parallel",
)

VERIFICATION_OPPORTUNITY_TERMS = (
    "safe local verifier",
    "local verifier available",
    "verifier available",
    "verify before continuing",
    "verification need",
    "needs proof",
    "run the verifier",
)

CIRCULAR_CONTEXT_TERMS = (
    "going in circles",
    "circling",
    "repeating decisions",
    "same decision again",
)

PRESERVATION_OPPORTUNITY_TERMS = (
    "repeating one-off",
    "repeating one off",
    "repeatable system",
    "reusable-system opportunity",
    "reusable system opportunity",
    "do this every time",
    "keep doing this",
)

MONITORING_OPPORTUNITY_TERMS = (
    "monitor this",
    "recurring observation",
    "recurring follow-up",
    "check this regularly",
    "watch for changes",
)

CAPABILITY_LIFECYCLE_TERMS = (
    "capability stewardship",
    "capability awareness",
    "capabilities you can use",
    "context-container judgment",
    "context container judgment",
    "proactive leverage surfacing",
    "persistent default",
    "without requiring magic words",
    "without magic words",
)


def normalize(query: str) -> str:
    return re.sub(r"\s+", " ", query.lower()).strip()


def has_any(query: str, terms: Iterable[str]) -> bool:
    return any(term in query for term in terms)


def word_count(query: str) -> int:
    return len(re.findall(r"[a-z0-9][a-z0-9-]*", query.lower()))


def _escalation_brief(*, buyer_uncertainty: bool, weak_evidence: bool) -> dict[str, Any]:
    """Describe the smallest permissioned evidence route without launching it."""

    if buyer_uncertainty:
        return {
            "missing_evidence": "Behavioral evidence from qualified buyers; public articles are context, not validation.",
            "proposed_route": "Prepare a small safe-to-fail buyer or market probe; use /ash-problem-validation if interviews are approved.",
            "expected_cost_or_quota": "Unknown until the channel/provider is selected; no paid or quota-heavy use is authorized.",
            "permissions_required": "Explicit approval before interviews, outreach, external market interaction, or paid/quota-heavy research.",
            "deliverable": "Behavioral evidence table with observed action, disconfirming signals, and a bounded conclusion.",
            "decision_unlocked": "Whether the problem is important enough for the proposed buyer to act or pay now.",
        }
    return {
        "missing_evidence": (
            "Decision-grade primary evidence that resolves the weak, conflicting, or outdated claims."
            if weak_evidence
            else "Evidence unavailable through the authorized local or free-primary path."
        ),
        "proposed_route": "Prepare a source-quality and contradiction brief through /deep-research-os before any paid escalation.",
        "expected_cost_or_quota": "$0 direct spend for native public-source research; any paid or quota-heavy provider requires a fresh quote.",
        "permissions_required": "Explicit approval before paid/quota-heavy research or any external interview or outreach.",
        "deliverable": "Primary-source evidence map, counterevidence, confidence labels, and remaining unknowns.",
        "decision_unlocked": "Whether the consequential claim is strong enough to support the decision rather than a labeled hypothesis.",
    }


def build_inquiry_decision(
    query: str,
    *,
    route: str = "",
    lane: str = "",
) -> dict[str, Any]:
    """Select adaptive inquiry and build depth without adding an enforcement gate."""

    q = normalize(query)
    tiny_mechanical = has_any(q, TINY_MECHANICAL_TERMS) and word_count(q) <= 18
    taste_continue = has_any(q, TASTE_CONTINUE_TERMS)
    iteration_reframe = has_any(q, ITERATION_REFRAME_TERMS)
    buyer_uncertainty = has_any(q, BUYER_BEHAVIOR_TERMS)
    weak_evidence = has_any(q, WEAK_EVIDENCE_TERMS)
    paid_or_permissioned = has_any(q, PAID_OR_PERMISSIONED_INQUIRY_TERMS)
    current_world = has_any(q, CURRENT_WORLD_TERMS) and has_any(
        q,
        CURRENT_DECISION_CONTEXT_TERMS,
    )
    creative_exploration = has_any(q, CREATIVE_EXPLORATION_TERMS)
    stable_analysis = has_any(q, STABLE_ANALYSIS_TERMS)
    production_request = has_any(q, PRODUCTION_REQUEST_TERMS)
    explicit_build_direction = has_any(q, EXPLICIT_BUILD_DIRECTION_TERMS)

    decision: dict[str, Any]
    if tiny_mechanical:
        decision = {
            "mode": "execute",
            "build_purpose": "production",
            "research_path": "skip",
            "source_floor": "Supplied text or file plus ordinary correctness checks.",
            "reason": "This is a tiny mechanical change; inquiry ceremony would add no decision value.",
            "next_action": "Perform the edit directly and verify the changed surface.",
            "visible": False,
        }
    elif taste_continue:
        decision = {
            "mode": "create",
            "build_purpose": "production",
            "research_path": "skip",
            "source_floor": "Accepted direction and the user's live taste judgment.",
            "reason": "The direction is confirmed; the remaining uncertainty is taste or craft, not truth.",
            "next_action": "Preserve accepted elements and continue the craft refinement.",
            "visible": True,
            "iteration_posture": "taste-continue",
        }
    elif iteration_reframe:
        decision = {
            "mode": "analyze",
            "build_purpose": "decision",
            "research_path": "local",
            "source_floor": "Visible conversation history and explicitly accepted elements; never an invented revision count.",
            "reason": "Two visible substantive passes have not converged, so another similar revision would compound the wrong uncertainty.",
            "next_action": "Preserve accepted elements, diagnose truth versus intent, scope, mechanism, or taste, then change the approach.",
            "visible": True,
            "iteration_posture": "reframe",
        }
    elif explicit_build_direction:
        decision = {
            "mode": "execute",
            "build_purpose": "production",
            "research_path": "skip",
            "source_floor": "The supplied brief plus claim-local truth checks; explicit direction cannot waive hard boundaries.",
            "reason": "Farrice explicitly chose building over advisory depth for this pass.",
            "next_action": "Build now at the requested fidelity and label any untested real-world assumptions.",
            "visible": True,
            "iteration_posture": "continue",
        }
    elif production_request and creative_exploration:
        decision = {
            "mode": "execute",
            "build_purpose": "production",
            "research_path": "skip",
            "source_floor": "The supplied creative brief; fictional or speculative elements remain labeled rather than researched as fact.",
            "reason": "The creative direction is explicitly production-bound, so exploration can move directly into the asset.",
            "next_action": "Build the production asset now and apply the existing craft and quality checks.",
            "visible": False,
            "iteration_posture": "continue",
        }
    elif creative_exploration:
        decision = {
            "mode": "create",
            "build_purpose": "exploration",
            "research_path": "skip",
            "source_floor": "No evidence floor; label fictional, speculative, or untested material and use sources only as inspiration.",
            "reason": "The purpose is to expand the creative possibility space, not prove a real-world claim.",
            "next_action": "Create the requested concept or prototype without evidence questions.",
            "visible": False,
            "iteration_posture": "continue",
        }
    elif buyer_uncertainty:
        decision = {
            "mode": "probe",
            "build_purpose": "decision",
            "research_path": "escalate" if paid_or_permissioned or weak_evidence else "free-primary",
            "source_floor": "Behavioral evidence from qualified buyers; public articles may frame the probe but cannot validate demand.",
            "reason": "Human action and complex-market response cannot be researched into certainty.",
            "next_action": "Build the smallest safe-to-fail demand test and keep any conclusion labeled until behavior is observed.",
            "visible": True,
            "iteration_posture": "continue",
        }
        if paid_or_permissioned or weak_evidence:
            decision["escalation"] = _escalation_brief(
                buyer_uncertainty=True,
                weak_evidence=weak_evidence,
            )
    elif weak_evidence:
        decision = {
            "mode": "analyze",
            "build_purpose": "decision",
            "research_path": "escalate",
            "source_floor": "Primary or canonical evidence fit to the claim, with counterevidence where consequential.",
            "reason": "Weak, conflicting, or outdated evidence cannot support certainty.",
            "next_action": "Continue only with a labeled hypothesis or learning prototype and prepare the evidence escalation brief.",
            "visible": True,
            "iteration_posture": "continue",
            "escalation": _escalation_brief(
                buyer_uncertainty=False,
                weak_evidence=True,
            ),
        }
    elif paid_or_permissioned:
        decision = {
            "mode": "analyze",
            "build_purpose": "decision",
            "research_path": "escalate",
            "source_floor": "Evidence fit to the question before selecting a paid or permissioned collection route.",
            "reason": "The proposed inquiry crosses a cost, quota, or external-participation boundary.",
            "next_action": "Prepare the route, cost or quota, permissions, deliverable, and decision value; stop before launch.",
            "visible": True,
            "iteration_posture": "continue",
            "escalation": _escalation_brief(
                buyer_uncertainty=False,
                weak_evidence=False,
            ),
        }
    elif current_world:
        decision = {
            "mode": "analyze",
            "build_purpose": "decision",
            "research_path": "free-primary",
            "source_floor": "Recent official or primary sources plus counterevidence where the decision is consequential.",
            "reason": "The claim can drift and fresh evidence could change the decision.",
            "next_action": "Research the decision-changing claim, label confidence, and keep unresolved disagreement visible.",
            "visible": True,
            "iteration_posture": "continue",
        }
    elif stable_analysis:
        decision = {
            "mode": "analyze",
            "build_purpose": "decision",
            "research_path": "local",
            "source_floor": "Original thinkers, primary literature, or canonical documentation appropriate to the question.",
            "reason": "This is a knowable conceptual or technical question where authoritative analysis can change the answer.",
            "next_action": "Use the best authoritative local sources first and escalate to free primary sources only if the decision remains open.",
            "visible": True,
            "iteration_posture": "continue",
        }
    elif production_request:
        decision = {
            "mode": "execute",
            "build_purpose": "production",
            "research_path": "local",
            "source_floor": "The supplied brief and claim-local proof required by the asset.",
            "reason": "The goal and production standard are explicit enough to build now.",
            "next_action": "Build the production asset and apply existing quality, claim, privacy, permission, and cost boundaries locally.",
            "visible": False,
            "iteration_posture": "continue",
        }
    else:
        decision = {
            "mode": "execute",
            "build_purpose": "production",
            "research_path": "skip",
            "source_floor": "The supplied context plus claim-local verification when factual claims are introduced.",
            "reason": "No decision-changing research or uncertainty probe is warranted.",
            "next_action": "Proceed at the requested depth and verify the resulting work locally.",
            "visible": False,
            "iteration_posture": "continue",
        }

    # The route is context, not authority: an explicit creative or production
    # request can still proceed even when the owner can perform research.
    decision["route_context"] = {"route": route, "lane": lane}
    return decision


def render_inquiry_signal(decision: dict[str, Any]) -> str:
    """Return the single allowed material-fork line, or stay quiet."""

    if not decision.get("visible"):
        return ""
    labels = {
        "create": "Create",
        "analyze": "Analyze",
        "probe": "Probe",
        "execute": "Execute",
    }
    label = labels.get(str(decision.get("mode")), str(decision.get("mode")).title())
    return f"Mode: {label} — {decision['reason']}"


def capability_stewardship_decision(
    query: str,
    *,
    route: str = "",
    lane: str = "",
    risk_reasons: Iterable[str] = (),
) -> dict[str, Any]:
    """Choose one quiet capability/container move without creating new authority."""
    q = normalize(query)
    risks = list(risk_reasons)

    move = "continue"
    destination = "current-task"
    reason = "The current owner and context remain clean."
    visible = False
    recommendation = "Continue here."
    action = "Execute the scoped local work without interrupting the operator."
    why_now = "No material leverage fork is present."
    approval_boundary = "None for safe, reversible workspace-local work."

    tiny_mechanical = has_any(q, TINY_MECHANICAL_TERMS) and word_count(q) <= 18
    fresh_pen = has_any(q, FRESH_PEN_REJECTION_TERMS) and has_any(q, FRESH_PEN_CONTEXT_TERMS)
    distinct_branch = has_any(q, DISTINCT_BRANCH_TERMS)
    durable_branch = distinct_branch and has_any(q, DURABLE_BRANCH_TERMS)
    lifecycle_build = has_any(q, CAPABILITY_LIFECYCLE_TERMS) and (
        "persistent" in q or "default" in q or "session" in q or "magic words" in q
    )
    external_action = bool(risks) or has_any(q, RISK_TERMS)

    if tiny_mechanical:
        return {
            "container_decision": {"move": move, "destination": destination, "reason": reason},
            "capability_move": {
                "visible": visible,
                "recommendation": recommendation,
                "action": action,
            },
            "why_now": why_now,
            "approval_boundary": approval_boundary,
            "auto_task_creation": False,
            "route_context": {"route": route, "lane": lane},
        }

    if fresh_pen:
        move = "fresh-pen"
        destination = "/fresh-pen"
        reason = "Repeated taste rejection plus context fatigue makes a clean pen more valuable than another in-place revision."
        recommendation = "Move the taste-bearing artifact to a fresh pen with locked verdicts and proof."
        action = "Prepare the /fresh-pen packet; stop drafting in the fatigued context."
        why_now = "Two rejected revisions indicate context contamination, not another wording tweak."
        approval_boundary = "Packet preparation is local; creating or opening a new user-owned task requires explicit approval."
        visible = True
    elif durable_branch:
        move = "recommend-new-task"
        destination = "new-user-owned-task"
        reason = "The branch has its own objective, acceptance criteria, sources, and next action."
        recommendation = "Recommend a separate task and prepare a purpose-built transfer packet."
        action = "Prepare the focused packet only; do not create or open the task automatically."
        why_now = "A durable retrieval home now outweighs the coordination cost of a split."
        approval_boundary = "Explicit approval is required before creating or opening a user-owned task."
        visible = True
    elif distinct_branch:
        move = "handoff"
        destination = "/handoff"
        reason = "A distinct branch deserves separate ownership while the current task remains integration owner."
        recommendation = "Create a focused handoff for the branch."
        action = "Prepare a purpose-built /handoff packet without copying the full transcript."
        why_now = "Continuing here would blur ownership and weaken retrieval."
        approval_boundary = "The handoff may be prepared locally; creating or opening a user-owned task requires explicit approval."
        visible = True
    elif external_action:
        move = "continue"
        destination = "current-task"
        reason = "Preparation can continue safely, but the next state-changing action crosses an approval boundary."
        recommendation = "Prepare the publish or send action, then request approval."
        action = "Complete the local draft/checklist and stop before the external action."
        why_now = "The work is ready to approach an external state change."
        approval_boundary = "Explicit approval is required before publish, send, outreach, connector write, paid, destructive, or global action."
        visible = True
    elif has_any(q, VERIFICATION_OPPORTUNITY_TERMS) or has_any(q, CIRCULAR_CONTEXT_TERMS):
        move = "verify"
        destination = "local-verifier"
        reason = "A safe proof surface can resolve uncertainty faster than another explanation or loop."
        recommendation = "Run the safe local verifier before continuing."
        action = "Execute the available verifier now and use its result as the next decision input."
        why_now = "Behavior, claims, or repeated decisions need proof before more work compounds them."
        visible = True
    elif has_any(q, EXPERT_COMPOSITION_TERMS) or has_any(q, PARALLEL_WORK_TERMS):
        move = "bounded-support"
        destination = "/expert-composition-governor"
        reason = "Several plausible contributors need one function owner and bounded contribution slots."
        recommendation = "Keep one function owner and add only bounded expert support."
        action = "Name the owner, support slots, integration evidence, and skipped-expert reasons before any delegation."
        why_now = "The candidate set is large enough to create expert soup or coordination drag."
        approval_boundary = "Real Codex subagents still require explicit run-specific authorization."
        visible = True
    elif lifecycle_build or has_any(q, PRESERVATION_OPPORTUNITY_TERMS):
        move = "preserve"
        destination = "companion-contract"
        reason = "A recurring high-leverage move should survive the current session in the smallest reusable form."
        recommendation = "Preserve the method as a companion contract plus regression proof."
        action = "Extend the existing owner surfaces and verifier; do not create a new hot route."
        why_now = "The behavior is recurring enough that a one-off instruction would create future operator debt."
        visible = True
    elif has_any(q, MONITORING_OPPORTUNITY_TERMS):
        move = "monitor"
        destination = "approval-gated-monitor"
        reason = "The value depends on recurring observation instead of a one-time answer."
        recommendation = "Prepare the smallest useful monitor or recurring check."
        action = "Define the trigger, useful change, and stop condition before scheduling anything."
        why_now = "The underlying state can change after this session."
        approval_boundary = "Creating or changing an automation requires the applicable explicit approval."
        visible = True

    return {
        "container_decision": {"move": move, "destination": destination, "reason": reason},
        "capability_move": {
            "visible": visible,
            "recommendation": recommendation,
            "action": action,
        },
        "why_now": why_now,
        "approval_boundary": approval_boundary,
        "auto_task_creation": False,
        "route_context": {"route": route, "lane": lane},
    }


def infer_predicted_need(query: str, route: str = "", lane: str = "") -> str:
    q = normalize(query)
    classified = classify_control_intent(query)
    if classified["route"] == "system-audit":
        return "Diagnose the control-plane wiring failure, remove accidental route coupling, and prove the prompt hook no longer leaks expert suggestions."
    if route == "repeatability-spine" or has_any(
        q,
        (
            "final version got worse again",
            "brief gets worse",
            "brief gets worse and worse",
            "brief just gets worse",
            "gets worse and worse",
            "artifact gets worse",
            "copied over everything",
            "copied everything over",
            "copying everything over",
            "previous session import",
            "import from my previous session",
            "import from previous session",
            "same caliber",
            "same calibre",
            "caliber or level",
            "calibre or level",
            "massive difference",
            "script is just an explanation",
            "like notes and not actually copywriting",
            "one fix breaks something else",
            "notes pretending to be copy",
        ),
    ):
        return (
            "Preserve the last good creative behavior, isolate the regression, "
            "repair the failing surface, and add a gate so the same drift cannot ship again."
        )
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
    classified = classify_control_intent(query)
    if classified["route"] == "system-audit":
        return "A control-plane front door where routing, hooks, and defaults are classified by intent shape instead of brittle magic phrases."
    if route == "repeatability-spine":
        return "A replayable preservation lock that compares the prior good run against the current degraded run before changing the system."
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


def infer_edges(query: str, risk_reasons: Iterable[str] = (), route: str = "") -> list[str]:
    q = normalize(query)
    edges: list[str] = []
    if route == "repeatability-spine":
        edges.append("Preserve the good run before repairing the current system.")
        edges.append("Compare evidence from the prior session or golden sample against the degraded run before mutating routes.")
        edges.append("Use system-audit only after the repeatability delta identifies a control-plane failure.")
    elif has_any(q, OPERATOR_COCKPIT_TERMS):
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
    if route == "repeatability-spine" or has_any(
        q,
        (
            "final version got worse again",
            "script is just an explanation",
            "like notes and not actually copywriting",
            "one fix breaks something else",
            "notes pretending to be copy",
        ),
    ):
        return (
            "The repair names the preservation lock, fixes the degraded surface, "
            "adds a verifier or fixture for the exact failure phrase, and only "
            "promotes the artifact after the regression guard passes."
        )
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


def missing_inputs(query: str, route: str = "") -> list[str]:
    q = normalize(query)
    missing: list[str] = []
    if route != "repeatability-spine" and has_any(q, OPERATOR_COCKPIT_TERMS):
        if not any(term in q for term in ("implement", "approved", "success", "prove", "quality", "bar", "standard", "verify")):
            missing.append("operator_success_standard")
        if not any(term in q for term in ("local", "global", "~/.codex", "workspace")):
            missing.append("scope_boundary")
        if not any(term in q for term in ("capture", "friction", "failure", "retrieval", "organization", "files")):
            missing.append("failure_capture_policy")
    if not has_any(q, ACTION_TERMS) and word_count(q) < 8:
        missing.append("deliverable")
    if not any(term in q for term in ("for ", "audience", "client", "user", "customer", "buyer", "avatar", "reader", "prospect", "farrice")):
        missing.append("audience")
    if not any(
        term in q
        for term in (
            "done",
            "success",
            "good",
            "prove",
            "quality",
            "bar",
            "standard",
            "verify",
            "production-ready",
            "production ready",
            "copy gate",
            "pass the copy gate",
            "passes the copy gate",
            "generic and scientific",
            "stating facts rather than appealing",
            "stating facts instead of appealing",
            "human psychology and copywriting",
            "research word banks",
            "research word bank",
            "customer avatar language",
            "avatar language",
            "word banks",
            "word bank",
            "script is just an explanation",
            "script is explanation",
            "like notes and not actually copywriting",
            "not actually copywriting",
            "notes pretending to be copy",
            "one fix breaks something else",
            "one fix and then something else breaks",
            "final version got worse again",
            "got worse again with the script",
            "paid-ad voiceover",
            "paid ad voiceover",
            "spoken ad copy",
            "recordable as-is",
            "recordable as is",
            "vo-only gate",
            "vo only gate",
        )
    ):
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
    if route == "repeatability-spine":
        primary = "repeatability-spine"
        support = ["system-audit", "routing-intelligence"]
        reason = "Prior-session or golden-run quality drift belongs to /repeatability-spine before control-plane repair."
    elif has_any(q, OPERATOR_COCKPIT_TERMS):
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
    route: str = "",
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
    classified = classify_control_intent(query)
    if classified["route"] == "system-audit" and route in {"", "system-audit"}:
        return {
            "decision": "run_with_assumptions",
            "reason": "Control-plane complaint is already classified; run local proof-first diagnosis instead of asking broad cockpit questions.",
            "requires_pause": False,
        }
    operator_missing = {
        "operator_success_standard",
        "scope_boundary",
        "failure_capture_policy",
    } & set(missing)
    if route != "repeatability-spine" and has_any(q, OPERATOR_COCKPIT_TERMS) and operator_missing:
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
    risk_reasons = tuple(risk_reasons)
    classified = classify_control_intent(query)
    inquiry = build_inquiry_decision(query, route=route, lane=lane)
    missing = missing_inputs(query, route)
    if classified["route"] == "system-audit" and route in {"", "system-audit"}:
        missing = []
    questions = questions_for(missing, query)
    pause = pause_or_run(
        query=query,
        missing=missing,
        route=route,
        risk_reasons=risk_reasons,
        clarity_score=clarity_score,
    )
    if (
        inquiry["mode"] == "create"
        and inquiry["build_purpose"] == "exploration"
        and not risk_reasons
        and not has_any(normalize(query), RISK_TERMS)
    ):
        questions = []
        pause = {
            "decision": "run_creative_exploration",
            "reason": "Creative exploration is clear enough to begin; label speculation and do not add evidence ceremony.",
            "requires_pause": False,
        }
    bias = route_bias(query, route, lane)
    center = infer_center(query, route, lane)
    success = infer_success_standard(query, route)
    constraints = infer_edges(query, risk_reasons, route)
    stewardship = capability_stewardship_decision(
        query,
        route=route,
        lane=lane,
        risk_reasons=risk_reasons,
    )
    return {
        "schema_version": "co-creative-launchpad/v3",
        "predicted_need": infer_predicted_need(query, route, lane),
        "center": center,
        "edges": constraints,
        "success_standard": success,
        "constraints": constraints,
        "missing_inputs": missing,
        "questions_that_change_execution": questions,
        "route_bias": bias,
        "pause_or_run": pause,
        "inquiry_decision": inquiry,
        **stewardship,
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
            "inquiry_decision": inquiry,
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
    inquiry_signal = render_inquiry_signal(packet["inquiry_decision"])
    if inquiry_signal:
        lines.append(f"- **{inquiry_signal}**")
    capability = packet.get("capability_move", {})
    if capability.get("visible"):
        container = packet.get("container_decision", {})
        lines.extend(
            [
                f"- **Container decision**: {container.get('move')} - {container.get('reason')}",
                f"- **Capability recommendation**: {capability.get('recommendation')}",
                f"- **Why now**: {packet.get('why_now')}",
                f"- **What I can do**: {capability.get('action')}",
                f"- **Approval boundary**: {packet.get('approval_boundary')}",
            ]
        )
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
