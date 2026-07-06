#!/usr/bin/env python3
"""harvest_memory_daily.py — deterministic daily completion of the claude.ai export memory layer.

Installed as launchd job `com.antigravity.harvest-memory-daily` (daily 07:40 + at load).
Exists because the free-tier Gemini quotas (1,000 embeds/day, 500 generates/day per user)
make one-shot completion impossible — and per Farrice's standing rule, infra must never
depend on a human (or Claude) remembering a daily command.

Each run, in order:
  1. EMBED  — `memory_embed.py backfill` (idempotent; embeds up to today's quota, 429s are expected
              near the cap and harmless).
  2. DISTILL — only if new embeddings landed this run: one capped export-inclusive batch
              (--max-clusters 15, judge 6.5). Proposals go to flagged_review; NOTHING
              auto-promotes — `memory_review.py` stays the human gate.
  3. LOG    — one status line to stdout (launchd routes it to .memory/backups/harvest-memory-daily.log).

Once embedding coverage is 100% and the export window has been distilled, every run is a
sub-second no-op. Safe to leave installed forever.

Manual run:  python3 execution/harvest_memory_daily.py
Uninstall:   launchctl unload ~/Library/LaunchAgents/com.antigravity.harvest-memory-daily.plist
"""
from __future__ import annotations

import os
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = str(ROOT / ".venv" / "bin" / "python3")
if not Path(PY).exists():
    PY = sys.executable
DB = ROOT / ".memory" / "sovereign.db"

# Review-queue staleness escalation (2026-07-06 fix): the script already
# prints a "review queue" reminder line, but a reminder never louder than
# the last one lets a `flagged_review` item age indefinitely (observed: 9
# pending, oldest 36 days as of 2026-07-06). Nothing else in the system
# escalates on age, so this script — the one thing guaranteed to run daily
# — is where it has to happen.
STALE_REVIEW_DAYS = 14


def coverage() -> tuple[int, int]:
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    try:
        total = con.execute("SELECT COUNT(*) FROM memories").fetchone()[0]
        emb = con.execute("SELECT COUNT(*) FROM memories WHERE embedding IS NOT NULL").fetchone()[0]
    finally:
        con.close()
    return emb, total


def oldest_pending_review_age_days() -> tuple[int, float] | None:
    """(pending_count, age_days_of_oldest) for flagged_review, or None if none pending."""
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    try:
        row = con.execute(
            "SELECT COUNT(*), MIN(created_at) FROM flagged_review WHERE status = 'pending'"
        ).fetchone()
    finally:
        con.close()
    count, oldest = row if row else (0, None)
    if not count or not oldest:
        return None
    try:
        oldest_dt = datetime.fromisoformat(oldest)
    except Exception:
        return None
    age_days = (datetime.now(timezone.utc) - oldest_dt).total_seconds() / 86400.0
    return count, age_days


def run(cmd: list[str], env: dict | None = None, timeout: int = 3600) -> int:
    e = dict(os.environ)
    if env:
        e.update(env)
    try:
        return subprocess.run(cmd, cwd=ROOT, env=e, timeout=timeout,
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    except subprocess.TimeoutExpired:
        return -1


def _log_review_queue_staleness(now: str) -> None:
    review = oldest_pending_review_age_days()
    if review is None:
        return
    count, age_days = review
    if age_days > STALE_REVIEW_DAYS:
        print(
            f"[{now}] ⚠️ REVIEW QUEUE STALE: {count} pending, oldest {age_days:.0f} days "
            f"(>{STALE_REVIEW_DAYS}d threshold) — run memory_review.py"
        )


def main() -> int:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    before, total = coverage()

    if before >= total:
        # 1-second no-op path: everything embedded; nothing to do unless new rows appear.
        print(f"[{now}] harvest-memory-daily: coverage complete ({before}/{total}) — no-op")
        _log_review_queue_staleness(now)
        return 0

    # 1. EMBED — up to today's quota (429s near the cap are expected; script never fails on them)
    run([PY, str(ROOT / "execution" / "memory_embed.py"), "backfill"])
    after, total = coverage()
    gained = after - before

    # 2. DISTILL — only when today actually added embeddings (capped, human-gated downstream)
    distilled = "skipped"
    if gained > 0:
        rc = run([PY, str(ROOT / "execution" / "memory_distill.py"), "run",
                  "--days", "3", "--min-cluster", "2", "--max-clusters", "15",
                  "--judge-threshold", "6.5"],
                 env={"ANTIGRAVITY_DISTILL_INCLUDE_EXPORT": "1"})
        distilled = "ok" if rc == 0 else f"deferred(rc={rc})"  # generate quota may be spent — retries tomorrow

    pct = 100.0 * after / max(1, total)
    print(f"[{now}] harvest-memory-daily: embedded +{gained} → {after}/{total} ({pct:.1f}%) · distill: {distilled}")
    if after >= total:
        print(f"[{now}] 🎉 embedding coverage COMPLETE — review queue: python3 execution/memory_review.py list")
    _log_review_queue_staleness(now)
    return 0


if __name__ == "__main__":
    sys.exit(main())
