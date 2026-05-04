---
description: 90-second pre-delivery technical audit — flip the design to see structure not content. Catches alignment, white-space, micro-rhythm errors invisible during normal viewing.
---

# /satori-flip-test — Flip-Design Technical Audit

The fastest, freest, most ruthlessly diagnostic check Satori teaches. Flip the design upside down. Your brain stops reading content and starts seeing structure. Catches amateur tells invisible during normal viewing. Ship it before delivery; never skip it.

## Pre-Flight Gate

**Use this when**:
- A design is heading to delivery — final pre-ship check
- You've been staring at a design for hours and need fresh-eyes diagnostic
- You're auditing someone else's work and want a fast structural read
- A draft "feels off" but you can't articulate why

**Do NOT use this when**:
- The design is at concept/sketch stage (too early — structural issues will be re-introduced)
- You haven't run `/satori-why-before-what` yet (the flip can't fix conceptual problems)
- The design is purely typographic in a way the flip won't reveal new issues (still useful, but combine with type-specific audit)

## Skill Acquisition

Load:
- `genius.md` — GP-12 (Flip-Design Technical Audit), GP-04 (Movement Ladder)
- `references/source-quotes.md` — Satori's verbatim flip-test material

## Execution

### Step 1: Flip the Design

**Tool options**:
- Figma / InDesign: rotate 180°
- Image preview: open in Preview / image viewer, rotate 180°
- Mental flip: experienced designers can flip mentally; for less experienced, always actually flip

Set a 90-second timer. Examine the flipped design.

### Step 2: Run the 6-Point Check

While flipped, examine each:

#### Check 1 — Alignment
- Are baselines aligned across columns? (Type baselines should hit consistent grid lines)
- Are vertical edges of elements consistent (left edges of paragraphs / right edges of cards)?
- Are elements visually aligned vs. only mathematically aligned (optical adjustments needed)?

**Common errors revealed**:
- Subtle baseline drift across columns
- Rounded shapes appearing larger than rectangles at same dimension (optical sizing needed)
- Type baselines unaligned to image bottoms

#### Check 2 — White Space (Macro)
- Is outer margin consistent on all sides? Or asymmetric without reason?
- Are section gaps proportionate to content density?
- Is there at least one breathing zone? Or is the design wall-to-wall content?

**Common errors revealed**:
- Margin "feels right" but is actually 18 / 22 / 16 / 24 px (random)
- Section gaps too uniform (every section same → no rhythm)
- No breathing zone (design exhausts the eye)

#### Check 3 — White Space (Micro)
- Is line leading consistent within type blocks?
- Is letter-spacing visually even (especially in display type)?
- Are inter-element gaps within groups consistent?

**Common errors revealed**:
- Tight leading on one paragraph, generous on another (no system)
- Display type with default tracking (visibly loose)
- Card/list items with inconsistent inner padding

#### Check 4 — Edge Tension
- Are elements too close to bleed (will get clipped in print)?
- Are CTAs / important elements floating in dangerous proximity to edges?
- Is there at least 0.25" / 6mm safety margin from cut/bleed?

**Common errors revealed**:
- Logos pushed into corners with no safety
- Text near edge that will clip in print or on smaller screens
- Inadequate gutter space leading to crowding

#### Check 5 — Visual Weight Balance
- When flipped, does any quadrant look heavier without reason?
- Is the leverage point still the obvious focal when flipped (or only when you can read the content)?
- Are decorative weights (illustrations, badges, photos) balanced or stacked on one side?

**Common errors revealed**:
- Heavy bottom-right (default photo placement) leaves top-left empty without intent
- Two competing focal points become obvious when content can't bias attention
- Stacked decorative elements that ride along one diagonal

#### Check 6 — Optical Sizing
- Do elements that should appear equal actually appear equal? (Squares look smaller than circles at identical dimensions; sharp angles look larger than rounded.)
- Are headlines optically aligned to display type vs mathematically aligned?
- Do icon weights match adjacent type weight?

**Common errors revealed**:
- Round logo same dimension as square button next to it (round looks smaller)
- Icons heavier or lighter than adjacent type stroke
- Headline mathematically centered but optically off-center due to character shapes

### Step 3: Document the Findings

For each issue found, document:

