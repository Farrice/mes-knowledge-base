#!/usr/bin/env python3
"""
render_brief.py — deterministic research-brief HTML renderer (Layer 3).

Takes a structured brief JSON, injects it into templates/research-brief/template.html,
writes deliverables/research-briefs/<slug>/<slug>-brief.html (+ copies the source JSON
alongside for provenance). The asset board indexes that directory as the Briefs shelf.

Design system: Farrice Cain Premium Minimal, report dialect
(_active/farrice-brand/premium-minimal/ + REPORT-DIALECT.md) — tokens live in the
template, never here. All content strings are html-escaped (XSS discipline
mirrors asset_gallery.py: briefs carry arbitrary scraped text).

Usage:
    python3 execution/render_brief.py <brief.json> [--out-dir DIR] [--open]

Outputs per slug: <slug>-brief.html, <slug>-brief.json (provenance copy),
<slug>-brief.md (agent-paste mirror), <slug>-context.json (agent context pack —
every file path + source URL the brief references, with roles).

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
  "category": "research",              # optional — Briefing Room sidebar shelf (brief_library.py)
  "priority": 1,                       # optional — 1-3 (1 highest; also accepts "P1"/"high")
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
      "cta":{"label":"OKAY, SO MAKE THE POST", "href":"#deploy-blocks"}},

    # ── enrichment kinds (2026-08-06, all additive) ──
    {"kind":"playbook", "heading":"the playbook", "tag":"RUN THIS",
      "plays":[{"title":"...", "intent":"one line on why this play", "command":"python3 …",
                "touches":["execution/foo.py", ".agent/bar.json"], "receipt":"what to check after"}]},
    {"kind":"assets",   "heading":"linked assets", "tag":"THE RAIL",
      "items":[{"title":"...", "role":"POSTER", "path":"deliverables/…/x.png",
                "thumb":"deliverables/…/x.png",   # optional image preview
                "note":"..."}]},
    {"kind":"timeline", "heading":"how we got here",
      "items":[{"date":"2026-08-05", "title":"...", "body":"...", "done":true}]},
    {"kind":"flow",     "heading":"the pipeline", "caption":"optional",
      "steps":[{"title":"...", "note":"..."}]},
    {"kind":"stats",    "heading":"by the numbers",
      "items":[{"value":"229", "unit":"engagers", "label":"4 POSTS SCRAPED", "note":"$0.50 total"}]},

    # ── chart kinds (2026-08-07). Inline SVG, no libraries, tokens from the template.
    # A chart earns its place or it is not emitted: the CALLER drops the section when
    # the series is flat or too short (see mission_brief.py::chart_earns_place).
    {"kind":"spark",    "heading":"momentum", "caption":"optional",
      "series":[{"label":"sessions", "values":[0,1,3,2,4], "value":"10", "unit":"in 14d",
                 "note":"per day"}]},            # each series scaled to its OWN range
    {"kind":"progress", "heading":"where this stands", "note":"optional line under",
      "stages":[{"label":"research", "state":"done"},      # done | current | todo | blocked
                {"label":"draft",    "state":"current", "note":"optional"},
                {"label":"shipped",  "state":"todo"}]},
    {"kind":"matrix",   "heading":"where things sit",
      "axes":{"x":"effort →", "y":"↑ impact"},
      "quads":[{"label":"HIGH IMPACT · LOW EFFORT",
                "items":[{"name":"...", "note":"..."}]}]},   # 4 quads: TL TR BL BR
    {"kind":"related",  "heading":"swings to", "tag":"CONNECTED",
      "links":[{"k":"BRIEF", "title":"...", "path":"deliverables/…/x-brief.html"},
               {"k":"SOLUTION", "title":"...", "path":"docs/solutions/….md"},
               {"k":"WEB", "title":"...", "href":"https://…"}]}
  ],
  "ledger":[{"source":"...", "url":"https://…", "retrieved":"2026-08-05",
             "used_for":"...", "confidence":"VERIFIED"}],
  "context":[{"path":"FARRICE-MASTER-CONTEXT.md", "role":"canonical identity"}]  # optional extras for the pack
}
"""
import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "research-brief" / "template.html"
DEFAULT_OUT = ROOT / "deliverables" / "research-briefs"
CONFIDENCE = {"VERIFIED", "LIKELY", "UNCONFIRMED"}

