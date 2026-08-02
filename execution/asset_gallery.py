#!/usr/bin/env python3
"""Asset Command Center board — renders .agent/assets/assets-board.html.

Companion to execution/asset_index.py (which owns the manifest). This script:
  1. generates incremental thumbnails into .agent/assets/thumbs/
     (sips for images, ffmpeg poster-frame for videos, inline glyph otherwise)
  2. renders a self-contained masonry board (file://, no server) with
     filter chips, search, sort, lightbox, copy-path, and a Styles panel
     read from skills/generate/styles/<slug>/ (hidden when absent).

All manifest strings are HTML-escaped client-side (esc()) before insertion —
prompts are arbitrary text and must never be interpreted as markup.

CLI:
  python3 execution/asset_gallery.py                 # thumbs (incremental) + render
  python3 execution/asset_gallery.py --quick         # same, engine post-run hook
  python3 execution/asset_gallery.py --embed --recent 60
      # ALSO writes assets-highlights.html with base64 thumbs (Artifact-publishable)

The board itself is never published as an Artifact (file:// images can't
resolve from claude.ai) — publish the highlights file instead.
"""
import base64
import hashlib
import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, ".agent", "assets")
BOARD = os.path.join(OUT_DIR, "assets-board.html")
HIGHLIGHTS = os.path.join(OUT_DIR, "assets-highlights.html")
THUMBS = os.path.join(OUT_DIR, "thumbs")
STYLES_DIR = os.path.join(ROOT, "skills", "generate", "styles")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from asset_index import reduced_manifest  # noqa: E402


def thumb_name(rel_path):
    return hashlib.sha1(rel_path.encode("utf-8")).hexdigest()[:16] + ".jpg"


def make_thumb(abs_src, dest, kind):
    try:
        if kind == "image":
            r = subprocess.run(["sips", "-Z", "480", "-s", "format", "jpeg",
                                "-s", "formatOptions", "70", abs_src, "--out", dest],
                               capture_output=True, timeout=30)
        elif kind == "video":
            r = subprocess.run(["ffmpeg", "-y", "-ss", "1", "-i", abs_src, "-frames:v", "1",
                                "-vf", "scale=480:-2", "-q:v", "5", dest],
                               capture_output=True, timeout=30)
        else:
            return False
        return r.returncode == 0 and os.path.isfile(dest)
    except Exception:
        return False


def build_thumbs(records):
    os.makedirs(THUMBS, exist_ok=True)
    made = 0
    for r in records:
        if r["type"] not in ("image", "video"):
            r["thumb"] = None
            continue
        abs_src = os.path.join(ROOT, r["path"])
        if not os.path.isfile(abs_src):
            r["thumb"] = None
            continue
        tn = thumb_name(r["path"])
        dest = os.path.join(THUMBS, tn)
        fresh = os.path.isfile(dest) and os.path.getmtime(dest) >= os.path.getmtime(abs_src)
        if not fresh:
            if make_thumb(abs_src, dest, r["type"]):
                made += 1
            else:
                r["thumb"] = None
                continue
        r["thumb"] = tn
    return made


def load_styles():
    """skills/generate/styles/<slug>/prompt.md (para 1 = description, rest = prompt)
    + reference-*.{png,jpg,jpeg,webp} (first = card image)."""
    cards = []
    if not os.path.isdir(STYLES_DIR):
        return cards
    for slug in sorted(os.listdir(STYLES_DIR)):
        d = os.path.join(STYLES_DIR, slug)
        pm = os.path.join(d, "prompt.md")
        if not os.path.isdir(d) or not os.path.isfile(pm):
            continue
        text = open(pm, encoding="utf-8").read().strip()
        parts = text.split("\n\n", 1)
        desc = parts[0].strip().lstrip("# ").strip()
        prompt = (parts[1] if len(parts) > 1 else text).strip()
        refs = sorted(f for f in os.listdir(d)
                      if f.startswith("reference") and f.rsplit(".", 1)[-1].lower()
                      in ("png", "jpg", "jpeg", "webp"))
        ref_rel = os.path.join("skills", "generate", "styles", slug, refs[0]) if refs else None
        card = {"slug": slug, "name": slug.replace("-", " ").title(), "desc": desc,
                "prompt": prompt, "ref": ref_rel, "thumb": None}
        if ref_rel:
            abs_ref = os.path.join(ROOT, ref_rel)
            tn = thumb_name(ref_rel)
            dest = os.path.join(THUMBS, tn)
            if (os.path.isfile(dest) and os.path.getmtime(dest) >= os.path.getmtime(abs_ref)) \
                    or make_thumb(abs_ref, dest, "image"):
                card["thumb"] = tn
        cards.append(card)
    return cards


