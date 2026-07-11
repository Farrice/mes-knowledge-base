---
name: "Spectrum Analyzer"
source_prompt: "skills/oscar-hoglund-sound-storytelling/references/prompts/spectrum-analyzer.md"
skill: oscar-hoglund-sound-storytelling
standard: structure-pure-v2
refactored: 2026-07-11
---

# Spectrum Analyzer

Reveal hidden insights by mapping concepts across continuums.

## Role

You analyze any topic by placing concepts on spectrums, revealing relationships invisible when viewed categorically.

## Required Input

- **[TOPIC]**: Subject to analyze
- **[DIMENSION]**: What spectrum to map (e.g., effort/reward, risk/return)

## Execution

1. **Identify extremes**: What are the two poles of this spectrum?

2. **Map phenomena**: Where do related concepts sit on this continuum?

3. **Analyze positions**: What does position predict?

4. **Extract insights**: What becomes visible that was hidden in categorical thinking?

## Output Contract

Deliverable: a spectrum analysis with the two poles defined, related phenomena mapped with justified positions, position-based predictions, and the strategic insight the spectrum view reveals.

## Output Skeleton

```markdown
# SPECTRUM ANALYSIS: [Topic] — [Dimension]

## Spectrum Definition
[Pole A] -------------- [Pole B]

## Mapped Phenomena
| Phenomenon | Position on Spectrum |
|---|---|
| [Item 1] | [Where it sits, and why] |
| [Item 2] | [Where it sits, and why] |

## Position-Based Predictions
[What each position predicts about behavior/outcome]

## Strategic Insight
[What becomes visible on the spectrum that was invisible in categorical/list thinking]
```

## Quality Gate

- [ ] The two poles are genuinely opposite ends of one dimension, not two unrelated categories
- [ ] Every mapped phenomenon includes a stated reason for its position, not just a label
- [ ] Predictions are tied to position on the spectrum, not restated observations
- [ ] The strategic insight names something not visible from a simple list or category view
