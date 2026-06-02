#!/usr/bin/env python3
"""
Routing Enforcer — Runtime validation of mandatory workflow bindings.

Source of truth for the "Mandatory Workflow Routing" table in CLAUDE.md.
This module exists because the 2026-04-21 incident proved that routing
guidance in markdown alone is advisory — Claude can read CLAUDE.md and
still pick the wrong workflow when the user's conversational ask points
elsewhere. This module makes the binding deterministic: code-checked,
not norm-checked.

Two modes:
    1. Pre-flight check (Claude calls before producing):
        python3 execution/routing_enforcer.py check \\
            --request "next parallax substack" --workflow writers-room
       Returns non-zero exit + JSON if invalid; logs the decision.

    2. Post-hoc validation (auto-fires from chain_runner.py finalize()
       when --workflow is supplied; flags violations into traces).

Both modes append a JSONL entry to:
    evolution_store/traces/routing_decisions.jsonl

Update BINDINGS to add new mandatory routes. Pattern: a domain signal
(set of keyword phrases) maps to ONE mandatory workflow and a list of
workflows that must NEVER substitute.
"""

import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

TRACE_DIR = Path(__file__).parent.parent / "evolution_store" / "traces"
ROUTING_LOG = TRACE_DIR / "routing_decisions.jsonl"

# ─────────────────────────────────────────────────────────
# MANDATORY BINDINGS — Source of truth for routing enforcement
# Mirror of CLAUDE.md "Mandatory Workflow Routing" table.
# Update both together; reference https://example/audit if adding new bindings.
# ─────────────────────────────────────────────────────────

