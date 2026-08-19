#!/usr/bin/env python3
"""
brief_library.py — the Briefing Room (Layer 3, deterministic, $0).

Scans deliverables/research-briefs/*/ and generates deliverables/research-briefs/index.html:
every brief in the Farrice Cain Premium Minimal report dialect
(_active/farrice-brand/premium-minimal/REPORT-DIALECT.md), with a sidebar
(category + priority filters, newest/priority sort) and 10-per-page pagination
so the room never becomes an infinite scroll.

Brief JSONs may carry optional top-level `category` (string, e.g. "research",
"angles", "build report") and `priority` (1-3; also accepts "P1"/"high" forms).
Missing values fall back gracefully: category ← first chip segment, priority ← unset.

Each card: open brief (click), `path` (copy .md abs path — file-access tools),
`copy brief` (entire brief inline — chat LLMs), `md`/`ctx` (open the artifacts).

Usage:
    python3 execution/brief_library.py [--open]
"""
import argparse
import html
import json
import re
import subprocess
import sys
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRIEFS = ROOT / "deliverables" / "research-briefs"
PAGE_SIZE = 10

sys.path.insert(0, str(Path(__file__).resolve().parent))
from degrade import degraded  # noqa: E402


def _canonical_repo_root():
    """Return the main checkout that owns the shared Git directory.

    Git worktrees store a tiny ``.git`` pointer into the main checkout. This
    lets portable context paths prefer the active lane while still finding
    main-only, untracked media assets that Git cannot replicate into a lane.
    """
    dotgit = ROOT / ".git"
    if dotgit.is_dir():
        return ROOT
    if dotgit.is_file():
        try:
            marker = dotgit.read_text(encoding="utf-8").strip()
            if marker.startswith("gitdir:"):
                gitdir = Path(marker.split(":", 1)[1].strip()).resolve()
                for parent in gitdir.parents:
                    if parent.name == ".git":
                        return parent.parent
        except OSError as e:
            degraded(None, "worktree .git pointer unreadable — canonical root falls back to this lane (main-only media may 404)", e)
    return ROOT


CANONICAL_ROOT = _canonical_repo_root()

# ── Lifecycle policy (the librarian; Farrice 2026-08-06, tuned same day) ─────
# Periodical categories auto-archive after N days — applied on every regen, so
# currency needs no cron and no memory. Everything else archives manually only
# (archive <slug>). ARCHIVED IS NEVER GONE: files, md mirrors, and context
# packs stay exactly where they are — still openable, referenceable, and
# agent-feedable; the shelf filter is presentation only. Nothing is deleted.
AUTO_ARCHIVE_DAYS = {"zeitgeist": 30, "angles": 30, "mission": 14}
STALE_DAYS = 30  # active non-periodical briefs older than this get flagged, never moved


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def accent_em(s):
    out = esc(str(s or ""))
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", out, count=1)


def norm_pri(v):
    """1-3 (1 = highest). 0 = unset (sorts last in priority order, no chip)."""
    if v is None:
        return 0
    s = str(v).strip().upper()
    if s.startswith("P"):
        s = s[1:]
    if s in {"HIGH", "H"}:
        return 1
    if s in {"MEDIUM", "MED", "M"}:
        return 2
    if s in {"LOW", "L"}:
        return 3
    try:
        n = int(float(s))
        return n if n in (1, 2, 3) else 0
    except ValueError as e:
        return degraded(0, f"unparseable brief priority {str(v)[:30]!r} — sorted last, no chip", e)


def derive_category(meta):
    cat = str(meta.get("category") or "").strip().lower()
    if cat:
        return cat
    chip = str(meta.get("chip") or "").split("·")[0].strip().lower()
    return chip or "uncategorized"


def sort_ts(meta, mtime):
    """True recency: the brief's `compiled` date when parseable, else file mtime.
    Bulk re-renders reset every mtime at once — compiled keeps the real order."""
    import datetime
    # "aug 6, 2026 · ~00:45" → "aug 6, 2026"; tolerate trailing annotations
    s = str(meta.get("compiled") or "").split("·")[0].strip().lower().replace(".", "")
    for fmt in ("%b %d, %Y", "%B %d, %Y", "%Y-%m-%d"):
        try:
            d = datetime.datetime.strptime(s, fmt)
            # same-day briefs tie-break on mtime (fractional, keeps intra-day order)
            return d.timestamp() + (mtime % 86400) / 86400.0
        except ValueError:
            continue
    return mtime


def _url_path(path, base):
    """Return a quoted URL path relative to a known Briefing Room root.

    Cards deliberately carry relative paths instead of checkout-specific
    ``file://`` URIs. The same generated index can therefore open beside its
    briefs in static mode and map to the active server's ROOT in live mode.
    """
    return urllib.parse.quote(path.relative_to(base).as_posix(), safe="/")


def room_href(path):
    """Static URL from deliverables/research-briefs/index.html to *path*."""
    return _url_path(path, BRIEFS)


