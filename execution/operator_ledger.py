#!/usr/bin/env python3
"""operator_ledger.py — the sink for the Operator Lesson line.

`directives/steering-loop.md` mandates that every shipped exchange closes with a
one-line `Operator Lesson: <text>`. Thousands of them have been written; none were
ever persisted. The teaching evaporated with the transcript. This is the sink:

  backfill — scan ALL episodic exchanges, extract every lesson line, dedupe, append.
  daily    — same scan limited to the last 48h (idempotent via the same dedupe).
  stats    — one-line count summary.

Read-only on the episodic sqlite (same contract as harvest_memory_daily.scan_thought_markers:
`mode=ro` URI + `PRAGMA query_only=ON`, never a write to that db). Writes go to
`knowledge/lessons/LEDGER.jsonl` (append-only) and are mirrored into `.memory/sovereign.db`
as tier='semantic', category='lesson' rows tagged `metadata.source = "operator-ledger"` —
that tag is the reversal handle: deleting every row carrying it undoes the mirror exactly.

Extraction is precision-first: a directive quoting the contract, a docs echo, a fenced code
block, or a placeholder template is NOT a lesson. Better to miss ten than bank one fake.

Manual run:  python3 execution/operator_ledger.py backfill
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import string
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / ".memory" / "sovereign.db"
LEDGER = ROOT / "knowledge" / "lessons" / "LEDGER.jsonl"
EPISODIC_DB = Path(os.environ.get(
    "ANTIGRAVITY_EPISODIC_DB",
    str(Path.home() / ".config" / "superpowers" / "conversation-index" / "db.sqlite"),
))

DAILY_HOURS = 48

# Wrappers the line may wear in transcript markdown: **bold**, *italic*, > quote,
# - bullet, • bullet, `code`, _underscore_ — before the label and around the text.
LESSON_RE = re.compile(
    r"^[\s>*_\-•`#]*operator\s+lesson[\s*_`]*:[\s*_`\"']*(.+?)[\s*_`\"']*$",
    re.IGNORECASE,
)
FENCE_RE = re.compile(r"^\s*```")

MIN_LEN = 25
MAX_LEN = 400

# Text that proves the line is the CONTRACT being quoted, not a lesson being taught.
REJECT_SUBSTRINGS = ("<one line teaching", "operator lesson")
# `Operator Lesson: Next time, ask for [X] if you want [Y].` — the SOP's own worked example.
PLACEHOLDER_RE = re.compile(r"\[[A-Za-z]\]")

TYPE_RULE_RE = re.compile(r"\b(never|always|must|don'?t|do not)\b", re.IGNORECASE)
TYPE_LOSS_RE = re.compile(r"\b(scar|failure|failed|broke|broken|cost|wasted)\b", re.IGNORECASE)
TYPE_WIN_RE = re.compile(r"\b(worked|shipped|landed|proved|proven)\b", re.IGNORECASE)
RULE_WINDOW = 80  # "early" = inside the opening clause, not anywhere in the sentence

# Ordered — first hit wins. "hook" belongs to harness-craft (hooks fire in .claude/settings.json)
# far more often than to content-science, so harness is checked first by design.
ARENAS: tuple[tuple[str, re.Pattern], ...] = (
    ("offer-linkedin", re.compile(r"\b(linkedin|offers?|outreach|dms?|campaigns?)\b", re.I)),
    ("clients", re.compile(r"\b(jen|andrea|javier|josh|clients?|listings?)\b", re.I)),
    ("harness-craft", re.compile(
        r"\b(hooks?|worktrees?|launchd|scripts?|router|routing|memory|sessions?|harness|"
        r"skills?|agents?|workflows?|pipelines?)\b", re.I)),
    ("voice-brand", re.compile(r"\b(voice|register|brand|slop|prose)\b", re.I)),
    ("content-science", re.compile(r"\b(posts?|content|reels?|carousels?)\b", re.I)),
    ("health", re.compile(r"\b(health|sleep|training)\b", re.I)),
    ("markets", re.compile(r"\b(betting|picks|markets?|arb)\b", re.I)),
)

_PUNCT = str.maketrans("", "", string.punctuation)


# ---------------------------------------------------------------- extraction


def normalize(text: str) -> str:
    """lowercase · punctuation stripped · whitespace collapsed — the dedupe key basis."""
    return " ".join(text.lower().translate(_PUNCT).split())


def lesson_hash(text: str) -> str:
    return hashlib.sha1(normalize(text).encode("utf-8")).hexdigest()


def classify_type(text: str) -> str:
    if TYPE_RULE_RE.search(text[:RULE_WINDOW]):
        return "rule"
    if TYPE_LOSS_RE.search(text):
        return "loss"
    if TYPE_WIN_RE.search(text):
        return "win"
    return "insight"


def classify_arena(text: str) -> str:
    for arena, pattern in ARENAS:
        if pattern.search(text):
            return arena
    return "general"


def extract_lessons(message: str) -> list[str]:
    """Every genuine `Operator Lesson: ...` line in one assistant message.

    Rejects, in order of how often each fires in practice:
      - anything inside a ``` fence (docs and directives quote the contract there),
      - text that re-mentions "Operator Lesson" or the `<one line teaching ...>` template,
      - a placeholder — opening with `<`, or carrying a `[X]`-style bracket slot,
      - text shorter than 25 or longer than 400 chars (headers, and runaway paragraphs).
    """
    out: list[str] = []
    in_fence = False
    for line in (message or "").splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = LESSON_RE.match(line)
        if not m:
            continue
        text = m.group(1).strip()
        if not text or text.startswith("<"):
            continue
        if not (MIN_LEN <= len(text) <= MAX_LEN):
            continue
        low = text.lower()
        if any(bad in low for bad in REJECT_SUBSTRINGS):
            continue
        if PLACEHOLDER_RE.search(text):
            continue
        out.append(text)
    return out


# ---------------------------------------------------------------- ledger io


def load_ledger() -> list[dict]:
    if not LEDGER.exists():
        return []
    rows = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def append_ledger(records: list[dict]) -> None:
    if not records:
        return
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def scan_exchanges(since_hours: int | None, source: str) -> list[dict]:
    """Read-only scan of episodic exchanges → new (unseen) lesson records, oldest first."""
    if not EPISODIC_DB.exists():
        return []

    con = sqlite3.connect(f"file:{EPISODIC_DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        con.execute("PRAGMA query_only=ON")
        sql = ("SELECT timestamp, assistant_message, session_id FROM exchanges "
               "WHERE assistant_message LIKE '%perator Lesson%'")
        params: tuple = ()
        if since_hours is not None:
            cutoff = (datetime.now(timezone.utc) - timedelta(hours=since_hours)).isoformat()
            sql += " AND timestamp >= ?"
            params = (cutoff,)
        sql += " ORDER BY timestamp ASC"
        rows = con.execute(sql, params).fetchall()
    finally:
        con.close()

    seen = {r.get("hash") for r in load_ledger()}
    new: list[dict] = []
    for r in rows:
        for text in extract_lessons(r["assistant_message"]):
            h = lesson_hash(text)
            if h in seen:
                continue
            seen.add(h)
            new.append({
                "ts": r["timestamp"],
                "lesson": text,
                "type": classify_type(text),
                "arena": classify_arena(text),
                "source": source,
                "session_id": r["session_id"],
                "hash": h,
            })
    return new


# ---------------------------------------------------------------- sovereign mirror


def mirror_to_sovereign(records: list[dict]) -> int:
    """One semantic memory per NEW lesson. Reversible by metadata.source='operator-ledger'."""
    if not records or not DB.exists():
        return 0
    con = sqlite3.connect(DB)
    inserted = 0
    try:
        for rec in records:
            mem_id = f"lesson-{rec['hash'][:8]}"
            exists = con.execute("SELECT 1 FROM memories WHERE id = ?", (mem_id,)).fetchone()
            if exists:
                continue
            con.execute(
                "INSERT INTO memories (id, tier, category, content, created_at, last_accessed, "
                "access_count, freshness, pinned, metadata, source_ids) "
                "VALUES (?, 'semantic', 'lesson', ?, ?, ?, 1, 1.0, 0, ?, '[]')",
                (
                    mem_id,
                    f"Operator Lesson ({rec['arena']}): {rec['lesson']}",
                    rec["ts"],
                    rec["ts"],
                    json.dumps({
                        "source": "operator-ledger",
                        "arena": rec["arena"],
                        "type": rec["type"],
                        "hash": rec["hash"],
                        "session_id": rec["session_id"],
                    }),
                ),
            )
            inserted += 1
        con.commit()
    finally:
        con.close()
    return inserted


# ---------------------------------------------------------------- commands


def cmd_scan(since_hours: int | None, source: str) -> int:
    before = len(load_ledger())
    new = scan_exchanges(since_hours, source)
    append_ledger(new)
    mirrored = mirror_to_sovereign(new)
    by_arena: dict[str, int] = {}
    for rec in new:
        by_arena[rec["arena"]] = by_arena.get(rec["arena"], 0) + 1
    breakdown = " · ".join(f"{k}:{v}" for k, v in sorted(by_arena.items())) or "none"
    print(f"operator-ledger {source}: +{len(new)} new lesson(s) "
          f"(ledger {before} → {before + len(new)}, sovereign +{mirrored}) [{breakdown}]")
    return 0


def cmd_stats() -> int:
    rows = load_ledger()
    if not rows:
        print("operator-ledger: empty (run `operator_ledger.py backfill`)")
        return 0
    arenas: dict[str, int] = {}
    types: dict[str, int] = {}
    for r in rows:
        arenas[r.get("arena", "?")] = arenas.get(r.get("arena", "?"), 0) + 1
        types[r.get("type", "?")] = types.get(r.get("type", "?"), 0) + 1
    span = f"{min(r['ts'] for r in rows)[:10]}→{max(r['ts'] for r in rows)[:10]}"
    a = " ".join(f"{k}:{v}" for k, v in sorted(arenas.items(), key=lambda kv: -kv[1]))
    t = " ".join(f"{k}:{v}" for k, v in sorted(types.items(), key=lambda kv: -kv[1]))
    print(f"operator-ledger: {len(rows)} lessons · {span} · arenas[{a}] · types[{t}]")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Operator Lesson ledger — extract, dedupe, persist.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("backfill", help="scan all episodic exchanges")
    sub.add_parser("daily", help=f"scan the last {DAILY_HOURS}h (idempotent)")
    sub.add_parser("stats", help="one-line count summary")
    args = ap.parse_args()

    if args.cmd == "backfill":
        return cmd_scan(None, "episodic-backfill")
    if args.cmd == "daily":
        return cmd_scan(DAILY_HOURS, "episodic-daily")
    return cmd_stats()


if __name__ == "__main__":
    sys.exit(main())
