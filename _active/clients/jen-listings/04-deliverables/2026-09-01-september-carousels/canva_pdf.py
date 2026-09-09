#!/usr/bin/env python3
"""Vector PDFs for Canva import: one PDF per carousel (7 pages) and one for the presentation (8 pages).
Text stays text (Canva makes it editable), photos ride along, line art stays vector.
Output: canva/*.pdf. Uses the headless Chrome already on disk."""
import base64, glob, os, pathlib, re, subprocess

HERE = pathlib.Path(__file__).parent
OUTD = HERE / "canva"
OUTD.mkdir(exist_ok=True)
IMG = HERE / "img"
CHROME = sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Overpass:wght@400;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap">'

def inline_images(html):
    def repl(m):
        p = IMG / m.group(1)
        return f'src="data:image/jpeg;base64,{base64.b64encode(p.read_bytes()).decode()}"' if p.exists() else m.group(0)
    return re.sub(r'src="([A-Za-z0-9._-]+\.jpg)"', repl, html)

def body_of(stem):
    src = (HERE / f"{stem}.dc.html").read_text()
    return inline_images(re.search(r"</helmet>\s*(.*?)\s*</x-dc>", src, re.S).group(1))

def build(name, stems):
    pages = "".join(f'<div style="width:1080px;height:1350px;overflow:hidden;position:relative;page-break-after:always;break-after:page;">{body_of(s)}</div>' for s in stems)
    html = (f"<!doctype html><html><head><meta charset='utf-8'>{FONTS}<style>@page{{size:1080px 1350px;margin:0}}"
            "html,body{margin:0;padding:0;background:#F7F5F2;font-family:Figtree,'Avenir Next',sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}"
            f"</style></head><body>{pages}</body></html>")
    src = OUTD / f"{name}.html"
    src.write_text(html)
    pdf = OUTD / f"{name}.pdf"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=6000",
                    f"--print-to-pdf={pdf}", f"file://{src}"], check=True, capture_output=True)
    print(f"{pdf.name}: {len(stems)} pages, {pdf.stat().st_size // 1024} KB")

build("jen-condo-carousel", [f"DD{i}" for i in range(1, 8)])
build("jen-rail-carousel", [f"DR{i}" for i in range(1, 8)])
build("jen-insurance-carousel", [f"DI{i}" for i in range(1, 8)])
build("jen-september-presentation", [f"S{i}" for i in range(1, 17)] + ["DM"])
