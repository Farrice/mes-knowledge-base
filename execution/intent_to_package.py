#!/usr/bin/env python3
"""
Intent → Mission Package resolver (Autopilot Wave 4 / 2026-05-21).

Pure-Python prescriptive routing. Same signal-phrase pattern as
`routing_enforcer.BINDINGS` (restrictive: "you may not use X"), but
this module is PRESCRIPTIVE: "for this intent, here is the assembled
mission package" — workflow + skills + experts + plugins + cost tier
+ fan-out pattern.

Why it exists: 232 skills + 886 workflows + 24 experts is too much
surface area to mentally compose for every session. This is the
cognitive-compression layer — fuzzy intent in, full package out.

Seven outcome classes (see directives/autopilot-mode.md for full doc):
    1. Single Deliverable Production
    2. Multi-Deliverable Mission
    3. Research / Intelligence
    4. Creative Atomization
    5. System / Maintenance
    6. Refinement / Diagnosis
    7. Freeform / Unclassified

Wave 4 ships ONLY class #3 (Research) populated; others stub to
freeform_default. Wave 5 populates the remaining 6.

CLI:
    python3 execution/intent_to_package.py resolve --intent "research the current state of X" --json
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Tuple


@dataclass
class MissionPackage:
    outcome_class: str
    primary_workflow: str
    sub_workflows: List[str] = field(default_factory=list)
    experts: List[str] = field(default_factory=list)
    skills_to_load: List[str] = field(default_factory=list)
    plugins: List[str] = field(default_factory=list)
    cost_tier: str = "free"             # free | cheap | medium | heavy
    fanout_pattern: str = "sequential"  # parallel | sequential
    gates_to_surface: List[str] = field(default_factory=list)
    confidence: float = 0.0
    reasoning: str = ""
    matched_signals: List[str] = field(default_factory=list)


# ─────────────────────────────────────────────────────────────
# BINDINGS — outcome class definitions (signal phrases → package)
# Mirror of the Wave 4 plan + autopilot-mode.md when it ships.
# Update both together — signal phrases are the user-facing contract.
# ─────────────────────────────────────────────────────────────

# Wave 4: only Research is populated. Others stub to freeform_default
# until Wave 5.

RESEARCH_SIGNALS = [
    "research the",
    "research on",
    "deep research",
    "competitive intel",
    "competitive intelligence",
    "what's the landscape",
    "landscape for",
    "market landscape",
    "investigate ",
    "study the",
    "what does the market",
    "comparative analysis",
    "literature review",
    "intelligence brief",
    "deep dive on",
    "deep dive into",
]

REFINEMENT_SIGNALS = [
    "polish this",
    "polish the",
    "writers room on",
    "writers' room on",
    "writer's room on",
    "refine this",
    "refine the",
    "diagnose this",
    "diagnose why",
    "review and fix",
    "fix this draft",
    "improve this draft",
]

MULTI_DELIVERABLE_SIGNALS = [
    "build me a brand for",
    "build a brand for",
    "make me a campaign for",
    "make a campaign for",
    "full content drop on",
    "full marketing for",
    "launch ",
    "hero shot and",
    "campaign for ",
]

ATOMIZATION_SIGNALS = [
    "atomize ",
    "atomize this",
    "remix this into",
    "platform-adapt",
    "make derivatives from",
    "derivatives of this",
    "11 derivatives",
]

SYSTEM_MAINTENANCE_SIGNALS = [
    "audit the system",
    "system audit",
    "system pulse",
    "evolve skill",
    "knowledge compiler",
    "sync instructions",
    "system health",
    "maintenance pass",
]

SINGLE_DELIVERABLE_SIGNALS = [
    "write me one",
    "draft a ",
    "draft one ",
    "write a ",
    "draft one linkedin",
    "draft one substack",
    "draft one post",
    "write one ",
]


def _match_signals(intent_lower: str, signals: List[str]) -> List[str]:
    """Return list of signal phrases that match."""
    return [s for s in signals if s in intent_lower]


def _freeform_default(intent: str, reason: str) -> MissionPackage:
    """Fallback package when no outcome class matches."""
    return MissionPackage(
        outcome_class="freeform",
        primary_workflow="big-project",
        sub_workflows=[],
        experts=[],
        skills_to_load=[],
        plugins=[],
        cost_tier="free",
        fanout_pattern="sequential",
        gates_to_surface=["G1"],  # intent sharpening likely needed
        confidence=0.2,
        reasoning=reason,
        matched_signals=[],
    )


def resolve(intent: str) -> MissionPackage:
    """Map fuzzy intent → assembled mission package.

    Wave 4 only populates Research outcome class. Other classes return
    freeform_default for now; Wave 5 fills them in.
    """
    if not intent or not intent.strip():
        return _freeform_default(intent, "Empty intent — sharpen via G1 before proceeding.")

    intent_lower = intent.strip().lower()

    # ── Class 3: Research / Intelligence (Wave 4 populated) ──
    research_hits = _match_signals(intent_lower, RESEARCH_SIGNALS)
    if research_hits:
        return MissionPackage(
            outcome_class="research",
            primary_workflow="research-swarm",
            sub_workflows=["deep-research", "spy-market", "competitor-intel"],
            experts=["researcher"],  # generic researcher archetype + domain experts loaded by workflow
            skills_to_load=[
                "research-landscape",
                "spy-market",
                "competitor-intel",
                "knowledge-search",
            ],
            plugins=["episodic-memory"],  # capture findings for future recall
            cost_tier="cheap",  # Perplexity ~$0.03/call typical
            fanout_pattern="parallel",
            gates_to_surface=["G2"],  # only if research spend exceeds threshold
            confidence=0.9,
            reasoning=(
                "Research signal matched. /research-swarm is the parallel-research "
                "orchestrator (3-5 angles fan out via parallel_swarm.py). Gemini Deep "
                "Research is the primary research tool per directives/research-protocol.md; "
                "Perplexity is fallback."
            ),
            matched_signals=research_hits,
        )

    # ── Classes 1, 2, 4, 5, 6: stub until Wave 5 ──
    refinement_hits = _match_signals(intent_lower, REFINEMENT_SIGNALS)
    if refinement_hits:
        return _freeform_default(
            intent,
            f"Refinement signals matched ({refinement_hits[:2]}) — Wave 5 will populate "
            "this outcome class with /writers-room. For now: invoke /writers-room directly.",
        )

    multi_hits = _match_signals(intent_lower, MULTI_DELIVERABLE_SIGNALS)
    if multi_hits:
        return _freeform_default(
            intent,
            f"Multi-deliverable signals matched ({multi_hits[:2]}) — Wave 5 will populate "
            "this outcome class with /supercomputer (gates suppressed). For now: invoke "
            "/supercomputer directly and live with its Phase 1 'Proceed?' gate.",
        )

    atom_hits = _match_signals(intent_lower, ATOMIZATION_SIGNALS)
    if atom_hits:
        return _freeform_default(
            intent,
            f"Atomization signals matched ({atom_hits[:2]}) — Wave 5 will populate with "
            "/atomize. For now: invoke /atomize directly.",
        )

    sys_hits = _match_signals(intent_lower, SYSTEM_MAINTENANCE_SIGNALS)
    if sys_hits:
        return _freeform_default(
            intent,
            f"System maintenance signals matched ({sys_hits[:2]}) — Wave 5 will populate. "
            "For now: invoke /system-audit, /maintenance, or knowledge_compiler directly.",
        )

    single_hits = _match_signals(intent_lower, SINGLE_DELIVERABLE_SIGNALS)
    if single_hits:
        return _freeform_default(
            intent,
            f"Single-deliverable signals matched ({single_hits[:2]}) — Wave 5 will populate. "
            "For now: invoke the appropriate production workflow per routing_enforcer.BINDINGS.",
        )

    # No match — freeform fallback
    return _freeform_default(
        intent,
        "No outcome-class signals matched. Falling back to /big-project scaffold. "
        "Consider sharpening intent (G1) or invoking a specific workflow.",
    )


# ─── CLI ────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Intent → Mission Package resolver")
    sub = parser.add_subparsers(dest="cmd")

    res = sub.add_parser("resolve", help="Resolve an intent string into a mission package")
    res.add_argument("--intent", required=True)
    res.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if args.cmd == "resolve":
        package = resolve(args.intent)
        if args.json:
            print(json.dumps(asdict(package), indent=2))
        else:
            print(f"\nOutcome class:     {package.outcome_class}")
            print(f"Primary workflow:  /{package.primary_workflow}")
            if package.sub_workflows:
                print(f"Sub-workflows:     {', '.join('/' + w for w in package.sub_workflows)}")
            print(f"Experts:           {package.experts or '(none specified)'}")
            print(f"Skills to load:    {package.skills_to_load or '(none)'}")
            print(f"Plugins:           {package.plugins or '(none)'}")
            print(f"Cost tier:         {package.cost_tier}")
            print(f"Fan-out pattern:   {package.fanout_pattern}")
            print(f"Gates to surface:  {package.gates_to_surface or '(none)'}")
            print(f"Confidence:        {package.confidence}")
            if package.matched_signals:
                print(f"Matched signals:   {package.matched_signals}")
            print(f"\nReasoning: {package.reasoning}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
