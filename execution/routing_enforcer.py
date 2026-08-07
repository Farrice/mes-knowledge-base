#!/usr/bin/env python3
"""
Routing Enforcer — Runtime validation of mandatory workflow bindings.

Source of truth for the "Mandatory Workflow Routing" table in CLAUDE.md.
This module exists because the 2026-04-21 incident proved that routing
guidance in markdown alone is advisory — Claude can read CLAUDE.md and
still pick the wrong workflow when the user's conversational ask points
elsewhere. Since the Compass Doctrine (2026-07-27) bindings are deterministic
SUGGESTIONS: code-matched, surfaced as warnings, never blocking.

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
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

if str(Path(__file__).parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).parent))

from control_intent import classify_control_intent

TRACE_DIR = Path(__file__).parent.parent / "evolution_store" / "traces"
ROUTING_LOG = TRACE_DIR / "routing_decisions.jsonl"

# ─────────────────────────────────────────────────────────
# MANDATORY BINDINGS — Source of truth for routing enforcement
# Mirror of CLAUDE.md "Mandatory Workflow Routing" table.
# Update both together (routing-bindings.md is the human twin of this table).
# ─────────────────────────────────────────────────────────

BINDINGS = [
    {
        "id": "operator_mission_control",
        "signal_phrases": [
            "mission control",
            "mission os",
            "long running system repair",
            "long-running system repair",
            "milestone handoff",
            "mission state",
        ],
        "mandatory_workflow": "mission",
        "forbidden_workflows": [],
        "reason": (
            "Mission-control language requires the Mission OS front door so the "
            "work gets a structured state, checkpoints, handoffs, and validation "
            "instead of drifting into an unrelated tactical workflow."
        ),
    },
    {
        "id": "operator_source_to_skill_system",
        "signal_phrases": [
            "source to skill system",
            "source-to-skill-system",
            "source to skill",
            "source-to-skill",
            "source to system",
            "source-to-system",
            "skill system",
            "reusable operating layer",
            "connected skill system",
        ],
        "mandatory_workflow": "source-to-skill-system",
        "forbidden_workflows": [],
        "reason": (
            "Source material becoming a reusable operating layer routes through "
            "/source-to-skill-system so evidence, route fit, component contracts, "
            "handoffs, and validation come before implementation."
        ),
    },
    {
        # Narrow on purpose: focused SEO, AEO, or GEO requests should continue
        # to reach their specialist workflows. This binding owns only the
        # unified operating-system shape introduced by Search Content Mastery.
        "id": "operator_search_content_mastery",
        "signal_phrases": [
            "search content mastery",
            "seo aeo geo content system",
            "seo aeo geo system",
            "search content system",
            "search content audit plan create score measure",
            "search content scoring and measurement",
            "rate any search content",
            "search project foundation",
            "search everywhere content system",
            "seo content service delivery",
            "aeo and seo writing prototype",
            "seo and aeo writing prototype",
            "prototype aeo and seo writing",
            "prototype seo and aeo writing",
        ],
        "mandatory_workflow": "search-content-mastery",
        "forbidden_workflows": [],
        "reason": (
            "Unified SEO/AEO/GEO system requests require the Search Content "
            "Mastery conductor so project truth, source rules, content scoring, "
            "strict measurement imports, and outcome receipts remain connected. "
            "Focused specialist tasks still route directly to Nathan Gotch, "
            "Ethan Smith, /create, or the relevant media workflow."
        ),
    },
    {
        # Amnesty 2026-07-29: signals narrowed 122 -> 53. Bare mood/maintenance
        # phrases ("not usable", "draining", "handcuff", "check and repair",
        # "running into walls") misfiled content verdicts and a partnership
        # complaint as control-plane work. Every surviving phrase names the
        # harness (hooks/routing/wiring/codex/preflight/orchestration).
        "id": "operator_system_audit",
        "signal_phrases": [
            "hook wiring",
            "route wiring",
            "routing wiring",
            "hooks or routes",
            "hooks and routes",
            "routes and hooks",
            "blocking hooks",
            "blocked hooks",
            "hooks not firing",
            "not firing hooks",
            "hooks are not firing",
            "hooks not running",
            "codex is blocking hooks",
            "claude parity",
            "claude-parity",
            "match claude code",
            "mirror claude code",
            "claude code works better",
            "not working like claude code",
            "codex vs claude code",
            "codex compared to claude code",
            "wrong default routing",
            "routing wrong defaults",
            "routing the wrong defaults",
            "default routing",
            "not routing even when obvious",
            "not routing even when it is obvious",
            "broken harness",
            "operator core",
            "control-plane audit",
            "operating alignment",
            "codex not working",
            "codex is not working",
            "codex feels ineffective",
            "no point in using codex",
            "codex not working in my workspace",
            "codex is not working in my workspace",
            "preflight didn't kick in",
            "preflight did not kick in",
            "pre-flight didn't kick in",
            "pre flight didn't kick in",
            "pre-flight did not kick in",
            "pre flight did not kick in",
            "pre-flight things didn't kick in",
            "pre-flight things did not kick in",
            "things that are not wired",
            "should not be wired together",
            "shouldn't be wired together",
            "routes are being handcuffed",
            "hooks are being handcuffed",
            "orchestration not doing its job",
            "orchestration isn't doing its job",
            "orchestration is not doing its job",
        ],
        "mandatory_workflow": "system-audit",
        "forbidden_workflows": [
            "vicious-hook",
            "diandra-hook-architect",
            "placek-hooks",
            "hook-bank",
            "hook-lab",
        ],
        "reason": (
            "Not-firing hooks and operating-alignment complaints are control-plane "
            "failures, not content-hook generation requests. /system-audit owns "
            "read-only proof, manual hook-equivalent gates, and local repair."
        ),
    },
    {
        "id": "operator_steering_compass",
        "signal_phrases": [
            "3 next prompts",
            "three next prompts",
            "operator lesson",
            "what should i do next",
            "better follow-up prompts",
            "steering compass",
            "use now harden expand",
        ],
        "mandatory_workflow": "steering-compass",
        "forbidden_workflows": [],
        "reason": (
            "Requests for continuation prompts, steering, or Operator Lessons "
            "route to /steering-compass so closeout advice is contextual, reusable, "
            "and formatted as Use Now, Harden, Expand."
        ),
    },
    {
        "id": "operator_expert_composition",
        "signal_phrases": [
            "full arsenal",
            "too many experts",
            "expert soup",
            "not interwoven",
            "one-man army",
            "one man army",
        ],
        "mandatory_workflow": "expert-composition-governor",
        "forbidden_workflows": [],
        "reason": (
            "Full-arsenal or too-many-experts language needs one function owner, "
            "bounded support slots, and a composition ledger instead of expert soup."
        ),
    },
    {
        "id": "operator_high_taste_output_os",
        "signal_phrases": [
            "high-taste plus copy-engine",
            "high taste plus copy engine",
            "copy-engine route",
            "copy engine route",
            "copy gate",
            "pass the copy gate",
            "passes the copy gate",
            "production-ready scripts that pass",
            "production ready scripts that pass",
            "load the pdp and prior brief",
            "pdp and prior brief",
            "production-ready paid ad scripts",
            "production ready paid ad scripts",
            "client-facing copy",
            "client ready copy",
            "client-ready copy",
            "publishable copy",
            "ready to send to the recruiter",
            "ready to send to the client",
            "recruiter and founder",
            "founder with no ai slop",
            "no ai slop",
            "ai tells",
            "ai slop",
            "generic scripts",
            "generic hooks",
            "generic and scientific",
            "sound generic and scientific",
            "sounds generic and scientific",
            "paid-ad voiceover",
            "paid ad voiceover",
            "spoken ad copy",
            "recordable as-is",
            "recordable as is",
            "vo-only gate",
            "vo only gate",
            "stating facts rather than appealing",
            "stating facts instead of appealing",
            "human psychology and copywriting",
            "research word banks",
            "research word bank",
            "customer avatar language",
            "avatar language",
            "word banks",
            "word bank",
            "violates the principles",
            "violates so many principles",
            "high taste output os",
            "high-taste output os",
            "high taste writing os",
            "high-taste writing os",
            "high taste os",
            "high-taste-os",
            "v4 high taste",
            "v4 bar",
            "remarkable output",
            "remarkable outputs",
            "make this as good as v4",
            "published copy v4",
            "v4 codex preflight",
            "consultant-clean",
            "consultant clean",
            "flat but structurally sound",
            "publish-ready high-taste",
            "publish ready high taste",
            "client-ready high-taste",
            "practitioner-grade artifact",
            "ai slop writing",
            "output elevation",
            "elevate this output",
        ],
        "negative_signals": [
            "name this",
            "naming",
            "brand name",
            "taste training",
            "taste roadmap",
            "taste stage",
            "design taste",
        ],
        "mandatory_workflow_any_of": [
            "high-taste-writing-os",
            "high-taste-os",
        ],
        "forbidden_workflows": [
            "taste-name",
            "taste-training",
            "taste-stage",
        ],
        "reason": (
            "V4/high-taste/remarkable-output language needs the V4 High-Taste "
            "Output OS: preflight proof, owner loading, source spine, human "
            "stakes, bounded support lanes, verification gates, and receipt. "
            "Generic taste-name or taste-training routes do not produce the "
            "artifact-level operating chain."
        ),
    },
    {
        "id": "operator_repeatability_spine",
        "signal_phrases": [
            "standard and floor",
            "quality floor",
            "this is the floor",
            "preserve this",
            "5 to 6 iterations",
            "five to six iterations",
            "iterate 5 to 6 times",
            "iterate five to six times",
            "keeps happening",
            "repeatability spine",
            "cannot repeat",
            "can't repeat",
            "lost the magic",
            "revision got worse",
            "brief gets worse",
            "brief gets worse and worse",
            "brief just gets worse",
            "gets worse and worse",
            "artifact gets worse",
            "final version got worse again",
            "got worse again with the script",
            "script is just an explanation",
            "script is explanation",
            "like notes and not actually copywriting",
            "not actually copywriting",
            "notes pretending to be copy",
            "notes pretending to be copywriting",
            "one fix breaks something else",
            "one fix and then something else breaks",
            "apply one fix and then something else breaks",
            "golden sample",
            "quality bar",
            "reproduce this",
        ],
        "mandatory_workflow": "repeatability-spine",
        "forbidden_workflows": [],
        "reason": (
            "Repeatability or regression language needs preservation of the good "
            "example, primary failure class, validation, and replay prompt."
        ),
    },
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
        "id": "offer_redteam_gate",
        "signal_phrases": [
            "new offer",
            "cold offer",
            "offer stack",
            "offer spine",
            "price the offer",
            "offer pricing",
            "what should i charge",
            "should i charge",
            "price point for",
            "launch an offer",
            "launch this offer",
            "offer structure",
            "pivot the offer",
            "change the offer",
        ],
        # Executing an already-red-teamed offer (sends, assets, fulfillment)
        # should not re-trigger the gate.
        "negative_signals": [
            "send the", "draft the dm", "outreach message", "fulfill",
            "already red-teamed", "already redteamed", "per the brief",
        ],
        "mandatory_workflow": "offer-redteam",
        "forbidden_workflows": [],
        "reason": (
            "Offer/pricing decisions route through /offer-redteam (offer_gate.py) "
            "BEFORE build or send. The gate's one prior firing killed the $400 "
            "audit offer and modified Signal Pilot — proven anti-echo-chamber. "
            "Loop-engineering brief candidate 5 (Farrice all-12 GO, 2026-07-24): "
            "a gate with no road through it never fires; this binding is the road."
        ),
        "override_flag": "--no-redteam",
        "override_warning": (
            "Only --no-redteam for offers that already carry a red-team receipt "
            "this cycle; a fresh offer skipping the gate is echo-chamber risk."
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
    # NOTE (2026-06-09, same-day reversal): the extraction_freeze binding was
    # removed at Farrice's explicit direction — extractions are never gated.
    # forge_gate.py remains as usage TELEMETRY only (status/record).
    {
        # Tight, unambiguous rhetorical-device signals → Ward Farnsworth engine.
        "id": "writing_ward_rhetoric",
        "signal_phrases": [
            "chiasmus", "saxon punch", "make this line memorable",
            "make it quotable", "rhetorical device", "anaphora", "epistrophe",
        ],
        "mandatory_workflow": "ward-rhetorical-engine",
        "forbidden_workflows": [],
        "reason": (
            "Explicit rhetorical-device / memorable-line requests route to the Ward "
            "Farnsworth engine, which applies classical devices to make the thesis line land and linger."
        ),
    },
    {
        # Tight, unambiguous Go-Direct communications signals → Lulu Cheng Meservey
        # M3 matrix front door. Specific phrases only — generic "PR" stays out to
        # avoid colliding with brand/messaging routes.
        "id": "lulu_go_direct_comms",
        "signal_phrases": [
            "go-direct", "go direct", "m3 matrix", "message-medium-messenger",
            "communications strategy", "comms strategy", "comms campaign",
            "crisis communications", "reality architect", "strategic wrongness",
        ],
        "mandatory_workflow": "lulu-m3-matrix",
        "forbidden_workflows": [],
        "reason": (
            "Go-Direct communications strategy routes to the Lulu Cheng Meservey M3 "
            "engine (Message-Medium-Messenger matrix gravity-welled to one named "
            "business goal), which owns the load-bearing comms strategy before any asset exists."
        ),
    },
    {
        # Tight, unambiguous theme-first / emotional-architecture signals →
        # Mitch Albom engine. Specific phrases only — generic "write a story"
        # stays out so it defers to the writers-room / story-stack routes.
        "id": "writing_albom_theme_first",
        "signal_phrases": [
            "theme-first", "theme first writing", "emotional architecture",
            "make the reader feel", "restraint pass", "gravedigger angle",
            "tuesdays with morrie", "sentiment without sentimentality",
        ],
        "mandatory_workflow": "albom-theme-first-engine",
        "forbidden_workflows": [],
        "reason": (
            "Explicit theme-first / emotional-architecture requests route to the Mitch "
            "Albom engine, which finds the one human truth and builds the piece backward to earn the feeling through restraint."
        ),
    },
    {
        # Tight, unambiguous Dan Wang analytical-essay signals → friction-map
        # front door. Specific phrases only — generic "essay"/"long-form" stays
        # out so it defers to writers-room / story-stack routes.
        "id": "writing_wang_analytical",
        "signal_phrases": [
            "friction map", "official story vs ground truth",
            "official story vs the ground truth", "annual letter",
            "dan wang", "draft 1.5 of history", "anchor sentence essay",
            "literary cornerstone",
        ],
        "mandatory_workflow": "wang-friction-map",
        "forbidden_workflows": [],
        "reason": (
            "Dan Wang analytical-essay requests route to the friction-map front "
            "door, which mines the gap between the official story and the ground "
            "truth (the analytical engine) before any drafting, then hands forward "
            "to /literary-cornerstone-sprint, /wang-anchor-sentence, and /wang-musical-pass."
        ),
    },
    {
        # Tight, unambiguous Michael Connelly vivid-writing signals → telling-detail
        # front door. Specific phrases only — generic "write a story"/"make it vivid"
        # stays out so it defers to writers-room / depth-layer / story-stack routes.
        "id": "writing_connelly_vivid",
        "signal_phrases": [
            "telling detail", "michael connelly", "connelly", "pick the one detail",
            "show don't tell", "show dont tell", "momentum audit",
            "good place to stop", "good places to stop",
        ],
        "mandatory_workflow": "telling-detail-engine",
        "forbidden_workflows": [],
        "reason": (
            "Explicit Michael Connelly / telling-detail / show-don't-tell / momentum "
            "requests route to the Connelly vivid-writing engine, which picks the one "
            "detail that reveals character AND situation, shows the tell instead of "
            "naming it, and keeps momentum sacred so the reader can't find a place to stop."
        ),
    },
    {
        # Tight, unambiguous Ocean Vuong perceptual-writing signals → estrangement
        # front door. Specific phrases only — generic "make it original"/"less AI"
        # stays out so it defers to writers-room / depth-layer routes.
        "id": "writing_ocean_perceptual",
        "signal_phrases": [
            "ocean vuong", "estrangement engine", "defamiliarize", "defamiliarization",
            "species test", "perceptual rewrite", "anti-homogenization",
            "escape the median sentence", "make the familiar strange",
        ],
        "mandatory_workflow": "estrangement-engine",
        "forbidden_workflows": [],
        "reason": (
            "Explicit Ocean Vuong / estrangement / defamiliarization / Species-Test "
            "requests route to the Ocean Vuong perceptual-writing engine, which leads "
            "with the concrete image, makes the familiar strange so the reader sees it "
            "for the first time, and refuses the AI-median sentence where slop and cliché "
            "live — estranging only what is TRUE (copy → /ocean-perceptual-copy, brand "
            "voice → /ocean-brand-estrangement, content → /ocean-content-anti-slop)."
        ),
    },
    {
        # Tight, unambiguous Bill Browder high-stakes-narrative-nonfiction signals →
        # next-sentence grip front door. Specific phrases only — generic "write a story"
        # / "make it gripping" stays out so it defers to writers-room / depth-layer.
        "id": "writing_browder",
        "signal_phrases": [
            "bill browder", "browder", "next-sentence test", "next sentence test",
            "make the dry material grip", "unputdownable nonfiction",
            "high-stakes narrative", "stakes escalation", "name the villain",
            "evidence as spine", "make finance gripping", "page-turner nonfiction",
        ],
        "mandatory_workflow": "browder-next-sentence-test",
        "forbidden_workflows": [],
        "reason": (
            "Explicit Bill Browder / next-sentence / high-stakes-narrative requests "
            "route to the Browder grip engine, which makes dry/complex domain material "
            "(finance/law/policy) unputdownable by escalating real jeopardy, rendering "
            "the villain through documentary evidence, and gripping the reader into the "
            "next sentence — on a load-bearing honesty spine (real stakes, real receipts)."
        ),
    },
    {
        # Tight, unambiguous Susan Orlean curiosity-driven-literary-journalism
        # signals → telling-subject front door. Specific phrases only — generic
        # "write a story" / "essay" stays out so it defers to writers-room /
        # depth-layer / story-stack.
        "id": "writing_orlean",
        "signal_phrases": [
            "susan orlean", "orlean", "telling subject", "the telling subject",
            "small overlooked subject", "find the story inside",
            "decide structure before writing", "structure before writing",
            "card structure", "three-phase process", "wait-what lead",
            "curiosity-driven literary journalism", "the orchid thief",
            "the library book",
        ],
        "mandatory_workflow": "orlean-telling-subject",
        "forbidden_workflows": [],
        "reason": (
            "Explicit Susan Orlean / telling-subject / structure-before-writing "
            "requests route to the Orlean engine, which finds the large theme "
            "hiding in a small overlooked subject, decides structure physically "
            "before any prose, protects the research/thinking/writing phases, and "
            "lifts saturation reporting into a told story — distinct from Browder "
            "thriller jeopardy, Wright Thompson lyric sportswriting, and Dan Wang "
            "analytical essay."
        ),
    },
    {
        # Tight, unambiguous Henry Shukman contemplative / wonder-writing signals →
        # concrete-doorway front door. Specific phrases only — generic "write a story"
        # / "make it poetic" stays out so it defers to writers-room / depth-layer.
        # Distinct from Ocean Vuong (estrangement) and Paul Harding (sensory maximalism).
        "id": "writing_shukman",
        "signal_phrases": [
            "henry shukman", "shukman", "concrete doorway", "the concrete doorway",
            "reopen the reader to wonder", "contemplative writing register",
            "presence over performance", "the romantic eye", "stillness in prose",
            "poetry as philosophy", "wonder of ordinary reality", "embodied word",
            "mythos register",
        ],
        "mandatory_workflow": "shukman-concrete-doorway",
        "forbidden_workflows": [],
        "reason": (
            "Explicit Henry Shukman / concrete-doorway / contemplative-wonder requests "
            "route to the Shukman engine, which reopens the reader to awe by carrying the "
            "largest feeling on one true concrete particular (presence over performance, "
            "the romantic eye, stillness, heart-first sincerity) — distinct from Ocean "
            "Vuong estrangement and Paul Harding sensory maximalism: wonder + presence + "
            "sincerity, on an honesty spine that vetoes faked mystery."
        ),
    },
    {
        # Tight, unambiguous Paul Harding lyric-perceptual / sensory-maximalism
        # signals → perception-engine front door. Specific phrases only — generic
        # "write a story" / "describe this" stays out so it defers to writers-room
        # / depth-layer. Distinct from Connelly (surgical economy), Ocean Vuong
        # (estrangement), and Henry Shukman (contemplative wonder).
        "id": "writing_harding",
        "signal_phrases": [
            "paul harding", "harding", "perception engine", "the perception engine",
            "lyric perceptual prose", "sensory maximalism", "the two things",
            "counterpoint description", "improvisation over outlining",
            "the music of prose", "translate sensation onto the page",
            "describe reality vividly", "tinkers",
        ],
        "mandatory_workflow": "harding-perception-engine",
        "forbidden_workflows": [],
        "reason": (
            "Explicit Paul Harding / perception-engine / lyric-perceptual requests "
            "route to the Harding engine, which describes reality vividly by slowing "
            "attention to the pre-linguistic instant and re-translating the raw seeing "
            "until the ordinary turns luminous (the two things, counterpoint, "
            "botanist's-precision-plus-calculus, the drummer's cadence, improvisation "
            "over outlining) — distinct from Connelly surgical economy, Ocean Vuong "
            "estrangement, and Henry Shukman contemplative wonder: sensory maximalism "
            "+ improvisation + the music of the sentence, on an honesty spine."
        ),
    },
    {
        # How-I-Write OS front door (2026-06-26) — skills/how-i-write-os.
        # The master writing conductor: composes the 10 How-I-Write experts +
        # the story-stack across altitudes for any multi-layer writing/content/
        # marketing piece. Owns no craft; diagnoses, composes, sequences, gates.
        "id": "writing_how_i_write_os",
        "signal_phrases": [
            "how i write",
            "how-i-write",
            "writing os",
            "writing council",
            "compose the writers",
            "writing operating system",
        ],
        "mandatory_workflow": "how-i-write",
        "forbidden_workflows": [],
        "reason": (
            "How-I-Write OS language routes to /how-i-write — the master writing "
            "conductor that diagnoses intent, picks the smallest sufficient altitude "
            "stack (3-6 of the 10 How-I-Write experts + story-stack), drafts in ONE "
            "voice, then runs the line + truth/clamp/prose/fact gates; it composes "
            "existing experts and never rebuilds a writer."
        ),
    },
    {
        # Deliberately narrow: explicit voice-identity language only. Voice OS is a
        # LAYER loaded by content workflows (via PRODUCTION_CORE boost + CLAUDE.md
        # Step 4), not a route that hijacks generic writing requests — a broad
        # binding here would steal routing from /ghostwrite, /parallax, /copy-engine.
        "id": "farrice_voice_alignment",
        "signal_phrases": [
            "sound like me", "in my voice", "my voice card", "voice card",
            "voice os", "voice-os", "voice alignment", "does this sound like me",
            "voice ratchet", "voice compile", "recompile the voice",
            "make it sound like farrice",
        ],
        "negative_signals": [
            "client voice", "jen", "andrea", "customer voice", "voice mining",
        ],
        "mandatory_workflow_any_of": [
            "voice-os", "voice-ratchet", "voice-compile", "voice-audit",
        ],
        "forbidden_workflows": [],
        "reason": (
            "Explicit voice-identity language routes to Voice OS (skills/voice-os/ + "
            "_active/farrice-brand/voice/VOICE-CARD.md) — the persistent compiled voice "
            "card with the 4-mode fidelity dial (MIRROR/BLEND/STRETCH/OFF) and the "
            "felt-verdict calibration loop. Improvising Farrice's voice from training "
            "memory instead of the compiled card is the failure this prevents. Client "
            "voice work (Jen, Andrea, customer VOC mining) is OFF-mode and keeps its "
            "own routes."
        ),
    },
    {
        # Social listening & audience intelligence (2026-07-16) — Apify-first pipeline.
        # Mirrors CLAUDE.md row "Social/audience/trend listening" in mandatory routing table.
        # Update both together when modifying signals or workflows.
        "id": "social_listening_apify_first",
        "signal_phrases": [
            "what's happening in", "what is happening in",
            "audience sentiment", "creator analysis", "#hashtag trends",
            "social listening", "social sentiment", "social trends",
            "creator trends", "trending in", "what's trending",
            "community sentiment", "niche trends",
        ],
        "mandatory_workflow_any_of": ["social-listen", "social-pulse"],
        "forbidden_workflows": [
            "deep-research", "deep-research-swarm", "research-topic",
            "web-research",
        ],
        "reason": (
            "Social/audience/trend listening queries require the Apify-first pipeline "
            "(/social-listen for on-demand, /social-pulse for recurring weekly). "
            "Generic deep-research workflows miss the extraction layer needed to capture "
            "raw creator data, hashtag volume, and sentiment signals before synthesis. "
            "Apify actors (Scrape Creators, hashtag actors, transcript pullers) provide "
            "the primary extraction; Perplexity synthesis follows. Skipping Apify routes "
            "to generic web search, missing the social-specific data layer."
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
            "what's happening", "social listening", "audience sentiment", "creator analysis",
            "hashtag trends", "social sentiment",
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
    {
        # Catch-all for multi-expert / collaborative / council-style creative & strategy work.
        # Routes to the reliable Collective Genius Council engine (not the fragile JCC stubs /
        # parallel_swarm). Distinct from unified_research (facts) by the negative_signals.
        "id": "collective_genius",
        "signal_phrases": [
            "convene", "the council", "get the experts together", "get the council",
            "collective genius", "multi-expert", "multiple perspectives", "roundtable",
            "what would the experts", "have the experts", "deliberate", "strike team",
            "full deploy", "cross-domain experts", "collaborate on", "experts collaborate",
        ],
        "negative_signals": [
            "deep research", "research the market", "research this", "comprehensive research",
            "system audit", "control-plane", "control plane", "hook", "hooks",
            "route", "routes", "routing", "wired", "wiring", "default settings",
            "not wired", "handcuffed", "chained together", "source-command-",
        ],
        "mandatory_workflow_any_of": [
            "convene", "collective-genius-council", "council", "roundtable",
            "strike", "campaign", "deploy", "jcc-deploy",
            "assemble", "expert-assembly", "panel-sync",
        ],
        "forbidden_workflows": ["parallel-swarm"],
        "reason": (
            "Multi-expert / council / collaborative creative & strategy work must route through "
            "the reliable Collective Genius Council (.agent/workflows/collective-genius-council."
            "workflow.js, via /convene + presets /council /roundtable /strike /campaign /deploy). "
            "It convenes a deliberately diverse cross-domain council + Farrice's lens, runs genuine "
            "2-round deliberation (genius-loaded, contradictions preserved as forks), synthesizes an "
            "outcome none could reach alone, and emits a 'How the Masters Thought' learning digest + "
            "growing rubric — holding the grounding floor at $0 incremental. The old JCC stubs forwarded "
            "to a missing plugin and parallel_swarm.py is the deprecated fragile subprocess pattern; "
            "neither should be used."
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


def match_bindings(text: str) -> List[Dict[str, str]]:
    """Pure, non-logging BINDINGS matcher for upstream (pre-ranking) consult.

    Wave 1 (Harness Apex, 2026-07-07): BINDINGS used to be consulted only
    post-finalize via check_routing() — the suggestion path (workflow_router,
    skill_router_hook) never asked. This gives routers a side-effect-free way
    to ask "does a mandatory binding own this request?" BEFORE fuzzy scoring.

    Deliberately narrower than check_routing():
      - no control_intent classification (callers handle control lanes)
      - no precondition_cmd subprocess execution (must stay pure/cheap)
      - no logging, no exit codes — just matches

    Returns a list of dicts (one per binding that fires, in BINDINGS order):
        {"signal": <matched phrase>, "workflow": <primary mandatory workflow>,
         "workflows": [<all acceptable workflows>], "reason": <binding reason>,
         "binding_id": <id>}
    Empty list = no binding fires. Never raises.
    """
    hits: List[Dict[str, str]] = []
    try:
        text_lower = text.lower()
        for binding in BINDINGS:
            matched_signal = _request_hits_signal(text, binding["signal_phrases"])
            if not matched_signal:
                continue
            negative_signals = binding.get("negative_signals") or []
            if any(neg.lower() in text_lower for neg in negative_signals):
                continue
            mandatory = binding.get("mandatory_workflow")
            any_of = binding.get("mandatory_workflow_any_of") or []
            workflows = [mandatory] if mandatory else list(any_of)
            workflows = [_normalize_workflow(w) for w in workflows if w]
            if not workflows:
                continue
            hits.append({
                "signal": matched_signal,
                "workflow": workflows[0],
                "workflows": workflows,
                "reason": binding.get("reason", ""),
                "binding_id": binding.get("id", ""),
            })
    except Exception:
        return []
    return hits


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
    classified = classify_control_intent(request)
    if classified["route"]:
        mandatory = str(classified["route"])
        result["binding_matched"] = "control_intent_classifier"
        result["matched_signal"] = ", ".join(classified["evidence"][:4]) or classified["reason"]
        result["mandatory_workflow"] = mandatory
        if chosen_norm != _normalize_workflow(mandatory):
            result["valid"] = False
            result["violation_reason"] = (
                f"Control-intent classifier routes this request to '{mandatory}', got '{chosen_norm}'. "
                f"Reason: {classified['reason']}"
            )
        return result

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

        # Amnesty 2026-07-29: the precondition_cmd gate (added 2026-06-09 for
        # the extraction freeze, reversed the same day) was removed — it had
        # ZERO users for seven weeks and was pre-compass blocking machinery.
        # Re-adding a precondition requires an explicit new decision from
        # Farrice, never a revert of this commit.

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
    chk.add_argument("--no-log", action="store_true", help="Validate without writing routing decision traces or memory")

    sub.add_parser("list", help="Print all mandatory bindings as JSON")
    sub.add_parser("appendix", help="Regenerate the generated appendix in directives/routing-bindings.md")

    args = parser.parse_args()

    if args.command == "appendix":
        # Amnesty 2026-07-29: hand-syncing the prose table drifted (RB-01
        # violated within weeks). The appendix is generated; machine list =
        # WHAT matches, prose table = WHY.
        doc = Path(__file__).parent.parent / "directives" / "routing-bindings.md"
        text = doc.read_text()
        marker = "## Appendix — machine bindings (GENERATED, do not hand-edit)"
        head = text.split("\n---\n\n" + marker)[0] if marker in text else text.rstrip() + "\n"
        lines = [
            "", "---", "", marker, "",
            "> Amnesty 2026-07-29: the header rule \"update BINDINGS and this table together\" was",
            "> violated within weeks (7+ code-only bindings, 7 prose-only rows). Hand-sync drifts;",
            "> this appendix is generated from `routing_enforcer.BINDINGS` — the machine list is",
            "> authoritative for WHAT matches; the prose table above is authoritative for WHY.",
            "> Rows above with no ID here are prose-only guidance (no machine twin) — that is fine.",
            "> Regenerate: `python3 execution/routing_enforcer.py appendix`.",
            "", "| Binding ID | Suggested workflow(s) | Signals |", "|---|---|---|",
        ]
        for b in BINDINGS:
            wf = b.get("mandatory_workflow") or " / ".join(b.get("mandatory_workflow_any_of") or [])
            lines.append(f"| `{b['id']}` | /{wf} | {len(b.get('signal_phrases') or [])} |")
        lines.append("")
        doc.write_text(head.rstrip("\n") + "\n" + "\n".join(lines))
        print(f"appendix regenerated: {len(BINDINGS)} bindings -> {doc}")
        sys.exit(0)

    if args.command == "check":
        result = check_routing(args.request, args.workflow)
        if not args.no_log:
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
