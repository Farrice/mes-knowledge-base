# Unit Plan: High-Taste Writing OS

Created: 2026-05-10
Mission: high-taste-writing-os

Stable-ID rule: never renumber existing U-IDs after reordering, splitting, or deleting units.

## Implementation Units
- U1. **OS Workflow And Bridge**
  - Covers: R1, R3
  - Scope: `.agent/workflows/high-taste-writing-os.md`, `.agents/skills/source-command-high-taste-writing-os/SKILL.md`, `.claude/commands/high-taste-writing-os.md`, and semantic primitive.
  - Decision: companion OS layer, not a mega-skill.
  - Tests or verification: bridge existence and contract term checks.
  - Dependencies: none
- U2. **Agent And Front-Door Integration**
  - Covers: R2, AE1, AE2
  - Scope: Writing Agent, Copywriting Agent, Publishable Copy Gate, Autopilot, Orchestrate.
  - Decision: High-Taste Writing OS runs before final/publishable scoring when the failure is flow, taste, reader pull, or low-quality prose.
  - Tests or verification: routing searches and verifier integration checks.
  - Dependencies: U1
- U3. **Verifier**
  - Covers: R4
  - Scope: `execution/verify_high_taste_writing_os.py`.
  - Decision: deterministic check for bridge, integration, and route discoverability.
  - Tests or verification: verifier pass.
  - Dependencies: U1, U2
- U4. **Pilot Rewrite**
  - Covers: R5, AE3
  - Scope: `docs/mission-artifacts/high-taste-writing-os/pilot-ai-misfire-rewrite.md`.
  - Decision: prove the OS changes line-level quality and flow.
  - Tests or verification: prose classifier and user-outcome review.
  - Dependencies: U1

## Sequencing
1. U1
2. U2
3. U3
4. U4

## Risks
- Risk: The OS becomes another ceremonial gate. Mitigation: require line-level before/after evidence and a Taste Evidence Ledger.
- Risk: Too many experts create patched-together writing. Mitigation: one composer, many scalpels; max three primary craft lenses per pass.
- Risk: Router misses natural phrasing. Mitigation: verifier includes natural language route tests.

## Validation Mapping
| Assertion | Covered by U-ID | Validator | Pass signal |
|---|---|---|---|
| OS is command-invokable | U1 | verifier | bridge files exist and required terms are present. |
| Agents route low-taste writing through OS | U2 | verifier and router search | `/high-taste-writing-os` appears for natural queries. |
| OS obeys skill-system contract | U1 | manual contract review and verifier | required contract fields appear. |
| Pilot demonstrates line-level improvement | U4 | prose classifier and review ledger | pilot has final draft plus Taste Evidence Ledger. |
