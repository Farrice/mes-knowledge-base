#!/usr/bin/env python3
"""Render the 21 September artboards to 1080x1350 PNGs (2x) for phone hand-off and fit checks.
Uses the chrome-headless-shell already on disk (playwright cache)."""
import glob, os, pathlib, shutil, subprocess

HERE = pathlib.Path(__file__).parent
OUT = HERE / "png"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]

ORDER = [("Main", "c1-01")] + [(f"C1S{i}", f"c1-0{i}") for i in range(2, 8)] \
    + [(f"C2S{i}", f"c2-0{i}") for i in range(1, 8)] \
    + [(f"C3S{i}", f"c3-0{i}") for i in range(1, 8)] \
    + [(f"DD{i}", f"dir-d-0{i}") for i in range(1, 8)] \
    + [("P0", "present-00-cover"), ("P1", "present-01-agenda"), ("R1", "present-reel-1"), ("R2", "present-reel-2"),
       ("R3", "present-reel-3"), ("R4", "present-reel-4"), ("P5", "present-05-your-words"),
       ("P2", "present-02-filming"), ("P3", "present-03-rulebook"), ("P4", "present-04-photos")]

def main():
    OUT.mkdir(exist_ok=True)
    tmp = HERE / ".render_tmp"
    tmp.mkdir(exist_ok=True)
    for img in (HERE / "img").glob("*.jpg"):
        shutil.copy(img, tmp / img.name)
    for stem, name in ORDER:
        html = (HERE / f"{stem}.dc.html").read_text()
        html = html.replace('<script src="./support.js"></script>', "")
        html = html.replace("<x-dc>", "").replace("</x-dc>", "")
        html = html.replace("<helmet>", "").replace("</helmet>", "")
        shim = tmp / f"{name}.html"
        shim.write_text(html)
        png = OUT / f"{name}.png"
        subprocess.run([
            CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1",
            "--window-size=1080,1350",
            "--virtual-time-budget=4000",
            f"--screenshot={png}", f"file://{shim}",
        ], check=True, capture_output=True)
        print(f"  {name}.png  ({png.stat().st_size // 1024} KB)")
    shutil.rmtree(tmp)
    print(f"\n{len(ORDER)} PNGs -> {OUT}")

if __name__ == "__main__":
    main()
