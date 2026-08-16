#!/usr/bin/env python3
"""Shared control-intent classifier for Codex operator routing.

This is deliberately broader than one-off phrase bindings. The failure mode it
prevents is letting system complaints fall through to BM25 expert-skill matches
just because the complaint used fresh wording.
"""

from __future__ import annotations

import re
from typing import Any

from antigravity_global_access import classify_global_access_intent


# Tiered evidence (2026-07-08 misfire fix): in THIS workspace "hook", "skill",
# "agent", "chain", "default" are content-craft vocabulary first and system
# vocabulary second. A single weak term + an everyday problem word ("why",
# "issue", "wrong") was routing client/content work to /system-audit at
# confidence 90+. Strong anchors are unambiguous control-plane words that may
# fire alone; weak surface terms only count in aggregate and never against a
# content-domain prompt.
STRONG_ANCHOR_TERMS = (
    "codex",
    "claude code",
    "claude parity",
    "claude-parity",
    "router",
    "routers",
    "skill router",
    "workflow router",
    "routing enforcer",
    "routing",
    "system-audit",
    "system audit",
    "wiring",
    "rewire",
    "hook wiring",
    "route wiring",
    "preflight",
    "verifier",
    "verifiers",
    "control plane",
    "control-plane",
    "front door",
    "settings.json",
    "harness",
    "misfire",
    "misfires",
    "misfiring",
    "source-command",
    "session ledger",
    "cost gate",
    "google antigravity",
    "codex antigravity",
    "global bridge",
    "prompt hook",
)

# "hook(s)" is only a system anchor next to a system verb — content hooks
# grip/convert/land; system hooks fire/block/inject/enforce/gate.
HOOK_SYSTEM_RE = re.compile(
    r"\bhooks?\b[^.!?]{0,60}?\b(fir\w*|block\w*|inject\w*|enforc\w*|wir\w*|gat\w*|trigger\w*|suppress\w*)\b"
    r"|\b(fir\w*|block\w*|inject\w*|enforc\w*|wir\w*|gat\w*|trigger\w*|suppress\w*)\b[^.!?]{0,60}?\bhooks?\b"
)

SYSTEM_SURFACE_TERMS = (
    "autopilot",
    "hook",
    "hooks",
    "route",
    "routes",
    "workflow",
    "workflows",
    "skill",
    "skills",
    "agent",
    "agents",
    "default",
    "defaults",
    "settings",
    "wrapper",
    "wrappers",
    "wired",
    "linked",
    "linking",
    "chained",
    "chain",
    "handcuffed",
    "selective language",
    "workspace",
    "workspaces",
    "global",
    "bridge",
)

