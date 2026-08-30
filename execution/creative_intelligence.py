#!/usr/bin/env python3
"""Governed creative-strategy learning shared by Claude and Codex.

This module is deliberately small and stdlib-only. It records append-only
creative evidence, attaches later feedback/outcomes, proposes qualified lessons
to the existing ``flagged_review`` queue, and recalls only human-approved
semantic memories. It never edits a skill, agent, or doctrine file.

Typical use:
    python3 execution/creative_intelligence.py capture --artifact brief.md \
        --project acme --hypothesis "A trigger-event lead will lift hold rate"
    python3 execution/creative_intelligence.py outcome <event-id> \
        --metric hold_rate --value 0.31 --baseline 0.22 --window 7d \
        --test-design comparative --lesson "2am symptom moments outperform benefits"
    python3 execution/creative_intelligence.py feedback <event-id> \
        --verdict approved --lesson "Prioritize spend before ROAS in monthly reports"
    python3 execution/creative_intelligence.py synthesize --run
    python3 execution/creative_intelligence.py recall "trigger event" --project acme
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = ROOT / ".agent" / "creative-strategy-learning-events.jsonl"
DEFAULT_DB = ROOT / ".memory" / "sovereign.db"

PROOF_STATES = {
    "NO_EVENT",
    "HUMAN_TASTE",
    "DESCRIPTIVE_SIGNAL",
    "COMPARATIVE_RESULT",
    "CAUSAL_TEST",
}
VERDICTS = {"approved", "rejected", "revise"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def stable_id(prefix: str, *parts: Any) -> str:
    raw = "|".join(str(part or "").strip().lower() for part in parts)
    return f"{prefix}_{hashlib.sha256(raw.encode('utf-8')).hexdigest()[:16]}"


def _ledger_path(path: str | Path | None = None) -> Path:
    if path:
        return Path(path)
    env_path = os.environ.get("CREATIVE_INTELLIGENCE_LEDGER", "").strip()
    return Path(env_path) if env_path else DEFAULT_LEDGER


def read_jsonl(path: str | Path | None = None) -> list[dict[str, Any]]:
    target = _ledger_path(path)
    if not target.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in target.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(row, dict):
            rows.append(row)
    return rows


def append_record(record: dict[str, Any], path: str | Path | None = None) -> None:
    target = _ledger_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def fold_events(rows: Iterable[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Fold the append-only ledger into current event state without erasing history."""
    states: dict[str, dict[str, Any]] = {}
    for row in rows:
        event_id = row.get("event_id")
        if not event_id:
            continue
        kind = row.get("record_type")
        if kind == "event":
            state = dict(row)
            state["outcomes"] = []
            state["feedback"] = []
            state["contradictions"] = []
            states[event_id] = state
            continue
        state = states.get(event_id)
        if not state:
            continue
        if kind == "outcome":
            state["outcomes"].append(row)
            state["proof_state"] = row.get("proof_state", state.get("proof_state"))
            if row.get("candidate_lesson"):
                state["candidate_lesson"] = row["candidate_lesson"]
            if row.get("contradicts"):
                state["contradictions"].append(row["contradicts"])
        elif kind == "feedback":
            state["feedback"].append(row)
            state["proof_state"] = "HUMAN_TASTE"
            if row.get("candidate_lesson"):
                state["candidate_lesson"] = row["candidate_lesson"]
            state["human_verdict"] = row.get("verdict")
    return states


