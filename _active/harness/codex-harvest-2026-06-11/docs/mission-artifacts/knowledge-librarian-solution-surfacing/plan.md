# Unit Plan: Knowledge Librarian Solution Surfacing

Created: 2026-05-08
Mission: knowledge-librarian-solution-surfacing

Stable-ID rule: never renumber existing U-IDs after reordering, splitting, or deleting units.

## Implementation Units

- U1. **Solution search command**
  - Covers: R1, AE1
  - Scope: `execution/knowledge_compiler.py`
  - Decision: Add lightweight inventory/search for `docs/solutions/`, separate from the full knowledge manifest.
  - Tests or verification: compile check; query returns the existing mission artifact contract solution.
  - Dependencies: none

- U2. **Knowledge Librarian pulse integration**
  - Covers: R2, R4, AE3
  - Scope: `.agent/workflows/knowledge-librarian.md`, `agents/knowledge-librarian/AGENT.md`, `.agent/knowledge-librarian-state.md`
  - Decision: Surface reusable solution docs before recommending new plans, assets, or commands.
  - Tests or verification: text checks for Reusable Solutions and solution search command.
  - Dependencies: U1

- U3. **Mission OS Library Decision integration**
  - Covers: R3, AE2
  - Scope: `.agent/workflows/mission.md`
  - Decision: Mission preflight runs solution search and Library Decision must state apply/adapt/ignore/promote for relevant docs.
  - Tests or verification: text checks and mission validation.
  - Dependencies: U1

- U4. **Reusable solution capture**
  - Covers: R5
  - Scope: `docs/solutions/knowledge-librarian-solution-surfacing.md`
  - Decision: Capture the pattern so future system expansions reuse this solution-first move.
  - Tests or verification: solution search finds the new entry.
  - Dependencies: U1, U2, U3

## Sequencing

1. U1
2. U2
3. U3
4. U4

## Risks

- Over-surfacing irrelevant docs: mitigated by scoring query/title/path/content overlap.
- Adding another thing to remember: mitigated by embedding solution search in Knowledge Librarian and Mission OS workflows.
- Manifest bloat: mitigated by keeping solution docs in a focused lightweight command until the folder grows.

## Validation Mapping

| Assertion | Covered by U-ID | Validator | Pass signal |
|---|---|---|---|
| Solution search works | U1 | scrutiny | Query returns relevant solution docs |
| Knowledge Librarian surfaces solutions | U2 | user-outcome | Workflow has Reusable Solutions section |
| Mission OS uses solutions before planning | U3 | user-outcome | Mission preflight includes solution search and Library Decision states reuse decision |
| New pattern is reusable | U4 | scrutiny | `docs/solutions/knowledge-librarian-solution-surfacing.md` exists and is searchable |
