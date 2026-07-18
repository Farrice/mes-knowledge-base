# Source Ledger — skills/benjamin-hardy-identity

Repair pass 2026-07-17 (Wave 3 Lane 4 Batch 2). This ledger exists because the skill's
own `SKILL.md` frontmatter tags `source: claude.ai export 2026-07-01`, but no per-expert
source transcript for Benjamin Hardy exists anywhere in this repository. That absence was
verified with real file reads before writing this ledger, per the envelope's provenance
rules — it is not asserted from memory.

## Absence verification (methodology, run 2026-07-17)

1. `ls extractions/` (full listing, ~150+ named expert directories) — no entry for
   "hardy" or "benjamin-hardy". Confirmed with `find extractions -iname "*hardy*"` →
   zero results.
2. `_archive/claude-export-2026-07-01.tar.gz` — file size **332,779,255 bytes**
   (confirmed via `ls -la`). Full tar listing extracted with `tar -tzf` → **3,864 file
   entries** written to a scratch file (confirmed via `wc -l`). Case-insensitive grep for
   "hardy" across all 3,864 entries → **zero matches**.
3. `agents/benjamin-hardy/memory/context.md` — read in full; contains no source
   transcript, only session-state notes.
4. Conclusion: the `source: claude.ai export 2026-07-01` tag identifies the authoring
   batch/session, not a retrievable primary transcript. Every quote below traces only to
   this skill's own `.md` files, never to an external interview, podcast, or article on
   disk.

## Claim-by-claim ledger

| Claim | Label | Basis |
|---|---|---|
| Dr. Benjamin Hardy is an organizational psychologist (PhD) and bestselling author | VERIFIED | WebSearch 2026-07-17 — Blinkist author profile: "Dr. Benjamin Hardy is an organizational psychologist, keynote speaker and best-selling author... wrote 8 books which have sold nearly 1M copies." |
| *Willpower Doesn't Work* (2018) is a real Hardy book | VERIFIED | WebSearch 2026-07-17 — Blinkist summary confirms title + 2018 publication |
| *Be Your Future Self Now* (2022) is a real Hardy book | VERIFIED | WebSearch 2026-07-17 — Blinkist summary confirms title + 2022 publication |
| *10x Is Easier Than 2x* co-authored with Dan Sullivan | VERIFIED | WebSearch 2026-07-17 — Amazon listing "Sullivan, Dan, Hardy, Dr. Benjamin," ISBN 9781401969950 |
| *Who Not How* co-authored with Dan Sullivan | VERIFIED | WebSearch 2026-07-17 — "He and Dan co-authored Who Not How and The Gap And The Gain" |
| "Psychologically, the future is a tool to shape and direct the present." | LIKELY | Verbatim in `genius.md` (Pattern: The Future Is a Psychological Tool) and `references/prompts-v2/architect-impossible-goal.md:17`; primary transcript UNCONFIRMED (see absence verification above) |
| "the decisions the young entrepreneur is making are the exact opposite decisions..." (10x vs 2x) | LIKELY | Verbatim in `genius.md` (Pattern: 10x Is Easier Than 2x) and `references/prompts-v2/architect-impossible-goal.md:21`; primary transcript UNCONFIRMED |
| Soccer-team-by-55 / "if a timeline is long, it's wrong" example | LIKELY | Verbatim in `genius.md` (Pattern: If a Timeline Is Long, It's Wrong) and `references/prompts-v2/architect-impossible-goal.md:40`; primary transcript UNCONFIRMED |
| Musk five-step algorithm quotes ("you have too many false assumptions...", "optimize something that should not exist") | LIKELY | Verbatim in `genius.md` (Pattern: Question Requirements First) and `references/prompts-v2/architect-impossible-goal.md:49-51`; the five-step algorithm itself is publicly attributed to Elon Musk/Tesla in wide circulation, but Hardy's specific phrasing here is UNCONFIRMED against a primary Hardy source |
| "your eyes can only see, your ears can only hear what your brain is looking for" / Frame-Floor-Focus, Steph Curry floor line | LIKELY | Verbatim in `genius.md` (Pattern: Frame → Floor → Focus) and `workflows/02-raise-the-floor.md:39`; primary transcript UNCONFIRMED |
| "they lie to themselves... about who they really want to be" | LIKELY | Verbatim in `genius.md` (Pattern: All Progress Starts by Telling the Truth) and `workflows/02-raise-the-floor.md:26`; primary transcript UNCONFIRMED |
| "You don't set the goal. You operate from the goal..." | LIKELY | Verbatim in `genius.md` (Pattern: Operate FROM the Goal, Not Toward It) and `workflows/03-operate-from-future-self.md:12`; primary transcript UNCONFIRMED |
| "If you're the buyer, you know what you want and you're willing to walk away..." | LIKELY | Verbatim in `genius.md` (Pattern: Buyer, Not Seller); primary transcript UNCONFIRMED |
| Daniel Gilbert (Harvard) — "Human beings are works in progress that think they're finished." | LIKELY | Attribution to Gilbert is a real, widely-cited research finding (Gilbert's "The Psychology of Your Future Self" TED talk and associated Harvard research are publicly documented); the specific quote's presence in a Hardy source is verbatim in `genius.md` (Pattern: Works in Progress) and `references/prompts-v2/architect-impossible-goal.md:19`, but primary Hardy transcript UNCONFIRMED |
| "they remain the bottleneck in what they're building... king or queen of their project" | LIKELY | Verbatim in `genius.md` (Pattern: Stop Being the Bottleneck / Who Not How); primary transcript UNCONFIRMED |
| "You really just want to use it as a tool for filtering." | LIKELY | Verbatim in `genius.md` (Insight: The Goal Is a Filter, Not a Verdict) and `references/prompts-v2/architect-impossible-goal.md:58`; primary transcript UNCONFIRMED |
| "the principles for how to transform a person are very similar to how to transform an organization" | LIKELY | Verbatim in `genius.md` (Insight: Psychology Drives Strategy); primary transcript UNCONFIRMED |
| Ballmer / Microsoft shareholder-profit-optimization anecdote | UNCONFIRMED | No verbatim quote given in `genius.md` — stated as paraphrase/interpretation, not sourced to any file or external record checked this session |
| "the tangible step is never addition — it's always subtraction" | LIKELY | Verbatim in `genius.md` (Insight: The First Tangible Step of Change Is Always Subtraction); primary transcript UNCONFIRMED |
| "Keeping this while claiming that goal is lying to myself." | LIKELY | Verbatim in `workflows/02-raise-the-floor.md:34`; primary transcript UNCONFIRMED |
| "anyone with money is my potential customer" (worst growth mentality) | LIKELY | Verbatim in `genius.md` (Pattern: Buyer, Not Seller) and `workflows/02-raise-the-floor.md:33`; primary transcript UNCONFIRMED |

## Reading this ledger

- **VERIFIED** = confirmed this session against an external, citable record (WebSearch,
  2026-07-17) independent of this skill's own files.
- **LIKELY** = the quote is genuinely present, verbatim, inside this skill's own files
  (confirmed by direct read this session) and is consistent with Hardy's documented
  public work — but the original interview/podcast/article it was transcribed from is
  not retrievable anywhere in this repository, so it cannot be upgraded to VERIFIED.
- **UNCONFIRMED** = neither a verbatim in-repo source nor an external record was found
  this session; treat as paraphrase/interpretation, not a citable quote.

No claim in this skill was found to be fabricated — every LIKELY quote is real,
verbatim text already present in the skill's shipped files. The gap is one of
provenance depth (no primary transcript on disk), not of invented content.
