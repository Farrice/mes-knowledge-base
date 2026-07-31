#!/usr/bin/env python3
"""Routing Governor — intent-aware guardrail for Antigravity routing.

This is an additive layer over command_menu.py and workflow_router.py. It does
not replace either router; it detects high-risk intent classes where raw
keyword rank is likely to be misleading, then explains the route that should
win and the routes that should be treated as noise.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]

REVENUE_STACK = (
    "first-10k",
    "revenue-offer-agent",
    "client-acquire",
    "zero-to-client-sprint",
    "service-first-productization",
)

REVENUE_SUPPORT_ROUTES = (
    "publishable-copy-gate",
    "cash-method",
    "24-assets-client-audit",
    "24-assets-productized-service",
    "cold-outreach-gen",
    "cold-to-close-proof-funnel",
    "draft-proposal",
    "blue-chip-client",
    "ash-offer-test",
)

PRODUCTIZED_AI_SERVICE_OS_STACK = (
    "productized-ai-service-os",
    "service-first-productization",
    "revenue-offer-agent",
    "24-assets-productized-service",
    "client-delivery-agent",
    "ash-productized-validation",
    "publishable-copy-gate",
)

PRODUCTIZED_AI_SERVICE_OS_SIGNALS = (
    "/productized-ai-service-os",
    "productized-ai-service-os",
    "productized ai service os",
    "productized service os",
    "ai service os",
    "designjoy service os",
    "designjoy-style",
    "ai slop cleanup productized service",
    "slop cleanup productized service",
    "productized ai service",
    "productized service",
    "no-call intake",
    "no call intake",
    "production queue",
    "pause subscription",
    "pause/cancel",
    "pause cancel",
    "client handoff",
    "proof sprint",
)

AI_EMPLOYEE_OS_STACK = (
    "ai-employee-os",
    "context-audit",
    "memory-architect",
    "conde-agent-experience-design",
    "24-assets-agent-system-design",
    "harness-audit",
)

AI_EMPLOYEE_OS_SIGNALS = (
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
)

REVENUE_SIGNALS = (
    "make income",
    "make money",
    "earn money",
    "fast cash",
    "urgent cash",
    "cash",
    "income",
    "revenue",
    "monetize",
    "paid audit",
    "paid sprint",
    "first client",
    "paying client",
    "client acquisition",
    "get clients",
    "land clients",
    "book calls",
    "side project",
    "first $",
    "$500",
    "$1k",
    "$1000",
    "24-48",
    "48 hour",
    "48-hour",
)

SKILL_SYSTEM_STACK = (
    "source-to-skill-system",
    "extraction-governor-agent",
    "mission",
    "autopilot",
    "self-evolve",
    "skill-anneal",
)

KISHOTENKETSU_STORYTELLING_STACK = (
    "kishotenketsu-contrast-storytelling",
    "high-taste-writing-os",
    "publishable-copy-gate",
    "messaging-positioning-agent",
    "positioning-message-bridge",
    "new-media-ghostwriting",
)

SKILL_SYSTEM_SIGNALS = (
    "skill system",
    "skill systems",
    "source-to-skill",
    "source to skill",
    "source-to-system",
    "source to system",
    "make skills make sense",
    "10x skills",
    "10 times better",
    "end-to-end source extraction",
    "end to end source extraction",
    "end-to-end workflow",
    "end to end workflow",
    "orchestrator skill",
    "skill orchestration",
    "codex orchestration",
    "component skills",
    "connected codex skill system",
    "connected skill system",
    "connected skill systems",
    "companion os layer",
    "companion os",
    "workflow bridge",
    "validation loop",
    "co-creative launchpad os",
    "co creative launchpad os",
    "co-creative launchpad contract",
    "co creative launchpad contract",
    "turn this video into",
    "turn this transcript into",
    "from this transcript",
    "isolated skills",
    "mega skill",
    "mega-skill",
    "mega skills",
    "mega-skills",
    "hot cold skills",
    "hot/cold skills",
    "skill handoffs",
    "agentic engineering",
    "agent-engineering",
    "agent engineering",
    "context engineering",
    "source truth",
    "source-code-as-truth",
    "review-until-stop",
    "review until stop",
    "small pr",
    "small prs",
    "dependency safety",
    "package safety",
)

EXTRACTION_GOVERNOR_STACK = (
    "extraction-governor-agent",
    "source-to-skill-system",
    "knowledge-librarian",
    "plugin-readiness-audit",
    "autopilot",
    "orchestrate",
)

EXTRACTION_GOVERNOR_SIGNALS = (
    "/extraction-governor-agent",
    "source-command-extraction-governor-agent",
    "source command extraction governor agent",
    "extraction governor",
    "extraction-governor",
    "extraction governance",
    "source triage",
    "source-to-capability",
    "source to capability",
    "route this source",
    "classify build shape",
    "build-shape decision",
    "build shape decision",
    "hidden mechanics",
    "extract hidden mechanics",
    "extract the mechanics",
    "duplicate-system avoidance",
    "duplicate system avoidance",
    "avoid duplicate systems",
    "avoid duplicate workflows",
    "decide whether source material should become",
)

MARK_OPERATING_TREE_STACK = (
    "source-to-skill-system",
    "self-evolve",
    "skill-anneal",
    "extraction-governor-agent",
    "silver-platter",
    "orchestrate",
)

MARK_OPERATING_TREE_REFERENCE = "semantic_libraries/antigravity/references/mark-kashef-operating-tree.md"

MARK_OPERATING_TREE_MARK_SIGNALS = (
    "mark kashef",
    "mark-kashef",
    "kashef",
)

MARK_OPERATING_TREE_SYSTEM_SIGNALS = (
    "self-improving workflow",
    "self improving workflow",
    "self-improving workflows",
    "self improving workflows",
    "self-improving system",
    "self improving system",
    "operating tree",
    "routing composition",
    "source-to-system",
    "source to system",
    "source-to-skill",
    "source to skill",
    "skill system",
    "skill orchestration",
)

MARK_OPERATING_TREE_VISUAL_ONLY_TERMS = (
    "banana",
    "image",
    "images",
    "visual",
    "wireframe",
    "wireframes",
    "sketch",
)

LIAM_LINKEDIN_LEAD_MAGNET_STACK = (
    "liam-linkedin-lead-magnet",
    "bank-lead-magnet",
    "diandra-linkedin-system",
    "profile-conversion",
    "diandra-first-50",
    "publishable-copy-gate",
)

LIAM_LINKEDIN_LEAD_MAGNET_CONTEXT_TERMS = (
    "ai",
    "personal brand",
    "personal-brand",
    "first 20",
    "20 posts",
    "post sprint",
    "first sprint",
    "monetizable expertise",
    "strategic arbitrage",
    "hook",
    "rehook",
    "content engine",
    "inbound",
    "lead magnet",
    "offer bridge",
)

EXPERT_COMPOSITION_STACK = (
    "expert-composition-governor",
    "autopilot",
    "orchestrate",
    "mission",
    "source-to-skill-system",
    "self-evolve",
)

EXPERT_COMPOSITION_SIGNALS = (
    "expert soup",
    "too many experts",
    "too many agents",
    "too many skills",
    "not interwoven",
    "not woven together",
    "hammer instead of scalpel",
    "full arsenal",
    "true end-to-end access",
    "true end to end access",
    "compose experts",
    "compose expert",
    "expert composition",
    "expert stack",
    "stacking experts",
    "many experts",
    "many skills",
    "many workflows",
)

EXPERT_COMPOSITION_CONTEXT_TERMS = (
    "expert",
    "experts",
    "agent",
    "agents",
    "skill",
    "skills",
    "workflow",
    "workflows",
    "arsenal",
    "stack",
    "stacking",
    "compose",
    "composition",
    "interwoven",
    "scalpel",
    "soup",
)

VIRTUOSO_STACK = (
    "virtuoso",
    "autopilot",
    "expert-composition-governor",
    "orchestrate",
    "routing-intelligence",
    "health-check",
)

VIRTUOSO_SIGNALS = (
    "/virtuoso",
    "source-command-virtuoso",
    "source command virtuoso",
    "virtuoso orchestration",
    "deploy virtuoso",
    "deploy the full harness",
    "deploy full harness",
    "deploy the full system",
    "full-system excellence",
    "full system excellence",
    "solo orchestration",
    "virtual solo orchestration",
    "use the full arsenal",
    "use full arsenal",
    "full harness orchestration",
    "one command orchestration",
    "deploy at will",
)

DEEP_RESEARCH_OS_STACK = (
    "deep-research-os",
    "research-intelligence-agent",
    "deep-research",
    "research-swarm",
    "parallel-research",
    "competitor-intel",
    "icp-deep-dive",
)

DEEP_RESEARCH_OS_SIGNALS = (
    "/deep-research-os",
    "source-command-deep-research-os",
    "source command deep research os",
    "deep research os",
    "ultimate research",
    "ultimate deep research",
    "research os",
    "research command package",
    "research package",
    "wide research",
    "widespread research",
    "manus wide research",
    "perplexity deep research",
    "kimi deep research",
    "kimi ai research",
    "chatgpt deep research",
    "gemini deep research",
    "deep research swarm",
    "latest market research",
    "current market research",
    "current competitors",
    "social listening",
    "anti-hallucination research",
    "anti hallucination research",
    "source-backed research",
    "source backed research",
    "market intelligence",
    "offer-market fit research",
    "offer market fit research",
    "product-market fit research",
    "product market fit research",
    "pmf research",
    "omf research",
    "icp deep canvassing",
    "deep canvassing research",
)

FRONT_DOOR_CHOICE_STACK = (
    "autopilot",
    "orchestrate",
    "command-menu",
    "routing-intelligence",
    "knowledge-librarian",
    "mission",
)

MENU_BACKEND_STACK = (
    "orchestrate",
    "command-menu",
    "autopilot",
    "routing-intelligence",
    "mission",
)

END_SESSION_STACK = (
    "end-session",
    "autopilot",
    "routing-intelligence",
    "health-check",
    "mission",
)

HEALTH_CHECK_STACK = (
    "health-check",
    "routing-intelligence",
    "system-audit",
    "autopilot",
    "mission",
)

ROUTING_INTELLIGENCE_STACK = (
    "routing-intelligence",
    "health-check",
    "system-audit",
    "autopilot",
    "orchestrate",
)

KNOWLEDGE_LIBRARIAN_STACK = (
    "knowledge-librarian",
    "autopilot",
    "command-menu",
    "routing-intelligence",
    "orchestrate",
)

SELF_EVOLVE_STACK = (
    "self-evolve",
    "routing-intelligence",
    "skill-anneal",
    "repeatability-spine",
    "system-audit",
    "autopilot",
)

SKILL_ANNEAL_STACK = (
    "skill-anneal",
    "self-evolve",
    "repeatability-spine",
    "routing-intelligence",
    "system-audit",
    "autopilot",
)

FRONT_DOOR_CHOICE_SIGNALS = (
    "too many tools and don't know what to use",
    "too many tools and dont know what to use",
    "too many tools and do not know what to use",
    "don't know what to use",
    "dont know what to use",
    "do not know what to use",
    "not sure what to use",
    "unsure what to use",
    "what should i use next",
    "what should i use",
    "which tool should i use",
    "which tools should i use",
    "what tool should i use",
    "what tools should i use",
    "which command should i use",
    "what command should i use",
    "what command should i run",
    "which workflow should i use",
    "what workflow should i use",
    "which route should i use",
    "what route should i use",
    "pick the right tool",
    "pick the right command",
    "pick the right workflow",
    "choose the right tool",
    "choose the right command",
    "choose the right workflow",
    "co-creative launchpad",
    "co creative launchpad",
    "cocreative launchpad",
    "launching pad before build",
    "apex before build",
    "raw intent",
    "better questions",
    "intent alignment before execution",
    "align intent before execution",
    "senior partner before execution",
    "what good looks like before execution",
)

MENU_BACKEND_SIGNALS = (
    "/orchestrate",
    "source-command-orchestrate",
    "source command orchestrate",
    "orchestrate execution menu",
    "show me the menu",
    "show the menu",
    "give me the menu",
    "open the menu",
    "execution menu",
    "ranked options",
    "ranked paths",
    "rank paths",
    "menu of options",
    "options menu",
    "show me options",
    "show options",
    "list options",
    "browse options",
    "show commands",
    "list commands",
    "browse commands",
    "command menu",
    "workflow menu",
)

END_SESSION_SIGNALS = (
    "/end-session",
    "source-command-end-session",
    "source command end session",
    "end session",
    "end-session",
    "endsession",
    "session closeout",
    "session close-out",
    "closeout intelligence",
    "closeout",
    "close out",
    "wrap this session",
    "wrap up this session",
    "session wrap",
    "handoff closeout",
    "handoff close-out",
)

END_SESSION_CONTEXT_TERMS = (
    "session",
    "closeout",
    "close-out",
    "close",
    "wrap",
    "handoff",
    "intelligence",
    "receipt",
    "status",
)

HEALTH_CHECK_SIGNALS = (
    "/health-check",
    "source-command-health-check",
    "source command health check",
    "health-check",
    "health check",
    "harness status",
    "run harness status",
    "show harness status",
    "system status",
    "system health",
    "status surface",
    "what is working stale broken",
    "what is working, stale, or broken",
)

ROUTING_INTELLIGENCE_SIGNALS = (
    "/routing-intelligence",
    "source-command-routing-intelligence",
    "source command routing intelligence",
    "routing-intelligence",
    "routing intelligence",
    "routing analytics",
    "routing dashboard",
    "routing scoreboard",
    "show routing scoreboard",
    "route scoreboard",
    "route analytics",
    "route feedback",
    "expert utilization",
    "domain distribution",
    "top combos",
    "underperforming routes",
    "unused experts",
)

ROUTING_INTELLIGENCE_CONTEXT_TERMS = (
    "routing",
    "route",
    "scoreboard",
    "analytics",
    "dashboard",
    "feedback",
    "utilization",
    "underperforming",
)

KNOWLEDGE_LIBRARIAN_SIGNALS = (
    "/knowledge-librarian",
    "source-command-knowledge-librarian",
    "source command knowledge librarian",
    "knowledge-librarian",
    "knowledge librarian",
    "knowledge library",
    "library pulse",
    "session start pulse",
    "session-start knowledge pulse",
    "prior decisions",
    "previous decisions",
    "reusable context",
    "prior reusable solution docs",
    "solution docs",
    "underused workflows",
    "underused skills",
    "sleeping giants",
    "one exact start command",
    "start command from the library",
    "what knowledge",
    "what workflows",
)

SELF_EVOLVE_SIGNALS = (
    "/self-evolve",
    "source-command-self-evolve",
    "source command self evolve",
    "self-evolve",
    "self evolve",
    "self evolution",
    "improve workflow with feedback",
    "improve a workflow",
    "improve this workflow",
    "evolve workflow",
    "evolve this workflow",
    "failure history",
    "performance logs",
    "regression-aware evolution",
    "regression aware evolution",
    "measured evolution",
    "recurring mistakes",
    "without adding unnecessary bloat",
)

SKILL_ANNEAL_SIGNALS = (
    "/skill-anneal",
    "source-command-skill-anneal",
    "source command skill anneal",
    "skill-anneal",
    "skill anneal",
    "anneal skill",
    "anneal this skill",
    "self-annealing",
    "self annealing",
    "improve this skill prompt",
    "improve skill prompt",
    "skill prompt",
    "skill's prompts",
    "specific skill",
    "rubric.md",
    "test_inputs.md",
)

HEALTH_CHECK_CONTEXT_TERMS = (
    "health",
    "status",
    "harness",
    "system",
    "working",
    "stale",
    "activation",
    "readiness",
)

STEERING_COMPASS_STACK = (
    "steering-compass",
    "autopilot",
    "end-session",
    "source-to-skill-system",
    "skill-anneal",
    "routing-intelligence",
    "mission",
)

HANDOFF_STACK = (
    "handoff",
    "end-session",
    "steering-compass",
    "autopilot",
    "source-to-skill-system",
    "mission",
)

REPEATABILITY_STACK = (
    "repeatability-spine",
    "autopilot",
    "system-audit",
    "publishable-copy-gate",
    "self-evolve",
    "skill-anneal",
    "routing-intelligence",
    "health-check",
    "mission",
    "orchestrate",
)

COPY_QUALITY_STACK = (
    "mission",
    "red-team-agent",
    "five-input-content-gate",
    "publishable-copy-gate",
    "copywriting-agent",
    "excellence-gate",
)

COPY_QUALITY_SIGNALS = (
    "copy gate",
    "publishable-copy-gate",
    "publishable copy gate",
    "ceremonial pass",
    "ceremonial",
    "over-scored",
    "overscored",
    "inflated score",
    "score inflation",
    "scored as 9",
    "rated 3",
    "rated 4",
    "user rates",
    "i rate it",
    "generic",
    "flat",
    "weak hook",
    "no tension",
    "doesn't have tension",
    "does not have tension",
    "hook is weak",
)

REPEATABILITY_SIGNALS = (
    "cannot repeat the magic",
    "can't repeat the magic",
    "repeat the magic",
    "not able to repeat it",
    "unable to repeat it",
    "not repeatable",
    "can't reproduce",
    "cannot reproduce",
    "revision failure",
    "revision failures",
    "revisions keep failing",
    "multiple revision failure points",
    "revision got worse",
    "rewrite got worse",
    "got worse",
    "lost the good part",
    "lost what worked",
    "lost the magic",
    "revision got flat",
    "rewrite got flat",
    "got flat",
    "preserve what made this work",
    "preserve what worked",
    "preserve the good part",
    "system chose the wrong route",
    "route picked the wrong workflow",
    "wrong workflow",
    "wrong route",
    "patch introduced a regression",
    "introduced a regression",
    "caused a regression",
)

REPEATABILITY_CONTEXT_TERMS = (
    "revision",
    "revisions",
    "rewrite",
    "draft",
    "output",
    "outputs",
    "route",
    "workflow",
    "patch",
    "regression",
    "magic",
    "repeat",
    "reproduce",
    "preserve",
)

SYSTEM_FAILURE_STACK = (
    "autopilot",
    "system-audit",
    "routing-intelligence",
    "health-check",
    "mission",
    "orchestrate",
    "self-evolve",
    "skill-anneal",
)

SYSTEM_AUDIT_FIRST_STACK = (
    "system-audit",
    "autopilot",
    "routing-intelligence",
    "health-check",
    "mission",
    "orchestrate",
    "self-evolve",
    "skill-anneal",
)

OPERATING_ALIGNMENT_STACK = (
    "system-audit",
    "autopilot",
    "virtuoso",
    "expert-composition-governor",
    "routing-intelligence",
    "health-check",
    "repeatability-spine",
    "self-evolve",
    "skill-anneal",
    "artifact-router",
)

OPERATING_ALIGNMENT_SIGNALS = (
    "operating alignment",
    "operating layer",
    "unified codex",
    "codex operating",
    "works globally",
    "work globally",
    "global and workspace",
    "global workflows",
    "global skills",
    "source skills",
    "slash commands",
    "proper orchestration",
    "orchestration layer",
    "multiple experts",
    "console of experts",
    "real experts",
    "subagents",
    "sub-agents",
    "maximum firepower",
    "output consistency",
    "level of genius",
    "not tapping into",
    "completely ineffective",
    "spending so much time",
    "correcting things",
    "self-improving",
    "self improving",
    "automations",
    "global no matter where",
    "disjointed",
    "magic moments",
    "magic preservation",
    "proper orchestration and layers",
)

CAPABILITY_STEWARDSHIP_SIGNALS = (
    "capability stewardship",
    "capability awareness",
    "capabilities you can use",
    "context-container judgment",
    "context container judgment",
    "bounded expert orchestration",
    "proactive leverage surfacing",
    "leverage surfacing",
    "capability recommendation",
    "capability recommendations",
)

CAPABILITY_STEWARDSHIP_LIFECYCLE_TERMS = (
    "session start",
    "start of session",
    "at the start",
    "mid-session",
    "mid session",
    "in the middle",
    "middle of the session",
    "session closeout",
    "at closeout",
    "at the end",
    "start, middle, and end",
    "start middle and end",
    "session lifecycle",
    "throughout the session",
)

CAPABILITY_STEWARDSHIP_DEFAULT_TERMS = (
    "persistent default",
    "persistent behavior",
    "persistent companion",
    "by default",
    "without magic words",
    "without requiring magic words",
    "without a command",
    "without commands",
    "automatically",
)

OPERATOR_COCKPIT_REBUILD_SIGNALS = (
    "operator cockpit",
    "cockpit-first",
    "cockpit first",
    "v2 operating cockpit",
    "engineering debt",
    "agentic workflow debt",
    "user failure mode",
    "user failure modes",
    "bottleneck",
    "bottlenecks",
    "safeguards are not working",
    "safeguards not working",
    "workflows to work around that",
    "ambiguous hoping you would catch",
    "catch all my intentions",
    "intent better",
    "conversational flow",
    "workspace of how my head",
    "how my mind work",
    "claude code",
    "claude catches my intent",
    "new model is out",
    "rebuild and enhancement",
    "rebuild and enhance",
    "smarter routing",
    "do not limit the arsenal",
    "don't limit the arsenal",
    "full arsenal access",
    "access to all the intelligence",
    "find what i need",
    "random numbers and letters",
    "can't find anything",
    "cannot find anything",
    "organization system",
)

OPERATING_ALIGNMENT_SYSTEM_TERMS = (
    "codex",
    "antigravity",
    "harness",
    "system",
    "workspace",
    "global",
    "workflow",
    "workflows",
    "skill",
    "skills",
    "command",
    "commands",
)

OPERATING_ALIGNMENT_ORCHESTRATION_TERMS = (
    "orchestration",
    "orchestrate",
    "autopilot",
    "virtuoso",
    "expert",
    "experts",
    "agent",
    "agents",
    "subagent",
    "subagents",
    "sub-agent",
    "sub-agents",
    "automation",
    "automations",
    "routing",
)

OPERATING_ALIGNMENT_FAILURE_TERMS = (
    "ineffective",
    "not working",
    "not tapping",
    "not getting",
    "behind",
    "disjointed",
    "noise",
    "redundancies",
    "wrong",
    "correcting",
    "lost",
    "alignment issues",
    "not as well",
    "not deployed",
    "not firing",
)

SYSTEM_FAILURE_SIGNALS = (
    "things are not working",
    "things aren't working",
    "fix everything",
    "fix the rest",
    "whatever is not fixed",
    "what is not fixed",
    "not fixed",
    "get fixed now",
    "repair everything",
    "repair the system",
    "repair the harness",
    "bigger repair",
    "get this harness up",
    "get this system up",
    "up to the standard",
    "standard and quality",
    "not working",
    "not firing",
    "not doing what it is supposed to do",
    "not doing what it is supposed",
    "not doing what it's supposed to do",
    "built are not firing",
    "we built are not firing",
    "said were built are not firing",
    "competing defaults",
    "competing things",
    "feels broken",
    "feel broken",
    "broken cluttered slow",
    "full system audit",
    "system audit",
    "control plane audit",
    "control-plane audit",
    "control plane",
    "autopilot is still not",
    "autopilot is not",
    "autopilot isn't",
    "autopilot not doing",
    "autopilot broken",
    "autopilot failing",
    "autopilot weaker",
    "autopilot is useless",
    "orchestration is useless",
    "orchestrate is useless",
    "executes without intent verification",
    "execute without intent verification",
    "executing without intent verification",
    "executes without menu",
    "execute without menu",
    "executes without planning",
    "execute without planning",
    "doesn't show the planning menu",
    "does not show the planning menu",
    "never give me a menu",
    "never gave me a menu",
    "never given me a menu",
    "never gives me a menu",
    "just go execute",
    "just execute",
    "just executes",
    "mission is the only thing working",
    "only thing working is mission",
    "outside native plan mode",
    "outside plan mode",
    "cannot repeat the magic",
    "can't repeat the magic",
    "not able to repeat it",
    "unable to repeat it",
    "not repeatable",
    "can't reproduce",
    "cannot reproduce",
    "revision failure",
    "revision failures",
    "revisions keep failing",
    "multiple revision failure points",
)

SYSTEM_FAILURE_CONTEXT_TERMS = (
    "autopilot",
    "system",
    "harness",
    "control plane",
    "control-plane",
    "route",
    "router",
    "routing",
    "workflow",
    "workflows",
    "orchestration",
    "orchestrate",
    "skill",
    "skills",
    "command",
    "commands",
    "agent",
    "agents",
    "plan mode",
    "planning menu",
    "intent verification",
    "menu",
    "protocol",
    "protocols",
    "self-evolve",
    "self evolve",
    "mutation",
    "mutating",
    "proof",
    "codex",
    "output",
    "outputs",
    "response",
    "responses",
    "revision",
    "revisions",
    "repeat",
    "repeatable",
    "magic",
    "expert-composition-governor",
    "expert composition",
    "expert-composition",
    "expert soup",
)

SYSTEM_META_SIGNALS = (
    "routing",
    "router",
    "orchestration",
    "skill selection",
    "self improvement",
    "self-improvement",
    "performance",
    "generic workflows",
)


@dataclass(frozen=True)
class RouteCandidate:
    name: str
    score: int | None = None
    source: str = ""


@dataclass(frozen=True)
class GovernorDecision:
    query: str
    detected_lane: str
    confidence: float
    required_candidates: tuple[str, ...]
    command_menu_winners: tuple[str, ...]
    workflow_router_winners: tuple[str, ...]
    chosen_route: str
    skipped_routes: tuple[str, ...]
    reason: str
    feedback_recommendation: str


def normalize_query(query: str) -> str:
    return re.sub(r"\s+", " ", query.lower()).strip()


def is_operating_alignment_intent(query: str) -> bool:
    """Return True when Codex operating alignment should be system-audit owned."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if "operating alignment" in normalized or "codex operating alignment" in normalized:
        return True
    if is_capability_stewardship_intent(normalized):
        return True

    direct_hits = sum(1 for signal in OPERATING_ALIGNMENT_SIGNALS if signal in normalized)
    system_hits = sum(1 for term in OPERATING_ALIGNMENT_SYSTEM_TERMS if term in normalized)
    orchestration_hits = sum(1 for term in OPERATING_ALIGNMENT_ORCHESTRATION_TERMS if term in normalized)
    failure_hits = sum(1 for term in OPERATING_ALIGNMENT_FAILURE_TERMS if term in normalized)
    cockpit_hits = sum(1 for signal in OPERATOR_COCKPIT_REBUILD_SIGNALS if signal in normalized)

    if cockpit_hits >= 2:
        return True
    if cockpit_hits >= 1 and (system_hits >= 1 or "claude" in normalized or "codex" in normalized):
        return True

    if direct_hits >= 2 and system_hits >= 1 and orchestration_hits >= 1:
        return True
    if direct_hits >= 1 and system_hits >= 2 and orchestration_hits >= 2:
        return True
    return system_hits >= 2 and orchestration_hits >= 2 and failure_hits >= 1


