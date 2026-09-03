# linkedin-carousel pool — review notes (ours; LIVING)

Farrice's verdicts on the pool, in his words, and what was done about each. The Scrapes Template Studio keeps pins in `comments.json`; this file keeps the decisions.

## 2026-09-03 — first Studio pass (Farrice)
> "It's pretty cool… the typography, spacing, and a few other things were done poorly on some of them. We just need to tighten that up and fix the composition and hierarchy."

Diagnosis (verified in the template sources): the builders' automatic gate demands a display cap-height ≥ 8.0cqw. The brand's own h1 is 72px (6.67cqw) and its largest display token 104px (9.63cqw). To pass the gate the builders scaled headlines to 104–127px and then pushed subtitles, rules, and captions down the canvas to dodge a ring-probe false positive in the overflow check. Result: oversized headlines, dead bands, hierarchy flattened. The refs (his own Premium Minimal frames) are the brand truth.

Craft pass (in-pool CSS only, canonical re-render via `render_template.py`, no AI, $0):
- every HEADLINE → 6.67cqw (72px, brand h1), letter-spacing −0.025em, line-height per ref (cover 1.05 · kicker stack 1.72 · marker body 1.25 · CTA 1.25); width back to the 84.44% content column; `white-space:nowrap` removed on the CTA (it ran the first line into the right edge)
- vertical composition restored to the ref: cover subtitle 51%, heavy rule 85.2%, footer caption 90.3% · kicker stack statement 80.5% · marker routes 62–74%, footer 89.9% · CTA routes 63–75%, footer 86.9%, recommendation name 91.6% at 2.6cqw
- fixed chrome (masthead, field index, hairline) untouched

Open: the Scrapes builder gate will re-flag these templates if a builder is ever re-spawned on them (Check D floor). That gate is theirs; we never edit inside `.claude/skills/`. Content-time rendering does not re-run it.

## How to leave notes next time
Template Studio → top bar → **Comment** pill (toggles comment mode) → click the slide where the note belongs → type. Pins land in `comments.json` next to this file; say "read my Studio comments" and they get pulled into the next pass.
