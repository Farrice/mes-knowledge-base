import json
import sqlite3
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import creative_intelligence as ci  # noqa: E402
import memory_review  # noqa: E402


def capture(tmp_path, project="acme", hypothesis="Trigger-event lead"):
    return ci.capture_event(
        artifact_refs=["brief.md"],
        project_scope=project,
        expert="alex-copper",
        skill="trigger-event-creative-strategy",
        workflow="trigger-event-mine",
        hypothesis=hypothesis,
        event_key=f"{project}-{hypothesis}",
        ledger_path=tmp_path / "events.jsonl",
    )["event_id"]


def test_capture_is_idempotent_and_starts_no_event(tmp_path):
    ledger = tmp_path / "events.jsonl"
    first = ci.capture_event(hypothesis="A", event_key="same", ledger_path=ledger)
    second = ci.capture_event(hypothesis="A", event_key="same", ledger_path=ledger)
    assert first["duplicate"] is False
    assert second["duplicate"] is True
    assert ci.status(ledger)["proof_states"] == {"NO_EVENT": 1}


def test_outcome_proof_states_are_bounded(tmp_path):
    ledger = tmp_path / "events.jsonl"
    event_id = capture(tmp_path)
    descriptive = ci.attach_outcome(event_id, metric="spend", value="1200", ledger_path=ledger)
    comparative = ci.attach_outcome(
        event_id,
        metric="hold_rate",
        value="0.31",
        baseline="0.22",
        test_design="comparative",
        ledger_path=ledger,
    )
    causal = ci.attach_outcome(
        event_id,
        metric="hold_rate",
        value="0.31",
        baseline="0.22",
        test_design="controlled",
        ledger_path=ledger,
    )
    assert descriptive["proof_state"] == "DESCRIPTIVE_SIGNAL"
    assert comparative["proof_state"] == "COMPARATIVE_RESULT"
    assert causal["proof_state"] == "CAUSAL_TEST"


def test_one_comparative_result_does_not_become_doctrine(tmp_path):
    ledger = tmp_path / "events.jsonl"
    event_id = capture(tmp_path)
    ci.attach_outcome(
        event_id,
        metric="hold_rate",
        value="0.31",
        baseline="0.22",
        test_design="comparative",
        candidate_lesson="Specific trigger events beat generic benefits",
        ledger_path=ledger,
    )
    assert ci.synthesize(ledger_path=ledger)["candidates"] == []


def test_two_comparative_results_queue_project_lesson(tmp_path):
    ledger = tmp_path / "events.jsonl"
    lesson = "Specific trigger events beat generic benefits"
    for hypothesis in ("test-a", "test-b"):
        event_id = capture(tmp_path, hypothesis=hypothesis)
        ci.attach_outcome(
            event_id,
            metric="hold_rate",
            value="0.31",
            baseline="0.22",
            test_design="comparative",
            candidate_lesson=lesson,
            ledger_path=ledger,
        )
    result = ci.synthesize(commit=True, ledger_path=ledger, db_path=tmp_path / "memory.db")
    assert len(result["candidates"]) == 1
    assert result["candidates"][0]["project_scope"] == "acme"
    assert result["candidates"][0]["inserted"] is True

    conn = sqlite3.connect(tmp_path / "memory.db")
    row = conn.execute("SELECT status, proposed_metadata FROM flagged_review").fetchone()
    conn.close()
    assert row[0] == "pending"
    assert json.loads(row[1])["auto_promotion_allowed"] is False


def test_human_taste_stays_project_scoped(tmp_path):
    ledger = tmp_path / "events.jsonl"
    event_id = capture(tmp_path)
    ci.attach_feedback(
        event_id,
        verdict="approved",
        candidate_lesson="Prioritize spend before ROAS in monthly reports",
        ledger_path=ledger,
    )
    candidate = ci.synthesize(ledger_path=ledger)["candidates"][0]
    assert candidate["scope"] == "project"
    assert candidate["project_scope"] == "acme"
    assert candidate["proof_state"] == "HUMAN_TASTE"