def is_capability_stewardship_intent(query: str) -> bool:
    """Return True for persistent capability/session-lifecycle behavior requests."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if "capability stewardship" in normalized:
        return True

    capability_hits = sum(1 for term in CAPABILITY_STEWARDSHIP_SIGNALS if term in normalized)
    lifecycle_hits = sum(1 for term in CAPABILITY_STEWARDSHIP_LIFECYCLE_TERMS if term in normalized)
    default_hits = sum(1 for term in CAPABILITY_STEWARDSHIP_DEFAULT_TERMS if term in normalized)

    if capability_hits >= 2 and (lifecycle_hits >= 2 or default_hits >= 2):
        return True
    return capability_hits >= 1 and lifecycle_hits >= 2 and default_hits >= 1


def is_operator_cockpit_rebuild_intent(query: str) -> bool:
    """Return True for V2 cockpit, operator-friction, or retrieval-overload repair."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    return any(signal in normalized for signal in OPERATOR_COCKPIT_REBUILD_SIGNALS)


def is_revenue_intent(query: str) -> bool:
    """Return True for requests that need a concrete income/revenue route."""
    normalized = normalize_query(query)
    if not normalized:
        return False

    signal_hits = sum(1 for signal in REVENUE_SIGNALS if signal in normalized)
    if signal_hits == 0:
        return False

    # If the request is only about diagnosing the routing system, keep it in
    # the system lane. If it includes a clear make/get/earn/sell action, treat
    # it as revenue even when system words are present.
    meta_hits = sum(1 for signal in SYSTEM_META_SIGNALS if signal in normalized)
    action_hit = bool(
        re.search(
            r"\b(make|earn|get|land|book|sell|monetize|launch|offer|client|clients|cash|income|revenue)\b",
            normalized,
        )
    )
    return action_hit or meta_hits < 2


