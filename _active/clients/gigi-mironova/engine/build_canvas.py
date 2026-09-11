#!/usr/bin/env python3
"""Assemble a Claude Design canvas from the engine artboards.
Page 1: the Unit 124 gift + the two calibration sets (cal/slides-cal.json).
Page 2: the seven pre-audit sets from slides.json that have not been rewritten yet.
Writes canvas-build/: alnum-stem .dc.html artboards with bare-basename image refs,
downsampled images (<=70 KB), canvas.json. Seeding/publishing happens outside this file."""
import json, pathlib, re, shutil, subprocess, sys

HERE = pathlib.Path(__file__).parent
BUILD = HERE / "canvas-build"
if BUILD.exists():
    shutil.rmtree(BUILD)
(BUILD / "img").mkdir(parents=True)

# 1. Filter the pre-audit spec to the seven sets not yet rewritten.
full = json.load(open(HERE / "slides.json"))
keep = {"c03-balcony-report", "c04-bill-after-closing", "c05-fees-go-down", "c07-net-sheet",
        "c08-who-holds-the-money", "c09-three-clocks", "c10-first-home-ru"}
pre = {"carousels": [c for c in full["carousels"] if c["slug"] in keep]}
(BUILD / "slides-pre.json").write_text(json.dumps(pre))

# 2. Generate both artboard sets.
subprocess.run([sys.executable, str(HERE / "gen_slides.py"), str(HERE / "cal" / "slides-cal.json"), str(BUILD / "gen-cal")], check=True)
subprocess.run([sys.executable, str(HERE / "gen_slides.py"), str(BUILD / "slides-pre.json"), str(BUILD / "gen-pre")], check=True)
DIRS = HERE / "cal" / "slides-directions.json"
if DIRS.exists():
    subprocess.run([sys.executable, str(HERE / "gen_slides.py"), str(DIRS), str(BUILD / "gen-dir")], check=True)

STEM = {  # slug -> alnum stem prefix
    "c01-read-before-you-tour": "Gift", "c02-five-pages": "FivePages", "c06-sell-with-tenant": "Tenant",
    "c03-balcony-report": "Balcony", "c04-bill-after-closing": "Bill", "c05-fees-go-down": "Fees",
    "c07-net-sheet": "Net", "c08-who-holds-the-money": "Escrow", "c09-three-clocks": "Clocks", "c10-first-home-ru": "FirstHomeRU",
    "dir-a-unit-124": "DirA", "dir-b-unit-124": "DirB", "dir-c-unit-124": "DirC",
}
images = set()
artboards, annotations = [], []


def place(spec, gen_dir, page, y0, label):
    y = y0
    for car in spec["carousels"]:
        stem = STEM[car["slug"]]
        for i in range(1, len(car["slides"]) + 1):
            src = gen_dir / f'{car["slug"]}-{i:02d}.dc.html'
            html = src.read_text()
            for m in re.findall(r'src="\.\./assets/[a-z0-9-]+/([^"]+)"', html):
                images.add(m)
            html = re.sub(r'src="\.\./assets/[a-z0-9-]+/([^"]+)"', r'src="\1"', html)
            name = f"{stem}{i:02d}"
            (BUILD / f"{name}.dc.html").write_text(html)
            artboards.append({"file": f"{name}.dc.html", "title": f'{car["title"]} · {i}/{len(car["slides"])}',
                              "x": (i - 1) * 1180, "y": y, "w": 1080, "h": 1350, "page": page})
        annotations.append({"id": f"note-{stem.lower()}", "x": -420, "y": y, "w": 360, "page": page,
                            "text": f'{car["title"]}\n{label}\nkeyword {car["keyword"]} · pairs with video {car["video"]}'})
        y += 1560
    return y


cal = json.load(open(HERE / "cal" / "slides-cal.json"))
y = place(cal, BUILD / "gen-cal", "page-1", 0, "Calibration take · audited numbers · ready for your verdict")
place(pre, BUILD / "gen-pre", "page-2", 0, "PRE-AUDIT · do not post · numbers and register being corrected")
if DIRS.exists():
    place(json.load(open(DIRS)), BUILD / "gen-dir", "page-3", 0, "Two-zone layout · photo zone carries no type · pick one")

