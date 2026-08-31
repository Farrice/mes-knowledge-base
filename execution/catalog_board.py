#!/usr/bin/env python3
"""catalog_board.py — THE LIBRARY: the catalog as a surface (2026-08-20).

Renders .agent/catalog/library.html from work_catalog.shelves(): Worth
resuming (merit + dormant — the lost-merit fix) · Live threads · The stacks
(everything, tag facets + search) · Graveyard (collapsed). Served at /library
by pulse_serve; registered in surface_nav. Premium Minimal report dialect.
Writers stay honest: kill/archive buttons use the existing verbs dual-mode.
"""
import html
import json
import os
import sys
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "execution"))
import work_catalog as wc  # noqa: E402

OUT = os.path.join(ROOT, ".agent", "catalog", "library.html")

KIND_ICON = {"thread": "🧵", "brief": "📋", "deliverable": "📦", "extraction": "⚗️",
             "knowledge": "📚", "guide": "🧭", "solution": "🔧"}


def esc(s):
    return html.escape(str(s or ""))


def _shared_nav(current):
    try:
        from surface_nav import nav_html
        return nav_html(current=current, style=False)
    except Exception:
        return ""


def row_html(r, actions=True):
    kind = r.get("kind") or "?"
    icon = KIND_ICON.get(kind, "·")
    tags = r.get("tags") or []
    tri = r.get("triage") or {}
    tri_html = ""
    if tri.get("call"):
        tcls = {"resume": "ok", "shelve": "muted", "kill": "crit"}.get(tri["call"], "muted")
        tri_html = (f'<span class="pill {tcls}" title="{esc(tri.get("why"))}">'
                    f'librarian: {esc(tri["call"])}</span>')
    merit = f'<span class="pill ok" title="{esc(r.get("merit_why"))}">★ merit</span>' if r.get("merit") else ""
    when = (r.get("last_active") or "")[:10] or "—"
    ev = r.get("evidence") or {}
    ev_line = " · ".join(f"{v} {k}" for k, v in ev.items() if v) if isinstance(ev, dict) else ""
    why = f'<p class="last">{esc(tri.get("why"))}</p>' if tri.get("why") else ""
    acts = []
    if r.get("resume"):
        acts.append(f'<button class="copybtn" type="button" data-copy="{esc(r["resume"])}">copy /resume</button>')
    if r.get("brief"):
        acts.append(f'<a class="actbtn alink" href="{esc((Path(ROOT) / r["brief"]).as_uri())}"'
                    f' data-repo="/repo/{esc(r["brief"])}">open brief ↗</a>')
    elif r.get("path"):
        acts.append(f'<a class="actbtn alink" href="{esc((Path(ROOT) / r["path"]).as_uri())}">open</a>')
        acts.append(f'<button class="copybtn" type="button" data-copy="{esc(r["path"])}">copy path</button>')
    if actions and kind == "thread" and r.get("handoff") and not r.get("killed"):
        acts.append(f'<button class="actbtn" type="button" data-action="thread-archive" data-thread="{esc(r["k"])}">archive</button>')
        acts.append(f'<button class="actbtn kill" type="button" data-action="kill" data-slug="{esc(r["k"])}">kill</button>')
    hay = esc(" ".join([str(r.get("title") or ""), r.get("k", ""), kind,
                        " ".join(tags), r.get("arena") or ""]).lower())
    tag_attr = esc(",".join(tags))
    return (f'<div class="mcard" data-hay="{hay}" data-tags="{tag_attr}" data-kind="{esc(kind)}">'
            f'<div class="row1"><h3>{icon} {esc(str(r.get("title"))[:110])}</h3>'
            f'<span class="pill muted">{esc(kind)}</span>{merit}{tri_html}</div>'
            f'{why}'
            f'<div class="meta"><span class="m">{esc(ev_line or "—")}</span>'
            f'<span class="m">last {esc(when)}</span>'
            f'<span class="acts">{"".join(acts)}</span></div></div>')


