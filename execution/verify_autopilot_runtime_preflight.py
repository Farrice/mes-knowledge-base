#!/usr/bin/env python3
"""Verify Autopilot intent-to-outcome runtime behavior."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

import autopilot_runtime_preflight as preflight  # type: ignore  # noqa: E402
import co_creative_launchpad as launchpad_runtime  # type: ignore  # noqa: E402
import codex_operator_preflight as codex_preflight  # type: ignore  # noqa: E402


GOLDEN_PROMPTS = [
    {
        "id": "current-market-research-free-first",
        "query": "Research the current market for AI lead generation tools.",
        "route": "deep-research-os",
        "lane": "deep-research-os",
        "status": "Running now",
        "required": ["deep-research-os", "research-intelligence-agent", "ground-truth"],
    },
    {
        "id": "missing-runtime-repair-owned-by-system-audit",
        "query": "Repair Autopilot so it never routes to missing or obsolete runtimes.",
        "route": "system-audit",
        "lane": "system-failure",
        "status": "Running now",
        "required": ["system-audit", "routing-intelligence", "health-check"],
    },
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
        "id": "capability-stewardship-lifecycle",
        "query": "Make capability awareness, context-container judgment, bounded expert orchestration, and proactive leverage surfacing a persistent default at session start, mid-session, and closeout without requiring magic words",
        "route": "system-audit",
        "lane": "system-failure",
        "status": "Running now",
        "required": ["system-audit", "autopilot", "expert-composition-governor", "routing-intelligence"],
        "container_move": "preserve",
        "capability_visible": True,
    },
    {
        "id": "capability-awareness-natural-language",
        "query": "Help me know what capabilities you can use at the start, middle, and end without magic words",
        "route": "system-audit",
        "lane": "system-failure",
        "status": "Running now",
        "required": ["system-audit", "autopilot", "expert-composition-governor", "routing-intelligence"],
        "container_move": "preserve",
        "capability_visible": True,
    },
    {
        "id": "genuine-current-session-closeout",
        "query": "Wrap this task and prepare the closeout",
        "route": "end-session",
        "lane": "end-session-closeout",
        "status": "Needs judgment",
        "required": ["end-session", "autopilot", "routing-intelligence", "health-check"],
        "container_move": "continue",
        "capability_visible": False,
    },
    {
        "id": "delegate-dry-run",
        "query": "autopilot --delegate use subagents to verify claims",
        "route": "autopilot",
        "lane": "delegate",
        "status": "Running now",
        "required": ["subagent-readiness", "expert-composition-governor"],
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
    "**Container decision**",
    "**Capability move**",
    "**Why now**",
    "**Approval boundary**",
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

    resolution = data["runtime_resolution"]
    if not resolution["ready"]:
        raise AssertionError(f"{label} selected unresolved runtime targets: {resolution['missing']}")

    all_routes = (
        set(trace["candidates"]["command_menu"])
        | set(trace["candidates"]["workflow_router"])
        | set(trace["support_gates"])
        | {chosen}
    )
    missing_routes = [route for route in case["required"] if route not in all_routes]
    if missing_routes:
        raise AssertionError(f"{label} missing required route candidates/gates: {', '.join(missing_routes)}")

    if status in {"Blocked by risk", "Blocked by configuration", "Plan only", "Needs judgment"} and "Run Prompt" not in output:
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
    launchpad = data["launchpad"]
    if expected_move := case.get("container_move"):
        actual_move = launchpad["container_decision"]["move"]
        if actual_move != expected_move:
            raise AssertionError(f"{label} expected container move {expected_move}, got {actual_move}")
    if "capability_visible" in case:
        actual_visible = launchpad["capability_move"]["visible"]
        if actual_visible is not case["capability_visible"]:
            raise AssertionError(f"{label} capability visibility mismatch: {actual_visible}")
    receipt = data["orchestration_receipt"]
    stewardship_fields = {
        "container_decision",
        "capability_move",
        "why_now",
        "approval_boundary",
        "auto_task_creation",
        "inquiry_mode",
        "build_purpose",
        "research_path",
        "iteration_posture",
    }
    missing_stewardship = stewardship_fields - set(receipt)
    if missing_stewardship:
        raise AssertionError(f"{label} receipt missing Capability Stewardship fields: {sorted(missing_stewardship)}")
    if receipt["auto_task_creation"] is not False:
        raise AssertionError(f"{label} receipt must forbid automatic task creation")
    receipt_command = data["run_receipt"]["command"]
    for flag in ("--container-decision", "--capability-move", "--why-now", "--approval-boundary"):
        if flag not in receipt_command:
            raise AssertionError(f"{label} persisted run receipt command missing {flag}")

    return f"{label}: route=/{chosen}, lane={governor['lane']}, status={status}"


def assert_missing_targets_fail_closed() -> str:
    resolution = preflight.resolve_runtime_targets(
        "definitely-nonexistent-route",
        ["python3 execution/definitely_missing_verifier.py"],
    )
    posture = preflight.apply_runtime_resolution_gate(
        {
            "status": "Running now",
            "first_action": "run",
            "approval_needed": "none",
            "risk_reasons": [],
            "safe_to_run": True,
        },
        resolution,
    )
    if resolution["ready"] or resolution["status"] != "BROKEN":
        raise AssertionError("negative control did not detect missing route/verifier targets")
    if posture["status"] != "Blocked by configuration" or posture["safe_to_run"]:
        raise AssertionError(f"negative control did not fail closed: {posture}")
    if "system-audit" not in posture["approval_needed"]:
        raise AssertionError("configuration block did not name the repair owner")
    return "negative-control: nonexistent route and verifier cannot inherit Running now"


STEWARDSHIP_CASES = [
    {
        "id": "tiny-mechanical-quiet",
        "query": "Make this five-minute mechanical edit in the current file",
        "move": "continue",
        "visible": False,
    },
    {
        "id": "distinct-branch-handoff",
        "query": "A distinct research branch has emerged and should keep the parent task as integration owner",
        "move": "handoff",
        "visible": True,
        "recommendation": "focused handoff",
        "boundary": "creating or opening a user-owned task requires explicit approval",
    },
    {
        "id": "durable-branch-new-task-recommendation",
        "query": "A distinct branch now has its own objective, own acceptance criteria, own sources, and own next action",
        "move": "recommend-new-task",
        "visible": True,
        "recommendation": "separate task",
        "boundary": "Explicit approval is required before creating or opening a user-owned task",
    },
    {
        "id": "taste-fatigue-fresh-pen",
        "query": "Two rejected taste revisions in heavy context are contaminating the artifact",
        "move": "fresh-pen",
        "visible": True,
        "action": "/fresh-pen",
    },
    {
        "id": "bounded-expert-composition",
        "query": "More than three experts are plausible for these independent workstreams",
        "move": "bounded-support",
        "visible": True,
        "recommendation": "one function owner",
        "boundary": "Real Codex subagents still require explicit run-specific authorization",
    },
    {
        "id": "safe-local-verifier",
        "query": "A safe local verifier is available before we continue",
        "move": "verify",
        "visible": True,
        "action": "Execute the available verifier now",
    },
    {
        "id": "external-publish-send-boundary",
        "query": "The external publish and send action is next",
        "move": "continue",
        "visible": True,
        "recommendation": "Prepare the publish or send action",
        "boundary": "Explicit approval is required before publish, send",
    },
    {
        "id": "repeatable-process-preservation",
        "query": "This repeating one-off is becoming a repeatable system",
        "move": "preserve",
        "visible": True,
        "recommendation": "companion contract plus regression proof",
    },
    {
        "id": "circling-verification-checkpoint",
        "query": "We are going in circles and repeating decisions",
        "move": "verify",
        "visible": True,
    },
]


INQUIRY_CASES = [
    {
        "id": "creative-fiction-free",
        "query": "Brainstorm three fictional story concepts for a wellness brand",
        "mode": "create",
        "purpose": "exploration",
        "research": "skip",
        "visible": False,
        "no_questions": True,
        "can_run": True,
    },
    {
        "id": "speculative-mechanism-free",
        "query": "Sketch a speculative mechanism as a rough prototype and label it untested",
        "mode": "create",
        "purpose": "exploration",
        "research": "skip",
        "visible": False,
        "no_questions": True,
        "can_run": True,
    },
    {
        "id": "fictional-production-free",
        "query": "Create a production-ready fictional story concept for this campaign",
        "mode": "execute",
        "purpose": "production",
        "research": "skip",
        "visible": False,
        "can_run": True,
    },
    {
        "id": "mechanical-bypass",
        "query": "Make this five-minute mechanical edit in the current file",
        "mode": "execute",
        "purpose": "production",
        "research": "skip",
        "visible": False,
    },
    {
        "id": "stable-authoritative-analysis",
        "query": "Explain this technical question using canonical documentation",
        "mode": "analyze",
        "purpose": "decision",
        "research": "local",
        "visible": True,
        "source_contains": "canonical documentation",
    },
    {
        "id": "current-primary-counterevidence",
        "query": "Assess the current regulation today before we make the decision",
        "mode": "analyze",
        "purpose": "decision",
        "research": "free-primary",
        "visible": True,
        "source_contains": "counterevidence",
    },
    {
        "id": "buyer-behavior-probe",
        "query": "Validate buyer pain and willingness to pay for this offer",
        "mode": "probe",
        "purpose": "decision",
        "research": "free-primary",
        "visible": True,
        "source_contains": "Behavioral evidence",
    },
    {
        "id": "weak-evidence-escalation",
        "query": "The sources are weak and outdated; decide whether this consequential claim holds",
        "mode": "analyze",
        "purpose": "decision",
        "research": "escalate",
        "visible": True,
        "escalation": True,
        "can_run": True,
    },
    {
        "id": "paid-research-stops-before-launch",
        "query": "Use Gemini Deep Research for this consequential decision",
        "mode": "analyze",
        "purpose": "decision",
        "research": "escalate",
        "visible": True,
        "escalation": True,
        "must_pause": True,
    },
    {
        "id": "buyer-interview-stops-before-launch",
        "query": "Interview buyers to validate this buyer pain",
        "mode": "probe",
        "purpose": "decision",
        "research": "escalate",
        "visible": True,
        "escalation": True,
        "must_pause": True,
    },
    {
        "id": "prototype-not-production-proof",
        "query": "Build a rough prototype for a fictional market mechanism",
        "mode": "create",
        "purpose": "exploration",
        "research": "skip",
        "visible": False,
        "source_contains": "No evidence floor",
    },
    {
        "id": "direct-production-request",
        "query": "Implement this approved plan as a production-ready local asset",
        "mode": "execute",
        "purpose": "production",
        "research": "local",
        "visible": False,
    },
    {
        "id": "two-pass-reframe",
        "query": "We completed two substantive passes and this is not converging",
        "mode": "analyze",
        "purpose": "decision",
        "research": "local",
        "visible": True,
        "iteration": "reframe",
    },
    {
        "id": "taste-confirmed-continue",
        "query": "The direction is right and the remaining gap is taste only",
        "mode": "create",
        "purpose": "production",
        "research": "skip",
        "visible": True,
        "iteration": "taste-continue",
    },
    {
        "id": "research-keyword-negative-control",
        "query": "Write a fictional story about a market research lab",
        "mode": "create",
        "purpose": "exploration",
        "research": "skip",
        "visible": False,
    },
    {
        "id": "current-keyword-negative-control",
        "query": "Summarize the current paragraph in one sentence",
        "mode": "execute",
        "purpose": "production",
        "research": "skip",
        "visible": False,
    },
    {
        "id": "explicit-build-depth-override",
        "query": "Just build the local concept now and label the market assumptions untested",
        "mode": "execute",
        "purpose": "production",
        "research": "skip",
        "visible": True,
    },
]


def assert_inquiry_case(case: dict[str, object]) -> str:
    packet = launchpad_runtime.build_launchpad(str(case["query"]), route="autopilot", lane="general")
    label = str(case["id"])
    if packet["schema_version"] != "co-creative-launchpad/v3":
        raise AssertionError(f"{label} did not emit launchpad/v3")
    decision = packet["inquiry_decision"]
    expected = (case["mode"], case["purpose"], case["research"])
    actual = (decision["mode"], decision["build_purpose"], decision["research_path"])
    if actual != expected:
        raise AssertionError(f"{label} expected {expected}, got {actual}")
    if decision["visible"] is not case["visible"]:
        raise AssertionError(f"{label} expected visible={case['visible']}, got {decision['visible']}")
    if expected_source := case.get("source_contains"):
        if str(expected_source).lower() not in str(decision["source_floor"]).lower():
            raise AssertionError(f"{label} source floor missing {expected_source!r}: {decision['source_floor']}")
    if expected_iteration := case.get("iteration"):
        if decision.get("iteration_posture") != expected_iteration:
            raise AssertionError(f"{label} expected iteration={expected_iteration}, got {decision.get('iteration_posture')}")
    if case.get("escalation"):
        escalation = decision.get("escalation")
        required = {
            "missing_evidence",
            "proposed_route",
            "expected_cost_or_quota",
            "permissions_required",
            "deliverable",
            "decision_unlocked",
        }
        if not isinstance(escalation, dict) or required - set(escalation):
            raise AssertionError(f"{label} escalation brief is incomplete: {escalation}")
    if case.get("no_questions") and packet["questions_that_change_execution"]:
        raise AssertionError(f"{label} added questions to free creative exploration")
    if case.get("can_run") and packet["pause_or_run"]["requires_pause"]:
        raise AssertionError(f"{label} incorrectly blocked safe continuation")
    if case.get("must_pause") and not packet["pause_or_run"]["requires_pause"]:
        raise AssertionError(f"{label} failed to stop before paid or permissioned inquiry")
    rendered = launchpad_runtime.render_launchpad(packet)
    has_mode_line = "Mode:" in rendered
    if has_mode_line is not bool(case["visible"]):
        raise AssertionError(f"{label} material-fork visibility mismatch")
    return f"{label}: {'/'.join(actual)}, visible={decision['visible']}"


def assert_routing_precedence() -> list[str]:
    operating_prompt = (
        "Implement an adaptive operating layer across meaningful work: extend the co-creative launchpad, "
        "add a research warrant, stop iteration loops, and repair routing precedence before expert matching."
    )
    operating = codex_preflight.build_preflight(operating_prompt)
    if operating["chosen_path"]["owner"] != "system-audit":
        raise AssertionError(f"operating-default prompt routed to {operating['chosen_path']['owner']}")
    mirror_prompt = (
        "Apply the prepared global mirror after rechecking both file hashes, verify the global behavior, "
        "and stop if either target has drifted."
    )
    mirror = codex_preflight.build_preflight(mirror_prompt)
    if mirror["chosen_path"]["owner"] != "system-audit":
        raise AssertionError(f"administrative global mirror routed to {mirror['chosen_path']['owner']}")
    creative_mirror_prompts = (
        "Write a fictional story about a global mirror that reflects everyone's dreams.",
        "Create an art installation called Global Mirror from fractured glass.",
        "Design a global campaign around a mirror as the central visual metaphor.",
    )
    for prompt in creative_mirror_prompts:
        creative = codex_preflight.build_preflight(prompt)
        if creative["chosen_path"]["owner"] == "system-audit":
            raise AssertionError(f"creative mirror prompt was stolen by system-audit: {prompt}")
    social_prompt = "Design a social AI product that creates an agent field around professional relationships"
    social = codex_preflight.build_preflight(social_prompt)
    if social["chosen_path"]["owner"] != "reid-hoffman-design-agent-field":
        raise AssertionError(f"social-AI domain prompt routed to {social['chosen_path']['owner']}")
    domain = codex_preflight.build_preflight("Build my first KDP book from scratch")
    if domain["chosen_path"]["owner"] != "kdp-engine":
        raise AssertionError(f"mandatory domain prompt routed to {domain['chosen_path']['owner']}")
    if domain["route_candidates"][0]["source"] != "mandatory-domain-binding":
        raise AssertionError(f"mandatory domain stage was not surfaced: {domain['route_candidates'][0]}")
    return [
        "routing-precedence: operating-default prompt -> /system-audit",
        "routing-precedence: administrative global mirror -> /system-audit",
        "routing-negative-control: creative mirror prompts remain domain-eligible",
        "routing-negative-control: social-AI product -> /reid-hoffman-design-agent-field",
        "routing-precedence: KDP domain binding -> /kdp-engine before fuzzy search",
    ]


def _blind_score(kind: str, sample: dict[str, object]) -> int:
    """Score unlabeled behavior facts against the task's approved decision criteria."""

    score = 0
    if kind == "creative":
        score += 3 if sample.get("mode") == "create" else 0
        score += 2 if sample.get("research_path") == "skip" else 0
        score += 2 if sample.get("question_count") == 0 else 0
        score += 2 if sample.get("requires_pause") is False else 0
    elif kind == "market":
        score += 3 if sample.get("mode") == "probe" else 0
        score += 3 if sample.get("behavioral_floor") is True else 0
        score += 2 if sample.get("articles_are_not_validation") is True else 0
        score += 1 if sample.get("requires_pause") is False else 0
    elif kind == "system":
        score += 5 if sample.get("route") == "system-audit" else 0
        score += 2 if sample.get("mode") == "execute" else 0
        score += 1 if sample.get("research_path") in {"skip", "local"} else 0
        score += 1 if sample.get("requires_pause") is False else 0
    return score


