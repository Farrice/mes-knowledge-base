#!/usr/bin/env python3
"""Verify Codex Antigravity control-plane firing behavior."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
MATRIX = ROOT / "execution" / "control_plane_golden_queries.json"
HELPER_TIMEOUT_SECONDS = 90

sys.path.insert(0, str(ROOT / "execution"))

import autopilot_runtime_preflight  # noqa: E402
import command_menu  # noqa: E402
import protocol_tracker  # noqa: E402
import routing_governor  # noqa: E402
import workflow_router  # noqa: E402


COMMAND_MENU_INDEX = None

CONTROL_PLANE_COMMANDS = (
    "autopilot",
    "end-session",
    "expert-composition-governor",
    "system-audit",
    "repeatability-spine",
    "orchestrate",
    "mission",
    "routing-intelligence",
    "health-check",
    "extraction-governor-agent",
    "self-evolve",
    "skill-anneal",
    "knowledge-librarian",
    "source-to-skill-system",
)

MANDATORY_PROTOCOLS = (
    "intent-pipeline.md",
    "session-state-protocol.md",
    "quality_gate.md",
    "feedback-ratchet.md",
)

AUTOPILOT_REQUIRED_TEXT = (
    "Intent-To-Outcome",
    "Execution Decision",
    "Running now",
    "Needs judgment",
    "Blocked by risk",
    "Plan only",
    "Run Prompt",
    "Run Receipt",
    "Friction Ledger",
    "Capability Graph",
    "Outcome Recipes",
    "Plugin Packaging Ladder",
    "safe workspace-local execution",
    "plugin_readiness_audit.py",
    "friction_ledger.py",
    "run_receipt.py",
    "capability_graph.py",
    "No global mirror, Google Antigravity edit, publishing, paid tool, destructive",
)

AUTOPILOT_SKILL_REQUIRED_TEXT = (
    "Intent-to-outcome",
    "safe execute-by-default",
    "Execution Decision",
    "Run Prompt",
    "Run Receipt",
    "Friction Ledger",
    "plugin-readiness-audit",
)

RUNTIME_REQUIRED_TEXT = (
    "## Intent Lock",
    "## Autopilot Trace",
    "## Execution Decision",
    "## Capability Graph",
    "## Run Prompt",
    "## Orchestration Receipt",
    "meta_intent",
    "composition_owner",
    "## Run Receipt",
    "## Friction Ledger",
    "## Approval/Risk Gate",
)

RESEARCH_INTELLIGENCE_REQUIRED_TEXT = (
    "Current/Deep Research Routing Rule",
    "context cannot establish what is true now",
    "/deep-research-os --free-first",
    "Codex native web search and opened full pages first",
    "Tavily Search/Extract",
    "never Tavily Research",
    "public RSS/Atom on demand",
    "/ground-truth",
    "/adversarial-review",
    "research_quality_gate.py",
    "Do not launch Apify, paid accelerators, schedules, background workers, or real",
)

ORCHESTRATE_REQUIRED_TEXT = (
    "menu-only backend",
    "Menu-only boundary",
    "must not execute",
    "Do not run the recommended first prompt or command",
    "canonical source of truth for Orchestrate behavior",
    "Real Codex subagents require explicit authorization",
)

END_SESSION_REQUIRED_TEXT = (
    "canonical source of truth for End-session behavior",
    "whole-session closeout",
    "not `/handoff`",
    "not `/steering-compass`",
    "3 Next Prompts",
    "Operator move:",
    "approval-blocked",
    "--format compact",
    "Task remains unarchived",
    "Approval needed:",
    "session_closeout_intelligence.py run --source end-session",
    "conversation_index.py stats",
    "handoff_store.py verify",
    "codex_end_session.py run --manifest",
    "[Domain]: [Specific Object] - [Outcome]",
    "archive only",
    "dedicated `codex/*` worktree",
    "Never auto-commit, auto-merge, or auto-push `main`",
    "Optional cleanup must be reviewed",
    "Real Codex subagents require explicit authorization",
)

HEALTH_CHECK_REQUIRED_TEXT = (
    "canonical source of truth for Health-check behavior",
    "read-only by default",
    "python3 execution/harness_status.py --plain",
    "python3 execution/savant_control_room.py --plain",
    "python3 execution/operator_core_fast_proof.py --plain",
    "python3 execution/system_health.py --quick",
    "python3 execution/operator_core_status.py --plain",
    "Do not write reports, sync Notion, optimize routes, mutate Mission, or perform cleanup unless explicitly requested",
    "Mission remains read-only unless `python3 execution/verify_mission_activation_contract.py` fails",
    "Route system-failure or drift-audit language to `/autopilot` or `/system-audit`",
    "Real Codex subagents require explicit authorization",
)

ROUTING_INTELLIGENCE_REQUIRED_TEXT = (
    "canonical source of truth for Routing-intelligence behavior",
    "read-only analytics by default",
    "python3 execution/routing_intelligence.py scoreboard",
    "python3 execution/routing_intelligence.py utilization",
    "python3 execution/routing_intelligence.py unused",
    "python3 execution/routing_intelligence.py domain-dist",
    "python3 execution/routing_intelligence.py top-combos",
    "python3 execution/routing_intelligence.py underperforming",
    "Only write routing feedback through `misroute` when the user explicitly reports a wrong route",
    "Do not auto-optimize routes, mutate workflows, sync Notion, mutate Mission, perform cleanup, or mirror global files",
    "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
    "Real Codex subagents require explicit authorization",
)

KNOWLEDGE_LIBRARIAN_REQUIRED_TEXT = (
    "canonical source of truth for Knowledge-librarian behavior",
    "compact session-start knowledge pulse by default",
    "python3 execution/knowledge_compiler.py stats",
    'python3 execution/knowledge_compiler.py solutions "[focus]" --top 8 --stdout',
    "Read `knowledge/compiled/briefing.md` if it exists",
    "do not generate or refresh the briefing by default",
    "Do not write `.agent/knowledge-librarian-state.md`, refresh compiled knowledge, create solution docs, mutate Mission, perform cleanup, or mirror global files unless explicitly requested",
    "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
    "Real Codex subagents require explicit authorization",
)

SELF_EVOLVE_REQUIRED_TEXT = (
    "canonical source of truth for Self-evolve behavior",
    "mutation-gated measured evolution",
    "Incomplete or vague goal packets produce a queue-only diagnosis",
    "Mutation requires a complete goal packet, Evolution Council Verdict, baseline, search set, measurable stop condition, turn cap, proof artifact, and no-regression check",
    "Permitted side effects must be local, reversible, and inside `/Users/farricecain/Google Antigravity`",
    "Stop at a human checkpoint for global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or scope expansion",
    "Do not mutate Mission unless `verify_mission_activation_contract.py` fails and the user explicitly approves Mission repair",
    "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
    "Real Codex subagents require explicit authorization",
)

SKILL_ANNEAL_REQUIRED_TEXT = (
    "canonical source of truth for Skill-anneal behavior",
    "prompt-level skill/component annealing",
    "Incomplete or vague goal packets produce a queue-only diagnosis",
    "Annealing requires a target skill directory, failure examples, rubric/test-input set, proof artifact, measurable stop condition, turn cap, and explicit no-regression clause",
    "preserve upstream input, downstream output, and validation contract",
    "Limit edits to the single weakest criterion unless the user approves a broader rewrite",
    "Side effects must be local, reversible, and inside `/Users/farricecain/Google Antigravity`",
    "Stop at a human checkpoint for broader workflow evolution, global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or Mission repair",
    "Route broad workflow evolution to `/self-evolve`",
    "Real Codex subagents require explicit authorization",
)

SOURCE_TO_SKILL_SYSTEM_REQUIRED_TEXT = (
    "canonical source of truth for Source-to-skill-system behavior",
    "turns source material into connected skill systems, not isolated mega-skills",
    "Evidence and existing-route fit come before building",
    "Every build needs the Skill System Contract fields before implementation",
    "Agentic engineering changes require the Agentic Engineering Packet",
    "Self-improvement, maintenance, cleanup, or evolution changes require a Goal Packet",
    "Prefer companion OS layers over duplicate expert skills",
    "Do not create hot skills, global mirrors, external writes, new dependencies, or broad workflow mutations without explicit approval and validation",
    "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
    "Real Codex subagents require explicit authorization",
)

SYSTEM_AUDIT_REQUIRED_TEXT = (
    "canonical source of truth for System-audit behavior",
    "control-plane audit and repair route",
    "Run read-only proof first",
    "Distinguish structural health from firing behavior",
    "Repairs must be severity-ranked, verifier-backed, and workspace-local by default",
    "Global `~/.codex` edits require explicit approval",
    "Mission remains untouched unless `verify_mission_activation_contract.py` fails and Farrice explicitly approves Mission repair",
    "Route normal status reads to `/health-check`, routing analytics to `/routing-intelligence`, and raw intent or broad broken-harness triage to `/autopilot`",
    "Real Codex subagents require explicit authorization",
)

REPEATABILITY_SPINE_REQUIRED_TEXT = (
    "canonical source of truth for Repeatability-spine behavior",
    "preserves the good example before repair",
    "Every run needs grounded evidence, one primary failure class, Preservation Lock, repair route, validation, regression guard, and replay prompt",
    "Inaccessible conversations are pending evidence, not invented findings",
    "Routing failures require a verifier query or routing feedback log before being called repaired",
    "Mutation-capable repair routes (`/self-evolve`, `/skill-anneal`, `/skill-evolution`) require a Goal Packet before edits",
    "Global `~/.codex` behavior changes require workspace proof and explicit approval",
    "Route broad broken-harness triage to `/autopilot` or `/system-audit`",
    "Real Codex subagents require explicit authorization",
)

EXPERT_COMPOSITION_REQUIRED_TEXT = (
    "canonical source of truth for Expert-composition-governor behavior",
    "prevents expert soup and full-arsenal sprawl",
    "more than three experts/routes are plausible",
    "One function owner must integrate the final result",
    "Specialists must occupy bounded slots",
    "The Composition Ledger must show accepted, skipped, or rejected contributions with evidence of change",
    "Expert names are not proof; integration evidence is proof",
    "Do not spawn real Codex subagents unless explicitly authorized",
    "Route broad broken-harness triage to `/autopilot` or `/system-audit`",
    "route reusable source-to-system builds to `/source-to-skill-system`",
)

EXTRACTION_GOVERNOR_REQUIRED_TEXT = (
    "canonical source of truth for Extraction-governor-agent behavior",
    "owns source-to-capability triage and routing, not isolated summarization or collection",
    "Default mode is read-only triage",
    "Preserve source grounding before synthesis",
    "Run existing-route and duplicate-system checks before recommending a new skill, workflow, agent, command bridge, or knowledge artifact",
    "Do not write `.agent/extraction-governor-agent-state.md`, create artifacts, promote hot skills, mirror global files, use paid/quota-heavy tools, fetch external sources, or mutate workflows unless explicitly requested and validated",
    "Hand off connected skill-system or orchestration builds to `/source-to-skill-system`",
    "overlap or prior-decision questions to `/knowledge-librarian`",
    "travel/plugin packaging decisions to `/plugin-readiness-audit`",
    "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
    "Real Codex subagents require explicit authorization",
)

CODEX_REQUIRED_TEXT = (
    "/autopilot",
    "intent-to-outcome front door",
    "safe workspace-local execution",
    "run receipts",
    "risk-gated judgment",
    "execution/autopilot_runtime_preflight.py",
    "execution/capability_graph.py",
    "execution/friction_ledger.py",
    "execution/run_receipt.py",
    "semantic_libraries/antigravity/primitives/operating-alignment-contract.md",
    "semantic_libraries/antigravity/primitives/magic-preservation-regression-set.md",
)

FORBIDDEN_AUTOPILOT_TEXT = (
    "Autopilot pauses every time",
    "Plan First Always applies to every Autopilot run",
    "Waiting for explicit approval before execution.",
    "**Execution not performed**",
)


def run(args: list[str]) -> str:
    try:
        result = subprocess.run(
            args,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=HELPER_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout if isinstance(exc.stdout, str) else ""
        raise AssertionError(
            f"{' '.join(args)} timed out after {HELPER_TIMEOUT_SECONDS}s:\n{stdout}"
        ) from exc
    if result.returncode != 0:
        raise AssertionError(f"{' '.join(args)} failed:\n{result.stdout}")
    return result.stdout


def load_matrix() -> dict:
    if not MATRIX.exists():
        raise AssertionError(f"Missing golden query matrix: {MATRIX}")
    return json.loads(MATRIX.read_text(encoding="utf-8"))


def command_routes(query: str, limit: int = 10) -> list[str]:
    global COMMAND_MENU_INDEX
    if COMMAND_MENU_INDEX is None:
        COMMAND_MENU_INDEX = command_menu.build_index()
    return [workflow.name for _, workflow in command_menu.search(COMMAND_MENU_INDEX, query, limit)]


def workflow_routes(query: str, limit: int = 10) -> list[str]:
    return [workflow["name"] for _, workflow in workflow_router.search_workflows(query, limit)]


def assert_first(label: str, routes: list[str], expected: Iterable[str]) -> None:
    expected_set = set(expected)
    if not routes:
        raise AssertionError(f"{label} returned no routes")
    if routes[0] not in expected_set:
        raise AssertionError(f"{label} expected first route in {sorted(expected_set)}, got /{routes[0]}")


def assert_subset(label: str, routes: list[str], allowed: Iterable[str], count: int = 8) -> None:
    allowed_set = set(allowed)
    offenders = [route for route in routes[:count] if route not in allowed_set]
    if offenders:
        raise AssertionError(
            f"{label} top {count} included non-control routes: "
            + ", ".join(f"/{route}" for route in offenders)
        )


def assert_forbidden_absent(label: str, routes: list[str], forbidden: Iterable[str], count: int = 8) -> None:
    forbidden_set = set(forbidden)
    offenders = [route for route in routes[:count] if route in forbidden_set]
    if offenders:
        raise AssertionError(
            f"{label} top {count} included forbidden routes: "
            + ", ".join(f"/{route}" for route in offenders)
        )


def assert_rank_above(label: str, routes: list[str], higher: str, lower: str) -> None:
    if higher not in routes:
        raise AssertionError(f"{label} missing expected route /{higher}")
    if lower in routes and routes.index(higher) > routes.index(lower):
        raise AssertionError(f"{label} ranked /{lower} above /{higher}")


def check_golden_queries() -> list[str]:
    matrix = load_matrix()
    control_routes = matrix["control_plane_routes"]
    results = []
    for case in matrix["queries"]:
        query = case["query"]
        menu = command_routes(query)
        router = workflow_routes(query)
        decision = routing_governor.evaluate(query, menu, router)

        expected_first = case.get("expected_first", [])
        if expected_first:
            assert_first(f"command_menu {case['id']}", menu, expected_first)
            if not str(case["id"]).startswith("autopilot-"):
                assert_first(f"workflow_router {case['id']}", router, expected_first)

        governor_first = case.get("governor_first") or expected_first
        if governor_first:
            assert_first(f"routing_governor {case['id']}", [decision.chosen_route], governor_first)

        expected_lane = case.get("expected_lane")
        if expected_lane and decision.detected_lane != expected_lane:
            raise AssertionError(
                f"routing_governor {case['id']} expected lane {expected_lane}, got {decision.detected_lane}"
            )

        if case.get("top_must_be_subset") == "control_plane_routes":
            assert_subset(f"command_menu {case['id']}", menu, control_routes)
            assert_subset(f"workflow_router {case['id']}", router, control_routes)

        forbidden = case.get("forbidden_top", [])
        if forbidden:
            assert_forbidden_absent(f"command_menu {case['id']}", menu, forbidden)
            assert_forbidden_absent(f"workflow_router {case['id']}", router, forbidden)

        for higher, lower in case.get("must_rank_above", {}).items():
            assert_rank_above(f"command_menu {case['id']}", menu, higher, lower)
            assert_rank_above(f"workflow_router {case['id']}", router, higher, lower)

        results.append(
            f"golden query {case['id']}: menu=/{menu[0]}, router=/{router[0]}, "
            f"governor=/{decision.chosen_route}, lane={decision.detected_lane}"
        )
    return results


def check_bridge_coverage() -> list[str]:
    results = []
    missing = []
    for command in CONTROL_PLANE_COMMANDS:
        workflow = ROOT / ".agent" / "workflows" / f"{command}.md"
        codex_skill = ROOT / ".agents" / "skills" / f"source-command-{command}" / "SKILL.md"
        source_command = ROOT / ".claude" / "commands" / f"{command}.md"
        if not workflow.exists():
            missing.append(f"/{command}: missing workflow")
        if not codex_skill.exists():
            missing.append(f"/{command}: missing Codex skill")
        if not source_command.exists():
            missing.append(f"/{command}: missing source command")
        if not any(item.startswith(f"/{command}:") for item in missing):
            results.append(f"bridge /{command}: workflow, Codex skill, source command")
    if missing:
        raise AssertionError("Control-plane bridge gaps:\n" + "\n".join(missing))
    return results


def require_text(path: Path, snippets: Iterable[str], label: str) -> str:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path}")
    text = path.read_text(encoding="utf-8", errors="ignore")
    missing = [snippet for snippet in snippets if snippet not in text]
    if missing:
        raise AssertionError(f"{path} missing {label}: {', '.join(missing)}")
    return text


def check_required_text() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "autopilot.md"
    skill = ROOT / ".agents" / "skills" / "source-command-autopilot" / "SKILL.md"
    codex = ROOT / "CODEX.md"
    system_audit = ROOT / ".agent" / "workflows" / "system-audit.md"

    workflow_text = require_text(workflow, AUTOPILOT_REQUIRED_TEXT, "intent-to-outcome text")
    require_text(skill, AUTOPILOT_SKILL_REQUIRED_TEXT, "source skill text")
    require_text(codex, CODEX_REQUIRED_TEXT, "Codex control-plane text")
    require_text(system_audit, ("Control-plane audit", "Issue Ledger", "verify_system_control_plane.py"), "system audit text")

    hits = [snippet for snippet in FORBIDDEN_AUTOPILOT_TEXT if snippet in workflow_text]
    if hits:
        raise AssertionError("Autopilot workflow still contains old always-pause text: " + ", ".join(hits))

    return [
        "contract text present: CODEX.md",
        "contract text present: .agent/workflows/autopilot.md",
        "contract text present: .agents/skills/source-command-autopilot/SKILL.md",
    ]


def check_autopilot_runtime_preflight() -> list[str]:
    cases = [
        (
            "runtime-safe-local",
            "autopilot build a local harness report and verify it",
            "autopilot",
            "general",
            "Running now",
        ),
        (
            "runtime-plan-only",
            "autopilot --plan build a local harness report and verify it",
            "autopilot",
            "general",
            "Plan only",
        ),
        (
            "runtime-risk-block",
            "autopilot publish this LinkedIn post and send outreach",
            "autopilot",
            "general",
            "Blocked by risk",
        ),
        (
            "runtime-system-failure",
            "I think our system is broken and things are not working as envisioned.",
            "autopilot",
            "system-failure",
            "Running now",
        ),
        (
            "runtime-control-plane-audit",
            "audit Autopilot control-plane routing drift",
            "system-audit",
            "system-failure",
            "Running now",
        ),
        (
            "runtime-operating-alignment",
            "repair Codex operating alignment for workspace orchestration experts automations and output consistency",
            "system-audit",
            "system-failure",
            "Running now",
        ),
        (
            "runtime-delegate-dry-run",
            "autopilot --delegate use subagents to verify claims",
            "autopilot",
            "delegate",
            "Running now",
        ),
        (
            "runtime-repeatability",
            "The revision got worse and lost the good part.",
            "repeatability-spine",
            "repeatability",
            "Running now",
        ),
    ]
    results = []
    for label, query, expected_route, expected_lane, expected_status in cases:
        data = autopilot_runtime_preflight.build_preflight(query)
        output = autopilot_runtime_preflight.render_preflight(data)
        missing = [snippet for snippet in RUNTIME_REQUIRED_TEXT if snippet not in output]
        if missing:
            raise AssertionError(f"Autopilot runtime preflight {label} missing text: " + ", ".join(missing))
        route = data["chosen_path"]["primary_route"]
        lane = data["trace"]["governor"]["lane"]
        status = data["execution_decision"]["status"]
        if route != expected_route:
            raise AssertionError(f"Autopilot runtime preflight {label} expected /{expected_route}, got /{route}")
        if lane != expected_lane:
            raise AssertionError(f"Autopilot runtime preflight {label} expected lane {expected_lane}, got {lane}")
        if status != expected_status:
            raise AssertionError(f"Autopilot runtime preflight {label} expected status {expected_status}, got {status}")
        results.append(f"autopilot runtime preflight {label}: /{route}, lane={lane}, status={status}")
    return results


def check_local_helpers() -> list[str]:
    results = []
    helper_commands = [
        [sys.executable, "execution/capability_graph.py", "--json"],
        [sys.executable, "execution/outcome_recipes.py", "--list"],
        [sys.executable, "execution/friction_ledger.py", "verify"],
        [sys.executable, "execution/run_receipt.py", "--verify"],
        [sys.executable, "execution/verify_operator_core_ai_employee_os.py"],
        [sys.executable, "execution/verify_operator_core_fast_proof.py"],
        [sys.executable, "execution/verify_session_state_freshness_loop.py"],
        [sys.executable, "execution/verify_savant_control_room.py"],
        [sys.executable, "execution/sync_global_operator_core.py", "--check"],
        [sys.executable, "execution/verify_operator_lesson.py"],
        [sys.executable, "execution/verify_global_autopilot_source_truth.py"],
        [sys.executable, "execution/sync_operator_core_orchestrate.py", "--check"],
        [sys.executable, "execution/verify_operator_core_orchestrate.py"],
        [sys.executable, "execution/sync_operator_core_end_session.py", "--check"],
        [sys.executable, "execution/verify_operator_core_end_session.py"],
        [sys.executable, "execution/sync_operator_core_health_check.py", "--check"],
        [sys.executable, "execution/verify_operator_core_health_check.py"],
        [sys.executable, "execution/sync_operator_core_routing_intelligence.py", "--check"],
        [sys.executable, "execution/verify_operator_core_routing_intelligence.py"],
        [sys.executable, "execution/sync_operator_core_knowledge_librarian.py", "--check"],
        [sys.executable, "execution/verify_operator_core_knowledge_librarian.py"],
        [sys.executable, "execution/sync_operator_core_self_evolve.py", "--check"],
        [sys.executable, "execution/verify_operator_core_self_evolve.py"],
        [sys.executable, "execution/sync_operator_core_skill_anneal.py", "--check"],
        [sys.executable, "execution/verify_operator_core_skill_anneal.py"],
        [sys.executable, "execution/sync_operator_core_source_to_skill_system.py", "--check"],
        [sys.executable, "execution/verify_operator_core_source_to_skill_system.py"],
        [sys.executable, "execution/sync_operator_core_system_audit.py", "--check"],
        [sys.executable, "execution/verify_operator_core_system_audit.py"],
        [sys.executable, "execution/sync_operator_core_repeatability_spine.py", "--check"],
        [sys.executable, "execution/verify_operator_core_repeatability_spine.py"],
        [sys.executable, "execution/sync_operator_core_expert_composition_governor.py", "--check"],
        [sys.executable, "execution/verify_operator_core_expert_composition_governor.py"],
        [sys.executable, "execution/sync_operator_core_extraction_governor_agent.py", "--check"],
        [sys.executable, "execution/verify_operator_core_extraction_governor_agent.py"],
        [sys.executable, "execution/verify_operator_core_status.py"],
        [sys.executable, "execution/harness_status.py", "--json"],
        [sys.executable, "execution/subagent_readiness.py", "--dry-run", "--json"],
        [sys.executable, "execution/verify_subagent_readiness.py"],
        [sys.executable, "execution/verify_plugin_readiness_stdout.py"],
    ]
    for command in helper_commands:
        label = " ".join(command[1:])
        start = time.monotonic()
        print(f"  helper running: {label}", flush=True)
        run(command)
        elapsed = time.monotonic() - start
        print(f"  helper ok: {label} ({elapsed:.1f}s)", flush=True)
        results.append("helper ok: " + label)
    return results


def check_free_first_research_contract() -> list[str]:
    files = [
        ROOT / "agents" / "research-intelligence-agent" / "AGENT.md",
        ROOT / ".agent" / "workflows" / "research-intelligence-agent.md",
    ]
    results = []
    for path in files:
        content = require_text(path, RESEARCH_INTELLIGENCE_REQUIRED_TEXT, "free-first research text")
        if not content:
            raise AssertionError(f"Empty research file: {path}")
        results.append(f"free-first research routing contract present: {path.relative_to(ROOT)}")
    return results


def check_orchestrate_menu_only_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "orchestrate.md"
    skill = ROOT / ".agents" / "skills" / "source-command-orchestrate" / "SKILL.md"
    require_text(workflow, ORCHESTRATE_REQUIRED_TEXT, "menu-only text")
    require_text(
        skill,
        (
            "Use this skill only",
            "Menu-only backend",
            "canonical behavior source",
            "execution intent routes through `/autopilot`",
        ),
        "orchestrate skill text",
    )
    return ["orchestrate menu-only contract enforced"]


def check_end_session_closeout_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "end-session.md"
    skill = ROOT / ".agents" / "skills" / "source-command-end-session" / "SKILL.md"
    require_text(workflow, END_SESSION_REQUIRED_TEXT, "end-session source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "whole-session closeout",
            "closeout intelligence capture",
            "3 Next Prompts",
            "Operator move:",
            "approval-blocked",
            "--format compact",
            "Task remains unarchived",
            "Approval needed:",
            "session_closeout_intelligence.py run --source end-session",
            "conversation_index.py stats",
            "handoff_store.py verify",
            "codex_end_session.py run --manifest",
            "[Domain]: [Specific Object] - [Outcome]",
            "archive only",
            "dedicated `codex/*` worktree",
            "Never auto-commit, auto-merge, or auto-push `main`",
            "real Codex subagents require explicit authorization",
            "no competing behavior contract",
        ),
        "end-session skill text",
    )
    run([sys.executable, "execution/verify_end_session_visible_closeout.py"])
    return ["end-session closeout contract and visible benchmark enforced"]


def check_health_check_status_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "health-check.md"
    skill = ROOT / ".agents" / "skills" / "source-command-health-check" / "SKILL.md"
    require_text(workflow, HEALTH_CHECK_REQUIRED_TEXT, "health-check source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "read-only status by default",
            "harness_status.py --plain",
            "system_health.py --quick",
            "verify_mission_activation_contract.py",
            "real Codex subagents require explicit authorization",
            "no competing behavior contract",
        ),
        "health-check skill text",
    )
    return ["health-check status contract enforced"]


def check_routing_intelligence_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "routing-intelligence.md"
    skill = ROOT / ".agents" / "skills" / "source-command-routing-intelligence" / "SKILL.md"
    require_text(workflow, ROUTING_INTELLIGENCE_REQUIRED_TEXT, "routing-intelligence source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "read-only routing analytics by default",
            "routing_intelligence.py scoreboard",
            "explicitly reports a wrong route",
            "real Codex subagents require explicit authorization",
            "no competing behavior contract",
        ),
        "routing-intelligence skill text",
    )
    return ["routing-intelligence analytics contract enforced"]


def check_knowledge_librarian_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "knowledge-librarian.md"
    skill = ROOT / ".agents" / "skills" / "source-command-knowledge-librarian" / "SKILL.md"
    require_text(workflow, KNOWLEDGE_LIBRARIAN_REQUIRED_TEXT, "knowledge-librarian source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "compact session-start knowledge pulse",
            "read-only default scans",
            "knowledge_compiler.py stats",
            "knowledge_compiler.py solutions",
            "--stdout",
            "local evidence",
            "real Codex subagents require explicit authorization",
            "no competing behavior contract",
        ),
        "knowledge-librarian skill text",
    )
    return ["knowledge-librarian pulse contract enforced"]


def check_self_evolve_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "self-evolve.md"
    skill = ROOT / ".agents" / "skills" / "source-command-self-evolve" / "SKILL.md"
    require_text(workflow, SELF_EVOLVE_REQUIRED_TEXT, "self-evolve source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "mutation-gated measured evolution",
            "queue-only diagnosis",
            "complete goal packet",
            "Evolution Council Verdict",
            "no-regression check",
            "verify_mission_activation_contract.py",
            "real Codex subagents require explicit authorization",
            "no competing behavior contract",
        ),
        "self-evolve skill text",
    )
    return ["self-evolve mutation-gated contract enforced"]


def check_skill_anneal_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "skill-anneal.md"
    skill = ROOT / ".agents" / "skills" / "source-command-skill-anneal" / "SKILL.md"
    require_text(workflow, SKILL_ANNEAL_REQUIRED_TEXT, "skill-anneal source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "prompt-level skill/component annealing",
            "queue-only diagnosis",
            "rubric/test-input set",
            "explicit no-regression clause",
            "/self-evolve",
            "real Codex subagents require explicit authorization",
            "no competing behavior contract",
        ),
        "skill-anneal skill text",
    )
    return ["skill-anneal prompt-level contract enforced"]


def check_source_to_skill_system_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "source-to-skill-system.md"
    skill = ROOT / ".agents" / "skills" / "source-command-source-to-skill-system" / "SKILL.md"
    require_text(workflow, SOURCE_TO_SKILL_SYSTEM_REQUIRED_TEXT, "source-to-skill-system source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "connected skill systems",
            "not isolated mega-skills",
            "evidence and existing-route fit",
            "Skill System Contract",
            "Agentic Engineering Packet",
            "Goal Packet",
            "companion OS layers",
            "real Codex subagents require explicit authorization",
            "no competing behavior contract",
        ),
        "source-to-skill-system skill text",
    )
    return ["source-to-skill-system source-truth contract enforced"]


def check_system_audit_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "system-audit.md"
    skill = ROOT / ".agents" / "skills" / "source-command-system-audit" / "SKILL.md"
    require_text(workflow, SYSTEM_AUDIT_REQUIRED_TEXT, "system-audit source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "control-plane audit and repair",
            "read-only proof first",
            "structural health",
            "firing behavior",
            "severity-ranked",
            "verifier-backed",
            "verify_mission_activation_contract.py",
            "real Codex subagents require explicit authorization",
            "no competing behavior contract",
        ),
        "system-audit skill text",
    )
    return ["system-audit control-plane contract enforced"]


def check_repeatability_spine_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "repeatability-spine.md"
    skill = ROOT / ".agents" / "skills" / "source-command-repeatability-spine" / "SKILL.md"
    require_text(workflow, REPEATABILITY_SPINE_REQUIRED_TEXT, "repeatability-spine source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "preserve the good example",
            "grounded evidence",
            "primary failure class",
            "Preservation Lock",
            "regression guard",
            "replay prompt",
            "Goal Packet",
            "real Codex subagents require explicit authorization",
            "no competing behavior contract",
        ),
        "repeatability-spine skill text",
    )
    return ["repeatability-spine regression-repair contract enforced"]


def check_expert_composition_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "expert-composition-governor.md"
    skill = ROOT / ".agents" / "skills" / "source-command-expert-composition-governor" / "SKILL.md"
    require_text(workflow, EXPERT_COMPOSITION_REQUIRED_TEXT, "expert-composition-governor source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "prevent expert soup",
            "full-arsenal sprawl",
            "more than three experts/routes",
            "one function owner integrates the final result",
            "bounded slots",
            "Composition Ledger",
            "evidence of change",
            "expert names are not proof",
            "real Codex subagents unless explicitly authorized",
            "no competing behavior contract",
        ),
        "expert-composition-governor skill text",
    )
    return ["expert-composition-governor composition contract enforced"]


def check_extraction_governor_contract() -> list[str]:
    workflow = ROOT / ".agent" / "workflows" / "extraction-governor-agent.md"
    skill = ROOT / ".agents" / "skills" / "source-command-extraction-governor-agent" / "SKILL.md"
    require_text(workflow, EXTRACTION_GOVERNOR_REQUIRED_TEXT, "extraction-governor-agent source-truth text")
    require_text(
        skill,
        (
            "canonical behavior source",
            "thin compatibility wrapper",
            "source-to-capability triage",
            "read-only triage",
            "source grounding before synthesis",
            "existing-route and duplicate-system checks",
            "no state writes",
            "hot skill promotion",
            "global mirrors",
            "paid/quota-heavy tools",
            "external source fetches",
            "workflow mutation",
            "/source-to-skill-system",
            "/knowledge-librarian",
            "/plugin-readiness-audit",
            "real Codex subagents require explicit authorization",
            "no competing behavior contract",
        ),
        "extraction-governor-agent skill text",
    )
    return ["extraction-governor-agent source-triage contract enforced"]


def check_protocol_activation() -> list[str]:
    report = protocol_tracker.audit_protocols()
    protocols = {item["file"]: item for item in report["protocols"]}
    results = []
    missing = [name for name in MANDATORY_PROTOCOLS if name not in protocols]
    if missing:
        raise AssertionError("Missing mandatory protocols: " + ", ".join(missing))

    inactive = []
    for name in MANDATORY_PROTOCOLS:
        status = protocols[name]
        if status["activation_count"] <= 0 or status["never_activated"]:
            inactive.append(name)
        else:
            results.append(
                f"protocol active: {name} count={status['activation_count']} last={status['last_activated']}"
            )
    if inactive:
        raise AssertionError("Mandatory protocols are not activated: " + ", ".join(inactive))
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--section", choices=("end-session",),
        help="Run one component contract without suppressing the full default suite.",
    )
    args = parser.parse_args()
    checks = []
    sections = [
        ("golden queries", check_golden_queries),
        ("bridge coverage", check_bridge_coverage),
        ("required text", check_required_text),
        ("autopilot runtime preflight", check_autopilot_runtime_preflight),
        ("local helpers", check_local_helpers),
        ("free-first research contract", check_free_first_research_contract),
        ("orchestrate menu-only contract", check_orchestrate_menu_only_contract),
        ("end-session closeout contract", check_end_session_closeout_contract),
        ("health-check status contract", check_health_check_status_contract),
        ("routing-intelligence contract", check_routing_intelligence_contract),
        ("knowledge-librarian contract", check_knowledge_librarian_contract),
        ("self-evolve contract", check_self_evolve_contract),
        ("skill-anneal contract", check_skill_anneal_contract),
        ("source-to-skill-system contract", check_source_to_skill_system_contract),
        ("system-audit contract", check_system_audit_contract),
        ("repeatability-spine contract", check_repeatability_spine_contract),
        ("expert-composition contract", check_expert_composition_contract),
        ("extraction-governor contract", check_extraction_governor_contract),
        ("protocol activation", check_protocol_activation),
    ]
    if args.section == "end-session":
        sections = [("end-session closeout contract", check_end_session_closeout_contract)]
    for label, check in sections:
        start = time.monotonic()
        print(f"running: {label}", flush=True)
        section_checks = check()
        elapsed = time.monotonic() - start
        print(f"ok: {label} ({len(section_checks)} checks, {elapsed:.1f}s)", flush=True)
        checks.extend(section_checks)
    print("SYSTEM CONTROL PLANE VERIFICATION PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
