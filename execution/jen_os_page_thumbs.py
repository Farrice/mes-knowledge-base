"""jen_os_page_thumbs.py: thumbnails for the Valley OS page. Run before jen_os_page.py.
  python3 execution/jen_os_page_thumbs.py .tmp/valley-os/thumbs
"""
import glob, os, pathlib, shutil, subprocess, sys

LANE = pathlib.Path(__file__).resolve().parents[1]
WEEKS = LANE / "_active/clients/jen-listings/04-deliverables/2026-09-06-engine-v2-weeks-1-2"
POOL = LANE / "_active/clients/jen-listings/04-deliverables/2026-09-01-september-carousels/img"
HERS = LANE / "_active/clients/jen-listings/06-system/valley-editions/photos/jen"
# edition-01 renders live in out/ (gitignored). Read from this tree first; fall back to the old
# jen-engine-v2-weeks worktree only if it still exists (2026-09-02: that lane merged into main).
# If neither has renders, re-render: python3 06-system/valley-editions/editions.py edition01
_ED_CANDIDATES = [
    LANE / "_active/clients/jen-listings/06-system/valley-editions/out/edition-01",
    pathlib.Path("/Users/farricecain/Google Antigravity/_active/clients/jen-listings/06-system/valley-editions/out/edition-01"),
    pathlib.Path("/Users/farricecain/Google Antigravity/.claude/worktrees/jen-engine-v2-weeks/_active/clients/jen-listings/06-system/valley-editions/out/edition-01"),
]
ED = next((p for p in _ED_CANDIDATES if p.exists()), _ED_CANDIDATES[0])
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
FF = shutil.which("ffmpeg") or sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/ffmpeg-*/ffmpeg-mac-arm64")))[-1]

def thumb(src, name, w):
    dst = OUT / (name + ".jpg")
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "72", "--resampleWidth", str(w), str(src), "--out", str(dst)],
                   check=True, capture_output=True)
    return dst

def frame(mp4, name, w):
    dst = OUT / (name + ".jpg")
    subprocess.run([FF, "-y", "-ss", "1.2", "-i", str(mp4), "-frames:v", "1", "-vf", f"scale={w}:-1", "-q:v", "5", str(dst)],
                   check=True, capture_output=True)
    return dst

made = []
for wk in ["week-of-2026-09-07", "week-of-2026-09-14", "week-of-2026-09-21"]:
    for p in sorted((WEEKS / wk).glob("*.png")):
        made.append(thumb(p, p.stem, 560))
    for m in sorted((WEEKS / wk).glob("*.mp4")):
        made.append(frame(m, m.stem, 400))
for p in sorted(ED.glob("*.png")):
    made.append(thumb(p, "ed01-" + p.stem, 420))
for p in sorted(HERS.glob("*.jpg")):
    made.append(thumb(p, "hers-" + p.stem, 240))
for p in sorted(POOL.glob("*.jpg")):
    made.append(thumb(p, "pool-" + p.stem, 240))
total = sum(f.stat().st_size for f in made)
print(len(made), "thumbs,", total // 1024, "KB total")
for f in made: print(f.name, f.stat().st_size // 1024, "KB")
