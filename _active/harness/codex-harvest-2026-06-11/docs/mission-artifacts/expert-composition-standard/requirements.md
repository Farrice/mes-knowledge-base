# Requirements: Expert Composition Standard

Created: 2026-05-10
Mission: expert-composition-standard

## Problem Frame
Codify and implement the expert-soup detection and composition process as a system-wide primitive so Autopilot, Mission, Orchestrate, and operator agents can deploy the full Antigravity arsenal end-to-end without broad expert soup, hidden routing, or low-quality stacked outputs.

## Requirements
- R1. Define expert soup as an observable failure mode with trigger phrases and routing conditions.
- R2. Create a reusable Expert Composition Contract with owner selection, contribution slots, specialist handoffs, integration rules, and Composition Ledger.
- R3. Add a callable `/expert-composition-governor` workflow with source command and Codex skill bridge.
- R4. Update Autopilot, Mission, Orchestrate, CODEX, Agent Arsenal Routing Contract, and Skill System Contract so composition is mandatory when many experts or skills are plausible.
- R5. Teach the routing governor to promote `/expert-composition-governor` for expert-soup, full-arsenal, and hammer-vs-scalpel intent.
- R6. Add a verifier that fails when the primitive, route, integration, or routing behavior is missing.

## Actors
- A1. User invoking Autopilot, Mission, Orchestrate, or raw goal routing.
- A2. Router layer: command menu, workflow router, routing governor.
- A3. System primitives: agent arsenal routing, skill-system contract, CODEX authority surface.
- A4. Operator agents and future specialist stacks that need bounded roles.

## Key Flows
- F1. User says "full arsenal," "expert soup," "too many agents," or equivalent -> router promotes `/expert-composition-governor` -> system chooses one owner and bounded slots before execution.
- F2. A task surfaces more than three plausible experts or skills -> Autopilot/Mission/Orchestrate include the composition gate -> final output includes Composition Ledger for high-stakes work.
- F3. A future patch accidentally removes routing/integration -> verifier fails with the missing surface.

## Acceptance Examples
- AE1. Given "hammer instead of scalpel many skills workflows," when routing runs, then `/expert-composition-governor` appears first.
- AE2. Given a high-stakes multi-expert output, when the standard is applied, then it has one owner, contribution slots, skipped-expert reasons, evidence of change, and an expert soup pass/revise/rework decision.
- AE3. Given the verification command, when the harness is healthy, then it reports `Expert Composition Standard verification: PASS`.

## Scope Boundaries
- In scope: composition primitive, route, bridge files, routing governor, harness authority docs, verification, and mission/solution capture.
- Out of scope: rewriting every existing domain workflow, creating new expert personas, changing external publishing behavior, or spawning real Codex subagents without explicit authorization.

## Open Questions
- Blocking: none.
- Deferred: add domain-specific composition presets after the primitive proves useful across several real tasks.
