#!/usr/bin/env python3
"""Local Book One cockpit for the Sean Dollwet KDP proof system.

This tool manages evidence, checkpoints, pace, and upload readiness. It never
logs into KDP, submits a book, spends money, or performs another external action.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACE_ORDER = ("rapid_7", "launch_14", "editorial_30")
STAGES = (
    "DISCOVERY",
    "MARKET_VALIDATION",
    "BLUEPRINT",
    "GOLD_CHAPTER",
    "MANUSCRIPT",
    "COVER",
    "COMPLIANCE",
    "UPLOAD_READY",
    "LAUNCH",
    "MEASUREMENT",
)
AXIS_STATES = {
    "production": ("NO_EVENT", "DRAFTED", "QA_PASSED", "UPLOAD_READY", "SUBMITTED", "LIVE"),
    "capability": ("SOURCE_CAPTURED", "STRUCTURAL_PASS", "ORCHESTRATOR_ATTESTED", "RUNTIME_OBSERVED"),
    "market": ("NO_EVENT", "DISCOVERED", "SOLD", "NET_COLLECTED"),
    "permission": ("NO_PERMISSION", "APPROVED"),
}
GATE_NAMES = (
    "demand",
    "sources",
    "manuscript",
    "cover",
    "metadata",
    "rights",
    "ai_disclosure",
    "originality",
    "claim_support",
    "review_integrity",
    "preview",
)
APPROVAL_NAMES = ("niche", "outline", "gold_chapter", "cover", "upload")
ARTIFACT_NAMES = (
    "market_dossier",
    "claim_ledger",
    "ai_asset_ledger",
    "rights_ledger",
    "manuscript",
    "cover",
    "metadata",
    "review_plan",
    "preview_receipt",
)
REQUIRED_ARTIFACTS = ARTIFACT_NAMES
ALLOWED_EBOOK_SUFFIXES = {".docx", ".epub", ".kpf"}
REVIEW_FAILURE_PHRASES = (
    "in exchange for a review",
    "in exchange for your honest feedback",
    "gift card",
    "book bounty",
    "book reverb",
    "if you liked it, ask for",
    "points-based review",
    "reciprocal review",
    "review swap",
)


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def fail(message: str, code: int = 2) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(code)


def project_path(raw: str) -> Path:
    path = Path(raw).expanduser().resolve()
    forbidden = {Path("/").resolve(), Path.home().resolve(), ROOT.resolve()}
    if path in forbidden or len(path.parts) < 3:
        fail(f"unsafe project path: {path}")
    return path


def state_path(project: Path) -> Path:
    return project / "06-system" / "book-one-state.json"


def proof_path(project: Path) -> Path:
    return project / "06-system" / "proof-state.jsonl"


def receipt_path(project: Path) -> Path:
    return project / "06-system" / "compliance-receipt.json"


def cockpit_path(project: Path) -> Path:
    return project / "00-start-here" / "BOOK-ONE-COCKPIT.md"


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing state file: {path}; run init first")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")
    return {}


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def save_state(project: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = now()
    write_json_atomic(state_path(project), state)


def resolve_evidence(project: Path, raw: str | None) -> Path | None:
    if not raw:
        return None
    candidate = Path(raw).expanduser()
    if not candidate.is_absolute():
        candidate = project / candidate
    return candidate.resolve()


def append_event(
    project: Path,
    state: dict[str, Any],
    axis: str,
    event_state: str,
    evidence: str | None,
    source: str,
    note: str,
    value: float | None = None,
    currency: str | None = None,
) -> dict[str, Any]:
    evidence_class = "UNTESTED"
    claim_state = "UNCONFIRMED"
    if axis == "capability" and event_state == "SOURCE_CAPTURED":
        evidence_class, claim_state = "OBSERVED", "VERIFIED"
    elif evidence:
        evidence_class, claim_state = "OBSERVED", "VERIFIED"
    row = {
        "event_id": uuid.uuid4().hex,
        "timestamp": now(),
        "book_id": state["book_id"],
        "axis": axis,
        "state": event_state,
        "claim_state": claim_state,
        "evidence_class": evidence_class,
        "evidence_path": evidence,
        "value": value,
        "currency": currency,
        "source": source,
        "note": note,
    }
    proof_path(project).parent.mkdir(parents=True, exist_ok=True)
    with proof_path(project).open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True) + "\n")
    return row


def load_events(project: Path) -> list[dict[str, Any]]:
    path = proof_path(project)
    if not path.exists():
        return []
    rows = []
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            fail(f"invalid proof row {index}: {exc}")
    return rows


def latest_axes(project: Path) -> dict[str, str]:
    latest = {axis: states[0] for axis, states in AXIS_STATES.items()}
    for row in load_events(project):
        axis = row.get("axis")
        event_state = row.get("state")
        if axis in AXIS_STATES and event_state in AXIS_STATES[axis]:
            latest[axis] = event_state
    return latest


def default_state(pace: str) -> dict[str, Any]:
    timestamp = now()
    return {
        "schema_version": "1.0",
        "book_id": f"book-one-{uuid.uuid4().hex[:8]}",
        "created_at": timestamp,
        "updated_at": timestamp,
        "pace_profile": pace,
        "stage": "DISCOVERY",
        "channel": "amazon_kdp",
        "acquisition": "organic_only",
        "kdp_select": False,
        "book": {
            "topic": "",
            "audience": "",
            "problem": "",
            "promise": "",
            "risk_class": "low_risk_unclassified",
            "title": "",
            "subtitle": "",
        },
        "author_identity": {"mode": "market_first_pen_name", "pen_name": "", "lock_status": "PENDING"},
        "artifacts": {
            "market_dossier": {"path": "02-research/market-dossier.md", "status": "MISSING"},
            "claim_ledger": {"path": "02-research/claim-ledger.md", "status": "MISSING"},
            "ai_asset_ledger": {"path": "02-research/ai-asset-ledger.jsonl", "status": "MISSING"},
            "rights_ledger": {"path": "02-research/rights-ledger.md", "status": "MISSING"},
            "manuscript": {"path": "04-deliverables/manuscript.epub", "status": "MISSING"},
            "cover": {"path": "05-assets/cover.jpg", "status": "MISSING"},
            "metadata": {"path": "04-deliverables/metadata.md", "status": "MISSING"},
            "review_plan": {"path": "04-deliverables/review-plan.md", "status": "MISSING"},
            "preview_receipt": {"path": "06-system/preview-receipt.json", "status": "MISSING"},
        },
        "approvals": {
            name: {"status": "PENDING", "evidence": None, "approved_at": None} for name in APPROVAL_NAMES
        },
        "gates": {
            name: {"state": "NOT_RUN", "evidence": None, "note": ""} for name in GATE_NAMES
        },
        "next_action": "Complete the deep operator interview and define low-risk topic boundaries.",
    }


def render_cockpit(project: Path, state: dict[str, Any]) -> str:
    axes = latest_axes(project)
    approvals = "\n".join(
        f"- {name.replace('_', ' ').title()}: {entry['status']}"
        for name, entry in state["approvals"].items()
    )
    gates = "\n".join(
        f"- {name.replace('_', ' ').title()}: {entry['state']}"
        for name, entry in state["gates"].items()
    )
    book = state["book"]
    return f"""# Book One Cockpit — {state['book_id']}

