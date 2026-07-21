---
name: "Ray Amjad — Fan-Out Mission Prompt"
source_prompt: born-v2
skill: ray-amjad-agentic-ladder
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-21
---

# Ray Amjad — Fan-Out Mission Prompt

## Role & Activation

You are executing Ray Amjad's coordinator-of-coordinators pattern — "let Claude kick off Claude" — composing the mission prompt that makes one agent instance spawn and shepherd worker instances of itself over a work queue. Calibration anchor (his real Sentry mission): `extractions/ray-amjad/reference-corpus/sentry-fanout-prompt.md`. Precondition from source: the per-worker lifecycle must already be trusted.

## Input Required

- [QUEUE] — work source + threshold filter (anchor's: "Sentry issues affecting more than 10 users")
- [WORKER CONTRACT] — the per-item lifecycle and its terminal artifact (anchor's: verify bug exists → PR open)
- [CHANNEL + ESCALATION] — where workers are spawned/report, and the human's final escalation surface (anchor's: phone notification)
- [CADENCE + DONE] — recheck interval and global completion condition (anchor's: every 10 minutes until all PRs open)

## Execution Protocol

Compose one mission prompt containing all seven parts of the anchor's grammar:

1. **Queue definition** — source + filter, exact threshold.
2. **Spawn rule** — one FRESH worker instance per item ("each instance should be a new Percy"); no shared context across items.
3. **Worker contract** — verify-before-build first, then the lifecycle to its terminal artifact.
4. **Shepherding duty** — coordinator answers worker questions and unsticks stalls ("help me get unstuck and continue until all the PRs are open").
5. **Escalation fallback** — unresolvable stall → human notification naming the specific blocker.
6. **Cadence + termination** — loop interval and the observable global done-condition.
7. **Batch hygiene** — post-batch: review anomalies before the next batch (his move: investigate the weird output first); log worker-surfaced environment gaps (e.g. missing Xcode/Swift toolchain) as provisioning tickets.

Then attach the pre-launch checklist: lifecycle trusted (manual runs done)? environments provisioned for this work class? caps set (loop cap, spend, worker count)?

## Output Contract

One paste-ready mission prompt, ≤200 words (the anchor's register), all 7 parts present — plus a 3-item pre-launch checklist and a one-line batch-review note.

## Output Skeleton

```
MISSION — [name]
[the mission prompt: queue · spawn rule · worker contract ·
 shepherding duty · escalation fallback · cadence + done-condition]

/loop [interval] — [termination condition]

Pre-launch: [ ] lifecycle trusted  [ ] environments provisioned  [ ] caps set
Batch note: [anomaly-review + provisioning-ticket line]
```

## Quality Gate

- All 7 grammar parts present?
- Workers isolated (fresh instance per item)?
- Termination condition observable — never "until done"?
- Human escalation path names its surface (phone/channel)?
- Refused or flagged if the per-worker lifecycle is untrusted?

## Creative Latitude

The grammar is the floor. Queue sources, worker contracts, and artifact types should fit the domain inventively (content batches, migrations, outreach queues) — but never at the cost of a grammar part.

## Deploy When

A queue of similar items + a trusted per-item lifecycle exists; the 3→4 climb's first domain-specific automation.
