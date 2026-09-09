#!/usr/bin/env python3
"""Deterministic regression checks for the workspace-local Monid budget guard."""

from __future__ import annotations

import contextlib
import io
import json
import tempfile
from pathlib import Path
from types import SimpleNamespace

import cost_gate
import monid_client


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def write_tracker(path: Path, spent: float, plan: float = 10.0) -> None:
    path.write_text(json.dumps({"plan_dollars": plan, "month_date": monid_client.month_date(), "month_spent_usd": spent, "month_calls": 1, "log": []}) + "\n")


def gate_args(estimate: float) -> SimpleNamespace:
    return SimpleNamespace(service="monid", est_cost=estimate, request="regression test", project="", quality=None, n=None, duration=None, audio=None)


def quiet_call(function, *args) -> int:
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        return int(function(*args))


def main() -> int:
    checks = 0
    with tempfile.TemporaryDirectory(prefix="monid-guard-") as temp_dir:
        temp = Path(temp_dir)
        tracker = temp / "monid-usage.json"
        monid_client.TRACKER_PATH = tracker
        cost_gate.TRACKER_PATH = temp / "cost-gate-state.json"
        cost_gate.LOG_PATH = temp / "cost-gate-log.jsonl"

        require(monid_client.MONID_DEFAULT_TASK_CAP_USD == 0.50, "default task quote drifted")
        require(monid_client.MONID_APPROVAL_THRESHOLD_USD == 0.50, "approval threshold drifted")
        require(monid_client.MONID_ABSOLUTE_TASK_CAP_USD == 3.00, "task hard cap drifted")
        require(monid_client.MONID_MONTHLY_BUDGET_USD == 10.00, "monthly hard stop drifted")
        checks += 4

        for estimate, decision, code in [(0.50, "approved", 0), (0.500001, "approval_required", 2), (3.00, "approval_required", 2), (3.01, "denied", 1)]:
            quote = monid_client.evaluate_quote(estimate)
            require(quote["decision"] == decision, f"${estimate} decision was {quote['decision']}")
            require(quote["exit_code"] == code, f"${estimate} exit code was {quote['exit_code']}")
            checks += 1

        require(monid_client.evaluate_quote(-0.01)["decision"] == "denied", "negative estimate was not denied")
        checks += 1

        quote_args = SimpleNamespace(task="dry quote", estimated_cost=None, json=True)
        require(quiet_call(monid_client.cmd_quote, quote_args) == 0, "default quote did not pass")
        require(not tracker.exists(), "read-only quote wrote a usage tracker")
        checks += 2

        write_tracker(tracker, spent=9.80, plan=25.00)
        normalized = monid_client.load_tracker()
        require(normalized["plan_dollars"] == 10.00, "legacy $25 tracker was not normalized")
        require(normalized["month_spent_usd"] == 9.80, "tracker migration lost recorded spend")
        require(monid_client.evaluate_quote(0.25)["decision"] == "denied", "monthly projection did not stop")
        checks += 3

        write_tracker(tracker, spent=1.00)
        log_args = SimpleNamespace(query="bounded run", cost=0.25, results=5)
        require(quiet_call(monid_client.cmd_log, log_args) == 0, "valid actual cost failed to log")
        recorded = json.loads(tracker.read_text())
        require(recorded["month_spent_usd"] == 1.25, "valid actual cost was not counted")
        checks += 2

        write_tracker(tracker, spent=9.50)
        overage_args = SimpleNamespace(query="unexpected overage", cost=0.75, results=5)
        require(quiet_call(monid_client.cmd_log, overage_args) == 1, "actual overage was not flagged")
        recorded = json.loads(tracker.read_text())
        require(recorded["month_spent_usd"] == 10.25, "actual overage was concealed instead of logged")
        require(recorded["log"][-1]["budget_violation"] is True, "overage receipt lacks violation flag")
        checks += 3

        write_tracker(tracker, spent=0.00)
        require(quiet_call(cost_gate._cmd_check_inner, gate_args(0.50)) == 0, "$0.50 cost gate did not pass")
        require(quiet_call(cost_gate._cmd_check_inner, gate_args(0.51)) == 2, "$0.51 did not require approval")
        require(quiet_call(cost_gate._cmd_check_inner, gate_args(3.01)) == 1, "$3.01 was not denied")
        checks += 3

        write_tracker(tracker, spent=9.90)
        require(quiet_call(cost_gate._cmd_check_inner, gate_args(0.50)) == 1, "cost gate ignored monthly stop")
        checks += 1

    print(f"MONID BUDGET GUARD: PASS ({checks} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