| Check # | Issue | Severity | Fix |
|---|---|---|---|
| 1 — Alignment | Subtle baseline drift in column 2 (baselines 4px lower than column 1) | High | Adjust column 2 starting baseline to align with column 1 |
| 2 — White space (macro) | Right margin 4px wider than left | Medium | Equalize to symmetric 32px or document asymmetric reason |
| 3 — Edge tension | CTA button only 8px from right edge | High | Move to 24px+ from edge for safety |
| ... | ... | ... | ... |

### Step 4: Severity Triage

- **High severity**: structural failure, clipping, illegibility, alignment errors visible at full size — MUST fix before delivery
- **Medium severity**: visible to a designer, less so to general audience — fix unless under deadline
- **Low severity**: only visible to a trained designer — fix on next iteration if time permits

### Step 5: Speed Validation

Confirm you stayed under 90 seconds for the diagnostic pass. If you went over:
- **Reason 1**: First time using the flip-test on this design — speed will improve with reps
- **Reason 2**: Design is too complex for fast structural read — investigate the complexity itself (may need composition simplification)
- **Reason 3**: You went past structural read into content critique — re-scope the test to structure only

The flip-test is a *structural* audit. Content critique belongs in different workflows (`/satori-why-before-what`, `/satori-predictive-empathy`).

### Step 6: Output the Flip-Test Report

```markdown
# Flip-Test Report — [design name]

## Speed
- Duration: [n seconds] (target: ≤90 sec)

## Findings

| Check | Issue | Severity | Fix |
|---|---|---|---|
| 1 — Alignment | [...] | [H/M/L] | [...] |
| 2 — White space (macro) | [...] | [H/M/L] | [...] |
| 3 — White space (micro) | [...] | [H/M/L] | [...] |
| 4 — Edge tension | [...] | [H/M/L] | [...] |
| 5 — Weight balance | [...] | [H/M/L] | [...] |
| 6 — Optical sizing | [...] | [H/M/L] | [...] |

## Severity Counts
- High: [n] — MUST fix
- Medium: [n] — fix unless deadline
- Low: [n] — fix next iteration

## Pre-Delivery Verdict
- [ ] All HIGH issues fixed
- [ ] All MEDIUM issues fixed (if not deadline)
- [ ] Re-flip after fixes to confirm

## Verdict
- READY TO SHIP / NEEDS REWORK / NEEDS MAJOR REWORK
```

## Content Type Adaptations

| Content type | Highest-risk check | Common amateur tell |
|---|---|---|
| **Print poster** | 4 — Edge tension (bleed clipping) | Important elements within 1cm of bleed |
| **Web hero** | 5 — Visual weight (stacked photo right-side) | Empty top-left; heavy bottom-right |
| **Mobile screen** | 4 — Edge tension (notch / safe area) | CTA below the fold or behind notch |
| **Slide deck** | 1 — Alignment (drift across slides) | Each slide drifts a few pixels from previous |
| **Listing reel frame** | 5 — Visual weight + 3 — micro spacing | Price tag floating without visual anchor |
| **Newsletter** | 2 — Macro white space | Sections with no breathing zone |
| **Logo lockup** | 6 — Optical sizing | Mark and wordmark mathematically aligned but optically off |
| **Editorial spread** | 1 — Alignment + 6 — optical | Baseline grid abandoned for "feel" |
| **Social tile** | 4 — Edge tension (square crop) | Important content too close to edge for square crops |
| **App icon** | 6 — Optical sizing | Icon mathematically centered but optically off in launcher |

## Output Requirements

Report must include:
1. Duration documented (target ≤90 seconds)
2. All 6 checks examined (no skips)
3. Findings table with severity per issue
4. Severity counts
5. Pre-delivery verdict (ready / rework / major rework)

## Quality Gate (Genius Rubric)

- [ ] **6 checks completed** — none skipped
- [ ] **All HIGH issues fixed** before ship
- [ ] **Re-flip** after fixes (confirm fixes don't introduce new issues)
- [ ] **Time discipline** — ≤90 seconds for the audit (excluding fixes)
- [ ] **Structural focus** — content critique stayed out of this workflow

## Source Grounding

> *"You can flip your design upside down. Now, look at it again. When you do this, your brain stops reading the content and the context of the work itself, and it starts seeing the actual structure instead."* — Satori

> *"This is good for testing and seeing if your design works on a technical level. So, the alignment, the white space, the micro white space."* — Satori

> *"It does ensure that you don't have any kind of amateur mistakes, technically speaking."* — Satori