def assert_shadow_receipts_and_blind_comparison() -> list[str]:
    """Prove three independent lanes and compare them without version labels."""

    cases = {
        "creative": "Brainstorm three fictional story concepts for a wellness brand",
        "market": "Validate buyer pain and willingness to pay for this offer",
        "system": (
            "Implement an adaptive operating layer across meaningful work: extend the co-creative launchpad, "
            "add a research warrant, prevent iteration loops, and repair routing precedence before expert matching."
        ),
    }
    legacy = {
        "creative": {
            "mode": "unspecified",
            "research_path": "unspecified",
            "question_count": 1,
            "requires_pause": True,
            "route": "autopilot",
        },
        "market": {
            "mode": "unspecified",
            "research_path": "unspecified",
            "question_count": 0,
            "requires_pause": False,
            "behavioral_floor": False,
            "articles_are_not_validation": False,
            "route": "autopilot",
        },
        "system": {
            "mode": "unspecified",
            "research_path": "unspecified",
            "question_count": 0,
            "requires_pause": False,
            "route": "routing-intelligence",
        },
    }
    results: list[str] = []
    for kind, query in cases.items():
        routed = codex_preflight.build_preflight(query)
        packet = routed["co_creative_launchpad"]
        inquiry = packet["inquiry_decision"]
        adaptive = {
            "mode": inquiry["mode"],
            "research_path": inquiry["research_path"],
            "question_count": len(packet["questions_that_change_execution"]),
            "requires_pause": packet["pause_or_run"]["requires_pause"],
            "route": routed["chosen_path"]["owner"],
            "behavioral_floor": "behavioral evidence" in inquiry["source_floor"].lower(),
            "articles_are_not_validation": "cannot validate demand" in inquiry["source_floor"].lower(),
        }
        adaptive_first = hashlib.sha256(query.encode("utf-8")).digest()[0] % 2 == 0
        samples = [adaptive, legacy[kind]] if adaptive_first else [legacy[kind], adaptive]
        scores = [_blind_score(kind, sample) for sample in samples]
        winner_index = 0 if scores[0] > scores[1] else 1
        expected_index = 0 if adaptive_first else 1
        if winner_index != expected_index or scores[0] == scores[1]:
            raise AssertionError(f"{kind} blind comparison did not prefer adaptive behavior: {scores}")
        sample_label = "A" if winner_index == 0 else "B"
        results.append(
            f"shadow-receipt-{kind}: PASS; blind sample {sample_label} preferred ({scores[winner_index]}>{scores[1-winner_index]})"
        )
    return results


