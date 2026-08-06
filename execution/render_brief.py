#!/usr/bin/env python3
"""
render_brief.py — deterministic research-brief HTML renderer (Layer 3).

Takes a structured brief JSON, injects it into templates/research-brief/template.html,
writes deliverables/research-briefs/<slug>/<slug>-brief.html (+ copies the source JSON
alongside for provenance). The asset board indexes that directory as the Briefs shelf.

Design system: Codex Antigravity (_active/codex-harvest-2026-06-11/DESIGN.md) — tokens
live in the template, never here. All content strings are html-escaped (XSS discipline
mirrors asset_gallery.py: briefs carry arbitrary scraped text).

Usage:
    python3 execution/render_brief.py <brief.json> [--out-dir DIR] [--open]

Brief JSON schema (all content fields are plain text; wrap ONE word in *asterisks*
inside title/heading fields to set it in the italic-serif accent voice):

{
  "slug": "ai-seo-zeitgeist",
  "chip": "RESEARCH BRIEF · X + WEB",
  "title": "what's moving in *ai seo*",
  "dek": "one-paragraph promise of what this brief covers and why now.",
  "window": "last 30 days",
  "lens": "marketing · creative · mcp",
  "sources": "~120 posts + press",
  "compiled": "aug 5, 2026",
  "footer_left": "ANTIGRAVITY RESEARCH",
  "footer_right": "@farricecain",
  "run_cost_usd": 0.03,                # optional — shown in ledger section head
  "stack": ["semrush", "reddit"],      # optional — tool provenance line
  "sections": [
    {"kind":"summary",  "heading":"the big picture", "kicker":"WHAT'S FORMING", "body":"..."},
    {"kind":"prose",    "heading":"context", "body":"...\n\nparagraphs split on blank lines"},
    {"kind":"evidence", "heading":"what the data says", "tag":"THE EVIDENCE",
      "rows":[{"claim":"...", "evidence":"...", "source_url":"https://…",
               "source_label":"r/seo · 2.4k upvotes", "confidence":"VERIFIED|LIKELY|UNCONFIRMED"}]},
    {"kind":"bars",     "heading":"search demand", "caption":"same scale, very different shapes",
      "series":[{"label":"ai seo", "note":"peaked mid-year", "values":[3,5,8,...]}]},
    {"kind":"decision", "heading":"where the lane actually *is*", "kicker":"THE OPENING",
      "dek":"what the data supports doing, in order.",
      "items":[{"action":"...", "why":"evidence sentence with the number in it"}]},
    {"kind":"deploy",   "heading":"deploy blocks", "tag":"COPY-PASTE",
      "blocks":[{"label":"research prompt", "text":"..."}]},
    {"kind":"caveats",  "heading":"what this *isn't*", "kicker":"CAVEATS WORTH KEEPING",
      "body":"reliability ranking of this brief's own data.",
      "cta":{"label":"OKAY, SO MAKE THE POST", "href":"#deploy-blocks"}}
  ],
  "ledger":[{"source":"...", "url":"https://…", "retrieved":"2026-08-05",
             "used_for":"...", "confidence":"VERIFIED"}]
}
"""
import argparse
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "research-brief" / "template.html"
DEFAULT_OUT = ROOT / "deliverables" / "research-briefs"
CONFIDENCE = {"VERIFIED", "LIKELY", "UNCONFIRMED"}


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def accent(s):
    """Escape, then set the single *starred* word in the italic-serif accent voice."""
    out = esc(s)
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", out, count=1)


def anchor(heading):
    plain = re.sub(r"[^a-z0-9]+", "-", re.sub(r"\*", "", str(heading)).lower()).strip("-")
    return plain or "section"


def conf_chip(value):
    v = str(value or "UNCONFIRMED").upper()
    if v not in CONFIDENCE:
        v = "UNCONFIRMED"
    return f'<span class="conf {v.lower()}">{v}</span>'


def paragraphs(body):
    parts = [p.strip() for p in str(body or "").split("\n\n") if p.strip()]
    return "".join(f"<p>{esc(p)}</p>" for p in parts) or "<p></p>"


def sec_head(num, heading, tag=None):
    tag_html = f'<span class="sectag">{esc(tag)}</span>' if tag else ""
    return (f'<div class="sechead"><span class="secnum">{num:02d}</span>'
            f'<h2 class="sec">{accent(heading)}</h2>{tag_html}</div>')


def render_summary(num, s):
    kicker = f'<span class="kicker" style="margin-bottom:8px">{esc(s.get("kicker"))}</span>' if s.get("kicker") else ""
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag"))}'
            f'{kicker}<div class="panel">{paragraphs(s.get("body"))}</div></section>')


