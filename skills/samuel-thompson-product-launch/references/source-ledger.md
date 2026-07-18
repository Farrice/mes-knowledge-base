# Source Ledger — samuel-thompson-product-launch

Claim-by-claim provenance. Labels: **VERIFIED** (found verbatim or as a directly-cited number/fact in a located source file), **LIKELY** (consistent with the source but paraphrased/summarized rather than quoted), **UNCONFIRMED** (no located source — treat as unverified until a primary source surfaces).

## Primary Source

- **Merlin AI transcript** — "I Spent $289 So AI Could Build My Business" (YouTube interview, Samuel Thompson), attached to a Claude.ai extraction conversation created 2026-01-18.
  - Location: `_archive/claude-export-2026-07-01.tar.gz` → member `claude-export/normalized/conversations/1ec27df4-be87-4c3f-8cab-e3062ab0bfc3.md` (80,716 bytes, `wc -c`).
  - Not present under `extractions/` — the only match there is `extractions/wright-thompson` (a different, unrelated expert: sports journalist Wright Thompson). Fragment searches run without apostrophes/punctuation for "samuel" and "thompson" against `extractions/` returned nothing; the transcript was located via a per-member content scan of the archive tarball (7,720 members scanned, matched on "samuel thompson" / "rigged slot machine").
  - This transcript is the ground truth behind every Genius Pattern, Hidden Knowledge point, and Anti-Pattern in `genius.md` — the skill's existing pattern language ("rigged slot machine," "Laker game," "It's just sugar," "80% head start") is Thompson's own phrasing, confirmed present verbatim in this file.

- **Secondary conversation file** — `claude-export/normalized/conversations/5e918eaf-f501-4b80-9588-688c51ea7dda.md` (13,753 bytes, `wc -c`), a follow-up Claude.ai session ("Digital Product Mastery 2") that continues generating Crown Jewel prompts by searching back into the primary conversation. Contains no new raw Thompson quotes — it is a meta-conversation about the extraction, not additional source material.

## Claims

| Claim | Label | Basis |
|---|---|---|
| "It started super simple as like a really messy chat GBT generated book... that I made in an hour while watching the Laker game" | VERIFIED | Verbatim in 1ec27df4...md |
| "99% of traffic is mobile, so I'm only thinking about uh mobile optimization" | VERIFIED | Verbatim in 1ec27df4...md |
| "I always do this compare at price... New Year sale... St. Patrick's Day sale" | VERIFIED | Verbatim in 1ec27df4...md (paraphrased order preserved) |
| "Yes, I'm going to put fake reviews on here to start and then I will replace them as I get real ones. I promise." | VERIFIED | Verbatim in 1ec27df4...md |
| "I am very rarely trying to get a final output out of AI. I need like... a 80% head start" | VERIFIED | Verbatim in 1ec27df4...md (minor ellipsis for a disfluency) |
| "well 50% of uh marriages end in divorce... if the wedding market is huge... the divorce market probably is like half the size" | VERIFIED | Verbatim in 1ec27df4...md |
| "we're going to hire somebody on Fiverr" | VERIFIED | Verbatim in 1ec27df4...md (opening tool-stack list) |
| "conversion optimize. You can literally just buy it and it has a bunch of these plugins already built in" | VERIFIED | Verbatim in 1ec27df4...md, describing the Solo Drop theme |
| Solo Drop ≈ $200 lifetime; Elixir ≈ $175 for one license | VERIFIED | Transcript: "Yeah, that's dope... I think lifetime's like 200" (Solo Drop) and "I don't remember their pricing. 175 for one license" (Elixir) |
| $29 base price, $17-18 upsell bump, ~$42-43 AOV, CAC "sub 40" good days / "45" bad days | VERIFIED | Transcript: "I was selling the book for 29 bucks... a $17 or $18 product... Mine was landing on average at like 42 43. And my CAC was roughly like on good days it was sub 40. On bad days it was like 45." |
| $199/year Facebook group for divorced parents | VERIFIED | Transcript: "grab 199 bucks a year for a Facebook group of like... these are all the people that have gone through what you've gone through" |
| Divorce book runs 197 printed pages | VERIFIED | Transcript: "this book... lands at 197 printed pages" |
| "100 companies in 10 years" | VERIFIED | Stated by both the interviewer and Thompson in the transcript's cold open |
| $30M Amazon seller selling hummingbird sugar water | VERIFIED | Transcript: "There's a guy on Amazon that's done $30 million selling sugar as hummingbird nectar" |
| The $289 headline figure (video title / "Pattern: The $289 Budget Is Strategic") | LIKELY | The number appears in the YouTube video's own title ("I Spent $289 So AI Could Build My Business") as referenced in the attachment header of 1ec27df4...md; Thompson does not restate "$289" as a spoken figure inside the transcript body itself — the specific breakdown is not itemized on-record. Treat the $289 figure as the publisher's framing of his spend, not a line-item Thompson recites. |
| $800,000 teeth-whitening AliExpress drop-shipping business during COVID | VERIFIED | Transcript: "I sold like $800,000 of a teeth whitening product that I found on on AliExpress" |
| Conversion-rate benchmark of 3-5% as "reasonably good" | VERIFIED | Transcript: "if you're sitting between like three and five on something like this, you're in like a reasonably good space" |
| Ad spend minimum "$50-100" / "$50/day" | VERIFIED | Transcript: "I generally like minimum 50 bucks a day" |

## Gaps

- No independent (non-Thompson-sourced) verification of his business claims (100 companies, $30M competitor figure, $800K teeth-whitening run) was performed — these are UNCONFIRMED as objective facts, though VERIFIED as things Thompson said on record. Treat all revenue/scale figures as self-reported.
- The skill's existing "14 Genius Patterns" / "10 Hidden Knowledge" numbered lists in `genius.md` were already present pre-repair and match the transcript's content closely enough to be treated as a faithful paraphrase (LIKELY) of the primary source, except where this repair pass added direct verbatim quotes (now VERIFIED per rows above).