def assert_stewardship_case(case: dict[str, object]) -> str:
    packet = launchpad_runtime.build_launchpad(str(case["query"]), route="autopilot", lane="general")
    label = str(case["id"])
    move = packet["container_decision"]["move"]
    visible = packet["capability_move"]["visible"]
    if move != case["move"]:
        raise AssertionError(f"{label} expected move {case['move']}, got {move}")
    if visible is not case["visible"]:
        raise AssertionError(f"{label} expected visible={case['visible']}, got {visible}")
    if packet.get("auto_task_creation") is not False:
        raise AssertionError(f"{label} must never auto-create a user-owned task")
    recommendation = str(packet["capability_move"]["recommendation"])
    action = str(packet["capability_move"]["action"])
    boundary = str(packet["approval_boundary"])
    if expected := case.get("recommendation"):
        if str(expected).lower() not in recommendation.lower():
            raise AssertionError(f"{label} recommendation missing {expected!r}: {recommendation}")
    if expected := case.get("action"):
        if str(expected).lower() not in action.lower():
            raise AssertionError(f"{label} action missing {expected!r}: {action}")
    if expected := case.get("boundary"):
        if str(expected).lower() not in boundary.lower():
            raise AssertionError(f"{label} boundary missing {expected!r}: {boundary}")
    rendered = launchpad_runtime.render_launchpad(packet)
    if not visible and "Capability recommendation" in rendered:
        raise AssertionError(f"{label} emitted a capability lecture on a quiet turn")
    return f"{label}: move={move}, visible={visible}"


def main() -> int:
    results = [assert_case(case) for case in GOLDEN_PROMPTS]
    results.append(assert_missing_targets_fail_closed())
    results.extend(assert_stewardship_case(case) for case in STEWARDSHIP_CASES)
    results.extend(assert_inquiry_case(case) for case in INQUIRY_CASES)
    results.extend(assert_routing_precedence())
    results.extend(assert_shadow_receipts_and_blind_comparison())
    print("Autopilot intent-to-outcome runtime verification: PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
