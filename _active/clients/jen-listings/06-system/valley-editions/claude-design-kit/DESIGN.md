---
version: alpha
name: Valley Editions · @_jiing
description: Jen Santulan's place-magazine carousel, "The Valley · <neighborhood> · Edition NN". One tall condensed serif in every role, a light wash over a warm real photo, thick hand-drawn doodles in one pale-blue accent, her face on the cover, her own close on the last frame. The Coffee & Contracts "Local Gem" carousel grammar, made hers.

colors:
  navy: "#1E3A5F"
  steel: "#4C7CA8"
  accent: "#C9D4E2"
  cream: "#F7F5F2"
  white: "#FFFFFF"
  wash: "#0F141E"
  headline-gradient: "linear-gradient(135deg, #C9D4E2 0%, #EEF2F7 40%, #FFFFFF 100%)"

typography:
  headline:
    fontFamily: "Instrument Serif"
    fontSize: 166px
    fontWeight: 400
    lineHeight: 0.78
    letterSpacing: -0.025em
  headline-italic:
    fontFamily: "Instrument Serif"
    fontSize: 166px
    fontStyle: italic
    lineHeight: 0.78
  masthead:
    fontFamily: "Instrument Serif"
    fontSize: 24px
    textTransform: uppercase
    letterSpacing: -0.01em
    lineHeight: 1.3
  pill:
    fontFamily: "Instrument Serif"
    fontSize: 25px
    textTransform: uppercase
  body:
    fontFamily: "Instrument Serif"
    fontSize: 28px
    lineHeight: 1.35
  label:
    fontFamily: "Instrument Serif"
    fontSize: 19px
    textTransform: uppercase
  hand:
    fontFamily: "Caveat"
    fontSize: 52px
    fontWeight: 500
  sans:
    fontFamily: "Jost"
    fontSize: 26px
    fontWeight: 500
    note: "only in the D2 / D4 / D5 alternate grammars; never on a Local Gem page"

rounded:
  photo-panel: 30px
  pill: ellipse

spacing:
  frame: 1080x1350
  gutter-cover: 57px
  gutter: 108px
  masthead-top: 97px
  cover-headline-top: 224px
  cover-subline-top: 518px
  interior-headline-top: 321px
  interior-pill-top: 562px
  interior-body-top: 675px
  panel-top: 892px
  panel-size: 432x262px
  label-top: 1270px

components:
  wash:
    cover: "linear-gradient(180deg, rgba(15,20,30,.60) 0%, rgba(15,20,30,.55) 33%, rgba(15,20,30,.55) 66%, rgba(15,20,30,0) 100%) over the top 71% only"
    interior: "linear-gradient(180deg, rgba(15,20,30,.55) 0%, rgba(15,20,30,.48) 33%, rgba(15,20,30,.46) 66%, rgba(15,20,30,.34) 100%) full bleed"
    rule: "light enough that the photo carries the frame"
  pill:
    shape: hand-drawn ellipse, 2.5px accent stroke, rotated -2deg
    size: 290x72px
    text: "@_JIING"
  doodles:
    smiley: single 7px accent stroke, ~130px wide
    arrow: single 7px accent stroke, ~200px, with a long thin trailing line to the right on the cover
    sparkle: 36-40px four-point star, accent fill
    rule: one doodle per interior frame, two on the cover (smiley + arrow), never on a face
  photo-panels:
    pair: two rounded 30px panels side by side at 66% height, 40% width each, 19.4% tall
    content: two more real photos of the same place; one may be a fact panel (dark translucent, cream hairline, one number in the headline gradient, one line under it)
---

# Valley Editions

## 1. What this is
A numbered series Jen publishes about the Valley, one neighborhood per edition, five frames each: cover → a place → her listing → what $X buys → the close. Every frame teaches one thing and asks one thing, in her words. The look is the Canva "Yellow Vintage Cafe & Restaurant Local Gem Carousel" (reference/template-local-gem/1–5.png) with her palette and her photos in place of the template's yellow and stock. That template is the target. Match its confidence, then make it hers.

