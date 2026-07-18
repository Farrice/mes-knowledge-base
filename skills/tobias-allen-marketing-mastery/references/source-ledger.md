# Source Ledger — Tobias Allen Marketing Mastery

Ground-truth source located and verified during Wave 3 Lane 4 repair (2026-07-18). No file
matching "tobias" or "allen" existed under `extractions/` at repair time (verified via
`ls extractions/ | grep -i tobias` / `grep -i allen`, both empty for this expert). Per
SOURCE-SEARCH DISCIPLINE, the archive `_archive/claude-export-2026-07-01.tar.gz` (332,779,255
bytes, verified via `wc -c`) was scanned member-by-member with a Python `tarfile` content scan
(7,728 members scanned) before concluding absence. 14 members matched "tobias"; of those, 8
conversation exports contain the phrase "Tobias Allen" and were extracted for review.

## Primary Source (VERIFIED as authentic transcript)

- **`claude-export/normalized/conversations/a9431aa3-52bf-40fb-ae87-404c532d58d3.md`** —
  115,616 bytes (`wc -c`), 2,605 lines. Title: "💎11-8-25 Tobias Allen: How to Sell Anything to
  Anyone - With Marketing Genius Tobias Allen." Created 2025-11-09. Contains, verbatim in the
  human turn, a timestamped Merlin AI transcript of the YouTube video **"How to Sell Anything to
  Anyone - With Marketing Genius Tobias Allen"** (youtube.com/watch?v=lpCAqZmNMQU), ~85 minutes,
  interviewer "Matthew," guest Tobias Allen. This is the single ground-truth primary source for
  every genius-pattern claim in this skill — all other conversation exports found in the archive
  (`fe85433c…`, `818a1066…`, `ddaff003…`, `99bb39f8…`, `f7f135a9…`, `e1e874bb…`,
  `3c8615c4…`) re-paste the SAME transcript (confirmed by identical opening paragraphs and video
  ID) as input to repeated AI-extraction/prompt-generation passes — they are not independent
  sources.
- Cross-check: `skills/tobias-allen-marketing-mastery/references/extraction-report.md` and
  `genius-patterns.md` (both dated 2026-02-12, pre-existing in the skill) describe themselves as
  a "re-extraction from deployed skill," i.e. downstream of the same transcript, not an
  independent source. Retained as secondary confirmation only.

## Claim-by-Claim Verification

| Claim (genius.md) | Status | Anchor |
|---|---|---|
| "Advised 12+ nine-figure businesses" | VERIFIED | Transcript 0:06–0:12: "only one in 6,000 businesses reached the 9 figure mark. I've had the privilege to either work, help, or advise a dozen of them." ("a dozen" = 12) |
| "$250K from single email list in 30 days" | VERIFIED | Transcript 1:56–2:01: "For the first email list I was given, I generated 250,000 out of it in the first 30 days." |
| Cialis vs. Viagra bullseye case study | VERIFIED (auto-transcription renders "Cialis" as "Scialis"/"Sialis"/"Pialis") | Transcript 0:16–1:19: 6 months of research, married couples buying for intimacy, outsold Viagra. |
| "Translation Test" — 37 languages | VERIFIED | Transcript 8:10–8:12: "I know this book is going to be translated in 37 different languages." |
| Domino Strategy — 1.5x geometric growth | VERIFIED | Transcript 27:49–27:57: "a small domino can knock over another domino that's about 1.5x larger than the next." |
| Behavioral Residue — Livestrong yellow bands | VERIFIED, with correction | Transcript 28:51–30:05: attributed to "the Nike campaign with Lance Armstrong" — bought 100,000 units, sold ~1 million in year one. genius.md's "Livestrong yellow bands" framing is directionally accurate but omits the Nike/Lance Armstrong attribution present in the source; not a fabrication, an omission. |
| Attention Arbitrage — "$1 → $30-100+ vs. typical $2-3" | VERIFIED (rounded) | Transcript 47:19–47:26: "you put $1 instead of getting $3 out, you're getting 30 or 100 bucks." Source says typical $3, not $2-3 — genius.md's range is a reasonable rounding, not a distortion. |
| Historical arbitrage example — comic book advertising | VERIFIED | Transcript 47:59–48:12: "an example looking at history is comic book advertising... super cheap... the first businesses that figured out about comic advertising, they were able to grow pretty large." |
| Historical arbitrage example — "early podcast sponsorships" | UNCONFIRMED | Podcasts are discussed extensively (skill acquisition, 1:32–1:46) but never paired with "sponsorship" or framed as a historical arbitrage example in the transcript. This specific pairing is an unsourced elaboration layered onto the verified comic-book example. |
| Investor reports / SEC filings / ChatGPT as free consulting | PARTIALLY VERIFIED | Transcript 38:18–38:40 confirms reading public-company investor reports and using ChatGPT to pull them ("You can actually get chat GBT to pull this for you"). "10-K filings," "earnings calls," and the "free McKinsey-level intelligence" comparison in `genius-patterns.md` do not appear in the transcript — LIKELY, a plausible elaboration on a verified core claim, not itself sourced. |
| Scale-appropriate strategy (<$10M / $10M-$100M / $100M+) | VERIFIED | Transcript 22:36–22:44 ("if you're small, focus on distribution. If you're big... doubling down on the message") and 23:53–24:10 (Facebook group funnels pointless at $100M scale). |
| CRM-first / backend-before-frontend economics | VERIFIED | Transcript 49:01–51:00: extended discussion of treating the email/SMS list as the primary asset, optimizing it before frontend ad spend. |
| Research-to-writing 80/20 ratio; "painful process" research standard | VERIFIED | Transcript 7:46–8:34: "I actually find the process quite painful because the amount of research that I have to go in and do... is I believe it requires an extraordinary level of effort." |
| **Pattern 9 — "Attribution Architecture by Design"** (revenue fingerprint, signal-before-sale, retroactive attribution debt) | **UNCONFIRMED** | No occurrence of "fingerprint," "signal action," or "attribution debt" anywhere in the transcript. The only attribution-adjacent material is transcript 50:03–50:08 (a passing remark that a purchase counts toward the contact list "even if the attribution comes from a Facebook ad"). The elaborate framework in Pattern 9 is a downstream synthesis, not a sourced extraction — flagged, not removed (additive-first boundary), but should be read as LIKELY/derived rather than a direct capture of Tobias's stated method. |
| 6 anti-pattern anchors added in genius.md (2026-07-18 repair) | VERIFIED | Each quote confirmed as an exact substring of the transcript via automated match (see PROVENANCE.md for line/timestamp detail). |

## Legend
- **VERIFIED** — quote or fact confirmed as an exact or near-exact match against the primary transcript.
- **LIKELY** — consistent with and adjacent to verified transcript content, but the specific phrasing/framework is not itself present in the source; a reasonable extrapolation.
- **UNCONFIRMED** — no supporting occurrence found in the primary transcript after a full read/grep pass; not removed under the additive-first boundary, but should not be treated as a direct Tobias Allen quote or claim.
