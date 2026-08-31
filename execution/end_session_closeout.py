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
    python3 execution/end_session_closeout.py run [--slug S] [--handoff PATH]
        [--git-policy legacy|codex-owned|off] [--degraded] [--dry-run]

Steps (in order): commit-gate, resolve-handoff, closeout-intelligence,
memory-bridge, cos-journal, archive-session-state, session-guide,
artifact-sweep, menu-parity, friction-nudge, finalize-debt-nudge,
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

# Module-style import ON PURPOSE: `degraded` is a bool parameter in nearly every
# step function here (same shadowing landmine mission_board.py hit 2026-08-08),
# so the ledgering calls are spelled degrade.degraded(...) — unshadowable.
import degrade  # noqa: E402

AGENT = ROOT / ".agent"
SESSIONS_DIR = AGENT / "sessions"
STATE_ARCHIVE_DIR = SESSIONS_DIR / "state-archive"
MEMORY_LEDGER = SESSIONS_DIR / "end-session-memory-ledger.jsonl"
SESSION_STATE = AGENT / "session-state.md"
FRICTION_LEDGER = AGENT / "friction-ledger.jsonl"
COS_DIR = AGENT / "cos"
GUIDES_DIR = ROOT / "guides"
GUIDES_INDEX = GUIDES_DIR / "INDEX.md"

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


def _handoff_context(path: Path) -> Dict[str, Any]:
    import handoff_store  # noqa: E402

    raw = path.read_text(encoding="utf-8")
    _fm, body = handoff_store.parse_frontmatter(raw)
    meta = handoff_store.read_meta(path)
    title = _first_h1(body, meta.get("title") or meta["thread"])
    completed = _grep_labeled(body, COMPLETED_RE)
    remaining = (_grep_labeled(body, REMAINING_RE) or
                 (meta.get("unfinished") or "") or (meta.get("resume_hint") or ""))
    return {
        "source_type": "handoff",
        "source_path": str(path.resolve()),
        "title": title,
        "thread": meta["thread"],
        "completed": completed,
        "remaining": remaining,
        "handoff_file": meta["name"],
        "mtime": meta.get("mtime", 0),
    }


def _resolve_from_handoff(path: Optional[Path] = None) -> Optional[Dict[str, Any]]:
    try:
        import handoff_store  # noqa: E402

        if path is not None:
            resolved = path.expanduser()
            if not resolved.is_absolute():
                resolved = ROOT / resolved
            if not resolved.exists():
                return None
            return _handoff_context(resolved)

        metas = handoff_store.all_metas()
        if not metas:
            return None
        return _handoff_context(metas[0]["path"])
    except Exception as e:
        # None also means "no handoff found" — the failure path is ledgered so
        # a broken handoff store is distinguishable from an empty one.
        return degrade.degraded(None, "handoff resolution failed — falling back as if none exists", e)


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
    except Exception as e:
        return degrade.degraded(None, "session-state.md unreadable/unparseable — treated as absent", e)


def resolve_content_source(degraded: bool, handoff_path: Optional[Path] = None) -> Tuple[Optional[Dict[str, Any]], str]:
    """Returns (ctx | None, detail-string). ctx carries title/thread/
    completed/remaining plus a dedup key (handoff_file or session_state_ts)."""
    handoff_ctx = _resolve_from_handoff(handoff_path)

    if handoff_path is not None:
        if handoff_ctx:
            return handoff_ctx, f"using exact handoff '{handoff_ctx['source_path']}'"
        return None, f"exact handoff not found or unreadable: {handoff_path}"

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
    content, detail = resolve_content_source(degraded, ctx.get("handoff_path"))
    if content is None:
        return "SKIP", detail
    ctx["content"] = content
    return "OK", detail + f" — title='{content['title']}'"


