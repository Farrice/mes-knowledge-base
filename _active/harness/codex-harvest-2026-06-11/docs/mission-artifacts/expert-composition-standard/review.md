# Review Ledger: Expert Composition Standard

Created: 2026-05-10
Mission: expert-composition-standard

## Scrutiny Review
- Scope reviewed: primitive, workflow, source command, Codex skill bridge, CODEX authority surface, Autopilot, Mission, Orchestrate, routing governor, command menu, workflow router, verifier, and solution capture.
- Checks run: `python3 execution/verify_expert_composition_standard.py`; targeted route checks for "hammer instead of scalpel many skills workflows."
- Findings: first verifier pass caught two misses: the skill lacked the exact `full arsenal` trigger and routing did not surface `/expert-composition-governor` for the hammer-vs-scalpel phrasing.
- Fixes applied: added exact trigger wording, created expert-composition intent detection and route bonuses in the routing governor, and wired command/workflow routers to use the new bonus.

## User-Outcome Review
- Intended user/client experience: the user can ask for the full arsenal without receiving expert soup. The system should pick one owner, use bounded specialist passes, skip overlaps, and show the integration evidence.
- Evidence inspected: command menu output, workflow router output, routing governor evaluation, and expert composition verifier.
- Gaps: domain-specific presets for writing, revenue, design, and system work can be added later after this generic primitive is exercised in real sessions.
- Decision: ship the primitive and keep future domain packs as optional expansions.

## Residual Work
| ID | Severity | Finding | Decision | Durable sink |
|---|---|---|---|---|
| RW1 | P2 | Composition Ledger is required by workflow convention but not yet enforced on every output type. | Accept for now; add domain-specific guards only after repeated real examples. | `semantic_libraries/antigravity/primitives/expert-composition-contract.md` |
| RW2 | P3 | Existing old workflows may still mention large expert stacks without this standard. | Let routing and Autopilot gate catch new work first; backfill only when a workflow is touched. | `.agent/workflows/` |
