#!/usr/bin/env python3
"""One contact sheet of every rendered slide, one carousel per row — look at the grid, not the source."""
import glob, json, os, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).parent
# Optional args: spec path, batch dir, review dir
SPEC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "slides.json"
BATCH = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "CAROUSEL-BATCH"
OUT = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else HERE / "review"
OUT.mkdir(parents=True, exist_ok=True)
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]

spec = json.load(open(SPEC))
W = 216  # thumb width (1080/5)
rows = ""
maxcols = max(len(c["slides"]) for c in spec["carousels"])
for car in spec["carousels"]:
    cells = "".join(f'<div><img src="{os.path.relpath((BATCH / car["slug"] / f"{i:02d}.png").resolve(), OUT.resolve())}" style="width:{W}px;display:block"></div>'
                    for i in range(1, len(car["slides"]) + 1))
    rows += (f'<div style="margin-bottom:22px"><div style="font:600 13px Helvetica;margin:0 0 6px;color:#333">{car["slug"]} — {car["title"]}</div>'
             f'<div style="display:flex;gap:8px">{cells}</div></div>')
page_w = maxcols * (W + 8) + 40
html = f'<html><body style="margin:0;padding:20px;background:#e9e6df;width:{page_w}px">{rows}</body></html>'
(OUT / "sheet.html").write_text(html)
h = 20 + sum(int(W * 1.25) + 22 + 20 for _ in spec["carousels"]) + 40
subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                f"--window-size={page_w},{h}", "--virtual-time-budget=6000",
                f"--screenshot={(OUT / 'sheet.png').resolve()}", (OUT / 'sheet.html').resolve().as_uri()], check=True, capture_output=True)
print("review/sheet.png", (OUT / "sheet.png").stat().st_size // 1024, "KB")
