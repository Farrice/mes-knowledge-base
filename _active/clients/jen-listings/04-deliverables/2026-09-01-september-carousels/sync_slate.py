#!/usr/bin/env python3
"""Sync the Jen-facing slate to COPY-FINAL-v2: replace each concept's reel block (hook / other hooks / script /
on screen / caption) and the condo carousel block with the final copy. Everything else in the slate stays."""
import pathlib, re

HERE = pathlib.Path(__file__).parent
SLATE = HERE.parent / "2026-09-01-local-signal-slate-v1.md"
FINAL = HERE / "COPY-FINAL-v2-condo-and-reels.md"

slate = SLATE.read_text()
final = FINAL.read_text()

def final_section(title_prefix):
    m = re.search(rf"\n## {re.escape(title_prefix)}.*?\n(.*?)(?=\n## |\Z)", final, re.S)
    return m.group(1).strip() if m else None

def reel_block(n):
    sec = final_section(f"reel {n}")
    sec = re.sub(r"^\*the opinion here.*?\n\n", "", sec, flags=re.S)  # slate already carries that note
    sec = sec.split("\n**her first reply back")[0].strip()
    # slate label shape: bold lowercase labels, 'other hooks if that one isn't you:'
    sec = sec.replace("**hook:**", "**hook** (first 2 seconds, on screen too):", 1)
    sec = sec.replace("**other hooks:**", "other hooks if that one isn't you:", 1)
    sec = re.sub(r"other hooks if that one isn't you: (.+)", lambda m: "other hooks if that one isn't you:\n" + "\n".join("- " + h.strip() for h in m.group(1).split(" · ")), sec)
    return sec

def replace_reel(slate, n):
    # from the '### reel' header of concept n up to the next '### carousel' or next concept/notes header
    concept_start = re.search(rf"\n## {n}\. ", slate).start()
    nxt = re.search(r"\n## (?:\d\. |filming notes)", slate[concept_start + 5:])
    concept_end = concept_start + 5 + (nxt.start() if nxt else len(slate) - concept_start - 5)
    block = slate[concept_start:concept_end]
    m = re.search(r"(### reel[^\n]*\n)(.*?)(?=\n### carousel|\Z)", block, re.S)
    new_block = block[:m.start(2)] + "\n" + reel_block(n) + "\n" + block[m.end(2):]
    return slate[:concept_start] + new_block + slate[concept_end:]

for n in (1, 2, 3, 4):
    slate = replace_reel(slate, n)

# condo carousel (concept 1): replace the numbered 1..7 lines + glossary line with the final list + caption glossary
car = final_section("condo carousel")
m = re.search(r"(### carousel · 7 slides[^\n]*\n\n)(.*?)(?=\n---\n)", slate, re.S)
slate = slate[:m.start(2)] + car.replace("### caption glossary", "**caption glossary**") + "\n" + slate[m.end(2):]

SLATE.write_text(slate)
print("slate synced:", SLATE.name)
