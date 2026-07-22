---
description: Replace descriptive paragraphs with 1-2 surgical details
---

# /connelly-detail

Deploy Michael Connelly's Telling Detail Engine.

## Steps

1. Load genius context: `skills/michael-connelly-vivid-writing/genius.md`
2. Load workflow: `skills/michael-connelly-vivid-writing/workflows/telling-detail-engine.md`
3. Execute the workflow against the provided draft or scene
4. Run quality gate from the workflow
5. Fire quality assurance per `directives/quality_assurance.md`

**Execution prompts**: before producing the deliverable, check `skills/michael-connelly-vivid-writing/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
