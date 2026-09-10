#!/usr/bin/env python3
"""harness_behavior_report.py — deterministic per-model-per-week harness
telemetry, modeled on session_ledger_report.py (same summary()/render()
contract so health_metrics.py or any other consumer can import it the same
way).

Purpose: a regression like "gpt-6-astra fell from 25 to 12 tool calls per
user turn" should show within a day, not get discovered three weeks later
in a felt-drift conversation. AI-memory-dependent observability is banned
(directives/feedback_ai-memory-dependent-observability.md) — this is the
deterministic backstop.

Data source: the episodic-memory index sqlite
(~/.config/superpowers/conversation-index/db.sqlite), table `exchanges`.
Each row is one user-turn window: harness, model, session_id, archive_path,
line_start, line_end (1-indexed, inclusive), timestamp. For every exchange
in the requested window this script opens archive_path (a JSONL transcript
mirrored from ~/.claude/projects/** or ~/.codex/sessions/**), reads lines
line_start..line_end, and counts:

  - tool calls   — Codex: response_item payloads of type function_call or
                   custom_tool_call. Claude: assistant-message content
                   blocks of type tool_use.
  - writes       — Codex: a tool call whose name or argument/input blob
                   references apply_patch (Codex routes file edits through
                   `tools.apply_patch(...)`, sometimes wrapped in a
                   custom_tool_call named "exec"). Claude: tool_use blocks
                   named Write / Edit / NotebookEdit / MultiEdit.
  - artifact path — whether the LAST assistant message text in the window
                   contains a repo-relative path
                   (_active|execution|deliverables|docs|skills|.agent)/...

A missing db or an unreadable/oversized archive is never silently turned
into a zero — see `status: UNKNOWN` and the per-run `skipped_archives` note.

Usage:
    python3 execution/harness_behavior_report.py [--days 7] [--json]
        [--db PATH] [--archive-root PATH] [--since ISO8601]
"""

import argparse
import json
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB = Path.home() / ".config" / "superpowers" / "conversation-index" / "db.sqlite"
DEFAULT_ARCHIVE_ROOT = Path.home() / ".config" / "superpowers" / "conversation-archive"

# Caps (repo rule: bound worst-case work deterministically, never spin).
MAX_ARCHIVE_BYTES = 60 * 1024 * 1024
MAX_EXCHANGES_PER_MODEL = 3000
MAX_ROWS_FETCHED = 100_000  # defensive net around the SQL fetch itself
BASELINE_DAYS = 14
DROP_FLAG_PCT = 30.0

ARTIFACT_PATH_RE = re.compile(r"(?:_active|execution|deliverables|docs|skills|\.agent)/[\w./-]+")
CLAUDE_WRITE_TOOLS = {"Write", "Edit", "NotebookEdit", "MultiEdit"}
APPLY_PATCH_RE = re.compile(r"apply_patch")


# ---------------------------------------------------------------------------
# Archive parsing
# ---------------------------------------------------------------------------

def _resolve_archive_path(raw_path: str, archive_root: Path) -> Path:
    p = Path(raw_path)
    if p.is_absolute():
        return p
    return archive_root / raw_path


def _load_archive_lines(raw_path: str, archive_root: Path, cache: dict, skipped: dict):
    """Read + cache one archive file's lines. Returns list[str] or None."""
    if raw_path in cache:
        return cache[raw_path]
    p = _resolve_archive_path(raw_path, archive_root)
    try:
        if not p.exists():
            skipped[raw_path] = "missing"
            cache[raw_path] = None
            return None
        size = p.stat().st_size
        if size > MAX_ARCHIVE_BYTES:
            skipped[raw_path] = f"too_large ({size} bytes > {MAX_ARCHIVE_BYTES})"
            cache[raw_path] = None
            return None
        lines = p.read_text(errors="replace").splitlines()
    except Exception as e:
        skipped[raw_path] = f"read_error: {type(e).__name__}: {e}"
        cache[raw_path] = None
        return None
    cache[raw_path] = lines
    return lines


def _slice(lines, line_start: int, line_end: int):
    """1-indexed, inclusive-inclusive slice, tolerant of out-of-range bounds."""
    n = len(lines)
    for i in range(max(1, line_start), line_end + 1):
        idx = i - 1
        if 0 <= idx < n:
            yield lines[idx]


def _claude_exchange_stats(lines, line_start: int, line_end: int):
    """Parse a Claude-shaped transcript slice: {"type": "assistant", "message":
    {"role": "assistant", "content": [...]}} lines. tool_use blocks are calls;
    Write/Edit/NotebookEdit/MultiEdit tool_use blocks are writes; text blocks
    are prose. `final_text` is the text of the LAST assistant line in range."""
    tool_calls = 0
    writes = 0
    prose_chars = 0
    final_text = ""
    for raw in _slice(lines, line_start, line_end):
        raw = raw.strip()
        if not raw:
            continue
        try:
            obj = json.loads(raw)
        except Exception:
            continue
        if obj.get("type") != "assistant":
            continue
        msg = obj.get("message") or {}
        if msg.get("role") != "assistant":
            continue
        content = msg.get("content")
        if not isinstance(content, list):
            continue
        text_parts = []
        for c in content:
            if not isinstance(c, dict):
                continue
            ctype = c.get("type")
            if ctype == "tool_use":
                tool_calls += 1
                if c.get("name") in CLAUDE_WRITE_TOOLS:
                    writes += 1
            elif ctype == "text":
                t = c.get("text") or ""
                prose_chars += len(t)
                text_parts.append(t)
        if text_parts:
            final_text = "\n".join(text_parts)
    return tool_calls, writes, prose_chars, final_text


