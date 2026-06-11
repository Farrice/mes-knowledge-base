#!/usr/bin/env python3
"""Regression checks for the Codex Dynamic Workflow runtime."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import codex_dynamic_workflow as runtime  # type: ignore  # noqa: E402


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_valid(manifest: dict, label: str) -> None:
    ok, failures = runtime.verify_manifest(manifest)
    require(ok, f"{label} manifest invalid: {failures}")
    require(manifest["final_integration_owner"] == "main Codex thread", f"{label} must keep main thread owner")
    require(manifest["approval_state"]["real_subagents_spawned"] is False, f"{label} must not spawn subagents")
    require(manifest["phases"], f"{label} must include phases")
    require(manifest["worker_packets"], f"{label} must include worker packets")


def main() -> int:
    no_subagent = runtime.build_manifest(
        "audit one bounded harness surface",
        recipe="codebase-audit",
        allow_subagents=False,
        run_id="fixture-no-subagent",
    )
    assert_valid(no_subagent, "no-subagent plan")
    require(
        all(packet["approval_required_for_real_subagent"] is False for packet in no_subagent["worker_packets"]),
        "no-subagent plan should not mark packets as authorized",
    )

    multi_worker = runtime.build_manifest(
        "cross checked research on dynamic workflow quality",
        recipe="cross-checked-research",
        allow_subagents=True,
        max_concurrency=6,
        run_id="fixture-multi-worker",
    )
    assert_valid(multi_worker, "approved multi-worker plan")
    require(multi_worker["approval_state"]["real_subagents_authorized"] is True, "authorization marker missing")
    require(multi_worker["approval_state"]["real_subagents_spawned"] is False, "script must not spawn real subagents")
    require(multi_worker["max_concurrency"] == 6, "max concurrency should be preserved within bounds")

    paused = runtime.build_manifest(
        "review a plan adversarially before implementation",
        recipe="adversarial-plan-review",
        run_id="fixture-paused",
    )
    paused["runtime_state"]["status"] = "paused"
    paused["runtime_state"]["blocked_reason"] = "waiting for approval"
    resumed = runtime.resume_manifest(paused, "continue after approval")
    assert_valid(resumed, "paused resume")
    require(resumed["runtime_state"]["status"] == "ready-to-continue", "resume should mark ready-to-continue")
    require(resumed["runtime_state"]["resume_count"] == 1, "resume count should increment")

    failed = runtime.build_manifest(
        "migration planning with retryable worker failure",
        recipe="migration-planning",
        run_id="fixture-failed-worker",
    )
    failed["worker_packets"][0]["status"] = "failed"
    failed["worker_packets"][0]["attempts"] = 1
    summary = runtime.status_summary(failed)
    assert_valid(failed, "failed worker fixture")
    require(summary["failed_packets"], "failed worker should appear in status summary")

    rejected = runtime.build_manifest(
        "research plan with rejected cross check",
        recipe="cross-checked-research",
        run_id="fixture-rejected-cross-check",
    )
    rejected["cross_checks"].append(
        {
            "claim": "Unsupported dynamic workflow claim",
            "verdict": "rejected",
            "reason": "No source ledger evidence.",
        }
    )
    receipt = runtime.build_receipt(rejected)
    assert_valid(rejected, "cross-check rejection fixture")
    require(receipt["rejected_cross_checks"], "receipt should preserve rejected cross-checks")
    require(receipt["manifest_valid"] is True, "receipt fixture should remain valid")

    with tempfile.TemporaryDirectory(prefix="codex-dwf-complete-") as complete_fixture_dir:
        complete_result = Path(complete_fixture_dir) / "scope-map.md"
        complete_result.write_text("# Scope Map\n\n- bounded surface\n- explicit skip list\n", encoding="utf-8")
        completed = runtime.complete_phase(
            no_subagent,
            "scope-map",
            result_path=str(complete_result),
            summary="Scope map completed by verifier fixture.",
        )
        assert_valid(completed, "completed phase fixture")
        completed_summary = runtime.status_summary(completed)
        require(completed_summary["current_phase"] == "slice-audits", "complete_phase should advance to next phase")
        require(completed_summary["completed_phase_results"], "status should expose completed phase result paths")
        require(
            completed["worker_packets"][0]["attempts"] == 1,
            "complete_phase should increment packet attempt count",
        )

    cli = subprocess.run(
        [
            sys.executable,
            "execution/codex_dynamic_workflow.py",
            "plan",
            "audit bounded runtime surface",
            "--recipe",
            "codebase-audit",
            "--no-save",
            "--json",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(cli.returncode == 0, f"plan CLI failed: {cli.stderr}")
    parsed = json.loads(cli.stdout)
    assert_valid(parsed, "plan CLI")

    with tempfile.TemporaryDirectory(prefix="codex-dwf-cli-") as temp_root:
        env = dict(os.environ)
        env["CODEX_DYNAMIC_WORKFLOW_ROOT"] = temp_root
        temp_result = Path(temp_root) / "result.md"
        temp_result.write_text("# CLI Scope Map\n\nBounded fixture result.\n", encoding="utf-8")
        plan_cli = subprocess.run(
            [
                sys.executable,
                "execution/codex_dynamic_workflow.py",
                "plan",
                "audit cli phase completion",
                "--recipe",
                "codebase-audit",
                "--json",
            ],
            cwd=ROOT,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        require(plan_cli.returncode == 0, f"saved plan CLI failed: {plan_cli.stderr}")
        saved_manifest = json.loads(plan_cli.stdout)
        complete_cli = subprocess.run(
            [
                sys.executable,
                "execution/codex_dynamic_workflow.py",
                "complete-phase",
                "scope-map",
                "--run-id",
                saved_manifest["run_id"],
                "--result-path",
                str(temp_result),
                "--summary",
                "CLI scope map completed.",
                "--json",
            ],
            cwd=ROOT,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        require(complete_cli.returncode == 0, f"complete-phase CLI failed: {complete_cli.stderr}")
        completed_cli = json.loads(complete_cli.stdout)
        require(completed_cli["current_phase"] == "slice-audits", "complete-phase CLI should advance phase")
        require(completed_cli["completed_phase_results"], "complete-phase CLI should expose result path")

    receipt_cli = subprocess.run(
        [
            sys.executable,
            "execution/codex_dynamic_workflow.py",
            "receipt",
            "--path",
            "execution/../.agent/nonexistent.json",
            "--no-save",
            "--json",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(receipt_cli.returncode != 0, "receipt CLI should fail for nonexistent path")

    print("Codex Dynamic Workflow verification: PASS")
    print("- no-subagent manifest plans without authorization")
    print("- approved multi-worker manifest remains packet-only")
    print("- paused run resumes without spawning workers")
    print("- failed worker and rejected cross-checks are visible")
    print("- complete-phase records result paths and advances state")
    print("- plan CLI JSON is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