# Share mode (--share): strip internals so the variant is safe to send outward.
# Module-level flag set only inside render(); single-threaded CLI, reset in finally.
SHARE = False


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


def _is_url(s):
    return bool(re.match(r"^[a-z][a-z0-9+.-]*://", str(s or "")))


def _file_href(path):
    """repo-relative or absolute path → file:// href."""
    p = str(path or "")
    if _is_url(p):
        return p
    ap = Path(p)
    if not ap.is_absolute():
        ap = ROOT / p
    return ap.as_uri()


def _rel_display(path):
    """Show paths repo-relative wherever possible."""
    p = str(path or "")
    root = str(ROOT) + "/"
    return p[len(root):] if p.startswith(root) else p


def render_playbook(num, s):
    plays = []
    for i, p in enumerate(s.get("plays", []), 1):
        intent = f'<p class="intent">{esc(p.get("intent"))}</p>' if p.get("intent") else ""
        touches = ""
        if p.get("touches") and not SHARE:
            touches = ('<div class="touches">'
                       + "".join(f"<span>{esc(_rel_display(t))}</span>" for t in p["touches"])
                       + "</div>")
        receipt = f'<div class="receipt"><b>receipt</b>{esc(p.get("receipt"))}</div>' if p.get("receipt") else ""
        plays.append(
            '<div class="play"><div class="head">'
            f'<span class="n">{i:02d}</span><h3>{esc(p.get("title"))}</h3>'
            '<button class="copybtn" type="button">copy</button></div>'
            f'<div class="body">{intent}<pre>{esc(p.get("command"))}</pre>{touches}{receipt}</div></div>'
        )
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag") or "RUN THIS")}'
            + "".join(plays) + "</section>")


def render_assets(num, s):
    cards = []
    for it in s.get("items", []):
        role = f'<span class="role">{esc(it.get("role") or "ASSET")}</span>'
        thumb = ""
        if it.get("thumb") and not SHARE:
            thumb = f'<img src="{esc(_file_href(it["thumb"]))}" alt="{esc(it.get("title"))}" loading="lazy">'
        note = f"<p>{esc(it.get('note'))}</p>" if it.get("note") else ""
        path_abs = str((ROOT / it["path"]) if it.get("path") and not _is_url(it["path"]) and not Path(it["path"]).is_absolute()
                       else it.get("path") or "")
        pathrow = ""
        if it.get("path") and not SHARE:
            pathrow = ('<div class="pathrow">'
                       f'<a class="path" href="{esc(_file_href(it["path"]))}">{esc(_rel_display(it["path"]))}</a>'
                       f'<button class="copybtn" type="button" data-copy="{esc(path_abs)}">copy path</button></div>')
        cards.append(f'<div class="asset">{role}<h3>{esc(it.get("title"))}</h3>{thumb}{note}{pathrow}</div>')
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag") or "THE RAIL")}'
            f'<div class="assetgrid">{"".join(cards)}</div></section>')


def render_timeline(num, s):
    items = []
    for it in s.get("items", []):
        done = " done" if it.get("done") else ""
        date = f'<span class="date">{esc(it.get("date"))}</span>' if it.get("date") else ""
        body = f"<p>{esc(it.get('body'))}</p>" if it.get("body") else ""
        items.append(f'<div class="tl-item{done}">{date}<h3>{esc(it.get("title"))}</h3>{body}</div>')
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag"))}'
            f'<div class="timeline">{"".join(items)}</div></section>')


def render_flow(num, s):
    parts = []
    steps = s.get("steps", [])
    for i, st in enumerate(steps, 1):
        note = f"<p>{esc(st.get('note'))}</p>" if st.get("note") else ""
        parts.append(f'<div class="step"><span class="n">{i:02d}</span><h3>{esc(st.get("title"))}</h3>{note}</div>')
        if i < len(steps):
            parts.append('<span class="arrow">→</span>')
    caption = f'<div class="bars-caption">{esc(s.get("caption"))}</div>' if s.get("caption") else ""
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag"))}'
            f'<div class="flow">{"".join(parts)}</div>{caption}</section>')


def render_stats(num, s):
    tiles = []
    for it in s.get("items", []):
        unit = f"<small> {esc(it['unit'])}</small>" if it.get("unit") else ""
        note = f'<div class="note">{esc(it.get("note"))}</div>' if it.get("note") else ""
        tiles.append(f'<div class="stat"><div class="num">{esc(it.get("value"))}{unit}</div>'
                     f'<span class="lab">{esc(it.get("label"))}</span>{note}</div>')
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag"))}'
            f'<div class="stats">{"".join(tiles)}</div></section>')


