#!/usr/bin/env python3
"""Build one self-contained HTML file for Canva's importer: every carousel slide is a page
(data-document-role="page"), images are inlined as base64, fonts come from Google Fonts.
Output: canva/jen-september-carousels.html (three carousels, 21 pages) and canva/jen-presentation.html (8 pages).
Canva needs a PUBLIC https URL to import; hosting is Farrice's call, never done here."""
import base64, pathlib, re

HERE = pathlib.Path(__file__).parent
OUTD = HERE / "canva"
OUTD.mkdir(exist_ok=True)
IMG = HERE / "img"

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Overpass:wght@400;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap">'

def inline_images(html):
    def repl(m):
        name = m.group(1)
        p = IMG / name
        if not p.exists():
            return m.group(0)
        b64 = base64.b64encode(p.read_bytes()).decode()
        return f'src="data:image/jpeg;base64,{b64}"'
    return re.sub(r'src="([A-Za-z0-9._-]+\.jpg)"', repl, html)

def page_body(stem):
    src = (HERE / f"{stem}.dc.html").read_text()
    m = re.search(r"</helmet>\s*(.*?)\s*</x-dc>", src, re.S)
    return inline_images(m.group(1))

def build(name, pages, title):
    parts = [f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title>{FONTS}"
             "<style>body{margin:0;background:#FFFFFF;font-family:Figtree,'Avenir Next',sans-serif;}"
             "[data-document-role=page]{width:1080px;height:1350px;overflow:hidden;position:relative;margin:0 0 40px;}</style></head><body>"]
    for stem, label in pages:
        parts.append(f'<div data-document-role="page" data-label="{label}">{page_body(stem)}</div>')
    parts.append("</body></html>")
    out = OUTD / name
    out.write_text("".join(parts))
    print(f"{name}: {len(pages)} pages, {out.stat().st_size // 1024} KB")

build("jen-september-carousels.html",
      [(f"DD{i}", f"condo · {i}") for i in range(1, 8)] + [(f"DR{i}", f"rail · {i}") for i in range(1, 8)] + [(f"DI{i}", f"insurance · {i}") for i in range(1, 8)],
      "Jen · September carousels")
build("jen-presentation.html",
      [(f"S{i}", f"presentation · {i}") for i in range(1, 8)] + [("DM", "saved DM reply")],
      "Jen · September presentation")
