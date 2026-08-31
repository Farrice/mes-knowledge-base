#!/usr/bin/env python3
"""Contact sheet of the rendered v2 artboards, whole-slide (contain, not cover),
so composition and cropping can be judged across the deck in one look."""
import base64, glob, os, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).parent
SRC = HERE.parent / "png"
OUT = HERE / "review"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]

COLS = 3
THUMB = 520
CELL_H = 660


def main():
    OUT.mkdir(exist_ok=True)
    tmp = HERE / ".rthumbs"
    tmp.mkdir(exist_ok=True)
    files = sorted(SRC.glob("*.png"))
    if not files:
        sys.exit("no renders in %s" % SRC)
    cells = []
    for f in files:
        dst = tmp / (f.stem + ".jpg")
        subprocess.run(["sips", "-Z", str(THUMB), "-s", "format", "jpeg",
                        "-s", "formatOptions", "78", str(f), "--out", str(dst)],
                       check=True, capture_output=True)
        b = base64.b64encode(dst.read_bytes()).decode()
        cells.append('<figure><img src="data:image/jpeg;base64,%s">'
                     '<figcaption>%s</figcaption></figure>' % (b, f.stem))
    rows = (len(cells) + COLS - 1) // COLS
    html = """<!doctype html><meta charset=utf-8><style>
      body{margin:0;background:#EDEDEA;font:13px/1.3 -apple-system,sans-serif;padding:18px}
      .g{display:grid;grid-template-columns:repeat(%d,1fr);gap:18px}
      figure{margin:0;background:#fff;padding:8px;box-shadow:0 1px 3px rgba(0,0,0,.14)}
      img{width:100%%;height:%dpx;object-fit:contain;display:block;background:#F6F6F4}
      figcaption{padding:7px 2px 2px;color:#222;font-size:12px;font-weight:600}
    </style><div class=g>%s</div>""" % (COLS, CELL_H, "".join(cells))
    page = OUT / "sheet.html"
    page.write_text(html)
    png = OUT / "sheet.png"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=%d,%d" % (COLS * 430 + 80, 70 + rows * (CELL_H + 60)),
                    "--virtual-time-budget=8000",
                    "--screenshot=%s" % png, "file://%s" % page],
                   check=True, capture_output=True)
    for t in tmp.iterdir():
        t.unlink()
    tmp.rmdir()
    print("%d slides -> %s" % (len(cells), png))


if __name__ == "__main__":
    main()
