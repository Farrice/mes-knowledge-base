#!/usr/bin/env python3
"""Render canvas/*.dc.html to 1080x1350 PNGs in CAROUSEL-BATCH/<slug>/NN.png (1x, phone-ready)."""
import glob, json, os, pathlib, shutil, subprocess, sys

HERE = pathlib.Path(__file__).parent
# Optional args: spec path, canvas dir, output dir
SPEC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "slides.json"
CANVAS = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "canvas"
OUT = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else HERE / "CAROUSEL-BATCH"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]


def main():
    spec = json.load(open(SPEC))
    tmp = HERE / ".render_tmp"
    if tmp.exists():
        shutil.rmtree(tmp)
    (tmp / "assets").mkdir(parents=True)
    # artboards reference ../assets/...; mirror that layout under tmp
    shutil.copytree(HERE / "assets", tmp / "assets", dirs_exist_ok=True)
    (tmp / "canvas").mkdir()
    n = 0
    for car in spec["carousels"]:
        d = OUT / car["slug"]
        d.mkdir(parents=True, exist_ok=True)
        for i in range(1, len(car["slides"]) + 1):
            src = CANVAS / f'{car["slug"]}-{i:02d}.dc.html'
            html = src.read_text().replace('<script src="./support.js"></script>', "")
            for tag in ("<x-dc>", "</x-dc>", "<helmet>", "</helmet>"):
                html = html.replace(tag, "")
            shim = tmp / "canvas" / src.name.replace(".dc.html", ".html")
            shim.write_text(html)
            png = d / f"{i:02d}.png"
            subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                            "--force-device-scale-factor=1", "--window-size=1080,1350",
                            "--virtual-time-budget=5000", f"--screenshot={png}", f"file://{shim}"],
                           check=True, capture_output=True)
            n += 1
        print(f"  {car['slug']}: {len(car['slides'])} slides")
    shutil.rmtree(tmp)
    print(f"{n} PNGs -> {OUT}")


if __name__ == "__main__":
    main()
