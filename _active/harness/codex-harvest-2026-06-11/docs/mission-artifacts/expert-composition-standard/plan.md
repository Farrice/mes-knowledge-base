# Unit Plan: Expert Composition Standard

Created: 2026-05-10
Mission: expert-composition-standard

Stable-ID rule: never renumber existing U-IDs after reordering, splitting, or deleting units.

## Implementation Units
- U1. **Composition Primitive**
  - Covers: R1, R2, AE2
  - Scope: `semantic_libraries/antigravity/primitives/expert-composition-contract.md`
  - Decision: create a general primitive with trigger signals, owner selection, contribution slots, handoffs, integration pass, score discipline, and fail conditions.
  - Tests or verification: required terms in `verify_expert_composition_standard.py`.
  - Dependencies: none.
- U2. **Command And Skill Bridge**
  - Covers: R3, AE1
  - Scope: `.agent/workflows/expert-composition-governor.md`, `.claude/commands/expert-composition-governor.md`, `.agents/skills/source-command-expert-composition-governor/SKILL.md`
  - Decision: expose the primitive as a route that can be invoked directly or selected by Autopilot/Orchestrate.
  - Tests or verification: `validate_skill.py`, command menu search, workflow router search.
  - Dependencies: U1.
- U3. **Harness Integration**
  - Covers: R4, AE2
  - Scope: `CODEX.md`, `.agent/workflows/autopilot.md`, `.agent/workflows/orchestrate.md`, `.agent/workflows/mission.md`, agent and skill primitives.
  - Decision: composition is mandatory when the task risks expert soup or more than three experts/skills/workflows are plausible.
  - Tests or verification: integration term checks and system verifiers.
  - Dependencies: U1, U2.
- U4. **Routing Promotion**
  - Covers: R5, AE1
  - Scope: `execution/routing_governor.py`, `execution/command_menu.py`, `execution/workflow_router.py`
  - Decision: expert composition becomes an intent lane, not a weak keyword match.
  - Tests or verification: route queries for expert soup, full arsenal, and hammer-vs-scalpel intent.
  - Dependencies: U2.
- U5. **Regression Guard And Capture**
  - Covers: R6, AE3
  - Scope: `execution/verify_expert_composition_standard.py`, `docs/solutions/expert-composition-standard.md`, mission artifacts.
  - Decision: make the standard durable, testable, and retrievable.
  - Tests or verification: verifier pass and solution lookup.
  - Dependencies: U1-U4.

## Sequencing
1. U1
2. U2
3. U3
4. U4
5. U5

## Risks
- Risk: The system still treats expert count as quality.
  - Mitigation: Score discipline in the primitive and Composition Ledger evidence requirements.
- Risk: Autopilot continues to choose broad strategy routes instead of composition.
  - Mitigation: routing governor lane plus explicit Autopilot trace field.
- Risk: The fix becomes another isolated command.
  - Mitigation: CODEX, Mission, Orchestrate, Agent Arsenal, and Skill System integration.

## Validation Mapping
| Assertion | Covered by U-ID | Validator | Pass signal |
|---|---|---|---|
| Expert soup has a named primitive and route | U1, U2 | `verify_expert_composition_standard.py` | PASS |
| The router promotes composition intent | U4 | command menu, workflow router, routing governor | `/expert-composition-governor` first for hammer-vs-scalpel query |
| The system specs require composition before output | U3 | static integration checks | CODEX/Autopilot/Mission/Orchestrate include composition references |
| The solution is reusable | U5 | solution capture | `docs/solutions/expert-composition-standard.md` exists |