BINDINGS = [
    {
        "id": "parallax_editions",
        "signal_phrases": [
            "parallax edition",
            "parallax substack",
            "next substack",
            "parallax prompt pack",
            "parallax post",
            "parallax draft",
        ],
        # Operation-class signals that override this production binding. When ANY
        # of these are also present, the user wants to OPERATE ON an existing
        # edition (atomize / polish / extract / refine), not PRODUCE a new one.
        # Added 2026-05-23 to fix Bug #3 from Wave 5 validation (false halt on
        # "atomize the most recent Parallax edition into 11 derivatives").
        "negative_signals": [
            "atomize", "remix", "platform-adapt", "platform adapt",
            "polish", "refine", "diagnose", "review", "study", "extract",
            "derivative", "derivatives", "spin into", "spin this into",
            "audit", "analyze",
        ],
        "mandatory_workflow": "parallax",
        "forbidden_workflows": ["writers-room"],
        "reason": (
            "Parallax editions require Phase 2.5 GROUND + ZEITGEIST and the full "
            "/parallax production sequence. writers-room is diagnostic-on-draft, "
            "not production-from-raw-take. Edition 02 shipped 7 fabrications when "
            "this binding was violated (2026-04-21)."
        ),
        "override_flag": "--no-ground",
        "override_warning": (
            "Only use --no-ground when the edition has zero external factual surface "
            "(pure memoir with no public figures, events, brands, or stats)."
        ),
    },
    {
        "id": "linkedin_from_scratch",
        "signal_phrases": [
            "linkedin post from scratch",
            "write a linkedin post",
            "draft a linkedin post",
            "new linkedin post",
            "linkedin content from scratch",
            "linkedin post production",
        ],
        "mandatory_workflow_any_of": [
            "ghostwrite",
            "lara-acosta-linkedin-ghostwriting",
            "high-dwell",
        ],
        "forbidden_workflows": ["writers-room"],
        "reason": (
            "LinkedIn post production from scratch requires Lara Acosta's pattern "
            "library (engineered virality, SLAY format, headline=pain+for-whom+proof). "
            "writers-room is for refinement of an existing draft, not first-pass production."
        ),
    },
    {
        "id": "writers_room_refinement",
        "signal_phrases": [
            "refine this draft",
            "improve this draft",
            "polish this draft",
            "writers room",
            "writer's room",
            "diagnose this content",
            "fix this draft",
        ],
        "mandatory_workflow": "writers-room",
        "forbidden_workflows": ["parallax", "ghostwrite", "high-dwell"],
        "reason": (
            "Writers' room is the diagnosis-and-treatment workflow for an EXISTING "
            "draft. Production workflows (/parallax, /ghostwrite) are for first-pass "
            "creation from raw input. Wrong direction = wrong tool."
        ),
    },
    {
        "id": "cold_start_converting_copy",
        "signal_phrases": [
            "converting copy from scratch",
            "cold start copy",
            "cold-start copy",
            "end-to-end copy",
            "write converting copy for",
            "copy that converts for",
            "vsl from scratch",
            "sales page from scratch",
            "ground the market and write",
        ],
        # Refinement / operate-on-existing signals route to the lean standalone
        # copy-blocks workflows (which reuse the market cache at $0), NOT a fresh
        # cold-start grounding run that would re-pay to ground.
        "negative_signals": [
            "refine", "polish", "improve this", "audit", "review this draft",
            "tweak", "rewrite this", "edit this", "diagnose",
        ],
        "mandatory_workflow": "copy-engine",
        "forbidden_workflows": [],
        "reason": (
            "Cold-start converting copy requires REAL market grounding before "
            "writing. /copy-engine routes through avatar_manifold_runner (ground "
            "once, reuse free) and gates proof via verify_proof_ledger. Writing from "
            "ungrounded context is the 'false confidence / fabricated market' failure "
            "mode. Refining EXISTING copy reuses the cache via the standalone "
            "copy-blocks workflows at $0 — those are not forbidden here."
        ),
        "override_flag": "--no-ground",
        "override_warning": (
            "Only --no-ground when you supply the market intelligence yourself "
            "(a manifold or VOC file); else the copy is built on [MODELED] guesses."
        ),
    },
    {
        "id": "brand_operating_system",
        "signal_phrases": [
            "brand operating system",
            "brand os",
            " bos ",
            "build a bos",
            "build a complete brand system",
            "full brand system for",
            "resonance-style package",
            "the kind of thing we built for andrea",
            "creative briefs and business documents and ai handoff",
            "6-layer brand",
            "six-layer brand",
        ],
        "mandatory_workflow": "build-bos",
        "forbidden_workflows": [
            "brand-system-builder",
            "design-md-synthesize",
            "brand-library",
        ],
        "reason": (
            "A complete Brand Operating System requires the orchestrated 7-phase "
            "build (Discovery → Foundation → Visual → Briefs → Marketing → AI Handoff "
            "→ Wrap) producing 43 docs across 6 layers. Single-component invocations "
            "(brand-system-builder agent, design-md-synthesize, brand-library) are "
            "Phase B/C components, not replacements for the orchestrated build. "
            "Skipping the orchestration loses the master-creative-brief inheritance, "
            "the AI Brain Master compression discipline, and the cross-phase quality "
            "gates that catch structural bugs (Resonance had a CRITICAL file-numbering "
            "bug that only Phase G1 adversarial review caught after 6 human reviews)."
        ),
        "override_flag": None,
        "override_warning": (
            "If the scope is genuinely a single layer (e.g., 'just make me a "
            "DESIGN.md'), use the component skill directly — the binding only fires "
            "when the request signals a complete BOS scope."
        ),
    },
    {
        "id": "supercomputer_mission",
        "signal_phrases": [
            "build me a brand for",
            "build a brand for",
            "build a brand around",
            "brand identity for",
            "launch a brand called",
            "start a brand called",
            "make me a campaign for",
            "make a campaign for",
            "run a campaign for",
            "launch a campaign for",
            "full marketing for",
            "full content drop on",
            "full content drop for",
            "marketing plan and assets for",
            "drop a campaign for",
            "ugc ad for",
            "ad campaign for",
            "complete asset pack for",
            "brief and visuals and copy for",
            "supercomputer",
        ],
        "mandatory_workflow": "supercomputer",
        "forbidden_workflows": [],
        "reason": (
            "Multi-deliverable marketing/creative missions require the anchor-memory "
            "+ pre-flight cost gate pattern. Running single-skill workflows for these "
            "produces incoherent outputs (each deliverable invents its own brand "
            "context). The Supercomputer composes existing skills (/build-bos, "
            "/parallax, /ghostwrite, fantastic-posters, Higgsfield MCP, Veo) and "
            "enforces project-scoped state via execution/anchor_memory.py + "
            "execution/cost_gate.py. Self-hosted Higgsfield Supercomputer equivalent. "
            "Trigger phrases live in directives/supercomputer-mode.md — update both "
            "this list AND that doc together when adding new triggers."
        ),
        "override_flag": None,
        "override_warning": (
            "If the request is genuinely single-deliverable (e.g., 'write me one "
            "LinkedIn post'), use the specific skill directly — the binding fires "
            "only when the request signals cross-deliverable cohesion."
        ),
    },
    {
        "id": "autopilot_orchestration",
        "signal_phrases": [
            "autopilot",
            "run end-to-end",
            "ship it end to end",
            "no gates",
            "just execute",
            "stop asking just do",
            "run the full thing",
            "true autopilot",
        ],
        "mandatory_workflow": "autopilot",
        "forbidden_workflows": [
            "supercomputer", "jcc-deploy", "campaign", "big-project",
        ],
        "reason": (
            "Autopilot is the gate-suppression dispatcher. When the user signals "
            "'run end-to-end' / 'no gates' / 'autopilot', they want zero "
            "mid-execution gates. Running supercomputer / jcc-deploy / campaign / "
            "big-project directly will halt at the Phase 1 'Proceed?' / approve / "
            "adjust gate. /autopilot picks the right orchestrator under the hood, "
            "runs it with halts suppressed, surfaces only taste-level gates "
            "(G1 intent-too-vague, G2 paid-cost > $5, G3 prose FLAGGED at "
            "Expert Standard ≥ 7). See .agent/workflows/autopilot.md."
        ),
        "override_flag": "--manual",
        "override_warning": (
            "Use --manual to restore conventional halt-and-confirm gates for "
            "high-stakes missions. Default autopilot behavior is 3-gates-only."
        ),
    },
    {
        # Phase C (2026-05-25) — Vertical Bootstrap
        # Mirrors VERTICAL_BOOTSTRAP_SIGNALS in execution/intent_to_package.py.
        # Update both together when adding new signal phrases.
        "id": "vertical_bootstrap",
        "signal_phrases": [
            "verticalize",
            "bootstrap a vertical",
            "bootstrap a new vertical",
            "bootstrap a domain",
            "new vertical for",
            "i'm entering",
            "i am entering",
            "entering the ",
            "new niche of ",
            "set up a new niche",
            "set up a vertical",
            "stand up a new vertical",
            "stand up a domain",
            "from zero in ",
            "from scratch in the ",
            "no audience yet for ",
            "no voice doc yet",
            "calibrate for ",
            "build the stack for ",
            "spin up calibration for",
        ],
        "mandatory_workflow": "verticalize",
        "forbidden_workflows": ["build-bos", "brand-arena", "zero-to-brand"],
        "reason": (
            "Vertical bootstrap is zero-state setup for a NEW domain (no voice doc, "
            "no ICP, no expert routing yet). /verticalize is the system-tier "
            "conductor that composes ICP + voice + ground-truth + routing + "
            "per-project CLAUDE.md generation. /build-bos, /brand-arena, and "
            "/zero-to-brand assume the vertical is CALIBRATED already; they "
            "produce brand-layer assets ON TOP of an existing voice + ICP. "
            "Wrong direction = brand layer built on un-calibrated foundation."
        ),
        "override_flag": "--skip-2.5",
        "override_warning": (
            "Use --skip-2.5 ONLY when verticalizing a domain you're already "
            "deeply expert in (lived experience) and can confirm ICP + voice "
            "from memory. Skipping Phase 2.5 in any other case guarantees "
            "grade inflation in the new vertical from day one."
        ),
    },
    {
        # Context Engineering OS (2026-05-30) — skills/chase-hughes-context-engineering.
        # Mirror of the CLAUDE.md Mandatory Routing row. The deterministic ethics
        # gate (execution/context_ethics_gate.py) is the backstop for all /ce-* output.
        "id": "context_engineering",
        "signal_phrases": [
            "context engineering",
            "engineer the context",
            "engineer conditions",
            "engineer the conditions",
            "design the conditions",
            "make the behavior automatic",
            "make the outcome inevitable",
            "make buying feel automatic",
            "what's upstream of",
            "what is upstream of",
            "context where the behavior",
            "perfect recipient first",
            "pcp design",
            "design the context so",
        ],
        # Multi-deliverable mission language defers to /supercomputer (which can call
        # /ce-build internally). Keeps single context-design intent on /ce-design.
        "negative_signals": [
            "full campaign for", "build me a brand for", "build a brand for",
            "complete asset pack", "full content drop",
        ],
        "mandatory_workflow": "ce-design",
        "forbidden_workflows": [],
        "reason": (
            "Requests to engineer the CONTEXT/CONDITIONS where a behavior becomes "
            "automatic (vs. pushing the outcome with a single tactic) route to "
            "/ce-design — the Context Engineering OS in skills/chase-hughes-context-"
            "engineering. /ce-design runs upstream -> force-map -> PCP -> conditions -> "
            "DEFENSE/ETHICS GATE -> followability and emits a Context-Design Spec. "
            "PRECEDENCE: /ce-design produces the spec; the routed PRODUCTION expert "
            "(Luke Iha copy, Lara Acosta LinkedIn, Caleb 4C, etc.) then writes INTO it "
            "— context design first, production second; never a single-tactic copy "
            "workflow alone when the user asked to engineer the context. The Defense/"
            "Ethics Gate is enforced deterministically by execution/context_ethics_gate.py "
            "(avoids the banned AI-memory-dependent-observability pattern). Multi-"
            "deliverable missions defer to /supercomputer, which composes /ce-build."
        ),
        "override_flag": None,
        "override_warning": (
            "If the user wants a single finished asset and NOT a context design "
            "(e.g. 'write me one LinkedIn post'), route to the production skill "
            "directly. /ce-design fires when the ask is to design the conditions / "
            "context, not to write one tactic."
        ),
    },
    {
        # Avatar Manifold cold-start (2026-05-31) — skills/luke-iha-avatar-machine.
        # Building an avatar/ICP/manifold from scratch for a market with no
        # pre-provided VOC requires the Phase 0 GROUND research execution
        # (execution/avatar_manifold_runner.py: Gemini Deep Research foundation +
        # Apify VOC scrape + FB Ad Library + Recall, gated by research_quality_gate
        # --strict). The GROUND phase is the deterministic backstop; this binding
        # makes /avatar-manifold (or the /avatar-machine orchestrator) the enforced
        # cold-start entry and forbids reasoning-only ICP substitutes that skip
        # real-VOC research and produce modeled language (genius.md rubric crit 6).
        "id": "avatar_manifold_coldstart",
        "signal_phrases": [
            "build an avatar", "build the avatar", "avatar manifold",
            "build an icp", "build a manifold", "build the manifold",
            "plot the market", "market intelligence package",
            "cold start avatar", "icp from scratch", "manifold for the",
            "avatar for the", "avatar machine",
        ],
        # Operate-on-existing language defers (audit an avatar, route to copy).
        "negative_signals": [
            "audit", "score this", "route", "to copy", "manifold to copy",
            "already have a manifold", "refine the avatar", "existing avatar",
        ],
        "mandatory_workflow": "avatar-manifold",
        "forbidden_workflows": ["icp-build", "icp-research", "icp-deep-dive"],
        "reason": (
            "Building an avatar/ICP/manifold from scratch requires the Phase 0 "
            "GROUND research execution (execution/avatar_manifold_runner.py: Gemini "
            "Deep Research + Apify VOC + FB Ad Library + Recall, gated by "
            "research_quality_gate.py --strict). Reasoning-only ICP workflows "
            "(icp-build, icp-research, icp-deep-dive) model the structure but do NOT "
            "fire real research, producing modeled language that fails genius.md "
            "rubric criterion 6 (specific-language). GROUND is the deterministic "
            "backstop that makes real VOC the default; it cannot be silently skipped. "
            "Use /avatar-machine for full cold-start → finished-copy orchestration."
        ),
        "override_flag": "--no-ground",
        "override_warning": (
            "Only use --no-ground when the user supplies their own real VOC (e.g. an "
            "existing deep ICP via --voc-file). Skipping GROUND on a zero-VOC cold "
            "start guarantees modeled language and rubric criterion-6 failure."
        ),
    },
    {
        # Placed LAST so domain-specific bindings (avatar, copy, parallax, BOS)
        # take precedence. This is the catch-all for GENERIC research that would
        # otherwise be answered from training memory instead of grounded in truth.
        "id": "unified_research",
        "signal_phrases": [
            "deep research", "do deep research", "research this", "research the market",
            "strategic intelligence on", "comprehensive research on", "research report on",
            "research the landscape", "go deep on", "ground this in research",
        ],
        # Domains with their own grounding bindings (above) handle their own research;
        # operate-on-existing language defers to refinement workflows.
        "negative_signals": [
            "avatar", "manifold", "icp", "cold start copy", "cold-start copy",
            "converting copy", "vsl", "sales page", "brand operating system",
            "parallax", "refine", "audit", "polish",
        ],
        "mandatory_workflow_any_of": ["deep-research", "deep-research-swarm",
                                       "deep-research-gemini", "research-swarm"],
        "forbidden_workflows": [],
        "reason": (
            "Generic research must route through the Unified Research Engine "
            "(execution/research.py). For deep/max, the PRIMARY is the native expert "
            "SWARM (.agent/workflows/deep-research-swarm.workflow.js): decompose → cast "
            "world-class personas → parallel fan-out → gap-fill → adversarial verify → "
            "synthesize, $0 incremental, Gemini Deep Research merging in parallel. The "
            "bedrock floor (Tavily research/extract + WebSearch/WebFetch) guarantees a "
            "real, sourced result at $0 even if every paid path fails. Every result "
            "carries an honest Research Receipt. Answering research from training memory "
            "instead of grounding it in live, cited sources is the failure this prevents."
        ),
    },
]


