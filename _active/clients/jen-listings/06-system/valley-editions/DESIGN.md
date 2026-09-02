# Valley Editions — design system v1 (2026-09-02)

The place-magazine surface for @_jiing. A series someone publishes, edition by edition, about the Valley, with the price signal inside and her door open at the end. Grammar extracted from six Canva templates Farrice chose (CANVA-GRAMMAR.md holds the numbers); palette and voice are hers. Generator: `editions.py`. Living doc; update in place.

## 1. Canvas and constants
- 1080 × 1350 (feed). Reels later at 1080 × 1920 with the same tokens.
- **Left gutter 108px** (10%). Every start-aligned text block sits on it.
- **Masthead row** top at 6–8% height. **Footer row** at 93% height.
- **One idea per frame. One headline. One accent. One photo** (or one pair).

## 2. Palette (hers; no yellow, no orange)
| token | value | use |
|---|---|---|
| ink | #1E3A5F | never on photos; reserved for paper pages if ever |
| cream | #F7F5F2 | headline base, body on dark |
| headline-gradient | #C9D4E2 → #EEF2F7 → #FFFFFF, 135° | the vintage-gem headline fill in the template's yellow slot (pale steel to white; ivory retired 2026-09-02, read flat) |
| accent | #C9D4E2 | doodles, pill stroke, sparkle: the one accent color, in the yellow's role |
| steel | #4C7CA8 | never on photos; tiny labels on paper only |
| white | #FFFFFF | body copy, pills, rules |
| wash | #0F141E | the gradient color over photos |

## 3. Type (three families, never a fourth; Playfair retired 2026-09-02 after Farrice's verdict on the first render)
| role | face | size | notes |
|---|---|---|---|
| headline | Instrument Serif 400, italic for the connector (the template's tall condensed serif; Playfair read generic) | 150–190px cover, 106px interior statement, 93px grid entry | 1–4 words, two lines max, `fit()` never lets a line wrap; the templates' faces run ~0.31em/char and Playfair ~0.5em, so fitted sizes land at roughly three-quarters of the template's number, and a two-line D1 headline is capped to end above the pill (`headline_size()`) |
| connector | Instrument Serif italic | 40–50% of the headline size | one short word ("this is", "the", "for", "in") bridging two headline clauses |
| masthead / eyebrow / footer / pill / label | Instrument Serif caps, tracking −0.01em (the template sets every role in one face; Jost caps survive only in D2/D4/D5 grammars) | 24–28px | "JEN SANTULAN · THE VALLEY", "TARZANA · EDITION 01", "@_JIING", "01 / 05" |
| subline / body | Instrument Serif 400 on D1 pages (28–30px, lh 1.35); Jost 300 on D2/D4/D5 | 26–40px | 1–3 short lines, never a paragraph |
| hand | Caveat 500 | 44–56px | the one handwritten line ("my DMs are open →"), never a headline |

## 4. Wash overlay
Black-to-transparent linear gradient over every photo, light enough that the photo carries the frame: cover `wash 60/55/55 → 0% at 71%`; interior/close `55/48/46/34%` (the first render's 60/55/55/42 read murky), rotated so the dark end sits at the headline's corner. Interior pages that carry a tall headline use the plateau: `60 / 55 / 55 / 42%`. Optional 10% grain rect on every page (Design 5's move) for the vintage editions.

## 5. Accents
One per frame (the cover carries the template's two: smiley + arrow with its long tail), accent #C9D4E2, hand-drawn SVG, 7px stroke: an arrow, a smiley, a sparkle, a ring badge. Off-axis by design: 7° on a stripe, −3° on an accent word. Never two accents on one frame.

## 6. Page archetypes
| archetype | from | what it is | Jen's use |
|---|---|---|---|
| **cover / gem** | D1 | eyebrow top-left, italic-connector + big serif headline lower-left third (ivory gradient), subline under it, handle pill, one accent | edition covers, the Attract district |
| **cover / stack** | D3 | two-word headline stack (word 2 bold) in a corner, italic connector at the break, one bold-italic quote line, credit in the opposite corner | edition covers, alt take; listing features |
| **moment** | D2 | short headline word top-left, three staggered body lines down the page, alignment mirrors page to page | "small true things about this neighborhood this month" |
| **spot** | D1/D4 | place-name headline, rounded-30px photo pair at 66% height, place label, one body sentence | a street, a coffee line, a park, with her photo of it |
| **grid** | D5 | canvas split into two 50% halves, each a numbered entry: eyebrow "01 — NAME", place headline 93px, one line, hours/price line | "what $X buys here": two homes, two numbers, no addresses |
| **statement** | D3 | two-word stack alternating corners, body opposite, wash points away | Position district: "Just Breathe." "Not Your Number." "Send the Street." |
| **big initial** | D6 | each headline word = a giant sans initial + the rest in serif, one baseline; eyebrow centered mid-page, body centered low | alt covers; a "Tarzana / this month" masthead move |
| **close / index** | D1/D5 | centered, no photo panels: the edition's index (01–05 recap) or the door line, handle, "next edition" | her verbatim close + the open door, every edition |

## 7. Edition shape (5–6 frames)
cover → moment → spot → grid (the price signal) → statement or spot → close/index. Every edition names a neighborhood and a month. The price signal lives on the grid frame; the door lives on the close.

## 8. Photo rules
- Her face only from real photos (Drive 03, Facebook profile album). Never AI.
- Places: her camera roll first, then AI Valley plates through the style vault with the realism lint on, then the cleared pool.
- Full-bleed photo needs negative space where the type goes (sky, wall, out-of-focus foliage). Legibility rule from ENGINE-V2 §6 stands.
- Nothing warm-orange in the grade; cool-neutral or golden-natural only.

## 9. What stays from the copy engine
Plain words with punch, one job per frame, her verbatim close, fair-housing floor, realism gate, no other broker's address on a frame, "buying or selling" in the ask, never "your first home." The job of every frame: a DM from someone willing to be educated, qualified in the reply layer.

## 10. Plate slots and fact panels (2026-09-02)
- A frame whose photo does not exist yet renders a **labeled slot** (`plate_bg`, `plate_inset`): a flat dark gradient with "photo slot · plate X" and the shot brief. Nothing on a frame pretends to be a photo. Plates are AI Valley plates through the style vault with the realism lint, cost gate first, never a photo of the actual business presented as such.
- A photo panel whose only honest fill would be another broker's listing photo becomes a **fact panel** (`fact_panel`): same 30px radius and hairline, a number in the ivory gradient, one line under it. Edition 01 frame 4 carries "sold in august · $840K–$950K" this way.
- Accents never cross a person: the D1 cover stripe and the D4 doodle drop when a person sits in that corner (`stripe=False`; `fill` implies no doodle).

## 11. Edition 01 (Tarzana, September 2026)
Frames and copy: `edition-01/CONTENT-PACK.md` · photos: `edition-01/PHOTO-PLAN.md` · facts: `edition-01/RESEARCH-PACK.md` · renders: `out/edition-01/` · canvas: `out/edition-01/canvas/` (`python3 editions.py canvas` rebuilds and re-checks the seeded page; republish to the same artifact). Commands: `python3 editions.py edition01` · `sheet` · `canvas`.
