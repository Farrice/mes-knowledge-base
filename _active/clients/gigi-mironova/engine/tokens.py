#!/usr/bin/env python3
"""Gigi Mironova — locked visual system for the engine run (Stage 5/6).

Lineage: the shared realtor editorial floor (`_shared/realtor-editorial-system/DESIGN.md`)
keyed to Gigi per DESIGN.md recommendations #1 (light register: warm paper, one warm
accent) and #2 (second hue per agent). Palette and character carried from the
"Calm Closer" pass in the gigi lanes (`production/same-door/tokens.py`), with two
tightenings to meet the carousel banlist: square corners, no drop shadows.

Her name outranks the brokerage lockup on every board. Brokerage sits in the footer.
"""

INK = "#173A54"        # all type on paper
BAND = "#244C68"       # dark grounds
BRAND = "#0C4071"      # House Sellers blue — lockup text only
MUTED = "#566E7E"      # secondary copy on paper
HAIRLINE = "#D7E2E8"   # rules, borders
ACCENT = "#BD765E"     # clay — one consequential mark per board, never body copy
ACCENT_LT = "#F0C7B8"
PAPER = "#F7F3EC"      # warm paper ground (light register)
BONE = "#ECE7DE"
MIST = "#DCE8EE"       # highlight underline on paper
WHITE = "#FFFDF8"
D_HAIRLINE = "rgba(255,253,248,0.28)"
D_MUTED = "rgba(255,253,248,0.78)"
SCRIM_RGB = "18,39,55"

HANDLE = "@GIGIMIRONOVA_REALESTATE"
NAME = "GIGI MIRONOVA"
DRE = "DRE 02025393"
LOCKUP = "HOUSE SELLERS · EQUITY UNION"

FONTS = ("https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800"
         "&family=Manrope:wght@400;500;600;700;800&display=swap")

CSS = f"""
*{{box-sizing:border-box}} body{{margin:0}}
.frame{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Figtree','Avenir Next',sans-serif;color:{INK};background:{PAPER}}}
.ru{{font-family:'Manrope','Figtree',sans-serif}}
.dark{{background:{BAND};color:{WHITE}}}
.hl{{font-weight:800;letter-spacing:-.035em;box-shadow:inset 0 -.22em 0 {MIST}}}
.dark .hl{{box-shadow:inset 0 -.22em 0 rgba(240,199,184,.44)}}
.caps{{font-weight:700;letter-spacing:.18em;text-transform:uppercase}}
.h{{font-weight:700;letter-spacing:-.04em;text-wrap:balance;line-height:1.04}}
.num{{font-weight:800;letter-spacing:-.055em;font-variant-numeric:tabular-nums;line-height:.92}}
.photo{{position:absolute;inset:0;z-index:0;overflow:hidden}}
.photo>img{{width:100%;height:100%;object-fit:cover;display:block;transform-origin:center}}
.tint,.lift,.scrim{{position:absolute;inset:0}}
.tint{{background:{BAND};mix-blend-mode:multiply}}
.duo>img{{filter:grayscale(1) contrast(1.03) brightness(1.02)}} .duo .tint{{opacity:.70}}
.duo .scrim{{background:linear-gradient(180deg,rgba({SCRIM_RGB},.12) 0%,rgba({SCRIM_RGB},.28) 58%,rgba({SCRIM_RGB},.74) 100%)}}
.bleed>img{{filter:saturate(.68) contrast(1.01) brightness(1.04) sepia(.05)}}
.bleed .tint{{opacity:.28}}
.bleed .scrim{{background:linear-gradient(180deg,rgba({SCRIM_RGB},.26) 0%,rgba({SCRIM_RGB},.14) 34%,rgba({SCRIM_RGB},.46) 68%,rgba({SCRIM_RGB},.84) 100%)}}
.pad{{position:relative;z-index:3;display:flex;flex-direction:column;height:100%;padding:60px 66px 56px;justify-content:space-between}}
.rule{{display:flex;justify-content:space-between;align-items:baseline;padding-bottom:18px;border-bottom:1px solid {HAIRLINE}}}
.dark .rule{{border-bottom-color:{D_HAIRLINE}}}
.foot{{display:flex;justify-content:space-between;align-items:center;font-size:17px}}
.card{{background:{WHITE};border:1px solid {HAIRLINE}}}
.dark .card{{background:rgba({SCRIM_RGB},.48);border-color:{D_HAIRLINE}}}
.tag{{display:inline-flex;align-items:center;gap:12px;padding:12px 16px;background:{MIST};color:{INK};font-size:17px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}}
.dark .tag{{background:rgba(255,253,248,.14);color:{WHITE}}}
.dot{{width:10px;height:10px;background:{ACCENT};display:inline-block}}
.mark{{width:14px;height:14px;background:{ACCENT};display:inline-block;flex:none;margin-top:14px}}
"""