def is_productized_ai_service_os_intent(query: str) -> bool:
    """Return True for productized AI service OS packaging/build requests."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if any(signal in normalized for signal in PRODUCTIZED_AI_SERVICE_OS_SIGNALS):
        return True
    has_service = "service" in normalized or "offer" in normalized or "audit" in normalized or "sprint" in normalized
    has_productized = "productized" in normalized or "subscription" in normalized or "no-call" in normalized or "no call" in normalized
    has_os = "os" in normalized or "operating system" in normalized or "delivery system" in normalized
    return has_service and has_productized and (has_os or "ai" in normalized)


def is_ai_employee_os_intent(query: str) -> bool:
    """Return True for AI employee/company-agent operating-system requests."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if any(signal in normalized for signal in AI_EMPLOYEE_OS_SIGNALS):
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


def is_skill_system_intent(query: str) -> bool:
    """Return True for source-to-system and skill orchestration upgrade requests."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if any(signal in normalized for signal in SKILL_SYSTEM_SIGNALS):
        return True
    return (
        ("skill" in normalized or "skills" in normalized)
        and ("orchestrat" in normalized or "handoff" in normalized or "system" in normalized or "component" in normalized)
        and (
            "better" in normalized
            or "improve" in normalized
            or "upgrade" in normalized
            or "end-to-end" in normalized
            or "end to end" in normalized
        )
    )


def is_extraction_governor_intent(query: str) -> bool:
    """Return True for source-to-capability triage and extraction-governance requests."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if is_system_audit_query(normalized):
        return False
    if is_system_failure_intent(normalized):
        return False
    direct = any(
        signal in normalized
        for signal in (
            "/extraction-governor-agent",
            "source-command-extraction-governor-agent",
            "source command extraction governor agent",
            "extraction governor",
            "extraction-governor",
            "extraction governance",
        )
    )
    if direct:
        return True
    if is_skill_system_intent(normalized):
        return False
    if any(signal in normalized for signal in EXTRACTION_GOVERNOR_SIGNALS):
        return True
    has_source = any(term in normalized for term in ("source", "transcript", "article", "guide", "video", "pdf"))
    has_triage = any(
        term in normalized
        for term in (
            "triage",
            "route",
            "classify",
            "build shape",
            "build-shape",
            "hidden mechanics",
            "mechanics",
            "duplicate",
            "reusable capability",
            "knowledge artifact",
        )
    )
    return has_source and has_triage


def is_mark_operating_tree_intent(query: str) -> bool:
    """Return True when Mark Kashef should route through the source-to-system tree."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if not any(signal in normalized for signal in MARK_OPERATING_TREE_MARK_SIGNALS):
        return False
    if any(term in normalized for term in MARK_OPERATING_TREE_VISUAL_ONLY_TERMS) and not any(
        signal in normalized for signal in MARK_OPERATING_TREE_SYSTEM_SIGNALS
    ):
        return False
    if any(signal in normalized for signal in MARK_OPERATING_TREE_SYSTEM_SIGNALS):
        return True

    has_workflow_surface = any(
        term in normalized for term in ("workflow", "workflows", "skill", "skills", "agent", "agents", "system")
    )
    has_improvement_surface = any(
        term in normalized
        for term in (
            "self-improving",
            "self improving",
            "self-evolve",
            "self evolve",
            "evolve",
            "anneal",
            "improve",
            "improving",
            "regression",
            "failure history",
            "performance log",
            "performance logs",
        )
    )
    return has_workflow_surface and has_improvement_surface


def is_liam_linkedin_lead_magnet_intent(query: str) -> bool:
    """Return True for AI-assisted LinkedIn lead magnet system requests."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    has_linkedin = "linkedin" in normalized
    has_lead_magnet = "lead magnet" in normalized or "lead-magnet" in normalized
    if not (has_linkedin and has_lead_magnet):
        return False
    return any(term in normalized for term in LIAM_LINKEDIN_LEAD_MAGNET_CONTEXT_TERMS)


def is_expert_composition_intent(query: str) -> bool:
    """Return True when many experts/skills need owner-led composition."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if is_system_audit_query(normalized):
        return False
    if is_system_failure_intent(normalized):
        return False
    if any(
        signal in normalized
        for signal in (
            "command bloat",
            "routing overhead",
            "context footprint",
            "system efficiency",
            "efficiency benchmark",
            "overengineering",
            "over-engineering",
            "what to tighten first",
        )
    ):
        return False
    if any(signal in normalized for signal in EXPERT_COMPOSITION_SIGNALS):
        return True

    has_many = any(term in normalized for term in ("many", "multiple", "too many", "several"))
    has_context = any(term in normalized for term in EXPERT_COMPOSITION_CONTEXT_TERMS)
    has_quality_problem = any(
        term in normalized
        for term in (
            "generic",
            "flat",
            "not integrated",
            "not interwoven",
            "stitched",
            "scattered",
            "slop",
            "soup",
            "overlap",
        )
    )
    return has_many and has_context and has_quality_problem


def is_virtuoso_intent(query: str) -> bool:
    """Return True when the user explicitly wants the Virtuoso front door."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    compact = re.sub(r"[^a-z0-9]", "", normalized)
    if compact in {"virtuoso", "sourcecommandvirtuoso"}:
        return True
    if any(signal in normalized for signal in VIRTUOSO_SIGNALS):
        return True
    return (
        "orchestration" in normalized
        and any(term in normalized for term in ("full harness", "full system", "deploy", "at will", "solo"))
    )


