#!/usr/bin/env python3
"""episodic_ingest.py — L1→L2 bridge: superpowers conversation history → sovereign episodic tier.

The L1 capture layer (the superpowers `episodic-memory` plugin) mechanically
indexes every CC/Codex exchange into a local SQLite store. That's the
"auto-remember" substrate, queryable through `memory_facade.py --sources episodic`.

This bridge promotes it INTO the distillation pipeline: it summarizes recent
*sessions* (not raw exchanges) and stores one episodic `milestone` record per
session in `.memory/sovereign.db`. The EXISTING weekly job then does the rest —
`memory_distill.py` clusters embedded episodic records, Gemini proposes+judges a
semantic rule per cluster, and writes to `flagged_review` for HUMAN approval via
`memory_review.py`. Nothing auto-promotes to semantic memory; the human-review
gate is the privacy backstop (raw chat never becomes a durable rule unsupervised).

Design rules (match the rest of the memory stack):
    - Read-only on the L1 index; the only writes are session summaries into the
      EXISTING sovereign store (no 8th store, no new file per the consolidation map).
    - Deterministic by default: NO LLM calls, NO embedding at ingest time (zero
      surprise spend). Embedding happens later via `memory_embed.py`; that's what
      makes a row distill-eligible.
    - Idempotent: dedup by session_id in source_ids, so re-runs don't duplicate.
    - PII-redacted: emails / phones / long digit runs are masked before storage.
    - Project-scoped to this repo by default (ANTIGRAVITY_EPISODIC_PROJECTS, same
      env var as the facade; "all" for cross-project).

Usage:
    python3 execution/episodic_ingest.py preview                 # dry-run (default), zero writes
    python3 execution/episodic_ingest.py run                     # write session summaries to sovereign episodic
    python3 execution/episodic_ingest.py run --days 14
    python3 execution/episodic_ingest.py run --max-sessions 5    # smoke test
    python3 execution/episodic_ingest.py run --json

Complete the L1→L2 loop after a run:
    python3 execution/memory_embed.py            # embed new episodic rows
    python3 execution/memory_distill.py preview  # see proposed semantic rules
    python3 execution/memory_review.py           # approve/reject (human gate)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

from memory_store import DB_PATH, store_memory  # noqa: E402

EPISODIC_DB = Path(os.environ.get(
    "ANTIGRAVITY_EPISODIC_DB",
    str(Path.home() / ".config" / "superpowers" / "conversation-index" / "db.sqlite"),
))

DEFAULT_DAYS = 7
INGEST_SOURCE = "episodic_ingest"


def project_keys() -> Optional[List[str]]:
    """This repo's project key by default; ANTIGRAVITY_EPISODIC_PROJECTS overrides
    (comma-separated, or "all" for no scope filter). Mirrors memory_facade."""
    env = os.environ.get("ANTIGRAVITY_EPISODIC_PROJECTS", "").strip()
    if env.lower() == "all":
        return None
    if env:
        return [p.strip() for p in env.split(",") if p.strip()]
    return ["-" + str(ROOT).strip("/").replace("/", "-").replace(" ", "-")]


def excluded_projects() -> List[str]:
    """Privacy lever: never ingest these projects (client/personal dirs)."""
    env = os.environ.get("ANTIGRAVITY_EPISODIC_EXCLUDE_PROJECTS", "").strip()
    return [p.strip() for p in env.split(",") if p.strip()]


_EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
_PHONE = re.compile(r"\b(?:\+?\d[\d\s().-]{7,}\d)\b")
_LONGDIGITS = re.compile(r"\b\d{6,}\b")


def redact(text: str) -> str:
    """Mask the obvious PII shapes before a summary enters durable storage."""
    if not text:
        return ""
    text = _EMAIL.sub("[email]", text)
    text = _PHONE.sub("[phone]", text)
    text = _LONGDIGITS.sub("[num]", text)
    return text


def _is_substantive(msg: str) -> bool:
    """A real user instruction, not a system reminder / tool-result / notification."""
    if not msg or len(msg.strip()) < 20:
        return False
    head = msg.strip()[:40].lower()
    if head.startswith("<") or "system-reminder" in head or "task-notification" in head:
        return False
    return True


def load_sessions(days: int) -> Dict[str, List[sqlite3.Row]]:
    """Group recent, non-sidechain exchanges by session_id (read-only)."""
    if not EPISODIC_DB.exists():
        raise FileNotFoundError(f"episodic db missing: {EPISODIC_DB}")
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    projects = project_keys()
    excl = excluded_projects()

    where = ["is_sidechain = 0", "timestamp >= ?"]
    params: List[Any] = [cutoff]
    if projects:
        where.append("project IN (%s)" % ",".join("?" for _ in projects))
        params.extend(projects)
    if excl:
        where.append("project NOT IN (%s)" % ",".join("?" for _ in excl))
        params.extend(excl)

    con = sqlite3.connect(f"file:{EPISODIC_DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        con.execute("PRAGMA query_only=ON")
        rows = con.execute(
            "SELECT session_id, project, timestamp, user_message, assistant_message, "
            "cwd, git_branch FROM exchanges "
            f"WHERE {' AND '.join(where)} ORDER BY session_id, timestamp ASC",
            params,
        ).fetchall()
    finally:
        con.close()

    sessions: Dict[str, List[sqlite3.Row]] = {}
    for r in rows:
        sid = r["session_id"] or f"_nosession_{r['timestamp'][:10]}"
        sessions.setdefault(sid, []).append(r)
    return sessions


def summarize_session(sid: str, rows: List[sqlite3.Row]) -> Dict[str, Any]:
    """One deterministic episodic record per session — no LLM."""
    intent = ""
    for r in rows:
        if _is_substantive(r["user_message"]):
            intent = r["user_message"].strip()
            break
    if not intent and rows:
        intent = (rows[0]["user_message"] or "").strip()
    outcome = (rows[-1]["assistant_message"] or "").strip() if rows else ""

    intent = redact(intent)[:240]
    outcome = redact(outcome)[:240]
    n = len(rows)
    start, end = rows[0]["timestamp"], rows[-1]["timestamp"]
    branch = rows[0]["git_branch"] or "?"
    day = start[:10]

    content = (
        f"Session {day} · {n} exchanges · branch {branch}\n"
        f"Intent: {intent}\n"
        f"Outcome: {outcome}"
    )
    meta = {
        "source": INGEST_SOURCE,
        "session_id": sid,
        "project": rows[0]["project"],
        "exchanges": n,
        "started": start,
        "ended": end,
        "cwd": rows[0]["cwd"],
        "branch": branch,
    }
    return {"content": content, "metadata": meta, "session_id": sid}


def ingested_session_ids() -> set:
    """Session ids already promoted into sovereign (dedup on re-run)."""
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    try:
        rows = con.execute(
            "SELECT source_ids FROM memories WHERE tier='episodic' "
            "AND metadata LIKE ?", (f'%"{INGEST_SOURCE}"%',)
        ).fetchall()
    finally:
        con.close()
    seen = set()
    for (sids,) in rows:
        try:
            for s in json.loads(sids or "[]"):
                seen.add(s)
        except (json.JSONDecodeError, TypeError):
            continue
    return seen


def run(days: int, dry_run: bool, max_sessions: Optional[int]) -> Dict[str, Any]:
    sessions = load_sessions(days)
    already = ingested_session_ids()
    candidates = {sid: rows for sid, rows in sessions.items() if sid not in already}

    # newest sessions first; cap if requested
    ordered = sorted(candidates.items(), key=lambda kv: kv[1][-1]["timestamp"], reverse=True)
    if max_sessions:
        ordered = ordered[:max_sessions]

    summary = {
        "days": days, "sessions_in_window": len(sessions),
        "already_ingested": len(sessions) - len(candidates),
        "to_ingest": len(ordered), "written": 0, "dry_run": dry_run,
        "records": [],
    }

    for sid, rows in ordered:
        rec = summarize_session(sid, rows)
        summary["records"].append({
            "session_id": sid, "exchanges": rec["metadata"]["exchanges"],
            "started": rec["metadata"]["started"], "preview": rec["content"][:160],
        })
        if dry_run:
            print(f"[would ingest] {sid[:12]} · {rec['metadata']['exchanges']} ex · {rec['metadata']['started'][:10]}")
            print(f"    {rec['content'][:160].replace(chr(10), ' / ')}")
            continue
        mid = store_memory(
            tier="episodic", category="milestone", content=rec["content"],
            metadata=rec["metadata"], source_ids=[sid], silent=True,
        )
        if mid:
            summary["written"] += 1
            print(f"[ingested {mid}] {sid[:12]} · {rec['metadata']['exchanges']} ex")

    print("\n─── EPISODIC INGEST SUMMARY ───")
    print(f"  window: last {days}d · sessions: {summary['sessions_in_window']}")
    print(f"  already ingested: {summary['already_ingested']} · new candidates: {summary['to_ingest']}")
    print(f"  written: {summary['written']}{' (dry-run)' if dry_run else ''}")
    if not dry_run and summary["written"]:
        print("  next: python3 execution/memory_embed.py && python3 execution/memory_distill.py preview")
    return summary


def main() -> int:
    ap = argparse.ArgumentParser(description="L1→L2 bridge: conversation history → sovereign episodic tier")
    ap.add_argument("command", nargs="?", default="preview", choices=["preview", "run"],
                    help="preview = dry-run (default); run = write session summaries")
    ap.add_argument("--days", type=int, default=DEFAULT_DAYS, help=f"Look back N days (default {DEFAULT_DAYS})")
    ap.add_argument("--max-sessions", type=int, help="Cap sessions ingested (smoke test)")
    ap.add_argument("--json", action="store_true", help="JSON summary output")
    args = ap.parse_args()

    dry_run = args.command == "preview"
    summary = run(days=args.days, dry_run=dry_run, max_sessions=args.max_sessions)
    if args.json:
        print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