def _spark_svg(values):
    """Inline sparkline SVG for one series. Returns "" when there's nothing to draw.

    Non-uniform scaling (preserveAspectRatio=none) lets the chart fill its box at
    any width; vector-effect keeps the strokes 1px instead of stretching with it.
    That rules out circles as markers — a scaled circle becomes an ellipse — so
    "you are here" is a vertical hairline, which survives the same transform.
    """
    vals = [float(v) for v in values if isinstance(v, (int, float))]
    if len(vals) < 2:
        return ""
    W, H, PAD = 100.0, 30.0, 3.0
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1.0
    step = W / (len(vals) - 1)

    def xy(i, v):
        x = i * step
        # Flat series (hi == lo) draws down the middle rather than pinned to an edge.
        y = H / 2 if hi == lo else (H - PAD) - ((v - lo) / span) * (H - 2 * PAD)
        return f"{x:.2f},{y:.2f}"

    pts = " ".join(xy(i, v) for i, v in enumerate(vals))
    first_x, last_x = 0.0, (len(vals) - 1) * step
    area = f"M0,{H:.2f} L" + " L".join(pts.split(" ")) + f" L{last_x:.2f},{H:.2f} Z"
    return (
        f'<svg class="sparksvg" viewBox="0 0 {W:.0f} {H:.0f}" preserveAspectRatio="none" '
        f'aria-hidden="true" focusable="false">'
        f'<path class="sparkarea" d="{area}"/>'
        f'<polyline class="sparkline" points="{pts}" vector-effect="non-scaling-stroke"/>'
        f'<line class="sparknow" x1="{last_x:.2f}" y1="0" x2="{last_x:.2f}" y2="{H:.0f}" '
        f'vector-effect="non-scaling-stroke"/>'
        f'<line class="sparkbase" x1="{first_x:.2f}" y1="{H:.0f}" x2="{last_x:.2f}" y2="{H:.0f}" '
        f'vector-effect="non-scaling-stroke"/>'
        f"</svg>"
    )


def render_spark(num, s):
    """Momentum row: label · sparkline · current value. One card per series.

    Each series is scaled to its OWN range — a sparkline answers "what shape is
    this trend", not "how does it compare to that one" (that's what `bars` is for
    with its shared scale). A series that can't be drawn degrades to its value
    alone rather than printing an empty box.
    """
    cards = []
    for x in s.get("series", []):
        svg = _spark_svg(x.get("values") or [])
        value = x.get("value")
        val_html = ""
        if value is not None and str(value) != "":
            unit = f"<small> {esc(x['unit'])}</small>" if x.get("unit") else ""
            val_html = f'<div class="sparkval">{esc(value)}{unit}</div>'
        note = f'<span class="sparknote">{esc(x.get("note"))}</span>' if x.get("note") else ""
        cards.append(
            f'<div class="sparkcard"><div class="sparkhead">'
            f'<span class="sparklab">{esc(x.get("label"))}</span>{note}</div>'
            f'<div class="sparkplot">{svg}</div>{val_html}</div>'
        )
    if not cards:
        return ""
    caption = f'<div class="bars-caption">{esc(s.get("caption"))}</div>' if s.get("caption") else ""
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag"))}'
            f'<div class="spark">{"".join(cards)}</div>{caption}</section>')


PROGRESS_STATES = {"done", "current", "todo", "blocked"}


def render_progress(num, s):
    """Segmented stage bar — where a thing sits in its own lifecycle.

    Stages are ordered and named by the caller, so this works for a mission
    (research → shipped → outcome) or any other pipeline without the renderer
    knowing the vocabulary.
    """
    stages = s.get("stages") or []
    if not stages:
        return ""
    segs, labs = [], []
    for st in stages:
        state = str(st.get("state") or "todo").lower()
        if state not in PROGRESS_STATES:
            state = "todo"
        segs.append(f'<i class="pseg {state}"></i>')
        mark = '<span class="pdot"></span>' if state == "current" else ""
        note = f'<span class="pnote">{esc(st.get("note"))}</span>' if st.get("note") else ""
        labs.append(f'<div class="plab {state}">{mark}<span>{esc(st.get("label"))}</span>{note}</div>')
    note = f'<div class="bars-caption">{esc(s.get("note"))}</div>' if s.get("note") else ""
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag"))}'
            f'<div class="progress"><div class="ptrack">{"".join(segs)}</div>'
            f'<div class="plabs">{"".join(labs)}</div></div>{note}</section>')


