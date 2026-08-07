#!/usr/bin/env python3
"""
Command Menu — dynamic command palette for Antigravity workflows.

This is the Codex-facing selection layer for slash-command style operation.
It indexes .agent/workflows, links each workflow to its migrated command skill
when present, and prints concise menus for browsing, searching, and choosing
what to run next.

Usage:
    python3 execution/command_menu.py
    python3 execution/command_menu.py search "linkedin growth"
    python3 execution/command_menu.py domain copy
    python3 execution/command_menu.py show deep-research
"""

import argparse
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterable, Optional

from routing_governor import (
    ai_employee_os_route_bonus,
    end_session_route_bonus,
    extraction_governor_route_bonus,
    expert_composition_route_bonus,
    front_door_choice_route_bonus,
    handoff_route_bonus,
    health_check_route_bonus,
    is_ai_employee_os_intent,
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
    deep_research_os_route_bonus,
)

# Keep the Codex-facing menu aligned with workflow_router: mandatory domain
# bindings pin their owner before lexical scoring, while control-plane intents
# retain precedence. The fallback keeps menu discovery available if the
# enforcer is temporarily unavailable.
try:
    from routing_enforcer import match_bindings
except Exception:  # pragma: no cover - defensive import boundary
    def match_bindings(text: str) -> list[dict[str, object]]:  # type: ignore
        return []

ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_DIR = ROOT / ".agent" / "workflows"
COMMAND_DIR = ROOT / ".claude" / "commands"
CODEX_SKILL_DIR = ROOT / ".agents" / "skills"
COLD_CODEX_SKILL_DIR = ROOT / ".agents" / "cold-skills" / "source-command-wrappers"
ARCHIVE_BRIDGE_DIR = ROOT / ".agent" / "archive" / "stale-bridges"

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
    "raw-intent-bridge",
    "mission",
    "orchestrate",
    "self-evolve",
    "skill-anneal",
}


DOMAIN_MAP = {
    "research": {
        "label": "Research & Strategy",
        "keywords": ["research", "brief", "analyze", "landscape", "trend", "market", "competitor", "icp", "intelligence"],
    },
    "agentic": {
        "label": "Swarms & Councils",
        "keywords": ["swarm", "council", "parallel", "roundtable", "agent", "orchestration", "sprint"],
    },
    "copy": {
        "label": "Copywriting & Ads",
        "keywords": ["copy", "ad", "hook", "vsl", "lead", "proof", "mechanism", "fascination", "persuasion"],
    },
    "content": {
        "label": "Content Engines",
        "keywords": ["content", "linkedin", "post", "newsletter", "ghost", "format", "serial", "atomize", "carousel"],
    },
    "brand": {
        "label": "Brand & Positioning",
        "keywords": ["brand", "position", "campaign", "taste", "arena", "manifesto", "message", "storybrand"],
    },
    "sales": {
        "label": "Sales & Clients",
        "keywords": ["client", "sales", "outreach", "proposal", "npq", "gap", "objection", "close"],
    },
    "offers": {
        "label": "Offers & Revenue",
        "keywords": ["offer", "pricing", "product", "revenue", "affiliate", "monetize", "lifestyle", "launch"],
    },
    "design": {
        "label": "Design & Visual",
        "keywords": ["design", "visual", "video", "image", "mood", "poster", "wireframe", "sketch", "carousel"],
    },
    "writing": {
        "label": "Writing Craft",
        "keywords": ["write", "writing", "connelly", "roth", "screenplay", "dialogue", "memoir", "prose", "story"],
    },
    "psychology": {
        "label": "Psychology & Belief",
        "keywords": ["belief", "identity", "drk", "consciousness", "resistance", "emotional", "threshold"],
    },
    "system": {
        "label": "System & Skills",
        "keywords": [
            "system", "skill", "skills", "harness", "audit", "calibrate",
            "session", "evolution", "workflow", "autopilot", "orchestrate",
            "routing", "router", "triage", "command", "notion", "monitoring",
            "mission", "handoff", "validation", "contract", "repeatability",
            "revision", "revisions", "preserve", "regression",
        ],
    },
}


STOPWORDS = {
    "and", "are", "for", "from", "how", "just", "should", "that", "the",
    "this", "use", "with", "what", "when", "where", "who", "why", "you",
    "your",
}


@dataclass(frozen=True)
class Workflow:
    name: str
    title: str
    description: str
    path: Path
    has_source_command: bool
    has_codex_skill: bool
    has_cold_codex_skill: bool
    domains: tuple[str, ...]


def bridge_status(workflow: Workflow) -> str:
    if workflow.has_codex_skill:
        return "hot-bridge"
    if workflow.has_cold_codex_skill:
        return "cold-bridge"
    if workflow.has_source_command:
        return "workflow-with-source"
    return "workflow-only"


