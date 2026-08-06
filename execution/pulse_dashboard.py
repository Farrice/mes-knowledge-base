#!/usr/bin/env python3
"""Pulse board generator — the operator console (Maestro layer, 2026-07-13;
cockpit+console rebuild 2026-08-06, Farrice-shaped).

Reads live system state and renders .agent/pulse/pulse-board.html.
Deterministic; no LLM. Design system: Farrice Cain Premium Minimal report
dialect (_active/farrice-brand/premium-minimal/REPORT-DIALECT.md) — light
canvas by default, Premium Minimal dark variant for dark mode.

Shape (Farrice, 2026-08-06): COCKPIT first (scoreboard · needs-you cards with
goal words + copy affordance · fresh intel from the Briefing Room), full
CONSOLE below (context-rich mission cards, collapsed history/threads).

Sources: .agent/missions.jsonl · .agent/cos/goals.json · .agent/jam/taste-ledger.jsonl
         .agent/handoffs (via handoff_store) · .agent/session.lock ·
         deliverables/research-briefs (via brief_library.collect)
"""
import html
import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, ".agent", "pulse", "pulse-board.html")


def jsonl(path):
    rows = []
    try:
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    pass
    except OSError:
        pass
    return rows


def esc(s):
    return html.escape(str(s or ""))


def pill(status):
    cls = {"running": "warn", "compiled": "warn", "waiting": "warn",
           "done": "ok", "stopped": "crit", "blocked": "crit"}.get(status, "muted")
    return f'<span class="pill {cls}">{esc(status)}</span>'


def mission_key(m):
    return m.get("slug") or " ".join((m.get("mission") or "?").split())


