---
description: Extract transferable one-sentence principles from content breakdowns
---

# Principle Extraction

Extract transferable one-sentence principles from completed Detail Stack breakdowns.

## Workflow

1. Load `skills/alex-content-science/genius.md`
2. Load `skills/alex-content-science/workflows/02-principle-extraction-engine.md`
3. **If breakdown sources include video URLs**, fetch visual context first (additive, auto-skips non-video):
   ```bash
   // turbo
   python3 execution/fetch-video-context.py "<source-url>" "<source-slug>" || true
   ```
   Visual-extracted principles (e.g., "first-frame visual contradicts opening line") are often the highest-transferability — they survive across content types because they're structural, not topical. See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md).
4. Execute the Principle Extraction Engine with completed breakdown(s)
5. Deliver:
   - Mechanism identification for each breakdown
   - One-Sentence Principles (zero content references)
   - Categorization (Visual, Structural, Psychological, Emotional, Sonic, Identity)
   - Transferability scoring (Universality, Actionability, Originality)
   - Principle stacks (compound combinations)
6. Quality gate: every principle passes zero-reference test, 3+ score 4+ on all dimensions