@dataclass(frozen=True)
class CommandSurface:
    name: str
    workflow_path: Path
    source_command_path: Path
    hot_skill_path: Path
    cold_skill_path: Path
    archived_paths: tuple[Path, ...]

    @property
    def has_workflow(self) -> bool:
        return self.workflow_path.exists()

    @property
    def has_source_command(self) -> bool:
        return self.source_command_path.exists()

    @property
    def has_hot_skill(self) -> bool:
        return self.hot_skill_path.exists()

    @property
    def has_cold_skill(self) -> bool:
        return self.cold_skill_path.exists()

    @property
    def execution_status(self) -> str:
        if self.has_workflow and self.has_hot_skill:
            return "hot-bridge"
        if self.has_workflow and self.has_cold_skill:
            return "cold-bridge"
        if self.has_workflow and self.has_source_command:
            return "workflow-with-source"
        if self.has_workflow:
            return "workflow-only"
        if self.has_source_command or self.has_hot_skill or self.has_cold_skill:
            return "stale-source-command"
        if self.archived_paths:
            return "stale-source-command"
        return "unknown-command"


def bridge_detail(workflow: Workflow) -> str:
    status = bridge_status(workflow)
    if status == "hot-bridge":
        return "hot-bridge (workflow + source command + live Codex skill)"
    if status == "cold-bridge":
        return "cold-bridge (workflow + recoverable cold Codex wrapper)"
    if status == "workflow-with-source":
        return "workflow-with-source (workflow + legacy source command; no Codex wrapper)"
    return "workflow-only (routable workflow; no slash-command bridge or Codex wrapper)"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def extract_description(content: str, fallback: str) -> str:
    match = re.search(r"^description:\s*(.+)$", content, re.MULTILINE)
    if match:
        return clean_inline(match.group(1))

    heading = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if heading:
        title = clean_inline(heading.group(1))
        if " — " in title:
            return title.split(" — ", 1)[1].strip()
        return title

    return fallback.replace("-", " ").title()


def extract_title(content: str, fallback: str) -> str:
    heading = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if heading:
        return clean_inline(heading.group(1))
    return f"/{fallback}"


def clean_inline(value: str) -> str:
    value = value.strip().strip("\"'")
    value = re.sub(r"\s+", " ", value)
    value = value.replace("|", "/")
    return value


def classify_domains(name: str, title: str, description: str) -> tuple[str, ...]:
    haystack = f"{name} {title} {description}".lower()
    scored = []
    for domain, config in DOMAIN_MAP.items():
        score = domain_score(name, haystack, config["keywords"])
        if score:
            scored.append((score, domain))

    if not scored:
        return ("other",)

    scored.sort(key=lambda item: (-item[0], item[1]))
    return tuple(domain for _, domain in scored[:2])


def domain_score(name: str, haystack: str, keywords: Iterable[str]) -> int:
    score = 0
    for keyword in keywords:
        if token_hit(keyword, name):
            score += 4
        elif token_hit(keyword, haystack):
            score += 2
        elif len(keyword) >= 4 and keyword in haystack:
            score += 1
    return score


def token_hit(keyword: str, text: str) -> bool:
    if " " in keyword:
        return keyword in text
    return bool(re.search(rf"(?<![a-z0-9]){re.escape(keyword)}(?![a-z0-9])", text))


def command_name_hit(name: str, phrase: str) -> bool:
    if not name:
        return False
    return bool(re.search(rf"(?<![a-z0-9-])/?{re.escape(name)}(?![a-z0-9-])", phrase))


def build_index() -> list[Workflow]:
    workflows = []
    for path in sorted(WORKFLOW_DIR.glob("*.md")):
        name = path.stem
        content = read_text(path)
        title = extract_title(content, name)
        description = extract_description(content, name)
        workflows.append(
            Workflow(
                name=name,
                title=title,
                description=description,
                path=path,
                has_source_command=(COMMAND_DIR / f"{name}.md").exists(),
                has_codex_skill=(CODEX_SKILL_DIR / f"source-command-{name}" / "SKILL.md").exists(),
                has_cold_codex_skill=(COLD_CODEX_SKILL_DIR / f"source-command-{name}" / "SKILL.md").exists(),
                domains=classify_domains(name, title, description),
            )
        )
    return workflows