def mission_age_days(m):
    try:
        ts = m.get("ts", "")
        return max(0, int((time.time() - time.mktime(
            time.strptime(ts[:19], "%Y-%m-%dT%H:%M:%S"))) // 86400))
    except Exception:
        return None


def open_missions():
    """The open set — latest state per mission, keyed on slug (falls back to
    title). Apex W1 (2026-07-29): this calc existed only inside the HTML
    generator while 41 missions sat open unseen; now it's callable.
    Title-keying alone double-counted whitespace-variant titles."""
    missions = jsonl(os.path.join(ROOT, ".agent", "missions.jsonl"))
    latest = {}
    for m in missions:
        latest[mission_key(m)] = m
    out = []
    for key, m in latest.items():
        if m.get("status") in ("compiled", "running"):
            out.append({"key": key, "age_days": mission_age_days(m),
                        "serves": m.get("serves") or "?",
                        "title": (m.get("mission") or key)[:90]})
    out.sort(key=lambda r: -(r["age_days"] if r["age_days"] is not None else 0))
    return out


def cmd_open(alarm: bool) -> int:
    """Plain-text open-mission surface. House style (pending_decisions_hook):
    silent when healthy, one actionable line per item, exit 0 always.
    --alarm: print only when >=3 open or any open >7d (Farrice's finisher
    threshold, ruled 2026-07-29)."""
    rows = open_missions()
    stale = [r for r in rows if (r["age_days"] or 0) > 7]
    if alarm and len(rows) < 3 and not stale:
        return 0
    if not rows:
        if not alarm:
            print("OPEN MISSIONS: none — the log is clean.")
        return 0
    print(f"OPEN MISSIONS ({len(rows)} — finisher rule: at 3+, finish or /park one "
          "before opening another; never a block):")
    for r in rows[:10]:
        age = f"{r['age_days']}d" if r["age_days"] is not None else "?"
        print(f"  ⚠ {age:>4}  {r['title']}  (serves: {r['serves']})")
    if len(rows) > 10:
        print(f"  … +{len(rows) - 10} more — python3 execution/pulse_dashboard.py --open")
    return 0


def load_goals():
    try:
        goals = json.load(open(os.path.join(ROOT, ".agent", "cos", "goals.json"))).get("goals", [])
    except (OSError, ValueError):
        goals = []
    names = {}
    for g in goals:
        gid = g.get("id")
        if gid:
            names[gid] = str(g.get("target") or gid)
    return goals, names


def goal_words(names, gid):
    if not gid or gid in ("orphan", "?"):
        return "ORPHAN ⚑ — not tied to a goal yet"
    t = names.get(gid)
    if not t:
        return gid
    return t if len(t) <= 90 else t[:87] + "…"


def copy_target(m):
    """What the card's copy button yields: the mission's portable run-packet
    path when one exists (agent-feedable, the briefing-room path grammar),
    else the mission title for pasting into any session."""
    slug = m.get("slug")
    if slug:
        p = os.path.join(ROOT, ".agent", "missions", slug, "portable.md")
        if os.path.exists(p):
            return p, "copy packet"
    return (m.get("mission") or "?"), "copy mission"


def mission_card(m, names, show_verdict=False, show_actions=False, show_reopen=False):
    age = mission_age_days(m)
    age_html = f'<span class="m">{age}d old</span>' if age is not None else ""
    tier = f'<span class="m">{esc(m.get("tier"))}</span>' if m.get("tier") else ""
    pat = f'<span class="m">{esc(m.get("pattern"))}</span>' if m.get("pattern") else ""
    outcome = ""
    if m.get("outcome"):
        outcome = f'<p class="last">{esc(str(m["outcome"])[:180])}</p>'
    verdict = ""
    if show_verdict and m.get("verdict"):
        v = str(m["verdict"])
        vcls = {"good": "ok", "marginal": "warn", "off": "crit"}.get(v, "muted")
        verdict = f'<span class="pill {vcls}">{esc(v)}</span>'
    txt, label = copy_target(m)
    slug = esc(m.get("slug") or " ".join((m.get("mission") or "?").split()))
    actions = ""
    if show_actions:
        actions = (f'<button class="actbtn ok" type="button" data-action="done" data-slug="{slug}">✓ done</button>'
                   f'<button class="actbtn" type="button" data-action="park" data-slug="{slug}">park</button>')
    if show_reopen:
        actions += f'<button class="actbtn" type="button" data-action="reopen" data-slug="{slug}">↺ reopen</button>'
    return (f'<div class="mcard" data-goal="{esc(m.get("serves"))}">'
            f'<div class="row1"><h3>{esc(m.get("mission"))}</h3>{pill(m.get("status"))}{verdict}</div>'
            f'<div class="gline">{esc(goal_words(names, m.get("serves")))}</div>'
            f'{outcome}'
            f'<div class="meta">{age_html}{tier}{pat}'
            f'<span class="acts">{actions}'
            f'<button class="copybtn" type="button" data-copy="{esc(txt)}">{label}</button></span></div></div>')


def outcomes_due_cards():
    """Outcome check-ins as actionable cards, straight from the JSON (the CLI's
    `due` output truncates deliverables to 70 chars and is un-round-trippable)."""
    try:
        data = json.load(open(os.path.join(ROOT, ".agent", "revenue-outcomes.json"), encoding="utf-8"))
    except (OSError, ValueError):
        return "", 0
    today = time.strftime("%Y-%m-%d")
    due = [o for o in data.get("outcomes", [])
           if o.get("outcome_type") == "pending" and (o.get("check_in_date") or "9999") <= today]
    due.sort(key=lambda o: o.get("check_in_date") or "")
    cards = []
    for o in due[:10]:
        d = str(o.get("deliverable") or "?")
        exp = f'<p class="last">expected: {esc(o.get("expected_outcome"))}</p>' if o.get("expected_outcome") else ""
        cards.append(
            f'<div class="mcard" data-deliverable="{esc(d)}">'
            f'<div class="row1"><h3>{esc(d[:140])}</h3><span class="pill warn">due {esc(o.get("check_in_date"))}</span></div>'
            f'<div class="gline">delivered {esc(o.get("date"))}'
            + (f' · {esc(o.get("expert"))}' if o.get("expert") else "") + "</div>"
            f'{exp}'
            '<div class="meta"><span class="acts">'
            '<button class="actbtn ok" type="button" data-action="outcome">log outcome</button>'
            '<button class="actbtn" type="button" data-action="outcome-snooze">snooze +14d</button>'
            '<button class="actbtn" type="button" data-action="outcome-dismiss">no outcome</button>'
            "</span></div>"
            '<div class="oform"><input class="o-rev" type="number" step="any" placeholder="$ revenue (0 ok)">'
            '<input class="o-out" type="text" placeholder="what actually happened — one line">'
            '<button class="actbtn ok o-save" type="button">save</button></div></div>')
    more = f'<div class="empty">+{len(due) - 10} more — python3 execution/revenue_tracker.py due</div>' if len(due) > 10 else ""
    return ("".join(cards) + more) if cards else '<div class="empty">nothing due — outer loop is current</div>', len(due)


def thread_cards():
    """Handoff threads as resumable cards (module import — no CLI text parsing)."""
    try:
        sys.path.insert(0, os.path.join(ROOT, "execution"))
        import handoff_store as hs
        metas = hs.threads()[:10]
    except Exception:
        return '<div class="empty">handoff store unavailable</div>'
    if not metas:
        return '<div class="empty">no live threads</div>'
    from pathlib import Path as _P
    cards = []
    for m in metas:
        pin = " 📌" if m.get("pin") else ""
        scls = {"blocked": "crit", "mid-build": "warn", "ready": "ok", "active": "ok"}.get(m.get("status"), "muted")
        hint = f'<p class="last">↪ {esc(str(m.get("resume_hint"))[:160])}</p>' if m.get("resume_hint") else ""
        unf = f'<p class="last">⧗ {esc(str(m.get("unfinished"))[:160])}</p>' if m.get("unfinished") else ""
        try:
            open_uri = _P(m["path"]).as_uri()
        except Exception:
            open_uri = "#"
        cards.append(
            f'<div class="mcard" data-thread="{esc(m.get("thread"))}">'
            f'<div class="row1"><h3>{esc(m.get("thread"))}{pin}</h3>'
            f'<span class="pill {scls}">{esc(m.get("status"))}</span>'
            f'<span class="m">{esc(m.get("date"))}</span></div>'
            f'{hint}{unf}'
            f'<div class="meta"><span class="acts">'
            f'<button class="copybtn" type="button" data-copy="/resume {esc(m.get("thread"))}">copy /resume</button>'
            f'<a class="actbtn alink" href="{esc(open_uri)}">open</a>'
            f'<button class="actbtn" type="button" data-action="thread-archive">archive</button>'
            f"</span></div></div>")
    return "".join(cards)


def fresh_intel():
    """Newest briefs from the Briefing Room — links only, never a duplicate
    of the room (Farrice's two-surfaces ruling, 2026-08-06)."""
    try:
        sys.path.insert(0, os.path.join(ROOT, "execution"))
        import brief_library as bl
        entries = bl.collect()[:3]
    except Exception:
        return ""
    rows = []
    for e in entries:
        pri = f'<span class="pill warn">P{e["priority"]}</span>' if e.get("priority") else ""
        rows.append(
            f'<a class="intel" href="{esc(e["html"].as_uri())}">'
            f'<span class="ik">📋 {esc(e["category"])}</span>'
            f'<span class="it">{esc(str(e["title"]).replace("*", ""))}</span>'
            f'{pri}<span class="m">{esc(e["compiled"])}</span></a>')
    if not rows:
        return ""
    room = os.path.join(ROOT, "deliverables", "research-briefs", "index.html")
    from pathlib import Path as _P
    return (f'<section><h2 class="tog">Fresh intel — from the briefing room</h2>'
            f'<div class="intelgrid f">{"".join(rows)}</div>'
            f'<a class="roomlink" href="{esc(_P(room).as_uri())}">open the briefing room ↗</a></section>')


def main():
    if "--open" in sys.argv:
        raise SystemExit(cmd_open(alarm="--alarm" in sys.argv))
    now = time.strftime("%Y-%m-%d %H:%M")
    missions = jsonl(os.path.join(ROOT, ".agent", "missions.jsonl"))
    latest = {}
    for m in missions:
        latest[mission_key(m)] = m
    active = [m for m in latest.values() if m.get("status") in ("compiled", "running")]
    active.sort(key=lambda m: -(mission_age_days(m) or 0))
    recent_done = [m for m in latest.values() if m.get("status") == "done"][-6:][::-1]

    goals, names = load_goals()
    sprint = next((g for g in goals if "SPRINT" in (g.get("why") or "")), None)

    taste = jsonl(os.path.join(ROOT, ".agent", "jam", "taste-ledger.jsonl"))

    outcomes_html, due_count = outcomes_due_cards()

    try:
        import importlib.util as _iu
        spec = _iu.spec_from_file_location("ra", os.path.join(ROOT, "execution", "renaissance_audit.py"))
        ra = _iu.module_from_spec(spec); spec.loader.exec_module(ra)
        _files = ra.v2_files()
        _fails = sum(1 for f in _files if ra.audit_file(f))
        corpus = f"{len(_files) - _fails}/{len(_files)}"
        corpus_ok = _fails == 0
    except Exception:
        corpus, corpus_ok = "?", True

    threads_html = thread_cards()

    lock = None
    try:
        lock = json.load(open(os.path.join(ROOT, ".agent", "session.lock")))
    except (OSError, ValueError):
        pass

    # Needs-you = T2/T3 compiled (explicitly awaiting his sign-off) first,
    # then the stalest open missions at the 7-day finisher threshold.
    # Tier match is prefix-loose: records carry values like "T2 waiting".
    def _t23(m):
        return str(m.get("tier") or "").upper().startswith(("T2", "T3"))
    waiting = [m for m in latest.values() if _t23(m) and m.get("status") == "compiled"]
    stale = [m for m in active if (mission_age_days(m) or 0) >= 7 and m not in waiting]
    needs_you = (waiting + stale)[:3]

    goal_ids = sorted({m.get("serves", "?") for m in latest.values()})
    chips = '<button class="chip active" data-f="all">all</button>' + "".join(
        f'<button class="chip" data-f="{esc(g)}">{esc(g)}</button>' for g in goal_ids)

    sprint_html = ""
    if sprint:
        import re as _re
        mm = _re.search(r"~(\d{2})-(\d{2})", sprint.get("why", ""))
        cd = ""
        if mm and 1 <= int(mm.group(1)) <= 12:
            year = time.strftime("%Y")
            deadline = time.mktime(time.strptime(f"{year}-{mm.group(1)}-{mm.group(2)}", "%Y-%m-%d"))
            days = int((deadline - time.time()) // 86400)
            if 0 <= days <= 366:
                cd = f'<span class="pill warn">{days} days left</span>'
        sprint_html = (f'<div class="sprint"><span class="sprint-tag">ACTIVE SPRINT</span>'
                       f'<strong>{esc(sprint.get("target"))}</strong>{cd}'
                       f'<span class="m">goal: {esc(sprint.get("id"))}</span></div>')

    lock_html = (f'<span class="pill warn">lock: {esc(lock["mission"])}</span>' if lock
                 else '<span class="pill ok">tree: single driver</span>')

    def cards(ms, show_verdict=False, show_actions=False, show_reopen=False):
        if not ms:
            return '<div class="empty">none — clean</div>'
        return "".join(mission_card(m, names, show_verdict, show_actions, show_reopen) for m in ms)

    from pathlib import Path as _P
    room_uri = _P(os.path.join(ROOT, "deliverables", "research-briefs", "index.html")).as_uri()
    board_uri = _P(os.path.join(ROOT, ".agent", "assets", "assets-board.html")).as_uri()

    body = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>the pulse · Antigravity</title>
<style>
/* ── Farrice Cain Premium Minimal — report dialect (_active/farrice-brand/premium-minimal/) ── */
:root {{
  --ground:#f3f3f0; --panel:#fafaf8; --ink:#101010; --muted:#8c8c82; --soft:#555553; --line:#d8d8d3;
  --accent:#3d5a94; --ok:#3e7d5f; --warn:#a8853e; --crit:#a85454;
  --mono:'JetBrains Mono',ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --sans:'Helvetica Neue','Neue Haas Grotesk Text Pro',Helvetica,Inter,system-ui,sans-serif;
  --serif:'Source Serif 4',Georgia,serif;
}}
@media (prefers-color-scheme: dark) {{ :root {{
  --ground:#0e0e0d; --panel:#181817; --ink:#fafaf8; --muted:#8c8c82; --soft:#b9b9b2; --line:#2c2c2a;
  --accent:#7c9fd9; --ok:#6fae8c; --warn:#c9a868; --crit:#c97b73;
}} }}
:root[data-theme="dark"] {{
  --ground:#0e0e0d; --panel:#181817; --ink:#fafaf8; --muted:#8c8c82; --soft:#b9b9b2; --line:#2c2c2a;
  --accent:#7c9fd9; --ok:#6fae8c; --warn:#c9a868; --crit:#c97b73;
}}
:root[data-theme="light"] {{
  --ground:#f3f3f0; --panel:#fafaf8; --ink:#101010; --muted:#8c8c82; --soft:#555553; --line:#d8d8d3;
  --accent:#3d5a94; --ok:#3e7d5f; --warn:#a8853e; --crit:#a85454;
}}
* {{ box-sizing:border-box; }}
body {{ background:var(--ground); color:var(--ink); font:14px/1.5 var(--sans); margin:0; padding:40px 24px 80px; }}
.wrap {{ max-width:960px; margin:0 auto; display:flex; flex-direction:column; gap:18px; }}
header {{ display:flex; align-items:baseline; gap:14px; flex-wrap:wrap; }}
.kicker {{ font-family:var(--mono); font-size:9px; letter-spacing:.22em; text-transform:uppercase; color:var(--muted); display:block; margin-bottom:8px; }}
h1 {{ font-size:38px; font-weight:700; letter-spacing:-.022em; margin:0; line-height:1.05; }}
h1 em {{ font-family:var(--serif); font-style:italic; font-weight:400; color:var(--accent); }}
.homenav {{ margin-left:auto; display:flex; gap:6px; align-items:center; }}
.homenav a {{ font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; text-decoration:none;
  color:var(--soft); border:1px solid var(--line); border-radius:99px; padding:4px 11px; }}
.homenav a:hover {{ border-color:var(--accent); color:var(--accent); }}
.stamp {{ color:var(--muted); font-family:var(--mono); font-size:10px; letter-spacing:.1em; text-transform:uppercase;
  display:flex; gap:10px; align-items:center; flex-wrap:wrap; border-top:1px solid var(--ink); padding-top:10px; }}
.sprint {{ background:var(--panel); border:1px solid var(--accent); border-radius:8px; padding:12px 16px;
  display:flex; gap:12px; align-items:baseline; flex-wrap:wrap; }}
.sprint-tag {{ font-family:var(--mono); font-size:9px; letter-spacing:.18em; color:var(--accent); text-transform:uppercase; }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; }}
.tile {{ border-top:2px solid var(--ink); padding-top:10px; }}
.tile .n {{ font-size:28px; font-weight:700; letter-spacing:-.02em; font-variant-numeric:tabular-nums; }}
.tile .l {{ color:var(--muted); font-family:var(--mono); font-size:8.5px; letter-spacing:.16em; text-transform:uppercase; margin-top:4px; }}
section {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:16px 18px; }}
h2 {{ font-family:var(--mono); font-size:9px; letter-spacing:.2em; text-transform:uppercase;
  color:var(--muted); margin:0 0 12px; border-bottom:1px solid var(--line); padding-bottom:8px; }}
.mcard {{ border:1px solid var(--line); border-radius:6px; background:var(--ground); padding:12px 14px; margin-bottom:10px; }}
.mcard:last-child {{ margin-bottom:0; }}
.mcard .row1 {{ display:flex; gap:10px; align-items:baseline; flex-wrap:wrap; }}
.mcard h3 {{ font-size:13.5px; font-weight:600; margin:0; line-height:1.35; flex:1; min-width:200px; }}
.mcard .gline {{ font-size:11.5px; color:var(--soft); margin-top:5px; }}
.mcard .gline::before {{ content:"goal · "; font-family:var(--mono); font-size:8.5px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--muted); }}
.mcard .last {{ font-size:11.5px; color:var(--muted); margin:5px 0 0; line-height:1.45; }}
.mcard .meta {{ display:flex; gap:12px; align-items:center; margin-top:8px; flex-wrap:wrap; }}
.m {{ font-family:var(--mono); font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }}
.pill {{ font-family:var(--mono); font-size:8px; letter-spacing:.12em; text-transform:uppercase; padding:2px 8px;
  border-radius:3px; white-space:nowrap; font-weight:700; }}
