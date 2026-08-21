#!/usr/bin/env python3
"""brain_graph.py — the visual second brain: /brain (2026-08-21).

Builds .agent/brain/brain.json (nodes + precomputed radial positions) and
.agent/brain/brain.html (self-contained canvas renderer, data EMBEDDED so the
page works over file:// exactly like every other board — no fetch, no server
dependency). Served at /brain by pulse_serve.py.

WHY (Farrice 2026-08-21, ARMS-video harvest): the level-3 memory view — see how
the workspace connects, search any skill/file instantly, click → preview/copy
path. This un-defers the "workspace force-graph" the 2026-08-20 homebase
mission parked.

Scale doctrine (stress-test 2026-08-21): ALLOWLIST, never a directory walk —
.agents/skills holds 2,564 entries and .agent/workflows 2,788; graphing those
drowns the canon. Departments below are the curated canon (~1,300 nodes).
Positions are computed HERE in Python (deterministic sunflower-in-sector), so
the renderer never runs a force simulation — 60fps at any node count.

Caching: --if-stale compares a directory-level fingerprint (top-level mtime +
entry count per source dir — never a 5k-file stat storm) and exits O(1) when
fresh. pulse_serve's regen("brain") calls exactly that.
"""
import argparse
import html as _html
import json
import math
import os
import sys
import time
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "execution"))

from board_theme import theme_css  # noqa: E402

OUT_DIR = os.path.join(ROOT, ".agent", "brain")
OUT_JSON = os.path.join(OUT_DIR, "brain.json")
OUT_HTML = os.path.join(OUT_DIR, "brain.html")
FPRINT = os.path.join(OUT_DIR, "fingerprint.json")

PHI = 0.6180339887498949

# The curated canon — key, label, source dir (repo-relative), member rule.
# Colors are a quiet brand-adjacent ramp (steel blues + graphite/sage/sand):
# category encoding on a data surface, not decoration (REPORT-DIALECT scope).
DEPARTMENTS = [
    ("directives", "Directives", "directives", "md", "#7c9fd9"),
    ("skills", "Skills", "skills", "dirs", "#5a7fc0"),
    ("agents", "Agents", "agents", "dirs", "#94a9c9"),
    ("active", "Active work", "_active", "dirs", "#c9a868"),
    ("briefs", "Briefs", "deliverables/research-briefs", "dirs", "#6fae8c"),
    ("solutions", "Solutions", "docs/solutions", "md", "#8fb8a8"),
    ("execution", "Execution", "execution", "py", "#8c8c82"),
    ("knowledge", "Knowledge", "knowledge", "any", "#b9a9c9"),
]


def _members(src, rule):
    """Member (label, rel, kind, mtime) list for one department. Top level
    only — the canon is the map, not the territory."""
    base = os.path.join(ROOT, src)
    out = []
    try:
        entries = sorted(os.scandir(base), key=lambda e: e.name.lower())
    except OSError:
        return out
    for e in entries:
        name = e.name
        if name.startswith((".", "_")) and name != "_framework":
            continue
        try:
            is_dir = e.is_dir()
            mtime = e.stat().st_mtime
        except OSError:
            continue
        rel = f"{src}/{name}"
        if rule == "dirs":
            if not is_dir:
                continue
            # point a dir node at its most useful file
            for probe in ("SKILL.md", "START-HERE.md", "README.md", "index.html",
                          f"{name}-brief.html", "AGENT.md"):
                if os.path.isfile(os.path.join(base, name, probe)):
                    rel = f"{src}/{name}/{probe}"
                    break
            out.append((name, rel, "dir", mtime))
        elif rule == "md":
            if is_dir or not name.endswith(".md"):
                continue
            out.append((name[:-3], rel, "md", mtime))
        elif rule == "py":
            if is_dir or not name.endswith(".py"):
                continue
            out.append((name[:-3], rel, "py", mtime))
        else:  # any
            out.append((name, rel, "dir" if is_dir else "file", mtime))
    return out