def lookup_command_surface(name: str) -> CommandSurface:
    clean_name = name.strip().lstrip("/")
    archived = tuple(
        sorted(ARCHIVE_BRIDGE_DIR.glob(f"**/{clean_name}*.md"))
        + sorted(ARCHIVE_BRIDGE_DIR.glob(f"**/source-command-{clean_name}/SKILL.md"))
    )
    return CommandSurface(
        name=clean_name,
        workflow_path=WORKFLOW_DIR / f"{clean_name}.md",
        source_command_path=COMMAND_DIR / f"{clean_name}.md",
        hot_skill_path=CODEX_SKILL_DIR / f"source-command-{clean_name}" / "SKILL.md",
        cold_skill_path=COLD_CODEX_SKILL_DIR / f"source-command-{clean_name}" / "SKILL.md",
        archived_paths=archived,
    )


@lru_cache(maxsize=512)
def intent_flags(phrase: str) -> dict[str, bool]:
    """Cache query-level intent checks that otherwise repeat per workflow."""
    revenue = is_revenue_intent(phrase)
    system_failure = is_system_failure_intent(phrase)
    productized_ai_service_os = is_productized_ai_service_os_intent(phrase)
    diandra_linkedin_system = is_diandra_linkedin_system_query(phrase)
    return {
        "explicit_autopilot_invocation": is_explicit_autopilot_invocation(phrase),
        "autopilot": is_autopilot_query(phrase),
        "operating_alignment": is_operating_alignment_intent(phrase),
        "virtuoso": is_virtuoso_intent(phrase),
        "kishotenketsu_storytelling": is_kishotenketsu_storytelling_intent(phrase),
        "deep_research_os": is_deep_research_os_intent(phrase),
        "front_door_choice": is_front_door_choice_intent(phrase),
        "explicit_menu_backend": is_explicit_menu_backend_intent(phrase),
        "end_session_closeout": is_end_session_closeout_intent(phrase),
        "health_check": is_health_check_intent(phrase),
        "routing_intelligence": is_routing_intelligence_intent(phrase),
        "skill_anneal": is_skill_anneal_intent(phrase),
        "transfer_handoff": is_transfer_handoff_intent(phrase),
        "steering_compass": is_steering_compass_intent(phrase),
        "mission": is_mission_query(phrase),
        "vibe_tax_deployment": is_vibe_tax_deployment_query(phrase),
        "vibe_tax_result_writer": is_vibe_tax_result_writer_query(phrase),
        "vibe_tax_brief": is_vibe_tax_brief_query(phrase),
        "efficiency_benchmark": is_efficiency_benchmark_query(phrase),
        "creative_brief": is_creative_brief_query(phrase),
        "extraction_source": is_extraction_source_query(phrase),
        "extraction_governor": is_extraction_governor_intent(phrase),
        "plugin_readiness": is_plugin_readiness_query(phrase),
        "self_evolution": is_self_evolution_query(phrase),
        "knowledge_librarian": is_knowledge_librarian_query(phrase),
        "system_orchestration": is_system_orchestration_query(phrase),
        "repeatability": is_repeatability_intent(phrase),
        "system_audit": is_system_audit_query(phrase),
        "system_failure": system_failure,
        "skill_system": is_skill_system_intent(phrase),
        "expert_composition": is_expert_composition_intent(phrase),
        "revenue": revenue,
        "liam_linkedin_lead_magnet": is_liam_linkedin_lead_magnet_intent(phrase),
        "productized_ai_service_os": productized_ai_service_os,
        "ai_employee_os": is_ai_employee_os_intent(phrase),
        "diandra_linkedin_system": diandra_linkedin_system,
        "kdp_book_one": is_kdp_book_one_query(phrase),
        "publishable_copy": is_publishable_copy_query(phrase),
        "steering": is_steering_query(phrase),
        "video_context": is_video_context_query(phrase),
        "ai_carousel": is_ai_carousel_query(phrase),
        "farrice_content_os": is_farrice_content_os_query(phrase),
    }


