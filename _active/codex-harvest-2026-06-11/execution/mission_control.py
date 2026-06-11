#!/usr/bin/env python3
"""Local Mission Control state helper for Codex Antigravity.

This is intentionally thin: it creates mission folders, stores compact state,
records handoffs, and checks that a mission has the minimum harness needed for
long-running work. It does not execute agents or bypass Codex approval rules.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path


def workspace_root() -> Path:
    override = os.environ.get("ANTIGRAVITY_ROOT")
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parent.parent


BASE = workspace_root()
MISSIONS_DIR = BASE / ".agent" / "missions"
DOCS_DIR = BASE / "docs"
MISSION_ARTIFACTS_DIR = DOCS_DIR / "mission-artifacts"
INTENT_MEMORY_PATH = BASE / ".agent" / "intent-memory" / "current.json"
COHESION_STATE_PATH = BASE / ".agent" / "system-cohesion-state.json"
SESSION_STATE_PATH = BASE / ".agent" / "session-state.md"

ENFORCED_STATUSES = {"active", "validating", "complete"}
TERMINAL_ACTIVATION_STATUSES = {"complete", "blocked", "skipped"}
ACTIVATION_STATUSES = ["planned", "active", "complete", "blocked", "skipped"]

ENGINEERING_ARTIFACTS = [
    (
        "strategy_anchor",
        "strategy-anchor.md",
        "Mission strategy grounding; summarize STRATEGY.md when present or capture the guiding bet.",
    ),
    (
        "requirements",
        "requirements.md",
        "Requirements with stable R/A/F/AE identifiers before planning.",
    ),
    (
        "unit_plan",
        "plan.md",
        "Implementation or workstream plan with stable U-IDs, sequencing, risks, and tests.",
    ),
    (
        "review_ledger",
        "review.md",
        "Scrutiny and user-outcome review record, including residual work decisions.",
    ),
    (
        "solution_capture",
        "solution-capture.md",
        "Fresh solved-problem or reusable-knowledge capture for docs/solutions when generalizable.",
    ),
    (
        "pulse",
        "pulse.md",
        "Post-ship or post-delivery signal report, with docs/pulse-reports handoff when applicable.",
    ),
]


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug[:72] or "mission"


def mission_dir(slug: str) -> Path:
    return MISSIONS_DIR / slug


def state_path(slug: str) -> Path:
    return mission_dir(slug) / "mission.json"


def markdown_path(slug: str) -> Path:
    return mission_dir(slug) / "mission.md"


def artifact_root(slug: str) -> Path:
    return MISSION_ARTIFACTS_DIR / slug


def rel(path: Path) -> str:
    return path.relative_to(BASE).as_posix()


def clean_list(values: list | None) -> list:
    if not values:
        return []
    cleaned = []
    seen = set()
    for value in values:
        item = value
        if isinstance(value, str):
            item = value.strip()
        if item in ("", None):
            continue
        key = json.dumps(item, sort_keys=True) if isinstance(item, dict) else str(item)
        if key not in seen:
            cleaned.append(item)
            seen.add(key)
    return cleaned


def safe_rel(path: Path) -> str:
    try:
        return rel(path)
    except ValueError:
        return str(path)


def evidence_path_exists(value: str) -> bool:
    value = (value or "").strip()
    if not value:
        return False
    if value.startswith(("http://", "https://")):
        return True
    clean_value = value.split("#", 1)[0]
    path = Path(clean_value).expanduser()
    if not path.is_absolute():
        path = BASE / path
    return path.exists()


def split_path_anchor(value: str) -> tuple[str, str]:
    value = (value or "").strip()
    if "#" not in value:
        return value, ""
    path, anchor = value.split("#", 1)
    return path, anchor


def package_path_exists(value: str) -> bool:
    value = (value or "").strip()
    if not value:
        return False
    if value.startswith(("http://", "https://")):
        return True
    clean_value, _ = split_path_anchor(value)
    path = Path(clean_value).expanduser()
    if not path.is_absolute():
        path = BASE / path
    return path.exists()


def normalize_assertion(assertion: object, index: int) -> dict:
    if isinstance(assertion, dict):
        item = dict(assertion)
    else:
        item = {"statement": str(assertion)}
    item.setdefault("id", f"VA{index}")
    item.setdefault("statement", "")
    item.setdefault("covered_by", "")
    item.setdefault("validator", "")
    item.setdefault("pass_signal", "")
    return item


def normalize_activation_item(item: object, index: int) -> dict:
    if isinstance(item, dict):
        normalized = dict(item)
    else:
        normalized = {"expected_artifact": str(item)}

    normalized.setdefault("id", f"A{index}")
    normalized.setdefault("owner", "")
    normalized.setdefault("workflow", "")
    normalized.setdefault("expected_artifact", "")
    normalized.setdefault("status", "planned")
    normalized.setdefault("evidence_path", "")
    normalized.setdefault("validation_assertion", "")
    normalized.setdefault("blocker", "")
    normalized.setdefault("next_action", "")
    normalized.setdefault("kind", "workstream")
    normalized.setdefault("updated_at", "")
    if normalized["status"] not in ACTIVATION_STATUSES:
        normalized["status"] = "planned"
    return normalized


def default_resume_packet(slug: str) -> dict:
    return {
        "required": False,
        "fresh_session_packet": "",
        "resume_command": f"/mission resume {slug}",
        "next_command": "",
        "notes": "",
        "state_sources": [
            f".agent/missions/{slug}/mission.json",
            ".agent/intent-memory/current.json",
            ".agent/system-cohesion-state.json",
        ],
    }


def is_deployment_style(state: dict) -> bool:
    haystack = " ".join(
        [
            str(state.get("name", "")),
            str(state.get("slug", "")),
            str(state.get("goal", "")),
            str(state.get("mode", "")),
        ]
    ).lower()
    return any(
        term in haystack
        for term in (
            "deploy",
            "deployment",
            "launch",
            "post",
            "outreach",
            "daily",
            "go-to-market",
            "go to market",
        )
    )


def build_execution_receipt(state: dict) -> dict:
    queue = state.get("activation_queue", [])
    explicit = state.get("execution_receipt", {}) if isinstance(state.get("execution_receipt"), dict) else {}
    planned = [item["id"] for item in queue]
    executed = [item["id"] for item in queue if item.get("status") == "complete"]
    skipped = [
        f"{item['id']}: {item.get('blocker') or item.get('next_action') or 'no reason recorded'}"
        for item in queue
        if item.get("status") in {"blocked", "skipped"}
    ]
    proof = [
        item["evidence_path"]
        for item in queue
        if item.get("evidence_path")
    ]
    validators = [
        assertion.get("validator", "")
        for assertion in state.get("validation_assertions", [])
        if assertion.get("validator")
    ]
    receipt = {
        "planned_lanes": clean_list(explicit.get("planned_lanes", []) + planned),
        "executed_lanes": clean_list(explicit.get("executed_lanes", []) + executed),
        "skipped_lanes": clean_list(explicit.get("skipped_lanes", []) + skipped),
        "proof_artifacts": clean_list(explicit.get("proof_artifacts", []) + proof),
        "validators_run": clean_list(explicit.get("validators_run", []) + validators),
        "resume_command": explicit.get("resume_command")
        or state.get("resume_packet", {}).get("resume_command")
        or f"/mission resume {state.get('slug', 'mission')}",
    }
    return receipt


def normalize_state(state: dict) -> dict:
    state = dict(state)
    slug = state.get("slug") or slugify(state.get("name", "mission"))
    state.setdefault("created_at", now())
    state.setdefault("goal", "")
    state.setdefault("handoffs", [])
    state.setdefault("artifact_contract", build_artifact_contract(slug, "none"))
    state.setdefault(
        "librarian",
        {"notes": "", "required": False, "status": "not_applicable"},
    )
    state.setdefault("mode", "general")
    state.setdefault("name", slug.replace("-", " ").title())
    state["slug"] = slug
    state.setdefault("status", "planned")
    state.setdefault("updated_at", state.get("created_at", now()))
    state["validation_assertions"] = [
        normalize_assertion(assertion, index)
        for index, assertion in enumerate(state.get("validation_assertions", []), start=1)
    ]
    state["activation_queue"] = [
        normalize_activation_item(item, index)
        for index, item in enumerate(state.get("activation_queue", []), start=1)
    ]
    resume_packet = default_resume_packet(slug)
    if isinstance(state.get("resume_packet"), dict):
        resume_packet.update(state["resume_packet"])
    if is_deployment_style(state):
        resume_packet["required"] = True
    resume_packet["state_sources"] = clean_list(resume_packet.get("state_sources", []))
    state["resume_packet"] = resume_packet
    state["approved_package_load_set"] = normalize_package_load_set(
        state.get("approved_package_load_set", [])
    )
    state["package_boundaries"] = clean_list(state.get("package_boundaries", []))
    state["context_requirements"] = clean_list(state.get("context_requirements", []))
    state["execution_receipt"] = build_execution_receipt(state)
    return state


def normalize_package_load_set(items: list | None) -> list[dict]:
    normalized = []
    seen = set()
    for index, item in enumerate(items or [], start=1):
        if isinstance(item, str):
            entry = {
                "id": f"P{index}",
                "path": item,
                "role": "",
                "reason": "",
                "required": True,
            }
        elif isinstance(item, dict):
            entry = {
                "id": item.get("id") or f"P{index}",
                "path": item.get("path") or "",
                "role": item.get("role") or "",
                "reason": item.get("reason") or "",
                "required": item.get("required", True),
            }
        else:
            continue
        if not entry["path"]:
            continue
        key = entry["path"]
        if key in seen:
            continue
        seen.add(key)
        normalized.append(entry)
    return normalized


def replace_or_append(items: list[dict], item: dict) -> list[dict]:
    item_id = item["id"]
    replaced = False
    updated = []
    for existing in items:
        if existing.get("id") == item_id:
            updated.append(item)
            replaced = True
        else:
            updated.append(existing)
    if not replaced:
        updated.append(item)
    return updated


def build_artifact_contract(slug: str, contract_type: str) -> dict:
    if contract_type == "none":
        return {"type": "none", "required": False, "root": "", "artifacts": []}

    if contract_type != "engineering":
        raise SystemExit(f"Unsupported artifact contract: {contract_type}")

    root = artifact_root(slug)
    return {
        "type": "engineering",
        "required": True,
        "root": rel(root),
        "artifacts": [
            {
                "kind": kind,
                "path": rel(root / filename),
                "purpose": purpose,
                "status": "created",
            }
            for kind, filename, purpose in ENGINEERING_ARTIFACTS
        ],
    }


def artifact_template(kind: str, state: dict) -> str:
    slug = state["slug"]
    name = state["name"]
    goal = state["goal"]
    created = state["created_at"][:10]

    templates = {
        "strategy_anchor": f"""# Strategy Anchor: {name}

