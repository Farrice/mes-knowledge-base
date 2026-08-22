#!/usr/bin/env python3
"""brain_graph.py — the visual second brain: /brain (v1 2026-08-21; v2 + v3
dark cockpit 2026-08-22).

v3 (Farrice: glow on hover, futuristic-on-brand, kill the residual scatter,
make it a monitor not a museum):
- ORDER: families sit on fixed concentric BANDS per sector (largest inner),
  evenly-spaced slots — the golden-ratio centroid scatter is dead. Dated
  departments (directives/solutions/briefs) group by month; misc pools ride
  the outer band dimmed.
- DARK COCKPIT: /brain defaults to the ink ground (data-theme=dark, 🌓 toggle
  persists) — the one cinematic room of the OS; glow reads only on dark.
- ALIVE: hover bloom + expanding ring pulse, breathing stars, orbiting dash
  on selection, eased zoom, one load sweep. Single ~30fps rAF loop, paused
  when hidden; prefers-reduced-motion → static frame, no loop.
- LIVE LAYER: nodes touched <24h/<48h pulse with a halo; TODAY chip filters
  to the hot set. Deep link /brain?q=term searches + zooms on load.

Every visual channel still carries a variable (Hansen HUD-bible discipline):
angle=department · band/slot=family · size=importance · glow=attention
(hover/star/hot) · color=department. Data embedded — file:// still works.
Allowlist canon only; --if-stale fingerprint keeps per-hit regen O(1).
"""
import argparse
import html as _html
import json
import math
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "execution"))

from board_theme import theme_css  # noqa: E402

OUT_DIR = os.path.join(ROOT, ".agent", "brain")
OUT_JSON = os.path.join(OUT_DIR, "brain.json")
OUT_HTML = os.path.join(OUT_DIR, "brain.html")
FPRINT = os.path.join(OUT_DIR, "fingerprint.json")
SUMMARIES = os.path.join(OUT_DIR, "summaries.json")

PHI = 0.6180339887498949
STAR_COUNT = 44

# key, label, source dir, member rule, color, family split
# ('-'/'_' = name prefix · 'month' = mtime month · None = flat)
DEPARTMENTS = [
    ("directives", "Directives", "directives", "md", "#7c9fd9", "month"),
    ("skills", "Skills", "skills", "dirs", "#5a7fc0", "-"),
    ("agents", "Agents", "agents", "dirs", "#94a9c9", "-"),
    ("active", "Active work", "_active", "dirs", "#c9a868", None),
    ("briefs", "Briefs", "deliverables/research-briefs", "dirs", "#6fae8c", "month"),
    ("solutions", "Solutions", "docs/solutions", "md", "#8fb8a8", "month"),
    ("execution", "Execution", "execution", "py", "#8c8c82", "_"),
    ("knowledge", "Knowledge", "knowledge", "any", "#b9a9c9", None),
]
MIN_FAMILY = 3


def _members(src, rule):
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
        else:
            out.append((name, rel, "dir" if is_dir else "file", mtime))
    return out


def fingerprint():
    fp = {}
    for _k, _l, src, _r, _c, _f in DEPARTMENTS:
        base = os.path.join(ROOT, src)
        try:
            st = os.stat(base)
            n = sum(1 for _ in os.scandir(base))
            fp[src] = [int(st.st_mtime), n]
        except OSError:
            fp[src] = [0, 0]
    for extra in ("CLAUDE.md",):
        try:
            fp[extra] = [int(os.stat(os.path.join(ROOT, extra)).st_mtime), 1]
        except OSError:
            fp[extra] = [0, 0]
    try:
        fp["summaries"] = [int(os.stat(SUMMARIES).st_mtime), 1]
    except OSError:
        fp["summaries"] = [0, 0]
    # the live layer keys off "today" — a date flip must rebuild
    fp["date"] = [time.strftime("%Y-%m-%d"), 0]
    return fp


def is_stale():
    try:
        old = json.load(open(FPRINT, encoding="utf-8"))
    except (OSError, ValueError):
        return True
    if not os.path.isfile(OUT_HTML) or not os.path.isfile(OUT_JSON):
        return True
    return old != fingerprint()


def _recency_score(mtime):
    days = (time.time() - mtime) / 86400
    return 3 if days < 7 else 2 if days < 30 else 1 if days < 120 else 0


def _hot(mtime):
    days = (time.time() - mtime) / 86400
    return 2 if days < 1 else 1 if days < 2 else 0


def _families(members, sep):
    """Real groupings: name-prefix families, or month-of-edit for dated/
    living sets. Prefix groups below MIN_FAMILY pool into 'misc'."""
    if not sep:
        return {"all": members}
    buckets = defaultdict(list)
    for m in members:
        if sep == "month":
            key = time.strftime("%b %y", time.localtime(m[3])).upper()
        else:
            key = m[0].split(sep, 1)[0] if sep in m[0] else m[0]
        buckets[key].append(m)
    fams, misc = {}, []
    for prefix, ms in buckets.items():
        if len(ms) >= MIN_FAMILY:
            fams[prefix] = ms
        else:
            misc.extend(ms)
    if misc:
        fams["misc"] = misc
    return fams