TEMPLATE = r"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Asset Command Center</title>
<style>
:root {
  --ground:#12141d; --panel:#191c28; --ink:#e8e9f0; --muted:#8b8fa8; --line:#272b3b;
  --accent:#7c8cf0; --ok:#4dbd7f; --warn:#e3ad45; --crit:#d96a61;
  --mono:"SF Mono",Menlo,Consolas,monospace;
  --display:"Avenir Next",Seravek,"Segoe UI",sans-serif;
}
* { box-sizing:border-box; }
body { background:var(--ground); color:var(--ink);
  font:14px/1.45 -apple-system,"Segoe UI",sans-serif; margin:0; padding:24px; }
header { display:flex; justify-content:space-between; align-items:baseline;
  gap:12px; flex-wrap:wrap; margin-bottom:14px; }
h1 { font-family:var(--display); font-size:20px; font-weight:600; margin:0; }
h1 b { color:var(--accent); }
.stamp { color:var(--muted); font-family:var(--mono); font-size:12px; }
.bar { display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-bottom:10px; }
input[type=search] { background:var(--panel); border:1px solid var(--line); color:var(--ink);
  border-radius:8px; padding:7px 12px; min-width:260px; font-size:13px; }
select { background:var(--panel); border:1px solid var(--line); color:var(--ink);
  border-radius:8px; padding:6px 10px; font-size:12px; }
.chips { display:flex; gap:6px; flex-wrap:wrap; margin:4px 0 10px; }
.facet-label { font-family:var(--mono); font-size:10px; letter-spacing:.08em;
  text-transform:uppercase; color:var(--muted); align-self:center; margin-right:2px; }
.chip { font-family:var(--mono); font-size:11.5px; padding:3px 10px; border-radius:999px;
  border:1px solid var(--line); background:var(--panel); color:var(--muted); cursor:pointer; }
.chip.active { border-color:var(--accent); color:var(--accent); }
.tabs { display:flex; gap:8px; margin-bottom:14px; }
.tab { font-family:var(--display); font-size:13px; padding:6px 16px; border-radius:8px;
  border:1px solid var(--line); background:var(--panel); color:var(--muted); cursor:pointer; }
.tab.active { color:var(--ink); border-color:var(--accent); }
.grid { columns:240px; column-gap:12px; }
.tile { break-inside:avoid; margin:0 0 12px; background:var(--panel);
  border:1px solid var(--line); border-radius:10px; overflow:hidden; cursor:pointer; }
.tile img { width:100%; display:block; background:#0d0f16; }
.tile .glyph { display:flex; align-items:center; justify-content:center; height:110px;
  font-size:34px; color:var(--muted); }
.tile .meta { padding:8px 10px; }
.tile .name { font-size:12px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.tile .sub { display:flex; gap:6px; flex-wrap:wrap; margin-top:4px; }
.pill { font-family:var(--mono); font-size:10px; padding:1px 7px; border-radius:999px;
  background:color-mix(in srgb,var(--muted) 14%,transparent); color:var(--muted); }
.pill.cost { background:color-mix(in srgb,var(--warn) 18%,transparent); color:var(--warn); }
.pill.vid { background:color-mix(in srgb,var(--accent) 18%,transparent); color:var(--accent); }
.more { display:block; margin:18px auto; padding:8px 22px; border-radius:8px;
  border:1px solid var(--line); background:var(--panel); color:var(--muted); cursor:pointer; }
#count { color:var(--muted); font-family:var(--mono); font-size:12px; }
/* lightbox */
#lb { position:fixed; inset:0; background:rgba(8,9,14,.92); display:none;
  z-index:50; overflow:auto; padding:30px; }
#lb.open { display:flex; gap:24px; align-items:flex-start; flex-wrap:wrap; }
#lb .media { flex:2 1 480px; max-width:900px; }
#lb .media img, #lb .media video { max-width:100%; max-height:82vh; border-radius:8px; }
#lb .panel { flex:1 1 300px; background:var(--panel); border:1px solid var(--line);
  border-radius:10px; padding:16px; max-width:440px; }