def _codex_exchange_stats(lines, line_start: int, line_end: int):
    """Parse a Codex-shaped transcript slice: {"payload": {"type": ...}} lines.
    function_call / custom_tool_call payloads are calls; a call referencing
    apply_patch (directly by name, or via a wrapped `tools.apply_patch(...)`
    exec call) is a write. `final_text` is the last assistant `message`
    payload's output_text, in file order (agent_message / reasoning /
    token_usage_record payloads are not the user-facing reply)."""
    tool_calls = 0
    writes = 0
    prose_chars = 0
    final_text = ""
    for raw in _slice(lines, line_start, line_end):
        raw = raw.strip()
        if not raw:
            continue
        try:
            obj = json.loads(raw)
        except Exception:
            continue
        p = obj.get("payload")
        if not isinstance(p, dict):
            continue
        ptype = p.get("type")
        if ptype in ("function_call", "custom_tool_call"):
            tool_calls += 1
            name = str(p.get("name") or "")
            blob = p.get("arguments") if ptype == "function_call" else p.get("input")
            if APPLY_PATCH_RE.search(name) or APPLY_PATCH_RE.search(str(blob or "")):
                writes += 1
        elif ptype == "message" and p.get("role") == "assistant":
            content = p.get("content")
            text_parts = []
            if isinstance(content, list):
                for c in content:
                    if isinstance(c, dict) and c.get("type") == "output_text":
                        t = c.get("text") or ""
                        prose_chars += len(t)
                        text_parts.append(t)
            if text_parts:
                final_text = "\n".join(text_parts)
    return tool_calls, writes, prose_chars, final_text


def _process_rows(rows, archive_root: Path, cache: dict, skipped: dict, cap: int):
    """rows: sqlite3.Row list for ONE model, most-recent-first. Returns the
    raw aggregate dict (harness, turns, calls, writes, prose_chars,
    le3_count, artifact_count) over at most `cap` exchanges."""
    harness_seen = None
    turns = calls = writes = prose_chars = le3_count = artifact_count = 0
    for r in rows[:cap]:
        harness = (r["harness"] or "").strip().lower()
        harness_seen = harness_seen or harness
        lines = _load_archive_lines(r["archive_path"], archive_root, cache, skipped)
        if lines is None:
            continue  # unreadable/oversized archive: exclude, never invent zeros
        if harness == "codex":
            tc, wc, pc, final_text = _codex_exchange_stats(lines, r["line_start"], r["line_end"])
        else:
            tc, wc, pc, final_text = _claude_exchange_stats(lines, r["line_start"], r["line_end"])
        turns += 1
        calls += tc
        writes += wc
        prose_chars += pc
        if tc <= 3:
            le3_count += 1
        if final_text and ARTIFACT_PATH_RE.search(final_text):
            artifact_count += 1
    return {
        "harness": harness_seen or "unknown",
        "turns": turns,
        "calls": calls,
        "writes": writes,
        "prose_chars": prose_chars,
        "le3_count": le3_count,
        "artifact_count": artifact_count,
    }


def _rollup(agg: dict) -> dict:
    turns = agg["turns"]
    calls = agg["calls"]
    return {
        "harness": agg["harness"],
        "turns": turns,
        "calls_per_turn": round(calls / turns, 2),
        "writes_per_turn": round(agg["writes"] / turns, 2),
        "prose_chars_per_call": round(agg["prose_chars"] / calls, 1) if calls else 0.0,
        "pct_turns_le3_calls": round(100.0 * agg["le3_count"] / turns, 1),
        "pct_final_with_artifact_path": round(100.0 * agg["artifact_count"] / turns, 1),
    }


# ---------------------------------------------------------------------------
# summary() / render() — the imported contract
# ---------------------------------------------------------------------------

def _fetch_rows(conn, cutoff_iso: str):
    cur = conn.execute(
        "SELECT harness, model, session_id, archive_path, line_start, line_end, timestamp "
        "FROM exchanges WHERE timestamp >= ? ORDER BY timestamp DESC LIMIT ?",
        (cutoff_iso, MAX_ROWS_FETCHED),
    )
    return cur.fetchall()


def _group_by_model(rows):
    by_model = defaultdict(list)
    for r in rows:
        by_model[r["model"] or "(unknown)"].append(r)
    return by_model


