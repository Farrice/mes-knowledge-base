# Repeatability Spine Contract

## Purpose

Use this primitive when a good output, route, or implementation worked once but
cannot be reliably reproduced. The goal is to preserve the conditions that made
the good run work, diagnose why the later run failed, and turn the failure into
a route, revision rule, or regression guard.

This is the spine for three recurring failure classes:

- creative revision degradation: a rewrite becomes flatter, generic, less
  human, or loses the strongest proof/voice/tension
- wrong workflow or routing: the system chooses a literal keyword route or a
  generic workflow instead of the correct operating lane
- code or workflow regression: a patch introduces a new failure, breaks a
  verifier, or changes behavior outside the intended surface

## When To Use

- The user says the system "cannot repeat the magic" or a revision got worse.
- A strong draft exists and the next revision must preserve its best moves.
- A route picked the wrong workflow and needs a golden query.
- A patch fixed one issue but caused a regression elsewhere.
- A source-to-skill, revenue, creative, or system run needs a replayable prompt
  instead of another one-off success.

## Required Contract Fields

Every repeatability run must define:

| Field | Requirement |
|---|---|
| Good example | Path, snippet, or trace for the run that worked |
| Failed example | Path, snippet, route output, verifier failure, or user quote for the run that failed |
| Failure class | creative revision degradation, wrong workflow/routing, code/workflow regression |
| Original route | Command/workflow/agent stack that produced the good output, if known |
| Loaded context | Files, source packages, memory notes, expert lenses, or gates used |
| Expert stack | Experts, workflows, or gates that materially improved the good run |
| Preservation lock | What must survive the next revision or patch |
| Revision intent | What should change, and what should not change |
| Changed surface | Draft, workflow, router, verifier, command bridge, artifact, or script |
| Validation | Gate, route probe, verifier, guard, or review check |
| Regression guard | Exact phrase, fixture, script check, or verifier case to prevent recurrence |
| Result surface | How the user sees the recovery output |
| Reuse hook | Where the replay prompt, rule, or fixture is reused later |

## Preservation Lock

Before revising, create this lock:

```markdown
## Preservation Lock
- **Keep**: [strongest voice/proof/tension/route behavior/code behavior]
- **Change**: [specific requested change]
- **Do not disturb**: [lines, mechanisms, constraints, gates, or tests]
- **Risk**: [most likely degradation]
- **Gate**: [copy gate, verifier, route probe, test, or review]
```

If the lock is missing, do not treat the revision as controlled.

## Repeatability Handoff

Use this compact handoff between repair steps:

```markdown
## Repeatability Handoff: [Step] -> [Next Step]
- **Good example**: [path or route output]
- **Failed example**: [path, quote, route output, or test failure]
- **Failure class**: [creative / routing / regression]
- **Preservation lock**: [summary]
- **Repair route**: [workflow/gate/script]
- **Validation**: [pass/fail/check command]
- **Replay prompt**: [paste-ready starter]
```

## Seed Evidence

The initial seed package lives at
`docs/mission-artifacts/repeatability-spine/seed-ai-misfire-examples.md`.
It records:

- the AI Misfire V3 voice-proof post set as a good example
- the generic/needy urgent-cash audit route as a failed example
- `Get Audit Customers Fast` as pending external conversation evidence until
  it is locally accessible

## Quality Gate

Reject a repeatability run if it:

- revises without a Preservation Lock
- treats "make it better" as enough direction
- loses the strongest part of the good example
- fails to classify the failure class
- fixes routing without adding an exact phrase regression guard
- claims inaccessible conversation evidence was inspected
- changes global `~/.codex` behavior before workspace proof and user approval

## Last Updated

2026-05-10
