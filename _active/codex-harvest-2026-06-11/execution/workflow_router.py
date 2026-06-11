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

from routing_governor import (
    end_session_route_bonus,
    extraction_governor_route_bonus,
    expert_composition_route_bonus,
    front_door_choice_route_bonus,
    deep_research_os_route_bonus,
    handoff_route_bonus,
    health_check_route_bonus,
    is_deep_research_os_intent,
    is_end_session_closeout_intent,
    is_explicit_menu_backend_intent,
    is_extraction_governor_intent,
    is_expert_composition_intent,
    is_front_door_choice_intent,
    is_health_check_intent,
    is_kishotenketsu_storytelling_intent,
    is_liam_linkedin_lead_magnet_intent,
    is_operating_alignment_intent,
    is_productized_ai_service_os_intent,
    is_repeatability_intent,
    is_revenue_intent,
    is_routing_intelligence_intent,
    is_skill_anneal_intent,
    is_system_audit_query,
    is_skill_system_intent,
    is_steering_compass_intent,
    is_system_failure_intent,
    is_transfer_handoff_intent,
    is_virtuoso_intent,
    kishotenketsu_storytelling_route_bonus,
    liam_linkedin_lead_magnet_route_bonus,
    menu_backend_route_bonus,
    operating_alignment_route_bonus,
    productized_ai_service_os_route_bonus,
    repeatability_route_bonus,
    revenue_route_bonus,
    routing_intelligence_route_bonus,
    skill_anneal_route_bonus,
    skill_system_route_bonus,
    steering_compass_route_bonus,
    system_failure_route_bonus,
    virtuoso_route_bonus,
)

WF_DIR = Path(".agent/workflows")
INDEX_CACHE = None

CONTROL_PLANE_ROUTES = {
    "autopilot",
    "system-audit",
    "repeatability-spine",
    "routing-intelligence",
    "health-check",
    "end-session",
    "knowledge-librarian",
    "source-to-skill-system",
    "extraction-governor-agent",
    "expert-composition-governor",
    "virtuoso",
    "mission",
    "orchestrate",
    "self-evolve",
    "skill-anneal",
}

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "do", "for", "from",
    "go", "how", "i", "if", "in", "is", "it", "just", "me", "of", "on",
    "or", "should", "that", "the", "this", "to", "use", "with", "what",
    "when", "where", "who", "why", "you", "your",
}