# Main = the gift's first slide (copy, keep the original too so the set stays complete)
shutil.copy(BUILD / "Gift01.dc.html", BUILD / "Main.dc.html")
for a in artboards:
    if a["file"] == "Gift01.dc.html":
        a["file"] = "Main.dc.html"
(BUILD / "Gift01.dc.html").unlink()

annotations.insert(0, {"id": "note-top", "x": 0, "y": -420, "w": 1400, "page": "page-1",
                       "text": "GIGI MIRONOVA · UNIT 124 GIFT + CALIBRATION TAKE · 2026-09-01\nRow 1 is the gift going out today (seven slides). Rows 2 and 3 are the other two calibration sets on the same register.\nEvery number on these boards is in the claims ledger as VERIFIED or COMPUTED-OK. The old \"same door, two prices\" set is gone: the $2,500 lease listing was removed from the MLS on Aug 17.\nPage 2 holds the seven sets not yet rewritten; they carry pre-audit copy and are marked do-not-post."})
annotations.append({"id": "note-top2", "x": 0, "y": -420, "w": 1400, "page": "page-2",
                    "text": "PRE-AUDIT SETS · DO NOT POST\nSeven sets from the first pass. Known corrections pending: loan contingency is 17 days on the current contract (not 21); the $60K assessment story has no season and is a few years old; deposit 1–3% is market custom, not a contract default; tenant-notice rule per Civil Code 1954. These get the calibration register once you give the verdict on page 1."})

# 3. Images: downsample to <=70 KB, bare basenames.
SRC = {}
for p in (HERE / "assets").rglob("*"):
    if p.suffix.lower() in (".jpg", ".jpeg", ".png"):
        SRC[p.name] = p
for name in sorted(images):
    dst = BUILD / "img" / name
    shutil.copy(SRC[name], dst)
    for px, q in ((1000, 52), (900, 45), (800, 40), (720, 36), (640, 32)):
        subprocess.run(["sips", "-Z", str(px), "-s", "format", "jpeg", "-s", "formatOptions", str(q), str(dst), "--out", str(dst)], check=True, capture_output=True)
        if dst.stat().st_size <= 70 * 1024:
            break

pages = [{"id": "page-1", "name": "Unit 124 gift + calibration"}, {"id": "page-2", "name": "Pre-audit sets (do not post)"}]
launch_page = "page-1"
if DIRS.exists():
    pages.append({"id": "page-3", "name": "Unit 124 layout directions A / B / C"})
    launch_page = "page-3"
    annotations.append({"id": "note-top3", "x": 0, "y": -420, "w": 1400, "page": "page-3",
                        "text": "UNIT 124 · THREE LAYOUT DIRECTIONS · same copy, same photos, same slides 1, 4, 5, 6\nThe rule behind all three: the photograph owns a zone with no type on it; the data owns paper. Nothing overlaps.\nA · Split spread: the room takes the top half untouched; the number and the list sit on paper below. Most breathing room.\nB · Inset column: type on the left, the room as a tall column on the right. The room is present on every slide but cropped to a sliver.\nC · Data-led: a strip of the room across the top, the number owns the page. Loudest numbers, least room.\nPick one and the full set rebuilds in it."})
canvas = {"pages": pages, "artboards": artboards, "annotations": annotations,
          "launch": {"view": "canvas", "page": launch_page}}
(BUILD / "canvas.json").write_text(json.dumps(canvas, indent=2))
for d in ("gen-cal", "gen-pre", "gen-dir"):
    if (BUILD / d).exists():
        shutil.rmtree(BUILD / d)
print(f"{len(artboards)} artboards, {len(images)} images -> {BUILD}")
print("images:", " ".join(f"{n} {((BUILD / 'img' / n).stat().st_size // 1024)}KB" for n in sorted(images)))