def render_prose(num, s):
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag"))}'
            f'{paragraphs(s.get("body"))}</section>')


def render_evidence(num, s):
    rows = []
    for r in s.get("rows", []):
        src = ""
        if r.get("source_url"):
            src = (f'<a class="srcref" href="{esc(r["source_url"])}" target="_blank" rel="noopener">'
                   f'{esc(r.get("source_label") or "view source")} ↗</a>')
        elif r.get("source_label"):
            src = f'<span class="srcref">{esc(r["source_label"])}</span>'
        rows.append(
            '<div class="ev"><span class="mark">✓</span><div>'
            f'<h3>{esc(r.get("claim"))}</h3><p>{esc(r.get("evidence"))}</p>'
            f'<div class="meta">{conf_chip(r.get("confidence"))}{src}</div>'
            "</div></div>"
        )
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag"))}'
            + "".join(rows) + "</section>")


def render_bars(num, s):
    series = s.get("series", [])
    global_max = max((max(x.get("values") or [0]) for x in series), default=1) or 1
    caption = f'<div class="bars-caption">{esc(s.get("caption"))}</div>' if s.get("caption") else ""
    single_valued = series and all(len(x.get("values") or []) == 1 for x in series)
    if single_valued:
        # comparison mode: one card, horizontal bars, shared scale
        rows = []
        for x in series:
            v = (x.get("values") or [0])[0]
            pct = max(1, round(100 * v / global_max))
            note = f'<span class="hnote">{esc(x.get("note"))}</span>' if x.get("note") else ""
            rows.append(
                f'<div class="hbar-row"><div class="hbar-label">{esc(x.get("label"))}{note}</div>'
                f'<div class="hbar-track"><i style="width:{pct}%"{" class=zero" if v == 0 else ""}></i></div>'
                f'<div class="hbar-val">{esc(v)}</div></div>'
            )
        body = f'<div class="bars-card">{"".join(rows)}</div>'
    else:
        # small multiples: one card per series, shared vertical scale
        cards = []
        for x in series:
            bars = "".join(
                f'<i style="height:{max(3, round(100 * v / global_max))}%"></i>' for v in (x.get("values") or [])
            )
            note = f'<div class="note">{esc(x.get("note"))}</div>' if x.get("note") else ""
            cards.append(f'<div class="bars-card"><h3>{esc(x.get("label"))}</h3>{note}<div class="bars">{bars}</div></div>')
        body = f'<div class="bars-group">{"".join(cards)}</div>'
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag"))}'
            f"{body}{caption}</section>")


def render_decision(num, s):
    items = "".join(
        f'<div class="dec-item"><span class="n">{i + 1:02d}</span><div>'
        f'<h3>{esc(it.get("action"))}</h3><p>{esc(it.get("why"))}</p></div></div>'
        for i, it in enumerate(s.get("items", []))
    )
    kicker = f'<span class="kicker">{esc(s.get("kicker") or "THE OPENING")}</span>'
    dek = f'<p class="dek">{esc(s.get("dek"))}</p>' if s.get("dek") else ""
    return (f'<section class="decision" id="{anchor(s["heading"])}">{kicker}'
            f'<h2>{accent(s["heading"])}</h2>{dek}<div style="margin-top:20px">{items}</div></section>')


def render_deploy(num, s):
    blocks = "".join(
        '<div class="deploy"><div class="bar">'
        f'<span class="k">{esc(b.get("label"))}</span><button class="copybtn" type="button">copy</button>'
        f"</div><pre>{esc(b.get('text'))}</pre></div>"
        for b in s.get("blocks", [])
    )
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag") or "COPY-PASTE")}'
            + blocks + "</section>")


def render_caveats(num, s):
    kicker = f'<span class="kicker" style="margin-bottom:10px">{esc(s.get("kicker") or "CAVEATS WORTH KEEPING")}</span>'
    cta = ""
    if s.get("cta"):
        cta = f'<a class="cta" href="{esc(s["cta"].get("href") or "#")}">{esc(s["cta"].get("label"))}</a>'
    return (f'<section class="blk caveats" id="{anchor(s["heading"])}">{kicker}'
            f'<h2>{accent(s["heading"])}</h2>{paragraphs(s.get("body"))}{cta}</section>')


RENDERERS = {
    "summary": render_summary,
    "prose": render_prose,
    "evidence": render_evidence,
    "bars": render_bars,
    "decision": render_decision,
    "deploy": render_deploy,
    "caveats": render_caveats,
}


