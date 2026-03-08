---
description: Run a multi-lens taste audit on a finished design using CEV framework, typography critique, composition analysis, and assumption scanning. Outputs scored report with specific refinement directives.
---

# /design-taste-gate — Design Quality Critique & Refinement

Takes a description of a finished or in-progress design and runs a multi-expert quality audit. Outputs specific, actionable refinement directives — not vague feedback, but exact changes formatted for copy-paste into Pencil or any design tool.

## Usage

```
/design-taste-gate [describe your current design state]
/design-taste-gate --quick "carousel with warm tones and serif typography"
/design-taste-gate --deep "landing page hero section — dark mode, gradient mesh background"
```

## Expert Stack

| Expert | Genius File | Role |
|--------|------------|------|
| **Oren** | `skills/oren-taste-development/genius.md` | CEV framework (Composition, Effectivity, Vibes) — the core quality lens |
| **Kittl** | `skills/kittl-graphic-design/genius.md` | Typography harmony audit + composition pattern analysis |
| **Mark Kashef** | `skills/mark-kashef-visual-design/genius.md` | Assumption Assassin — surface unstated assumptions and AI defaults |

## Steps

### 1. Capture Design State

Ask the user to describe the current design. Capture:
- **What was built**: Asset type, platform, dimensions
- **Design decisions made**: Fonts, colors, layout approach, imagery
- **What changed from the brief** (if a `/design-brief` was used): Deviations, adaptations, Pencil/tool modifications
- **What feels off** (if anything): User's gut reaction, specific concerns

If the user provides a design brief alongside the current state, diff them to identify divergence points.

### 2. Load Oren Genius — CEV Framework

Read `skills/oren-taste-development/genius.md`. Focus on Pattern 6 (CEV Matrix):

- **Composition**: Spatial logic, hierarchy clarity, balance, alignment consistency, whitespace rhythm
- **Effectivity**: Does the design achieve its stated purpose? Will it stop a scroll, communicate the message, drive the action?
- **Vibes**: Does the palette + type + composition create the intended emotional resonance? Does it feel cohesive or frankensteined?

### 3. CEV Audit

Score each dimension 1-10 with specific observations:

```
COMPOSITION: [X]/10
- [Specific observation about spatial relationships]
- [Specific observation about hierarchy]
- [Specific observation about alignment/grid]

EFFECTIVITY: [X]/10
- [Will this stop a scroll? Why/why not]
- [Is the message clear in <3 seconds?]
- [Is the CTA compelling and findable?]

VIBES: [X]/10
- [Emotional coherence assessment]
- [Does palette match intended mood?]
- [Typography personality alignment]
```

> **CHECKPOINT**: If `--quick` flag was used, skip to Step 8 (Generate Refinement Directives) using CEV scores only.

### 4. Load Kittl Genius — Typography & Composition Intelligence

Read `skills/kittl-graphic-design/genius.md`. Apply these audit patterns:

- **Pattern 1** (Mood-First): Do the fonts match the mood, or were they chosen arbitrarily?
- **Pattern 2** (Serif/Sans Mapping): Is the serif/sans choice aligned with the emotional target?
- **Pattern 3** (Height-Width Contrast): Does the font pairing have sufficient visual contrast?
- **Pattern 4** (Letter Spacing): Is tracking appropriate for the mood (tight = modern, loose = luxury)?
- **Pattern 5** (Line Spacing Compression): Is display type compressed enough for impact?
- **Pattern 11** (Gray Hierarchy): Is there clear primary/secondary/tertiary text differentiation?

### 5. Typography Audit

Score 1-10 with specific observations:

```
TYPOGRAPHY: [X]/10
- Font pairing harmony: [assessment]
- Tracking appropriateness: [assessment]
- Hierarchy clarity: [assessment — can you read the visual order in <1 second?]
- Weight contrast: [assessment — enough difference between levels?]
- Mood alignment: [assessment — do the fonts feel right for the brief?]
```

### 6. Composition Audit

Score 1-10 with specific observations:

```
COMPOSITION DETAIL: [X]/10
- Spatial logic: [assessment — do elements relate to each other intentionally?]
- Proportion: [assessment — are relative sizes creating the right emphasis?]
- Whitespace: [assessment — breathing room or claustrophobic?]
- Visual rhythm: [assessment — is there a repeating pattern that creates flow?]
- Edge alignment: [assessment — are elements on a grid or floating randomly?]
```

### 7. Assumption Scan

Load Mark Kashef Pattern 2 (Assumption Assassin) from `skills/mark-kashef-visual-design/genius.md`.

Surface unstated assumptions that may be degrading the design:

- **AI defaults**: Where did the tool/AI make choices that weren't specified? (Default spacing, generic color values, placeholder-style layouts)
- **Unstated assumptions**: What did the designer assume the viewer would understand without being shown?
- **Dangerous ambiguities**: Where could two reasonable people interpret the design differently?
- **Compound divergence**: Count the assumption points — 3+ unstated assumptions across 10+ elements = high divergence risk

```
ASSUMPTIONS SURFACED:
1. [Assumption] — Risk: [low/medium/high] — Fix: [specific fix]
2. [Assumption] — Risk: [low/medium/high] — Fix: [specific fix]
...
```

### 8. Generate Refinement Directives

Based on all audit scores, produce 3-7 specific, numbered, actionable fixes. These are NOT vague suggestions — they are exact changes formatted for execution:

**Good directive**: "Change subtitle tracking from 0 to +2px and reduce opacity from 100% to 60% to create secondary hierarchy"
**Bad directive**: "Make the typography better"

Each directive should include:
- **What to change** (specific element)
- **How to change it** (exact values)
- **Why** (which audit dimension it addresses)

Prioritize directives by impact — highest-impact fixes first.

> **CHECKPOINT for `--deep`**: If `--deep` flag was used, also load Kittl's Design Mastery & Quality Audit workflow (`skills/kittl-graphic-design/workflows/design-mastery-quality-audit.md`) and run a full professional-grade review. Append additional findings to the directive list.

### 9. Report

Present the complete taste gate report:

```
# Taste Gate Report: [Title]

## Scores
| Dimension | Score | Notes |
|-----------|-------|-------|
| Composition (CEV) | [X]/10 | [1-line summary] |
| Effectivity (CEV) | [X]/10 | [1-line summary] |
| Vibes (CEV) | [X]/10 | [1-line summary] |
| Typography | [X]/10 | [1-line summary] |
| Composition Detail | [X]/10 | [1-line summary] |

## Overall: [Average]/10 — [PASS / NEEDS REFINEMENT]
Pass threshold: >= 7.5 average

## Refinement Directives
1. [Specific change + why]
2. [Specific change + why]
3. [Specific change + why]
...

## Assumptions Surfaced
1. [Assumption + risk + fix]
2. [Assumption + risk + fix]
...

## Verdict
[1-2 sentences: What's working well, what's the single biggest lever for improvement]
```

If overall score >= 7.5: **PASS** — Design is production-ready with optional polish items.
If overall score < 7.5: **NEEDS REFINEMENT** — Apply directives and re-run taste gate.

## Options

- **`--quick`**: CEV audit only — skip detailed typography/composition audit and assumption scan. Fastest feedback loop.
- **`--deep`**: Add Kittl's full Design Mastery Quality Audit workflow for professional-grade review. Most thorough.
- **`--compare [brief]`**: Diff the current design against the original `/design-brief` output to identify where execution diverged from direction.
