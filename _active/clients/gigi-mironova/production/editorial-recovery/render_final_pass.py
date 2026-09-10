#!/usr/bin/env python3
import glob,os,subprocess
from pathlib import Path
from PIL import Image,ImageDraw
HERE=Path(__file__).parent
CHROME=sorted(glob.glob(os.path.expanduser('~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell')))[-1]
out=HERE/'final-pass.png'
subprocess.run([CHROME,'--headless','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2','--window-size=1080,1350','--virtual-time-budget=7000',f'--screenshot={out}',f'file://{HERE}/final-pass.html'],check=True,capture_output=True)
old=Image.open(HERE/'senior-pass.png').convert('RGB'); new=Image.open(out).convert('RGB')
old.thumbnail((540,675)); new.thumbnail((540,675))
sheet=Image.new('RGB',(1180,770),(225,223,217)); sheet.paste(old,(30,50)); sheet.paste(new,(610,50))
d=ImageDraw.Draw(sheet); d.text((30,22),'TWO-IMAGE SENIOR PASS',fill=(22,58,82)); d.text((610,22),'ONE-IMAGE RESTRAINT PASS',fill=(22,58,82))
sheet.save(HERE/'restraint-comparison.jpg',quality=94)
print(out)
