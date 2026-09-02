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

# carousels 2 and 3: the valley native copy (plain words with punch), stamps van nuys 91401 / sherman oaks 91403
SET_COPY = {
    2: """1. **that torn-up median on van nuys blvd... is a train.** · and it doesn't open until december 2031. · stamp: van nuys · 91401
2. **eleven stations. van nuys to pacoima.** · the east valley light rail runs down the middle of van nuys blvd, from the G line to san fernando road. metro signed the $2.43 billion contract in august... so it's real. it's just five years out. · keyed map: 01 what it doesn't do · 02 what it does · 03 the construction years · 04 the stations
3. **01 it doesn't promise prices.** · nobody can put a number on 2031 today. anyone telling you the station adds value is guessing... and you'd be paying for the guess. · numerals: 6.7 miles · 11 stations · december 2031
4. *(navy slide)* **02 it changes the timeline question.** · how long you stay matters more than what you pay. · 7-year buyer: the blocks people skip for the traffic deserve a second look. · 2-year buyer: you'd be buying five years of construction, not a train.
5. **03 lane closures and detours through 2031.** · and the van nuys G line station is closed for its own rebuild until around the end of 2027. plan around the detours, not the ribbon-cutting.
6. **04 the corridor to actually look at.** · the eleven stations, oxnard st (G line) to van nuys / san fernando. · small print: la metro project status report
7. **tell me how long you're staying.** · i'll tell you if the train changes your math... and that's usually the whole conversation. i'm here for you... i do this to protect you and your best interest. · my DMs are open · small print: la metro · la daily news aug 24 2026 · commercial observer aug 14 2026""",
    3: """1. **fully approved... and the insurance quote still moves your payment.** · what october 15 changes. · stamp: sherman oaks · 91403
2. **october 15. the state's backup fire policy goes up.** · the california FAIR plan is what you get when no regular company will cover the house. on october 15 it rises 29.1% on average... weighted to wildfire, so hillsides move a lot more. · keyed map: 01 who it hits · 02 who it mostly doesn't · 03 the date detail · 04 what it actually covers
3. **01 29.1% is the average. hillsides, canyons and foothills can move far more.** · sherman oaks hills · woodland hills · chatsworth · the sylmar fringe
4. *(navy slide)* **02 the valley floor.** · most homes down here still get a regular company. get the real quote anyway... it's part of your payment, and i'd rather you see it on a tuesday than once we're in escrow with the clock running.
5. **03 the day your policy starts decides your rate.** · starts before oct 15: generally today's rate, for the whole term. · starts on or after: the new rate, from day one. · closing anywhere near mid-october? that's a call to your insurance broker this week, not next month.
6. **04 fire only.** · the backup policy covers fire. you add a second policy for theft, water and liability. together they usually cost well above a regular one... which is why the quote comes first now.
7. **send me the address before you write.** · i'll get the quote in hand first... approved and insured are two different yeses. i'm here for you... i do this to protect you and your best interest. · my DMs are open · small print: california department of insurance · rate change effective oct 15 2026""",
}
for n, copy in SET_COPY.items():
    concept_start = re.search(rf"\n## {n}\. ", slate).start()
    nxt = re.search(r"\n## (?:\d\. |filming notes)", slate[concept_start + 5:])
    concept_end = concept_start + 5 + (nxt.start() if nxt else len(slate) - concept_start - 5)
    block = slate[concept_start:concept_end]
    m = re.search(r"(### carousel[^\n]*\n\n)(.*?)(?=\n---|\Z)", block, re.S)
    if m:
        header = "### carousel · 7 slides · valley native look\n\n"
        block = block[:m.start(1)] + header + copy + "\n" + block[m.end(2):]
        slate = slate[:concept_start] + block + slate[concept_end:]

slate = slate.replace("### carousel · 7 slides · your warm editorial look (cream ground, navy ink, one navy slide)", "### carousel · 7 slides · valley native look")
while "\n---\n\n---\n" in slate:
    slate = slate.replace("\n---\n\n---\n", "\n---\n")
SLATE.write_text(slate)
print("slate synced:", SLATE.name)
