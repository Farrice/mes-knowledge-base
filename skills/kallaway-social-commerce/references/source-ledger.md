# Source Ledger — kallaway-social-commerce

Claim-by-claim verification for every factual assertion in `SKILL.md` and `genius.md`.
Labels: **VERIFIED** (verbatim or numerically exact match found in primary source) /
**LIKELY** (concept/number confirmed, a supporting detail — name, attribution, or
framing — is either paraphrased beyond what the source states or drawn from general
knowledge, not the transcript itself) / **UNCONFIRMED** (no matching text found in any
source file read for this repair; treat as extractor synthesis, not a Kallaway quote).

## Critical Finding (read first)

`genius.md`'s citation block names the source as *"Three Biggest Social Media Shifts"
(YouTube, 2026)*. That phrase does not exist as a video title — it is Kallaway's own
in-video description of the video's content ("I'm going to walk through the three
biggest social media shifts happening right now," transcript @ 00:00:54). The actual
source material was **not** found anywhere under `extractions/kallaway/` or
`extractions/kallaway-content-system/` — those five files (`extraction-report.md`,
`internet-money-machine-extraction.md`, `internet-money-machine-transcript.txt`,
`transcript.txt`, `word-mastery-extraction.md`) were read in full and grepped for
`Manis|Instagram Shop|TikTok Shop|peak taste|permissionless|64 billion|revenue per
view|RPV|agentic commerce|dollar store` — zero matches. Those files cover a different
Kallaway topic (the "illusion of novelty" storytelling framework and an "internet money
machine" funnel breakdown), confirmed by direct file size (34,072 and 24,657 bytes
respectively — not empty, just off-topic) and content read.

The real primary source was located at
`_active/harness/codex-harvest-2026-06-11/extractions/video-context/ImzoNTrgvFg/` (a prior Codex
harvest import, not indexed under `extractions/kallaway*`):
- `transcript.txt` — full line-timestamped transcript (1,487 lines), read in full for this repair.
- `metadata.json` — confirms: title **"The NEW Way to WIN on Social Media in 2026,"**
  channel/uploader **Kallaway**, `upload_date`/`publish_date` **2026-04-29**, URL
  `https://www.youtube.com/watch?v=ImzoNTrgvFg`, duration 24:14.
- `video-context-ledger.md` / `.json`, `frame-notes.md`, `analysis.md`,
  `uncertainty-report.md` — supporting artifacts, not needed for this repair.

Every VERIFIED/LIKELY label below is anchored against `transcript.txt` at that path,
cross-checked with `metadata.json` for title/date/URL. This does not mean the original
`genius.md` content was fabricated — every checked number and framework matches the
transcript closely — but the citation pointed at the wrong location, which would have
sent a future auditor (or the adversarial verifier) to empty files. That mismatch is the
gap this ledger closes.

---

## Claim Ledger