def summary(days: int = 7, since: str = None, db_path: str = None, archive_root: str = None) -> dict:
    """Machine-readable rollup. Deterministic, stdlib only. Never invents
    zeros for data it could not read — a missing db or a fully-unreadable
    window degrades to {"status": "UNKNOWN", "reason": ...}."""
    db_p = Path(db_path) if db_path else DEFAULT_DB
    archive_root_p = Path(archive_root) if archive_root else DEFAULT_ARCHIVE_ROOT

    now = datetime.now(timezone.utc)
    if since:
        try:
            start = datetime.fromisoformat(since)
        except Exception:
            return {"status": "UNKNOWN", "reason": f"invalid --since value: {since!r}"}
        window_desc = f"since {since}"
    else:
        start = now - timedelta(days=days)
        window_desc = f"last {days}d"
    window_cutoff = start.isoformat()
    baseline_cutoff = (now - timedelta(days=BASELINE_DAYS)).isoformat()

    if not db_p.exists():
        return {"status": "UNKNOWN", "reason": f"db not found: {db_p}"}

    try:
        conn = sqlite3.connect(str(db_p))
        conn.row_factory = sqlite3.Row
    except Exception as e:
        return {"status": "UNKNOWN", "reason": f"db open failed: {type(e).__name__}: {e}"}

    try:
        window_rows = _fetch_rows(conn, window_cutoff)
        baseline_rows = _fetch_rows(conn, baseline_cutoff)
    except Exception as e:
        conn.close()
        return {"status": "UNKNOWN", "reason": f"query failed (schema mismatch?): {type(e).__name__}: {e}"}
    conn.close()

    cache: dict = {}
    skipped: dict = {}

    window_by_model = _group_by_model(window_rows)
    baseline_by_model = _group_by_model(baseline_rows)

    by_model = {}
    for model, rows in window_by_model.items():
        agg = _process_rows(rows, archive_root_p, cache, skipped, MAX_EXCHANGES_PER_MODEL)
        if agg["turns"] == 0:
            continue  # nothing readable for this model in-window — omit, don't zero-fill
        by_model[model] = _rollup(agg)

    baseline_14d = {}
    for model, rows in baseline_by_model.items():
        agg = _process_rows(rows, archive_root_p, cache, skipped, MAX_EXCHANGES_PER_MODEL)
        if agg["turns"] == 0:
            continue
        baseline_14d[model] = round(agg["calls"] / agg["turns"], 2)

    flags = []
    for model, m in by_model.items():
        base = baseline_14d.get(model)
        if not base or base <= 0:
            continue
        drop_pct = 100.0 * (base - m["calls_per_turn"]) / base
        if drop_pct > DROP_FLAG_PCT:
            flags.append(
                f"{model}: calls/turn {m['calls_per_turn']} is {round(drop_pct, 1)}% "
                f"below 14-day median {base}"
            )

    if not by_model:
        return {
            "status": "UNKNOWN",
            "reason": "no readable exchanges in window (db opened but archives missing/empty)",
            "window": window_desc,
        }

    result = {
        "window": window_desc,
        "generated": datetime.now().isoformat(timespec="seconds"),
        "by_model": by_model,
        "baseline_14d": baseline_14d,
        "flags": flags,
    }
    if skipped:
        result["skipped_archives"] = skipped
    return result


def render(s: dict) -> str:
    if not s or s.get("status") == "UNKNOWN":
        reason = (s or {}).get("reason", "no data")
        return f"# Harness Behavior Report\n\n(UNKNOWN: {reason})\n"

    lines = [
        "# Harness Behavior Report",
        f"Generated {s['generated']} · window: {s['window']} · source: conversation-index/db.sqlite",
        "",
        "| model | harness | turns | calls/turn | writes/turn | prose/call | %<=3 calls | %final w/ path |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for model, m in sorted(s["by_model"].items(), key=lambda kv: -kv[1]["turns"]):
        lines.append(
            f"| {model} | {m['harness']} | {m['turns']} | {m['calls_per_turn']} | "
            f"{m['writes_per_turn']} | {m['prose_chars_per_call']} | "
            f"{m['pct_turns_le3_calls']}% | {m['pct_final_with_artifact_path']}% |"
        )

    if s.get("flags"):
        lines += ["", "## Flags (>30% drop vs 14-day baseline)", ""]
        lines += [f"- {f}" for f in s["flags"]]
    else:
        lines += ["", "No model dropped more than 30% below its 14-day baseline calls/turn."]

    if s.get("skipped_archives"):
        lines += ["", f"_{len(s['skipped_archives'])} archive(s) skipped (missing/too large/unreadable) — excluded, not zero-filled._"]

    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Per-model harness behavior telemetry (tool calls, writes, artifact-path rate).")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--since", default=None, help="ISO8601 override for the window start")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--db", default=None)
    ap.add_argument("--archive-root", default=None)
    args = ap.parse_args(argv)

    s = summary(days=args.days, since=args.since, db_path=args.db, archive_root=args.archive_root)
    if args.json:
        print(json.dumps(s, indent=2))
    else:
        print(render(s))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
