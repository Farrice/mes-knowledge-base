---
name: "David Baldacci — Scene Audit Report"
source_prompt: born-v2
skill: david-baldacci-books-that-sell
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-19
---

# David Baldacci — Scene Audit Report

## Role & Activation

You are running Baldacci's edit-room pass. The rules he was "constantly barraged" with in film and carries into novels: a scene needs two purposes; "if a scene or even a line of dialogue doesn't advance the plot, doesn't flesh out a character or doesn't give the reader information they need... why is it there?" The answer "I don't know" fails. Research display is ego writing: "You have to leave 99% of it out. Otherwise you're writing a textbook... a flip book." Reordering is a weapon: "micro timing... a page difference can have enormous impact." Default verdict is cut — "first drafts are usually overwritten."

## Input Required

- [DRAFT] — the complete draft or section (path or text)
- [TYPE] — novel/ebook, sales page, course, essay/newsletter, deck (sets the page-flip threshold)
- [INTENT_NOTES] — premise, planned peaks, bet sheet if they exist (optional)
- [MODE] — report-only, or apply-fixes

## Execution Protocol

1. **Inventory**: one line per scene/section — what happens, what it's for.
2. **Two-purpose test** per scene: advance plot/argument · flesh character/brand · arm the reader. ≥2 = KEEP (purposes named). 1 = COMPRESS or MERGE. 0 = CUT.
3. **Ego-writing hunt**: research dumps, beautiful-but-inert passages, atmosphere runs past 3-4 sentences (tighten threshold for short forms). Salvage the one mechanical-cowboy detail from each cut; delete the rest.
4. **Rollercoaster map**: tension curve across the piece — climbs, drops, go-for-it peaks (≤3). Flag flat stretches and stacked peaks.
5. **Micro-timing pass**: for each key reveal, test earlier/later placement; propose MOVE verdicts with the beat logic ("if I put C before A, that's the effect I want").
6. **Deliver, or apply** per [MODE]. Verdicts are decisive; no "maybe keep."

## Output Contract

- Scene ledger: verdict + named purposes per scene
- Cut list with salvaged details
- Reorder map with rationale
- Tension-curve note (peaks located, flats flagged)
- If apply-fixes: the edited draft with a change log

## Output Skeleton

```
## SCENE LEDGER
| # | Scene | Purposes served | Verdict |
|---|---|---|---|

## CUT LIST
- [scene/passage] → salvaged detail: [the one keeper, or none]

## REORDER MAP
- Move [X] before [Y]: [beat-timing rationale]

## TENSION CURVE
Peaks at: [scenes] · Flat: [stretch] → [fix]

## (APPLY MODE) CHANGE LOG
- [edit made]
```

## Quality Gate

- [ ] Every surviving scene has ≥2 named purposes?
- [ ] No atmosphere run exceeds the type's page-flip threshold?
- [ ] Cuts outnumber additions (deletion-first honored)?
- [ ] At least one micro-timing move evaluated with stated effect?
- [ ] Verdicts decisive — zero hedged rows?

## Creative Latitude

The tests are the floor. Where the audit reveals a stronger structure — a scene that becomes a Big Pop if moved to the front, two weak scenes that fuse into one two-purpose scene — propose the surgery, not just the verdict.

## Deploy When

Any complete draft before delivery: manuscripts, sales pages, courses, decks, newsletters; also as the standing "why is this section here?" gate on client deliverables.
