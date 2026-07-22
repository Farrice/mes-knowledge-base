---
description: Context-engineered production — finished copy across 7 verticals
---

## Workflow: CE-Write (`/ce-write`)

**Expert**: Chase Hughes (Context Engineering) × craft experts
**Skill**: `skills/chase-hughes-context-engineering/`

The flagship production workflow. Vertical-aware. Input a vertical (social | content | media | storytelling | marketing | copywriting | ghostwriting) + brief + target/voice → output FINISHED, deployable copy. Runs a compressed PCP context-design internally, loads the craft expert(s) for the vertical, has the craft method write INTO the engineered context.

### Steps

1. Read the context-engineering spine:
   - `skills/chase-hughes-context-engineering/SKILL.md`
   - `skills/chase-hughes-context-engineering/genius.md`
   - `skills/chase-hughes-context-engineering/references/production-cross-pollination.md` (the vertical → craft-expert map)
   - `skills/chase-hughes-context-engineering/references/context-design-spec.md` (the compressed PCP logic)

2. Load the craft expert(s) for the chosen vertical (SKILL.md + genius.md) per the cross-pollination map in `ce-write.md`.

3. Read and execute the workflow:
   - `skills/chase-hughes-context-engineering/workflows/ce-write.md`

4. **Ethics gate on the finished output:**
   ```bash
   // turbo
   python3 execution/context_ethics_gate.py check --file <output-path> --kind copy --workflow ce-write --technique "<named technique>"
   # exit 2 = BLOCK (rewrite); REVIEW = clear flags; PASS = ship
   ```

5. Quality gate: Is this a FINISHED piece (publishable as-is), not a brief? Did the craft fuse with the context (the action feels self-chosen), rather than push the outcome? Could you defend it if the reader saw the design?

**Execution prompts**: before producing the deliverable, check `skills/chase-hughes-context-engineering/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
