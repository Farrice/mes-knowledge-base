#!/usr/bin/env python3
"""Render a labeled contact sheet of the raw bank so it can be curated by eye."""
import base64, glob, os, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).parent
RAW = HERE / "raw"
OUT = HERE / "contact-sheet"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]

COLS = 3
THUMB = 620


def thumb_b64(src, tmp):
    dst = tmp / (src.stem + ".jpg")
    subprocess.run(["sips", "-Z", str(THUMB), "-s", "format", "jpeg",
                    str(src), "--out", str(dst)], check=True, capture_output=True)
    return base64.b64encode(dst.read_bytes()).decode()


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    OUT.mkdir(exist_ok=True)
    tmp = HERE / ".thumbs"
    tmp.mkdir(exist_ok=True)
    root = RAW
    if only and (HERE / only).is_dir():
        root, only = HERE / only, sys.argv[1]
        files = sorted(root.rglob("*.jpg")) + sorted(root.rglob("*.png"))
    else:
        files = sorted(RAW.rglob("*.jpg")) + sorted(RAW.rglob("*.png"))
        if only:
            files = [f for f in files if only in str(f)]
    cells = []
    for f in files:
        try:
            b = thumb_b64(f, tmp)
        except Exception as e:
            print("skip %s (%s)" % (f.name, e), file=sys.stderr)
            continue
        cells.append(
            '<figure><img src="data:image/jpeg;base64,%s"><figcaption>%s</figcaption></figure>'
            % (b, f.stem))
    rows = (len(cells) + COLS - 1) // COLS
    html = """<!doctype html><meta charset=utf-8><style>
      body{margin:0;background:#fff;font:13px/1.3 -apple-system,sans-serif;padding:16px}
      .g{display:grid;grid-template-columns:repeat(%d,1fr);gap:14px}
      figure{margin:0}
      img{width:100%%;height:420px;object-fit:cover;display:block;background:#eee}
      figcaption{padding:5px 2px;color:#333;font-size:12px;word-break:break-all}
    </style><div class=g>%s</div>""" % (COLS, "".join(cells))
    page = OUT / ("sheet-%s.html" % (only or "all"))
    page.write_text(html)
    png = OUT / ("sheet-%s.png" % (only or "all"))
    height = 60 + rows * 470
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=%d,%d" % (COLS * 420 + 80, height),
                    "--virtual-time-budget=6000",
                    "--screenshot=%s" % png, "file://%s" % page], check=True, capture_output=True)
    for t in tmp.iterdir():
        t.unlink()
    tmp.rmdir()
    print("%d images -> %s" % (len(cells), png))


if __name__ == "__main__":
    main()
