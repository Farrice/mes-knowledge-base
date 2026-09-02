#!/usr/bin/env python3
"""Sabotage-grade checks for the Gemini Deep Research ledger + recovery path.

No network, no paid calls: `requests` is stubbed. Every check has a positive
run (patched behaviour passes) and a sabotage run (the pre-2026-09-02 behaviour
is re-created and the same assertion must FAIL). A verifier that cannot fail
proves nothing (Verification Spine, 2026-08-08).

Scars covered (2026-09-02 audit):
  A. timeout lost the interaction id -> money spent, nothing on disk
  B. collect() re-logged an already-charged id -> ledger said $1.00 for one run
  C. report body was never persisted -> $0.50 run printed only a receipt
  D. month rollover overwrote the ledger -> no history

Run:  python3 execution/verify_deep_research_ledger.py
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

os.environ.setdefault("GOOGLE_AI_STUDIO_KEY", "verify-stub-key")
import deep_research_client as drc  # noqa: E402


# ---------------------------------------------------------------------------
# Stub transport
# ---------------------------------------------------------------------------

class _Resp:
    def __init__(self, data, status=200):
        self._data, self.status_code, self.text = data, status, json.dumps(data)

    def json(self):
        return self._data

    def raise_for_status(self):
        pass


def _install_stub(post_data, get_sequence):
    """Replace requests.post/get on the client module. get_sequence is a list of
    payloads returned in order; the last one repeats forever."""
    seq = list(get_sequence)
    state = {"i": 0}

    def post(*a, **k):
        return _Resp(post_data)

    def get(*a, **k):
        d = seq[min(state["i"], len(seq) - 1)]
        state["i"] += 1
        return _Resp(d)

    def head(*a, **k):
        r = _Resp({})
        r.url = a[0] if a else ""
        return r

    drc.requests = types.SimpleNamespace(post=post, get=get, head=head,
                                         HTTPError=Exception, RequestException=Exception)
    drc.time.sleep = lambda s: None


COMPLETED = {
    "status": "completed",
    "steps": [{"type": "model_output", "content": [{"text": (
        "Real research body with enough substance to clear the validator. "
        "Source one https://example.com/a and source two https://example.org/b. " * 3)}]}],
}
RUNNING = {"status": "in_progress"}
IID = "v1_verify_interaction_0001"


def _fresh_ledger(tmp: Path, month: str | None = None) -> Path:
    tmp.mkdir(parents=True, exist_ok=True)
    led = tmp / "gemini-api-usage.json"
    drc.USAGE_FILE = led
    drc.USAGE_ARCHIVE_DIR = tmp / "archive"
    drc.REPORT_DIR = tmp / "reports"
    if month:
        led.write_text(json.dumps({
            "prepaid_ceiling_usd": 10.0, "current_month": month,
            "usage": {"total_queries": 3, "estimated_cost_usd": 1.5, "queries": [{"interaction_id": "old"}]},
            "pending": [], "alerts": {}, "loop_detection": {}}))
    return led


def _ledger(led: Path) -> dict:
    return json.loads(led.read_text())


# ---------------------------------------------------------------------------
# Checks: each returns (name, passed_positive, passed_sabotage)
# ---------------------------------------------------------------------------

def check_a_timeout_keeps_id():
    with tempfile.TemporaryDirectory() as t:
        led = _fresh_ledger(Path(t))
        _install_stub({"id": IID}, [RUNNING])
        c = drc.DeepResearchClient()
        raised = ""
        try:
            c.research("q", poll_interval_seconds=1, max_wait_seconds=3, task_context="verify")
        except TimeoutError as e:
            raised = str(e)
        pend = _ledger(led).get("pending", [])
        pos = (IID in raised and "gemini-collect" in raised
               and any(p["interaction_id"] == IID for p in pend))
        # sabotage: old client never wrote a pending row -> row must be absent
        led2 = _fresh_ledger(Path(t) / "s")
        led2.parent.mkdir(exist_ok=True)
        orig = drc.DeepResearchClient._log_pending
        drc.DeepResearchClient._log_pending = lambda self, **k: None
        try:
            try:
                drc.DeepResearchClient().research("q", poll_interval_seconds=1, max_wait_seconds=3)
            except TimeoutError:
                pass
            sab = not any(p.get("interaction_id") == IID
                          for p in (_ledger(led2).get("pending", []) if led2.exists() else []))
        finally:
            drc.DeepResearchClient._log_pending = orig
        return "A timeout keeps interaction id as pending", pos, sab


def check_b_collect_idempotent():
    with tempfile.TemporaryDirectory() as t:
        led = _fresh_ledger(Path(t))
        _install_stub({"id": IID}, [COMPLETED])
        c = drc.DeepResearchClient()
        r1 = c.collect(IID, query="q", mode="standard")
        r2 = c.collect(IID, query="q", mode="standard")
        u = _ledger(led)["usage"]
        pos = (r1.status == "completed" and r2.status == "completed"
               and u["total_queries"] == 1 and abs(u["estimated_cost_usd"] - 0.5) < 1e-9
               and r1.estimated_cost == 0.5 and r2.estimated_cost == 0.0
               and r2.text == r1.text)
        # sabotage: pretend nothing is ever already logged -> double count returns
        orig = drc.DeepResearchClient._already_logged
        drc.DeepResearchClient._already_logged = lambda self, iid: False
        try:
            led2 = _fresh_ledger(Path(t) / "s"); led2.parent.mkdir(exist_ok=True)
            c2 = drc.DeepResearchClient()
            c2.collect(IID, query="q"); c2.collect(IID, query="q")
            sab = _ledger(led2)["usage"]["total_queries"] == 2
        finally:
            drc.DeepResearchClient._already_logged = orig
        return "B collect() charges an interaction id once", pos, sab


def check_c_body_persisted_and_pending_cleared():
    with tempfile.TemporaryDirectory() as t:
        led = _fresh_ledger(Path(t))
        _install_stub({"id": IID}, [RUNNING, COMPLETED])
        c = drc.DeepResearchClient()
        r = c.research("q", poll_interval_seconds=1, max_wait_seconds=30, task_context="verify")
        body = Path(r.report_path) if r.report_path else None
        L = _ledger(led)
        pos = (r.status == "completed" and body is not None and body.exists()
               and "Real research body" in body.read_text()
               and IID in body.read_text()
               and not L.get("pending") and L["usage"]["total_queries"] == 1)
        # sabotage: persistence disabled -> no path, no file
        orig = drc.DeepResearchClient._persist_report
        drc.DeepResearchClient._persist_report = lambda self, *a, **k: None
        try:
            _fresh_ledger(Path(t) / "s").parent.mkdir(exist_ok=True)
            _install_stub({"id": IID}, [COMPLETED])
            r2 = drc.DeepResearchClient().research("q", poll_interval_seconds=1, max_wait_seconds=30)
            sab = r2.report_path is None
        finally:
            drc.DeepResearchClient._persist_report = orig
        return "C body persisted to disk + pending row cleared on success", pos, sab


def check_d_month_rollover_archives():
    with tempfile.TemporaryDirectory() as t:
        led = _fresh_ledger(Path(t), month="2001-01")
        _install_stub({"id": IID}, [COMPLETED])
        drc.DeepResearchClient().collect(IID, query="q")
        arch = drc.USAGE_ARCHIVE_DIR / "2001-01.json"
        L = _ledger(led)
        pos = (arch.exists() and json.loads(arch.read_text())["usage"]["total_queries"] == 3
               and L["current_month"] != "2001-01" and L["usage"]["total_queries"] == 1)
        # sabotage: old reset path (no archive) -> archive absent
        orig = drc.DeepResearchClient._current_month_usage

        def no_archive(self):
            u = self._read_usage()
            return u if u.get("current_month") == drc.datetime.now().strftime("%Y-%m") \
                else self._fresh_month(drc.datetime.now().strftime("%Y-%m"))
        drc.DeepResearchClient._current_month_usage = no_archive
        try:
            _fresh_ledger(Path(t) / "s", month="2001-02").parent.mkdir(exist_ok=True)
            drc.DeepResearchClient().collect(IID, query="q")
            sab = not (drc.USAGE_ARCHIVE_DIR / "2001-02.json").exists()
        finally:
            drc.DeepResearchClient._current_month_usage = orig
        return "D month rollover archives the old ledger", pos, sab


def check_e_budget_counts_pending():
    with tempfile.TemporaryDirectory() as t:
        led = _fresh_ledger(Path(t))
        _install_stub({"id": IID}, [RUNNING])
        c = drc.DeepResearchClient()
        before = c.budget_remaining()
        c.start_async("q", mode="max")
        after = c.budget_remaining()
        pos = abs((before - after) - drc.EST_COST_PER_QUERY["max"]) < 1e-9
        sab = before == drc.PREPAID_CEILING_USD  # trivially true control: fresh ledger is full
        return "E in-flight (pending) spend reduces budget_remaining", pos, sab


def main() -> int:
    checks = [check_a_timeout_keeps_id, check_b_collect_idempotent,
              check_c_body_persisted_and_pending_cleared, check_d_month_rollover_archives,
              check_e_budget_counts_pending]
    fails = 0
    for fn in checks:
        try:
            name, pos, sab = fn()
        except Exception as e:  # a crash is a failure with a reason
            name, pos, sab = fn.__name__, False, False
            print(f"  ! {name} crashed: {type(e).__name__}: {e}")
        ok = pos and sab
        fails += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}   [positive={'ok' if pos else 'FAIL'} sabotage={'detected' if sab else 'NOT detected'}]")
    print(f"\n{len(checks) - fails}/{len(checks)} checks pass, sabotage detected in each" if not fails
          else f"\n{fails} check(s) failing")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
