# Source Ledger — sam-parr-copywriting

Every source consulted during the wave-3 lane-4 batch-15 repair, and every claim it
backs, labeled VERIFIED / LIKELY / UNCONFIRMED. Ground truth = files under
`extractions/sam-parr/` plus verbatim quotes already inside the skill files.

## Sources Consulted

| Source | File | Size | Notes |
|---|---|---|---|
| YouTube DR copywriting masterclass (Sam Parr, w/ Hormozi's team/Alex) | `extractions/sam-parr/transcript.txt` | 68,567 bytes (`wc -c`) | 56 min, 13,484-word transcript. youtube.com/watch?v=uf4fR3qcDkU per `extractions/sam-parr/vision-copywriting.md`. Primary source for all anti-pattern anchors added in this repair. |
| Deep extraction (MES 3.0) | `extractions/sam-parr/copywriting-extraction.md` | 19,451 bytes (`wc -c`) | Structured genius-pattern writeup derived from the transcript above; first tracked in git 2026-05-30 (`git log --diff-filter=A`). |
| Extraction vision/scoping doc | `extractions/sam-parr/vision-copywriting.md` | 5,074 bytes (`wc -c`) | Roster-crowding rationale, video URL, deferral map. |

## Claim-by-Claim Ledger (this repair's additions to genius.md)

| Claim / Quote | Label | Basis |
|---|---|---|
| "A lot of the incentives are just to like shove the benefits in your face" | VERIFIED | Exact substring match, `transcript.txt` (`grep -o -i ".\{80\}shove.\{80\}"` confirms verbatim). Also independently verified by the predecessor worker per envelope context; re-confirmed here rather than trusted blind. |
| "the man was sad, he wanted to go fish" | VERIFIED | Exact substring match, `transcript.txt` (Hemingway/Old Man and the Sea passage). |
| "imagine storing your food in the toilet bowl" | VERIFIED | Exact substring match, `transcript.txt` (Caraway/Tupperware rewrite passage). |
| "Now everything I just said was fake. I don't know if that's true." | VERIFIED | Exact substring match, `transcript.txt` (the guardrail moment already cited elsewhere in genius.md). |
| "There's no such thing as too long, just too boring." | VERIFIED | Exact substring match, `transcript.txt`. Note: the pre-existing genius.md anti-pattern bullet had paraphrased this as "there's no such thing as too long, only too boring" — this repair corrects the anti-pattern anchor to the verbatim wording; the paraphrase elsewhere in the file (Pattern 6) is left untouched per additive-first/minimal-touch. |
| Extraction git-add date 2026-05-30 for `copywriting-extraction.md` | VERIFIED | `git log --diff-filter=A --format="%ad %h" --date=short -- extractions/sam-parr/copywriting-extraction.md` → `2026-05-30 205d3dc14`. |
| "Cheap question sign-offs / generic CTAs with no story behind them" (anti-pattern 6) | UNCONFIRMED (attribution) | No matching Sam Parr quote found in `transcript.txt` after searching "sign", "CTA", "call to action", "question". This anti-pattern is a Farrice house rule (`feedback_no-cheap-question-signoffs.md`) folded into the skill's quality bar, not a claim about what Sam said. Left in place, unanchored, and labeled here rather than fabricating a Sam attribution. |
| All other pre-existing genius.md pattern/exemplar quotes (Patterns 1-15, Hall of Fame exemplars 1-3, Hidden Knowledge) | Not re-verified this pass | Out of scope for this repair (already passing `verbatim_exemplars` and `named_entity_floor`); flagged here for a future pass if the skill is re-audited end to end. |

## Absence Checks Performed (per source-search discipline)

- `ls extractions/ | grep -i parr` → only `sam-parr/` exists; no additional Sam Parr extraction directories missed.
- No `_archive/claude-export-2026-07-01.tar.gz` scan was required — primary extraction files under `extractions/sam-parr/` were sufficient and non-empty (sizes recorded above via `wc -c`), so absence-claim discipline for the tarball path did not trigger.