.pill.ok {{ color:var(--ok); border:1px solid var(--ok); }}
.pill.warn {{ color:var(--warn); border:1px solid var(--warn); }}
.pill.crit {{ color:var(--crit); border:1px solid var(--crit); }}
.pill.muted {{ color:var(--muted); border:1px solid var(--line); }}
.acts {{ margin-left:auto; display:flex; gap:6px; align-items:center; flex-wrap:wrap; }}
.copybtn, .actbtn {{ font-family:var(--mono); font-size:8.5px; letter-spacing:.12em; text-transform:uppercase;
  cursor:pointer; background:none; border:1px solid var(--line); border-radius:4px; padding:3px 9px; color:var(--soft);
  text-decoration:none; display:inline-block; }}
.copybtn:hover, .actbtn:hover {{ border-color:var(--accent); color:var(--accent); }}
.actbtn.ok {{ color:var(--ok); border-color:var(--ok); }}
.actbtn.ok:hover {{ background:var(--ok); color:var(--panel); }}
.oform {{ display:none; gap:8px; margin-top:10px; flex-wrap:wrap; }}
.oform.show {{ display:flex; }}
.oform input {{ font-family:var(--mono); font-size:11px; background:var(--panel); color:var(--ink);
  border:1px solid var(--line); border-radius:4px; padding:6px 9px; }}