def score_workflow(workflow: Workflow, query: str) -> int:
    query_terms = normalize_terms(query)
    if not query_terms:
        return 0

    name = workflow.name.lower()
    title = workflow.title.lower()
    description = workflow.description.lower()
    searchable = f"{name} {title} {description}"

    score = 0
    phrase = query.lower().strip()
    flags = intent_flags(phrase)
    if command_name_hit(name, phrase):
        score += 160
    if phrase and phrase in searchable:
        score += 6
    compact_phrase = re.sub(r"[^a-z0-9]", "", phrase)
    if workflow.name == "end-session" and compact_phrase in {"endsession", "sourcecommandendsession"}:
        score += 160
    if workflow.name == "autopilot" and flags["explicit_autopilot_invocation"] and not flags["revenue"]:
        score += 260
    if workflow.name == "autopilot" and flags["autopilot"]:
        score += 48
    if workflow.name == "buyer-trigger-os" and (
        "buyer-trigger-os" in phrase
        or "buyer trigger os" in phrase
        or "meg heckman" in phrase
        or "print on demand trigger audit" in phrase
        or "apparel buyer psychology" in phrase
        or "current buyer insights" in phrase
        or "buyer insight" in phrase and "trend" in phrase
        or "purchase intent research" in phrase
        or "social listening" in phrase and ("product" in phrase or "buyer" in phrase or "shirt" in phrase or "apparel" in phrase)
        or "trend-backed shirt" in phrase
        or "research-backed trigger audit" in phrase
        or "find buyer trends" in phrase
        or "buyer trends" in phrase and ("shirt" in phrase or "product" in phrase or "offer" in phrase)
        or "josh shirt purchase intent" in phrase
        or "mybpm streetwear design psychology" in phrase
        or "edm streetwear purchase intent" in phrase
        or "shirt purchase intent" in phrase
    ):
        score += 180
    if flags["operating_alignment"]:
        score += operating_alignment_route_bonus(workflow.name)
    if flags["virtuoso"]:
        score += virtuoso_route_bonus(workflow.name)
    if flags["kishotenketsu_storytelling"]:
        score += kishotenketsu_storytelling_route_bonus(workflow.name)
    if flags["deep_research_os"]:
        score += deep_research_os_route_bonus(workflow.name)
        if workflow.name == "autopilot":
            score -= 220
    if flags["front_door_choice"]:
        score += front_door_choice_route_bonus(workflow.name)
    if flags["explicit_menu_backend"]:
        score += menu_backend_route_bonus(workflow.name)
    if flags["end_session_closeout"]:
        score += end_session_route_bonus(workflow.name)
    if flags["health_check"]:
        score += health_check_route_bonus(workflow.name)
    if flags["routing_intelligence"]:
        score += routing_intelligence_route_bonus(workflow.name)
    if flags["skill_anneal"]:
        score += skill_anneal_route_bonus(workflow.name)
    if flags["transfer_handoff"]:
        score += handoff_route_bonus(workflow.name)
    if flags["steering_compass"]:
        score += steering_compass_route_bonus(workflow.name)
    if workflow.name == "mission" and flags["mission"]:
        score += 80
    vibe_tax_deployment = flags["vibe_tax_deployment"]
    if workflow.name == "vibe-tax-deploy" and vibe_tax_deployment:
        score += 220
    if workflow.name == "vibe-tax-result-writer" and flags["vibe_tax_result_writer"]:
        score += 260
    if workflow.name == "vibe-tax-brief" and flags["vibe_tax_brief"]:
        explicit_copy_gate_terms = ("publishable", "copy", "hook", "post", "linkedin")
        score += 40 if any(term in phrase for term in explicit_copy_gate_terms) else 180
        if flags["vibe_tax_result_writer"]:
            score -= 120
        if vibe_tax_deployment:
            score -= 80
    if workflow.name == "system-efficiency-benchmark" and flags["efficiency_benchmark"]:
        score += 125
    if flags["efficiency_benchmark"]:
        score += efficiency_benchmark_bonus(workflow.name)
    if flags["creative_brief"]:
        score += creative_brief_bonus(workflow.name)
    if flags["extraction_source"]:
        score += extraction_source_bonus(workflow.name)
    if flags["extraction_governor"]:
        score += extraction_governor_route_bonus(workflow.name)
    if flags["plugin_readiness"]:
        score += plugin_readiness_bonus(workflow.name)
    if flags["self_evolution"] and not flags["system_failure"]:
        score += self_evolution_bonus(workflow.name)
    if flags["knowledge_librarian"] and not flags["system_failure"]:
        score += knowledge_librarian_bonus(workflow.name)
    if flags["system_orchestration"]:
        score += system_orchestration_bonus(workflow.name)
        if workflow.name.startswith("fladlien-"):
            score -= 30
    repeatability_intent = flags["repeatability"]
    if repeatability_intent:
        score += repeatability_route_bonus(workflow.name)
    if flags["system_failure"] and not repeatability_intent:
        score += system_failure_route_bonus(workflow.name, phrase)
        if flags["system_audit"]:
            if workflow.name == "system-audit":
                score += 220
            elif workflow.name == "autopilot":
                score -= 180
            elif workflow.name not in CONTROL_PLANE_ROUTES:
                score -= 80
        elif workflow.name == "autopilot":
            score += 120
    if flags["skill_system"] and not flags["system_failure"]:
        score += skill_system_route_bonus(workflow.name)
    if flags["expert_composition"]:
        score += expert_composition_route_bonus(workflow.name)
    if flags["revenue"]:
        score += revenue_route_bonus(workflow.name)
        if workflow.name == "autopilot":
            score -= 170
    if flags["liam_linkedin_lead_magnet"]:
        score += liam_linkedin_lead_magnet_route_bonus(workflow.name)
    if flags["productized_ai_service_os"]:
        score += productized_ai_service_os_route_bonus(workflow.name)
    if flags["ai_employee_os"]:
        score += ai_employee_os_route_bonus(workflow.name)
    if flags["diandra_linkedin_system"]:
        score += diandra_linkedin_system_bonus(workflow.name)
    if flags["kdp_book_one"]:
        kdp_bonuses = {
            "kdp-engine": 360,
            "sean-dollwet-book-one-pilot": 300,
            "publishable-copy-gate": -220,
            "ocean-content-anti-slop": -80,
            "anti-slop-audit": -80,
        }
        score += kdp_bonuses.get(workflow.name, 0)
    if (
        workflow.name == "publishable-copy-gate"
        and flags["publishable_copy"]
        and not flags["kdp_book_one"]
        and not flags["productized_ai_service_os"]
        and not flags["diandra_linkedin_system"]
        and not flags["kishotenketsu_storytelling"]
    ):
        score += 140
    if workflow.name == "steering-compass" and flags["steering"]:
        score += 18
    if workflow.name == "video-context-ledger" and flags["video_context"]:
        score += 18
    if workflow.name == "ai-carousel-engine" and flags["ai_carousel"]:
        score += 18
    if flags["farrice_content_os"]:
        score += farrice_content_os_bonus(workflow.name)

    matched_terms = set()
    for term in query_terms:
        term_score = 0
        if term == name:
            term_score = max(term_score, 12)
        elif token_hit(term, name):
            term_score = max(term_score, 6)
        elif len(term) >= 4 and term in name:
            term_score = max(term_score, 5)
        if token_hit(term, title):
            term_score = max(term_score, 3)
        elif len(term) >= 4 and term in title:
            term_score = max(term_score, 2)
        if token_hit(term, description):
            term_score = max(term_score, 2)
        elif len(term) >= 4 and term in description:
            term_score = max(term_score, 1)

        if term_score:
            matched_terms.add(term)
            score += term_score

    score += len(matched_terms) * 5

    return score