| # | Claim (as stated in genius.md / SKILL.md) | Label | Source anchor | Note |
|---|---|---|---|---|
| 1 | Three eras: Social 1.0 (2005-2020), Interest Media 2.0 (2020-2025), Social Commerce 3.0 (2025+) | VERIFIED | transcript.txt @ 00:08:38–00:10:24 | Dates match almost exactly: "Between like 2005 and 2020, it was mostly social first... social media 1.0"; "2020... interest media... social media 2.0... 2020 to just a few months ago, 2025 early 2026"; "we are now shifting into a third era... social commerce 3.0." |
| 2 | "Whenever there's massive change, the marketing game completely resets. The rules change, the strategies change... smaller players can have huge advantages if they can adapt quickly." | VERIFIED | transcript.txt @ 00:00:15–00:00:27 | Verbatim (transcript reads "like with AI" inline; genius.md's quote drops that clause but preserves meaning). |
| 3 | TikTok Shop: $64B revenue in 2025, 2 years old | VERIFIED | transcript.txt @ 00:11:59–00:12:07 | "last year, 2025, 64 billion with a B dollars of revenue flowed through TikTok Shop globally. It's 2 years old." |
| 4 | TikTok Shop launched 2023 | VERIFIED | transcript.txt @ 00:11:33–00:11:36 | "TikTok Shop was an insane innovation when it came out in 2023." |
| 5 | Some TikTok Shop brands went $0 to $50M in 3 years | VERIFIED | transcript.txt @ 00:12:35–00:12:39 | "Some brands went from zero to 50 million in 3 years." |
| 6 | Instagram Shops: 30 products/video vs. TikTok Shop's 1 | VERIFIED | transcript.txt @ 00:12:58–00:13:01 | "TikTok Shop only let you link one video, Instagram letting creators link up to 30 products per video." |
| 7 | 2-click Apple Pay checkout | VERIFIED | transcript.txt @ 00:13:03–00:13:06 | "watch, click, tap, buy, Apple Pay, two clicks, done." |
| 8 | Instagram = "peak taste" / "apex predator"; TikTok Shop = "dollar store" execution | VERIFIED | transcript.txt @ 00:12:42–00:12:48 | "it felt a little grungy or grimy in a way... Instagram, on the other hand, is peak taste when it comes to social. It is the apex predator of this space." |
| 9 | Projected $10B+ through Instagram Shops in 2026 | VERIFIED | transcript.txt @ 00:13:08–00:13:16 | "I wouldn't be shocked for Instagram to report that over 10 billion dollars of revenue flowed through Instagram Shops just in the rest of 2026 alone." |
| 10 | Instagram Shops launched "in the last couple weeks" (relative to video date) | VERIFIED | transcript.txt @ 00:11:28–00:11:31 | Matches video publish date 2026-04-29 per metadata.json. |
| 11 | Permissionless mechanic: "you just saw the product, got a sample, ripped the video, and if the sales came in, you could monetize it" | VERIFIED | transcript.txt @ 00:11:50–00:11:53 | Verbatim match, including "no coordination, no asking for permission" clause immediately prior. |
| 12 | Meta acquired an AI agent company for $2B, integrating it into Instagram/Facebook (genius.md calls it "Manis") | **LIKELY** — name mismatch | transcript.txt @ 00:13:44–00:13:51, 00:13:56–00:13:58 | Transcript names the company **"Manifold,"** not "Manis": "Meta very quietly acquired a company called Manifold for $2 billion... Manifold is an AI agent platform." The $2B figure, the quiet-acquisition framing, and the Instagram/Facebook integration are all VERIFIED verbatim — only the company name is off. Likely a mishearing/mistranscription carried forward from the original (pre-existing) extraction, not introduced by this repair. Flagging rather than silently editing genius.md per repair-boundary rules — a future pass should correct "Manis" → "Manifold" throughout `genius.md` and `SKILL.md`. |
| 13 | Agentic commerce use cases: analytics attribution, auto-DM selling, automated outreach | VERIFIED | transcript.txt @ 00:14:21–00:14:32 | "better analytic attribution... auto DM agentic selling... automatic outreach via DM." |
| 14 | "Already live for Meta Ads; organic deployment in 6-12 months" | VERIFIED | transcript.txt @ 00:14:44–00:14:56, 00:14:57–00:15:00 | "Meta already launched their Manifold agent for Meta Ads" (paid, live today); "this whole category of agentic social commerce is going to be a big, big wave... coming over the next 6 to 12 months" (organic, forward-looking). |
| 15 | Production cost collapse → 100-10,000x more creator-led brands | VERIFIED | transcript.txt @ 00:15:58–00:16:02 | "you're going to see 100x to 10,000x more creator-led brands." |
| 16 | AI visual recognition shopping: click-to-buy on untagged products, "final boss of affiliate marketing," 12-month horizon | VERIFIED | transcript.txt @ 00:17:07–00:17:12, 00:17:22 | "this kind of thing is the final boss of affiliate marketing. Completely democratized affiliate marketing"; "I think we're going to be there in 12-ish months." |
| 17 | Average creator: $30-50K/yr; projected $300-500K/yr in 1-2 years | VERIFIED | transcript.txt @ 00:17:38–00:17:51 | "the average creator makes 30 to 50k per year... that same skill set is going to be worth 3 to 500k per year in just 1 to 2 more years." |
| 18 | Top-line prediction: distribution-fluent operators earning $500K-$1M/yr | VERIFIED | transcript.txt @ 00:10:59–00:11:02 | "I predict we will see a lot of people start making 500k to a million a year relatively easily just off the back of knowing this skill." (Distinct claim from #17 — both independently verified.) |
| 19 | White-collar retraining prediction (AI layoffs → distribution-skill retraining) | VERIFIED | transcript.txt @ 00:11:06–00:11:20 | "as a lot of smart white-collar people get laid off as companies adopt AI, there will be a great retraining towards this distribution bucket." |
| 20 | "Every business is technically a media company" | VERIFIED | transcript.txt @ 00:18:03–00:18:09 | Verbatim: "every business is going to have to have a content person. Every business is technically a media company, and most people are going to want to learn these skills." |
| 21 | Three-role architecture: Brand Owner / Content Creator / Facilitator | VERIFIED | transcript.txt @ 00:13:26–00:13:33 | "you could win as a brand owner supplying products on there, as a creator making the content, or as a third-party helping to facilitate that relationship." ("Facilitator" is the extractor's label for "third-party" — same concept, paraphrased term.) |
| 22 | "Don't mix roles until you've mastered one" | **UNCONFIRMED** | — | Not found anywhere in transcript.txt. Kallaway states the three roles exist; he does not say not to mix them, or to master one before another. This appears to be extractor-added strategic advice, plausible but not a Kallaway statement — do not present it as a direct quote or attribute the "don't mix roles" rule to him specifically. |
| 23 | Creator brand economics table (10-30% affiliate commission vs. 60-90% owned-brand margin, capital/ops/brand-equity comparison) | **UNCONFIRMED** | — | Not stated in transcript.txt in this structured form. Kallaway discusses the capital/ops shift qualitatively ("capital needed to start businesses... is going down to zero," "agentic workflows can help augment" ops — both individually VERIFIED, see #15 area) but the specific percentage ranges (10-30%, 60-90%) are not in the source. Treat as a reasonable extractor estimate, not a Kallaway-stated figure. |
| 24 | Creator brand examples: Feastables, Prime, Chamberlain Coffee, Happy Dad (NELK), Sour Strips | VERIFIED (brand list) / **LIKELY** (parenthetical attributions) | transcript.txt @ 00:09:52–00:10:01 | Brand list is a verbatim match: "things like Feastables, Prime, Chamberlain Coffee, Happy Dad from Nelk, Sour Strips." The parenthetical founder attributions in genius.md — "(MrBeast)" for Feastables, "(KSI/Logan Paul)" for Prime — are **not stated by Kallaway in this video** and were not independently re-verified in this repair pass (they are widely known public facts, but that is a claim about general knowledge, not this source). Label them LIKELY, not VERIFIED against this transcript. |
| 25 | Storytelling era: chasing trends / overstimulating editing "worked in the previous era" but is losing to premium narrative | VERIFIED | transcript.txt @ 00:19:11–00:19:34 | Close paraphrase of a real passage; see Anti-Patterns section in genius.md for the exact quote and timestamp. |
| 26 | Alex Garcia (referenced storytelling producer) and the "fast cuts/crazy editing... not really working anymore" critique | VERIFIED | transcript.txt @ 00:20:13–00:20:34 | "My friend Alex Garcia... he's the goat... what he's been saying is that the old playbook of like fast cuts and crazy editing and all this like text on screen, that's not really working anymore." |
| 27 | Five storytelling pillars: Characters, Pacing, Narrative Arcs, World Building, Tension | VERIFIED | transcript.txt @ 00:21:52–00:21:58 | "Characters, pacing, narrative arcs, world building, and then tension." (Referenced in `genius.md`'s domain framing but not a "Genius Pattern" in this skill — noted here for completeness since it's the same source.) |
| 28 | Quality Rubric table, Signature Moves list, workflow tier structure | N/A — not a provenance claim | — | This is original skill-authoring synthesis (standard practice for every skill in the roster), not a factual assertion about Kallaway or an attributed quote. No VERIFIED/LIKELY/UNCONFIRMED label applies; flagged here only so a reviewer doesn't mistake its absence from the table above for an oversight. |

---

## Files Read For This Verification Pass (with sizes, confirming none were silently assumed empty)

| File | Size | Result |
|---|---|---|
| `extractions/kallaway/extraction-report.md` | 6,971 bytes | Read in full — different topic (novelty/storytelling extraction summary). |
| `extractions/kallaway/internet-money-machine-extraction.md` | 12,864 bytes | Read in full — different topic (funnel/offer breakdown). |
| `extractions/kallaway/internet-money-machine-transcript.txt` | 24,657 bytes | Grepped for social-commerce terms — zero matches. |
| `extractions/kallaway/word-mastery-extraction.md` | 16,292 bytes | Read in full — different topic (copywriting/word choice). |
| `extractions/kallaway/transcript.txt` | 34,072 bytes | Read (head) + grepped — "illusion of novelty" storytelling transcript, zero social-commerce matches. |
| `extractions/kallaway-content-system/*` (4 files incl. 398,725-byte .vtt) | — | Grepped for social-commerce terms — zero matches; this is the "content system / 10x batch" extraction, a different Kallaway skill (`kallaway-content-system`). |
| `_active/harness/codex-harvest-2026-06-11/extractions/video-context/ImzoNTrgvFg/transcript.txt` | 1,487 lines | **Read in full — this is the actual primary source for `kallaway-social-commerce`.** |
| `_active/harness/codex-harvest-2026-06-11/extractions/video-context/ImzoNTrgvFg/metadata.json` | — | Read in full — confirms title, channel, publish date, URL. |
| `_active/harness/codex-harvest-2026-06-11/brain/e51c78e9-.../artifacts/kallaway-expansion-vision.md` | — | Read (excerpt) — the original extraction vision doc that produced this skill; corroborates the four-tailwind framing and confirms "Manis" should read "Manifold" (this doc also uses "Manis," so the error predates this repair and traces to the original extraction). |
