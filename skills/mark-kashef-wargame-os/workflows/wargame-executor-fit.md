---
description: Fire when a DONE wargame needs rewriting for a specific, named executor model/harness — "I want you to tailor this war game to exactly how Sonnet 5 would execute it." Never fires for a generic "cheaper executor" — only when the executor is named precisely enough to have documented behavior.
---

# /wargame-executor-fit — Tailor The Route To Its Runner

"Executors differ, and a route in the recipient's dialect fails less." A wargame that's DONE against a generic mid-tier model still has slack in it — tool names, context-window assumptions, and known failure patterns are model-specific. This workflow closes that slack for a named executor.

## Pre-Flight Gate

- **DONE-first check**: has the wargame already passed all 8 `SUCCESS.md` points before tailoring starts? Tailoring a still-broken draft wastes the dialect pass on a route that's going to change anyway — run `/wargame-run` → `/wargame-grade` to DONE first.
- **Named-executor check**: is the executor a specific model + harness ("Sonnet 5 in Claude Code," "GPT-5.1 via the Assistants API"), not a placeholder like "a cheaper model"? If unnamed, this workflow doesn't apply — leave the generic executor framing as written.
- **Source-of-truth check**: is there actual documentation to tailor against (a model card, a harness's tool-use docs, a system card) — or would this pass just be guessing? Heuristic 8 requires a real dialect to translate into, not an assumed one.

## Skill Acquisition

- `genius.md` — Decision Heuristic 8 (tail the executor to the model), the Signature Moves section (mode-switch open stays intact, only the executor framing narrows)
- `extractions/wargame-source/mes-extraction.md` — Genius Pattern 12 (Model-Card Dialect Migration): "spin up a sub agent or sub agents to go through all the documentation, maybe the system card of that model"
- `references/goal-and-loop-contracts.md` — the "Platform landmine" WATCH OUT box: never ask a model to expose or reproduce its own reasoning

## Execution

1. **Identify the executor precisely.** Model name, version, and harness (Claude Code / Claude Desktop / API-direct / Cursor / another IDE). Write it at the top of the tailored wargame file so anyone reading it later knows exactly what dialect it's written in.
2. **Dispatch a behavioral-notes pass.** If the executor is a Claude model in Claude Code, use the `claude-code-guide` agent. Otherwise, WebFetch the executor's public docs/system card. Request BEHAVIORAL FINDINGS ONLY:
   - documented tool-calling conventions (what it calls its tools, how it prefers to batch calls)
   - context-window size and compaction behavior (does it summarize, truncate, or fail past a limit)
   - known failure patterns (documented weaknesses, common hallucination triggers, formatting quirks)
   - anything in the docs about how it handles ambiguous or underspecified instructions

   **WATCH OUT (verbatim, generalized beyond Fable)**: "Do not ask the model to explain its thinking or reproduce its reasoning in the output... Ask for artifacts, findings, quotes, and rewrites, never for the thinking itself." Any reasoning-model harness carries some version of this risk — treat the rule as universal, not platform-specific.
3. **Rewrite the Moves in the executor's dialect.** Swap generic tool references for the executor's actual tool names ("search the repo" → "use Grep/Glob," "run a long job" → "use Bash with run_in_background"). Adjust recon steps for the executor's real context-window/compaction behavior — chunk large reads into its actual working-set limits. Rewrite any move that assumes a capability the named executor doesn't have.
4. **Re-grade against all 8 points, post-rewrite.** Tailoring can silently break points 1–3 — an executor-specific tool name might not produce the identical observable the original move predicted. Run the `eight-point-standard.md` checklist against the REWRITTEN version, not the original; a wargame that was DONE pre-tailoring is not automatically DONE post-tailoring.
5. **Log the delta.** What changed (tool names, context handling, failure patterns newly addressed) versus what stayed identical (move order, RECON NEEDED structure, abort conditions). This delta log is the proof the tailoring pass did real work rather than a cosmetic relabel.

## Tool-Name Dialect Reference (starting point, not exhaustive)

| Generic move language | Claude Code (Sonnet/Opus) | A non-Claude harness |
|---|---|---|
| "search the codebase" | Grep/Glob | its native search tool — confirm the name from docs, don't assume |
| "read a file" | Read (whole-file, line-numbered) | may require chunking if its context window is smaller |
| "run a long job" | Bash with `run_in_background: true` | may lack background execution entirely — the move needs a synchronous-wait fallback |
| "write/edit a file" | Edit (diff-based) or Write (full overwrite) | confirm whether it diffs or overwrites — this changes what a "successful edit" observation looks like |

## Content Type Adaptations

| Type | What typically needs tailoring | What usually stays fixed |
|---|---|---|
| **Code build** | Tool names (Grep/Glob/Bash specifics), test-runner invocation, file-write conventions | Move order, abort conditions, design-token freezes |
| **Copy/content** | Draft-and-revise loop shape (single-pass vs. iterative editor tools) | Voice rules, CTA, evidence rules |
| **Research/analysis** | Search-tool names (WebFetch/WebSearch/Perplexity-specific), citation format the executor natively produces | RECON NEEDED settling checks, verification pass criteria |
| **Ops/automation** | Subagent-dispatch conventions, background-process handling | Phase sequencing, acceptance checks per phase |

## Worked Example: Why Behavioral, Not Just Vocabulary

The crown exemplar's Move 9 (`extractions/wargame-source/mes-extraction.md`) predicts a failure caused by the EXECUTOR'S OWN pattern-matching: the About-page headshot SVG "incorrectly inherits `aria-hidden='true'` from Move 7's icon pattern." That's the standard this workflow holds itself to — a tailoring pass that only renames tools ("use Grep instead of grep") is cosmetic. A tailoring pass that predicts a NAMED executor's specific tendency to over-generalize a pattern it just used, and writes the counter-move for it, has actually done the job Heuristic 8 describes.

## When NOT To Tailor

Not every executor swap justifies this workflow. Skip it and keep the generic version when:
- the named executor is close enough in tier/dialect to the "cheaper executor" the wargame was already written for (e.g. Sonnet-to-Sonnet across sessions) — tailoring a wargame to itself is wasted motion
- the mission's moves are already tool-agnostic (pure judgment/copy work with no file-system or repo interaction) — dialect differences mostly live in tool-calling conventions, which don't apply
- there's no real documentation to tailor against — a guess dressed as a tailored wargame is worse than the honest generic version, because it reads as more authoritative than it is

## Output Requirements

Tailored wargame at `.agent/missions/<name>/wargames/<NN>-<slug>.<executor-slug>.md` (executor named in the filename and the file's header), plus a delta-log entry appended to the mission's `LEDGER.md` naming what changed and confirming the re-grade result.

## Quality Gate

- [ ] No reasoning-extraction requests made to the executor-docs pass (WATCH OUT rule enforced without exception)
- [ ] Re-grade is run on the rewritten file, not inherited from the pre-tailoring grade — a point cannot be marked passing without being re-checked against the new dialect
- [ ] The dialect swap covers both vocabulary (tool names) AND behavior (documented failure patterns, context limits) — a rewrite that only changes tool-name strings without addressing behavioral differences hasn't actually tailored anything
- [ ] The executor is named explicitly in the file header — a "tailored" wargame with no stated target executor has failed silently
- [ ] The delta log names at least one behavioral (not just cosmetic) change, or explains why none was needed
