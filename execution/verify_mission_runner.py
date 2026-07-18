#!/usr/bin/env python3
"""verify_mission_runner.py — fixture gate for execution/mission_runner.py.

WHY: the mission runner is the thing that acts while nobody is watching
(overnight, unattended). Its three guards — tier gate, outward-action
refusal net, lock lifecycle — are exactly the guards that must never regress
silently, since a silent regression here means an autonomous claude -p spawn
does something T2/T3 or outward while Farrice is asleep. This fixture proves
all three plus the receipt trail in one deterministic run, isolated from the
real overnight queue via --queue-dir / --cos-dir overrides (never touches
.agent/mission-queue or .agent/cos in the live repo).

Fixture: a temp queue with (a) a plain T1 card, (b) a T2 card, (c) a T1 card
whose body contains the word "publish". Runs `mission_runner.py run
--dry-run` against it (dry-run skips the real `claude -p` spawn — the
tier/refusal/lock/receipt logic is what's under test, not the live CLI) and
asserts:
  1. the T1 card executed (dry-run stub transcript, moved to done/)
  2. the T2 card parked (untouched body, reason recorded)
  3. the "publish" T1 card parked (refusal-net reason recorded, NOT executed
     despite being tier T1 — proves the outward-action net outranks tier)
  4. the session lock was claimed and released cleanly (uses the real
     session_lock.py — no dir override exists for the lock itself, so this
     briefly touches the live repo lock file, claiming it only if it is
     currently unheld or stale, then always releasing it)
  5. the receipt lists all three cards by name

Run: python3 execution/verify_mission_runner.py
Exit 0 = 5/5 PASS; exit 1 = any check failed, printed.
"""
from __future__ import annotations

import shutil
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "execution" / "mission_runner.py"

T1_CARD = """MISSION CARD
Intent: rename a scratch file for the fixture test
Pattern: solo — trivial
Loads: none
Gates: none
Tier: T1 auto   Cost: $0
"""

T2_CARD = """MISSION CARD
Intent: post an update to an external channel
Pattern: solo
Loads: none
Gates: none
Tier: T2 waiting   Cost: $0
"""

T1_PUBLISH_CARD = """MISSION CARD
Intent: publish the finished draft to the live site
Pattern: solo
Loads: none
Gates: none
Tier: T1 auto   Cost: $0
"""


# Isolate the fixture from the LIVE session lock: without this, results flip
# 5/5↔0/5 with the tree's lock state (caught 2026-07-18 when the conductor's
# independent re-run failed 0/5 under a fresh-held lock — and the first run had
# stale-claimed the conductor's own lock as a side effect).
_ENV = dict(os.environ, SESSION_LOCK_PATH=str(ROOT / ".tmp" / "mission-runner-fixtures" / "session.lock.test"))


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, env=_ENV)


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="mission-runner-verify-"))
    queue_dir = tmp / "mission-queue"
    cos_dir = tmp / "cos"
    pending = queue_dir / "pending"
    parked = queue_dir / "parked"
    done = queue_dir / "done"

    checks: list[tuple[str, bool, str]] = []

    try:
        pending.mkdir(parents=True)
        (pending / "t1-plain.md").write_text(T1_CARD)
        (pending / "t2-outreach.md").write_text(T2_CARD)
        (pending / "t1-publish.md").write_text(T1_PUBLISH_CARD)

        result = run([
            sys.executable, str(RUNNER),
            "--queue-dir", str(queue_dir), "--cos-dir", str(cos_dir),
            "run", "--dry-run",
        ])
        run_output = result.stdout + result.stderr
        print("--- mission_runner.py run --dry-run output ---")
        print(run_output)
        print("--- end output ---\n")

        # 1. T1 card executed (dry-run stub, landed in done/)
        t1_card_done = (done / "t1-plain.md").exists()
        t1_transcript = done / "t1-plain-transcript.md"
        t1_stub_ok = t1_transcript.exists() and "DRY-RUN STUB" in t1_transcript.read_text()
        checks.append(("T1 card executed (stub transcript in done/)", t1_card_done and t1_stub_ok,
                        f"card_in_done={t1_card_done} transcript_ok={t1_stub_ok}"))

        # 2. T2 card parked with reason
        t2_parked = (parked / "t2-outreach.md").exists()
        t2_reason_path = parked / "t2-outreach.md.reason.txt"
        t2_reason_ok = t2_reason_path.exists() and "T2" in t2_reason_path.read_text()
        checks.append(("T2 card parked (untouched, reason recorded)", t2_parked and t2_reason_ok,
                        f"parked={t2_parked} reason_ok={t2_reason_ok}"))

        # 3. T1-but-publish card parked with refusal-net reason, NOT executed
        publish_parked = (parked / "t1-publish.md").exists()
        publish_not_done = not (done / "t1-publish.md").exists()
        publish_reason_path = parked / "t1-publish.md.reason.txt"
        publish_reason_ok = publish_reason_path.exists() and "publish" in publish_reason_path.read_text().lower()
        checks.append(("publish-matching T1 card parked, not executed", publish_parked and publish_not_done and publish_reason_ok,
                        f"parked={publish_parked} not_done={publish_not_done} reason_ok={publish_reason_ok}"))

        # 4. Lock claimed + released cleanly
        lock_claimed = "claimed:" in run_output
        lock_blocked = "ABORT: session lock held" in run_output
        lock_released = "released" in run_output
        lock_ok = lock_claimed and not lock_blocked and lock_released
        checks.append(("session lock claimed and released", lock_ok,
                        f"claimed={lock_claimed} blocked={lock_blocked} released={lock_released}"))

        # 5. Receipt written listing all three cards
        receipt_run = run([
            sys.executable, str(RUNNER),
            "--queue-dir", str(queue_dir), "--cos-dir", str(cos_dir),
            "receipt",
        ])
        print("--- mission_runner.py receipt output ---")
        print(receipt_run.stdout + receipt_run.stderr)
        print("--- end output ---\n")
        receipt_files = list(cos_dir.glob("overnight-receipt-*.md"))
        receipt_ok = False
        detail = "no receipt file found"
        if receipt_files:
            text = receipt_files[0].read_text()
            receipt_ok = all(name in text for name in ("t1-plain.md", "t2-outreach.md", "t1-publish.md"))
            detail = f"file={receipt_files[0].name} all_three_listed={receipt_ok}"
        checks.append(("receipt written, lists all three cards", receipt_ok, detail))

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    passed = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'} — {name} ({detail})")
    print(f"\n{passed}/{len(checks)} PASS")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