def is_steering_query(query: str) -> bool:
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


def is_vibe_tax_brief_query(query: str) -> bool:
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


def is_vibe_tax_result_writer_query(query: str) -> bool:
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


def is_vibe_tax_deployment_query(query: str) -> bool:
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


def is_autopilot_query(query: str) -> bool:
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
        "verify intent",
        "raw thoughts",
        "raw notes",
        "raw context",
        "messy idea",
        "messy context",
        "figure out what to do",
        "gateway command",
        "gateway to my workflow",
        "full arsenal",
        "ambiguity before execution",
        "before executing",
        "what should i do with this",
        "what should this become",
        "should this become",
        "decide what to work on",
        "what to work on today",
        "help me figure out",
        "plan and execute",
        "verify my intent",
        "intent then execute",
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
        ("raw" in query and ("execute" in query or "plan" in query))
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


def is_explicit_autopilot_invocation(query: str) -> bool:
    compact = re.sub(r"[^a-z0-9]", "", query.lower())
    if compact in {"autopilot", "sourcecommandautopilot"}:
        return True
    return bool(re.match(r"\s*/?(source[- ]command[- ])?autopilot\b", query.lower()))


def is_mission_query(query: str) -> bool:
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


def is_diandra_linkedin_system_query(query: str) -> bool:
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


def is_farrice_content_os_query(query: str) -> bool:
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


def farrice_content_os_bonus(workflow_name: str) -> int:
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


def diandra_linkedin_system_bonus(workflow_name: str) -> int:
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


def is_kdp_book_one_query(query: str) -> bool:
    """Detect a first-book or AI-ebook request owned by the KDP conductor."""
    direct_phrases = (
        "amazon kdp",
        "kindle direct publishing",
        "first kdp book",
        "kdp book from scratch",
        "first book on amazon",
        "ai ebook that is not slop",
        "ai ebook without slop",
        "book under a pen name",
        "ebook under a pen name",
    )
    if any(phrase in query for phrase in direct_phrases):
        return True
    platform = any(term in query for term in ("amazon", "kdp", "kindle"))
    book = any(term in query for term in ("book", "ebook", "paperback"))
    coldstart = any(term in query for term in ("first", "from scratch", "pen name", "without ads", "no ads"))
    return platform and book and coldstart


def is_publishable_copy_query(query: str) -> bool:
    """Detect public/revenue copy that should surface the publishable copy gate."""
    if is_kdp_book_one_query(query):
        return False

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


def is_creative_brief_query(query: str) -> bool:
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


