# Canva Grammar Extraction — 5 Templates → HTML Design System

All canvases 1080×1350 except Design 2 (1080×1440, noted). % = left/top/width/height as share of page W/H. Font size in px (Canva pt = px here). Read via `read-design` structured JSON, `open_transaction:true`. No edits made.

---

## DESIGN 1 — DAHUD1-FGgs "Yellow Vintage Cafe & Restaurant Local Gem Carousel" (5 pages, 1080×1350)
Font A = `YAFcfq7XuZE,0` (italic-capable serif/script, used for EVERY text role in this design — headline, masthead, subline, handle).

### Page 1 — Cover
| Role | Text | px | Wt | It | Color | LH | LS | L% | T% | W% | H% | Rot | Op |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| masthead | "Cafe & Restaurant \nEdition 1" | 24.28 | normal | no | #ffffff | 1.4 | -0.087 | 5.6 | 7.2 | 24.1 | 4.5 | 0 | 1 |
| headline | "Hidden Gem\nin " (italic) + "New York City" (upright), same block | 165.97 | normal | mixed | #ffe477 | 0.75 | -0.087 | 5.3 | 16.6 | 73.3 | 23.9 | 0 | 1 |
| subline | "Local's hidden gem cafés range from calm work-friendly…" | 26.35 | normal | no | #ffffff | 1.4 | 0 | 5.3 | 38.4 | 55.4 | 5.0 | 0 | 1 |
| doodle-accent | badge shape (recolored #ffeb95) | — | — | — | — | — | — | 5.3 | 48.0 | 11.6 | 5.6 | 0 | 1 |
| handle pill | "@reallygreatsite" in rounded-arrow badge | 24.28 | normal | no | #ffffff | 1.4 | -0.087 | 53.1 | 20.4 | 30.0 | 5.2 | 0 | 1 |
| frame bar | decorative stripe (recolored #ffeb95) | — | — | — | — | — | — | 27.1 | 91.9 | 64.8 | 3.1 | 6.94 | 1 |
| frame bar 2 | small badge stripe (#ffeb95) | — | — | — | — | — | — | 5.3 | 88.8 | 20.0 | 6.5 | 0 | 1 |
| wash overlay | gradient: #000 60%@0, #000 43.5%@0.5, #fff 0%@1, rot180 | covers L0 T0 W100% H71.1% | | | | | | | | | | | |

Background photo: `isMediaReplaceable:true`, imageBox top -134.3, W100%, H119.9% (bleeds past frame top).

### Pages 2–4 — Interior (inset-photo pair), same geometry, only text/image content differs
| Role | Text (varies by pg) | px | Color | Align | L% | T% | W% | H% |
|---|---|---|---|---|---|---|---|---|
| masthead | "Cafe & Restaurant \nEdition 1" | 24.28 | #ffffff | center | ~33-35 | 7.2 | ~24-27 | 4.5 |
| headline | pg2 "Borcelle Place\nCafe & Studio" / pg3 "Lake Coffee by Fradel and Spies" / pg4 "Salford Coffee\nand Pastry Center" | 165.33-165.97 | #ffe477 | center | 9.2-15.0 | 23.8-34.6 | 69.9-78.3 | 23.9-24.5 |
| handle pill | "@reallygreatsite" | 24.28 | #ffffff | center | 33.3 | 41.6 | 30.0 | 5.2 |
| subline | "Local's hidden gem cafés range from…" | 26.35 | #ffffff | center | 20.6 | 50.0 | 55.4 | 4.9 |
| doodle-accent | small icon (recolored #ffeb95) | — | — | — | 46.7 | 12.3 | 3.3 | 2.7 |
| frame badge | bottom stripe (#ffeb95) | — | — | — | 42.5 | 94.1 | 11.6 | 3.8 |
| inset photo L | isMediaReplaceable, cornerRounding 30 | — | — | — | 8.3 | 66.1 | 40.0 | 19.4 |
| inset photo R | isMediaReplaceable, cornerRounding 30 | — | — | — | 51.6 | 66.1 | 40.0 | 19.4 |
| wash overlay | 4-stop: #000 60%@0 / 55%@.33 / 55%@.66 / 42.5%@1, rot180 | full-bleed | | | | | | |

### Page 5 — Close/CTA
| Role | Text | px | Color | Align | L% | T% | W% | H% |
|---|---|---|---|---|---|---|---|---|
| headline | "Follow for\nNext Edition" | 165.97 | #ffe477 | center | 9.2 | 34.6 | 78.3 | 23.9 |
| handle pill | "@reallygreatsite" | 24.28 | #ffffff | center | 33.3 | 53.3 | 30.0 | 5.2 |
| masthead | "Cafe & Restaurant \nEdition 1" | 24.28 | #ffffff | center | 31.1 | 7.2 | 34.5 | 4.5 |
| doodle-accent | badge (#ffeb95) | — | — | — | 45.1 | 86.4 | 11.6 | 5.6 |
No inset photos — CTA page drops photo panels entirely.

---

## DESIGN 2 — DAHUD4Cq4uw "Yellow and Black Modern Travel Moments Carousel" (6 pages, **1080×1440**)
Font B1 = `YAEp6dGWhEw,0` (upright sans — masthead/body/slide-counter). Font B2 = `YAEz2L9phwY,0` (heavier sans, tight LS -0.031, used only for the rotated accent word).

Chrome present on all 6 pages (unchanged position): 2 thin white rules top (T2.4%, T8.6%), 2 thin white rules bottom (T91.3%, T97.5%); masthead "Salford & Co." L5.9% T4.4% px26.67; brandmark icon top-right L87.8% T4.9%; handle "@reallygreatsite" bottom-left L5.9% T93.4% px26.67; "slide 0X" counter bottom-right L73.6% T93.4% (end-align).

| Pg | Headline word(s) | px | L%/T% | Accent word (rotated -3.05°, font B2) | px | L%/T% | Body lines (px37.33, font B1) top% |
|---|---|---|---|---|---|---|---|
| 1 (cover) | "Small Travel Moments" (center) | 147.73 | 15.9/25.2 | "I'll Always Remember" (center) | 191.71 | 17.5/51.8 | — |
| 2 | "Quiet" (start) | 147.73 | 10.0/11.5 | "Mornings" | 191.71 | 26.2/16.5 | 66.4, 75.5, 84.0 (last wide, W77.8%) |
| 3 | "Local" (start, bg flipX mirrored) | 147.73 | 10.0/15.1 | "Streets" | 191.71 | 26.6/22.0 | 40.1, 51.3, 77.2 |
| 4 | "Simple" (start) | 147.73 | 10.0/12.6 | "Meals" | 191.71 | 35.0/18.4 | 40.1 (start), 57.9 (end, L44.9%), 77.2 |
| 5 | "A Simple" (start) | 138.67 | 10.0/15.0 | "Realization" (end-align) | 191.71 | 35.5/21.2 | 34.9 (end, L46.4%), 68.3, 78.9 |
| 6 (close) | "Travel isn't always about" (start) | 147.73 | 10.0/15.1 | "big adventures" (start) | 191.71 | 25.0/38.9 | 72.7, 83.4 (2 closing lines only) |

Body text always L10% (left=108px) except when explicitly end-aligned. Doodle icon pairs (small recolored rects, ~40-92px) flank each headline/accent pair on every page.

---

## DESIGN 3 — DAHUDwHv30c "White and Green Simple Elegant Holiday Instagram Post" (6 pages, 1080×1350)
Font C1 = `YAFdJhem5V8,1` (headline, weights normal/semibold/bold + italic connector). Font C2 = `YAGzXW3gftg,0` (lorem-ipsum placeholder body, regular).

Chrome on all 6 pages: masthead "Studio Shodwe" L10.8% T8.0% px28 bold; tagline "Break free. Go explore" opposite top corner, px28 italic; footer credit "post by:" (px26.67) + "NAME" (px34.67 bold) in bottom corner, mirrored to whichever side the headline is NOT on.

| Pg | Headline stack (word1 normal / word2 bold) | px | Corner (L%/T%) | Connector word (italic, ~44-50% headline size) | Lorem body (font C2, px28) L%/T% |
|---|---|---|---|---|---|
| 1 (cover) | "Escape" / "Routine" | 178.96/198.34 | 10.0/20.3 | "the" (px78.09, end, L59.2 T28.1) | quote line only (bold italic px32, L11.7 T51.4) |
| 2 | "Plan Less," / "Feel More" (end-align, mirrored bg) | 106.67 | 39.6/57.0 | — | 47.1/79.1 |
| 3 | "Wake Up " / "Early" (start-align) | 106.67 | 10.0/20.8 | — | 55.7/23.8 |
| 4 | "Choose" / "Experiences" (end-align) | 106.67 | 32.6/58.5 | — | 35.4/81.2 |
| 5 | "Rest Is" / "Productive" (start-align) | 106.67 | 10.0/37.2 | — | 10.0/59.9 (start-align) |
| 6 (close) | "Follow" / "More" (end-align, bold) | 200.63/189.8 | 26.7/21.3 | "for" (px87.55, end, L34.5 T37.9) | 3 social-icon glyphs bottom (L71.4/78.3/84.4 T54.4) + credit mirrored right |

Wash: vertical black→transparent linear gradient, rotation flips 90°/180°/-90° per page to always point away from the headline corner (light-source-at-headline logic).

---

## DESIGN 4 — DAHUD7M8w1U "Green and Yellow Simple Local Gems Carousel" (5 pages, 1080×1350)
Font D1 = `YAFcfq7XuZE,0` (headline — **same fontRef as Design 1's headline/masthead font**). Font D2 = `YAGL32gJeyU,0` (eyebrow label + handle, tracked, LS -0.111). Font D3 = `YACgETiWKS8,0` (body sentence, LS -0.044).

### Page 1 — Cover
eyebrow "the city guide" px50.67 #ffde59 L10/T5.8 (font D2) → headline "My Favorite Local Gems" px186.84 #ffde59 L10/T16.1 W60.9 (font D1) → divider rule L10/T53.9 W40 → body "From cozy cafés to hidden art…" px40 #ffde59 L10/T46.8 W42.6 (font D3) → handle "@reallygreatsite" px50.67 #ffffff L10/T87.6. Doodle quote-icon L58.9/T30.0 W18.7/H19.1; rotated doodle (76.5°) L75.0/T80.9.

### Pages 2–4 — "Spot" pages
| Pg | Order | Headline (place name) | px | L%/T% | Photo panel(s) | Place label | Eyebrow tag position |
|---|---|---|---|---|---|---|---|
| 2 | body-above-headline | "Cozy Café Vibes" | 186.84 | 10.0/22.2 | L26.3/T22.2 (W47.4/H15.2) + L67.6/T72.4 (W28.5/H33.3) | "Rimberio Cafe" L15.6/T49.1 | bottom-left T87.6 |
| 3 | headline-above-body | "Hidden Street Art" | 186.84 | 10.0/6.5 | L42.6/T6.5 (W19.2/H16.4) + L41.8/T47.3 (W40/H5.4) | "Borcelle Street" L15.6/T77.2 | bottom-RIGHT (end-align) T47.8 L61.9 |
| 4 | headline right-aligned | "Secret Park Corner" | 186.84 | 30.4/6.0 (end) | (marker icon L54.8/T31.5) | "Rimberio Park" L60.4/T34.1 | bottom-right (end) T87.6 L62.3 |

Body sentence px40, color #ffde59, font D3, ~42-52% width, positioned opposite the eyebrow's vertical half.

### Page 5 — Close
Centered: eyebrow "the city guide" L36.0/T8.0 → headline "Follow for More" px186.84 center L20.0/T36.1 W59.9 → url "www.reallygreatsite.com" px40 center L24.1/T88.5 (font D3). No photos.

---

## DESIGN 5 — DAHUD1TJ_EA "Beige Black and White Urban Travel City Guide" (5 pages, 1080×1350)
Font E1 = `YAFcfnjI7Vk,0` (big serif headline). Font E2 = `YAEnS2G4JLg,0` (eyebrow/label/address/hours/body, tracked caps, used everywhere except the two headline fonts). Font E3 = `YACkoPnfjjY,0` (lighter serif subhead accent, page 1 only: "A Short Guide to").

**Grain wash (every page, identical):** a full-bleed rect, `mediaId MADA650_gto`, **opacity 0.1**, positioned L-1.2% T-0.8% W102.4% H101.7% — a constant texture/grain overlay independent of the black-gradient wash.

### Page 1 — Cover
ring badge (stroke-only circle, no fill, 2px stroke #fff7d7) L36.1/T8.0 W27.8/H7.2 → eyebrow "THE LOCAL SIDE" centered inside ring L40.7/T10.4 px26.67 (E2) → subhead "A Short Guide to" center L31.7/T31.3 W36.5 px81.91 (E3) → headline "Everyday City Finds" center L17.4/T37.9 W65.1 px186.67 (E1) → body center L27.4/T74.4 W45.3 px26.67 (E2) → footer tag "CITY GUIDE / LOCAL EDIT / 01" center L33.7/T89.6 px26.67.

### Pages 2–4 — "Grid" pages (two 50%-height photo halves, each a self-contained numbered entry)
Top half (T0-50%) and bottom half (T50-100%) each carry: eyebrow "0X — NAME" px26.67, headline/place-name px93.33 (E1), address "123 Anywhere St., Any City" px26.67, hours (bold px40), body px26.67, one divider rule under the eyebrow. Alignment mirrors: start-align entries sit at L10%; end-align entries sit right-justified around L55-62%, W34-38%.

| Pg | Top-half entry (align) | Bottom-half entry (align) |
|---|---|---|
| 2 | "01 — MORNING COFFEE" / "Corner Café" (start, L10/T8-35.4) | "02 — TAKE THE SIDE STREET" / "Local Walk" (end, L52-58/T72.2-84.9) |
| 3 | "03 — LOCAL TABLE" / "Harvest Kitchen" (end, L39-77/T8-35.4) | "04 — QUIET CULTURE" / "Open Pages" (start, L10/T58-85.4) |
| 4 | "05 — Outdoors" / "Public Park" (start, L10/T8-35.4) | "06 — SHOPPING" / "Cornerstone Retail" (end, L57-77/T58-85.4) |

Divider rule under each eyebrow: T26.4%/W52.1% (top half), T76.4%/W52.1% (bottom half, mirrored offset).

### Page 5 — Close / numbered index
ring badge + eyebrow "THE LOCAL EDIT" repeated exactly as page 1 header (L36.1/T8.0). 5 divider rules stacked every ~121px = T29.4/38.4/47.3/56.3/65.2%, each spanning L10-90%. 6 index rows, label bold px46.67 left-start ("01 Coffee"…"06 Shopping"), value px26.67 right-end (place name), rows at T22.9→67.6%. Closing statement centered "A LITTLE CITY GOES A LONG WAY." px33.34 bold T81.9, subtext centered px26.67 T87.3.

---

## Layout Archetypes (page numbers per design)

- **D1**: cover (pg1, headline lower-left ~T17-40%, wash top-heavy) → inset-pair interior (pg2-4, centered headline stack + 2 rounded-30px photos side-by-side at T66%) → close (pg5, centered CTA, no photos).
- **D2**: cover (pg1, centered headline + oversized rotated accent) → "moment" pages (pg2-5, short headline word top-left T11-15% + huge -3.05° rotated accent word + 2-3 staggered body lines down the page, alignment mirrors L/R across pages) → close (pg6, full sentence headline + accent + 2 closing lines).
- **D3**: cover (pg1, 2-word headline stack lower-left third + italic connector word + bold-italic quote + credit) → statement interior (pg2,3,4,5 — 2-word headline stack alternating left/right corner, mirrored bg image, lorem body on opposite side) → close (pg6, 3-word headline "Follow"+italic "for"+"More" right-aligned + 3 social icons + credit).
- **D4**: cover (pg1, eyebrow+headline+divider+body+handle stacked left, T5.8-87.6%) → spot pages (pg2-4, headline+photo-panel(s)+place-label+body, order and alignment alternate by page) → close (pg5, fully centered CTA, no photos).
- **D5**: cover (pg1, ring badge+eyebrow+subhead+headline+body+footer tag, all centered) → grid pages (pg2-4, canvas split into 2 equal 50%-height photo halves, each a numbered listing with mirrored start/end alignment) → close/index (pg5, ring badge+eyebrow repeated + 6-row numbered index with divider rules + centered closing line).

## Shared Grammar Across All Five

- **Masthead/eyebrow row**: pinned top of frame at T4.4-10.4% (px24.28-50.67). Constant across every page of a given design.
- **Left gutter**: **108px (10% of 1080w)** is the dominant constant — used by D2, D3, D4, D5 for every start-aligned text box. D1 is the outlier at 57.49px (5.3%).
- **Bottom margin**: handle/footer/credit rows sit at T87.6-97.5% (i.e. ~33-172px from the bottom edge) in all five designs.
- **Headline scale**: 147.7-200.6px for hero/cover headlines, always 1-4 words, frequently split across 2 lines ("word1\nword2" or word1-then-bold-word2 stack).
- **Italic-fragment move**: a single short connector word ("the", "for", "in") rendered in italic at **~40-50% of the headline's own point size**, tucked at the line-break to visually bridge two headline clauses. Present in D1 (embedded mid-headline) and D3 (as a separate small text box between the two headline words).
- **Subline/body scale**: eyebrow/label text 26.6-28px (D2, D3, D5) except D4's eyebrow at 50.67px (outlier, sized to match its headline family). Body sentence copy 26.35-40px, line-height 0.98-1.4.
- **Wash overlay recipe**: every design lays a black→transparent linear gradient over the photo behind text. Standard 2-stop: `#000 60%@0 → transparent@1`. Multi-stop plateau version (D1 interior, used to keep dark tone across a taller headline block): `#000 60%@0, #000 55%@.33, #000 55%@.66, #000 42.5%@1`. Rotation (0/90/180/-90°) always points the dark end at the text block's corner. D5 adds a second, independent **10%-opacity full-bleed grain-texture rect** on every page — not present in D1-D4.
- **Accent/doodle placement**: small icon/badge accents run 36-125px square, either flanking the headline (D1: below-left; D4: above-right) or as paired icons bracketing body copy (D2). Rotation on accents is deliberately off-axis: 6.94° (D1 stripe), 76.5° (D4 icon), -3.05° (D2's giant accent word itself, not just a small icon).
- **Inset/photo panels**: D1 is the only design using **rounded corners (cornerRounding 30px)** on photo panels, always in a side-by-side pair at ~40% width / 19% height each, positioned at T66%. D4 and D5 use **hard-edged (0px corner), full-bleed or full-width photo splits** instead — D5 splits the whole canvas into two 50%-height halves; D4 uses smaller irregular framed rectangles.
- **Cover → interior → close changes**: cover pages always carry the single largest headline + one body sentence + brand/handle row. Interior pages either (a) keep the masthead and swap the headline for place/moment copy while adding photo panels (D1, D4, D5) or (b) drop photos entirely and stack short staggered body lines under a smaller headline (D2, D3). Close pages universally drop photo panels and center the final CTA text; they end on a handle/URL (D1, D4), a social-icon row + credit (D3), or a numbered recap index (D5).

## Fonts (by fontRef)

| fontRef | Design(s) | Roles | Weights seen | Italic? | Guessed family (unverified — thumbnails not pulled) |
|---|---|---|---|---|---|
| `YAFcfq7XuZE,0` | D1 (all text), D4 (headline only) | headline, masthead, subline, handle (D1); headline only (D4) | normal | yes | Vintage script/serif display face — GUESS, based on "Vintage Cafe" theme + italic capability spanning the whole design in D1 |
| `YAEp6dGWhEw,0` | D2 | masthead, body, slide-counter, headline word | normal | no | Clean geometric sans (e.g. Poppins/Montserrat-class) — GUESS |
| `YAEz2L9phwY,0` | D2 | oversized rotated accent word | normal | no | Heavier condensed sans, same family group as YAEp6dGWhEw likely a bold cut — GUESS |
| `YAFdJhem5V8,1` | D3 | headline stack, connector word, masthead, tagline, credit | normal/semibold/bold | yes (connector + tagline) | Modern grotesque sans with true italic + multiple weights — GUESS |
| `YAGzXW3gftg,0` | D3 | lorem-ipsum body paragraph | normal | no | Serif text face (placeholder body copy) — GUESS |
| `YAGL32gJeyU,0` | D4 | eyebrow label, handle, place-name | normal | no | Tracked sans caps, LS -0.111 — GUESS |
| `YACgETiWKS8,0` | D4 | body sentence | normal | no | Sans body face, LS -0.044, distinct from D4's eyebrow font — GUESS |
| `YAFcfnjI7Vk,0` | D5 | big headline | normal | no | Serif display headline, different id from D1/D4's serif but same visual category — GUESS |
| `YAEnS2G4JLg,0` | D5 | eyebrow, address, hours, body, index labels | normal/bold | no | Tracked sans caps (utility text face used everywhere in D5 except the two headline fonts) — GUESS |
| `YACkoPnfjjY,0` | D5 | subhead accent "A Short Guide to" (page 1 only) | normal | no | Lighter-weight serif, distinct from the bold headline serif — GUESS |

No read-design calls failed or truncated; all pages of all 5 designs returned full structured `design_content`.

---

## DESIGN 6 — DAHUEETAQQs "Brown and Beige Local Cafe City Guide Carousel" (5 pages, 1080×1350) — read 2026-09-02
Font F1 = `YAFcfq7XuZE,0` (the D1/D4 serif; here the headline body letters, italic connector, "Try this" labels). Font F2 = `YAEz2L9phwY,0` (D2's heavy sans; here ONLY the giant initial letters on the cover). Font F3 = `YAFdJiLU_Ko,0` (body sentence + place name, LS -0.044, lh .98). Font F4 = `YAEblDjyZs8,0` (eyebrow "the city guide", LS -0.071). All text #ffffff. **No gradient/wash element on any page** — the templates' photos are dark enough on their own; a wash is ours to add.

### Page 1 — Cover: the "big initial" move
Each headline word is split into a giant sans initial (px287.6, end-aligned, lh .81, LS -0.071) and the rest of the word in serif (px211.9, start-aligned) overlapping at the baseline. Two rows:
| piece | text | px | L px | T px | W px | font |
|---|---|---|---|---|---|---|
| row1 initial | "f" | 287.6 | 128.8 | 50.2 | 287 | F2 |
| row1 rest | "avorite" | 211.9 | 443.8 | 95.5 | 467 | F1 |
| row2 initial | "l" | 287.6 | 30.3 | 234.8 | 221 | F2 |
| row2 rest | "ocal" | 211.9 | 279.8 | 280.1 | 320 | F1 |
| row2 initial 2 | "c" | 287.6 | 545.7 | 234.8 | 218 | F2 |
| row2 rest 2 | "afe" | 211.9 | 791.3 | 280.1 | 258 | F1 |
| eyebrow | "the city guide" | 58.9 | 293.2 (center, W493.5) | 717.5 | 493 | F4 |
| body | "Cozy corners, perfect brews…" | 40 | 130.6 (center, W818.7) | 1155.2 | 819 | F3, lh .98 |
Background photo imageBox top −283 H1916 (bleeds far past the top). Serif letters in this face run ~0.31em/char (467px for 7 chars at 212px); Playfair runs ~0.5em/char, so the same words fit at ~0.76× the size.

### Pages 2–4 — "Try this" spot pages (identical geometry, content varies)
| role | text | px | L% | T% | W% | align | font |
|---|---|---|---|---|---|---|---|
| brandmark | small recolored icon | — | 10.0 | 8.0 | 4.8 | — | — |
| place name | "Borcelle Cafe" | 40 semibold | 16.3 | 8.7 | 23.6 | start | F3 |
| eyebrow | "the city guide" | 45.3 | 52.9 | 8.7 | 37.1 | end | F4 |
| detail block | "*Try this*: Almond croissant + flat white ⏎ *Price Range*: $5 - $25" (labels italic) | 40.06 | 10.0 | 26.3 | 46.0 | start | F1 |
| headline | "*The* ⏎ Cozy Classic" (connector italic, same size) | 211.9 | 18.3 (pg2) · 15.5 (pg3) · 4.7 (pg4) | 46.2 (pg2) · 50.0 (pg3, pg4) | 71.7 · 74.5 · 85.3 | end | F1, lh .81 |
| body | one sentence | 34.7 | 24.0 | 78.8 (pg2) · 81.4 (pg3, pg4) | 66.0 | end | F3, lh .98 |

### Page 5 — Close
headline "*Follow* ⏎ For More" px211.9 center L16.5 T8.0 W67.1 → question line italic px40 center L24.3 T55.8 W51.4 ("What's your go-to local café? … Tag them below") → eyebrow "the city guide" px45.3 center L31.4 T88.0. Background photo panned (imageBox left −942, W2022). No photos panels.

### What D6 adds to the shared grammar
- **Big-initial headline**: a word split into a giant sans initial + serif remainder, overlapped at the baseline; the one grammar where two type families share a word.
- **"Try this / Price Range" detail block**: a two-line italic-label spec block at L10% T26% — the natural slot for "beds / baths / lot" or "sold / days on market" on a real-estate page.
- **End-aligned headline + end-aligned body in the lower half** (T46–92%) with the identity row (place name + eyebrow) at T8.7%: the mirror of D1's centered stack.
- Confirms the shared constants: L10% gutter (108px), identity row at T8–9%, body 35–40px, headline ~212px in a condensed serif.
