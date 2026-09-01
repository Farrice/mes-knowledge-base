#!/usr/bin/env python3
"""
Workflow Router — Intelligent workflow lookup to reduce context overhead.

Instead of loading all 524 workflow descriptions into every prompt,
this script provides fast keyword/domain-based routing.

Usage:
    python3 execution/workflow_router.py search "linkedin content strategy"
    python3 execution/workflow_router.py domain "proof"
    python3 execution/workflow_router.py stats
    python3 execution/workflow_router.py domains
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

from control_intent import classify_control_intent
from command_aliases import resolve_explicit_command_alias

# Wave 1 (Harness Apex, 2026-07-07): BINDINGS consulted upstream — a mandatory
# binding hit pins its workflow(s) to rank #1 before any fuzzy scoring runs.
try:
    from routing_enforcer import match_bindings
except Exception:  # never let enforcer import problems break search
    def match_bindings(text):  # type: ignore
        return []

# Stopword filter (Wave 1, Harness Apex 2026-07-07). Reuses find_skill's
# curated list when importable; the replica below only covers the failure
# path (find_skill hard-exits at import when PyYAML is missing — SystemExit,
# which a bare `except Exception` would NOT catch). Keep replica in sync
# with execution/find_skill.py STOPWORDS.
try:
    from find_skill import STOPWORDS as QUERY_STOPWORDS
except BaseException:
    QUERY_STOPWORDS = {
        "a", "an", "the", "and", "or", "but", "if", "then", "of", "on", "in", "to", "for",
        "with", "from", "by", "as", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "should", "could",
        "may", "might", "i", "you", "we", "they", "it", "this", "that", "these", "those",
        "my", "your", "our", "their", "its", "use", "using", "used", "when", "where",
        "what", "which", "who", "how", "why", "just", "into", "out", "up", "down",
        "over", "about", "like", "get", "got", "make", "made",
    }

from routing_governor import (
    governed_route_names,
    is_ai_employee_os_intent,
    is_deep_research_os_intent,
    is_end_session_closeout_intent,
    is_explicit_menu_backend_intent,
    is_expert_composition_intent,
    is_extraction_governor_intent,
    is_front_door_choice_intent,
    is_health_check_intent,
    is_knowledge_librarian_intent,
    is_operating_alignment_intent,
    is_repeatability_intent,
    is_revenue_intent,
    is_routing_intelligence_intent,
    is_self_evolve_intent,
    is_skill_anneal_intent,
    is_skill_system_intent,
    is_steering_compass_intent,
    is_system_failure_intent,
    is_transfer_handoff_intent,
    is_virtuoso_intent,
)

ROOT = Path(__file__).resolve().parent.parent
WF_DIR = ROOT / ".agent" / "workflows"
INDEX_CACHE = None

OPERATOR_FRONT_DOOR_STACK = (
    "autopilot",
    "source-to-skill-system",
    "orchestrate",
    "routing-intelligence",
    "self-evolve",
    "skill-anneal",
)

MISSION_STACK = (
    "mission",
    "autopilot",
    "orchestrate",
)

RESEARCH_STACK = (
    "research-swarm",
    "parallel-research",
    "deep-research-gemini",
    "deep-research",
)

# Some workflow names contain ordinary words used by unrelated control-plane
# experiments. A fuzzy hit on one such word is not enough to claim the route.
# Explicit command aliases, bindings, and governed routes bypass this guard.
FUZZY_CONTEXT_REQUIREMENTS = {
    "shadow-market-validation-report": (
        "shadow market",
        "market",
        "validation",
        "validate",
        "demand",
        "launch",
        "niche",
        "aftermath",
        "mvp",
    ),
}


def fuzzy_context_allows_route(
    workflow_name: str,
    normalized_query: str,
    *,
    explicitly_selected: bool = False,
    bound_or_governed: bool = False,
) -> bool:
    """Reject ambiguous single-token matches for context-dependent routes."""

    if explicitly_selected or bound_or_governed:
        return True
    required_context = FUZZY_CONTEXT_REQUIREMENTS.get(workflow_name)
    if not required_context:
        return True
    return any(
        re.search(
            r"\b" + re.escape(term).replace(r"\ ", r"\s+") + r"\b",
            normalized_query,
        )
        for term in required_context
    )


def mission_query(query: str) -> bool:
    """Detect mission-continuity prompts that should beat generic build routes."""

    phrase_hits = (
        "mission mode",
        "mission control",
        "long running",
        "long-running",
        "multi milestone",
        "multi-milestone",
        "multiple milestones",
        "validation contract",
        "mission charter",
        "durable state",
        "persistent state",
        "state path",
        "artifact contract",
        "engineering artifact",
        "govern long-running",
        "resume later",
        "client-facing system",
        "system-changing",
    )
    if any(phrase in query for phrase in phrase_hits):
        return True

    mission_terms = {
        "mission",
        "milestone",
        "milestones",
        "handoff",
        "handoffs",
        "persistent",
        "durable",
        "state",
        "governance",
        "govern",
        "validation",
        "contract",
        "charter",
        "artifact",
        "resume",
        "multi-step",
        "multistep",
        "long-running",
        "long running",
    }
    return sum(1 for term in mission_terms if term in query) >= 3


def operator_front_door_query(query: str) -> bool:
    """Detect operator-navigation prompts that should start at Autopilot."""

    if "autopilot" not in query:
        return False
    context_hits = sum(
        1
        for term in (
            "notion",
            "routing",
            "orchestration",
            "skill selection",
            "triage",
            "menu",
            "self improving",
            "self-improving",
            "monitoring",
        )
        if term in query
    )
    return context_hits >= 2


def explicit_research_stack_query(query: str) -> bool:
    """Detect explicit research-stack menu probes without overriding deep-research-os."""

    return (
        "research swarm" in query
        and "parallel research" in query
        and ("deep research gemini" in query or "gemini" in query)
    )


def operator_lesson_front_door_query(query: str) -> bool:
    """Detect always-on Operator Lesson / subagent-coaching intents.

    Autopilot is the operator front door for "teach me every exchange",
    "I'm underusing subagents", and "autopilot + operator lesson + subagent
    worth it" prompts. These should start at Autopilot, which now owns the
    always-on Operator Core closeout (3 Next Prompts, Operator Lesson,
    Subagent worth it?, Reuse hook). Kept narrow so it does not hijack the
    dedicated steering-compass route for pure "3 next prompts" requests.
    """

    lesson_signal = (
        "operator lesson" in query
        or "teach me every exchange" in query
        or ("teach me" in query and "every exchange" in query)
        or "every exchange" in query
    )
    agent_signal = (
        "subagent" in query
        or "subagents" in query
        or "underusing agents" in query
        or "forgetting subagents" in query
        or "underusing subagents" in query
    )
    autopilot_signal = "autopilot" in query

    # Q-shape 1: coaching on underused agents + learning each exchange.
    if agent_signal and lesson_signal:
        return True
    # Q-shape 2: explicit autopilot + operator-lesson + subagent framing.
    if autopilot_signal and lesson_signal and agent_signal:
        return True
    return False


def governed_query_active(query: str) -> bool:
    """Return True when the routing governor has a required route stack."""

    checks = (
        mission_query,
        is_operating_alignment_intent,
        is_virtuoso_intent,
        is_deep_research_os_intent,
        is_ai_employee_os_intent,
        is_extraction_governor_intent,
        is_expert_composition_intent,
        is_front_door_choice_intent,
        is_explicit_menu_backend_intent,
        is_end_session_closeout_intent,
        is_health_check_intent,
        is_routing_intelligence_intent,
        is_knowledge_librarian_intent,
        is_skill_anneal_intent,
        is_self_evolve_intent,
        is_steering_compass_intent,
        is_repeatability_intent,
        is_system_failure_intent,
        is_skill_system_intent,
        is_revenue_intent,
    )
    return any(check(query) for check in checks)

# Domain mapping for intelligent routing
DOMAIN_MAP = {
    "linkedin": ["diandra", "lara", "high-dwell", "profile-conversion", "algorithmic-reach"],
    "copy": ["proof", "vicious", "hook", "mechanism", "copy", "fascination", "persuasion"],
    "brand": ["junyuh", "caleb", "oren", "taste", "grace", "zero-to-brand", "manifesto"],
    "ghostwriting": ["ghost", "voice", "cole", "roth"],
    "content": ["content", "atomize", "format", "serial", "parallel-content", "quantity-sprint"],
    "newsletter": ["newsletter", "substack", "parallax", "book-never-ends"],
    "psychology": ["drk", "kallaway", "belief", "identity", "consciousness", "resistance"],
    "seo": ["gotch", "parasite-seo", "seo-keyword-audit"],
    "ads": ["ad-script", "full-stack-ad", "cash-method", "creative-diversity", "ai-ad-production"],
    "offers": ["design-offer", "offer-stack", "offer-cycle", "high-ticket", "nuclear-vsl"],
    "real-estate": ["enrico", "listing", "data-driven-ops"],
    "agentic": ["saraev", "swarm", "council", "parallel", "orchestration", "auto-experiment"],
    "system": ["system", "health-check", "calibrate", "harness", "evolution", "session"],
    "writing": ["connelly", "wright", "roth", "word", "haunt", "erosion", "estrangement", "memoir"],
    "research": ["research", "deep-research", "competitor", "icp", "generate-brief"],
    "extraction": ["extract", "convert", "compile-knowledge", "knowledge"],
    "client": ["client", "outreach", "proposal", "npq", "cold-outreach", "upwork"],
    "fladlien": ["fladlien"],
    "revenue": ["revenue", "monetize", "recurring", "affiliate", "lifestyle-business"],
}

CONTROL_ROUTE_KEYWORDS = {
    "mission": [
        "mission control",
        "mission os",
        "long running system repair",
        "long-running system repair",
        "milestone handoff",
        "mission state",
    ],
    "source-to-skill-system": [
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
    "system-audit": [
        "claude code works better",
        "claude code catches my intent",
        "not working like claude code",
        "codex vs claude code",
        "codex compared to claude code",
        "match claude code",
        "mirror claude code",
        "claude parity",
        "claude-parity",
        "blocking hooks",
        "blocked hooks",
        "codex is blocking hooks",
        "wrong defaults",
        "wrong default",
        "wrong default routing",
        "routing wrong defaults",
        "routing the wrong defaults",
        "default routing",
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
        "things that have no business being the default",
        "things that shouldn't be the default",
        "thin wrappers",
        "too many thin wrappers",
        "specific things blocking performance",
        "blocking performance",
        "complete errors and issues",
        "running into complete errors",
        "running into walls",
        "without breaking my workspace",
        "without breaking claude code",
        "without breaking my claude code workspace",
        "not trying to break anything",
        "pre-flight did not kick in",
        "pre flight did not kick in",
        "preflight did not kick in",
        "pre-flight didn't kick in",
        "pre flight didn't kick in",
        "preflight didn't kick in",
        "pre-flight things did not kick in",
        "pre-flight things didn't kick in",
        "orchestration is not doing its job",
        "orchestration isn't doing its job",
        "orchestration not doing its job",
        "wording not routing",
        "not routing even when obvious",
        "not routing even when it is obvious",
        "routing even when obvious",
        "routing even when it is obvious",
        "obvious routing",
        "have to be so deterministic",
        "too deterministic",
        "high cognitive intent",
        "shooting in the dark",
        "draining",
        "painful experience",
        "hooks not firing",
        "hooks are not firing",
        "hooks not running",
        "not firing hooks",
        "codex feels ineffective",
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
        "noisy disjointed",
        "broken harness",
        "control-plane audit",
        "operating alignment",
        "operator core",
        "execution bias",
        "global/workspace drift",
        "global workspace drift",
        "workspace drift",
        "split workspace",
        "split workspaces",
        "archived codex antigravity",
        "google antigravity only",
        "global codex antigravity bridge",
        "global codex bridge",
        "dual-writing conflicts",
        "dual writing conflicts",
        "dual writing",
        "safe local next actions",
        "safe local action",
        "explains instead of executing",
        "explain instead of execute",
        "plans instead of acting",
        "planning instead of acting",
        "hands back prompts",
        "handing back prompts",
        "prompt instead of execute",
        "execute what you said",
        "patch and verify",
        "global/workspace drift",
        "global workspace drift",
        "workspace drift",
        "split workspace",
        "split workspaces",
        "archived codex antigravity",
        "google antigravity only",
        "global codex antigravity bridge",
        "global codex bridge",
        "dual-writing conflicts",
        "dual writing conflicts",
        "dual writing",
        "parallel agents",
        "delegate to agents",
        "spawn subagent",
        "read-only diagnostic subagents",
    ],
    "steering-compass": [
        "3 next prompts",
        "three next prompts",
        "operator lesson",
        "what should i do next",
        "better follow-up prompts",
        "steering compass",
        "use now harden expand",
    ],
    "convene": [
        "convene",
        "convene the council",
        "collective genius",
        "the council",
        "roundtable",
        "deliberate",
    ],
    "assemble": [
        "assemble",
        "assemble an expert panel",
        "expert assembly",
        "hybrid panel",
        "bespoke personas",
        "synthesized expert",
        "domain coverage",
        "thin coverage",
        "coverage gaps",
    ],
    "expert-composition-governor": [
        "full arsenal",
        "too many experts",
        "expert soup",
        "not interwoven",
        "one-man army",
        "one man army",
    ],
    "high-taste-writing-os": [
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
    "extraction-governor-agent": [
        "extraction governance",
        "source triage",
        "source-to-capability",
        "source to capability",
        "duplicate-system avoidance",
        "hidden mechanics",
    ],
    "repeatability-spine": [
        "copied over everything",
        "copied everything over",
        "copying everything over",
        "copied over everything from claude code",
        "copying claude code workspace",
        "copied claude code workspace",
        "previous session import",
        "import from my previous session",
        "import from previous session",
        "run an import from my previous session",
        "same caliber",
        "same calibre",
        "caliber or level",
        "calibre or level",
        "massive difference",
        "level as the previous session",
        "caliber as the previous session",
        "calibre as the previous session",
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
    "knowledge-librarian": [
        "knowledge librarian",
        "library pulse",
        "session start pulse",
        "prior decisions",
        "underused workflows",
        "sleeping giants",
    ],
}


def build_index():
    """Build the workflow index from .agent/workflows/."""
    global INDEX_CACHE
    if INDEX_CACHE is not None:
        return INDEX_CACHE

    index = []
    for f in sorted(WF_DIR.glob("*.md")):
        name = f.stem
        try:
            content = f.read_text(errors="ignore")
        except (FileNotFoundError, OSError):
            continue  # Skip missing/inaccessible workflow files gracefully

        # Extract description from YAML frontmatter
        desc_match = re.search(r"^description:\s*(.+)$", content, re.MULTILINE)
        if desc_match:
            desc = desc_match.group(1).strip().strip("\"'")
        else:
            # Fallback: first heading after frontmatter
            heading = re.search(r"^#+\s+(.+)$", content, re.MULTILINE)
            desc = heading.group(1) if heading else name

        # Extract first-level heading for full name
        h1 = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        full_name = h1.group(1) if h1 else name

        index.append({
            "name": name,
            "full_name": full_name,
            "description": desc,
            "size": len(content),
            "path": str(f),
        })

    INDEX_CACHE = index
    return index


def search_workflows(query, top_n=10):
    """Search workflows by keyword matching against name + description."""
    index = build_index()
    indexed_names = {wf["name"] for wf in index}
    explicit_alias = resolve_explicit_command_alias(query, indexed_names)
    # Wave 1 (Harness Apex, 2026-07-07): stopwords and <3-char tokens no
    # longer participate in substring scoring. Before this, the connective
    # "but" in a query substring-matched the workflow literally named
    # "bw-but-therefore" (+3 name, +2 desc) and outranked the real owner.
    query_terms = [
        t for t in query.lower().split()
        if len(t) >= 3 and t not in QUERY_STOPWORDS
    ]
    normalized_query = query.lower()

    # Wave 1: mandatory BINDINGS consulted BEFORE fuzzy scoring. A binding
    # hit pins its workflow(s) to the top of the ranking with an explicit
    # BINDING marker — routing_enforcer.BINDINGS is the source of truth the
    # post-finalize check already enforces; now the suggestion path asks too.
    binding_hits = match_bindings(query)
    binding_rank = {}  # workflow name -> (boost, matched signal)
    for pos, hit in enumerate(binding_hits):
        for sub, wf_name in enumerate(hit["workflows"]):
            if wf_name not in binding_rank:
                binding_rank[wf_name] = (50000 - pos * 200 - sub * 50, hit["signal"])
    control_intent = classify_control_intent(query)
    governed_order = []
    governed_boost = {}

    # High-confidence control-plane intents suppress EXPERTISE-DOMAIN routing only,
    # not other control-plane routes. Preserve routing_governor recommendations.
    suppress_expertise_routes = (
        control_intent["route"]
        and control_intent["confidence"] >= 88
        and control_intent["lane"] == "system-failure"
    )

    if is_transfer_handoff_intent(normalized_query):
        governed_order = governed_route_names(normalized_query, [wf["name"] for wf in index])
    elif operator_lesson_front_door_query(normalized_query):
        route_names = [wf["name"] for wf in index]
        governed_order = [route for route in OPERATOR_FRONT_DOOR_STACK if route in route_names]
    elif is_end_session_closeout_intent(normalized_query):
        governed_order = governed_route_names(normalized_query, [wf["name"] for wf in index])
    elif mission_query(normalized_query):
        route_names = [wf["name"] for wf in index]
        governed_order = [route for route in MISSION_STACK if route in route_names]
    elif operator_front_door_query(normalized_query):
        route_names = [wf["name"] for wf in index]
        governed_order = [route for route in OPERATOR_FRONT_DOOR_STACK if route in route_names]
    elif explicit_research_stack_query(normalized_query):
        route_names = [wf["name"] for wf in index]
        governed_order = [route for route in RESEARCH_STACK if route in route_names]
    elif governed_query_active(normalized_query):
        governed_order = governed_route_names(normalized_query, [wf["name"] for wf in index])
    governed_boost = {
        route: 10000 - (position * 100)
        for position, route in enumerate(governed_order[: max(top_n, 12)])
    }

    # Bindings pin rank #1 ONLY when no control-plane governance claimed the
    # query (governed stack or control-intent classification). Control-plane
    # routing stays untouched (Wave 1 constraint); a binding hit under an
    # active control lane demotes to an advisory marker, never an override.
    control_plane_active = bool(governed_order) or bool(control_intent["route"])
    if control_plane_active and binding_rank:
        binding_rank = {
            name: (50, signal) for name, (boost, signal) in binding_rank.items()
        }
    scored = []

    # If suppress_expertise_routes, only consider control-plane routes.
    if suppress_expertise_routes:
        CONTROL_PLANE_ROUTES = {
            "autopilot", "system-audit", "orchestrate", "self-evolve",
            "skill-anneal", "source-to-skill-system", "routing-intelligence",
            "end-session", "mission", "repeatability-spine",
            # health-check is control-plane too — omitting it filtered the
            # governed #1 route out of its own query class (health/status
            # queries misrouted to /system-audit, caught by two verifiers
            # 2026-07-15).
            "health-check",
        }
        wf_to_score = [
            wf for wf in index
            if (
                wf["name"] in CONTROL_PLANE_ROUTES
                or wf["name"] in binding_rank
                or (explicit_alias and wf["name"] == explicit_alias[1])
            )
        ]
    else:
        wf_to_score = index

    for wf in wf_to_score:
        if not fuzzy_context_allows_route(
            wf["name"],
            normalized_query,
            explicitly_selected=bool(explicit_alias and wf["name"] == explicit_alias[1]),
            bound_or_governed=(
                wf["name"] in binding_rank
                or wf["name"] in governed_boost
                or (control_intent["route"] and wf["name"] == control_intent["route"])
            ),
        ):
            continue
        searchable = f"{wf['name']} {wf['description']} {wf['full_name']}".lower()
        score = 0
        if explicit_alias and wf["name"] == explicit_alias[1]:
            score += 100000
            wf = dict(wf, explicit_alias=explicit_alias[0])
        if wf["name"] in binding_rank:
            boost, signal = binding_rank[wf["name"]]
            score += boost
            wf = dict(wf, binding_signal=signal)
        if wf["name"] in governed_boost:
            score += governed_boost[wf["name"]]
        if control_intent["route"] and wf["name"] == control_intent["route"]:
            confidence = int(control_intent["confidence"])
            if governed_order and governed_order[0] != control_intent["route"]:
                # If routing_governor made a specific control-plane classification,
                # it should win (it's more specific). Only boost control_intent if
                # the governed route is an expertise domain or explicit command invocation.
                CONTROL_PLANE_SET = {
                    "autopilot", "system-audit", "orchestrate", "self-evolve",
                    "skill-anneal", "source-to-skill-system", "routing-intelligence",
                    "end-session", "mission", "handoff", "repeatability-spine",
                    "extraction-governor-agent", "expert-composition-governor", "virtuoso"
                }
                governed_is_control_plane = governed_order[0] in CONTROL_PLANE_SET

                if governed_is_control_plane and confidence < 90:
                    # routing_governor picked a control-plane route and the classifier
                    # is not highly confident — let governed_boost win.
                    pass
                else:
                    # Either the governed route is expertise/domain, or the purpose-built
                    # control classifier is >=90 confident. The classifier wins — the
                    # green-core router probes assert this precedence (e.g. a "repair
                    # plan" complaint must land on /system-audit even when the governor
                    # ranks /self-evolve first).
                    if confidence >= 90:
                        score += 10100 + confidence
                    else:
                        score += 20
            else:
                score += confidence + 40
        for route, phrases in CONTROL_ROUTE_KEYWORDS.items():
            if wf["name"] == route:
                matched_phrases = [phrase for phrase in phrases if phrase in normalized_query]
                if matched_phrases:
                    score += 100 + max(len(phrase) for phrase in matched_phrases)
        for term in query_terms:
            if term in searchable:
                # Exact name match scores highest
                if term in wf["name"]:
                    score += 3
                # Description match
                if term in wf["description"].lower():
                    score += 2
                # Full name match
                if term in wf["full_name"].lower():
                    score += 1
        if score > 0:
            scored.append((score, wf))

    # A bound PRIMARY workflow with no .agent/workflows/ file still surfaces
    # (as a stub) so a binding hit is never silently dropped by index gaps.
    for hit in binding_hits:
        primary = hit["workflow"]
        if primary not in indexed_names:
            boost, signal = binding_rank[primary]
            scored.append((boost, {
                "name": primary,
                "full_name": primary,
                "description": f"(binding target — no workflow file in index) {hit['reason']}"[:200],
                "size": 0,
                "path": "",
                "binding_signal": signal,
            }))

    scored.sort(key=lambda x: (-x[0], x[1]["name"]))
    return scored[:top_n]


def domain_lookup(domain):
    """Get all workflows in a domain."""
    index = build_index()
    domain = domain.lower()

    if domain in DOMAIN_MAP:
        prefixes = DOMAIN_MAP[domain]
    else:
        prefixes = [domain]

    results = []
    for wf in index:
        for prefix in prefixes:
            if prefix in wf["name"]:
                results.append(wf)
                break

    return results


def list_domains():
    """List all available domains with workflow counts."""
    index = build_index()
    for domain, prefixes in sorted(DOMAIN_MAP.items()):
        count = len(domain_lookup(domain))
        print(f"  {domain:20s} ({count:3d} workflows) → prefixes: {', '.join(prefixes)}")


def show_stats():
    """Show index statistics."""
    index = build_index()
    total_chars = sum(wf["size"] for wf in index)
    avg_size = total_chars / len(index) if index else 0

    print(f"Total workflows:        {len(index)}")
    print(f"Total content:          {total_chars:,} chars ({total_chars // 4:,} est. tokens)")
    print(f"Avg workflow size:      {avg_size:,.0f} chars ({avg_size // 4:,.0f} est. tokens)")
    print(f"Domains mapped:         {len(DOMAIN_MAP)}")
    print()

    # Show domain distribution
    print("Domain distribution:")
    list_domains()


def main():
    parser = argparse.ArgumentParser(description="Workflow Router")
    sub = parser.add_subparsers(dest="command")

    search_p = sub.add_parser("search", help="Search workflows by keyword")
    search_p.add_argument("query", help="Search query")
    search_p.add_argument("-n", "--top", type=int, default=10, help="Number of results")

    domain_p = sub.add_parser("domain", help="List workflows in a domain")
    domain_p.add_argument("name", help="Domain name")

    sub.add_parser("domains", help="List all domains")
    sub.add_parser("stats", help="Show index statistics")

    args = parser.parse_args()

    if args.command == "search":
        results = search_workflows(args.query, args.top)
        if not results:
            print(f"No workflows match '{args.query}'")
            return
        print(f"Top {len(results)} matches for '{args.query}':\n")
        for score, wf in results:
            marker = ""
            if wf.get("binding_signal"):
                marker = f" [BINDING — mandatory route, signal: '{wf['binding_signal']}']"
            print(f"  /{wf['name']:40s}{marker} — {wf['description']}")

    elif args.command == "domain":
        results = domain_lookup(args.name)
        if not results:
            print(f"No workflows in domain '{args.name}'")
            return
        print(f"{len(results)} workflows in '{args.name}':\n")
        for wf in results:
            print(f"  /{wf['name']:40s} — {wf['description']}")

    elif args.command == "domains":
        list_domains()

    elif args.command == "stats":
        show_stats()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
