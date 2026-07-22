---
description: Comprehensive audit of any copy against the full
---

# 360° Proof Audit

Run the 360° Proof Audit workflow from the Proof Ladder Architecture skill.

## Steps

1. Load the skill: read `skills/luke-iha-proof-ladder/SKILL.md`
2. Load genius context: read `skills/luke-iha-proof-ladder/genius.md`
3. Load the workflow: read `skills/luke-iha-proof-ladder/workflows/proof-audit-360.md`
4. Execute the workflow with user-provided inputs:
   - The copy asset to audit (paste, file path, or URL)
   - Context: what the copy is for, who the audience is
5. Produce the full audit report with tier-by-tier analysis and fix prescriptions
6. Finalize via chain_runner.py

**Execution prompts**: before producing the deliverable, check `skills/luke-iha-proof-ladder/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