## 2. Palette (hers; nothing warm)
Navy and steel are her brand; on these frames they live only in the accent tints, never as color blocks. Cream and white carry the type. The one accent, #C9D4E2, does everything the template's yellow did: the headline gradient's dark end, the pill stroke, the doodles, the sparkle. **No yellow. No orange. No terracotta. No navy panels or bands.** Type and accent over photo, that is the whole system.

## 3. Type (three families, never a fourth)
Instrument Serif in every role on a Local Gem page: masthead, headline, pill, body, label. The headline is 1–4 words on two lines, the first clause italic, the second upright, lines tight (line-height 0.78) so the descenders of line one touch the ascenders of line two, exactly as the template does. The headline fill is the gradient, pale blue at top-left to white at bottom-right. Body is the same serif at 28px, never a sans. Caveat carries one handwritten line on the close ("my DMs are open →"). Jost exists only for the D2/D4/D5 alternate grammars.

## 4. Layout grammar (Local Gem, five pages, geometry from the Canva source)
- **Cover** (page 1): masthead top-left at (57, 97). Headline block at (57, 224), 73% wide, italic clause then upright clause. Subline at (57, 518), 55% wide, 28px serif, two lines. Pill at (573, 275). Smiley at (57, 648). Arrow bottom-left at (57, 1221) with its long trailing line rising to the right. Wash over the top 71% only. Subject of the photo sits in the lower two-thirds; the type sits on the quiet part of the photo.
- **Spot** (pages 2–4): everything centered. Masthead at top 97px. Sparkle under it at 166px. Headline at top 321px, 78% wide, two lines. Pill at top 562px. Body at top 675px, 55% wide, 2–3 lines. Two rounded photo panels at top 892px, each 432×262, at left 90px and 557px. A one-line uppercase label in the bottom slot at 1270px (place · address · hours, or the listing address, or the ask).
- **Close** (page 5): masthead at top 97px. Headline at top 467px. Pill at top 720px. Her close line at top 850px, 64% wide, 30px serif. The Caveat hand line at top 999px. An arrow in the bottom slot. No photo panels; a big sky or a quiet backdrop behind.

## 5. Photos
Only from `photos/`. Her face only from her real photos; never generated. Her listing photos are hers to use. Where a frame needs a place we do not have (a coffee shop, a street), use her interiors as placeholders for the demo and say so in the layer name; the real plates come later. **Type never sits on a face.** Put the subject small or off-axis and the type in the sky, the wall, the counter. Nothing warm-orange in the grade: cool-neutral or golden-natural.

## 6. What never happens
No stock photography. No yellow, orange, or navy blocks. No emoji as graphics. No drop shadows on type. No second typeface on a Local Gem page. No "your first home" (fair housing and her rule): the ask is always "buying or selling". No "safe," "family," "great schools," "quiet neighborhood," or who a place is for. Copy in COPY-DECK.md is final; design explores, never rewrites.

## 7. The alternate grammars (system sheet)
Five other Canva carousels Farrice picked are extracted in GRAMMAR.md: D2 moment (rules top and bottom, short headline word, giant rotated accent word), D3 stack (two-word headline stack in a corner, italic connector, credit opposite), D4 city guide (left-aligned eyebrow, headline, body, divider, handle), D5 urban guide (ring badge eyebrow, centered subhead and headline, grain), D6 big initial (giant sans initial + serif rest per word). One cover per grammar lets Farrice pick a grammar per edition.

## 8. Verification
Every number on a frame traces to a labeled ledger (RESEARCH-PACK, FACTS). A frame passes when: thumbnail-readable at 150px, type on no face, one accent, the copy unchanged, and it would survive as a single screenshot with no other frames around it.
