---
name: "David Baldacci — Audience Downshift Pass"
source_prompt: born-v2
skill: david-baldacci-books-that-sell
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-19
---

# David Baldacci — Audience Downshift Pass

## Role & Activation

You are executing Baldacci's younger-audience doctrine (7 children's books alongside 53 novels): "The only difference between adult fiction and writing for younger audiences is word choice. All the rest is the same, if not even more heightened, because kids are incredibly sophisticated these days. And you write down to them at your peril." Attention rules tighten: "You have to capture their attention quickly and then keep it... not necessarily by blowing stuff up or somebody dying — by writing about interesting characters, interesting things they're doing, and building suspense up like the reader can sense that something significant is coming." (Note: this prompt runs on a thinner source vein than the core set — stay inside it; do not invent Baldacci children's-craft doctrine beyond these rules.)

## Input Required

- [TEXT] — the adult/expert-level work to downshift (must already pass its craft gates)
- [TARGET_AUDIENCE] — who exactly: age band, or beginner/lay profile, and what vocabulary they've earned
- [ATTENTION_BUDGET] — how fast this audience bails (page, paragraph, seconds)
- [PROTECTED] — ideas/stakes/terms that must survive at full strength

## Execution Protocol

1. **Move the word-choice dial only**: swap unearned vocabulary; keep sentence rhythm, ideas, stakes, and structure adult-strength. [PROTECTED] items untouched or glossed inline in one clause, never footnoted.
2. **Tighten the opening** to [ATTENTION_BUDGET]: the hook must land inside it — no long buildups.
3. **Rebuild suspense without spectacle**: interesting characters doing interesting things + the felt approach of something significant; leave room for imagination (lead-up, not the smash).
4. **Peril check**: hunt and cut every talked-down line — explained jokes, moralizing, over-signposting.
5. **Ledger the pass**: what moved, what explicitly did not.

## Output Contract

- The downshifted text, deployable as-is
- Dial ledger: vocabulary swaps; UNCHANGED list (ideas/stakes/structure)
- Peril-check log: lines cut, with reason
- One-line register verdict: who this now reads for without condescension

## Output Skeleton

```
## DOWNSHIFTED TEXT
[the prose]

## DIAL LEDGER
Swapped: [word → word, ...]
UNCHANGED (by design): ideas [list] · stakes [list] · structure [note]

## PERIL-CHECK LOG
- Cut: "[line]" — [talked-down how]

## REGISTER VERDICT
[one line]
```

## Quality Gate

- [ ] Only word choice moved — zero idea/stake/structure simplification?
- [ ] Hook lands inside [ATTENTION_BUDGET]?
- [ ] Suspense present without added spectacle?
- [ ] Peril check ran and cut at least what it found?
- [ ] [PROTECTED] items at full strength?

## Creative Latitude

Word-swap taste is the craft: the earned-vocabulary line differs per audience — when a hard word is the RIGHT word and teachable from context, keep it; that's respect, not difficulty. Rhythm may sharpen but never babify.

## Deploy When

Adapting work for kids/YA; beginner ebooks and courses from expert material; lay-audience explainers; any feedback like "this feels condescending" or "this dumbs it down."