def render_matrix(num, s):
    axes = ""
    if s.get("axes"):
        axes = f'<div class="matrix-axes">{esc(s["axes"].get("y") or "")} · {esc(s["axes"].get("x") or "")}</div>'
    quads = []
    for q in (s.get("quads") or [])[:4]:
        lis = []
        for i in q.get("items", []):
            note = f"<small>{esc(i.get('note'))}</small>" if i.get("note") else ""
            lis.append(f"<li>{esc(i.get('name'))}{note}</li>")
        quads.append(f'<div class="quad"><span class="qlab">{esc(q.get("label"))}</span><ul>{"".join(lis)}</ul></div>')
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag"))}'
            f'{axes}<div class="matrix">{"".join(quads)}</div></section>')


def render_related(num, s):
    links = []
    for l in s.get("links", []):
        if SHARE and not _is_url(l.get("href") or ""):
            continue  # file-path swings are internal-only
        href = l.get("href") or (_file_href(l["path"]) if l.get("path") else "#")
        ext = ' target="_blank" rel="noopener"' if _is_url(l.get("href") or "") else ""
        links.append(f'<a href="{esc(href)}"{ext}><span class="k">{esc(l.get("k") or "LINK")}</span>'
                     f'<span class="t">{esc(l.get("title"))}</span></a>')
    if not links:
        return ""
    return (f'<section class="blk" id="{anchor(s["heading"])}">{sec_head(num, s["heading"], s.get("tag") or "CONNECTED")}'
            f'<div class="swing">{"".join(links)}</div></section>')


RENDERERS = {
    "summary": render_summary,
    "prose": render_prose,
    "evidence": render_evidence,
    "bars": render_bars,
    "decision": render_decision,
    "deploy": render_deploy,
    "caveats": render_caveats,
    "playbook": render_playbook,
    "assets": render_assets,
    "timeline": render_timeline,
    "flow": render_flow,
    "stats": render_stats,
    "spark": render_spark,
    "progress": render_progress,
    "matrix": render_matrix,
    "related": render_related,
}


def render_ledger(num, brief):
    rows = brief.get("ledger", [])
    if not rows:
        return ""
    cost = brief.get("run_cost_usd")
    stack = brief.get("stack")
    meta_bits = []
    if not SHARE:
        if cost is not None:
            meta_bits.append(f"run cost ${float(cost):.2f}")
        if stack:
            meta_bits.append("stack: " + " · ".join(str(x) for x in stack))
    tag = " — ".join(meta_bits) if meta_bits else None
    body_rows = []
    for i, r in enumerate(rows):
        if r.get("url") and not (SHARE and str(r["url"]).startswith("file://")):
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


def build_context_pack(brief):
    """Collect every file path + source URL the brief references, with roles.

    This is the agent-feed manifest: hand it (or <slug>-context.json) to any
    agent/LLM and it knows exactly which documents ground this brief.
    """
    paths, urls, seen_p, seen_u = [], [], set(), set()

    def add_path(p, role):
        p = str(p or "").strip()
        if not p:
            return
        if p.startswith("file://"):
            p = urllib.parse.unquote(p[len("file://"):])
        ap = Path(p)
        if not ap.is_absolute():
            ap = ROOT / p
        key = str(ap)
        if key in seen_p:
            return
        seen_p.add(key)
        paths.append({"path": _rel_display(str(ap)), "abs": str(ap), "role": role})

    def add_url(u, label):
        u = str(u or "").strip()
        if not u:
            return
        if u.startswith("file://"):
            add_path(u, label)
            return
        if not _is_url(u) or u in seen_u:
            return
        seen_u.add(u)
        urls.append({"url": u, "label": label})

    for extra in brief.get("context", []):
        add_path(extra.get("path"), extra.get("role") or "context")
    for s in brief.get("sections", []):
        kind = s.get("kind")
        if kind == "evidence":
            for r in s.get("rows", []):
                add_url(r.get("source_url"), r.get("source_label") or "evidence source")
        elif kind == "playbook":
            for p in s.get("plays", []):
                for t in p.get("touches", []):
                    add_path(t, f"playbook · {p.get('title') or 'play'}")
        elif kind == "assets":
            for it in s.get("items", []):
                add_path(it.get("path"), f"asset · {it.get('role') or 'asset'}")
        elif kind == "related":
            for l in s.get("links", []):
                if l.get("path"):
                    add_path(l["path"], f"related · {l.get('k') or 'link'}")
                add_url(l.get("href"), l.get("title") or "related")
    for r in brief.get("ledger", []):
        add_url(r.get("url"), r.get("source") or "ledger source")

    slug = brief.get("slug") or "brief"
    return {
        "slug": slug,
        "title": _plain(brief.get("title")),
        "compiled": brief.get("compiled"),
        "generated_by": "execution/render_brief.py",
        "brief_html": f"deliverables/research-briefs/{slug}/{slug}-brief.html",
        "brief_md": f"deliverables/research-briefs/{slug}/{slug}-brief.md",
        "paths": paths,
        "urls": urls,
    }


