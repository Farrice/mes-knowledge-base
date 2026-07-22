---
description: End-to-end master copywriting engine
---

# Proof Copy Engine — Master Workflow

Run the master end-to-end copywriting workflow from the Proof Ladder Architecture skill.

## Steps

1. Load the skill: read `skills/luke-iha-proof-ladder/SKILL.md`
2. Load genius context: read `skills/luke-iha-proof-ladder/genius.md`
3. Load the workflow: read `skills/luke-iha-proof-ladder/workflows/proof-copy-engine.md`
4. Execute the workflow with user-provided inputs:
   - Platform (YouTube / LinkedIn / Instagram / Article / Substack / Newsletter / Email / Ad / Sales Page / Twitter Thread / Carousel / All)
   - Topic
   - Core Mechanism
   - Proof Assets
   - Audience
   - Voice
   - Desired Outcome
5. If platform = "All", produce full content for primary platform then atomize across all others
6. Optional depth layer: when the user asks for emotional truth, heart, resonance, reader trust, less generic copy, or a more human feel, load `skills/lamott-allen-really-real-writing/` after proof checks. Use it to make proof feel honest and humane without inflating claims or weakening conversion.
7. Run quality gate (all 10 checks must pass)
8. Finalize via chain_runner.py

**Execution prompts**: before producing the deliverable, check `skills/luke-iha-proof-ladder/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
