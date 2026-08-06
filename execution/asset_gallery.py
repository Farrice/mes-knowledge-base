#!/usr/bin/env python3
"""Asset Command Center board — renders .agent/assets/assets-board.html.

Companion to execution/asset_index.py (which owns the manifest). This script:
  1. generates incremental thumbnails into .agent/assets/thumbs/
     (sips for images, ffmpeg poster-frame for videos, inline glyph otherwise)
  2. renders a self-contained board (file://, no server) in a NETFLIX register
     (Farrice UI take 3, 2026-08-02 — takes 1 chip-pile and 2 sidebar both
     rejected): thin top nav, full-bleed HERO BILLBOARD of the latest work,
     edge-to-edge dark gloss, big shelf rows, hover cards that scale up with
     quick actions and muted live video preview, a Gallery view with compact
     facet dropdowns, and a Style Cards view from skills/generate/styles/.
     Copy-path 📋 + copy-prompt 📝 provenance everywhere (the loved features).

All manifest strings are inserted via DOM textContent (el()) — prompts are
arbitrary text and must never be interpreted as markup.

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
  /* Netflix register, Premium Minimal dark edition (Farrice 2026-08-06):
     same gloss UI + shelf/hover functionality, tokens from the Farrice Cain
     Premium Minimal family (_active/farrice-brand/premium-minimal/REPORT-DIALECT.md):
     ink-black ground w/ the brand's warm-neutral cast, paper-white type,
     stone muted, steel-blue accent where Netflix runs red. */
  --ground:#0e0e0d; --panel:#181817; --ink:#fafaf8; --muted:#8c8c82;
  --accent:#7c9fd9; --warn:#c9a868; --ok:#6fae8c;
  --mono:"SF Mono",Menlo,Consolas,monospace;
  --display:"Helvetica Neue",Seravek,"Segoe UI",sans-serif;
}
* { box-sizing:border-box; }
html, body { background:var(--ground); color:var(--ink); margin:0;
  font:14px/1.45 -apple-system,"Segoe UI",sans-serif; }
/* ── top nav (thin, translucent over hero) ── */
nav { position:fixed; top:0; left:0; right:0; z-index:30; display:flex;
  align-items:center; gap:22px; padding:14px 4%;
  background:linear-gradient(to bottom, rgba(14,14,13,.92), rgba(14,14,13,0));
  transition:background .25s; }
nav.solid { background:rgba(14,14,13,.96); box-shadow:0 1px 0 rgba(255,255,255,.06); }
nav .brand { font-family:var(--display); font-weight:700; font-size:17px;
  letter-spacing:.02em; }
nav .brand b { color:var(--accent); }
nav a.navlink { color:var(--muted); text-decoration:none; font-size:13.5px;
  cursor:pointer; }
nav a.navlink.active { color:var(--ink); font-weight:600; }
nav input[type=search] { margin-left:auto; background:rgba(20,20,20,.85);
  border:1px solid rgba(255,255,255,.14); color:var(--ink); border-radius:8px;
  padding:7px 14px; font-size:13px; width:250px; }
/* ── hero billboard ── */
.hero { position:relative; min-height:72vh; display:flex; align-items:flex-end;
  background-size:cover; background-position:center 30%; }
.hero::after { content:""; position:absolute; inset:0;
  background:linear-gradient(to top, var(--ground) 4%, rgba(14,14,13,.55) 38%, rgba(14,14,13,.12) 70%, rgba(14,14,13,.35) 100%),
             linear-gradient(to right, rgba(14,14,13,.78) 0%, rgba(14,14,13,0) 55%); }
.hero .inner { position:relative; z-index:2; padding:0 4% 56px; max-width:640px; }
.hero.mini { min-height:42vh; }
.hero.mini .inner { padding-bottom:34px; }
.hero.mini h1 { font-size:clamp(22px, 3vw, 34px); }
.hero .kicker { font-family:var(--mono); font-size:11px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--accent); margin-bottom:10px; }
.hero h1 { font-family:var(--display); font-size:clamp(26px, 4vw, 44px);
  font-weight:700; margin:0 0 10px; letter-spacing:-.01em;
  text-shadow:0 2px 18px rgba(0,0,0,.6); }
.hero .meta { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:18px; }
.hero .btns { display:flex; gap:10px; flex-wrap:wrap; }
.btn { display:inline-flex; align-items:center; gap:8px; font-size:14px;
  font-weight:600; padding:10px 22px; border-radius:6px; border:none;
  cursor:pointer; }
.btn.primary { background:var(--ink); color:#101010; }
.btn.primary:hover { background:#e7e7e3; }
.btn.ghost { background:rgba(128,128,128,.32); color:var(--ink); }
.btn.ghost:hover { background:rgba(128,128,128,.5); }
.pill { font-family:var(--mono); font-size:10.5px; padding:2px 9px; border-radius:999px;
  background:rgba(128,128,128,.25); color:var(--muted); }
.pill.cost { color:var(--warn); background:rgba(227,173,69,.16); }
/* ── shelves ── */
.shelves { position:relative; z-index:3; margin-top:-40px; padding:0 0 60px; }
.shelf { margin-bottom:34px; }
.shelf h2 { font-family:var(--display); font-size:17px; font-weight:600;
  margin:0 0 10px; padding:0 4%; }
.shelf h2 span { color:var(--muted); font-family:var(--mono); font-size:11px;
  font-weight:400; margin-left:10px; }
.row { display:flex; gap:8px; overflow-x:auto; padding:14px 4% 22px;
  scroll-snap-type:x proximity; scrollbar-width:none; }
.row::-webkit-scrollbar { display:none; }
.card { flex:0 0 auto; width:264px; aspect-ratio:16/9; scroll-snap-align:start;
  position:relative; border-radius:6px; overflow:hidden; cursor:pointer;
  background:var(--panel); transition:transform .22s ease, box-shadow .22s ease;
  transform-origin:center bottom; }
.card img, .card video { width:100%; height:100%; object-fit:cover; display:block; }
.card .glyph { display:flex; align-items:center; justify-content:center;
  height:100%; font-size:40px; }
.card .brief-glyph { flex-direction:column; gap:8px; padding:14px;
  /* Premium Minimal report dialect (_active/farrice-brand/premium-minimal/REPORT-DIALECT.md) */
  background:linear-gradient(135deg, #F3F3F0, #E9E9E5); border-top:2px solid #3D5A94; }
.card .brief-glyph .bg-icon { font-size:26px; }
.card .brief-glyph .bg-title { font-size:12px; line-height:1.35; text-align:center;
  color:#101010; font-weight:600; letter-spacing:.01em; max-height:3.9em; overflow:hidden; }
.card .tbadge { position:absolute; top:8px; left:8px; font-size:12px;
  background:rgba(14,14,13,.7); border-radius:6px; padding:2px 7px; z-index:2; }
.card .ov { position:absolute; inset:auto 0 0 0; padding:26px 12px 10px;
  background:linear-gradient(to top, rgba(14,14,13,.92), rgba(14,14,13,0));
  opacity:0; transition:opacity .18s; z-index:2; }
.card:hover { transform:scale(1.16); z-index:5;
  box-shadow:0 18px 50px rgba(0,0,0,.65); }
.card:hover .ov { opacity:1; }
.card .ov .nm { font-size:12px; font-weight:600; overflow:hidden;
  text-overflow:ellipsis; white-space:nowrap; margin-bottom:6px; }
.card .ov .acts { display:flex; gap:6px; }
.iconbtn { font-size:12px; padding:4px 9px; border-radius:6px; border:none;
  background:rgba(128,128,128,.35); color:var(--ink); cursor:pointer; }
.iconbtn:hover { background:var(--accent); }
/* ── gallery view ── */
.page { padding:86px 4% 60px; }
.filters { display:flex; gap:10px; flex-wrap:wrap; align-items:center;
  margin-bottom:6px; }
.filters select { background:var(--panel); border:1px solid rgba(255,255,255,.12);
  color:var(--ink); border-radius:8px; padding:7px 10px; font-size:12.5px; }
.afilters { display:flex; gap:6px; flex-wrap:wrap; margin:6px 0 16px; }
.fchip { display:inline-flex; align-items:center; gap:6px; font-family:var(--mono);
  font-size:11px; padding:3px 6px 3px 10px; border-radius:999px;
  border:1px solid var(--accent); color:var(--accent); }
.fchip button { border:none; background:none; color:var(--accent); cursor:pointer; }
.mgrid { columns:250px; column-gap:10px; }
.tile { position:relative; break-inside:avoid; margin:0 0 10px; border-radius:6px;
  overflow:hidden; cursor:pointer; background:var(--panel);
  transition:transform .18s, box-shadow .18s; }
.tile:hover { transform:scale(1.03); box-shadow:0 10px 34px rgba(0,0,0,.55); z-index:4; }
.tile img { width:100%; display:block; }
.tile .glyph { display:flex; align-items:center; justify-content:center;
  height:120px; font-size:36px; }
.tile .ov { position:absolute; inset:auto 0 0 0; padding:24px 10px 8px;
  background:linear-gradient(to top, rgba(14,14,13,.92), rgba(14,14,13,0));
  opacity:0; transition:opacity .15s; }
.tile:hover .ov { opacity:1; }
.tile .ov .nm { font-size:11.5px; overflow:hidden; text-overflow:ellipsis;
  white-space:nowrap; }
.tile .tbadge { position:absolute; top:8px; left:8px; font-size:12px;
  background:rgba(14,14,13,.7); border-radius:6px; padding:2px 7px; }
.more { display:block; margin:22px auto; padding:9px 26px; border-radius:8px;
  border:1px solid rgba(255,255,255,.15); background:var(--panel);
  color:var(--muted); cursor:pointer; }
#count { color:var(--muted); font-family:var(--mono); font-size:12px; }
/* ── style cards ── */
.stylegrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr));
  gap:14px; }
.stylecard { background:var(--panel); border-radius:8px; overflow:hidden;
  transition:transform .18s; }
.stylecard:hover { transform:scale(1.03); }
.stylecard img { width:100%; aspect-ratio:16/10; object-fit:cover; display:block; }
.stylecard .meta { padding:12px 14px; }
.stylecard .name { font-weight:600; font-size:14px; }
.stylecard .desc { color:var(--muted); font-size:12px; margin:5px 0 10px; }
.hint { color:var(--muted); font-size:13px; margin:0 0 18px; max-width:640px; }
/* ── lightbox / copy / toast ── */
#lb { position:fixed; inset:0; background:rgba(0,0,0,.94); display:none;
  z-index:50; overflow:auto; padding:70px 4% 40px; }
#lb.open { display:flex; gap:26px; align-items:flex-start; flex-wrap:wrap; }
#lb .media { flex:2 1 480px; max-width:960px; }
#lb .media img, #lb .media video { max-width:100%; max-height:80vh; border-radius:8px; }
#lb .panel { flex:1 1 300px; background:var(--panel); border-radius:10px;
  padding:18px; max-width:440px; }
#lb h3 { margin:0 0 10px; font-size:14px; word-break:break-all; }
#lb table { font-size:12px; width:100%; border-collapse:collapse; }
#lb td { padding:3px 8px 3px 0; vertical-align:top; color:var(--muted); }
#lb td:first-child { font-family:var(--mono); white-space:nowrap; }
#lb .prompt { font-size:12px; color:var(--muted); white-space:pre-wrap;
  max-height:220px; overflow:auto; background:var(--ground); border-radius:6px;
  padding:9px; margin:8px 0; }
button.act { font-family:var(--mono); font-size:11.5px; padding:6px 13px;
  border-radius:7px; border:1px solid var(--accent); background:transparent;
  color:var(--accent); cursor:pointer; margin:4px 6px 0 0; }
button.act:hover { background:var(--accent); color:#101010; }
#lb .x { position:fixed; top:16px; right:22px; font-size:26px; color:var(--muted);
  cursor:pointer; background:none; border:none; z-index:51; }
#toast { position:fixed; bottom:24px; left:50%; transform:translateX(-50%);
  background:var(--panel); border:1px solid var(--ok); color:var(--ok);
  font-family:var(--mono); font-size:12px; padding:8px 18px; border-radius:999px;
  opacity:0; transition:opacity .2s; pointer-events:none; z-index:99; }
#toast.show { opacity:1; }
#cpm { position:fixed; inset:0; background:rgba(0,0,0,.85); display:none;
  align-items:center; justify-content:center; z-index:60; }
#cpm.open { display:flex; }
#cpm .box { background:var(--panel); border-radius:10px; padding:20px;
  max-width:640px; width:90%; }
#cpm textarea { width:100%; height:72px; background:var(--ground); color:var(--ink);
  border:1px solid rgba(255,255,255,.15); border-radius:6px;
  font-family:var(--mono); font-size:12px; }
</style></head><body>
<nav id="topnav">
  <span class="brand">🎨 <b>ACC</b></span>
  <a class="navlink active" data-v="home">Home</a>
  <a class="navlink" data-v="gen">Gallery</a>
  <a class="navlink" data-v="styles" id="styleslink" style="display:none">Styles</a>
  <a class="navlink" href="../../deliverables/research-briefs/index.html">📋 Briefing Room</a>
  <a class="navlink" href="../pulse/pulse-board.html">📡 Pulse</a>
  <input type="search" id="q" placeholder="🔍 search everything…">
</nav>
<div id="view-home">
  <div class="hero" id="hero">
    <div class="inner">
      <div class="kicker" id="hero-kicker">LATEST</div>
      <h1 id="hero-title"></h1>
      <div class="meta" id="hero-meta"></div>
      <div class="btns" id="hero-btns"></div>
    </div>
  </div>
  <div class="shelves" id="shelves"></div>
</div>
<div id="view-gen" style="display:none">
  <div class="hero mini" id="hero-gen"><div class="inner">
    <div class="kicker">🖼️ GALLERY</div>
    <h1 id="gen-title">ALL ASSETS</h1>
    <div class="meta" id="gen-meta"></div>
  </div></div>
  <div class="page" style="padding-top:20px">
    <div class="filters" id="filters"></div>
    <div class="afilters" id="afilters"></div>
    <div class="mgrid" id="grid"></div>
    <button class="more" id="more" style="display:none">Load more</button>
    <div style="text-align:center;margin-top:8px"><span id="count"></span></div>
    <div id="sentinel"></div>
  </div>
</div>
<div id="view-styles" style="display:none">
  <div class="hero mini" id="hero-styles"><div class="inner">
    <div class="kicker">✨ TASTE LIBRARY</div>
    <h1>STYLE CARDS</h1>
    <div class="meta" id="styles-meta"></div>
  </div></div>
  <div class="page" style="padding-top:20px">
    <p class="hint">Copy a style's full prompt or reference path and feed it to /generate (direct lane). Winners become new cards here.</p>
    <div class="stylegrid" id="stylegrid"></div>
  </div>
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
const TYPE_ICON = { image:'🖼️', video:'🎬', audio:'🎵', doc:'📄' };
const FACETS = [
  { key:'type',    label:'Type' },
  { key:'project', label:'Project' },
  { key:'zone',    label:'Zone' },
  { key:'style',   label:'Style' },
  { key:'engine',  label:'Engine' },
];
const sel = {}; FACETS.forEach(f => sel[f.key] = null);
let shown = 0, filtered = [], CHUNK = 200;

function el(tag, cls, textVal) {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (textVal != null) n.textContent = textVal;
  return n;
}
const relPath = r => '../../' + r.path;
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
// ── lightbox ──
function openLB(r) {
  const lb = document.getElementById('lb');
  const abs = REPO + '/' + r.path;
  const lbm = document.getElementById('lbm'); lbm.textContent = '';
  if (r.type === 'video') { const v = document.createElement('video');
    v.controls = true; v.autoplay = true; v.src = relPath(r); lbm.appendChild(v); }
  else if (r.type === 'image') { const i = el('img'); i.src = relPath(r); lbm.appendChild(i); }
  else if (r.type === 'audio') { const a = document.createElement('audio');
    a.controls = true; a.src = relPath(r); a.style.width = '100%'; lbm.appendChild(a); }
  else lbm.appendChild(el('div', 'glyph', '📄'));
  const lbp = document.getElementById('lbp'); lbp.textContent = '';
  lbp.appendChild(el('h3', null, r.path.split('/').pop()));
  const tbl = document.createElement('table');
  [['zone', r.zone], ['project', r.project], ['engine', r.engine],
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
    const sum = document.createElement('summary'); sum.textContent = '📝 prompt';
    sum.style.cssText = 'cursor:pointer;font-size:12px;color:var(--muted)';
    det.appendChild(sum);
    det.appendChild(el('div', 'prompt', r.prompt));
    const bp = el('button', 'act', '📝 Copy prompt'); bp.onclick = () => copyText(r.prompt);
    det.appendChild(bp);
    lbp.appendChild(det);
  }
  const row = el('div');
  const bc = el('button', 'act', '📋 Copy path'); bc.onclick = () => copyText(abs);
  row.appendChild(bc);
  lbp.appendChild(row);
  lb.classList.add('open');
}
function closeLB() {
  const lb = document.getElementById('lb');
  lb.querySelectorAll('video,audio').forEach(m => m.pause());
  lb.classList.remove('open');
}
// ── hero ──
function buildHero() {
  const byTs = [...ALL].sort((a,b) => (b.ts||'').localeCompare(a.ts||''));
  const pick = byTs.find(r => r.thumb) || byTs[0];
  if (!pick) return;
  const hero = document.getElementById('hero');
  hero.style.backgroundImage = 'url("thumbs/' + encodeURIComponent(pick.thumb) + '")';
  document.getElementById('hero-kicker').textContent =
    (TYPE_ICON[pick.type] || '') + '  LATEST · ' + (pick.engine || pick.zone || '');
  document.getElementById('hero-title').textContent =
    (pick.style || pick.project || pick.path.split('/').pop().split('_')[0])
      .replace(/-/g, ' ').toUpperCase();
  const meta = document.getElementById('hero-meta'); meta.textContent = '';
  [pick.project && '📁 ' + pick.project, pick.style && '🎭 ' + pick.style,
   pick.cost_usd != null && '$' + (+pick.cost_usd).toFixed(2), pick.ts && pick.ts.slice(0,10)]
   .filter(Boolean).forEach(t => meta.appendChild(el('span', 'pill', t)));
  const btns = document.getElementById('hero-btns'); btns.textContent = '';
  const b1 = el('button', 'btn primary', '▶  View'); b1.onclick = () => openLB(pick);
  btns.appendChild(b1);
  const b2 = el('button', 'btn ghost', '📋 Copy path');
  b2.onclick = () => copyText(REPO + '/' + pick.path); btns.appendChild(b2);
  if (pick.prompt) { const b3 = el('button', 'btn ghost', '📝 Copy prompt');
    b3.onclick = () => copyText(pick.prompt); btns.appendChild(b3); }
}
// ── cards / shelves ──
function card(r) {
  const c = el('div', 'card');
  let media;
  const isBrief = r.zone === 'research-briefs';
  if (r.thumb) { media = el('img'); media.loading = 'lazy';
    media.src = 'thumbs/' + encodeURIComponent(r.thumb); c.appendChild(media); }
  else if (isBrief) {
    const g = el('div', 'glyph brief-glyph');
    g.appendChild(el('span', 'bg-icon', '📋'));
    g.appendChild(el('span', 'bg-title', (r.project || r.path.split('/').pop()).replace(/-/g, ' ')));
    c.appendChild(g);
  }
  else c.appendChild(el('div', 'glyph', TYPE_ICON[r.type] || '📄'));
  if (r.type !== 'image') c.appendChild(el('span', 'tbadge', TYPE_ICON[r.type] || ''));
  const ov = el('div', 'ov');
  ov.appendChild(el('div', 'nm', r.path.split('/').pop()));
  const acts = el('div', 'acts');
  const a1 = el('button', 'iconbtn', '📋');
  a1.title = 'Copy path';
  a1.onclick = e => { e.stopPropagation(); copyText(REPO + '/' + r.path); };
  acts.appendChild(a1);
  if (r.prompt) { const a2 = el('button', 'iconbtn', '📝');
    a2.title = 'Copy prompt';
    a2.onclick = e => { e.stopPropagation(); copyText(r.prompt); };
    acts.appendChild(a2); }
  ov.appendChild(acts);
  c.appendChild(ov);
  if (r.type === 'video') {
    let vid = null;
    c.addEventListener('mouseenter', () => {
      if (vid) return;
      vid = document.createElement('video');
      vid.muted = true; vid.loop = true; vid.autoplay = true; vid.src = relPath(r);
      if (media) c.replaceChild(vid, media); else c.prepend(vid);
    });
    c.addEventListener('mouseleave', () => {
      if (vid && media) { c.replaceChild(media, vid); vid = null; }
    });
  }
  c.onclick = () => { if (isBrief) window.open(relPath(r), '_blank'); else openLB(r); };
  return c;
}
function shelf(title, note, items) {
  if (!items.length) return null;
  const s = el('div', 'shelf');
  const h = el('h2', null, title);
  if (note) h.appendChild(el('span', null, note));
  s.appendChild(h);
  const row = el('div', 'row');
  items.forEach(r => row.appendChild(card(r)));
  s.appendChild(row);
  return s;
}
function facetValues(key) {
  const m = new Map();
  ALL.forEach(r => { const v = r[key]; if (v) m.set(v, (m.get(v)||0)+1); });
  return [...m.entries()].sort((a,b) => b[1]-a[1]);
}
function buildShelves() {
  const host = document.getElementById('shelves'); host.textContent = '';
  const byTs = [...ALL].sort((a,b) => (b.ts||'').localeCompare(a.ts||''));
  const add = s => { if (s) host.appendChild(s); };
  add(shelf('🕒 Recently added', byTs.length + ' total', byTs.slice(1, 21)));
  add(shelf('🎬 Video', null, byTs.filter(r => r.type === 'video').slice(0, 20)));
  add(shelf('🎵 Audio', null, byTs.filter(r => r.type === 'audio').slice(0, 20)));
  add(shelf('📋 Research Briefs', null, byTs.filter(r => r.zone === 'research-briefs').slice(0, 20)));
  facetValues('project').slice(0, 8).forEach(([p, n]) =>
    add(shelf('📁 ' + p, n + ' assets', byTs.filter(r => r.project === p).slice(0, 20))));
  facetValues('style').slice(0, 5).forEach(([st, n]) =>
    add(shelf('🎭 ' + st, n + ' assets', byTs.filter(r => r.style === st).slice(0, 20))));
}
// ── gallery view ──
function renderFilters() {
  const host = document.getElementById('filters'); host.textContent = '';
  FACETS.forEach(f => {
    const vals = facetValues(f.key); if (!vals.length) return;
    const s = document.createElement('select');
    const o0 = document.createElement('option');
    o0.value = ''; o0.textContent = f.label + ': all';
    s.appendChild(o0);
    vals.forEach(([v, n]) => { const o = document.createElement('option');
      o.value = v; o.textContent = v + ' (' + n + ')';
      if (sel[f.key] === v) o.selected = true;
      s.appendChild(o); });
    s.onchange = () => { sel[f.key] = s.value || null; refresh(); };
    host.appendChild(s);
  });
  const af = document.getElementById('afilters'); af.textContent = '';
  FACETS.forEach(f => {
    if (!sel[f.key]) return;
    const c = el('span', 'fchip', sel[f.key] + ' ');
    const x = el('button', null, '✕');
    x.onclick = () => { sel[f.key] = null; refresh(); };
    c.appendChild(x); af.appendChild(c);
  });
}
function tile(r) {
  const d = el('div', 'tile');
  if (r.thumb) { const img = el('img'); img.loading = 'lazy';
    img.src = 'thumbs/' + encodeURIComponent(r.thumb); d.appendChild(img); }
  else d.appendChild(el('div', 'glyph', TYPE_ICON[r.type] || '📄'));
  if (r.type !== 'image') d.appendChild(el('span', 'tbadge', TYPE_ICON[r.type] || ''));
  const ov = el('div', 'ov');
  ov.appendChild(el('div', 'nm', r.path.split('/').pop()));
  d.appendChild(ov);
  d.onclick = () => openLB(r);
  return d;
}
function applyFilters() {
  const q = document.getElementById('q').value.toLowerCase().trim();
  filtered = ALL.filter(r => {
    for (const f of FACETS) if (sel[f.key] && r[f.key] !== sel[f.key]) return false;
    if (q) {
      const hay = [(r.prompt||''), r.path, (r.style||''), (r.project||''),
                   (r.engine||''), (r.tags||[]).join(' ')].join(' ').toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return true;
  });
  filtered.sort((a,b) => (b.ts||'').localeCompare(a.ts||''));
}
function renderMore() {
  const grid = document.getElementById('grid');
  const next = filtered.slice(shown, shown + CHUNK);
  next.forEach(r => grid.appendChild(tile(r)));
  shown += next.length;
  document.getElementById('more').style.display = shown < filtered.length ? 'block' : 'none';
  document.getElementById('count').textContent = shown + ' / ' + filtered.length;
}
function refresh() {
  applyFilters(); renderFilters();
  document.getElementById('grid').textContent = ''; shown = 0; renderMore();
  // gallery hero mirrors the active filter set
  const hg = document.getElementById('hero-gen');
  const lead = filtered.find(r => r.thumb);
  if (hg && lead) hg.style.backgroundImage =
    'url("thumbs/' + encodeURIComponent(lead.thumb) + '")';
  const active = FACETS.map(f => sel[f.key]).filter(Boolean);
  document.getElementById('gen-title').textContent =
    (active.length ? active.join(' · ') : 'All Assets').replace(/-/g, ' ').toUpperCase();
  const gm = document.getElementById('gen-meta'); gm.textContent = '';
  gm.appendChild(el('span', 'pill', filtered.length + ' assets'));
  const vids = filtered.filter(r => r.type === 'video').length;
  if (vids) gm.appendChild(el('span', 'pill', '🎬 ' + vids));
  const cost = filtered.reduce((s, r) => s + (+r.cost_usd || 0), 0);
  if (cost) gm.appendChild(el('span', 'pill cost', '$' + cost.toFixed(2) + ' invested'));
}
// ── nav / views ──
function setView(v) {
  ['home', 'gen', 'styles'].forEach(k => {
    const n = document.getElementById('view-' + k);
    if (n) n.style.display = v === k ? '' : 'none';
  });
  document.querySelectorAll('.navlink').forEach(a =>
    a.classList.toggle('active', a.dataset.v === v));
  document.getElementById('topnav').classList.toggle('solid', window.scrollY > 40);
  window.scrollTo(0, 0);
}
document.querySelectorAll('.navlink[data-v]').forEach(a =>
  a.addEventListener('click', () => setView(a.dataset.v)));
document.getElementById('q').addEventListener('input', () => {
  clearTimeout(window.__qt);
  window.__qt = setTimeout(() => { setView('gen'); refresh(); }, 200); });
document.getElementById('lbx').addEventListener('click', closeLB);
document.getElementById('cpx').addEventListener('click',
  () => document.getElementById('cpm').classList.remove('open'));
document.addEventListener('keydown', e => { if (e.key === 'Escape') {
  closeLB(); document.getElementById('cpm').classList.remove('open'); } });
document.getElementById('more').addEventListener('click', renderMore);
new IntersectionObserver(es => { if (es[0].isIntersecting && shown < filtered.length) renderMore(); })
  .observe(document.getElementById('sentinel'));
window.addEventListener('scroll', () => {
  document.getElementById('topnav').classList.toggle('solid', window.scrollY > 40);
});
// ── style cards ──
if (STYLES.length) {
  document.getElementById('styleslink').style.display = '';
  const hs = document.getElementById('hero-styles');
  const sthumb = (STYLES.find(s => s.thumb) || {}).thumb ||
    (([...ALL].sort((a,b) => (b.ts||'').localeCompare(a.ts||'')).find(r => r.thumb)) || {}).thumb;
  if (hs && sthumb) hs.style.backgroundImage =
    'url("thumbs/' + encodeURIComponent(sthumb) + '")';
  const sm = document.getElementById('styles-meta');
  sm.appendChild(el('span', 'pill', STYLES.length + ' styles banked'));
}
const sg = document.getElementById('stylegrid');
if (sg) STYLES.forEach(s => {
  const c = el('div', 'stylecard');
  if (s.thumb) { const img = el('img'); img.loading = 'lazy';
    img.src = 'thumbs/' + encodeURIComponent(s.thumb); c.appendChild(img); }
  const m = el('div', 'meta');
  m.appendChild(el('div', 'name', s.name));
  m.appendChild(el('div', 'desc', s.desc));
  const b1 = el('button', 'act', '📝 Copy prompt'); b1.onclick = () => copyText(s.prompt);
  m.appendChild(b1);
  if (s.ref) { const b2 = el('button', 'act', '📋 Copy reference path');
    b2.onclick = () => copyText(REPO + '/' + s.ref); m.appendChild(b2); }
  c.appendChild(m);
  sg.appendChild(c);
});
buildHero(); buildShelves(); refresh();
</script></body></html>"""


def render_board(records, styles):
    data = []
    for r in records:
        row = {k: r.get(k) for k in ("path", "type", "zone", "project", "style",
                                     "prompt", "cost_usd", "ts", "w", "h",
                                     "dur_s", "tags", "size", "thumb")}
        row["engine"] = r.get("model") or r.get("src")
        data.append(row)
    html_doc = (TEMPLATE
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
:root {{ --ground:#0e0e0d; --panel:#181817; --ink:#fafaf8; --muted:#8c8c82; --line:#2c2c2a;
  --accent:#7c9fd9; }}
@media (prefers-color-scheme: light) {{ :root {{ --ground:#f3f3f0; --panel:#fafaf8;
  --ink:#101010; --muted:#8c8c82; --line:#d8d8d3; --accent:#3d5a94; }} }}
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
