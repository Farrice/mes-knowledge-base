---
description: Engineer 3+ deliberate contrast forms from the 9-form menu onto a design or brief — each form assigned to a flow anchor, with the double-whammy check, restraint calls, and the audience gate
---

# 22 — Contrast Stack

> **/satori-contrast-stack** — Contrast is the strongest anti-generic mechanism in design. AI-default layouts distribute emphasis evenly; this workflow stacks 3+ deliberate, zonal contrast forms so the right things win.

> *"You are about to watch the most important teachings I've ever shown on this channel about contrast."* — Satori

The 9 forms in 3 tiers — **Basic**: color, size, typography · **Intermediate**: shape, style, texture · **Advanced**: psychology, emotion, concept. Full system: `references/contrast-stack.md`.

## Pre-Flight Gate

**Use this when**:
- A layout spine exists (three anchors committed) and the anchors need to *win* their beats
- Briefing a generation tool and you want non-generic output — contrast decisions are the brief's teeth
- A design is "clean but flat" — everything intentional in the same tidy way (the AI-default tell)
- Building CTA/conversion surfaces where contrast is choice architecture (HK-13)

**Do NOT use this when**:
- No spine exists — run `/satori-three-flow` first; contrast serves anchors, unassigned contrast is confetti
- You're diagnosing an *existing* design — that's `/satori-contrast-audit` (the reader twin)
- The failure is palette strategy (which colors, what jobs) — that's `/satori-color`; this workflow decides where color *contrasts*, not what the palette is
- The vibe is wrong but emphasis is right — `/satori-feeling-calibrate`

## Skill Acquisition

```
Load: skills/satori-graphics/genius.md
  ├─ GP-20 (Contrast Stack — the 9 forms and operating rules)
  ├─ GP-18 (Three-Flow Rule — the anchors contrast serves)
  ├─ GP-14 (Feeling-Before-Information — the audience gate)
  └─ HK-13 (Contrast is choice architecture)
Load: skills/satori-graphics/references/contrast-stack.md
```

## Execution

### Step 1 — Inputs on the Table

State: the three anchors (from `/satori-three-flow` or committed now), target audience + feeling (GP-14), and surface. No anchor list = halt and route to workflow 21.

### Step 2 — Select 3–5 Forms and Assign Each to an Anchor

Walk the 9-form menu. For each selected form, commit: **form → zone → what it makes win**.

| Tier | Form | Selection trigger |
|---|---|---|
| Basic | Color | An anchor must pop off its ground; CTA surfaces (the addictive-response lever); mood via grayscale+one-color |
| Basic | Size | Hierarchy itself; option-steering (larger option gets clicked); surreal scale for intrigue |
| Basic | Typography | Headline/body scale steps; weight breaks; contrasting typeface styles (the logo-neatening move) |
| Intermediate | Shape | Field of one geometry, product in the other (Nike: angular field, curved shoe wins) |
| Intermediate | Style | ONE rendering break (flat field + one photographic element). Restraint rule applies |
| Intermediate | Texture | Tactile sensation against flatness — expresses touch (marker strokes, balloon rubber) |
| Advanced | Psychology | Invert a learned association (serif ≠ luxury-context; skull ≠ death-palette) |
| Advanced | Emotion | Two opposing feelings on one design (humor × serious; love × sadness) |
| Advanced | Concept | The whole treatment contradicts the expected treatment (flat-2D flipped 3D-modern) |

Rules enforced while selecting:
1. **≥3 deliberate forms** (Nike standard) — minimal designs still stack; the forms are quiet and **zonal, not global** (black shoes may sit on a black zone where no contest is needed).
2. **Every form serves an anchor.** A contrast serving nothing is decoration — rent test (GP-01).
3. **Restraint is logged.** Style contrast NOT used = write the decision. *"Advanced designers know when or where not to use it."*

### Step 3 — The Advanced-Tier Decision

Attempt exactly one advanced form (psychology / emotion / concept) — this is the memorability tier:
- Write the **learned association** the audience holds (norm), then the **inversion** (flip).
- Gate it: does the flip serve the communication problem, or is it cleverness for its own sake? The NHS humor serves memorability of a serious message; a flip that confuses the message fails GP-17.
- If no flip survives the gate, log "advanced tier: intentionally absent — [reason]." Absence-as-decision passes; absence-as-miss fails.

### Step 4 — The Double-Whammy Check (strongest zones work twice)

For each high-stakes zone (hook, CTA, cards): does the element contrast its container AND does its internal content contrast itself? (Fashion-app exemplar: bold color cards pop off the white ground; each photo internally contrast-paired red-on-blue, blue-on-orange.) Upgrade at least one zone to double-whammy.

### Step 5 — The Audience Gate

> *"Both of these designs could actually have a time and a place depending on that target audience."*

Verify the stack's net feeling against the audience (GP-14): a hectic high-contrast "cheap" stack is CORRECT for a value-brief; a restrained premium stack is correct for luxury. Taste never overrides the gate.

### Step 6 — Output the Spec

Execution prompt: `references/prompts-v2/contrast-stack-spec.md`

## Content-Type Adaptations

| Surface | Typical stack | Watch for |
|---|---|---|
| **Poster** | Color + shape + texture (the Nike trio) | Zonal discipline; one style break max |
| **Landing page / UI** | Color (CTA) + size (option steering) + double-whammy cards | Contrast = choice architecture; red urgency signals |
| **Social carousel** | Size + color + one advanced flip on frame 1 | The flip IS the scroll-stopper |
| **Listing frame** | Color (label chips) + size (price) + texture (property photo vs. flat UI) | Photo already carries texture — don't double |
| **Logo/brand** | Typography (contrasting typefaces) + shape | Style contrast rarely belongs in a mark |
| **Editorial** | Typography + style + emotion | Emotion pairs carry longform mood |

## Output Requirements

A **Contrast Stack Spec**: (1) anchors + audience inputs, (2) the form table `FORM → ZONE → WHAT IT MAKES WIN` (3–5 rows), (3) advanced-tier norm/flip or logged absence, (4) double-whammy zone(s), (5) restraint log (forms deliberately not used, with reasons), (6) audience-gate verdict, (7) executable directives per zone (specific enough for a designer or generation prompt without re-asking).

## Quality Gate

Guards anti-patterns **#18 Flat emphasis**, **#1 decoration without reason**, **#16 feeling-audience mismatch**.

- [ ] ≥3 deliberate forms, each mapped to an anchor (no orphan contrast)
- [ ] Zonal, not global — at least one zone deliberately quiet
- [ ] Advanced tier attempted; kept only if it serves the message; absence logged as a decision
- [ ] One double-whammy zone minimum
- [ ] Restraint log present (what you did NOT use and why)
- [ ] Audience gate passed — the stack's feeling matches who's buying, not the designer's taste

## Related Workflows

- **`/satori-three-flow`** (21) — upstream: the anchors this stack serves
- **`/satori-contrast-audit`** (23) — the diagnostic twin for existing designs
- **`/satori-expectation-flip`** (25) — deep-dive when the advanced tier is the whole play
- **`/satori-color`** (17) — palette strategy the color-contrast decisions draw from
- **`/satori-feeling-calibrate`** (19) — when the gate fails: retune the stack's net feeling
- **`/satori-frontend-flow`** (26) — compiles this stack into UI section rhythm
