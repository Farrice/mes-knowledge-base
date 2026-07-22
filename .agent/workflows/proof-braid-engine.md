---
description: Rewrite any draft
---

# Proof Braid Engine

Run the Proof Braid Engine from the Proof Ladder Architecture skill.

## Steps

1. Load: `skills/luke-iha-proof-ladder/SKILL.md` + `skills/luke-iha-proof-ladder/genius.md`
2. Load workflow: `skills/luke-iha-proof-ladder/workflows/proof-braid-engine.md`
3. Execute with inputs: Draft Copy, Available Proof Assets, Audience Temperature
4. Produce: Naked Claim Audit, Claim-Proof Matching Table, Braided Draft, Proof Annotations, Missing Proof Report
5. Finalize via chain_runner.py

**Execution prompts**: before producing the deliverable, check `skills/luke-iha-proof-ladder/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
