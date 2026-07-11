---
name: "Critique Loop Optimizer"
source_prompt: "skills/mark-kashef-banana-squad/references/prompts/critique-loop-optimizer.md"
skill: mark-kashef-banana-squad
standard: structure-pure-v2
refactored: 2026-07-11
---

# Critique Loop Optimizer

## Purpose
Fine-tune the Critic agent's evaluation criteria, minimum quality thresholds, and iteration depth to match your use case — from quick social content to premium brand imagery.

## Configuration Presets

### Quick Content (Social Media, Blog Headers)
```
QUALITY_THRESHOLD: 6/10
MAX_ITERATIONS: 1
SCORING_WEIGHTS:
  composition: 0.15
  color_harmony: 0.15
  detail_quality: 0.10
  brand_alignment: 0.30
  emotional_impact: 0.30
PASS_CRITERIA: "Must meet threshold on brand_alignment AND emotional_impact"
```

### Professional Content (Landing Pages, Ads, Thumbnails)
```
QUALITY_THRESHOLD: 7.5/10
MAX_ITERATIONS: 2
SCORING_WEIGHTS:
  composition: 0.20
  color_harmony: 0.20
  detail_quality: 0.15
  brand_alignment: 0.25
  emotional_impact: 0.20
PASS_CRITERIA: "Must meet threshold on ALL dimensions"
```

### Premium Brand (Print, Campaigns, Hero Images)
```
QUALITY_THRESHOLD: 8.5/10
MAX_ITERATIONS: 3
SCORING_WEIGHTS:
  composition: 0.25
  color_harmony: 0.20
  detail_quality: 0.25
  brand_alignment: 0.15
  emotional_impact: 0.15
PASS_CRITERIA: "Must meet threshold on ALL dimensions. Detail quality weighted highest."
```

## When To Use
- Before starting a Banana Squad session, set the quality level
- When images keep not meeting expectations (raise thresholds)
- When spending too many API calls (lower thresholds, reduce iterations)
- When switching between use cases (social vs. premium)

## Output Contract
For every generated image, the Critic agent produces exactly one scorecard containing: five numeric scores (composition, color harmony, detail quality, brand alignment, emotional impact, each 0-10 with a one-line reason), the weighted total computed from the active preset's SCORING_WEIGHTS, a single verdict (PASS / ITERATE / REJECT) evaluated against that preset's PASS_CRITERIA, and — only when the verdict is ITERATE — specific improvement notes directing the next generation pass.

## Output Skeleton
```
IMAGE: [filename]
SCORES:
  Composition:      [X/10] — [one-line reasoning]
  Color Harmony:    [X/10] — [one-line reasoning]
  Detail Quality:   [X/10] — [one-line reasoning]
  Brand Alignment:  [X/10] — [one-line reasoning]
  Emotional Impact: [X/10] — [one-line reasoning]

WEIGHTED TOTAL: [X/10]
VERDICT: PASS / ITERATE / REJECT
IMPROVEMENT NOTES: [If ITERATE, specific direction for next generation]
```

## Quality Gate
- [ ] The active preset (Quick / Professional / Premium) is stated before scoring begins
- [ ] All 5 dimensions are scored with a one-line reason each — no blank or skipped dimension
- [ ] The weighted total is computed using the preset's declared SCORING_WEIGHTS, not an ad hoc average
- [ ] The verdict matches the preset's PASS_CRITERIA exactly (e.g. Quick Content requires threshold on brand_alignment AND emotional_impact specifically, not just the weighted total)
- [ ] ITERATE verdicts always carry improvement notes; PASS/REJECT verdicts do not require them
- [ ] Iteration count for a single image never exceeds the preset's MAX_ITERATIONS
