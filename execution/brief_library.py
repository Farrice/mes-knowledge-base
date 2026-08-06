#!/usr/bin/env python3
"""
brief_library.py — the Briefing Room (Layer 3, deterministic, $0).

Scans deliverables/research-briefs/*/ and generates deliverables/research-briefs/index.html:
every brief newest-first in the Farrice Cain Premium Minimal report dialect
(_active/farrice-brand/premium-minimal/REPORT-DIALECT.md). Each card links the
HTML brief, the agent-paste .md mirror, and the -context.json agent pack.

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


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def accent(s):
    out = esc(re.sub(r"\*", "", str(s or "")))
    return out


def accent_em(s):
    out = esc(str(s or ""))
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", out, count=1)


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
    --ag-ink-soft: oklch(44% 0.003 110);  /* graphite */
    --ag-ink-mute: oklch(62% 0.012 110);  /* stone */
    --sans:'Helvetica Neue','Neue Haas Grotesk Text Pro',Helvetica,Inter,system-ui,Arial,sans-serif;
    --serif:'Source Serif 4',Georgia,'Times New Roman',serif;
    --mono:'JetBrains Mono',ui-monospace,'SF Mono',Menlo,monospace;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  body{ background:var(--ag-paper); color:var(--ag-ink); font-family:var(--sans) }
  .wrap{ max-width:760px; margin:0 auto; padding:52px 28px 90px }
  .kicker{ font-family:var(--mono); font-size:10px; letter-spacing:.22em; text-transform:uppercase; color:var(--ag-ink-mute); display:block }
  h1{ font-size:48px; line-height:1.05; letter-spacing:-.022em; font-weight:700; margin-top:16px }
  h1 em{ font-family:var(--serif); font-style:italic; font-weight:400; color:var(--ag-accent) }
  .dek{ font-size:14px; line-height:1.55; color:var(--ag-ink-soft); margin-top:14px; max-width:56ch }
  .count{ font-family:var(--mono); font-size:9px; letter-spacing:.16em; text-transform:uppercase; color:var(--ag-ink-mute);
    border-top:1px solid var(--ag-ink); margin-top:28px; padding-top:10px }
  .brief-card{ display:block; border:1px solid var(--ag-line); border-radius:8px; background:var(--ag-surface);
    padding:20px 22px; margin-top:16px; text-decoration:none; color:var(--ag-ink); transition:border-color .15s }
  .brief-card:hover{ border-color:var(--ag-accent) }
  .brief-card .chip{ display:inline-block; font-family:var(--mono); font-size:8.5px; letter-spacing:.18em; text-transform:uppercase;
    color:var(--ag-accent); border:1px solid var(--ag-accent); border-radius:99px; padding:3px 10px }
  .brief-card h2{ font-size:22px; letter-spacing:-.015em; font-weight:700; margin-top:12px; line-height:1.2 }
  .brief-card h2 em{ font-family:var(--serif); font-style:italic; font-weight:400; color:var(--ag-accent) }
  .brief-card p{ font-size:12.5px; line-height:1.55; color:var(--ag-ink-soft); margin-top:8px; max-width:60ch }
  .brief-card .meta{ display:flex; gap:14px; flex-wrap:wrap; margin-top:14px; align-items:center }
  .brief-card .m{ font-family:var(--mono); font-size:8.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--ag-ink-mute) }
  .brief-card .links{ margin-left:auto; display:flex; gap:8px }
  .brief-card .links span{ font-family:var(--mono); font-size:8.5px; letter-spacing:.12em; text-transform:uppercase;
    color:var(--ag-ink-soft); border:1px solid var(--ag-line); border-radius:4px; padding:3px 8px }
  .brief-card .links span:hover{ border-color:var(--ag-accent); color:var(--ag-accent) }
  footer{ margin-top:80px; border-top:1px solid var(--ag-ink); padding-top:12px; display:flex; justify-content:space-between;
    font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--ag-ink-mute) }
  @media (max-width:640px){ h1{ font-size:34px } .brief-card .links{ margin-left:0 } }
</style>
</head>
<body>
<div class="wrap">
  <header>
    <span class="kicker">ANTIGRAVITY RESEARCH · LIBRARY</span>
    <h1>the briefing <em>room</em></h1>
    <p class="dek">every rendered brief, newest first. each card opens the visual brief; md is the agent-paste mirror; ctx is the agent context pack.</p>
    <div class="count">{{COUNT}} briefs on file · regenerated {{STAMP}}</div>
  </header>
  {{CARDS}}
  <footer><span>ANTIGRAVITY RESEARCH</span><span>@farricecain</span></footer>
</div>
<script>
  document.querySelectorAll('.brief-card .links span[data-href]').forEach(function(el){
    el.addEventListener('click', function(ev){ ev.preventDefault(); ev.stopPropagation(); window.location = el.dataset.href; });
  });
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
    links = ""
    for label, f in (("md", e["md"]), ("ctx", e["ctx"])):
        if f.exists():
            links += f'<span data-href="{esc(f.as_uri())}">{label}</span>'
    metas = ""
    if e["compiled"]:
        metas += f'<span class="m">{esc(e["compiled"])}</span>'
    if e["lens"]:
        metas += f'<span class="m">{esc(e["lens"])}</span>'
    return (f'<a class="brief-card" href="{esc(e["html"].as_uri())}">'
            f'<span class="chip">{esc(e["chip"])}</span>'
            f'<h2>{accent_em(e["title"])}</h2>'
            f'<p>{esc(dek)}</p>'
            f'<div class="meta">{metas}<div class="links">{links}</div></div></a>')


def main():
    ap = argparse.ArgumentParser(description="Generate the Briefing Room index.")
    ap.add_argument("--open", action="store_true")
    args = ap.parse_args()

    entries = collect()
    import datetime
    stamp = datetime.date.today().isoformat()
    page = (PAGE
            .replace("{{COUNT}}", str(len(entries)))
            .replace("{{STAMP}}", stamp)
            .replace("{{CARDS}}", "".join(card(e) for e in entries)))
    out = BRIEFS / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"[brief_library] OK → {out} ({len(entries)} briefs)")
    if args.open:
        subprocess.run(["open", str(out)], check=False)


if __name__ == "__main__":
    main()
