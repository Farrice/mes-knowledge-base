#!/usr/bin/env python3
import glob, json, os, subprocess
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw

HERE=Path(__file__).parent
OUT=HERE/"png"
CHROME=sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]

def main():
    spec=json.loads((HERE/"manifest.json").read_text())
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.png"): old.unlink()
    for name,dim in spec["assets"].items():
        out=OUT/f"{name}.png"
        subprocess.run([CHROME,"--headless","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=2",f"--window-size={dim['width']},{dim['height']}","--virtual-time-budget=7000",f"--screenshot={out}",f"file://{HERE/name}.html"],check=True,capture_output=True)
    comp=Image.open(OUT/"comparison.png").convert("RGB"); comp.thumbnail((1500,917))
    hero=Image.open(OUT/"hero.png").convert("RGB"); hero.thumbnail((520,650))
    sheet=Image.new("RGB",(1700,1000),(228,225,218)); sheet.paste(comp,(30,30)); sheet.paste(hero,(1140,300))
    ImageDraw.Draw(sheet).text((1140,270),"DEFINITIVE HERO",fill=(23,58,84))
    sheet.save(HERE/"review.jpg",quality=92)
    print("comparison.png + hero.png + review.jpg")

if __name__=="__main__": main()