.oform .o-rev {{ width:120px; }}
.oform .o-out {{ flex:1; min-width:200px; }}
.livechip {{ font-family:var(--mono); font-size:8px; letter-spacing:.14em; text-transform:uppercase; padding:2px 8px;
  border-radius:3px; font-weight:700; }}
.intelgrid {{ display:flex; flex-direction:column; gap:8px; }}
.intel {{ display:flex; gap:12px; align-items:baseline; text-decoration:none; color:var(--ink);
  border:1px solid var(--line); border-radius:6px; background:var(--ground); padding:10px 14px; flex-wrap:wrap; }}
.intel:hover {{ border-color:var(--accent); }}
.intel .ik {{ font-family:var(--mono); font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--accent); }}
.intel .it {{ font-size:13px; font-weight:600; flex:1; min-width:200px; }}
.roomlink {{ display:inline-block; margin-top:10px; font-family:var(--mono); font-size:9px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--accent); text-decoration:none; }}
.roomlink:hover {{ text-decoration:underline; }}
.empty {{ color:var(--muted); font-style:italic; font-size:12.5px; }}
pre {{ overflow-x:auto; font-family:var(--mono); font-size:11px; color:var(--soft); margin:0; line-height:1.7; }}
.chips {{ display:flex; gap:8px; flex-wrap:wrap; }}
.chip {{ font-family:var(--mono); font-size:9px; letter-spacing:.1em; text-transform:uppercase; padding:4px 12px;
  border-radius:99px; border:1px solid var(--line); background:var(--panel); color:var(--soft); cursor:pointer; }}
