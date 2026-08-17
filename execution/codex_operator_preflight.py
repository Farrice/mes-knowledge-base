#!/usr/bin/env python3
"""Google Antigravity raw-intent preflight for Codex Desktop.

This is the manual hook-equivalent entry point for Codex surfaces. Claude Code
hooks remain physical there; in Codex Desktop this command makes the gate
visible and verifiable without claiming automatic hook enforcement.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT / "execution") not in sys.path:
    sys.path.insert(0, str(ROOT / "execution"))

from co_creative_launchpad import build_launchpad  # noqa: E402
from control_intent import classify_control_intent  # noqa: E402
from workflow_router import CONTROL_ROUTE_KEYWORDS, search_workflows  # noqa: E402


SUPPORT_GATES = {
    "mission": ["system-audit", "health-check"],
    "source-to-skill-system": ["extraction-governor-agent", "knowledge-librarian"],
    "system-audit": ["health-check", "routing-intelligence", "repeatability-spine"],
    "steering-compass": ["recommend", "validate-intent"],
    "expert-composition-governor": ["system-audit", "routing-intelligence"],
    "extraction-governor-agent": ["source-to-skill-system", "knowledge-librarian"],
    "repeatability-spine": ["system-audit"],
    "high-taste-writing-os": ["copy-engine", "publishable-copy-gate", "repeatability-spine", "content-finish-gate"],
    "high-taste-os": ["copy-engine", "publishable-copy-gate", "repeatability-spine", "content-finish-gate"],
    "knowledge-librarian": ["routing-intelligence"],
    "orchestrate": ["system-audit", "routing-intelligence"],
}

RISK_TERMS = {
    "external write": ["publish", "send", "email", "dm ", "post ", "connector write", "notion write", "drive write"],
    "destructive action": ["delete", "wipe", "remove all", "purge", "destroy", "reset --hard"],
    "global scope": ["~/.codex", "global codex", "codex antigravity", "/users/farricecain/codex antigravity"],
    "paid or quota-heavy tool": [
        "paid api",
        "paid tool",
        "paid tools",
        "quota-heavy",
        "quota heavy",
        "buy credits",
        "purchase credits",
        "spend $",
        "spend money",
        "fal",
        "kling",
        "seedance",
        "deep research api",
        "gemini deep research",
        "perplexity research",
    ],
    "real subagents": ["spawn subagent", "real subagent", "parallel agents", "delegate to agents"],
}

EXECUTION_BIAS_ROUTES = {"system-audit"}

SUBAGENT_APPROVAL_TERMS = (
    "authorize",
    "read-only",
    "diagnostic",
    "worker count",
    "scope",
    "deny list",
    "halt condition",
    "no further subagents",
)

STOP_CONDITIONS = [
    "external write, publishing, outreach, or connector write",
    "destructive cleanup or broad delete/archive/reset",
    "global ~/.codex or Codex Antigravity mutation",
    "paid or quota-heavy tool use without cost-gate approval",
    "real subagent edits or further subagent spawning without explicit authorization",
]


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def clarity_score(intent: str) -> int:
    q = normalize(intent)
    score = 0
    if any(term in q for term in ("build", "create", "fix", "repair", "audit", "run", "write", "rewrite", "revise", "turn", "implement", "use")):
        score += 1
    if any(term in q for term in ("for ", "audience", "client", "user", "customer", "buyer", "prospect", "avatar", "operator", "farrice")):
        score += 1
    if any(term in q for term in ("because", "context", "workspace", "google antigravity", "codex", "research", "source", "brief", "pdp")):
        score += 1
    if any(
        term in q
        for term in (
            "done",
            "success",
            "prove",
            "verify",
            "quality",
            "bar",
            "acceptance",
            "production-ready",
            "production ready",
            "copy gate",
            "pass the copy gate",
            "passes the copy gate",
            "generic and scientific",
            "stating facts rather than appealing",
            "stating facts instead of appealing",
            "human psychology and copywriting",
            "research word banks",
            "research word bank",
            "customer avatar language",
            "avatar language",
            "word banks",
            "word bank",
            "script is just an explanation",
            "script is explanation",
            "like notes and not actually copywriting",
            "not actually copywriting",
            "notes pretending to be copy",
            "one fix breaks something else",
            "final version got worse again",
            "got worse again with the script",
            "previous session import",
            "import from my previous session",
            "same caliber",
            "same calibre",
            "caliber or level",
            "calibre or level",
            "massive difference",
            "brief gets worse",
            "brief gets worse and worse",
            "brief just gets worse",
            "gets worse and worse",
            "codex is not working",
            "codex is not working in my workspace",
            "no point in using codex",
            "not working at all",
            "blocking hooks",
            "blocked hooks",
            "wrong defaults",
            "wrong default routing",
            "routing wrong defaults",
            "default settings",
            "not wired",
            "should not be wired",
            "wired together",
            "wiring",
            "hooks or routes",
            "handcuffed",
            "chained together",
            "check and repair",
            "audit and repair",
            "thin wrappers",
            "too many thin wrappers",
            "match claude code",
            "mirror claude code",
            "claude parity",
            "claude-parity",
            "without breaking my workspace",
            "without breaking claude code",
            "not trying to break anything",
            "context issue",
            "context issue and not usable",
            "not usable",
            "paid-ad voiceover",
            "paid ad voiceover",
            "spoken ad copy",
            "recordable as-is",
            "recordable as is",
            "vo-only gate",
            "vo only gate",
        )
    ):
        score += 1
    if len(re.findall(r"[a-z0-9][a-z0-9-]*", q)) >= 8:
        score += 1
    return max(1, min(5, score))


def _has_requested_action(intent: str, action_pattern: str) -> bool:
    """Return True when an action is requested rather than explicitly denied."""
    denial_scope_words = {
        "a",
        "all",
        "an",
        "and",
        "any",
        "approved",
        "automatic",
        "automatically",
        "broad",
        "broadly",
        "delete",
        "deleted",
        "deleting",
        "deletion",
        "deletions",
        "destructive",
        "external",
        "file",
        "files",
        "further",
        "local",
        "locally",
        "material",
        "materials",
        "original",
        "originals",
        "or",
        "publish",
        "published",
        "publishing",
        "public",
        "the",
        "unauthorized",
        "unapproved",
        "user",
    }
    for match in re.finditer(action_pattern, intent):
        prefix = intent[: match.start()]
        local_prefix = re.split(
            r"[.;!?]|\b(?:but|however|then)\b",
            prefix,
        )[-1]
        deny_matches = list(
            re.finditer(r"\b(?:do not|don't|never|without|no)\b", local_prefix)
        )
        if not deny_matches:
            return True
        between = local_prefix[deny_matches[-1].end() :]
        between_words = re.findall(r"[a-z]+", between)
        if any(word not in denial_scope_words for word in between_words):
            return True
    return False


def risk_reasons(intent: str) -> list[str]:
    q = normalize(intent)
    reasons: list[str] = []
    for label, terms in RISK_TERMS.items():
        literal_terms = tuple(term for term in terms if term not in {"publish", "delete"})
        requested = any(term in q for term in literal_terms)
        if label == "external write":
            requested = requested or _has_requested_action(
                q,
                r"\bpublish(?:es|ed|ing)?\b",
            )
        elif label == "destructive action":
            requested = requested or _has_requested_action(
                q,
                r"\bdelet(?:e|es|ed|ing|ion|ions)\b",
            )
        if requested:
            reasons.append(label)
    if "real subagents" in reasons and subagent_approval_packet_present(intent):
        reasons.remove("real subagents")
    return reasons


def subagent_approval_packet_present(intent: str) -> bool:
    q = normalize(intent)
    if not any(term in q for term in ("subagent", "parallel agents", "delegate to agents")):
        return False
    return all(term in q for term in SUBAGENT_APPROVAL_TERMS)


def control_hits(intent: str) -> list[tuple[int, str, str]]:
    q = normalize(intent)
    hits: list[tuple[int, str, str]] = []
    classified = classify_control_intent(intent)
    if classified["route"]:
        evidence = ", ".join(classified["evidence"][:3]) or classified["reason"]
        hits.append((int(classified["confidence"]) + 40, str(classified["route"]), evidence))
    for route, phrases in CONTROL_ROUTE_KEYWORDS.items():
        for phrase in phrases:
            if phrase in q:
                hits.append((100 + len(phrase), route, phrase))
                break
    return sorted(hits, key=lambda item: (-item[0], item[1]))


def route_candidates(intent: str, top_n: int = 5) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    seen: set[str] = set()
    for score, route, phrase in control_hits(intent):
        candidates.append(
            {
                "route": route,
                "score": score,
                "source": "control-route-boost",
                "matched": phrase,
                "description": f"Control-plane trigger matched: {phrase}",
            }
        )
        seen.add(route)

    for score, wf in search_workflows(intent, top_n=top_n + 5):
        route = wf["name"]
        if route in seen:
            continue
        candidates.append(
            {
                "route": route,
                "score": score,
                "source": "workflow-router",
                "matched": "",
                "description": wf["description"],
            }
        )
        seen.add(route)
        if len(candidates) >= top_n:
            break
    return candidates[:top_n]


def classify_lane(intent: str, route: str) -> str:
    q = normalize(intent)
    classified = classify_control_intent(intent)
    if classified["lane"]:
        return str(classified["lane"])
    if route == "system-audit" or any(
        term in q
        for term in (
            "not firing",
            "broken harness",
            "ineffective",
            "disjointed",
            "claude code works better",
            "not working like claude code",
            "match claude code",
            "mirror claude code",
            "claude parity",
            "claude-parity",
            "blocking hooks",
            "blocked hooks",
            "wrong defaults",
            "wrong default routing",
            "routing wrong defaults",
            "default settings",
            "not wired",
            "should not be wired",
            "wired together",
            "wiring",
            "hooks or routes",
            "handcuffed",
            "chained together",
            "check and repair",
            "audit and repair",
            "thin wrappers",
            "too many thin wrappers",
            "without breaking my workspace",
            "without breaking claude code",
            "not trying to break anything",
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
            "pre-flight did not kick in",
            "pre-flight didn't kick in",
            "preflight did not kick in",
            "preflight didn't kick in",
            "orchestration is not doing its job",
            "orchestration isn't doing its job",
            "orchestration not doing its job",
            "wording not routing",
            "not routing even when obvious",
            "not routing even when it is obvious",
            "routing even when obvious",
            "routing even when it is obvious",
            "have to be so deterministic",
            "too deterministic",
            "shooting in the dark",
            "draining",
            "explains instead of executing",
            "safe local next actions",
            "execution bias",
            "hands back prompts",
            "plans instead of acting",
        )
    ):
        return "system-failure"
    if route == "repeatability-spine" or any(
        term in q
        for term in (
            "copied over everything",
            "copied everything over",
            "copying everything over",
            "previous session import",
            "import from my previous session",
            "import from previous session",
            "same caliber",
            "same calibre",
            "caliber or level",
            "calibre or level",
            "massive difference",
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
            "one fix breaks something else",
            "one fix and then something else breaks",
            "apply one fix and then something else breaks",
        )
    ):
        return "output-regression"
    if route in {"source-to-skill-system", "extraction-governor-agent"}:
        return "source-system"
    if route in {"high-taste-writing-os", "high-taste-os"}:
        return "output-quality"
    if route in {"steering-compass", "knowledge-librarian"}:
        return "steering"
    if route in {"mission", "orchestrate"}:
        return "mission-control"
    return "general"


def manual_gates(route: str, risks: list[str]) -> list[dict[str, str]]:
    gates = [
        {
            "gate": "Routing binding",
            "status": "required",
            "check": f"python3 execution/routing_enforcer.py check --request \"<raw intent>\" --workflow {route} --no-log",
        },
        {
            "gate": "Codex hook reality",
            "status": "required",
            "check": ".codex/hooks.json must use codex_hook_runner.py and current-root hook states must be trusted and not explicitly disabled; verify with execution/verify_google_operator_core.py.",
        },
        {
            "gate": "Cost gate",
            "status": "conditional",
            "check": "Before paid or quota-heavy APIs: python3 execution/cost_gate.py check --service <id>",
        },
        {
            "gate": "Finalize debt",
            "status": "conditional",
            "check": "If an expert deliverable is produced, run chain_runner.py finalize from the repo root.",
        },
        {
            "gate": "Run receipt",
            "status": "recommended",
            "check": "After meaningful system work: python3 execution/run_receipt.py --query \"...\" --route <route> --status \"PASS|PARTIAL|BLOCKED\" ...",
        },
    ]
    if risks:
        gates.insert(
            0,
            {
                "gate": "Human approval",
                "status": "blocked",
                "check": "Approval required before: " + ", ".join(risks),
            },
        )
    return gates


def verification_plan(route: str) -> list[str]:
    plan = [
        f"python3 execution/workflow_router.py search \"<raw intent>\" should rank /{route} first.",
        f"python3 execution/routing_enforcer.py check --request \"<raw intent>\" --workflow {route} --no-log should return valid true when a binding applies.",
    ]
    if route in {"mission", "source-to-skill-system", "system-audit", "steering-compass", "expert-composition-governor", "repeatability-spine"}:
        plan.append("python3 execution/verify_google_operator_core.py should pass hot command, routing, preflight, receipt, and manual-gate checks.")
    if route == "steering-compass":
        plan.append("python3 execution/contextual_next_prompts.py --objective \"<objective>\" should emit Use Now, Harden, Expand.")
    return plan


def safe_local_execution_default(route: str, lane: str, risks: list[str]) -> bool:
    return not risks and route in EXECUTION_BIAS_ROUTES and lane == "system-failure"


def local_next_action(intent: str, route: str, decision: dict[str, Any], approved_subagents: bool) -> dict[str, Any]:
    if decision["status"] == "Blocked":
        return {
            "mode": "approval_required",
            "owner": route,
            "action": "Stop and ask for the smallest approval needed before changing local state.",
            "first_command": "",
            "verifier_command": "",
            "receipt_required": False,
            "subagent_policy": "No real Codex subagents until explicitly authorized.",
            "stop_conditions": STOP_CONDITIONS,
        }
    if decision["status"] == "Needs Judgment":
        return {
            "mode": "sharpen_then_execute",
            "owner": route,
            "action": "Ask only the execution-changing question, then run the safe local verifier-backed path.",
            "first_command": f"python3 execution/workflow_router.py search \"{intent}\"",
            "verifier_command": f"python3 execution/routing_enforcer.py check --request \"{intent}\" --workflow {route} --no-log",
            "receipt_required": False,
            "subagent_policy": "Read-only diagnostic subagents only when Farrice explicitly authorizes them for this run.",
            "stop_conditions": STOP_CONDITIONS,
        }
    return {
        "mode": "patch_and_verify",
        "owner": route,
        "action": (
            "Run the next safe workspace-local repair step now: inspect the failing proof, patch only the local owner surface, "
            "rerun the verifier, and write a run receipt. Do not hand Farrice a prompt when the next step is safe and local."
        ),
        "first_command": f"python3 execution/workflow_router.py search \"{intent}\"",
        "verifier_command": "python3 execution/verify_google_operator_core.py",
        "receipt_required": True,
        "subagent_policy": (
            "Read-only diagnostic subagents are authorized for this run only when the approval packet names worker count, "
            "read-only scope, deny list, halt condition, and no further subagents; main thread owns edits and integration."
            if approved_subagents
            else "Main thread owns edits; subagents, if later authorized, are read-only diagnostics."
        ),
        "stop_conditions": STOP_CONDITIONS,
    }


def closeout_prompt(intent: str, route: str, decision: dict[str, Any]) -> str:
    if decision["status"] == "Blocked":
        return (
            f"/{route} preflight is blocked for this intent: {intent}. "
            "Ask for the smallest approval needed, then rerun the verifier before mutation."
        )
    if decision["status"] == "Needs Judgment":
        return (
            f"/{route} sharpen this intent before acting: {intent}. "
            "Ask only the execution-changing question, then proceed locally with verifier proof."
        )
    return (
        f"/{route} run this Google-local path: {intent}. "
        "State assumptions, run manual gates, verify, write a run receipt, and close with 3 Next Prompts."
    )


def build_preflight(intent: str) -> dict[str, Any]:
    candidates = route_candidates(intent)
    chosen = candidates[0]["route"] if candidates else "autopilot"
    clarity = clarity_score(intent)
    approved_subagents = subagent_approval_packet_present(intent)
    risks = risk_reasons(intent)
    lane = classify_lane(intent, chosen)
    launchpad = build_launchpad(
        intent,
        route=chosen,
        lane=lane,
        risk_reasons=risks,
        clarity_score=clarity * 20,
    )
    pause = launchpad["pause_or_run"]
    safe_default = safe_local_execution_default(chosen, lane, risks)
    if risks:
        decision = {
            "status": "Blocked",
            "reason": "Risk boundary requires approval before execution: " + ", ".join(risks),
            "can_execute_now": False,
        }
    elif safe_default:
        decision = {
            "status": "Run Locally",
            "reason": "Execution-bias/system-failure repair can start with safe workspace-local proof, patch, verify, and receipt.",
            "can_execute_now": True,
        }
    elif pause["requires_pause"]:
        decision = {
            "status": "Needs Judgment",
            "reason": pause["reason"],
            "can_execute_now": False,
        }
    else:
        decision = {
            "status": "Run Locally",
            "reason": "No execution-changing ambiguity detected; keep work local and verifier-backed.",
            "can_execute_now": True,
        }

    payload = {
        "schema_version": "google-operator-preflight/v1",
        "intent_lock": {
            "raw_intent": intent,
            "clarity_score": clarity,
            "lane": lane,
            "risk_reasons": risks,
        },
        "co_creative_launchpad": launchpad,
        "route_candidates": candidates,
        "chosen_path": {
            "owner": chosen,
            "support_gates": SUPPORT_GATES.get(chosen, ["validate-intent", "recommend"]),
            "subagents": (
                "Approved read-only diagnostic subagents only; main thread owns edits and integration."
                if approved_subagents
                else "No real Codex subagents without explicit authorization."
            ),
        },
        "execution_decision": decision,
        "manual_gate_checklist": manual_gates(chosen, risks),
        "verification_plan": verification_plan(chosen),
        "local_next_action": local_next_action(intent, chosen, decision, approved_subagents),
        "closeout_prompt": closeout_prompt(intent, chosen, decision),
        "run_prompt": closeout_prompt(intent, chosen, decision),
        "orchestration_receipt": {
            "platform": "codex",
            "workspace": str(ROOT),
            "hooks": "codex hook bridge configured through .codex/hooks.json and codex_hook_runner.py; verifier must confirm trusted, not-explicitly-disabled current-root state",
            "container_decision": launchpad["container_decision"]["move"],
            "capability_move": (
                launchpad["capability_move"]["recommendation"]
                if launchpad["capability_move"]["visible"]
                else "Quiet execution; no capability interruption needed."
            ),
            "why_now": launchpad["why_now"],
            "approval_boundary": launchpad["approval_boundary"],
            "auto_task_creation": False,
        },
    }
    return payload


def render_plain(payload: dict[str, Any]) -> str:
    chosen = payload["chosen_path"]
    decision = payload["execution_decision"]
    lock = payload["intent_lock"]
    lines = [
        "## Intent Lock",
        f"- Raw intent: {lock['raw_intent']}",
        f"- Clarity score: {lock['clarity_score']}/5",
        f"- Lane: {lock['lane']}",
        f"- Risk reasons: {', '.join(lock['risk_reasons']) or 'none'}",
        "",
        "## Co-Creative Launchpad",
        f"- Predicted need: {payload['co_creative_launchpad']['predicted_need']}",
        f"- Center: {payload['co_creative_launchpad']['center']}",
        f"- What good looks like: {payload['co_creative_launchpad']['success_standard']}",
        f"- Questions that change execution: {', '.join(payload['co_creative_launchpad']['questions_that_change_execution']) or 'none'}",
    ]
    capability = payload["co_creative_launchpad"]["capability_move"]
    if capability.get("visible"):
        container = payload["co_creative_launchpad"]["container_decision"]
        lines.extend(
            [
                f"- Container decision: {container['move']} - {container['reason']}",
                f"- Capability recommendation: {capability['recommendation']}",
                f"- Why now: {payload['co_creative_launchpad']['why_now']}",
                f"- What I can do: {capability['action']}",
                f"- Approval boundary: {payload['co_creative_launchpad']['approval_boundary']}",
            ]
        )
    lines.extend(["", "## Route Candidates"])
    for item in payload["route_candidates"]:
        lines.append(f"- /{item['route']} ({item['source']}, score {item['score']}): {item['description']}")
    lines.extend(
        [
            "",
            "## Chosen Owner",
            f"- Owner: /{chosen['owner']}",
            f"- Support gates: {', '.join('/' + gate for gate in chosen['support_gates'])}",
            f"- Subagents: {chosen['subagents']}",
            "",
            "## Execution Decision",
            f"- Status: {decision['status']}",
            f"- Reason: {decision['reason']}",
            "",
            "## Manual Gate Checklist",
        ]
    )
    for gate in payload["manual_gate_checklist"]:
        lines.append(f"- {gate['gate']} [{gate['status']}]: {gate['check']}")
    lines.extend(["", "## Verification Plan"])
    for check in payload["verification_plan"]:
        lines.append(f"- {check}")
    action = payload["local_next_action"]
    lines.extend(
        [
            "",
            "## Local Next Action",
            f"- Mode: {action['mode']}",
            f"- Action: {action['action']}",
            f"- First command: {action['first_command'] or 'none'}",
            f"- Verifier: {action['verifier_command'] or 'none'}",
            f"- Receipt required: {action['receipt_required']}",
            f"- Subagent policy: {action['subagent_policy']}",
            "",
            "## Closeout Prompt",
            payload["closeout_prompt"],
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Preflight raw intent through the Google operator core.")
    parser.add_argument("intent", nargs="+", help="Raw user intent to route.")
    parser.add_argument("--plain", action="store_true", help="Print a readable preflight packet.")
    parser.add_argument("--json", action="store_true", help="Print JSON.")
    args = parser.parse_args()

    payload = build_preflight(" ".join(args.intent))
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=True))
    else:
        print(render_plain(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
