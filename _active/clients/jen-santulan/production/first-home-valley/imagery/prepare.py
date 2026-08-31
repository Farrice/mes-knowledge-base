#!/usr/bin/env python3
"""Downscale the curated shortlist to artboard-ready JPEGs.

Long edge 1600px, quality 70 — enough for a 1080x1350 artboard at 2x export,
small enough that twelve of them base64'd stay well under the artifact size cap.
No cropping here: CSS object-fit does the framing so it stays editable in the
Claude Design canvas. macOS `sips` only — no PIL on this machine.
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).parent
SRC = HERE / "shortlist"
DST = HERE / "prepared"
LONG_EDGE = 1600
QUALITY = 70


def main():
    DST.mkdir(exist_ok=True)
    files = sorted(SRC.glob("*.jpg")) + sorted(SRC.glob("*.png"))
    if not files:
        sys.exit("nothing in %s" % SRC)
    total = 0
    for f in files:
        # short, stable name: drop the openverse hash suffix
        stem = f.stem.rsplit("-", 1)[0]
        out = DST / (stem + ".jpg")
        subprocess.run(["sips", "-Z", str(LONG_EDGE), "-s", "format", "jpeg",
                        "-s", "formatOptions", str(QUALITY),
                        str(f), "--out", str(out)], check=True, capture_output=True)
        kb = out.stat().st_size // 1024
        total += kb
        print("  %-42s %4d KB" % (out.name, kb))
    print("\n%d files, %.1f MB total -> %s" % (len(files), total / 1024, DST))


if __name__ == "__main__":
    main()
