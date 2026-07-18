# PROVENANCE.md — damon-cart-nlp repair (Wave 3 Lane 4 Batch 3)

Anchor → source file+location table for every claim added or reformatted in this
repair. See `skills/damon-cart-nlp/references/source-ledger.md` for the
claim-by-claim VERIFIED/LIKELY/UNCONFIRMED table (this file is the pointer index;
that file is the judgment).

## Root fact: no primary source file exists in this repo

- Checked: `ls extractions/ | grep -iE "damon|cart"` → 0 matches of 193 dirs.
- Checked: `find . -iname "*damon*"` (repo-wide) → only this skill's own scaffold
  (`skills/damon-cart-nlp/`, `agents/damon-cart/`, `.claude/commands/damon-cart*.md`)
  plus an identical mirror of `skills/` inside the stale, unrelated worktree
  `.claude/worktrees/w3-lane3-repair-execution/` (confirmed via `diff -q` — zero
  content differences from `skills/damon-cart-nlp/`, i.e. not a separate source).
- Both checks run and recorded 2026-07-17.

## File sizes actually read (wc -c, not wc -l)

| File | Bytes |
|---|---|
| `skills/damon-cart-nlp/SKILL.md` | 4,593 |
| `skills/damon-cart-nlp/genius.md` (pre-repair) | 13,695 |
| `skills/damon-cart-nlp/workflows/01-dissolve-resistance.md` | 4,827 |
| `skills/damon-cart-nlp/workflows/02-transform-self-concept.md` | 5,279 |
| `skills/damon-cart-nlp/workflows/03-persuade-through-their-map.md` | 5,902 |
| `skills/damon-cart-nlp/references/prompts-v2/dissolve-resistance-cycle.md` | 8,812 |
| `skills/damon-cart-nlp/references/prompts-v2/persuasion-through-their-map.md` | 9,930 |
| `skills/damon-cart-nlp/references/prompts-v2/self-concept-transformation.md` | 8,556 |

None are 0-byte or truncated — the absence of a source export is a checked-in
fact, not an assumption.

## Anchors added in `genius.md` → `## Anti-Patterns`

| Anti-pattern item | Anchor | Status |
|---|---|---|
| "overcome/defeat/push through" language | genius.md, Pattern "The Japanese Soldier Reframe," lines 5-8 (pre-repair numbering) | Skill-text VERIFIED (present, read in full); external origin UNCONFIRMED |
| Affirmations / fake-it-till-you-make-it | genius.md, Pattern "The Anti-Affirmation Principle," lines 25-28 | Skill-text VERIFIED; external origin UNCONFIRMED |
| Euphoria treated as success | genius.md, Pattern "Grounded Change (The Anti-Euphoria Rule)," lines 30-33 | Skill-text VERIFIED; external origin UNCONFIRMED |
| Literal "parts" committee framing | genius.md, Pattern "Wholeness Over Parts," lines 35-38 | Skill-text VERIFIED; external origin UNCONFIRMED |
| Selling success to a "failure"-state prospect | genius.md, Pattern "Enter the Model of Reality," lines 40-43 | Skill-text VERIFIED; external origin UNCONFIRMED |
| Countering objections instead of utilizing them | genius.md, Pattern "Utilization," lines 45-48 | Skill-text VERIFIED; external origin UNCONFIRMED |
| Why/what-questions instead of how-questions | `workflows/03-persuade-through-their-map.md`, Phase 1 (unmodified file, 5,902 bytes) | Skill-text VERIFIED; external origin UNCONFIRMED |

## External (web-checked) anchors used in `references/source-ledger.md`

All checked via live web search, 2026-07-17:

- `youtube.com/c/DamonCart`, `youtube.com/damoncart` — channel existence
- `youtube.com/watch?v=WQi5-sb_Yhk` — "Candid Interview With NLP Master Steve Andreas & Damon Cart - Part 1"
- `youtube.com/watch?v=6jiRWnSvzPM` — Part 2 of the same interview series
- `youtube.com/watch?v=ef1TfgsAkJc` — "Rare Interview With NLP Legends Steve & Connirae Andreas & Damon Cart"
- `andreasnlp.com/articles/second-interview-of-steve-andreas-by-damon-cart/`
- `buzzsprout.com/2250263/episodes/16325577-nlp-sales-secrets-to-make-your-first-1-million-in-2025-the-self-concept-podcast-24`
- `podcasts.apple.com/nz/podcast/sales-masterclass-nlp-techniques-you-can-use-instantly/id1708739673`
- `lifemasterygym.com/blog/Influence-And-Persuasion-Skills-From-World-Record-Holder-Jason-Fladlien`
- `themindsetandselfmasteryshow.com/breaking-free-of-the-self-worth-trap-using-nlp-with-damon-cart/`

These establish Cart's real-world identity and the Andreas/Fladlien connections
at LIKELY-to-VERIFIED confidence; they do NOT verify any specific quote inside
`genius.md` (no transcript of these specific videos/episodes was pulled and
diffed against the skill's quoted lines — that remains UNCONFIRMED work for a
future pass if a deeper audit is warranted).

## Model Calibration section

Added `## How to Use This Skill (Model Calibration)` to `genius.md`, modeled on
`skills/ben-watkins-storytelling/genius.md` lines 7-16 (read once, not copied).
Written fresh against this expert's own texture: resistance-as-ally language
discipline, the Strategic Pause on the page, and the anti-euphoria register —
sourced from the existing patterns already in this file, not invented.
