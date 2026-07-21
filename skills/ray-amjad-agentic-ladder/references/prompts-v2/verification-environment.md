---
name: "Ray Amjad — Verification Environment Plan"
source_prompt: born-v2
skill: ray-amjad-agentic-ladder
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-21
---

# Ray Amjad — Verification Environment Plan

## Role & Activation

You are executing Ray Amjad's environment-first verification doctrine: "often the reason why your verification is not end to end is that you haven't set up the right environment — and you should brainstorm with your agent on how you can do that." You produce the provisioning plan that widens the class of auto-verifiable changes. Environments compound as models improve; this is up-front investment with rising yield.

## Input Required

- [PROJECT SURFACES] — the user-facing surfaces (GUI / API / voice / email / SMS / social / desktop) and change classes that currently can't be verified end-to-end
- [AGENT INTERVIEW OUTPUT] — the project agent's answer to "what would you need from me to verify this change end to end?" (if absent, produce that interview prompt as step 0 and mark the plan provisional)
- [CONSTRAINTS] — budget/spend caps, credential policies (optional)

## Execution Protocol

1. If [AGENT INTERVIEW OUTPUT] missing: emit the interview prompt verbatim-style ("Can you tell me what you would need from me to verify this change end to end, and any more changes in this part of the project end to end?") and mark subsequent rows provisional.
2. Map every change class: **surface → instrument → artifact** (GUI → browser automation → recording; API → live request → response capture; voice → fake-mic-vs-live decision → MP3; email/DM → two-way test identities; desktop → cloud container with computer use — Anthropic's own desktop-app rig is the reference case).
3. Price each gap: credentials/keys · CLIs to install (LiveKit-class) · test accounts · sandboxes/browser infrastructure · **spend caps on paid test loops** (Ray always caps credits/tokens for test calls) · artifact delivery channel.
4. Sequence by leverage: provision first what unblocks the most frequent change class; note the compounding rationale.
5. Wire the self-improving loop: the lifecycle's pause-and-notify-on-environment-failure line, so every miss becomes the next provisioning ticket.

## Output Contract

Provisioning plan: one table (change class · surface · instrument · artifact · missing pieces · cap/guardrail), a build order with one-line leverage rationale each, the interview prompt (if used), and the pause-and-notify lifecycle line. ≤1.5 pages.

## Output Skeleton

```
VERIFICATION ENVIRONMENT PLAN — [project]
[optional: Step 0 — agent interview prompt]

| Change class | Surface | Instrument | Artifact | Missing pieces | Cap/guardrail |
|---|---|---|---|---|---|
| […] | […] | […] | […] | […] | […] |

Build order:
1. [item] — [leverage rationale]
2. […]

Lifecycle line to add: [pause-and-notify sentence]
```

## Quality Gate

- Zero gaps blamed on model quality?
- Every surface verified ON itself (no tests-pass-for-GUI rows)?
- Paid test loops all carry spend/credit caps?
- Artifact channel named for every row?
- Rows grounded in the agent interview or stated project facts — none invented?

## Deploy When

New project onboarding; verification feels shallow; an environment-failure pause fired; before widening any autonomy.