def render_context_pack(num, pack):
    if not pack["paths"] and not pack["urls"]:
        return ""
    rows = []
    for i, p in enumerate(pack["paths"], 1):
        rows.append(f'<tr><td>{i:02d}</td><td><a href="{esc(Path(p["abs"]).as_uri())}">{esc(p["path"])}</a></td>'
                    f'<td>{esc(p["role"])}</td></tr>')
    off = len(pack["paths"])
    for i, u in enumerate(pack["urls"], 1):
        rows.append(f'<tr><td>{off + i:02d}</td><td><a href="{esc(u["url"])}" target="_blank" rel="noopener">'
                    f'{esc(u["url"])}</a></td><td>{esc(u["label"])}</td></tr>')
    pack_json = json.dumps(pack, indent=2, ensure_ascii=False)
    return (f'<section class="blk" id="context-pack">{sec_head(num, "context pack", "AGENT FEED")}'
            '<p>every document and source this brief stands on — feed the block below (or the '
            '<span style="font-family:var(--mono);font-size:12px">-context.json</span> beside this file) '
            "to any agent and it has the full grounding instantly.</p>"
            '<table class="ledger" style="margin-top:14px"><thead><tr><th>#</th><th>Path / URL</th><th>Role</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table>'
            '<div class="deploy"><div class="bar"><span class="k">agent context pack · json</span>'
            '<button class="copybtn" type="button">copy</button></div>'
            f"<pre>{esc(pack_json)}</pre></div></section>")


def build_nav(brief, has_pack=False):
    links = []
    for s in brief.get("sections", []):
        if SHARE and s.get("kind") == "related" and not any(_is_url(l.get("href") or "") for l in s.get("links", [])):
            continue  # section is dropped entirely in share mode
        if s.get("heading"):
            plain = re.sub(r"\*", "", s["heading"])
            links.append(f'<a href="#{anchor(s["heading"])}">{esc(plain)}</a>')
    if brief.get("ledger"):
        links.append('<a href="#source-ledger">sources</a>')
    if has_pack:
        links.append('<a href="#context-pack">context pack</a>')
    return "".join(links)


