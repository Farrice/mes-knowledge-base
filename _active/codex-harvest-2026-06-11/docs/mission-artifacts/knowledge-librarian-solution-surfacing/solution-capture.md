# Solution Capture: Knowledge Librarian Solution Surfacing

Created: 2026-05-08
Mission: knowledge-librarian-solution-surfacing

## Track

- Type: workflow / knowledge operations

## Symptoms Or Context

- `docs/solutions/` exists as the durable sink for solved-problem guidance.
- Future missions would not automatically consult it without an explicit librarian step.
- The user asked to expand the system so Knowledge Librarian surfaces reusable solution entries during future missions.

## What Did Not Work

- Merely having `docs/solutions/` is passive; it does not change mission behavior.
- Putting the burden on Farrice to remember solution docs would recreate the same underuse problem.

## Working Solution Or Durable Guidance

- Add `python3 execution/knowledge_compiler.py solutions "[focus]" --top 8`.
- Make `/knowledge-librarian` include a Reusable Solutions section.
- Make `/mission` run solution search during librarian preflight and name reuse decisions in the Library Decision.
- Capture this pattern as `docs/solutions/knowledge-librarian-solution-surfacing.md`.

## Why This Works

- It makes solution reuse part of mission preflight rather than optional memory.
- It keeps `docs/solutions/` small, focused, and actionable.
- It avoids bloating the main knowledge manifest while the solution library is still young.

## Prevention Or Reuse

- Every future system/code mission should check solution docs before drafting a new plan.
- If a solution applies, the mission should say apply, adapt, ignore with reason, or promote a new solution after completion.

## Generalization Decision

- Keep mission-local: yes, as implementation evidence.
- Promote to `docs/solutions/`: yes, see `docs/solutions/knowledge-librarian-solution-surfacing.md`.
