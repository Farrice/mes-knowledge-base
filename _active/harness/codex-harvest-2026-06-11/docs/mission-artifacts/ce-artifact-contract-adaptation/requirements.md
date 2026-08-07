# Requirements: CE Artifact Contract Adaptation

Created: 2026-05-08
Mission: ce-artifact-contract-adaptation

## Problem Frame

Adapt Compound Engineering-style artifact contracts into Antigravity Mission OS without replacing existing routers, Knowledge Librarian, or command bridges.

## Requirements

- R1. Mission Control must support an optional engineering artifact contract while keeping `none` as the default.
- R2. The engineering contract must create durable starter artifacts for strategy, requirements, U-ID planning, review, solution capture, and pulse reporting.
- R3. Mission OS workflow instructions must tell future agents when to use the engineering contract and when to skip it.
- R4. Existing missions without the contract must continue to work and validate.
- R5. Reusable solved problems and signal reports must have visible durable sinks under `docs/solutions/` and `docs/pulse-reports/`.

## Actors

- A1. Farrice, who wants compounding system work without extra magic words.
- A2. Codex Mission OS, which creates state and enforces validation.
- A3. Future agents, who need artifact continuity across sessions.
- A4. Validators, who check correctness, usability, and non-duplication.

## Key Flows

- F1. User asks for a system/code mission -> Mission OS creates state with `--artifact-contract engineering` -> starter artifacts are created.
- F2. Worker updates U-ID plan and artifacts during implementation -> validator checks files and handoff.
- F3. A generalizable learning appears -> solution capture promotes or links it to `docs/solutions/`.
- F4. A shipped or delivered mission produces signal -> pulse is recorded mission-locally and optionally promoted to `docs/pulse-reports/`.

## Acceptance Examples

- AE1. Given a new system mission, when `mission_control.py create --artifact-contract engineering` runs, then six starter artifact files exist under `docs/mission-artifacts/<slug>/`.
- AE2. Given an engineering-contract mission, when validation runs after librarian completion, then validation passes only if the artifact contract section and files exist.
- AE3. Given an older mission without an artifact contract, when validation runs, then the mission is not forced to create engineering artifacts.
- AE4. Given a future agent reading `/mission`, when the work is code/system/product infrastructure, then the agent knows to use the engineering artifact contract instead of adding duplicate CE commands.

## Scope Boundaries

- In scope: Mission OS workflow, mission state helper, artifact starter templates, durable docs folders, and a live smoke mission.
- Out of scope: wholesale Compound Engineering plugin installation, external repo dependency, new slash command surface, and changes outside `/Users/farricecain/Codex Antigravity`.

## Open Questions

- Blocking: none.
- Deferred: whether to add a richer artifact-lint command after this contract sees repeated real-world use.
