---
description: Complete Proof Ladder strategy
---

# Proof Ladder Builder

Run the Proof Ladder Builder workflow from the Proof Ladder Architecture skill.

## Steps

1. Load: `skills/luke-iha-proof-ladder/SKILL.md` + `skills/luke-iha-proof-ladder/genius.md`
2. Load workflow: `skills/luke-iha-proof-ladder/workflows/proof-ladder-builder.md`
3. Execute with inputs: Offer, Audience, Current Proof Inventory, Primary Claim, Biggest Objection
4. Produce: 5-Tier Inventory, Gap Analysis, 30-60-90 Build Plan, Deployment Architecture, Next Win Prescription
5. Finalize via chain_runner.py

**Execution prompts**: before producing the deliverable, check `skills/luke-iha-proof-ladder/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