Created: {created}
Mission: {slug}

## Target Problem
[What is broken, costly, unclear, slow, or strategically important?]

## Guiding Bet
[What approach will shape decisions during this mission?]

## Audience
[Who benefits from the mission outcome?]

## Key Metrics Or Proof Signals
- [Signal 1]
- [Signal 2]

## Active Tracks
- [Track 1]
- [Track 2]

## Source Strategy
- Root `STRATEGY.md` checked: [yes/no/not applicable]
- Mission-local strategy decision: {goal}
""",
        "requirements": f"""# Requirements: {name}

Created: {created}
Mission: {slug}

## Problem Frame
{goal}

## Requirements
- R1. [Required outcome or behavior]
- R2. [Required outcome or behavior]

## Actors
- A1. [Person, system, workflow, or agent affected]

## Key Flows
- F1. [Start state -> action -> end state]

## Acceptance Examples
- AE1. Given [context], when [action], then [observable result].

## Scope Boundaries
- In scope: [what this mission owns]
- Out of scope: [what this mission will not change]

## Open Questions
- Blocking: [none or question]
- Deferred: [none or question]
""",
        "unit_plan": f"""# Unit Plan: {name}

Created: {created}
Mission: {slug}

Stable-ID rule: never renumber existing U-IDs after reordering, splitting, or deleting units.

