#!/usr/bin/env python3
"""Assemble the forward-ready Unit 124 gift: 7 slides + message + caption + reel script + don't-say."""
import pathlib, re, shutil

CAL = pathlib.Path(__file__).parent
OUT = CAL.parent / "GIFT-124"
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

src = CAL / "CAROUSEL-BATCH" / "c01-read-before-you-tour"
for p in sorted(src.glob("*.png")):
    shutil.copy(p, OUT / f"unit-124-slide-{p.stem}.png")

send = (CAL / "SEND-124.md").read_text()
(OUT / "MESSAGE-TO-GIGI.txt").write_text(send)

script = (CAL / "SCRIPT-PACK-CAL.md").read_text()
v1 = script.split("## Video 3 ")[0]
spoken = v1.split("### Script (word for word)")[1].split("### Bullet version")[0].strip()
onscreen = v1.split("### On-screen text")[1].strip()
captions = send.split("## Caption, pick one")[1].split("## Don't say")[0].strip()
dont = send.split("## Don't say")[1].split("This one is on me")[0].strip()

(OUT / "REEL-SCRIPT-unit-124.txt").write_text(
    "REEL · at the unit · keyword 124 · under 40 seconds\n\n" + spoken + "\n\nON SCREEN\n" + onscreen + "\n")
(OUT / "CAPTION-pick-one.txt").write_text(captions + "\n")
(OUT / "DONT-SAY.txt").write_text(dont + "\n")
(OUT / "README-FIRST.txt").write_text(
    "Unit 124 gift for Gigi · forward in this order\n\n"
    "1. MESSAGE-TO-GIGI.txt (paste as the text)\n"
    "2. unit-124-slide-01.png ... 07.png (the carousel, post in order)\n"
    "3. CAPTION-pick-one.txt\n"
    "4. REEL-SCRIPT-unit-124.txt\n"
    "5. DONT-SAY.txt\n\n"
    "Before it posts: she confirms $299,999 and $620 still hold and OKs her listing photos.\n")
print(sorted(p.name for p in OUT.iterdir()))
