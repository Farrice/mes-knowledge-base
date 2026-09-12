#!/usr/bin/env python3
"""job_board.py — the manager-loop job board (façade over mission_control state).

Born 2026-09-09 from Nate B Jones's manager-loop video and one on-disk scar:
54 missions open, the oldest 41 days — compiled by /go, never driven. A JOB is a
mission dir `.agent/missions/<slug>/` that carries:

  card.md        the instantiated recipe (recipes/<recipe>.md filled in)
  mission.json   mission_control state — its activation_queue IS the lane list
                 (id, owner, workflow, status, after[], expected_artifact,
                 evidence_path, blocker, next_action)
  decisions.md   DECISION PACKETS waiting on Farrice + his answers
  portable.md    paste-anywhere packet for the other harness / ChatGPT (handoff)
  closeout.md    Nate's four questions, answered with receipts

Zero new stores. Same file, same CLI, under Claude Code and Codex, so either
harness can open, drive, hand off, or resume a job without the other existing.
ONE BOARD: state always lives in the MAIN checkout (`resolve_state_root`), so a
job opened from any worktree lane is on the same board every session sees.
Every mission.json write takes a file lock (two writers never lose a lane).

The one rule this board makes physical: `next` prints TURN MUST CONTINUE while
any lane is runnable, and MAY END only when every lane is complete, skipped, or
blocked on a decision that is his. Nothing here blocks (compass doctrine) —
the manager reads the line and acts.

Two more things made physical on 2026-09-10 (scar: the Coach Cooz job ran the
Poppy card's lanes on a website audit, no interview, no trace — "it just does
things"):
  plan.md   `open` writes and prints a JOB PLAN (goal · recipe + match verdict ·
            every lane as "what I'll do" · questions · approvals). `next` prints
            PLAN PENDING until `go <slug>` records his nod (`open --go` = "just do
            it"). The opening turn's reply IS the plan; lanes start next turn.
  trace.md  a timeline. Every open / go / lane change / packet / close writes a
            line; the manager adds `log` lines (did / found / skipped). `trace`
            prints it, `status --all --trace` and Homebase show the tail. He reads
            the trace to learn the process and to step in at any line.

Usage:
  python3 execution/job_board.py open <slug> --recipe <recipe> [--goal "..."] [--owner claude|codex|chat] [--serves <goal-id>] [--go]
  python3 execution/job_board.py plan <slug>                              # re-print the JOB PLAN (plan.md)
  python3 execution/job_board.py go <slug> [--note "his words"]           # his nod → lanes may start
  python3 execution/job_board.py log <slug> <lane|-> "<did / found / skipped>" [--kind did|found|skipped|note]
  python3 execution/job_board.py trace <slug> [--last N] | trace --all [--last N]
  python3 execution/job_board.py lanes <slug>
  python3 execution/job_board.py lane <slug> <id> [--status S] [--evidence P] [--did "..."] [--blocker B] [--owner O] [--next N]
  python3 execution/job_board.py next <slug>
  python3 execution/job_board.py packet <slug> add --lane L --choice "..." --options "A … / B …" --recommend "A — why" [--irreversible "..."] [--if-none "..."]
  python3 execution/job_board.py packet <slug> answer <n> "<his words>"
  python3 execution/job_board.py packet <slug> list
  python3 execution/job_board.py checkpoint <slug> [--note "..."]        # turn-end save → /resume finds it
  python3 execution/job_board.py handoff <slug> --to codex|claude|chat   # portable.md + handoff store
  python3 execution/job_board.py resume <slug>
  python3 execution/job_board.py status [--all] [slug]
  python3 execution/job_board.py --brief                                 # one line for session_brief
  python3 execution/job_board.py close <slug> --done "..." --aligned "..." --unauthorized "..." --approvals "..." [--verdict good|marginal|off] [--ratchet "..."] [--force]
  python3 execution/job_board.py lint <slug>
"""
from __future__ import annotations

import argparse
import datetime as _dt
import fcntl
import json
import os
import re
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # this checkout: code + recipes travel with the branch
EXEC = ROOT / "execution"
if str(EXEC) not in sys.path:
    sys.path.insert(0, str(EXEC))


def resolve_state_root() -> Path:
    """ONE BOARD ACROSS EVERY LANE (2026-09-10). Job state lives in the MAIN checkout's
    `.agent/missions/` no matter which worktree lane the session sits in — otherwise a
    job opened in a lane is invisible to every other session until the lane merges
    (seen: lane board 4 jobs, main board 8). ANTIGRAVITY_ROOT still wins (verifiers,
    temp roots)."""
    env = os.environ.get("ANTIGRAVITY_ROOT")
    if env:
        return Path(env).expanduser().resolve()
    try:
        out = subprocess.run(["git", "rev-parse", "--git-common-dir"], cwd=str(ROOT),
                             capture_output=True, text=True, timeout=5).stdout.strip()
        if out:
            common = Path(out)
            if not common.is_absolute():
                common = (ROOT / common).resolve()
            if common.name == ".git" and common.parent.is_dir():
                return common.parent.resolve()
    except Exception:
        pass
    return ROOT


STATE_ROOT = resolve_state_root()
# mission_control reads ANTIGRAVITY_ROOT at import; its subprocesses inherit it too
os.environ["ANTIGRAVITY_ROOT"] = str(STATE_ROOT)

import mission_control as mc  # noqa: E402
import recipe_cards as rc  # noqa: E402

MISSIONS_JSONL = STATE_ROOT / ".agent" / "missions.jsonl"
TERMINAL = {"complete", "skipped"}
WAITING = {"blocked"}
RUNNABLE_STATES = {"planned", "active"}
PACKET_HEAD_RE = re.compile(r"^## Packet (\d+) — (\S+) · (open|answered)", re.M)