def is_kishotenketsu_storytelling_intent(query: str) -> bool:
    """Return True for contrast-first narrative work owned by Kishotenketsu."""
    normalized = normalize_query(query)
    if not normalized:
        return False

    if any(
        gate in normalized
        for gate in (
            "/publishable-copy-gate",
            "publishable-copy-gate",
            "publishable copy gate",
            "copy gate",
        )
    ):
        return False

    explicit_signals = (
        "kishotenketsu",
        "ki-sho-ten-ketsu",
        "ki sho ten ketsu",
        "contrast driven storytelling",
        "contrast-driven storytelling",
        "contrast storytelling",
        "contrast story",
        "variable over villain",
        "process as plot",
        "process-as-plot",
        "integration over victory",
        "integration instead of victory",
        "integration instead of enemies",
        "perspective shift",
        "perspective-shift",
        "world invitation",
        "changed-world messaging",
        "changed world messaging",
        "non-conflict story",
        "non conflict story",
        "forced villain",
        "fake villain",
        "fake conflict",
        "problem-agitation relapse",
        "problem agitation relapse",
    )
    if any(signal in normalized for signal in explicit_signals):
        return True

    domain_terms = (
        "story",
        "storytelling",
        "narrative",
        "writing",
        "copy",
        "copywriting",
        "ad",
        "ads",
        "media",
        "script",
        "content",
        "post",
        "campaign",
        "brand",
        "branding",
        "marketing",
        "messaging",
        "positioning",
        "ghostwriting",
        "product",
        "service",
        "concept",
        "offer",
        "page",
        "pitch",
    )
    engine_terms = (
        "contrast",
        "world",
        "ritual",
        "texture",
        "process",
        "variable",
        "integration",
        "reframe",
        "reframing",
        "changed reality",
        "changed category",
        "changed world",
        "new operating reality",
        "not a villain",
        "no villain",
        "without a villain",
        "without rage bait",
        "without rage-bait",
        "without fake urgency",
    )
    return any(term in normalized for term in domain_terms) and sum(
        1 for term in engine_terms if term in normalized
    ) >= 2


def is_deep_research_os_intent(query: str) -> bool:
    """Return True when the user wants the composed deep-research OS."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    compact = re.sub(r"[^a-z0-9]", "", normalized)
    if compact in {"deepresearchos", "sourcecommanddeepresearchos"}:
        return True
    if any(signal in normalized for signal in DEEP_RESEARCH_OS_SIGNALS):
        return True

    has_deep_research = (
        "deep research" in normalized
        or "wide research" in normalized
        or ("research" in normalized and any(term in normalized for term in ("deep", "widespread", "wide")))
    )
    has_research_domain = any(
        term in normalized
        for term in (
            "social listening",
            "market intelligence",
            "competitive intelligence",
            "competitor",
            "competitors",
            "icp",
            "buyer",
            "avatar",
            "pmf",
            "product-market",
            "product market",
            "offer-market",
            "offer market",
            "trend",
            "claims",
            "hallucination",
            "source ledger",
            "first principles",
            "systems thinking",
            "deep canvassing",
        )
    )
    return has_deep_research and has_research_domain


def is_explicit_menu_backend_intent(query: str) -> bool:
    """Return True when the user explicitly asks to browse menus/options."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if any(
        signal in normalized
        for signal in (
            "never give me",
            "never gave me",
            "never gives me",
            "never given me",
            "without menu",
            "without a menu",
            "doesn't show",
            "does not show",
            "not showing",
            "useless",
            "execute without",
            "executes without",
            "executing without",
            "just execute",
            "just executes",
        )
    ):
        return False
    if any(signal in normalized for signal in MENU_BACKEND_SIGNALS):
        return True
    has_menu_or_options = any(term in normalized for term in ("menu", "options", "commands", "workflows"))
    has_browse_verb = any(term in normalized for term in ("show", "list", "browse", "open", "give me"))
    return has_menu_or_options and has_browse_verb


def is_end_session_closeout_intent(query: str) -> bool:
    """Return True for session closeout, handoff, and wrap-up intent."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    compact = re.sub(r"[^a-z0-9]", "", normalized)
    if compact in {"endsession", "sourcecommandendsession"}:
        return True
    # Lifecycle/default requests may mention closeout as one phase. They are
    # operating-alignment work, not instructions to close the current session.
    if is_capability_stewardship_intent(normalized):
        return False
    if any(signal in normalized for signal in END_SESSION_SIGNALS):
        return True
    has_session = "session" in normalized or "conversation" in normalized or "thread" in normalized
    has_closeout = any(
        term in normalized
        for term in ("closeout", "close out", "wrap", "handoff", "recap", "end session", "end this session")
    )
    has_context = sum(1 for term in END_SESSION_CONTEXT_TERMS if term in normalized) >= 2
    return has_session and has_closeout and has_context


def is_steering_compass_intent(query: str) -> bool:
    """Return True when the user wants richer next-step/operator steering."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    direct_signals = (
        "/steering-compass",
        "source-command-steering-compass",
        "source command steering compass",
        "steering compass",
        "steering output",
        "operator lesson",
        "operator coach",
        "three next paths",
        "three next prompts",
        "3 next prompts",
        "three next things",
        "three recommendations",
        "best three next",
        "best 3 next",
        "next best steps",
        "next best prompts",
        "continuation prompts",
        "enhancement prompts",
        "enrichment prompts",
        "use now harden expand",
        "use now / harden / expand",
        "what should i do next",
        "what do i do next",
        "what should i ask you next",
        "what should i ask next",
        "go with your verdict",
        "use your recommendation",
        "recommended path",
        "help me steer",
        "better steer",
        "contextually read the entire session",
        "leverage this conversation",
        "leverage the conversation",
    )
    if any(signal in normalized for signal in direct_signals):
        return True
    steering_terms = ("steer", "steering", "recommendation", "recommendations", "next")
    quality_terms = ("elevate", "enrich", "enhance", "sophisticated", "deeper", "better")
    output_terms = ("output", "closeout", "lesson", "prompt", "prompts", "session")
    return (
        any(term in normalized for term in steering_terms)
        and any(term in normalized for term in quality_terms)
        and any(term in normalized for term in output_terms)
    )


def is_transfer_handoff_intent(query: str) -> bool:
    """Return True for a focused transfer handoff, not general session closeout."""
    normalized = normalize_query(query)
    if not normalized or is_end_session_closeout_intent(normalized):
        return False
    direct_signals = (
        "/handoff",
        "source-command-handoff",
        "source command handoff",
        "handoff document",
        "transfer-ready handoff",
        "prepare context for next chat",
        "prepare context for a new chat",
        "summarize for a new session",
        "summarise for a new session",
        "continue this in another conversation",
        "fresh agent",
        "another agent",
        "separate agent",
        "separate session",
        "new conversation",
        "new chat",
        "pass work to",
        "handoff to prototype",
        "handoff branch",
        "branch session",
    )
    if any(signal in normalized for signal in direct_signals):
        return True
    return "handoff" in normalized and any(
        term in normalized
        for term in (
            "agent",
            "session",
            "conversation",
            "prototype",
            "branch",
            "transfer",
            "continue",
            "context",
        )
    )


def is_front_door_choice_intent(query: str) -> bool:
    """Return True when the user needs the system to choose the first door."""
    normalized = normalize_query(query)
    if not normalized or is_explicit_menu_backend_intent(normalized):
        return False
    if is_skill_system_intent(normalized) and any(
        term in normalized
        for term in (
            "source",
            "video",
            "transcript",
            "source-to-skill",
            "source to skill",
            "source-to-system",
            "source to system",
            "turn this video",
        )
    ):
        return False
    if any(signal in normalized for signal in FRONT_DOOR_CHOICE_SIGNALS):
        return True

    has_choice_verb = any(
        term in normalized
        for term in (
            "choose",
            "pick",
            "select",
            "recommend",
            "route",
            "use",
        )
    )
    has_tool_surface = any(
        term in normalized
        for term in (
            "tool",
            "tools",
            "command",
            "commands",
            "workflow",
            "workflows",
            "route",
            "routes",
            "agent",
            "agents",
            "skill",
            "skills",
        )
    )
    has_uncertainty = any(
        term in normalized
        for term in (
            "too many",
            "don't know",
            "dont know",
            "do not know",
            "not sure",
            "unsure",
            "which",
            "what should",
            "next",
        )
    )
    return has_choice_verb and has_tool_surface and has_uncertainty


def is_repeatability_intent(query: str) -> bool:
    """Return True when the user is asking to reproduce or recover a good run."""
    normalized = normalize_query(query)
    if not normalized:
        return False

    # Avoid sending actual Phil M Jones "magic words" work into system repair.
    if "magic words" in normalized and not any(
        term in normalized
        for term in ("repeat", "reproduce", "revision", "failed", "failing", "worse", "lost")
    ):
        return False

    if any(signal in normalized for signal in REPEATABILITY_SIGNALS):
        return True

    has_repeatability_word = any(
        term in normalized
        for term in ("repeatability", "reproduce", "preserve", "revision", "rewrite", "regression")
    )
    has_failure_word = any(
        term in normalized
        for term in ("failed", "failing", "failure", "worse", "flat", "lost", "wrong", "introduced", "caused")
    )
    has_context = any(term in normalized for term in REPEATABILITY_CONTEXT_TERMS)
    return has_repeatability_word and has_failure_word and has_context


