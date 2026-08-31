#!/usr/bin/env python3
import glob,json,os,subprocess,shutil
from pathlib import Path
from PIL import Image,ImageDraw
HERE=Path(__file__).parent; OUT=HERE/'png'; POST=HERE/'post-ready'
CHROME=sorted(glob.glob(os.path.expanduser('~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell')))[-1]
def main():
    spec=json.loads((HERE/'manifest.json').read_text()); OUT.mkdir(exist_ok=True); deliver=HERE/'deliver'; deliver.mkdir(exist_ok=True)
    for name,dim in spec['assets'].items():
        subprocess.run([CHROME,'--headless','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2',f"--window-size={dim['width']},{dim['height']}",'--virtual-time-budget=7000',f'--screenshot={OUT/name}.png',f'file://{HERE/name}.html'],check=True,capture_output=True)
    for old_name in ['identity-overview.png','03-private-showing.png','04-next-listing.png','04-close-white.png','04-close-navy.png','CAPTIONS.txt']:
        old_path=deliver/old_name
        if old_path.exists(): old_path.unlink()
    final_names=['01-remodel-date','02-in-unit-laundry','03-private-balcony','04-contact-gigi']
    for name in final_names:
        shutil.copy2(OUT/f'{name}.png',deliver/f'{name}.png')
    POST.mkdir(exist_ok=True)
    for old in POST.iterdir():
        if old.is_file(): old.unlink()
    for name in final_names:
        shutil.copy2(OUT/f'{name}.png',POST/f'{name}.png')
    for source,target in [('POST-CAPTION.md','CAPTION.txt'),('ALT-TEXT.md','ALT-TEXT.txt')]:
        shutil.copy2(HERE/source,deliver/target); shutil.copy2(HERE/source,POST/target)
    names=final_names; thumb=(360,450)
    sheet=Image.new('RGB',(1580,560),(225,223,217)); d=ImageDraw.Draw(sheet)
    for i,name in enumerate(names):
        im=Image.open(OUT/f'{name}.png').convert('RGB'); im.thumbnail(thumb); x=25+i*390
        sheet.paste(im,(x,52)); d.text((x,25),name,fill=(22,58,82))
    sheet.save(HERE/'final-review.jpg',quality=94)
    print('gift package rendered')
if __name__=='__main__': main()
