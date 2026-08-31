#!/usr/bin/env python3
"""
"Same Door" — soft-navy register, v3.

v2 verdict (Farrice, 2026-08-31): Bodoni italic at display scale is unreadable flare;
the raw brand navy is harsh; flat type-only slides sit below the First Home Valley floor;
no visual enrichment. All four fixed here.

The grammar reverts to the PROVEN floor (_shared/realtor-editorial-system/DESIGN.md):
Figtree structural type, lowercase headlines, ONE Playfair italic accent word at headline
scale only — never at numeral scale — photography with duo/bleed treatments, the ghost
numeral, dense white structure slides. The hue family stays HouseSellers navy, softened:
ink desaturated and lifted, warm-white paper, generous air.

Numerals are Figtree 600 with tabular figures — readable at any size, which is where the
Bodoni experiment died.

Cyrillic: Figtree has no cyrillic subset; Manrope (closest geometric match, ships
cyrillic) carries structural type on Russian slides, Playfair italic carries the accent —
same solution the oxblood register proved. Verified against Google Fonts CSS API.
"""

# --- soft navy family (derived from HouseSellers #0C4071 / EU #174579, softened) ----
INK        = "#2C4A68"   # softened navy — headings + body on white
BAND       = "#243D56"   # deep ground for photo slides (tint layer base)
MUTED      = "#75879C"   # secondary copy on white
HAIRLINE   = "#E3E9F0"   # rules, dividers, left-borders
GHOST      = "#EDF1F6"   # oversized background numeral on white
ACCENT     = "#5E86AC"   # Playfair italic accent on light grounds
ACCENT_LT  = "#C3D4E5"   # accent on dark grounds
PAPER      = "#FDFDFC"   # warm-white, not clinical white
BONE       = "#F2F5F8"   # tint panel on white slides

D_GHOST    = "rgba(255,255,255,0.16)"
D_HAIRLINE = "rgba(255,255,255,0.34)"
D_MUTED    = "rgba(255,255,255,0.78)"

SCRIM_RGB  = "13,26,41"  # near-black in the navy family

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Figtree:wght@400;500;600;700"
         "&family=Manrope:wght@400;500;600;700"
         "&family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500"
         "&display=swap")

CSS = f"""
  body {{ margin:0; }}
  .frame {{ width:1080px; height:1350px; position:relative; overflow:hidden;
           font-family:'Figtree','Avenir Next',sans-serif; box-sizing:border-box; }}
  .ru {{ font-family:'Manrope','Figtree','Avenir Next',sans-serif; }}
  .light {{ background:{PAPER}; color:{INK}; }}
  .dark  {{ background:{BAND};  color:#FFFFFF; }}

  /* ONE italic accent word per slide, headline scale only — never numerals */
  .si {{ font-family:'Playfair Display',Georgia,serif; font-style:italic; font-weight:500; }}
  .light .si {{ color:{ACCENT}; }}
  .dark .si  {{ color:{ACCENT_LT}; }}

  .caps {{ font-weight:600; letter-spacing:0.24em; text-transform:uppercase; }}
  .h    {{ font-weight:600; letter-spacing:-0.02em; }}
  .num  {{ font-weight:600; letter-spacing:-0.02em; font-variant-numeric:tabular-nums;
          line-height:1; }}

  /* --- photography layer (framing per slide, inline on the img — never global) --- */
  .photo {{ position:absolute; inset:0; z-index:0; overflow:hidden; }}
  .photo > img {{ width:100%; height:100%; object-fit:cover; display:block;
                 transform-origin:center; }}
  .tint  {{ position:absolute; inset:0; background:{BAND}; mix-blend-mode:multiply; }}
  .lift  {{ position:absolute; inset:0; background:#C9D7E8; mix-blend-mode:screen; }}
  .scrim {{ position:absolute; inset:0; }}
  .duo > img {{ filter:grayscale(1) contrast(1.14) brightness(0.86); }}
  .duo .tint {{ opacity:0.92; }}
  .duo .lift {{ opacity:0.10; }}
  .bleed > img {{ filter:saturate(0.72) contrast(1.06) brightness(0.94); }}
  .bleed .scrim {{ background:linear-gradient(180deg,
        rgba({SCRIM_RGB},0.60) 0%, rgba({SCRIM_RGB},0.46) 26%,
        rgba({SCRIM_RGB},0.62) 60%, rgba({SCRIM_RGB},0.86) 100%); }}

  .pad  {{ position:relative; z-index:1; display:flex; flex-direction:column; height:100%;
          box-sizing:border-box; padding:64px 72px; justify-content:space-between; }}
  .rule {{ display:flex; justify-content:space-between; align-items:baseline;
          padding-bottom:22px; }}
  .foot {{ display:flex; justify-content:space-between; align-items:baseline; }}
  .ghost {{ position:absolute; font-family:'Playfair Display',Georgia,serif;
           font-weight:500; font-size:760px; line-height:0.8; z-index:0; }}
"""
