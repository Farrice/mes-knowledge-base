#!/usr/bin/env python3
"""Regression checks for the Virtuoso orchestration layer."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import virtuoso_orchestration  # type: ignore  # noqa: E402


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_core_shape(data: dict) -> None:
    required = {
        "objective",
        "launchpad",
        "orchestration_receipt",
        "meta_intent",
        "composition_owner",
        "primary_route",
        "owner",
        "support_gates",
        "recommended_stack",
        "composition_slots",
        "subagent_candidates",
        "plugin_tool_surface",
        "routing_log",
        "execution_receipt",
        "verification_plan",
        "first_action",
    }
    missing = sorted(required - set(data))
    require(not missing, f"missing top-level fields: {missing}")
    require(len(data["composition_slots"]) == 5, "composition slots must include the five bounded slots")
    require("predicted_need" in data["launchpad"], "launchpad must include predicted need")
    require("pause_or_run" in data["launchpad"], "launchpad must include pause/run decision")
    require(data["subagent_candidates"]["real_subagents_spawned"] is False, "verifier must not spawn real subagents")
    require(data["plugin_tool_surface"]["plugin_name"] == "antigravity-operator-core", "operator-core plugin surface missing")
    receipt = data["execution_receipt"]
    require("considered_gates" in receipt, "execution receipt must show considered gates")
    require("executed_workflows" in receipt, "execution receipt must show executed workflows")
    require("executed_scripts" in receipt, "execution receipt must show executed scripts")
    require("expert_lenses_applied" in receipt, "execution receipt must show expert lenses applied")
    require(receipt["real_subagents_spawned"] is False, "execution receipt must keep real subagents gated")
    require("python3 execution/verify_virtuoso_orchestration.py" in data["verification_plan"], "self verifier missing")
    orchestration = data["orchestration_receipt"]
    for key in ("objective", "meta_intent", "owner", "composition_owner", "route", "support_gates", "expert_lenses", "subagent_boundary", "verifier_results", "feedback_hook"):
        require(key in orchestration, f"orchestration receipt missing {key}")
    require("meta_intent" in receipt, "execution receipt must show meta intent")
    require("composition_owner" in receipt, "execution receipt must show composition owner")
    require("subagent_boundary" in receipt, "execution receipt must show subagent boundary")


def main() -> int:
    alignment_query = "repair Codex operating alignment for workspace orchestration experts automations and output consistency"
    alignment_data = virtuoso_orchestration.build_virtuoso(alignment_query, delegate_intent=False, log_routing=False)
    assert_core_shape(alignment_data)
    require(alignment_data["primary_route"] == "system-audit", "operating alignment should route to /system-audit")
    require(alignment_data["meta_intent"] == "operating-alignment", "operating alignment meta_intent missing")
    require(alignment_data["composition_owner"] == "System Audit", "operating alignment composition owner should be System Audit")
    require(alignment_data["recommended_stack"]["recommended_stack"] == "No recommended stack", "operating alignment should not force a domain stack")
    require(alignment_data["routing_log"]["ensemble"] is False, "operating alignment should not log a forced ensemble")

    system_query = "system audit elevate agents subagents orchestration cross-pollination virtuoso creative outputs"
    system_data = virtuoso_orchestration.build_virtuoso(system_query, delegate_intent=True, log_routing=False)
    assert_core_shape(system_data)
    require(system_data["primary_route"] == "system-audit", "system elevation query should route to /system-audit")
    require(system_data["owner"], "owner must be named")
    require(system_data["recommended_stack"]["recommended_stack"] == "nick-saraev + boris", "agent-fleet stack should surface")
    require(system_data["routing_log"]["ensemble"] is True, "compound stack should be marked as ensemble")
    require("expert_lenses_applied" in system_data["routing_log"], "routing log must expose expert lenses")
    require(system_data["subagent_candidates"]["selected"], "delegate intent should select candidate packets")

    content_data = virtuoso_orchestration.build_virtuoso(
        "create a client-facing research-backed content package and verify the claims",
        delegate_intent=False,
        log_routing=False,
    )
    assert_core_shape(content_data)
    require(content_data["composition_slots"][0]["slot"] == "Spine", "first slot should be Spine")
    require(content_data["subagent_candidates"]["integration_owner"] == "main Codex thread", "main thread must integrate")

    trace_only = virtuoso_orchestration.build_virtuoso(
        "create a client offer",
        trace_only=True,
    )
    assert_core_shape(trace_only)
    require(trace_only["execution_decision"]["status"] == "Trace only", "trace-only must stop execution")

    workflow_data = virtuoso_orchestration.build_virtuoso(
        "audit one bounded harness surface with a dynamic workflow",
        workflow_intent=True,
    )
    assert_core_shape(workflow_data)
    require(workflow_data["dynamic_workflow"], "workflow mode must attach dynamic workflow trace")
    require(
        workflow_data["dynamic_workflow"]["manifest"]["schema_version"] == "codex-dynamic-workflow/v1",
        "workflow manifest schema missing",
    )
    require(workflow_data["execution_decision"]["status"] == "Workflow trace", "workflow mode should stop at trace")
    require(
        "python3 execution/verify_codex_dynamic_workflow.py" in workflow_data["verification_plan"],
        "dynamic workflow verifier missing",
    )

    cli = subprocess.run(
        [
            sys.executable,
            "execution/virtuoso_orchestration.py",
            system_query,
            "--json",
            "--delegate-intent",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(cli.returncode == 0, f"CLI failed: {cli.stderr}")
    parsed = json.loads(cli.stdout)
    assert_core_shape(parsed)

    trace_cli = subprocess.run(
        [
            sys.executable,
            "execution/virtuoso_orchestration.py",
            "create a client offer",
            "--trace-only",
            "--json",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(trace_cli.returncode == 0, f"trace-only CLI failed: {trace_cli.stderr}")
    parsed_trace = json.loads(trace_cli.stdout)
    require(parsed_trace["execution_decision"]["status"] == "Trace only", "trace-only CLI did not stop")

    workflow_cli = subprocess.run(
        [
            sys.executable,
            "execution/virtuoso_orchestration.py",
            "audit one bounded harness surface",
            "--workflow",
            "--json",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(workflow_cli.returncode == 0, f"workflow CLI failed: {workflow_cli.stderr}")
    parsed_workflow = json.loads(workflow_cli.stdout)
    require(parsed_workflow["dynamic_workflow"], "workflow CLI did not include manifest trace")
    require(parsed_workflow["execution_decision"]["status"] == "Workflow trace", "workflow CLI should stop at trace")

    print("Virtuoso orchestration verification: PASS")
    print("- operating alignment routes to /system-audit without a forced domain stack")
    print("- system elevation routes to /system-audit with Nick Saraev + Boris stack")
    print("- delegation remains gated with main-thread integration")
    print("- dynamic workflow mode attaches a manifest trace without spawning workers")
    print("- plugin/tool surface, execution receipt, and composition slots render")
    print("- CLI JSON is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
