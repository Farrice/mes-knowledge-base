---
description: Fire as an OPTIONAL pre-flight offer inside a /swarm or /supercomputer mission — never automatically, never as a required step — when a workstream is high-stakes, spans multiple sessions, or will hand off to a cheaper/degraded executor than the one planning it. Per the binding "no forced wiring, hubs compose freely": this workflow surfaces the option, it does not insert itself.
---

# /wargame-mission — Wargaming As An Offer, Not A Gate

A conductor, not a procedure. It composes Tier 1 (`/wargame-order`, `/wargame-run`, `/wargame-grade`) against exactly one risky workstream inside a larger mission — it does not re-explain their mechanics, and it does not run unless Farrice says yes.

## The Binding This Workflow Exists Under

Farrice, 2026-07-07: "No Forced Wiring — Hubs Compose Freely" — cross-hub handoffs are options, never pipeline steps. This workflow is the wargame skill's one and only touchpoint with `/swarm` and `/supercomputer`, and it exists specifically so those two hubs never get a hardcoded "always wargame first" step baked into their own workflow prose. If either hub's instructions are ever edited to say something like "run wargame-mission before every workstream," that edit is the anti-pattern, not a strengthening — revert it and let this workflow keep doing the asking.

## Pre-Flight Gate

- **Stakes check**: does the workstream actually meet the bar — multi-session (spans more than one sitting), handed off to a cheaper/different-tier executor than the one planning it, or client-facing with real cost of error? Heuristic 1 (cheaper executor than planner) and Heuristic 7 (consequence horizon) are the two triggers; if neither fires, this workflow has nothing to do here.
- **Scope check**: has `/swarm` or `/supercomputer`'s own decomposition already identified which workstream(s) carry the risk? Wargame only the riskiest 1–2, never the whole mission — full-portfolio treatment belongs to `/wargame-batch`, not this workflow.
- **Forced-wiring check**: is this being invoked because another workflow's prose made it mandatory? That is the exact anti-pattern this workflow exists to prevent — re-read `feedback_no-forced-wiring-hubs-compose-freely.md`'s binding before proceeding. This step is surfaced to Farrice as a choice, every time.

## Skill Acquisition

- `genius.md` — Decision Heuristic 1 (wargame when the executor is cheaper than the planner), Decision Heuristic 7 (human sets the consequence horizon)
- Tier 1 workflows (`wargame-order`, `wargame-run`, `wargame-grade`) — pointed to for mechanics, never duplicated here

## What "Compose, Never Force" Means Here

This workflow has no independent trigger of its own — it only ever fires from inside `/swarm` or `/supercomputer`'s own decomposition step, as a question the parent mission asks itself, never as a step the parent mission is required to include. The test: could this mission ship correctly with this workflow deleted entirely? If the honest answer is yes (most missions), that's the system working as designed, not a gap. Contrast with `/wargame-batch`, which DOES have its own trigger (a laundry list handed over directly) — that's a Tier 2 procedure with its own front door; this is a Tier 3 conductor with none.

## Execution

1. Assess stakes against the two Pre-Flight checks for each workstream the parent mission has already decomposed. Name explicitly which workstream(s), if any, qualify.
2. If none qualify, say so in one line and continue the parent mission unmodified — this is the expected outcome most of the time, not a failure of the workflow.
3. If a workstream qualifies, SURFACE the option to Farrice by name: "Workstream [X] touches [the specific stakes — e.g. hands off to Haiku, spans three sessions]; want the route wargamed before an agent executes it?" Do not auto-run past this point.
4. On approval, invoke `/wargame-order` → `/wargame-run` → `/wargame-grade` scoped ONLY to that workstream's brief, at the consequence horizon Farrice names (Heuristic 7 — the human sets the depth, not this workflow).
5. Once DONE, attach the wargame file to the mission folder — `.agent/missions/<parent-mission>/wargames/<workstream-slug>.md` — so the workstream's executing agent receives the route as its brief, replacing whatever raw task description it would otherwise improvise from.
6. Log the decision (wargamed / skipped, and why) in the parent mission's own ledger or handoff doc, so whoever resumes the mission later sees the call that was made and doesn't re-litigate it.

## Why This Sits At Tier 3, Not Tier 1

Tier 1 (`wargame-order`/`wargame-run`/`wargame-grade`) is the mechanism. This workflow is a JUDGMENT CALL about when to invoke that mechanism inside someone else's mission — the same distinction the craft standard draws between conductors and procedures (§6): a conductor composes, points, and stays thin; duplicating Tier 1's move/expect/fail/trigger mechanics here would create two sources of truth for how a wargame actually gets built. If this file starts explaining HOW to write a move, it has drifted out of its lane.

## Content Type Adaptations

| Mission type | Typical qualifying workstream | What gets wargamed |
|---|---|---|
| **Code build** | The workstream handed to a cheaper coding model mid-mission | Build/test/verify route, not the whole codebase |
| **Copy/content** | A multi-session content series with a voice-risk workstream | The riskiest single asset's production route |
| **Research/analysis** | A workstream whose findings feed a client-facing deliverable | The verification/citation route, not the whole research pass |
| **Ops/automation** | A workstream that touches production state or irreversible actions | The abort-condition and guardrail set for that specific phase |

## Worked Example

A `/supercomputer` mission with five workstreams, one of which is "migrate the client's Notion DB schema and re-point 40 downstream references." That workstream is irreversible if it breaks and will be handed to a cheaper model to actually execute — it clears both Pre-Flight checks. The other four (drafting copy, generating images, scheduling posts, updating a tracker) don't touch irreversible state and don't qualify. Surface the DB-migration workstream alone; the other four proceed exactly as `/supercomputer` already planned them, untouched by this workflow.

## Declining The Offer, Repeatedly

If Farrice declines the offer on two consecutive missions of the same general shape (e.g. two straight database-migration workstreams), stop re-offering for that shape going forward and log it as a standing preference in the parent mission's context file — re-asking the same question after two clear declines is noise, not diligence. This doesn't retire the workflow; it narrows when it re-surfaces, consistent with COS being a compass, never a cage.

## Output Requirements

Exactly one of: (a) a one-line "no wargame needed" entry in the parent mission's log, or (b) a DONE-graded wargame file at `.agent/missions/<parent-mission>/wargames/<workstream-slug>.md` plus the one-line decision-log entry recording Farrice's approval.

## Quality Gate

- [ ] Never inserted as a mandatory step — the forced-wiring check from Pre-Flight is re-verified at delivery, not just at the start
- [ ] Scoped to the riskiest workstream(s) only — a wargame covering the entire parent mission here is scope creep into `/wargame-batch`'s territory
- [ ] Farrice's approval is recorded before `/wargame-order` fires — no wargame gets built on an assumed yes
- [ ] The "no wargame needed" outcome is logged with the same visibility as a DONE wargame — a skip that isn't recorded looks identical to a skip that was never considered
- [ ] The attached wargame actually replaces the workstream's raw task description for its executing agent — attaching it without wiring it into the handoff defeats the point
