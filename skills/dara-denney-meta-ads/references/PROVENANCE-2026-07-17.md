# Provenance — dara-denney-meta-ads repair

Anchor → source file+location table for every quote/claim used or referenced while fixing `recognition_test` and `source_ledger`.

| Anchor (in this repair's output) | Source file | Location |
|---|---|---|
| "I bet against this... and was proved wrong" | `extractions/dara-denney/transcript.txt` | opening paragraph |
| "We're not cheap, and we don't want to be" / "Shout out to our creative strategist Nika" | `extractions/dara-denney/transcript.txt` | We're-not-cheap section |
| "the big differentiator... eight and nine-figure brands... have figured out partnership ads" | `extractions/dara-denney/transcript.txt` | yapper/partnership section |
| Apothékary anti-exemplar quote | `extractions/dara-denney/transcript.txt` | yapper section |
| Meta Creator Marketplace hook-rate example (50%/7%) | `extractions/dara-denney/transcript.txt` | yapper/partnership section |
| Purge/self-correction note ("invented headlines... PURGED") | `skills/dara-denney-meta-ads/references/static-ad-exemplars.md` | line 5 |
| Static-ads-masterclass sourcing claim (5,412 words, watched) | `extractions/dara-denney/static-ads-masterclass/VISION.md` | line 3 |
| File sizes for all four consulted sources | direct `wc -c` on each path (see references/source-ledger.md table) | this repair pass |
| `_archive/claude-export-2026-07-01.tar.gz` size (332,779,255 bytes) | `ls -la _archive/` | this repair pass |

No new quotes were invented. Every claim in `references/source-ledger.md` traces to one of the four files above, or is explicitly labeled UNCONFIRMED with the search evidence recorded (see "Two additional video transcripts" section of the ledger).