def step_closeout_intelligence(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    if dry_run:
        return "OK", "[dry-run] would run session_closeout_intelligence.py run --source end-session"
    try:
        command = [sys.executable, str(EXEC / "session_closeout_intelligence.py"),
                   "run", "--source", "end-session"]
        if ctx.get("git_policy") == "codex-owned":
            command.append("--no-prune")
        content = ctx.get("content") or {}
        if content.get("source_path"):
            command.extend(["--state-file", content["source_path"]])
        r = subprocess.run(
            command,
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
    except Exception as e:
        degrade.degraded(None, "memory ledger unreadable — dedup keys incomplete, may double-write", e)
    return keys


def _memory_ledger_append(row: dict) -> None:
    try:
        SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
        with open(MEMORY_LEDGER, "a", encoding="utf-8") as f:
            f.write(json.dumps(row) + "\n")
    except Exception as e:
        degrade.degraded(None, "memory ledger append failed — this close may re-run its writes", e)


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


def step_notion_session_memory(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    """Queue an allow-listed closeout summary locally for explicit review.

    This step never contacts Notion. Network delivery belongs to the nightly
    mirror and is eligible only after an `approved` event.
    """
    content = ctx.get("content")
    if not content:
        return "SKIP", "no content source resolved (see resolve-handoff)"
    source_key = _dedup_key(content)
    if dry_run:
        return "OK", f"[dry-run] would queue Session Memory for review (key={source_key})"
    try:
        from notion_session_memory import queue_record  # noqa: E402

        row = queue_record(
            title=content["title"],
            key_decisions=content.get("completed") or "",
            pickup_prompt=content.get("remaining") or "",
            mode="Codex/Claude closeout",
            source_key=source_key,
        )
        suffix = "already queued" if row.get("duplicate") else "queued for review"
        return "OK", f"Session Memory {suffix} (key={row['key']})"
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
        content = ctx.get("content") or {}
        exact_source = Path(content["source_path"]) if content.get("source_path") else None
        source = exact_source if exact_source and exact_source.exists() else SESSION_STATE
        if not source.exists() or not source.read_text(encoding="utf-8").strip():
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
            return "OK", f"[dry-run] would archive {source.name} to .agent/sessions/state-archive/{dest.name}"

        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)
        return "OK", (f"archived exact source to .agent/sessions/state-archive/{dest.name} "
                      "(original left in place)")
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def _lane_helpers():
    """Import worktree_lane lazily (stdlib-only module, same dir)."""
    import sys as _sys
    _sys.path.insert(0, str(ROOT / "execution"))
    import worktree_lane as wl
    return wl


def _in_lane() -> bool:
    try:
        return _lane_helpers().is_lane(ROOT)
    except Exception as e:
        # False = "assume main tree" (the cautious default for the commit gate) —
        # but a broken lane detector is ledgered, not passed off as a measurement.
        return degrade.degraded(False, "lane detection failed — assuming main tree", e)


def step_commit_gate(ctx: Dict[str, Any], degraded: bool, dry_run: bool, git_policy: str = "legacy") -> Tuple[str, str]:
    """Commit gate (Farrice policy 2026-07-13, all-work-on-main): no session ends
    with silent uncommitted changes. Auto-commits the working tree with a session
    label (the post-commit hook then auto-pushes). Decline explicitly with
    END_SESSION_NO_AUTOCOMMIT=1 — the decline is logged, never silent. Born from
    docs/solutions/2026-07-13-divergent-branch-work-silently-lost.md.

    Lane-aware (2026-08-06): in a worktree lane, `add -A` is safe — single
    writer by construction. In MAIN with a fresh main-tree sibling session,
    `add -A` would sweep the sibling's in-flight edits into this commit (it
    happened 2026-08-04) — scope to this session's ledger paths instead, or
    skip loudly."""
    import os
    try:
        if git_policy == "codex-owned":
            return "SKIP", "Codex-owned Git gate runs after closeout through codex_end_session.py"
        if git_policy == "off":
            return "SKIP", "Git policy is off — no commit or push attempted"
        in_lane = _in_lane()
        r = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                           capture_output=True, text=True, timeout=15)
        dirty = [l for l in r.stdout.splitlines() if l.strip()]
        if not dirty:
            return "SKIP", "working tree clean — nothing to commit"
        if os.environ.get("END_SESSION_NO_AUTOCOMMIT") == "1":
            return "OK", f"DECLINED (env): {len(dirty)} changed files left uncommitted — logged, not silent"

        scope_note = ""
        add_cmd = ["git", "add", "-A"]
        label = "session"
        if in_lane:
            label = "lane"
        else:
            sibling = None
            try:
                wl = _lane_helpers()
                sibling = wl.fresh_main_writer(ROOT)
            except Exception:
                sibling = None
            if sibling:
                # Never sweep a sibling's tree. Scope to what THIS session produced.
                produced = _own_session_paths()
                if not produced:
                    return "OK", (f"SKIPPED add -A: fresh sibling on main ({sibling}) and no "
                                  f"session ledger to scope by — {len(dirty)} files left; commit "
                                  f"manually or re-run when the tree is quiet")
                add_cmd = ["git", "add", "--"] + produced
                scope_note = f" (scoped to {len(produced)} own paths; sibling: {sibling})"

        if dry_run:
            return "OK", f"[dry-run] would auto-commit {len(dirty)} changed files{scope_note}"
        subprocess.run(add_cmd, cwd=ROOT, capture_output=True, timeout=30)
        staged = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=ROOT,
                                capture_output=True, text=True, timeout=15)
        if not staged.stdout.strip():
            return "OK", f"nothing staged after scoping{scope_note} — no commit"
        msg = (f"chore({label}): end-session commit gate — {datetime.now().date().isoformat()}\n\n"
               "Auto-committed by the closeout spine so no work is left uncommitted\n"
               "(all-work-on-main policy, 2026-07-13).\n\n"
               "Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>")
        c = subprocess.run(["git", "commit", "-m", msg], cwd=ROOT,
                           capture_output=True, text=True, timeout=60)
        if c.returncode == 0:
            return "OK", f"auto-committed{scope_note or f' {len(dirty)} changed files'} (post-commit hook pushes)"
        return "FAIL", f"git commit failed: {(c.stderr or c.stdout)[:120]}"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def _own_session_paths() -> list:
    """Paths this session produced, from the newest session ledger, plus the
    handoff store — the safe commit scope when a sibling shares the main tree."""
    paths = []
    try:
        import os as _os
        sid = _os.environ.get("CLAUDE_SESSION_ID", "")
        own = (ROOT / ".agent" / "sessions" / f"ledger-{sid}.json") if sid else None
        if own and own.exists():
            ledgers = [own]
        else:
            ledgers = sorted((ROOT / ".agent" / "sessions").glob("ledger-*.json"),
                             key=lambda p: p.stat().st_mtime, reverse=True)
        if ledgers:
            data = json.loads(ledgers[0].read_text(encoding="utf-8"))
            for p in data.get("produced_paths", []) or data.get("files", []):
                if (ROOT / p).exists():
                    paths.append(p)
    except Exception as e:
        degrade.degraded(None, "session ledger unreadable — commit scope reduced to handoffs only", e)
    if (ROOT / ".agent" / "handoffs").exists():
        paths.append(".agent/handoffs")
    return paths


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


