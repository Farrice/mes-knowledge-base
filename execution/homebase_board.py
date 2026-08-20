#!/usr/bin/env python3
"""homebase_board.py — THE hub surface of the Readout OS (2026-08-20).

Renders .agent/homebase/homebase.html: the one page Farrice opens to work —
FOCUS (sprint, money, missions that need him), LIBRARY (fresh briefs, asset
shelf, what the system holds), LAUNCH (resumable work threads with one-click
copy prompts). Served at / by pulse_serve.py; every deeper surface is one nav
hop away. Fills the operator-cockpit-v2 shell that was named 2026-08 and never
built.

WHY (Farrice, 2026-08-20, verbatim): "a full working assets or homebase I can
rely on and can consistently work with or from so I have an actual system and
not context switching… work more fluently and easily without having to keep
switching between different tabs."

Doctrine (docs/solutions/2026-08-06-live-local-board-pattern.md):
- Reads .agent/sweep/latest.json + existing ledgers — NEVER a second collector.
- Reuses pulse_dashboard's readers/cards — one calc per fact, everywhere.
- Dual-mode JS: served → POST /action; file:// → buttons copy the honest CLI.
Design: Farrice Cain Premium Minimal report dialect. The asset shelf is the
one sanctioned dark interruption in the sequence.
"""
import html
import json
import os
import sys
import time
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "execution"))

import pulse_dashboard as pd  # noqa: E402 — shared readers/cards, one source of calc
from degrade import degraded, degraded_html  # noqa: E402

OUT = os.path.join(ROOT, ".agent", "homebase", "homebase.html")
SWEEP = os.path.join(ROOT, ".agent", "sweep", "latest.json")


def esc(s):
    return html.escape(str(s or ""))


def _rel(p):
    """Repo-relative posix path for dual-mode media/link resolution."""
    try:
        return Path(p).resolve().relative_to(Path(ROOT).resolve()).as_posix()
    except ValueError:
        return None