## Implementation Units
- U1. **[Unit name]**
  - Covers: R1, AE1
  - Scope: [files, artifacts, workflows, or surfaces]
  - Decision: [guardrail, not step-by-step code]
  - Tests or verification: [machine check, behavior check, review pass]
  - Dependencies: [none or U-ID]

## Sequencing
1. U1

## Risks
- [Risk]: [mitigation]

## Validation Mapping
| Assertion | Covered by U-ID | Validator | Pass signal |
|---|---|---|---|
| [Assertion] | U1 | [scrutiny/user-outcome] | [observable pass signal] |
""",
        "review_ledger": f"""# Review Ledger: {name}

Created: {created}
Mission: {slug}

## Scrutiny Review
- Scope reviewed:
- Checks run:
- Findings:
- Fixes applied:

## User-Outcome Review
- Intended user/client experience:
- Evidence inspected:
- Gaps:
- Decision:

## Residual Work
| ID | Severity | Finding | Decision | Durable sink |
|---|---|---|---|---|
| RW1 | [P0-P3] | [finding] | [fix/file/accept/stop] | [path or issue] |
""",
        "solution_capture": f"""# Solution Capture: {name}

Created: {created}
Mission: {slug}

Use this while context is fresh. If the learning is generalizable, copy or convert it into `docs/solutions/`.

## Track
- Type: [bug / knowledge / workflow / architecture]

## Symptoms Or Context
- [What happened or what was learned?]

## What Did Not Work
- [Failed attempt, false assumption, or discarded route]

## Working Solution Or Durable Guidance
- [What solved it or what should future agents do?]

## Why This Works
- [Mechanism, constraint, or evidence]

## Prevention Or Reuse
- [Rule, check, template, or workflow update]

## Generalization Decision
- Keep mission-local: [yes/no]
- Promote to `docs/solutions/`: [yes/no/path]
""",
        "pulse": f"""# Pulse: {name}

Created: {created}
Mission: {slug}

Use after a release, delivery, experiment, or meaningful mission milestone. Keep it single-page.

## Headlines
- [What changed?]
- [What mattered?]

## Usage Or Adoption
- [Observable usage, completion, client response, or operational signal]

## System Or Delivery Performance
- [Errors, latency, quality issues, handoff friction, or operational load]

## Quality Sample
- [Small sample of outcomes or sessions, anonymized when relevant]

## Followups
- F1. [Followup worth routing into ideation, debugging, hardening, or a new mission]

## Report Decision
- Save or mirror to `docs/pulse-reports/`: [yes/no/path]
""",
    }
    return templates[kind]


def write_artifact_contract_files(state: dict) -> None:
    contract = state.get("artifact_contract", {})
    if contract.get("type") != "engineering":
        return

    root = BASE / contract["root"]
    root.mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / "solutions").mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / "pulse-reports").mkdir(parents=True, exist_ok=True)

    for artifact in contract.get("artifacts", []):
        path = BASE / artifact["path"]
        if not path.exists():
            path.write_text(artifact_template(artifact["kind"], state), encoding="utf-8")


def read_state(slug: str) -> dict:
    path = state_path(slug)
    if not path.exists():
        raise SystemExit(f"Mission not found: {slug}")
    return normalize_state(json.loads(path.read_text(encoding="utf-8")))


def write_state(slug: str, state: dict) -> None:
    state = normalize_state(state)
    path = state_path(slug)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_markdown(state: dict) -> str:
    state = normalize_state(state)
    handoffs = state.get("handoffs", [])
    handoff_lines = "\n".join(
        f"- {item['created_at']} | {item['role']} | {item['summary']}" for item in handoffs
    ) or "- None yet"
    assertions = state.get("validation_assertions", [])
    assertion_lines = "\n".join(
        "| {id} | {statement} | {covered_by} | {validator} | {pass_signal} |".format(
            id=item.get("id", ""),
            statement=item.get("statement", ""),
            covered_by=item.get("covered_by", ""),
            validator=item.get("validator", ""),
            pass_signal=item.get("pass_signal", ""),
        )
        for item in assertions
    ) or "| - | No assertions recorded yet | - | - | - |"
    queue = state.get("activation_queue", [])
    queue_lines = "\n".join(
        "| {id} | {owner} | {workflow} | {status} | {expected_artifact} | {evidence_path} | {validation_assertion} | {blocker} | {next_action} |".format(
            id=item.get("id", ""),
            owner=item.get("owner", ""),
            workflow=item.get("workflow", ""),
            status=item.get("status", ""),
            expected_artifact=item.get("expected_artifact", ""),
            evidence_path=item.get("evidence_path", ""),
            validation_assertion=item.get("validation_assertion", ""),
            blocker=item.get("blocker", ""),
            next_action=item.get("next_action", ""),
        )
        for item in queue
    ) or "| - | No activation items recorded yet | - | - | - | - | - | - | - |"
    receipt = state.get("execution_receipt", {})
    default_resume_command = f"/mission resume {state['slug']}"
    receipt_lines = [
        f"- Planned lanes: {', '.join(receipt.get('planned_lanes', [])) or '[none]'}",
        f"- Executed lanes: {', '.join(receipt.get('executed_lanes', [])) or '[none]'}",
        f"- Skipped or blocked lanes: {', '.join(receipt.get('skipped_lanes', [])) or '[none]'}",
        f"- Proof artifacts: {', '.join(receipt.get('proof_artifacts', [])) or '[none]'}",
        f"- Validators run: {', '.join(receipt.get('validators_run', [])) or '[none]'}",
        f"- Resume command: {receipt.get('resume_command') or default_resume_command}",
    ]
    resume_packet = state.get("resume_packet", default_resume_packet(state["slug"]))
    resume_lines = [
        f"- Required: {resume_packet.get('required', False)}",
        f"- Fresh session packet: `{resume_packet.get('fresh_session_packet') or '[none]'}`",
        f"- Resume command: `{resume_packet.get('resume_command') or default_resume_command}`",
        f"- Next command: `{resume_packet.get('next_command') or '[none]'}`",
        f"- State sources: {', '.join(resume_packet.get('state_sources', [])) or '[none]'}",
        f"- Notes: {resume_packet.get('notes') or '[none]'}",
    ]
    contract = state.get("artifact_contract", {"type": "none", "artifacts": []})
    if contract.get("type") == "engineering":
        artifact_lines = "\n".join(
            f"| {item['kind']} | `{item['path']}` | {item['status']} | {item['purpose']} |"
            for item in contract.get("artifacts", [])
        )
        artifact_section = f"""## Artifact Contract
