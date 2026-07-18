---
description: "/forge workflow <concept> — Workflow Forge lane: repeated manual loop or bare orchestration concept → a real `.agent/workflows/<name>.md` command with gates and verification inline."
---

# Workflow Forge — Manual Loop → `.agent/workflows/<name>.md`

Dispatches `skills/forge-os/references/prompts-v2/workflow-forge.md` (the engine). Status:
**LIVE (Wave 2)**.

## Invocation

`/forge workflow <raw intent>` — fires when the intent is orchestration (sequencing existing
assets, gates, and verification), not a request for new domain expertise.

## Stages

1. **Lane confirmation** — is this actually orchestration, or does it need new expert grounding
   (→ Skill Forge instead)? Never build a workflow to paper over a missing skill.
2. **House-style exemplar reads** — open 2-3 existing `.agent/workflows/*.md` files whose shape
   the new command should match (frontmatter description, Invocation, staged sections, Boundaries,
   Verification, Fixtures).
3. **Process contract from real loop evidence** — the protocol traces to [LOOP EVIDENCE] (an
   actual repeated manual sequence the operator ran), never an imagined ideal process.
4. **Write** `.agent/workflows/<name>.md` with gates embedded inline per stage and 2 fixtures
   (invocation → expected artifacts/receipts) inside the file.
5. **Register** — SLASH_COMMANDS.md row + collision check against existing command names.

## Output Schema

One workflow file at `.agent/workflows/<name>.md`: frontmatter `description` (one line,
verb-first) → title → a when-to-use/when-NOT-to-use paragraph → `## Invocation` (all valid
forms) → `## Stage 1..N` (ordered, each naming its own gate or stating explicitly it has none,
with failure behavior defined — no silent-continue paths) → `## Boundaries` (a never-do list) →
`## Verification` (deterministic proof-of-honest-run checks) → `## Fixtures` (2: invocation →
expected artifacts/receipts), per `workflow-forge.md`'s own Output Skeleton. This is a command
file other operators and agents will execute cold — ambiguity here is the exact failure class the
2026-07-14 cold-start-probe solution card exists to catch (`docs/solutions/2026-07-14-cold-start-
probe-anneals-new-engine-prompts.md`).

## Quality Gate

- Lane confirmed as orchestration (not disguised new-expertise work) before drafting.
- Every stage names its gate or explicitly states it has none — no silent-continue paths.
- The protocol traces to real [LOOP EVIDENCE] / [OWNING ASSETS], not an imagined process.
- Collision check run against SLASH_COMMANDS.md BEFORE writing the file, not after.
- Both fixtures present inside the file, each specifying a checkable output shape.
- A fresh-context cold-start pass ran on the finished command and its friction points were fixed
  same-session (per the annealing pattern this skill's own build already proved on
  `prompt-forge.md`).