def _age_words(iso):
    try:
        t = time.mktime(time.strptime(iso[:19], "%Y-%m-%dT%H:%M:%S"))
        h = max(0, int((time.time() - t) // 3600))
        return f"{h}h ago" if h < 48 else f"{h // 24}d ago"
    except Exception:
        return "age unknown"


def load_sweep():
    try:
        return json.load(open(SWEEP, encoding="utf-8"))
    except (OSError, ValueError) as e:
        return degraded(None, "sweep bundle unreadable — launch zone degrades", e)


def launch_cards(sweep):
    """Resumable work threads from the sweep bundle (promotion bar already
    applied there — activity never mints a card). Pinned first, then status."""
    if not sweep:
        return degraded_html(
            "launch zone unavailable — .agent/sweep/latest.json unreadable; "
            "run python3 execution/session_sweep.py run", None)
    threads = list((sweep.get("threads") or {}).values())
    rank = {"blocked": 0, "mid-build": 1, "active": 2, "ready": 3}
    threads.sort(key=lambda t: (0 if t.get("pin") else 1,
                                rank.get(t.get("status"), 2)))
    cards = []
    for t in threads[:12]:
        slug = t.get("slug") or "?"
        pin = " 📌" if t.get("pin") else ""
        scls = {"blocked": "crit", "mid-build": "warn", "ready": "ok",
                "active": "ok"}.get(t.get("status"), "muted")
        hint = t.get("resume_hint") or ""
        hint_html = (f'<p class="last">↪ {esc(hint[:150])}</p>'
                     if hint and hint != t.get("title") else "")
        unf = (f'<p class="last">⧗ {esc(str(t.get("unfinished"))[:150])}</p>'
               if t.get("unfinished") else "")
        made = []
        if t.get("deliverables"):
            made.append(f'{len(t["deliverables"])} deliverable(s)')
        if t.get("assets"):
            made.append(f'{len(t["assets"])} asset(s)')
        if t.get("sessions"):
            made.append(f'{len(t["sessions"])} session(s)')
        open_btn = ""
        handoff = t.get("handoff")
        if handoff:
            try:
                open_btn = (f'<a class="actbtn alink" href='
                            f'"{esc((Path(ROOT) / handoff).as_uri())}">open handoff</a>')
            except Exception:
                open_btn = ""
        cards.append(
            f'<div class="mcard">'
            f'<div class="row1"><h3>{esc(str(t.get("title") or slug)[:120])}{pin}</h3>'
            f'<span class="pill {scls}">{esc(t.get("status"))}</span></div>'
            f'{hint_html}{unf}'
            f'<div class="meta"><span class="m">{esc(" · ".join(made))}</span>'
            f'<span class="acts">'
            f'<button class="copybtn" type="button" data-copy="/resume {esc(slug)}">copy /resume</button>'
            f'{open_btn}</span></div></div>')
    return "".join(cards) or '<div class="empty">no promoted threads in the sweep window</div>'


def asset_shelf():
    """The dark interruption: newest visual assets straight off the manifest.
    Thumbs resolve dual-mode via data-rel (live → /repo/, file:// → absolute)."""
    try:
        from asset_index import reduced_manifest
        from asset_gallery import thumb_name
        rows = [r for r in reduced_manifest().values()
                if r.get("status", "active") == "active"
                and r.get("type") in ("image", "video") and r.get("keep") is not False]
    except Exception as e:
        return degraded_html("asset shelf unavailable — asset_index failed; "
                             "run python3 execution/asset_index.py", e), 0
    total = len(rows)
    rows.sort(key=lambda r: r.get("ts") or "", reverse=True)
    tiles = []
    for r in rows[:8]:
        rel = str(r.get("path") or "")
        thumb_rel = f".agent/assets/thumbs/{thumb_name(rel)}"
        if not os.path.isfile(os.path.join(ROOT, thumb_rel)):
            continue
        label = (r.get("project") or r.get("zone") or "").replace("-", " ")[:24]
        kind = "▶" if r.get("type") == "video" else ""
        tiles.append(
            f'<a class="shelf-tile" href="{esc((Path(ROOT) / rel).as_uri())}" title="{esc(rel)}">'
            f'<img data-rel="{esc(thumb_rel)}" alt="{esc(label)}" loading="lazy">'
            f'<span class="shelf-cap">{kind} {esc(label)}</span></a>')
        if len(tiles) == 8:
            break
    if not tiles:
        return '<div class="empty">no thumbed assets yet — run python3 execution/asset_gallery.py</div>', total
    return "".join(tiles), total


def brief_rows():
    try:
        import brief_library as bl
        entries = [e for e in bl.collect() if e.get("status") != "archived"][:5]
    except Exception as e:
        return degraded_html("briefing room index unavailable — "
                             "run python3 execution/brief_library.py audit", e), 0, 0
    try:
        all_count = len(bl.collect())
    except Exception:
        all_count = len(entries)
    rows = []
    for e in entries:
        pri = f'<span class="pill warn">P{e["priority"]}</span>' if e.get("priority") else ""
        rows.append(
            f'<a class="intel" href="{esc(Path(e["html"]).as_uri())}">'
            f'<span class="ik">📋 {esc(e["category"])}</span>'
            f'<span class="it">{esc(str(e["title"]).replace("*", ""))}</span>'
            f'{pri}<span class="m">{esc(e["compiled"])}</span></a>')
    return "".join(rows) or '<div class="empty">no briefs yet</div>', all_count, len(entries)


def system_counts():
    try:
        h = json.load(open(os.path.join(ROOT, ".agent", "health", "latest.json"),
                           encoding="utf-8"))
        a = h.get("assets") or {}
        return {"skills": a.get("skills"), "workflows": a.get("workflows"),
                "scripts": a.get("execution_scripts"), "solutions": a.get("solution_cards")}
    except (OSError, ValueError) as e:
        return degraded({}, "health receipt unreadable — system counts unknown", e)


def main():
    now = time.strftime("%Y-%m-%d %H:%M")
    sweep = load_sweep()
    sweep_age = _age_words(sweep.get("generated", "")) if sweep else "unknown"
    counts = (sweep or {}).get("counts") or {}

    # --- FOCUS: reuse the Pulse's own calcs — one source per fact ---
    missions = pd.jsonl(os.path.join(ROOT, ".agent", "missions.jsonl"))
    latest = {}
    for m in missions:
        latest[pd.mission_key(m)] = m
    active = [m for m in latest.values() if m.get("status") in ("compiled", "running")]
    active.sort(key=lambda m: -(pd.mission_age_days(m) or 0))
    goals, names = pd.load_goals()
    sprint = next((g for g in goals if "SPRINT" in (g.get("why") or "")), None)
    sprint_id = (sprint or {}).get("id")

    def _t23(m):
        return str(m.get("tier") or "").upper().startswith(("T2", "T3"))
    waiting = [m for m in latest.values() if _t23(m) and m.get("status") == "compiled"]
    stale = [m for m in active if (pd.mission_age_days(m) or 0) >= 7 and m not in waiting]
    flagged = waiting + stale
    flagged.sort(key=lambda m: (0 if (sprint_id and m.get("serves") == sprint_id) else 1,
                                0 if _t23(m) else 1,
                                -(pd.mission_age_days(m) or 0)))
    needs_you = flagged[:3]
    needs_html = ("".join(pd.mission_card(m, names, show_actions=True) for m in needs_you)
                  or '<div class="empty">nothing flagged — clean</div>')

    _, due_count = pd.outcomes_due_cards()

    sprint_html = ""
    if sprint:
        import re as _re
        mm = _re.search(r"~(\d{2})-(\d{2})", sprint.get("why", ""))
        cd = ""
        if mm and 1 <= int(mm.group(1)) <= 12:
            deadline = time.mktime(time.strptime(
                f"{time.strftime('%Y')}-{mm.group(1)}-{mm.group(2)}", "%Y-%m-%d"))
            days = int((deadline - time.time()) // 86400)
            if 0 <= days <= 366:
                cd = f'<span class="pill warn">{days} days left</span>'
        sprint_html = (f'<div class="sprint"><span class="sprint-tag">ACTIVE SPRINT</span>'
                       f'<strong>{esc(sprint.get("target"))}</strong>{cd}'
                       f'{pd.money_line()}</div>')

    # --- LIBRARY ---
    briefs_html, brief_total, _shown = brief_rows()
    shelf_html, asset_total = asset_shelf()
    sc = system_counts()
    sys_line = " · ".join(f"{v:,} {k}" for k, v in sc.items() if v) if sc else ""

    # --- LAUNCH ---
    launch_html = launch_cards(sweep)
    threads_promoted = counts.get("threads_promoted", "?")

    room_uri = Path(ROOT, "deliverables", "research-briefs", "index.html").as_uri()
    board_uri = Path(ROOT, ".agent", "assets", "assets-board.html").as_uri()
    missions_uri = Path(ROOT, ".agent", "missions", "mission-control.html").as_uri()

    body = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>homebase · Antigravity</title>
<style>
/* ── Farrice Cain Premium Minimal — report dialect ── */
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
.homenav {{ margin-left:auto; display:flex; gap:6px; align-items:center; flex-wrap:wrap; }}
.homenav a, .homenav .here {{ font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; text-decoration:none;
  color:var(--soft); border:1px solid var(--line); border-radius:99px; padding:4px 11px; }}
.homenav a:hover {{ border-color:var(--accent); color:var(--accent); }}
.homenav .here {{ opacity:.45; border-style:dashed; }}
.stamp {{ color:var(--muted); font-family:var(--mono); font-size:10px; letter-spacing:.1em; text-transform:uppercase;
  display:flex; gap:10px; align-items:center; flex-wrap:wrap; border-top:1px solid var(--ink); padding-top:10px; }}
.zone {{ font-family:var(--mono); font-size:9px; letter-spacing:.26em; text-transform:uppercase; color:var(--accent);
  margin:8px 0 -8px; }}
.sprint {{ background:var(--panel); border:1px solid var(--accent); border-radius:8px; padding:12px 16px;
  display:flex; gap:12px; align-items:baseline; flex-wrap:wrap; }}
.sprint-tag {{ font-family:var(--mono); font-size:9px; letter-spacing:.18em; color:var(--accent); text-transform:uppercase; }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(140px,1fr)); gap:12px; }}
.tile {{ border-top:2px solid var(--ink); padding-top:10px; }}
.tile a {{ color:inherit; text-decoration:none; }}
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
.livechip {{ font-family:var(--mono); font-size:8px; letter-spacing:.14em; text-transform:uppercase; padding:2px 8px;
  border-radius:3px; font-weight:700; }}
.intelgrid {{ display:flex; flex-direction:column; gap:8px; }}
.intel {{ display:flex; gap:12px; align-items:baseline; text-decoration:none; color:var(--ink);
  border:1px solid var(--line); border-radius:6px; background:var(--ground); padding:10px 14px; flex-wrap:wrap; }}
.intel:hover {{ border-color:var(--accent); }}
.intel .ik {{ font-family:var(--mono); font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--accent); }}
.intel .it {{ font-size:13px; font-weight:600; flex:1; min-width:200px; }}
.roomlink {{ display:inline-block; margin-top:10px; margin-right:16px; font-family:var(--mono); font-size:9px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--accent); text-decoration:none; }}
.roomlink:hover {{ text-decoration:underline; }}
.empty {{ color:var(--muted); font-style:italic; font-size:12.5px; }}
/* the ONE dark interruption — asset shelf */
section.shelf {{ background:#101010; border-color:#101010; }}
section.shelf h2 {{ color:#8c8c82; border-color:#2c2c2a; }}
.shelfgrid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(150px,1fr)); gap:10px; }}
.shelf-tile {{ display:block; text-decoration:none; border-radius:6px; overflow:hidden; background:#181817;
  border:1px solid #2c2c2a; transition:transform .15s ease; }}
.shelf-tile:hover {{ transform:scale(1.03); border-color:#7c9fd9; }}
.shelf-tile img {{ width:100%; aspect-ratio:4/3; object-fit:cover; display:block; }}
.shelf-cap {{ display:block; padding:6px 9px; font-family:var(--mono); font-size:8px; letter-spacing:.12em;
  text-transform:uppercase; color:#8c8c82; }}
section.shelf .roomlink {{ color:#7c9fd9; }}
section.shelf .empty {{ color:#8c8c82; }}
.sysline {{ font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }}
#toast {{ position:fixed; bottom:24px; left:50%; transform:translateX(-50%); background:var(--ink); color:var(--panel);
  font-family:var(--mono); font-size:10px; letter-spacing:.14em; text-transform:uppercase; padding:9px 20px;
  border-radius:99px; opacity:0; transition:opacity .2s; pointer-events:none; z-index:99; }}
#toast.show {{ opacity:1; }}
footer {{ border-top:1px solid var(--ink); padding-top:12px; display:flex; justify-content:space-between;
  font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }}
</style>
<div class="wrap">
<header>
  <div><span class="kicker">ANTIGRAVITY · COMMAND CENTER</span><h1>home<em>base</em></h1></div>
  {pd._shared_nav("homebase")}
</header>
<div class="stamp"><span>{now}</span>
  <span class="livechip pill muted" id="livechip">static — actions copy commands</span>
  <span class="m">sweep {esc(sweep_age)}</span>
  <button class="actbtn" type="button" data-action="refresh">↻ refresh data</button></div>

<div class="zone">Focus</div>
{sprint_html}
<div class="tiles">
  <div class="tile"><a href="{esc(missions_uri)}" data-route="/missions"><div class="n">{len(active)}</div><div class="l">missions live</div></a></div>
  <div class="tile"><div class="n">{len(needs_you)}</div><div class="l">need you now</div></div>
  <div class="tile"><div class="n">{due_count}</div><div class="l">outcomes due</div></div>
  <div class="tile"><a href="{esc(room_uri)}" data-route="/room"><div class="n">{brief_total}</div><div class="l">briefs in the room</div></a></div>
  <div class="tile"><a href="{esc(board_uri)}" data-route="/assets"><div class="n">{asset_total}</div><div class="l">assets on the board</div></a></div>
  <div class="tile"><div class="n">{esc(threads_promoted)}</div><div class="l">threads promoted</div></div>
</div>
<section><h2>⚑ Needs you — top {len(needs_you)} of {len(flagged)} flagged</h2>{needs_html}</section>

<div class="zone">Launch — pick up where work left off</div>
<section><h2>Resumable threads (sweep, {esc(sweep_age)})</h2>{launch_html}</section>

<div class="zone">Library</div>
<section><h2>Fresh intel — newest briefs</h2><div class="intelgrid">{briefs_html}</div>
  <a class="roomlink" href="{esc(room_uri)}" data-route="/room">open the briefing room ↗</a>
  <a class="roomlink" href="{esc(missions_uri)}" data-route="/missions">mission control ↗</a></section>
<section class="shelf"><h2>Asset shelf — newest generations</h2>
  <div class="shelfgrid">{shelf_html}</div>
  <a class="roomlink" href="{esc(board_uri)}" data-route="/assets">open the asset board ↗</a></section>
<section><h2>What the system holds</h2><span class="sysline">{esc(sys_line) or "health receipt unavailable"}</span></section>

<footer><span>ANTIGRAVITY HOMEBASE</span><span>@farricecain</span></footer>
</div>
<div id="toast">copied</div>
<script>
const PULSE_LIVE = location.protocol.startsWith('http');
const REPO_ROOT_URI = {json.dumps(Path(ROOT).as_uri())};
if (PULSE_LIVE) {{
  const lc = document.getElementById('livechip');
  lc.textContent = 'live — actions write instantly';
  lc.classList.remove('muted'); lc.classList.add('ok');
}}
if (PULSE_LIVE) document.querySelectorAll('a[data-route]').forEach(a => {{ a.href = a.dataset.route; }});
// dual-mode media: live pages load thumbs over /repo/, file:// pages from disk
document.querySelectorAll('img[data-rel]').forEach(img => {{
  img.src = PULSE_LIVE ? '/repo/' + img.dataset.rel : REPO_ROOT_URI + '/' + img.dataset.rel;
}});
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
  if (action === 'refresh') return base + 'refresh';
  return base;
}}
function doAction(action, args) {{
  if (!PULSE_LIVE) {{ _copy(_cli(action, args), 'server offline — command copied'); return; }}
  fetch('/action', {{ method: 'POST', headers: {{ 'Content-Type': 'application/json' }},
                     body: JSON.stringify({{ action, args }}) }})
    .then(r => r.json())
    .then(j => {{
      if (j.ok) {{ _toast(action === 'refresh' ? 'refreshing data — page reloads when ready' : 'done — refreshing');
                  if (action !== 'refresh') setTimeout(() => location.reload(), 700); }}
      else {{ _toast('action failed — see server log'); }}
    }})
    .catch(() => {{ _copy(_cli(action, args), 'server unreachable — command copied'); }});
}}
document.querySelectorAll('.actbtn[data-action]').forEach(b => b.addEventListener('click', () => {{
  const act = b.dataset.action;
  if (act === 'done') {{
    const outcome = prompt('One-line outcome for the log:', 'closed from homebase');
    if (outcome === null) return;
    doAction('done', {{ slug: b.dataset.slug, outcome }});
  }} else if (act === 'park') {{
    const reason = prompt('Park reason (one line):');
    if (reason === null) return;
    doAction('park', {{ slug: b.dataset.slug, reason }});
  }} else if (act === 'refresh') {{
    doAction('refresh', {{}});
  }}
}}));
document.querySelectorAll('.copybtn').forEach(b => b.addEventListener('click', () => {{
  if (b.dataset.copy !== undefined) _copy(b.dataset.copy);
}}));
if (PULSE_LIVE) {{
  // http pages cannot navigate to file:// — route those clicks through the server's OS opener.
  document.querySelectorAll('a[href^="file:"]:not([data-route])').forEach(a => a.addEventListener('click', ev => {{
    ev.preventDefault();
    fetch('/action', {{ method: 'POST', headers: {{ 'Content-Type': 'application/json' }},
                       body: JSON.stringify({{ action: 'open-path', args: {{ uri: a.href }} }}) }})
      .then(r => r.json()).then(j => _toast(j.ok ? 'opened' : 'open failed'))
      .catch(() => _toast('open failed'));
  }}));
  // side-window live reload — refresh when the board regenerates underneath us
  let baseline = null;
  setInterval(() => {{
    fetch('/ping').then(r => r.json()).then(j => {{
      if (baseline === null) {{ baseline = j.homebase_mtime; return; }}
      if (j.homebase_mtime && j.homebase_mtime !== baseline) location.reload();
    }}).catch(() => {{}});
  }}, 5000);
}}
</script>"""

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(body)
    print(f"homebase → {OUT}")


if __name__ == "__main__":
    main()
