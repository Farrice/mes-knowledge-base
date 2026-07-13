---
description: Chart a decision map for a foggy multi-session effort — offer launches, campaigns, client engagements, learning missions — then work its frontier one ticket at a time until the way is clear
tier: system
---

# /wayfinder-work — Decision Maps for Operator Work

The work-domain layer over the imported `/wayfinder` skill (Matt Pocock v1.1, `~/.claude/skills/wayfinder/`). **Invoke the `wayfinder` skill first and follow it** — map anatomy, fog of war, out-of-scope discipline, ticket claiming, and the "produce decisions, not deliverables" rule all live there and are not restated here. Everything below is the delta for Farrice's non-code work; where the two conflict, this file wins.

## When

- A loose idea has arrived, too big for one session, and the way to the destination isn't visible: offer launches, campaign builds, client engagements, brand OS builds, pivots, learning missions (`/operator-school` hangs lessons off a map for week-scale domains).
- NOT for: single-session deliverables (run the Chain), execution of an already-clear plan (`/supercomputer` / fleet), or repo code work (use `/wayfinder` directly with `.scratch/`).

## Tracker — local markdown in the project folder (Farrice's standing default, 2026-07-10)

- **Map**: `_active/<project>/wayfinder/MAP.md` — body exactly per the wayfinder skill (Destination / Notes / Decisions so far / Not yet specified / Out of scope).
- **Tickets**: `_active/<project>/wayfinder/tickets/NNNN-<slug>.md`, numbered from 0001. Frontmatter:

  ```yaml
  status: open | closed
  type: research | prototype | grilling | task
  blocked_by: [0001, 0003]   # ticket numbers; empty = unblocked
  claimed_by:                # session pin name; empty = unclaimed
  ```

- **Frontier**: open tickets whose `blocked_by` are all closed and `claimed_by` is empty. Open every session by listing the frontier by ticket *name*.
- **Resolution**: append the answer under `## Resolution` in the ticket, set `status: closed`, add the one-line gist + link to MAP.md Decisions-so-far.

## Ticket types → harness machinery

| Type | Mode | Runs on |
|---|---|---|
| research | AFK | deep-research agent, `execution/research.py`, Recall grounding — findings saved as a linked asset in the project folder, Receipt-carrying |
| prototype | HITL | a cheap concrete artifact to react to: `/jam` two-takes, `/prototype`, a sample post, a mocked offer page |
| grilling | HITL | `/grilling` with Farrice — *facts* get dug up first (memory facade, project files, receipts); *decisions* go to Farrice one at a time, with a recommended answer each |
| task | HITL/AFK | the unblock-a-decision work: account setup, permission nods, data pulls, payment links |

Orchestration binding (`directives/orchestration-primitive.md`): Fable holds the map and every HITL ticket; AFK tickets dispatch to subagents and may run the frontier in parallel. One HITL ticket per session, per the wayfinder skill.

## Chain compliance

The map and its tickets are system artifacts — no finalize. Any deliverable produced *en route* (a post, a brief, a page) runs the full Chain, including Step 6.

## Done

Nothing left to decide before someone goes and does the thing → hand off: compress the Decisions-so-far into the destination artifact (brief, spec, offer doc) and route execution to the owning OS. The map stays in the project folder as the decision record.