def render_ledger(num, brief):
    rows = brief.get("ledger", [])
    if not rows:
        return ""
    cost = brief.get("run_cost_usd")
    stack = brief.get("stack")
    meta_bits = []
    if cost is not None:
        meta_bits.append(f"run cost ${float(cost):.2f}")
    if stack:
        meta_bits.append("stack: " + " · ".join(str(x) for x in stack))
    tag = " — ".join(meta_bits) if meta_bits else None
    body_rows = []
    for i, r in enumerate(rows):
        if r.get("url"):
            url = esc(r["url"])
            url_cell = f'<a href="{url}" target="_blank" rel="noopener">{url}</a>'
        else:
            url_cell = "—"
        body_rows.append(
            "<tr>"
            f'<td>{i + 1:02d}</td><td>{esc(r.get("source"))}</td>'
            f"<td>{url_cell}</td>"
            f'<td>{esc(r.get("retrieved"))}</td><td>{esc(r.get("used_for"))}</td>'
            f"<td>{conf_chip(r.get('confidence'))}</td>"
            "</tr>"
        )
    body_rows = "".join(body_rows)
    return (f'<section class="blk" id="source-ledger">{sec_head(num, "source ledger", tag)}'
            '<table class="ledger"><thead><tr><th>#</th><th>Source</th><th>URL</th>'
            "<th>Retrieved</th><th>Used for</th><th>Confidence</th></tr></thead>"
            f"<tbody>{body_rows}</tbody></table></section>")


def build_nav(brief):
    links = []
    for s in brief.get("sections", []):
        if s.get("heading"):
            plain = re.sub(r"\*", "", s["heading"])
            links.append(f'<a href="#{anchor(s["heading"])}">{esc(plain)}</a>')
    if brief.get("ledger"):
        links.append('<a href="#source-ledger">sources</a>')
    return "".join(links)


def render(brief):
    tpl = TEMPLATE.read_text(encoding="utf-8")
    sections_html, n = [], 0
    for s in brief.get("sections", []):
        kind = s.get("kind")
        if kind not in RENDERERS:
            raise SystemExit(f"unknown section kind: {kind!r}")
        n += 1
        sections_html.append(RENDERERS[kind](n, s))
    ledger_html = render_ledger(n + 1, brief)
    if ledger_html:
        sections_html.append(ledger_html)
    title_plain = re.sub(r"\*", "", brief.get("title", "untitled"))
    subs = {
        "{{TITLE_PLAIN}}": esc(title_plain),
        "{{NAV}}": build_nav(brief),
        "{{CHIP}}": esc(brief.get("chip") or "RESEARCH BRIEF"),
        "{{TITLE}}": accent(brief.get("title") or "untitled"),
        "{{DEK}}": esc(brief.get("dek") or ""),
        "{{WINDOW}}": esc(brief.get("window") or "—"),
        "{{LENS}}": esc(brief.get("lens") or "—"),
        "{{SOURCES}}": esc(brief.get("sources") or "—"),
        "{{COMPILED}}": esc(brief.get("compiled") or "—"),
        "{{SECTIONS}}": "".join(sections_html),
        "{{FOOTER_LEFT}}": esc(brief.get("footer_left") or "ANTIGRAVITY RESEARCH"),
        "{{FOOTER_RIGHT}}": esc(brief.get("footer_right") or ""),
    }
    for k, v in subs.items():
        tpl = tpl.replace(k, v)
    return tpl


def _plain(s):
    return re.sub(r"\*", "", str(s or ""))


