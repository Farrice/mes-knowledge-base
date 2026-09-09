#!/usr/bin/env python3
"""Photo-motion reel: her photos with slow movement, one serif line per beat, her lockup. No talking, no filming.
  python3 build_reel.py reels/<spec>.json
spec: {"out": "name", "beats": [{"photo": "img/x.jpg", "line": "serif line", "hand": "handwritten line (optional)", "secs": 4, "zoom": "in|out"}], "lockup": true}
Frames are 1080x1920. Text is rendered as a transparent PNG (chrome headless) and overlaid, so the type stays sharp
while the photo moves. Output: video/<out>.mp4 (silent; add trending audio in Instagram at post time)."""
import glob, json, os, pathlib, shutil, subprocess, sys

HERE = pathlib.Path(__file__).parent
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]
W, H, FPS = 1080, 1920, 30
SERIF = "font-family: 'Playfair Display', Georgia, serif;"
HAND = "font-family: 'Caveat', cursive;"
SANS = "font-family: 'Jost', system-ui, sans-serif;"


def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def overlay_html(line, hand, lockup, size=104):
    lk = f'''<div style="position:absolute;left:0;right:0;bottom:120px;display:flex;flex-direction:column;align-items:center;gap:2px;">
      <span style="{HAND} font-size:54px;color:#fff;line-height:1;">Jen Santulan</span>
      <span style="{SANS} font-size:17px;letter-spacing:.34em;color:rgba(255,255,255,.88);">REALTOR&#174; &#183; SAN FERNANDO VALLEY</span></div>''' if lockup else ""
    hd = f'<div style="{HAND} font-size:60px;font-weight:500;color:#fff;text-align:center;line-height:1.1;">{hand}</div>' if hand else ""
    return f'''<!doctype html><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&family=Jost:wght@400;500&family=Playfair+Display:ital,wght@0,400;1,400&display=swap">
<style>html,body{{margin:0;width:{W}px;height:{H}px;background:transparent;overflow:hidden}}</style>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,20,30,.18) 0%,rgba(15,20,30,.42) 55%,rgba(15,20,30,.62) 100%);"></div>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;padding:0 90px 160px;">
  <div style="{SERIF} font-size:{size}px;line-height:1.04;letter-spacing:-.02em;color:#fff;text-align:center;text-shadow:0 2px 28px rgba(0,0,0,.35);">{line}</div>
  {hd}
</div>
{lk}'''


def main():
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
    tmp = HERE / ".reel_tmp"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()
    out_dir = pathlib.Path(spec["out_dir"]) if spec.get("out_dir") else HERE / "video"
    out_dir.mkdir(exist_ok=True)
    parts = []
    for k, b in enumerate(spec["beats"]):
        html = tmp / f"o{k}.html"
        png = tmp / f"o{k}.png"
        html.write_text(overlay_html(b["line"], b.get("hand", ""), spec.get("lockup", True), b.get("size", 104)))
        run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
             "--default-background-color=00000000", f"--window-size={W},{H}", "--virtual-time-budget=2500",
             f"--screenshot={png}", html.as_uri()])
        secs = float(b.get("secs", 4))
        n = int(secs * FPS)
        zoom = b.get("zoom", "in")
        z = f"min(zoom+0.0009,1.14)" if zoom == "in" else f"if(eq(on,1),1.14,max(zoom-0.0009,1.0))"
        seg = tmp / f"s{k}.mp4"
        run(["ffmpeg", "-y", "-loop", "1", "-i", str(HERE / b["photo"]), "-loop", "1", "-framerate", str(FPS), "-i", str(png),
             "-filter_complex",
             f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
             f"zoompan=z='{z}':d={n}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},"
             f"fade=t=in:st=0:d=0.5,fade=t=out:st={secs - 0.5}:d=0.5[bg];"
             f"[1:v]format=rgba,fade=t=in:st=0.3:d=0.5:alpha=1,fade=t=out:st={secs - 0.6}:d=0.5:alpha=1[tx];"
             f"[bg][tx]overlay=0:0:format=auto",
             "-t", f"{secs}", "-r", str(FPS), "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "19", str(seg)])
        parts.append(seg)
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    out = out_dir / f"{spec['out']}.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", str(out)])
    print(f"reel: {out} ({out.stat().st_size // 1024} KB, {sum(float(b.get('secs', 4)) for b in spec['beats']):.0f}s)")


if __name__ == "__main__":
    main()