def repo_path(path):
    """Server URL payload from the active repository root to *path*."""
    return _url_path(path, ROOT)


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>the briefing room · Antigravity Research</title>
<style>
  /* ── Farrice Cain Premium Minimal — report dialect (_active/farrice-brand/premium-minimal/) ── */
  :root{
    --ag-ink: oklch(18% 0 0);             /* #101010 */
    --ag-paper: oklch(96% 0.003 107);     /* #F3F3F0 canvas */
    --ag-surface: oklch(98% 0.002 107);   /* #FAFAF8 paper */
    --ag-line: oklch(88% 0.005 107);      /* #D8D8D3 */
    --ag-accent: oklch(46% 0.084 262);    /* steel blue */
    --ag-proof: oklch(48% 0.07 165);
    --ag-risk: oklch(52% 0.10 25);      /* muted risk red — broken grounding */
    --ag-ink-soft: oklch(44% 0.003 110);  /* graphite */
    --ag-ink-mute: oklch(62% 0.012 110);  /* stone */
    --sans:'Helvetica Neue','Neue Haas Grotesk Text Pro',Helvetica,Inter,system-ui,Arial,sans-serif;
    --serif:'Source Serif 4',Georgia,'Times New Roman',serif;
    --mono:'JetBrains Mono',ui-monospace,'SF Mono',Menlo,monospace;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  body{ background:var(--ag-paper); color:var(--ag-ink); font-family:var(--sans) }
  .wrap{ max-width:980px; margin:0 auto; padding:52px 28px 90px }
  .kicker{ font-family:var(--mono); font-size:10px; letter-spacing:.22em; text-transform:uppercase; color:var(--ag-ink-mute); display:block }
  .topline{ display:flex; align-items:center; gap:14px; flex-wrap:wrap }
  .tagc.risk{ border-color:var(--ag-risk); color:var(--ag-risk) }
  .brief-card .links span.warned{ border-color:var(--ag-risk); color:var(--ag-risk) }
  .homenav{ margin-left:auto; display:flex; gap:6px }
  .homenav a{ font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; text-decoration:none;
    color:var(--ag-ink-soft); border:1px solid var(--ag-line); border-radius:99px; padding:4px 11px }
  .homenav a:hover{ border-color:var(--ag-accent); color:var(--ag-accent) }
  h1{ font-size:48px; line-height:1.05; letter-spacing:-.022em; font-weight:700; margin-top:16px }
  h1 em{ font-family:var(--serif); font-style:italic; font-weight:400; color:var(--ag-accent) }
  .dek{ font-size:14px; line-height:1.55; color:var(--ag-ink-soft); margin-top:14px; max-width:56ch }
  .count{ font-family:var(--mono); font-size:9px; letter-spacing:.16em; text-transform:uppercase; color:var(--ag-ink-mute);
    border-top:1px solid var(--ag-ink); margin-top:28px; padding-top:10px }

  .layout{ display:grid; grid-template-columns:190px 1fr; gap:28px; margin-top:22px; align-items:start }
  /* ── sidebar ── */
  .side{ position:sticky; top:20px }
  .side .grp{ margin-bottom:22px }
  .side .lab{ font-family:var(--mono); font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--ag-ink-mute);
    border-bottom:1px solid var(--ag-line); padding-bottom:6px; margin-bottom:8px; display:block }
  .side button{ display:flex; justify-content:space-between; gap:8px; width:100%; text-align:left; background:none;
    cursor:pointer; font-family:var(--sans); font-size:12.5px; color:var(--ag-ink-soft); padding:5px 8px; border-radius:5px; border:1px solid transparent }
  .side button:hover{ color:var(--ag-accent) }
  .side button.on{ background:var(--ag-surface); border-color:var(--ag-line); color:var(--ag-ink); font-weight:600 }
  .side button .c{ font-family:var(--mono); font-size:9px; color:var(--ag-ink-mute) }

  /* ── cards ── */
  .brief-card{ display:block; border:1px solid var(--ag-line); border-radius:8px; background:var(--ag-surface);
    padding:20px 22px; margin-bottom:16px; text-decoration:none; color:var(--ag-ink); transition:border-color .15s }
  .brief-card:hover{ border-color:var(--ag-accent) }
  .brief-card .toprow{ display:flex; gap:8px; align-items:center; flex-wrap:wrap }
  .brief-card .chip{ display:inline-block; font-family:var(--mono); font-size:8.5px; letter-spacing:.18em; text-transform:uppercase;
    color:var(--ag-accent); border:1px solid var(--ag-accent); border-radius:99px; padding:3px 10px }
  .tagp{ font-family:var(--mono); font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; border-radius:4px; padding:3px 8px; font-weight:700 }
  .tagp.p1{ color:var(--ag-paper); background:var(--ag-accent) }
  .tagp.p2{ color:var(--ag-accent); border:1px solid var(--ag-accent) }
  .tagp.p3{ color:var(--ag-ink-mute); border:1px solid var(--ag-line) }
  .tagc{ font-family:var(--mono); font-size:8.5px; letter-spacing:.14em; text-transform:uppercase;
    color:var(--ag-ink-soft); border:1px solid var(--ag-line); border-radius:4px; padding:3px 8px }
  .tagc.arch{ color:var(--ag-ink-mute); border-style:dashed }
  .tagc.sup{ color:var(--ag-accent); border-color:var(--ag-accent); text-decoration:none }
  .hkeep{ font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--ag-ink-mute); margin-top:6px }
  .hkeep b{ color:var(--ag-risk); font-weight:700 }
  .brief-card h2{ font-size:22px; letter-spacing:-.015em; font-weight:700; margin-top:12px; line-height:1.2 }
  .brief-card h2 em{ font-family:var(--serif); font-style:italic; font-weight:400; color:var(--ag-accent) }
  .brief-card p{ font-size:12.5px; line-height:1.55; color:var(--ag-ink-soft); margin-top:8px; max-width:60ch }
  .brief-card .meta{ display:flex; gap:14px; flex-wrap:wrap; margin-top:14px; align-items:center }
  .brief-card .m{ font-family:var(--mono); font-size:8.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--ag-ink-mute) }
  .brief-card .links{ margin-left:auto; display:flex; gap:8px }
  .brief-card .links span{ font-family:var(--mono); font-size:8.5px; letter-spacing:.12em; text-transform:uppercase;
    color:var(--ag-ink-soft); border:1px solid var(--ag-line); border-radius:4px; padding:3px 8px }
  .brief-card .links span:hover{ border-color:var(--ag-accent); color:var(--ag-accent) }
  .brief-card .links span.cp{ color:var(--ag-accent); border-color:var(--ag-accent) }
  .brief-card .links span.done{ color:var(--ag-proof); border-color:currentColor }

  /* ── pager ── */
  .pager{ display:flex; gap:6px; justify-content:center; margin-top:26px; flex-wrap:wrap }
  .pager button{ font-family:var(--mono); font-size:10px; letter-spacing:.1em; text-transform:uppercase; cursor:pointer;
    background:var(--ag-surface); border:1px solid var(--ag-line); border-radius:5px; padding:6px 12px; color:var(--ag-ink-soft) }
  .pager button:hover{ border-color:var(--ag-accent); color:var(--ag-accent) }
  .pager button.on{ background:var(--ag-ink); color:var(--ag-paper); border-color:var(--ag-ink) }
  .pager button:disabled{ opacity:.35; cursor:default }
  .showing{ font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--ag-ink-mute);
    text-align:center; margin-top:10px }

  #toast{ position:fixed; bottom:24px; left:50%; transform:translateX(-50%); background:var(--ag-ink); color:var(--ag-paper);
    font-family:var(--mono); font-size:10px; letter-spacing:.14em; text-transform:uppercase; padding:9px 20px;
    border-radius:99px; opacity:0; transition:opacity .2s; pointer-events:none; z-index:99 }
  #toast.show{ opacity:1 }
  footer{ margin-top:80px; border-top:1px solid var(--ag-ink); padding-top:12px; display:flex; justify-content:space-between;
    font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--ag-ink-mute) }
  @media (max-width:760px){
    h1{ font-size:34px }
    .layout{ grid-template-columns:1fr }
    .side{ position:static }
    .side .grp{ margin-bottom:12px }
    .side button{ display:inline-flex; width:auto }
    .brief-card .links{ margin-left:0 }
  }
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="topline"><span class="kicker">ANTIGRAVITY RESEARCH · LIBRARY</span>
      {{HOMENAV}}</div>
    <h1>the briefing <em>room</em></h1>
    <p class="dek">every rendered brief. click a card to open it; path feeds file-access tools, copy brief feeds any chat AI; md and ctx open the artifacts.</p>
    <div class="count">{{COUNT}} briefs on file · regenerated {{STAMP}}</div>
    <div class="hkeep">{{HKEEP}}</div>
  </header>
  <div class="layout">
    <aside class="side">
      <div class="grp"><span class="lab">Shelf</span>
        <button data-shelf="active" class="on">active <span class="c">{{N_ACTIVE}}</span></button>
        <button data-shelf="archived">archived <span class="c">{{N_ARCH}}</span></button>
      </div>
      <div class="grp"><span class="lab">Sort</span>
        <button data-sort="newest" class="on">newest first</button>
        <button data-sort="priority">priority first</button>
      </div>
      <div class="grp"><span class="lab">Priority</span>{{PRI_BTNS}}</div>
      <div class="grp"><span class="lab">Category</span>{{CAT_BTNS}}</div>
    </aside>
    <main>
      <div id="cards">{{CARDS}}</div>
      <div class="pager" id="pager"></div>
      <div class="showing" id="showing"></div>
    </main>
  </div>
  <footer><span>ANTIGRAVITY RESEARCH</span><span>@farricecain</span></footer>
