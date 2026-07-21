---
description: Write a coordinator fan-out mission prompt — Claude kicks off Claude, with unstick protocol, loop cadence, and completion condition
---

# Fan-Out Mission — Coordinator of Coordinators

Builds the "let Claude kick off Claude" prompt: one coordinator instance spawning worker instances of itself over a work queue, shepherding them to a global completion condition. Calibration anchor: `extractions/ray-amjad/reference-corpus/sentry-fanout-prompt.md`.

## Pre-Flight Gate

Load `genius.md` (patterns 4, 6, 10) + the anchor. Require: work source + filter (e.g. "Sentry issues affecting >10 users"), per-worker task contract, delivery channel, human escalation path. **Trust check**: the per-worker lifecycle must already be trusted (run manually before fan-out) — if not, route to `task-lifecycle-forge` first.

## Skill Acquisition

- `extractions/ray-amjad/reference-corpus/sentry-fanout-prompt.md` — the seven-part grammar
- `genius.md` — Capped Repair Loops, Coordinator Not Worker

## Execution

Compose the mission with all seven parts of the anchor's grammar:

1. **Queue definition**: source + threshold filter ("issues affecting more than 10 users").
2. **Spawn rule**: one fresh worker instance per queue item ("each instance should be a new Percy") — never shared context across items.
3. **Worker contract**: verify-before-build ("first verify the bug exists"), then the full lifecycle to its terminal artifact ("all the way to opening up a PR").
4. **Shepherding duty**: coordinator answers worker questions and unsticks them ("if Percy gets stuck, help me get unstuck and continue").
5. **Escalation fallback**: unresolvable stalls → human notification with the specific blocker ("send me a notification to my phone: Percy is stuck on this, I can't help it").
6. **Loop cadence + termination**: recheck interval and global done-condition ("loop every 10 minutes until all PRs are open").
7. **Batch hygiene**: before the next batch, review anomalies from this one (his move: investigate the weird output before rerunning); log environment gaps workers surfaced (missing toolchains) as provisioning tickets.

## Content Type Adaptations

| Work class | Adaptation |
|---|---|
| Bug queue (easiest — start here) | Verify-repro as worker step 1; PR as terminal artifact |
| Feature requests | Vision-filter gate before spawn; HTML mock/artifact options before build (his Excalidraw example) |
| Content/asset batch | Terminal artifact = draft in channel; QA gate replaces code review |
| Migration/refactor | Worktree isolation mandatory; per-module workers; merge order in coordinator duty |

## Output Requirements

One paste-ready mission prompt (all 7 parts, ≤200 words like the anchor) + pre-launch checklist (lifecycle trusted? environments provisioned? caps set?) + batch-review note.
Execution prompt: `references/prompts-v2/fanout-mission.md` — honor its Output Contract.

## Quality Gate

Reject if: any of the 7 grammar parts missing; workers share context; no human-escalation path; termination condition vague ("until done"); fan-out proposed over an untrusted lifecycle.
