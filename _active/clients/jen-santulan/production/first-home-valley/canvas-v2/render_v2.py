#!/usr/bin/env python3
"""Render the v2 artboards to 1080x1350 PNGs (2x) for review and phone hand-off."""
import glob, json, os, pathlib, shutil, subprocess

HERE = pathlib.Path(__file__).parent
OUT = HERE / "png"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]


def slug(t):
    return (t.lower().replace(" · ", "-").replace(" ", "-")
            .replace("→", "to").replace("%", "pct"))


def main():
    cv = json.load(open(HERE / "canvas.json"))
    OUT.mkdir(exist_ok=True)
    tmp = HERE / ".tmp"
    tmp.mkdir(exist_ok=True)
    for i, a in enumerate(cv["artboards"], 1):
        html = (HERE / a["file"]).read_text()
        html = html.replace('<script src="./support.js"></script>', "")
        for tag in ("<x-dc>", "</x-dc>", "<helmet>", "</helmet>"):
            html = html.replace(tag, "")
        shim = tmp / ("%02d.html" % i)
        shim.write_text(html)
        png = OUT / ("%02d-%s.png" % (i, slug(a["title"])))
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=2",
                        "--window-size=%d,%d" % (a["w"], a["h"]),
                        "--virtual-time-budget=6000",
                        "--screenshot=%s" % png, "file://%s" % shim],
                       check=True, capture_output=True)
        print("  %-34s %5d KB" % (png.name, png.stat().st_size // 1024))
    shutil.rmtree(tmp)
    print("\n%d PNGs -> %s" % (len(cv["artboards"]), OUT))


if __name__ == "__main__":
    main()