# ── helpers ───────────────────────────────────────────────────────────────
def now_iso() -> str:
    return _dt.datetime.now().astimezone().isoformat(timespec="seconds")


def harness() -> str:
    """Who is running this command. Codex's own shell does not carry ANTIGRAVITY_HARNESS
    (that is set only for hook runs), but it does carry CODEX_THREAD_ID / CODEX_SANDBOX
    (probed live 2026-09-10 — Astra's lane writes had been stamped [claude])."""
    if os.environ.get("ANTIGRAVITY_HARNESS", "").lower() == "codex":
        return "codex"
    if os.environ.get("CODEX_THREAD_ID") or os.environ.get("CODEX_SANDBOX"):
        return "codex"
    return "claude"


def git_branch() -> str:
    try:
        out = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=str(ROOT),
                             capture_output=True, text=True, timeout=5)
        return out.stdout.strip() or "?"
    except Exception:
        return "?"


@contextmanager
def locked(slug: str):
    d = mc.mission_dir(slug)
    d.mkdir(parents=True, exist_ok=True)
    lock = d / ".lock"
    with open(lock, "w") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


def is_job(slug: str) -> bool:
    return (mc.mission_dir(slug) / "card.md").exists() and mc.state_path(slug).exists()


def read(slug: str) -> dict:
    if not mc.state_path(slug).exists():
        raise SystemExit(f"no job '{slug}' — job_board.py status --all")
    return mc.read_state(slug)


def write(slug: str, state: dict) -> None:
    state["updated_at"] = mc.now()
    mc.write_state(slug, state)
    try:
        mc.write_markdown(state)
    except Exception:
        pass


def lanes_of(state: dict) -> list[dict]:
    return list(state.get("activation_queue") or [])


def lane_by_id(state: dict, lane_id: str) -> dict | None:
    for item in lanes_of(state):
        if item.get("id") == lane_id:
            return item
    return None


def deps_met(lane: dict, state: dict) -> bool:
    for dep in lane.get("after") or []:
        d = lane_by_id(state, dep)
        if d is None or d.get("status") not in TERMINAL:
            return False
    return True


def classify(state: dict) -> dict:
    runnable, waiting_deps, blocked, done = [], [], [], []
    for lane in lanes_of(state):
        s = lane.get("status")
        if s in TERMINAL:
            done.append(lane)
        elif s in WAITING:
            blocked.append(lane)
        elif s in RUNNABLE_STATES and deps_met(lane, state):
            runnable.append(lane)
        else:
            waiting_deps.append(lane)
    # a lane whose deps can never be met this turn (dep is blocked) is waiting on him too
    truly_waiting = []
    for lane in waiting_deps:
        chain_blocked = any((lane_by_id(state, d) or {}).get("status") in WAITING
                            for d in lane.get("after") or [])
        (blocked if chain_blocked else truly_waiting).append(lane)
    return {"runnable": runnable, "waiting_deps": truly_waiting, "blocked": blocked, "done": done}


