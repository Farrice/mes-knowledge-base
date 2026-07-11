---
name: "Critique Loop Optimizer"
source_prompt: "extractions/mark-kashef-banana-squad/prompts/critique-loop-optimizer.md"
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
- **Deliverable**: one Critic scoring record per generated image, produced against the active preset's weights and pass criteria.
- **Format**: a fixed-field block — five dimension scores with one-line reasoning each, a weighted total, a verdict, and improvement notes when the verdict is ITERATE.
- **Cardinality**: one block per image evaluated; a batch of images gets one block each, never a merged summary.

## Output Skeleton
```
IMAGE: [filename]
PRESET: [Quick / Professional / Premium]
SCORES:
  Composition:      [X/10] — [one-line reasoning]
  Color Harmony:    [X/10] — [one-line reasoning]
  Detail Quality:   [X/10] — [one-line reasoning]
  Brand Alignment:  [X/10] — [one-line reasoning]
  Emotional Impact: [X/10] — [one-line reasoning]

WEIGHTED TOTAL: [X/10]
VERDICT: PASS / ITERATE / REJECT
IMPROVEMENT NOTES: [If ITERATE — specific direction for the next generation pass; omit if PASS/REJECT]
```

## Quality Gate
- [ ] All 5 dimensions are scored — none skipped or marked N/A without stated justification
- [ ] Weighted total is computed using the active preset's weights, not a flat average
- [ ] Verdict matches the active preset's PASS_CRITERIA rule exactly (e.g., "ALL dimensions" vs. "brand_alignment AND emotional_impact")
- [ ] ITERATE verdicts carry specific, actionable improvement notes — not vague feedback like "make it better"
- [ ] The active preset is named before scoring begins, so the threshold in effect is unambiguous
