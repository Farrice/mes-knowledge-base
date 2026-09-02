---
version: alpha
name: Valley Native · @_jiing
description: Jen Santulan's Instagram carousel system. Navy line drawings on cream, a place stamp on every slide, real Valley photography as prints, one serif-italic accent word, her own close on the last slide. Built to make a first-time buyer feel she's from here and she's the one you text.

colors:
  primary: "#1E3A5F"
  secondary: "#4C7CA8"
  tertiary: "#C9D4E2"
  neutral: "#F7F5F2"
  hairline: "#E0DBD2"
  body: "#6B6C70"
  caption: "#A6A296"
  dark-ground: "#1E3A5F"
  dark-ghost: "#24436B"
  dark-rule: "#3A5578"
  dark-caption: "#9FB4CC"
  dark-dim: "#7E96B4"
  print-mat-dark: "#24436B"
  bar-track: "#EDE9E2"
  bar-muted: "#D9D3C8"

typography:
  headline:
    fontFamily: "Figtree"
    fontSize: 70px
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: "Figtree"
    fontSize: 84px
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: -0.015em
  accent-italic:
    fontFamily: "Playfair Display"
    fontSize: 94px
    fontWeight: 400
    lineHeight: 1.0
    fontStyle: italic
  numeral:
    fontFamily: "Playfair Display"
    fontSize: 176px
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.03em
  subhead:
    fontFamily: "Figtree"
    fontSize: 46px
    fontWeight: 500
    lineHeight: 1.32
    letterSpacing: -0.01em
  body:
    fontFamily: "Figtree"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.55
  eyebrow:
    fontFamily: "Figtree"
    fontSize: 26px
    fontWeight: 400
    letterSpacing: 0.24em
  masthead:
    fontFamily: "Figtree"
    fontSize: 28px
    fontWeight: 500
    letterSpacing: 0.24em
  sign:
    fontFamily: "Overpass"
    fontSize: 22px
    fontWeight: 600
    letterSpacing: 0.2em
  sign-sm:
    fontFamily: "Overpass"
    fontSize: 16px
    fontWeight: 600
    letterSpacing: 0.2em
  caption-print:
    fontFamily: "Overpass"
    fontSize: 17px
    fontWeight: 600
    letterSpacing: 0.2em
  page-number:
    fontFamily: "Playfair Display"
    fontSize: 30px
    fontWeight: 400
    fontStyle: italic

rounded:
  none: 0px

spacing:
  frame-padding: 100px
  stack: 38px
  masthead-gap: 26px
  body-rule-gap: 32px
  print-mat: 14px
  print-border: 3px
  line-weight: 2px

components:
  frame:
    width: 1080px
    height: 1350px
    padding: 100px
    background: "#F7F5F2"
  masthead:
    left: "@_JIING"
    right: "FIRST-TIME BUYER FILE"
    rule: "#E0DBD2"
  stamp:
    mark: roundel-ridge-over-boulevard
    line1: "<NEIGHBORHOOD> · <ZIP>"
    line2: "FROM THE VALLEY"
    position: under-masthead-left
  print:
    border: 3px solid "#1E3A5F"
    mat: 14px
    tilt: 1.5deg
    caption: sign 17px tracked caps
  keyed-map:
    stops: 4
    marker: 44px square outline with 01-04
    glyphs: stroke-only SVG, 2px
  bar:
    height: 10px
    track: "#EDE9E2"
    fill-strong: "#4C7CA8"
    fill-muted: "#D9D3C8"
  panels:
    two-up, left cream, right white with hairline (dark variant: right ghost navy)
  close:
    ground: "#1E3A5F"
    ask-box: cream box, Playfair italic 46px, text "my DMs are open"
    print: her photo, cream border
    source: 22px tracked caps in "#7E96B4"
---

# Valley Native

## 1. Overview