def _normalize_workflow(name: str) -> str:
    """Strip leading slashes/at-signs and lowercase for comparison."""
    return name.lower().lstrip("/@").strip()


def _request_hits_signal(request: str, signal_phrases: List[str]) -> Optional[str]:
    """Return the first signal phrase that appears in the request, or None."""
    request_lower = request.lower()
    for phrase in signal_phrases:
        if phrase.lower() in request_lower:
            return phrase
    return None


def check_routing(request: str, chosen_workflow: str) -> Dict[str, Any]:
    """
    Validate a routing decision against mandatory bindings.

    Args:
        request: The user's original request (or sharpened intent).
        chosen_workflow: The workflow Claude proposes to run (with or without /).

    Returns:
        {
            "valid": bool,
            "binding_matched": str | None,    # binding id that fired
            "matched_signal": str | None,     # which phrase matched
            "mandatory_workflow": str | list | None,
            "chosen_workflow": str,
            "violation_reason": str | None,   # why it's invalid (if invalid)
            "advisory": str | None,           # informational notes (e.g., override flag)
        }

    A request that doesn't match any binding is automatically valid —
    bindings only fire when the signal is present.
    """
    chosen_norm = _normalize_workflow(chosen_workflow)
    result = {
        "valid": True,
        "binding_matched": None,
        "matched_signal": None,
        "mandatory_workflow": None,
        "chosen_workflow": chosen_norm,
        "violation_reason": None,
        "advisory": None,
    }

    request_lower = request.lower()
    for binding in BINDINGS:
        matched_signal = _request_hits_signal(request, binding["signal_phrases"])
        if not matched_signal:
            continue

        # Operation-class override (added 2026-05-23 — Bug #3 fix). If the
        # request also names an operation that supersedes production (atomize,
        # polish, extract, etc.), this production binding does NOT fire.
        # Lets atomize-this-existing-edition / polish-this-draft / etc. flow
        # through the resolver to the correct downstream workflow.
        negative_signals = binding.get("negative_signals") or []
        if any(neg.lower() in request_lower for neg in negative_signals):
            continue

        # Signal matched — this binding applies.
        result["binding_matched"] = binding["id"]
        result["matched_signal"] = matched_signal

        mandatory = binding.get("mandatory_workflow")
        mandatory_any_of = binding.get("mandatory_workflow_any_of")
        forbidden = [_normalize_workflow(w) for w in binding.get("forbidden_workflows", [])]

        # Is the chosen workflow forbidden for this signal?
        if chosen_norm in forbidden:
            result["valid"] = False
            result["mandatory_workflow"] = mandatory or mandatory_any_of
            result["violation_reason"] = (
                f"Signal '{matched_signal}' triggers binding '{binding['id']}'. "
                f"Workflow '{chosen_norm}' is forbidden for this domain. "
                f"Required: {result['mandatory_workflow']}. "
                f"Reason: {binding['reason']}"
            )
            if binding.get("override_flag"):
                result["advisory"] = (
                    f"Override available via {binding['override_flag']}. "
                    f"{binding.get('override_warning', '')}"
                )
            return result

        # Does the chosen workflow match the mandatory one?
        if mandatory:
            if chosen_norm != _normalize_workflow(mandatory):
                result["valid"] = False
                result["mandatory_workflow"] = mandatory
                result["violation_reason"] = (
                    f"Signal '{matched_signal}' triggers binding '{binding['id']}'. "
                    f"Mandatory workflow is '{mandatory}', got '{chosen_norm}'. "
                    f"Reason: {binding['reason']}"
                )
                return result

        if mandatory_any_of:
            allowed = [_normalize_workflow(w) for w in mandatory_any_of]
            if chosen_norm not in allowed:
                result["valid"] = False
                result["mandatory_workflow"] = mandatory_any_of
                result["violation_reason"] = (
                    f"Signal '{matched_signal}' triggers binding '{binding['id']}'. "
                    f"Workflow must be one of {mandatory_any_of}, got '{chosen_norm}'. "
                    f"Reason: {binding['reason']}"
                )
                return result

        # Signal matched + workflow valid — record for trace, return ok.
        result["mandatory_workflow"] = mandatory or mandatory_any_of
        return result

    # No binding fired — request doesn't match any signal.
    return result