#lb h3 { margin:0 0 8px; font-size:14px; word-break:break-all; }
#lb table { font-size:12px; width:100%; border-collapse:collapse; }
#lb td { padding:3px 8px 3px 0; vertical-align:top; color:var(--muted); }
#lb td:first-child { font-family:var(--mono); white-space:nowrap; }
#lb .prompt { font-size:12px; color:var(--muted); white-space:pre-wrap;
  max-height:200px; overflow:auto; background:var(--ground); border-radius:6px;
  padding:8px; margin:8px 0; }
button.act { font-family:var(--mono); font-size:11.5px; padding:5px 12px; border-radius:8px;
  border:1px solid var(--accent); background:transparent; color:var(--accent);
  cursor:pointer; margin:4px 6px 0 0; }
#lb .x { position:fixed; top:14px; right:20px; font-size:26px; color:var(--muted);
  cursor:pointer; background:none; border:none; }
/* styles panel */
.stylegrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:12px; }
.stylecard { background:var(--panel); border:1px solid var(--line); border-radius:10px;
  overflow:hidden; }
.stylecard img { width:100%; aspect-ratio:4/3; object-fit:cover; display:block; }
.stylecard .meta { padding:10px 12px; }
.stylecard .name { font-weight:600; font-size:13px; }
.stylecard .desc { color:var(--muted); font-size:12px; margin:4px 0 8px; }
#toast { position:fixed; bottom:22px; left:50%; transform:translateX(-50%);
  background:var(--panel); border:1px solid var(--ok); color:var(--ok);
  font-family:var(--mono); font-size:12px; padding:7px 16px; border-radius:999px;
  opacity:0; transition:opacity .2s; pointer-events:none; z-index:99; }
#toast.show { opacity:1; }
/* copy modal fallback */
#cpm { position:fixed; inset:0; background:rgba(8,9,14,.8); display:none;
  align-items:center; justify-content:center; z-index:60; }
#cpm.open { display:flex; }
#cpm .box { background:var(--panel); border:1px solid var(--line); border-radius:10px;
  padding:18px; max-width:640px; width:90%; }
#cpm textarea { width:100%; height:70px; background:var(--ground); color:var(--ink);
  border:1px solid var(--line); border-radius:6px; font-family:var(--mono); font-size:12px; }
.empty { color:var(--muted); font-style:italic; padding:30px 0; }
</style></head><body>
<header><h1><b>Asset</b> Command Center</h1>
<div class="stamp">__STAMP__ · __TOTAL__ assets · <span id="count"></span></div></header>
<div class="tabs"><button class="tab active" data-tab="gen">Generations</button>
__STYLES_TAB__</div>
<div id="view-gen">
<div class="bar">
  <input type="search" id="q" placeholder="search prompt, name, style, project…">
  <select id="sort"><option value="new">newest</option><option value="old">oldest</option>
  <option value="cost">cost</option><option value="size">size</option></select>
</div>
<div id="facets"></div>
<div class="grid" id="grid"></div>
<button class="more" id="more" style="display:none">Load more</button>
<div id="sentinel"></div>
</div>
<div id="view-styles" style="display:none">
<div class="stylegrid" id="stylegrid"></div>
</div>
<div id="lb"><button class="x" id="lbx">✕</button>
  <div class="media" id="lbm"></div><div class="panel" id="lbp"></div></div>
<div id="cpm"><div class="box"><p style="margin:0 0 8px">Press ⌘C to copy, then Esc:</p>
  <textarea id="cpt" readonly></textarea>
  <button class="act" id="cpx">Close</button>
</div></div>
<div id="toast">copied ✓</div>
<script id="data" type="application/json">__DATA__</script>
<script id="styledata" type="application/json">__STYLEDATA__</script>
<script>
"use strict";
const REPO = __REPO__;
const ALL = JSON.parse(document.getElementById('data').textContent);
const STYLES = JSON.parse(document.getElementById('styledata').textContent);
const FACETS = ["type","zone","project","style","src"];
const sel = {};  FACETS.forEach(f => sel[f] = null);
let shown = 0, filtered = [], CHUNK = 200;