def creative_brief_bonus(workflow_name: str) -> int:
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


def is_system_orchestration_query(query: str) -> bool:
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


def is_efficiency_benchmark_query(query: str) -> bool:
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


def efficiency_benchmark_bonus(workflow_name: str) -> int:
    bonuses = {
        "system-efficiency-benchmark": 225,
        "bloat-optimizer": 195,
        "context-audit": 150,
        "system-hygiene": 130,
        "routing-intelligence": 115,
        "expert-composition-governor": -220,
    }
    return bonuses.get(workflow_name, 0)


def is_extraction_source_query(query: str) -> bool:
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


def extraction_source_bonus(workflow_name: str) -> int:
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


def is_plugin_readiness_query(query: str) -> bool:
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


def plugin_readiness_bonus(workflow_name: str) -> int:
    bonuses = {
        "plugin-readiness-audit": 150,
        "system-efficiency-benchmark": 40,
        "knowledge-librarian": 25,
    }
    return bonuses.get(workflow_name, 0)


def is_self_evolution_query(query: str) -> bool:
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


def self_evolution_bonus(workflow_name: str) -> int:
    bonuses = {
        "self-evolve": 145,
        "routing-intelligence": 85,
        "skill-anneal": 45,
        "system-efficiency-benchmark": 35,
        "knowledge-librarian": 25,
    }
    return bonuses.get(workflow_name, 0)


def is_knowledge_librarian_query(query: str) -> bool:
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


def knowledge_librarian_bonus(workflow_name: str) -> int:
    bonuses = {
        "knowledge-librarian": 180,
        "knowledge-search": 35,
        "compile-knowledge": 30,
        "context-audit": 15,
        "end-session": -45,
        "session-kickoff": -25,
    }
    return bonuses.get(workflow_name, 0)


def system_orchestration_bonus(workflow_name: str) -> int:
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


def is_video_context_query(query: str) -> bool:
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


def is_ai_carousel_query(query: str) -> bool:
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


def normalize_terms(query: str) -> list[str]:
    return [
        term
        for term in re.findall(r"[a-z0-9][a-z0-9-]+", query.lower())
        if len(term) > 2 and term not in STOPWORDS
    ]


def search(workflows: Iterable[Workflow], query: str, limit: int) -> list[tuple[int, Workflow]]:
    phrase = query.lower().strip()
    flags = intent_flags(phrase)
    binding_hits = match_bindings(query)
    control_plane_active = any(
        flags[key]
        for key in (
            "explicit_autopilot_invocation",
            "autopilot",
            "operating_alignment",
            "virtuoso",
            "deep_research_os",
            "front_door_choice",
            "explicit_menu_backend",
            "end_session_closeout",
            "health_check",
            "routing_intelligence",
            "skill_anneal",
            "transfer_handoff",
            "steering_compass",
            "mission",
            "extraction_governor",
            "self_evolution",
            "knowledge_librarian",
            "system_orchestration",
            "repeatability",
            "system_audit",
            "system_failure",
            "skill_system",
            "expert_composition",
            "revenue",
            "ai_employee_os",
        )
    )
    # "Run the search workflows" is ordinary operator language in a search
    # prototype request, but the generic system-orchestration detector also
    # sees the word "workflows". Let the narrowly matched Search Content
    # Mastery binding survive that one weak control-plane signal while keeping
    # explicit Autopilot, audit, mission, handoff, and other control intents in
    # charge.
    search_mastery_hit = any(
        hit.get("binding_id") == "operator_search_content_mastery"
        for hit in binding_hits
    )
    strong_control_plane_active = any(
        flags[key]
        for key in (
            "explicit_autopilot_invocation",
            "autopilot",
            "operating_alignment",
            "virtuoso",
            "deep_research_os",
            "front_door_choice",
            "explicit_menu_backend",
            "end_session_closeout",
            "health_check",
            "routing_intelligence",
            "skill_anneal",
            "transfer_handoff",
            "steering_compass",
            "mission",
            "extraction_governor",
            "self_evolution",
            "knowledge_librarian",
            "repeatability",
            "system_audit",
            "system_failure",
            "skill_system",
            "expert_composition",
            "ai_employee_os",
        )
    )
    binding_boost: dict[str, int] = {}
    if not control_plane_active or (search_mastery_hit and not strong_control_plane_active):
        for position, hit in enumerate(binding_hits):
            for subposition, workflow_name in enumerate(hit.get("workflows", [])):
                binding_boost.setdefault(
                    str(workflow_name),
                    50_000 - position * 200 - subposition * 50,
                )

    scored = [
        (score_workflow(workflow, query) + binding_boost.get(workflow.name, 0), workflow)
        for workflow in workflows
    ]
    matches = [(score, workflow) for score, workflow in scored if score > 0]
    matches.sort(key=lambda item: (-item[0], item[1].name))
    return matches[:limit]


