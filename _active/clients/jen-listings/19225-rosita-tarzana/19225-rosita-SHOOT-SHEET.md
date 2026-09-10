# 19225 Rosita St, Tarzana — intro reel substrate (2026-09-10)

Deliverable: `SEND-TO-JEN-text.md` (forwardable) + `reel/19225-rosita-intro.mp4` (photo-motion, ENGINE-V2 §15 grammar). This sheet is the repo backup: strategy, facts, photo map, diagnostics.

## Strategy card (10 lines)

1. Tier: $4,800,000 → luxury → **Quiet Flex Elite Advisor**. Title Case on screen, thesis first, property as evidence, "let's talk strategy" closer.
2. Thesis the reel defends: at this scale builders go vertical; a 6,500 sq ft single-story on a flat half-acre south of Ventura is the rare configuration.
3. Buyers (life-logistics, fair-housing-safe): (a) the multigenerational household that needs a second kitchen and no stairs; (b) the entertainer who hosts at scale (motor court, outdoor kitchen); (c) the Encino/Calabasas shopper at $4–5M who has not driven west of Reseda Blvd.
4. Magic trifecta: single-story at 6,500 sq ft (pattern interrupt) · flat half acre south of the Boulevard (the real pitch) · guest quarters with own kitchen + 11-car motor court (bonus proof).
5. Honesty anchor: $738/sq ft sits inside the 2026 closed-sale band for 5,000+ sq ft Tarzana homes ($598–$875/sq ft; see facts). No "deal" framing exists; the frame is what-you-get.
6. Ambush 1: last sale $2,200,000 (2022-01-28), +118%. The 2021 listing described a 6bd/3ba ~3,603 sq ft house; this is a rebuild/expansion. Q&A prep only, never content.
7. Ambush 2: Zestimate $3,325,600 vs Redfin Estimate $4,772,176. Q&A prep only.
8. Contradiction caught: MLS kitchen field says "Tile Counters"; photos 10–14 show slab. Copy says "the island," never the material.
9. Rights: listing agents are Marty Azoulay (DRE 01234131) and Shane Zvulun (DRE 02129052), Equity Union. Jen is not on the listing. Same pattern as 5421 Bothwell → HOLD posting until Jen confirms she is cleared; address on the final frame is conditional on that.
10. Photo quality: web copies are 1024×682. The reel renders (2.8× upscale, softened by the gradient + motion) but the ship-grade render needs the shoot originals from Marty.

## Facts used on screen / in caption (all in `claims-ledger.json`, 24 VERIFIED)

| fact | label | source |
|---|---|---|
| $4,800,000 · 6 bd / 7 ba · 6,500 sq ft · 0.49 ac (21,379 sq ft) · 1 story · built 1952 · MLS SR26195670 | VERIFIED | Zillow JSON-LD + facts list, Redfin, 2026-09-10 |
| all 6 bedrooms + 7 baths on the main level | VERIFIED | Zillow facts ("Main level bedrooms: 6") |
| heated in-ground pool + spa · outdoor fireplace · guest/maid's quarters · 11 uncovered parking spaces · no garage listed | VERIFIED | MLS description + facts |
| outdoor kitchen (grill line, fridges, sink under a pavilion) | VERIFIED by photo | photos 50–51 |
| guest quarters have their own kitchen + living room | VERIFIED by photo | photos 52–59 (second living room, second kitchen with island + fridge, bedrooms 55–57, baths 58–59) |
| great room opens on pocket doors to the yard | VERIFIED by photo | photo 9 |
| south of Ventura Blvd | VERIFIED | geo 34.1559, −118.5517 (Ventura Blvd in Tarzana ≈ 34.168); 2021 listing text "south of Ventura Blvd" |
| flat lot | VERIFIED by photo + record | aerials 71–72, 2021 listing "Huge Flat lot" |
| $738/sq ft | VERIFIED (derived) | Zillow |
| open house Sat 1–4pm | LIKELY (date not shown) | Redfin, 2026-09-10 |
| 2026 Tarzana closed sales ≥5,000 sq ft: 19024 Sprague $5.25M/5,999 sf ($875) Jan · 4981 Amigo $4.10M/5,995 sf ($684) Mar · 4101 Clarinda $3.235M/5,380 sf ($601) Jul · 19739 Henshaw $3.05M/5,100 sf ($598) Feb | LIKELY (Redfin comp panel, not a CMA) | Redfin estimate panel, 2026-09-10 |
| nearby actives $2.7M–$5.5M at 4,400–8,100 sf ($507–$937/sf) | LIKELY (Zillow similar-homes panel) | Zillow, 2026-09-10 |
| listing agents Marty Azoulay + Shane Zvulun, Equity Union | VERIFIED | Zillow + Redfin |
| "only two flat lots on Rosita" | UNCONFIRMED — never used | 2021 listing agent claim |
| "detached" guest house | UNCONFIRMED — never used | aerial 71 is ambiguous; guest wing may be attached |
| year renovated | UNCONFIRMED (county shows 1973) — never used | Redfin |

## Photo map (Redfin CDN order, `photos/rNN.jpg`; contact sheets in scratchpad only)

0–2 motor court (twilight/day) · 3 front door · 4 entry hall · 5–9 great room, 9 = pocket doors open · 10–14 kitchen · 15–18 pantry/laundry/bar · 19–21 dining · 23–48 bedrooms/baths/closets · 49 side yard · 50–51 outdoor kitchen pavilion · 52–59 guest quarters (living, kitchen, 3 bedrooms, baths) · 60–66 covered patios, 66 outdoor fireplace · 67–70, 73–74 pool + spa (73 aerial, 74 twilight) · 71–72 aerials, 72 = lot outline.

Reel beats use 1 · 4 · 73 · 53 · 74 · 02. No faces in any photo; type never on a face.

## Render

```
cd _active/clients/jen-listings/04-deliverables/2026-09-01-september-carousels
python3 build_reel.py ../../19225-rosita-tarzana/reel/19225-rosita-intro.json
```
Output: `_active/clients/jen-listings/19225-rosita-tarzana/reel/19225-rosita-intro.mp4` (gitignored; Drive holds the copy). Re-render with originals by replacing `photos/rNN.jpg` at the same names.

## Diagnostics

- Fetch rung: Browser pane DOM read of Zillow (bot-check overlay left untouched) + Redfin page + Redfin CDN for photos. $0.
- Market research: `research.py --depth standard` returned a PLANNED runbook only (no data, $0); comps come from the Redfin/Zillow panels, labeled LIKELY.
- Ledger: `listing_intel.py` parse → diff → ledger. 0 contradictions detected by code (the counter-material contradiction is photo-vs-MLS, added by hand above); 1 risk (price-jump ambush).
- Blind Bar (self-check vs 5421 Bothwell convert reel + Armida "true privacy" hook): thesis-first, one fact per beat, Title Case, address+price last — same species. PASS, 0 repair rounds.
