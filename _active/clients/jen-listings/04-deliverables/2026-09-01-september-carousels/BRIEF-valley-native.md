# Executor brief: "Valley Native" visual system for Jen Santulan (@_jiing)

Confirmed by Farrice 2026-09-01. You are building ONE new visual direction ("D · valley native") as a complete 7-slide carousel plus a one-page visual rulebook. Design execution only: the copy is final.

## What it must do

Make a first-time buyer scrolling at midnight feel: *she's from here, she knows every block, she's the one you text.* Fix feed fatigue: her grid today is a cream-and-navy column that blurs together at thumbnail size. The fix must compound (a system, not a one-off).

## Hard constraints

- **Palette, fixed:** navy #1E3A5F (deep #16304F ok), steel blue #4C7CA8, soft blue #C9D4E2, cream #F7F5F2, hairline #E0DBD2, grey #6B6C70. **Nothing warm. No orange, no terracotta, no red, no yellow, no tan. Ever.** If you need a second color, it is steel or soft blue.
- **Her existing look, keep it:** cream/white grounds, deep-navy hand-drawn line icons (keys, sold house, heart envelope), Figtree sans + Playfair Display serif italic accent words, lowercase headlines, masthead "@_JIING · FIRST-TIME BUYER FILE", italic serif page number "n / 7". No House Sellers lockup on her personal carousels.
- **Field-notes energy, translated on brand.** The composition ideas from direction B are wanted: layered/tilted photo prints, annotations, place markers, a recurring signature. The paper/tape/red-pencil skin is NOT wanted. Translate: annotations become navy line-drawn arrows and circles (the way her grid already draws icons), prints get thin navy or cream borders, the stamp is a navy line-icon "from the valley" mark.
- **Real photography only**, from `img/` and `img/jen/`. Reference by bare filename in `<img src="name.jpg">` (double quotes). Jen photos: `jen-porch-vannuys.jpg` (her on a Van Nuys porch), `jen-frontdoor.jpg` (her at a front door, waist-up), `jen-portrait.jpg` (headshot square). Place photos: `vannuys-blvd-2024.jpg`, `vannuys-valerio-2024.jpg` (both real Van Nuys Blvd, Oct 2024, portrait), `vannuys-street-scene.jpg`, `sfv-aerial-nara.jpg` (archival Valley aerial, b/w), `apartment-building-dusk-03.jpg`, `california-bungalow-00.jpg`, `front-door-house-00.jpg`, `house-key-lock-00.jpg`, `sunlight-through-window-floor-00.jpg`, `valley-street-01.jpg`, `palm-tree-sunset-city-02.jpg`, `suburban-neighborhood-aerial-02.jpg`.
- **Place devices:** a hand-drawn navy line map is welcome (the Valley grid: Ventura Blvd, Van Nuys Blvd, the 101/405/170; or the light-rail corridor). Street-sign typography for neighborhood names is welcome. Coordinates or zip codes as small tracked-caps labels are welcome. No emoji anywhere. No gradients, no drop shadows on type, no rounded cards, no stock-photo smiles that aren't hers.
- **Fair housing:** never "safe," "family," "great schools," "quiet neighborhood," or who a place is for.
- **Copy is final.** Use the condo set copy exactly as in the 7 existing artboards `Main.dc.html`, `C1S2.dc.html` … `C1S7.dc.html` (read them; the text lives in the HTML). Do not rewrite, shorten, or "improve" it.

## Format and conventions (match exactly)

- Read `gen_slides.py` and `gen_directions.py` first: same `HEAD` wrapper (keep `<script src="./support.js"></script>` exactly), inline styles only, 1080×1350 root div, `box-sizing: border-box`, `overflow: hidden`, flex/grid with `gap`, no external CSS. Fonts via the same Google Fonts `<link>` in `<helmet>`; you may add ONE more Google font family if a street-sign or stencil voice is essential (name it in the rulebook), max 3 families total.
- Write a new generator `gen_valley.py` in this folder that writes 7 artboards `DD1.dc.html` … `DD7.dc.html` (DD1 = cover, DD7 = close). Do not touch the other generators or artboards.
- Then run `python3 render_png.py` after adding your seven stems to its `ORDER` list (append `[(f"DD{i}", f"dir-d-0{i}") for i in range(1, 8)]`), and LOOK at every PNG you produced with the Read tool. Fix clipping, overlap, illegible text over photos, and any rule above you broke. Iterate until all seven pass. Photos must never make type unreadable: use a solid translucent navy scrim, never a gradient.
- Write `VALLEY-NATIVE-RULEBOOK.md` (one page): the 5 to 7 rules a future carousel inherits (where the photo goes, where the map/stamp goes, the annotation grammar, the dark-slide rhythm, the close-slide shape, what rotates per series so the grid never blurs). Include the fonts and the exact hex values. Plain language, no operator jargon; Jen could read it.

## Reference research

See `REFERENCES-valley-native.md` in this folder (appended before dispatch). Use it as evidence for which devices to borrow. Do not copy any reference's wording or logo.

## Return

Only the artifact: the seven `DD*.dc.html` files, `gen_valley.py`, `VALLEY-NATIVE-RULEBOOK.md`, and the seven rendered PNGs under `png/dir-d-0*.png`. Then a 10-line note: what the recurring signature is, what rotates per series, which two slides you'd want Jen's own photo swapped into first, and anything you could not verify.

no Chain, no finalize, no Notion, no Next Moves, return only the artifact.
