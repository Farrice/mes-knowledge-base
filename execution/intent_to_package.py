#!/usr/bin/env python3
"""
Intent → Mission Package resolver (Autopilot Wave 5 / 2026-05-21).

Pure-Python prescriptive routing. Same signal-phrase pattern as
`routing_enforcer.BINDINGS` (which is RESTRICTIVE — "you may not use X"),
but this module is PRESCRIPTIVE: "for this intent, here is the assembled
mission package" — workflow + skills + experts + plugins + cost tier +
fan-out pattern + gates to surface.

Why it exists: 232 skills + 886 workflows + 24 experts is too much surface
area to mentally compose for every session. This is the cognitive-
compression layer — fuzzy intent in, full package out.

Seven outcome classes (full taxonomy):

    1. Single Deliverable Production — "draft a LinkedIn post", "write me one X"
    2. Multi-Deliverable Mission     — "build me a brand for X", "campaign for Y"
    3. Research / Intelligence       — "research X", "competitive intel on Y"
    4. Creative Atomization          — "atomize this", "remix into N formats"
    5. System / Maintenance          — "audit the system", "evolve skill X"
    6. Refinement / Diagnosis        — "polish this draft", "writers room on this"
    7. Freeform / Unclassified       — fall-through to /big-project

Resolution order (specificity descending — first match wins):
    refinement → research → atomization → maintenance → multi-deliverable
    → single-deliverable subroute (parallax/linkedin/seo/brand/design)
    → freeform fallback

CLI:
    python3 execution/intent_to_package.py resolve --intent "<text>" --json
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field, asdict
from typing import List, Optional


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
    # Wave 5: extra hints for /autopilot Phase 2 execution
    fanout_workers_estimate: int = 1           # how many parallel Agent calls
    halt_suppressions: List[str] = field(default_factory=list)  # which gates we suppress


# ═══════════════════════════════════════════════════════════════
# SIGNAL PHRASES — outcome-class trigger lexicons.
# Order: refinement first (most specific), then narrower → wider.
# Update directives/autopilot-mode.md when adding new signal phrases.
# ═══════════════════════════════════════════════════════════════

# Class 6: Refinement (checked FIRST — most specific)
REFINEMENT_SIGNALS = [
    "polish this", "polish the",
    "writers room on", "writers' room on", "writer's room on",
    "refine this", "refine the",
    "diagnose this", "diagnose why",
    "review and fix", "fix this draft", "improve this draft",
    "tighten this", "tighten the",
    "rewrite this", "rewrite the",
    "what's wrong with this", "whats wrong with this",
]

# Class 3: Research
RESEARCH_SIGNALS = [
    "research the", "research on", "deep research",
    "competitive intel", "competitive intelligence",
    "what's the landscape", "landscape for", "market landscape",
    "investigate ", "study the",
    "what does the market", "comparative analysis", "literature review",
    "intelligence brief", "deep dive on", "deep dive into",
    "scan the field", "what are the best",
]

# Class 4: Atomization
ATOMIZATION_SIGNALS = [
    "atomize ", "atomize this",
    "remix this into", "remix into",
    "platform-adapt", "platform adapt",
    "make derivatives from", "derivatives of this",
    "11 derivatives",
    "spin this into", "spin into",
    "adapt for instagram", "adapt for linkedin", "adapt for substack",
    "multi-format", "across platforms",
]

# Class 5: System / Maintenance
SYSTEM_MAINTENANCE_SIGNALS = [
    "audit the system", "system audit", "system pulse", "system health",
    "evolve skill", "skill evolution",
    "knowledge compiler", "knowledge-compiler",
    "sync instructions", "sync registries",
    "maintenance pass", "system hygiene",
    "compile knowledge", "rebuild index",
    "system status", "evolution status",
]

# Class 2: Multi-Deliverable Mission (mirrors supercomputer-mode triggers)
MULTI_DELIVERABLE_SIGNALS = [
    "build me a brand for", "build a brand for",
    "make me a campaign for", "make a campaign for",
    "full content drop on", "full marketing for",
    "launch ",  # leading space avoids matching "launching"
    "hero shot and", "and listing visuals",
    "campaign for ",
    "full marketing", "complete brand system",
    "across all platforms",
    "ugc ad for",  # supercomputer trigger
]

# Class 1 subroutes (single-deliverable production)
# Order: most-specific routing signals first per routing_enforcer.BINDINGS

PARALLAX_SIGNALS = [
    "parallax edition", "parallax substack", "next substack",
    "parallax prompt pack", "parallax post", "parallax draft",
    "next parallax", "substack edition",
]

LINKEDIN_PRODUCTION_SIGNALS = [
    "linkedin post from scratch", "write a linkedin post",
    "draft a linkedin post", "draft one linkedin",
    "new linkedin post", "linkedin content from scratch",
    "linkedin post production", "linkedin headline",
]

BRAND_OS_SIGNALS = [
    "brand operating system", "brand os ", " bos ",
    "build a bos", "build a complete brand system",
    "full brand system for", "resonance-style package",
]

DESIGN_MD_SIGNALS = [
    "design.md", "make it look like",
    "synthesize design", "extract design",
    "brand library entry", "design system spec",
]

SEO_SIGNALS = [
    "seo strategy", "seo audit", "seo content",
    "search gap analysis", "keyword research",
]

VSL_SIGNALS = [
    "vsl ", "video sales letter",
    "build a vsl", "write a vsl",
]

GENERIC_SINGLE_DELIVERABLE_SIGNALS = [
    "write me one", "draft a ", "draft one ", "write a ",
    "write one ", "make one ", "create one ",
    "give me a ", "produce a ",
]


# ═══════════════════════════════════════════════════════════════
# RESOLVERS — one function per class
# ═══════════════════════════════════════════════════════════════

def _match_signals(intent_lower: str, signals: List[str]) -> List[str]:
    return [s for s in signals if s in intent_lower]


def _resolve_refinement(intent_lower: str) -> Optional[MissionPackage]:
    hits = _match_signals(intent_lower, REFINEMENT_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="refinement",
        primary_workflow="writers-room",
        sub_workflows=["adversarial-review", "prose-check", "anti-slop-audit"],
        experts=[
            "lara-acosta", "luke-iha", "nicolas-cole", "wright-thompson",
            "ocean-vuong", "kallaway", "dai-media", "oren-john", "grace-andrews",
        ],
        skills_to_load=[
            "writers-room", "adversarial-review", "prose-check",
            "anti-slop-audit", "word-audit", "anti-homogenization-audit",
        ],
        plugins=["hookify", "episodic-memory"],
        cost_tier="free",
        fanout_pattern="parallel",
        fanout_workers_estimate=5,   # 5 of 9 expert lenses typical
        gates_to_surface=["G3"],     # taste call on final prose
        halt_suppressions=[
            "writers-room phase-boundary halts (the 3 craft layers run internally)",
        ],
        confidence=0.95,
        reasoning=(
            "Refinement is the cleanest parallel fan-out case in the system — "
            "9 expert lenses, all independent. /writers-room is the bound "
            "diagnostic-on-draft workflow per routing_enforcer.BINDINGS."
        ),
        matched_signals=hits,
    )


def _resolve_research(intent_lower: str) -> Optional[MissionPackage]:
    hits = _match_signals(intent_lower, RESEARCH_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="research",
        primary_workflow="research-swarm",
        sub_workflows=["deep-research", "spy-market", "competitor-intel"],
        experts=["researcher"],
        skills_to_load=[
            "research-landscape", "spy-market", "competitor-intel",
            "knowledge-search", "deep-research",
        ],
        plugins=["episodic-memory"],
        cost_tier="cheap",
        fanout_pattern="parallel",
        fanout_workers_estimate=4,
        gates_to_surface=["G2"],
        halt_suppressions=[],
        confidence=0.9,
        reasoning=(
            "Research signal matched. /research-swarm orchestrates parallel "
            "research via parallel_swarm.py (3-5 angles fan out). Gemini Deep "
            "Research is primary per directives/research-protocol.md; "
            "Perplexity is fallback."
        ),
        matched_signals=hits,
    )


def _resolve_atomization(intent_lower: str) -> Optional[MissionPackage]:
    hits = _match_signals(intent_lower, ATOMIZATION_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="atomization",
        primary_workflow="atomize",
        sub_workflows=["multi-format-deploy", "platform-adapt", "content-bundle"],
        experts=["lara-acosta", "diandra", "caleb", "kallaway"],  # platform-native experts
        skills_to_load=[
            "atomize", "multi-format-deploy", "platform-adapt",
            "content-bundle", "insight-vectors",
        ],
        plugins=["episodic-memory"],
        cost_tier="free",
        fanout_pattern="parallel",
        fanout_workers_estimate=6,  # typical: 11 derivative formats, parallel-able in chunks
        gates_to_surface=["G3"],
        halt_suppressions=[],
        confidence=0.9,
        reasoning=(
            "Atomization signal matched. /atomize produces N derivatives from "
            "one source; each derivative is independent → maximal parallel "
            "fan-out. Each platform-native expert handles their format."
        ),
        matched_signals=hits,
    )


def _resolve_maintenance(intent_lower: str) -> Optional[MissionPackage]:
    hits = _match_signals(intent_lower, SYSTEM_MAINTENANCE_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="maintenance",
        primary_workflow="system-audit",
        sub_workflows=["maintenance", "system-pulse", "evolution-status"],
        experts=[],  # deterministic Python, no expert needed
        skills_to_load=["system-audit", "system-pulse", "maintenance"],
        plugins=["hookify"],
        cost_tier="free",
        fanout_pattern="sequential",  # scripts depend on order
        fanout_workers_estimate=1,
        gates_to_surface=[],  # no taste judgment in deterministic ops
        halt_suppressions=[],
        confidence=0.95,
        reasoning=(
            "System maintenance — deterministic Python scripts run in a fixed "
            "order. No parallel benefit, no taste gate needed. Use "
            "knowledge_compiler / evolution_orchestrator / skill_auditor."
        ),
        matched_signals=hits,
    )


def _resolve_multi_deliverable(intent_lower: str) -> Optional[MissionPackage]:
    hits = _match_signals(intent_lower, MULTI_DELIVERABLE_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="multi_deliverable",
        primary_workflow="supercomputer",
        sub_workflows=[
            "build-bos", "voice-document", "icp-build",
            "parallax", "ghostwrite",
        ],
        experts=["oren-john", "lara-acosta", "luke-iha", "grace-andrews"],
        skills_to_load=[
            "supercomputer", "build-bos", "voice-document",
            "icp-build", "parallax", "ghostwrite",
        ],
        plugins=["hookify", "episodic-memory", "watch"],
        cost_tier="medium",
        fanout_pattern="parallel",
        fanout_workers_estimate=4,  # supercomputer phases run independent deliverables
        gates_to_surface=["G2"],  # paid cost likely > $5
        halt_suppressions=[
            "supercomputer Phase 1 'Proceed?' aggregate cost gate (replaced by autopilot G2)",
            "supercomputer per-step paid confirmations within G2-approved budget",
        ],
        confidence=0.92,
        reasoning=(
            "Multi-deliverable mission. Autopilot wraps /supercomputer with "
            "halts suppressed — Phase 1 aggregate gate replaced by autopilot "
            "G2; per-step gates auto-fire under threshold. Independent "
            "deliverables (hero shot + listing visuals + ad concepts) fan out "
            "via parallel Agent calls; sequential dependency chains "
            "(brand-brief → hero shot) stay sequential per anchor_memory graph."
        ),
        matched_signals=hits,
    )


def _resolve_single_deliverable(intent_lower: str) -> Optional[MissionPackage]:
    """Class 1 has multiple subroutes. Most-specific binding wins."""
    # Parallax editions
    hits = _match_signals(intent_lower, PARALLAX_SIGNALS)
    if hits:
        return MissionPackage(
            outcome_class="single_deliverable",
            primary_workflow="parallax",
            sub_workflows=[],
            experts=["nicolas-cole", "wright-thompson", "kallaway"],
            skills_to_load=["parallax", "voice-document", "voice-niche"],
            plugins=["hookify", "watch"],
            cost_tier="cheap",  # Perplexity verification in Phase 2.5
            fanout_pattern="sequential",  # parallax phases are dependent
            fanout_workers_estimate=1,
            gates_to_surface=["G3"],
            halt_suppressions=[
                "parallax topic selection halt (--topic inferred from intent or anchor memory)",
                "parallax raw-take halt (sourced from session context if available)",
                "parallax post-audit approval gate (replaced by G3 prose check)",
            ],
            confidence=0.95,
            reasoning=(
                "Parallax edition signal. The Phase 2.5 grounding gate STAYS "
                "(load-bearing — Edition 02 shipped 7 fabrications when "
                "skipped). Other halts suppressed."
            ),
            matched_signals=hits,
        )

    # LinkedIn from scratch
    hits = _match_signals(intent_lower, LINKEDIN_PRODUCTION_SIGNALS)
    if hits:
        return MissionPackage(
            outcome_class="single_deliverable",
            primary_workflow="ghostwrite",
            sub_workflows=["high-dwell"],
            experts=["lara-acosta"],
            skills_to_load=[
                "lara-acosta-linkedin-ghostwriting",
                "ghostwrite", "high-dwell", "hook-forge",
            ],
            plugins=["hookify"],
            cost_tier="free",
            fanout_pattern="sequential",
            fanout_workers_estimate=1,
            gates_to_surface=["G3"],
            halt_suppressions=[],
            confidence=0.95,
            reasoning=(
                "LinkedIn from scratch. /ghostwrite + Lara Acosta skill is the "
                "bound production workflow. Wave 1+2 caps especially relevant "
                "here — LinkedIn content is content-type most prone to AI-prose "
                "drift."
            ),
            matched_signals=hits,
        )

    # Brand OS
    hits = _match_signals(intent_lower, BRAND_OS_SIGNALS)
    if hits:
        return MissionPackage(
            outcome_class="single_deliverable",
            primary_workflow="build-bos",
            sub_workflows=["voice-document", "icp-build", "brand-dna-extraction"],
            experts=["oren-john", "grace-andrews", "lulu"],
            skills_to_load=[
                "brand-operating-system", "build-bos", "voice-document",
                "icp-build", "brand-dna-extraction",
            ],
            plugins=["hookify", "episodic-memory"],
            cost_tier="cheap",
            fanout_pattern="sequential",  # BOS phases are dependent
            fanout_workers_estimate=2,
            gates_to_surface=["G3"],
            halt_suppressions=[],
            confidence=0.9,
            reasoning=(
                "Brand OS signal. /build-bos is a system-tier skill with "
                "internal phase structure — 6-layer brand build orchestrated "
                "via skills/brand-operating-system/. Autopilot calls it with "
                "phase-boundary halts that ARE load-bearing intact."
            ),
            matched_signals=hits,
        )

    # DESIGN.md
    hits = _match_signals(intent_lower, DESIGN_MD_SIGNALS)
    if hits:
        return MissionPackage(
            outcome_class="single_deliverable",
            primary_workflow="design-md-synthesize",
            sub_workflows=["brand-library", "design-md-extract", "design-md-validate"],
            experts=["creative-director", "oren-john"],
            skills_to_load=["design-md", "creative-direction"],
            plugins=["hookify"],
            cost_tier="free",
            fanout_pattern="sequential",
            fanout_workers_estimate=1,
            gates_to_surface=["G3"],
            halt_suppressions=[],
            confidence=0.9,
            reasoning=(
                "DESIGN.md signal. Routed to skills/design-md/ workflows. "
                "Always lint via `npx @google/design.md lint` per CLAUDE.md."
            ),
            matched_signals=hits,
        )

    # SEO
    hits = _match_signals(intent_lower, SEO_SIGNALS)
    if hits:
        return MissionPackage(
            outcome_class="single_deliverable",
            primary_workflow="spy-market",
            sub_workflows=["seo-strategy"],
            experts=["nathan-gotch"],
            skills_to_load=["spy-market", "seo-strategy"],
            plugins=[],
            cost_tier="cheap",
            fanout_pattern="sequential",
            fanout_workers_estimate=1,
            gates_to_surface=[],
            halt_suppressions=[],
            confidence=0.85,
            reasoning="SEO signal. Nathan Gotch is the bound expert per DOMAIN_REGISTRY.",
            matched_signals=hits,
        )

    # VSL / video sales letter
    hits = _match_signals(intent_lower, VSL_SIGNALS)
    if hits:
        return MissionPackage(
            outcome_class="single_deliverable",
            primary_workflow="nuclear-vsl",
            sub_workflows=["vsl-lead", "vsl-atomize"],
            experts=["luke-iha"],
            skills_to_load=["nuclear-vsl", "vsl-lead", "luke-iha-cross-domain"],
            plugins=[],
            cost_tier="free",
            fanout_pattern="sequential",
            fanout_workers_estimate=1,
            gates_to_surface=["G3"],
            halt_suppressions=[],
            confidence=0.9,
            reasoning="VSL signal. Luke Iha is the bound expert; nuclear-vsl is the production-grade workflow.",
            matched_signals=hits,
        )

    # Generic single-deliverable (no subroute matched, but explicit production signal)
    hits = _match_signals(intent_lower, GENERIC_SINGLE_DELIVERABLE_SIGNALS)
    if hits:
        return MissionPackage(
            outcome_class="single_deliverable",
            primary_workflow="solo",  # JCC solo mission — generic single-expert delivery
            sub_workflows=[],
            experts=[],  # deferred to runtime intent analysis
            skills_to_load=[],
            plugins=["hookify"],
            cost_tier="free",
            fanout_pattern="sequential",
            fanout_workers_estimate=1,
            gates_to_surface=["G3"],
            halt_suppressions=[],
            confidence=0.5,
            reasoning=(
                "Generic single-deliverable signal but no subroute matched. "
                "Falls to /solo (JCC solo mission). Expert/skill routing "
                "deferred to runtime — autopilot should re-resolve at "
                "Phase 2 with more context, or surface G1 for sharpening."
            ),
            matched_signals=hits,
        )

    return None


def _freeform_default(reason: str) -> MissionPackage:
    return MissionPackage(
        outcome_class="freeform",
        primary_workflow="big-project",
        sub_workflows=[],
        experts=[],
        skills_to_load=["big-project"],
        plugins=[],
        cost_tier="free",
        fanout_pattern="sequential",
        fanout_workers_estimate=1,
        gates_to_surface=["G1"],  # likely needs sharpening
        halt_suppressions=[],
        confidence=0.2,
        reasoning=reason,
        matched_signals=[],
    )


# ═══════════════════════════════════════════════════════════════
# PUBLIC: resolve()
# ═══════════════════════════════════════════════════════════════

# Resolution chain — first match wins. Order = specificity descending.
_RESOLVERS = [
    _resolve_refinement,         # Class 6
    _resolve_research,           # Class 3
    _resolve_atomization,        # Class 4
    _resolve_maintenance,        # Class 5
    _resolve_multi_deliverable,  # Class 2
    _resolve_single_deliverable, # Class 1 (multi-subroute)
]


def resolve(intent: str) -> MissionPackage:
    """Map fuzzy intent → assembled mission package.

    Walks the resolver chain in specificity order. First match wins.
    Falls back to freeform if no class matches.
    """
    if not intent or not intent.strip():
        return _freeform_default(
            "Empty intent — sharpen via G1 before proceeding."
        )

    intent_lower = intent.strip().lower()

    for resolver in _RESOLVERS:
        package = resolver(intent_lower)
        if package is not None:
            return package

    return _freeform_default(
        "No outcome-class signals matched. Falling back to /big-project "
        "scaffold. Consider sharpening intent (G1) or invoking a specific "
        "workflow directly."
    )


# ─── CLI ────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Intent → Mission Package resolver")
    sub = parser.add_subparsers(dest="cmd")

    res = sub.add_parser("resolve", help="Resolve an intent into a mission package")
    res.add_argument("--intent", required=True)
    res.add_argument("--json", action="store_true")

    sub.add_parser("classes", help="List all outcome classes + their signal lexicons")

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
            print(f"Experts:           {package.experts or '(none)'}")
            print(f"Skills to load:    {package.skills_to_load or '(none)'}")
            print(f"Plugins:           {package.plugins or '(none)'}")
            print(f"Cost tier:         {package.cost_tier}")
            print(f"Fan-out pattern:   {package.fanout_pattern} (~{package.fanout_workers_estimate} workers)")
            print(f"Gates to surface:  {package.gates_to_surface or '(none)'}")
            if package.halt_suppressions:
                print(f"Halts suppressed:")
                for h in package.halt_suppressions:
                    print(f"  - {h}")
            print(f"Confidence:        {package.confidence}")
            if package.matched_signals:
                print(f"Matched signals:   {package.matched_signals}")
            print(f"\nReasoning: {package.reasoning}")
    elif args.cmd == "classes":
        print(json.dumps({
            "1_single_deliverable": {
                "parallax": PARALLAX_SIGNALS,
                "linkedin": LINKEDIN_PRODUCTION_SIGNALS,
                "brand_os": BRAND_OS_SIGNALS,
                "design_md": DESIGN_MD_SIGNALS,
                "seo": SEO_SIGNALS,
                "vsl": VSL_SIGNALS,
                "generic": GENERIC_SINGLE_DELIVERABLE_SIGNALS,
            },
            "2_multi_deliverable": MULTI_DELIVERABLE_SIGNALS,
            "3_research": RESEARCH_SIGNALS,
            "4_atomization": ATOMIZATION_SIGNALS,
            "5_maintenance": SYSTEM_MAINTENANCE_SIGNALS,
            "6_refinement": REFINEMENT_SIGNALS,
            "7_freeform": "(fallback when no other class matches)",
        }, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