def load_summaries():
    try:
        return json.load(open(SUMMARIES, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def build_graph():
    """Layout: dept = annular sector (angle span ∝ sqrt(count)); families on
    FIXED concentric bands inside their sector — sorted by size, largest
    inner, evenly-spaced slots (order, not organic scatter); members in a
    tight sunflower inside the family disc. Deterministic, zero physics."""
    sums = load_summaries()
    depts = []
    for key, label, src, rule, color, sep in DEPARTMENTS:
        members = _members(src, rule)
        depts.append({"key": key, "label": label, "color": color,
                      "families": _families(members, sep),
                      "count": len(members)})
    total = sum(d["count"] for d in depts) or 1
    weights = [math.sqrt(max(d["count"], 4)) for d in depts]
    wsum = sum(weights)
    R_IN, R_OUT = 210, 640
    GAP = 0.035
    nodes = [{"id": "claude-md", "label": "CLAUDE.MD", "dept": "core", "fam": "",
              "kind": "md", "rel": "CLAUDE.md", "x": 0, "y": 0, "hub": True,
              "imp": 4, "hot": 0,
              "sum": (sums.get("CLAUDE.md") or {}).get(
                  "sum", "The master router — every session starts here.")}]
    fam_out, sector_out = [], []
    ang = -math.pi / 2
    all_members = []
    for d, w in zip(depts, weights):
        span = 2 * math.pi * (w / wsum)
        a0, a1 = ang + GAP / 2, ang + span - GAP / 2
        sector_out.append({"dept": d["key"], "label": d["label"],
                           "color": d["color"], "a0": round(a0, 4),
                           "a1": round(a1, 4), "count": d["count"]})
        # order: largest first, misc always last (outer band, dimmed)
        fam_items = sorted(d["families"].items(),
                           key=lambda kv: (kv[0] == "misc", -len(kv[1]), kv[0]))
        n_f = len(fam_items)
        n_bands = 1 if n_f <= 2 else 2 if n_f <= 8 else 3
        band_radii = {1: [(R_IN + R_OUT) / 2 - 40],
                      2: [R_IN + 115, R_IN + 300],
                      3: [R_IN + 95, R_IN + 235, R_IN + 380]}[n_bands]
        # distribute families across bands: round-robin fill keeps slot
        # counts even so angular spacing stays wide
        bands = [[] for _ in range(n_bands)]
        for fi, item in enumerate(fam_items):
            bands[fi % n_bands].append(item)
        for bi, band in enumerate(bands):
            for si, (fname, members) in enumerate(band):
                fr = 15 + 8.5 * math.sqrt(len(members))
                fa = a0 + (a1 - a0) * ((si + 0.5) / max(len(band), 1))
                br = band_radii[bi] + (18 if bi == n_bands - 1 and fname == "misc" else 0)
                cx, cy = br * math.cos(fa), br * math.sin(fa)
                fid = f"{d['key']}:{fname}"
                fam_out.append({"id": fid, "dept": d["key"], "label": fname,
                                "x": round(cx, 1), "y": round(cy, 1),
                                "r": round(fr, 1), "count": len(members),
                                "dim": 1 if fname == "misc" else 0})
                for i, (label, rel, kind, mtime) in enumerate(members):
                    mt_r = fr * 0.82 * math.sqrt((i + 0.5) / max(len(members), 1))
                    mt_a = 2 * math.pi * ((i * PHI) % 1.0)
                    imp = _recency_score(mtime) + (1 if kind == "dir" else 0)
                    all_members.append({
                        "id": f"{d['key']}-{len(all_members)}", "label": label,
                        "dept": d["key"], "fam": fid, "kind": kind, "rel": rel,
                        "x": round(cx + mt_r * math.cos(mt_a), 1),
                        "y": round(cy + mt_r * math.sin(mt_a), 1),
                        "imp": imp, "hot": _hot(mtime),
                        "mt": time.strftime("%Y-%m-%d", time.localtime(mtime)),
                        "sum": (sums.get(rel) or {}).get("sum", "")})
        ang += span
    by_imp = sorted(all_members, key=lambda n: -n["imp"])
    per_dept_cap = max(3, STAR_COUNT // len(depts))
    star_ids, dept_seen = set(), defaultdict(int)
    for n in by_imp:
        if len(star_ids) >= STAR_COUNT:
            break
        if dept_seen[n["dept"]] >= per_dept_cap + 2:
            continue
        star_ids.add(n["id"])
        dept_seen[n["dept"]] += 1
    for n in all_members:
        n["star"] = 1 if n["id"] in star_ids else 0
    nodes.extend(all_members)
    covered = sum(1 for n in all_members if n.get("sum"))
    hot_count = sum(1 for n in all_members if n["hot"])
    return {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "total": len(all_members), "sum_covered": covered,
            "hot_count": hot_count,
            "depts": [{"key": d["key"], "label": d["label"], "color": d["color"],
                       "count": d["count"]} for d in depts],
            "sectors": sector_out, "families": fam_out, "nodes": nodes}


CSS = """
* { box-sizing:border-box; }
html, body { height:100%; }
body { background:var(--ground); color:var(--ink); font:14px/1.5 var(--sans); margin:0; overflow:hidden;
  background-image:radial-gradient(color-mix(in oklab, var(--line) 60%, transparent) 1px, transparent 1px);
  background-size:26px 26px; }
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
  border:1px solid var(--line); border-radius:99px; padding:8px 16px; width:320px; outline:none; }
#search:focus { border-color:var(--accent); box-shadow:0 0 12px color-mix(in oklab, var(--accent) 35%, transparent); }
.homenav { margin-left:auto; display:flex; gap:6px; flex-wrap:wrap; }
.homenav a, .homenav .here { font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase;
  text-decoration:none; color:var(--soft); border:1px solid var(--line); border-radius:99px; padding:4px 11px; background:var(--panel); }
.homenav a:hover { border-color:var(--accent); color:var(--accent); }
.homenav .here { opacity:.45; border-style:dashed; }
#hits { position:fixed; top:64px; left:20px; width:400px; display:flex; flex-direction:column; gap:4px; z-index:10; }
#hits button { text-align:left; font:12px/1.4 var(--sans); background:var(--panel); color:var(--ink);
  border:1px solid var(--line); border-radius:6px; padding:7px 11px; cursor:pointer; }
#hits button .hs { display:block; font-size:11px; color:var(--muted); margin-top:1px; }
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
.chip.hoton { border-color:var(--warn); color:var(--warn); }
.slider { display:flex; align-items:center; gap:8px; margin-top:8px; flex-wrap:wrap; }
.slider label { font-family:var(--mono); font-size:8px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); flex:1; }
#hovercard { position:fixed; z-index:30; width:290px; background:var(--panel); border:1px solid var(--accent);
  border-radius:8px; padding:11px 13px; pointer-events:none; display:none;
  box-shadow:0 0 24px color-mix(in oklab, var(--accent) 22%, transparent); }
#hovercard.show { display:block; }
#hovercard .hk { display:flex; gap:8px; align-items:baseline; margin-bottom:3px; }
#hovercard .badge { font-family:var(--mono); font-size:7.5px; letter-spacing:.14em; text-transform:uppercase;
  padding:2px 7px; border-radius:3px; border:1px solid var(--line); color:var(--soft); }
#hovercard h4 { font-size:12.5px; font-weight:700; margin:0; line-height:1.3; }
#hovercard .hsum { font-size:11.5px; line-height:1.5; color:var(--ink); margin:4px 0 5px; }
#hovercard .hmeta { font-family:var(--mono); font-size:8px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); }
#detail { position:fixed; left:16px; bottom:16px; width:390px; max-height:52vh; overflow:auto; background:var(--panel);
  border:1px solid var(--line); border-radius:8px; padding:14px 16px; z-index:10; display:none; }
#detail.show { display:block; }
#detail h3 { font-size:14px; font-weight:700; margin:0 0 2px; }
#detail .dsum { font-size:12px; line-height:1.55; margin:4px 0 8px; color:var(--ink);
  border-left:2px solid var(--accent); padding-left:10px; }
#detail .meta { font-family:var(--mono); font-size:8.5px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); margin-bottom:8px; }
#detail .acts { display:flex; gap:6px; margin-bottom:8px; flex-wrap:wrap; }
#detail button, #detail a { font-family:var(--mono); font-size:8.5px; letter-spacing:.12em; text-transform:uppercase;
  cursor:pointer; background:none; border:1px solid var(--line); border-radius:4px; padding:3px 9px; color:var(--soft); text-decoration:none; }
#detail button:hover, #detail a:hover { border-color:var(--accent); color:var(--accent); }
#detail pre { font:10.5px/1.5 var(--mono); background:var(--ground); border:1px solid var(--line); border-radius:6px;
  padding:10px; white-space:pre-wrap; word-break:break-word; max-height:22vh; overflow:auto; margin:0; }
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
const MONO = 'JetBrains Mono, Menlo, monospace';
const colors = {}; DATA.depts.forEach(d => colors[d.key] = d.color);
const famById = {}; DATA.families.forEach(f => famById[f.id] = f);
const center = DATA.nodes.find(n => n.id === 'claude-md');
const members = DATA.nodes.filter(n => !n.hub);
const hotSet = members.filter(n => n.hot);
const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
function fitScale() {
  return Math.max(0.3, Math.min(innerWidth || 1280, innerHeight || 800) / 1520);
}
let view = { tx: 0, ty: 0, scale: fitScale() };
const hidden = new Set();
let hover = null, selected = null, searchHits = new Set(), searching = false;
let hotOnly = false;
let T = 0;                    // animation clock (seconds)
let animT0 = null;            // first ANIMATED frame timestamp (sweep base)
function animAge() { return animT0 === null ? -1 : (performance.now() - animT0) / 1000; }
let hoverPulseT = -9;         // when the current hover began (for ring pulse)
function lod() { return view.scale < 0.85 ? 0 : view.scale < 1.7 ? 1 : 2; }
function isDark() { return (document.documentElement.dataset.theme || 'dark') !== 'light'; }
function css(v) { return getComputedStyle(document.documentElement).getPropertyValue(v).trim(); }

function resize() {
  cv.width = innerWidth * DPR; cv.height = innerHeight * DPR;
  cv.style.width = innerWidth + 'px'; cv.style.height = innerHeight + 'px';
  if (view.scale < 0.31 && view.tx === 0 && view.ty === 0) view.scale = fitScale();
  draw();
}
addEventListener('resize', resize);
function S(x, y) {
  return [ (x * view.scale + view.tx) * DPR + cv.width / 2,
           (y * view.scale + view.ty) * DPR + cv.height / 2 ];
}
function nodeR(n) {
  const base = n.id === 'claude-md' ? 14 : (2 + n.imp * 1.1 + (n.star ? 2.5 : 0));
  return base * DPR * Math.min(Math.max(view.scale, 0.55), 1.6);
}
function visible(n) { return !hidden.has(n.dept) && (!hotOnly || n.hot || n.hub); }
function dimmedBySearch(n) { return searching && !searchHits.has(n.id); }

function glow(x, y, r, color, alpha, blur) {
  // additive bloom — the futurism budget, spent only on nodes that carry
  // attention (hover/star/hot/selected); intensity collapses on light theme
  const k = isDark() ? 1 : 0.35;
  ctx.save();
  ctx.globalCompositeOperation = 'lighter';
  ctx.shadowColor = color;
  ctx.shadowBlur = blur * k;
  ctx.globalAlpha = alpha * k;
  ctx.fillStyle = color;
  ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.fill();
  ctx.restore();
}

function arcLabel(sec, r, ink) {
  let label = (sec.label + ' · ' + sec.count).toUpperCase();
  const mid = (sec.a0 + sec.a1) / 2;
  const flip = Math.sin(mid) > 0;
  if (flip) label = label.split('').reverse().join('');
  const per = 11.5 / (r * view.scale) * 1.15;
  let a = mid - per * label.length / 2;
  ctx.font = `${9.5 * DPR}px ${MONO}`;
  ctx.fillStyle = ink;
  for (const chch of label) {
    const [x, y] = S(r * Math.cos(a), r * Math.sin(a));
    ctx.save(); ctx.translate(x, y);
    ctx.rotate(a + (flip ? -Math.PI / 2 : Math.PI / 2));
    ctx.textAlign = 'center';
    ctx.fillText(chch, 0, 0);
    ctx.restore();
    a += per;
  }
}

function draw() {
  const ink = css('--ink'), muted = css('--muted'), accent = css('--accent');
  ctx.clearRect(0, 0, cv.width, cv.height);
  const L = lod();
  // sweepAge counts ANIMATED frames only — a suspended rAF (hidden pane)
  // must never leave arcs/labels stuck at 0 alpha, so nothing else fades
  const sweepAge = animAge();
  const intro = 1;
  // ── sectors ──
  DATA.sectors.forEach((sec, si) => {
    if (hidden.has(sec.dept)) return;
    const a = 1;
    const [cx, cy] = S(0, 0);
    const r1 = 180 * view.scale * DPR, r2 = 680 * view.scale * DPR;
    ctx.beginPath();
    ctx.arc(cx, cy, r2, sec.a0, sec.a1);
    ctx.arc(cx, cy, r1, sec.a1, sec.a0, true);
    ctx.closePath();
    ctx.globalAlpha = 0.055 * a; ctx.fillStyle = sec.color; ctx.fill();
    ctx.globalAlpha = 0.35 * a; ctx.strokeStyle = sec.color; ctx.lineWidth = 1 * DPR; ctx.stroke();
    ctx.globalAlpha = a;
    arcLabel(sec, si % 2 ? 742 : 700, muted);
  });
  ctx.globalAlpha = 0.18 * intro; ctx.lineWidth = 1 * DPR;
  for (const sec of DATA.sectors) {
    if (hidden.has(sec.dept)) continue;
    const mid = (sec.a0 + sec.a1) / 2;
    const [x1, y1] = S(0, 0), [x2, y2] = S(180 * Math.cos(mid), 180 * Math.sin(mid));
    ctx.strokeStyle = sec.color;
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
  }
  ctx.globalAlpha = 1;
  // ── load radar sweep (once, first 1.8s of ANIMATED time) ──
  if (!REDUCED && sweepAge >= 0 && sweepAge < 1.8) {
    const [cx, cy] = S(0, 0);
    const sa = -Math.PI / 2 + sweepAge * 3.6;
    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    ctx.globalAlpha = 0.5 * (1 - sweepAge / 1.8);
    ctx.strokeStyle = accent; ctx.lineWidth = 1.4 * DPR;
    ctx.beginPath(); ctx.moveTo(cx, cy);
    ctx.lineTo(cx + Math.cos(sa) * 700 * view.scale * DPR,
               cy + Math.sin(sa) * 700 * view.scale * DPR);
    ctx.stroke();
    ctx.restore();
  }
  // ── families ──
  if (L >= 1) {
    for (const f of DATA.families) {
      if (hidden.has(f.dept)) continue;
      const dimF = f.dim ? 0.5 : 1;
      const [x, y] = S(f.x, f.y);
      const r = f.r * view.scale * DPR;
      ctx.globalAlpha = 0.10 * dimF; ctx.fillStyle = colors[f.dept];
      ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.fill();
      ctx.globalAlpha = 0.5 * dimF; ctx.strokeStyle = colors[f.dept];
      ctx.lineWidth = 0.8 * DPR;
      ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.stroke();
      ctx.globalAlpha = 1;
      if ((f.count >= 5 && f.label !== 'misc' && f.label !== 'all') || L === 2) {
        ctx.font = `${8.5 * DPR}px ${MONO}`;
        ctx.fillStyle = muted; ctx.textAlign = 'center';
        ctx.globalAlpha = dimF;
        ctx.fillText(f.label.toUpperCase() + ' ' + f.count, x, y - r - 5 * DPR);
        ctx.globalAlpha = 1;
      }
    }
  }
  // ── members ──
  const W = cv.width, H = cv.height;
  for (const n of members) {
    if (!visible(n)) continue;
    const isStar = !!n.star;
    if (L === 0 && !isStar && n.hot !== 2) continue;
    const [x, y] = S(n.x, n.y);
    if (x < -40 || y < -40 || x > W + 40 || y > H + 40) continue;
    const dim = dimmedBySearch(n);
    if (L === 1 && !isStar && !n.hot) {
      ctx.globalAlpha = dim ? 0.05 : 0.30;
      ctx.fillStyle = colors[n.dept];
      ctx.beginPath(); ctx.arc(x, y, 1.4 * DPR * view.scale, 0, 7); ctx.fill();
      continue;
    }
    ctx.globalAlpha = dim ? 0.08 : (0.45 + n.imp * 0.14);
    ctx.fillStyle = colors[n.dept];
    ctx.beginPath(); ctx.arc(x, y, nodeR(n), 0, 7); ctx.fill();
    if (isStar && !dim) {
      // breathing star bloom — staggered phase keeps the field alive, not strobing
      const breathe = REDUCED ? 0.5 : 0.5 + 0.28 * Math.sin(T * 1.3 + n.x * 0.05);
      glow(x, y, nodeR(n) * 0.9, colors[n.dept], 0.35 * breathe, 14 * DPR);
      ctx.globalAlpha = 0.85;
      ctx.strokeStyle = accent; ctx.lineWidth = 1.1 * DPR;
      ctx.beginPath(); ctx.arc(x, y, nodeR(n) + 2.5 * DPR, 0, 7); ctx.stroke();
    }
    if (n.hot && !dim && (L >= 1 || n.hot === 2)) {
      // live-layer halo: the map shows what the system touched today
      const p = REDUCED ? 0.5 : 0.5 + 0.5 * Math.sin(T * 2.4 + n.y * 0.07);
      const hr = nodeR(n) + (5 + 3 * p) * DPR;
      ctx.save();
      ctx.globalAlpha = (n.hot === 2 ? 0.5 : 0.28) * (0.5 + 0.5 * p) * (isDark() ? 1 : 0.5);
      ctx.strokeStyle = css('--warn'); ctx.lineWidth = 1.2 * DPR;
      ctx.beginPath(); ctx.arc(x, y, hr, 0, 7); ctx.stroke();
      ctx.restore();
      if (n.hot === 2) glow(x, y, nodeR(n), css('--warn'), 0.18, 10 * DPR);
    }
    if (n === selected) {
      // orbiting dash — the pinned node keeps a satellite
      ctx.save();
      ctx.strokeStyle = accent; ctx.lineWidth = 1.2 * DPR;
      ctx.setLineDash([5 * DPR, 7 * DPR]);
      ctx.lineDashOffset = REDUCED ? 0 : -T * 26 * DPR;
      ctx.globalAlpha = 0.9;
      ctx.beginPath(); ctx.arc(x, y, nodeR(n) + 6 * DPR, 0, 7); ctx.stroke();
      ctx.restore();
    }
    if (n === hover) {
      glow(x, y, nodeR(n) * 1.15, colors[n.dept], 0.55, 22 * DPR);
      const p = (T - hoverPulseT) / 0.45;
      if (p >= 0 && p < 1 && !REDUCED) {
        ctx.save();
        ctx.globalAlpha = (1 - p) * 0.6;
        ctx.strokeStyle = accent; ctx.lineWidth = 1.3 * DPR;
        ctx.beginPath(); ctx.arc(x, y, nodeR(n) + (4 + 30 * p) * DPR, 0, 7); ctx.stroke();
        ctx.restore();
      }
      ctx.globalAlpha = 1; ctx.strokeStyle = ink; ctx.lineWidth = 1.2 * DPR;
      ctx.beginPath(); ctx.arc(x, y, nodeR(n) + 3.5 * DPR, 0, 7); ctx.stroke();
    }
  }
  // ── star labels (collision-skipped) ──
  if (L <= 1) {
    ctx.font = `${8.5 * DPR}px ${MONO}`; ctx.textAlign = 'center';
    const placed = [];
    for (const n of members) {
      if (!n.star || !visible(n) || dimmedBySearch(n)) continue;
      const [x, y] = S(n.x, n.y);
      if (x < 0 || y < 0 || x > W || y > H) continue;
      const label = n.label.slice(0, 22);
      const w = ctx.measureText(label).width + 8 * DPR, h = 13 * DPR;
      const ly = y - nodeR(n) - 5 * DPR;
      const box = [x - w / 2, ly - h, x + w / 2, ly];
      if (placed.some(b => box[0] < b[2] && box[2] > b[0] && box[1] < b[3] && box[3] > b[1]))
        continue;
      placed.push(box);
      ctx.globalAlpha = 0.8 * intro; ctx.fillStyle = ink;
      ctx.fillText(label, x, ly);
    }
  }
  // ── center core ──
  const [ccx, ccy] = S(0, 0);
  ctx.globalAlpha = 1;
  glow(ccx, ccy, nodeR(center) * 0.9, accent, 0.5, 26 * DPR);
  ctx.fillStyle = accent;
  ctx.beginPath(); ctx.arc(ccx, ccy, nodeR(center), 0, 7); ctx.fill();
  ctx.strokeStyle = ink; ctx.lineWidth = 1 * DPR;
  ctx.globalAlpha = 0.9;
  ctx.beginPath(); ctx.arc(ccx, ccy, nodeR(center) + 5 * DPR, 0, 7); ctx.stroke();
  ctx.globalAlpha = 1;
  ctx.font = `700 ${10.5 * DPR}px ${MONO}`; ctx.textAlign = 'center'; ctx.fillStyle = ink;
  ctx.fillText('CLAUDE.MD', ccx, ccy - nodeR(center) - 9 * DPR);
  const focus = hover || selected;
  if (focus && !focus.hub && lod() === 2) {
    const [x, y] = S(focus.x, focus.y);
    ctx.font = `${9.5 * DPR}px ${MONO}`; ctx.fillStyle = ink; ctx.textAlign = 'center';
    ctx.fillText(focus.label, x, y - nodeR(focus) - 5 * DPR);
  }
}

// ── the one animation loop: ~30fps, hidden-paused; reduced-motion = none ──
let lastFrame = 0;
function loop(ts) {
  requestAnimationFrame(loop);
  if (document.hidden) return;
  if (ts - lastFrame < 33) return;
  if (animT0 === null) animT0 = ts;
  lastFrame = ts; T = ts / 1000;
  if (tween) {
    const p = Math.min(1, (ts - tween.t0) / tween.dur);
    const e = 1 - Math.pow(1 - p, 3); // easeOutCubic
    view.tx = tween.fx + (tween.tx - tween.fx) * e;
    view.ty = tween.fy + (tween.ty - tween.fy) * e;
    view.scale = tween.fs + (tween.ts_ - tween.fs) * e;
    if (p >= 1) tween = null;
  }
  draw();
}
let tween = null;
function zoomTo(x, y, scale) {
  if (REDUCED) { view.scale = scale; view.tx = -x * scale; view.ty = -y * scale; draw(); return; }
  tween = { t0: performance.now(), dur: 380, fx: view.tx, fy: view.ty, fs: view.scale,
            tx: -x * scale, ty: -y * scale, ts_: scale };
}
if (!REDUCED) requestAnimationFrame(loop);

function pick(mx, my) {
  const px = mx * DPR, py = my * DPR;
  const L = lod();
  let best = null, bd = 14 * DPR;
  const cands = L === 0 ? members.filter(n => n.star || n.hot) : members;
  for (const n of cands) {
    if (!visible(n)) continue;
    const [x, y] = S(n.x, n.y);
    const d = Math.hypot(px - x, py - y) - nodeR(n);
    if (d < bd) { bd = d; best = n; }
  }
  {
    const [x, y] = S(0, 0);
    if (Math.hypot(px - x, py - y) < nodeR(center) + 6 * DPR) best = center;
  }
  if (!best && L >= 1) {
    for (const f of DATA.families) {
      if (hidden.has(f.dept)) continue;
      const [x, y] = S(f.x, f.y);
      if (Math.hypot(px - x, py - y) < f.r * view.scale * DPR) return { famPick: f };
    }
  }
  return best;
}

let panning = false, px0 = 0, py0 = 0, moved = false;
cv.addEventListener('mousedown', e => { panning = true; moved = false; px0 = e.clientX; py0 = e.clientY; cv.classList.add('panning'); });
addEventListener('mousemove', e => {
  if (panning) {
    const dx = e.clientX - px0, dy = e.clientY - py0;
    if (Math.abs(dx) + Math.abs(dy) > 2) moved = true;
    tween = null;
    view.tx += dx; view.ty += dy; px0 = e.clientX; py0 = e.clientY;
    hideHover(); if (REDUCED) draw();
    return;
  }
  onHoverMove(e);
});
addEventListener('mouseup', e => {
  cv.classList.remove('panning');
  if (panning && !moved) {
    const n = pick(e.clientX, e.clientY);
    if (n && n.famPick) { zoomTo(n.famPick.x, n.famPick.y, 2.0); }
    else if (n) select(n);
    else { selected = null; detail(false); if (REDUCED) draw(); }
  }
  panning = false;
});
cv.addEventListener('wheel', e => {
  e.preventDefault();
  tween = null;
  const f = Math.exp(-e.deltaY * 0.0012);
  const mx = (e.clientX - innerWidth / 2), my = (e.clientY - innerHeight / 2);
  view.tx = mx - (mx - view.tx) * f;
  view.ty = my - (my - view.ty) * f;
  view.scale *= f; hideHover(); if (REDUCED) draw();
}, { passive: false });
cv.addEventListener('dblclick', e => {
  const n = pick(e.clientX, e.clientY);
  if (n && !n.hub && n.rel && !n.famPick)
    window.open(LIVE ? '/repo/' + n.rel : REPO_ROOT_URI + '/' + n.rel, '_blank');
});

const hcard = document.getElementById('hovercard');
let hoverTimer = null;
function hideHover() {
  if (hoverTimer) clearTimeout(hoverTimer);
  hcard.classList.remove('show');
  if (hover) { hover = null; if (REDUCED) draw(); }
}
function onHoverMove(e) {
  const n = pick(e.clientX, e.clientY);
  cv.style.cursor = n ? 'pointer' : 'grab';
  if (!n || n.famPick) { hideHover(); return; }
  if (n !== hover) {
    if (hoverTimer) clearTimeout(hoverTimer);
    hover = n; hoverPulseT = T;
    if (REDUCED) draw();
    hoverTimer = setTimeout(() => showHover(n, e.clientX, e.clientY), 300);
  }
}
function showHover(n, mx, my) {
  while (hcard.firstChild) hcard.removeChild(hcard.firstChild);
  const hk = document.createElement('div'); hk.className = 'hk';
  const badge = document.createElement('span'); badge.className = 'badge';
  badge.textContent = n.dept === 'core' ? 'router' : n.dept;
  badge.style.borderColor = colors[n.dept] || css('--line');
  badge.style.color = colors[n.dept] || css('--soft');
  hk.appendChild(badge);
  if (n.hot) {
    const hb = document.createElement('span'); hb.className = 'badge';
    hb.textContent = n.hot === 2 ? '● today' : '● recent';
    hb.style.borderColor = css('--warn'); hb.style.color = css('--warn');
    hk.appendChild(hb);
  }
  const h4 = document.createElement('h4'); h4.textContent = n.label; hk.appendChild(h4);
  hcard.appendChild(hk);
  const sum = document.createElement('div'); sum.className = 'hsum';
  sum.textContent = n.sum || 'No snapshot yet — summaries refresh with brain_summaries.py.';
  hcard.appendChild(sum);
  const meta = document.createElement('div'); meta.className = 'hmeta';
  const fam = n.fam && famById[n.fam] ? famById[n.fam].label : '';
  meta.textContent = [fam !== 'all' ? fam : '', n.kind, n.mt ? 'edited ' + n.mt : '',
                      n.star ? '★ star' : ''].filter(Boolean).join(' · ');
  hcard.appendChild(meta);
  hcard.classList.add('show');
  const w = hcard.offsetWidth, h = hcard.offsetHeight;
  hcard.style.left = Math.min(mx + 18, innerWidth - w - 12) + 'px';
  hcard.style.top = Math.min(Math.max(my - h / 2, 10), innerHeight - h - 12) + 'px';
}

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
function select(n) {
  selected = n; hideHover(); if (REDUCED) draw();
  while (det.firstChild) det.removeChild(det.firstChild);
  const h3 = document.createElement('h3'); h3.textContent = n.label; det.appendChild(h3);
  if (n.sum) {
    const s = document.createElement('div'); s.className = 'dsum'; s.textContent = n.sum;
    det.appendChild(s);
  }
  const meta = document.createElement('div'); meta.className = 'meta';
  const fam = n.fam && famById[n.fam] ? famById[n.fam].label : '';
  meta.textContent = [n.dept, fam !== 'all' ? fam : '', n.kind,
                      n.mt ? 'edited ' + n.mt : '', n.hot ? '● hot' : '']
    .filter(Boolean).join(' · ');
  det.appendChild(meta);
  if (n.rel) {
    const acts = document.createElement('div'); acts.className = 'acts';
    const op = document.createElement('a'); op.textContent = 'open ↗';
    op.href = LIVE ? '/repo/' + n.rel : REPO_ROOT_URI + '/' + n.rel;
    op.target = '_blank'; acts.appendChild(op);
    const ed = document.createElement('button'); ed.textContent = 'editor';
    ed.title = 'open with the OS default app';
    ed.addEventListener('click', () => openInEditor(n.rel)); acts.appendChild(ed);
    const cp = document.createElement('button'); cp.textContent = 'copy path';
    cp.addEventListener('click', () => {
      navigator.clipboard && navigator.clipboard.writeText(n.rel).then(() => _toast('path copied'));
    }); acts.appendChild(cp);
    const zm = document.createElement('button'); zm.textContent = 'zoom to';
    zm.addEventListener('click', () => zoomTo(n.x, n.y, 2.2)); acts.appendChild(zm);
    det.appendChild(acts);
    const pre = document.createElement('pre');
    if (LIVE && /\.(md|py|json|txt|html)$/.test(n.rel)) {
      pre.textContent = 'loading preview…';
      fetch('/repo/' + n.rel).then(r => r.ok ? r.text() : Promise.reject())
        .then(t => { pre.textContent = t.split('\n').slice(0, 60).join('\n'); })
        .catch(() => { pre.textContent = 'preview unavailable'; });
    } else {
      pre.textContent = LIVE ? 'no preview for this type' : 'preview needs the live server';
    }
    det.appendChild(pre);
  }
  detail(true);
}
addEventListener('keydown', e => {
  if (e.key === 'Escape') { selected = null; detail(false); hideHover(); searchClear(); if (REDUCED) draw(); }
});

const inp = document.getElementById('search');
const hitsEl = document.getElementById('hits');
function searchClear() {
  searching = false; searchHits.clear();
  while (hitsEl.firstChild) hitsEl.removeChild(hitsEl.firstChild);
  inp.value = '';
}
function runSearch(q) {
  searching = !!q; searchHits.clear();
  while (hitsEl.firstChild) hitsEl.removeChild(hitsEl.firstChild);
  let matches = [];
  if (q) {
    matches = members.filter(n =>
      n.label.toLowerCase().includes(q) || (n.sum || '').toLowerCase().includes(q)
      || (n.rel || '').toLowerCase().includes(q));
    // name hits outrank path hits outrank snapshot hits; ties break on recency
    const rank = n => (n.label.toLowerCase().includes(q) ? 0
                       : (n.rel || '').toLowerCase().includes(q) ? 1 : 2);
    matches.sort((a, b) => rank(a) - rank(b) || (b.mt || '').localeCompare(a.mt || ''));
    matches.forEach(n => searchHits.add(n.id));
    const hd = document.createElement('div'); hd.className = 'hd';
    hd.textContent = matches.length + ' match' + (matches.length === 1 ? '' : 'es');
    hitsEl.appendChild(hd);
    matches.slice(0, 7).forEach(n => {
      const b = document.createElement('button');
      const t = document.createElement('span'); t.textContent = n.label + '  ·  ' + n.dept;
      b.appendChild(t);
      if (n.sum) { const s = document.createElement('span'); s.className = 'hs';
        s.textContent = n.sum.slice(0, 90); b.appendChild(s); }
      b.addEventListener('click', () => { select(n); zoomTo(n.x, n.y, 2.2); });
      hitsEl.appendChild(b);
    });
  }
  if (REDUCED) draw();
  return matches;
}
inp.addEventListener('input', () => runSearch(inp.value.trim().toLowerCase()));
inp.addEventListener('keydown', e => {
  if (e.key !== 'Enter') return;
  const first = members.find(n => searchHits.has(n.id));
  if (first) { select(first); zoomTo(first.x, first.y, 2.2); }
});

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
    if (REDUCED) draw();
  });
  chipsEl.appendChild(c);
});
// live-layer chip: TODAY count doubles as the hot-only filter
const hotChip = document.getElementById('hotchip');
if (hotChip) hotChip.addEventListener('click', () => {
  hotOnly = !hotOnly;
  hotChip.classList.toggle('hoton', hotOnly);
  if (REDUCED) draw();
});
// dark-cockpit toggle — /brain is dark by default; choice persists
const themeBtn = document.getElementById('themetoggle');
if (themeBtn) themeBtn.addEventListener('click', () => {
  const next = isDark() ? 'light' : 'dark';
  document.documentElement.dataset.theme = next;
  try { localStorage.setItem('brain_theme', next); } catch (e) {}
  if (REDUCED) draw();
});
document.getElementById('resetview').addEventListener('click', () => {
  tween = null; view = { tx: 0, ty: 0, scale: fitScale() }; hidden.clear(); hotOnly = false;
  if (hotChip) hotChip.classList.remove('hoton');
  document.querySelectorAll('#chips .chip').forEach(c => c.classList.remove('off'));
  if (REDUCED) draw();
});
if (LIVE) document.querySelectorAll('a[data-route]').forEach(a => { a.href = a.dataset.route; });
resize();
// deep link: /brain?q=term → search + zoom first hit
(function () {
  const q = new URLSearchParams(location.search).get('q');
  if (!q) return;
  inp.value = q;
  const matches = runSearch(q.toLowerCase());
  if (matches.length) { select(matches[0]); zoomTo(matches[0].x, matches[0].y, 2.2); }
})();
"""


def render_html(graph):
    try:
        import surface_nav as sn
        nav = sn.nav_html(current="brain", style=False)
    except Exception:
        nav = ""
    data = json.dumps(graph, separators=(",", ":")).replace("</", "<\\/")
    js = JS.replace("__REPO_ROOT_URI__", json.dumps(Path(ROOT).as_uri()))
    cov = graph["sum_covered"]
    hot = graph["hot_count"]
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>second brain · Agentic OS</title>
<script>/* dark cockpit before first paint (Farrice 2026-08-22) */
document.documentElement.dataset.theme = (function () {{
  try {{ return localStorage.getItem('brain_theme') || 'dark'; }} catch (e) {{ return 'dark'; }}
}})();</script>
<style>
{theme_css()}
{CSS}
</style>
<canvas id="cv"></canvas>
<div class="bar">
  <div class="brand"><span class="kicker">FARRICE CAIN · AGENTIC OS</span>
    <h1>second <em>brain</em></h1></div>
  <input id="search" type="search" placeholder="search {graph['total']:,} nodes + snapshots…" autocomplete="off">
  {nav}
</div>
<div id="hits"></div>
<div class="panel">
  <h2>Departments</h2>
  <div id="chips"></div>
  <div class="slider">
    <span class="chip" id="hotchip" title="show only what was touched in the last 48h">● today {hot}</span>
    <span class="chip" id="themetoggle" title="cockpit dark / paper light">🌓</span>
    <button id="resetview" class="chip" type="button">reset</button>
  </div>
</div>
<div id="hovercard"></div>
<div id="detail"></div>
<div class="foot">{graph['total']:,} nodes · {cov:,} snapshots · {hot} hot · zoom = detail · hover = snapshot · click = inspect · dbl-click = open · esc</div>
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
    from board_theme import atomic_write
    atomic_write(OUT_HTML, render_html(graph))
    json.dump(fingerprint(), open(FPRINT, "w", encoding="utf-8"))
    print(f"brain → {OUT_HTML}  ({graph['total']:,} nodes, "
          f"{len(graph['families'])} families, {graph['sum_covered']:,} snapshots, "
          f"{graph['hot_count']} hot, {time.time() - t0:.2f}s)")


if __name__ == "__main__":
    main()
