#!/usr/bin/env python3
import glob,json,os,subprocess,shutil
from pathlib import Path
from PIL import Image,ImageDraw
HERE=Path(__file__).parent; OUT=HERE/'png'
CHROME=sorted(glob.glob(os.path.expanduser('~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell')))[-1]
def main():
    spec=json.loads((HERE/'manifest.json').read_text()); OUT.mkdir(exist_ok=True); deliver=HERE/'deliver'; deliver.mkdir(exist_ok=True)
    for name,dim in spec['assets'].items():
        subprocess.run([CHROME,'--headless','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2',f"--window-size={dim['width']},{dim['height']}",'--virtual-time-budget=7000',f'--screenshot={OUT/name}.png',f'file://{HERE/name}.html'],check=True,capture_output=True)
        shutil.copy2(OUT/f'{name}.png',deliver/f'{name}.png')
    names=['01-remodel-date','02-in-unit-laundry','03-private-showing','identity-overview']; thumb=(360,450)
    sheet=Image.new('RGB',(1580,560),(225,223,217)); d=ImageDraw.Draw(sheet)
    for i,name in enumerate(names):
        im=Image.open(OUT/f'{name}.png').convert('RGB'); im.thumbnail(thumb); x=25+i*390
        sheet.paste(im,(x,52)); d.text((x,25),name,fill=(22,58,82))
    sheet.save(HERE/'gift-review.jpg',quality=94)
    print('gift package rendered')
if __name__=='__main__': main()
