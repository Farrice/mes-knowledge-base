# Kallaway Content System — Source Ledger

Claim-by-claim source accounting for `skills/kallaway-content-system/`. Companion to
`references/source-map.md` (operating-model tables, unchanged, already passing).

## Sources Consulted

| Source | Path | Size | Status |
|---|---|---|---|
| Primary transcript | `extractions/kallaway-content-system/transcript.txt` | 43,221 bytes (wc -c) | VERIFIED — read in full, quotes below are verbatim line matches |
| Raw captions (.vtt) | `extractions/kallaway-content-system/B9l9TRhu5Vw.en-orig.vtt` | 398,725 bytes (wc -c) | VERIFIED (exists, not needed — transcript.txt is the cleaned derivative and sufficient for all claims below) |
| Extraction report | `extractions/kallaway-content-system/extraction-report.md` | 4,963 bytes (wc -c) | VERIFIED — cross-checked genius pattern count (10) and hidden-knowledge count (6) against genius.md |
| `extractions/kallaway-content-system/integrity-patch.md` | same dir | 5,108 bytes (wc -c) | NOT USED — this file documents `kallaway-trend-hook-engine`, a different skill; excluded to avoid cross-skill provenance contamination |
| `extractions/kallaway/` (internet-money-machine, word-mastery) | separate dir | n/a | NOT USED — belongs to `kallaway-ai-content-engine` / `kallaway-word-mastery`, out of scope for this skill's claims |

## Claim Verification

| Claim / Anchor | Location Cited | Status |
|---|---|---|
| "The topic should not be at the category level." | transcript.txt:204 | VERIFIED — verbatim |
| "hooks or storytelling or Nike or Apple, that's way too broad" | transcript.txt:372 | VERIFIED — verbatim (paraphrase joins two adjacent lines) |
| "I find AI is good at regurgitating what it's been trained on and what it's heard." / "It's not great at coming up with novel things outside the box." | transcript.txt:472, 474 | VERIFIED — verbatim, two adjacent lines |
| "I don't recommend combining multiple creators here because oftentimes... speaking patterns are like fingerprints." / "If you combine examples from all three, it'll confuse the writer and make it generic." | transcript.txt:688, 692 | VERIFIED — verbatim, two lines in the same passage |
| "You cannot be editing." / "It's too low leverage of a task for you as the creator to be doing it." | transcript.txt:804, 806 | VERIFIED — verbatim, adjacent lines |
| "You're not going to run all 10 like that cuz it's going to get way too repetitive for you and the viewer." | transcript.txt:952 | VERIFIED — verbatim |
| "my process is if I don't have an original idea I want to make, I'm always starting with this list" | transcript.txt:222 | VERIFIED — verbatim |
| "one video flopping and one crushing in the exact same hook, but one has title text and one doesn't" | transcript.txt:452 | VERIFIED — verbatim |
| "To make one video, I go through the same six stages every single time." | transcript.txt:44 | VERIFIED — verbatim |
| S-tier rank format / hooks contrarian-take example | transcript.txt:504-512 | VERIFIED — paraphrased for length, source lines confirm the example (S A B C D F ranking constrains the take) |
| "Constraints breed creativity is like a common frame." | transcript.txt:516 | VERIFIED — verbatim |
| "It's not that AI is going to remove human creativity." / "It's that it frees up human creativity." | transcript.txt:830, 832 | VERIFIED — verbatim, adjacent lines |
| 6-stage rep, 5x/10x carry-forward numbers, metric hierarchy (conversions > followers > views) | transcript.txt:844-962 | VERIFIED — matches `references/source-map.md` Carry-Forward Rules section, pre-existing and unmodified |
| Video title, duration (32:47), acquisition date 2026-05-07 | genius.md header (pre-existing, not authored this pass) | VERIFIED against `references/source-map.md` line 8 ("Duration: 1967 seconds" = 32:47) |
| "Moving to scripting before format is locked" (Anti-Pattern) | — | UNCONFIRMED — no direct transcript quote located; left as an unsourced anti-pattern bullet in genius.md, not anchored, not fabricated |
| "Repeating the same message across visual, text, and spoken hook" (Anti-Pattern) | — | UNCONFIRMED — inferred from the Hook Triad Coordination pattern (transcript.txt:564 defines the three distinct layers) but no explicit warning-against-repetition quote found; left unanchored in genius.md rather than force a citation |

## Notes

- Two of the eight Anti-Pattern bullets in genius.md are honestly left without a source anchor (see UNCONFIRMED rows above) — the check requires ≥5 sourced of however many exist; 6 of 8 are now sourced, meeting the gate without inventing provenance for the remaining 2.
- All quoted material was located by direct `grep -n` against `extractions/kallaway-content-system/transcript.txt` and confirmed by reading the surrounding lines with the Read tool before citing.
- No claim in this ledger relies on the `.vtt` file or the `integrity-patch.md` file — both exist and are non-zero-byte (sizes above), but were not needed as sources for any claim added this pass.
