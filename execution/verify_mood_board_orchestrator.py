#!/usr/bin/env python3
"""Deterministic regression guard for the connected /mood-board front door."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXECUTION = ROOT / "execution"
if str(EXECUTION) not in sys.path:
    sys.path.insert(0, str(EXECUTION))

from routing_enforcer import check_routing, match_bindings  # noqa: E402


WORKFLOW = ROOT / ".agent" / "workflows" / "mood-board.md"
PROMPT = ROOT / "skills" / "creative-direction" / "references" / "prompts-v2" / "mood-board.md"
SKILL = ROOT / "skills" / "creative-direction" / "SKILL.md"
CODEX_BRIDGE = ROOT / ".agents" / "skills" / "source-command-mood-board" / "SKILL.md"
CLAUDE_BRIDGE = ROOT / ".claude" / "commands" / "mood-board.md"
ROUTING_DOC = ROOT / "directives" / "routing-bindings.md"
CONTRACT = ROOT / "docs" / "mission-artifacts" / "mood-board-orchestrator-repair" / "CONTRACT.md"


POSITIVE_QUERIES = (
    "Build a high-taste mood board from this discovery brief, with three materially different visual territories, real references, a blind taste choice, and one proving surface",
    "Turn these discovery notes into three materially different visual territories and a blind taste choice",
    "Create three reference-locked moodboards and test them on one proving surface",
    "Build a moodboard for a campaign from this brief",
    "Can you turn my discovery notes into a moodboard for the brand?",
    "Use the discovery session to make three moodboards for the client",
    "Translate this discovery into visual directions and a moodboard",
    "I need visual directions from discovery before we design anything",
)

NEGATIVE_QUERIES = (
    "Characterize my existing moodboard library with null runs, a weight sweep, and named recipes",
    "Turn this approved moodboard into a DESIGN.md with durable tokens",
    "Use the approved moodboard to generate campaign assets",
    "Build a complete Brand Operating System with mood boards, creative briefs, and an AI handoff",
)


failures: list[str] = []
notes: list[str] = []


def require(condition: bool, message: str) -> None:
    if condition:
        notes.append(message)
    else:
        failures.append(message)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        failures.append(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return ""


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def first_menu_route(output: str) -> str | None:
    match = re.search(r"(?m)^1\. `/([^`]+)`", output)
    return match.group(1) if match else None


def first_workflow_route(output: str) -> str | None:
    match = re.search(r"(?m)^\s{2}/([^\s]+)", output)
    return match.group(1) if match else None


workflow = read(WORKFLOW)
prompt = read(PROMPT)
skill = read(SKILL)
codex_bridge = read(CODEX_BRIDGE)
claude_bridge = read(CLAUDE_BRIDGE)
routing_doc = read(ROUTING_DOC)
contract = read(CONTRACT)
workflow_flat = re.sub(r"\s+", " ", workflow)

for phrase in (
    "creative-direction` is the sole function owner",
    "Phase 1 — Acquire And Ledger References",
    "Phase 2 — Build Three Territory Hypotheses",
    "Phase 3 — Construct Actual Visual Boards",
    "Phase 4 — Comparative Proving Surface",
    "Phase 5 — Blind Taste Decision",
    "Phase 6 — Lock And Hand Off The Winner",
    "Do not call a text-only specification a completed moodboard",
    "at least four of the five visual layers differ materially",
    "Human preference, approval-speed improvement, commercial lift, and market",
):
    require(phrase in workflow_flat, f"workflow contains required contract: {phrase}")

for component in (
    "Refero styles when available",
    "oren-slop-era-creative-strategy",
    "oren-taste-development",
    "/design-md-synthesize",
    "/moodboard-sweep",
    "Andrew Lane",
):
    require(component in workflow, f"workflow composes or bounds existing component: {component}")

require(
    "Optional after selection" in workflow and "never owns reference research" in workflow,
    "Andrew Lane is explicitly downstream rather than moodboard owner",
)
require("The Connected Moodboard System" in skill, "creative-direction skill exposes the connected system")
require("three actual visual boards" in prompt, "v2 prompt requires actual visual boards")
require("Recommendation withheld until the vote" in prompt, "v2 prompt preserves blind selection")
require("reference-first moodboard orchestrator" in codex_bridge.lower(), "Codex bridge advertises the repaired outcome")
require(".agent/workflows/mood-board.md" in codex_bridge, "Codex bridge remains thin")
require(".agent/workflows/mood-board.md" in claude_bridge, "Claude command remains thin")
require("`mood_board_orchestrator`" in routing_doc, "routing documentation names the moodboard binding")
require("| `mood_board_orchestrator` | /mood-board |" in routing_doc, "generated routing appendix contains the binding")

for field in (
    "## Preservation Lock",
    "## Goal Packet",
    "## Agentic Engineering Packet",
    "## Skill System Contract",
    "## Evolution Council Verdict",
    "## Systems Thinking Trace",
):
    require(field in contract, f"repair contract contains {field}")

for query in POSITIVE_QUERIES:
    hits = match_bindings(query)
    require(bool(hits), f"positive query has a binding: {query}")
    require(
        bool(hits) and hits[0].get("workflow") == "mood-board",
        f"positive query binds to /mood-board: {query}",
    )

    menu = run("execution/command_menu.py", "search", query)
    require(menu.returncode == 0, f"command menu runs for: {query}")
    require(first_menu_route(menu.stdout) == "mood-board", f"command menu ranks /mood-board first: {query}")

    router = run("execution/workflow_router.py", "search", query)
    require(router.returncode == 0, f"workflow router runs for: {query}")
    require(first_workflow_route(router.stdout) == "mood-board", f"workflow router ranks /mood-board first: {query}")

    valid = check_routing(query, "mood-board")
    wrong = check_routing(query, "creative-brief-gen")
    require(valid.get("valid") is True, f"routing enforcer accepts /mood-board: {query}")
    require(wrong.get("valid") is False, f"routing enforcer rejects generic creative brief: {query}")

for query in NEGATIVE_QUERIES:
    hits = match_bindings(query)
    mood_hits = [hit for hit in hits if hit.get("binding_id") == "mood_board_orchestrator"]
    require(not mood_hits, f"negative control is not hijacked by moodboard binding: {query}")

require("source-command-mood-board" not in workflow, "runtime workflow does not recurse through its bridge")
require("new command" in contract.lower(), "contract explicitly forbids a new command")

if failures:
    print(f"FAIL — mood-board orchestrator: {len(failures)} failure(s)")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print(
    "PASS — mood-board orchestrator: "
    f"{len(POSITIVE_QUERIES)} positive routes, "
    f"{len(NEGATIVE_QUERIES)} negative controls, "
    f"{len(notes)} structure/proof assertions"
)
