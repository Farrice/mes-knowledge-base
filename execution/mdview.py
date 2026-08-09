#!/usr/bin/env python3
"""mdview — read ANY markdown file in the Premium Minimal brand, not raw source.

WHY (Farrice, 2026-08-08): he read repo markdown through a VS Code extension
(Office Viewer) that rendered tables and layout. In the desktop app, clicking a
.md shows raw `|---|---|` and it's unreadable. The READOUT OS already solved
this for *deliverables* (render_brief.py -> briefs) but nothing rendered the
other 4,000 files — CLAUDE.md, directives/, ledgers, solution cards.

This reuses the SAME shell as the research briefs (templates/research-brief/
template.html), so a directive and a client brief wear one typeface. Extend,
never rebuild.

Usage:
    python3 execution/mdview.py CLAUDE.md                 # render + open
    python3 execution/mdview.py directives/*.md           # many at once
    python3 execution/mdview.py PROJECTS.md --no-open     # just write the html
"""
from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "research-brief" / "template.html"
OUTDIR = ROOT / ".agent" / "mdview"

sys.path.insert(0, str(ROOT / "execution"))
from degrade import degraded  # noqa: E402

# Generic-markdown styling layered ON TOP of the brief shell. The shell styles
# structured sections (h2.sec, table.ledger); plain markdown emits bare tags, so
# these rules give them the same voice without touching the shared template.
EXTRA_CSS = """
<style>
  .mdbody{ margin-top:56px }
  .mdbody h1{ font-size:31px; letter-spacing:-.02em; font-weight:700; margin:52px 0 14px }
  .mdbody h2{ font-size:25px; letter-spacing:-.015em; font-weight:700; margin:46px 0 12px;
    padding-bottom:9px; border-bottom:1px solid var(--ag-rule) }
  .mdbody h3{ font-size:18px; font-weight:650; margin:32px 0 9px }
  .mdbody h4{ font-size:14px; font-weight:650; margin:24px 0 7px; color:var(--ag-muted);
    font-family:var(--mono); letter-spacing:.05em; text-transform:uppercase }
  .mdbody p{ margin:0 0 15px; line-height:1.72 }
  .mdbody ul,.mdbody ol{ margin:0 0 16px; padding-left:22px; line-height:1.72 }
  .mdbody li{ margin-bottom:6px }
  .mdbody li::marker{ color:var(--ag-accent) }
  .mdbody a{ color:var(--ag-accent); text-underline-offset:2px }
  .mdbody code{ font-family:var(--mono); font-size:12.5px; background:var(--ag-rule);
    padding:1.5px 5px; border-radius:3px; word-break:break-word }
  .mdbody pre{ background:var(--ag-rule); border-radius:6px; padding:15px 17px; overflow-x:auto;
    margin:0 0 18px }
  .mdbody pre code{ background:none; padding:0; font-size:12px; line-height:1.65 }
  .mdbody blockquote{ margin:0 0 18px; padding:3px 0 3px 18px;
    border-left:3px solid var(--ag-accent); color:var(--ag-muted) }
  .mdbody table{ width:100%; border-collapse:collapse; margin:0 0 22px; font-size:14px;
    display:block; overflow-x:auto }
  .mdbody thead th{ text-align:left; font-family:var(--mono); font-size:11px;
    letter-spacing:.09em; text-transform:uppercase; color:var(--ag-muted);
    border-bottom:1.5px solid var(--ag-ink); padding:9px 12px 9px 0; white-space:nowrap }
  .mdbody tbody td{ padding:10px 12px 10px 0; border-bottom:1px solid var(--ag-rule);
    vertical-align:top; line-height:1.6 }
  .mdbody tbody tr:hover{ background:var(--ag-rule) }
  .mdbody hr{ border:0; border-top:1px solid var(--ag-rule); margin:38px 0 }
  .mdbody img{ max-width:100%; height:auto; border-radius:4px }
</style>
"""


def _reexec_in_venv() -> None:
    """Find the interpreter that HAS markdown, instead of failing quietly.

    Scar (2026-08-08): the first version fell back to <pre>{raw}</pre> when the
    import failed. Run under system python3 — which is exactly what the README
    line said to do — it produced a page of raw markdown that LOOKED like a
    render bug rather than a missing dependency. A silent fallback is a failure
    wearing the costume of success. Never ship one.
    """
    venv = ROOT / ".venv" / "bin" / "python3"
    if venv.exists() and Path(sys.executable).resolve() != venv.resolve():
        import os
        os.execv(str(venv), [str(venv), str(Path(__file__).resolve()), *sys.argv[1:]])
    sys.exit(
        "mdview: the 'markdown' package is not importable and no usable .venv was found.\n"
        "  fix:  .venv/bin/python3 -m pip install markdown\n"
        "  (refusing to emit a raw-text page that would look like a rendering bug)"
    )


def _nav() -> str:
    """Shared home-base nav; degraded to empty ONLY with a visible ledger trail."""
    try:
        sys.path.insert(0, str(ROOT / "execution"))
        from surface_nav import nav_html
        return nav_html()
    except Exception as e:
        # DELIBERATE-QUIET: a nav bug must never block a doc render
        return degraded("", "surface_nav unavailable — mdview page renders without home-base nav", e)


def render_markdown(text: str) -> str:
    try:
        import markdown
    except ImportError:
        _reexec_in_venv()
    import markdown
    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists", "nl2br"],
        output_format="html5",
    )