def log_decision(request: str, chosen_workflow: str, validation: Dict[str, Any],
                 source: str = "cli", override_used: Optional[str] = None) -> None:
    """Append a routing decision to evolution_store/traces/routing_decisions.jsonl."""
    try:
        TRACE_DIR.mkdir(parents=True, exist_ok=True)
        entry = {
            "timestamp": datetime.now().isoformat(),
            "source": source,
            "request": request[:500],
            "chosen_workflow": chosen_workflow,
            "valid": validation["valid"],
            "binding_matched": validation.get("binding_matched"),
            "matched_signal": validation.get("matched_signal"),
            "mandatory_workflow": validation.get("mandatory_workflow"),
            "violation_reason": validation.get("violation_reason"),
            "override_used": override_used,
        }
        with open(ROUTING_LOG, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception:
        # Logging is non-fatal — never block a chain on observability.
        pass

    # Sprint 1: also store as episodic/decision in sovereign memory so routing
    # decisions are queryable alongside finalize milestones and cost events.
    try:
        try:
            from memory_store import store_memory_silent, _detect_workspace
        except ImportError:
            from execution.memory_store import store_memory_silent, _detect_workspace
        verdict = "VALID" if validation.get("valid") else "VIOLATION"
        store_memory_silent(
            tier="episodic",
            category="decision",
            content=f"ROUTING {verdict}: chose={chosen_workflow} for '{request[:80]}'",
            metadata={
                "source": "routing_enforcer",
                "binding": validation.get("binding_matched"),
                "matched_signal": validation.get("matched_signal"),
                "mandatory_workflow": validation.get("mandatory_workflow"),
                "violation": validation.get("violation_reason"),
                "override_used": override_used,
                "workspace": _detect_workspace(),
            },
        )
    except Exception:
        # Memory ingestion is non-fatal — never block a chain on memory failure.
        pass


def list_bindings() -> List[Dict[str, Any]]:
    """Return all mandatory bindings (for inspection / sync with CLAUDE.md)."""
    return BINDINGS


def main():
    parser = argparse.ArgumentParser(description="Routing Enforcer — validate workflow choices against mandatory bindings.")
    sub = parser.add_subparsers(dest="command")

    chk = sub.add_parser("check", help="Validate a routing decision")
    chk.add_argument("--request", required=True, help="The user's original request or sharpened intent")
    chk.add_argument("--workflow", required=True, help="The chosen workflow name (with or without leading /)")
    chk.add_argument("--source", default="cli", help="Caller identifier for trace log (default: cli)")
    chk.add_argument("--override", default=None, help="Override flag the model invoked (e.g. --no-ground)")
    chk.add_argument("--quiet", action="store_true", help="Only print on violation; exit non-zero on invalid")

    sub.add_parser("list", help="Print all mandatory bindings as JSON")

    args = parser.parse_args()

    if args.command == "check":
        result = check_routing(args.request, args.workflow)
        log_decision(args.request, args.workflow, result, source=args.source, override_used=args.override)
        if not result["valid"]:
            print(json.dumps(result, indent=2))
            sys.exit(2)  # Non-zero exit on violation
        if not args.quiet:
            print(json.dumps(result, indent=2))
        sys.exit(0)

    if args.command == "list":
        print(json.dumps(BINDINGS, indent=2))
        sys.exit(0)

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
