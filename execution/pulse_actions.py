#!/usr/bin/env python3
"""pulse_actions.py — deterministic writers behind the Pulse board's live
actions (Readout OS phase 4, 2026-08-06). Importable + CLI; every action is a
small, honest append/edit that a session could equally type by hand.

Actions:
    done <slug> --outcome "..."          append done line to .agent/missions.jsonl
    park <slug> --reason "..."           append stopped line (+ annotate handoff if one exists)
    outcome "<full deliverable>" --revenue N --outcome "..."   → revenue_tracker log
    outcome-dismiss "<full deliverable>"                       → log --type archived-no-data
    outcome-snooze "<full deliverable>"                        check_in_date +14d (atomic)
    thread-archive <thread>                                    → handoff_store archive

    refresh                              re-collect ledgers (sweep + asset index) then regen boards

Contracts: mission line schema per .agent/workflows/go.md Stage 2.5; append
style per raw_intent_run_packet._log_mission (json.dumps + newline, never
blocks on OSError). Revenue numbers are NEVER invented — they arrive from
Farrice via the board form; absent revenue logs 0 per tracker default.
"""
import argparse
import datetime
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MISSIONS = os.path.join(ROOT, ".agent", "missions.jsonl")
OUTCOMES = os.path.join(ROOT, ".agent", "revenue-outcomes.json")
PY = sys.executable or "python3"


def _now():
    return datetime.datetime.now().isoformat(timespec="seconds")