def fingerprint():
    fp = {}
    for _key, _label, src, _rule, _c in DEPARTMENTS:
        base = os.path.join(ROOT, src)
        try:
            st = os.stat(base)
            n = sum(1 for _ in os.scandir(base))
            fp[src] = [int(st.st_mtime), n]
        except OSError:
            fp[src] = [0, 0]
    try:
        fp["CLAUDE.md"] = [int(os.stat(os.path.join(ROOT, "CLAUDE.md")).st_mtime), 1]
    except OSError:
        fp["CLAUDE.md"] = [0, 0]
    return fp


def is_stale():
    try:
        old = json.load(open(FPRINT, encoding="utf-8"))
    except (OSError, ValueError):
        return True
    if not os.path.isfile(OUT_HTML) or not os.path.isfile(OUT_JSON):
        return True
    return old != fingerprint()


def build_graph():
    """Nodes with precomputed positions. Layout: CLAUDE.md at origin; dept
    hubs on an inner ring; members sunflower-scattered inside each dept's
    angular sector between R_IN and R_OUT — organic galaxy, zero physics."""
    depts = []
    for key, label, src, rule, color in DEPARTMENTS:
        depts.append({"key": key, "label": label, "color": color,
                      "members": _members(src, rule)})
    total = sum(len(d["members"]) for d in depts) or 1
    # sector width ∝ sqrt(count) — big depts get room, small ones stay legible
    weights = [math.sqrt(max(len(d["members"]), 3)) for d in depts]
    wsum = sum(weights)
    R_HUB, R_IN, R_OUT = 150, 230, 660
    nodes = [{"id": "claude-md", "label": "CLAUDE.md", "dept": "core",
              "kind": "md", "rel": "CLAUDE.md", "x": 0, "y": 0, "hub": True}]
    hubs = {}
    ang = -math.pi / 2
    for d, w in zip(depts, weights):
        span = 2 * math.pi * (w / wsum)
        mid = ang + span / 2
        hx, hy = R_HUB * math.cos(mid), R_HUB * math.sin(mid)
        hubs[d["key"]] = (hx, hy)
        nodes.append({"id": f"hub-{d['key']}", "label": d["label"],
                      "dept": d["key"], "kind": "hub", "rel": "",
                      "x": round(hx, 1), "y": round(hy, 1), "hub": True,
                      "count": len(d["members"])})
        n = len(d["members"])
        pad = span * 0.06
        for i, (label, rel, kind, mtime) in enumerate(d["members"]):
            t = (i + 0.5) / max(n, 1)
            r = R_IN + (R_OUT - R_IN) * math.sqrt(t)
            a = ang + pad + (span - 2 * pad) * ((i * PHI) % 1.0)
            nodes.append({"id": f"{d['key']}-{i}", "label": label,
                          "dept": d["key"], "kind": kind, "rel": rel,
                          "x": round(r * math.cos(a), 1),
                          "y": round(r * math.sin(a), 1),
                          "mt": time.strftime("%Y-%m-%d", time.localtime(mtime))})
        ang += span
    return {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "total": total,
            "depts": [{"key": d["key"], "label": d["label"], "color": d["color"],
                       "count": len(d["members"])} for d in depts],
            "nodes": nodes}


