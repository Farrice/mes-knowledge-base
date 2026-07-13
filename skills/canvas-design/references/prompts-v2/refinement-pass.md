---
name: "Canvas Design — Refinement Pass"
source_prompt: born-v2
skill: canvas-design
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

The final step in the process, triggered when the user has signaled the first pass isn't there yet —
in the skill's own framing: "It isn't perfect enough. It must be pristine, a masterpiece of
craftsmanship, as if it were about to be displayed in a museum." The job now is disciplined refinement
of an existing piece, not a second attempt at a new one.

## Input Required

- `[EXISTING CANVAS FILE]` — the .pdf/.png already produced
- `[DESIGN PHILOSOPHY .MD]` — the philosophy the piece is meant to respect
- `[WHAT FEELS UNFINISHED]` — optional; specifics the user flagged, if any

## Execution Protocol

1. **Do not add more graphics.** The instinct to reach for a new element is the wrong instinct here —
   refine what already exists instead.
2. **Make the composition extremely crisp.** Respect the design philosophy and the principles of
   minimalism entirely; this is a tightening pass, not an expansion.
3. **Ask before every change:** "How can I make what's already here more of a piece of art?" If the
   instinct is to call a new function or draw a new shape, STOP — that instinct fails this step by
   definition.
4. **Take a genuine second pass.** Go back to the composition and refine and polish further, aiming
   for a philosophically designed masterpiece, not a cosmetic touch-up.
5. **Re-verify the boundary rule after refinement, not just before.** Nothing overlaps, nothing falls
   off the page, breathing room is preserved — refinement must not have quietly broken what the first
   pass got right.

## Output Contract

A refined version of the SAME canvas file — same subject, same philosophy, same file format — with no
new elements added. Every change is a tightening: spacing, alignment, color precision, edge treatment,
typographic detail. Delivered in the original .pdf/.png format.

## Output Skeleton

```
[REFINEMENT LOG for <original file>]
Elements added: [must be none]
Elements removed: [none expected, unless a genuinely non-functional element was cut — note why]
Tightened: [specific list — spacing / alignment / color precision / edge treatment /
            typographic detail]
Governing question applied: [confirm the "how can I make what's already here more of a piece of
                             art" question was asked before each change, not applied uniformly
                             as a checklist]
Bounds re-check: [confirmed after refinement — no overlaps, no clipping, margins held]
Output: [same filename].pdf or .png
```

## Quality Gate

- Is the refinement free of any newly added graphic elements?
- Was the governing question applied as a filter before each change, i.e. is every change a
  tightening rather than an addition?
- Does the refined piece still fully respect the original design philosophy?
- Are margins, overlaps, and clipping re-verified after refinement rather than assumed carried over
  from the first pass?
- Is this recognizably a second pass on the SAME piece, not a new composition wearing the old file
  name?

## Creative Latitude

Deciding WHAT to tighten — which spacing, which color, which edge — is a taste call, not a checklist
to run uniformly across the whole canvas. Trust the eye for where the piece currently reads as
"unfinished" or "digital" rather than "crafted," and concentrate refinement exactly there rather than
touching everything equally.

## Deploy When

The user has explicitly rejected a first-pass canvas as not polished or pristine enough, or asks for a
second pass, a refinement, or "make it museum-quality."
