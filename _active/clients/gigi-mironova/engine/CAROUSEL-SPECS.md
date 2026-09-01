# Carousel Specs — Gigi Mironova · 10 carousels · Stage 5 (design brief) + Stage 6 (rendered)

**Status: DRY-RUN.** The sample-carousel approval gate (Stage 5, step 3) did not fire; Farrice judges the grid instead. Machine source of every slide's copy and layout: `slides.json`. Render: `python3 gen_slides.py && python3 render.py && python3 review_sheet.py`. Output: `CAROUSEL-BATCH/<slug>/NN.png` (1080×1350) and `review/sheet.png` (one grid, one carousel per row).

## Locked visual system

Lineage: the shared realtor editorial floor (`_shared/realtor-editorial-system/DESIGN.md`), keyed to Gigi per its open recommendations #1 (light register: warm paper, one warm accent) and #2 (a second hue per agent). Character and palette carried from the "Calm Closer" pass in the earlier gigi lanes; two tightenings so it meets the carousel banlist: **square corners, no drop shadows.**

| Token | Value | Role |
|---|---|---|
| paper | #F7F3EC | ground on structure slides |
| ink | #173A54 | all type on paper |
| band | #244C68 | dark grounds (pause and CTA slides) |
| clay | #BD765E | one consequential mark per slide: the row number, the unit, the keyword. Never body copy. |
| mist | #DCE8EE | the highlight underline that replaces italic accent words |
| hairline | #D7E2E8 | rules and card borders |
| muted | #566E7E | secondary copy |

- **Type:** Figtree 400–800 for everything; Manrope for Russian slides (Figtree's Cyrillic is thin). No script, no italic accent, no serif. Her voice is plain-spoken; the editorial move here is composition and the highlight underline, not a flourish.
- **No ghost numerals, no decorative geometry.** Proof objects (a number, a list, a comparison) carry the slide.
- **Masthead:** `GIGI MIRONOVA · DRE 02025393` left, series label right. **Footer:** `HOUSE SELLERS · EQUITY UNION` small, source note center, page count right. Her name outranks the lockup on every board; that inversion is half the concept.
- **Photo treatments:** `bleed` (colour held, darkened) for her listing photography and place; `duo` (band duotone) for documents and archival place. Framing per slide via `pos` / `scale` in `slides.json`, never global.
- **Slide kinds:** hook (photo, headline low) · stat (one number) · list (numbered evidence rows) · two (side-by-side comparison) · dark (the pause) · quote (duotone photo + one spoken line) · photo-fact (listing photo + white fact card) · cta (portrait + keyword). Repeat the character, not the layout.
- **Ratio:** roughly 2 photo slides + 1 dark + the rest paper per set, so ten sets in a feed read as one voice without reading as one template.

## Imagery and rights

- Unit 124 frames (`assets/listing-124/`): 7 of her 25 MLS photographs, mapped in `PROVENANCE.md`. She is the listing agent; **she confirms publishing rights before anything posts** (the rights are hers to grant, not ours).
- Place frames (`assets/place/`): CC0 / Public Domain Mark from the First Home Valley bank, provenance rows in `provenance.jsonl`. No attribution obligation on her feed. Photographs of people were deliberately not used (the pool has no usable portraiture); her own headshot is the only face.
- Her headshot: 512×512 from her Equity Union profile, used at 300px inside a bordered block. Ask her for the original.

## The ten sets

| # | Slug | Pairs with video | Series | Slides | Keyword | Ledger notes |
|---|---|---|---|---|---|---|
| 1 | c01-same-door | 1 | PROPERTY FILE 124 | 7 | 124 | $299,999 · $620 · $2,500 · 6.66% · $2,535 est, all VERIFIED/COMPUTED 2026-09-01; "estimate, not a quote" on slides 2 and 3 |
| 2 | c02-five-pages | 3 | THE CONDO FILE | 7 | HOA | No figures; her bio line on slide 6 exactly as published |
| 3 | c03-balcony-report | 6 | THE CONDO FILE | 6 | HOA | SB 410 VERIFIED; "inspection and repairs completed" is the listing's own line |
| 4 | c04-bill-after-closing | 7 | THE CONDO FILE | 6 | HOA | $60K is a forum anecdote, labeled on-slide; 12% / 40% is an illustration, labeled |
| 5 | c05-fees-go-down | 8 | THE CONDO FILE | 5 | HOA | "Almost never" is opinion; $620 VERIFIED |
| 6 | c06-sell-with-tenant | 11 | THE SELLER FILE | 6 | NET | Notice periods not stated; source line points to CAA guidance |
| 7 | c07-net-sheet | 14 | THE SELLER FILE | 6 | NET | $25K / "more than half" LIKELY, labeled on-slide as one broker's compilation |
| 8 | c08-who-holds-the-money | 16 | THE TRANSACTION, EXPLAINED | 6 | CLOCK | 3 business days, 1–3% = C.A.R. defaults VERIFIED; RU line on slide 5 is a draft for her |
| 9 | c09-three-clocks | 17 | THE TRANSACTION, EXPLAINED | 6 | CLOCK | 17/17/21 = C.A.R. defaults VERIFIED, "negotiable" on-slide |
| 10 | c10-first-home-ru | 19 | ПЕРВЫЙ ДОМ В США | 6 | DOCS | Entire set is Russian; **her native pass before it posts**; process only, no numbers |

## Caption pairing

Each carousel posts the day after its reel and reuses that video's Instagram caption from `SCRIPT-PACK.md` with one change: the first line becomes the carousel's slide-1 headline. Pairing: c01→Video 1 · c02→Video 3 · c03→Video 6 · c04→Video 7 · c05→Video 8 · c06→Video 11 · c07→Video 14 · c08→Video 16 · c09→Video 17 · c10→Video 19.

## Banlist check (carousel engine + KIT runbook)

- No stock people, no posed families: PASS (no human frames except her headshot)
- No emoji as design elements: PASS
- No gradients except photo scrims: PASS
- No drop shadows: PASS (removed from the inherited tokens)
- No clip art: PASS
- No text touching edges: PASS (66px gutters, checked on the grid)
- One idea per slide: PASS by construction (one kind per slide)
- Square corners: PASS
- Max 2 typefaces: PASS (Figtree; Manrope only on RU slides)
- Fair-housing lint on every slide's copy: see `PIPELINE-READOUT.md` for the run receipt

## What would change with her input

- Her own photography of the unit at the door, the balcony, the pool (replaces nothing, adds warmth).
- The unit's actual reserve-study percentage and the delinquency figure: slides c02-5 and c04-5 would carry real numbers instead of the frame.
- Her correction of the Russian sets (c08-5, all of c10).
- Her verdict on the register: if she wants more edge, the dark "pause" slides are where it goes.