def step_projects_index(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    """Regenerate PROJECTS.md so a session that moved files leaves a correct map
    behind. Runs AFTER artifact-sweep for that reason. Cheap (~0.3s, one git
    call). The daily 06:00 audit is the deterministic backstop if this is skipped."""
    script = EXEC / "projects_index.py"
    if not script.exists():
        return "SKIP", "projects_index.py not present"
    if dry_run:
        return "OK", "[dry-run] would regenerate PROJECTS.md"
    try:
        r = subprocess.run(
            [sys.executable, str(script), "sync"],
            capture_output=True, text=True, timeout=60, cwd=str(ROOT),
        )
        last = (r.stdout or "").strip().splitlines()[-1:] or ["(no output)"]
        if r.returncode != 0:
            return "FAIL", f"exit {r.returncode} — {(r.stderr or '')[-160:]}"
        return "OK", last[0][:200]
    except subprocess.TimeoutExpired:
        return "FAIL", "timed out after 60s"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def step_artifact_sweep(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    """File unambiguous recent loose project-root artifacts into canonical
    subfolders (only-populated policy). Degraded-safe: project_filer sweep
    never throws and always exits 0, so a failure here never breaks closeout."""
    filer = EXEC / "project_filer.py"
    if not filer.exists():
        return "SKIP", "project_filer.py not present"
    if dry_run:
        return "OK", "[dry-run] would run project_filer.py sweep"
    try:
        # BOUNDED window on purpose. The watermark default (no --since-minutes)
        # widens to catch up after a gap, which can exceed this step's 60s budget
        # on a repo this size. Session close stays fast and handles today's files;
        # the daily 06:00 audit runs the unbounded catch-up. Both are wired, so
        # nothing is permanently invisible either way.
        r = subprocess.run(
            [sys.executable, str(filer), "sweep", "--since-minutes", "1440"],
            capture_output=True, text=True, timeout=60, cwd=str(ROOT),
        )
        out_lines = [ln for ln in (r.stdout or "").splitlines() if ln.strip()]
        last = out_lines[-1] if out_lines else "(no output)"
        if r.returncode != 0:
            return "FAIL", f"exit {r.returncode} — {last[:200]}"
        return "OK", last[:200]
    except subprocess.TimeoutExpired:
        return "FAIL", "timed out after 60s"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def step_session_guide(ctx: Dict[str, Any], degraded: bool, dry_run: bool, slug: str) -> Tuple[str, str]:
    """Operator-guide library (Farrice 2026-07-13, binding): every meaningful
    session files a scannable document in guides/ — a full OPERATOR GUIDE when
    the session shipped operator assets (skills/workflows/execution/directives),
    a SESSION BRIEF otherwise. This deterministic half writes a stub so coverage
    never depends on the model remembering (AI-memory-dependent observability is
    banned); the /end-session model half enriches the stub to the
    docs/ROOT-CORE-OPERATOR-GUIDE.md format (the Matt Pocock exemplar: mental
    model up top, per-capability sections — what it is / when to reach for it /
    when NOT to / worked examples / honest edges) and updates guides/INDEX.md."""
    try:
        today = datetime.now().date().isoformat()
        content = ctx.get("content") or {}
        # Empty slug must never produce a blank filename (guides/YYYY-MM-DD-.md):
        # fall back to the stub's title, then to a fixed sentinel.
        safe_slug = re.sub(r"[^a-z0-9]+", "-", (slug or "").lower()).strip("-")
        if not safe_slug:
            title_src = (content.get("title") or "").lower()
            safe_slug = re.sub(r"[^a-z0-9]+", "-", title_src)[:60].strip("-") or "unnamed-session"
        guide_path = GUIDES_DIR / f"{today}-{safe_slug}.md"
        rel = guide_path.relative_to(ROOT)
        if guide_path.exists():
            if "status: stub" in guide_path.read_text(encoding="utf-8"):
                return "OK", f"stub awaiting enrichment: {rel} — enrich to full guide + update guides/INDEX.md"
            return "OK", f"session guide filed: {rel}"

        # Tier detection: operator assets changed since the last guide-sync stamp?
        assets: list = []
        try:
            r = subprocess.run(
                [sys.executable, str(EXEC / "operator_guide_sync.py"), "check"],
                capture_output=True, text=True, timeout=30, cwd=str(ROOT),
            )
            if r.returncode == 1:
                for ln in (r.stdout or "").splitlines():
                    t = ln.strip()
                    if t.startswith("- "):
                        assets.append(t[2:])
        except Exception as e:
            degrade.degraded(None, "operator_guide_sync check failed — guide tier may downgrade to brief", e)

        if not assets and not content:
            return "SKIP", "conversational session — no guide or brief needed"

        tier = "operator-guide" if assets else "session-brief"
        if dry_run:
            return "OK", f"[dry-run] would write {tier} stub → {rel}"

        GUIDES_DIR.mkdir(exist_ok=True)
        title = content.get("title") or safe_slug.replace("-", " ").title()
        completed = content.get("completed") or ""
        remaining = content.get("remaining") or ""
        asset_lines = "\n".join(f"- `{a}`" for a in assets[:40]) or "- (none detected)"
        stub = (
            f"---\n"
            f"date: {today}\n"
            f"session: {safe_slug}\n"
            f"tier: {tier}\n"
            f"status: stub  # written deterministically by end_session_closeout.py — ENRICH to the\n"
            f"              # docs/ROOT-CORE-OPERATOR-GUIDE.md format, then set status: enriched\n"
            f"---\n\n"
            f"# {title} — What We Built {today} and How to Use It\n\n"
            f"> STUB — auto-filed by the closeout spine so this session is never uncovered.\n"
            f"> Enrich per guides/FORMAT.md (exemplar: docs/ROOT-CORE-OPERATOR-GUIDE.md): 10-line\n"
            f"> payload block, command table, mental model, per-capability sections with honest\n"
            f"> edges. Update guides/INDEX.md and stamp operator_guide_sync.py record.\n\n"
            f"## Session snapshot\n\n"
            f"- **Completed:** {completed or '(see session state archive)'}\n"
            f"- **Remaining:** {remaining or '(none recorded)'}\n\n"
            f"## Operator assets changed this cycle ({len(assets)})\n\n{asset_lines}\n"
        )
        guide_path.write_text(stub, encoding="utf-8")

        if GUIDES_INDEX.exists():
            idx = GUIDES_INDEX.read_text(encoding="utf-8")
            marker = "## Pending enrichment"
            line = f"- [{today} — {title}]({guide_path.name}) — {tier} stub, needs enrichment"
            if guide_path.name not in idx:
                if marker in idx:
                    idx = idx.replace(marker, f"{marker}\n{line}", 1)
                else:
                    idx = idx.rstrip() + f"\n\n{marker}\n{line}\n"
                GUIDES_INDEX.write_text(idx, encoding="utf-8")

        return "OK", f"{tier} STUB written → {rel} — enrich before closing (exemplar: docs/ROOT-CORE-OPERATOR-GUIDE.md)"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def step_mission_briefs(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    """Build mission briefs from the latest sweep bundle.

    Reads .agent/sweep/latest.json (or most recent sweep-<date>.json) and
    generates living briefs for each promoted thread in deliverables/research-briefs/mission-<slug>/.
    Updates briefs in place so sessions append to the timeline section.

    Skipped if sweep unavailable or degraded mode.
    """
    if degraded:
        return "SKIP", "degraded mode — sweep infrastructure unavailable"

    try:
        # Check if sweep bundle exists
        sweep_dir = ROOT / ".agent" / "sweep"
        if not sweep_dir.exists():
            return "SKIP", "no sweep data — run session_sweep.py first"

        if dry_run:
            # Count what would be built
            briefs_dir = ROOT / "deliverables" / "research-briefs"
            count = 0
            if briefs_dir.exists():
                count = len([d for d in briefs_dir.iterdir() if d.is_dir() and d.name.startswith("mission-")])
            return "OK", f"[dry-run] would build ~{count} mission briefs"

        # Run mission_brief.py build --all
        import subprocess
        r = subprocess.run(
            [sys.executable, str(EXEC / "mission_brief.py"), "build", "--all"],
            capture_output=True, text=True, timeout=120, cwd=str(ROOT),
        )
        if r.returncode != 0:
            return "SKIP", f"mission-brief failed: check sweep data"

        # Count briefs
        briefs_dir = ROOT / "deliverables" / "research-briefs"
        count = len([d for d in briefs_dir.iterdir() if d.is_dir() and d.name.startswith("mission-")])
        if count == 0:
            return "SKIP", "no promoted threads"

        # Also build mission-board
        subprocess.run(
            [sys.executable, str(EXEC / "mission_brief.py"), "build-board"],
            capture_output=True, text=True, timeout=30, cwd=str(ROOT),
        )

        return "OK", f"mission briefs: {count} threads + mission-board"
    except Exception as e:
        return "SKIP", f"mission-brief error: {e}"


def step_menu_parity(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    """Make everything this session built actually fireable (Arsenal Loop,
    2026-07-25).

    A workflow written into skills/<skill>/workflows/ is invisible until a
    wrapper + shim exist, and that minting was a MANUAL step for months — 728
    workflows accumulated unfireable. Heartbeat check 7 detects the drift;
    detection alone cannot fix a minting gap, so this step MINTS. It never
    blocks: a closeout that fails because of housekeeping is a closeout that
    gets skipped.

    Index regeneration is best-effort and separately reported — a minted
    command already fires from .claude/commands/ whether or not the markdown
    indexes got refreshed.
    """
    try:
        r = subprocess.run(
            [sys.executable, str(EXEC / "mint_menu_wrappers.py"), "--scope", "all", "--apply"],
            capture_output=True, text=True, timeout=240, cwd=str(ROOT),
        ) if not dry_run else None
        if dry_run:
            d = subprocess.run(
                [sys.executable, str(EXEC / "mint_menu_wrappers.py"), "--scope", "all", "--dry-run"],
                capture_output=True, text=True, timeout=240, cwd=str(ROOT),
            )
            first = next((ln for ln in (d.stdout or "").splitlines() if ln.strip()), "(no output)")
            return "SKIP", f"dry-run — {first[:180]}"
        if r.returncode != 0:
            err = [ln for ln in (r.stderr or "").splitlines() if ln.strip()]
            return "FAIL", f"exit {r.returncode} — {(err[-1] if err else '')[:200]}"

        minted_line = next((ln for ln in (r.stdout or "").splitlines() if ln.startswith("MINTED")),
                           "MINTED 0 file(s)")
        minted = int(re.search(r"MINTED (\d+)", minted_line).group(1)) if "MINTED" in minted_line else 0

        idx_note = ""
        if minted:
            for script in ("sync_registries.py", "generate_slash_commands.py"):
                try:
                    g = subprocess.run([sys.executable, str(EXEC / script)],
                                       capture_output=True, text=True, timeout=180, cwd=str(ROOT))
                    if g.returncode != 0:
                        idx_note += f" · {script} exit {g.returncode}"
                except Exception as e:
                    idx_note += f" · {script} {type(e).__name__}"
            idx_note = idx_note or " · indexes refreshed"

        remaining = 0
        try:
            dr = subprocess.run([sys.executable, str(EXEC / "arsenal_index.py"), "drift", "--json"],
                                capture_output=True, text=True, timeout=120, cwd=str(ROOT))
            remaining = int(json.loads(dr.stdout).get("total", 0))
        except Exception:
            remaining = -1

        try:
            rec = {"ts": _now_iso(), "source": "end-session", "minted": minted,
                   "remaining_drift": max(remaining, 0)}
            path = SESSIONS_DIR / "menu-parity.jsonl"
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(rec) + "\n")
        except Exception as e:
            degrade.degraded(None, "menu-parity receipt append failed — minting still done, receipt lost", e)

        if not minted:
            return "OK", ("nothing new to mint — everything built is fireable"
                          if remaining == 0 else
                          f"nothing minted; {remaining} pre-existing unreachable workflow(s) remain")
        return "OK", (f"minted {minted} file(s){idx_note}"
                      + (f" · {remaining} still unreachable" if remaining > 0 else " · parity clean"))
    except subprocess.TimeoutExpired:
        return "FAIL", "mint timed out (240s) — run mint_menu_wrappers.py --scope all --apply by hand"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def step_self_heal(ctx: Dict[str, Any], degraded: bool, dry_run: bool,
                   mutation_allowed: bool = True) -> Tuple[str, str]:
    """PRIMARY healing path (Farrice, 2026-07-27, binding).

    "When I run the end session or close out a session, self-heal should run as
    a backup just in case. If there are any errors or issues or failure points
    within that session, it sweeps the session and then heals in that moment.
    That way it's not something waiting to get healed later that day or the
    week, at a timetable interval that is inconvenient if I'm creating at speed."

    So this — not the 06:45 job — is where repairs happen. The daily brief was
    demoted to observation-only the same day. A failure produced in a session
    gets swept and repaired in that session, and `failure_learning.py` (invoked
    inside the heal path) turns any recurrence into a written prevention rule,
    so the same failure cannot quietly return.

    Runs FIRST in the spine, before `commit-gate`, with `--no-commit` — the
    commit gate then sweeps the repairs into the one session commit instead of
    self-heal minting a second. Never blocks: a heal that fails or times out
    degrades to a reported line and the closeout continues.
    """
    if not mutation_allowed:
        if dry_run:
            return "OK", "[dry-run] would scan self-heal findings into the Codex review queue"
        try:
            r = subprocess.run(
                [sys.executable, str(ROOT / "execution" / "self_heal.py"),
                 "report", "--json", "--no-cache"],
                cwd=ROOT, capture_output=True, text=True, timeout=180,
            )
            findings = json.loads(r.stdout or "[]") if r.returncode == 0 else []
            ctx["self_heal_findings"] = findings
            if r.returncode != 0:
                return "FAIL", f"self-heal report failed: {(r.stderr or r.stdout)[-180:]}"
            return "OK", f"{len(findings)} finding(s) captured for review; no automatic mutation"
        except (subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
            return "FAIL", f"self-heal review scan failed: {type(exc).__name__}"
    if dry_run:
        return "OK", "[dry-run] would sweep this session and apply AUTO/EVIDENCE repairs"
    try:
        r = subprocess.run(
            [sys.executable, str(ROOT / "execution" / "self_heal.py"), "heal", "--no-commit"],
            cwd=ROOT, capture_output=True, text=True, timeout=420)
        out = (r.stdout or "") + (r.stderr or "")
        healed = out.count("[FIXED]")
        failed = out.count("[COULD NOT FIX]")
        m = re.search(r"(\d+) need your judgment", out)
        judgment = int(m.group(1)) if m else 0
        learned = ""
        try:
            lp = subprocess.run(
                [sys.executable, str(ROOT / "execution" / "failure_learning.py")],
                cwd=ROOT, capture_output=True, text=True, timeout=60)
            lm = re.search(r"(\d+) rule\(s\) written", lp.stdout or "")
            if lm:
                learned = f" · {lm.group(1)} prevention rule(s) learned"
        except Exception as e:
            degrade.degraded(None, "failure_learning.py run failed — no prevention rules this close", e)
        parts = []
        if healed:
            parts.append(f"{healed} repaired")
        if failed:
            parts.append(f"{failed} could not be fixed")
        if judgment:
            parts.append(f"{judgment} need judgment (surfaced at next session open)")
        return "OK", (("; ".join(parts) if parts else "nothing to heal — session closed clean")
                      + learned)
    except subprocess.TimeoutExpired:
        return "FAIL", "self-heal timed out (420s) — run `python3 execution/self_heal.py heal` by hand"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


def step_lane_merge(ctx: Dict[str, Any], degraded: bool, dry_run: bool) -> Tuple[str, str]:
    """LAST step, lane-only (2026-08-06 lanes build): auto-merge-when-clean.
    worktree_lane.py merge re-seals first, so files written by the intermediate
    closeout steps are captured; on conflict it PARKS the branch and surfaces
    one line — never silent loss. Its final act removes this worktree, which is
    why nothing may run after this step. Decline: END_SESSION_NO_AUTOMERGE=1."""
    import os, sys as _sys
    if not _in_lane():
        return "SKIP", "main tree — no lane to merge"
    if os.environ.get("END_SESSION_NO_AUTOMERGE") == "1":
        return "OK", "DECLINED (env): lane left in place — logged, not silent; " \
                     "merge later: python3 execution/worktree_lane.py merge"
    if dry_run:
        return "OK", "[dry-run] would run worktree_lane.py merge (seal -> gate -> merge -> teardown)"
    try:
        r = subprocess.run([_sys.executable, str(ROOT / "execution" / "worktree_lane.py"),
                            "merge"], capture_output=True, text=True, timeout=600,
                           cwd=str(ROOT))
        out = (r.stdout or "").strip().splitlines()
        last = out[-1] if out else "(no output)"
        if r.returncode == 0:
            return "OK", last
        return "FAIL", f"{last} — stderr: {(r.stderr or '')[:120]}"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"


# ─────────────────────────────────────────────────────────────
# spine runner
# ─────────────────────────────────────────────────────────────

def run(slug: str, degraded: bool, dry_run: bool,
        handoff_path: Optional[Path] = None, git_policy: str = "legacy") -> int:
    ctx: Dict[str, Any] = {"handoff_path": handoff_path, "git_policy": git_policy}
    codex_owned = git_policy == "codex-owned"
    steps = [
        # self-heal runs BEFORE commit-gate so its repairs land in the session's
        # own commit rather than a second one (see step_self_heal docstring).
        ("self-heal", lambda: step_self_heal(ctx, degraded, dry_run, not codex_owned)),
        ("commit-gate", lambda: step_commit_gate(ctx, degraded, dry_run, git_policy)),
        ("resolve-handoff", lambda: step_resolve_handoff(ctx, degraded, dry_run)),
        ("closeout-intelligence", lambda: step_closeout_intelligence(ctx, degraded, dry_run)),
        ("memory-bridge", lambda: step_memory_bridge(ctx, degraded, dry_run)),
        ("notion-session-memory", lambda: step_notion_session_memory(ctx, degraded, dry_run)),
        ("cos-journal", lambda: step_cos_journal(ctx, degraded, dry_run)),
        ("archive-session-state", lambda: step_archive_session_state(ctx, degraded, dry_run, slug)),
        ("session-guide", lambda: step_session_guide(ctx, degraded, dry_run, slug)),
        ("mission-briefs", lambda: step_mission_briefs(ctx, degraded, dry_run)),
        ("artifact-sweep", lambda: (
            ("SKIP", "Codex organization is manifest-scoped in codex_end_session.py")
            if codex_owned else step_artifact_sweep(ctx, degraded, dry_run)
        )),
        ("projects-index", lambda: (
            ("SKIP", "Codex closeout does not rewrite unrelated project indexes")
            if codex_owned else step_projects_index(ctx, degraded, dry_run)
        )),
        ("menu-parity", lambda: (
            ("SKIP", "Codex closeout does not regenerate broad command indexes")
            if codex_owned else step_menu_parity(ctx, degraded, dry_run)
        )),
        ("friction-nudge", lambda: step_friction_nudge(ctx, degraded, dry_run)),
        ("finalize-debt-nudge", lambda: step_finalize_debt_nudge(ctx, degraded, dry_run)),
        ("solution-cards", lambda: step_solution_cards(ctx, degraded, dry_run)),
        # LAST by contract: its final act removes the worktree this process
        # may be running in — nothing can run after it (lanes build 2026-08-06).
        ("lane-merge", lambda: step_lane_merge(ctx, degraded, dry_run)),
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
    rp.add_argument("--handoff", default="", help="Exact stored handoff path; disables newest-handoff fallback")
    rp.add_argument("--git-policy", choices=("legacy", "codex-owned", "off"), default="legacy",
                    help="Legacy auto-commit, Codex coordinator-owned Git, or no Git mutation")
    rp.add_argument("--degraded", action="store_true", help="Run in degraded mode (SessionEnd-hook backstop path)")
    rp.add_argument("--dry-run", action="store_true", help="Perform reads and print intent; write nothing")
    args = ap.parse_args()

    if args.command == "run":
        try:
            handoff_path = Path(args.handoff).expanduser() if args.handoff else None
            return run(args.slug, args.degraded, args.dry_run, handoff_path, args.git_policy)
        except Exception as e:
            # Was: "CLOSEOUT SPINE COMPLETE (0 ok, 0 skip, 1 fail) — fatal: ..."
            # It LED WITH THE WORD COMPLETE on a fatal crash, so anything
            # grepping for COMPLETE (or checking $?) recorded a success, and the
            # last line a human sees at end-of-session said the spine finished.
            # exit 0 is kept deliberately — launchd and the SessionEnd hook must
            # not be broken by a closeout failure (Compass Doctrine) — but the
            # MESSAGE now tells the truth. Non-blocking is not the same as quiet.
            print(f"CLOSEOUT SPINE FAILED — nothing completed. "
                  f"fatal: {type(e).__name__}: {e}", file=sys.stderr)
            print("CLOSEOUT SPINE FAILED (0 ok, 0 skip, 1 fail) — "
                  "rerun: python3 execution/end_session_closeout.py run")
            return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
