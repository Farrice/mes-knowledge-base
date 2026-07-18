# Source Ledger — wright-thompson-mastery

Claim-by-claim provenance for this skill. Sources consulted during the Wave 3 Lane 4
Batch 18 repair pass are listed below with VERIFIED / LIKELY / UNCONFIRMED labels.

## Sources Consulted

| Source | Path | Size | Status |
|---|---|---|---|
| Primary transcript | `extractions/wright-thompson/transcript.txt` | 62,511 bytes (`wc -c`); 0 newlines — single-line dump (`wc -l`) | VERIFIED — read in full during this repair pass |
| Archive tarball fallback | `_archive/claude-export-2026-07-01.tar.gz` | 7,728 members | NOT NEEDED — `extractions/wright-thompson/` was found non-thin (62KB, one substantial transcript) on first search; per ENVELOPE source-search discipline the archive scan is only required when extractions/ is thin |
| Pre-existing skill content (genius.md Core Philosophy, Voice DNA, Signature Moves 1-6, Decision Framework, Quality Rubric, Cross-Domain Application) | `skills/wright-thompson-mastery/genius.md` | 10,624 bytes (`wc -c`) | VERIFIED against transcript.txt by prior extraction pass — not re-verified line-by-line this pass (out of scope: this pass targeted the three failing heartbeat checks only) |
| `references/cross-domain-patterns.md` (12 numbered patterns) | `skills/wright-thompson-mastery/references/cross-domain-patterns.md` | pre-existing | VERIFIED against transcript.txt by prior extraction pass — spot-checked this pass (Patterns 1, 3, 9, 11): Patterns 1 and 9 matched exact substring; Patterns 3 and 11 matched in substance with the transcript-side transcription artifacts noted in PROVENANCE.md ("under reportported," repeated "280,000" figure) — not fabrications, just un-cleaned transcript noise |

## Provenance note: podcast identity

The transcript self-references its show at char offset 605: "You wouldn't believe it, but How I Write costs a fortune to run" — confirms the source is the "How I Write" podcast. The host's name is never stated anywhere in transcript.txt (searched for "Perell" — zero hits). Externally, "How I Write" is a podcast hosted by David Perell, but since that fact is **not present in the source file itself**, it is not asserted in genius.md and is labeled here as LIKELY (external knowledge), not VERIFIED (in-source). No episode date or number appears anywhere in transcript.txt — episode date is UNCONFIRMED and not fabricated into any anchor.

## Claim-by-Claim Verification (Anti-Patterns section, this repair)

| Claim / quote | Transcript anchor (char offset) | Status |
|---|---|---|
| "I don't think I'm ever gonna say that explicitly, but like hopefully when you read the piece it'll vibrate with that." | 46834–46951 | VERIFIED — verbatim in transcript.txt |
| "struggle with what to do when time was diminishing your most valuable asset, which was the way people remembered you" (Joe Montana example) | 47071–47189 | VERIFIED — verbatim in transcript.txt |
| "I don't think I ever said that" | 47198–47230 | VERIFIED — verbatim in transcript.txt |
| "Every time I feel like I can sort of write myself out of I can write around a hole in my knowledge, it's just bad" | 40943–41056 | VERIFIED — verbatim in transcript.txt |
| "Jay Love used to always warn me about like repetition of effect" | 50559–50622 | VERIFIED — verbatim in transcript.txt |
| "I'd get into things I'm obsessed with and then I'll just like keep going back and back and back and back and back and back" | 50653–50775 | VERIFIED — verbatim in transcript.txt (genius.md quotes a shortened form, "back and back and back," which is a truncation of the same verbatim run, not a fabrication) |
| "you can't depressurize the cabin" | 28491–28523 | VERIFIED — verbatim in transcript.txt; spoken by Thompson's book editor Scott Moyers, reported by Thompson |
| "that you break the spell by jumping ahead in time" | 28673–28722 | VERIFIED — verbatim in transcript.txt |
| "push a ball downhill and then clear out all the obstacles so it rolls" | 28778–28847 | VERIFIED — verbatim in transcript.txt |
| "one of the things you get better at the more you do it is not being so hamfisted with posing the question literally in the piece" | 46236–46364 | VERIFIED — verbatim in transcript.txt |
| "in most braintorming sessions the goal for the individuals in the brainstorming session is to look good not to make the thing good" | 52521–52651 | VERIFIED — verbatim in transcript.txt; note the transcript itself misspells "braintorming" (transcription artifact, not this skill's error) — genius.md quote preserves the correctly-spelled second instance ("brainstorming session") from the same sentence |
| "the accidental thing done in a sense of collaborative fun and joy is always better than something on your calendar" | 53604–53718 | VERIFIED — verbatim in transcript.txt |

## Scope of this repair pass

Fixed: `anti_patterns_sourced` (6 anti-pattern items reformatted from prose headers into
sourced list bullets, each anchor on the list-item line itself, quote + `source:` +
`transcript` keywords present), `recognition_test` (added "recognize this as" language
in the new Model Calibration section), `source_ledger` (this file). Not touched:
`verbatim_exemplars`, `named_entity_floor`, `workflow_contracts` — all three already
passing and left as-is (additive-first, no rewrite of passing content).
