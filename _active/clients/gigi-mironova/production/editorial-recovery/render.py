#!/usr/bin/env python3
import glob,os,subprocess
from pathlib import Path
HERE=Path(__file__).parent
CHROME=sorted(glob.glob(os.path.expanduser('~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell')))[-1]
out=HERE/'recovery-proof.png'
subprocess.run([CHROME,'--headless','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2','--window-size=1080,1350','--virtual-time-budget=7000',f'--screenshot={out}',f'file://{HERE}/recovery-proof.html'],check=True,capture_output=True)
print(out)