.chip.active {{ border-color:var(--accent); color:var(--accent); }}
.tog {{ cursor:pointer; user-select:none; }}
.tog::before {{ content:"▾ "; color:var(--accent); }}
section.closed .tog {{ margin-bottom:0; border-bottom:none; padding-bottom:0; }}
section.closed .tog::before {{ content:"▸ "; }}
section.closed .body {{ display:none; }}
#toast {{ position:fixed; bottom:24px; left:50%; transform:translateX(-50%); background:var(--ink); color:var(--panel);
  font-family:var(--mono); font-size:10px; letter-spacing:.14em; text-transform:uppercase; padding:9px 20px;
  border-radius:99px; opacity:0; transition:opacity .2s; pointer-events:none; z-index:99; }}
#toast.show {{ opacity:1; }}
footer {{ border-top:1px solid var(--ink); padding-top:12px; display:flex; justify-content:space-between;
  font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }}
</style>
<div class="wrap">
<header>
  <div><span class="kicker">ANTIGRAVITY · OPERATOR CONSOLE</span><h1>the <em>pulse</em></h1></div>
  <span class="homenav"><a href="{esc(room_uri)}">📋 briefing room ↗</a><a href="{esc(board_uri)}">🎨 asset board ↗</a></span>
</header>
<div class="stamp"><span>{now}</span>{lock_html}<span class="livechip pill muted" id="livechip">static — actions copy commands</span></div>
{sprint_html}
<div class="tiles">
  <div class="tile"><div class="n">{len(active)}</div><div class="l">missions live</div></div>
  <div class="tile"><div class="n">{len(needs_you)}</div><div class="l">need you now</div></div>
  <div class="tile"><div class="n">{due_count}</div><div class="l">outcomes due</div></div>
  <div class="tile"><div class="n">{len(taste)}</div><div class="l">taste verdicts banked</div></div>
  <div class="tile"><div class="n" style="color:var(--{'ok' if corpus_ok else 'crit'})">{corpus}</div><div class="l">v2 corpus pass</div></div>