def is_copy_quality_failure_intent(query: str) -> bool:
    """Return True when the user says the Copy Gate overstated quality."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if "copy" not in normalized and "gate" not in normalized and "publishable-copy-gate" not in normalized:
        return False
    signal_hits = sum(1 for signal in COPY_QUALITY_SIGNALS if signal in normalized)
    if signal_hits >= 3:
        return True
    if "copy gate" in normalized and any(
        term in normalized for term in ("ceremonial", "inflated", "generic", "flat", "weak hook", "no tension")
    ):
        return True
    return False


def is_system_audit_query(query: str) -> bool:
    """Return True when the user is directly asking for a system audit."""
    normalized = normalize_query(query)
    if is_operating_alignment_intent(normalized):
        return True
    if any(
        signal in normalized
        for signal in (
            "system audit",
            "full system audit",
            "control plane audit",
            "control-plane audit",
            "audit the system",
            "audit our system",
            "audit this system",
            "system control plane audit",
        )
    ):
        return True

    has_audit = "audit" in normalized or "diagnose" in normalized or "inspect" in normalized
    has_control_context = any(
        term in normalized
        for term in (
            "autopilot",
            "routing",
            "router",
            "bridge",
            "control plane",
            "control-plane",
            "harness",
            "workflow",
            "workflows",
            "skill",
            "skills",
            "drift",
            "firing",
        )
    )
    return has_audit and has_control_context


def is_system_failure_intent(query: str) -> bool:
    """Return True for broken/failing harness, routing, or Autopilot intent."""
    normalized = normalize_query(query)
    if not normalized:
        return False

    if is_operating_alignment_intent(normalized):
        return True

    if is_system_audit_query(normalized):
        return True

    exactish_hits = (
        "things are not working",
        "things aren't working",
        "fix everything",
        "fix the rest",
        "whatever is not fixed",
        "what is not fixed",
        "not fixed",
        "get fixed now",
        "repair everything",
        "repair the system",
        "repair the harness",
        "bigger repair",
        "get this harness up",
        "get this system up",
        "up to the standard",
        "standard and quality",
        "not firing",
        "built are not firing",
        "competing defaults",
        "competing things",
        "feels broken",
        "feel broken",
        "broken cluttered slow",
        "outside native plan mode",
        "outside plan mode",
        "cannot repeat the magic",
        "can't repeat the magic",
        "not able to repeat it",
        "unable to repeat it",
        "not repeatable",
        "can't reproduce",
        "cannot reproduce",
        "revision failure",
        "revision failures",
        "revisions keep failing",
        "multiple revision failure points",
    )
    if any(signal in normalized for signal in exactish_hits):
        return True

    has_failure_word = any(
        signal in normalized
        for signal in (
            "not working",
            "not fixed",
            "fix everything",
            "fix the rest",
            "repair everything",
            "bigger repair",
            "broken",
            "failing",
            "fail",
            "not doing what it is supposed",
            "not doing what it's supposed",
            "weaker",
            "competing",
            "useless",
            "executes without",
            "execute without",
            "executing without",
            "never give me",
            "never gave me",
            "never given me",
            "never gives me",
            "just execute",
            "just executes",
            "just go execute",
        )
    )
    has_system_context = any(term in normalized for term in SYSTEM_FAILURE_CONTEXT_TERMS)
    return has_failure_word and has_system_context


def is_health_check_intent(query: str) -> bool:
    """Return True for explicit read-only health/status checks."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if is_system_audit_query(normalized):
        return False
    if is_system_failure_intent(normalized) and "failure examples" not in normalized:
        return False
    compact = re.sub(r"[^a-z0-9]", "", normalized)
    if compact in {"healthcheck", "sourcecommandhealthcheck", "runharnessstatus"}:
        return True
    if any(signal in normalized for signal in HEALTH_CHECK_SIGNALS):
        return True
    has_status = any(term in normalized for term in ("status", "health", "readiness"))
    has_context = any(term in normalized for term in ("harness", "system", "activation", "feedback loop"))
    return has_status and has_context and sum(1 for term in HEALTH_CHECK_CONTEXT_TERMS if term in normalized) >= 2


def is_routing_intelligence_intent(query: str) -> bool:
    """Return True for explicit read-only routing analytics checks."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if is_system_audit_query(normalized):
        return False
    if is_system_failure_intent(normalized) and "failure examples" not in normalized:
        return False
    compact = re.sub(r"[^a-z0-9]", "", normalized)
    if compact in {"routingintelligence", "sourcecommandroutingintelligence", "routingscoreboard", "showroutingscoreboard"}:
        return True
    if any(signal in normalized for signal in ROUTING_INTELLIGENCE_SIGNALS):
        return True
    has_routing = any(term in normalized for term in ("routing", "route", "router"))
    has_analytics = any(term in normalized for term in ("scoreboard", "analytics", "dashboard", "feedback", "utilization", "underperforming"))
    return has_routing and has_analytics and sum(1 for term in ROUTING_INTELLIGENCE_CONTEXT_TERMS if term in normalized) >= 2


def is_knowledge_librarian_intent(query: str) -> bool:
    """Return True for explicit library-pulse and reusable-context prompts."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if is_system_audit_query(normalized):
        return False
    if is_system_failure_intent(normalized):
        return False
    if is_repeatability_intent(normalized):
        return False
    if is_skill_system_intent(normalized):
        return False
    compact = re.sub(r"[^a-z0-9]", "", normalized)
    if compact in {"knowledgelibrarian", "sourcecommandknowledgelibrarian"}:
        return True
    if any(signal in normalized for signal in KNOWLEDGE_LIBRARIAN_SIGNALS):
        return True
    has_knowledge = any(term in normalized for term in ("knowledge", "library", "context", "solution docs", "workflow"))
    has_retrieval = any(term in normalized for term in ("retrieve", "surface", "prior", "reusable", "underused", "start command", "pulse"))
    return has_knowledge and has_retrieval