# Domain mapping for intelligent routing
DOMAIN_MAP = {
    "linkedin": ["diandra", "lara", "high-dwell", "profile-conversion", "algorithmic-reach"],
    "copy": ["proof", "vicious", "hook", "mechanism", "copy", "fascination", "persuasion"],
    "brand": ["junyuh", "caleb", "oren", "taste", "grace", "zero-to-brand", "manifesto"],
    "ghostwriting": ["ghost", "voice", "cole", "roth"],
    "content": ["content", "atomize", "format", "serial", "parallel-content", "quantity-sprint"],
    "newsletter": ["newsletter", "substack", "parallax", "book-never-ends"],
    "psychology": ["drk", "kallaway", "belief", "identity", "consciousness", "resistance"],
    "seo": ["gotch", "parasite-seo", "analyze-intent"],
    "ads": ["ad-script", "full-stack-ad", "cash-method", "creative-diversity", "ai-ad-production"],
    "offers": ["design-offer", "offer-stack", "offer-cycle", "high-ticket", "nuclear-vsl"],
    "real-estate": ["enrico", "listing", "data-driven-ops"],
    "agentic": ["saraev", "swarm", "council", "parallel", "orchestration", "auto-experiment"],
    "system": [
        "system", "health-check", "calibrate", "harness", "evolution", "session",
        "autopilot", "orchestrate", "routing-intelligence", "command-menu",
        "skill-anneal", "self-evolve", "gap-analysis", "notion", "mission",
        "repeatability-spine", "repeatability", "revision", "regression",
    ],
    "writing": ["connelly", "wright", "roth", "word", "haunt", "erosion", "estrangement", "memoir"],
    "research": ["research", "deep-research", "competitor", "icp", "generate-brief"],
    "extraction": ["extract", "convert", "compile-knowledge", "knowledge"],
    "client": ["client", "outreach", "proposal", "npq", "cold-outreach", "upwork"],
    "fladlien": ["fladlien"],
    "revenue": [
        "revenue", "monetize", "recurring", "affiliate", "lifestyle-business",
        "first-10k", "revenue-offer-agent", "client-acquire",
        "zero-to-client-sprint", "service-first-productization", "cash-method",
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
    normalized_query = query.lower()
    query_terms = [
        term
        for term in re.findall(r"[a-z0-9][a-z0-9-]*", normalized_query)
        if len(term) > 2 and term not in STOPWORDS
    ]
    scored = []

    for wf in index:
        searchable = f"{wf['name']} {wf['description']} {wf['full_name']}".lower()
        score = 0
        compact_query = re.sub(r"[^a-z0-9]", "", normalized_query)
        if command_name_hit(wf["name"], normalized_query):
            score += 160
        if wf["name"] == "end-session" and compact_query in {"endsession", "sourcecommandendsession"}:
            score += 160
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
        if wf["name"] == "steering-compass" and is_steering_query(normalized_query):
            score += 12
        if is_steering_compass_intent(normalized_query):
            score += steering_compass_route_bonus(wf["name"])
        if is_transfer_handoff_intent(normalized_query):
            score += handoff_route_bonus(wf["name"])
        if wf["name"] == "autopilot" and is_explicit_autopilot_invocation(normalized_query) and not is_revenue_intent(normalized_query):
            score += 260
        if wf["name"] == "autopilot" and is_autopilot_query(normalized_query):
            score += 40
        if wf["name"] == "buyer-trigger-os" and (
            "buyer-trigger-os" in normalized_query
            or "buyer trigger os" in normalized_query
            or "meg heckman" in normalized_query
            or "print on demand trigger audit" in normalized_query
            or "apparel buyer psychology" in normalized_query
            or "current buyer insights" in normalized_query
            or "buyer insight" in normalized_query and "trend" in normalized_query
            or "purchase intent research" in normalized_query
            or "social listening" in normalized_query and ("product" in normalized_query or "buyer" in normalized_query or "shirt" in normalized_query or "apparel" in normalized_query)
            or "trend-backed shirt" in normalized_query
            or "research-backed trigger audit" in normalized_query
            or "find buyer trends" in normalized_query
            or "buyer trends" in normalized_query and ("shirt" in normalized_query or "product" in normalized_query or "offer" in normalized_query)
            or "josh shirt purchase intent" in normalized_query
            or "mybpm streetwear design psychology" in normalized_query
            or "edm streetwear purchase intent" in normalized_query
            or "shirt purchase intent" in normalized_query
        ):
            score += 180
        if is_operating_alignment_intent(normalized_query):
            score += operating_alignment_route_bonus(wf["name"])
        if is_virtuoso_intent(normalized_query):
            score += virtuoso_route_bonus(wf["name"])
        if is_kishotenketsu_storytelling_intent(normalized_query):
            score += kishotenketsu_storytelling_route_bonus(wf["name"])
        if is_deep_research_os_intent(normalized_query):
            score += deep_research_os_route_bonus(wf["name"])
            if wf["name"] == "autopilot":
                score -= 220
        if is_front_door_choice_intent(normalized_query):
            score += front_door_choice_route_bonus(wf["name"])
        if is_explicit_menu_backend_intent(normalized_query):
            score += menu_backend_route_bonus(wf["name"])
        if is_end_session_closeout_intent(normalized_query):
            score += end_session_route_bonus(wf["name"])
        if is_health_check_intent(normalized_query):
            score += health_check_route_bonus(wf["name"])
        if is_routing_intelligence_intent(normalized_query):
            score += routing_intelligence_route_bonus(wf["name"])
        if is_skill_anneal_intent(normalized_query):
            score += skill_anneal_route_bonus(wf["name"])
        if wf["name"] == "mission" and is_mission_query(normalized_query):
            score += 80
        if wf["name"] == "system-efficiency-benchmark" and is_efficiency_benchmark_query(normalized_query):
            score += 125
        if is_efficiency_benchmark_query(normalized_query):
            score += efficiency_benchmark_bonus(wf["name"])
        if is_creative_brief_query(normalized_query):
            score += creative_brief_bonus(wf["name"])
        if is_extraction_source_query(normalized_query):
            score += extraction_source_bonus(wf["name"])
        if is_extraction_governor_intent(normalized_query):
            score += extraction_governor_route_bonus(wf["name"])
        if is_plugin_readiness_query(normalized_query):
            score += plugin_readiness_bonus(wf["name"])
        if is_self_evolution_query(normalized_query) and not is_system_failure_intent(normalized_query):
            score += self_evolution_bonus(wf["name"])
        if is_knowledge_librarian_query(normalized_query) and not is_system_failure_intent(normalized_query):
            score += knowledge_librarian_bonus(wf["name"])
        if is_system_orchestration_query(normalized_query):
            score += system_orchestration_bonus(wf["name"])
            if wf["name"].startswith("fladlien-"):
                score -= 30
        repeatability_intent = is_repeatability_intent(normalized_query)
        if repeatability_intent:
            score += repeatability_route_bonus(wf["name"])
        system_audit_intent = is_system_audit_query(normalized_query)
        if is_system_failure_intent(normalized_query) and not repeatability_intent:
            score += system_failure_route_bonus(wf["name"], normalized_query)
            if system_audit_intent:
                if wf["name"] == "system-audit":
                    score += 220
                elif wf["name"] == "autopilot":
                    score -= 180
                elif wf["name"] not in CONTROL_PLANE_ROUTES:
                    score -= 80
            elif wf["name"] == "autopilot":
                score += 120
        if is_skill_system_intent(normalized_query) and not is_system_failure_intent(normalized_query):
            score += skill_system_route_bonus(wf["name"])
        if is_expert_composition_intent(normalized_query):
            score += expert_composition_route_bonus(wf["name"])
        if is_revenue_intent(normalized_query):
            score += revenue_route_bonus(wf["name"])
            if wf["name"] == "autopilot":
                score -= 170
        if is_liam_linkedin_lead_magnet_intent(normalized_query):
            score += liam_linkedin_lead_magnet_route_bonus(wf["name"])
        if is_productized_ai_service_os_intent(normalized_query):
            score += productized_ai_service_os_route_bonus(wf["name"])
        if is_ai_employee_os_intent(normalized_query):
            score += ai_employee_os_route_bonus(wf["name"])
        vibe_tax_deployment = is_vibe_tax_deployment_query(normalized_query)
        if wf["name"] == "vibe-tax-deploy" and vibe_tax_deployment:
            score += 220
        if wf["name"] == "vibe-tax-result-writer" and is_vibe_tax_result_writer_query(normalized_query):
            score += 260
        if wf["name"] == "vibe-tax-brief" and is_vibe_tax_brief_query(normalized_query):
            explicit_copy_gate_terms = ("publishable", "copy", "hook", "post", "linkedin")
            score += 40 if any(term in normalized_query for term in explicit_copy_gate_terms) else 180
            if is_vibe_tax_result_writer_query(normalized_query):
                score -= 120
            if vibe_tax_deployment:
                score -= 80
        if is_farrice_content_os_query(normalized_query):
            score += farrice_content_os_bonus(wf["name"])
        if is_diandra_linkedin_system_query(normalized_query):
            score += diandra_linkedin_system_bonus(wf["name"])
        if (
            wf["name"] == "publishable-copy-gate"
            and is_publishable_copy_query(normalized_query)
            and not is_productized_ai_service_os_intent(normalized_query)
            and not is_diandra_linkedin_system_query(normalized_query)
            and not is_kishotenketsu_storytelling_intent(normalized_query)
        ):
            score += 140
        if wf["name"] == "video-context-ledger" and is_video_context_query(normalized_query):
            score += 12
        if wf["name"] == "ai-carousel-engine" and is_ai_carousel_query(normalized_query):
            score += 12
        if score > 0:
            scored.append((score, wf))

    scored.sort(key=lambda x: (-x[0], x[1]["name"]))
    return scored[:top_n]


def command_name_hit(name, query):
    if not name:
        return False
    return bool(re.search(rf"(?<![a-z0-9-])/?{re.escape(name)}(?![a-z0-9-])", query))


def is_steering_query(query):
    """Detect natural closeout/next-step phrases that should route to steering."""
    phrase_hits = [
        "go with your verdict",
        "use your verdict",
        "your recommendation",
        "recommended path",
        "what should i do next",
        "what do i do next",
        "next steps",
        "post output",
        "post-output",
        "after extraction output",
        "after completed work",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True
    return ("verdict" in query and "next" in query) or ("output" in query and "next" in query)


def is_autopilot_query(query):
    """Detect natural planning/intent-front-door phrases that should route to Autopilot."""
    if is_front_door_choice_intent(query):
        return True
    phrase_hits = [
        "autopilot skill",
        "autopilot plan",
        "plan gate",
        "plan mode",
        "clarity score",
        "clarity percentage",
        "ask clarifying questions",
        "clarifying questions",
        "verify my intent",
        "verify intent",
        "intent then execute",
        "raw thoughts",
        "raw notes",
        "raw context",
        "messy idea",
        "messy context",
        "figure out what to do",
        "what should i do with this",
        "what should this become",
        "gateway command",
        "gateway to my workflow",
        "full arsenal",
        "ambiguity before execution",
        "before executing",
        "plan and execute",
        "use subagents",
        "use agents",
        "delegate this",
        "parallel agents",
        "underusing agents",
        "forgetting subagents",
        "forgetting agents",
        "teach me every exchange",
        "operator lesson",
        "compounding intelligence",
        "cognitive load",
        "routing orchestration",
        "skill selection",
        "triage menu",
        "autopilot visibility",
        "auto-pilot visibility",
        "self improving monitoring",
        "self-improving monitoring",
        "co-creative launchpad",
        "co creative launchpad",
        "cocreative launchpad",
        "launching pad before build",
        "apex before build",
        "raw intent",
        "better questions",
        "intent alignment before execution",
        "senior partner before execution",
        "what good looks like",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True
    return (
        ("raw" in query and ("execute" in query or "plan" in query or "intent" in query))
        or ("messy" in query and ("idea" in query or "context" in query or "notes" in query))
        or ("clarity" in query and ("intent" in query or "percentage" in query or "score" in query or "execute" in query))
        or ("ambiguity" in query and ("execute" in query or "execution" in query or "intent" in query))
        or ("clarifying" in query and ("question" in query or "questions" in query or "intent" in query))
        or ("plan" in query and ("mode" in query or "gate" in query or "execute" in query or "intent" in query))
        or ("gateway" in query and ("workflow" in query or "command" in query or "process" in query))
        or ("arsenal" in query and ("workflow" in query or "skill" in query or "agent" in query or "power" in query))
        or ("subagent" in query and ("research" in query or "write" in query or "red-team" in query))
        or ("underusing" in query and ("agent" in query or "agents" in query or "system" in query or "tools" in query))
        or ("forgetting" in query and ("agent" in query or "agents" in query or "subagent" in query or "subagents" in query or "workflow" in query))
        or ("teach" in query and ("exchange" in query or "interaction" in query or "prompt" in query or "system" in query))
        or ("operator" in query and "lesson" in query)
        or ("cognitive" in query and ("load" in query or "flow" in query))
        or ("routing" in query and ("orchestration" in query or "skill" in query or "triage" in query or "visibility" in query))
        or ("notion" in query and ("routing" in query or "orchestration" in query or "autopilot" in query or "monitoring" in query))
    )


def is_explicit_autopilot_invocation(query):
    """Detect a literal /autopilot or source-command-autopilot opening."""
    compact = re.sub(r"[^a-z0-9]", "", query.lower())
    if compact in {"autopilot", "sourcecommandautopilot"}:
        return True
    return bool(re.match(r"\s*/?(source[- ]command[- ])?autopilot\b", query.lower()))


def is_mission_query(query):
    """Detect persistent, governed, multi-step work that should route to Mission OS."""
    phrase_hits = [
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
        "handoff",
        "handoffs",
        "artifact contract",
        "engineering artifact",
        "govern long-running",
        "resume later",
        "client-facing system",
        "system-changing",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True

    mission_terms = {
        "mission", "milestone", "milestones", "handoff", "handoffs",
        "persistent", "durable", "state", "governance", "govern",
        "validation", "contract", "charter", "artifact", "resume",
        "multi-step", "multistep", "long-running", "long running",
    }
    hits = sum(1 for term in mission_terms if term in query)
    return hits >= 3


def is_diandra_linkedin_system_query(query):
    """Detect whole LinkedIn operating-system requests owned by Diandra."""
    source_system_terms = (
        "source-to-skill",
        "source to skill",
        "source-to-system",
        "source to system",
        "turn this source",
        "convert this source",
        "video source",
    )
    if any(term in query for term in source_system_terms):
        return False

    phrase_hits = (
        "diandra linkedin system",
        "diandra's linkedin system",
        "linkedin operating system",
        "linkedin content system",
        "linkedin system",
        "profile content buckets",
        "content buckets comment flywheel",
        "comment flywheel",
        "linkedin seo profile",
        "profile-first linkedin",
        "profile first linkedin",
        "360brew",
        "360 brew",
        "40 30 20 10",
    )
    if any(phrase in query for phrase in phrase_hits):
        return True

    has_linkedin = "linkedin" in query or "diandra" in query
    system_terms = ("system", "operating", "profile", "seo", "bucket", "buckets", "flywheel")
    content_terms = ("content", "post", "posts", "comment", "comments", "growth", "authority")
    return (
        has_linkedin
        and sum(1 for term in system_terms if term in query) >= 2
        and any(term in query for term in content_terms)
    )


def is_vibe_tax_brief_query(query):
    phrase_hits = [
        "vibe tax",
        "vibe-tax",
        "vibe tax brief",
        "vibe tax diagnostic",
        "false-signal diagnostic",
        "false signal diagnostic",
        "false signal brief",
        "run the vibe",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True
    return (
        ("false signal" in query or "proof gap" in query)
        and ("buyer" in query or "offer" in query or "strategy" in query or "content" in query)
    )


def is_vibe_tax_result_writer_query(query):
    if "vibe tax" not in query and "vibe-tax" not in query:
        return False
    result_terms = (
        "result",
        "read",
        "sendable",
        "pasted",
        "paste",
        "row",
        "notion codex input",
        "codex input",
        "reply status",
        "reply status = new",
        "polish",
        "diagnostic response",
        "response row",
        "google form",
        "google sheet",
        "tracker",
    )
    return any(term in query for term in result_terms)


def is_vibe_tax_deployment_query(query):
    if "vibe tax" not in query and "vibe-tax" not in query:
        return False
    deployment_terms = (
        "deploy",
        "deployment",
        "launch",
        "post",
        "linkedin",
        "daily",
        "outreach",
        "brief-demo",
        "brief demo",
        "proof demo",
        "sell",
        "sales",
        "diagnostic launch",
        "fresh session",
        "bootstrap",
    )
    return any(term in query for term in deployment_terms)


def is_farrice_content_os_query(query):
    """Detect Farrice-specific end-to-end content operating-system requests."""
    phrase_hits = (
        "farrice content os",
        "farrice-content-os",
        "diandra to farrice",
        "diandra-to-farrice",
        "content done end to end",
        "end to end content",
        "end-to-end content",
        "raw concepts into content",
        "raw concept into content",
        "voice taste brandjack",
        "voice taste brandjacking",
        "writers room content system",
        "writer's room content system",
        "hook room",
        "brandjack opportunity board",
        "brandjacking hooks",
        "my content operating system",
        "my content os",
    )
    if any(phrase in query for phrase in phrase_hits):
        return True

    farrice_terms = ("farrice" in query) or ("my voice" in query and "content" in query)
    system_terms = ("content os", "content system", "content operating system", "operating system")
    quality_terms = ("voice", "taste", "writers room", "anti slop", "anti-slop", "hook", "hooks")
    research_terms = ("brandjack", "brandjacking", "research", "outlier", "newsjack", "namejack")
    return (
        farrice_terms
        and any(term in query for term in system_terms)
        and any(term in query for term in quality_terms)
    ) or (
        "diandra" in query
        and "content" in query
        and any(term in query for term in quality_terms)
        and any(term in query for term in research_terms)
    )


def farrice_content_os_bonus(workflow_name):
    bonuses = {
        "farrice-content-os": 360,
        "diandra-linkedin-system": 90,
        "diandra-content-engine": 82,
        "diandra-growth-sprint": 78,
        "diandra-steal-and-remix": 74,
        "writers-room": 72,
        "high-taste-writing-os": 68,
        "voice-first-content": 66,
        "anti-slop-audit": 60,
        "publishable-copy-gate": 54,
        "content-brand-forge": 44,
    }
    return bonuses.get(workflow_name, 0)


def diandra_linkedin_system_bonus(workflow_name):
    bonuses = {
        "diandra-linkedin-system": 240,
        "diandra-content-engine": 86,
        "diandra-growth-sprint": 82,
        "diandra-algorithm-audit": 78,
        "diandra-semantic-lanes": 64,
        "diandra-headline-engineer": 58,
        "diandra-steal-and-remix": 54,
        "profile-conversion": 36,
        "publishable-copy-gate": -160,
    }
    return bonuses.get(workflow_name, 0)


def is_publishable_copy_query(query):
    """Detect public/revenue copy that should surface the publishable copy gate."""
    creative_visual_terms = (
        "creative brief",
        "visual direction",
        "design brief",
        "generate images",
        "generate videos",
        "image direction",
        "video direction",
    )
    copy_specific_terms = ("copy", "post", "linkedin", "outreach", "sales", "revenue", "cta")
    if any(term in query for term in creative_visual_terms) and not any(term in query for term in copy_specific_terms):
        return False

    unresolved_offer_terms = (
        "unclear offer",
        "offer unclear",
        "needs positioning",
        "positioning before copy",
        "before copy",
        "position before copy",
        "not ready for copy",
        "offer needs",
    )
    if any(term in query for term in unresolved_offer_terms):
        return False

    public_terms = (
        "publishable",
        "public",
        "public-facing",
        "client-facing",
        "linkedin",
        "outreach",
        "marketplace",
        "proposal",
        "dm",
        "checkout",
        "offer",
        "sales",
        "revenue",
    )
    copy_terms = (
        "copy",
        "post",
        "hook",
        "voice",
        "tension",
        "punch",
        "cta",
        "comment",
        "opener",
        "rewrite",
    )
    quality_terms = (
        "flat",
        "generic",
        "slop",
        "copywriting agent",
        "brand-jack",
        "buyer language",
        "ai misfire",
        "proof-led",
    )
    return (
        any(term in query for term in public_terms)
        and any(term in query for term in copy_terms)
    ) or any(term in query for term in quality_terms)


def is_creative_brief_query(query):
    phrase_hits = (
        "creative brief",
        "design brief",
        "visual direction",
        "image direction",
        "video direction",
        "generate images",
        "generate videos",
        "mood board",
        "art direct",
    )
    return any(phrase in query for phrase in phrase_hits) and not is_publishable_copy_query(query)


def creative_brief_bonus(workflow_name):
    bonuses = {
        "creative-brief-gen": 185,
        "design-brief": 170,
        "creative-design-agent": 155,
        "higgsfield-studio": 140,
        "mood-board": 95,
        "art-direct": 85,
        "publishable-copy-gate": -180,
    }
    return bonuses.get(workflow_name, 0)


def is_system_orchestration_query(query):
    """Detect harness/routing/observability work that should surface system workflows."""
    signals = {
        "autopilot", "auto-pilot", "routing", "router", "orchestration",
        "orchestrate", "skill", "skills", "triage", "menu", "visibility",
        "visible", "monitoring", "self-improving", "self improving", "notion",
        "bridge", "command", "commands", "workflow", "workflows", "harness",
        "system", "mission",
    }
    hits = sum(1 for signal in signals if signal in query)
    return hits >= 2 or (
        ("routing" in query or "router" in query) and
        ("skill" in query or "orchestration" in query or "workflow" in query)
    )


def is_efficiency_benchmark_query(query):
    """Detect performance/overengineering checks before changing the system shape."""
    phrase_hits = [
        "system efficiency",
        "efficiency benchmark",
        "measure first",
        "routing latency",
        "routing overhead",
        "context footprint",
        "command bloat",
        "system bloat",
        "too many skills",
        "overengineering",
        "over-engineering",
        "broad restructuring",
        "package the whole system",
        "package everything",
        "whole system",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True
    return (
        ("plugin" in query or "packaging" in query or "restructuring" in query)
        and ("performance" in query or "efficiency" in query or "bloat" in query or "overhead" in query)
    )


def efficiency_benchmark_bonus(workflow_name):
    bonuses = {
        "system-efficiency-benchmark": 225,
        "bloat-optimizer": 195,
        "context-audit": 150,
        "system-hygiene": 130,
        "routing-intelligence": 115,
        "expert-composition-governor": -220,
    }
    return bonuses.get(workflow_name, 0)


def is_extraction_source_query(query):
    """Detect source-to-capability extraction work before generic orchestration wins."""
    phrase_hits = [
        "source material",
        "source-to-system",
        "source to system",
        "source-to-skill",
        "source to skill",
        "hidden mechanics",
        "reusable commands",
        "reusable command",
        "reusable workflows",
        "reusable workflow",
        "duplicate systems",
        "duplicate system",
        "avoid duplicate",
        "turn this source",
        "convert this source",
        "extract the mechanics",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True
    source_terms = ("source" in query or "transcript" in query or "article" in query or "guide" in query)
    build_terms = (
        "extract" in query
        or "forge" in query
        or "skill" in query
        or "workflow" in query
        or "command" in query
        or "library" in query
    )
    return source_terms and build_terms and ("duplicate" in query or "reusable" in query or "mechanic" in query)


def extraction_source_bonus(workflow_name):
    bonuses = {
        "source-to-skill-system": 120,
        "extraction-governor-agent": 145,
        "extract-forge": 90,
        "convert-extraction": 80,
        "compile-knowledge": 65,
        "knowledge-librarian": 45,
        "video-source-extract": 35,
        "extract": 30,
    }
    return bonuses.get(workflow_name, 0)


def is_plugin_readiness_query(query):
    """Detect plugin-family packaging decisions before generic system routing wins."""
    phrase_hits = [
        "plugin readiness",
        "plugin-readiness",
        "workflow family should become",
        "become a codex plugin",
        "become a plugin",
        "stay as workflows",
        "stay as workflow",
        "stay as skills",
        "stay as skill",
        "package a workflow",
        "package this workflow",
        "package this family",
        "fresh-thread",
        "fresh thread",
        "plugin acceptance",
        "plugin tests",
        "repo-local plugin",
        "repo local plugin",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True
    return (
        ("plugin" in query or "packaging" in query or "package" in query)
        and ("workflow" in query or "skill" in query or "family" in query or "readiness" in query)
        and "whole system" not in query
    )


def plugin_readiness_bonus(workflow_name):
    bonuses = {
        "plugin-readiness-audit": 150,
        "system-efficiency-benchmark": 40,
        "knowledge-librarian": 25,
    }
    return bonuses.get(workflow_name, 0)


def is_self_evolution_query(query):
    """Detect feedback/failure-history improvement work before generic orchestration wins."""
    phrase_hits = [
        "self evolution",
        "self-evolution",
        "self evolve",
        "self-evolve",
        "failure history",
        "feedback history",
        "performance log",
        "performance logs",
        "regression detection",
        "improve the workflow",
        "improve workflows",
        "evolve the workflow",
        "measured evolution",
        "without adding unnecessary bloat",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True
    return (
        ("feedback" in query or "failure" in query or "regression" in query or "performance" in query)
        and ("improve" in query or "evolve" in query or "workflow" in query or "routing" in query)
    )


def self_evolution_bonus(workflow_name):
    bonuses = {
        "self-evolve": 145,
        "routing-intelligence": 85,
        "skill-anneal": 45,
        "system-efficiency-benchmark": 35,
        "knowledge-librarian": 25,
    }
    return bonuses.get(workflow_name, 0)


def is_knowledge_librarian_query(query):
    """Detect library-pulse and prior-decision retrieval work."""
    phrase_hits = [
        "/knowledge-librarian",
        "source-command-knowledge-librarian",
        "source command knowledge librarian",
        "session start pulse",
        "session-start knowledge pulse",
        "knowledge librarian",
        "knowledge library",
        "prior decisions",
        "previous decisions",
        "reusable context",
        "prior reusable solution docs",
        "library pulse",
        "underused workflows",
        "underused skills",
        "sleeping giants",
        "solution docs",
        "one exact start command",
        "start command from the library",
        "what knowledge",
        "what workflows",
        "retrieve the best",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True
    return (
        ("knowledge" in query or "library" in query or "context" in query)
        and ("retrieve" in query or "surface" in query or "prior" in query or "reusable" in query or "underused" in query)
    )


def knowledge_librarian_bonus(workflow_name):
    bonuses = {
        "knowledge-librarian": 180,
        "knowledge-search": 35,
        "compile-knowledge": 30,
        "context-audit": 15,
        "end-session": -45,
        "session-kickoff": -25,
    }
    return bonuses.get(workflow_name, 0)


def system_orchestration_bonus(workflow_name):
    """Promote the system control plane when the query is about routing itself."""
    bonuses = {
        "autopilot": 70,
        "source-to-skill-system": 70,
        "mission": 60,
        "orchestrate": 55,
        "routing-intelligence": 50,
        "self-evolve": 45,
        "skill-anneal": 45,
        "command-menu": 35,
        "system-health": 35,
        "health-check": 35,
        "gap-analysis": 35,
        "knowledge-librarian": 25,
        "compile-knowledge": 20,
    }
    return bonuses.get(workflow_name, 0)


def is_ai_employee_os_intent(query):
    """Detect AI employee/company-agent operating-system requests."""
    normalized = query.lower().strip()
    if not normalized:
        return False
    phrase_hits = [
        "/ai-employee-os",
        "ai-employee-os",
        "ai employee",
        "ai employees",
        "ai coworker",
        "ai co-worker",
        "company agent",
        "team agent",
        "internal operator",
        "operating partner",
        "memory leakage",
        "memory leak",
        "context leakage",
        "context leak",
        "shared integration",
        "shared integrations",
        "scoped integration",
        "scoped integrations",
        "proactive workflow",
        "proactive workflows",
        "proactive suggestion",
        "proactive suggestions",
        "model personality",
        "personality regression",
    ]
    if any(phrase in normalized for phrase in phrase_hits):
        return True
    if (
        ("workflow" in normalized or "route" in normalized or "command" in normalized)
        and ("proactive" in normalized or "proactively" in normalized)
        and ("suggest" in normalized or "next action" in normalized or "next actions" in normalized)
    ):
        return True
    has_agent = "agent" in normalized or "coworker" in normalized or "co-worker" in normalized or "employee" in normalized
    has_employee_system_issue = any(
        term in normalized
        for term in (
            "memory",
            "leak",
            "leakage",
            "context",
            "integration",
            "proactive",
            "proactivity",
            "personality",
            "permission",
            "permissions",
            "rollout",
            "trust",
        )
    )
    return has_agent and has_employee_system_issue


def ai_employee_os_route_bonus(workflow_name):
    """Promote /ai-employee-os for AI employee/company-agent intents."""
    bonuses = {
        "ai-employee-os": 260,
        "context-audit": 60,
        "memory-architect": 56,
        "conde-agent-experience-design": 52,
        "24-assets-agent-system-design": 48,
        "harness-audit": 20,
        "source-to-skill-system": 18,
    }
    return bonuses.get(workflow_name, 0)


def is_video_context_query(query):
    phrase_hits = [
        "video context",
        "youtube context",
        "youtube video",
        "video ledger",
        "context ledger",
        "analyze youtube video",
        "visuals transcript frames",
        "transcript frames",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True
    return "video" in query and ("transcript" in query or "frames" in query or "visuals" in query or "ocr" in query)


def is_ai_carousel_query(query):
    phrase_hits = [
        "article carousel",
        "blog carousel",
        "gpt image carousel",
        "designed social carousel",
        "turn blog article into",
        "carousel engine",
        "ai carousel",
    ]
    if any(phrase in query for phrase in phrase_hits):
        return True
    return "carousel" in query and ("article" in query or "blog" in query or "gpt" in query or "image" in query or "design" in query)


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


def log_routing_choice(query, results, source="workflow-router"):
    """Log the top matched workflow when a caller opts into routing evidence."""
    if not results:
        return None
    score, wf = results[0]
    try:
        from routing_intelligence import log_routing_decision

        domain = "unknown"
        for candidate, prefixes in DOMAIN_MAP.items():
            searchable = f"{wf['name']} {wf['description']} {wf['full_name']}".lower()
            if any(prefix in searchable for prefix in prefixes):
                domain = candidate
                break

        intent_score = max(1, min(5, round(score / 3)))
        return log_routing_decision(
            request_summary=query,
            intent_score=intent_score,
            domain_detected=domain,
            experts_deployed=["antigravity-orchestrator"],
            tier_loaded=1,
            mode="output",
            workflow_used=wf["name"],
            session_id=source,
        )
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(description="Workflow Router")
    sub = parser.add_subparsers(dest="command")

    search_p = sub.add_parser("search", help="Search workflows by keyword")
    search_p.add_argument("query", help="Search query")
    search_p.add_argument("-n", "--top", type=int, default=10, help="Number of results")
    search_p.add_argument("--log-routing", action="store_true", help="Log the top matched workflow as routing evidence.")

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
        routing_id = log_routing_choice(args.query, results) if args.log_routing else None
        print(f"Top {len(results)} matches for '{args.query}':\n")
        if is_front_door_choice_intent(args.query):
            print("Routing Governor: front-door choice intent detected. /autopilot is promoted first so the system chooses the right route before exposing a broad menu.\n")
        elif is_explicit_menu_backend_intent(args.query):
            print("Routing Governor: explicit menu/options intent detected. /orchestrate remains the ranked-options backend.\n")
        elif is_revenue_intent(args.query):
            print("Routing Governor: revenue intent detected. Concrete acquisition, paid-audit, proof, and delivery routes are promoted above generic strategy.\n")
        for score, wf in results:
            print(f"  /{wf['name']:40s} — {wf['description']}")
        if routing_id:
            print(f"\nRouting logged: {routing_id}")

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
