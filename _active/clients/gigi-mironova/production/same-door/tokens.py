#!/usr/bin/env python3
"""Same Door v4 — The Calm Closer visual character."""

INK="#173A54"; BAND="#244C68"; BRAND="#0C4071"; MUTED="#566E7E"
HAIRLINE="#D7E2E8"; ACCENT="#BD765E"; ACCENT_LT="#F0C7B8"
PAPER="#F7F3EC"; BONE="#ECE7DE"; MIST="#DCE8EE"; WHITE="#FFFDF8"
D_HAIRLINE="rgba(255,253,248,0.28)"
D_MUTED="rgba(255,253,248,0.78)"; SCRIM_RGB="18,39,55"

FONTS=("https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800"
       "&family=Manrope:wght@400;500;600;700;800&display=swap")

CSS=f"""
*{{box-sizing:border-box}} body{{margin:0}}
.frame{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Figtree','Avenir Next',sans-serif;color:{INK}}}
.ru{{font-family:'Manrope','Figtree',sans-serif}} .light{{background:{PAPER}}} .dark{{background:{BAND};color:{WHITE}}}
/* Former script hook is now a readable highlight. Character comes from composition. */
.si{{font-family:inherit;font-style:normal;font-weight:800;letter-spacing:-.035em;color:inherit;box-shadow:inset 0 -.22em 0 {MIST}}}
.dark .si{{color:{WHITE};box-shadow:inset 0 -.22em 0 rgba(240,199,184,.44)}} .ru .si{{letter-spacing:-.02em}}
.caps{{font-weight:700;letter-spacing:.18em;text-transform:uppercase}} .h{{font-weight:700;letter-spacing:-.04em;text-wrap:balance}}
.num{{font-weight:800;letter-spacing:-.055em;font-variant-numeric:tabular-nums;line-height:.92}}
.photo{{position:absolute;inset:0;z-index:0;overflow:hidden}} .photo>img{{width:100%;height:100%;object-fit:cover;display:block;transform-origin:center}}
.tint,.lift,.scrim{{position:absolute;inset:0}} .tint{{background:{BAND};mix-blend-mode:multiply}}
.duo>img{{filter:grayscale(1) contrast(1.03) brightness(1.02)}} .duo .tint{{opacity:.70}}
.duo .scrim{{background:linear-gradient(180deg,rgba({SCRIM_RGB},.12) 0%,rgba({SCRIM_RGB},.28) 58%,rgba({SCRIM_RGB},.72) 100%)}}
.bleed>img{{filter:saturate(.68) contrast(1.01) brightness(1.04) sepia(.05)}}
.bleed .tint{{opacity:.28!important}}
.bleed .scrim{{background:linear-gradient(180deg,rgba({SCRIM_RGB},.24) 0%,rgba({SCRIM_RGB},.12) 34%,rgba({SCRIM_RGB},.42) 68%,rgba({SCRIM_RGB},.82) 100%)}}
.pad{{position:relative;z-index:3;display:flex;flex-direction:column;height:100%;padding:58px 64px 54px;justify-content:space-between}}
.rule{{display:flex;justify-content:space-between;align-items:baseline;padding-bottom:18px}} .foot{{display:flex;justify-content:space-between;align-items:center}}
.evidence{{background:rgba(255,253,248,.94);border:1px solid {HAIRLINE};border-radius:24px;box-shadow:0 18px 52px rgba(23,58,84,.065)}}
.dark .evidence{{background:rgba({SCRIM_RGB},.48);border-color:{D_HAIRLINE};box-shadow:0 18px 48px rgba(7,22,34,.16)}}
.tag{{display:inline-flex;align-items:center;padding:13px 18px;border-radius:999px;background:{MIST};color:{INK};font-size:17px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}}
.dark .tag{{background:rgba(255,253,248,.14);color:{WHITE}}} .dot{{width:10px;height:10px;border-radius:50%;background:{ACCENT};display:inline-block}}
"""