def is_self_evolve_intent(query: str) -> bool:
    """Return True for explicit measured workflow-evolution prompts."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if is_system_audit_query(normalized):
        return False
    if is_system_failure_intent(normalized):
        return False
    if is_repeatability_intent(normalized):
        return False
    if is_skill_system_intent(normalized):
        return False
    compact = re.sub(r"[^a-z0-9]", "", normalized)
    if compact in {"selfevolve", "sourcecommandselfevolve"}:
        return True
    if any(signal in normalized for signal in SELF_EVOLVE_SIGNALS):
        return True
    has_target = any(term in normalized for term in ("workflow", "prompt", "retrieval", "orchestration", "routing", "skill"))
    has_evolution = any(term in normalized for term in ("evolve", "improve", "failure history", "performance", "regression", "recurring mistake"))
    return has_target and has_evolution


def is_skill_anneal_intent(query: str) -> bool:
    """Return True for explicit prompt-level skill annealing prompts."""
    normalized = normalize_query(query)
    if not normalized:
        return False
    if is_system_audit_query(normalized):
        return False
    if is_system_failure_intent(normalized) and "failure examples" not in normalized:
        return False
    compact = re.sub(r"[^a-z0-9]", "", normalized)
    if compact in {"skillanneal", "sourcecommandskillanneal"}:
        return True
    if any(signal in normalized for signal in SKILL_ANNEAL_SIGNALS):
        return True
    has_skill = any(term in normalized for term in ("skill", "skill prompt", "skill.md", "prompt"))
    has_anneal = any(term in normalized for term in ("anneal", "self-anneal", "self anneal", "rubric", "test input", "failure examples"))
    return has_skill and has_anneal


def revenue_route_bonus(route_name: str) -> int:
    """Score bonus for the revenue stack when revenue intent is detected."""
    bonuses = {
        "first-10k": 120,
        "revenue-offer-agent": 112,
        "client-acquire": 104,
        "zero-to-client-sprint": 98,
        "service-first-productization": 92,
    }
    if route_name in bonuses:
        return bonuses[route_name]
    if route_name in REVENUE_SUPPORT_ROUTES:
        return 48
    if route_name.startswith("fourth-wall-"):
        return -35
    return 0


def productized_ai_service_os_route_bonus(route_name: str) -> int:
    """Score bonus for productized AI service OS packaging intent."""
    bonuses = {
        "productized-ai-service-os": 260,
        "service-first-productization": 112,
        "revenue-offer-agent": 96,
        "24-assets-productized-service": 84,
        "client-delivery-agent": 72,
        "ash-productized-validation": 64,
        "publishable-copy-gate": -80,
    }
    return bonuses.get(route_name, 0)


def ai_employee_os_route_bonus(route_name: str) -> int:
    """Score bonus for AI employee/company-agent OS intent."""
    bonuses = {
        "ai-employee-os": 260,
        "context-audit": 60,
        "memory-architect": 56,
        "conde-agent-experience-design": 52,
        "24-assets-agent-system-design": 48,
        "harness-audit": 20,
        "source-to-skill-system": 18,
    }
    return bonuses.get(route_name, 0)


def skill_system_route_bonus(route_name: str) -> int:
    """Score bonus for the skill-system stack when source-to-system intent is detected."""
    bonuses = {
        "source-to-skill-system": 240,
        "extraction-governor-agent": 125,
        "mission": 105,
        "autopilot": 95,
        "self-evolve": 80,
        "skill-anneal": 72,
        "orchestrate": 45,
        "knowledge-librarian": 35,
    }
    return bonuses.get(route_name, 0)


def extraction_governor_route_bonus(route_name: str) -> int:
    """Score bonus for extraction-governance and source-triage prompts."""
    bonuses = {
        "extraction-governor-agent": 285,
        "source-to-skill-system": 120,
        "knowledge-librarian": 95,
        "plugin-readiness-audit": 80,
        "autopilot": 70,
        "orchestrate": 45,
        "extract-forge": 35,
        "convert-extraction": 30,
        "compile-knowledge": 25,
    }
    return bonuses.get(route_name, 0)


def liam_linkedin_lead_magnet_route_bonus(route_name: str) -> int:
    """Score bonus for the Liam/Ottley LinkedIn AI lead magnet route."""
    bonuses = {
        "liam-linkedin-lead-magnet": 220,
        "bank-lead-magnet": 35,
        "diandra-linkedin-system": 24,
        "profile-conversion": 18,
        "diandra-first-50": 16,
        "publishable-copy-gate": -120,
    }
    return bonuses.get(route_name, 0)


def expert_composition_route_bonus(route_name: str) -> int:
    """Score bonus for expert-soup prevention and composition routes."""
    bonuses = {
        "expert-composition-governor": 260,
        "autopilot": 105,
        "orchestrate": 95,
        "mission": 80,
        "source-to-skill-system": 65,
        "self-evolve": 45,
        "skill-anneal": 35,
    }
    return bonuses.get(route_name, 0)


def virtuoso_route_bonus(route_name: str) -> int:
    """Score bonus for the deploy-at-will Virtuoso front door."""
    bonuses = {
        "virtuoso": 320,
        "autopilot": 95,
        "expert-composition-governor": 86,
        "orchestrate": 72,
        "routing-intelligence": 48,
        "health-check": 42,
    }
    return bonuses.get(route_name, 0)


def kishotenketsu_storytelling_route_bonus(route_name: str) -> int:
    """Score bonus for the Kishotenketsu contrast storytelling OS."""
    bonuses = {
        "kishotenketsu-contrast-storytelling": 320,
        "publishable-copy-gate": -90,
        "messaging-positioning-agent": -35,
        "positioning-message-bridge": -25,
        "dunford-positioning-to-copy": -25,
    }
    return bonuses.get(route_name, 0)


def deep_research_os_route_bonus(route_name: str) -> int:
    """Score bonus for composed deep-research/social-listening intent."""
    bonuses = {
        "deep-research-os": 300,
        "research-intelligence-agent": 125,
        "deep-research": 90,
        "research-swarm": 82,
        "parallel-research": 76,
        "competitor-intel": 68,
        "icp-deep-dive": 64,
        "deep-research-gemini": 58,
    }
    return bonuses.get(route_name, 0)


def front_door_choice_route_bonus(route_name: str) -> int:
    """Score bonus for tool-choice prompts that should start at Autopilot."""
    bonuses = {
        "autopilot": 260,
        "orchestrate": 125,
        "command-menu": 95,
        "routing-intelligence": 82,
        "knowledge-librarian": 72,
        "mission": 62,
        "tool-router-design": -30,
        "compile-knowledge": -35,
        "knowledge-search": -25,
        "knowledge-alchemy": -25,
    }
    return bonuses.get(route_name, 0)


def menu_backend_route_bonus(route_name: str) -> int:
    """Score bonus for explicit menu/options prompts that belong to Orchestrate."""
    bonuses = {
        "orchestrate": 260,
        "command-menu": 125,
        "autopilot": 85,
        "routing-intelligence": 55,
        "mission": 45,
    }
    return bonuses.get(route_name, 0)


def steering_compass_route_bonus(route_name: str) -> int:
    """Score bonus for next-step steering and Operator Coach prompts."""
    bonuses = {
        "steering-compass": 280,
        "autopilot": 105,
        "end-session": 90,
        "source-to-skill-system": 75,
        "skill-anneal": 65,
        "routing-intelligence": 52,
        "mission": -70,
    }
    return bonuses.get(route_name, 0)


def handoff_route_bonus(route_name: str) -> int:
    """Score bonus for transfer-ready handoffs to another session or agent."""
    bonuses = {
        "handoff": 300,
        "end-session": 120,
        "steering-compass": 95,
        "autopilot": 70,
        "source-to-skill-system": 55,
        "mission": -60,
    }
    return bonuses.get(route_name, 0)


def end_session_route_bonus(route_name: str) -> int:
    """Score bonus for natural-language session closeout and handoff prompts."""
    bonuses = {
        "end-session": 280,
        "autopilot": 105,
        "routing-intelligence": 70,
        "health-check": 55,
        "mission": -80,
        "orchestrate": 20,
    }
    return bonuses.get(route_name, 0)


def health_check_route_bonus(route_name: str) -> int:
    """Score bonus for explicit read-only harness health/status prompts."""
    bonuses = {
        "health-check": 280,
        "routing-intelligence": 90,
        "system-audit": 75,
        "autopilot": 65,
        "mission": -60,
        "evolution-status": -80,
        "status-trap": -80,
        "picks-status": -90,
    }
    return bonuses.get(route_name, 0)


def routing_intelligence_route_bonus(route_name: str) -> int:
    """Score bonus for explicit routing analytics and scoreboard prompts."""
    bonuses = {
        "routing-intelligence": 280,
        "health-check": 105,
        "system-audit": 80,
        "autopilot": 65,
        "orchestrate": 45,
        "mission": -60,
        "source-to-skill-system": -80,
    }
    return bonuses.get(route_name, 0)


def knowledge_librarian_route_bonus(route_name: str) -> int:
    """Score bonus for explicit library-pulse and prior-context retrieval prompts."""
    bonuses = {
        "knowledge-librarian": 280,
        "autopilot": 75,
        "command-menu": 65,
        "routing-intelligence": 55,
        "orchestrate": 45,
        "end-session": -60,
        "mission": -55,
    }
    return bonuses.get(route_name, 0)


def self_evolve_route_bonus(route_name: str) -> int:
    """Score bonus for explicit measured workflow-evolution prompts."""
    bonuses = {
        "self-evolve": 280,
        "routing-intelligence": 110,
        "skill-anneal": 95,
        "repeatability-spine": 75,
        "system-audit": 65,
        "autopilot": 55,
        "mission": -55,
    }
    return bonuses.get(route_name, 0)


def skill_anneal_route_bonus(route_name: str) -> int:
    """Score bonus for explicit prompt-level skill annealing prompts."""
    bonuses = {
        "skill-anneal": 300,
        "self-evolve": 110,
        "repeatability-spine": 75,
        "routing-intelligence": 65,
        "system-audit": 55,
        "autopilot": 45,
        "source-to-skill-system": -90,
        "mission": -60,
    }
    return bonuses.get(route_name, 0)


def repeatability_route_bonus(route_name: str) -> int:
    """Score bonus for repeatability/revision recovery routes."""
    bonuses = {
        "repeatability-spine": 260,
        "autopilot": 135,
        "system-audit": 120,
        "publishable-copy-gate": 110,
        "self-evolve": 95,
        "skill-anneal": 85,
        "routing-intelligence": 75,
        "health-check": 45,
        "mission": 40,
        "orchestrate": 35,
        "pmj-magic-words": -90,
    }
    return bonuses.get(route_name, 0)


def operating_alignment_route_bonus(route_name: str) -> int:
    """Score bonus for operating-alignment repair with bounded support gates."""
    bonuses = {
        "system-audit": 360,
        "autopilot": 185,
        "virtuoso": 160,
        "expert-composition-governor": 145,
        "routing-intelligence": 132,
        "health-check": 120,
        "repeatability-spine": 96,
        "self-evolve": 82,
        "skill-anneal": 66,
        "orchestrate": 42,
        "mission": -60,
    }
    if route_name.startswith("fladlien-"):
        return -70
    return bonuses.get(route_name, 0)


def system_failure_route_bonus(route_name: str, query: str = "") -> int:
    """Score bonus for control-plane repair routes when the system feels broken."""
    audit_first = is_system_audit_query(query)
    if audit_first:
        bonuses = {
            "system-audit": 280,
            "autopilot": 170,
            "routing-intelligence": 130,
            "health-check": 125,
            "mission": 110,
            "orchestrate": 90,
            "self-evolve": 75,
            "skill-anneal": 65,
            "context-audit": 35,
            "harness-audit": 35,
            "system-hygiene": 30,
        }
    else:
        bonuses = {
            "autopilot": 185,
            "system-audit": 165,
            "routing-intelligence": 130,
            "health-check": 125,
            "mission": 110,
            "orchestrate": 90,
            "self-evolve": 75,
            "skill-anneal": 65,
            "context-audit": 30,
            "harness-audit": 30,
            "system-hygiene": 25,
        }
    if route_name.startswith("kcs-"):
        return -60
    return bonuses.get(route_name, 0)


def governed_route_names(query: str, raw_routes: Iterable[str]) -> list[str]:
    """Return route names with governor-required routes promoted first."""
    routes = [route for route in raw_routes if route]
    if is_operating_alignment_intent(query):
        ordered = [route for route in OPERATING_ALIGNMENT_STACK if route in routes]
        ordered.extend(route for route in OPERATING_ALIGNMENT_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_virtuoso_intent(query):
        ordered = [route for route in VIRTUOSO_STACK if route in routes]
        ordered.extend(route for route in VIRTUOSO_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_kishotenketsu_storytelling_intent(query):
        ordered = [route for route in KISHOTENKETSU_STORYTELLING_STACK if route in routes]
        ordered.extend(route for route in KISHOTENKETSU_STORYTELLING_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_deep_research_os_intent(query):
        ordered = [route for route in DEEP_RESEARCH_OS_STACK if route in routes]
        ordered.extend(route for route in DEEP_RESEARCH_OS_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_ai_employee_os_intent(query):
        ordered = [route for route in AI_EMPLOYEE_OS_STACK if route in routes]
        ordered.extend(route for route in AI_EMPLOYEE_OS_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_productized_ai_service_os_intent(query):
        ordered = [route for route in PRODUCTIZED_AI_SERVICE_OS_STACK if route in routes]
        ordered.extend(route for route in PRODUCTIZED_AI_SERVICE_OS_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_mark_operating_tree_intent(query):
        ordered = [route for route in MARK_OPERATING_TREE_STACK if route in routes]
        ordered.extend(route for route in MARK_OPERATING_TREE_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_extraction_governor_intent(query):
        ordered = [route for route in EXTRACTION_GOVERNOR_STACK if route in routes]
        ordered.extend(route for route in EXTRACTION_GOVERNOR_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_copy_quality_failure_intent(query):
        ordered = [route for route in COPY_QUALITY_STACK if route in routes]
        ordered.extend(route for route in COPY_QUALITY_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_expert_composition_intent(query):
        ordered = [route for route in EXPERT_COMPOSITION_STACK if route in routes]
        ordered.extend(route for route in EXPERT_COMPOSITION_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_front_door_choice_intent(query):
        ordered = [route for route in FRONT_DOOR_CHOICE_STACK if route in routes]
        ordered.extend(route for route in FRONT_DOOR_CHOICE_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_explicit_menu_backend_intent(query):
        ordered = [route for route in MENU_BACKEND_STACK if route in routes]
        ordered.extend(route for route in MENU_BACKEND_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_end_session_closeout_intent(query):
        ordered = [route for route in END_SESSION_STACK if route in routes]
        ordered.extend(route for route in END_SESSION_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_health_check_intent(query):
        ordered = [route for route in HEALTH_CHECK_STACK if route in routes]
        ordered.extend(route for route in HEALTH_CHECK_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_routing_intelligence_intent(query):
        ordered = [route for route in ROUTING_INTELLIGENCE_STACK if route in routes]
        ordered.extend(route for route in ROUTING_INTELLIGENCE_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_knowledge_librarian_intent(query):
        ordered = [route for route in KNOWLEDGE_LIBRARIAN_STACK if route in routes]
        ordered.extend(route for route in KNOWLEDGE_LIBRARIAN_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_skill_anneal_intent(query):
        ordered = [route for route in SKILL_ANNEAL_STACK if route in routes]
        ordered.extend(route for route in SKILL_ANNEAL_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_self_evolve_intent(query):
        ordered = [route for route in SELF_EVOLVE_STACK if route in routes]
        ordered.extend(route for route in SELF_EVOLVE_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_transfer_handoff_intent(query):
        ordered = [route for route in HANDOFF_STACK if route in routes]
        ordered.extend(route for route in HANDOFF_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_steering_compass_intent(query):
        ordered = [route for route in STEERING_COMPASS_STACK if route in routes]
        ordered.extend(route for route in STEERING_COMPASS_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_repeatability_intent(query):
        ordered = [route for route in REPEATABILITY_STACK if route in routes]
        ordered.extend(route for route in REPEATABILITY_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_system_failure_intent(query):
        stack = SYSTEM_AUDIT_FIRST_STACK if is_system_audit_query(query) else SYSTEM_FAILURE_STACK
        ordered = [route for route in stack if route in routes]
        ordered.extend(route for route in stack if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if is_liam_linkedin_lead_magnet_intent(query):
        ordered = [route for route in LIAM_LINKEDIN_LEAD_MAGNET_STACK if route in routes]
        ordered.extend(route for route in LIAM_LINKEDIN_LEAD_MAGNET_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered
    if not is_revenue_intent(query):
        if not is_skill_system_intent(query):
            return routes
        ordered = [route for route in SKILL_SYSTEM_STACK if route in routes]
        ordered.extend(route for route in SKILL_SYSTEM_STACK if route not in ordered)
        ordered.extend(route for route in routes if route not in ordered)
        return ordered

    ordered = [route for route in REVENUE_STACK if route in routes]
    ordered.extend(route for route in REVENUE_STACK if route not in ordered)
    ordered.extend(route for route in routes if route not in ordered)
    return ordered


def choose_route(query: str, routes: Iterable[str]) -> str:
    ordered = governed_route_names(query, routes)
    return ordered[0] if ordered else ""


def flagged_routes_for(query: str, routes: Iterable[str]) -> tuple[str, ...]:
    if is_operating_alignment_intent(query):
        allowed = set(OPERATING_ALIGNMENT_STACK) | {"system-hygiene", "context-audit", "harness-audit"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_virtuoso_intent(query):
        allowed = set(VIRTUOSO_STACK) | {"system-audit", "source-to-skill-system"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_kishotenketsu_storytelling_intent(query):
        allowed = set(KISHOTENKETSU_STORYTELLING_STACK) | {
            "source-to-skill-system",
            "lucas-alpay-storytelling",
            "category-building-os",
            "dunford-positioning-diagnostic",
        }
        return tuple(route for route in routes if route and route not in allowed)
    if is_deep_research_os_intent(query):
        allowed = set(DEEP_RESEARCH_OS_STACK) | {"deep-research-gemini", "research-topic", "research-landscape"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_ai_employee_os_intent(query):
        allowed = set(AI_EMPLOYEE_OS_STACK) | {"source-to-skill-system", "extraction-governor-agent"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_productized_ai_service_os_intent(query):
        allowed = set(PRODUCTIZED_AI_SERVICE_OS_STACK) | {"source-to-skill-system", "extraction-governor-agent"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_mark_operating_tree_intent(query):
        allowed = set(MARK_OPERATING_TREE_STACK) | {"autopilot", "mission", "routing-intelligence", "knowledge-librarian"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_extraction_governor_intent(query):
        allowed = set(EXTRACTION_GOVERNOR_STACK) | {"extract-forge", "convert-extraction", "compile-knowledge", "video-source-extract", "extract"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_copy_quality_failure_intent(query):
        allowed = set(COPY_QUALITY_STACK) | {"repeatability-spine", "autopilot"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_expert_composition_intent(query):
        allowed = set(EXPERT_COMPOSITION_STACK) | {"system-audit", "routing-intelligence", "knowledge-librarian"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_front_door_choice_intent(query):
        allowed = set(FRONT_DOOR_CHOICE_STACK) | {"system-audit", "health-check"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_explicit_menu_backend_intent(query):
        allowed = set(MENU_BACKEND_STACK)
        return tuple(route for route in routes if route and route not in allowed)
    if is_end_session_closeout_intent(query):
        allowed = set(END_SESSION_STACK) | {"session-calibrate", "project-coordinate"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_health_check_intent(query):
        allowed = set(HEALTH_CHECK_STACK) | {"system-health"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_routing_intelligence_intent(query):
        allowed = set(ROUTING_INTELLIGENCE_STACK)
        return tuple(route for route in routes if route and route not in allowed)
    if is_knowledge_librarian_intent(query):
        allowed = set(KNOWLEDGE_LIBRARIAN_STACK)
        return tuple(route for route in routes if route and route not in allowed)
    if is_skill_anneal_intent(query):
        allowed = set(SKILL_ANNEAL_STACK)
        return tuple(route for route in routes if route and route not in allowed)
    if is_self_evolve_intent(query):
        allowed = set(SELF_EVOLVE_STACK)
        return tuple(route for route in routes if route and route not in allowed)
    if is_transfer_handoff_intent(query):
        allowed = set(HANDOFF_STACK) | {"session-calibrate", "project-coordinate"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_steering_compass_intent(query):
        allowed = set(STEERING_COMPASS_STACK) | {"orchestrate", "knowledge-librarian"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_repeatability_intent(query):
        allowed = set(REPEATABILITY_STACK) | {"copywriting-agent", "excellence-gate", "quality-judge"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_system_failure_intent(query):
        allowed = set(SYSTEM_FAILURE_STACK) | {"context-audit", "harness-audit", "system-hygiene"}
        return tuple(route for route in routes if route and route not in allowed)
    if is_liam_linkedin_lead_magnet_intent(query):
        allowed = set(LIAM_LINKEDIN_LEAD_MAGNET_STACK) | {"high-dwell", "algorithmic-reach"}
        return tuple(route for route in routes if route and route not in allowed)
    if not is_revenue_intent(query):
        return ()
    allowed = set(REVENUE_STACK) | set(REVENUE_SUPPORT_ROUTES)
    return tuple(route for route in routes if route and route not in allowed)


def evaluate(
    query: str,
    command_menu_winners: Iterable[str],
    workflow_router_winners: Iterable[str],
) -> GovernorDecision:
    menu_routes = tuple(command_menu_winners)
    workflow_routes = tuple(workflow_router_winners)
    combined = list(dict.fromkeys([*menu_routes, *workflow_routes]))

    if is_operating_alignment_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.97 if chosen == "system-audit" else 0.87
        return GovernorDecision(
            query=query,
            detected_lane="system-failure",
            confidence=confidence,
            required_candidates=OPERATING_ALIGNMENT_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Operating-alignment intent detected. Prefer /system-audit as the "
                "single owner for control-plane repair, with /autopilot, /virtuoso, "
                "/expert-composition-governor, /routing-intelligence, and "
                "/repeatability-spine as bounded support gates. Do not let a domain "
                "expert stack become the owner."
            ),
            feedback_recommendation=(
                "If an operating-alignment request routes to a domain expert or "
                "standalone composition route, log it with `python3 "
                "execution/routing_intelligence.py misroute --request \"...\" "
                "--wrong \"...\" --correct \"system-audit\"`."
            ),
        )

    if is_virtuoso_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.96 if chosen == "virtuoso" else 0.86
        return GovernorDecision(
            query=query,
            detected_lane="virtuoso",
            confidence=confidence,
            required_candidates=VIRTUOSO_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Virtuoso orchestration intent detected. Prefer /virtuoso as the "
                "single hot front door for trace, owner, stack, support gates, "
                "delegation packets, verification, and the first safe local action."
            ),
            feedback_recommendation=(
                "If a component route wins an explicit Virtuoso query, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"...\" --correct \"virtuoso\"`."
            ),
        )

    if is_kishotenketsu_storytelling_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.97 if chosen == "kishotenketsu-contrast-storytelling" else 0.86
        return GovernorDecision(
            query=query,
            detected_lane="kishotenketsu-contrast-storytelling",
            confidence=confidence,
            required_candidates=KISHOTENKETSU_STORYTELLING_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Kishotenketsu contrast-storytelling intent detected. Prefer "
                "/kishotenketsu-contrast-storytelling as the owner for world invitation, "
                "variable-over-villain, process-as-plot, changed-world messaging, "
                "perspective shift, and integration work. Use publishable-copy, "
                "positioning, ghostwriting, and high-taste gates as bounded support."
            ),
            feedback_recommendation=(
                "If this intent routes to a generic copy, positioning, or content gate, "
                "log it with `python3 execution/routing_intelligence.py misroute "
                "--request \"...\" --wrong \"...\" --correct "
                "\"kishotenketsu-contrast-storytelling\"`."
            ),
        )

    if is_deep_research_os_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.95 if chosen == "deep-research-os" else 0.84
        return GovernorDecision(
            query=query,
            detected_lane="deep-research-os",
            confidence=confidence,
            required_candidates=DEEP_RESEARCH_OS_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Deep research OS intent detected. Prefer /deep-research-os for "
                "research planning, wide decomposition, social listening, source "
                "ledgers, claim labels, anti-hallucination checks, and packaged synthesis."
            ),
            feedback_recommendation=(
                "If a narrow research route wins an explicit research OS query, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"...\" --correct \"deep-research-os\"`."
            ),
        )

    if is_ai_employee_os_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "ai-employee-os" else 0.84
        return GovernorDecision(
            query=query,
            detected_lane="ai-employee-os",
            confidence=confidence,
            required_candidates=AI_EMPLOYEE_OS_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "AI employee/company-agent intent detected. Prefer /ai-employee-os "
                "for role ownership, memory isolation, scoped integrations, event "
                "semantics, trust ladders, rollout gates, and model/personality checks."
            ),
            feedback_recommendation=(
                "If a generic agent audit or UX route wins this query, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"...\" --correct \"ai-employee-os\"`."
            ),
        )

    if is_productized_ai_service_os_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "productized-ai-service-os" else 0.84
        return GovernorDecision(
            query=query,
            detected_lane="productized-ai-service-os",
            confidence=confidence,
            required_candidates=PRODUCTIZED_AI_SERVICE_OS_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Productized AI service OS intent detected. Prefer the service OS route for "
                "intake, queue, proof sprint, quality gate, handoff, and offer packaging. "
                "Use /publishable-copy-gate only as a downstream public-copy quality check."
            ),
            feedback_recommendation=(
                "If a copy or generic revenue route wins this query, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"...\" --correct \"productized-ai-service-os\"`."
            ),
        )

    if is_mark_operating_tree_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.93 if chosen == "source-to-skill-system" else 0.84
        return GovernorDecision(
            query=query,
            detected_lane="mark-operating-tree",
            confidence=confidence,
            required_candidates=MARK_OPERATING_TREE_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Mark Kashef operating-tree intent detected. Prefer "
                "/source-to-skill-system as the compact front door for Mark "
                "source-to-system and self-improving workflow composition; keep "
                "/self-evolve and /skill-anneal as support routes instead of "
                "adding a broad Mark command. Selector: "
                f"{MARK_OPERATING_TREE_REFERENCE}."
            ),
            feedback_recommendation=(
                "If a generic front door or standalone Mark specialist wins this query, "
                "log it with `python3 execution/routing_intelligence.py misroute "
                "--request \"...\" --wrong \"...\" --correct \"source-to-skill-system\"`."
            ),
        )

    if is_extraction_governor_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "extraction-governor-agent" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="extraction-governance",
            confidence=confidence,
            required_candidates=EXTRACTION_GOVERNOR_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Extraction-governance intent detected. Prefer "
                "/extraction-governor-agent for source-to-capability triage, "
                "source grounding, duplicate-system checks, build-shape decision, "
                "and the next executable handoff."
            ),
            feedback_recommendation=(
                "If a generic extraction, knowledge, or source-to-skill route wins "
                "an explicit extraction-governor query, log it with `python3 "
                "execution/routing_intelligence.py misroute --request \"...\" "
                "--wrong \"...\" --correct \"extraction-governor-agent\"`."
            ),
        )

    if is_expert_composition_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.93 if chosen == "expert-composition-governor" else 0.84
        return GovernorDecision(
            query=query,
            detected_lane="expert-composition",
            confidence=confidence,
            required_candidates=EXPERT_COMPOSITION_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Expert-soup or full-arsenal composition intent detected. Prefer "
                "/expert-composition-governor so the system picks one owner, assigns "
                "bounded contribution slots, skips overlapping experts, and proves "
                "integration with a Composition Ledger."
            ),
            feedback_recommendation=(
                "If broad Autopilot or a component expert wins this query, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"...\" --correct \"expert-composition-governor\"`."
            ),
        )

    if is_front_door_choice_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "autopilot" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="front-door-choice",
            confidence=confidence,
            required_candidates=FRONT_DOOR_CHOICE_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Front-door choice intent detected. The user is asking the system "
                "to pick the right tool, command, workflow, or route, so prefer "
                "/autopilot before exposing a broad menu."
            ),
            feedback_recommendation=(
                "If a knowledge, tool-design, or specialist route wins this query, "
                "log it with `python3 execution/routing_intelligence.py misroute "
                "--request \"...\" --wrong \"...\" --correct \"autopilot\"`."
            ),
        )

    if is_explicit_menu_backend_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "orchestrate" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="menu-backend",
            confidence=confidence,
            required_candidates=MENU_BACKEND_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Explicit menu/options intent detected. Keep /orchestrate as the "
                "menu backend for ranked choices while /autopilot remains the "
                "front door for ambiguous tool-choice prompts."
            ),
            feedback_recommendation=(
                "If an explicit menu/options query stops ranking /orchestrate first, "
                "log it with `python3 execution/routing_intelligence.py misroute "
                "--request \"...\" --wrong \"...\" --correct \"orchestrate\"`."
            ),
        )

    if is_end_session_closeout_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "end-session" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="end-session-closeout",
            confidence=confidence,
            required_candidates=END_SESSION_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Session closeout or handoff intent detected. Prefer /end-session "
                "for closeout intelligence, run receipts, routing feedback, and "
                "retrieval handoff; keep /mission as a downstream continuity route."
            ),
            feedback_recommendation=(
                "If /mission outranks /end-session for closeout language, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"mission\" --correct \"end-session\"`."
            ),
        )

    if is_health_check_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "health-check" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="health-check-status",
            confidence=confidence,
            required_candidates=HEALTH_CHECK_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Read-only harness status or health-check intent detected. "
                "Prefer /health-check for the trust/status surface and activation "
                "detail; keep repair or drift-audit language on /autopilot or /system-audit."
            ),
            feedback_recommendation=(
                "If explicit harness-status language does not rank /health-check first, "
                "log it with `python3 execution/routing_intelligence.py misroute "
                "--request \"...\" --wrong \"...\" --correct \"health-check\"`."
            ),
        )

    if is_routing_intelligence_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "routing-intelligence" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="routing-intelligence-analytics",
            confidence=confidence,
            required_candidates=ROUTING_INTELLIGENCE_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Explicit routing analytics or scoreboard intent detected. "
                "Prefer /routing-intelligence for read-only routing evidence; "
                "keep repair or drift-audit language on /autopilot or /system-audit."
            ),
            feedback_recommendation=(
                "If explicit routing scoreboard language does not rank "
                "/routing-intelligence first, log it with `python3 "
                "execution/routing_intelligence.py misroute --request \"...\" "
                "--wrong \"...\" --correct \"routing-intelligence\"`."
            ),
        )

    if is_knowledge_librarian_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "knowledge-librarian" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="knowledge-librarian-pulse",
            confidence=confidence,
            required_candidates=KNOWLEDGE_LIBRARIAN_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Explicit library-pulse or reusable-context intent detected. "
                "Prefer /knowledge-librarian for prior decisions, solution docs, "
                "underused workflows, and one grounded start command."
            ),
            feedback_recommendation=(
                "If explicit library-pulse language does not rank "
                "/knowledge-librarian first, log it with `python3 "
                "execution/routing_intelligence.py misroute --request \"...\" "
                "--wrong \"...\" --correct \"knowledge-librarian\"`."
            ),
        )

    if is_skill_anneal_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "skill-anneal" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="skill-anneal",
            confidence=confidence,
            required_candidates=SKILL_ANNEAL_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Explicit skill prompt annealing intent detected. Prefer "
                "/skill-anneal for a bounded SKILL.md/component prompt repair; "
                "use /self-evolve for broader workflow evolution."
            ),
            feedback_recommendation=(
                "If explicit skill-anneal language does not rank /skill-anneal "
                "first, log it with `python3 execution/routing_intelligence.py "
                "misroute --request \"...\" --wrong \"...\" --correct "
                "\"skill-anneal\"`."
            ),
        )

    if is_self_evolve_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "self-evolve" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="self-evolution",
            confidence=confidence,
            required_candidates=SELF_EVOLVE_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Explicit measured workflow-evolution intent detected. Prefer "
                "/self-evolve when the work is feedback-backed, regression-aware, "
                "and bounded by a goal packet."
            ),
            feedback_recommendation=(
                "If explicit self-evolution language does not rank /self-evolve "
                "first, log it with `python3 execution/routing_intelligence.py "
                "misroute --request \"...\" --wrong \"...\" --correct "
                "\"self-evolve\"`."
            ),
        )

    if is_transfer_handoff_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "handoff" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="handoff-transfer",
            confidence=confidence,
            required_candidates=HANDOFF_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Transfer handoff intent detected. Prefer /handoff for focused "
                "new-session or cross-agent context packets; use /end-session "
                "when the whole session is being closed."
            ),
            feedback_recommendation=(
                "If /mission wins a transfer handoff request, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"mission\" --correct \"handoff\"`."
            ),
        )

    if is_steering_compass_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.94 if chosen == "steering-compass" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="steering-compass",
            confidence=confidence,
            required_candidates=STEERING_COMPASS_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Operator steering intent detected. Prefer /steering-compass for "
                "contextual next prompts, rationale, route suggestions, quality bars, "
                "and reusable operator learning."
            ),
            feedback_recommendation=(
                "If /mission wins a steering/next-prompt request, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"mission\" --correct \"steering-compass\"`."
            ),
        )

    if is_copy_quality_failure_intent(query):
        chosen = choose_route(query, combined) or "mission"
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.92 if chosen in COPY_QUALITY_STACK[:3] else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="copy-quality",
            confidence=confidence,
            required_candidates=COPY_QUALITY_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Copy-quality failure detected (Copy Gate inflation / ceremonial PASS / generic-flat output). "
                "Route to mission-level fix: red-team + five-input gate + calibrated Copy Gate discipline."
            ),
            feedback_recommendation=(
                "If `/publishable-copy-gate` wins this complaint, log it with "
                "`python3 execution/routing_intelligence.py misroute --request \"...\" "
                "--wrong \"publishable-copy-gate\" --correct \"mission\"`."
            ),
        )

    if is_repeatability_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.93 if chosen == "repeatability-spine" else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="repeatability",
            confidence=confidence,
            required_candidates=REPEATABILITY_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Repeatability or revision-recovery intent detected. Prefer "
                "/repeatability-spine so the run preserves the good example, "
                "classifies the failure, chooses the repair route, and leaves "
                "a regression guard."
            ),
            feedback_recommendation=(
                "If a literal keyword route or generic workflow wins this query, "
                "log it with `python3 execution/routing_intelligence.py misroute "
                "--request \"...\" --wrong \"...\" --correct \"repeatability-spine\"`."
            ),
        )

    if is_system_failure_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        required = SYSTEM_AUDIT_FIRST_STACK if is_system_audit_query(query) else SYSTEM_FAILURE_STACK
        confidence = 0.92 if chosen in required[:2] else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="system-failure",
            confidence=confidence,
            required_candidates=required,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Broken-system or Autopilot-failure intent detected. Prefer the "
                "control plane, audit, routing telemetry, health, and governance "
                "routes over unrelated specialist workflows."
            ),
            feedback_recommendation=(
                "If a specialist workflow wins this query, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"...\" --correct \"autopilot\"` or "
                "`--correct \"system-audit\"` for direct audit requests."
            ),
        )

    if is_revenue_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.9 if chosen in REVENUE_STACK[:2] else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="revenue",
            confidence=confidence,
            required_candidates=REVENUE_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Immediate-income intent detected. Prefer concrete buyer, offer, "
                "acquisition, proof, and delivery workflows over generic strategy."
            ),
            feedback_recommendation=(
                "If a generic or non-revenue workflow wins this query, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"...\" --correct \"first-10k\"`."
            ),
        )

    if is_liam_linkedin_lead_magnet_intent(query):
        chosen = choose_route(query, combined)
        skipped = flagged_routes_for(query, combined[:8])
        confidence = 0.9 if chosen == "liam-linkedin-lead-magnet" else 0.78
        return GovernorDecision(
            query=query,
            detected_lane="linkedin-ai-lead-magnet",
            confidence=confidence,
            required_candidates=LIAM_LINKEDIN_LEAD_MAGNET_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "AI-assisted LinkedIn lead magnet intent detected. Prefer "
                "/liam-linkedin-lead-magnet for monetizable expertise, strategic "
                "arbitrage, prompt set, first 20-post sprint, and offer bridge."
            ),
            feedback_recommendation=(
                "If a generic copy gate wins this query, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"...\" --correct \"liam-linkedin-lead-magnet\"`."
            ),
        )

    if is_skill_system_intent(query):
        chosen = choose_route(query, combined)
        allowed = set(SKILL_SYSTEM_STACK) | {"orchestrate", "knowledge-librarian"}
        skipped = tuple(route for route in combined[:8] if route and route not in allowed)
        confidence = 0.9 if chosen in SKILL_SYSTEM_STACK[:2] else 0.82
        return GovernorDecision(
            query=query,
            detected_lane="skill-system",
            confidence=confidence,
            required_candidates=SKILL_SYSTEM_STACK,
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route=chosen,
            skipped_routes=skipped,
            reason=(
                "Skill-system intent detected. Prefer source-to-system, extraction governance, "
                "mission governance, and measured evolution over random component workflows."
            ),
            feedback_recommendation=(
                "If a component workflow wins this query, log it with "
                "`python3 execution/routing_intelligence.py misroute --request "
                "\"...\" --wrong \"...\" --correct \"source-to-skill-system\"`."
            ),
        )

    chosen = combined[0] if combined else ""
    decision = GovernorDecision(
        query=query,
        detected_lane="general",
        confidence=0.65 if chosen else 0.0,
        required_candidates=(),
        command_menu_winners=menu_routes,
        workflow_router_winners=workflow_routes,
        chosen_route=chosen,
        skipped_routes=(),
        reason="No governor override detected; use normal router rank and workflow gates.",
        feedback_recommendation=(
            "If the route is generic, useless, or mismatched, log a correction with "
            "`routing_intelligence.py misroute`."
        ),
    )
    # Confidence floor: when intent is ambiguous but the user is talking about the system/router,
    # prefer the plan-first front door instead of trusting a narrow keyword match.
    normalized = normalize_query(query)
    if decision.confidence and decision.confidence < 0.75 and any(
        term in normalized for term in ("routing", "router", "workflow", "workflows", "skills", "autopilot", "system", "broken", "failing")
    ):
        return GovernorDecision(
            query=query,
            detected_lane="general",
            confidence=0.75,
            required_candidates=(),
            command_menu_winners=menu_routes,
            workflow_router_winners=workflow_routes,
            chosen_route="autopilot",
            skipped_routes=(),
            reason="Low-confidence route with system/meta language; default to /autopilot Plan Gate.",
            feedback_recommendation=decision.feedback_recommendation,
        )
    return decision


def _route_names_from_command_menu(query: str, limit: int) -> list[str]:
    import command_menu  # Imported lazily to avoid circular imports.

    workflows = command_menu.build_index()
    return [workflow.name for _, workflow in command_menu.search(workflows, query, limit)]


def _route_names_from_workflow_router(query: str, limit: int) -> list[str]:
    import workflow_router  # Imported lazily to avoid circular imports.

    return [workflow["name"] for _, workflow in workflow_router.search_workflows(query, limit)]


def render_decision(decision: GovernorDecision) -> str:
    def route_list(routes: Iterable[str]) -> str:
        values = [f"/{route}" for route in routes if route]
        return ", ".join(values) if values else "None"

    lines = [
        "# Routing Governor Evaluation",
        "",
        f"- **Detected lane**: {decision.detected_lane}",
        f"- **Confidence**: {decision.confidence:.2f}",
        f"- **Chosen route**: /{decision.chosen_route}" if decision.chosen_route else "- **Chosen route**: None",
        f"- **Reason**: {decision.reason}",
        f"- **Required candidates**: {route_list(decision.required_candidates)}",
        f"- **Command menu winners**: {route_list(decision.command_menu_winners)}",
        f"- **Workflow router winners**: {route_list(decision.workflow_router_winners)}",
        f"- **Flagged/skipped routes**: {route_list(decision.skipped_routes)}",
        f"- **Feedback/logging**: {decision.feedback_recommendation}",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate Antigravity routing through the governor layer.")
    sub = parser.add_subparsers(dest="command", required=True)
    evaluate_p = sub.add_parser("evaluate", help="Evaluate a query against command/workflow router winners.")
    evaluate_p.add_argument("query", help="User query or goal to evaluate.")
    evaluate_p.add_argument("--limit", type=int, default=8, help="Number of raw routes to inspect from each router.")
    evaluate_p.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    if args.command == "evaluate":
        menu_routes = _route_names_from_command_menu(args.query, args.limit)
        workflow_routes = _route_names_from_workflow_router(args.query, args.limit)
        decision = evaluate(args.query, menu_routes, workflow_routes)
        if args.json:
            print(json.dumps(asdict(decision), indent=2))
        else:
            print(render_decision(decision))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
