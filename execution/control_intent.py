#!/usr/bin/env python3
"""Shared control-intent classifier for Codex operator routing.

This is deliberately broader than one-off phrase bindings. The failure mode it
prevents is letting system complaints fall through to BM25 expert-skill matches
just because the complaint used fresh wording.
"""

from __future__ import annotations

import re
from typing import Any


SYSTEM_SURFACE_TERMS = (
    "codex",
    "claude code",
    "hook",
    "hooks",
    "route",
    "routes",
    "routing",
    "workflow",
    "workflows",
    "skill",
    "skills",
    "agent",
    "agents",
    "default",
    "defaults",
    "settings",
    "front door",
    "preflight",
    "prompt hook",
    "wrapper",
    "wrappers",
    "wired",
    "wiring",
    "linked",
    "linking",
    "chained",
    "chain",
    "handcuffed",
    "source-command",
    "selective language",
)

SYSTEM_PROBLEM_TERMS = (
    "nonsense",
    "issue",
    "issues",
    "problem",
    "problems",
    "wrong",
    "broken",
    "break",
    "blocking",
    "not firing",
    "did not fire",
    "didn't fire",
    "did not kick in",
    "didn't kick in",
    "not working",
    "doesn't make sense",
    "does not make sense",
    "what's going on",
    "what is going on",
    "why",
    "random",
    "irrelevant",
    "off target",
    "unusable",
    "unusable to do anything",
    "confused",
    "start from scratch",
    "restart",
    "restarted",
    "causing",
    "should not",
    "shouldn't",
    "no business",
    "handcuffed",
    "chained",
)

GENERAL_DISTRESS_TERMS = (
    "things are not working",
    "things aren't working",
    "things are broken",
    "so broken",
    "everything is broken",
    "almost unusable",
    "unusable",
    "becoming unusable",
    "start from scratch",
    "get something restarted",
    "restart",
    "confused",
    "so confused",
    "random assumptions",
    "not able to replicate",
)

DELIVERABLE_VERBS = (
    "write",
    "draft",
    "create",
    "generate",
    "build",
    "design",
    "research",
    "compose",
    "produce",
    "rewrite",
    "make",
    "turn",
    "convert",
)

SYSTEM_ACTION_TERMS = (
    "audit",
    "check",
    "repair",
    "fix",
    "diagnose",
    "debug",
    "unwire",
    "unlink",
    "dechain",
    "suppress",
)

REPEATABILITY_TERMS = (
    "copied over everything",
    "copied everything over",
    "previous session import",
    "import from my previous session",
    "same caliber",
    "same calibre",
    "caliber or level",
    "calibre or level",
    "massive difference",
    "cannot repeat",
    "can't repeat",
    "lost the magic",
    "revision got worse",
    "got worse again",
    "golden sample",
)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def _hits(query: str, terms: tuple[str, ...]) -> list[str]:
    return [term for term in terms if term in query]


def _looks_like_repair_status_review(query: str) -> bool:
    """Detect post-repair/status review turns without relying on exact complaints."""

    has_status_question = bool(
        re.search(r"\b(what|why|how|where|when|show|tell|explain)\b", query)
        or "from the looks" in query
        or "looks like" in query
    )
    has_repair_state = bool(
        re.search(
            r"\b(fix|fixed|repair|repaired|patch|patched|implemented|done|changed|working|resolved)\b",
            query,
        )
    )
    has_negative_or_mismatch = bool(
        re.search(
            r"\b(nothing|not|no|never|didn't|did not|wasn't|was not|isn't|is not|wanted|asked)\b",
            query,
        )
    )
    has_direct_task_request = bool(
        re.search(
            r"\b(write|draft|create|generate|build|design|research|compose|produce|rewrite|make|turn|convert)\b",
            query,
        )
    )
    return has_status_question and has_repair_state and has_negative_or_mismatch and not has_direct_task_request


def classify_control_intent(prompt: str) -> dict[str, Any]:
    """Return a route recommendation for control-plane/repeatability prompts.

    Shape beats exact phrase: system-surface evidence plus complaint/action
    evidence should route to /system-audit and suppress expert suggestions.
    """

    q = normalize(prompt)
    surface_hits = _hits(q, SYSTEM_SURFACE_TERMS)
    problem_hits = _hits(q, SYSTEM_PROBLEM_TERMS)
    action_hits = _hits(q, SYSTEM_ACTION_TERMS)
    repeatability_hits = _hits(q, REPEATABILITY_TERMS)
    repair_status_review = _looks_like_repair_status_review(q)

    embedded_system_repair_plan = bool(
        repeatability_hits
        and surface_hits
        and action_hits
        and any(
            term in q
            for term in (
                "implement this plan",
                "repair plan",
                "routing/wiring",
                "routing and wiring",
                "control plane",
                "control-plane",
                "preflight",
                "verifier",
                "verifiers",
                "hook probes",
                "route probes",
            )
        )
    )
    if repeatability_hits and not embedded_system_repair_plan:
        return {
            "route": "repeatability-spine",
            "lane": "output-regression",
            "reason": "Prior-session, golden-run, or repeatability language needs preservation before repair.",
            "evidence": repeatability_hits[:5],
            "confidence": 90 + min(len(repeatability_hits), 9),
        }

    source_command_control = "source-command-" in q and (problem_hits or action_hits or surface_hits)
    selective_language_complaint = "selective language" in q and (problem_hits or "linked" in q or "linking" in q)
    shape_match = bool(surface_hits and (problem_hits or action_hits))
    multi_surface_complaint = len(surface_hits) >= 2 and bool(problem_hits)
    general_distress = any(term in q for term in GENERAL_DISTRESS_TERMS)
    concrete_deliverable = any(re.search(rf"\b{re.escape(term)}\b", q) for term in DELIVERABLE_VERBS)

    if (
        repair_status_review
        or source_command_control
        or selective_language_complaint
        or shape_match
        or multi_surface_complaint
    ):
        return {
            "route": "system-audit",
            "lane": "system-failure",
            "reason": "System, route, hook, default, or wiring complaint should use control-plane repair before expert matching.",
            "evidence": (
                (["repair/status review"] if repair_status_review else [])
                + surface_hits
                + problem_hits
                + action_hits
            )[:8],
            "confidence": 90
            + min(
                (1 if repair_status_review else 0)
                + len(surface_hits)
                + len(problem_hits)
                + len(action_hits),
                9,
            ),
        }

    if general_distress and not concrete_deliverable:
        return {
            "route": "autopilot",
            "lane": "system-failure",
            "reason": "Broad operator distress should enter the Codex front door before specialist workflows.",
            "evidence": [term for term in GENERAL_DISTRESS_TERMS if term in q][:5],
            "confidence": 88,
        }

    return {
        "route": "",
        "lane": "",
        "reason": "",
        "evidence": [],
        "confidence": 0,
    }