def split_frontmatter(text: str) -> tuple[dict, str]:
    """YAML frontmatter becomes trust-strip metadata instead of noise at the top."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw, body = text[3:end], text[end + 4:]
    meta = {}
    for line in raw.splitlines():
        if ":" in line and not line.startswith((" ", "-", "#")):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body.lstrip("\n")


def first_heading(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def build(src: Path) -> Path:
    raw = src.read_text(encoding="utf-8", errors="replace")
    meta, body = split_frontmatter(raw)
    rel = src.resolve().relative_to(ROOT) if str(src.resolve()).startswith(str(ROOT)) else src
    title = meta.get("name") or first_heading(body, src.stem.replace("-", " ").title())
    dek = meta.get("description", "")
    stat = src.stat()

    tpl = TEMPLATE.read_text(encoding="utf-8")
    words = len(body.split())
    repl = {
        "TITLE_PLAIN": html.escape(title),
        "TITLE": html.escape(title),
        "CHIP": html.escape(str(rel.parent) if str(rel.parent) != "." else "repo root"),
        "DEK": html.escape(dek),
        "WINDOW": f"{words:,} words · ~{max(1, words // 220)} min",
        "LENS": html.escape(meta.get("type") or meta.get("status") or "source file"),
        "SOURCES": html.escape(src.name),
        "COMPILED": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
        # navttl + the SHARED home-base nav (2026-08-08): every rendered doc was
        # a cul-de-sac — the .brief-nav bar existed but carried only a filename.
        "NAV": f'<span class="navttl">{html.escape(str(rel))}</span>{_nav()}',
        "NAVTOOLS": "",
        "SECTIONS": f'<div class="mdbody">{render_markdown(body)}</div>',
        "FOOTER_LEFT": "ANTIGRAVITY · mdview",
        "FOOTER_RIGHT": html.escape(str(rel)),
        "REPO_ROOT": html.escape(str(ROOT)),
        "PAGEPACK": "",
    }
    out = tpl
    for k, v in repl.items():
        out = out.replace("{{" + k + "}}", v)
    out = out.replace("</head>", EXTRA_CSS + "</head>")

    OUTDIR.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^A-Za-z0-9]+", "-", str(rel)).strip("-").lower()
    dest = OUTDIR / f"{slug}.html"
    dest.write_text(out, encoding="utf-8")
    return dest


def build_index() -> Path:
    """.agent/mdview/index.html — every rendered doc, newest first.

    Without this, mdview was one-file-at-a-time: each page a cul-de-sac and no
    way to see what had been rendered. This is the 'docs' home base the shared
    nav (surface_nav.py) points at.
    """
    from surface_nav import nav_html
    rows = []
    for f in sorted(OUTDIR.glob("*.html"), key=lambda p: -p.stat().st_mtime):
        if f.name == "index.html" or f.name.startswith("_"):
            continue
        stamp = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        title = f.stem.replace("-", " ")
        rows.append(f'<a class="doc" href="{html.escape(f.as_uri())}">'
                    f'<span class="t">{html.escape(title)}</span>'
                    f'<span class="d">{stamp}</span></a>')
    body = "".join(rows) or '<p class="empty">nothing rendered yet — python3 execution/mdview.py &lt;file.md&gt;</p>'
    page = f"""<!doctype html><html><head><meta charset="utf-8">
<title>Rendered docs · Antigravity</title>
<style>
 body{{font-family:-apple-system,sans-serif;max-width:760px;margin:40px auto;padding:0 20px;
      background:#101014;color:#e8e6e1}}
 header{{display:flex;align-items:center;gap:14px;margin-bottom:28px}}
 h1{{font-size:22px;letter-spacing:-.01em;margin:0}}
 .doc{{display:flex;justify-content:space-between;gap:12px;padding:13px 4px;
      border-bottom:1px solid rgba(255,255,255,.08);text-decoration:none;color:inherit}}
 .doc:hover .t{{color:#7fb2d9}}
 .doc .d{{font-family:"SF Mono",Menlo,monospace;font-size:11px;opacity:.55;white-space:nowrap}}
 .empty{{opacity:.6}}
</style></head><body>
<header><h1>Rendered docs</h1>{nav_html(current="docs")}</header>
{body}
</body></html>"""
    OUTDIR.mkdir(parents=True, exist_ok=True)
    dest = OUTDIR / "index.html"
    dest.write_text(page, encoding="utf-8")
    return dest


def main() -> int:
    ap = argparse.ArgumentParser(description="Render markdown in the Premium Minimal brand.")
    ap.add_argument("files", nargs="*", help="markdown file(s)")
    ap.add_argument("--no-open", action="store_true", dest="no_open")
    ap.add_argument("--index", action="store_true", help="(re)build the docs index page")
    args = ap.parse_args()

    if args.index and not args.files:
        dest = build_index()
        print(dest)
        if not args.no_open:
            subprocess.run(["open", str(dest)], check=False)
        return 0
    if not args.files:
        ap.error("give me markdown file(s), or --index")

    built = []
    for f in args.files:
        p = Path(f)
        if not p.exists():
            print(f"skip (missing): {f}", file=sys.stderr)
            continue
        dest = build(p)
        built.append(dest)
        print(dest)

    if built:
        build_index()  # keep the docs home base current on every render
    if built and not args.no_open:
        subprocess.run(["open", *[str(b) for b in built]], check=False)
    return 0 if built else 1


if __name__ == "__main__":
    sys.exit(main())
