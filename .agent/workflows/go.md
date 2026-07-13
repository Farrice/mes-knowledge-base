---
description: The Maestro front door — compile any raw thought into a goal-aligned Mission Card, orchestrate it per doctrine, run it, deliver with steering
---

# /go - The Maestro Front Door (v2, 2026-07-13)

`/go "<messy thought>"` turns an underspecified thought into a routed, executed
deliverable in one pass — now compiled against Farrice's standing goals and the
orchestration doctrine (`directives/orchestration-doctrine.md`). `/go` never
returns a bare clarifying question when it can propose an answer instead.

## Stage 0 — MISSION COMPILE (silent)

1. DICE-score the raw thought per CLAUDE.md Step 1 (Deliverable, Audience,
   Context/constraints, End state, Specific language). 1 point each, 1-5 total.
2. Score >= 3: skip questions, write the MISSION CARD below, and proceed.
   Score <= 2: ONE question round, only the DICE dimensions actually missing.
3. **Goal spine**: read `.agent/cos/goals.json` — name the goal this mission
   serves in the card. No match = `ORPHAN ⚑` flag (one line, compass never
   cage, then execute fully). While a SPRINT is active in goals.json, surface it.
4. **Pattern**: pick the PRIMARY orchestration shape from the doctrine's
   Pattern Table — solo / solo+jam / fleet / proof-first / council / wargame /
   swarm / verify-fleet / wayfinder — with a one-line reason.
5. **Tier**: classify blast radius per doctrine (T1 auto-run · T2 wait ·
   T3 always wait). Standing grants elevate T2→T1 for their scope only.

```
MISSION CARD
Intent: <sharpened one-liner>            Serves: <goal-id | ORPHAN ⚑>
Pattern: <doctrine row> — <one-line reason>
Loads: <experts/skills + the v2 prompts whose contracts govern output>
Gates: <audit / prose / verify / jam / voice — whichever will fire>
Tier: <T1 auto | T2 waiting | T3 waiting>   Cost: <$0 | flagged>
```

T1: card is shown as the mission starts. T2/T3: card waits for the nod.

## Stage 1 — ROUTE

Hand the mission to exactly one conductor. Running two conductors requires two
genuinely separate deliverables — don't split one ask into a mini-mission.

| Mission shape | Conductor |
|---|---|
| Single content/copy piece | `/create` (+ v2 prompt contract + voice layer if Farrice-named) |
| Multi-deliverable mission | `/supercomputer` |
| Campaign (multi-asset, multi-platform) | `/jw-engine` |
| Fleet-shaped work (10+ units / 3+ workstreams) | Workflow engine per doctrine (scout → agents → gate) |
| Decision with real tradeoffs | `/convene` |
| Plan-for-cheaper-executor | `/wargame-run` |
| Full-auto, gates explicitly suppressed | `/autopilot` |
| System/harness repair or audit | `/system-audit` |
| Research question | `execution/research.py` / `/swarm` |
| Voice overlay on expert-pure output | `/voice-over` |

If two rows plausibly match, name the fork in one line and pick the stronger
match. Never default to `/autopilot` as a catch-all.

## Stage 2 — RUN

Hand the RUN PACKET to the chosen conductor as its intent input, then let the
conductor run its own sequence: Chain Steps 3-6 for content conductors,
`/autopilot`'s own Intent Lock -> Trace -> Execution Decision -> Verify -> Run
Receipt for gate-suppressed work. `/go` stages the engine; it does not
re-implement what the conductor already owns.

## Stage 2.5 — LOG (deterministic, both ends)

At compile AND at close, append one line to `.agent/missions.jsonl`:
```json
{"ts":"<iso>","mission":"<intent one-liner>","serves":"<goal-id|orphan>","pattern":"<row>","tier":"T1|T2|T3","status":"compiled|running|done|stopped","outcome":"<one line at close>"}
```
The pulse dashboard (`/pulse-board`) and COS read from this log — an unlogged
mission is invisible to the operator console.

## Stage 3 — DELIVER + Next-Prompts

Deliver the output, then close with the 3 Next-Prompts steering block below.
As of 2026-07-08 this spec IS global: CLAUDE.md Chain Step 7 (Steering Loop,
`directives/steering-loop.md`) enforces a per-exchange Next Moves block via
`execution/hooks/steering_loop_hook.py` on every model. This stage remains the
conductor-level version of the same contract.

### Next-Prompts Spec (canonical, always in this order)

1. **Deepen** — go further on the thread just delivered (more depth, rigor, or
   proof on the same deliverable).
2. **Adjacent** — the opportunity this delivery unlocked that wasn't the
   original ask (new angle, new asset, new audience).
3. **Next milestone** — the next concrete step toward the active goal. Read
   `.agent/cos/goals.json` and name the specific active goal it advances (e.g.
   the $5K/mo Incumbency Rule threshold) — never a generic "next step."

Skip only when Farrice explicitly asks for a terse answer.

## Reuse, Not Duplication

- `execution/workflow_router.py search "<intent>"` and
  `execution/control_intent.py` — reusable, tool-agnostic route-scoring logic.
  Safe to call directly for a second opinion on the Stage 1 table.
- `execution/raw_intent_run_packet.py` (the raw-intent-bridge skill's engine)
  has real compile logic (clarity score, route candidates via
  `workflow_router.search_workflows`) but wraps it in Codex-only framing
  (`~/.codex`, Codex Antigravity mutation, Codex-subagent authorization
  language, a SUPPORT_GATES table keyed to Codex control-plane workflows).
  Don't invoke it as the Stage 0 packet generator here — read its scoring
  functions for reference, don't ship its output format.

`/go` is the front door; conductors stay the owners of their own execution.
