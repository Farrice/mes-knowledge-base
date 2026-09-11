#!/usr/bin/env python3
"""
eli5_state.py — the collector behind /eli5 ("explain it to me like a fifth grader").

WHY THIS EXISTS. /eli5 must READ real state and never guess. A markdown workflow
alone drifts: the narrator starts summarising from memory. So every fact the
narration may use is gathered here, deterministically, with a `source` on each
item, and the narrator (Claude or Codex) only rephrases what this prints.

UNKNOWN IS NOT PASS. A feed that cannot be read lands in `unavailable[]` with a
plain reason. It is never rendered as zero, never as "clean". (Scar:
pulse_dashboard.py prints "OPEN MISSIONS: none" when .agent/missions.jsonl is
simply missing.)

READ-ONLY. This script writes nothing. It shells out only to commands that are
themselves read-only (git status/log, self_heal.py report --json,
job_board.py status --all when present).

Usage:
    python3 execution/eli5_state.py [--scope here|jobs|all] [--json] [--render]
                                    [--root DIR] [--limit N]

    --scope here   this lane: session-state, git, handoffs on this branch
    --scope jobs   every open thread/mission/decision across the repo
    --scope all    both (default)
    --json         print the fact bundle (what the narrator reads)
    --render       print the markdown blocks (table / A-vs-B) for a terminal seat
    --root DIR     read every feed from DIR instead of the repo (sabotage/empty test)
    --limit N      cap pieces per bucket (default 8)

Feeds (all optional, each reported when missing):
    .agent/session-state.md · git · .agent/handoffs/*.md (frontmatter) ·
    .agent/sweep/latest.json (threads, missions, last_active) ·
    .agent/sweep/synthesis.json (plain-English ledes) · .agent/cos/goals.json ·
    .agent/cos/decisions.md (Status: OPEN entries + due dates) ·
    .agent/missions/<slug>/{contract.json,mission.json} · .agent/mission-queue/{pending,parked} ·
    execution/self_heal.py report --json · execution/job_board.py status --all (probe)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import warnings
from datetime import date, datetime
from pathlib import Path

warnings.filterwarnings("ignore")  # brief_library.py:381 SyntaxWarning noise on import

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))

STATES = ("done", "working", "stuck", "waiting_on_you")
STALE_DAYS = 7
DEFAULT_LIMIT = 8

# ── helpers ─────────────────────────────────────────────────────────────


def _today() -> date:
    return datetime.now().date()


def _days_since(s: str | None) -> int | None:
    if not s:
        return None
    try:
        return (_today() - datetime.fromisoformat(str(s)[:19]).date()).days
    except ValueError:
        try:
            return (_today() - datetime.strptime(str(s)[:10], "%Y-%m-%d").date()).days
        except ValueError:
            return None


def _dur(days: int | None) -> str:
    if days is None:
        return "an unknown time"
    if days <= 0:
        return "less than a day"
    return f"{days} day{'s' if days != 1 else ''}"


def _age(days: int | None) -> str:
    if days is None:
        return "no date"
    if days <= 0:
        return "today"
    return f"{_dur(days)} ago"


def _one_line(s: str, n: int = 140) -> str:
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def _run(cmd: list[str], cwd: Path, timeout: int = 40) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=timeout,
                           env={**os.environ, "PYTHONWARNINGS": "ignore"})
        return p.returncode, p.stdout
    except (OSError, subprocess.TimeoutExpired) as e:
        return 1, f"__error__ {e}"


class Bundle:
    def __init__(self, root: Path, limit: int):
        self.root = root
        self.limit = limit
        self.doing_and_why: dict = {}
        self.pieces: list[dict] = []
        self.decisions: list[dict] = []
        self.deadlines: list[dict] = []
        self.unavailable: list[dict] = []
        self.notes: list[str] = []
        self.counts: dict = {}

    def missing(self, feed: str, why: str):
        if any(u["feed"] == feed for u in self.unavailable):
            return
        self.unavailable.append({"feed": feed, "why": why})

    def piece(self, name, state, reason, source, **extra):
        assert state in STATES, state
        self.pieces.append({"name": _one_line(name, 90), "state": state,
                            "reason": _one_line(reason), "source": source, **extra})

    def decision(self, question, source, options=None, hint=""):
        self.decisions.append({"question": _one_line(question, 200), "options_in_source": options or [],
                               "hint": _one_line(hint), "source": source})

    def to_dict(self) -> dict:
        return {
            "generated": datetime.now().isoformat(timespec="seconds"),
            "root": str(self.root),
            "doing_and_why": self.doing_and_why,
            "pieces": self.pieces,
            "decisions": self.decisions,
            "deadlines": self.deadlines,
            "counts": self.counts,
            "unavailable": self.unavailable,
            "notes": self.notes,
            "empty": not (self.pieces or self.decisions),
        }


# ── feeds: here ─────────────────────────────────────────────────────────


def feed_session_state(b: Bundle):
    p = b.root / ".agent" / "session-state.md"
    if not p.exists():
        return b.missing(".agent/session-state.md", "file is not there")
    text = p.read_text(encoding="utf-8", errors="replace")
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    heads = [l.lstrip("# ").strip() for l in lines if l.startswith("#")]
    body = [l for l in lines if not l.startswith("#")]
    b.doing_and_why["session_state_title"] = heads[0] if heads else ""
    b.doing_and_why["session_state_first_lines"] = [_one_line(l) for l in body[:4]]
    b.doing_and_why["session_state_source"] = ".agent/session-state.md"
    if len(lines) <= 3:
        b.notes.append("session-state.md is a fresh-lane stub (nothing recorded yet)")


def feed_git(b: Bundle):
    if not (b.root / ".git").exists():
        return b.missing("git", "no git repo at root")
    rc, branch = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"], b.root)
    if rc != 0:
        return b.missing("git", "git rev-parse failed")
    branch = branch.strip()
    _, status = _run(["git", "status", "--short"], b.root)
    _, log = _run(["git", "log", "-5", "--format=%h %s"], b.root)
    dirty = [l for l in status.splitlines() if l.strip()]
    commits = [_one_line(l, 110) for l in log.splitlines() if l.strip()]
    b.doing_and_why["branch"] = branch
    b.doing_and_why["uncommitted_files"] = len(dirty)
    b.doing_and_why["recent_commits"] = commits[:3]
    b.doing_and_why["git_source"] = "git status --short · git log -5"
    if commits:
        b.piece(f"latest commit on {branch}", "done", commits[0], "git log -1")
    if dirty:
        b.piece(f"{len(dirty)} changed file(s) not committed on {branch}", "working",
                "edits in progress in this lane", "git status --short")


def feed_lane_handoffs(b: Bundle, branch: str):
    """Handoffs whose frontmatter names this branch (the lane's own threads)."""
    store = b.root / ".agent" / "handoffs"
    if not store.exists():
        return  # reported by feed_handoffs
    try:
        import handoff_store as hs
    except Exception as e:  # noqa: BLE001
        return b.missing("handoff_store import", str(e))
    for p in hs._files(store):
        m = hs.read_meta(p)
        if m.get("branch") and m["branch"] == branch and m["status"] != "done":
            b.piece(m["thread"], _state_from_status(m["status"], m["date"]),
                    m.get("resume_hint") or m["title"], f".agent/handoffs/{p.name}")


# ── feeds: jobs ─────────────────────────────────────────────────────────


def _state_from_status(status: str, date_str: str | None) -> str:
    s = (status or "").lower()
    if s in ("done", "complete", "completed", "shipped"):
        return "done"
    if s == "blocked":
        return "stuck"
    if s in ("mid-build", "awaiting", "waiting", "needs-you", "review"):
        return "waiting_on_you"
    d = _days_since(date_str)
    if d is not None and d > STALE_DAYS:
        return "stuck"
    return "working"


def feed_goals(b: Bundle):
    p = b.root / ".agent" / "cos" / "goals.json"
    if not p.exists():
        return b.missing(".agent/cos/goals.json", "goal file is not there — I can't say the why from record")
    try:
        goals = json.loads(p.read_text(encoding="utf-8")).get("goals", [])
    except ValueError:
        return b.missing(".agent/cos/goals.json", "goal file is not valid JSON")
    active = [g for g in goals if g.get("status") == "active"]
    if not active:
        return b.missing(".agent/cos/goals.json", "no active goal recorded")
    g = active[0]
    why = _one_line(g.get("why", ""), 220)
    b.doing_and_why["goal"] = {"id": g.get("id"), "target": _one_line(g.get("target", ""), 160),
                               "why": why, "horizon": g.get("horizon"),
                               "last_reviewed": g.get("last_reviewed"), "source": ".agent/cos/goals.json"}
    d = _days_since(g.get("last_reviewed"))
    if d is not None and d > (g.get("review_cadence_days") or 7) * 2:
        b.notes.append(f"top goal '{g.get('id')}' last reviewed {_age(d)} — its own cadence is "
                       f"{g.get('review_cadence_days')} days")


def feed_handoffs(b: Bundle):
    store = b.root / ".agent" / "handoffs"
    if not store.exists():
        return b.missing(".agent/handoffs/", "handoff folder is not there")
    try:
        import handoff_store as hs
    except Exception as e:  # noqa: BLE001
        return b.missing("handoff_store import", str(e))
    latest: dict[str, dict] = {}
    metas = sorted((hs.read_meta(p) for p in hs._files(store)),
                   key=lambda m: (m["date"], m["mtime"]), reverse=True)
    for m in metas:
        latest.setdefault(m["thread"], m)
    live = [m for m in latest.values() if m["status"] != "done"]
    parked = [m for m in live if m["status"] in ("blocked", "mid-build")]
    stale = [m for m in live if (_days_since(m["date"]) or 0) > STALE_DAYS]
    b.counts.update({"handoff_threads_live": len(live), "handoff_threads_blocked_or_midbuild": len(parked),
                     "handoff_threads_stale": len(stale)})
    # Surface: blocked/mid-build first (a promise to resume), then pinned recent.
    parked.sort(key=lambda m: (not m["pin"], m["date"]), reverse=False)
    parked.sort(key=lambda m: m["pin"], reverse=True)
    shown = 0
    for m in parked + [m for m in live if m["pin"] and m not in parked][:3]:
        if shown >= b.limit:
            break
        days = _days_since(m["date"])
        state = _state_from_status(m["status"], m["date"])
        reason = m.get("resume_hint") or m["title"]
        if m["status"] == "blocked":
            reason = f"blocked for {_dur(days)}: {reason}"
        elif m["status"] == "mid-build":
            reason = f"half-built, untouched for {_dur(days)}: {reason}"
        b.piece(m["thread"], state, reason, f".agent/handoffs/{m['name']}",
                pinned=m["pin"], age_days=days)
        shown += 1
        if m.get("unfinished"):
            b.decision(f"{m['thread']}: {m['unfinished']}", f".agent/handoffs/{m['name']} (unfinished:)",
                       options=_options_in(m["unfinished"]), hint=m.get("resume_hint", ""))


def _options_in(text: str) -> list[str]:
    """Pull 'A vs B' / 'A or B' / 'A) … B) …' shapes out of a source line. Never invents."""
    t = str(text or "")
    m = re.findall(r"\b([A-D])\)\s*([^A-D)]{3,80}?)(?=\s+[A-D]\)|$)", t)
    if len(m) >= 2:
        return [f"{k}) {_one_line(v, 80)}" for k, v in m[:2]]
    for sep in (" vs ", " vs. ", " versus ", " or "):
        if sep in t:
            a, _, rest = t.partition(sep)
            a = a.split(":")[-1].split(",")[-1].strip()
            bb = re.split(r"[;,.(]", rest, 1)[0].strip()
            if 3 <= len(a) <= 80 and 3 <= len(bb) <= 80:
                return [a, bb]
    return []


def feed_sweep(b: Bundle):
    p = b.root / ".agent" / "sweep" / "latest.json"
    if not p.exists():
        return b.missing(".agent/sweep/latest.json", "sweep bundle is not there (session_sweep.py run never happened here)")
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except ValueError:
        return b.missing(".agent/sweep/latest.json", "sweep bundle is not valid JSON")
    age_h = None
    try:
        age_h = (datetime.now() - datetime.fromisoformat(data.get("generated", "")[:19])).total_seconds() / 3600
    except ValueError:
        pass
    if age_h is not None and age_h > 48:
        b.notes.append(f"the session sweep is {age_h / 24:.0f} days old — thread facts below may lag")
    try:
        import mission_board as mb
    except Exception as e:  # noqa: BLE001
        mb = None
        b.notes.append(f"mission_board import failed ({e}); using plain status only")
    threads = data.get("threads") or {}
    synth = {}
    sp = b.root / ".agent" / "sweep" / "synthesis.json"
    if sp.exists():
        try:
            synth = json.loads(sp.read_text(encoding="utf-8"))
        except ValueError:
            b.missing(".agent/sweep/synthesis.json", "not valid JSON")
    else:
        b.missing(".agent/sweep/synthesis.json", "plain-English thread ledes not there")
    ranked = []
    for slug, t in threads.items():
        rank, why = mb.why_needs_you(t) if mb else (None, "")
        open_missions = [m for m in t.get("missions", []) if m.get("open")]
        if rank is None and not open_missions:
            continue
        ranked.append((rank if rank is not None else 9, slug, t, why, open_missions))
    ranked.sort(key=lambda r: (r[0], r[1]))
    b.counts["sweep_threads_needing_you"] = len(ranked)
    seen = {p_["name"] for p_ in b.pieces}
    for rank, slug, t, why, open_missions in ranked[: b.limit]:
        if slug in seen:
            continue
        state = "stuck" if rank == 0 else ("waiting_on_you" if rank in (1, 2) else "stuck")
        lede = (synth.get(slug) or {}).get("lede") or ""
        next_move = (synth.get(slug) or {}).get("next_move") or ""
        reason = lede or why or t.get("resume_hint") or t.get("title") or slug
        b.piece(slug, state, reason, f".agent/sweep/latest.json → threads.{slug} ({why})",
                next_move=_one_line(next_move), open_missions=[_one_line(m.get("title", ""), 100)
                                                                for m in open_missions[:3]])


def feed_cos_decisions(b: Bundle):
    p = b.root / ".agent" / "cos" / "decisions.md"
    if not p.exists():
        return b.missing(".agent/cos/decisions.md", "decision ledger is not there")
    text = p.read_text(encoding="utf-8", errors="replace")
    # Standing decisions (Path A lock etc.) are rules in force, not choices waiting
    # on him — only the sections after them hold pending commitments.
    standing_end = re.search(r"^## (?!Standing)", text, re.M)
    pending_text = text[standing_end.start():] if standing_end else text
    blocks = re.split(r"\n(?=### )", pending_text)
    open_count = 0
    for blk in blocks:
        head = blk.splitlines()[0].lstrip("# ").strip() if blk.strip() else ""
        if not head or not blk.startswith("### "):
            continue
        if re.search(r"^Status:\s*OPEN", blk, re.M | re.I):
            open_count += 1
            b.decision(head, ".agent/cos/decisions.md (Status: OPEN)",
                       hint=_one_line(re.sub(r"^#.*\n", "", blk, 1), 160))
        for m in re.finditer(r"(?:due|Review:?)[^\n]{0,60}?(\d{4}-\d{2}-\d{2})", blk):
            d = _days_since(m.group(1))
            if d is not None and -45 <= d <= 0:
                b.deadlines.append({"what": _one_line(head, 90), "date": m.group(1),
                                    "in_days": -d, "source": ".agent/cos/decisions.md"})
    b.counts["cos_open_decisions"] = open_count


def feed_mission_dirs(b: Bundle):
    root = b.root / ".agent" / "missions"
    if not root.exists():
        return b.missing(".agent/missions/", "mission folders are not there")
    n_contract = n_mission = 0
    for d in sorted(root.iterdir()):
        if not d.is_dir():
            continue
        cj, mj = d / "contract.json", d / "mission.json"
        if mj.exists():
            n_mission += 1
            try:
                m = json.loads(mj.read_text(encoding="utf-8"))
            except ValueError:
                b.missing(str(mj.relative_to(b.root)), "not valid JSON")
                continue
            status = str(m.get("status", "")).lower()
            if status in ("complete", "completed", "done", "closed"):
                continue
            queue = m.get("activation_queue") or []
            blocked = [q for q in queue if q.get("blocker")]
            open_q = [q for q in queue if str(q.get("status", "")).lower() not in ("complete", "done")]
            state = "stuck" if blocked else ("working" if open_q else "waiting_on_you")
            reason = (blocked[0].get("blocker") if blocked else
                      (open_q[0].get("next_action") if open_q else "every lane done but mission not closed"))
            b.piece(m.get("name") or d.name, state, reason, f".agent/missions/{d.name}/mission.json",
                    lanes_open=len(open_q), lanes_total=len(queue))
            for q in blocked[:2]:
                b.decision(f"{d.name} lane '{q.get('id')}' is blocked: {q.get('blocker')}",
                           f".agent/missions/{d.name}/mission.json → activation_queue.{q.get('id')}")
        elif cj.exists():
            n_contract += 1
    if n_contract:
        b.notes.append(f"{n_contract} mission folder(s) use contract.json, which records intent but no status — "
                       "their state comes from the handoff/sweep feeds, not the folder")
    b.counts.update({"mission_dirs_contract": n_contract, "mission_dirs_mission_json": n_mission})


def feed_mission_queue(b: Bundle):
    q = b.root / ".agent" / "mission-queue"
    if not q.exists():
        return b.missing(".agent/mission-queue/", "queue folder is not there")
    pend = sorted((q / "pending").glob("card-*.md")) if (q / "pending").exists() else []
    park = [p for p in (q / "parked").glob("card-*.md")] if (q / "parked").exists() else []
    b.counts.update({"queue_pending": len(pend), "queue_parked": len(park)})
    for p in pend[: b.limit]:
        text = p.read_text(encoding="utf-8", errors="replace")
        title = next((l.lstrip("# ").strip() for l in text.splitlines() if l.startswith("#")), p.stem)
        needs_human = bool(re.search(r"human review required|Farrice runs or nods", text, re.I))
        b.piece(title, "waiting_on_you" if needs_human else "working",
                "queued card needs your nod before it runs" if needs_human else "queued for the overnight runner",
                f".agent/mission-queue/pending/{p.name}")
        if needs_human:
            b.decision(f"Run or park the queued card: {title}", f".agent/mission-queue/pending/{p.name}",
                       options=["run it", "park it"])


def feed_self_heal(b: Bundle):
    script = b.root / "execution" / "self_heal.py"
    if not script.exists():
        return b.missing("execution/self_heal.py", "health script is not there")
    rc, out = _run([sys.executable, "-W", "ignore", str(script), "report", "--json"], b.root, timeout=90)
    if rc != 0 or not out.strip().startswith("["):
        return b.missing("self_heal report --json", "health report did not return JSON")
    try:
        items = json.loads(out)
    except ValueError:
        return b.missing("self_heal report --json", "health report JSON unreadable")
    judgment = [i for i in items if i.get("cls") == "JUDGMENT"]
    b.counts["health_needs_judgment"] = len(judgment)
    if judgment:
        top = judgment[0]
        b.piece(f"system health: {len(judgment)} thing(s) need your judgment", "waiting_on_you",
                f"first one: {top.get('what', '')}", "python3 execution/self_heal.py report --json",
                ids=[i.get("id") for i in judgment[:6]])


def feed_job_board(b: Bundle):
    script = b.root / "execution" / "job_board.py"
    if not script.exists():
        b.notes.append("no job board yet (execution/job_board.py not here) — the /job manager loop is still being built")
        return
    rc, out = _run([sys.executable, "-W", "ignore", str(script), "status", "--all"], b.root, timeout=60)
    if rc != 0:
        return b.missing("job_board.py status --all", f"exit {rc}")
    b.doing_and_why["job_board_raw"] = [_one_line(l, 160) for l in out.splitlines() if l.strip()][:20]
    b.notes.append("job board present — its lines are in doing_and_why.job_board_raw (parse pending until its schema settles)")


# ── assembly ────────────────────────────────────────────────────────────


def collect(scope: str, root: Path, limit: int) -> dict:
    b = Bundle(root, limit)
    branch = ""
    if scope in ("here", "all"):
        feed_session_state(b)
        feed_git(b)
        branch = b.doing_and_why.get("branch", "")
        feed_lane_handoffs(b, branch)
        feed_goals(b)
    if scope in ("jobs", "all"):
        if "goal" not in b.doing_and_why:
            feed_goals(b)
        feed_handoffs(b)
        feed_sweep(b)
        feed_cos_decisions(b)
        feed_mission_dirs(b)
        feed_mission_queue(b)
        feed_self_heal(b)
        feed_job_board(b)
    # de-dupe pieces by name, keep first (most authoritative feed order)
    seen, uniq = set(), []
    for p in b.pieces:
        if p["name"] in seen:
            continue
        seen.add(p["name"])
        uniq.append(p)
    b.pieces = uniq
    b.counts["pieces_by_state"] = {s: sum(1 for p in b.pieces if p["state"] == s) for s in STATES}
    b.doing_and_why["if_nothing"] = _if_nothing(b)
    return b.to_dict()


def _if_nothing(b: Bundle) -> str:
    stuck = [p for p in b.pieces if p["state"] == "stuck"]
    waiting = [p for p in b.pieces if p["state"] == "waiting_on_you"]
    parts = []
    if stuck:
        oldest = max((p.get("age_days") or 0) for p in stuck)
        parts.append(f"{len(stuck)} stuck thing(s) stay stuck" + (f" (oldest already {oldest} days)" if oldest else ""))
    if waiting:
        parts.append(f"{len(waiting)} thing(s) keep waiting on you")
    due = [d for d in b.deadlines if d["in_days"] >= 0]
    if due:
        d = min(due, key=lambda x: x["in_days"])
        parts.append(f"'{d['what']}' comes due in {d['in_days']} day(s) ({d['date']})")
    return "; ".join(parts) if parts else "nothing is waiting, so nothing slips"


# ── terminal render (Codex seat pastes this) ────────────────────────────

LABEL = {"done": "done", "working": "working", "stuck": "stuck", "waiting_on_you": "waiting on you"}
GLYPH = {"done": "✅", "working": "🔄", "stuck": "⛔", "waiting_on_you": "🙋"}


def render(d: dict) -> str:
    out = []
    if d["empty"]:
        out.append("Nothing is open right now. Nothing is waiting on you.")
        if d["unavailable"]:
            out.append("I can't see: " + "; ".join(f"{u['feed']} ({u['why']})" for u in d["unavailable"][:4]))
        return "\n".join(out)
    g = d["doing_and_why"].get("goal")
    if g:
        out.append(f"Why: {g['target']}  (source: {g['source']})")
    pieces = d["pieces"]
    if len(pieces) >= 3:
        # Grouped by urgency; past 8 rows the tail collapses to one count line.
        order = {"stuck": 0, "waiting_on_you": 1, "working": 2, "done": 3}
        rows = sorted(pieces, key=lambda p: order[p["state"]])
        shown, rest = rows[:8], rows[8:]
        out.append("")
        out.append("| thing | state | what it needs |")
        out.append("|---|---|---|")
        for p in shown:
            out.append(f"| {p['name']} | {GLYPH[p['state']]} {LABEL[p['state']]} | {_one_line(p['reason'], 90)} |")
        if rest:
            by = {}
            for p in rest:
                by[LABEL[p["state"]]] = by.get(LABEL[p["state"]], 0) + 1
            out.append("| +" + str(len(rest)) + " more | " +
                       ", ".join(f"{n} {k}" for k, n in by.items()) + " | ask for the full list (`--limit 50`) |")
    else:
        for p in pieces:
            out.append(f"{GLYPH[p['state']]} {p['name']} — {LABEL[p['state']]}. {_one_line(p['reason'], 110)}")
    if d["decisions"]:
        out.append("")
        out.append("Only you can decide:")
        for i, dec in enumerate(d["decisions"][:4], 1):
            opts = dec["options_in_source"]
            ab = f"  A) {opts[0]}  B) {opts[1]}" if len(opts) >= 2 else "  (options not written down in the source)"
            out.append(f"{i}. {dec['question']}{ab}")
    out.append("")
    out.append(f"If you do nothing: {d['doing_and_why'].get('if_nothing', '')}")
    if d["unavailable"]:
        out.append("I can't see: " + "; ".join(f"{u['feed']}" for u in d["unavailable"][:4]))
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="collector behind /eli5 — reads real state, never guesses")
    ap.add_argument("--scope", choices=("here", "jobs", "all"), default="all")
    ap.add_argument("--root", default=None, help="read feeds from this dir instead of the repo")
    ap.add_argument("--json", action="store_true", help="print the fact bundle")
    ap.add_argument("--render", action="store_true", help="print markdown blocks for a terminal seat")
    ap.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    a = ap.parse_args(argv)
    root = Path(a.root).expanduser().resolve() if a.root else REPO
    d = collect(a.scope, root, a.limit)
    if a.json or not a.render:
        print(json.dumps(d, indent=2, ensure_ascii=False))
    if a.render:
        if a.json:
            print()
        print(render(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
