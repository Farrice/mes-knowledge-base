---
description: Build subtext dialogue
---

# /connelly-subtext

Deploy Michael Connelly's Subtext Dialogue Builder.

## Steps

1. Load genius context: `skills/michael-connelly-vivid-writing/genius.md`
2. Load workflow: `skills/michael-connelly-vivid-writing/workflows/subtext-dialogue-builder.md`
3. Gather inputs: characters, surface topic, real subtext conflict
4. Execute the workflow to produce layered dialogue with annotation
5. Run quality gate from the workflow
6. Fire quality assurance per `directives/quality_assurance.md`

**Execution prompts**: before producing the deliverable, check `skills/michael-connelly-vivid-writing/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
