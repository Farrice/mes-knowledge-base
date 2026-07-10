---
description: Anti-bottleneck front door — compile a messy thought into a run packet, route it to a conductor, run it, deliver with steering
---

# /go - Anti-Bottleneck Front Door

`/go "<messy thought>"` turns an underspecified thought into a routed, executed
deliverable in one pass. It exists because Farrice is the bottleneck when the
system asks HIM to sharpen intent instead of writing the assumptions and moving.
`/go` never returns a bare clarifying question when it can propose an answer
instead.

## Stage 0 — INTENT COMPILE (silent)

1. DICE-score the raw thought per CLAUDE.md Step 1 (Deliverable, Audience,
   Context/constraints, End state, Specific language). 1 point each, 1-5 total.
2. Score >= 3: skip questions, write the RUN PACKET below, and proceed.
3. Score <= 2: ONE question round, asking only about the DICE dimensions
   actually missing — never re-ask something inferable from context or prior
   session state.
4. Write the RUN PACKET, then proceed (don't wait for sign-off unless the next
   step is destructive/paid/external per the Chain's normal rules):

```
RUN PACKET
Assuming: deliverable=<X>, audience=<Y>, done=<Z> — correct me or I proceed.
Outcomes (>=2): <outcome A> / <outcome B>
Constraints: <voice, budget, deadline, format>
Taste refs: <named skill/expert/rubric anchor if one applies>
Budget note: <$0 default | cost-gated API flagged>
```

## Stage 1 — ROUTE

Match the packet's deliverable shape to exactly one conductor. Running two
conductors requires the packet to name two genuinely separate deliverables —
don't split one ask into a mini-mission.

| Packet shape | Conductor |
|---|---|
| Single content/copy piece | `/create` |
| Multi-deliverable mission | `/supercomputer` |
| Campaign (multi-asset, multi-platform) | `/jw-engine` |
| Full-auto, gates explicitly suppressed | `/autopilot` |
| System/harness repair or audit | `/system-audit` |
| Research question | `execution/research.py` |

If two rows plausibly match, name the fork in one line and pick the stronger
match. Never default to `/autopilot` as a catch-all — that habit is exactly
what made routing feel arbitrary before.

## Stage 2 — RUN

Hand the RUN PACKET to the chosen conductor as its intent input, then let the
conductor run its own sequence: Chain Steps 3-6 for content conductors,
`/autopilot`'s own Intent Lock -> Trace -> Execution Decision -> Verify -> Run
Receipt for gate-suppressed work. `/go` stages the engine; it does not
re-implement what the conductor already owns.

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
