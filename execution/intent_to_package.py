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

Nine outcome classes (full taxonomy):

    1. Single Deliverable Production — "draft a LinkedIn post", "write me one X"
    2. Multi-Deliverable Mission     — "build me a brand for X", "campaign for Y"
    3. Research / Intelligence       — "research X", "competitive intel on Y"
    4. Creative Atomization          — "atomize this", "remix into N formats"
    5. System / Maintenance          — "audit the system", "evolve skill X"
    6. Refinement / Diagnosis        — "polish this draft", "writers room on this"
    7. Freeform / Unclassified       — fall-through to /big-project
    8. Conversation / Reflection     — "what do you think", "your take on" (Phase A)
    9. Exploration                   — "let's explore", "help me figure out" (Phase A)

Resolution order (specificity descending — first match wins):
    refinement → research → atomization → maintenance → multi-deliverable
    → conversation → exploration → single-deliverable subroute (parallax/
    linkedin/seo/brand/design) → freeform fallback

Classes 8 + 9 (Phase A / 2026-05-25): The "universal front door" — autopilot
now handles reflective and exploratory intents without punting to freeform.
Both skip G1 (reflective questions are sharp by being exploratory; forcing
DICE sharpening on them ruins the dialogue) and skip chain_runner.finalize
(no deliverable → nothing to score). Ledger still emits so calls get
tracked for ledger-learning (Phase B).

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
    "not firing", "isn't firing", "workflow not firing", "workflows not firing",
    "codex feels", "harness", "routing layer", "orchestration layer",
    "hook parity", "hook layer", "context load", "skill loading",
    "claude code", "codex parity", "global orchestration",
]

REPEATABILITY_SPINE_SIGNALS = [
    "lost the magic", "cannot repeat", "can't repeat", "repeatability",
    "revision got worse", "got worse", "regression", "regressed",
    "preserve the good", "preservation lock", "route picked the wrong",
]

KNOWLEDGE_LIBRARIAN_SIGNALS = [
    "knowledge pulse", "library pulse", "knowledge-librarian",
    "session start pulse", "prior decisions", "reusable solution",
    "reusable solutions", "underused workflow", "underused workflows",
    "sleeping giants",
]

