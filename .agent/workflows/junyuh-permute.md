---
description: Generate 50+ brand-aligned content ideas via permutation
---

# /junyuh-permute — Content Permutation Engine

## Steps

1. **Load Context**: Read `skills/jun-yuh-creator-vision/genius.md` at Tier 2.
2. **Pre-Flight**: Confirm Creator Vision exists. If not, route to `/junyuh-identity`.
3. **Execute Workflow**: Run `skills/jun-yuh-creator-vision/workflows/content-permutation-engine.md`.
4. **Deliver**: Produce the ranked idea list and 2-week calendar as a conversation artifact.
5. **Finalize**: Run chain_runner.py finalize with expert=jun-yuh-creator-vision, skill=jun-yuh-creator-vision, workflow=content-permutation-engine, type=Content.

**Execution prompts**: before producing the deliverable, check `skills/jun-yuh-creator-vision/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
