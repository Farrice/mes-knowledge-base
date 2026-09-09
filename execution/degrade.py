#!/usr/bin/env python3
"""degraded() — keep the non-blocking behaviour, stop dropping the signal.

WHY (2026-08-08 audit): ~30 handlers across execution/ degrade quietly. Their
NON-BLOCKING INTENT IS CORRECT — a board must never break a caller, a launchd
job must not exit nonzero (Compass Doctrine). What is wrong is that they drop
the signal instead of downgrading it, so a failure renders as health:

    pulse_dashboard.lane_state()  except -> ("", 0)   -> GREEN "0 commits stranded"
    pulse_dashboard corpus audit  except -> True      -> GREEN "v2 corpus pass"
    mission_board.build()         empty  -> falls through -> "everything live is moving"
    session_sweep.main()          crash  -> exit 0    -> orchestrator believes it worked

Two graceful handlers compose into a confident lie. This module is the fix and
it is deliberately one line per site, because a convention that costs more than
that will not be adopted across thirty of them.

    except OSError as e:
        return degraded("", "lane-reconciler receipt unreadable", e)

`degraded()` RETURNS THE VALUE YOU GIVE IT — it drops into an existing
`return ""` verbatim. It also appends a record naming the module, function,
line, and reason, so the hole is visible somewhere even when the surface cannot
show it. Authoring lanes use tracked `.agent/health/degradations.jsonl`;
canonical integration main uses ignored
`.agent/health/degradations-runtime.jsonl` so observation cannot block the next
merge.

It never raises and never blocks. A bug in this module must never be able to
disturb the code that called it.

Correct shapes already in this repo that inspired it: avatar_manifold_runner.py
writes `_GROUND STATUS: DEGRADED_` into its own artifact; health_metrics.py uses
-1 sentinels so unknown is distinguishable from zero; pulse_dashboard's
thread_cards() returns a VISIBLE '<div class="empty">handoff store unavailable'.
Six of its siblings return "" instead. This makes that shape the default.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKED_LEDGER = ROOT / ".agent" / "health" / "degradations.jsonl"
RUNTIME_LEDGER = ROOT / ".agent" / "health" / "degradations-runtime.jsonl"
# Kept mutable for callers/tests that intentionally redirect the recorder.
LEDGER = TRACKED_LEDGER
MAX_LINES = 2000


def _on_integration_main() -> bool:
    """True only for the canonical main checkout, never a worktree lane."""
    try:
        def probe(*args: str) -> subprocess.CompletedProcess[str]:
            return subprocess.run(
                ["git", "-C", str(ROOT), *args], capture_output=True,
                text=True, timeout=10,
            )

        branch = probe("rev-parse", "--abbrev-ref", "HEAD")
        git_dir = probe("rev-parse", "--path-format=absolute", "--git-dir")
        common_dir = probe("rev-parse", "--path-format=absolute", "--git-common-dir")
        return (
            branch.returncode == git_dir.returncode == common_dir.returncode == 0
            and branch.stdout.strip() == "main"
            and Path(git_dir.stdout.strip()).resolve()
            == Path(common_dir.stdout.strip()).resolve()
        )
    except Exception:
        return False


def _ledger_for(integration_main: bool | None = None) -> Path:
    """Select runtime-only telemetry on main while preserving lane learning."""
    if LEDGER != TRACKED_LEDGER:  # explicit caller/test override
        return LEDGER
    on_main = _on_integration_main() if integration_main is None else integration_main
    return RUNTIME_LEDGER if on_main else TRACKED_LEDGER


def _record(why: str, exc: BaseException | None, depth: int) -> None:
    try:
        f = sys._getframe(depth)
        entry = {
            "ts": datetime.now().isoformat(timespec="seconds"),
            "module": Path(f.f_code.co_filename).name,
            "function": f.f_code.co_name,
            "line": f.f_lineno,
            "why": str(why)[:200],
            "exc": f"{type(exc).__name__}: {exc}"[:200] if exc else None,
            "session": os.environ.get("CLAUDE_SESSION_ID", ""),
        }
        ledger = _ledger_for()
        ledger.parent.mkdir(parents=True, exist_ok=True)
        with open(ledger, "a") as fh:
            fh.write(json.dumps(entry) + "\n")
        # cheap trim so the ledger can never grow unbounded
        if ledger.stat().st_size > 1_500_000:
            lines = ledger.read_text().splitlines()[-MAX_LINES:]
            ledger.write_text("\n".join(lines) + "\n")
    except Exception:
        pass  # DELIBERATE-QUIET: the degradation recorder must never itself raise


def degraded(value, why: str, exc: BaseException | None = None):
    """Record that this return value is a hole, then return it unchanged."""
    _record(why, exc, depth=2)
    return value


def degraded_html(why: str, exc: BaseException | None = None) -> str:
    """A VISIBLE marker for a rendered surface. Use instead of returning ''.

    An absent section is invisible; an empty div that says why is not.
    """
    _record(why, exc, depth=2)
    safe = (str(why).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    return (f'<div class="empty" data-degraded="1">⚠ unavailable — {safe}</div>')


def recent(limit: int = 20) -> list[dict]:
    paths = [_ledger_for()]
    if LEDGER == TRACKED_LEDGER and _on_integration_main():
        paths = [TRACKED_LEDGER, RUNTIME_LEDGER]
    rows: list[dict] = []
    for path in paths:
        try:
            rows.extend(json.loads(line) for line in path.read_text().splitlines() if line.strip())
        except (OSError, ValueError):
            continue
    return rows[-limit:]


def self_test() -> int:
    ok, bad = 0, []

    def check(name, cond):
        nonlocal ok
        ok += 1 if cond else 0
        if not cond:
            bad.append(name)

    check("integration main selects runtime ledger", _ledger_for(True) == RUNTIME_LEDGER)
    check("authoring lane selects tracked ledger", _ledger_for(False) == TRACKED_LEDGER)
    orig = globals()["LEDGER"]
    with tempfile.TemporaryDirectory() as temp:
        globals()["LEDGER"] = Path(temp) / "degradations.jsonl"
        try:
            before = len(recent(9999))
            check("passes str through unchanged", degraded("", "selftest str") == "")
            check("passes tuple through unchanged", degraded(("", 0), "selftest tuple") == ("", 0))
            check("passes bool through unchanged", degraded(True, "selftest bool") is True)
            after = recent(9999)
            check("every call left a record", len(after) >= before + 3)
            check("record names this module + function",
                  after and after[-1]["module"] == "degrade.py" and after[-1]["function"] == "self_test")
            html = degraded_html("receipt unreadable")
            check("html marker is VISIBLE, not empty", "unavailable" in html and len(html) > 20)
            check("html marker is tagged for the detector", 'data-degraded="1"' in html)
            # must never raise even when the ledger is unwritable
            globals()["LEDGER"] = Path("/nonexistent-dir-xyz/degradations.jsonl")
            check("survives an unwritable ledger", degraded("v", "unwritable") == "v")
        finally:
            globals()["LEDGER"] = orig

    print(f"degrade self-test: {'OK' if not bad else 'FAILED'} ({ok} passed, {len(bad)} failed)")
    for b in bad:
        print(f"  FAIL: {b}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(self_test())
