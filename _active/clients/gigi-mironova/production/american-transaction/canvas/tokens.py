#!/usr/bin/env python3
"""
Oxblood register of the realtor editorial system.

Same grammar as `_shared/realtor-editorial-system/DESIGN.md`. One hue family swapped,
plus one genuine extension the navy system never needed: a Cyrillic type path.

Figtree ships latin + latin-ext only — no Cyrillic subset at all. Russian slides set in
it would silently fall back to a system sans and break the register. Manrope is the
closest geometric-humanist match on Google Fonts that carries cyrillic + cyrillic-ext,
and Playfair Display's italic carries Cyrillic too, so the accent-word move survives the
language switch intact. Verified against the Google Fonts CSS API, 2026-08-30.
"""

# --- hue family -------------------------------------------------------------
# left column = this register, right column = the navy original it maps from
INK        = "#4A1420"   # oxblood, all body/heading type on white      (#1E3A5F)
BAND       = "#3B0F1A"   # deeper oxblood, dark grounds + photo tint    (#16304F)
MUTED      = "#7A5A60"   # secondary copy on white                      (#5A6B80)
HAIRLINE   = "#EADEE0"   # rules, dividers, left-borders                (#DCE2EA)
GHOST      = "#F3E7E9"   # the oversized background numeral             (#E7EDF4)
ACCENT     = "#A85A52"   # the Playfair italic accent on light grounds  (#4C7CA8)
ACCENT_LT  = "#E8C4BE"   # the Playfair italic accent on dark grounds   (#C9D4E2)
PAPER      = "#FFFFFF"

# dark-ground equivalents (authored dark from the start — never remapped, per DESIGN.md)
D_GHOST    = "rgba(255,255,255,0.22)"
D_HAIRLINE = "rgba(255,255,255,0.34)"
D_MUTED    = "rgba(255,255,255,0.74)"

# photo scrim base: near-black in the oxblood family, not the navy's rgba(9,20,34,·)
SCRIM_RGB  = "26,8,13"

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Figtree:wght@400;500;600;700"
         "&family=Manrope:wght@400;500;600;700"
         "&family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500"
         "&display=swap")

CSS = f"""
  body {{ margin:0; }}
  .frame {{ width:1080px; height:1350px; position:relative; overflow:hidden;
           font-family:'Figtree','Avenir Next',sans-serif; box-sizing:border-box; }}
  /* Russian slides only. Figtree has no cyrillic subset; Manrope does. */
  .ru {{ font-family:'Manrope','Figtree','Avenir Next',sans-serif; }}
  .light {{ background:{PAPER}; color:{INK}; }}
  .dark  {{ background:{BAND};  color:#FFFFFF; }}
  .si {{ font-family:'Playfair Display',Georgia,serif; font-style:italic; font-weight:500; }}
  .light .si {{ color:{ACCENT}; }}
  .dark .si  {{ color:{ACCENT_LT}; }}
  .caps {{ font-weight:600; letter-spacing:0.24em; text-transform:uppercase; }}

  /* --- photography layer (framing is per slide, inline on the img — never global) --- */
  .photo {{ position:absolute; inset:0; z-index:0; overflow:hidden; }}
  .photo > img {{ width:100%; height:100%; object-fit:cover; display:block;
                 transform-origin:center; }}
  .tint  {{ position:absolute; inset:0; background:{BAND}; mix-blend-mode:multiply; }}
  .lift  {{ position:absolute; inset:0; background:#E8D2CE; mix-blend-mode:screen; }}
  .scrim {{ position:absolute; inset:0; }}
  .duo > img {{ filter:grayscale(1) contrast(1.14) brightness(0.86); }}
  .duo .tint {{ opacity:0.92; }}
  .duo .lift {{ opacity:0.10; }}
  .bleed > img {{ filter:sepia(0.30) hue-rotate(-10deg) saturate(0.88)
                          contrast(1.06) brightness(0.94); }}
  .bleed .scrim {{ background:linear-gradient(180deg,
        rgba({SCRIM_RGB},0.62) 0%, rgba({SCRIM_RGB},0.48) 26%,
        rgba({SCRIM_RGB},0.64) 60%, rgba({SCRIM_RGB},0.86) 100%); }}

  /* --- shared furniture --- */
  .pad  {{ position:relative; z-index:1; display:flex; flex-direction:column; height:100%;
          box-sizing:border-box; padding:64px 72px; justify-content:space-between; }}
  .rule {{ display:flex; justify-content:space-between; align-items:baseline;
          padding-bottom:22px; }}
  .foot {{ display:flex; justify-content:space-between; align-items:baseline; }}
  .ghost {{ position:absolute; font-family:'Playfair Display',Georgia,serif; font-weight:500;
           font-size:760px; line-height:0.8; z-index:0; }}
  .h    {{ font-weight:600; letter-spacing:-0.02em; }}
"""