def capture_event(
    *,
    artifact_refs: list[str] | None = None,
    project_scope: str = "unscoped",
    expert: str = "",
    skill: str = "",
    workflow: str = "",
    hypothesis: str = "",
    mechanic: str = "",
    audience: str = "",
    format_name: str = "",
    funnel_stage: str = "",
    source_evidence: list[str] | None = None,
    expected_outcome: str = "",
    check_in_date: str = "",
    event_key: str = "",
    ledger_path: str | Path | None = None,
) -> dict[str, Any]:
    artifacts = [str(Path(ref)) for ref in (artifact_refs or []) if str(ref).strip()]
    sources = [str(ref).strip() for ref in (source_evidence or []) if str(ref).strip()]
    project = project_scope.strip() or "unscoped"
    fingerprint = event_key or stable_id(
        "fingerprint",
        project,
        expert,
        skill,
        workflow,
        hypothesis,
        ",".join(artifacts),
        date.today().isoformat(),
    )
    event_id = stable_id("creative", fingerprint)
    existing = fold_events(read_jsonl(ledger_path))
    if event_id in existing:
        return {"event_id": event_id, "duplicate": True, "record": existing[event_id]}

    record = {
        "record_type": "event",
        "event_id": event_id,
        "recorded_at": utc_now(),
        "project_scope": project,
        "artifact_refs": artifacts,
        "expert": expert,
        "skill": skill,
        "workflow": workflow,
        "hypothesis": hypothesis,
        "mechanic": mechanic,
        "audience": audience,
        "format": format_name,
        "funnel_stage": funnel_stage,
        "source_evidence": sources,
        "expected_outcome": expected_outcome,
        "check_in_date": check_in_date,
        "proof_state": "NO_EVENT",
        "candidate_lesson": "",
        "status": "pending",
    }
    append_record(record, ledger_path)
    return {"event_id": event_id, "duplicate": False, "record": record}


def capture_finalize_event(
    *,
    output_description: str,
    expert: str,
    skill: str,
    workflow: str,
    task_type: str,
    project: str,
    content_path: str,
    expected_outcome: str,
    check_in_date: str = "",
) -> dict[str, Any]:
    """Non-fatal-friendly adapter used by ``chain_runner.finalize``."""
    if task_type not in {"Creative", "Strategy"}:
        return {"skipped": True, "reason": f"task_type '{task_type}' is not creative strategy"}
    return capture_event(
        artifact_refs=[content_path] if content_path else [],
        project_scope=project or "unscoped",
        expert=expert,
        skill=skill,
        workflow=workflow,
        hypothesis=output_description,
        expected_outcome=expected_outcome,
        check_in_date=check_in_date,
    )


def attach_outcome(
    event_id: str,
    *,
    metric: str,
    value: str,
    baseline: str = "",
    window: str = "",
    test_design: str = "descriptive",
    candidate_lesson: str = "",
    contradicts: str = "",
    notes: str = "",
    ledger_path: str | Path | None = None,
) -> dict[str, Any]:
    states = fold_events(read_jsonl(ledger_path))
    if event_id not in states:
        raise ValueError(f"unknown event_id: {event_id}")
    if test_design == "controlled" and baseline:
        proof_state = "CAUSAL_TEST"
    elif test_design in {"comparative", "controlled"} and baseline:
        proof_state = "COMPARATIVE_RESULT"
    else:
        proof_state = "DESCRIPTIVE_SIGNAL"
    outcome_id = stable_id(
        "outcome", event_id, metric, value, baseline, window, test_design,
        candidate_lesson, contradicts,
    )
    for row in read_jsonl(ledger_path):
        if row.get("outcome_id") == outcome_id:
            return {**row, "duplicate": True}
    record = {
        "record_type": "outcome",
        "outcome_id": outcome_id,
        "event_id": event_id,
        "recorded_at": utc_now(),
        "metric": metric,
        "value": value,
        "baseline": baseline,
        "window": window,
        "test_design": test_design,
        "proof_state": proof_state,
        "candidate_lesson": candidate_lesson.strip(),
        "contradicts": contradicts.strip(),
        "notes": notes.strip(),
        "duplicate": False,
    }
    append_record(record, ledger_path)
    return record


def attach_feedback(
    event_id: str,
    *,
    verdict: str,
    candidate_lesson: str,
    note: str = "",
    ledger_path: str | Path | None = None,
) -> dict[str, Any]:
    if verdict not in VERDICTS:
        raise ValueError(f"verdict must be one of {sorted(VERDICTS)}")
    states = fold_events(read_jsonl(ledger_path))
    if event_id not in states:
        raise ValueError(f"unknown event_id: {event_id}")
    feedback_id = stable_id("feedback", event_id, verdict, candidate_lesson, note)
    for row in read_jsonl(ledger_path):
        if row.get("feedback_id") == feedback_id:
            return {**row, "duplicate": True}
    record = {
        "record_type": "feedback",
        "feedback_id": feedback_id,
        "event_id": event_id,
        "recorded_at": utc_now(),
        "verdict": verdict,
        "candidate_lesson": candidate_lesson.strip(),
        "note": note.strip(),
        "proof_state": "HUMAN_TASTE",
        "duplicate": False,
    }
    append_record(record, ledger_path)
    return record


