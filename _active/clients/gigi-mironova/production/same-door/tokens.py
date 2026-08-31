#!/usr/bin/env python3
"""
Equity Union register of the realtor editorial system.

Not an invented palette. Every value below was pulled from the live brand on 2026-08-31 —
computed styles on equityunion.com, and the HouseSellers logo pixel-sampled from
`company-logo.png`. See ../../DEMAND-BRIEF.md § 1.

The finding this register rests on: Equity Union's own homepage is already built in this
grammar — geometric sans, high-contrast serif italic accent word, navy ("MOVE *FORWARD*").
So working inside the brokerage brand and working editorially are the same move here.
Nobody on the team uses it below the homepage.

Type, and its one known gap:
  Jost      — Equity Union's own declared Futura fallback. Free, and ships cyrillic, so a
              single brand-faithful face carries both languages.
  Bodoni Moda — the brokerage display serif. Latin/latin-ext only, NO cyrillic subset.
  Playfair Display italic — carries cyrillic; stands in for the accent word on Russian
              slides only. Verified against the Google Fonts CSS API, 2026-08-31.
"""

# --- brand values, observed not chosen -------------------------------------
INK        = "#174579"   # Equity Union primary navy — headings + body on white
BAND       = "#0F2D4F"   # Equity Union deep navy — dark grounds, photo tint
LOGO_BLUE  = "#0C4071"   # HouseSellers lockup blue, pixel-sampled
MUTED      = "#687994"   # Equity Union steel — secondary copy on white
HAIRLINE   = "#DCE3EC"   # rules, dividers, left-borders
GHOST      = "#E9EFF6"   # the oversized background numeral
ACCENT     = "#4A6E96"   # the serif italic accent on light grounds
ACCENT_LT  = "#AFC5DC"   # the serif italic accent on dark grounds
PAPER      = "#FFFFFF"
BONE       = "#F4F7FA"   # tint panel on white slides

# dark-ground equivalents (authored dark from the start — never remapped, per DESIGN.md)
D_GHOST    = "rgba(255,255,255,0.20)"
D_HAIRLINE = "rgba(255,255,255,0.32)"
D_MUTED    = "rgba(255,255,255,0.76)"

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Jost:ital,wght@0,400;0,500;0,600;0,700;1,400"
         "&family=Bodoni+Moda:ital,opsz,wght@0,6..96,500;1,6..96,400;1,6..96,500"
         "&family=Playfair+Display:ital,wght@1,400;1,500"
         "&display=swap")

CSS = f"""
  body {{ margin:0; }}
  .frame {{ width:1080px; height:1350px; position:relative; overflow:hidden;
           font-family:'Jost','Futura','Avenir Next',sans-serif; box-sizing:border-box; }}
  .light {{ background:{PAPER}; color:{INK}; }}
  .dark  {{ background:{BAND};  color:#FFFFFF; }}

  /* the accent word. Bodoni is the brokerage serif; Russian slides fall to Playfair,
     which is the closest high-contrast face that actually ships cyrillic. */
  .si    {{ font-family:'Bodoni Moda',Didot,Georgia,serif; font-style:italic;
           font-weight:500; }}
  .ru .si {{ font-family:'Playfair Display',Georgia,serif; }}
  .light .si {{ color:{ACCENT}; }}
  .dark .si  {{ color:{ACCENT_LT}; }}

  .caps  {{ font-weight:500; letter-spacing:0.26em; text-transform:uppercase; }}
  .h     {{ font-weight:600; letter-spacing:-0.015em; }}
  .num   {{ font-family:'Bodoni Moda',Didot,Georgia,serif; font-weight:500;
           font-variant-numeric:tabular-nums; line-height:0.92; }}

  .photo {{ position:absolute; inset:0; z-index:0; overflow:hidden; }}
  .photo > img {{ width:100%; height:100%; object-fit:cover; display:block; }}
  .tint  {{ position:absolute; inset:0; background:{BAND}; mix-blend-mode:multiply; }}
  .lift  {{ position:absolute; inset:0; background:#C9D9EC; mix-blend-mode:screen; }}
  .duo > img {{ filter:grayscale(1) contrast(1.12) brightness(0.9); }}
  .duo .tint {{ opacity:0.88; }}
  .duo .lift {{ opacity:0.12; }}

  .pad   {{ position:relative; z-index:1; display:flex; flex-direction:column; height:100%;
           box-sizing:border-box; padding:64px 72px; justify-content:space-between; }}
  .rule  {{ display:flex; justify-content:space-between; align-items:baseline;
           padding-bottom:22px; }}
  .foot  {{ display:flex; justify-content:space-between; align-items:baseline; }}
  .ghost {{ position:absolute; font-family:'Bodoni Moda',Didot,Georgia,serif;
           font-weight:500; font-size:700px; line-height:0.8; z-index:0; }}
"""
