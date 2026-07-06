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
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = str(ROOT / ".venv" / "bin" / "python3")
if not Path(PY).exists():
    PY = sys.executable
DB = ROOT / ".memory" / "sovereign.db"

sys.path.insert(0, str(ROOT / "execution"))

# Thought-bank capture backstop (2026-07-06): `thought_bank.py capture` is the
# deterministic front door, but it only fires if the model remembers to shell
# it mid-conversation — exactly the failure mode that left the thought-bank
# with one entry in two months. This is the physical backstop: scan the raw
# episodic exchanges (the same superpowers sqlite `episodic_ingest.py` reads)
# for user turns that opened with a thought-capture marker, and append any
# that never made it into today's inbox file. Dedup is by normalized
# first-60-chars against the SAME hash `thought_bank.py` writes per entry, so
# a fragment already captured mid-conversation is never double-appended.
THOUGHT_MARKERS = ("/dump", "thought:", "note to self", "capture this")
EPISODIC_DB = Path(os.environ.get(
    "ANTIGRAVITY_EPISODIC_DB",
    str(Path.home() / ".config" / "superpowers" / "conversation-index" / "db.sqlite"),
))
THOUGHT_BACKSTOP_HOURS = 24

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


def scan_thought_markers(hours: int = THOUGHT_BACKSTOP_HOURS) -> dict:
    """Deterministic backstop over the last `hours` of episodic exchanges.

    Read-only on the episodic sqlite (same contract as episodic_ingest.py:
    query_only pragma, no writes to that db). Any marker-prefixed user message
    not already present in today's thought-bank inbox (by dedupe hash) gets
    appended via `thought_bank.capture(..., source="backstop-episodic-scan")`.
    """
    if not EPISODIC_DB.exists():
        return {"scanned": 0, "captured": 0, "db_missing": True}

    cutoff = (datetime.now(timezone.utc) - timedelta(hours=hours)).isoformat()
    con = sqlite3.connect(f"file:{EPISODIC_DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        con.execute("PRAGMA query_only=ON")
        rows = con.execute(
            "SELECT user_message FROM exchanges "
            "WHERE is_sidechain = 0 AND timestamp >= ? ORDER BY timestamp ASC",
            (cutoff,),
        ).fetchall()
    finally:
        con.close()

    from thought_bank import capture as tb_capture, is_duplicate  # noqa: E402

    scanned = 0
    captured = 0
    for r in rows:
        msg = (r["user_message"] or "").strip()
        if not msg:
            continue
        head = msg.lower()
        if not any(head.startswith(marker) for marker in THOUGHT_MARKERS):
            continue
        scanned += 1
        if is_duplicate(msg):
            continue
        tb_capture(msg, source="backstop-episodic-scan", silent=True)
        captured += 1
    return {"scanned": scanned, "captured": captured, "db_missing": False}


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


def _log_thought_backstop(now: str) -> None:
    try:
        result = scan_thought_markers()
    except Exception as e:
        print(f"[{now}] thought-bank backstop scan FAILED (non-fatal): {e}")
        return
    if result.get("db_missing"):
        return  # episodic db not present this environment — silent skip
    if result["captured"] > 0:
        print(f"[{now}] thought-bank backstop: {result['captured']} marker fragment(s) "
              f"captured from last {THOUGHT_BACKSTOP_HOURS}h ({result['scanned']} matched, "
              f"rest already in inbox)")


def main() -> int:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    before, total = coverage()

    # Thought-bank backstop runs every invocation, independent of embed/distill
    # coverage state — it's the physical guarantee, not an optimization path.
    _log_thought_backstop(now)

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