def stamp_writer(state: dict) -> dict | None:
    """Record who wrote last (branch + harness + time); return the PREVIOUS stamp when it
    came from another branch within 30 minutes — the 'two sessions on one job' nudge."""
    job = state.setdefault("job", {})
    prev = job.get("last_writer") or {}
    cur = {"branch": git_branch(), "harness": harness(), "ts": now_iso()}
    job["last_writer"] = cur
    if prev and prev.get("branch") and prev["branch"] != cur["branch"]:
        try:
            age = (_dt.datetime.fromisoformat(cur["ts"]) - _dt.datetime.fromisoformat(prev["ts"])).total_seconds()
        except Exception:
            age = 10 ** 9
        if age < 30 * 60:
            prev["age_min"] = int(age // 60)
            return prev
    return None


def writer_nudge(prev: dict | None, slug: str) -> None:
    if prev:
        print(f"  nudge: another session (branch {prev['branch']}, {prev.get('harness', '?')}) wrote to {slug} "
              f"{prev['age_min']} min ago — one session per job: resume there, or hand off first")


def finished_unclosed(state: dict) -> bool:
    c = classify(state)
    lanes = lanes_of(state)
    return bool(lanes) and len(c["done"]) == len(lanes) and state.get("status") not in ("complete", "closed", "parked")


def decisions_path(slug: str) -> Path:
    return mc.mission_dir(slug) / "decisions.md"


def packets(slug: str) -> list[dict]:
    p = decisions_path(slug)
    if not p.exists():
        return []
    text = p.read_text(encoding="utf-8")
    out = []
    heads = list(PACKET_HEAD_RE.finditer(text))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        out.append({"n": int(m.group(1)), "lane": m.group(2), "state": m.group(3),
                    "body": text[m.start():end].strip()})
    return out


def open_packets(slug: str) -> list[dict]:
    return [p for p in packets(slug) if p["state"] == "open"]


def job_slugs(include_closed: bool = False) -> list[str]:
    out = []
    if not mc.MISSIONS_DIR.exists():
        return out
    for d in sorted(mc.MISSIONS_DIR.iterdir()):
        if not (d / "card.md").exists() or not (d / "mission.json").exists():
            continue
        try:
            st = mc.read_state(d.name)
        except Exception:
            continue
        if not include_closed and st.get("status") in ("complete", "closed", "parked"):
            continue
        out.append(d.name)
    return out


def append_mission_line(slug: str, status: str, mission: str, serves: str = "orphan",
                        tier: str = "T1", outcome: str = "", verdict=None,
                        expected_spawns=None) -> None:
    line = {
        "ts": now_iso(), "mission": mission, "slug": slug, "serves": serves,
        "pattern": "manager-loop", "tier": tier, "status": status,
        "expected_spawns": expected_spawns, "measured_spawns": None,
        "verdict": verdict, "outcome": outcome, "platform": harness(),
    }
    MISSIONS_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with open(MISSIONS_JSONL, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(line, ensure_ascii=False) + "\n")


def plan_path(slug: str) -> Path:
    return mc.mission_dir(slug) / "plan.md"


def trace_path(slug: str) -> Path:
    return mc.mission_dir(slug) / "trace.md"


def plan_state(state: dict) -> str:
    """'pending' | 'confirmed'. Jobs opened before plan.md existed carry no key → confirmed."""
    return (state.get("job") or {}).get("plan") or "confirmed"


def trace_add(slug: str, lane: str, kind: str, text: str, who: str | None = None) -> str:
    """Append one timeline line to trace.md (creates the file). Returns the line."""
    tp = trace_path(slug)
    tp.parent.mkdir(parents=True, exist_ok=True)
    if not tp.exists():
        tp.write_text(f"# Trace — {slug}\n\nWhat was done, found, skipped, asked and answered — "
                      f"one line each, oldest first.\n\n", encoding="utf-8")
    who = who or harness()
    line = f"- {now_iso()} · {lane or '-'} · {kind} · {' '.join(str(text).split())} · [{who}]"
    with open(tp, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


def trace_lines(slug: str) -> list[str]:
    tp = trace_path(slug)
    if not tp.exists():
        return []
    return [l for l in tp.read_text(encoding="utf-8").splitlines() if l.startswith("- ")]


def plan_text(slug: str, card: dict, recipe: str, goal: str, match_note: str,
              extra_ask=None, found=None) -> str:
    secs = card["sections"]
    lines = [f"JOB PLAN — {slug}", f"Goal: {goal}", f"Recipe: {recipe} · {match_note}"]
    if re.match(r"^\s*(decide|should (i|we)|which|whether|do i|is it worth|what should i)\b", goal, re.I) \
            and len(card["lanes"]) > 2:
        lines.append("Shape check: this goal reads like a DECISION. If one packet answers it, this is not a job — "
                     "use recipes/decision-packet.md (one lane, one packet) instead of running these lanes.")
    lines += ["", "What I'll do (lanes):"]
    for l in card["lanes"]:
        dep = f"after {', '.join(l['after'])}" if l["after"] else "parallel"
        lines.append(f"  {l['id']} {l['name']} [{dep}] — {l['desc']}")
    ask = [x.strip() for x in secs.get("Ask me first", "").splitlines() if x.strip().startswith("-")]
    ask = [x.lstrip('- ').strip() for x in ask] + [q.strip() for q in (extra_ask or []) if q.strip()]
    if found:
        lines += ["", "Found on disk (interview questions answered without asking):"]
        lines += [f"  - {f.strip()}" for f in found if f.strip()]
    lines += ["", "Questions I need answered before lane 1 (only ones that change the plan):"]
    lines += [f"  {x}" for x in ask] or ["  none — everything is on disk"]
    alone = " ".join(secs.get("Handles alone", "").split())
    back = [x.strip().lstrip("- ") for x in secs.get("Comes back when", "").splitlines() if x.strip()]
    appr = " ".join(secs.get("Needs approval", "").split())
    lines += ["", f"I handle alone: {alone or '—'}", "I come back with a packet when:"]
    lines += [f"  - {b}" for b in back] or ["  - (the card names nothing)"]
    lines += [f"Needs your approval: {appr or '—'}", "",
              f"Reply 'go' (or edit any line) to start lane 1 · python3 execution/job_board.py go {slug}"]
    return "\n".join(lines) + "\n"


def lane_table(state: dict) -> str:
    rows = ["| id | status | owner | after | expected | evidence | blocker |", "|---|---|---|---|---|---|---|"]
    for l in lanes_of(state):
        rows.append("| {id} | {status} | {owner} | {after} | {exp} | {ev} | {bl} |".format(
            id=l.get("id"), status=l.get("status"), owner=l.get("owner") or "",
            after=",".join(l.get("after") or []) or "—",
            exp=(l.get("workflow") or l.get("expected_artifact") or "")[:60],
            ev=(l.get("evidence_path") or "")[:50], bl=(l.get("blocker") or "")[:50]))
    return "\n".join(rows)


# ── commands ──────────────────────────────────────────────────────────────
def cmd_open(a):
    recipe = a.recipe
    if not rc.card_path(recipe).exists():
        print(f"no recipe '{recipe}' — python3 execution/recipe_cards.py list | new")
        return 1
    errs = rc.lint(recipe)
    if errs:
        print("recipe lint failed (fix the card first):\n  " + "\n  ".join(errs))
        return 1
    card = rc.parse(recipe)
    goal = a.goal or card["sections"].get("The job", "").strip().splitlines()[0]
    slug = a.slug
    existed = mc.state_path(slug).exists()
    if existed and not a.force:
        print(f"job '{slug}' already exists — job_board.py resume {slug} (or --force)")
        return 1
    if existed:
        print(f"  NOTE: --force re-opens '{slug}': every lane resets to planned and lane progress is gone "
              f"(trace.md and decisions.md are kept)")
    cmd = [sys.executable, str(EXEC / "mission_control.py"), "create", "--name", card["frontmatter"].get("name", slug),
           "--slug", slug, "--goal", goal, "--mode", a.mode,
           "--next-command", f"python3 execution/job_board.py next {slug}"]
    if a.force:
        cmd.append("--force")
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
    if r.returncode != 0:
        print(r.stdout + r.stderr)
        return 1
    with locked(slug):
        state = mc.read_state(slug)
        state["status"] = "active"
        state["job"] = {"recipe": recipe, "opened_at": now_iso(), "opened_by": a.owner,
                        "harness": harness(), "serves": a.serves}
        queue = []
        for l in card["lanes"]:
            queue.append({"id": l["id"], "owner": a.owner, "workflow": l["name"],
                          "expected_artifact": l["desc"], "status": "planned",
                          "after": l["after"], "kind": "lane", "updated_at": mc.now()})
        state["activation_queue"] = queue
        write(slug, state)
        # instantiate the card
        text = rc.card_path(recipe).read_text(encoding="utf-8")
        inst = (f"<!-- instance of recipes/{recipe}.md · opened {now_iso()} by {a.owner} "
                f"on {harness()} · goal: {goal} -->\n" + text)
        (mc.mission_dir(slug) / "card.md").write_text(inst, encoding="utf-8")
        dp = decisions_path(slug)
        if not dp.exists():
            dp.write_text(f"# Decisions — {slug}\n\nPackets the manager brought back; "
                          f"answers recorded verbatim.\n", encoding="utf-8")
    append_mission_line(slug, "compiled", goal, serves=a.serves,
                        tier=card["frontmatter"].get("tier_default", "T1"),
                        expected_spawns=len([l for l in card["lanes"] if not l["after"]]))
    # match verdict on HIS goal sentence — a weak match is said out loud in the plan
    rows = rc.match(goal, top=3)
    v = rc.verdict(rows)
    top = rows[0]["slug"] if rows else None
    if v["confident"] and top == recipe:
        match_note = f"CONFIDENT match ({v['reason']})"
    elif top == recipe:
        match_note = f"WEAK match ({v['reason']}) — check that the lanes below fit before saying go"
    else:
        match_note = (f"chosen by hand (the matcher's top pick was {top}: {v['reason']})"
                      if top else "chosen by hand (the matcher scored nothing)")
    ptxt = plan_text(slug, card, recipe, goal, match_note,
                     extra_ask=getattr(a, "ask", None), found=getattr(a, "found", None))
    with locked(slug):
        state = mc.read_state(slug)
        state["job"]["plan"] = "confirmed" if a.go else "pending"
        state["job"]["match"] = {"top": top, "confident": v["confident"], "reason": v["reason"]}
        stamp_writer(state)
        write(slug, state)
        plan_path(slug).write_text(ptxt, encoding="utf-8")
        trace_add(slug, "-", "opened", f"recipe {recipe} · {len(card['lanes'])} lanes · {match_note}", a.owner)
        if a.go:
            trace_add(slug, "-", "go", "opened with --go (his 'just do it')", a.owner)
    print(f"JOB OPEN — {slug} (recipe {recipe}, {len(card['lanes'])} lanes, owner {a.owner}, {harness()})")
    print(f"  card: {mc.rel(mc.mission_dir(slug) / 'card.md')} · plan: {mc.rel(plan_path(slug))} · "
          f"trace: {mc.rel(trace_path(slug))}")
    print()
    print(ptxt)
    return cmd_next(argparse.Namespace(slug=slug))


def cmd_plan(a):
    pp = plan_path(a.slug)
    st = read(a.slug)
    if not pp.exists():
        print(f"no plan.md for {a.slug} (opened before plans existed) — lanes: job_board.py lanes {a.slug}")
        return 0
    print(pp.read_text(encoding="utf-8"))
    print(f"plan: {plan_state(st)}")
    return 0


def cmd_go(a):
    with locked(a.slug):
        state = read(a.slug)
        prev = stamp_writer(state)
        if plan_state(state) == "confirmed":
            print(f"  {a.slug}: plan already confirmed")
        else:
            state.setdefault("job", {})["plan"] = "confirmed"
            state["job"]["go_at"] = now_iso()
        write(a.slug, state)
        writer_nudge(prev, a.slug)
        trace_add(a.slug, "-", "go", a.note or "his nod", "farrice")
        dp = decisions_path(a.slug)
        with open(dp, "a", encoding="utf-8") as fh:
            fh.write(f"\n## Plan confirmed · {now_iso()}\n{a.note or 'his nod'}\n")
    print(f"GO — {a.slug}: lanes may start")
    return cmd_next(argparse.Namespace(slug=a.slug))


def cmd_log(a):
    if not mc.state_path(a.slug).exists():
        print(f"no job '{a.slug}'")
        return 1
    print(trace_add(a.slug, a.lane if a.lane != "-" else "-", a.kind, a.text))
    return 0


def cmd_trace(a):
    slugs = job_slugs() if a.all else [a.slug]
    if a.all and not slugs:
        print("TRACE: no jobs open")
        return 0
    for s_ in slugs:
        if not s_:
            print("trace needs a slug or --all")
            return 1
        ls = trace_lines(s_)
        tail = ls[-a.last:] if a.last else ls
        cut = f", last {a.last}" if a.last and len(ls) > a.last else ""
        print(f"TRACE — {s_} ({len(ls)} line(s){cut}) · {mc.rel(trace_path(s_))}")
        for l in tail:
            print("  " + l[2:])
        if not ls:
            print("  (empty — opened before traces existed, or nothing logged yet)")
    return 0


def cmd_lanes(a):
    state = read(a.slug)
    print(f"LANES — {a.slug} ({state.get('status')})")
    print(lane_table(state))
    ops = open_packets(a.slug)
    if ops:
        print(f"  decision packets open: {len(ops)} — job_board.py packet {a.slug} list")
    return 0


def cmd_lane(a):
    with locked(a.slug):
        state = read(a.slug)
        lane = lane_by_id(state, a.id)
        if lane is None:
            print(f"no lane '{a.id}' in {a.slug}")
            return 1
        before = lane.get("status")
        if a.status:
            if a.status not in mc.ACTIVATION_STATUSES:
                print(f"status must be one of {mc.ACTIVATION_STATUSES}")
                return 1
            lane["status"] = a.status
        if a.evidence is not None:
            lane["evidence_path"] = a.evidence
        if a.blocker is not None:
            lane["blocker"] = a.blocker
        if a.owner:
            lane["owner"] = a.owner
        if a.next is not None:
            lane["next_action"] = a.next
        if a.did is not None:
            lane["did"] = a.did
        lane["updated_at"] = mc.now()
        nudges = []
        if lane["status"] == "blocked" and not lane.get("blocker"):
            nudges.append("a blocked lane names its blocker (--blocker \"<decision needed>\")")
        if lane["status"] == "complete" and not lane.get("evidence_path"):
            nudges.append("complete with no --evidence path: the trace will say only 'complete'")
        if lane["status"] in ("complete", "skipped", "blocked") and not lane.get("did"):
            nudges.append("no --did line: say what was done / found / skipped so he can read it in the trace")
        prev = stamp_writer(state)
        write(a.slug, state)
        writer_nudge(prev, a.slug)
        if a.status or a.did or a.evidence or a.blocker:
            what = []
            if a.status and a.status != before:
                what.append(f"{before} → {a.status}")
            if a.did:
                what.append(f"did: {a.did}")
            if a.evidence:
                what.append(f"evidence: {a.evidence}")
            if a.blocker:
                what.append(f"blocker: {a.blocker}")
            trace_add(a.slug, a.id, a.status or "update", " · ".join(what) or "touched")
    for n in nudges:
        print(f"  nudge: {n}")
    receipt = (f"LANE RECEIPT — {a.slug}/{a.id} {lane.get('workflow') or ''}: {lane['status']}"
               + (f" · did: {lane['did']}" if lane.get("did") else "")
               + (f" · evidence: {lane['evidence_path']}" if lane.get("evidence_path") else "")
               + (f" · blocker: {lane['blocker']}" if lane.get("blocker") else ""))
    print(receipt)
    return 0


def cmd_next(a):
    state = read(a.slug)
    c = classify(state)
    ops = open_packets(a.slug)
    if plan_state(state) == "pending" and state.get("status") not in ("complete", "closed", "parked"):
        print(f"PLAN PENDING — {a.slug}: the reply IS the plan ({mc.rel(plan_path(a.slug))}); the turn ends there. "
              f"Lanes start on his nod: python3 execution/job_board.py go {a.slug}")
        return 0
    if c["runnable"]:
        ids = ", ".join(f"{l['id']} {l.get('workflow') or ''}".strip() for l in c["runnable"])
        print(f"TURN MUST CONTINUE — {a.slug}: runnable lanes: {ids}")
        if c["waiting_deps"]:
            print("  queued behind them: " + ", ".join(l["id"] for l in c["waiting_deps"]))
        if ops:
            print(f"  decision packets open: {len(ops)} (deliver them with the turn, keep the lanes moving)")
        return 0
    if c["blocked"]:
        names = ", ".join(f"{l['id']}({(l.get('blocker') or 'no blocker named')[:40]})" for l in c["blocked"])
        print(f"MAY END — {a.slug}: every remaining lane waits on Farrice: {names}; "
              f"decision packets open: {len(ops)}")
        if not ops:
            print("  nudge: blocked lanes with no packet — write one (job_board.py packet add) before ending")
        return 0
    if state.get("status") in ("complete", "closed"):
        print(f"MAY END — {a.slug}: closed")
        return 0
    print(f"MAY END — {a.slug}: all lanes complete. Close it: job_board.py close {a.slug} …")
    return 0


def cmd_packet(a):
    slug = a.slug
    dp = decisions_path(slug)
    if a.action == "list":
        ps = packets(slug)
        if not ps:
            print(f"no packets for {slug}")
            return 0
        for p in ps:
            print(p["body"] + "\n")
        return 0
    if a.action == "add":
        if not (a.lane and a.choice and a.options and a.recommend):
            print("packet add needs --lane --choice --options --recommend")
            return 1
        with locked(slug):
            n = len(packets(slug)) + 1
            block = (f"\n## Packet {n} — {a.lane} · open · {now_iso()}\n"
                     f"Choice: {a.choice}\n"
                     f"Irreversible? {a.irreversible or 'no'}\n"
                     f"Options: {a.options}\n"
                     f"Recommend: {a.recommend}\n"
                     f"If no answer: {a.if_none or 'the lane stays blocked; everything else keeps moving'}\n")
            dp.parent.mkdir(parents=True, exist_ok=True)
            with open(dp, "a", encoding="utf-8") as fh:
                fh.write(block)
            trace_add(slug, a.lane, "asked", f"packet #{n}: {a.choice}")
        print(f"DECISION PACKET — {slug}/{a.lane} · #{n}\nChoice: {a.choice}\nIrreversible? {a.irreversible or 'no'}\n"
              f"Options: {a.options}\nRecommend: {a.recommend}\nIf no answer: {a.if_none or 'the lane stays blocked; everything else keeps moving'}")
        return 0
    if a.action == "answer":
        if a.n is None or not a.text:
            print("packet answer needs <n> \"<text>\"")
            return 1
        with locked(slug):
            text = dp.read_text(encoding="utf-8") if dp.exists() else ""
            head = re.search(rf"^## Packet {a.n} — (\S+) · open · [^\n]*$", text, re.M)
            if not head:
                print(f"no open packet #{a.n} in {slug}")
                return 1
            new_head = head.group(0).replace(" · open · ", " · answered · ")
            # insert the answer at the end of this packet's block
            nxt = re.search(r"^## Packet ", text[head.end():], re.M)
            ins = head.end() + (nxt.start() if nxt else len(text) - head.end())
            answer = f"\nAnswer (Farrice, {now_iso()}): {a.text}\n"
            text = text[:head.start()] + new_head + text[head.end():ins].rstrip("\n") + "\n" + answer + text[ins:]
            dp.write_text(text, encoding="utf-8")
            trace_add(slug, head.group(1), "answered", f"packet #{a.n}: {a.text}", "farrice")
        print(f"  packet #{a.n} answered — unblock the lane: job_board.py lane {slug} {head.group(1)} --status active")
        return 0
    return 1


def portable_text(slug: str, target: str) -> str:
    state = read(slug)
    card = (mc.mission_dir(slug) / "card.md").read_text(encoding="utf-8")
    ops = open_packets(slug)
    answered = [p for p in packets(slug) if p["state"] == "answered"]
    c = classify(state)
    lines = [f"# JOB PACKET — {slug} · for {target} · generated {now_iso()} on {harness()} (branch {git_branch()})", ""]
    lines += ["## Resume"]
    if target == "chat":
        lines += ["You are the manager for this job. You have no repo access. Work every lane below whose "
                  "dependencies are met, in order of readiness. Return each lane's result as a block headed "
                  "`LANE <id> RESULT` (what you produced, in full) and each question as a `DECISION PACKET` "
                  "(Choice · Irreversible? · Options A/B + recommendation · If no answer). Farrice files them with "
                  f"`python3 execution/job_board.py lane {slug} <id> --status complete --evidence <path>`."]
    else:
        lines += [f"- `python3 execution/job_board.py resume {slug}` then follow "
                  "`skills/nate-b-jones-manager-loop/workflows/manager-loop-run.md`",
                  f"- end the turn only when `python3 execution/job_board.py next {slug}` prints MAY END"]
    lines += ["", "## Rules that travel",
              "- Keep every unblocked lane moving; batch questions into DECISION PACKETS; deliver packets + receipts, not status.",
              "- Never publish, send, spend, delete outside the repo, or ship AS Farrice without approval (the card's `Needs approval`).",
              "- Dispatch briefs carry verbatim: \"no Chain, no finalize, no Notion, no Next Moves, return only the artifact\".",
              "", "## Lanes now", lane_table(state),
              f"runnable: {', '.join(l['id'] for l in c['runnable']) or 'none'} · waiting on deps: "
              f"{', '.join(l['id'] for l in c['waiting_deps']) or 'none'} · blocked on Farrice: "
              f"{', '.join(l['id'] for l in c['blocked']) or 'none'} · done: {', '.join(l['id'] for l in c['done']) or 'none'}",
              "", "## Decision packets open"]
    lines += [p["body"] for p in ops] or ["none"]
    lines += ["", "## Decisions answered"]
    lines += [p["body"] for p in answered] or ["none"]
    tl = trace_lines(slug)
    lines += ["", f"## Trace (last {min(12, len(tl))} of {len(tl)})"] + (tl[-12:] or ["none"])
    lines += ["", "## Card", card]
    return "\n".join(lines) + "\n"


def _save_handoff(slug: str, status: str, hint: str, unfinished: str) -> str:
    if os.environ.get("JOB_BOARD_SKIP_HANDOFF_STORE"):
        return "handoff store skipped (JOB_BOARD_SKIP_HANDOFF_STORE)"  # verifiers on a temp root
    pm = mc.mission_dir(slug) / "portable.md"
    cmd = [sys.executable, str(EXEC / "handoff_store.py"), "save", "--from", str(pm), "--thread", slug,
           "--status", status, "--hint", hint, "--unfinished", unfinished, "--branch", git_branch(), "--overwrite"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT), timeout=30)
        return (r.stdout.strip().splitlines() or ["saved"])[-1] if r.returncode == 0 else f"handoff_store failed: {(r.stderr or r.stdout).strip()[:200]}"
    except Exception as exc:
        return f"handoff_store failed: {exc.__class__.__name__}"


def cmd_handoff(a):
    target = a.to
    text = portable_text(a.slug, target)
    pm = mc.mission_dir(a.slug) / "portable.md"
    pm.write_text(text, encoding="utf-8")
    state = read(a.slug)
    c = classify(state)
    unfinished = ", ".join(l["id"] for l in c["runnable"] + c["waiting_deps"] + c["blocked"]) or "none"
    hint = (f"python3 execution/job_board.py resume {a.slug}" if target != "chat"
            else f"paste {mc.rel(pm)} into the chat manager; file results with job_board.py lane")
    # handoff_store accepts only its own status vocabulary; the target rides in the hint
    receipt = _save_handoff(a.slug, "mid-build", f"[→ {target}] {hint}", unfinished)
    print(f"HANDOFF — {a.slug} → {target}\n  packet: {mc.rel(pm)}\n  {receipt}")
    if target == "chat":
        print("  paste the packet as-is; results come back as LANE <id> RESULT blocks")
    else:
        print(f"  on {target}: python3 execution/job_board.py resume {a.slug}")
    return 0


def cmd_checkpoint(a):
    text = portable_text(a.slug, harness())
    pm = mc.mission_dir(a.slug) / "portable.md"
    pm.write_text(text, encoding="utf-8")
    state = read(a.slug)
    c = classify(state)
    unfinished = ", ".join(l["id"] for l in c["runnable"] + c["waiting_deps"] + c["blocked"]) or "none"
    if a.note:
        with locked(a.slug):
            state = read(a.slug)
            state.setdefault("job", {})["last_note"] = a.note
            write(a.slug, state)
    receipt = _save_handoff(a.slug, "mid-build", f"python3 execution/job_board.py resume {a.slug}", unfinished)
    print(f"CHECKPOINT — {a.slug}: {receipt}")
    return 0


def cmd_resume(a):
    slug = a.slug
    state = read(slug)
    card = (mc.mission_dir(slug) / "card.md").read_text(encoding="utf-8")
    print(f"RESUME — {slug} ({state.get('status')}) · recipe {(state.get('job') or {}).get('recipe')} · "
          f"opened {(state.get('job') or {}).get('opened_at')} by {(state.get('job') or {}).get('opened_by')}")
    print(card.strip()[:4000])
    print("\n" + lane_table(state))
    tl = trace_lines(slug)
    if tl:
        print(f"\nTRACE (last {min(8, len(tl))} of {len(tl)}):")
        for l in tl[-8:]:
            print("  " + l[2:])
    print(f"plan: {plan_state(state)}")
    ops = open_packets(slug)
    if ops:
        print(f"\nDECISION PACKETS OPEN ({len(ops)}):")
        for p in ops:
            print(p["body"] + "\n")
    print()
    return cmd_next(argparse.Namespace(slug=slug))


def job_summary(slug: str) -> dict:
    state = read(slug)
    c = classify(state)
    owners = sorted({l.get("owner") or "" for l in lanes_of(state)} - {""})
    return {"slug": slug, "status": state.get("status"), "recipe": (state.get("job") or {}).get("recipe"),
            "lanes": len(lanes_of(state)), "runnable": len(c["runnable"]), "waiting_deps": len(c["waiting_deps"]),
            "blocked": len(c["blocked"]), "done": len(c["done"]), "packets": len(open_packets(slug)),
            "owners": owners, "opened": (state.get("job") or {}).get("opened_at", "")[:10],
            "plan": plan_state(state), "last": (trace_lines(slug) or ["- "])[-1][2:],
            "finished_unclosed": finished_unclosed(state)}


def cmd_status(a):
    slugs = [a.slug] if a.slug else job_slugs(include_closed=a.all)
    if getattr(a, "json", False):
        print(json.dumps([job_summary(s_) for s_ in slugs], indent=2))
        return 0
    if not slugs:
        print("JOBS: none open")
        return 0
    print(f"  board: {STATE_ROOT / '.agent' / 'missions'}" + ("" if STATE_ROOT == ROOT else f"  (shared with main; code from {ROOT.name})"))
    print("JOBS (manager loop) — lanes: runnable / queued / blocked-on-you / done · packets = decisions waiting")
    for s in slugs:
        j = job_summary(s)
        flag = ("  PLAN PENDING (say go)" if j["plan"] == "pending"
                else (f"  FINISHED, NOT CLOSED (job_board.py close {j['slug']} …)" if j["finished_unclosed"] else ""))
        print(f"  {j['slug']:<32} {j['status']:<9} {j['runnable']}/{j['waiting_deps']}/{j['blocked']}/{j['done']} of {j['lanes']}"
              f"  packets={j['packets']}  owners={','.join(j['owners']) or '—'}  opened {j['opened']}  recipe={j['recipe']}{flag}")
        if getattr(a, "trace", False) and j["last"]:
            print(f"      last: {j['last'][:150]}")
    return 0


def cmd_brief(_a=None):
    slugs = job_slugs()
    if not slugs:
        return 0
    js = [job_summary(s) for s in slugs]
    packets_total = sum(j["packets"] for j in js)
    runnable_total = sum(j["runnable"] for j in js if j["plan"] != "pending")
    plans_pending = sum(1 for j in js if j["plan"] == "pending")
    unclosed = sum(1 for j in js if j["finished_unclosed"])
    head = f"JOBS: {len(js)} open"
    if plans_pending:
        head += f" · {plans_pending} plan(s) waiting for your go"
    if unclosed:
        head += f" · {unclosed} finished but not closed"
    if packets_total:
        head += f" · {packets_total} decision packet(s) waiting for you"
    if runnable_total:
        head += f" · {runnable_total} lane(s) runnable"
    first = js[0]
    head += f" — {first['slug']} {first['done']}/{first['lanes']} done"
    print(head)
    for j in js[1:]:
        print(f"  {j['slug']} {j['done']}/{j['lanes']} done · packets={j['packets']}")
    return 0


def cmd_close(a):
    slug = a.slug
    state = read(slug)
    c = classify(state)
    if (c["runnable"] or c["waiting_deps"]) and not a.force:
        print(f"not closing — runnable/queued lanes remain: "
              f"{', '.join(l['id'] for l in c['runnable'] + c['waiting_deps'])} (mark them skipped, or --force)")
        return 1
    recipe = (state.get("job") or {}).get("recipe")
    receipts = "\n".join(f"- {l['id']} {l.get('workflow') or ''}: {l.get('status')} · {l.get('evidence_path') or 'no evidence path'}"
                         for l in lanes_of(state))
    closeout = (f"# Closeout — {slug} · {now_iso()} on {harness()}\n\n"
                f"Nate's four questions, answered with receipts.\n\n"
                f"1. **Is it done?** {a.done}\n\n{receipts}\n\n"
                f"2. **Did the actions line up with what he asked?** {a.aligned}\n\n"
                f"3. **Any unauthorized actions?** {a.unauthorized}\n\n"
                f"4. **Was he told each time approval was needed?** {a.approvals}\n\n"
                f"Verdict: {a.verdict or 'unasked'}\n")
    with locked(slug):
        state = read(slug)
        state["status"] = "complete"
        state.setdefault("job", {})["closed_at"] = now_iso()
        state["job"]["verdict"] = a.verdict
        write(slug, state)
        (mc.mission_dir(slug) / "closeout.md").write_text(closeout, encoding="utf-8")
        trace_add(slug, "-", "closed", f"done: {a.done} · verdict: {a.verdict or 'unasked'}")
    # ratchet the recipe (LIVING doc, updated in place)
    if recipe and rc.card_path(recipe).exists():
        p = rc.card_path(recipe)
        text = p.read_text(encoding="utf-8")
        today = _dt.date.today().isoformat()
        text = re.sub(r"^runs:\s*(\d+)", lambda m: f"runs: {int(m.group(1)) + 1}", text, count=1, flags=re.M)
        text = re.sub(r"^last_ratchet:.*$", f"last_ratchet: {today}", text, count=1, flags=re.M)
        if a.ratchet:
            text = text.replace("- none yet", f"- {today} — {a.ratchet}", 1) if "- none yet" in text \
                else text.rstrip("\n") + f"\n- {today} — {a.ratchet}\n"
        p.write_text(text, encoding="utf-8")
    append_mission_line(slug, "done", state.get("goal", slug), verdict=a.verdict,
                        outcome=a.done[:160])
    print(closeout)
    if not a.verdict:
        print("Verdict on this one — good / marginal / off?")
    return 0


def cmd_lint(a):
    slug = a.slug
    errs = []
    if not (mc.mission_dir(slug) / "card.md").exists():
        errs.append("card.md missing")
    if not mc.state_path(slug).exists():
        errs.append("mission.json missing")
    else:
        # read the RAW file here: mission_control.normalize silently resets an
        # illegal status to "planned", which is exactly what lint must catch.
        try:
            raw = json.loads(mc.state_path(slug).read_text(encoding="utf-8"))
        except Exception as exc:
            return_err = f"mission.json unreadable: {exc.__class__.__name__}"
            print(f"JOB LINT — {slug}: problems\n  {return_err}")
            return 1
        state = mc.normalize_state(raw)
        ids = {l.get("id") for l in lanes_of(state)}
        for l in (raw.get("activation_queue") or []):
            if isinstance(l, dict) and l.get("status") not in mc.ACTIVATION_STATUSES:
                errs.append(f"lane {l.get('id')}: illegal status {l.get('status')!r}")
        for l in lanes_of(state):
            for d in l.get("after") or []:
                if d not in ids:
                    errs.append(f"lane {l.get('id')}: depends on unknown lane {d}")
            if l.get("status") == "blocked" and not l.get("blocker"):
                errs.append(f"lane {l.get('id')}: blocked with no blocker named")
    ns = [p["n"] for p in packets(slug)]
    if ns != list(range(1, len(ns) + 1)):
        errs.append(f"decisions.md packets not numbered 1..n: {ns}")
    if errs:
        print(f"JOB LINT — {slug}: problems\n  " + "\n  ".join(errs))
        return 1
    print(f"JOB LINT — {slug}: clean")
    return 0


# ── main ──────────────────────────────────────────────────────────────────
def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv == ["--brief"]:
        return cmd_brief()
    ap = argparse.ArgumentParser(description="Manager-loop job board")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("open"); s.add_argument("slug"); s.add_argument("--recipe", required=True)
    s.add_argument("--goal"); s.add_argument("--owner", default=harness()); s.add_argument("--serves", default="orphan")
    s.add_argument("--mode", default="general", choices=["general", "client", "personal", "code", "research", "system"])
    s.add_argument("--force", action="store_true")
    s.add_argument("--go", action="store_true", help="skip the plan beat (his 'just do it')")
    s.add_argument("--ask", action="append", help="interview question that survived disk-first (repeatable)")
    s.add_argument("--found", action="append", help="'<path>: <answer>' found on disk instead of asked (repeatable)")
    s.set_defaults(fn=cmd_open)
    s = sub.add_parser("plan"); s.add_argument("slug"); s.set_defaults(fn=cmd_plan)
    s = sub.add_parser("go"); s.add_argument("slug"); s.add_argument("--note"); s.set_defaults(fn=cmd_go)
    s = sub.add_parser("log"); s.add_argument("slug"); s.add_argument("lane"); s.add_argument("text")
    s.add_argument("--kind", default="did", choices=["did", "found", "skipped", "note", "asked", "answered"])
    s.set_defaults(fn=cmd_log)
    s = sub.add_parser("trace"); s.add_argument("slug", nargs="?"); s.add_argument("--all", action="store_true")
    s.add_argument("--last", type=int, default=0); s.set_defaults(fn=cmd_trace)
    s = sub.add_parser("lanes"); s.add_argument("slug"); s.set_defaults(fn=cmd_lanes)
    s = sub.add_parser("lane"); s.add_argument("slug"); s.add_argument("id"); s.add_argument("--status")
    s.add_argument("--evidence"); s.add_argument("--did"); s.add_argument("--blocker"); s.add_argument("--owner")
    s.add_argument("--next"); s.set_defaults(fn=cmd_lane)
    s = sub.add_parser("next"); s.add_argument("slug"); s.set_defaults(fn=cmd_next)
    s = sub.add_parser("packet"); s.add_argument("slug"); s.add_argument("action", choices=["add", "answer", "list"])
    s.add_argument("n", nargs="?", type=int); s.add_argument("text", nargs="?")
    s.add_argument("--lane"); s.add_argument("--choice"); s.add_argument("--options"); s.add_argument("--recommend")
    s.add_argument("--irreversible"); s.add_argument("--if-none", dest="if_none"); s.set_defaults(fn=cmd_packet)
    s = sub.add_parser("checkpoint"); s.add_argument("slug"); s.add_argument("--note"); s.set_defaults(fn=cmd_checkpoint)
    s = sub.add_parser("handoff"); s.add_argument("slug"); s.add_argument("--to", required=True, choices=["codex", "claude", "chat"])
    s.set_defaults(fn=cmd_handoff)
    s = sub.add_parser("resume"); s.add_argument("slug"); s.set_defaults(fn=cmd_resume)
    s = sub.add_parser("status"); s.add_argument("slug", nargs="?"); s.add_argument("--all", action="store_true")
    s.add_argument("--trace", action="store_true", help="add each job's last trace line")
    s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_status)
    s = sub.add_parser("close"); s.add_argument("slug")
    for f in ("done", "aligned", "unauthorized", "approvals"):
        s.add_argument(f"--{f}", required=True)
    s.add_argument("--verdict", choices=["good", "marginal", "off"]); s.add_argument("--ratchet")
    s.add_argument("--force", action="store_true"); s.set_defaults(fn=cmd_close)
    s = sub.add_parser("lint"); s.add_argument("slug"); s.set_defaults(fn=cmd_lint)
    a = ap.parse_args(argv)
    return a.fn(a) or 0


if __name__ == "__main__":
    sys.exit(main())