CSS = """
* { box-sizing:border-box; }
html, body { height:100%; }
body { background:var(--ground); color:var(--ink); font:14px/1.5 var(--sans); margin:0; overflow:hidden; }
#cv { position:fixed; inset:0; width:100vw; height:100vh; display:block; cursor:grab; }
#cv.panning { cursor:grabbing; }
.bar { position:fixed; top:0; left:0; right:0; display:flex; gap:12px; align-items:center;
  padding:14px 20px; pointer-events:none; z-index:10; }
.bar > * { pointer-events:auto; }
.brand { display:flex; flex-direction:column; }
.kicker { font-family:var(--mono); font-size:8.5px; letter-spacing:.22em; text-transform:uppercase; color:var(--muted); }
.brand h1 { font-size:20px; font-weight:700; letter-spacing:-.02em; margin:0; }
.brand h1 em { font-family:var(--serif); font-style:italic; font-weight:400; color:var(--accent); }
#search { font-family:var(--mono); font-size:11px; background:var(--panel); color:var(--ink);
  border:1px solid var(--line); border-radius:99px; padding:8px 16px; width:300px; outline:none; }
#search:focus { border-color:var(--accent); }
.homenav { margin-left:auto; display:flex; gap:6px; flex-wrap:wrap; }
.homenav a, .homenav .here { font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase;
  text-decoration:none; color:var(--soft); border:1px solid var(--line); border-radius:99px; padding:4px 11px; background:var(--panel); }
.homenav a:hover { border-color:var(--accent); color:var(--accent); }
.homenav .here { opacity:.45; border-style:dashed; }
#hits { position:fixed; top:64px; left:20px; width:340px; display:flex; flex-direction:column; gap:4px; z-index:10; }
#hits button { text-align:left; font:12px/1.4 var(--sans); background:var(--panel); color:var(--ink);
  border:1px solid var(--line); border-radius:6px; padding:6px 10px; cursor:pointer; }
#hits button:hover { border-color:var(--accent); }
#hits .hd { font-family:var(--mono); font-size:8px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }
.panel { position:fixed; right:16px; top:64px; width:250px; background:var(--panel); border:1px solid var(--line);
  border-radius:8px; padding:14px 16px; z-index:10; }
.panel h2 { font-family:var(--mono); font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--muted);
  margin:0 0 10px; border-bottom:1px solid var(--line); padding-bottom:6px; }
.chip { display:inline-flex; align-items:center; gap:6px; font-family:var(--mono); font-size:8.5px; letter-spacing:.1em;
  text-transform:uppercase; color:var(--soft); border:1px solid var(--line); border-radius:99px; padding:3px 9px;
  margin:0 4px 6px 0; cursor:pointer; user-select:none; }
.chip .sw { width:7px; height:7px; border-radius:50%; }
.chip.off { opacity:.3; }
.slider { display:flex; align-items:center; gap:8px; margin-top:8px; }
.slider label { font-family:var(--mono); font-size:8px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); flex:1; }
.slider input { width:100px; accent-color:var(--accent); }
#detail { position:fixed; left:16px; bottom:16px; width:380px; max-height:46vh; overflow:auto; background:var(--panel);
  border:1px solid var(--line); border-radius:8px; padding:14px 16px; z-index:10; display:none; }
#detail.show { display:block; }
#detail h3 { font-size:14px; font-weight:700; margin:0 0 2px; }
#detail .meta { font-family:var(--mono); font-size:8.5px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); margin-bottom:8px; }
#detail .acts { display:flex; gap:6px; margin-bottom:8px; flex-wrap:wrap; }
#detail button, #detail a { font-family:var(--mono); font-size:8.5px; letter-spacing:.12em; text-transform:uppercase;
  cursor:pointer; background:none; border:1px solid var(--line); border-radius:4px; padding:3px 9px; color:var(--soft); text-decoration:none; }
#detail button:hover, #detail a:hover { border-color:var(--accent); color:var(--accent); }
#detail pre { font:10.5px/1.5 var(--mono); background:var(--ground); border:1px solid var(--line); border-radius:6px;
  padding:10px; white-space:pre-wrap; word-break:break-word; max-height:24vh; overflow:auto; margin:0; }
.hublist { display:flex; flex-direction:column; gap:3px; }
.hubitem { text-align:left; font:11.5px/1.4 var(--mono); background:var(--ground); color:var(--ink);
  border:1px solid var(--line); border-radius:5px; padding:5px 9px; cursor:pointer;
  overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.hubitem:hover { border-color:var(--accent); color:var(--accent); }
.foot { position:fixed; bottom:14px; right:16px; font-family:var(--mono); font-size:8.5px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--muted); z-index:10; }
#toast { position:fixed; bottom:24px; left:50%; transform:translateX(-50%); background:var(--ink); color:var(--panel);
  font-family:var(--mono); font-size:10px; letter-spacing:.14em; text-transform:uppercase; padding:9px 20px;
  border-radius:99px; opacity:0; transition:opacity .2s; pointer-events:none; z-index:99; }
#toast.show { opacity:1; }
"""

