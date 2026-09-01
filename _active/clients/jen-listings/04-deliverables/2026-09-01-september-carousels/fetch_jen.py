#!/usr/bin/env python3
"""Pull 3-5 photos of Jen from her own public Instagram posts (URLs captured in the 2026-05 recon scrape).
Farrice authorized this 2026-09-01. Saves to img/jen/ and shrinks under ~70 KB."""
import json, pathlib, subprocess, urllib.request

HERE = pathlib.Path(__file__).parent
OUT = HERE / "img" / "jen"
OUT.mkdir(parents=True, exist_ok=True)
RAW = pathlib.Path("/Users/farricecain/Google Antigravity/.claude/worktrees/jen-carousel-reel-concepts/_active/clients/jen-santulan/recon/ig-scrape-raw.json")
H = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"}

# shortCode -> label. Her intro post, recognition post, and talking-head reel covers.
WANT = {
    "DJFE4JovTfb": "intro",          # "Hi, I'm Jen — welcome!" sidecar (6 images)
    "DWHdckmjykK": "recognition",    # award sidecar (3 images)
    "DYkn2gBPWJq": "talking-head",   # buyer-misconceptions reel cover
    "DVeL1xBD-Tq": "fthb-reel",      # FTHB down payment reel cover
    "DWR0NcbDNvf": "team-duo",       # "more than a duo" reel cover
    "DW2ZoZfD0Is": "buyers-story",   # first-time buyers reel cover
}
items = {x["shortCode"]: x for x in json.load(open(RAW))["items"]}
saved = []
for code, label in WANT.items():
    x = items.get(code)
    if not x:
        print("missing", code); continue
    urls = [x.get("displayUrl")] + list(x.get("images") or [])[:6]
    for i, u in enumerate([u for u in urls if u]):
        name = f"{label}-{i:02d}.jpg"
        try:
            data = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=30).read()
            if len(data) < 5000:
                print("tiny", name); continue
            (OUT / name).write_bytes(data)
            saved.append(name)
            print("ok", name, len(data) // 1024, "KB")
        except Exception as e:
            print("FAIL", name, str(e)[:80])
for f in sorted(OUT.glob("*.jpg")):
    for px, q in ((1000, 52), (900, 45), (800, 40), (720, 36)):
        subprocess.run(["sips", "-Z", str(px), "-s", "format", "jpeg", "-s", "formatOptions", str(q), str(f), "--out", str(f)], check=True, capture_output=True)
        if f.stat().st_size <= 70 * 1024:
            break
print("saved", len(saved), "->", OUT)
