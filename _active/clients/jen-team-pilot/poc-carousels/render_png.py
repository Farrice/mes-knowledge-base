#!/usr/bin/env python3
"""Render the 12 carousel artboards to 1080x1350 PNGs for phone hand-off.
Uses the chrome-headless-shell already on disk (playwright cache). No network deps beyond Google Fonts."""
import json, pathlib, subprocess, shutil, sys, os, glob

HERE = pathlib.Path(__file__).parent
OUT = HERE / "png"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]

ORDER = [
    ("Main.dc.html",    "jen-buyers-01"),
    ("Buyer2.dc.html",  "jen-buyers-02"),
    ("Buyer3.dc.html",  "jen-buyers-03"),
    ("Buyer4.dc.html",  "jen-buyers-04"),
    ("Buyer5.dc.html",  "jen-buyers-05"),
    ("Buyer6.dc.html",  "jen-buyers-06"),
    ("Seller1.dc.html", "jen-sellers-01"),
    ("Seller2.dc.html", "jen-sellers-02"),
    ("Seller3.dc.html", "jen-sellers-03"),
    ("Seller4.dc.html", "jen-sellers-04"),
    ("Seller5.dc.html", "jen-sellers-05"),
    ("Seller6.dc.html", "jen-sellers-06"),
]

def main():
    OUT.mkdir(exist_ok=True)
    tmp = HERE / ".render_tmp"
    tmp.mkdir(exist_ok=True)
    for src, name in ORDER:
        html = (HERE / src).read_text()
        # strip the canvas runtime script (not present locally) and unwrap the custom elements
        html = html.replace('<script src="./support.js"></script>', "")
        html = html.replace("<x-dc>", "").replace("</x-dc>", "")
        html = html.replace("<helmet>", "").replace("</helmet>", "")
        shim = (HERE / ".render_tmp" / f"{name}.html")
        shim.write_text(html)
        png = OUT / f"{name}.png"
        subprocess.run([
            CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=2",
            "--window-size=1080,1350",
            "--virtual-time-budget=4000",
            f"--screenshot={png}", f"file://{shim}",
        ], check=True, capture_output=True)
        print(f"  {name}.png  ({png.stat().st_size//1024} KB)")
    shutil.rmtree(tmp)
    print(f"\n12 PNGs -> {OUT}")

if __name__ == "__main__":
    main()