JS = r"""
const DATA = JSON.parse(document.getElementById('braindata').textContent);
const LIVE = location.protocol.startsWith('http');
const REPO_ROOT_URI = __REPO_ROOT_URI__;
const cv = document.getElementById('cv');
const ctx = cv.getContext('2d');
const DPR = window.devicePixelRatio || 1;
const colors = {}; DATA.depts.forEach(d => colors[d.key] = d.color);
colors.core = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim();
const hubs = {}; DATA.nodes.forEach(n => { if (n.id.startsWith('hub-')) hubs[n.dept] = n; });
const center = DATA.nodes.find(n => n.id === 'claude-md');
let view = { tx: 0, ty: 0, scale: 0.9 };
let linkAlpha = 0.14, nodeScale = 1.0;
const hidden = new Set();
let hover = null, selected = null, searchHits = new Set(), searching = false;

function resize() {
  cv.width = innerWidth * DPR; cv.height = innerHeight * DPR;
  cv.style.width = innerWidth + 'px'; cv.style.height = innerHeight + 'px';
  draw();
}
addEventListener('resize', resize);

function toScreen(n) {
  return [ (n.x * view.scale + view.tx) * DPR + cv.width / 2,
           (n.y * view.scale + view.ty) * DPR + cv.height / 2 ];
}

function nodeR(n) {
  const base = n.id === 'claude-md' ? 13 : (n.hub ? 7 : 2.4);
  return base * nodeScale * DPR * (n.hub ? 1 : Math.max(0.7, Math.min(view.scale, 2)));
}

function draw() {
  const ink = getComputedStyle(document.documentElement).getPropertyValue('--ink').trim();
  const muted = getComputedStyle(document.documentElement).getPropertyValue('--muted').trim();
  ctx.clearRect(0, 0, cv.width, cv.height);
  // edges hub → member, center → hub
  ctx.lineWidth = 0.6 * DPR;
  for (const n of DATA.nodes) {
    if (n.hub || hidden.has(n.dept)) continue;
    const h = hubs[n.dept]; if (!h) continue;
    const dim = (searching && !searchHits.has(n.id));
    ctx.globalAlpha = dim ? linkAlpha * 0.15 : linkAlpha;
    ctx.strokeStyle = colors[n.dept] || muted;
    const [x1, y1] = toScreen(h), [x2, y2] = toScreen(n);
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
  }
  for (const key in hubs) {
    if (hidden.has(key)) continue;
    ctx.globalAlpha = Math.min(0.5, linkAlpha * 2.4);
    ctx.strokeStyle = colors[key] || muted;
    ctx.lineWidth = 1.1 * DPR;
    const [x1, y1] = toScreen(center), [x2, y2] = toScreen(hubs[key]);
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
  }
  // nodes
  for (const n of DATA.nodes) {
    if (!n.hub && hidden.has(n.dept)) continue;
    if (n.hub && n.dept !== 'core' && hidden.has(n.dept)) continue;
    const [x, y] = toScreen(n);
    const dim = (searching && !searchHits.has(n.id) && !n.hub);
    ctx.globalAlpha = dim ? 0.10 : (n.hub ? 1 : 0.85);
    ctx.fillStyle = colors[n.dept] || ink;
    ctx.beginPath(); ctx.arc(x, y, nodeR(n), 0, 7); ctx.fill();
    if (n === hover || n === selected) {
      ctx.globalAlpha = 1; ctx.strokeStyle = ink; ctx.lineWidth = 1.2 * DPR;
      ctx.beginPath(); ctx.arc(x, y, nodeR(n) + 3 * DPR, 0, 7); ctx.stroke();
    }
  }
  // labels: center + hubs always; hover/selected member
  ctx.globalAlpha = 1;
  ctx.textAlign = 'center';
  for (const n of DATA.nodes) {
    if (!n.hub || (n.dept !== 'core' && hidden.has(n.dept))) continue;
    const [x, y] = toScreen(n);
    ctx.font = `${(n.id === 'claude-md' ? 11 : 9.5) * DPR}px ${'JetBrains Mono, Menlo, monospace'}`;
    ctx.fillStyle = ink;
    const lab = n.id === 'claude-md' ? 'CLAUDE.MD' : (n.label + (n.count ? ' · ' + n.count : '')).toUpperCase();
    ctx.fillText(lab, x, y - nodeR(n) - 6 * DPR);
  }
  const focus = hover || selected;
  if (focus && !focus.hub) {
    const [x, y] = toScreen(focus);
    ctx.font = `${10 * DPR}px ${'JetBrains Mono, Menlo, monospace'}`;
    ctx.fillStyle = ink;
    ctx.fillText(focus.label, x, y - nodeR(focus) - 5 * DPR);
  }
}

function pick(mx, my) {
  const px = mx * DPR, py = my * DPR;
  let best = null, bd = 12 * DPR;
  for (const n of DATA.nodes) {
    if (!n.hub && hidden.has(n.dept)) continue;
    const [x, y] = toScreen(n);
    const d = Math.hypot(px - x, py - y) - nodeR(n);
    if (d < bd) { bd = d; best = n; }
  }
  return best;
}

// pan + zoom
let panning = false, px0 = 0, py0 = 0, moved = false;
cv.addEventListener('mousedown', e => { panning = true; moved = false; px0 = e.clientX; py0 = e.clientY; cv.classList.add('panning'); });
addEventListener('mousemove', e => {
  if (panning) {
    const dx = e.clientX - px0, dy = e.clientY - py0;
    if (Math.abs(dx) + Math.abs(dy) > 2) moved = true;
    view.tx += dx; view.ty += dy; px0 = e.clientX; py0 = e.clientY; draw();
  } else {
    const h = pick(e.clientX, e.clientY);
    if (h !== hover) { hover = h; draw(); }
    cv.style.cursor = h ? 'pointer' : 'grab';
  }
});
addEventListener('mouseup', e => {
  cv.classList.remove('panning');
  if (panning && !moved) {
    const n = pick(e.clientX, e.clientY);
    if (n) select(n); else { selected = null; detail(false); draw(); }
  }
  panning = false;
});
cv.addEventListener('wheel', e => {
  e.preventDefault();
  const f = Math.exp(-e.deltaY * 0.0012);
  const mx = (e.clientX - innerWidth / 2), my = (e.clientY - innerHeight / 2);
  view.tx = mx - (mx - view.tx) * f;
  view.ty = my - (my - view.ty) * f;
  view.scale *= f; draw();
}, { passive: false });

function centerOn(n, scale) {
  view.scale = scale || Math.max(view.scale, 1.6);
  view.tx = -n.x * view.scale; view.ty = -n.y * view.scale;
  draw();
}

// detail panel — DOM building, textContent only
const det = document.getElementById('detail');
function detail(show) { det.classList.toggle('show', !!show); }
function _toast(m) {
  const t = document.getElementById('toast'); t.textContent = m; t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 1500);
}
function openInEditor(rel) {
  if (!LIVE) { _toast('editor open needs the live server'); return; }
  fetch('/action', { method: 'POST', headers: { 'Content-Type': 'application/json' },
                     body: JSON.stringify({ action: 'open-path', args: { uri: REPO_ROOT_URI + '/' + rel } }) })
    .then(r => r.json()).then(j => _toast(j.ok ? 'opened in editor' : 'open failed'))
    .catch(() => _toast('open failed'));
}
function soloDept(key) {
  const wasSolo = DATA.depts.every(d => d.key === key ? !hidden.has(d.key) : hidden.has(d.key));
  hidden.clear();
  if (!wasSolo) DATA.depts.forEach(d => { if (d.key !== key) hidden.add(d.key); });
  document.querySelectorAll('#chips .chip').forEach((c, i) => {
    const d = DATA.depts[i];
    if (d) c.classList.toggle('off', hidden.has(d.key));
  });
  draw();
  return !wasSolo;
}
function selectHub(n) {
  // a hub click is a DEPARTMENT view: summary + the freshest members, never a dead end
  while (det.firstChild) det.removeChild(det.firstChild);
  const h3 = document.createElement('h3'); h3.textContent = n.label; det.appendChild(h3);
  const meta = document.createElement('div'); meta.className = 'meta';
  meta.textContent = (n.count || 0) + ' items in the canon';
  det.appendChild(meta);
  const acts = document.createElement('div'); acts.className = 'acts';
  const solo = document.createElement('button');
  const isSolo = DATA.depts.every(d => d.key === n.dept ? !hidden.has(d.key) : hidden.has(d.key));
  solo.textContent = isSolo ? 'show all departments' : 'solo this department';
  solo.addEventListener('click', () => {
    const nowSolo = soloDept(n.dept);
    solo.textContent = nowSolo ? 'show all departments' : 'solo this department';
  });
  acts.appendChild(solo);
  det.appendChild(acts);
  const hd = document.createElement('div'); hd.className = 'meta'; hd.textContent = 'freshest — click to inspect';
  det.appendChild(hd);
  const list = document.createElement('div'); list.className = 'hublist';
  DATA.nodes.filter(m => !m.hub && m.dept === n.dept)
    .sort((a, b) => (b.mt || '').localeCompare(a.mt || '')).slice(0, 8)
    .forEach(m => {
      const b = document.createElement('button'); b.className = 'hubitem';
      b.textContent = (m.mt ? m.mt + '  ' : '') + m.label;
      b.addEventListener('click', () => { select(m); centerOn(m, 1.8); });
      list.appendChild(b);
    });
  det.appendChild(list);
  detail(true);
}
function select(n) {
  selected = n; draw();
  if (n.hub && n.id !== 'claude-md') { centerOn(n, 1.2); selectHub(n); return; }
  while (det.firstChild) det.removeChild(det.firstChild);
  const h3 = document.createElement('h3'); h3.textContent = n.label; det.appendChild(h3);
  const meta = document.createElement('div'); meta.className = 'meta';
  meta.textContent = (n.dept || '') + (n.kind ? ' · ' + n.kind : '') + (n.mt ? ' · edited ' + n.mt : '');
  det.appendChild(meta);
  if (n.rel) {
    const acts = document.createElement('div'); acts.className = 'acts';
    const op = document.createElement('a'); op.textContent = 'open ↗';
    op.href = LIVE ? '/repo/' + n.rel : REPO_ROOT_URI + '/' + n.rel;
    op.target = '_blank';
    acts.appendChild(op);
    const ed = document.createElement('button'); ed.textContent = 'editor';
    ed.title = 'open with the OS default app';
    ed.addEventListener('click', () => openInEditor(n.rel));
    acts.appendChild(ed);
    const cp = document.createElement('button'); cp.textContent = 'copy path';
    cp.addEventListener('click', () => {
      navigator.clipboard && navigator.clipboard.writeText(n.rel).then(() => _toast('path copied'));
    });
    acts.appendChild(cp);
    det.appendChild(acts);
    const pre = document.createElement('pre');
    if (LIVE && /\.(md|py|json|txt|html)$/.test(n.rel)) {
      pre.textContent = 'loading preview…';
      fetch('/repo/' + n.rel).then(r => r.ok ? r.text() : Promise.reject())
        .then(t => { pre.textContent = t.split('\n').slice(0, 60).join('\n'); })
        .catch(() => { pre.textContent = 'preview unavailable'; });
    } else {
      pre.textContent = LIVE ? 'no preview for this type' : 'preview needs the live server (127.0.0.1:8765/brain)';
    }
    det.appendChild(pre);
  }
  detail(true);
}
addEventListener('keydown', e => { if (e.key === 'Escape') { selected = null; detail(false); searchClear(); draw(); } });
cv.addEventListener('dblclick', e => {
  const n = pick(e.clientX, e.clientY);
  if (n && !n.hub && n.rel) window.open(LIVE ? '/repo/' + n.rel : REPO_ROOT_URI + '/' + n.rel, '_blank');
});

// search
const inp = document.getElementById('search');
const hitsEl = document.getElementById('hits');
function searchClear() { searching = false; searchHits.clear(); while (hitsEl.firstChild) hitsEl.removeChild(hitsEl.firstChild); }
inp.addEventListener('input', () => {
  const q = inp.value.trim().toLowerCase();
  searchClear();
  if (q) {
    searching = true;
    const matches = DATA.nodes.filter(n => !n.hub && (n.label.toLowerCase().includes(q) || (n.rel || '').toLowerCase().includes(q)));
    matches.forEach(n => searchHits.add(n.id));
    const hd = document.createElement('div'); hd.className = 'hd';
    hd.textContent = matches.length + ' match' + (matches.length === 1 ? '' : 'es');
    hitsEl.appendChild(hd);
    matches.slice(0, 8).forEach(n => {
      const b = document.createElement('button');
      b.textContent = n.label + '  ·  ' + n.dept;
      b.addEventListener('click', () => { select(n); centerOn(n, 2.0); });
      hitsEl.appendChild(b);
    });
  }
  draw();
});
inp.addEventListener('keydown', e => {
  if (e.key !== 'Enter') return;
  const first = DATA.nodes.find(n => searchHits.has(n.id));
  if (first) { select(first); centerOn(first, 2.0); }
});

// filters
const chipsEl = document.getElementById('chips');
DATA.depts.forEach(d => {
  const c = document.createElement('span'); c.className = 'chip';
  const sw = document.createElement('span'); sw.className = 'sw'; sw.style.background = d.color;
  c.appendChild(sw);
  const t = document.createElement('span'); t.textContent = d.label + ' ' + d.count;
  c.appendChild(t);
  c.addEventListener('click', () => {
    if (hidden.has(d.key)) hidden.delete(d.key); else hidden.add(d.key);
    c.classList.toggle('off', hidden.has(d.key));
    draw();
  });
  chipsEl.appendChild(c);
});
document.getElementById('linkop').addEventListener('input', e => { linkAlpha = parseFloat(e.target.value); draw(); });
document.getElementById('nodesz').addEventListener('input', e => { nodeScale = parseFloat(e.target.value); draw(); });
document.getElementById('resetview').addEventListener('click', () => { view = { tx: 0, ty: 0, scale: 0.9 }; draw(); });

// nav live rewrite (same pattern as every board)
if (LIVE) document.querySelectorAll('a[data-route]').forEach(a => { a.href = a.dataset.route; });

resize();
"""