## State

- Pace: `{state['pace_profile']}`
- Stage: `{state['stage']}`
- Channel: `{state['channel']}`
- Acquisition: `{state['acquisition']}`
- KDP Select: `{str(state['kdp_select']).lower()}`
- Topic: {book['topic'] or 'UNSET'}
- Reader: {book['audience'] or 'UNSET'}
- Pen name: {state['author_identity']['pen_name'] or 'PENDING'}

## Proof Axes

- Production: `{axes['production']}`
- Capability: `{axes['capability']}`
- Market: `{axes['market']}`
- Permission: `{axes['permission']}`

## Approvals

{approvals}

## Gates

{gates}

## Next Action

{state['next_action']}

## Boundary

This cockpit never publishes, spends, enrolls in KDP Select, or treats production progress as sales proof. Upload requires a separate explicit approval receipt.
"""


def cmd_init(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    if state_path(project).exists():
        fail(f"pilot already exists at {project}; use status")
    for relative in ("00-start-here", "01-source", "02-research", "06-system"):
        (project / relative).mkdir(parents=True, exist_ok=True)
    state = default_state(args.pace)
    write_json_atomic(state_path(project), state)
    source_pointer = project / "01-source" / "source-ledger.md"
    source_pointer.write_text(
        "# Book One Source Pointer\n\n"
        "Canonical corpus: `extractions/sean-dollwet-kdp-book-one-system/source-ledger.md`.\n"
        "Official policy: `skills/sean-dollwet-kdp-publishing/references/kdp-policy-and-evidence-boundary.md`.\n",
        encoding="utf-8",
    )
    append_event(project, state, "production", "NO_EVENT", None, "init", "No production event yet.")
    append_event(project, state, "capability", "SOURCE_CAPTURED", "01-source/source-ledger.md", "init", "Source package linked.")
    append_event(project, state, "market", "NO_EVENT", None, "init", "No discovery or buyer event yet.")
    append_event(project, state, "permission", "NO_PERMISSION", None, "init", "External upload is not approved.")
    cockpit_path(project).write_text(render_cockpit(project, state), encoding="utf-8")
    print(f"initialized: {project}")
    print(f"book_id: {state['book_id']}")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    state = read_json(state_path(project))
    payload = {
        "book_id": state["book_id"],
        "pace_profile": state["pace_profile"],
        "stage": state["stage"],
        "proof_axes": latest_axes(project),
        "next_action": state["next_action"],
    }
    if args.plain:
        for key, value in payload.items():
            print(f"{key}: {value}")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def cmd_configure(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    state = read_json(state_path(project))
    for field in ("topic", "audience", "problem", "promise", "risk_class", "title", "subtitle"):
        value = getattr(args, field)
        if value is not None:
            state["book"][field] = value
    if args.pen_name is not None:
        state["author_identity"]["pen_name"] = args.pen_name
        state["author_identity"]["lock_status"] = "LOCKED" if args.pen_name else "PENDING"
    if len((state["book"]["title"] + state["book"]["subtitle"]).strip()) > 200:
        fail("title plus subtitle exceeds 200 characters")
    save_state(project, state)
    print("configuration updated")
    return 0


def cmd_stage(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    state = read_json(state_path(project))
    current = STAGES.index(state["stage"])
    target = STAGES.index(args.set)
    if target < current:
        fail("stage regression is not allowed")
    if target > current + 1:
        fail("advance one stage at a time so checkpoints cannot be skipped")
    state["stage"] = args.set
    state["next_action"] = args.next_action or state["next_action"]
    save_state(project, state)
    print(f"stage: {args.set}")
    return 0


def cmd_artifact(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    state = read_json(state_path(project))
    if args.name not in ARTIFACT_NAMES:
        fail(f"unknown artifact: {args.name}")
    resolved = resolve_evidence(project, args.path)
    if args.status == "READY" and (not resolved or not resolved.exists()):
        fail("READY artifact path must exist")
    try:
        stored = str(resolved.relative_to(project)) if resolved else args.path
    except ValueError:
        stored = str(resolved)
    state["artifacts"][args.name] = {"path": stored, "status": args.status}
    save_state(project, state)
    print(f"artifact {args.name}: {args.status}")
    return 0


def cmd_gate(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    state = read_json(state_path(project))
    evidence = resolve_evidence(project, args.evidence)
    if args.state == "PASS" and (not evidence or not evidence.exists()):
        fail("PASS requires an existing evidence path")
    state["gates"][args.name] = {
        "state": args.state,
        "evidence": str(evidence) if evidence else None,
        "note": args.note or "",
    }
    save_state(project, state)
    print(f"gate {args.name}: {args.state}")
    return 0


def cmd_approve(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    state = read_json(state_path(project))
    evidence = resolve_evidence(project, args.evidence)
    if not evidence or not evidence.exists():
        fail("approval requires an existing evidence receipt")
    if args.checkpoint == "upload" and not args.explicit_upload_permission:
        fail("upload approval requires --explicit-upload-permission")
    state["approvals"][args.checkpoint] = {
        "status": "APPROVED",
        "evidence": str(evidence),
        "approved_at": now(),
    }
    save_state(project, state)
    if args.checkpoint == "upload":
        axes = latest_axes(project)
        if axes["permission"] != "APPROVED":
            append_event(project, state, "permission", "APPROVED", str(evidence), "operator", "Explicit upload permission recorded.")
    print(f"approval {args.checkpoint}: APPROVED")
    return 0


def cmd_record(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    state = read_json(state_path(project))
    sequence = AXIS_STATES[args.axis]
    current = latest_axes(project)[args.axis]
    if args.state == current:
        fail(f"duplicate state: {args.axis} is already {current}")
    if sequence.index(args.state) != sequence.index(current) + 1:
        fail(f"invalid transition: {args.axis} {current} -> {args.state}")
    evidence = resolve_evidence(project, args.evidence)
    if args.state not in {"NO_EVENT", "NO_PERMISSION"} and (not evidence or not evidence.exists()):
        fail("observed transitions require an existing evidence path")
    event = append_event(
        project,
        state,
        args.axis,
        args.state,
        str(evidence) if evidence else None,
        args.source,
        args.note or "",
        args.value,
        args.currency,
    )
    print(json.dumps(event, indent=2, sort_keys=True))
    return 0


def artifact_path(project: Path, state: dict[str, Any], name: str) -> Path:
    raw = state["artifacts"][name]["path"]
    path = Path(raw)
    return path if path.is_absolute() else project / path


def check_ai_ledger(path: Path, holds: list[str], blocking: list[str]) -> None:
    if not path.exists():
        holds.append("AI asset ledger is missing")
        return
    rows = []
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            blocking.append(f"AI asset ledger row {index} is invalid JSON")
    if not rows:
        holds.append("AI asset ledger has no asset rows")
    for row in rows:
        asset = row.get("asset_id", "unknown")
        mode = row.get("creation_mode")
        if mode not in {"human", "ai_assisted", "ai_generated", "third_party"}:
            blocking.append(f"asset {asset} has an invalid creation_mode")
        if mode == "ai_generated":
            if row.get("kdp_disclosure_required") is not True:
                blocking.append(f"AI-generated asset {asset} is not marked for KDP disclosure")
            if str(row.get("disclosure_answer", "")).lower() not in {"yes", "true", "ai_generated"}:
                blocking.append(f"AI-generated asset {asset} lacks a yes disclosure answer")
        if mode in {"ai_generated", "third_party"} and not row.get("rights_basis"):
            blocking.append(f"asset {asset} lacks rights basis")
        if str(row.get("status", "")).upper() != "PASS":
            holds.append(f"asset {asset} has not passed rights review")


def preflight(project: Path, state: dict[str, Any]) -> dict[str, Any]:
    holds: list[str] = []
    blocking: list[str] = []

    if state.get("channel") != "amazon_kdp":
        blocking.append("Book One channel drifted from amazon_kdp")
    if state.get("acquisition") != "organic_only":
        blocking.append("Book One acquisition drifted from organic_only")
    if state.get("kdp_select") is not False:
        blocking.append("KDP Select must remain off for the approved Book One pilot")
    if state["book"].get("risk_class") in {"excluded_high_stakes", "unreviewed_high_stakes"}:
        blocking.append("book is in an excluded or unreviewed high-stakes lane")
    if len((state["book"].get("title", "") + state["book"].get("subtitle", "")).strip()) > 200:
        blocking.append("title plus subtitle exceeds 200 characters")
    if not state["book"].get("title"):
        holds.append("book title is not set")

    for name, gate in state["gates"].items():
        gate_state = gate.get("state")
        if gate_state == "FAIL":
            blocking.append(f"gate failed: {name}")
        elif gate_state != "PASS":
            holds.append(f"gate not passed: {name}")
        elif not gate.get("evidence") or not Path(gate["evidence"]).exists():
            holds.append(f"gate evidence missing: {name}")

    for name in REQUIRED_ARTIFACTS:
        artifact = state["artifacts"][name]
        path = artifact_path(project, state, name)
        if artifact.get("status") != "READY" or not path.exists():
            holds.append(f"artifact not ready: {name}")

    manuscript = artifact_path(project, state, "manuscript")
    if manuscript.exists() and manuscript.suffix.lower() not in ALLOWED_EBOOK_SUFFIXES:
        holds.append("narrative ebook must be a previewed DOCX, EPUB, or KPF—not PDF-only")

    check_ai_ledger(artifact_path(project, state, "ai_asset_ledger"), holds, blocking)

    review_plan = artifact_path(project, state, "review_plan")
    if review_plan.exists():
        review_text = review_plan.read_text(encoding="utf-8", errors="ignore").lower()
        for phrase in REVIEW_FAILURE_PHRASES:
            if phrase in review_text:
                blocking.append(f"review plan contains prohibited tactic: {phrase}")

    for checkpoint in APPROVAL_NAMES[:-1]:
        if state["approvals"][checkpoint]["status"] != "APPROVED":
            holds.append(f"approval missing: {checkpoint}")

    holds = sorted(set(holds))
    blocking = sorted(set(blocking))
    if blocking:
        verdict = "BLOCKED"
    elif holds:
        verdict = "HOLD"
    elif state["approvals"]["upload"]["status"] == "APPROVED" and latest_axes(project)["permission"] == "APPROVED":
        verdict = "READY_TO_SUBMIT"
    else:
        verdict = "READY_FOR_APPROVAL"
    return {
        "schema_version": "1.0",
        "checked_at": now(),
        "book_id": state["book_id"],
        "verdict": verdict,
        "blocking": blocking,
        "holds": holds,
        "permission": latest_axes(project)["permission"],
        "external_action_performed": False,
    }


def cmd_preflight(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    state = read_json(state_path(project))
    receipt = preflight(project, state)
    if not args.dry_run:
        write_json_atomic(receipt_path(project), receipt)
    if args.json:
        print(json.dumps(receipt, indent=2, sort_keys=True))
    else:
        print(f"verdict: {receipt['verdict']}")
        for item in receipt["blocking"]:
            print(f"BLOCKED: {item}")
        for item in receipt["holds"]:
            print(f"HOLD: {item}")
    return 0 if receipt["verdict"] in {"READY_FOR_APPROVAL", "READY_TO_SUBMIT"} else 1


def cmd_escalate(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    state = read_json(state_path(project))
    failed = [name for name, gate in state["gates"].items() if gate["state"] != "PASS"]
    if not failed:
        print("no escalation: every gate passes")
        return 0
    current_index = PACE_ORDER.index(state["pace_profile"])
    if current_index == len(PACE_ORDER) - 1:
        print("pace remains editorial_30 until the gates pass")
        return 0
    state["pace_profile"] = PACE_ORDER[current_index + 1]
    state["next_action"] = f"Resolve failed gates at {state['pace_profile']} pace: {', '.join(failed)}."
    save_state(project, state)
    print(f"pace escalated: {state['pace_profile']}")
    return 0


def cmd_render(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    state = read_json(state_path(project))
    content = render_cockpit(project, state)
    if args.write:
        cockpit_path(project).parent.mkdir(parents=True, exist_ok=True)
        cockpit_path(project).write_text(content, encoding="utf-8")
        print(f"rendered: {cockpit_path(project)}")
    else:
        print(content)
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Manage the local KDP Book One proof cockpit.")
    sub = root.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("--project", required=True)
    init.add_argument("--pace", choices=PACE_ORDER, default="launch_14")
    init.set_defaults(func=cmd_init)

    status = sub.add_parser("status")
    status.add_argument("--project", required=True)
    status.add_argument("--plain", action="store_true")
    status.set_defaults(func=cmd_status)

    configure = sub.add_parser("configure")
    configure.add_argument("--project", required=True)
    for field in ("topic", "audience", "problem", "promise", "risk_class", "pen_name", "title", "subtitle"):
        configure.add_argument(f"--{field.replace('_', '-')}")
    configure.set_defaults(func=cmd_configure)

    stage = sub.add_parser("stage")
    stage.add_argument("--project", required=True)
    stage.add_argument("--set", choices=STAGES, required=True)
    stage.add_argument("--next-action")
    stage.set_defaults(func=cmd_stage)

    artifact = sub.add_parser("artifact")
    artifact.add_argument("--project", required=True)
    artifact.add_argument("--name", choices=ARTIFACT_NAMES, required=True)
    artifact.add_argument("--path", required=True)
    artifact.add_argument("--status", choices=("MISSING", "DRAFT", "READY"), required=True)
    artifact.set_defaults(func=cmd_artifact)

    gate = sub.add_parser("gate")
    gate.add_argument("--project", required=True)
    gate.add_argument("--name", choices=GATE_NAMES, required=True)
    gate.add_argument("--state", choices=("NOT_RUN", "HOLD", "PASS", "FAIL"), required=True)
    gate.add_argument("--evidence")
    gate.add_argument("--note")
    gate.set_defaults(func=cmd_gate)

    approve = sub.add_parser("approve")
    approve.add_argument("--project", required=True)
    approve.add_argument("--checkpoint", choices=APPROVAL_NAMES, required=True)
    approve.add_argument("--evidence", required=True)
    approve.add_argument("--explicit-upload-permission", action="store_true")
    approve.set_defaults(func=cmd_approve)

    record = sub.add_parser("record")
    record.add_argument("--project", required=True)
    record.add_argument("--axis", choices=tuple(AXIS_STATES), required=True)
    record.add_argument("--state", required=True)
    record.add_argument("--evidence")
    record.add_argument("--source", default="operator")
    record.add_argument("--note")
    record.add_argument("--value", type=float)
    record.add_argument("--currency")
    record.set_defaults(func=cmd_record)

    preflight_cmd = sub.add_parser("preflight")
    preflight_cmd.add_argument("--project", required=True)
    preflight_cmd.add_argument("--json", action="store_true")
    preflight_cmd.add_argument(
        "--dry-run",
        action="store_true",
        help="Evaluate and print the verdict without writing a compliance receipt.",
    )
    preflight_cmd.set_defaults(func=cmd_preflight)

    escalate = sub.add_parser("escalate")
    escalate.add_argument("--project", required=True)
    escalate.set_defaults(func=cmd_escalate)

    render = sub.add_parser("render")
    render.add_argument("--project", required=True)
    render.add_argument("--write", action="store_true")
    render.set_defaults(func=cmd_render)
    return root


def main() -> int:
    args = parser().parse_args()
    if args.command == "record" and args.state not in AXIS_STATES[args.axis]:
        fail(f"state {args.state} is invalid for axis {args.axis}")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
