---
description: LIFT system layered diagnostic on any layout — Leverage / Eye / Friction / Transferability scored with rewrite directives
---

# /satori-lift-audit — LIFT System Diagnostic

Audit any layout (poster, slide, listing card, web hero, ad, social tile) against Satori's LIFT system. Produces a scored diagnostic + specific rewrite directives.

## Pre-Flight Gate

**Use this when**:
- A layout is in draft and needs structural critique before delivery
- A live layout is underperforming and you need to diagnose why
- You're stress-testing a competitor's layout to learn from it
- You want a defensible rationale for a redesign brief

**Do NOT use this when**:
- The design is still at concept/sketch stage — too early; use `/satori-why-before-what` first
- It's a logo (LIFT is for layouts; use `/satori-logo-concept` for logos)
- It's pure typography decisions (use Kittl)
- The brief itself is unclear — fix the brief first via `/satori-why-before-what` or one-sentence reduction

## Skill Acquisition

Load before executing:
- `genius.md` — GP-06 (LIFT System), GP-04 (Movement Ladder), GP-12 (Flip Test)
- `references/lift-system-decision-criteria.md` — full scoring rubric, edge cases
- `references/movement-flow-ladder.md` — for the "I" dimension

## Execution

### Step 1: Pre-Apply Checklist

Confirm before scoring:
- [ ] One-sentence brief documented (what the design is for)
- [ ] Visual primitive identified (line type / geometry / motif)
- [ ] Predictive-empathy emotion identified (desired *next* emotion)
- [ ] Why-before-what gate passed (every element has a reason)

If any item is missing, **halt scoring** and route to `/satori-why-before-what` or `/satori-logo-concept` (as appropriate). LIFT score on a foundation-less design is meaningless.

### Step 2: Score Each Dimension (1-10)

#### L — Leverage Point
- Identify the leverage element (the one most-important thing)
- Test: Could a stranger name it in <2 seconds?
- Document the dominance tools used (scale / contrast / positioning / isolation)
- Identify any competing leverage candidates → these are friction with the wrong dimension
- **Score 1-10** (anchor: 10 = unmistakable in <1 sec, 6 = needs 4-5 sec, 4 = ambiguous)

#### I — Internal Rhythm (Eye Choreography)
- Trace the eye journey: where does the eye go 1st, 2nd, 3rd?
- Test: Is spacing predictable enough to trust?
- Test: Is there at least one deliberate disruption that re-engages?
- Test: Does the journey end at the desired action point?
- **Score 1-10** (anchor: 10 = beat-by-beat choreographed, 6 = exists but accidental, 4 = bouncing eye)

#### F — Friction & Flow
- Identify friction zones (tight spacing, blur, rotated elements, scribble, half-cuts)
- Categorize each: GOOD friction (serves leverage) or BAD friction (competes/noises)
- Identify flow zones (smooth-reading sections that release tension)
- Compute friction-to-flow ratio (~80/20 standard, 60/40 for editorial, 50/50 = chaos territory)
- **Score 1-10** (anchor: 10 = precisely placed friction at leverage, 6 = friction unclear, 4 = noise-as-friction)

#### T — Transferability
- Run the Thumbnail Test (mental: shrink to 64×64 px — does it hold?)
- Run the Light/Dark Test (does it work on white AND black?)
- Run the Format Test (mock at 2 relevant formats — mobile, desktop, square social, vertical reel, A4 print)
- Identify any size/format-dependent failures
- **Score 1-10** (anchor: 10 = holds across thumbnail + light/dark + 3 formats, 6 = full size only, 4 = ideal context only)

### Step 3: Compute Composite + Veto Check

| Composite (sum of 4) | Grade | Action |
|---|---|---|
| 36-40 | A — Ship | Polish only |
| 32-35 | B — Polish | Minor work on weakest dimension |
| 28-31 | C — Rework | Rework weakest 1-2 dimensions |
| 24-27 | D — Major | Restart at concept layer |
| <24 | F — Restart | Concept is wrong |

