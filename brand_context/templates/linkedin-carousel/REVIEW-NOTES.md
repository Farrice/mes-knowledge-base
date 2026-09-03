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

## 2026-09-03 — aesthetic pivot: the editorial style (Farrice)
> "I would rather this be the template. Our content aesthetic needs to be better… clean, minimal, and durable… pictures of the product, pictures that are relevant and context-aware… the call to action and sign-off."

Bar: the Canva "Creative Presentation" set he pasted (grey canvas, giant lowercase words, red script signature, big editorial photos, header title + date + arrow, footer strip). Re-solved for 4:5 as eight HTML reference frames in `brand_context/visual-identity/compositions/editorial/frames/` → rendered to `brand_context/visual_refs/editorial/`. Decisions: red unlocked for the signature only (`tokens.json colors.signature_accent`, move #10); Snell Roundhand (system) as the placeholder signature until his handwriting lands in `visual-identity/logos/`; every photo zone holds a REAL source (Meta Ad Library capture, Huel product page capture, his studio portrait) — stock imagery rejected on sight; `styles.json` splits the pool into `editorial` (default for teardowns) and `typographic`.

His read on the frames (approved with notes): "compositional layout and hierarchy… crowding… spacing… bleed… positioning." Pass applied: giant words fit the canvas margin to margin without clipping, body left-aligned (justified made rivers), items spaced on a 160–170px rhythm, hairline added above the three-column row, labels shortened to one line, CTA label right-aligned with an arrow.

## How to leave notes next time (verified 2026-09-03 with a test pin)
Template Studio → top bar → **Comment** pill (toggles comment mode; a toast confirms) → click the slide where the note belongs → a small composer opens → type → press the composer's **Comment** button (Return does NOT submit) → top bar **Save**. The pin lands in `<template>/comments.json` (per template, not at the pool root). Say "read my Studio comments" and every `comments.json` under this pool gets pulled into the next pass. Four pins on four templates is a full review.

## 2026-09-03 · signature placement (Farrice)
"I don't like the layering of it. It's a little distracting." The red script signature now sits UNDER the giant word on `signature-cover` (top 57%) and `signature-close-cta` (top 60%). The approved frames in `visual_refs/editorial/` still show the layered version; the pool templates are the truth from here. Last template change before the next session.