def domain_matches(workflows: Iterable[Workflow], domain: str) -> list[Workflow]:
    domain = domain.lower().strip()
    aliases = {config["label"].lower(): key for key, config in DOMAIN_MAP.items()}
    domain = aliases.get(domain, domain)
    if domain not in DOMAIN_MAP and domain != "other":
        keyword_hits = [
            workflow
            for workflow in workflows
            if domain in workflow.name.lower() or domain in workflow.description.lower()
        ]
        return sorted(keyword_hits, key=lambda workflow: workflow.name)

    if domain == "other":
        return sorted(
            [workflow for workflow in workflows if "other" in workflow.domains],
            key=lambda workflow: workflow.name,
        )

    keywords = DOMAIN_MAP[domain]["keywords"]
    scored = []
    for workflow in workflows:
        haystack = f"{workflow.name} {workflow.title} {workflow.description}".lower()
        score = domain_score(workflow.name.lower(), haystack, keywords)
        if score:
            scored.append((score, workflow))

    scored.sort(key=lambda item: (-item[0], item[1].name))
    return [workflow for _, workflow in scored]


def render_overview(workflows: list[Workflow]) -> str:
    lines = ["# Command Menu", ""]
    lines.append(f"Indexed {len(workflows)} workflows from `.agent/workflows/`.")
    lines.append("")
    lines.append("## Domains")

    for domain, config in DOMAIN_MAP.items():
        count = sum(1 for workflow in workflows if domain in workflow.domains)
        lines.append(f"- `{domain}` — {config['label']} ({count})")

    other_count = sum(1 for workflow in workflows if "other" in workflow.domains)
    lines.append(f"- `other` — Unclassified ({other_count})")
    lines.append("")
    lines.append("## Usage")
    lines.append("- `python3 execution/command_menu.py search \"client acquisition\"`")
    lines.append("- `python3 execution/command_menu.py domain copy`")
    lines.append("- `python3 execution/command_menu.py show deep-research`")
    return "\n".join(lines)


def render_menu(matches: list[tuple[int, Workflow]], query: str) -> str:
    if not matches:
        return f"No workflows matched `{query}`. Try a broader goal or run the overview."

    lines = [f"# Command Menu: {query}", ""]
    if is_front_door_choice_intent(query):
        lines.extend(
            [
                "Routing Governor: front-door choice intent detected. /autopilot is promoted first so the system chooses the right route before exposing a broad menu.",
                "",
            ]
        )
    elif is_explicit_menu_backend_intent(query):
        lines.extend(
            [
                "Routing Governor: explicit menu/options intent detected. /orchestrate remains the ranked-options backend.",
                "",
            ]
        )
    elif is_revenue_intent(query):
        lines.extend(
            [
                "Routing Governor: revenue intent detected. Concrete acquisition, paid-audit, proof, and delivery routes are promoted above generic strategy.",
                "",
            ]
        )
    for index, (score, workflow) in enumerate(matches, 1):
        lines.extend(render_workflow_option(index, workflow, score=score))
    lines.append("## Next")
    lines.append("Reply with the number or command name to run it, or ask for alternatives in a narrower domain.")
    return "\n".join(lines)


def render_domain(workflows: list[Workflow], domain: str, limit: Optional[int]) -> str:
    matches = domain_matches(workflows, domain)
    if limit:
        matches = matches[:limit]

    label = DOMAIN_MAP.get(domain, {}).get("label", domain.replace("-", " ").title())
    lines = [f"# {label}", ""]
    lines.append(f"{len(matches)} workflows shown.")
    lines.append("")
    for index, workflow in enumerate(matches, 1):
        lines.extend(render_workflow_option(index, workflow))
    return "\n".join(lines)


def render_workflow_option(index: int, workflow: Workflow, score: Optional[int] = None) -> list[str]:
    score_text = f" | score {score}" if score is not None else ""
    domains = ", ".join(workflow.domains)
    return [
        f"{index}. `/{workflow.name}`{score_text}",
        f"   {workflow.description}",
        f"   Domains: {domains} | Status: {bridge_status(workflow)}",
        "",
    ]