**Veto rule**: If any single dimension scores ≤4, composite cannot exceed C grade regardless of total.

### Step 4: Rewrite Directives

For each dimension scoring <8, produce 2-3 specific rewrite directives. Format:

```
DIMENSION: [L/I/F/T]
SCORE: [n/10]
ANCHOR: [why this score, not 8 or 6]
DIRECTIVE 1: [specific change — element, location, method]
DIRECTIVE 2: [specific change]
DIRECTIVE 3: [specific change]
```

Directives must be **executable** (not "improve hierarchy" but "scale headline 1.4× larger; reduce subhead leading from 1.4 to 1.2").

### Step 5: Flip-Test Confirmation (free 90-sec check)

Run the Flip Test mentally — describe what flipping would reveal:
- Alignment: is everything baseline-aligned or are baselines drifting?
- White space: is it intentional or accidental?
- Edge tension: are elements too close to bleed?
- Visual weight: is one quadrant heavier than the others without reason?

Add findings to the directive list.

### Step 6: Output the Audit

```markdown
# LIFT Audit — [layout name]

**One-sentence brief**: [...]
**Visual primitive**: [...]
**Predictive-empathy emotion**: [...]

## Scores
| Dimension | Score | Anchor |
|---|---|---|
| L (Leverage) | n/10 | ... |
| I (Eye) | n/10 | ... |
| F (Friction) | n/10 | ... |
| T (Transferability) | n/10 | ... |
| **Composite** | **n/40** | **Grade [A/B/C/D/F]** |

## Rewrite Directives
[per-dimension list]

## Flip-Test Findings
[bullet list]

## Verdict
[Ship / Polish / Rework / Major rework / Restart]

## Next workflow
[Recommend: /satori-flip-test, /satori-predictive-empathy, /satori-anti-ai-slop, etc. based on weakest dimension]
```

## Content Type Adaptations

| Content type | LIFT focus | Common failure |
|---|---|---|
| **Poster** | Strong on L+T; F often overdone | Multiple competing leverage points |
| **Web hero** | Strong on T; weak on F | No friction = boring; too much = chaos |
| **Listing reel frame** | Strong on L (price + bedrooms); T critical (mobile + thumbnail) | Hierarchy lost at thumbnail |
| **Slide deck** | Strong on I/internal rhythm; weak on T (rarely tested cross-format) | Slides break in screenshot/share-card |
| **Social tile** | T (square ↔ vertical) is everything | Concept built for one aspect ratio only |
| **Ad creative** | L (CTA) must be unmistakable | Decoration outweighs CTA |
| **Logo** | DOES NOT APPLY — use `/satori-logo-concept` | Don't try to LIFT a logo |
| **Type-only design** | F is over-weighted; T weak | Use Kittl typography scoring instead |

## Output Requirements

Audit must include:
1. Pre-apply checklist with explicit pass/fail (no scoring without foundation)
2. All four dimensional scores with anchor justifications (no naked numbers)
3. Composite grade + veto status
4. Rewrite directives that are **executable** (specific element + change + method)
5. Flip-test findings as bullet list
6. Recommended next workflow

## Quality Gate (Genius Rubric)

Before delivering the audit, verify against `genius.md` quality criteria:

- [ ] **Why-defensibility**: Each rewrite directive references a why-rule, not aesthetic preference
- [ ] **Anchored scores**: Every score names which anchor it matches and why
- [ ] **Veto applied**: If any dimension ≤4, composite grade reflects the veto
- [ ] **Executable directives**: A second designer could implement directives without re-asking

If any check fails, revise the audit before delivery.

## Source Grounding

Direct quote from Satori (genius.md GP-06):
> *"The mastery here is kind of like a time-based journey on a design. That's when you've truly mastered flow."*

This audit is the formal version of that mastery — making the choreography explicit and testable instead of intuited.
