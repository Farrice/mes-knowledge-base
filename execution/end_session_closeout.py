#!/usr/bin/env python3
"""end_session_closeout.py — deterministic closeout spine for /end-session.

WHY: /end-session persisted a handoff but never ran closeout intelligence,
never wrote sovereign memory, never touched the COS journal, and never
archived session-state.md — despite the workflow's own preamble claiming
closeout intelligence ran. This script makes the rest of the closeout
physical: one deterministic sequence, run either explicitly (`/end-session`
Step 1.4) or automatically in degraded mode by the SessionEnd hook backstop
when a session produced artifacts but was never closed out by hand.

Design rules (match memory_facade.py's degraded-reporting principle):
    - Every step is independently try/except'd. A failure or skip in one step
      NEVER stops the sequence — the spine always runs to completion.
    - Every skipped store is REPORTED, never silent.
    - Idempotent: the memory-bridge and cos-journal steps dedupe on a shared
      ledger (.agent/sessions/end-session-memory-ledger.jsonl, one JSON line
      per store with a "step" field) keyed by handoff basename (or
      session-state timestamp in degraded mode), so re-running the spine
      twice for the same close never double-writes.
    - Always exits 0. This is a reporting spine, not a gate.

Usage:
    python3 execution/end_session_closeout.py run [--slug S] [--degraded] [--dry-run]

Steps (in order): resolve-handoff, closeout-intelligence, memory-bridge,
cos-journal, archive-session-state, friction-nudge, finalize-debt-nudge,
solution-cards.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
EXEC = ROOT / "execution"
sys.path.insert(0, str(EXEC))

AGENT = ROOT / ".agent"
SESSIONS_DIR = AGENT / "sessions"
STATE_ARCHIVE_DIR = SESSIONS_DIR / "state-archive"
MEMORY_LEDGER = SESSIONS_DIR / "end-session-memory-ledger.jsonl"
SESSION_STATE = AGENT / "session-state.md"
FRICTION_LEDGER = AGENT / "friction-ledger.jsonl"
COS_DIR = AGENT / "cos"

DEGRADED_STALE_HOURS = 12


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ─────────────────────────────────────────────────────────────
# content-source resolution (handoff, or session-state.md fallback)
# ─────────────────────────────────────────────────────────────

COMPLETED_RE = re.compile(r"^\*\*\s*completed\s*\*\*[:：]?\s*(.*)$", re.IGNORECASE)
REMAINING_RE = re.compile(r"^\*\*\s*remaining\s*priorit\w*\s*\*\*[:：]?\s*(.*)$", re.IGNORECASE)


def _clean_line(t: str) -> str:
    return re.sub(r"[*`]+", "", re.sub(r"^[-\d.)\s]+", "", t)).strip()


def _grep_labeled(body: str, label_re: "re.Pattern[str]", cap: int = 3) -> str:
    """Tolerant single-field extraction: same-line value, else following
    bullet/plain lines until a blank line or the next bold label."""
    lines = body.splitlines()
    for i, line in enumerate(lines):
        m = label_re.match(line.strip())
        if not m:
            continue
        val = (m.group(1) or "").strip()
        if val:
            return _clean_line(val)[:240]
        out = []
        for nxt in lines[i + 1:]:
            t = nxt.strip()
            if not t or t.startswith("#") or re.match(r"^\*\*[^*]+\*\*", t):
                break
            c = _clean_line(t)
            if c:
                out.append(c)
            if len(out) >= cap:
                break
        return " / ".join(out)[:240]
    return ""


def _first_h1(body: str, fallback: str) -> str:
    for line in body.splitlines():
        t = line.strip()
        if t.startswith("# "):
            return t[2:].strip()
    return fallback


def _resolve_from_handoff() -> Optional[Dict[str, Any]]:
    try:
        import handoff_store  # noqa: E402

        metas = handoff_store.all_metas()
        if not metas:
            return None
        m = metas[0]
        raw = m["path"].read_text(encoding="utf-8")
        _fm, body = handoff_store.parse_frontmatter(raw)
        title = _first_h1(body, m.get("title") or m["thread"])
        completed = _grep_labeled(body, COMPLETED_RE)
        remaining = _grep_labeled(body, REMAINING_RE) or (m.get("unfinished") or "") or (m.get("resume_hint") or "")
        return {
            "source_type": "handoff",
            "title": title,
            "thread": m["thread"],
            "completed": completed,
            "remaining": remaining,
            "handoff_file": m["name"],
            "mtime": m.get("mtime", 0),
        }
    except Exception:
        return None


def _resolve_from_session_state() -> Optional[Dict[str, Any]]:
    try:
        if not SESSION_STATE.exists():
            return None
        text = SESSION_STATE.read_text(encoding="utf-8")
        if not text.strip():
            return None
        ts_m = re.search(r"Last updated:\s*(\S+)", text)
        ts = ts_m.group(1).strip() if ts_m else datetime.now().isoformat()
        title = _first_h1(text, "Session")
        active_m = re.search(r"^## Active Task\n(.+?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
        completed = _clean_line(active_m.group(1).splitlines()[0]) if active_m and active_m.group(1).strip() else ""
        next_m = re.search(r"^## Next Steps\n(.+?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
        remaining = ""
        if next_m:
            for line in next_m.group(1).splitlines():
                c = _clean_line(line)
                if c:
                    remaining = c
                    break
        if not completed:
            completed = " ".join(text.splitlines()[:40]).strip()[:240]
        return {
            "source_type": "session_state",
            "title": title,
            "thread": "session",
            "completed": completed,
            "remaining": remaining,
            "session_state_ts": ts,
        }
    except Exception:
        return None


def resolve_content_source(degraded: bool) -> Tuple[Optional[Dict[str, Any]], str]:
    """Returns (ctx | None, detail-string). ctx carries title/thread/
    completed/remaining plus a dedup key (handoff_file or session_state_ts)."""
    handoff_ctx = _resolve_from_handoff()

    if degraded:
        stale = True
        if handoff_ctx:
            age_hours = (datetime.now().timestamp() - handoff_ctx.get("mtime", 0)) / 3600.0
            stale = age_hours > DEGRADED_STALE_HOURS
        if not handoff_ctx or stale:
            state_ctx = _resolve_from_session_state()
            if state_ctx:
                return state_ctx, "degraded mode — using session-state.md (no fresh handoff)"
            if handoff_ctx:
                return handoff_ctx, "degraded mode — stale handoff and no session-state.md; using stale handoff anyway"
            return None, "no fresh handoff and no session-state.md found"
        return handoff_ctx, f"degraded mode — handoff '{handoff_ctx['handoff_file']}' is fresh enough"

    if handoff_ctx:
        return handoff_ctx, f"using handoff '{handoff_ctx['handoff_file']}'"
    state_ctx = _resolve_from_session_state()
    if state_ctx:
        return state_ctx, "no handoff found — falling back to session-state.md"
    return None, "no handoff and no session-state.md found"


# ─────────────────────────────────────────────────────────────
# steps
# ─────────────────────────────────────────────────────────────

def step_resolve_handoff(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    content, detail = resolve_content_source(degraded)
    if content is None:
        return "SKIP", detail
    ctx["content"] = content
    return "OK", detail + f" — title='{content['title']}'"


def step_closeout_intelligence(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    if dry_run:
        return "OK", "[dry-run] would run session_closeout_intelligence.py run --source end-session"
    try:
        r = subprocess.run(
            [sys.executable, str(EXEC / "session_closeout_intelligence.py"), "run", "--source", "end-session"],
            capture_output=True, text=True, timeout=60, cwd=str(ROOT),
        )
        out_lines = [ln for ln in (r.stdout or "").splitlines() if ln.strip()]
        last = out_lines[-1] if out_lines else "(no output)"
        if r.returncode != 0:
            err_lines = [ln for ln in (r.stderr or "").splitlines() if ln.strip()]
            return "FAIL", f"exit {r.returncode} — {(err_lines[-1] if err_lines else last)[:200]}"
        return "OK", last[:200]
    except subprocess.TimeoutExpired:
        return "FAIL", "timed out after 60s"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def _memory_ledger_keys(step: str = "memory") -> set:
    """Dedup keys already recorded for a given step ("memory" or "cos").
    Lines without a "step" field predate the cos-journal dedup and are
    treated as "memory" for backward compatibility."""
    keys = set()
    if not MEMORY_LEDGER.exists():
        return keys
    try:
        for line in MEMORY_LEDGER.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except Exception:
                continue
            if row.get("key") and row.get("step", "memory") == step:
                keys.add(row["key"])
    except Exception:
        pass
    return keys


def _memory_ledger_append(row: dict) -> None:
    try:
        SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
        with open(MEMORY_LEDGER, "a", encoding="utf-8") as f:
            f.write(json.dumps(row) + "\n")
    except Exception:
        pass


def _dedup_key(content: Dict[str, Any]) -> str:
    """Stable per-close dedup key: handoff basename, or session-state timestamp
    in degraded/fallback mode. Shared by memory-bridge and cos-journal."""
    if content["source_type"] == "handoff":
        return content["handoff_file"]
    return content["session_state_ts"]


def step_memory_bridge(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    content = ctx.get("content")
    if not content:
        return "SKIP", "no content source resolved (see resolve-handoff)"

    key = _dedup_key(content)
    if content["source_type"] == "handoff":
        meta_extra = {"handoff_file": content["handoff_file"]}
    else:
        meta_extra = {"session_state_ts": content["session_state_ts"]}

    if key in _memory_ledger_keys("memory"):
        return "SKIP", f"already stored (key={key})"

    text = (
        f"Session closeout: {content['title']}\n"
        f"Completed: {content.get('completed') or '(not captured)'}\n"
        f"Remaining: {content.get('remaining') or '(not captured)'}"
    )
    metadata = {"source": "end_session", **meta_extra}

    if dry_run:
        return "OK", f"[dry-run] would store episodic milestone — key={key} — {text[:100].replace(chr(10), ' / ')}"

    try:
        from memory_store import store_memory  # noqa: E402

        mid = store_memory(
            tier="episodic", category="milestone", content=text,
            metadata=metadata, source_ids=[key], silent=True,
        )
        if not mid:
            return "FAIL", "store_memory returned no id"
        _memory_ledger_append({"key": key, "step": "memory", "ts": _now_iso(), "memory_id": mid})
        return "OK", f"stored episodic milestone id={mid} (key={key})"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def step_cos_journal(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    if not COS_DIR.exists():
        return "SKIP", ".agent/cos/ does not exist"
    content = ctx.get("content")
    if not content:
        return "SKIP", "no content source resolved (see resolve-handoff)"

    key = _dedup_key(content)
    if key in _memory_ledger_keys("cos"):
        return "SKIP", f"already journaled (key={key})"

    remaining = content.get("remaining") or "(no remaining priority captured)"
    text = f"Session closed: {content['title']} — next: {remaining}"

    if dry_run:
        return "OK", f"[dry-run] would append to COS journal: {text[:150]}"

    try:
        r = subprocess.run(
            [sys.executable, str(EXEC / "cos_prep.py"), "capture", "--text", text, "--route", "journal"],
            capture_output=True, text=True, timeout=15, cwd=str(ROOT),
        )
        if r.returncode != 0 or "Captured to journal" not in (r.stdout or ""):
            err = (r.stderr or r.stdout or "").strip().splitlines()
            return "FAIL", (err[-1] if err else f"exit {r.returncode}")[:200]
        _memory_ledger_append({"key": key, "step": "cos", "ts": _now_iso()})
        return "OK", (r.stdout or "").strip().splitlines()[-1][:200]
    except subprocess.TimeoutExpired:
        return "FAIL", "timed out after 15s"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def step_archive_session_state(ctx: Dict[str, Any], degraded: bool, dry_run: bool, slug: str) -> Tuple[str, str]:
    try:
        if not SESSION_STATE.exists() or not SESSION_STATE.read_text(encoding="utf-8").strip():
            return "SKIP", "session-state.md missing or empty"

        date_str = datetime.now().date().isoformat()
        safe_slug = re.sub(r"[^a-z0-9-]+", "-", (slug or "session").lower()).strip("-") or "session"
        dest_dir = STATE_ARCHIVE_DIR
        base = f"{date_str}-{safe_slug}.md"
        dest = dest_dir / base
        n = 2
        while dest.exists():
            dest = dest_dir / f"{date_str}-{safe_slug}-{n}.md"
            n += 1

        if dry_run:
            return "OK", f"[dry-run] would archive session-state.md to .agent/sessions/state-archive/{dest.name}"

        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SESSION_STATE, dest)
        return "OK", f"archived to .agent/sessions/state-archive/{dest.name} (original left in place)"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def step_friction_nudge(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    if not FRICTION_LEDGER.exists():
        return "SKIP", "no friction ledger found"
    try:
        captured = []
        for line in FRICTION_LEDGER.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except Exception:
                continue
            if row.get("status") == "captured":
                captured.append(row.get("timestamp", ""))
        if not captured:
            return "SKIP", "0 unresolved friction entries"
        oldest = sorted(t for t in captured if t)
        oldest_date = oldest[0][:10] if oldest else "?"
        return "OK", f"{len(captured)} unresolved friction entries (oldest: {oldest_date}) — review via /system-audit"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def step_finalize_debt_nudge(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    try:
        if not SESSIONS_DIR.exists():
            return "SKIP", "no .agent/sessions/ directory"
        candidates = sorted(SESSIONS_DIR.glob("ledger-*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not candidates:
            return "SKIP", "no session ledger files found"
        ledger = json.loads(candidates[0].read_text(encoding="utf-8"))
        produced = bool(ledger.get("produced")) or bool(ledger.get("produced_paths"))
        finalized_at = ledger.get("finalized_at")
        if produced and not finalized_at:
            return "OK", "finalize debt open: run chain_runner.py finalize"
        return "SKIP", "no open finalize debt in the newest session ledger"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def step_solution_cards(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    """Report Solution Card capture health (Solution Recorder, 2026-07-07):
    how many cards were saved today, and whether FRESH learning_debt (<4h,
    solution_recorder.split_debt_freshness) is still open on the newest
    session ledger — stale debt is reported as 'stale, ignored', never as
    open. SKIPs when neither applies."""
    try:
        solutions_dir = ROOT / "docs" / "solutions"
        today = datetime.now().date().isoformat()
        saved_today = list(solutions_dir.glob(f"{today}-*.md")) if solutions_dir.exists() else []

        learning_debt: list = []
        if SESSIONS_DIR.exists():
            candidates = sorted(SESSIONS_DIR.glob("ledger-*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
            if candidates:
                try:
                    ledger = json.loads(candidates[0].read_text(encoding="utf-8"))
                    learning_debt = ledger.get("learning_debt") or []
                except Exception:
                    learning_debt = []

        try:
            from solution_recorder import split_debt_freshness
            fresh_debt, stale_debt = split_debt_freshness(learning_debt)
        except ImportError:
            # Inline fallback mirroring split_debt_freshness (4h window;
            # unparseable ts = stale).
            from datetime import timedelta
            cutoff = datetime.now() - timedelta(hours=4)
            fresh_debt, stale_debt = [], []
            for d in learning_debt:
                try:
                    ok = datetime.fromisoformat(str(d.get("ts", ""))) >= cutoff
                except Exception:
                    ok = False
                (fresh_debt if ok else stale_debt).append(d)

        parts = []
        if saved_today:
            parts.append(f"OK — {len(saved_today)} card(s) saved today")
        if fresh_debt:
            parts.append(f"OK — learning debt OPEN ({len(fresh_debt)} entries) — run /extract-approach")
        if stale_debt:
            parts.append(f"{len(stale_debt)} debt entr{'y' if len(stale_debt) == 1 else 'ies'} >4h old — stale, ignored")

        if not parts:
            return "SKIP", "no cards saved today and no open learning debt"
        return "OK", "; ".join(parts)
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


# ─────────────────────────────────────────────────────────────
# spine runner
# ─────────────────────────────────────────────────────────────

def run(slug: str, degraded: bool, dry_run: bool) -> int:
    ctx: Dict[str, Any] = {}
    steps = [
        ("resolve-handoff", lambda: step_resolve_handoff(ctx, degraded, dry_run)),
        ("closeout-intelligence", lambda: step_closeout_intelligence(ctx, degraded, dry_run)),
        ("memory-bridge", lambda: step_memory_bridge(ctx, degraded, dry_run)),
        ("cos-journal", lambda: step_cos_journal(ctx, degraded, dry_run)),
        ("archive-session-state", lambda: step_archive_session_state(ctx, degraded, dry_run, slug)),
        ("friction-nudge", lambda: step_friction_nudge(ctx, degraded, dry_run)),
        ("finalize-debt-nudge", lambda: step_finalize_debt_nudge(ctx, degraded, dry_run)),
        ("solution-cards", lambda: step_solution_cards(ctx, degraded, dry_run)),
    ]

    counts = {"OK": 0, "SKIP": 0, "FAIL": 0}
    for name, fn in steps:
        try:
            status, detail = fn()
        except Exception as e:
            status, detail = "FAIL", f"unhandled {type(e).__name__}: {e}"
        if status not in counts:
            status = "FAIL"
        counts[status] += 1
        print(f"CLOSEOUT {name}: {status} — {detail}")

    print(f"CLOSEOUT SPINE COMPLETE ({counts['OK']} ok, {counts['SKIP']} skip, {counts['FAIL']} fail)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic closeout spine for /end-session")
    sub = ap.add_subparsers(dest="command", required=True)
    rp = sub.add_parser("run", help="Run the closeout spine")
    rp.add_argument("--slug", default="", help="Thread slug — used to name the archived session-state file")
    rp.add_argument("--degraded", action="store_true", help="Run in degraded mode (SessionEnd-hook backstop path)")
    rp.add_argument("--dry-run", action="store_true", help="Perform reads and print intent; write nothing")
    args = ap.parse_args()

    if args.command == "run":
        try:
            return run(args.slug, args.degraded, args.dry_run)
        except Exception as e:
            print(f"CLOSEOUT SPINE COMPLETE (0 ok, 0 skip, 1 fail) — fatal: {type(e).__name__}: {e}")
            return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