- Type: engineering
- Root: `{contract['root']}`
- Rule: Strategy, requirements, U-ID plans, review, learning capture, and pulse reports are durable mission artifacts.

| Kind | Path | Status | Purpose |
|---|---|---|---|
{artifact_lines}
"""
    else:
        artifact_section = """## Artifact Contract
- Type: none
"""
    package_items = state.get("approved_package_load_set", [])
    if package_items:
        package_lines = "\n".join(
            "| {id} | `{path}` | {role} | {required} | {reason} |".format(
                id=item.get("id", ""),
                path=item.get("path", ""),
                role=item.get("role", ""),
                required=item.get("required", True),
                reason=item.get("reason", ""),
            )
            for item in package_items
        )
        boundary_lines = "\n".join(
            f"- {item}" for item in state.get("package_boundaries", [])
        ) or "- [none]"
        requirement_lines = "\n".join(
            f"- {item}" for item in state.get("context_requirements", [])
        ) or "- [none]"
        package_section = f"""## Approved Package Load Set
Mission-backed workflows must load this context before drafting, routing, or handing off.

| ID | Path | Role | Required | Reason |
|---|---|---|---:|---|
{package_lines}

### Package Boundaries
{boundary_lines}

### Context Requirements
{requirement_lines}
"""
    else:
        package_section = """## Approved Package Load Set
- None recorded.
"""

    return f"""# Mission: {state['name']}

## Charter
- Slug: {state['slug']}
- Mode: {state['mode']}
- Status: {state['status']}
- Goal: {state['goal']}
- Created: {state['created_at']}
- Updated: {state['updated_at']}
- Librarian: {state.get('librarian', {}).get('status', 'not_recorded')}

## Validation Contract
- Define correctness before execution.
- Assign every feature or workstream to at least one assertion.
- Run scrutiny and user-outcome validators at milestone boundaries.

| ID | Assertion | Covered by | Validator | Pass signal |
|---|---|---|---|---|
{assertion_lines}

{artifact_section}

{package_section}

## Mission Activation Queue
| ID | Owner | Workflow/Skill | Status | Expected artifact | Evidence path | Assertion | Blocker | Next action |
|---|---|---|---|---|---|---|---|---|
{queue_lines}

## Execution Receipt
{chr(10).join(receipt_lines)}

## Fresh Session Packet
{chr(10).join(resume_lines)}