def test_explicit_feedback_after_descriptive_outcome_remains_reviewable_taste(tmp_path):
    ledger = tmp_path / "events.jsonl"
    event_id = capture(tmp_path)
    ci.attach_outcome(
        event_id,
        metric="distribution",
        value="0 sends; 0 published",
        test_design="descriptive",
        ledger_path=ledger,
    )
    ci.attach_feedback(
        event_id,
        verdict="approved",
        candidate_lesson="Keep the listing launch system as the project flagship",
        ledger_path=ledger,
    )
    candidate = ci.synthesize(ledger_path=ledger)["candidates"][0]
    assert candidate["scope"] == "project"
    assert candidate["proof_state"] == "HUMAN_TASTE"


def test_three_taste_preferences_do_not_become_shared_doctrine(tmp_path):
    ledger = tmp_path / "events.jsonl"
    lesson = "Use the client's preferred reporting order"
    for project in ("acme", "beacon", "cobalt"):
        event_id = capture(tmp_path, project=project)
        ci.attach_feedback(
            event_id,
            verdict="approved",
            candidate_lesson=lesson,
            ledger_path=ledger,
        )
    candidates = ci.synthesize(ledger_path=ledger)["candidates"]
    assert len(candidates) == 3
    assert {candidate["scope"] for candidate in candidates} == {"project"}


def test_three_independent_projects_can_propose_shared_lesson(tmp_path):
    ledger = tmp_path / "events.jsonl"
    lesson = "Mine the intolerable moment before writing the benefit"
    for project in ("acme", "beacon", "cobalt"):
        event_id = capture(tmp_path, project=project)
        ci.attach_outcome(
            event_id,
            metric="hold_rate",
            value="0.31",
            baseline="0.22",
            test_design="controlled",
            candidate_lesson=lesson,
            ledger_path=ledger,
        )
    candidate = ci.synthesize(ledger_path=ledger)["candidates"][0]
    assert candidate["scope"] == "shared"
    assert candidate["project_scope"] == "shared"
    assert len(candidate["event_ids"]) == 3


def test_contradiction_blocks_promotion(tmp_path):
    ledger = tmp_path / "events.jsonl"
    lesson = "Benefit leads always lose"
    first = capture(tmp_path, hypothesis="first")
    second = capture(tmp_path, hypothesis="second")
    ci.attach_outcome(
        first,
        metric="hold_rate",
        value="0.31",
        baseline="0.22",
        test_design="comparative",
        candidate_lesson=lesson,
        ledger_path=ledger,
    )
    ci.attach_outcome(
        second,
        metric="hold_rate",
        value="0.18",
        baseline="0.22",
        test_design="comparative",
        candidate_lesson=lesson,
        contradicts=first,
        ledger_path=ledger,
    )
    assert ci.synthesize(ledger_path=ledger)["candidates"] == []


def test_revenue_resolution_auto_attaches_only_descriptive_signal(tmp_path):
    ledger = tmp_path / "events.jsonl"
    event_id = capture(tmp_path, hypothesis="Monthly creative report")
    result = ci.attach_outcome_by_deliverable(
        deliverable="Monthly creative report",
        revenue=0,
        outcome="Client approved the report",
        outcome_type="feedback",
        expert="alex-copper",
        skill="trigger-event-creative-strategy",
        ledger_path=ledger,
    )
    assert result["event_id"] == event_id
    assert result["proof_state"] == "DESCRIPTIVE_SIGNAL"
    assert ci.attach_outcome_by_deliverable(
        deliverable="Monthly creative report",
        outcome="Client approved the report",
        outcome_type="feedback",
        expert="alex-copper",
        skill="trigger-event-creative-strategy",
        ledger_path=ledger,
    )["duplicate"] is True


def test_creative_candidates_cannot_auto_promote(tmp_path, monkeypatch):
    ledger = tmp_path / "events.jsonl"
    db = tmp_path / "memory.db"
    lesson = "Mine the intolerable moment before writing the benefit"
    for project in ("acme", "beacon", "cobalt"):
        event_id = capture(tmp_path, project=project)
        ci.attach_outcome(
            event_id,
            metric="hold_rate",
            value="0.31",
            baseline="0.22",
            test_design="controlled",
            candidate_lesson=lesson,
            ledger_path=ledger,
        )
    ci.synthesize(commit=True, ledger_path=ledger, db_path=db)
    monkeypatch.setattr(memory_review, "DB_PATH", db)
    assert memory_review.auto_promote(threshold=9.0) == []
    conn = sqlite3.connect(db)
    status = conn.execute("SELECT status FROM flagged_review").fetchone()[0]
    conn.close()
    assert status == "pending"
