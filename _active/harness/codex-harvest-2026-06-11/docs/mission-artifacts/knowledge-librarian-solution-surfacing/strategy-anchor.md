# Strategy Anchor: Knowledge Librarian Solution Surfacing

Created: 2026-05-08
Mission: knowledge-librarian-solution-surfacing

## Target Problem

`docs/solutions/` can hold reusable solved-problem guidance, but future missions will not benefit unless Knowledge Librarian checks it before mission planning.

## Guiding Bet

Make reusable solution surfacing a deterministic Knowledge Librarian action, backed by `execution/knowledge_compiler.py solutions`, and require Mission OS to cite applicable solution docs in the Library Decision.

## Audience

- Farrice, when starting future missions.
- Knowledge Librarian, before it recommends new work.
- Mission OS, before it drafts charters and validation contracts.
- Future Codex agents, when they need prior solved-problem guidance.

## Key Metrics Or Proof Signals

- `python3 execution/knowledge_compiler.py solutions "[focus]" --top 8` returns relevant solution docs.
- `/knowledge-librarian` workflow includes a Reusable Solutions section.
- `/mission` preflight includes solution search before planning.
- A reusable solution doc exists for this pattern.

## Active Tracks

- `execution/knowledge_compiler.py` solution inventory/search.
- `.agent/workflows/knowledge-librarian.md` solution surfacing.
- `.agent/workflows/mission.md` Library Decision integration.
- `docs/solutions/` reusable pattern docs.

## Source Strategy

- Root `STRATEGY.md` checked: not applicable.
- Mission-local strategy decision: solved-problem docs must be surfaced before new mission work is invented.
