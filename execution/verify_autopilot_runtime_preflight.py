#!/usr/bin/env python3
"""Verify Autopilot intent-to-outcome runtime behavior."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

import autopilot_runtime_preflight as preflight  # type: ignore  # noqa: E402


GOLDEN_PROMPTS = [
    {
        "id": "safe-local-run",
        "query": "autopilot build a local harness report and verify it",
        "route": "autopilot",
        "lane": "general",
        "status": "Running now",
        "required": ["autopilot", "capability-graph", "run-receipt"],
    },
    {
        "id": "plan-mode-pauses",
        "query": "autopilot --plan build a local harness report and verify it",
        "route": "autopilot",
        "lane": "general",
        "status": "Plan only",
        "required": ["autopilot"],
    },
    {
        "id": "menu-mode-orchestrate",
        "query": "autopilot --menu show me the menu of options",
        "route": "orchestrate",
        "lane": "menu-backend",
        "status": "Plan only",
        "required": ["orchestrate", "autopilot"],
    },
    {
        "id": "publish-risk-blocks",
        "query": "autopilot publish this LinkedIn post and send outreach",
        "route": "autopilot",
        "lane": "general",
        "status": "Blocked by risk",
        "required": ["autopilot"],
    },
    {
        "id": "plugin-packaging",
        "query": "autopilot package this workflow family as a plugin",
        "route": "plugin-readiness-audit",
        "lane": "plugin-packaging",
        "status": "Running now",
        "required": ["plugin-readiness-audit", "capability-graph"],
    },
    {
        "id": "control-plane-audit",
        "query": "audit Autopilot control-plane routing drift",
        "route": "system-audit",
        "lane": "system-failure",
        "status": "Running now",
        "required": ["system-audit", "routing-intelligence", "health-check"],
    },
    {
        "id": "operating-alignment",
        "query": "repair Codex operating alignment for workspace orchestration experts automations and output consistency",
        "route": "system-audit",
        "lane": "system-failure",
        "status": "Running now",
        "required": ["system-audit", "autopilot", "virtuoso", "expert-composition-governor", "routing-intelligence"],
    },
    {
        "id": "delegate-dry-run",
        "query": "autopilot --delegate use subagents to verify claims",
        "route": "autopilot",
        "lane": "delegate",
        "status": "Running now",
        "required": ["subagent-readiness", "delegation-receipt", "expert-composition-governor"],
    },
    {
        "id": "front-door-choice",
        "query": "I have too many tools and do not know what workflow to use",
        "route": "autopilot",
        "lane": "front-door-choice",
        "status": "Running now",
        "required": ["autopilot", "orchestrate"],
    },
    {
        "id": "raw-intent-bridge",
        "query": "I do not know how to ask Codex to turn messy entrepreneurial intent into an executable run packet",
        "route": "autopilot",
        "lane": "front-door-choice",
        "status": "Running now",
        "required": ["autopilot", "orchestrate"],
        "bridge": True,
    },
    {
        "id": "repeatability",
        "query": "The revision got worse and lost the good part.",
        "route": "repeatability-spine",
        "lane": "repeatability",
        "status": "Running now",
        "required": ["repeatability-spine", "autopilot", "system-audit"],
    },
    {
        "id": "system-broken",
        "query": "I think our system is broken and things are not working as envisioned.",
        "route": "autopilot",
        "lane": "system-failure",
        "status": "Running now",
        "required": ["system-audit", "routing-intelligence", "health-check", "friction-ledger"],
    },
    {
        "id": "launchpad-vague-raw-intent",
        "query": "raw intent",
        "route": "autopilot",
        "lane": "front-door-choice",
        "status": "Needs judgment",
        "required": ["autopilot", "orchestrate"],
    },
    {
        "id": "launchpad-clear-execution",
        "query": "autopilot build a local co-creative launchpad proof report and verify it",
        "route": "autopilot",
        "lane": "front-door-choice",
        "status": "Running now",
        "required": ["autopilot"],
    },
    {
        "id": "launchpad-source-system",
        "query": "turn this video source into a co-creative launchpad OS for the harness",
        "route": "source-to-skill-system",
        "lane": "skill-system",
        "status": "Running now",
        "required": ["source-to-skill-system", "extraction-governor-agent", "autopilot"],
    },
    {
        "id": "launchpad-taste-pause",
        "query": "autopilot create something world-class for my brand",
        "route": "autopilot",
        "lane": "general",
        "status": "Needs judgment",
        "required": ["autopilot"],
    },
    {
        "id": "dynamic-workflow-escalation",
        "query": "autopilot plan a many-file migration with cross-checked repeated verification",
        "route": "autopilot",
        "lane": "general",
        "status": "Running now",
        "required": ["autopilot", "codex-dynamic-workflow", "run-receipt"],
    },
    {
        "id": "operator-cockpit-engineering-debt",
        "query": "engineering debt and user failure modes are creating bottlenecks in my Codex harness",
        "route": "system-audit",
        "lane": "system-failure",
        "status": "Needs judgment",
        "required": ["system-audit", "autopilot", "health-check", "routing-intelligence"],
        "no_stack": True,
    },
    {
        "id": "operator-cockpit-ambiguous-intent",
        "query": "I was ambiguous hoping you would catch all my intentions and the safeguards are not working",
        "route": "system-audit",
        "lane": "system-failure",
        "status": "Needs judgment",
        "required": ["system-audit", "autopilot", "health-check", "routing-intelligence"],
        "no_stack": True,
    },
    {
        "id": "operator-cockpit-claude-intent",
        "query": "Claude Code catches my intent better and I need smarter routing without limiting the arsenal",
        "route": "system-audit",
        "lane": "system-failure",
        "status": "Needs judgment",
        "required": ["system-audit", "autopilot", "expert-composition-governor", "routing-intelligence"],
        "no_stack": True,
    },
    {
        "id": "operator-cockpit-retrieval-failure",
        "query": "I cannot find anything because folders have random numbers and letters in the organization system",
        "route": "system-audit",
        "lane": "system-failure",
        "status": "Needs judgment",
        "required": ["system-audit", "artifact-router", "health-check"],
        "no_stack": True,
    },
]

ORDERED_SECTIONS = [
    "## Intent Lock",
    "## Intent Confidence Packet",
    "## Co-Creative Launchpad",
    "## Raw Intent Bridge",
    "## Autopilot Trace",
    "## Execution Decision",
    "## Chosen Path",
    "## Capability Graph",
    "## Execution Plan",
    "## Orchestration Receipt",
    "## Run Prompt",
    "## Run Receipt",
    "## Friction Ledger",
    "## Harness Surface Classification",
    "## Global Mirror Proposal",
    "## Approval/Risk Gate",
]

REQUIRED_TEXT = [
    "**Read-only checks performed**",
    "## Intent Confidence Packet",
    "**Arsenal policy**",
    "**Retrieval home**",
    "## Co-Creative Launchpad",
    "## Raw Intent Bridge",
    "**Dynamic Workflow**",
    "**Predicted need**",
    "**Questions that change execution**",
    "**Verification planned**",
    "## Execution Decision",
    "## Orchestration Receipt",
    "meta_intent",
    "composition_owner",
    "Running now",
    "safe workspace-local execution",
    "## Run Prompt",
    "## Run Receipt",
    "## Friction Ledger",
    "python3 execution/capability_graph.py --json",
    "python3 execution/run_receipt.py --verify",
    "python3 execution/friction_ledger.py verify",
    "Do not mirror until local proof passes",
]

FORBIDDEN_TEXT = [
    "**Execution not performed**",
    "Waiting for explicit approval before execution.",
    "Autopilot pauses every time",
    "Plan First Always",
]


def assert_output_order(output: str, label: str) -> None:
    positions = [output.find(section) for section in ORDERED_SECTIONS]
    missing = [section for section, position in zip(ORDERED_SECTIONS, positions) if position < 0]
    if missing:
        raise AssertionError(f"{label} missing sections: {', '.join(missing)}")
    if positions != sorted(positions):
        raise AssertionError(f"{label} sections are not intent-to-outcome ordered")


def assert_required_text(output: str, label: str) -> None:
    missing = [item for item in REQUIRED_TEXT if item not in output]
    if missing:
        raise AssertionError(f"{label} missing runtime text: {', '.join(missing)}")
    hits = [item for item in FORBIDDEN_TEXT if item in output]
    if hits:
        raise AssertionError(f"{label} still exposes always-pause text: {', '.join(hits)}")


def assert_case(case: dict[str, object]) -> str:
    data = preflight.build_preflight(str(case["query"]))
    output = preflight.render_preflight(data)
    label = str(case["id"])

    assert_output_order(output, label)
    assert_required_text(output, label)

    trace = data["trace"]
    governor = trace["governor"]
    chosen = data["chosen_path"]["primary_route"]
    status = data["execution_decision"]["status"]
    if chosen != case["route"]:
        raise AssertionError(f"{label} expected /{case['route']}, got /{chosen}")
    if governor["lane"] != case["lane"]:
        raise AssertionError(f"{label} expected lane {case['lane']}, got {governor['lane']}")
    if status != case["status"]:
        raise AssertionError(f"{label} expected status {case['status']}, got {status}")

    all_routes = (
        set(trace["candidates"]["command_menu"])
        | set(trace["candidates"]["workflow_router"])
        | set(trace["support_gates"])
        | {chosen}
    )
    missing_routes = [route for route in case["required"] if route not in all_routes]
    if missing_routes:
        raise AssertionError(f"{label} missing required route candidates/gates: {', '.join(missing_routes)}")

    if status in {"Blocked by risk", "Plan only", "Needs judgment"} and "Run Prompt" not in output:
        raise AssertionError(f"{label} blocked/planned runs must include a Run Prompt")

    if data["global_mirror"]["status"] != "deferred":
        raise AssertionError(f"{label} global mirror must remain deferred")

    packet = data["intent_confidence_packet"]
    if case.get("no_stack") and data["trace"]["recommended_stack"]["recommended_stack"] != "No recommended stack":
        raise AssertionError(f"{label} should suppress irrelevant expert stacks")
    if route := case.get("route"):
        if packet["chosen_route"] != route:
            raise AssertionError(f"{label} confidence packet expected /{route}, got /{packet['chosen_route']}")
    if status == "Needs judgment" and not packet["questions"]:
        raise AssertionError(f"{label} Needs judgment runs should include confidence-packet questions")
    if case.get("bridge"):
        bridge = data.get("raw_intent_bridge", {})
        if bridge.get("status") != "triggered":
            raise AssertionError(f"{label} expected raw intent bridge to trigger")
        if "raw_intent_run_packet.py" not in bridge.get("packet_command", ""):
            raise AssertionError(f"{label} missing raw intent packet compiler command")

    return f"{label}: route=/{chosen}, lane={governor['lane']}, status={status}"


def main() -> int:
    results = [assert_case(case) for case in GOLDEN_PROMPTS]
    print("Autopilot intent-to-outcome runtime verification: PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
