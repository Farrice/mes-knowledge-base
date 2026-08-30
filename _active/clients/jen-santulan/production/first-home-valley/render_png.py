#!/usr/bin/env python3
"""Render First Home Valley artboards -> 1080x1350 PNGs (2x) for phone hand-off."""
import json, pathlib, subprocess, shutil, os, glob
HERE = pathlib.Path(__file__).parent
SRC  = HERE / "canvas"
OUT  = HERE / "png"
CHROME = sorted(glob.glob(os.path.expanduser(
  "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]

def slug(t):
    return t.lower().replace(" · ", "-").replace(" ", "-").replace("→","to").replace("%","pct")

cv = json.load(open(SRC / "canvas.json"))
OUT.mkdir(exist_ok=True)
tmp = HERE / ".tmp"; tmp.mkdir(exist_ok=True)
for i, a in enumerate(cv["artboards"], 1):
    html = (SRC / a["file"]).read_text()
    html = html.replace('<script src="./support.js"></script>', "")
    for tag in ("<x-dc>", "</x-dc>", "<helmet>", "</helmet>"):
        html = html.replace(tag, "")
    shim = tmp / f"{i:02d}.html"; shim.write_text(html)
    name = f"{i:02d}-{slug(a['title'])}"
    png = OUT / f"{name}.png"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=2", f"--window-size={a['w']},{a['h']}",
        "--virtual-time-budget=4000", f"--screenshot={png}", f"file://{shim}"],
        check=True, capture_output=True)
    print(f"  {name}.png  ({a['w']}x{a['h']} @2x, {png.stat().st_size//1024} KB)")
shutil.rmtree(tmp)
print(f"\n{len(cv['artboards'])} PNGs -> {OUT}")