## Handoffs
{handoff_lines}
"""


def write_markdown(state: dict) -> None:
    markdown_path(state["slug"]).write_text(render_markdown(state), encoding="utf-8")


def create(args: argparse.Namespace) -> None:
    slug = slugify(args.slug or args.name)
    path = state_path(slug)
    if path.exists() and not args.force:
        raise SystemExit(f"Mission already exists: {slug}. Use --force to overwrite.")

    state = {
        "created_at": now(),
        "goal": args.goal,
        "handoffs": [],
        "artifact_contract": build_artifact_contract(slug, args.artifact_contract),
        "librarian": {
            "notes": "",
            "required": args.librarian_required,
            "status": "pending" if args.librarian_required else "not_applicable",
        },
        "mode": args.mode,
        "name": args.name,
        "slug": slug,
        "status": "planned",
        "updated_at": now(),
        "validation_assertions": [],
        "activation_queue": [],
        "resume_packet": {
            **default_resume_packet(slug),
            "fresh_session_packet": args.fresh_session_packet or "",
            "next_command": args.next_command or "",
            "required": args.fresh_session_required,
        },
    }
    write_state(slug, state)
    write_markdown(state)
    write_artifact_contract_files(state)
    print(f"Created mission: {slug}")
    print(f"State: {state_path(slug).relative_to(BASE)}")
    print(f"Brief: {markdown_path(slug).relative_to(BASE)}")
    if state["artifact_contract"]["type"] != "none":
        print(f"Artifacts: {state['artifact_contract']['root']}")


def list_missions(_: argparse.Namespace) -> None:
    MISSIONS_DIR.mkdir(parents=True, exist_ok=True)
    paths = sorted(MISSIONS_DIR.glob("*/mission.json"))
    if not paths:
        print("No missions found.")
        return
    for path in paths:
        state = normalize_state(json.loads(path.read_text(encoding="utf-8")))
        print(f"{state['slug']} | {state['status']} | {state['mode']} | {state['name']}")


def status(args: argparse.Namespace) -> None:
    state = read_state(args.slug)
    print(f"Mission: {state['name']}")
    print(f"Slug: {state['slug']}")
    print(f"Status: {state['status']}")
    print(f"Mode: {state['mode']}")
    print(f"Goal: {state['goal']}")
    librarian = state.get("librarian", {})
    print(f"Librarian: {librarian.get('status', 'not_recorded')}")
    contract = state.get("artifact_contract", {"type": "none"})
    print(f"Artifact contract: {contract.get('type', 'none')}")
    if contract.get("root"):
        print(f"Artifact root: {contract['root']}")
    print(f"Handoffs: {len(state.get('handoffs', []))}")
    print(f"Validation assertions: {len(state.get('validation_assertions', []))}")
    print(f"Activation items: {len(state.get('activation_queue', []))}")
    packet = state.get("resume_packet", default_resume_packet(state["slug"]))
    print(f"Fresh session packet: {packet.get('fresh_session_packet') or '[none]'}")
    print(f"Next command: {packet.get('next_command') or '[none]'}")
    print(f"Updated: {state['updated_at']}")


def set_status(args: argparse.Namespace) -> None:
    state = read_state(args.slug)
    state["status"] = args.status
    state["updated_at"] = now()
    write_state(args.slug, state)
    write_markdown(state)
    print(f"Updated {args.slug} status to {args.status}")


def add_handoff(args: argparse.Namespace) -> None:
    state = read_state(args.slug)
    state.setdefault("handoffs", []).append(
        {
            "commands": args.commands,
            "created_at": now(),
            "issues": args.issues,
            "next": args.next,
            "role": args.role,
            "summary": args.summary,
        }
    )
    state["updated_at"] = now()
    write_state(args.slug, state)
    write_markdown(state)
    print(f"Added handoff to {args.slug}")


def mark_librarian(args: argparse.Namespace) -> None:
    state = read_state(args.slug)
    state["librarian"] = {
        "notes": args.notes,
        "required": args.required or state.get("librarian", {}).get("required", False),
        "status": args.status,
    }
    state["updated_at"] = now()
    write_state(args.slug, state)
    write_markdown(state)
    print(f"Updated librarian status for {args.slug} to {args.status}")


def add_assertion(args: argparse.Namespace) -> None:
    state = read_state(args.slug)
    assertion = normalize_assertion(
        {
            "id": args.id,
            "statement": args.statement,
            "covered_by": args.covered_by,
            "validator": args.validator,
            "pass_signal": args.pass_signal,
        },
        len(state.get("validation_assertions", [])) + 1,
    )
    state["validation_assertions"] = replace_or_append(
        state.get("validation_assertions", []),
        assertion,
    )
    state["updated_at"] = now()
    write_state(args.slug, state)
    write_markdown(state)
    print(f"Recorded validation assertion {assertion['id']} for {args.slug}")


def add_activation(args: argparse.Namespace) -> None:
    state = read_state(args.slug)
    item = normalize_activation_item(
        {
            "id": args.id,
            "owner": args.owner,
            "workflow": args.workflow,
            "expected_artifact": args.expected_artifact,
            "status": args.status,
            "evidence_path": args.evidence_path,
            "validation_assertion": args.validation_assertion,
            "blocker": args.blocker,
            "next_action": args.next_action,
            "kind": args.kind,
            "updated_at": now(),
        },
        len(state.get("activation_queue", [])) + 1,
    )
    state["activation_queue"] = replace_or_append(state.get("activation_queue", []), item)
    state["updated_at"] = now()
    write_state(args.slug, state)
    write_markdown(state)
    print(f"Recorded activation item {item['id']} for {args.slug}")


def set_activation(args: argparse.Namespace) -> None:
    state = read_state(args.slug)
    queue = []
    found = False
    for item in state.get("activation_queue", []):
        if item.get("id") != args.id:
            queue.append(item)
            continue
        found = True
        updated = dict(item)
        for field, value in {
            "owner": args.owner,
            "workflow": args.workflow,
            "expected_artifact": args.expected_artifact,
            "status": args.status,
            "evidence_path": args.evidence_path,
            "validation_assertion": args.validation_assertion,
            "blocker": args.blocker,
            "next_action": args.next_action,
            "kind": args.kind,
        }.items():
            if value is not None:
                updated[field] = value
        updated["updated_at"] = now()
        queue.append(normalize_activation_item(updated, len(queue) + 1))
    if not found:
        raise SystemExit(f"Activation item not found: {args.id}")
    state["activation_queue"] = queue
    state["updated_at"] = now()
    write_state(args.slug, state)
    write_markdown(state)
    print(f"Updated activation item {args.id} for {args.slug}")


def set_resume_packet(args: argparse.Namespace) -> None:
    state = read_state(args.slug)
    packet = state.get("resume_packet", default_resume_packet(args.slug))
    for field, value in {
        "fresh_session_packet": args.fresh_session_packet,
        "resume_command": args.resume_command,
        "next_command": args.next_command,
        "notes": args.notes,
    }.items():
        if value is not None:
            packet[field] = value
    if args.required:
        packet["required"] = True
    if args.state_source is not None:
        packet["state_sources"] = clean_list(args.state_source)
    state["resume_packet"] = packet
    state["updated_at"] = now()
    write_state(args.slug, state)
    write_markdown(state)
    print(f"Updated resume packet for {args.slug}")


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def state_mtime(path: Path) -> float:
    return path.stat().st_mtime if path.exists() else 0.0


def source_slug(payload: dict, kind: str) -> str:
    if kind == "intent":
        return str(payload.get("mission", {}).get("slug", ""))
    return str(payload.get("mission", {}).get("slug", ""))


def resume_diagnostics(slug: str) -> tuple[str, list[str]]:
    session_text = SESSION_STATE_PATH.read_text(encoding="utf-8", errors="ignore") if SESSION_STATE_PATH.exists() else ""
    intent = load_json(INTENT_MEMORY_PATH)
    cohesion = load_json(COHESION_STATE_PATH)
    intent_slug = source_slug(intent, "intent")
    cohesion_slug = source_slug(cohesion, "cohesion")
    newer_structured = max(state_mtime(INTENT_MEMORY_PATH), state_mtime(COHESION_STATE_PATH)) > state_mtime(SESSION_STATE_PATH)
    warnings = []
    preferred = "mission-state"

    if intent_slug == slug or cohesion_slug == slug:
        preferred = "intent-memory + system-cohesion"
    if newer_structured and preferred == "intent-memory + system-cohesion":
        warnings.append("structured intent/cohesion state is newer than .agent/session-state.md")
    if session_text and slug not in session_text and preferred == "intent-memory + system-cohesion":
        warnings.append(".agent/session-state.md does not mention this mission slug; treating it as stale")
    if intent_slug and intent_slug != slug:
        warnings.append(f"intent memory points to {intent_slug}, not {slug}")
    if cohesion_slug and cohesion_slug != slug:
        warnings.append(f"system cohesion state points to {cohesion_slug}, not {slug}")
    return preferred, warnings


def resume(args: argparse.Namespace) -> None:
    state = read_state(args.slug)
    packet = state.get("resume_packet", default_resume_packet(args.slug))
    preferred, warnings = resume_diagnostics(args.slug)
    print(f"Mission: {state['name']}")
    print(f"Slug: {state['slug']}")
    print(f"Status: {state['status']}")
    print(f"Preferred resume source: {preferred}")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    print("State sources:")
    for source in packet.get("state_sources", []):
        print(f"- {source}")
    print(f"Fresh session packet: {packet.get('fresh_session_packet') or '[none]'}")
    print(f"Next command: {packet.get('next_command') or '[none]'}")
    print(f"Resume command: {packet.get('resume_command') or f'/mission resume {args.slug}'}")


def context_bundle(slug: str) -> dict:
    state = read_state(slug)
    packet = state.get("resume_packet", default_resume_packet(slug))
    intent = load_json(INTENT_MEMORY_PATH)
    cohesion = load_json(COHESION_STATE_PATH)
    intent_matches = source_slug(intent, "intent") == slug
    cohesion_matches = source_slug(cohesion, "cohesion") == slug

    route = intent.get("route", {}) if intent_matches else {}
    active_intent = intent.get("active_intent", {}) if intent_matches else {}
    chosen_route = cohesion.get("chosen_route", {}) if cohesion_matches else {}

    support_gates = clean_list(
        state.get("support_gates", [])
        + route.get("support_gates", [])
        + (cohesion.get("support_gates", []) if cohesion_matches else [])
    )
    expert_stack = clean_list(
        state.get("expert_stack", [])
        + route.get("expert_stack", [])
        + (cohesion.get("expert_stack", []) if cohesion_matches else [])
    )
    boundaries = clean_list(
        state.get("package_boundaries", [])
        + active_intent.get("constraints", [])
    )

    approved_sources = []
    for item in state.get("approved_package_load_set", []):
        entry = dict(item)
        entry["exists"] = package_path_exists(entry.get("path", ""))
        approved_sources.append(entry)

    activation_evidence = [
        {
            "id": item.get("id", ""),
            "owner": item.get("owner", ""),
            "workflow": item.get("workflow", ""),
            "status": item.get("status", ""),
            "evidence_path": item.get("evidence_path", ""),
            "evidence_exists": package_path_exists(item.get("evidence_path", "")),
            "expected_artifact": item.get("expected_artifact", ""),
            "validation_assertion": item.get("validation_assertion", ""),
        }
        for item in state.get("activation_queue", [])
    ]

    proof_artifacts = []
    for path in state.get("execution_receipt", {}).get("proof_artifacts", []):
        proof_artifacts.append({"path": path, "exists": package_path_exists(path)})

    missing_required = [
        item["path"]
        for item in approved_sources
        if item.get("required", True) and not item.get("exists")
    ]
    missing_proof = [
        item["path"]
        for item in proof_artifacts
        if not item.get("exists")
    ]

    return {
        "mission": {
            "slug": state["slug"],
            "name": state["name"],
            "status": state["status"],
            "mode": state["mode"],
            "goal": state["goal"],
            "state_path": rel(state_path(slug)),
            "preferred_resume_source": resume_diagnostics(slug)[0],
        },
        "resume_packet": packet,
        "approved_package_load_set": approved_sources,
        "activation_evidence": activation_evidence,
        "proof_artifacts": proof_artifacts,
        "support_gates": support_gates,
        "expert_stack": expert_stack,
        "handoff_decisions": {
            "librarian": state.get("librarian", {}),
            "handoffs": state.get("handoffs", []),
            "execution_receipt": state.get("execution_receipt", {}),
        },
        "next_command_constraints": {
            "next_command": packet.get("next_command", ""),
            "resume_command": packet.get("resume_command") or f"/mission resume {slug}",
            "chosen_route": route.get("chosen_route") or chosen_route.get("route", ""),
            "must_show_mission_handoff_receipt": True,
            "must_load_before_drafting_or_routing": True,
        },
        "context_requirements": state.get("context_requirements", []),
        "boundaries": boundaries,
        "missing_required_sources": missing_required,
        "missing_proof_artifacts": missing_proof,
    }


def format_context(bundle: dict) -> str:
    mission = bundle["mission"]
    packet = bundle["resume_packet"]

    def lines_for_sources(items: list[dict]) -> str:
        if not items:
            return "- [none]"
        return "\n".join(
            "- [{status}] `{path}` — {role}{reason}".format(
                status="OK" if item.get("exists") else "MISSING",
                path=item.get("path", ""),
                role=item.get("role", "source"),
                reason=f": {item.get('reason')}" if item.get("reason") else "",
            )
            for item in items
        )

    def lines_for_evidence(items: list[dict]) -> str:
        if not items:
            return "- [none]"
        return "\n".join(
            "- {id} | {status} | {owner} via {workflow} | evidence `{path}` ({exists})".format(
                id=item.get("id", ""),
                status=item.get("status", ""),
                owner=item.get("owner", ""),
                workflow=item.get("workflow", ""),
                path=item.get("evidence_path", ""),
                exists="OK" if item.get("evidence_exists") else "MISSING",
            )
            for item in items
        )

    def bullet_list(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- [none]"

    return f"""# Mission Package Context: {mission['name']}

