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
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRIEFS = ROOT / "deliverables" / "research-briefs"
PAGE_SIZE = 10


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
    except ValueError:
        return 0


def derive_category(meta):
    cat = str(meta.get("category") or "").strip().lower()
    if cat:
        return cat
    chip = str(meta.get("chip") or "").split("·")[0].strip().lower()
    return chip or "uncategorized"


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
    <span class="kicker">ANTIGRAVITY RESEARCH · LIBRARY</span>
    <h1>the briefing <em>room</em></h1>
    <p class="dek">every rendered brief. click a card to open it; path feeds file-access tools, copy brief feeds any chat AI; md and ctx open the artifacts.</p>
    <div class="count">{{COUNT}} briefs on file · regenerated {{STAMP}}</div>
  </header>
  <div class="layout">
    <aside class="side">
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
  var state = { sort:'newest', pri:'all', cat:'all', page:1 };

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
      state.page = 1; apply();
    });
  });
  function mark(sel, on){
    document.querySelectorAll('.side button' + sel).forEach(function(x){ x.classList.remove('on'); });
    on.classList.add('on');
  }

  document.querySelectorAll('.brief-card .links span[data-href]').forEach(function(el){
    el.addEventListener('click', function(ev){ ev.preventDefault(); ev.stopPropagation(); window.location = el.dataset.href; });
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
        entries.append({
            "slug": slug,
            "mtime": html_f.stat().st_mtime,
            "chip": meta.get("chip") or "RESEARCH BRIEF",
            "title": meta.get("title") or slug,
            "dek": meta.get("dek") or "",
            "lens": meta.get("lens") or "",
            "compiled": meta.get("compiled") or "",
            "category": derive_category(meta),
            "priority": norm_pri(meta.get("priority")),
            "html": html_f, "json": json_f,
            "md": d / f"{slug}-brief.md",
            "ctx": d / f"{slug}-context.json",
        })
    entries.sort(key=lambda e: e["mtime"], reverse=True)
    return entries


def card(e):
    dek = e["dek"]
    if len(dek) > 220:
        dek = dek[:217].rstrip() + "…"
    pri_tag = f'<span class="tagp p{e["priority"]}">P{e["priority"]}</span>' if e["priority"] else ""
    cat_tag = f'<span class="tagc">{esc(e["category"])}</span>'
    links = (f'<span data-act="path" data-slug="{esc(e["slug"])}" title="copy the .md path — for Codex / Claude Code / any tool with file access">path</span>'
             f'<span class="cp" data-act="brief" data-slug="{esc(e["slug"])}" title="copy the full brief inline — paste into any AI chat">copy brief</span>')
    for label, f in (("md", e["md"]), ("ctx", e["ctx"])):
        if f.exists():
            links += f'<span data-href="{esc(f.as_uri())}">{label}</span>'
    metas = ""
    if e["compiled"]:
        metas += f'<span class="m">{esc(e["compiled"])}</span>'
    if e["lens"]:
        metas += f'<span class="m">{esc(e["lens"])}</span>'
    return (f'<a class="brief-card" href="{esc(e["html"].as_uri())}" data-cat="{esc(e["category"])}" '
            f'data-pri="{e["priority"]}" data-mtime="{e["mtime"]}">'
            f'<div class="toprow"><span class="chip">{esc(e["chip"])}</span>{pri_tag}{cat_tag}</div>'
            f'<h2>{accent_em(e["title"])}</h2>'
            f'<p>{esc(dek)}</p>'
            f'<div class="meta">{metas}<div class="links">{links}</div></div></a>')


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


def main():
    ap = argparse.ArgumentParser(description="Generate the Briefing Room index.")
    ap.add_argument("--open", action="store_true")
    args = ap.parse_args()

    entries = collect()
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
                  f"COMPILED: {e['compiled'] or '—'}\n\n")
        packs[e["slug"]] = {"path": str(e["md"]), "brief": header + md_text}
    packs_json = json.dumps(packs, ensure_ascii=False).replace("</", "<\\/")
    pri_btns, cat_btns = side_buttons(entries)
    page = (PAGE
            .replace("{{COUNT}}", str(len(entries)))
            .replace("{{STAMP}}", stamp)
            .replace("{{PACKS}}", packs_json)
            .replace("{{PAGE_SIZE}}", str(PAGE_SIZE))
            .replace("{{PRI_BTNS}}", pri_btns)
            .replace("{{CAT_BTNS}}", cat_btns)
            .replace("{{CARDS}}", "".join(card(e) for e in entries)))
    out = BRIEFS / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"[brief_library] OK → {out} ({len(entries)} briefs)")
    if args.open:
        subprocess.run(["open", str(out)], check=False)


if __name__ == "__main__":
    main()