def main():
    import time
    s = wc.shelves()
    all_tags = sorted({t for r in s["stacks"] for t in (r.get("tags") or [])})
    chips = ('<button class="chip active" data-f="all">all</button>'
             + "".join(f'<button class="chip" data-f="{esc(t)}">{esc(t)}</button>' for t in all_tags))
    kill_recs = [r for r in s["stacks"] if (r.get("triage") or {}).get("call") == "kill"]

    resume_html = "".join(row_html(r) for r in s["resume"][:10]) or '<div class="empty">nothing dormant with merit — clean</div>'
    live_html = "".join(row_html(r) for r in s["live"]) or '<div class="empty">no live threads</div>'
    stacks_html = "".join(row_html(r) for r in s["stacks"][:400])
    dead_html = "".join(row_html(r, actions=False) for r in s["dead"][:60]) or '<div class="empty">empty graveyard</div>'
    kill_html = "".join(row_html(r) for r in kill_recs[:20]) or '<div class="empty">no kill recommendations pending</div>'

    from board_theme import theme_css
    body = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>the library · Antigravity</title>
<style>
{theme_css()}
* {{ box-sizing:border-box; }}
body {{ background:var(--ground); color:var(--ink); font:14px/1.5 var(--sans); margin:0; padding:40px 24px 80px; }}
.wrap {{ max-width:960px; margin:0 auto; display:flex; flex-direction:column; gap:18px; }}
header {{ display:flex; align-items:baseline; gap:14px; flex-wrap:wrap; }}
.kicker {{ font-family:var(--mono); font-size:9px; letter-spacing:.22em; text-transform:uppercase; color:var(--muted); display:block; margin-bottom:8px; }}
h1 {{ font-size:38px; font-weight:700; letter-spacing:-.022em; margin:0; }}
h1 em {{ font-family:var(--serif); font-style:italic; font-weight:400; color:var(--accent); }}
.homenav {{ margin-left:auto; display:flex; gap:6px; align-items:center; flex-wrap:wrap; }}
.homenav a, .homenav .here {{ font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; text-decoration:none;
  color:var(--soft); border:1px solid var(--line); border-radius:99px; padding:4px 11px; }}
.homenav a:hover {{ border-color:var(--accent); color:var(--accent); }}
.homenav .here {{ opacity:.45; border-style:dashed; }}
.stamp {{ color:var(--muted); font-family:var(--mono); font-size:10px; letter-spacing:.1em; text-transform:uppercase;
  display:flex; gap:10px; align-items:center; flex-wrap:wrap; border-top:1px solid var(--ink); padding-top:10px; }}
#q {{ font-family:var(--mono); font-size:12px; background:var(--panel); color:var(--ink);
  border:1px solid var(--line); border-radius:6px; padding:9px 14px; width:100%; max-width:480px; }}
#q:focus {{ outline:none; border-color:var(--accent); }}
.chips {{ display:flex; gap:8px; flex-wrap:wrap; }}
.chip {{ font-family:var(--mono); font-size:9px; letter-spacing:.1em; text-transform:uppercase; padding:4px 12px;
  border-radius:99px; border:1px solid var(--line); background:var(--panel); color:var(--soft); cursor:pointer; }}
.chip.active {{ border-color:var(--accent); color:var(--accent); }}
section {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:16px 18px; }}
h2 {{ font-family:var(--mono); font-size:9px; letter-spacing:.2em; text-transform:uppercase;
  color:var(--muted); margin:0 0 12px; border-bottom:1px solid var(--line); padding-bottom:8px; }}
.mcard {{ border:1px solid var(--line); border-radius:6px; background:var(--ground); padding:11px 14px; margin-bottom:9px; }}
.mcard:last-child {{ margin-bottom:0; }}
.mcard .row1 {{ display:flex; gap:10px; align-items:baseline; flex-wrap:wrap; }}
.mcard h3 {{ font-size:13px; font-weight:600; margin:0; line-height:1.35; flex:1; min-width:200px; }}
.mcard .last {{ font-size:11.5px; color:var(--soft); margin:5px 0 0; line-height:1.45; }}
.mcard .meta {{ display:flex; gap:12px; align-items:center; margin-top:7px; flex-wrap:wrap; }}
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
.actbtn.kill {{ color:var(--crit); border-color:var(--crit); }}
.actbtn.kill:hover {{ background:var(--crit); color:var(--panel); }}
.empty {{ color:var(--muted); font-style:italic; font-size:12.5px; }}
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
  <div><span class="kicker">ANTIGRAVITY · THE CATALOG</span><h1>the <em>library</em></h1></div>
  {_shared_nav("library")}
