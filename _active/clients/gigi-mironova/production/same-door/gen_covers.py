#!/usr/bin/env python3
"""Nine Instagram highlight covers, 1080x1080, uploadable as-is.

Soft-navy register per tokens.py. IG crops highlight covers to a circle, so everything
lives inside the centered disc; the word sits on one hairline ring."""
import glob
import os
import pathlib
import subprocess

import tokens as T

HERE = pathlib.Path(__file__).parent
OUT = HERE / "covers"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/"
    "chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]

WORDS = ["ESCROW?", "UNIT 124", "RESEDA", "LEASING", "BUYING",
         "РУССКИЙ", "REVIEWS", "TEAM", "GIGI"]
WORDS[0] = "THE DOCS"

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="%s">
<style>
body {{ margin:0; }}
.f {{ width:1080px; height:1080px; background:{band}; position:relative;
     font-family:'Manrope','Figtree',sans-serif; display:flex;
     align-items:center; justify-content:center; }}
.ring {{ position:absolute; width:640px; height:640px; border-radius:50%%;
        border:1px solid rgba(255,255,255,0.35); }}
.ring2 {{ position:absolute; width:840px; height:840px; border-radius:50%%;
         border:1px solid rgba(255,255,255,0.12); }}
.w {{ color:#FFFFFF; font-weight:600; letter-spacing:0.22em; font-size:{fs}px;
     text-transform:uppercase; text-align:center; z-index:1; }}
.dot {{ position:absolute; bottom:295px; width:5px; height:5px; border-radius:50%%;
       background:{accent}; }}
</style></head><body><div class="f">
<div class="ring2"></div><div class="ring"></div>
<div class="w">{word}</div><div class="dot"></div>
</div></body></html>"""


def main():
    OUT.mkdir(exist_ok=True)
    tmp = HERE / ".ctmp"
    tmp.mkdir(exist_ok=True)
    for i, w in enumerate(WORDS, 1):
        fs = 96 if len(w) <= 6 else 76
        html = (PAGE % T.FONTS).format(band=T.BAND, accent=T.ACCENT_LT, fs=fs, word=w)
        f = tmp / ("%d.html" % i)
        f.write_text(html)
        slug = w.lower().replace(" ", "-").replace("?", "")
        png = OUT / ("cover-%d-%s.png" % (i, slug))
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--window-size=1080,1080", "--virtual-time-budget=6000",
                        "--screenshot=%s" % png, "file://%s" % f],
                       check=True, capture_output=True)
        print(" ", png.name)
    import shutil
    shutil.rmtree(tmp)


if __name__ == "__main__":
    main()
