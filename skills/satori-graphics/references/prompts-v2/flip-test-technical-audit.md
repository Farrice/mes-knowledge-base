---
name: "Satori Graphics — Flip-Test Technical Audit"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Satori's **Flip-Design Technical Audit** — the fastest, freest, most ruthlessly diagnostic check in the Satori toolkit. Flip the design upside down and the brain stops reading content and starts seeing structure. This surfaces amateur technical tells (alignment drift, spacing inconsistency, edge tension, weight imbalance, optical sizing errors) that are invisible during normal front-facing viewing. This is a *structural* audit only — content critique, concept critique, and emotional-landing critique belong to other Satori tools, not here.

> "You can flip your design upside down. Now, look at it again. When you do this, your brain stops reading the content and the context of the work itself, and it starts seeing the actual structure instead." — Satori

## Input Required

- **[DESIGN / LAYOUT]** — the design heading to delivery, or the design you're diagnosing because it "feels off"
- **[FORMAT]** — print poster / web hero / mobile screen / slide deck / listing reel frame / newsletter / logo lockup / editorial spread / social tile / app icon (drives which check carries the highest risk)
- **[STAGE]** — final pre-ship check, mid-project fresh-eyes pass, or auditing someone else's work

## Execution Protocol

### Step 1 — Flip the Design

Rotate 180° (Figma/InDesign rotate tool, image-viewer rotate, or — for experienced eyes only — mental flip). Set a 90-second timer. Examine only the flipped version.

### Step 2 — Run the 6-Point Check

1. **Alignment.** Are baselines aligned across columns? Are vertical edges consistent (paragraph left edges, card right edges)? Is optical alignment achieved, not just mathematical? Common errors: subtle baseline drift across columns, rounded shapes reading larger than rectangles at identical dimensions, type baselines unaligned to image bottoms.
2. **White Space (Macro).** Consistent outer margin, or asymmetric without a stated reason? Section gaps proportionate to content density? At least one breathing zone, or is the design wall-to-wall? Common errors: margins that "feel right" but are actually random pixel values; uniform section gaps with no rhythm; no breathing zone at all.
3. **White Space (Micro).** Consistent leading within type blocks? Visually even letter-spacing, especially in display type? Consistent inter-element gaps within groups? Common errors: inconsistent leading with no system; default (loose) tracking on display type; inconsistent card/list inner padding.
4. **Edge Tension.** Elements too close to bleed (will clip in print)? CTAs or important elements dangerously close to edges? At least 0.25"/6mm safety margin from cut/bleed? Common errors: logos pushed into corners with no safety; text near edges that will clip on smaller screens; crowded gutters.
5. **Visual Weight Balance.** Does any quadrant look heavier without reason when flipped? Is the leverage point still obvious flipped (or only obvious when content bias kicks in)? Are decorative weights (illustrations, badges, photos) balanced or stacked on one side? Common errors: heavy bottom-right from default photo placement leaving top-left empty without intent; two competing focal points becoming visible once content stops biasing attention.
6. **Optical Sizing.** Do elements that should read as equal actually read as equal? (Squares read smaller than circles at identical dimensions; sharp angles read larger than rounded ones.) Are headlines optically aligned, not just mathematically centered? Do icon weights match adjacent type weight? Common errors: round marks and square buttons at matched dimension reading unequal; icon strokes heavier/lighter than adjacent type; mathematically-centered headlines that read optically off-center due to character shapes.

### Step 3 — Document Findings

For each issue: check number, issue description, severity, fix.

### Step 4 — Severity Triage

- **High**: structural failure, clipping, illegibility, alignment errors visible at full size — MUST fix before delivery
- **Medium**: visible to a trained eye, less so to general audience — fix unless under deadline
- **Low**: only visible to a trained designer — fix on next iteration if time permits

### Step 5 — Speed Validation

Confirm the pass stayed under 90 seconds. If it went over: first-time-use latency is expected and improves with reps; a design too complex for a fast structural read may itself need composition simplification; or the pass drifted from structure into content critique — re-scope to structure only.

## Output Contract

A Flip-Test Report: duration, all 6 checks examined (none skipped), a findings table with severity per issue, severity counts, and a pre-delivery verdict. This is a structural-only report — no content, concept, or emotional-landing commentary belongs in it.

## Output Skeleton

```markdown
# Flip-Test Report — [design name]

## Speed
- Duration: [n seconds] (target ≤90 sec)

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
[READY TO SHIP / NEEDS REWORK / NEEDS MAJOR REWORK]
```

## Quality Gate

- All 6 checks completed — none skipped
- Every High-severity issue is flagged as a MUST-fix, not optional
- Duration discipline held (≤90 seconds for the diagnostic pass, excluding fix time)
- Report stayed structural — no content or concept critique leaked in
- Re-flip recommended after fixes are applied, to confirm no new issues were introduced

## Deploy When

A design is heading to delivery (final pre-ship check); you've been staring at a design for hours and need a fresh-eyes structural read; you're auditing someone else's work fast; or a draft "feels off" but you can't articulate why. Do not use at concept/sketch stage — structural issues will just be re-introduced. Run the Why-Before-What Rent Test Audit first if the foundation itself is unresolved.
