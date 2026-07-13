---
name: "Mark Kashef — Executor-Tailored Wargame"
source_prompt: born-v2
skill: mark-kashef-wargame-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are closing the last slack in a DONE wargame: "executors differ, and a route in the recipient's dialect fails less." A wargame graded against a generic mid-tier model still assumes generic tool names, generic context-window behavior, and generic failure patterns. This pass rewrites the route in a specifically named executor's actual dialect — tool-calling conventions, context/compaction behavior, documented failure patterns — and re-proves the eight-point standard against the rewritten version, because tailoring can silently break the very points that were passing before.

## Input Required

- `[GRADED WARGAME]` — the full contents of the DONE `wargames/NN-<name>.md`
- `[NAMED EXECUTOR]` — the specific model + harness this route will actually run on (e.g. "Sonnet 5 in Claude Code," "GPT-5.1 via the Assistants API") — not a placeholder like "a cheaper model"
- `[EXECUTOR DOCUMENTATION SOURCE]` — the model card, harness tool-use docs, or system card to tailor against; if none exists, this workflow does not apply

## Execution Protocol

**Pre-Flight:** confirm the wargame is already DONE against all 8 points before tailoring starts — tailoring a still-broken draft wastes the pass on a route that's going to change anyway. Confirm the executor is named specifically enough to have documented behavior, not a generic placeholder. Confirm real documentation exists to tailor against — a guess dressed as tailoring is worse than the honest generic version, because it reads as more authoritative than it is.

**When NOT to tailor:** the named executor is close enough in tier/dialect to the generic "cheaper executor" the wargame was already written for (e.g. Sonnet-to-Sonnet across sessions); the mission's moves are already tool-agnostic (pure judgment/copy work with no filesystem/repo interaction — dialect differences live in tool-calling conventions, which don't apply); or there's no real documentation to tailor against.

**Steps:**
1. Identify the executor precisely — model name, version, harness. Write it at the top of the tailored file so anyone reading it later knows exactly what dialect it's written in.
2. Dispatch a behavioral-notes pass against the documentation source, requesting BEHAVIORAL FINDINGS ONLY: documented tool-calling conventions (what it calls its tools, how it prefers to batch calls); context-window size and compaction behavior (summarize, truncate, or fail past a limit); known failure patterns (documented weaknesses, common hallucination triggers, formatting quirks); how it handles ambiguous or underspecified instructions.

   **WATCH OUT (verbatim, generalized beyond any one platform):** never ask the model to explain its thinking or reproduce its reasoning in the output — on reasoning-model harnesses this can trigger a reasoning-extraction safeguard and silently reroute the session mid-run. Ask for artifacts, findings, quotes, and rewrites, never for the thinking itself. Treat this as universal, not platform-specific.
3. Rewrite the Moves in the executor's dialect: swap generic tool references for the executor's actual tool names ("search the repo" → its native search tool; "run a long job" → its actual background-execution mechanism, or a synchronous-wait fallback if it lacks one). Adjust recon steps for the executor's real context-window/compaction behavior — chunk large reads into its actual working-set limits. Rewrite any move that assumes a capability the named executor doesn't have.
4. Re-grade against all 8 points, on the REWRITTEN version, not the original — tailoring can silently break points 1–3 (an executor-specific tool name might not produce the identical observable the original move predicted). A wargame DONE pre-tailoring is not automatically DONE post-tailoring.
5. Log the delta: what changed (tool names, context handling, failure patterns newly addressed) versus what stayed identical (move order, RECON NEEDED structure, abort conditions). This delta log is the proof the pass did real work rather than a cosmetic relabel.

**What separates a real tailoring pass from a cosmetic one:** the crown exemplar's Move 9 predicts a failure caused by the executor's OWN pattern-matching — an About-page headshot SVG incorrectly inheriting an ARIA attribute from an earlier move's icon pattern. A tailoring pass that only renames tools ("use Grep instead of grep") is cosmetic. A tailoring pass that predicts a named executor's specific tendency to over-generalize a pattern it just used, and writes the counter-move for it, has actually done the job.

**Dialect emphasis by content type:**
- Code build: tool names, test-runner invocation, file-write conventions typically need tailoring; move order, abort conditions, design-token freezes usually stay fixed.
- Copy-content: draft-and-revise loop shape (single-pass vs. iterative editor tools) needs tailoring; voice rules, CTA, evidence rules stay fixed.
- Research-analysis: search-tool names and the citation format the executor natively produces need tailoring; RECON NEEDED settling checks and verification pass criteria stay fixed.
- Ops-automation: subagent-dispatch conventions and background-process handling need tailoring; phase sequencing and per-phase acceptance checks stay fixed.

## Output Contract

Tailored wargame at `.agent/missions/<name>/wargames/<NN>-<slug>.<executor-slug>.md` (executor named in both the filename and the file's header), plus a delta-log entry appended to `LEDGER.md` naming what changed and confirming the re-grade result.

## Output Skeleton

```
# Wargame — [mission] — NN-[slug] — tailored for [NAMED EXECUTOR]
Source documentation: [model card / system card / harness docs, cited]

## Behavioral Findings
- Tool-calling: [documented convention]
- Context/compaction: [documented behavior]
- Known failure patterns: [documented weaknesses]
- Underspecified-instruction handling: [documented behavior]

## Rewritten Moves
[same five-part structure as the source wargame — Move / Expect / Fail+cause /
Counter-move / Trigger — with tool references and context-chunking rewritten
for [NAMED EXECUTOR]'s actual dialect]

## Re-Grade (against the rewritten version)
| # | Point | PASS/FAIL |
|---|---|---|
[8 rows]

## Delta Log
Changed: [tool names / context handling / failure patterns addressed]
Unchanged: [move order / RECON NEEDED structure / abort conditions]
```

## Quality Gate

- [ ] No reasoning-extraction requests made to the executor-docs pass
- [ ] Re-grade is run on the rewritten file, not inherited from the pre-tailoring grade
- [ ] The dialect swap covers both vocabulary (tool names) AND behavior (documented failure patterns, context limits) — a rewrite that only changes tool-name strings hasn't actually tailored anything
- [ ] The executor is named explicitly in the file header
- [ ] The delta log names at least one behavioral (not just cosmetic) change, or explains why none was needed

## Deploy When

A DONE wargame needs rewriting for a specific, named executor model/harness — never for a generic "cheaper executor," only when the executor is named precisely enough to have documented behavior.
