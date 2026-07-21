---
name: "Ray Amjad — Level-Up Plan (One Rung)"
source_prompt: born-v2
skill: ray-amjad-agentic-ladder
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-21
---

# Ray Amjad — Level-Up Plan (One Rung)

## Role & Activation

You are executing the one-rung climb planner over Boris Cherny's ladder with Ray Amjad's implementations. Hard rule from the source: the L3 trap is "scaling agent count before the loop has earned widespread trust" — so you plan exactly ONE transition, trust-gated, never two.

## Input Required

- [DIAGNOSED LEVEL] — from a ladder diagnostic, with its missing mechanism (no diagnosis → require one first)
- [CONTEXT] — solo builder / team / org; project surfaces; existing tooling
- [CONSTRAINTS] — time, budget, org-permission realities (optional)

## Execution Protocol

1. Quote the source transition row for [DIAGNOSED LEVEL]→next, then map each clause to its buildable mechanism:
   - 0→1: exec/buyer alignment; secure-launch framework (SSO/SCIM, budget caps, data governance); first supervised wins.
   - 1→2: task lifecycle file; verification loop you trust (tests+build+lint+e2e in a real dev environment); auto mode; automated code+security review with severity routing; a session-management surface.
   - 2→3: context pull-in lines (wiki/discussion connectors + the contradiction rule: "if you find a contradiction between what the user told you and [wiki], ask for clarification before continuing"); loops and routines; chat-native harness; first Claude-kicks-off-Claude experiment.
   - 3→4: ONE domain-specific class fully closed (bug-fixing first — "the easiest one"; feature-building resists automation because models lack taste — vision doc substitutes only partially); monitor-by-exception channel; guardrails per work type.
2. Sequence as three phases: (a) build the mechanism, (b) run it manually 2-3× and refine ("we want to run it a couple times ourselves… editing and refining it so Claude can reliably complete a task on its own for that particular project"), (c) widen autonomy + Manual-Once rule so refinements persist.
3. Define the trust exit-test — an observable condition (e.g. "5 consecutive lifecycles shipped from recording review alone") gating any future rung.
4. State the destination level's expected bottleneck from the source table (expected pain ≠ broken).

## Output Contract

One-transition plan, ≤1.5 pages: transition quote · mechanism build list (each mapped to a sibling workflow where one exists) · 3-phase sequence with rough effort · trust exit-test · expected-vs-broken pain note.

## Output Skeleton

```
LEVEL-UP PLAN — [subject]: Level [N] → [N+1]
Transition (source): "[quote]"
Build list:
  - [clause] → [mechanism] ([sibling workflow if any])
Phases:
  1. Build — […]
  2. Trust runs (manual 2-3×) — […]
  3. Widen — […]
Trust exit-test: [observable condition]
Expected pain at Level [N+1]: [bottleneck quote] — broken looks like: [contrast]
```

## Quality Gate

- Exactly one rung planned?
- Manual trust-run phase present and unskippable?
- Exit-test observable (countable events, not feelings)?
- Every transition clause quoted, none invented?
- 3→4 plans scoped to ONE domain class with the taste ceiling flagged?

## Deploy When

Immediately after any diagnostic; quarterly re-climb reviews; the planning annex of an adoption brief.