</div>
<div id="toast">copied</div>
<script id="packs" type="application/json">{{PACKS}}</script>
<script>
  /* All dynamic DOM below is built with createElement/textContent only — no
     innerHTML — so scraped brief text can never execute as markup. */
  var PACKS = JSON.parse(document.getElementById('packs').textContent);
  var PAGE_SIZE = {{PAGE_SIZE}};
  var cardsEl = document.getElementById('cards');
  var allCards = Array.prototype.slice.call(cardsEl.querySelectorAll('.brief-card'));
  var state = { sort:'newest', pri:'all', cat:'all', shelf:'active', page:1 };
  /* HTTP alone does not mean this is the Pulse server. Generic preview
     servers cannot answer /repo/ routes, so live behavior stays off until a
     same-checkout /ping handshake succeeds. */
  var ROOM_LIVE = false;
  var ROOM_HANDSHAKE = Promise.resolve(false);

  function toast(msg){
    var t = document.getElementById('toast'); t.textContent = msg; t.classList.add('show');
    setTimeout(function(){ t.classList.remove('show'); }, 1600);
  }
  function copyText(txt, ok){
    function fallback(){
      var ta=document.createElement('textarea'); ta.value=txt; ta.style.position='fixed'; ta.style.opacity='0';
      document.body.appendChild(ta); ta.select(); try{ document.execCommand('copy'); }catch(e){} document.body.removeChild(ta);
    }
    if (navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(txt).then(function(){ toast(ok); }, function(){ fallback(); toast(ok); });
    } else { fallback(); toast(ok); }
  }

  function filtered(){
    var list = allCards.filter(function(c){
      var archived = c.dataset.status !== 'active';
      if (state.shelf === 'active' && archived) return false;
      if (state.shelf === 'archived' && !archived) return false;
      if (state.pri !== 'all' && c.dataset.pri !== state.pri) return false;
      if (state.cat !== 'all' && c.dataset.cat !== state.cat) return false;
      return true;
    });
    list.sort(function(a, b){
      if (state.sort === 'priority'){
        var pa = parseInt(a.dataset.pri, 10) || 9, pb = parseInt(b.dataset.pri, 10) || 9;
        if (pa !== pb) return pa - pb;
      }
      return parseFloat(b.dataset.mtime) - parseFloat(a.dataset.mtime);
    });
    return list;
  }

  function apply(){
    var list = filtered();
    var pages = Math.max(1, Math.ceil(list.length / PAGE_SIZE));
    if (state.page > pages) state.page = pages;
    var start = (state.page - 1) * PAGE_SIZE;
    var slice = list.slice(start, start + PAGE_SIZE);
    allCards.forEach(function(c){ c.style.display = 'none'; });
    slice.forEach(function(c){ cardsEl.appendChild(c); c.style.display = 'block'; });
    var pager = document.getElementById('pager');
    while (pager.firstChild) pager.removeChild(pager.firstChild);
    function pbtn(label, page, on, dis){
      var b = document.createElement('button'); b.textContent = label;
      if (on) b.className = 'on';
      b.disabled = !!dis;
      b.addEventListener('click', function(){ state.page = page; apply(); window.scrollTo({top:0, behavior:'smooth'}); });
      pager.appendChild(b);
    }
    if (pages > 1){
      pbtn('‹ prev', Math.max(1, state.page - 1), false, state.page === 1);
      for (var i = 1; i <= pages; i++) pbtn(String(i), i, i === state.page, false);
      pbtn('next ›', Math.min(pages, state.page + 1), false, state.page === pages);
    }
    var sh = document.getElementById('showing');
    sh.textContent = list.length
      ? 'showing ' + (start + 1) + '–' + (start + slice.length) + ' of ' + list.length
      : 'nothing matches this filter';
  }

  document.querySelectorAll('.side button').forEach(function(b){
    b.addEventListener('click', function(){
      if (b.dataset.sort){ state.sort = b.dataset.sort; mark('[data-sort]', b); }
      if (b.dataset.pri !== undefined){ state.pri = b.dataset.pri; mark('[data-pri]', b); }
      if (b.dataset.cat !== undefined){ state.cat = b.dataset.cat; mark('[data-cat]', b); }
      if (b.dataset.shelf){ state.shelf = b.dataset.shelf; mark('[data-shelf]', b); }
      state.page = 1; apply();
    });
  });
  function mark(sel, on){
    document.querySelectorAll('.side button' + sel).forEach(function(x){ x.classList.remove('on'); });
    on.classList.add('on');
  }

  /* Cards carry checkout-independent relative links for static use plus an
     explicit repo-relative path for the live server. This keeps a generated
     Room portable between main and isolated worktrees without teaching the
     browser an absolute path that becomes stale after integration. */
  function liveRepo(repoPath){
    if (!ROOM_LIVE || !repoPath) return null;
    return '/repo/' + repoPath.replace(/^\/+/, '');
  }
  function go(staticHref, repoPath){ window.location = liveRepo(repoPath) || staticHref; }

  /* Absolute file links still exist in the sibling-board nav. Keep the legacy
     mapper only for that surface; brief cards no longer depend on it. */
  var REPO_ROOT = {{REPO_ROOT_JSON}};
  var PREFIX = REPO_ROOT ? ('file://' + encodeURI(REPO_ROOT).replace(/#/g, '%23') + '/') : '';
  if (location.protocol.startsWith('http')){
    ROOM_HANDSHAKE = fetch('/ping', {cache:'no-store'})
      .then(function(r){ return r.ok ? r.json() : null; })
      .then(function(j){
        ROOM_LIVE = !!(j && j.pulse && j.root === REPO_ROOT);
        document.documentElement.dataset.roomLive = ROOM_LIVE ? 'true' : 'false';
        return ROOM_LIVE;
      })
      .catch(function(){ ROOM_LIVE = false; return false; });
  }
  function toRepo(uri){
    if (!ROOM_LIVE || !PREFIX || !uri || uri.indexOf(PREFIX) !== 0) return null;
    return '/repo/' + uri.slice(PREFIX.length);
  }
  document.querySelectorAll('.brief-card').forEach(function(card){
    card.addEventListener('click', function(ev){
      ev.preventDefault();
      ROOM_HANDSHAKE.then(function(){
        window.location = liveRepo(card.dataset.repoPath) || card.getAttribute('href');
      });
    });
  });
  document.querySelectorAll('.brief-card .links span[data-static-href]').forEach(function(el){
    el.addEventListener('click', function(ev){
      ev.preventDefault(); ev.stopPropagation();
      ROOM_HANDSHAKE.then(function(){ go(el.dataset.staticHref, el.dataset.repoPath); });
    });
  });
  document.querySelectorAll('.brief-card a.tagc.sup').forEach(function(el){
    el.addEventListener('click', function(ev){
      ev.preventDefault(); ev.stopPropagation();
      ROOM_HANDSHAKE.then(function(){
        window.location = liveRepo(el.dataset.repoPath) || el.getAttribute('href');
      });
    });
  });
  /* Sibling boards get their live ROUTE, not their file. /repo/ would serve a
     stale snapshot; the route regenerates on every hit. */
  var BOARD_ROUTES = [['/.agent/pulse/pulse-board.html','/'],
                      ['/.agent/missions/mission-control.html','/missions'],
                      ['/.agent/oracle/oracle-dashboard.html','/oracle'],
                      ['/deliverables/research-briefs/index.html','/room']];
  document.querySelectorAll('.homenav a[href^="file:"]').forEach(function(el){
    el.addEventListener('click', function(ev){
      ev.preventDefault();
      ROOM_HANDSHAKE.then(function(){
        var href = decodeURI(el.getAttribute('href') || '');
        if (!ROOM_LIVE){ window.location = el.getAttribute('href'); return; }
        for (var i = 0; i < BOARD_ROUTES.length; i++){
          if (href.indexOf(BOARD_ROUTES[i][0]) !== -1){
            window.location = BOARD_ROUTES[i][1]; return;
          }
        }
        var mapped = toRepo(el.getAttribute('href'));
        window.location = mapped || el.getAttribute('href');
      });
    });
  });
  document.querySelectorAll('.brief-card .links span[data-act]').forEach(function(el){
    el.addEventListener('click', function(ev){
      ev.preventDefault(); ev.stopPropagation();
      var p = PACKS[el.dataset.slug]; if(!p) return;
      if (el.dataset.act === 'path'){ copyText(p.path, 'path copied'); }
      else { copyText(p.brief, 'full brief copied — paste into any ai'); }
      el.classList.add('done'); setTimeout(function(){ el.classList.remove('done'); }, 1600);
    });
  });

  // librarian actions — live when served by pulse_serve, copy-command otherwise
  document.querySelectorAll('.brief-card .links span[data-life]').forEach(function(el){
    el.addEventListener('click', function(ev){
      ev.preventDefault(); ev.stopPropagation();
      var life = el.dataset.life, slug = el.dataset.slug;
      var cli = 'python3 execution/brief_library.py ' + life + ' ' + slug;
      ROOM_HANDSHAKE.then(function(){
        if (!ROOM_LIVE){ copyText(cli, 'server offline — command copied'); return; }
        fetch('/action', { method: 'POST', headers: { 'Content-Type': 'application/json' },
                          body: JSON.stringify({ action: 'brief-' + life, args: { slug: slug } }) })
          .then(function(r){ return r.json(); })
          .then(function(j){
            if (j.ok){ var t = document.getElementById('toast');
              t.textContent = life + 'd — refreshing'; t.classList.add('show');
              setTimeout(function(){ location.reload(); }, 700); }
          })
          .catch(function(){ copyText(cli, 'server unreachable — command copied'); });
      });
    });
  });

  // side-window live reload — when served, poll for regenerations and refresh
  ROOM_HANDSHAKE.then(function(live){
    if (!live) return;
    var baseline = null;
    setInterval(function(){
      fetch('/ping').then(function(r){ return r.json(); }).then(function(j){
        if (baseline === null){ baseline = j.room_mtime; return; }
        if (j.room_mtime && j.room_mtime !== baseline){ location.reload(); }
      }).catch(function(){});
    }, 5000);
  });

  apply();
</script>
</body>
</html>
"""


def collect():
    entries = []
    if not BRIEFS.exists():
        return entries
    for d in sorted(BRIEFS.iterdir()):
        if not d.is_dir():
            continue
        slug = d.name
        html_f = d / f"{slug}-brief.html"
        json_f = d / f"{slug}-brief.json"
        if not html_f.exists():
            continue
        meta = {}
        if json_f.exists():
            try:
                meta = json.loads(json_f.read_text(encoding="utf-8"))
            except Exception:
                meta = {}
        mtime = html_f.stat().st_mtime
        entries.append({
            "slug": slug,
            "mtime": sort_ts(meta, mtime),
            "chip": meta.get("chip") or "RESEARCH BRIEF",
            "title": meta.get("title") or slug,
            "dek": meta.get("dek") or "",
            "lens": meta.get("lens") or "",
            "compiled": meta.get("compiled") or "",
            "category": derive_category(meta),
            "priority": norm_pri(meta.get("priority")),
            "status": (meta.get("status") or "active").lower(),
            "superseded_by": meta.get("superseded_by") or "",
            "html": html_f, "json": json_f,
            "md": d / f"{slug}-brief.md",
            "ctx": d / f"{slug}-context.json",
        })
    entries.sort(key=lambda e: e["mtime"], reverse=True)
    return entries


def _write_status(json_f, status):
    import os
    try:
        meta = json.loads(json_f.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"[brief_library] ERROR reading {json_f}: {e}")
        return False
    meta["status"] = status
    tmp = str(json_f) + ".tmp"
    Path(tmp).write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, json_f)
    return True


def apply_currency(entries):
    """Auto-archive periodicals past policy age. Runs on every regen; returns
    the number flipped this pass. Deterministic librarian, never deletes."""
    import time as _t
    now = _t.time()
    flipped = 0
    for e in entries:
        days = AUTO_ARCHIVE_DAYS.get(e["category"])
        if days is None or e["status"] != "active":
            continue
        if (now - e["mtime"]) / 86400.0 > days:
            if _write_status(e["json"], "archived"):
                e["status"] = "archived"
                flipped += 1
                print(f"[brief_library] auto-archived ({e['category']} > {days}d): {e['slug']}")
    return flipped


def resolve_context_path(item):
    """Resolve a context-pack entry in the checkout that is active now.

    Repo-relative ``path`` is authoritative. ``abs`` remains a compatibility
    hint for old packs and genuinely external files, but it must never make a
    missing repo file look healthy merely because an old worktree still exists.
    """
    raw = str(item.get("path") or "").strip()
    if raw:
        candidate = Path(raw)
        if not candidate.is_absolute():
            for base in dict.fromkeys((ROOT.resolve(), CANONICAL_ROOT.resolve())):
                target = (base / candidate).resolve()
                if _inside(target, base) and target.exists():
                    return target
            return None
        return candidate if candidate.exists() else None

    legacy = str(item.get("abs") or "").strip()
    if legacy:
        candidate = Path(legacy)
        return candidate if candidate.is_absolute() and candidate.exists() else None
    return None


def housekeeping(entries):
    """Deterministic standards check: counts + stale + broken context-pack paths."""
    import time as _t
    now = _t.time()
    active = [e for e in entries if e["status"] == "active"]
    archived = [e for e in entries if e["status"] != "active"]
    stale = [e for e in active
             if e["category"] not in AUTO_ARCHIVE_DAYS
             and (now - e["mtime"]) / 86400.0 > STALE_DAYS]
    broken = []
    # Per-slug tally as well as the flat list. The aggregate "N broken paths"
    # tells you a number and hides the diagnosis: a context pack whose paths no
    # longer resolve grounds nothing, and it fails silently INSIDE the agent you
    # fed it to, not on this page. Flagging the card is what makes it actionable.
    by_slug = {}
    for e in entries:
        if not e["ctx"].exists():
            continue
        try:
            pack = json.loads(e["ctx"].read_text(encoding="utf-8"))
        except (OSError, ValueError):
            broken.append((e["slug"], "context pack unreadable"))
            by_slug[e["slug"]] = (1, 1)
            continue
        paths = pack.get("paths", [])
        gone = [p for p in paths if resolve_context_path(p) is None]
        for p in gone:
            broken.append((e["slug"], p.get("path") or "?"))
        if gone:
            by_slug[e["slug"]] = (len(gone), len(paths))
    return {"active": len(active), "archived": len(archived),
            "stale": [e["slug"] for e in stale], "broken": broken,
            "broken_by_slug": by_slug}


def card(e, broken_by_slug=None):
    dek = e["dek"]
    if len(dek) > 220:
        dek = dek[:217].rstrip() + "…"
    pri_tag = f'<span class="tagp p{e["priority"]}">P{e["priority"]}</span>' if e["priority"] else ""
    bk = (broken_by_slug or {}).get(e["slug"])
    pri_tag += (f'<span class="tagc risk" title="the context pack cites files that are gone">'
                f'ctx {bk[0]}/{bk[1]} paths gone</span>') if bk else ""
    cat_tag = f'<span class="tagc">{esc(e["category"])}</span>'
    if e["status"] != "active":
        cat_tag += '<span class="tagc arch">archived</span>'
    if e["superseded_by"]:
        succ = BRIEFS / e["superseded_by"] / f'{e["superseded_by"]}-brief.html'
        cat_tag += (f'<a class="tagc sup" href="{esc(room_href(succ))}" '
                    f'data-repo-path="{esc(repo_path(succ))}" '
                    f'onclick="event.stopPropagation()">superseded → {esc(e["superseded_by"])}</a>')
    links = (f'<span data-act="path" data-slug="{esc(e["slug"])}" title="copy the .md path — for Codex / Claude Code / any tool with file access">path</span>'
             f'<span class="cp" data-act="brief" data-slug="{esc(e["slug"])}" title="copy the full brief inline — paste into any AI chat">copy brief</span>')
    for label, f in (("md", e["md"]), ("ctx", e["ctx"])):
        if f.exists():
            warn = ""
            if label == "ctx" and (broken_by_slug or {}).get(e["slug"]):
                gone, total = broken_by_slug[e["slug"]]
                warn = f' class="warned" title="{gone} of {total} grounding paths no longer exist — re-render this brief before feeding its pack to an agent"'
            links += (f'<span data-static-href="{esc(room_href(f))}" '
                      f'data-repo-path="{esc(repo_path(f))}"{warn}>{label}</span>')
    arch_act = "unarchive" if e["status"] != "active" else "archive"
    links += f'<span data-life="{arch_act}" data-slug="{esc(e["slug"])}" title="librarian action — live when served, copies the command otherwise">{arch_act}</span>'
    metas = ""
    if e["compiled"]:
        metas += f'<span class="m">{esc(e["compiled"])}</span>'
    if e["lens"]:
        metas += f'<span class="m">{esc(e["lens"])}</span>'
    return (f'<a class="brief-card" href="{esc(room_href(e["html"]))}" '
            f'data-repo-path="{esc(repo_path(e["html"]))}" data-cat="{esc(e["category"])}" '
            f'data-pri="{e["priority"]}" data-mtime="{e["mtime"]}" data-status="{esc(e["status"])}">'
            f'<div class="toprow"><span class="chip">{esc(e["chip"])}</span>{pri_tag}{cat_tag}</div>'
            f'<h2>{accent_em(e["title"])}</h2>'
            f'<p>{esc(dek)}</p>'
            f'<div class="meta">{metas}<div class="links">{links}</div></div></a>')


class _RoomRouteParser(HTMLParser):
    """Collect portable card routes from the generated page without a browser."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.cards = []
        self.repo_links = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "a" and "brief-card" in classes:
            self.cards.append(values)
        if values.get("data-repo-path"):
            self.repo_links.append(values)


def _inside(path, root):
    # Predicate, not a handler: "not inside" is a real answer, not a hole.
    return path.is_relative_to(root)


def room_route_errors(page, entries):
    """Return card/link failures that would become 404s under static or live use."""
    parser = _RoomRouteParser()
    parser.feed(page)
    errors = []
    expected = {repo_path(e["html"]): room_href(e["html"]) for e in entries}
    cards = {}

    for attrs in parser.cards:
        route = attrs.get("data-repo-path") or ""
        if route in cards:
            errors.append(f"duplicate card route: {route}")
        cards[route] = attrs
        if (attrs.get("href") or "").startswith("file:"):
            errors.append(f"checkout-specific card href: {attrs.get('href')}")

    for route, href in expected.items():
        attrs = cards.get(route)
        if attrs is None:
            errors.append(f"missing card route: {route}")
        elif attrs.get("href") != href:
            errors.append(f"wrong static href for {route}: {attrs.get('href')} != {href}")
    for route in sorted(set(cards) - set(expected)):
        errors.append(f"unexpected card route: {route}")

    root_real = ROOT.resolve()
    briefs_real = BRIEFS.resolve()
    for attrs in parser.repo_links:
        route = urllib.parse.unquote(attrs.get("data-repo-path") or "")
        target = (ROOT / route).resolve()
        if not route or route.startswith("/") or not _inside(target, root_real):
            errors.append(f"unsafe live route: {route or '<empty>'}")
        elif not target.is_file():
            errors.append(f"missing live target: {route}")

        static = attrs.get("href") or attrs.get("data-static-href") or ""
        static_target = (BRIEFS / urllib.parse.unquote(static)).resolve()
        if not static or not _inside(static_target, briefs_real):
            errors.append(f"unsafe static route: {static or '<empty>'}")
        elif not static_target.is_file():
            errors.append(f"missing static target: {static}")

    return errors


def verify_room(page=None, entries=None):
    """Verify the current or proposed Briefing Room index without changing it."""
    entries = collect() if entries is None else entries
    if page is None:
        out = BRIEFS / "index.html"
        if not out.is_file():
            return [f"Briefing Room index missing: {out}"]
        page = out.read_text(encoding="utf-8")
    return room_route_errors(page, entries)


def side_buttons(entries):
    pri_counts = {}
    cat_counts = {}
    for e in entries:
        pri_counts[e["priority"]] = pri_counts.get(e["priority"], 0) + 1
        cat_counts[e["category"]] = cat_counts.get(e["category"], 0) + 1
    pri = [f'<button data-pri="all" class="on">all <span class="c">{len(entries)}</span></button>']
    for p in (1, 2, 3):
        if pri_counts.get(p):
            pri.append(f'<button data-pri="{p}">P{p} <span class="c">{pri_counts[p]}</span></button>')
    if pri_counts.get(0):
        pri.append(f'<button data-pri="0">unset <span class="c">{pri_counts[0]}</span></button>')
    cat = [f'<button data-cat="all" class="on">all <span class="c">{len(entries)}</span></button>']
    for c in sorted(cat_counts):
        cat.append(f'<button data-cat="{esc(c)}">{esc(c)} <span class="c">{cat_counts[c]}</span></button>')
    return "".join(pri), "".join(cat)


def find_entry(entries, slug):
    for e in entries:
        if e["slug"] == slug:
            return e
    return None


def cmd_lifecycle(action, slug):
    entries = collect()
    e = find_entry(entries, slug)
    if e is None:
        print(f"[brief_library] no brief with slug: {slug}")
        return 1
    status = "archived" if action == "archive" else "active"
    if not _write_status(e["json"], status):
        return 1
    print(f"[brief_library] {action}d: {slug}")
    generate()
    return 0


def cmd_audit():
    entries = collect()
    hk = housekeeping(entries)
    print(f"[brief_library] audit — {hk['active']} active · {hk['archived']} archived · "
          f"{len(hk['stale'])} stale · {len(hk['broken'])} broken context paths")
    for s in hk["stale"]:
        print(f"  stale (> {STALE_DAYS}d active): {s}")
    for slug, path in hk["broken"]:
        print(f"  broken path in {slug}: {path}")
    return 0


def cmd_verify():
    entries = collect()
    errors = verify_room(entries=entries)
    context_errors = housekeeping(entries)["broken"]
    errors.extend(f"missing context target in {slug}: {path}" for slug, path in context_errors)
    if errors:
        print(f"[brief_library] FAIL — {len(errors)} Briefing Room integrity error(s)")
        for error in errors:
            print(f"  {error}")
        return 1
    print(f"[brief_library] PASS — {len(entries)} cards and context packs resolve from the active root")
    return 0


def generate(open_after=False):
    entries = collect()
    apply_currency(entries)
    hk = housekeeping(entries)
    import datetime
    stamp = datetime.date.today().isoformat()
    packs = {}
    for e in entries:
        md_text = ""
        if e["md"].exists():
            try:
                md_text = e["md"].read_text(encoding="utf-8")
            except Exception:
                md_text = ""
        header = (f"SOURCE: {e['md']}  (research brief · Antigravity)\n"
                  f"HTML: {e['html']}\nCONTEXT PACK: {e['ctx']}\n"
                  "CONTEXT PATH RULE: resolve `path` from the active Antigravity root; "
                  "`abs` is a render-time hint only.\n"
                  f"COMPILED: {e['compiled'] or '—'}\n\n")
        packs[e["slug"]] = {"path": str(e["md"]), "brief": header + md_text}
    packs_json = json.dumps(packs, ensure_ascii=False).replace("</", "<\\/")
    pri_btns, cat_btns = side_buttons(entries)
    hk_bits = f"{hk['active']} active · {hk['archived']} archived"
    if hk["stale"]:
        hk_bits += f" · <b>{len(hk['stale'])} stale</b>"
    if hk["broken"]:
        hk_bits += f" · <b>{len(hk['broken'])} broken paths</b> (flagged on cards)"
    if not hk["stale"] and not hk["broken"]:
        hk_bits += " · shelves clean"
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from surface_nav import nav_html
        homenav = nav_html(current="briefs", style=False)
    except Exception:
        homenav = ""  # DELIBERATE-QUIET: nav bug must never block the room render
    page = (PAGE
            .replace("{{HOMENAV}}", homenav)
            .replace("{{COUNT}}", str(len(entries)))
            .replace("{{STAMP}}", stamp)
            .replace("{{HKEEP}}", hk_bits)
            .replace("{{N_ACTIVE}}", str(hk["active"]))
            .replace("{{N_ARCH}}", str(hk["archived"]))
            .replace("{{BOARD_URI}}", esc((ROOT / ".agent" / "assets" / "assets-board.html").as_uri()))
            .replace("{{PULSE_URI}}", esc((ROOT / ".agent" / "pulse" / "pulse-board.html").as_uri()))
            .replace("{{ORACLE_URI}}", esc((ROOT / ".agent" / "oracle" / "oracle-dashboard.html").as_uri()))
            .replace("{{MISSIONS_URI}}", esc((ROOT / ".agent" / "missions" / "mission-control.html").as_uri()))
            .replace("{{REPO_ROOT_JSON}}", json.dumps(str(ROOT)))
            .replace("{{PACKS}}", packs_json)
            .replace("{{PAGE_SIZE}}", str(PAGE_SIZE))
            .replace("{{PRI_BTNS}}", pri_btns)
            .replace("{{CAT_BTNS}}", cat_btns)
            .replace("{{CARDS}}", "".join(card(e, hk.get("broken_by_slug")) for e in entries)))
    route_errors = verify_room(page=page, entries=entries)
    if route_errors:
        details = "\n  ".join(route_errors)
        raise RuntimeError(f"Briefing Room route verification failed:\n  {details}")
    out = BRIEFS / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"[brief_library] OK → {out} ({len(entries)} briefs · routes verified · "
          f"{hk_bits.replace('<b>', '').replace('</b>', '')})")
    if open_after:
        subprocess.run(["open", str(out)], check=False)


def main():
    ap = argparse.ArgumentParser(description="The Briefing Room librarian: generate (default), archive, unarchive, audit, verify.")
    ap.add_argument("cmd", nargs="?", default="generate",
                    choices=["generate", "archive", "unarchive", "audit", "verify"])
    ap.add_argument("slug", nargs="?", default=None)
    ap.add_argument("--open", action="store_true")
    args = ap.parse_args()
    if args.cmd in ("archive", "unarchive"):
        if not args.slug:
            raise SystemExit(f"usage: brief_library.py {args.cmd} <slug>")
        raise SystemExit(cmd_lifecycle(args.cmd, args.slug))
    if args.cmd == "audit":
        raise SystemExit(cmd_audit())
    if args.cmd == "verify":
        raise SystemExit(cmd_verify())
    generate(open_after=args.open)


if __name__ == "__main__":
    main()
