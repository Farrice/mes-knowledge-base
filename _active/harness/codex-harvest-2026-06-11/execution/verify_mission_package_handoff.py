#!/usr/bin/env python3
"""Verify mission package context handoff enforcement."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MISSION = "vibe-tax-brief-deployment-os"

AUTOPILOT = ROOT / ".agent" / "workflows" / "autopilot.md"
ORCHESTRATE = ROOT / ".agent" / "workflows" / "orchestrate.md"
VIBE_DEPLOY = ROOT / ".agent" / "workflows" / "vibe-tax-deploy.md"
MISSION_STATE = ROOT / ".agent" / "missions" / MISSION / "mission.json"
MISSION_MD = ROOT / ".agent" / "missions" / MISSION / "mission.md"

REQUIRED_CONTEXT_PATHS = (
    ".agent/missions/vibe-tax-brief-deployment-os/mission.json",
    "_active/vibe-tax-brief-deployment-os/START-HERE.md",
    "_active/vibe-tax-brief-deployment-os/BOOTSTRAP-PROMPT.md",
    "_active/vibe-tax-brief-deployment-os/DEPLOYMENT-RUNBOOK.md",
    "_active/vibe-tax-brief-deployment-os/RESEARCH-LEDGER.md",
    "_active/vibe-tax-brief-deployment-os/LINKEDIN-LAUNCH-POST.md",
    "_active/vibe-tax-brief-deployment-os/content-cards/vibe-tax-launch-001.md",
    "_active/research-intelligence-entry-point/README.md",
    "_active/research-intelligence-entry-point/EXPERT-COUNCIL.md",
    "_active/research-intelligence-entry-point/HUMAN-RESONANCE-GATE.md",
    "_active/research-intelligence-entry-point/STICKINESS-GATE.md",
    "_active/research-intelligence-entry-point/SOCIAL-DISTRIBUTION-PACK.md",
    "_active/research-intelligence-entry-point/SAMPLE-BRIEF.md",
    "_active/research-intelligence-entry-point/COPY-GATE-RESULT.md",
    "_active/research-intelligence-entry-point/LEAD-MAGNET.md",
    "_active/research-intelligence-entry-point/OFFER-PAGE.md",
    "_active/research-intelligence-entry-point/RESEARCH-BRIEF-TEMPLATE.md",
    "_exports/vibe-tax-brief-ai-handoff-2026-05-11/00-START-HERE.md",
    "_exports/vibe-tax-brief-ai-handoff-2026-05-11/EXPORT-TRACE.md",
)

WORKFLOW_TERMS = {
    AUTOPILOT: (
        "Mission Package Continuation Rule",
        "mission_control.py context",
        "Mission Handoff Receipt",
        "**Mission Package**",
    ),
    ORCHESTRATE: (
        "Mission Package Continuation Rule",
        "mission_control.py context",
        "Mission Handoff Receipt",
        "approved package",
    ),
    VIBE_DEPLOY: (
        "python3 execution/mission_control.py context vibe-tax-brief-deployment-os",
        "Mission Handoff Receipt",
        "approved mission package",
        "EXPERT-COUNCIL.md",
        "HUMAN-RESONANCE-GATE.md",
        "STICKINESS-GATE.md",
        "SOCIAL-DISTRIBUTION-PACK.md",
        "SAMPLE-BRIEF.md",
        "COPY-GATE-RESULT.md",
    ),
}


def run(args: list[str], env: dict[str, str] | None = None, expect_ok: bool = True) -> subprocess.CompletedProcess[str]:
    run_env = os.environ.copy()
    if env:
        run_env.update(env)
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=run_env,
        check=False,
    )
    if expect_ok and result.returncode != 0:
        raise AssertionError(f"{' '.join(args)} failed:\n{result.stdout}")
    if not expect_ok and result.returncode == 0:
        raise AssertionError(f"{' '.join(args)} unexpectedly passed:\n{result.stdout}")
    return result


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8", errors="ignore")


def check_context_bundle() -> list[str]:
    human = run([sys.executable, "execution/mission_control.py", "context", MISSION]).stdout
    payload = json.loads(
        run([sys.executable, "execution/mission_control.py", "context", MISSION, "--json"]).stdout
    )

    if "Mission Handoff Receipt Requirement" not in human:
        raise AssertionError("human context output is missing Mission Handoff Receipt Requirement")
    if payload["mission"]["slug"] != MISSION:
        raise AssertionError("context bundle returned the wrong mission slug")
    if payload["missing_required_sources"]:
        raise AssertionError("context bundle has missing approved sources: " + ", ".join(payload["missing_required_sources"]))
    if payload["missing_proof_artifacts"]:
        raise AssertionError("context bundle has missing proof artifacts: " + ", ".join(payload["missing_proof_artifacts"]))
    if not payload["next_command_constraints"]["must_show_mission_handoff_receipt"]:
        raise AssertionError("context bundle does not require Mission Handoff Receipt")

    paths = {item["path"] for item in payload["approved_package_load_set"]}
    missing = [path for path in REQUIRED_CONTEXT_PATHS if path not in paths]
    if missing:
        raise AssertionError("context bundle missing required package paths: " + ", ".join(missing))

    for term in ("EXPERT-COUNCIL.md", "SOCIAL-DISTRIBUTION-PACK.md", "SAMPLE-BRIEF.md", "COPY-GATE-RESULT.md"):
        if term not in human:
            raise AssertionError(f"context output missing approved asset term: {term}")

    return ["mission_control.py context emits complete Vibe Tax package bundle"]


def check_workflow_enforcement() -> list[str]:
    checks = []
    for path, terms in WORKFLOW_TERMS.items():
        text = read(path)
        for term in terms:
            if term not in text:
                raise AssertionError(f"{path.relative_to(ROOT)} missing term: {term}")
        checks.append(f"{path.relative_to(ROOT)} requires mission package handoff")

    vibe = read(VIBE_DEPLOY)
    if "BOOTSTRAP-PROMPT.md" in vibe and "EXPERT-COUNCIL.md" not in vibe:
        raise AssertionError("/vibe-tax-deploy can still operate from a thin bootstrap-only context")
    return checks


def check_mission_state_contract() -> list[str]:
    state = json.loads(read(MISSION_STATE))
    mission_md = read(MISSION_MD)
    paths = {item.get("path", "") for item in state.get("approved_package_load_set", [])}
    missing = [path for path in REQUIRED_CONTEXT_PATHS if path not in paths]
    if missing:
        raise AssertionError("mission state missing approved package load set paths: " + ", ".join(missing))
    if not any("mission_control.py context" in item for item in state.get("context_requirements", [])):
        raise AssertionError("mission state missing context resolver requirement")
    if "Approved Package Load Set" not in mission_md:
        raise AssertionError("mission markdown missing approved package load set")
    return ["mission state and mission markdown carry approved package load set"]


def check_missing_package_validation() -> list[str]:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        env = {"ANTIGRAVITY_ROOT": str(tmp)}
        run(
            [
                sys.executable,
                "execution/mission_control.py",
                "create",
                "--name",
                "Missing Package Fixture",
                "--slug",
                "missing-package-fixture",
                "--goal",
                "Prove approved packages cannot validate with missing load-set files",
                "--mode",
                "system",
                "--next-command",
                "/mission resume missing-package-fixture",
            ],
            env=env,
        )
        state_path = tmp / ".agent" / "missions" / "missing-package-fixture" / "mission.json"
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["status"] = "active"
        state["validation_assertions"] = [
            {
                "id": "VA1",
                "statement": "Approved package context is recoverable",
                "covered_by": "A1",
                "validator": "mission package handoff verifier",
                "pass_signal": "missing approved package paths fail validation",
            }
        ]
        state["activation_queue"] = [
            {
                "id": "A1",
                "owner": "Mission Package Fixture",
                "workflow": "/mission",
                "expected_artifact": "Fixture evidence",
                "status": "complete",
                "evidence_path": str(tmp / "evidence.md"),
                "validation_assertion": "VA1",
                "blocker": "",
                "next_action": "",
                "kind": "workstream",
            }
        ]
        (tmp / "evidence.md").write_text("# Evidence\n", encoding="utf-8")
        state["approved_package_load_set"] = [
            {
                "id": "P1",
                "path": "missing/approved-package.md",
                "role": "approved source",
                "reason": "Fixture should fail",
                "required": True,
            }
        ]
        state["context_requirements"] = [
            "Run `python3 execution/mission_control.py context missing-package-fixture` before use."
        ]
        state_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        result = run(
            [sys.executable, "execution/mission_control.py", "validate", "missing-package-fixture"],
            env=env,
            expect_ok=False,
        )
        if "approved package paths missing" not in result.stdout:
            raise AssertionError("missing package fixture failed for the wrong reason:\n" + result.stdout)
    return ["mission validation fails when approved package load-set files are missing"]


def check_cold_start_routing() -> list[str]:
    query = "continue the Vibe Tax Brief content deployment"
    menu = run([sys.executable, "execution/command_menu.py", "search", query]).stdout
    router = run([sys.executable, "execution/workflow_router.py", "search", query]).stdout
    combined = menu + "\n" + router
    if "/vibe-tax-deploy" not in combined:
        raise AssertionError("cold-start Vibe Tax deployment query did not surface /vibe-tax-deploy")
    return ["cold-start Vibe Tax deployment query surfaces /vibe-tax-deploy"]


def main() -> int:
    failures: list[str] = []
    checks: list[str] = []
    for label, check in (
        ("context bundle", check_context_bundle),
        ("workflow enforcement", check_workflow_enforcement),
        ("mission state contract", check_mission_state_contract),
        ("missing package validation", check_missing_package_validation),
        ("cold-start routing", check_cold_start_routing),
    ):
        try:
            checks.extend(check())
        except AssertionError as exc:
            failures.append(f"{label}: {exc}")

    if failures:
        print("Mission Package Handoff verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Mission Package Handoff verification: PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