</header>
<div class="stamp"><span>{time.strftime("%Y-%m-%d %H:%M")}</span>
  <span class="m">{len(s["stacks"])} items · {len(s["resume"])} worth resuming · {len(s["dead"])} at rest</span></div>
<input id="q" type="search" placeholder="search the estate — half-remembered words work: 'supplement teardown', 'trailer', 'jen hooks'…">
<div class="chips">{chips}</div>
<section><h2>★ Worth resuming — merit, gone quiet</h2>{resume_html}</section>
<section><h2>Live threads</h2>{live_html}</section>
<section class="closed"><h2 class="tog">Librarian recommends killing ({len(kill_recs)})</h2><div class="body">{kill_html}</div></section>
<section><h2>The stacks — everything ({len(s["stacks"])})</h2>{stacks_html}</section>
<section class="closed"><h2 class="tog">Graveyard ({len(s["dead"])})</h2><div class="body">{dead_html}</div></section>
<footer><span>ANTIGRAVITY LIBRARY</span><span>@farricecain</span></footer>
</div>
<div id="toast">copied</div>
<script>
const LIVE = location.protocol.startsWith('http');
if (LIVE) document.querySelectorAll('a[data-repo]').forEach(a => {{ a.href = a.dataset.repo; }});
function _toast(m) {{ const t = document.getElementById('toast'); t.textContent = m; t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 1500); }}
function _copy(txt, msg) {{
  if (navigator.clipboard && navigator.clipboard.writeText)
    navigator.clipboard.writeText(txt).then(() => _toast(msg || 'copied'));
}}
document.querySelectorAll('.copybtn').forEach(b => b.addEventListener('click', () => _copy(b.dataset.copy)));
function doAction(action, args) {{
  if (!LIVE) {{ _copy('python3 execution/pulse_actions.py ' + action, 'static — command copied'); return; }}
  fetch('/action', {{ method: 'POST', headers: {{ 'Content-Type': 'application/json' }},
                     body: JSON.stringify({{ action, args }}) }})
    .then(r => r.json()).then(j => {{ if (j.ok) {{ _toast('done — refreshing'); setTimeout(() => location.reload(), 700); }}
                                     else _toast('failed — see server log'); }})
    .catch(() => _toast('server unreachable'));
}}
document.querySelectorAll('.actbtn[data-action]').forEach(b => b.addEventListener('click', () => {{
  const act = b.dataset.action;
  if (act === 'kill') {{
    if (!confirm('Kill this thread? It disappears from every board (ledger-recoverable).')) return;
    const reason = prompt('Kill reason (required):'); if (!reason) return;
    doAction('kill', {{ slug: b.dataset.slug, reason }});
  }} else if (act === 'thread-archive') {{
    if (confirm('Archive this thread?')) doAction('thread-archive', {{ thread: b.dataset.thread }});
  }}
}}));
const q = document.getElementById('q');
let activeTag = 'all';
function applyFilter() {{
  const words = q.value.toLowerCase().split(/\\s+/).filter(w => w.length > 1);
  document.querySelectorAll('.mcard[data-hay]').forEach(c => {{
    const hay = c.dataset.hay;
    const tagOk = activeTag === 'all' || (c.dataset.tags || '').split(',').includes(activeTag);
    const qOk = words.every(w => hay.includes(w));
    c.style.display = (tagOk && qOk) ? '' : 'none';
  }});
}}
q.addEventListener('input', applyFilter);
document.querySelectorAll('.chip').forEach(c => c.addEventListener('click', () => {{
  document.querySelectorAll('.chip').forEach(x => x.classList.remove('active'));
  c.classList.add('active'); activeTag = c.dataset.f; applyFilter();
}}));
document.querySelectorAll('.tog').forEach(h => h.addEventListener('click', () =>
  h.closest('section').classList.toggle('closed')));
</script>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(body)
    print(f"library → {OUT}")


if __name__ == "__main__":
    main()
