# Source Ledger — sean-macintyre-persuasion-philosophy

Claim-by-claim provenance for this skill. Every source consulted during the Wave 3 Lane 4 Batch 15 repair pass is listed below with a VERIFIED / LIKELY / UNCONFIRMED label.

## Sources Consulted

| Source | Path | Size | Status |
|---|---|---|---|
| Primary transcript | `extractions/sean-macintyre/transcript-consolidated.md` | 37,446 bytes (`wc -c`) | VERIFIED — read in full during this repair pass |
| Source metadata | `extractions/sean-macintyre/source-metadata.md` | 1,933 bytes (`wc -c`) | VERIFIED — read in full; confirms YouTube video ID `5m6CSnfDNks`, host Matthew Volkwyn, extraction date 2026-04-27 |
| Existing quote bank | `skills/sean-macintyre-persuasion-philosophy/references/source-quotes.md` | 12,876 bytes (`wc -c`) | VERIFIED — pre-existing curated quote file, cross-checked against transcript-consolidated.md |
| Archive tarball fallback | `_archive/claude-export-2026-07-01.tar.gz` | N/A | NOT NEEDED — the primary extraction (`extractions/sean-macintyre/`) was found and confirmed non-empty on first search; the archive fallback per ENVELOPE's source-search discipline was not required |

## Claim-by-Claim Verification (Anti-Patterns Section, this repair)

| Claim / quote | Transcript anchor | Status |
|---|---|---|
| "Why are you using problem agitate solution when the market's already level four sophistication? ... why don't you use a mechanism lead or something" | line 57, timestamp 00:17:21-00:17:34 | VERIFIED — verbatim in transcript-consolidated.md, spoken by Matthew Volkwyn |
| "If you come up with it out of thin air, the second people start digging, they don't find any substance and then they're like their ad skepticism" | line 43, timestamp 00:09:19-00:09:29 | VERIFIED — verbatim, spoken by Sean Macintyre |
| "David is looking to music and seeing, okay, what can I learn from this field that I can apply to my copy to make it better?" | line 171, timestamp 01:13:49-01:15:10 | VERIFIED — verbatim, spoken by Sean Macintyre |
| "[Hormozi's books] are great if you are selling something that people already want. They are not great if you're reaching somebody who doesn't realize they have a problem" | line 29, timestamp 00:05:25-00:05:44 | VERIFIED — verbatim, spoken by Sean Macintyre |
| "a realization smacked me in the face like a wet bag of burritos. It was the simple fact that I was not operating at an optimal or high enough level for that optimization to matter" | line 101, timestamp 00:40:12-00:40:21 | VERIFIED — verbatim, spoken by Sean Macintyre |
| "What if I just not spend that and go read a goddamn book?" | line 173, timestamp 01:15:32-01:16:20 | VERIFIED — verbatim, spoken by Sean Macintyre |
| "every time you inspire yourself about a particular topic, diminishing returns ... the hedonic treadmill kicks in and your ability to feel inspired about something ... diminishes" | line 139, timestamp 01:00:12-01:00:25 | VERIFIED — verbatim, spoken by Sean Macintyre |
| "I'm not enjoying Spanish anymore when I was just learning it" | line 185, timestamp 01:22:47-01:23:22 | VERIFIED — verbatim, spoken by Matthew Volkwyn |
| Idea resonance "only gets you through the first five pages of a 70-page promo" | line 15, timestamp 00:01:06-00:01:47 | VERIFIED — verbatim, spoken by Sean Macintyre |
| "It's only for some people that habit eventually transmogrifies into passion. Very few people are passionate about writing ads for dick pills" | line 143, timestamp 01:01:47 | VERIFIED — verbatim (transcript has a typo "transmogriies," corrected in the skill text), spoken by Sean Macintyre |

## Pre-Existing Content (not touched this pass, inherited status)

The remaining genius.md content (Genius Patterns 1-12, Hall of Fame Exemplars, Signature Moves, Source Quote Bank) was written by the original extraction and is VERIFIED against `transcript-consolidated.md` and `source-quotes.md` by prior passes — not re-verified line-by-line in this repair (out of scope: this pass targeted only the two failing heartbeat checks, `anti_patterns_sourced` and `recognition_test`).

## Note on the "Citing cross-domain references without applying them" anti-pattern

This item was originally marked "(Implied)" with no direct quote — it is Sean's *implicit* stance inferred from his cross-pollination doctrine (see verified quote above, line 171), not a verbatim anti-pattern statement. Labeled here as an inference, not fabricated as a direct quote, to keep the distinction honest.