SOURCE_TO_SKILL_SYSTEM_SIGNALS = [
    "source-to-skill-system", "source to skill system",
    "source-to-system", "source to system", "source-to-skill",
    "source to skill", "turn this source", "source material into",
    "connected skill system", "workflow bridge", "reusable command surface",
    "build out all the workflows", "harvest all the genius",
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

# Class 11: Long-Running Project (Phase D — agent_tick, 2026-05-25)
# Matches multi-day / background / scheduled-advance intents. Distinct from
# multi_deliverable (which produces N artifacts in one session). Long-
# running means: this work spans days, agent_tick wakes on schedule and
# advances by one phase per tick.
LONG_RUNNING_SIGNALS = [
    # Explicit multi-day framing
    "over the next week", "over the next few days", "over the next month",
    "for the next week", "for the next month",
    "multi-day", "multi day",
    "across multiple sessions", "spread across days",
    # Background-work framing
    "while i sleep", "while i'm away",
    "in the background", "as a background project",
    "keep advancing on", "keep moving forward on",
    "keep working on", "in the background while",
    # Scheduled / tick framing
    "agent tick", "daily tick",
    "wake up tomorrow and", "tomorrow morning continue",
    "schedule a daily", "schedule daily progress",
    "autonomous tick", "autonomous mode",
]


# Class 10: Vertical Bootstrap (Phase C — /verticalize, 2026-05-25)
# Strong, specific patterns. Fires BEFORE multi_deliverable because both
# could match "build me a brand" — but /verticalize is the right call when
# the user is bootstrapping a NEW domain from scratch (no existing voice
# doc, no ICP yet, no expert routing). Multi_deliverable assumes the
# vertical exists.
VERTICAL_BOOTSTRAP_SIGNALS = [
    # Explicit signals
    "verticalize", "bootstrap a vertical", "bootstrap a new vertical",
    "bootstrap a domain", "new vertical for",
    # Entering a new domain
    "i'm entering", "i am entering",
    "entering the ", "new niche of ",
    "set up a new niche", "set up a vertical",
    "stand up a new vertical", "stand up a domain",
    # Zero-state bootstrap framing
    "from zero in ", "from scratch in the ",
    "no audience yet for ", "no voice doc yet",
    # Calibration-bootstrap framing
    "calibrate for ", "build the stack for ",
    "spin up calibration for",
]


# Class 8: Conversation / Reflection (Phase A — universal autopilot front door)
# Strict patterns — explicit opinion solicitation or judgment requests.
# Deliberately tight so mission intents ("write me a X") catch first.
CONVERSATION_SIGNALS = [
    # Direct opinion solicitation
    "what do you think", "what's your opinion", "what's your read",
    "in your opinion", "your honest take", "your take on",
    "your thoughts on", "your thoughts about",
    "what's your honest", "your honest opinion",
    # Decision help / judgment requests
    "if you had to pick", "if forced to choose", "if you were me",
    "what would you do", "how would you ",
    "help me think through", "help me decide",
    "help me weigh ", "weigh in on",
    # Recommendation requests (judgment-flavored)
    "what do you recommend", "would you recommend",
    "which is better between", "which would you pick",
    # Meta / reflective on the work itself
    "in your view", "from your perspective",
    "tell me your read",
]

# Class 9: Exploration (Phase A — open-ended landscape mapping)
# Distinct from research signals — exploration is dialogic, not deliverable-shaped.
EXPLORATION_SIGNALS = [
    "let's explore", "let me explore", "let's think about",
    "help me figure out", "help me understand",
    "i don't know yet but", "i'm not sure where to start",
    "walk me through your view", "walk me through how you think",
    "i'm curious about", "i'm wondering about",
    "where do i start with", "where would you begin",
    "lay of the land", "give me a lay of",
    "talk me through", "think out loud about",
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
        # Wave 5 v1 constraint (per .agent/workflows/autopilot.md and Cognition's
        # "Don't Build Multi-Agents"): atomization is a WRITE phase. Parallel
        # writers diverge in voice across the N derivatives (the bird-hat /
        # bird-body failure mode). Each derivative writes sequentially against
        # the single anchored source-of-truth. fanout_workers_estimate is kept
        # as a batch-sizing hint, NOT a parallel-worker count. (Bug #4 fix,
        # 2026-05-23 — Wave 5 validation surfaced the resolver/workflow contradiction.)
        fanout_pattern="sequential",
        fanout_workers_estimate=6,  # batch-size hint; sequential execution
        gates_to_surface=["G3"],
        halt_suppressions=[],
        confidence=0.9,
        reasoning=(
            "Atomization signal matched. /atomize produces N derivatives from "
            "one source. Each derivative writes SEQUENTIALLY against the single "
            "anchored source-of-truth to prevent voice drift across formats "
            "(Cognition's bird-hat failure mode). Platform-native experts pick "
            "the appropriate skill per format in order."
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


def _resolve_repeatability_spine(intent_lower: str) -> Optional[MissionPackage]:
    hits = _match_signals(intent_lower, REPEATABILITY_SPINE_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="repeatability_repair",
        primary_workflow="repeatability-spine",
        sub_workflows=["system-audit"],
        experts=["repeatability-spine"],
        skills_to_load=["repeatability-spine"],
        plugins=[],
        cost_tier="free",
        fanout_pattern="sequential",
        fanout_workers_estimate=1,
        gates_to_surface=[],
        halt_suppressions=[],
        confidence=0.9,
        reasoning=(
            "Repeatability regression signal matched. Preserve the good example "
            "first, classify one failure mode, then repair through /repeatability-spine."
        ),
        matched_signals=hits,
    )


def _resolve_knowledge_librarian(intent_lower: str) -> Optional[MissionPackage]:
    hits = _match_signals(intent_lower, KNOWLEDGE_LIBRARIAN_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="knowledge_librarian",
        primary_workflow="knowledge-librarian",
        sub_workflows=[],
        experts=["knowledge-librarian"],
        skills_to_load=["knowledge-librarian"],
        plugins=[],
        cost_tier="free",
        fanout_pattern="sequential",
        fanout_workers_estimate=1,
        gates_to_surface=[],
        halt_suppressions=[],
        confidence=0.88,
        reasoning=(
            "Knowledge/library pulse signal matched. Use /knowledge-librarian "
            "for prior decisions, reusable solutions, and sleeping assets."
        ),
        matched_signals=hits,
    )


def _resolve_source_to_skill_system(intent_lower: str) -> Optional[MissionPackage]:
    hits = _match_signals(intent_lower, SOURCE_TO_SKILL_SYSTEM_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="source_to_system",
        primary_workflow="source-to-skill-system",
        sub_workflows=["system-audit"],
        experts=["source-to-skill-system"],
        skills_to_load=["source-to-skill-system"],
        plugins=[],
        cost_tier="free",
        fanout_pattern="sequential",
        fanout_workers_estimate=1,
        gates_to_surface=[],
        halt_suppressions=[],
        confidence=0.9,
        reasoning=(
            "Source-to-capability signal matched. Build a connected skill system "
            "or workflow bridge after evidence and existing-route checks."
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


def _resolve_long_running_project(intent_lower: str) -> Optional[MissionPackage]:
    """Class 11 — Long-running project (Phase D, 2026-05-25).

    Multi-day work that advances autonomously via agent_tick. The user
    states the brief once; agent_tick wakes on schedule, loads state.yaml +
    sovereign memory + anchors, advances exactly ONE phase per tick, and
    writes a wake-report.

    NON-NEGOTIABLE behaviors (per directives/agent-tick-protocol.md):
    - One phase per tick. Never auto-execute multiple phases.
    - Block-on-ambiguity: if next phase needs taste call, halt to
      blocked.jsonl. Wait for user.
    - Explicit opt-in required: a project does NOT get a launchd tick
      unless the user runs `agent_tick.py enable --project <slug>`.
    """
    hits = _match_signals(intent_lower, LONG_RUNNING_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="long_running_project",
        primary_workflow="agent-tick",
        sub_workflows=[],  # agent_tick chooses sub-workflows per-tick from state.yaml
        experts=[],         # determined per-tick
        skills_to_load=["agent-tick"],
        plugins=["episodic-memory"],
        cost_tier="standard",  # per-project daily cap enforced by cost_gate extension
        fanout_pattern="sequential",  # one phase per tick, hard rule
        fanout_workers_estimate=1,
        gates_to_surface=["G2"],  # paid-API costs accumulate over days
        halt_suppressions=[],     # safety gates STAY — no blanket suppression for autonomous mode
        confidence=0.88,
        reasoning=(
            "Long-running / multi-day project. Routes to agent_tick wake "
            "handler which loads project state.yaml, advances ONE phase per "
            "tick, and writes a wake-report. Hard rules: one phase per tick "
            "(no compounding); block-on-ambiguity (no improvising past "
            "taste calls); explicit opt-in only (no surprise background "
            "work). Per-project daily cost cap enforced via cost_gate."
        ),
        matched_signals=hits,
    )


def _resolve_vertical_bootstrap(intent_lower: str) -> Optional[MissionPackage]:
    """Class 10 — Vertical bootstrap (Phase C, 2026-05-25).

    Fires when the user is bootstrapping a NEW domain from scratch — no
    voice doc, no ICP, no expert routing exists yet. /verticalize composes
    existing atoms (icp-deep-dive, voice-document, extract, ground_truth
    init-domain, per-project CLAUDE.md generation) into one orchestrated
    pass. Today this takes 1-2 weeks bespoke per vertical; verticalize
    cuts it to 1-2 hours.

    Phase 2.5 gate (ICP + voice user-validation) is NON-skippable —
    without it, the new vertical's ground truth calibrates to auto-seed
    and grade inflation enters from day one (per 2026-05-03 lesson).
    """
    hits = _match_signals(intent_lower, VERTICAL_BOOTSTRAP_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="vertical_bootstrap",
        primary_workflow="verticalize",
        sub_workflows=[
            "icp-deep-dive", "voice-document", "extract",
            "research-landscape",
        ],
        experts=["mcraney", "lulu", "oren-john", "lara-acosta"],
        skills_to_load=[
            "verticalize", "icp-deep-dive", "voice-document",
            "extract", "research-landscape",
        ],
        plugins=["hookify", "episodic-memory"],
        cost_tier="standard",  # Perplexity for landscape research + Gemini for extraction
        fanout_pattern="sequential",  # phases have hard dependencies (ICP → voice → ground-truth)
        fanout_workers_estimate=1,
        gates_to_surface=["G2", "G3"],  # paid research + ICP/voice user-validation gate
        halt_suppressions=[],  # Phase 2.5 user-validation gate STAYS (load-bearing)
        confidence=0.92,
        reasoning=(
            "Vertical bootstrap signal. /verticalize is a system-tier "
            "conductor that orchestrates ICP + voice + ground-truth + "
            "routing + per-project CLAUDE.md generation for a NEW domain. "
            "Phase 2.5 user-validation gate is non-skippable: without it, "
            "the new vertical's ground-truth calibrates to auto-seed and "
            "grade inflation enters from day one (per 2026-05-03 lesson)."
        ),
        matched_signals=hits,
    )


def _resolve_conversation(intent_lower: str) -> Optional[MissionPackage]:
    """Class 8 — Reflective / opinion-solicitation intent. Phase A.

    NO deliverable. NO G1 sharpening (reflective questions are already
    sharp BY being exploratory). NO chain_runner.finalize (nothing to
    score). Ledger still emits — these calls inform ledger-learning.
    """
    hits = _match_signals(intent_lower, CONVERSATION_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="conversation",
        primary_workflow="dialogue",  # SIGNAL tag, not a workflow file —
                                       # autopilot.md Phase 2 handles inline.
        sub_workflows=[],
        experts=[],  # the dialogue uses session context; no expert load required
        skills_to_load=[],
        plugins=["episodic-memory"],
        cost_tier="free",
        fanout_pattern="sequential",
        fanout_workers_estimate=1,
        gates_to_surface=[],  # no deliverable, no quality gate
        halt_suppressions=[
            "G1 intent sharpening (reflective questions are sharp by being exploratory)",
            "Step 6 chain_runner.finalize (no deliverable to score)",
        ],
        confidence=0.85,
        reasoning=(
            "Reflective / opinion-solicitation intent. User wants Claude's "
            "judgment, ranking, or take — not a deliverable file. Skip G1 "
            "(forcing DICE sharpening on a reflective question ruins it) and "
            "skip Step 6 finalize (nothing to score). Ledger still emits so "
            "the call gets tracked for Phase B ledger-learning."
        ),
        matched_signals=hits,
    )


def _resolve_exploration(intent_lower: str) -> Optional[MissionPackage]:
    """Class 9 — Open-ended landscape mapping. Phase A.

    Distinct from research (which produces an intelligence brief) — this is
    dialogic. May optionally invoke /research-landscape or /reflect as a
    sub-workflow if mid-dialogue the user wants structured output.
    """
    hits = _match_signals(intent_lower, EXPLORATION_SIGNALS)
    if not hits:
        return None
    return MissionPackage(
        outcome_class="exploration",
        primary_workflow="dialogue",
        sub_workflows=["research-landscape", "reflect"],
        experts=[],
        skills_to_load=["research-landscape", "reflect"],
        plugins=["episodic-memory"],
        cost_tier="cheap",  # may pull cards / light research to ground dialogue
        fanout_pattern="sequential",
        fanout_workers_estimate=1,
        gates_to_surface=[],
        halt_suppressions=[
            "G1 intent sharpening (exploratory by design)",
            "Step 6 chain_runner.finalize (no deliverable to score)",
        ],
        confidence=0.8,
        reasoning=(
            "Open-ended exploration intent. User is mapping a space, not "
            "requesting a deliverable. Defaults to conversational mode; "
            "/research-landscape or /reflect are available as optional sub-"
            "workflows if structured output is needed mid-dialogue."
        ),
        matched_signals=hits,
    )


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
    _resolve_refinement,            # Class 6
    _resolve_research,              # Class 3
    _resolve_atomization,           # Class 4
    _resolve_source_to_skill_system,
    _resolve_knowledge_librarian,
    _resolve_repeatability_spine,
    _resolve_maintenance,           # Class 5
    _resolve_long_running_project,  # Class 11 (Phase D — fires early because
                                     #            "build me a brand over the next week"
                                     #            is long-running, not multi_deliverable)
    _resolve_vertical_bootstrap,    # Class 10 (Phase C — fires before multi/single
                                     #            since "build me a brand for [new domain]"
                                     #            should bootstrap, not assume vertical exists)
    _resolve_multi_deliverable,     # Class 2
    _resolve_conversation,          # Class 8  (Phase A — universal front door)
    _resolve_exploration,           # Class 9  (Phase A — landscape mapping)
    _resolve_single_deliverable,    # Class 1  (multi-subroute)
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
        "No outcome-class signals matched (including conversation and "
        "exploration patterns). Falling back to /big-project scaffold. "
        "Consider sharpening intent (G1) or invoking a specific workflow "
        "directly."
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
            "8_conversation": CONVERSATION_SIGNALS,
            "9_exploration": EXPLORATION_SIGNALS,
            "10_vertical_bootstrap": VERTICAL_BOOTSTRAP_SIGNALS,
            "11_long_running_project": LONG_RUNNING_SIGNALS,
            "7_freeform": "(fallback when no other class matches)",
        }, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