def render_show(workflows: list[Workflow], name: str) -> str:
    clean_name = name.strip().lstrip("/")
    surface = lookup_command_surface(clean_name)
    match = next((workflow for workflow in workflows if workflow.name == clean_name), None)
    if not match and surface.execution_status != "unknown-command":
        text = read_text(surface.source_command_path)
        if not text and surface.archived_paths:
            text = read_text(surface.archived_paths[0])
        lines = [f"# /{clean_name}", ""]
        lines.append(extract_description(text, clean_name))
        lines.append("")
        lines.append(f"- Execution status: {surface.execution_status}")
        lines.append(f"- Workflow: `{relative(surface.workflow_path)}`" if surface.has_workflow else f"- Workflow: missing `{relative(surface.workflow_path)}`")
        lines.append(f"- Source command: `{relative(surface.source_command_path)}`" if surface.has_source_command else "- Source command: absent")
        lines.append(f"- Hot Codex skill: `{relative(surface.hot_skill_path)}`" if surface.has_hot_skill else "- Hot Codex skill: absent")
        lines.append(f"- Cold Codex wrapper: `{relative(surface.cold_skill_path)}`" if surface.has_cold_skill else "- Cold Codex wrapper: absent")
        if surface.archived_paths:
            archived = ", ".join(f"`{relative(path)}`" for path in surface.archived_paths[:4])
            lines.append(f"- Archived evidence: {archived}")
        lines.append("- Domains: legacy")
        lines.append("- Invocation: unavailable")
        lines.append(f"- Repair note: restore `{relative(surface.workflow_path)}` or archive the stale bridge artifacts.")
        return "\n".join(lines)

    if not match:
        matches = search(workflows, clean_name, 5)
        return render_menu(matches, clean_name)

    lines = [f"# /{match.name}", ""]
    lines.append(match.description)
    lines.append("")
    lines.append(f"- Execution status: {bridge_status(match)}")
    lines.append(f"- Workflow: `{relative(match.path)}`")
    lines.append(f"- Source command: `{relative(COMMAND_DIR / f'{match.name}.md')}`" if match.has_source_command else "- Source command: absent")
    lines.append(f"- Hot Codex skill: `{relative(CODEX_SKILL_DIR / f'source-command-{match.name}' / 'SKILL.md')}`" if match.has_codex_skill else "- Hot Codex skill: absent")
    lines.append(f"- Cold Codex wrapper: `{relative(COLD_CODEX_SKILL_DIR / f'source-command-{match.name}' / 'SKILL.md')}`" if match.has_cold_codex_skill else "- Cold Codex wrapper: absent")
    lines.append(f"- Domains: {', '.join(match.domains)}")
    if bridge_status(match) == "workflow-only":
        lines.append(f"- Invocation: `/{match.name} [your context]` via workflow menu; no source-command bridge is installed.")
    else:
        lines.append(f"- Invocation: `/{match.name} [your context]`")
    return "\n".join(lines)


def log_routing_choice(query: str, matches: list[tuple[int, Workflow]], source: str = "command-menu") -> Optional[str]:
    """Log the top matched workflow when a caller opts into routing evidence."""
    if not matches:
        return None
    score, workflow = matches[0]
    try:
        from routing_intelligence import log_routing_decision

        intent_score = max(1, min(5, round(score / 8)))
        return log_routing_decision(
            request_summary=query,
            intent_score=intent_score,
            domain_detected=workflow.domains[0] if workflow.domains else "unknown",
            experts_deployed=["antigravity-orchestrator"],
            tier_loaded=1,
            mode="output",
            workflow_used=workflow.name,
            session_id=source,
        )
    except Exception:
        return None


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Browse and search Antigravity slash-command workflows.")
    sub = parser.add_subparsers(dest="command")

    search_parser = sub.add_parser("search", help="Search workflows by goal or keyword.")
    search_parser.add_argument("query", help="Goal, domain, or keyword to search.")
    search_parser.add_argument("-n", "--limit", type=int, default=8, help="Number of results to show.")
    search_parser.add_argument("--log-routing", action="store_true", help="Log the top matched workflow as routing evidence.")

    domain_parser = sub.add_parser("domain", help="Show workflows in a domain.")
    domain_parser.add_argument("domain", help="Domain key, label, or keyword.")
    domain_parser.add_argument("-n", "--limit", type=int, default=25, help="Number of results to show.")

    show_parser = sub.add_parser("show", help="Show one workflow's bridge details.")
    show_parser.add_argument("name", help="Workflow or slash command name.")

    args = parser.parse_args()
    workflows = build_index()

    if args.command == "search":
        matches = search(workflows, args.query, args.limit)
        routing_id = log_routing_choice(args.query, matches) if args.log_routing else None
        print(render_menu(matches, args.query))
        if routing_id:
            print(f"\nRouting logged: {routing_id}")
        return 0

    if args.command == "domain":
        print(render_domain(workflows, args.domain, args.limit))
        return 0

    if args.command == "show":
        print(render_show(workflows, args.name))
        return 0

    print(render_overview(workflows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