def _latest_mission(slug):
    """Latest record for a slug (or normalized-title key) from missions.jsonl."""
    latest = None
    try:
        for line in open(MISSIONS, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            try:
                m = json.loads(line)
            except ValueError:
                continue
            key = m.get("slug") or " ".join((m.get("mission") or "?").split())
            if key == slug:
                latest = m
    except OSError:
        pass
    return latest


def _append_mission(line):
    try:
        with open(MISSIONS, "a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
        return True
    except OSError as e:
        print(f"[pulse_actions] ERROR appending mission line: {e}", file=sys.stderr)
        return False


def _close_line(slug, status, outcome):
    prev = _latest_mission(slug) or {}
    return {
        "ts": _now(),
        "mission": prev.get("mission") or slug,
        "slug": prev.get("slug") or slug,
        "serves": prev.get("serves") or "orphan",
        "pattern": prev.get("pattern"),
        "tier": prev.get("tier"),
        "status": status,
        "expected_spawns": prev.get("expected_spawns"),
        "measured_spawns": prev.get("measured_spawns"),
        "verdict": None,
        "outcome": outcome,
    }


def act_done(slug, outcome):
    line = _close_line(slug, "done", outcome or "closed from pulse board")
    ok = _append_mission(line)
    if ok:
        print(f"done: {slug} — {line['outcome']}")
    return ok


def act_reopen(slug):
    """Inverse of done/park — appends a compiled line so the mission re-enters
    the open set (open = status in compiled/running per pulse_dashboard)."""
    prev = _latest_mission(slug) or {}
    line = _close_line(slug, "compiled",
                       f"REOPENED from pulse board (was {prev.get('status') or 'closed'})")
    ok = _append_mission(line)
    if ok:
        print(f"reopened: {slug}")
    return ok


def act_park(slug, reason):
    reason = reason or "parked from pulse board"
    line = _close_line(slug, "stopped",
                       f"PARKED: {reason}. Resume: /resume {slug}")
    ok = _append_mission(line)
    if not ok:
        return False
    # If a handoff thread by this name exists, mark it PARKED with the reason.
    # Was "blocked" — which ranks rank-0 most-urgent in why_needs_you, so every
    # parked thread shouted from the top of needs-you (bug, fixed 2026-08-20).
    try:
        r = subprocess.run(
            [PY, os.path.join(ROOT, "execution", "handoff_store.py"),
             "annotate", slug, "--status", "parked", "--hint", reason],
            capture_output=True, text=True, timeout=20)
        if r.returncode == 0:
            print(f"parked: {slug} (handoff annotated blocked)")
        else:
            print(f"parked: {slug} (no matching handoff thread — mission line only)")
    except Exception:
        print(f"parked: {slug} (handoff annotate skipped)")
    return True


def act_kill(slug, reason):
    """Kill = dead + hidden (Farrice's ruling, 2026-08-20). Appends a terminal
    `killed` line to the append-only ledger (never a delete) and archives the
    handoff thread so it stops surfacing on boards and in sweep promotion.
    Recoverable only by digging: `reopen` + `handoff_store.py unarchive`.
    A reason is REQUIRED — a kill with no reason is a decision with no record."""
    reason = (reason or "").strip()
    if not reason:
        print("[pulse_actions] kill refused: --reason is required", file=sys.stderr)
        return False
    line = _close_line(slug, "killed", f"KILLED: {reason}")
    if not _append_mission(line):
        return False
    try:
        r = subprocess.run(
            [PY, os.path.join(ROOT, "execution", "handoff_store.py"), "archive", slug],
            capture_output=True, text=True, timeout=20)
        note = "handoff archived" if r.returncode == 0 else "no matching handoff thread"
    except Exception:
        note = "handoff archive skipped"
    print(f"killed: {slug} ({note}) — {reason}")
    return True


def act_outcome(deliverable, revenue, outcome, kind=None):
    cmd = [PY, os.path.join(ROOT, "execution", "revenue_tracker.py"), "log",
           deliverable, "--revenue", str(revenue or 0), "--outcome", outcome or ""]
    if kind:
        cmd += ["--type", kind]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    out = (r.stdout or "").strip() or (r.stderr or "").strip()
    print(out[-400:] if out else f"logged: {deliverable[:60]}")
    return r.returncode == 0


def act_outcome_dismiss(deliverable):
    return act_outcome(deliverable, 0,
                       "no outcome expected (dismissed from pulse board)",
                       kind="archived-no-data")


def act_outcome_snooze(deliverable, days=14):
    try:
        data = json.load(open(OUTCOMES, encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"[pulse_actions] ERROR reading outcomes: {e}", file=sys.stderr)
        return False
    hit = None
    dl = deliverable.strip().lower()
    for o in data.get("outcomes", []):
        if o.get("outcome_type") == "pending" and (o.get("deliverable") or "").strip().lower() == dl:
            hit = o
            break
    if hit is None:  # containment fallback, first pending match (tracker's own rule)
        for o in data.get("outcomes", []):
            od = (o.get("deliverable") or "").strip().lower()
            if o.get("outcome_type") == "pending" and (dl in od or od in dl):
                hit = o
                break
    if hit is None:
        print(f"[pulse_actions] no pending entry matches: {deliverable[:80]}", file=sys.stderr)
        return False
    base = hit.get("check_in_date") or datetime.date.today().isoformat()
    try:
        base_d = datetime.date.fromisoformat(base)
    except ValueError:
        base_d = datetime.date.today()
    new_date = max(base_d, datetime.date.today()) + datetime.timedelta(days=days)
    hit["check_in_date"] = new_date.isoformat()
    data["last_updated"] = _now()
    tmp = OUTCOMES + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, OUTCOMES)
    print(f"snoozed to {hit['check_in_date']}: {hit['deliverable'][:70]}")
    return True


def act_thread_archive(thread):
    r = subprocess.run(
        [PY, os.path.join(ROOT, "execution", "handoff_store.py"), "archive", thread],
        capture_output=True, text=True, timeout=20)
    out = (r.stdout or "").strip() or (r.stderr or "").strip()
    print(out[-200:] if out else f"archived: {thread}")
    return r.returncode == 0


def act_refresh():
    """Re-collect the data every board reads, then regenerate the hub surfaces.
    Order matters: ledgers first (sweep, asset index), boards last — the
    homebase regen flips /ping's homebase_mtime, which is the open page's
    signal that the data is actually fresh. Synchronous and honest here; the
    server wraps this CLI in a detached Popen so the button returns instantly."""
    steps = [
        ("session sweep", ["session_sweep.py", "run"], 600),
        ("asset index", ["asset_index.py"], 300),
        ("mission briefs", ["mission_brief.py", "build", "--quiet"], 300),
        ("homebase", ["homebase_board.py"], 90),
    ]
    all_ok = True
    for label, cmd, timeout in steps:
        try:
            r = subprocess.run([PY, os.path.join(ROOT, "execution", cmd[0]), *cmd[1:]],
                               capture_output=True, text=True, timeout=timeout)
            ok = r.returncode == 0
        except Exception as e:
            print(f"[pulse_actions] refresh {label} crashed: {e}", file=sys.stderr)
            ok = False
        print(f"refresh {label}: {'ok' if ok else 'FAILED'}")
        all_ok = all_ok and ok
    return all_ok


def act_oracle_closes():
    """Capture closing lines for pending paper bets (Oracle board button)."""
    r = subprocess.run([PY, os.path.join(ROOT, "execution", "paper_trader.py"), "closes"],
                       capture_output=True, text=True, timeout=120)
    out = (r.stdout or "").strip() or (r.stderr or "").strip()
    print(out[-300:] if out else "closes: done")
    return r.returncode == 0


def act_oracle_gate():
    """Run the graduation gate check; verdict lands in the regenerated board."""
    r = subprocess.run([PY, os.path.join(ROOT, "execution", "live_trader.py"), "check"],
                       capture_output=True, text=True, timeout=60)
    out = (r.stdout or "").strip()
    for line in out.splitlines():
        if "VERDICT" in line:
            print(line.strip())
    return r.returncode == 0


def act_oracle_note(text):
    """Drop a note into the event inbox; the listener mints the mission card."""
    text = (text or "").strip()
    if not text:
        print("[pulse_actions] empty note refused", file=sys.stderr)
        return False
    inbox = os.path.join(ROOT, ".agent", "inbox")
    os.makedirs(inbox, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%H%M%S")
    path = os.path.join(inbox, f"oracle-note-{stamp}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"note dropped: {os.path.basename(path)} (card mints on next listener poll)")
    return True


def main():
    ap = argparse.ArgumentParser(description="Pulse board action writers.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("done"); d.add_argument("slug"); d.add_argument("--outcome", default="")
    p = sub.add_parser("park"); p.add_argument("slug"); p.add_argument("--reason", default="")
    r = sub.add_parser("reopen"); r.add_argument("slug")
    k = sub.add_parser("kill"); k.add_argument("slug"); k.add_argument("--reason", default="")
    o = sub.add_parser("outcome"); o.add_argument("deliverable")
    o.add_argument("--revenue", type=float, default=0); o.add_argument("--outcome", default="")
    x = sub.add_parser("outcome-dismiss"); x.add_argument("deliverable")
    s = sub.add_parser("outcome-snooze"); s.add_argument("deliverable"); s.add_argument("--days", type=int, default=14)
    t = sub.add_parser("thread-archive"); t.add_argument("thread")
    sub.add_parser("refresh")
    sub.add_parser("oracle-closes")
    sub.add_parser("oracle-gate")
    n = sub.add_parser("oracle-note"); n.add_argument("text")
    a = ap.parse_args()
    ok = {
        "done": lambda: act_done(a.slug, a.outcome),
        "park": lambda: act_park(a.slug, a.reason),
        "reopen": lambda: act_reopen(a.slug),
        "kill": lambda: act_kill(a.slug, a.reason),
        "outcome": lambda: act_outcome(a.deliverable, a.revenue, a.outcome),
        "outcome-dismiss": lambda: act_outcome_dismiss(a.deliverable),
        "outcome-snooze": lambda: act_outcome_snooze(a.deliverable, a.days),
        "thread-archive": lambda: act_thread_archive(a.thread),
        "refresh": act_refresh,
        "oracle-closes": act_oracle_closes,
        "oracle-gate": act_oracle_gate,
        "oracle-note": lambda: act_oracle_note(a.text),
    }[a.cmd]()
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