def render_html(graph):
    try:
        import surface_nav as sn
        nav = sn.nav_html(current="brain", style=False)
    except Exception:
        nav = ""
    data = json.dumps(graph, separators=(",", ":"))
    # embed safely inside a <script type="application/json"> block
    data = data.replace("</", "<\\/")
    js = JS.replace("__REPO_ROOT_URI__", json.dumps(Path(ROOT).as_uri()))
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>second brain · Agentic OS</title>
<style>
{theme_css()}
{CSS}
</style>
<canvas id="cv"></canvas>
<div class="bar">
  <div class="brand"><span class="kicker">FARRICE CAIN · AGENTIC OS</span>
    <h1>second <em>brain</em></h1></div>
  <input id="search" type="search" placeholder="search {graph['total']:,} nodes — skills, briefs, scripts…" autocomplete="off">
  {nav}
</div>
<div id="hits"></div>
<div class="panel">
  <h2>Departments</h2>
  <div id="chips"></div>
  <div class="slider"><label>link opacity</label><input id="linkop" type="range" min="0.02" max="0.5" step="0.02" value="0.14"></div>
  <div class="slider"><label>node size</label><input id="nodesz" type="range" min="0.5" max="2.4" step="0.1" value="1.0"></div>
  <div class="slider"><label>view</label><button id="resetview" class="chip" type="button">reset</button></div>
</div>
<div id="detail"></div>
<div class="foot">{graph['total']:,} nodes · built {_html.escape(graph['generated'][:16])} · drag pans · scroll zooms · click inspects · double-click opens · esc clears</div>
<div id="toast"></div>
<script id="braindata" type="application/json">{data}</script>
<script>
{js}
</script>"""


def main():
    ap = argparse.ArgumentParser(description="Build the second-brain graph surface.")
    ap.add_argument("--if-stale", action="store_true",
                    help="rebuild only when the source fingerprint changed")
    args = ap.parse_args()
    if args.if_stale and not is_stale():
        print("brain → fresh (fingerprint unchanged)")
        return
    t0 = time.time()
    graph = build_graph()
    os.makedirs(OUT_DIR, exist_ok=True)
    json.dump(graph, open(OUT_JSON, "w", encoding="utf-8"), separators=(",", ":"))
    open(OUT_HTML, "w", encoding="utf-8").write(render_html(graph))
    json.dump(fingerprint(), open(FPRINT, "w", encoding="utf-8"))
    print(f"brain → {OUT_HTML}  ({graph['total']:,} nodes, {time.time() - t0:.2f}s)")


if __name__ == "__main__":
    main()
