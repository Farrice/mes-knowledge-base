#!/usr/bin/env python3
"""
mission_board.py — Mission Control: the fourth home base (2026-08-07).

Renders .agent/missions/mission-control.html from the sweep fact bundle. Served
live at http://127.0.0.1:8765/missions alongside the Pulse (/), the Briefing
Room (/room) and the Oracle (/oracle).

WHY A BOARD AND NOT A BRIEF. The mission sweep already renders one living brief
per thread, and those are the right shape for READING a thread. They are the
wrong shape for deciding what to do next: a brief has no buttons, no route, no
liveness, and its links were dead the moment it was reached over http. This is
the deciding surface — needs-you first, one card per live thread, every card
carrying the four things Farrice asked for: open, resume, copy context, close.

FACTS COME FROM THE SWEEP, NEVER FROM HERE. session_sweep.py is the only
collector; this file reads .agent/sweep/latest.json and renders. If a number
looks wrong the bug is upstream, and fixing it here would create a second
source of truth that silently disagrees with the briefs.

WRITERS FIRST (docs/solutions/2026-08-06-live-local-board-pattern.md): every
button maps to a CLI a session could equally type. Served → POST /action;
file:// → the identical command lands on the clipboard. Nothing ever breaks.
"never skip part 1 — a server without honest CLI writers is just hidden state
mutation."

Usage:
    python3 execution/mission_board.py [--open]
"""
import argparse
import html
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from degrade import degraded, degraded_html  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SWEEP = ROOT / ".agent" / "sweep" / "latest.json"
OUT = ROOT / ".agent" / "missions" / "mission-control.html"
BRIEFS_REL = "deliverables/research-briefs"

