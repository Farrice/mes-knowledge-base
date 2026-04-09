# Evolution Log: Michael Connelly Vivid Writing

**Date**: 2026-04-09
**Skill**: michael-connelly-vivid-writing
**Workflow**: telling-detail-engine
**Aspect**: Detail Selection (Narrative Load Ranking)
**Status**: KEEP

## Hypothesis

Adding a "Narrative Load Ranking" step before the 3-Question Filter will produce telling details that carry more narrative weight. Instead of binary filtering (yes/no), rank candidates by counting how many of 7 narrative vectors they serve simultaneously (character, stakes, tension, foreshadowing, world-building, subtext, mood).

## Benchmark

**Prompt**: "Write a 150-word scene of an S&C coach's first meeting with a new executive client, using vivid writing principles."

### Control (3-Question Filter only)
- Selected detail: Theraband on laptop bag strap, knotted where it snapped
- Vector count: 2 (character, world-building)
- Composite score: 7.0

### Variant (+ Narrative Load Ranking)
- Selected detail: Shoulder hitch on handshake — "a flinch so practiced it had become posture"
- Vector count: 7 (character, stakes, tension, foreshadowing, world-building, subtext, mood)
- Composite score: 8.7

## Delta

| Dimension | Control | Variant | Delta |
|---|---|---|---|
| Telling Detail Economy | 7 | 9 | +2 |
| Narrative Momentum | 7 | 9 | +2 |
| Character Revelation | 6 | 9 | +3 |
| Subtext Density | 7 | 9 | +2 |
| Prose Transparency | 8 | 8 | 0 |
| Economy of Expression | 7 | 8 | +1 |
| **Composite** | **7.0** | **8.7** | **+1.7** |

## What Changed

Added Step 3 "Rank by Narrative Load" to `workflows/telling-detail-engine.md`. The step scores every candidate detail against 7 narrative vectors before applying the existing 3-Question Filter. Quality Gate updated with 2 new checks: was ranking performed, and does selected detail carry 4+ vectors.

## Key Insight

The Narrative Load Ranking forced a fundamentally different detail selection. The control picked an OBJECT (Theraband) that was clever but only served 2 vectors. The variant picked a BEHAVIOR (shoulder hitch during handshake) that served 7 vectors — and because it was a behavior rather than a prop, it also revealed the OTHER character (the coach's diagnostic eye), created a power shift, and generated forward momentum ("Your shoulder did"). High-vector details tend to be behaviors, not objects.
