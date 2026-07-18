---
description: "/forge prompt <concept> — Prompt Forge lane: bare concept → one born-v2 structure-pure execution prompt, corpus-grounded, wired into its owning skill's prompts-v2 menu."
---

# Prompt Forge — Bare Concept → Structure-Pure v2 Prompt

Dispatches `skills/forge-os/references/prompts-v2/prompt-forge.md` (the engine — read it first,
this file is the workflow contract wrapping it). Status per `SKILL.md`'s Five Lanes table:
**LIVE (Wave 1)**.

## Invocation

`/forge prompt <raw intent>` or the front door (`/forge <messy concept>`) classifying WANTS-axis
= prompt.

## Stages

1. **Translate** — Translation Card from the raw intent (anchor, deliverable, audience, felt
   standard verbatim).
2. **Ground** — `python3 execution/prompt_library.py search "<deliverable keywords>"` +
   `ls skills/ | grep -iE "<domain terms>"`; no corpus anywhere → run the Skill Forge lane's
   Grounding Sprint first, or narrow scope and declare `fidelity: low`.
3. **Forge** — the eight born-v2 sections per `directives/prompt-forging-spec.md`: Role &
   Activation, Input Required, Execution Protocol, Output Contract, Output Skeleton, Quality
   Gate, Creative Latitude, Deploy When, plus 2-3 Fixtures inside the file.
4. **Gate** — `python3 execution/renaissance_audit.py` (0 fail).
5. **Wire** — `python3 execution/prompt_library.py build` →
   `python3 execution/wire_prompt_pointers.py --write` → SLASH_COMMANDS.md row if a new command
   name is introduced.

## Output Schema

The deliverable is one v2 prompt file at `skills/<owning-skill>/references/prompts-v2/<name>.md`,
never a chat reply. It must carry, in order: born-v2 frontmatter (`name` / `source_prompt` /
`skill` / `standard: structure-pure-v2` / `forged` / `refactored`) → the eight sections listed
above → 2-3 Fixtures (`input values → expected output shape`) inside the same file, per
`prompt-forge.md`'s own Output Contract (item 2: "Golden fixtures (2–3) — inside the forged file
under `## Fixtures`"). A forge run that returns prose instead of this file, or omits any of the
eight sections, has not produced a Prompt Forge deliverable — it has produced a draft.

## Quality Gate

- Every claim in Role & Activation and Execution Protocol traces to [GROUNDING MATERIAL] — zero
  training-memory methodology, zero invented credentials or stats (prompt-forge.md's own gate).
- All eight spec sections present and non-stub; the prompt is scoped to exactly ONE deliverable
  class (a pipeline intent "X → Y" collapses to Y as primary, X as intermediate).
- `renaissance_audit.py` returns 0 fail before the prompt is wired.
- Fidelity is declared honestly (`fidelity: low` on a thin corpus, never silently upgraded).
- All four wiring gates ran: audit / `prompt_library.py build` / `wire_prompt_pointers.py` /
  SLASH_COMMANDS.md row-or-explicit-gap.
