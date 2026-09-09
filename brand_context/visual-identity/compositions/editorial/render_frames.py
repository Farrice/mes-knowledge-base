#!/usr/bin/env python3
"""Render the editorial reference frames (HTML, 1080x1350) to PNG.

    uv run --with playwright python render_frames.py [--out DIR] [frame.html ...]

Default: every frames/*.html -> ../../../visual_refs/editorial/<stem>.png (the
ssc-template-builder's ref input). Deterministic, no AI, $0. Requires the
Playwright chromium already used by mkt-visual-identity's brand-bible script.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRAMES = HERE / "frames"
DEFAULT_OUT = HERE.parents[2] / "visual_refs" / "editorial"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("frames", nargs="*")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args()
    from playwright.sync_api import sync_playwright

    files = [Path(f) for f in args.frames] or sorted(FRAMES.glob("[0-9]*.html"))
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        for f in files:
            page.goto(f.resolve().as_uri())
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(250)
            target = out / f"{f.stem}.png"
            page.screenshot(path=str(target), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            print(f"rendered -> {target}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