# Content-domain context: if the prompt lives in deliverable land, weak-only
# evidence must never route it to control-plane repair.
CONTENT_DOMAIN_TERMS = (
    "post",
    "posts",
    "email",
    "emails",
    "copy",
    "headline",
    "headlines",
    "linkedin",
    "reel",
    "reels",
    "video",
    "script",
    "newsletter",
    "substack",
    "essay",
    "article",
    "carousel",
    "listing",
    "client",
    "program",
    "workout",
    "fitness",
    "offer",
    "funnel",
    "landing page",
    "brand",
    "campaign",
    "converting",
    "conversion",
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
    "failing",
    "drift",
    "drifted",
    "global/workspace drift",
    "split workspace",
    "split workspaces",
    "not-firing",
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
    "obsolete",
    "nonexistent",
    "missing",
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
    "apply",
    "run",
    "use",
    "execute",
    "invoke",
    "test",
    "evaluate",
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


def strip_explicit_invocation_artifacts(value: str) -> str:
    """Remove explicit skill/link invocation plumbing before control matching.

    Prompts can begin with app-style or markdown skill links such as:
    ``[$raw-intent-bridge](/Users/.../.codex/skills/raw-intent-bridge/SKILL.md)``.
    The path contains words like ``skills`` even when the user is asking for
    normal client work. If the same prompt mentions domain risks like
    "copyright issues", the unstripped path looks like a system complaint
    ("skill" + "issues") and incorrectly routes to /system-audit.
    """

    def replace_markdown_link(match: re.Match[str]) -> str:
        label = match.group(1)
        href = match.group(2)
        href_low = href.lower()
        if (
            "/skills/" in href_low
            or "/.codex/skills/" in href_low
            or "/.agents/skills/" in href_low
            or href_low.endswith("/skill.md")
            or href_low.endswith("skill.md")
            or href_low.startswith("app://")
        ):
            return label
        return match.group(0)

    stripped = re.sub(r"\[([^\]]+)\]\(([^)]*)\)", replace_markdown_link, value)
    stripped = re.sub(
        r"/\S*(?:\.codex|\.agents)?/skills/\S*/SKILL\.md",
        " ",
        stripped,
        flags=re.IGNORECASE,
    )
    stripped = re.sub(r"\s+", " ", stripped)
    return stripped.strip()


def _hits(query: str, terms: tuple[str, ...]) -> list[str]:
    return [term for term in terms if term in query]


def _word_hits(query: str, terms: tuple[str, ...]) -> list[str]:
    """Word-boundary matching — 'chain' must not hit 'blockchain', 'issue' not 'tissue'."""

    hits = []
    for term in terms:
        pattern = r"\b" + re.escape(term).replace(r"\ ", r"\s+") + r"\b"
        if re.search(pattern, query):
            hits.append(term)
    return hits


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
    has_direct_task_request = any(
        re.search(rf"\b{re.escape(term)}\b", query) for term in DELIVERABLE_VERBS
    )
    return has_status_question and has_repair_state and has_negative_or_mismatch and not has_direct_task_request


def _looks_like_bare_failed_repair_complaint(query: str) -> bool:
    """Preserve the narrow operator-core complaint without catching task reviews.

    The control plane intentionally owns bare aftermath complaints such as
    "nothing was fixed that I wanted", even when the user does not repeat the
    words router, hook, or Codex. Keep that contract explicit instead of letting
    every "show what changed; do not ..." prompt inherit system-audit.
    """

    has_failed_result = bool(
        re.search(
            r"\b(nothing|none)\b[^.!?]{0,80}\b(fixed|repaired|changed|resolved|implemented)\b",
            query,
        )
    )
    has_operator_mismatch = bool(re.search(r"\b(wanted|asked|expected)\b", query))
    return has_failed_result and has_operator_mismatch


def classify_control_intent(prompt: str) -> dict[str, Any]:
    """Return a route recommendation for control-plane/repeatability prompts.

    Shape beats exact phrase: system-surface evidence plus complaint/action
    evidence should route to /system-audit and suppress expert suggestions.
    """

    q = normalize(strip_explicit_invocation_artifacts(prompt))
    global_access = classify_global_access_intent(q)
    if global_access["matched"]:
        return {
            "route": global_access["route"],
            "lane": global_access["lane"],
            "reason": global_access["reason"],
            "evidence": global_access["evidence"],
            "confidence": global_access["confidence"],
        }
    # Explicit slash-workflow invocation ("run /extract-forge …", "… and /watch <url>"):
    # the user is deliberately DRIVING the control plane, not complaining about it
    # (2026-07-13 misfire: an /extract-forge mission carrying "orchestrate" + "we're
    # not doing 12 separate workflows" routed to /autopilot as a broken-system
    # complaint). This only suppresses the broad-front-door and general-distress
    # branches — anchored complaints ("the router keeps misfiring, fix it") still
    # fire via anchored_match even when a slash command is present. URL paths
    # (youtube.com/watch) don't match: the slash must follow start-of-text or
    # whitespace, optionally led by an invocation verb.
    explicit_workflow_invoke = bool(
        re.search(r"(?:^|\s)(?:run|use|execute|invoke)\s+/[a-z][a-z0-9-]{2,}\b", q)
        or re.search(r"(?:^|\s)/[a-z][a-z0-9-]{2,}(?=\s|$)", q)
    )
    concrete_deliverable = any(
        re.search(rf"\b{re.escape(term)}\b", q) for term in DELIVERABLE_VERBS
    )
    anchor_hits = _word_hits(q, STRONG_ANCHOR_TERMS)
    if HOOK_SYSTEM_RE.search(q):
        anchor_hits.append("hook+system-verb")
    surface_hits = _word_hits(q, SYSTEM_SURFACE_TERMS)
    problem_hits = _word_hits(q, SYSTEM_PROBLEM_TERMS)
    action_hits = _word_hits(q, SYSTEM_ACTION_TERMS)
    content_context = bool(_word_hits(q, CONTENT_DOMAIN_TERMS))
    repeatability_hits = _hits(q, REPEATABILITY_TERMS)
    # A repair/status review needs actual control-surface evidence. Without
    # this guard, ordinary capability requests such as "apply the overlay,
    # show what changed, do not promote" look like failed system repairs.
    # Preserve the narrow bare aftermath complaint required by Operator Core.
    bare_failed_repair_complaint = _looks_like_bare_failed_repair_complaint(q)
    repair_status_review = (
        _looks_like_repair_status_review(q)
        and not content_context
        and (bool(anchor_hits or surface_hits) or bare_failed_repair_complaint)
    )

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

    # source-command-X is only a system-control intent if there's a PROBLEM being reported.
    # If it's just "source-command-orchestrate show ranked options", that's a normal use,
    # not a wiring complaint. Don't confuse explicit command invocation with repair requests.

    # Check if this is an explicit command invocation (source-command-X pattern).
    # If so, extract what comes after "source-command-" to avoid false positives
    # (e.g., "source-command-health-check" contains "check" but that's the command name).
    explicit_command_match = re.search(r"source-command-([\w-]+)", q)
    if explicit_command_match:
        command_name = explicit_command_match.group(1)
        # Check for explicit problems or actions NOT within the command name itself
        # Remove the command name from consideration to avoid false flags
        q_without_command = q.replace(f"source-command-{command_name}", "").strip()
        has_problem_after_command = any(term in q_without_command for term in problem_hits)
        has_action_after_command = any(term in q_without_command for term in action_hits)
        explicit_command_invoke = not (has_problem_after_command or has_action_after_command)
    else:
        explicit_command_invoke = False

    # Don't treat "wrong route" / "wrong workflow" as system-failure.
    # Those are repeatability intents (preserved via routing_governor).
    wrong_route_complaint = any(
        phrase in q for phrase in ("wrong route", "wrong workflow", "route picked the wrong")
    )
    broad_front_door_surfaces = (
        "autopilot",
        "orchestration",
        "orchestrate",
        "router",
        "routing intelligence",
        "knowledge library",
        "harness",
        "self-evolve",
        "skill-anneal",
        "source-to-skill-system",
        "extraction-governor-agent",
        "repeatability-spine",
        "expert-composition-governor",
    )
    broad_front_door_problems = (
        "broken",
        "wrong",
        "useless",
        "not doing",
        "not working",
        "mutating without proof",
        "rewriting everything",
        "creates bloat",
        "writes state automatically",
        "inventing findings",
        "creates expert soup",
    )
    broad_front_door_complaint = (
        any(term in q for term in broad_front_door_surfaces)
        and any(term in q for term in broad_front_door_problems)
        and not action_hits
        # 2026-07-13 guards: a deliverable-laden mission ("create", "make",
        # "write") or an explicit /workflow invocation is work being driven,
        # not a system being reported broken — parity with weak_aggregate_match.
        and not concrete_deliverable
        and not content_context
        and not explicit_workflow_invoke
        and "codex" not in q
        and "hook" not in q
        and "hooks" not in q
        and "default" not in q
        and "defaults" not in q
        and "wiring" not in q
        and "wired" not in q
        and "source-command-" not in q
    )

    if broad_front_door_complaint:
        return {
            "route": "autopilot",
            "lane": "system-failure",
            "reason": "Broad broken-system complaints should enter the Codex front door before specialist repair.",
            "evidence": [
                term for term in broad_front_door_surfaces if term in q
            ][:4],
            "confidence": 90,
        }

    source_command_control = (
        "source-command-" in q and
        (problem_hits or action_hits or surface_hits) and
        not explicit_command_invoke
    )
    selective_language_complaint = "selective language" in q and (problem_hits or "linked" in q or "linking" in q)
    general_distress = any(term in q for term in GENERAL_DISTRESS_TERMS)

    # Tiered shape match (2026-07-08): a strong anchor + any problem/action
    # evidence fires; weak surface terms alone need aggregate evidence (2+
    # distinct surfaces, a problem AND an action) and lose to deliverable or
    # content-domain context. This is what stops "why is this post not
    # converting, check the hook" from routing to /system-audit.
    anchored_match = bool(anchor_hits and (problem_hits or action_hits))
    weak_lemmas = {t.rstrip("s") for t in surface_hits}
    weak_aggregate_match = (
        len(weak_lemmas) >= 2
        and bool(problem_hits)
        and bool(action_hits)
        and not concrete_deliverable
        and not content_context
    )
    shape_match = (
        (anchored_match or weak_aggregate_match)
        and not wrong_route_complaint
        and not explicit_command_invoke
    )

    # Read-only health/status ask (2026-07-15): "health check" / "harness
    # status" with ZERO problem language is a status QUESTION, not a failure
    # complaint — /health-check owns it per its own workflow contract ("use
    # /health-check for explicit status and health questions"). Without this
    # guard the harness+check anchor fired system-audit@93 and outranked the
    # governor's correct health-check pick (caught by two verifiers).
    health_status_ask = (
        (
            ("health" in q and ("check" in q or "status" in q or "vitals" in q))
            or "harness status" in q
        )
        and not problem_hits
        and not general_distress
        and not any(term in q for term in ("repair", "fix", "audit", "broken"))
    )
    if health_status_ask:
        return {
            "route": "health-check",
            "lane": "status",
            "reason": "Explicit read-only health/status question routes to /health-check, not control-plane repair.",
            "evidence": [t for t in ("health", "check", "status", "harness", "vitals") if t in q][:4],
            "confidence": 92,
        }

    if (
        repair_status_review
        or source_command_control
        or selective_language_complaint
        or shape_match
    ):
        return {
            "route": "system-audit",
            "lane": "system-failure",
            "reason": "System, route, hook, default, or wiring complaint should use control-plane repair before expert matching.",
            "evidence": (
                (["repair/status review"] if repair_status_review else [])
                + anchor_hits
                + surface_hits
                + problem_hits
                + action_hits
            )[:8],
            "confidence": 90
            + min(
                (1 if repair_status_review else 0)
                + len(anchor_hits) * 2
                + len(surface_hits)
                + len(problem_hits)
                + len(action_hits),
                9,
            ),
        }

    if general_distress and not concrete_deliverable and not explicit_workflow_invoke:
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