</div>
<section><h2 class="tog">⚑ Needs you — top {len(needs_you)}</h2><div class="body">{cards(needs_you, show_actions=True)}</div></section>
{fresh_intel()}
<div class="chips">{chips}</div>
<section><h2 class="tog">Missions — live ({len(active)})</h2><div class="body f">{cards(active, show_actions=True)}</div></section>
<section class="closed"><h2 class="tog">Recently closed</h2><div class="body f">{cards(recent_done, show_verdict=True, show_reopen=True)}</div></section>
<section class="closed"><h2 class="tog">Outcomes due ({due_count})</h2><div class="body">{outcomes_html}</div></section>
<section class="closed"><h2 class="tog">Threads (handoff store)</h2><div class="body">{threads_html}</div></section>
<footer><span>ANTIGRAVITY PULSE</span><span>@farricecain</span></footer>
</div>
<div id="toast">copied</div>
<script>
const PULSE_LIVE = location.protocol.startsWith('http');
if (PULSE_LIVE) {{
  const lc = document.getElementById('livechip');
  lc.textContent = 'live — actions write instantly';
  lc.classList.remove('muted'); lc.classList.add('ok');
}}
function _toast(msg) {{
  const t = document.getElementById('toast'); t.textContent = msg; t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 1600);
}}
function _copy(txt, msg) {{
  function done() {{ _toast(msg || 'copied'); }}
  if (navigator.clipboard && navigator.clipboard.writeText) {{
    navigator.clipboard.writeText(txt).then(done, () => {{
      const ta = document.createElement('textarea'); ta.value = txt; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try {{ document.execCommand('copy'); }} catch (e) {{}}
      document.body.removeChild(ta); done();
    }});
  }}
}}
function _sq(s) {{ return "'" + String(s).replace(/'/g, `'\\''`) + "'"; }}
function _cli(action, args) {{
  const base = 'python3 execution/pulse_actions.py ';
  if (action === 'done') return base + 'done ' + _sq(args.slug) + ' --outcome ' + _sq(args.outcome || '');
  if (action === 'park') return base + 'park ' + _sq(args.slug) + ' --reason ' + _sq(args.reason || '');
  if (action === 'reopen') return base + 'reopen ' + _sq(args.slug);
  if (action === 'outcome') return base + 'outcome ' + _sq(args.deliverable) + ' --revenue ' + (args.revenue || 0) + ' --outcome ' + _sq(args.outcome || '');
  if (action === 'outcome-snooze') return base + 'outcome-snooze ' + _sq(args.deliverable);
  if (action === 'outcome-dismiss') return base + 'outcome-dismiss ' + _sq(args.deliverable);
  if (action === 'thread-archive') return base + 'thread-archive ' + _sq(args.thread);
  return base;
}}
function doAction(action, args) {{
  if (!PULSE_LIVE) {{ _copy(_cli(action, args), 'server offline — command copied'); return; }}
  fetch('/action', {{ method: 'POST', headers: {{ 'Content-Type': 'application/json' }},
                     body: JSON.stringify({{ action, args }}) }})
    .then(r => r.json())
    .then(j => {{
      if (j.ok) {{ _toast('done — refreshing'); setTimeout(() => location.reload(), 700); }}
      else {{ _toast('action failed — see server log'); }}
    }})
    .catch(() => {{ _copy(_cli(action, args), 'server unreachable — command copied'); }});
}}
document.querySelectorAll('.actbtn[data-action]').forEach(b => b.addEventListener('click', () => {{
  const card = b.closest('.mcard');
  const act = b.dataset.action;
  if (act === 'done') {{
    const outcome = prompt('One-line outcome for the log:', 'closed from pulse board');
    if (outcome === null) return;
    doAction('done', {{ slug: b.dataset.slug, outcome }});
  }} else if (act === 'park') {{
    const reason = prompt('Park reason (one line):');
    if (reason === null) return;
    doAction('park', {{ slug: b.dataset.slug, reason }});
  }} else if (act === 'reopen') {{
    doAction('reopen', {{ slug: b.dataset.slug }});
  }} else if (act === 'outcome') {{
    card.querySelector('.oform').classList.toggle('show');
  }} else if (act === 'outcome-snooze') {{
    doAction('outcome-snooze', {{ deliverable: card.dataset.deliverable }});
  }} else if (act === 'outcome-dismiss') {{
    if (confirm('Mark as no-outcome-expected? (writes archived-no-data)'))
      doAction('outcome-dismiss', {{ deliverable: card.dataset.deliverable }});
  }} else if (act === 'thread-archive') {{
    if (confirm('Archive this thread? (moves the handoff to archive/)'))
      doAction('thread-archive', {{ thread: card.dataset.thread }});
  }}
}}));
document.querySelectorAll('.o-save').forEach(b => b.addEventListener('click', () => {{
  const card = b.closest('.mcard');
  doAction('outcome', {{ deliverable: card.dataset.deliverable,
                        revenue: parseFloat(card.querySelector('.o-rev').value) || 0,
                        outcome: card.querySelector('.o-out').value || '' }});
}}));
document.querySelectorAll('.copybtn').forEach(b => b.addEventListener('click', () => {{
  if (b.dataset.copy !== undefined) _copy(b.dataset.copy);
}}));
if (PULSE_LIVE) {{
  // http pages cannot navigate to file:// — route those clicks through the server's OS opener.
  document.querySelectorAll('a[href^="file:"]').forEach(a => a.addEventListener('click', ev => {{
    ev.preventDefault();
    fetch('/action', {{ method: 'POST', headers: {{ 'Content-Type': 'application/json' }},
                       body: JSON.stringify({{ action: 'open-path', args: {{ uri: a.href }} }}) }})
      .then(r => r.json()).then(j => _toast(j.ok ? 'opened' : 'open failed'))
      .catch(() => _toast('open failed'));
  }}));
}}
document.querySelectorAll(".chip").forEach(c => c.addEventListener("click", () => {{
  document.querySelectorAll(".chip").forEach(x => x.classList.remove("active"));
  c.classList.add("active");
  const f = c.dataset.f;
  document.querySelectorAll(".body.f .mcard[data-goal]").forEach(r =>
    r.style.display = (f === "all" || r.dataset.goal === f) ? "" : "none");
}}));
document.querySelectorAll(".tog").forEach(h => h.addEventListener("click", () =>
  h.closest("section").classList.toggle("closed")));
</script>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(body)
    print(f"pulse board → {OUT}")


if __name__ == "__main__":
    main()
