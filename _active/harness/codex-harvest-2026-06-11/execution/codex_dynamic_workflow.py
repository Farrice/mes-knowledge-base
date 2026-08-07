#!/usr/bin/env python3
"""Manifest-held dynamic workflow runtime for Codex workspaces.

This runtime plans, stores, resumes, verifies, and receipts multi-phase work.
It prepares worker packets but never spawns real Codex subagents. Real
delegation remains gated by the Codex subagent tool surface and explicit user
authorization.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def workspace_root() -> Path:
    explicit = os.environ.get("CODEX_DYNAMIC_WORKFLOW_ROOT")
    if explicit:
        return Path(explicit).expanduser().resolve()
    cwd = Path.cwd().resolve()
    for candidate in (cwd, *cwd.parents):
        if any((candidate / marker).exists() for marker in (".agent", "AGENTS.md", "CODEX.md", ".git")):
            return candidate
    script_root = Path(__file__).resolve().parents[1]
    if any((script_root / marker).exists() for marker in (".agent", "AGENTS.md", "CODEX.md", ".git")):
        return script_root
    return cwd


ROOT = workspace_root()
STATE_DIR = ROOT / ".agent" / "dynamic-workflows"
RUN_DIR = STATE_DIR / "runs"
RECEIPT_DIR = STATE_DIR / "receipts"
LATEST = STATE_DIR / "latest.json"

SCHEMA_VERSION = "codex-dynamic-workflow/v1"
REAL_SUBAGENT_BOUNDARY = (
    "Real Codex subagents are prepared as packets only. Spawning requires "
    "explicit user authorization and the Codex subagent tool surface."
)

APPROVAL_GATES = [
    "external writes",
    "publishing",
    "outreach or DMs",
    "connector writes",
    "global mirrors",
    "paid/API actions",
    "destructive cleanup",
    "Mission/system memory mutation",
    "real Codex subagents",
]

RUNTIME_STATUSES = {
    "planned",
    "in-progress",
    "ready-to-continue",
    "receipt-ready",
    "paused",
    "completed",
    "failed",
}
PHASE_STATUSES = {"pending", "ready", "in-progress", "completed", "failed"}
PACKET_STATUSES = {"packet-ready", "in-progress", "completed", "failed", "needs-retry", "skipped"}


RECIPES: dict[str, dict[str, Any]] = {
    "codebase-audit": {
        "signals": ("audit", "codebase", "repo", "harness", "system", "surface", "control plane"),
        "purpose": "Audit a bounded repo or harness surface with independent slices and synthesis.",
        "workers": ("surface-mapper", "risk-sweeper", "verification-planner"),
        "phases": [
            {
                "id": "scope-map",
                "name": "Scope Map",
                "purpose": "Name the audited surface, boundaries, source files, and success criteria.",
                "workers": ["surface-mapper"],
                "inputs": ["objective", "repo paths", "known risk signals"],
                "outputs": ["audit scope", "file/path map", "skip list"],
                "verification": ["scope has boundaries", "skip list is explicit"],
            },
            {
                "id": "slice-audits",
                "name": "Slice Audits",
                "purpose": "Inspect separable slices without duplicating work.",
                "workers": ["surface-mapper", "risk-sweeper"],
                "inputs": ["audit scope", "file/path map"],
                "outputs": ["slice findings", "severity labels", "evidence paths"],
                "verification": ["findings cite local evidence", "no destructive action"],
            },
            {
                "id": "cross-check",
                "name": "Cross-Check",
                "purpose": "Challenge findings, merge duplicates, and reject weak claims.",
                "workers": ["verification-planner"],
                "inputs": ["slice findings"],
                "outputs": ["accepted findings", "rejected findings", "open questions"],
                "verification": ["rejected claims recorded", "severity order confirmed"],
            },
            {
                "id": "synthesis",
                "name": "Synthesis",
                "purpose": "Produce the owner-led audit result and verifier plan.",
                "workers": ["integration-owner"],
                "inputs": ["accepted findings", "open questions"],
                "outputs": ["audit report", "repair path", "run receipt"],
                "verification": ["receipt exists", "next action is concrete"],
            },
        ],
    },
    "migration-planning": {
        "signals": ("migration", "migrate", "many-file", "compatibility", "backfill", "refactor"),
        "purpose": "Plan a many-file change with partitions, compatibility notes, and verifiers.",
        "workers": ("inventory-mapper", "compatibility-reviewer", "rollout-planner"),
        "phases": [
            {
                "id": "inventory",
                "name": "Inventory",
                "purpose": "List affected files, contracts, entrypoints, and existing tests.",
                "workers": ["inventory-mapper"],
                "inputs": ["objective", "target surface"],
                "outputs": ["affected inventory", "ownership map"],
                "verification": ["affected files are bounded", "tests or verifiers named"],
            },
            {
                "id": "partition",
                "name": "Partition",
                "purpose": "Split work into reviewable chunks with disjoint write scopes.",
                "workers": ["rollout-planner"],
                "inputs": ["affected inventory"],
                "outputs": ["chunk plan", "dependency order"],
                "verification": ["chunks are independently reviewable", "dependency order is explicit"],
            },
            {
                "id": "compatibility-map",
                "name": "Compatibility Map",
                "purpose": "Name compatibility risks, data migrations, and rollback boundaries.",
                "workers": ["compatibility-reviewer"],
                "inputs": ["chunk plan", "existing contracts"],
                "outputs": ["compatibility risks", "rollback notes"],
                "verification": ["public interfaces are listed", "rollback rule exists"],
            },
            {
                "id": "rollout-plan",
                "name": "Rollout Plan",
                "purpose": "Produce the migration execution plan and acceptance checks.",
                "workers": ["integration-owner"],
                "inputs": ["chunk plan", "compatibility risks"],
                "outputs": ["execution plan", "acceptance checks", "receipt"],
                "verification": ["acceptance checks are runnable", "receipt exists"],
            },
        ],
    },
    "cross-checked-research": {
        "signals": ("research", "current", "latest", "market", "competitor", "claim", "source"),
        "purpose": "Run independent research angles and reconcile claims before synthesis.",
        "workers": ("evidence-researcher", "claim-verifier", "synthesis-owner"),
        "phases": [
            {
                "id": "angle-plan",
                "name": "Angle Plan",
                "purpose": "Split the research question into independent angles.",
                "workers": ["synthesis-owner"],
                "inputs": ["objective", "known sources"],
                "outputs": ["research angles", "source criteria"],
                "verification": ["angles are non-overlapping", "source criteria named"],
            },
            {
                "id": "independent-evidence",
                "name": "Independent Evidence",
                "purpose": "Collect evidence per angle with source labels and confidence.",
                "workers": ["evidence-researcher"],
                "inputs": ["research angles", "source criteria"],
                "outputs": ["source ledger", "angle findings"],
                "verification": ["each claim has source status", "uncertainty is labeled"],
            },
            {
                "id": "claim-reconciliation",
                "name": "Claim Reconciliation",
                "purpose": "Cross-check claims and reject unsupported synthesis moves.",
                "workers": ["claim-verifier"],
                "inputs": ["source ledger", "angle findings"],
                "outputs": ["verified claims", "rejected claims", "gaps"],
                "verification": ["rejected claims are preserved", "gaps are explicit"],
            },
            {
                "id": "research-brief",
                "name": "Research Brief",
                "purpose": "Produce the final claim-labeled brief and receipt.",
                "workers": ["synthesis-owner"],
                "inputs": ["verified claims", "gaps"],
                "outputs": ["research brief", "source ledger", "receipt"],
                "verification": ["claim labels are present", "receipt exists"],
            },
        ],
    },
    "adversarial-plan-review": {
        "signals": ("red team", "adversarial", "review plan", "critique", "risk", "ship"),
        "purpose": "Stress-test a plan, repair it, and preserve approval gates.",
        "workers": ("plan-decomposer", "adversarial-reviewer", "repair-owner"),
        "phases": [
            {
                "id": "decompose",
                "name": "Decompose",
                "purpose": "Break the plan into claims, assumptions, risks, and decision points.",
                "workers": ["plan-decomposer"],
                "inputs": ["plan", "objective"],
                "outputs": ["assumption list", "risk list", "decision points"],
                "verification": ["assumptions are explicit", "decision points are named"],
            },
            {
                "id": "adversarial-review",
                "name": "Adversarial Review",
                "purpose": "Find the strongest failure modes before execution.",
                "workers": ["adversarial-reviewer"],
                "inputs": ["assumption list", "risk list"],
                "outputs": ["must-fix issues", "ship/no-ship verdict"],
                "verification": ["top risks are severity-ranked", "verdict is explicit"],
            },
            {
                "id": "repair",
                "name": "Repair",
                "purpose": "Patch the plan around must-fix issues.",
                "workers": ["repair-owner"],
                "inputs": ["must-fix issues", "decision points"],
                "outputs": ["repaired plan", "residual risk"],
                "verification": ["each must-fix issue addressed", "residual risk named"],
            },
            {
                "id": "approval-packet",
                "name": "Approval Packet",
                "purpose": "Return the final approval packet and next action.",
                "workers": ["integration-owner"],
                "inputs": ["repaired plan", "residual risk"],
                "outputs": ["approval packet", "run prompt", "receipt"],
                "verification": ["approval gate is clear", "receipt exists"],
            },
        ],
    },
    "source-to-system-extraction": {
        "signals": ("source", "transcript", "video", "book", "extract", "skill system", "capability"),
        "purpose": "Turn grounded source material into a reusable system without duplicate bloat.",
        "workers": ("source-grounder", "route-fit-reviewer", "proof-lab-owner"),
        "phases": [
            {
                "id": "source-evidence",
                "name": "Source Evidence",
                "purpose": "Verify source package, evidence limits, and unavailable modalities.",
                "workers": ["source-grounder"],
                "inputs": ["source path or URL", "objective"],
                "outputs": ["evidence ledger", "evidence limits"],
                "verification": ["source identity is verified", "limits are explicit"],
            },
            {
                "id": "route-fit",
                "name": "Route Fit",
                "purpose": "Check existing routes before creating a new component.",
                "workers": ["route-fit-reviewer"],
                "inputs": ["evidence ledger", "capability objective"],
                "outputs": ["existing-route fit", "build shape decision"],
                "verification": ["duplicate-system risk addressed", "owner selected"],
            },
            {
                "id": "capability-shape",
                "name": "Capability Shape",
                "purpose": "Define workflow, companion layer, gate, or no-build decision.",
                "workers": ["route-fit-reviewer"],
                "inputs": ["build shape decision"],
                "outputs": ["component contract", "handoff rules"],
                "verification": ["contract fields present", "context policy named"],
            },
            {
                "id": "behavior-proof",
                "name": "Behavior Proof",
                "purpose": "Create a proof artifact that shows the capability changed behavior.",
                "workers": ["proof-lab-owner"],
                "inputs": ["component contract", "test scenario"],
                "outputs": ["proof lab", "before/after or cold-start result"],
                "verification": ["behavior-changing proof exists", "live surface check named"],
            },
        ],
    },
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:64] or "dynamic-workflow"


def recipe_for_objective(objective: str, requested: str | None = None) -> str:
    if requested:
        if requested not in RECIPES:
            raise ValueError(f"unknown recipe: {requested}")
        return requested
    lowered = objective.lower()
    scores: dict[str, int] = {}
    for name, recipe in RECIPES.items():
        scores[name] = sum(1 for signal in recipe["signals"] if signal in lowered)
    best = max(scores, key=lambda name: scores[name])
    return best if scores[best] > 0 else "codebase-audit"


def run_id_for(objective: str, recipe: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    digest = hashlib.sha1(f"{recipe}:{objective}".encode("utf-8")).hexdigest()[:8]
    return f"{stamp}-{slugify(objective)[:36]}-{digest}"


def worker_packet(worker: str, phase: dict[str, Any], allow_subagents: bool) -> dict[str, Any]:
    packet_id = f"{phase['id']}::{worker}"
    return {
        "id": packet_id,
        "worker": worker,
        "phase_id": phase["id"],
        "role": worker.replace("-", " ").title(),
        "prompt": (
            f"Handle only phase `{phase['id']}` for the Codex Dynamic Workflow. "
            f"Purpose: {phase['purpose']}."
        ),
        "input_contract": phase["inputs"],
        "output_contract": phase["outputs"],
        "stop_condition": "Return the phase output, evidence paths, and unresolved blockers.",
        "may_spawn_real_subagent": False,
        "approval_required_for_real_subagent": bool(allow_subagents),
        "activation_boundary": REAL_SUBAGENT_BOUNDARY,
        "status": "packet-ready",
        "attempts": 0,
        "last_result": None,
    }


def build_manifest(
    objective: str,
    *,
    recipe: str | None = None,
    allow_subagents: bool = False,
    max_concurrency: int = 4,
    run_id: str | None = None,
) -> dict[str, Any]:
    selected_recipe = recipe_for_objective(objective, recipe)
    recipe_data = deepcopy(RECIPES[selected_recipe])
    created = now_iso()
    max_concurrency = max(1, min(int(max_concurrency), 8))
    manifest_id = run_id or run_id_for(objective, selected_recipe)
    phases = []
    packets = []
    for index, phase in enumerate(recipe_data["phases"], 1):
        phase_packets = [worker_packet(worker, phase, allow_subagents) for worker in phase["workers"]]
        packets.extend(phase_packets)
        phases.append(
            {
                "id": phase["id"],
                "name": phase["name"],
                "index": index,
                "purpose": phase["purpose"],
                "inputs": phase["inputs"],
                "outputs": phase["outputs"],
                "worker_packet_ids": [packet["id"] for packet in phase_packets],
                "approval_gates": ["real Codex subagents"] if allow_subagents and len(phase_packets) > 1 else [],
                "verification": phase["verification"],
                "status": "pending",
                "result_path": None,
            }
        )

    phases[0]["status"] = "ready"
    return {
        "schema_version": SCHEMA_VERSION,
        "run_id": manifest_id,
        "objective": objective,
        "recipe": {
            "id": selected_recipe,
            "purpose": recipe_data["purpose"],
            "signals": list(recipe_data["signals"]),
        },
        "created_at": created,
        "updated_at": created,
        "max_concurrency": max_concurrency,
        "final_integration_owner": "main Codex thread",
        "approval_gates": APPROVAL_GATES,
        "approval_state": {
            "real_subagents_authorized": bool(allow_subagents),
            "real_subagents_spawned": False,
            "authorization_note": (
                "Worker packets may be used after explicit authorization; this script still does not spawn them."
                if allow_subagents
                else "No real subagent authorization recorded."
            ),
        },
        "runtime_state": {
            "status": "planned",
            "current_phase_index": 1,
            "completed_phases": [],
            "blocked_reason": None,
            "next_action": "Review the manifest, then explicitly authorize any real subagent execution if needed.",
            "resume_count": 0,
        },
        "phases": phases,
        "worker_packets": packets,
        "cross_checks": [],
        "verification_rules": [
            "manifest has objective, recipe, phases, workers, gates, and owner",
            "real_subagents_spawned remains false unless a Delegation Receipt proves otherwise",
            "every phase has inputs, outputs, and verification rules",
            "receipt names accepted work, rejected work, and remaining approval gates",
        ],
        "receipt": None,
    }


def ensure_state_dirs() -> None:
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)


def manifest_path(run_id: str) -> Path:
    return RUN_DIR / f"{run_id}.json"


def save_manifest(manifest: dict[str, Any]) -> Path:
    ensure_state_dirs()
    manifest["updated_at"] = now_iso()
    path = manifest_path(manifest["run_id"])
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    LATEST.write_text(json.dumps({"run_id": manifest["run_id"], "path": str(path.relative_to(ROOT))}, indent=2) + "\n", encoding="utf-8")
    return path


def latest_run_id() -> str:
    if not LATEST.exists():
        raise FileNotFoundError("no dynamic workflow has been saved yet")
    data = json.loads(LATEST.read_text(encoding="utf-8"))
    return str(data["run_id"])


def load_manifest(run_id: str | None = None, path: str | None = None) -> dict[str, Any]:
    if path:
        manifest_file = Path(path)
        if not manifest_file.is_absolute():
            manifest_file = ROOT / manifest_file
    else:
        manifest_file = manifest_path(run_id or latest_run_id())
    return json.loads(manifest_file.read_text(encoding="utf-8"))


def save_manifest_to_path(manifest: dict[str, Any], path: str) -> Path:
    manifest_file = Path(path)
    if not manifest_file.is_absolute():
        manifest_file = ROOT / manifest_file
    manifest_file.parent.mkdir(parents=True, exist_ok=True)
    manifest["updated_at"] = now_iso()
    manifest_file.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest_file


def resolve_result_path(value: str) -> Path:
    result = Path(value)
    return result if result.is_absolute() else ROOT / result


def manifest_result_path(value: str) -> str:
    result = resolve_result_path(value)
    try:
        return str(result.relative_to(ROOT))
    except ValueError:
        return str(result)


def phase_result_rows(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for phase in sorted(manifest.get("phases", []), key=lambda item: item.get("index", 0)):
        if phase.get("status") == "completed":
            rows.append(
                {
                    "id": phase.get("id"),
                    "name": phase.get("name"),
                    "index": phase.get("index"),
                    "result_path": phase.get("result_path"),
                }
            )
    return rows


def verify_manifest(manifest: dict[str, Any]) -> tuple[bool, list[str]]:
    failures: list[str] = []
    if manifest.get("schema_version") != SCHEMA_VERSION:
        failures.append("schema_version mismatch")
    for field in ("run_id", "objective", "recipe", "phases", "worker_packets", "approval_gates", "runtime_state"):
        if not manifest.get(field):
            failures.append(f"missing {field}")
    if manifest.get("final_integration_owner") != "main Codex thread":
        failures.append("final integration owner must be main Codex thread")
    approval = manifest.get("approval_state", {})
    if approval.get("real_subagents_spawned"):
        failures.append("manifest claims real subagents spawned without external Delegation Receipt support")

    state = manifest.get("runtime_state", {})
    if state.get("status") not in RUNTIME_STATUSES:
        failures.append(f"unknown runtime status {state.get('status')}")

    phases = manifest.get("phases", [])
    phase_ids = [phase.get("id") for phase in phases]
    if len(phase_ids) != len(set(phase_ids)):
        failures.append("phase ids must be unique")
    phase_indices = [phase.get("index") for phase in phases]
    if sorted(phase_indices) != list(range(1, len(phases) + 1)):
        failures.append("phase indices must be contiguous starting at 1")
    current_index = state.get("current_phase_index")
    if current_index is not None and current_index not in phase_indices:
        failures.append("current_phase_index must reference an existing phase or be null")

    packet_by_id = {packet.get("id"): packet for packet in manifest.get("worker_packets", [])}
    completed_state = set(state.get("completed_phases", []))
    for completed_phase in completed_state:
        if completed_phase not in phase_ids:
            failures.append(f"completed phase {completed_phase} does not exist")

    for packet in manifest.get("worker_packets", []):
        if packet.get("status") not in PACKET_STATUSES:
            failures.append(f"packet {packet.get('id', '?')} has unknown status {packet.get('status')}")
        if packet.get("may_spawn_real_subagent"):
            failures.append(f"packet {packet.get('id', '?')} may not directly spawn real Codex subagents")
        if packet.get("status") == "completed":
            result = packet.get("last_result") or {}
            result_path = result.get("result_path")
            if not result_path:
                failures.append(f"packet {packet.get('id', '?')} completed without result_path")
            elif not resolve_result_path(str(result_path)).exists():
                failures.append(f"packet {packet.get('id', '?')} result_path does not exist: {result_path}")
            if result.get("real_subagents_spawned"):
                failures.append(f"packet {packet.get('id', '?')} claims real subagents spawned")

    for phase in phases:
        phase_id = phase.get("id", "?")
        if phase.get("status") not in PHASE_STATUSES:
            failures.append(f"phase {phase_id} has unknown status {phase.get('status')}")
        for field in ("id", "inputs", "outputs", "verification", "worker_packet_ids"):
            if not phase.get(field):
                failures.append(f"phase {phase_id} missing {field}")
        for packet_id in phase.get("worker_packet_ids", []):
            if packet_id not in packet_by_id:
                failures.append(f"phase {phase_id} references missing packet {packet_id}")
        if phase.get("status") == "completed":
            if phase_id not in completed_state:
                failures.append(f"phase {phase_id} completed but missing from runtime_state.completed_phases")
            result_path = phase.get("result_path")
            if not result_path:
                failures.append(f"phase {phase_id} completed without result_path")
            elif not resolve_result_path(str(result_path)).exists():
                failures.append(f"phase {phase_id} result_path does not exist: {result_path}")
            for packet_id in phase.get("worker_packet_ids", []):
                packet = packet_by_id.get(packet_id, {})
                if packet.get("status") != "completed":
                    failures.append(f"phase {phase_id} completed but packet {packet_id} is not completed")
        elif phase_id in completed_state:
            failures.append(f"runtime_state.completed_phases includes unfinished phase {phase_id}")

    receipt = manifest.get("receipt")
    if receipt and receipt.get("path") and not resolve_result_path(str(receipt["path"])).exists():
        failures.append(f"receipt path does not exist: {receipt['path']}")
    if manifest.get("max_concurrency", 0) < 1 or manifest.get("max_concurrency", 0) > 8:
        failures.append("max_concurrency must be between 1 and 8")
    return (not failures, failures)


def status_summary(manifest: dict[str, Any]) -> dict[str, Any]:
    phase_by_index = {phase["index"]: phase for phase in manifest.get("phases", [])}
    current = phase_by_index.get(manifest.get("runtime_state", {}).get("current_phase_index"))
    failed_packets = [
        packet["id"]
        for packet in manifest.get("worker_packets", [])
        if packet.get("status") in {"failed", "needs-retry"}
    ]
    rejected_checks = [
        check
        for check in manifest.get("cross_checks", [])
        if str(check.get("verdict", "")).lower() in {"rejected", "fail", "failed"}
    ]
    return {
        "run_id": manifest.get("run_id"),
        "objective": manifest.get("objective"),
        "recipe": manifest.get("recipe", {}).get("id"),
        "status": manifest.get("runtime_state", {}).get("status"),
        "current_phase": current["id"] if current else None,
        "current_phase_status": current.get("status") if current else None,
        "completed_phases": manifest.get("runtime_state", {}).get("completed_phases", []),
        "completed_phase_results": phase_result_rows(manifest),
        "failed_packets": failed_packets,
        "rejected_cross_checks": rejected_checks,
        "real_subagents_spawned": manifest.get("approval_state", {}).get("real_subagents_spawned", False),
        "next_action": manifest.get("runtime_state", {}).get("next_action"),
    }


def resume_manifest(manifest: dict[str, Any], note: str = "") -> dict[str, Any]:
    manifest = deepcopy(manifest)
    state = manifest["runtime_state"]
    state["resume_count"] = int(state.get("resume_count", 0)) + 1
    state["status"] = "ready-to-continue"
    state["blocked_reason"] = None
    state["next_action"] = note or "Continue with the current phase; spawn real subagents only after explicit approval."
    manifest["updated_at"] = now_iso()
    return manifest


def complete_phase(
    manifest: dict[str, Any],
    phase_id: str,
    *,
    result_path: str,
    summary: str,
    outputs: list[str] | None = None,
    execution_mode: str = "local main-thread phase execution",
    allow_out_of_order: bool = False,
) -> dict[str, Any]:
    manifest = deepcopy(manifest)
    result_file = resolve_result_path(result_path)
    if not result_file.exists():
        raise FileNotFoundError(f"phase result_path does not exist: {result_path}")

    phases = sorted(manifest["phases"], key=lambda item: item["index"])
    phase = next((item for item in phases if item["id"] == phase_id), None)
    if not phase:
        raise ValueError(f"unknown phase: {phase_id}")
    state = manifest["runtime_state"]
    if phase.get("status") == "completed":
        raise ValueError(f"phase already completed: {phase_id}")
    if not allow_out_of_order and state.get("current_phase_index") != phase["index"]:
        raise ValueError(
            f"phase {phase_id} is not current; current_phase_index is {state.get('current_phase_index')}"
        )

    stored_result_path = manifest_result_path(str(result_file))
    completed_at = now_iso()
    phase_outputs = outputs or list(phase.get("outputs", []))
    packet_by_id = {packet["id"]: packet for packet in manifest["worker_packets"]}
    packet_result = {
        "completed_at": completed_at,
        "result_path": stored_result_path,
        "summary": summary,
        "outputs": phase_outputs,
        "real_subagents_spawned": False,
        "execution_mode": execution_mode,
    }
    for packet_id in phase["worker_packet_ids"]:
        packet = packet_by_id[packet_id]
        packet["status"] = "completed"
        packet["attempts"] = int(packet.get("attempts", 0)) + 1
        packet["last_result"] = dict(packet_result)

    phase["status"] = "completed"
    phase["result_path"] = stored_result_path
    completed_phases = list(state.get("completed_phases", []))
    if phase_id not in completed_phases:
        completed_phases.append(phase_id)
    state["completed_phases"] = completed_phases
    state["blocked_reason"] = None

    next_phase = next((item for item in phases if item["index"] > phase["index"] and item.get("status") != "completed"), None)
    if next_phase:
        if next_phase.get("status") == "pending":
            next_phase["status"] = "ready"
        state["current_phase_index"] = next_phase["index"]
        state["status"] = "in-progress"
        state["next_action"] = f"Continue with {next_phase['id']} using {stored_result_path} as the previous phase handoff."
    else:
        state["current_phase_index"] = None
        state["status"] = "completed"
        state["next_action"] = "All workflow phases are complete; refresh the receipt and integrate the final result."

    manifest["updated_at"] = completed_at
    return manifest


def build_receipt(manifest: dict[str, Any]) -> dict[str, Any]:
    ok, failures = verify_manifest(manifest)
    summary = status_summary(manifest)
    receipt = {
        "run_id": manifest["run_id"],
        "objective": manifest["objective"],
        "recipe": manifest["recipe"]["id"],
        "manifest_valid": ok,
        "verification_failures": failures,
        "status": summary["status"],
        "completed_phases": summary["completed_phases"],
        "completed_phase_results": summary["completed_phase_results"],
        "failed_packets": summary["failed_packets"],
        "rejected_cross_checks": summary["rejected_cross_checks"],
        "real_subagents_spawned": summary["real_subagents_spawned"],
        "approval_gates_remaining": manifest["approval_gates"],
        "final_integration_owner": manifest["final_integration_owner"],
        "next_action": summary["next_action"],
        "created_at": now_iso(),
    }
    return receipt


def render_manifest(manifest: dict[str, Any]) -> str:
    summary = status_summary(manifest)
    lines = [
        "## Codex Dynamic Workflow Manifest",
        f"- **Run ID**: {manifest['run_id']}",
        f"- **Objective**: {manifest['objective']}",
        f"- **Recipe**: {manifest['recipe']['id']} - {manifest['recipe']['purpose']}",
        f"- **Status**: {summary['status']}",
        f"- **Current phase**: {summary['current_phase'] or 'none'}",
        f"- **Max concurrency**: {manifest['max_concurrency']}",
        f"- **Integration owner**: {manifest['final_integration_owner']}",
        f"- **Real subagents spawned**: {summary['real_subagents_spawned']}",
        f"- **Boundary**: {REAL_SUBAGENT_BOUNDARY}",
        "",
        "## Phases",
        "| # | Phase | Workers | Outputs | Verification |",
        "|---:|---|---|---|---|",
    ]
    packets = {packet["id"]: packet for packet in manifest["worker_packets"]}
    for phase in manifest["phases"]:
        workers = ", ".join(packets[packet_id]["worker"] for packet_id in phase["worker_packet_ids"])
        lines.append(
            f"| {phase['index']} | {phase['name']} | {workers} | {', '.join(phase['outputs'])} | {', '.join(phase['verification'])} |"
        )
    lines.extend(
        [
            "",
            "## Approval Gates",
            "- " + "\n- ".join(manifest["approval_gates"]),
            "",
            "## Next Action",
            f"- {summary['next_action']}",
        ]
    )
    return "\n".join(lines)


def render_status(manifest: dict[str, Any]) -> str:
    summary = status_summary(manifest)
    lines = [
        "## Codex Dynamic Workflow Status",
        f"- **Run ID**: {summary['run_id']}",
        f"- **Recipe**: {summary['recipe']}",
        f"- **Status**: {summary['status']}",
        f"- **Current phase**: {summary['current_phase'] or 'none'}",
        f"- **Current phase status**: {summary['current_phase_status'] or 'none'}",
        f"- **Completed phases**: {', '.join(summary['completed_phases']) or 'none'}",
        f"- **Failed packets**: {', '.join(summary['failed_packets']) or 'none'}",
        f"- **Rejected cross-checks**: {len(summary['rejected_cross_checks'])}",
        f"- **Real subagents spawned**: {summary['real_subagents_spawned']}",
        f"- **Next action**: {summary['next_action']}",
    ]
    if summary["completed_phase_results"]:
        lines.extend(["", "## Phase Results"])
        for row in summary["completed_phase_results"]:
            lines.append(f"- `{row['id']}`: `{row['result_path']}`")
    return "\n".join(lines)


def receipt_to_markdown(receipt: dict[str, Any]) -> str:
    lines = [
        "# Codex Dynamic Workflow Receipt",
        "",
        f"- **Run ID**: {receipt['run_id']}",
        f"- **Objective**: {receipt['objective']}",
        f"- **Recipe**: {receipt['recipe']}",
        f"- **Manifest valid**: {receipt['manifest_valid']}",
        f"- **Status**: {receipt['status']}",
        f"- **Completed phases**: {', '.join(receipt['completed_phases']) or 'none'}",
        f"- **Failed packets**: {', '.join(receipt['failed_packets']) or 'none'}",
        f"- **Rejected cross-checks**: {len(receipt['rejected_cross_checks'])}",
        f"- **Real subagents spawned**: {receipt['real_subagents_spawned']}",
        f"- **Integration owner**: {receipt['final_integration_owner']}",
        f"- **Next action**: {receipt['next_action']}",
    ]
    if receipt["completed_phase_results"]:
        lines.extend(["", "## Phase Results"])
        for row in receipt["completed_phase_results"]:
            lines.append(f"- `{row['id']}`: `{row['result_path']}`")
    lines.extend(["", "## Remaining Approval Gates"])
    lines.extend(f"- {gate}" for gate in receipt["approval_gates_remaining"])
    if receipt["verification_failures"]:
        lines.extend(["", "## Verification Failures"])
        lines.extend(f"- {failure}" for failure in receipt["verification_failures"])
    return "\n".join(lines) + "\n"


def save_receipt(manifest: dict[str, Any], receipt: dict[str, Any], manifest_path_arg: str | None = None) -> Path:
    ensure_state_dirs()
    path = RECEIPT_DIR / f"{manifest['run_id']}.md"
    path.write_text(receipt_to_markdown(receipt), encoding="utf-8")
    manifest["receipt"] = {
        "path": str(path.relative_to(ROOT)),
        "created_at": receipt["created_at"],
        "manifest_valid": receipt["manifest_valid"],
    }
    manifest["runtime_state"]["status"] = "receipt-ready"
    if manifest_path_arg:
        save_manifest_to_path(manifest, manifest_path_arg)
    else:
        save_manifest(manifest)
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan, track, verify, resume, and receipt Codex Dynamic Workflows.")
    sub = parser.add_subparsers(dest="command", required=True)

    plan = sub.add_parser("plan", help="Create a workflow manifest.")
    plan.add_argument("objective", nargs="+")
    plan.add_argument("--recipe", choices=sorted(RECIPES))
    plan.add_argument("--max-concurrency", type=int, default=4)
    plan.add_argument("--allow-subagents", action="store_true", help="Record explicit authorization for packet planning only.")
    plan.add_argument("--no-save", action="store_true", help="Render a manifest without saving it.")
    plan.add_argument("--json", action="store_true")

    status = sub.add_parser("status", help="Show saved workflow status.")
    status.add_argument("--run-id")
    status.add_argument("--path")
    status.add_argument("--json", action="store_true")

    resume = sub.add_parser("resume", help="Mark a saved workflow ready to continue.")
    resume.add_argument("--run-id")
    resume.add_argument("--path")
    resume.add_argument("--note", default="")
    resume.add_argument("--json", action="store_true")

    complete = sub.add_parser("complete-phase", help="Record a completed phase result and advance the saved workflow.")
    complete.add_argument("phase_id")
    complete.add_argument("--run-id")
    complete.add_argument("--path")
    complete.add_argument("--result-path", required=True)
    complete.add_argument("--summary", required=True)
    complete.add_argument("--outputs", nargs="*", default=None)
    complete.add_argument("--execution-mode", default="local main-thread phase execution")
    complete.add_argument("--allow-out-of-order", action="store_true")
    complete.add_argument("--json", action="store_true")

    verify = sub.add_parser("verify", help="Verify a saved workflow manifest.")
    verify.add_argument("--run-id")
    verify.add_argument("--path")
    verify.add_argument("--json", action="store_true")

    receipt = sub.add_parser("receipt", help="Create a receipt for a saved workflow.")
    receipt.add_argument("--run-id")
    receipt.add_argument("--path")
    receipt.add_argument("--no-save", action="store_true")
    receipt.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if args.command == "plan":
        manifest = build_manifest(
            " ".join(args.objective).strip(),
            recipe=args.recipe,
            allow_subagents=args.allow_subagents,
            max_concurrency=args.max_concurrency,
        )
        path = None if args.no_save else save_manifest(manifest)
        if args.json:
            payload = dict(manifest)
            if path:
                payload["manifest_path"] = str(path.relative_to(ROOT))
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print(render_manifest(manifest))
            if path:
                print(f"\nSaved: {path.relative_to(ROOT)}")
        return 0

    manifest = load_manifest(getattr(args, "run_id", None), getattr(args, "path", None))

    if args.command == "status":
        summary = status_summary(manifest)
        print(json.dumps(summary, indent=2, ensure_ascii=False) if args.json else render_status(manifest))
        return 0

    if args.command == "resume":
        updated = resume_manifest(manifest, args.note)
        if args.path:
            save_manifest_to_path(updated, args.path)
        else:
            save_manifest(updated)
        print(json.dumps(status_summary(updated), indent=2, ensure_ascii=False) if args.json else render_status(updated))
        return 0

    if args.command == "complete-phase":
        updated = complete_phase(
            manifest,
            args.phase_id,
            result_path=args.result_path,
            summary=args.summary,
            outputs=args.outputs,
            execution_mode=args.execution_mode,
            allow_out_of_order=args.allow_out_of_order,
        )
        if args.path:
            save_manifest_to_path(updated, args.path)
        else:
            save_manifest(updated)
        print(json.dumps(status_summary(updated), indent=2, ensure_ascii=False) if args.json else render_status(updated))
        return 0

    if args.command == "verify":
        ok, failures = verify_manifest(manifest)
        payload = {"ok": ok, "failures": failures, "run_id": manifest.get("run_id")}
        if args.json:
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print("CODEX DYNAMIC WORKFLOW VERIFY PASS" if ok else "CODEX DYNAMIC WORKFLOW VERIFY FAIL")
            for failure in failures:
                print(f"- {failure}")
        return 0 if ok else 1

    if args.command == "receipt":
        built_receipt = build_receipt(manifest)
        path = None if args.no_save else save_receipt(manifest, built_receipt, args.path)
        if args.json:
            payload = dict(built_receipt)
            if path:
                payload["receipt_path"] = str(path.relative_to(ROOT))
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print(receipt_to_markdown(built_receipt), end="")
            if path:
                print(f"\nSaved: {path.relative_to(ROOT)}")
        return 0 if built_receipt["manifest_valid"] else 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
