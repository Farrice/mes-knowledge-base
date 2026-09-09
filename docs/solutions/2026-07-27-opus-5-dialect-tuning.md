---
date: 2026-07-27
session: opus-5 dialect tuning
name: opus-5-dialect-tuning
problem_class: harness / model dialect / apparent regression
domain: harness
status: proven
problem_signature: "output quality drops after a model upgrade — over-structured, not conversational, expanding the ask off one detail, spiraling rounds on a single artifact — and it feels like the new model is worse or just hard to prompt"
tags: [opus-5, model-dialect, claude-md, verification, subagents, prompting]
---
# Solution Card — "the model got worse" was a harness tuned for the previous model

**Date:** 2026-07-27 · **Domain:** harness / model dialect · **Trigger:** *"Is this my fault? Is Opus 5 just a different model from 4.8, because we were doing great with 4.8?"*

## The problem

Output quality fell across a session. Eight rounds of LinkedIn headline variants, each worse than the last by the operator's own read. His diagnosis: over-structured, not conversational, doesn't read between the lines, cherry-picks one detail and builds everything on it.

The tempting conclusion — *"Opus 5 is a hard model to prompt, we need to redo the system"* — was wrong and expensive.

## What it actually was

**The harness was tuned for Opus 4.8 + Fable.** Anthropic's migration guide documents four Opus 5 behavior shifts, each matching a reported symptom exactly:

| Symptom | Documented behavior |
|---|---|
| Over-structured, not conversational | Longer output by default. **`effort` is not the lever** — only prompting shortens it |
| Went off on one detail, expanded the ask | Task scope expansion — adds steps, applies its own judgment silently |
| Spiraling rounds on one artifact | Over-verification: it self-verifies natively, so *instructions to verify* create redundant work |
| — | Over-delegates to subagents — **the reverse of 4.8**, which needed encouragement to delegate |

The harness was actively fighting all four: CLAUDE.md Step 5.5 mandated an isolated verification subagent, the sub-agent trigger was a floor ("2+ experts or 10+ files"), and a hook appended a five-line Next Moves block to *every* reply including one-line answers.

## The fix

**Five edits to one file.** No rebuild.

1. A **Model Dialect** block near the top of CLAUDE.md carrying the four DO/DON'Ts inline — including the `<tone_preference>` conciseness tag and the scope-discipline paragraph.
2. **Deleted** the isolated-verification-subagent dispatch. Kept the no-fabrication floor, VERIFIED/LIKELY/UNCONFIRMED labels, and the Factual Grounding veto — those are anti-hallucination, a different thing from self-check scaffolding.
3. **Inverted** the sub-agent trigger from a floor to a ceiling.
4. Made the **Next Moves** block conditional on a delivery instead of mandatory every turn.
5. Made **Step 0 co-creation fire** by inlining the PARTNER dial — interview before producing on taste work.

## The rule

**Before concluding a model regressed, check whether the harness is still written for the previous one.**

Two second-order lessons worth more than the fix:

- **The evidence already existed and was unwired.** `directives/model-dialects/claude-opus-5.md` had been probed the day before and predicted the exact failures — but it was referenced only from a file framed as "for writing LLM-calling scripts," so it never entered the operating context. **A card nobody loads is a card nobody has.** Same for the co-creation layer: nominally always-on for eleven days, fired zero times.
- **"Tell the model to double-check" is now wrong on this tier.** It's a standard prompting instinct and it inverts here. Any prompt library that applies self-check uniformly needs a carve-out, not a global rule.

Related: [[2026-07-27-compass-doctrine-blocking-gate-audit]] · `feedback_opus-5-dialect-tuning`
