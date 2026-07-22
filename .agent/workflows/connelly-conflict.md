---
description: Vonnegut Conflict Audit
---

# /connelly-conflict

Deploy Michael Connelly's Vonnegut Conflict Audit.

## Steps

1. Load genius context: `skills/michael-connelly-vivid-writing/genius.md`
2. Load workflow: `skills/michael-connelly-vivid-writing/workflows/conflict-audit.md`
3. Execute the workflow against the provided draft with characters identified
4. Produce conflict map, dead zone report, and ambient conflict suggestion
5. Run quality gate from the workflow
6. Fire quality assurance per `directives/quality_assurance.md`

**Execution prompts**: before producing the deliverable, check `skills/michael-connelly-vivid-writing/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