def _latest_proof(state: dict[str, Any]) -> str:
    outcomes = state.get("outcomes") or []
    if outcomes:
        return outcomes[-1].get("proof_state", "DESCRIPTIVE_SIGNAL")
    if state.get("feedback"):
        return "HUMAN_TASTE"
    return state.get("proof_state", "NO_EVENT")


def build_candidates(states: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """Apply the governed promotion thresholds; return proposals, never approvals."""
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    contradicted_ids: set[str] = set()
    for state in states.values():
        contradicted_ids.update(state.get("contradictions") or [])
        if state.get("contradictions"):
            contradicted_ids.add(state["event_id"])
    for state in states.values():
        lesson = (state.get("candidate_lesson") or "").strip()
        if not lesson or state.get("human_verdict") == "rejected":
            continue
        groups[lesson.casefold()].append(state)

    candidates: list[dict[str, Any]] = []
    for group in groups.values():
        lesson = group[0]["candidate_lesson"].strip()
        usable = [row for row in group if row["event_id"] not in contradicted_ids]
        if not usable:
            continue
        by_project: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in usable:
            by_project[row.get("project_scope") or "unscoped"].append(row)

        eligible_projects: dict[str, dict[str, Any]] = {}
        for project, rows in by_project.items():
            causal = [row for row in rows if _latest_proof(row) == "CAUSAL_TEST"]
            comparative = [row for row in rows if _latest_proof(row) == "COMPARATIVE_RESULT"]
            taste = [
                row for row in rows
                if _latest_proof(row) == "HUMAN_TASTE" and row.get("human_verdict") == "approved"
            ]
            if causal:
                eligible_projects[project] = {"proof": "CAUSAL_TEST", "rows": causal, "score": 8.8}
            elif len(comparative) >= 2:
                eligible_projects[project] = {"proof": "COMPARATIVE_RESULT", "rows": comparative, "score": 8.2}
            elif taste:
                eligible_projects[project] = {"proof": "HUMAN_TASTE", "rows": taste, "score": 7.5}

        # Human taste is always project-scoped, even if three projects happen
        # to express the same preference. Shared promotion requires measured
        # comparative or causal evidence.
        real_projects = [
            project for project, evidence in eligible_projects.items()
            if project != "unscoped" and evidence["proof"] != "HUMAN_TASTE"
        ]
        if len(real_projects) >= 3:
            evidence_rows = [eligible_projects[p]["rows"][0] for p in sorted(real_projects)]
            candidates.append({
                "lesson": lesson,
                "scope": "shared",
                "project_scope": "shared",
                "proof_state": "CROSS_PROJECT",
                "judge_score": 9.2,
                "event_ids": [row["event_id"] for row in evidence_rows],
            })
            continue

        for project, evidence in sorted(eligible_projects.items()):
            candidates.append({
                "lesson": lesson,
                "scope": "project",
                "project_scope": project,
                "proof_state": evidence["proof"],
                "judge_score": evidence["score"],
                "event_ids": [row["event_id"] for row in evidence["rows"]],
            })
    return candidates


def _ensure_review_schema(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS flagged_review (
            id TEXT PRIMARY KEY,
            proposed_tier TEXT NOT NULL,
            proposed_category TEXT NOT NULL,
            proposed_content TEXT NOT NULL,
            proposed_metadata TEXT,
            source_memory_ids TEXT,
            judge_score REAL NOT NULL,
            judge_rationale TEXT,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TEXT NOT NULL,
            reviewed_at TEXT,
            promoted_memory_id TEXT
        )
    """)
    conn.commit()
    conn.close()


def queue_candidates(candidates: list[dict[str, Any]], db_path: str | Path | None = None) -> list[dict[str, Any]]:
    target = Path(db_path) if db_path else DEFAULT_DB
    _ensure_review_schema(target)
    conn = sqlite3.connect(str(target))
    results: list[dict[str, Any]] = []
    for candidate in candidates:
        fid = stable_id(
            "fr_creative",
            candidate["lesson"],
            candidate["project_scope"],
            ",".join(sorted(candidate["event_ids"])),
        )
        content = (
            f"[CREATIVE INTELLIGENCE | scope={candidate['project_scope']} | "
            f"proof={candidate['proof_state']}]\n{candidate['lesson']}"
        )
        metadata = {
            "source": "creative_intelligence",
            "scope": candidate["scope"],
            "project_scope": candidate["project_scope"],
            "proof_state": candidate["proof_state"],
            "event_ids": candidate["event_ids"],
            "auto_promotion_allowed": False,
        }
        inserted = conn.execute("SELECT 1 FROM flagged_review WHERE id = ?", (fid,)).fetchone() is None
        if inserted:
            conn.execute("""
                INSERT INTO flagged_review
                    (id, proposed_tier, proposed_category, proposed_content,
                     proposed_metadata, source_memory_ids, judge_score,
                     judge_rationale, status, created_at)
                VALUES (?, 'semantic', ?, ?, ?, ?, ?, ?, 'pending', ?)
            """, (
                fid,
                "preference" if candidate["proof_state"] == "HUMAN_TASTE" else "pattern",
                content,
                json.dumps(metadata, sort_keys=True),
                json.dumps(candidate["event_ids"]),
                candidate["judge_score"],
                "Deterministic evidence threshold met; human review required before recall.",
                utc_now(),
            ))
        results.append({"flagged_id": fid, "inserted": inserted, **candidate})
    conn.commit()
    conn.close()
    return results


def attach_outcome_by_deliverable(
    *,
    deliverable: str,
    revenue: float = 0.0,
    outcome: str = "",
    outcome_type: str = "feedback",
    expert: str = "",
    skill: str = "",
    ledger_path: str | Path | None = None,
) -> dict[str, Any]:
    """Attach a revenue-tracker resolution to the latest matching event.

    Revenue tracker does not know baselines or experiment design, so this path
    can only create a DESCRIPTIVE_SIGNAL. A later explicit ``outcome`` command
    may add comparative/controlled evidence.
    """
    want = deliverable.strip().casefold()
    matches = []
    for state in fold_events(read_jsonl(ledger_path)).values():
        have = (state.get("hypothesis") or "").strip().casefold()
        if not want or not have or not (want == have or want in have or have in want):
            continue
        if expert and state.get("expert") and state.get("expert") != expert:
            continue
        if skill and state.get("skill") and state.get("skill") != skill:
            continue
        matches.append(state)
    if not matches:
        return {"skipped": True, "reason": "no matching creative event"}
    latest = sorted(matches, key=lambda row: row.get("recorded_at", ""))[-1]
    metric = "revenue" if revenue else (outcome_type or "outcome")
    value = str(revenue) if revenue else (outcome or outcome_type or "observed")
    return attach_outcome(
        latest["event_id"],
        metric=metric,
        value=value,
        test_design="descriptive",
        notes=outcome,
        ledger_path=ledger_path,
    )


def synthesize(
    *,
    commit: bool = False,
    ledger_path: str | Path | None = None,
    db_path: str | Path | None = None,
) -> dict[str, Any]:
    states = fold_events(read_jsonl(ledger_path))
    candidates = build_candidates(states)
    return {
        "events": len(states),
        "candidates": queue_candidates(candidates, db_path) if commit else candidates,
        "committed": commit,
    }


def recall(query: str, *, project_scope: str = "", top: int = 8) -> list[dict[str, Any]]:
    sys.path.insert(0, str(ROOT / "execution"))
    from memory_store import search_memories  # noqa: WPS433 - local system dependency

    rows = search_memories(query, top_k=max(top * 4, 20), tier="semantic")
    found: list[dict[str, Any]] = []
    for _, row in rows:
        try:
            metadata = json.loads(row.get("metadata") or "{}")
        except json.JSONDecodeError:
            metadata = {}
        if metadata.get("source") != "creative_intelligence":
            continue
        scope = metadata.get("project_scope")
        if project_scope and scope not in {project_scope, "shared"}:
            continue
        found.append({
            "id": row.get("id"),
            "content": row.get("content"),
            "project_scope": scope,
            "proof_state": metadata.get("proof_state"),
            "event_ids": metadata.get("event_ids", []),
        })
        if len(found) >= top:
            break
    return found


def status(ledger_path: str | Path | None = None) -> dict[str, Any]:
    states = fold_events(read_jsonl(ledger_path))
    proof_counts: dict[str, int] = defaultdict(int)
    due = 0
    today = date.today().isoformat()
    for state in states.values():
        proof_counts[_latest_proof(state)] += 1
        if state.get("proof_state") == "NO_EVENT" and state.get("check_in_date") and state["check_in_date"] <= today:
            due += 1
    return {
        "events": len(states),
        "proof_states": dict(sorted(proof_counts.items())),
        "due_outcomes": due,
        "candidate_lessons": sum(1 for state in states.values() if state.get("candidate_lesson")),
    }


def _print(payload: Any) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ledger", default="", help="Override append-only ledger path")
    sub = parser.add_subparsers(dest="command", required=True)

    cap = sub.add_parser("capture", help="Register a creative artifact with NO_EVENT")
    cap.add_argument("--artifact", action="append", default=[])
    cap.add_argument("--project", default="unscoped")
    cap.add_argument("--expert", default="")
    cap.add_argument("--skill", default="")
    cap.add_argument("--workflow", default="")
    cap.add_argument("--hypothesis", required=True)
    cap.add_argument("--mechanic", default="")
    cap.add_argument("--audience", default="")
    cap.add_argument("--format", dest="format_name", default="")
    cap.add_argument("--funnel-stage", default="")
    cap.add_argument("--source", action="append", default=[])
    cap.add_argument("--expected-outcome", default="")
    cap.add_argument("--check-in-date", default="")
    cap.add_argument("--event-key", default="")

    out = sub.add_parser("outcome", help="Attach measured evidence to an event")
    out.add_argument("event_id")
    out.add_argument("--metric", required=True)
    out.add_argument("--value", required=True)
    out.add_argument("--baseline", default="")
    out.add_argument("--window", default="")
    out.add_argument("--test-design", choices=["descriptive", "comparative", "controlled"], default="descriptive")
    out.add_argument("--lesson", default="")
    out.add_argument("--contradicts", default="")
    out.add_argument("--notes", default="")

    feedback = sub.add_parser("feedback", help="Attach an explicit human verdict")
    feedback.add_argument("event_id")
    feedback.add_argument("--verdict", choices=sorted(VERDICTS), required=True)
    feedback.add_argument("--lesson", required=True)
    feedback.add_argument("--note", default="")

    syn = sub.add_parser("synthesize", help="Propose qualified lessons; --run queues them for review")
    syn.add_argument("--run", action="store_true")
    syn.add_argument("--db", default="")

    rec = sub.add_parser("recall", help="Recall approved creative lessons")
    rec.add_argument("query")
    rec.add_argument("--project", default="")
    rec.add_argument("--top", type=int, default=8)

    sub.add_parser("status", help="Show evidence and due-outcome counts")
    args = parser.parse_args()
    ledger = args.ledger or None

    try:
        if args.command == "capture":
            _print(capture_event(
                artifact_refs=args.artifact,
                project_scope=args.project,
                expert=args.expert,
                skill=args.skill,
                workflow=args.workflow,
                hypothesis=args.hypothesis,
                mechanic=args.mechanic,
                audience=args.audience,
                format_name=args.format_name,
                funnel_stage=args.funnel_stage,
                source_evidence=args.source,
                expected_outcome=args.expected_outcome,
                check_in_date=args.check_in_date,
                event_key=args.event_key,
                ledger_path=ledger,
            ))
        elif args.command == "outcome":
            _print(attach_outcome(
                args.event_id,
                metric=args.metric,
                value=args.value,
                baseline=args.baseline,
                window=args.window,
                test_design=args.test_design,
                candidate_lesson=args.lesson,
                contradicts=args.contradicts,
                notes=args.notes,
                ledger_path=ledger,
            ))
        elif args.command == "feedback":
            _print(attach_feedback(
                args.event_id,
                verdict=args.verdict,
                candidate_lesson=args.lesson,
                note=args.note,
                ledger_path=ledger,
            ))
        elif args.command == "synthesize":
            _print(synthesize(commit=args.run, ledger_path=ledger, db_path=args.db or None))
        elif args.command == "recall":
            _print(recall(args.query, project_scope=args.project, top=args.top))
        elif args.command == "status":
            _print(status(ledger))
    except (OSError, ValueError, sqlite3.Error) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