NEEDS_YOU_CAP = 3          # matches the Pulse; a "top 3" you actually read
STALE_DAYS = 7             # finisher threshold, same as the open-mission alarm


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def load_bundle():
    try:
        return json.loads(SWEEP.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        # Was a silent {}. Combined with the fall-through in build() (fixed
        # 2026-08-08) a missing sweep rendered "everything live is moving".
        return degraded({}, f"sweep bundle unreadable at {SWEEP}", e)


def _dt(s):
    try:
        return datetime.fromisoformat(str(s)[:19])
    except (ValueError, TypeError):
        return None


def days_since(s):
    d = _dt(s)
    return (datetime.now() - d).days if d else None


def title_case(slug):
    return " ".join(str(slug).replace("-", " ").split())


def brief_uri(slug):
    return (ROOT / BRIEFS_REL / f"mission-{slug}" / f"mission-{slug}-brief.html").as_uri()


def stage_pill(stage):
    cls = {"research": "muted", "build": "warn", "shipped": "ok", "outcome": "ok"}.get(stage, "muted")
    return f'<span class="pill {cls}">{esc(stage)}</span>'


def status_pill(status):
    cls = {"blocked": "crit", "active": "warn", "mid-build": "warn",
           "ready": "ok", "done": "muted"}.get(status, "muted")
    return f'<span class="pill {cls}">{esc(status)}</span>' if status else ""


def idle_days(t, window_days):
    """Days since anything happened. A thread with NO recorded activity in the
    window is the most neglected kind there is, not the least — an empty
    last_active used to sort as "most recent" and pushed the quietest threads
    off the bottom of the list."""
    d = days_since(t.get("last_active"))
    return d if d is not None else max(int(window_days or 14), STALE_DAYS)


def why_needs_you(t, window_days=14):
    """The reason this thread is at the top — always a fact, never a vibe.
    Returns (rank, reason); lower rank = more urgent. rank None = doesn't qualify."""
    if t.get("status") == "blocked":
        return 0, "handoff is marked blocked"
    for m in t.get("missions", []):
        if m.get("open"):
            return 1, f"open mission ({m.get('status')})"
    if days_since(t.get("last_active")) is None:
        return 2, f"no recorded activity at all while still {t.get('status') or 'open'}"
    idle = idle_days(t, window_days)
    if idle >= STALE_DAYS:
        return 3, f"no activity in {idle}d while still {t.get('status') or 'open'}"
    return None, ""


def context_pack(slug, t):
    """The paste-into-a-chat form of a thread. Same grammar as the Room's
    `copy brief`: a header of pointers, then everything an agent needs to
    pick the thread up without being re-briefed."""
    lines = [f"THREAD: {t.get('title') or title_case(slug)}",
             f"SLUG: {slug}",
             f"STATUS: {t.get('status') or '—'} · STAGE: {t.get('stage') or '—'}",
             f"BRIEF: {ROOT / BRIEFS_REL / f'mission-{slug}' / f'mission-{slug}-brief.md'}"]
    if t.get("handoff"):
        lines.append(f"HANDOFF: {ROOT / t['handoff']}")
    lines.append("")
    if t.get("resume_hint"):
        lines.append(f"RESUME HERE: {t['resume_hint']}")
    if t.get("unfinished"):
        lines.append(f"STILL OPEN: {t['unfinished']}")
    for m in t.get("missions", []):
        if m.get("open"):
            lines.append(f"OPEN MISSION: {m.get('title')} (serves: {m.get('serves') or '—'})")
    delivs = t.get("deliverables") or []
    if delivs:
        lines.append("")
        lines.append("SHIPPED IN WINDOW:")
        for d in delivs[:5]:
            lines.append(f"  - {d.get('date')} · {(d.get('output') or '')[:160]}")
    arts = t.get("artifacts") or []
    if arts:
        lines.append("")
        lines.append(f"FILES TOUCHED ({len(arts)}):")
        for a in arts[:12]:
            lines.append(f"  - {a.get('path')}")
        if len(arts) > 12:
            lines.append(f"  … +{len(arts) - 12} more")
    lines.append("")
    lines.append("(assembled by mission_board.py from .agent/sweep/latest.json — "
                 "every line above is a record, not a summary)")
    return "\n".join(lines)


def card(slug, t, needs_reason=""):
    counts = []
    for n, label in ((len(t.get("deliverables") or []), "shipped"),
                     (len(t.get("artifacts") or []), "files"),
                     (len(t.get("assets") or []), "assets"),
                     (len(t.get("sessions") or []), "sessions")):
        if n:
            counts.append(f"{n} {label}")
    idle = days_since(t.get("last_active"))
    when = "today" if (idle is not None and idle <= 0) else (f"{idle}d ago" if idle is not None else "—")

    resume = t.get("resume_hint") or t.get("unfinished") or ""
    reason_html = (f'<p class="why">{esc(needs_reason)}</p>' if needs_reason else "")
    resume_html = f'<p class="last">{esc(resume)}</p>' if resume else ""

    # Buttons map to the writer that actually owns this thread's domain.
    # A handoff thread has no mission record, so `done` would invent one —
    # archive is the honest verb there.
    acts = [f'<a class="actbtn brief" href="{esc(brief_uri(slug))}">open brief ↗</a>',
            f'<button class="actbtn" data-action="resume" data-slug="{esc(slug)}">resume</button>',
            f'<button class="actbtn" data-action="context" data-slug="{esc(slug)}">copy context</button>']
    open_mission = next((m for m in t.get("missions", []) if m.get("open")), None)
    if open_mission:
        acts.append(f'<button class="actbtn ok" data-action="done" data-slug="{esc(open_mission["slug"] or slug)}">✓ done</button>')
        acts.append(f'<button class="actbtn" data-action="park" data-slug="{esc(open_mission["slug"] or slug)}">park</button>')
    if t.get("handoff"):
        acts.append(f'<button class="actbtn" data-action="thread-archive" data-thread="{esc(slug)}">archive</button>')

    return (f'<div class="mcard" data-slug="{esc(slug)}">'
            f'<div class="row1"><h3>{esc(t.get("title") or title_case(slug))}</h3>'
            f'{status_pill(t.get("status"))}{stage_pill(t.get("stage"))}</div>'
            f'{reason_html}{resume_html}'
            f'<div class="meta"><span class="m">{esc(t.get("arena") or "—")}</span>'
            f'<span class="m">{esc(" · ".join(counts) or "no activity in window")}</span>'
            f'<span class="m">last {esc(when)}</span>'
            f'<span class="acts">{"".join(acts)}</span></div></div>')


def build():
    b = load_bundle()
    threads = b.get("threads") or {}
    # STICKY EMPTY STATE (2026-08-08). This block used to assign needs_html and
    # live_html and then FALL THROUGH with no return — lines below overwrote
    # both unconditionally, so the honest "no sweep yet" message was unreachable
    # code and a missing bundle rendered "nothing blocked, nothing stale —
    # everything live is moving." The board asserted the system was healthy
    # precisely when it had no idea. Highest-blast-radius silent fallback found
    # in the audit. The flag is checked again after those assignments.
    no_sweep = not threads
    wdays = (b.get("window") or {}).get("days", 14)
    # A thread with no recorded activity sorts as MOST neglected, not most
    # recent — "" used to win a reverse string sort and float to the top.
    live = sorted(threads.items(),
                  key=lambda kv: (idle_days(kv[1], wdays), kv[0]))

    scored = []
    for slug, t in live:
        rank, reason = why_needs_you(t, wdays)
        if rank is not None:
            scored.append((rank, -idle_days(t, wdays), slug, t, reason))
    # blocked → open mission → never-active → longest-idle. Consequence order,
    # not recency: what is most at risk should never be decided by who was
    # touched last.
    scored.sort(key=lambda x: (x[0], x[1], x[2]))
    needs = [(s, t, r) for _, _, s, t, r in scored[:NEEDS_YOU_CAP]]
    needs_total = len(scored)

    needs_html = ("".join(card(s, t, r) for s, t, r in needs) if needs
                  else '<p class="empty">nothing blocked, nothing stale — everything live is moving.</p>')
    # No silent caps: if more qualify than fit, the page says so.
    needs_label = (f"⚑ needs you — top {len(needs)} of {needs_total}"
                   if needs_total > len(needs) else "⚑ needs you")
    live_html = ("".join(card(s, t) for s, t in live) if live
                 else '<p class="empty">no live threads in the window.</p>')

    # The flag set above wins over both assignments. "We have no data" and
    # "we looked and everything is fine" must never render the same.
    if no_sweep:
        needs_html = live_html = degraded_html(
            "no sweep data — run <code>python3 execution/session_sweep.py run</code>, then reload")
        needs_label = "⚑ needs you — NO SWEEP DATA"

    shipped = b.get("also_shipped") or []
    shipped_html = ("".join(
        f'<div class="mcard"><div class="row1"><h3>{esc(s.get("output") or "")[:140]}</h3>'
        f'<span class="pill muted">{esc(s.get("date"))}</span></div>'
        f'<div class="meta"><span class="m">{esc(s.get("workflow") or s.get("type") or "—")}</span>'
        f'<span class="m">no live thread</span></div></div>'
        for s in shipped[:12]) if shipped else '<p class="empty">nothing.</p>')

    over = b.get("overflow") or []
    filtered = b.get("filtered_out") or []
    below_html = (
        f'<p class="last">{len(over)} thread(s) cleared the bar but sit below the card ceiling: '
        f'{esc(", ".join(title_case(k) for k in over[:20]))}'
        f'{"…" if len(over) > 20 else ""}</p>'
        f'<p class="last">{len(filtered)} key(s) were seen but never declared a thread — '
        f'no live handoff, no open mission, no finalized deliverable. Activity alone '
        f'does not mint a mission.</p>') if (over or filtered) else '<p class="empty">nothing held back.</p>'

    packs = {slug: context_pack(slug, t) for slug, t in live}
    packs_json = json.dumps(packs, ensure_ascii=False).replace("</", "<\\/")

    c = b.get("counts") or {}
    win = b.get("window") or {}
    now = datetime.now().strftime("%a %b %d · %H:%M")
    gen = (b.get("generated") or "")[:16].replace("T", " ")
    # renamed from `degraded` 2026-08-08: it shadowed the imported degraded()
    # for the whole function body, which would silently break any future use.
    deg_list = b.get("degraded") or []
    deg_html = (f'<div class="sprint"><span class="sprint-tag">degraded</span>'
                f'<span>{esc("; ".join(deg_list))}</span></div>') if deg_list else ""

    room_uri = (ROOT / BRIEFS_REL / "index.html").as_uri()
    pulse_uri = (ROOT / ".agent" / "pulse" / "pulse-board.html").as_uri()
    assets_uri = (ROOT / ".agent" / "assets" / "assets-board.html").as_uri()
    oracle_uri = (ROOT / ".agent" / "oracle" / "oracle-dashboard.html").as_uri()

    page = PAGE.format(
        now=esc(now), gen=esc(gen), days=esc(win.get("days", "—")),
        n_live=len(live), n_needs=needs_total,
        n_ship=c.get("deliverables", 0), n_files=c.get("artifacts", 0),
        n_assets=c.get("assets", 0), n_sessions=c.get("sessions", 0),
        needs=needs_html, needs_label=esc(needs_label),
        live=live_html, shipped=shipped_html, below=below_html,
        deg=deg_html, packs=packs_json, repo_root=json.dumps(str(ROOT)),
        room=esc(room_uri), pulse=esc(pulse_uri), assets=esc(assets_uri), oracle=esc(oracle_uri),
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    return OUT, len(live), len(needs)


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>mission control · antigravity</title>
<style>
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
.sprint {{ background:var(--panel); border:1px solid var(--crit); border-radius:8px; padding:12px 16px;
  display:flex; gap:12px; align-items:baseline; flex-wrap:wrap; }}
.sprint-tag {{ font-family:var(--mono); font-size:9px; letter-spacing:.18em; color:var(--crit); text-transform:uppercase; }}
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
.mcard .why {{ font-size:11.5px; color:var(--crit); margin:6px 0 0; }}
.mcard .why::before {{ content:"⚑ "; }}
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
.actbtn {{ font-family:var(--mono); font-size:8.5px; letter-spacing:.12em; text-transform:uppercase;
  cursor:pointer; background:none; border:1px solid var(--line); border-radius:4px; padding:3px 9px; color:var(--soft);
  text-decoration:none; display:inline-block; }}
.actbtn:hover {{ border-color:var(--accent); color:var(--accent); }}
.actbtn.brief {{ border-color:var(--accent); color:var(--accent); }}
.actbtn.brief:hover {{ background:var(--accent); color:var(--panel); }}
.actbtn.ok {{ color:var(--ok); border-color:var(--ok); }}
.actbtn.ok:hover {{ background:var(--ok); color:var(--panel); }}
.livechip {{ font-family:var(--mono); font-size:8px; letter-spacing:.14em; text-transform:uppercase; padding:2px 8px;
  border-radius:3px; font-weight:700; }}
.empty {{ color:var(--muted); font-style:italic; font-size:12.5px; }}
code {{ font-family:var(--mono); font-size:11px; color:var(--accent); }}
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
  <div><span class="kicker">ANTIGRAVITY · MISSION CONTROL</span><h1>the <em>threads</em></h1></div>
  <span class="homenav"><a href="{pulse}">⚡ pulse ↗</a><a href="{room}">📋 briefing room ↗</a><a href="{assets}">🎨 asset board ↗</a><a href="{oracle}">🔮 oracle ↗</a></span>
</header>
<div class="stamp"><span>{now}</span><span>swept {gen}</span><span>window {days}d</span>
  <span class="livechip pill muted" id="livechip">static — actions copy commands</span></div>
{deg}
<div class="tiles">
  <div class="tile"><div class="n">{n_live}</div><div class="l">threads live</div></div>
  <div class="tile"><div class="n">{n_needs}</div><div class="l">need you now</div></div>
  <div class="tile"><div class="n">{n_ship}</div><div class="l">deliverables shipped</div></div>
  <div class="tile"><div class="n">{n_files}</div><div class="l">files written</div></div>
  <div class="tile"><div class="n">{n_sessions}</div><div class="l">sessions swept</div></div>
</div>
<section><h2>{needs_label}</h2>{needs}</section>
<section><h2>threads — live</h2>{live}</section>
<section class="closed"><h2 class="tog">also shipped — no live thread</h2><div class="body">{shipped}</div></section>
<section class="closed"><h2 class="tog">held back — named, never silently dropped</h2><div class="body">{below}</div></section>
<footer><span>ANTIGRAVITY · MISSION CONTROL</span><span>facts from .agent/sweep/latest.json</span></footer>
</div>
<div id="toast">copied</div>
<script id="packs" type="application/json">{packs}</script>
<script>
const LIVE = location.protocol.startsWith('http');
const REPO_ROOT = {repo_root};
const PACKS = JSON.parse(document.getElementById('packs').textContent);

function _toast(m){{ const t=document.getElementById('toast'); t.textContent=m; t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'), 1600); }}
function _copy(txt, msg){{
  if (navigator.clipboard && navigator.clipboard.writeText) {{
    navigator.clipboard.writeText(txt).then(()=>_toast(msg), ()=>_fallback(txt, msg));
  }} else {{ _fallback(txt, msg); }}
}}
function _fallback(txt, msg){{
  const ta=document.createElement('textarea'); ta.value=txt; ta.style.position='fixed'; ta.style.opacity='0';
  document.body.appendChild(ta); ta.select(); try{{ document.execCommand('copy'); }}catch(e){{}}
  document.body.removeChild(ta); _toast(msg);
}}
function _sq(s){{ return "'" + String(s).replace(/'/g, `'\\''`) + "'"; }}
/* Every button's CLI twin. A board whose actions exist only in the browser is
   hidden state mutation — this is the half that keeps it honest. */
function _cli(action, args){{
  const pa = 'python3 execution/pulse_actions.py ';
  if (action === 'done') return pa + 'done ' + _sq(args.slug) + ' --outcome ' + _sq(args.outcome || '');
  if (action === 'park') return pa + 'park ' + _sq(args.slug) + ' --reason ' + _sq(args.reason || '');
  if (action === 'thread-archive') return pa + 'thread-archive ' + _sq(args.thread);
  return pa;
}}
function doAction(action, args){{
  if (!LIVE) {{ _copy(_cli(action, args), 'server offline — command copied'); return; }}
  fetch('/action', {{method:'POST', headers:{{'Content-Type':'application/json'}},
                     body: JSON.stringify({{action, args}})}})
    .then(r=>r.json())
    .then(j=>{{ if (j.ok) {{ _toast('done — refreshing'); setTimeout(()=>location.reload(), 700); }}
               else {{ _toast('action failed — see server log'); }} }})
    .catch(()=>_copy(_cli(action, args), 'server unreachable — command copied'));
}}

if (LIVE) {{
  const lc = document.getElementById('livechip');
  lc.textContent = 'live — actions write instantly';
  lc.classList.remove('muted'); lc.classList.add('ok');
}}

document.querySelectorAll('.actbtn[data-action]').forEach(b => b.addEventListener('click', () => {{
  const act = b.dataset.action;
  if (act === 'resume') {{
    _copy('python3 execution/handoff_store.py resume ' + b.dataset.slug,
          'resume command copied — paste in a fresh session');
  }} else if (act === 'context') {{
    const p = PACKS[b.dataset.slug];
    if (p) _copy(p, 'thread context copied — paste into claude or codex');
  }} else if (act === 'done') {{
    const outcome = prompt('One-line outcome for the log:', 'closed from mission control');
    if (outcome === null) return;
    doAction('done', {{ slug: b.dataset.slug, outcome }});
  }} else if (act === 'park') {{
    const reason = prompt('Park reason (one line):');
    if (reason === null) return;
    doAction('park', {{ slug: b.dataset.slug, reason }});
  }} else if (act === 'thread-archive') {{
    if (confirm('Archive this thread? (moves the handoff to archive/)'))
      doAction('thread-archive', {{ thread: b.dataset.thread }});
  }}
}}));

/* Brief links are file:// so this board works standalone. Served, map them to
   the ROOT-jailed /repo/ route — otherwise the browser refuses the click and
   the card looks broken for no visible reason. */
if (LIVE && REPO_ROOT) {{
  const PREFIX = 'file://' + encodeURI(REPO_ROOT).replace(/#/g, '%23') + '/';
  const ROUTES = [['/.agent/pulse/pulse-board.html','/'],
                  ['/.agent/oracle/oracle-dashboard.html','/oracle'],
                  ['/deliverables/research-briefs/index.html','/room']];
  document.querySelectorAll('a[href^="file:"]').forEach(a => {{
    const raw = a.getAttribute('href');
    const plain = decodeURI(raw);
    for (const [needle, route] of ROUTES) {{
      if (plain.indexOf(needle) !== -1) {{ a.setAttribute('href', route); return; }}
    }}
    if (raw.indexOf(PREFIX) === 0) a.setAttribute('href', '/repo/' + raw.slice(PREFIX.length));
    else a.addEventListener('click', ev => {{
      ev.preventDefault();
      fetch('/action', {{method:'POST', headers:{{'Content-Type':'application/json'}},
                         body: JSON.stringify({{action:'open-path', args:{{uri: raw}}}})}})
        .then(r=>r.json()).then(j=>_toast(j.ok ? 'opened' : 'open failed')).catch(()=>_toast('open failed'));
    }});
  }});
}}

document.querySelectorAll('h2.tog').forEach(h =>
  h.addEventListener('click', () => h.closest('section').classList.toggle('closed')));

/* side-window live reload — the board refreshes itself when a sweep rewrites it */
if (LIVE) {{
  let baseline = null;
  setInterval(() => {{
    fetch('/ping').then(r=>r.json()).then(j => {{
      if (baseline === null) {{ baseline = j.missions_mtime; return; }}
      if (j.missions_mtime && j.missions_mtime !== baseline) location.reload();
    }}).catch(()=>{{}});
  }}, 5000);
}}
</script>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description="Render Mission Control from the sweep bundle.")
    ap.add_argument("--open", action="store_true", help="open the board after rendering")
    args = ap.parse_args()
    try:
        out, n_live, n_needs = build()
    except Exception as e:  # noqa: BLE001 — a board must never break a caller
        print(f"[mission_board] FAILED (non-blocking): {type(e).__name__}: {e}", file=sys.stderr)
        return 0
    print(f"mission control → {out}  ({n_live} live, {n_needs} need you)")
    if args.open:
        subprocess.run(["open", str(out)], check=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
