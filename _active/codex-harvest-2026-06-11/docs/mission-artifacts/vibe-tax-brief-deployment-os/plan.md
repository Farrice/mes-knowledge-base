# Unit Plan: Vibe Tax Brief Deployment OS

Created: 2026-05-11  
Mission: vibe-tax-brief-deployment-os

Stable-ID rule: never renumber existing U-IDs after reordering, splitting, or deleting units.

## Implementation Units

- U1. **Mission spine and library decision**
  - Covers: R2, R3
  - Scope: Mission state and `docs/mission-artifacts/vibe-tax-brief-deployment-os/`
  - Decision: Extend existing Vibe Tax and Farrice Content OS routes.
  - Tests: `mission_control.py validate`
  - Dependencies: none

- U2. **Deployment command bridge**
  - Covers: R1, R2, AE4
  - Scope: `.agent/workflows/vibe-tax-deploy.md`, `.agents/skills/source-command-vibe-tax-deploy/SKILL.md`, `.claude/commands/vibe-tax-deploy.md`
  - Decision: `/vibe-tax-deploy` is a wrapper, not a replacement.
  - Tests: `validate_skill.py source-command-vibe-tax-deploy`, command/workflow search.
  - Dependencies: U1

- U3. **Fresh-session startup packet**
  - Covers: R3, R7, AE1
  - Scope: `_active/vibe-tax-brief-deployment-os/START-HERE.md`, `BOOTSTRAP-PROMPT.md`, `DEPLOYMENT-RUNBOOK.md`
  - Decision: Make a new session immediately operable without hidden chat context.
  - Tests: artifact guards and manual cold-start read.
  - Dependencies: U2

- U4. **Research and proof ledger**
  - Covers: R4, AE3
  - Scope: `_active/vibe-tax-brief-deployment-os/RESEARCH-LEDGER.md`
  - Decision: Keep numbers out of launch copy unless they are cited; use research as proof support.
  - Tests: source URLs present; public post avoids unsupported stats.
  - Dependencies: U3

- U5. **First LinkedIn launch draft**
  - Covers: R5, R6, R8, AE2
  - Scope: `_active/vibe-tax-brief-deployment-os/LINKEDIN-LAUNCH-POST.md`, content card
  - Decision: Lead with false-signal buyer tension, not AI consulting.
  - Tests: Copy Gate Result, voice evidence, no external action.
  - Dependencies: U4

- U6. **Mission package context enforcement**
  - Covers: R9, R10, AE5, AE6
  - Scope: `execution/mission_control.py`, `execution/verify_mission_package_handoff.py`, `.agent/workflows/autopilot.md`, `.agent/workflows/orchestrate.md`, `.agent/workflows/vibe-tax-deploy.md`, mission state
  - Decision: Approved mission packages must be resolved and shown before downstream workflows draft, route, or hand off.
  - Tests: `mission_control.py context vibe-tax-brief-deployment-os`, `verify_mission_package_handoff.py`, existing control-plane and Vibe Tax validators.
  - Dependencies: U1, U2, U3, U4, U5

## Sequencing

1. U1
2. U2
3. U3
4. U4
5. U5
6. U6

## Risks

- Generic AI consulting drift: mitigate with Vibe Tax source and Farrice voice lock.
- Expert soup: mitigate with one content owner and bounded expert slots.
- Unsupported claim leakage: mitigate with research ledger and source labels.
- Premature external action: mitigate with draft-only status and hard rules.
- Approved package not recovered in active runs: mitigate with Mission Package Context Resolver and Mission Handoff Receipt.

## Validation Mapping

| Assertion | Covered by U-ID | Validator | Pass signal |
|---|---|---|---|
| `/vibe-tax-deploy` is discoverable and bridged | U2 | scrutiny | command search and skill validation pass |
| Fresh session can resume without this chat | U3 | user-outcome | bootstrap prompt names source paths and first command |
| Public copy is grounded and draft-only | U4, U5 | scrutiny/user-outcome | research ledger exists, post has Copy Gate Result, no publish action |
| Existing OS is extended, not duplicated | U1, U2 | scrutiny | workflow names `/vibe-tax-brief` and `/farrice-content-os` as owners |
| Approved mission package is recovered before active deployment | U6 | scrutiny/user-outcome | context resolver includes approved load set and workflows require Mission Handoff Receipt |
