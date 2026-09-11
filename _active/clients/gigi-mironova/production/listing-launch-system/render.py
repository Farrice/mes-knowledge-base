#!/usr/bin/env python3
import glob,json,os,subprocess
from pathlib import Path
from PIL import Image,ImageDraw,ImageOps

HERE=Path(__file__).parent; OUT=HERE/'png'
CHROME=sorted(glob.glob(os.path.expanduser('~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell')))[-1]

def contact(names,path,cols=4,thumb=(360,450)):
    rows=(len(names)+cols-1)//cols
    sheet=Image.new('RGB',(cols*thumb[0]+(cols+1)*24,rows*thumb[1]+(rows+1)*50),(228,225,218))
    d=ImageDraw.Draw(sheet)
    for i,n in enumerate(names):
        im=Image.open(OUT/f'{n}.png').convert('RGB'); im.thumbnail(thumb)
        x=24+(i%cols)*(thumb[0]+24); y=24+(i//cols)*(thumb[1]+50)
        sheet.paste(im,(x,y)); d.text((x,y+thumb[1]+8),n,fill=(23,58,84))
    sheet.save(path,quality=92)

def main():
    spec=json.loads((HERE/'manifest.json').read_text()); OUT.mkdir(exist_ok=True)
    for old in OUT.glob('*.png'): old.unlink()
    for name,dim in spec['assets'].items():
        subprocess.run([CHROME,'--headless','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2',f"--window-size={dim['width']},{dim['height']}",'--virtual-time-budget=7000',f'--screenshot={OUT/name}.png',f'file://{HERE/name}.html'],check=True,capture_output=True)
    contact(['01-reveal','02-feature','03-financial','04-open-house'],HERE/'launch-review.jpg',4)
    contact([f'gift-0{i}' for i in range(1,7)],HERE/'gift-review.jpg',3)
    print('rendered launch, gift, and standard')

if __name__=='__main__': main()
