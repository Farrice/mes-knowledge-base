#!/usr/bin/env python3
"""Assemble the Claude Design kit: everything needed to explore variations of Valley Native inside Claude Design.
Writes claude-design-kit/ and zips it."""
import pathlib, re, shutil

HERE = pathlib.Path(__file__).parent
KIT = HERE / "claude-design-kit"
if KIT.exists():
    shutil.rmtree(KIT)
(KIT / "photos").mkdir(parents=True)
(KIT / "reference" / "carousels").mkdir(parents=True)
(KIT / "reference" / "presentation").mkdir(parents=True)
(KIT / "source").mkdir()

# spec + rules
shutil.copy(HERE / "DESIGN.md", KIT / "DESIGN.md")
shutil.copy(HERE / "VALLEY-NATIVE-RULEBOOK.md", KIT / "RULEBOOK.md")
for f in ("HANDOFF.md", "PROMPTS.md", "COPY-DECK.md"):
    shutil.copy(HERE / "kit-docs" / f, KIT / f)

# photos with provenance
for p in (HERE / "img").glob("*.jpg"):
    shutil.copy(p, KIT / "photos" / p.name)
shutil.copy(HERE / "img" / "provenance.json", KIT / "photos" / "provenance.json")

# reference renders
for key, prefix in (("condo", "dir-d"), ("rail", "rail"), ("insurance", "insurance")):
    for i in range(1, 8):
        src = HERE / "png" / f"{prefix}-{i:02d}.png"
        if src.exists():
            shutil.copy(src, KIT / "reference" / "carousels" / f"{key}-{i:02d}.png")
for i in range(1, 17):
    src = HERE / "png" / f"deck-{i:02d}.png"
    if src.exists():
        shutil.copy(src, KIT / "reference" / "presentation" / f"board-{i:02d}.png")
shutil.copy(HERE / "png" / "deck-17-dm-reply.png", KIT / "reference" / "presentation" / "saved-dm-reply.png")

# vector pdfs (canva-ready, also fine as claude design attachments)
for p in (HERE / "canva").glob("*.pdf"):
    shutil.copy(p, KIT / "reference" / p.name)

# generator source
for name in ("gen_valley.py", "gen_valley_sets.py", "new_set.py", "render_png.py"):
    shutil.copy(HERE / name, KIT / "source" / name)
shutil.copytree(HERE / "sets", KIT / "source" / "sets")

zip_path = shutil.make_archive(str(HERE / "jen-valley-native-claude-design-kit"), "zip", KIT)
print("kit:", KIT, "->", zip_path, f"({pathlib.Path(zip_path).stat().st_size // 1024} KB)")
