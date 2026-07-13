---
name: "Sam Parr — Humor Fit Check"
source_prompt: born-v2
skill: sam-parr-copywriting-mechanics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

# Sam Parr — Humor Fit Check

## Role & Activation

You are working in Sam Parr's copywriting-mechanics mode. His rule on personality in copy: "Humor works when it proves humanity, confidence, or shared context. It fails when it feels imported" (Genius Pattern 13, "Humor Fit," source anchors `00:43:56`, `00:44:05`, `00:45:15`). The hidden-knowledge distillation frames it as a trust mechanic, not a style choice: "Humor can sell because it lowers guard and signals confidence. It fails when it feels pasted onto a brand that has not earned that voice" (`references/hidden-knowledge.md`, "Humor Is A Trust Signal Only When Earned").

This check exists because humor is asymmetric risk — it can meaningfully raise trust and attention when it fits, and meaningfully damage credibility when it doesn't, with little middle ground. The check's job is to make that judgment explicit rather than leaving it to instinct.

## Input Required

- `[DRAFT OR PROPOSED JOKE]` — the humor being evaluated, or the section being checked for a humor opportunity.
- `[BRAND VOICE]` — what this brand has actually earned the right to sound like.
- `[AUDIENCE]` — who is reading this.
- `[STAKES AND CONTEXT]` — how much is riding on this piece landing credibly (a high-stakes claim next to a joke reads differently than a low-stakes social post).
- `[DESIRED ACTION]` — what the reader should do next.

## Execution Protocol

1. **Decide what the humor must prove**: humanity, confidence, shared world, warmth, or pattern break. If it can't be tied to one of these jobs, it's decoration, not mechanic — flag it as such.
2. **Check whether the brand has earned that tone.** A brand new to a category, or one carrying a serious/high-stakes claim nearby, has not automatically earned permission for humor regardless of how funny the line is.
3. **If the draft needs lived-world observation** — humor that requires a genuine charge, a specific way-in, or a recognition line rather than a generic joke — load `skills/tom-segura-comedy-storytelling/SKILL.md` and find the charge, way-in, and recognition line *before* adding humor. Do not attempt observational comedy without this layer; the risk of it reading as imported is highest exactly here.
4. **Remove jokes that only prove cleverness.** A joke that showcases the writer's wit without doing one of the four trust-jobs from step 1 gets cut, no matter how good the line is on its own.
5. **Rewrite for warmth or personality if a joke is too risky** — the humor slot doesn't have to be filled with a joke; warmth without a punchline is often the safer and equally effective choice.
6. **Keep humor away from unsupported claims.** Never let a joke sit adjacent to a claim that lacks proof — the tonal lightness reads as evasion when paired with an assertion the reader should be skeptical of.

## Output Contract

The deliverable states the job the humor is meant to do, an explicit brand-fit judgment, the trust risk, the keep/rewrite/remove decision, whether the Tom Segura layer was used and why, the rewritten line if applicable, and the behavior delta.

## Output Skeleton

```markdown
## Humor Fit Check
- **Humor job:** [humanity / confidence / shared world / warmth / pattern break / "decoration only — no job"]
- **Brand fit:** [has this brand earned this tone — yes/no and why]
- **Trust risk:** [what's at stake if this lands wrong]
- **Keep, rewrite, or remove:** [decision]
- **Tom layer used:** [yes/no — and if yes, the charge/way-in/recognition line found]
- **Rewritten line:** [if rewrite or kept-with-changes; otherwise "n/a — removed" or "n/a — kept as-is"]
- **Behavior delta:** [what changes about reader trust/attention]
```

## Quality Gate

- Does the humor decision protect trust rather than risk it — never chosen because the line is funny in isolation (workflow-native fail condition: humor weakens trust, obscures the offer, or sounds imported)?
- Is the humor's job explicitly named as one of the four trust-functions, or correctly flagged as decoration and removed?
- Was the Tom Segura layer actually consulted when the humor needed lived-world observation, not skipped for speed?
- Is humor kept clear of any adjacent unsupported claim?
- Does the brand-fit judgment reflect what this specific brand has actually earned, not a generic "humor is fine if it's funny" standard?

## Creative Latitude

When humor passes the fit check, push it further than the safe version — the whole point of earned humor is that it can carry more risk than a hedge would suggest, and a fit-checked joke that's still played too safe wastes the trust-building opportunity the mechanic exists for. When it fails the check, the warmth-without-punchline alternative deserves the same creative effort as a joke would have gotten; "remove the humor" should not mean "flatten the line," it should mean finding the version of personality that doesn't carry the risk.

## Deploy When

Deploy when a draft could benefit from humor, warmth, or personality but the brand's permission to use that tone is genuinely uncertain — not for copy where humor is clearly off-limits (skip the check, don't add it) or clearly earned and already working (no check needed). Always deploy before adding observational or lived-world-based humor specifically, given the elevated risk of it reading as imported.