## Mission State
- Slug: `{mission['slug']}`
- Status: {mission['status']}
- Mode: {mission['mode']}
- Goal: {mission['goal']}
- State path: `{mission['state_path']}`
- Preferred resume source: {mission['preferred_resume_source']}

## Approved Package Load Set
{lines_for_sources(bundle['approved_package_load_set'])}

## Activation Evidence
{lines_for_evidence(bundle['activation_evidence'])}

## Proof Artifacts
{lines_for_sources(bundle['proof_artifacts'])}

## Support Gates
{bullet_list(bundle['support_gates'])}

## Expert Stack
{bullet_list(bundle['expert_stack'])}

## Context Requirements
{bullet_list(bundle['context_requirements'])}

## Boundaries
{bullet_list(bundle['boundaries'])}

## Next Command Constraints
- Fresh session packet: `{packet.get('fresh_session_packet') or '[none]'}`
- Next command: `{bundle['next_command_constraints']['next_command'] or '[none]'}`
- Resume command: `{bundle['next_command_constraints']['resume_command']}`
- Must show Mission Handoff Receipt: {bundle['next_command_constraints']['must_show_mission_handoff_receipt']}
- Must load before drafting or routing: {bundle['next_command_constraints']['must_load_before_drafting_or_routing']}

## Mission Handoff Receipt Requirement
Every resumed mission-backed run must show:
- approved package files loaded,
- activation lanes used,
- proof artifacts consulted,
- support gates run or skipped,
- package boundaries preserved,
- missing or skipped sources with reasons.
"""


def context(args: argparse.Namespace) -> None:
    bundle = context_bundle(args.slug)
    if args.json:
        print(json.dumps(bundle, indent=2, sort_keys=True))
    else:
        print(format_context(bundle))


def validate_state(state: dict, md: str) -> list[tuple[str, bool]]:
    librarian = state.get("librarian", {})
    librarian_ok = not librarian.get("required") or librarian.get("status") == "complete"
    contract = state.get("artifact_contract", {"type": "none", "artifacts": []})
    contract_enabled = contract.get("type") != "none"
    artifact_paths = [BASE / item["path"] for item in contract.get("artifacts", [])]
    artifact_section_ok = not contract_enabled or "## Artifact Contract" in md
    artifact_files_ok = not contract_enabled or all(path.exists() for path in artifact_paths)
    enforced = state.get("status") in ENFORCED_STATUSES
    assertions = state.get("validation_assertions", [])
    activation_queue = state.get("activation_queue", [])
    unfinished_without_blocker = [
        item["id"]
        for item in activation_queue
        if item.get("status") not in TERMINAL_ACTIVATION_STATUSES and not item.get("blocker")
    ]
    completed_without_evidence = [
        item["id"]
        for item in activation_queue
        if item.get("status") == "complete" and not evidence_path_exists(item.get("evidence_path", ""))
    ]
    expert_without_evidence = [
        item["id"]
        for item in activation_queue
        if (
            item.get("kind") == "expert"
            or "expert" in item.get("owner", "").lower()
            or "agent" in item.get("owner", "").lower()
            or "agent" in item.get("workflow", "").lower()
        )
        and item.get("status") == "complete"
        and not evidence_path_exists(item.get("evidence_path", ""))
    ]
    packet = state.get("resume_packet", default_resume_packet(state["slug"]))
    fresh_session_required = packet.get("required") or is_deployment_style(state)
    fresh_session_packet = packet.get("fresh_session_packet", "")
    fresh_session_ok = not fresh_session_required or evidence_path_exists(fresh_session_packet)
    resume_packet_ok = bool(packet.get("resume_command")) and bool(packet.get("next_command"))
    package_items = state.get("approved_package_load_set", [])
    missing_package_paths = [
        item.get("path", "")
        for item in package_items
        if item.get("required", True) and not package_path_exists(item.get("path", ""))
    ]
    context_requirements_ok = (
        not package_items
        or any("mission_control.py context" in item for item in state.get("context_requirements", []))
    )

    checks = [
        ("state file exists", state_path(state["slug"]).exists()),
        ("mission brief exists", markdown_path(state["slug"]).exists()),
        ("goal is present", bool(state.get("goal"))),
        ("mode is present", bool(state.get("mode"))),
        ("required librarian checkpoint complete", librarian_ok),
        ("validation contract section exists", "## Validation Contract" in md),
        ("artifact contract section exists when enabled", artifact_section_ok),
        ("artifact contract files exist when enabled", artifact_files_ok),
        ("handoff section exists", "## Handoffs" in md),
        ("validation assertions recorded for active mission", (not enforced) or bool(assertions)),
        ("activation queue recorded for active mission", (not enforced) or bool(activation_queue)),
        (
            "activation items are complete, skipped, or blocked",
            (not enforced) or not unfinished_without_blocker,
        ),
        (
            "completed activation items have evidence paths",
            (not enforced) or not completed_without_evidence,
        ),
        (
            "expert or agent lanes have evidence",
            (not enforced) or not expert_without_evidence,
        ),
        ("resume packet has resume and next command", (not enforced) or resume_packet_ok),
        ("fresh-session packet exists when required", (not enforced) or fresh_session_ok),
        (
            "approved package load set paths exist",
            (not enforced) or not missing_package_paths,
        ),
        (
            "mission package context requirements recorded",
            (not enforced) or context_requirements_ok,
        ),
    ]
    for label, ids in (
        ("unfinished activation items", unfinished_without_blocker),
        ("completed items missing evidence", completed_without_evidence),
        ("expert lanes missing evidence", expert_without_evidence),
        ("approved package paths missing", missing_package_paths),
    ):
        if ids:
            checks.append((f"{label}: {', '.join(ids)}", False))
    return checks


def validate(args: argparse.Namespace) -> None:
    state = read_state(args.slug)
    md = markdown_path(args.slug).read_text(encoding="utf-8") if markdown_path(args.slug).exists() else ""
    checks = validate_state(state, md)
    failed = [label for label, ok in checks if not ok]
    for label, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'} {label}")
    if failed:
        raise SystemExit(1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local Mission Control state helper")
    sub = parser.add_subparsers(dest="command", required=True)

    create_cmd = sub.add_parser("create", help="Create a mission state folder")
    create_cmd.add_argument("--name", required=True)
    create_cmd.add_argument("--goal", required=True)
    create_cmd.add_argument("--mode", default="general", choices=["general", "client", "personal", "code", "research", "system"])
    create_cmd.add_argument("--slug")
    create_cmd.add_argument("--force", action="store_true")
    create_cmd.add_argument("--librarian-required", action="store_true")
    create_cmd.add_argument("--fresh-session-packet", default="")
    create_cmd.add_argument("--fresh-session-required", action="store_true")
    create_cmd.add_argument("--next-command", default="")
    create_cmd.add_argument(
        "--artifact-contract",
        default="none",
        choices=["none", "engineering"],
        help="Create a durable mission artifact contract and starter files",
    )
    create_cmd.set_defaults(func=create)

    list_cmd = sub.add_parser("list", help="List missions")
    list_cmd.set_defaults(func=list_missions)

    status_cmd = sub.add_parser("status", help="Show mission status")
    status_cmd.add_argument("slug")
    status_cmd.set_defaults(func=status)

    resume_cmd = sub.add_parser("resume", help="Show a mission resume packet and stale-state warnings")
    resume_cmd.add_argument("slug")
    resume_cmd.set_defaults(func=resume)

    context_cmd = sub.add_parser("context", help="Show the approved mission package context bundle")
    context_cmd.add_argument("slug")
    context_cmd.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    context_cmd.set_defaults(func=context)

    set_status_cmd = sub.add_parser("set-status", help="Update mission status")
    set_status_cmd.add_argument("slug")
    set_status_cmd.add_argument("status", choices=["planned", "active", "blocked", "validating", "complete"])
    set_status_cmd.set_defaults(func=set_status)

    handoff_cmd = sub.add_parser("add-handoff", help="Append a compact handoff")
    handoff_cmd.add_argument("slug")
    handoff_cmd.add_argument("--role", required=True)
    handoff_cmd.add_argument("--summary", required=True)
    handoff_cmd.add_argument("--commands", default="")
    handoff_cmd.add_argument("--issues", default="")
    handoff_cmd.add_argument("--next", default="")
    handoff_cmd.set_defaults(func=add_handoff)

    librarian_cmd = sub.add_parser("mark-librarian", help="Record Knowledge Librarian checkpoint status")
    librarian_cmd.add_argument("slug")
    librarian_cmd.add_argument("--status", required=True, choices=["pending", "complete", "not_applicable"])
    librarian_cmd.add_argument("--notes", default="")
    librarian_cmd.add_argument("--required", action="store_true")
    librarian_cmd.set_defaults(func=mark_librarian)

    assertion_cmd = sub.add_parser("add-assertion", help="Record or update a validation assertion")
    assertion_cmd.add_argument("slug")
    assertion_cmd.add_argument("--id", required=True)
    assertion_cmd.add_argument("--statement", required=True)
    assertion_cmd.add_argument("--covered-by", default="")
    assertion_cmd.add_argument("--validator", default="")
    assertion_cmd.add_argument("--pass-signal", default="")
    assertion_cmd.set_defaults(func=add_assertion)

    activation_cmd = sub.add_parser("add-activation", help="Record or update an activation item")
    activation_cmd.add_argument("slug")
    activation_cmd.add_argument("--id", required=True)
    activation_cmd.add_argument("--owner", required=True)
    activation_cmd.add_argument("--workflow", required=True)
    activation_cmd.add_argument("--expected-artifact", required=True)
    activation_cmd.add_argument("--status", default="planned", choices=ACTIVATION_STATUSES)
    activation_cmd.add_argument("--evidence-path", default="")
    activation_cmd.add_argument("--validation-assertion", default="")
    activation_cmd.add_argument("--blocker", default="")
    activation_cmd.add_argument("--next-action", default="")
    activation_cmd.add_argument("--kind", default="workstream")
    activation_cmd.set_defaults(func=add_activation)

    activation_update_cmd = sub.add_parser("set-activation", help="Update an existing activation item")
    activation_update_cmd.add_argument("slug")
    activation_update_cmd.add_argument("--id", required=True)
    activation_update_cmd.add_argument("--owner")
    activation_update_cmd.add_argument("--workflow")
    activation_update_cmd.add_argument("--expected-artifact")
    activation_update_cmd.add_argument("--status", choices=ACTIVATION_STATUSES)
    activation_update_cmd.add_argument("--evidence-path")
    activation_update_cmd.add_argument("--validation-assertion")
    activation_update_cmd.add_argument("--blocker")
    activation_update_cmd.add_argument("--next-action")
    activation_update_cmd.add_argument("--kind")
    activation_update_cmd.set_defaults(func=set_activation)

    resume_packet_cmd = sub.add_parser("set-resume-packet", help="Record the fresh-session resume packet")
    resume_packet_cmd.add_argument("slug")
    resume_packet_cmd.add_argument("--fresh-session-packet")
    resume_packet_cmd.add_argument("--resume-command")
    resume_packet_cmd.add_argument("--next-command")
    resume_packet_cmd.add_argument("--notes")
    resume_packet_cmd.add_argument("--state-source", action="append")
    resume_packet_cmd.add_argument("--required", action="store_true")
    resume_packet_cmd.set_defaults(func=set_resume_packet)

    validate_cmd = sub.add_parser("validate", help="Validate mission harness")
    validate_cmd.add_argument("slug")
    validate_cmd.set_defaults(func=validate)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