def render_markdown(brief):
    """Agent-paste mirror of the brief. JSON stays canonical; this is the compact context form."""
    out = [f"# {_plain(brief.get('title'))}", ""]
    out.append(f"> {brief.get('chip', 'RESEARCH BRIEF')} · window: {brief.get('window', '—')} · "
               f"lens: {brief.get('lens', '—')} · sources: {brief.get('sources', '—')} · "
               f"compiled: {brief.get('compiled', '—')}")
    if brief.get("dek"):
        out += ["", brief["dek"]]
    for s in brief.get("sections", []):
        kind = s.get("kind")
        out += ["", f"## {_plain(s.get('heading', kind))}"]
        if kind == "evidence":
            for r in s.get("rows", []):
                conf = str(r.get("confidence", "UNCONFIRMED")).upper()
                src = r.get("source_url") or r.get("source_label") or ""
                out.append(f"- **{r.get('claim')}** [{conf}] — {r.get('evidence')} ({src})")
        elif kind == "decision":
            if s.get("dek"):
                out.append(s["dek"])
            for i, it in enumerate(s.get("items", []), 1):
                out.append(f"{i}. **{it.get('action')}** — {it.get('why')}")
        elif kind == "bars":
            for x in s.get("series", []):
                vals = x.get("values") or []
                val = vals[0] if len(vals) == 1 else vals
                note = f" ({x.get('note')})" if x.get("note") else ""
                out.append(f"- {x.get('label')}: {val}{note}")
            if s.get("caption"):
                out.append(f"_{s['caption']}_")
        elif kind == "deploy":
            for b in s.get("blocks", []):
                out += [f"**{b.get('label')}**", "```", str(b.get("text", "")), "```"]
        else:  # summary / prose / caveats
            if s.get("kicker"):
                out.append(f"_{s['kicker']}_")
            out.append(str(s.get("body", "")))
    if brief.get("ledger"):
        out += ["", "## Source ledger"]
        for i, r in enumerate(brief["ledger"], 1):
            url = f" — {r['url']}" if r.get("url") else ""
            out.append(f"{i}. {r.get('source')}{url} (retrieved {r.get('retrieved', '?')}, "
                       f"{str(r.get('confidence', 'UNCONFIRMED')).upper()}; used for: {r.get('used_for', '')})")
    if brief.get("run_cost_usd") is not None or brief.get("stack"):
        bits = []
        if brief.get("run_cost_usd") is not None:
            bits.append(f"run cost ${float(brief['run_cost_usd']):.2f}")
        if brief.get("stack"):
            bits.append("stack: " + " · ".join(str(x) for x in brief["stack"]))
        out += ["", f"_{' — '.join(bits)}_"]
    return "\n".join(out) + "\n"


def export_gdoc(out_html, title):
    """Upload the rendered HTML to Drive as a native Google Doc via the gws CLI.

    Graceful by design: any failure (7-day OAuth expiry is the known one) returns None
    with a one-line warning — the brief itself must never block on Google.
    """
    try:
        r = subprocess.run(
            ["gws", "drive", "files", "create",
             "--json", json.dumps({"name": title,
                                   "mimeType": "application/vnd.google-apps.document"}),
             "--upload", str(out_html),
             "--upload-content-type", "text/html"],
            capture_output=True, text=True, timeout=120,
        )
        if r.returncode != 0:
            print(f"[render_brief] WARN gdoc export failed (brief still rendered): {r.stderr.strip()[:160]}")
            return None
        data = json.loads(r.stdout)
        file_id = data.get("id")
        if not file_id:
            print("[render_brief] WARN gdoc export returned no file id")
            return None
        return f"https://docs.google.com/document/d/{file_id}/edit"
    except Exception as e:  # gws missing, timeout, bad JSON — same graceful contract
        print(f"[render_brief] WARN gdoc export failed (brief still rendered): {e}")
        return None


def main():
    ap = argparse.ArgumentParser(description="Render a research-brief JSON to house-style HTML.")
    ap.add_argument("brief_json")
    ap.add_argument("--out-dir", default=None, help="override output root (default deliverables/research-briefs)")
    ap.add_argument("--open", action="store_true", help="open the rendered brief in the default browser")
    ap.add_argument("--gdoc", action="store_true",
                    help="also export as a native Google Doc via gws (graceful skip on auth failure)")
    args = ap.parse_args()

    src = Path(args.brief_json)
    brief = json.loads(src.read_text(encoding="utf-8"))
    slug = brief.get("slug") or src.stem
    out_root = Path(args.out_dir) if args.out_dir else DEFAULT_OUT
    out_dir = out_root / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    out_html = out_dir / f"{slug}-brief.html"
    out_html.write_text(render(brief), encoding="utf-8")
    out_json = out_dir / f"{slug}-brief.json"
    if src.resolve() != out_json.resolve():
        shutil.copyfile(src, out_json)

    gdoc_url = export_gdoc(out_html, _plain(brief.get("title") or slug)) if args.gdoc else None
    if gdoc_url:
        brief["gdoc_url"] = gdoc_url
        out_json.write_text(json.dumps(brief, indent=2, ensure_ascii=False), encoding="utf-8")

    md = render_markdown(brief)
    if gdoc_url:
        md += f"\n_Google Doc: {gdoc_url}_\n"
    (out_dir / f"{slug}-brief.md").write_text(md, encoding="utf-8")

    print(f"[render_brief] OK → {out_html}")
    print(f"[render_brief] md → {out_dir / (slug + '-brief.md')}")
    if gdoc_url:
        print(f"[render_brief] gdoc → {gdoc_url}")
    if args.open:
        subprocess.run(["open", str(out_html)], check=False)


if __name__ == "__main__":
    main()