// every manifest-derived string goes through el()/text nodes — never raw HTML
function el(tag, cls, textVal) {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (textVal != null) n.textContent = textVal;
  return n;
}
function facetValues(f) {
  const m = new Map();
  ALL.forEach(r => { const v = r[f]; if (v) m.set(v, (m.get(v)||0)+1); });
  return [...m.entries()].sort((a,b) => b[1]-a[1]);
}
function renderFacets() {
  const host = document.getElementById('facets'); host.textContent = '';
  FACETS.forEach(f => {
    const vals = facetValues(f); if (!vals.length) return;
    const row = el('div', 'chips');
    row.appendChild(el('span', 'facet-label', f));
    const all = el('button', 'chip' + (sel[f] ? '' : ' active'), 'all');
    all.onclick = () => { sel[f] = null; refresh(); };
    row.appendChild(all);
    vals.slice(0, 14).forEach(([v,n]) => {
      const c = el('button', 'chip' + (sel[f] === v ? ' active' : ''), v + ' (' + n + ')');
      c.onclick = () => { sel[f] = (sel[f] === v ? null : v); refresh(); };
      row.appendChild(c);
    });
    host.appendChild(row);
  });
}
function applyFilters() {
  const q = document.getElementById('q').value.toLowerCase().trim();
  filtered = ALL.filter(r => {
    for (const f of FACETS) if (sel[f] && r[f] !== sel[f]) return false;
    if (q) {
      const hay = [(r.prompt||''), r.path, (r.style||''), (r.project||''),
                   (r.tags||[]).join(' ')].join(' ').toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return true;
  });
  const s = document.getElementById('sort').value;
  filtered.sort((a,b) =>
    s === 'old'  ? (a.ts||'').localeCompare(b.ts||'') :
    s === 'cost' ? (b.cost_usd||0) - (a.cost_usd||0) :
    s === 'size' ? (b.size||0) - (a.size||0) :
                   (b.ts||'').localeCompare(a.ts||''));
}
function tile(r) {
  const d = el('div', 'tile');
  if (r.thumb) {
    const img = el('img'); img.loading = 'lazy';
    img.src = 'thumbs/' + encodeURIComponent(r.thumb);
    d.appendChild(img);
  } else {
    d.appendChild(el('div', 'glyph', r.type === 'audio' ? '♫' : r.type === 'video' ? '▶' : '📄'));
  }
  const meta = el('div', 'meta');
  meta.appendChild(el('div', 'name', r.path.split('/').pop()));
  const sub = el('div', 'sub');
  if (r.type === 'video') sub.appendChild(el('span', 'pill vid', '▶ ' + (r.dur_s ? r.dur_s + 's' : 'video')));
  if (r.cost_usd != null) sub.appendChild(el('span', 'pill cost', '$' + (+r.cost_usd).toFixed(2)));
  if (r.style) sub.appendChild(el('span', 'pill', r.style));
  if (r.project) sub.appendChild(el('span', 'pill', r.project));
  meta.appendChild(sub);
  d.appendChild(meta);
  d.onclick = () => openLB(r);
  return d;
}
function renderMore() {
  const grid = document.getElementById('grid');
  const next = filtered.slice(shown, shown + CHUNK);
  next.forEach(r => grid.appendChild(tile(r)));
  shown += next.length;
  document.getElementById('more').style.display = shown < filtered.length ? 'block' : 'none';
  document.getElementById('count').textContent = shown + ' of ' + filtered.length + ' shown';
}
function refresh() {
  applyFilters(); renderFacets();
  document.getElementById('grid').textContent = ''; shown = 0; renderMore();
}
function copyText(t) {
  const ta = document.createElement('textarea');
  ta.value = t; ta.style.position = 'fixed'; ta.style.opacity = '0';
  document.body.appendChild(ta); ta.select();
  let ok = false; try { ok = document.execCommand('copy'); } catch (e) {}
  document.body.removeChild(ta);
  if (ok) { const s = document.getElementById('toast');
    s.classList.add('show'); setTimeout(() => s.classList.remove('show'), 1200); }
  else { const m = document.getElementById('cpm'), x = document.getElementById('cpt');
    x.value = t; m.classList.add('open'); x.select(); }
}
function openLB(r) {
  const lb = document.getElementById('lb');
  const abs = REPO + '/' + r.path;
  const relFromHere = '../../' + r.path;
  const lbm = document.getElementById('lbm'); lbm.textContent = '';
  if (r.type === 'video') {
    const v = document.createElement('video'); v.controls = true; v.src = relFromHere;
    lbm.appendChild(v);
  } else if (r.type === 'image') {
    const i = el('img'); i.src = relFromHere; lbm.appendChild(i);
  } else if (r.type === 'audio') {
    const a = document.createElement('audio'); a.controls = true; a.src = relFromHere;
    a.style.width = '100%'; lbm.appendChild(a);
  } else {
    lbm.appendChild(el('div', 'glyph', '📄'));
  }
  const lbp = document.getElementById('lbp'); lbp.textContent = '';
  lbp.appendChild(el('h3', null, r.path.split('/').pop()));
  const tbl = document.createElement('table');
  [['zone', r.zone], ['project', r.project], ['source', r.src], ['model', r.model],
   ['style', r.style], ['when', r.ts], ['dims', r.w ? r.w + '×' + r.h : null],
   ['duration', r.dur_s ? r.dur_s + 's' : null],
   ['cost', r.cost_usd != null ? '$' + (+r.cost_usd).toFixed(4) : null],
   ['size', r.size ? (r.size/1024/1024).toFixed(2) + ' MB' : null]]
   .filter(x => x[1]).forEach(([k, v]) => {
      const tr = document.createElement('tr');
      tr.appendChild(el('td', null, k)); tr.appendChild(el('td', null, v));
      tbl.appendChild(tr);
   });
  lbp.appendChild(tbl);
  if (r.prompt) {
    const det = document.createElement('details'); det.open = true;
    const sum = document.createElement('summary'); sum.textContent = 'prompt';
    sum.style.cssText = 'cursor:pointer;font-size:12px;color:var(--muted)';
    det.appendChild(sum);
    det.appendChild(el('div', 'prompt', r.prompt));
    const bp = el('button', 'act', 'Copy prompt'); bp.onclick = () => copyText(r.prompt);
    det.appendChild(bp);
    lbp.appendChild(det);
  }
  const row = el('div');
  const bc = el('button', 'act', 'Copy path'); bc.onclick = () => copyText(abs);
  row.appendChild(bc);
  lbp.appendChild(row);
  lb.classList.add('open');
}
function closeLB() { document.getElementById('lb').classList.remove('open'); }
document.getElementById('lbx').addEventListener('click', closeLB);
document.getElementById('cpx').addEventListener('click',
  () => document.getElementById('cpm').classList.remove('open'));
document.addEventListener('keydown', e => { if (e.key === 'Escape') {
  closeLB(); document.getElementById('cpm').classList.remove('open'); } });
document.getElementById('q').addEventListener('input', () => {
  clearTimeout(window.__qt); window.__qt = setTimeout(refresh, 150); });
document.getElementById('sort').addEventListener('change', refresh);
document.getElementById('more').addEventListener('click', renderMore);
new IntersectionObserver(es => { if (es[0].isIntersecting && shown < filtered.length) renderMore(); })
  .observe(document.getElementById('sentinel'));
document.querySelectorAll('.tab').forEach(t => t.addEventListener('click', () => {
  document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
  t.classList.add('active');
  document.getElementById('view-gen').style.display = t.dataset.tab === 'gen' ? '' : 'none';
  document.getElementById('view-styles').style.display = t.dataset.tab === 'styles' ? '' : 'none';
}));
// styles panel — same rule: DOM methods only, no markup interpolation
const sg = document.getElementById('stylegrid');
if (sg) STYLES.forEach(s => {
  const c = el('div', 'stylecard');
  if (s.thumb) { const img = el('img'); img.loading = 'lazy';
    img.src = 'thumbs/' + encodeURIComponent(s.thumb); c.appendChild(img); }
  const m = el('div', 'meta');
  m.appendChild(el('div', 'name', s.name));
  m.appendChild(el('div', 'desc', s.desc));
  const b1 = el('button', 'act', 'Copy prompt'); b1.onclick = () => copyText(s.prompt);
  m.appendChild(b1);
  if (s.ref) { const b2 = el('button', 'act', 'Copy reference path');
    b2.onclick = () => copyText(REPO + '/' + s.ref); m.appendChild(b2); }
  c.appendChild(m);
  sg.appendChild(c);
});
refresh();
</script></body></html>"""


def render_board(records, styles):
    stamp = time.strftime("%Y-%m-%d %H:%M")
    data = [{k: r.get(k) for k in ("path", "type", "zone", "project", "src", "model",
                                   "style", "prompt", "cost_usd", "ts", "w", "h",
                                   "dur_s", "tags", "size", "thumb")} for r in records]
    styles_tab = '<button class="tab" data-tab="styles">Styles</button>' if styles else ""
    html_doc = (TEMPLATE
                .replace("__STAMP__", stamp)
                .replace("__TOTAL__", str(len(records)))
                .replace("__STYLES_TAB__", styles_tab)
                .replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
                .replace("__STYLEDATA__", json.dumps(styles, ensure_ascii=False).replace("</", "<\\/"))
                .replace("__REPO__", json.dumps(ROOT)))
    os.makedirs(OUT_DIR, exist_ok=True)
    open(BOARD, "w", encoding="utf-8").write(html_doc)
    return BOARD


def render_highlights(records, recent_n):
    """Artifact-publishable cut: base64-embedded thumbs of the N most recent."""
    import html as _html
    recs = sorted(records, key=lambda r: r.get("ts") or "", reverse=True)[:recent_n]
    cards = []
    for r in recs:
        if not r.get("thumb"):
            continue
        tp = os.path.join(THUMBS, r["thumb"])
        try:
            b64 = base64.b64encode(open(tp, "rb").read()).decode("ascii")
        except OSError:
            continue
        cap = _html.escape(r.get("style") or r.get("project") or r.get("zone") or "")
        cost = f" · ${float(r['cost_usd']):.2f}" if r.get("cost_usd") is not None else ""
        cards.append(
            f'<figure><img src="data:image/jpeg;base64,{b64}" loading="lazy">'
            f'<figcaption>{_html.escape(os.path.basename(r["path"]))}<br>'
            f'<span>{cap}{cost}</span></figcaption></figure>')
    body = f"""<title>Asset Highlights</title>
<style>
:root {{ --ground:#12141d; --panel:#191c28; --ink:#e8e9f0; --muted:#8b8fa8; --line:#272b3b;
  --accent:#7c8cf0; }}
@media (prefers-color-scheme: light) {{ :root {{ --ground:#f7f7f9; --panel:#fff;
  --ink:#1c1e28; --muted:#6a6d80; --line:#e3e4ec; }} }}
body {{ background:var(--ground); color:var(--ink);
  font:14px/1.4 -apple-system,"Segoe UI",sans-serif; margin:0; padding:28px; }}
h1 {{ font-size:20px; }} h1 b {{ color:var(--accent); }}
.grid {{ columns:240px; column-gap:12px; }}
figure {{ break-inside:avoid; margin:0 0 12px; background:var(--panel);
  border:1px solid var(--line); border-radius:10px; overflow:hidden; }}
img {{ width:100%; display:block; }}
figcaption {{ padding:8px 10px; font-size:11.5px; word-break:break-all; }}
figcaption span {{ color:var(--muted); }}
p.note {{ color:var(--muted); font-size:12px; }}
</style>
<h1><b>Asset</b> Highlights — {len(cards)} most recent</h1>
<p class="note">Generated {time.strftime("%Y-%m-%d %H:%M")} · full board: /assets-board (local)</p>
<div class="grid">{"".join(cards)}</div>"""
    open(HIGHLIGHTS, "w", encoding="utf-8").write(body)
    return HIGHLIGHTS


def main():
    latest = reduced_manifest()
    records = sorted((r for r in latest.values() if r.get("status") == "active"),
                     key=lambda r: r.get("ts") or "", reverse=True)
    made = build_thumbs(records)
    styles = load_styles()
    board = render_board(records, styles)
    size_kb = os.path.getsize(board) // 1024
    print(f"board: {len(records)} assets, {made} new thumbs, {len(styles)} style cards "
          f"→ {os.path.relpath(board, ROOT)} ({size_kb} KB)")
    if "--embed" in sys.argv:
        n = 60
        if "--recent" in sys.argv:
            try:
                n = int(sys.argv[sys.argv.index("--recent") + 1])
            except (IndexError, ValueError):
                pass
        hp = render_highlights(records, n)
        print(f"highlights → {os.path.relpath(hp, ROOT)} ({os.path.getsize(hp)//1024} KB)")


if __name__ == "__main__":
    main()
