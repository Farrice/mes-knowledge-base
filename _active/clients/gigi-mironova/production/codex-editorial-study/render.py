#!/usr/bin/env python3
"""Render the three self-contained editorial boards and a review strip."""
import glob
import os
import subprocess
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw

HERE = Path(__file__).parent
OUT = HERE / "png"
CHROME = sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]


def main():
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.png"):
        old.unlink()
    for html in sorted(HERE.glob("0*.html")):
        png = OUT / f"{html.stem}.png"
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=2", "--window-size=1080,1350",
                        "--virtual-time-budget=7000", f"--screenshot={png}", f"file://{html}"],
                       check=True, capture_output=True)
    sheet = Image.new("RGB", (1680, 760), (225, 223, 217))
    draw = ImageDraw.Draw(sheet)
    for i, png in enumerate(sorted(OUT.glob("*.png"))):
        im = Image.open(png).convert("RGB")
        im.thumbnail((520, 650))
        tile = Image.new("RGB", (540, 700), "white")
        tile.paste(im, ((540-im.width)//2, 12))
        draw.text((20+i*550, 725), png.stem, fill=(23,58,84))
        sheet.paste(tile, (i*550, 0))
    sheet.save(HERE / "review-strip.jpg", quality=92)
    print("3 PNGs + review-strip.jpg")


if __name__ == "__main__":
    main()
