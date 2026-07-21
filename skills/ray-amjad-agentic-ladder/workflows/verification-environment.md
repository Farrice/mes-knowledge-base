---
description: Design the verification environment for a project — agent-authored provisioning list, artifact spec, compounding roadmap
---

# Verification Environment Designer — Fix the Environment, Not the Model

Ray's doctrine: "often the reason why your verification is not end to end is that you haven't set up the right environment." This workflow produces the provisioning plan that widens the class of auto-verifiable changes.

## Pre-Flight Gate

Load `genius.md` (patterns 2, 7, 8). Require: the project's user-facing surfaces and the change classes that currently can't be verified end-to-end. If unknown, run the agent-interview move first (Execution step 1) — that IS the workflow's opening.

## Skill Acquisition

- `genius.md` — Environment-First Verification, Verification Surface Rule
- `extractions/ray-amjad/extraction-report.md` — worked examples (LiveKit/voice, email channel, Instagram/browserbase, Anthropic's cloud-Windows computer-use rig)

## Execution

1. **Agent interview** (Ray's inversion): ask the project's own agent — "What would you need from me to verify this change end to end, and any more changes in this part of the project end to end?" The agent writes the first provisioning list.
2. **Map surface → instrument → artifact** for every change class: GUI → Playwright/browser MCP → recording; API → live request → response capture; voice → fake mic vs live + MP3; email/DM channels → test accounts able to converse both ways; desktop app → container/computer-use rig.
3. **Price the gaps**: per item — credentials/keys, CLIs to install, test accounts, sandboxes, spend caps (his move: token/credit limits on test calls), artifact delivery channel.
4. **Sequence by leverage**: provision first whatever unblocks the most frequent change class. Note compounding: environment investment appreciates as models improve.
5. **Wire the reminder loop**: add the lifecycle line — on environment-failure, pause and notify — so every miss becomes a provisioning ticket ("it will constantly keep reminding me… and over time our verification environment will be getting better").

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| SaaS web product | Playwright + seeded test accounts + staging data |
| Voice/realtime | Fake-mic strategy decision, API keys, credit caps, MP3 artifacts |
| Multi-channel (email/SMS/social) | Per-channel test identities; browser automation (browserbase-style) where no API |
| Desktop/native | Cloud container with computer use; recording pipeline out |

## Output Requirements

Provisioning plan: table (change class · surface · instrument · artifact · missing pieces · cap/guardrail) + build order with leverage rationale + the pause-and-notify lifecycle line.
Execution prompt: `references/prompts-v2/verification-environment.md` — honor its Output Contract.

## Quality Gate

Reject if: gaps blamed on model quality; any surface verified below itself; no spend/credit caps on paid test loops; no artifact channel named; provisioning list invented without the agent interview or stated project facts.
