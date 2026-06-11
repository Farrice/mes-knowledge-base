# Requirements: Knowledge Librarian Solution Surfacing

Created: 2026-05-08
Mission: knowledge-librarian-solution-surfacing

## Problem Frame

Let Knowledge Librarian surface reusable `docs/solutions/` entries during future missions.

## Requirements

- R1. Knowledge Compiler must expose a command that inventories and searches `docs/solutions/`.
- R2. Knowledge Librarian workflow must run solution search during focus-based pulses and show a Reusable Solutions section.
- R3. Mission OS must run solution search during librarian preflight and require applicable solution docs in the Library Decision.
- R4. Knowledge Librarian agent guidance must treat solution reuse as a first-class competency.
- R5. The pattern must be captured as a reusable `docs/solutions/` entry.

## Actors

- A1. Knowledge Librarian.
- A2. Mission OS.
- A3. Future mission orchestrators and validators.
- A4. Farrice.

## Key Flows

- F1. A mission objective is known -> Mission OS runs `knowledge_compiler.py solutions` -> applicable solution docs are reviewed before chartering.
- F2. Knowledge Librarian produces a pulse -> Reusable Solutions names exact docs and mission uses.
- F3. A mission creates new reusable learning -> `solution-capture.md` promotes it to `docs/solutions/` when generalizable.

## Acceptance Examples

- AE1. Given the query "mission engineering artifact contract", solution search returns `docs/solutions/mission-engineering-artifact-contract.md`.
- AE2. Given future mission planning, `/mission` includes solution search before command routing and chartering.
- AE3. Given a Knowledge Librarian pulse, output includes a Reusable Solutions section before sleeping giants or new-work recommendations.

## Scope Boundaries

- In scope: deterministic solution search, workflow instructions, agent guidance, reusable solution doc, smoke validation.
- Out of scope: destructive library consolidation, external sync, or broad changes to the knowledge manifest.

## Open Questions

- Blocking: none.
- Deferred: whether `docs/solutions/` should later be merged into the larger manifest after it grows.