def render(brief, share=False, pagepack=None):
    """Render the brief HTML. share=True strips internals (safe to send outward);
    pagepack embeds {path, brief} for the page-level path / copy-brief buttons."""
    global SHARE
    SHARE = share
    try:
        tpl = TEMPLATE.read_text(encoding="utf-8")
        sections_html, n = [], 0
        for s in brief.get("sections", []):
            kind = s.get("kind")
            if kind not in RENDERERS:
                raise SystemExit(f"unknown section kind: {kind!r}")
            n += 1
            html_out = RENDERERS[kind](n, s)
            if not html_out:
                n -= 1  # section dropped entirely (e.g. related in share mode)
                continue
            sections_html.append(html_out)
        ledger_html = render_ledger(n + 1, brief)
        if ledger_html:
            n += 1
            sections_html.append(ledger_html)
        pack_html = ""
        if not share:
            pack = build_context_pack(brief)
            pack_html = render_context_pack(n + 1, pack)
            if pack_html:
                sections_html.append(pack_html)
        navtools, pagepack_html = "", ""
        if pagepack and not share:
            navtools = ('<span class="navtool" data-act="path" title="copy the .md path — for Codex / Claude Code / any tool with file access">path</span>'
                        '<span class="navtool cp" data-act="brief" title="copy the full brief inline — paste into any AI chat">copy brief</span>')
            pp_json = json.dumps(pagepack, ensure_ascii=False).replace("</", "<\\/")
            pagepack_html = f'<script id="pagepack" type="application/json">{pp_json}</script>'
        title_plain = re.sub(r"\*", "", brief.get("title", "untitled"))
        subs = {
            "{{TITLE_PLAIN}}": esc(title_plain),
            "{{NAV}}": build_nav(brief, has_pack=bool(pack_html)),
            "{{NAVTOOLS}}": navtools,
            "{{PAGEPACK}}": pagepack_html,
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
            # Lets a SERVED page map its own file:// links back to /repo/ routes.
            # Empty in share mode: an outward copy must carry no local paths.
            "{{REPO_ROOT}}": "" if share else esc(str(ROOT)),
        }
        for k, v in subs.items():
            tpl = tpl.replace(k, v)
        return tpl
    finally:
        SHARE = False


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
        elif kind == "playbook":
            for i, p in enumerate(s.get("plays", []), 1):
                intent = f" — {p.get('intent')}" if p.get("intent") else ""
                out.append(f"{i}. **{p.get('title')}**{intent}")
                if p.get("command"):
                    out += ["```", str(p["command"]), "```"]
                if p.get("touches"):
                    out.append("   touches: " + " · ".join(_rel_display(t) for t in p["touches"]))
                if p.get("receipt"):
                    out.append(f"   receipt: {p['receipt']}")
        elif kind == "assets":
            for it in s.get("items", []):
                note = f" — {it.get('note')}" if it.get("note") else ""
                out.append(f"- **{it.get('title')}** [{it.get('role') or 'ASSET'}] `{_rel_display(it.get('path'))}`{note}")
        elif kind == "timeline":
            for it in s.get("items", []):
                body = f" — {it.get('body')}" if it.get("body") else ""
                out.append(f"- {it.get('date', '')} · **{it.get('title')}**{body}")
        elif kind == "flow":
            out.append(" → ".join(str(st.get("title")) for st in s.get("steps", [])))
            for st in s.get("steps", []):
                if st.get("note"):
                    out.append(f"  - {st.get('title')}: {st['note']}")
        elif kind == "stats":
            for it in s.get("items", []):
                unit = f" {it.get('unit')}" if it.get("unit") else ""
                note = f" ({it.get('note')})" if it.get("note") else ""
                out.append(f"- {it.get('label')}: **{it.get('value')}{unit}**{note}")
        elif kind == "matrix":
            for q in s.get("quads", []):
                names = ", ".join(
                    str(i.get("name")) + (f" ({i.get('note')})" if i.get("note") else "")
                    for i in q.get("items", [])
                )
                out.append(f"- **{q.get('label')}**: {names}")
        elif kind == "related":
            for l in s.get("links", []):
                ref = l.get("href") or _rel_display(l.get("path"))
                out.append(f"- [{l.get('k') or 'LINK'}] {l.get('title')} — {ref}")
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
    pack = build_context_pack(brief)
    if pack["paths"] or pack["urls"]:
        out += ["", "## Context pack (agent feed)"]
        for p in pack["paths"]:
            out.append(f"- `{p['path']}` — {p['role']}")
        for u in pack["urls"]:
            out.append(f"- {u['url']} — {u['label']}")
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


