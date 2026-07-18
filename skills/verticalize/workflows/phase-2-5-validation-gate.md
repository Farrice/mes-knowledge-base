# Phase 2.5 — GATE: User Validation (Non-Skippable)

**Duration**: synchronous — this phase does not advance without the user. Per SKILL.md: "Why Phase 2.5 is non-skippable" cites `feedback_auto-evolution-cant-substitute-for-ground-truth.md` (2026-05-03 lesson) directly.

## Required inputs

The completed Phase 1 ICP master (`00-foundation/02-icp-master.md`) and Phase 2 voice document (`00-foundation/03-voice-document.md`), both scored and anchored.

## Steps

1. Surface the gate block to the user verbatim (see `.agent/workflows/verticalize.md` Phase 2.5 for the exact halt-question script) — three questions: does the ICP recognize the audience at the identity/resistance level (not demographic accuracy); does the voice doc produce a "yes" on the voice test for lines the owner would actually say; are there cultural or lived-experience claims that need validation by someone with that experience before ground-truth generation.
2. **Do not auto-advance.** Wait for an explicit reply: `continue`, `revise icp`, `revise voice`, or `halt`.
3. If `revise icp` or `revise voice`: re-run the corresponding phase from `workflows/phase-0-2-foundation-capture.md` before re-presenting the gate.
4. `--skip-2.5` is valid ONLY when the user is bootstrapping a domain they are already deeply expert in and confirms ICP/voice from memory — and only when passed as the literal flag, never inferred from conversational urgency (per `directives/workflow-gate-convention.md`'s skip-syntax rule).

## Output Schema

The gate itself produces no new file — its output is a decision, logged as the transition condition for Phase 3:

- **Explicit user verdict** — one of `continue` / `revise icp` / `revise voice` / `halt` / `--skip-2.5` (with justification for the skip, since skip is the exception, not the default).
- **If cultural/lived-experience risk was flagged (question 3)** — a named validator (who has the lived experience) and their explicit sign-off, recorded in `_working/phase-2.5-validation.md`, before Phase 3 can register the domain.

## Quality Gate

Before advancing to Phase 3:
- [ ] The three-question gate block was actually surfaced to the user — not summarized or assumed
- [ ] The reply was an explicit signal, not inferred agreement from a fast-moving conversation
- [ ] If question 3 (cultural/lived-experience validation) flagged a risk, it has a named validator's sign-off — not a self-assessment
- [ ] If `--skip-2.5` was used, the literal flag was passed by the user, not inferred, and the "deeply expert in this domain" condition is true and stated

Per `directives/workflow-gate-convention.md`'s anti-pattern list, answering this gate with "looks good, proceed" and no structured follow-up is treated as equivalent to skipping it — the 2026-04-11 naming-sprint failure ("Lake Effect," "Thaw" — both scored 8.6+/10 internally, rated 2/10 by someone with actual lived Chicago experience) is the standing proof that confidence without this specific check produces confidently wrong output.