A seven-slide Instagram carousel system for @_jiing (Jen Santulan, San Fernando Valley realtor, first-time buyers). The identity is the navy line system, not the serif: 16 of 18 competitor "neighborhood guide" covers run white serif italic over a warm photo, so serif italic here is one accent word per slide and never the whole voice. Everything drawn is stroke-only SVG at one 2px weight, navy on cream. Photography is real, cleared, and treated as a print with a border and a caption, never a background behind type.

## 2. Colors

Navy `#1E3A5F` is ink: all headlines, all line art, the dark-slide ground. Steel `#4C7CA8` is the one accent: filled bars, the % sign, eyebrow numbers on the deck. Soft blue `#C9D4E2` is body type on navy and the ghost map on cream. Cream `#F7F5F2` is the ground. Nothing warm, ever: no orange, terracotta, red, yellow, tan. Jen hates orange. A second color, if one is ever needed, is steel or soft blue.

## 3. Typography

Figtree carries headlines (lowercase, 600), body (400), masthead and eyebrow (tracked caps). Playfair Display italic carries exactly one accent word or phrase per slide, the big numerals ($50K, 15%, 29.1%, 6.7), and the page number. Overpass 600 is the sign face: the stamp, map labels, print captions, small caps under rules. Three families, never a fourth. Headlines stay lowercase. Ellipses over exclamation points. No em-dashes.

## 4. Layout

1080×1350, 100px padding on every side, flex column with space-between: masthead on top (handle · file name · hairline · stamp), content stack in the middle (gap 38px), footer at the bottom (tracked-caps label left, italic page number right). Cover and close are absolute-positioned specials: cover pins the headline to the bottom-left with the print upper-right and a ghost Valley map bleeding off the right edge; close is the navy ground with the ask box left and her print right.

## 5. Elevation & Depth

None. No drop shadows, no gradients, no rounded cards. Depth comes from the print device (border + mat + 1.5° tilt) and from the two navy slides (4 and 7) beating against cream.

## 6. Shapes

Square corners everywhere. Markers are 44px squares with 2px navy borders. Stations are 20px squares on a 2px spine. Buildings are four drawn facades on a 100×120 grid: flat-roof dingbat, courtyard walk-up with outside stair, mid-rise slab, gabled bungalow. Tiling them (twenty across two rows, three hatched) is the house move for a share or a count.

## 7. Components

- **Masthead + stamp** on all seven slides, identical position. Stamp line 1 rotates per series (VAN NUYS · 91401, SHERMAN OAKS · 91403); line 2 is always FROM THE VALLEY.
- **Cover:** headline bottom-left (Figtree 70, one Playfair italic phrase), one-line dek with a 76px rule, her print upper-right, one drawn arrow pointing at it.
- **Keyed map (slide 2):** italic line + sans line + body, then four drawn glyphs on one 2px line with 01–04 markers and tracked labels. This slide lays out the set.
- **Stat slide:** eyebrow, big Playfair numeral, headline, body, optional bars or list.
- **Dark scene (slide 4):** navy ground, headline with italic accent in soft blue, body in soft blue, one print with cream border, one drawn detail row (pages, tiles) with a small-caps caption.
- **Panels:** two-up comparison, labels in sign caps, Playfair 40 inside.
- **Station / place list:** 2px spine, squares, Playfair names, sign tags.
- **Close (slide 7):** navy ground, headline with italic accent, body ending on her verbatim close, cream ask box "my DMs are open", her print with cream border, source line in dark-dim caps, footer JEN SANTULAN · SFV & LOS ANGELES.

## 8. Do's and Don'ts

Do: translate every lender term in place or with a six-word gloss; keep numbers exact and sourced on slide 6 or 7; end every close on her words ("i'm here for you... i do this to protect you and your best interest"); one annotation per slide, pointing at something real; one emoji maximum, only in a caption.
Don't: put type on a photo without a solid navy scrim; use stock smiles that aren't hers; write "safe," "family," "great schools," "quiet neighborhood," or who a place is for; use "top producer" or years in business; invent a found detail (a page, a month) she never saw; use a keyword CTA.