def write_brief(brief, out_root=None, share=False, src_json=None):
    """Render a brief dict to disk and return the paths written.

    `render()` is a pure function that returns HTML; the file layout used to live
    only inside main(), so every non-CLI caller either reimplemented it or
    silently wrote nothing. One layout, one owner.

    Returns {"dir","html","md","json","context","share"} — values are Paths, and
    "context"/"share" are None when not written.
    """
    slug = brief.get("slug") or "brief"
    out_dir = (Path(out_root) if out_root else DEFAULT_OUT) / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    out_html = out_dir / f"{slug}-brief.html"
    out_md = out_dir / f"{slug}-brief.md"
    out_json = out_dir / f"{slug}-brief.json"

    md = render_markdown(brief)
    pp_header = (f"SOURCE: {out_md}  (research brief · Antigravity)\n"
                 f"HTML: {out_html}\nCONTEXT PACK: {out_dir / (slug + '-context.json')}\n"
                 f"COMPILED: {brief.get('compiled') or '—'}\n\n")
    out_html.write_text(render(brief, pagepack={"path": str(out_md), "brief": pp_header + md}),
                        encoding="utf-8")
    out_md.write_text(md, encoding="utf-8")

    # Provenance copy. A generated brief (front door, mission sweep) has no
    # source file on disk, so the dict itself is the record — and preserving an
    # existing `status` keeps the librarian's archive flip from being undone on
    # every re-render, which is what makes a LIVING brief safe to regenerate.
    if src_json and Path(src_json).resolve() == out_json.resolve():
        pass
    elif src_json:
        shutil.copyfile(src_json, out_json)
    else:
        prior = {}
        if out_json.exists():
            try:
                prior = json.loads(out_json.read_text(encoding="utf-8"))
            except ValueError:
                prior = {}
        if prior.get("status") and "status" not in brief:
            brief = dict(brief, status=prior["status"])
        out_json.write_text(json.dumps(brief, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    ctx_path = None
    pack = build_context_pack(brief)
    if pack["paths"] or pack["urls"]:
        ctx_path = out_dir / f"{slug}-context.json"
        ctx_path.write_text(json.dumps(pack, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    share_path = None
    if share:
        share_path = out_dir / f"{slug}-brief-share.html"
        share_path.write_text(render(brief, share=True), encoding="utf-8")

    return {"dir": out_dir, "html": out_html, "md": out_md, "json": out_json,
            "context": ctx_path, "share": share_path}


def main():
    ap = argparse.ArgumentParser(description="Render a research-brief JSON to house-style HTML.")
    ap.add_argument("brief_json")
    ap.add_argument("--out-dir", default=None, help="override output root (default deliverables/research-briefs)")
    ap.add_argument("--open", action="store_true", help="open the rendered brief in the default browser")
    ap.add_argument("--gdoc", action="store_true",
                    help="also export as a native Google Doc via gws (graceful skip on auth failure)")
    ap.add_argument("--share", action="store_true",
                    help="also render <slug>-brief-share.html with internals stripped (safe to send outward)")
    ap.add_argument("--no-index", action="store_true",
                    help="skip the automatic Briefing Room index refresh")
    args = ap.parse_args()

    src = Path(args.brief_json)
    brief = json.loads(src.read_text(encoding="utf-8"))
    slug = brief.get("slug") or src.stem
    out_root = Path(args.out_dir) if args.out_dir else DEFAULT_OUT
    paths = write_brief(brief, out_root=out_root, share=args.share, src_json=src)
    out_dir, out_html, out_md, out_json = paths["dir"], paths["html"], paths["md"], paths["json"]

    gdoc_url = export_gdoc(out_html, _plain(brief.get("title") or slug)) if args.gdoc else None
    if gdoc_url:
        brief["gdoc_url"] = gdoc_url
        out_json.write_text(json.dumps(brief, indent=2, ensure_ascii=False), encoding="utf-8")
        out_md.write_text(render_markdown(brief) + f"\n_Google Doc: {gdoc_url}_\n", encoding="utf-8")

    if paths["context"]:
        print(f"[render_brief] ctx → {paths['context']}")
    if paths["share"]:
        print(f"[render_brief] share → {paths['share']}  (internals stripped — the only client-visible form)")

    print(f"[render_brief] OK → {out_html}")
    print(f"[render_brief] md → {out_md}")
    if gdoc_url:
        print(f"[render_brief] gdoc → {gdoc_url}")

    # Keep the Briefing Room current on EVERY render, no matter the caller
    # (launchd loops, workflows, hand runs). Graceful: the brief never blocks on it.
    if not args.no_index:
        try:
            r = subprocess.run([sys.executable, str(ROOT / "execution" / "brief_library.py")],
                               capture_output=True, text=True, timeout=60)
            if r.returncode == 0:
                print(f"[render_brief] index → {(r.stdout or '').strip() or 'briefing room refreshed'}")
            else:
                print(f"[render_brief] WARN index refresh failed (brief still rendered): {r.stderr.strip()[:160]}")
        except Exception as e:
            print(f"[render_brief] WARN index refresh failed (brief still rendered): {e}")

    if args.open:
        subprocess.run(["open", str(out_html)], check=False)


if __name__ == "__main__":
    main()
