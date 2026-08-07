# Source Ledger — Tim Danilov: Niche Bending

Claim-by-claim provenance for `genius.md` and `SKILL.md`. Labels: **VERIFIED**
(quote/claim confirmed against a primary source file, byte-checked), **LIKELY**
(consistent synthesis derived from a verified source but not a direct quote),
**UNCONFIRMED** (not found in any source file — flagged, never anchored as fact).

## Primary Sources Consulted

| # | Source | Path | Size | Status |
|---|--------|------|------|--------|
| 1 | Video transcript (plain text) | `extractions/niche-bending/transcript.txt` | 11,053 bytes (`wc -c`) | VERIFIED — read in full |
| 2 | Video transcript (duplicate copy) | `extractions/transcripts/fLDrB_wmbNE.txt` | 11,053 bytes (`wc -c`) | VERIFIED — identical byte count to #1, same content |
| 3 | Mastery extraction report | `extractions/niche-bending/extraction-report.md` | 18,269 bytes (`wc -c`) | VERIFIED — read in full, cross-checked against transcript |
| 4 | Video metadata | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/fLDrB_wmbNE/metadata.json` | 1,654 bytes (`wc -c`) | VERIFIED — read in full |
| 5 | Video context ledger (timestamped transcript) | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/fLDrB_wmbNE/video-context-ledger.md` | 78,900 bytes (`wc -c`) | VERIFIED — spot-checked, confirms transcript.txt content with timestamps |

**Canonical source video**: "​The NEW YouTube Strategy Dominating in 2026" — vidIQ (YouTube channel), video ID `fLDrB_wmbNE`, published 2026-02-16 (per `metadata.json` `upload_date`/`publish_date`: `20260216`), duration 11:04, URL `https://www.youtube.com/watch?v=fLDrB_wmbNE`. Featured guest: Tim Danilov (`@timdanilovhi`).

## Search Discipline Followed

Searched `extractions/` for the fragment `danilov` (no apostrophes/punctuation) per source-search discipline. Found `extractions/niche-bending/` directly — no need to fall back to the `_archive/claude-export-2026-07-01.tar.gz` per-member scan, since primary transcript + extraction report + timestamped video-context ledger were all present and readable on disk with confirmed non-zero byte sizes (`wc -c`, not `wc -l`).

## Claim-by-Claim Verification

### Genius Patterns (genius.md, items 1-8)

| Claim | Status | Note |
|---|---|---|
| Format-Market Decomposition (niche = market × format, not topic) | VERIFIED | Direct quote in transcript: "essentially your niche is the combination of the format and the market" |
| The Empty Square Method (grid mapping) | VERIFIED | Transcript: "when you do see an empty square on that map, this isn't due to a lack of interest. It's an opportunity. It is blue ocean." |
| Viral Format Transplantation | VERIFIED | Transcript: NFL Stories → Minecraft → spirituality "my matrix" example, same title structure, three markets |
| Language Adoption (Borrowed Fluency) — Tazoo gaming vocabulary | VERIFIED | Transcript: "current meta," "nerfed," "OP African builds," "patch update" all direct quotes from Tazoo clip |
| Audience Bridge Architecture | VERIFIED | Transcript: "Tazoo is speaking to an entirely new audience who might never watch a traditional nature documentary" |
| The Expertise Constraint | VERIFIED | Transcript: "Do not bend a format you cannot deliver the expertise in... if you are a dentist, use the gaming tier list to rank toothpaste... don't try to use a finance format if you don't understand money" |
| Outlier-Driven Format Scouting | VERIFIED | Transcript: 75,000 views / "three and a half times more views than typical," "100 times outlier," VidIQ AI-coach demo surfacing a Vegas-casino outlier |
| Saturation Arbitrage | VERIFIED | Transcript: nature documentaries described as "traditional... slow and boring," Tazoo "take a saturated market... and made it feel brand new" (extraction-report §8, consistent framing) |

### Hidden Knowledge (genius.md, items 1-6)

| Claim | Status | Note |
|---|---|---|
| Markets Are Fixed; Formats Are Infinite | VERIFIED | Transcript: "these [markets] rarely ever change. You can't really invent a new market... there are thousands of new formats every single day" |
| Virality Is Format-Native, Not Market-Native | LIKELY | Synthesized interpretation in extraction-report §2; not a direct Danilov quote but a fair reading of the NFL→Minecraft→spirituality triple-market example |
| The Trojan Horse Principle | VERIFIED (concept) / interpretive label | Transcript: "he's tricked them into learning something." The phrase "Trojan Horse" itself is the extraction's naming for this mechanic, not Danilov's own term — mechanic is VERIFIED, the label is an analytical framing |
| Empty Squares Are Demand Signals, Not Gaps | VERIFIED | Transcript: "this isn't due to a lack of interest. It's an opportunity" |
| Small Channels Are Format Laboratories | VERIFIED | Transcript: Finn's Play (3,500 subscribers, 2.7M-view outlier), VidIQ prompt explicitly targets "small channels that are getting unusually high views" |
| Visual Language Transfer | VERIFIED | Transcript: "thumbnails have S tier rankings, health bars, and knockout screens" on a biology channel |

### Case Studies / Named Examples

| Claim | Status | Note |
|---|---|---|
| Danilov's own results: 0→$56K/mo in 30 days; 0→150M views; 0→$23K in <90 days | VERIFIED (source-claim) | Stated verbatim by the narrator in the source video. This is the video's own marketing claim about Danilov — confirmed present in the source, not independently audited against third-party channel analytics |
| Tazoo "Current Meta of African Savannah Predators (Patch 2.1 Update)" title | LIKELY | Genius.md's exact title/thumbnail description ("Tier S badge") is a constructed composite consistent with transcript details (tier rankings, health bars, "current meta," sloth/human "patch" narration) but the transcript never states this exact video title verbatim — treat the mechanic as VERIFIED, the specific title string as LIKELY |
| NFL Stories → Rafa (Minecraft) → "my matrix" (spirituality) chain | VERIFIED | Transcript: "This video will change the way you see Patrick Mahomes forever," 75,000 views; Minecraft version "4 days later"; spirituality "100 times outlier" |
| Finn's Play "POV You're an NPC in Vice City" (2.7M views, 3,500 subs) | VERIFIED | Transcript, exact numbers match |
| "The Life of a Minecraft Wolf" (1.7M views) | VERIFIED | Transcript, exact numbers match |
| Spider-Man NPC POV video (quarter-million views) | VERIFIED | Transcript: "over a quarter of a million views, the highest performing video on their channel so far" |
| Vegas-casino VidIQ AI-coach demo ("Which casino dies first?", ~1M views) | VERIFIED | Transcript: "five Vegas casinos that will close next... nearly a million longorn [long-form] views on a 20 minute video" |
| "Unboxing Your First Roth IRA: What's Inside?" Series (Hall of Fame Exemplar) | **UNCONFIRMED** | Not present anywhere in transcript, extraction-report, or video-context ledger. This is a constructed illustrative example added during genius.md authoring to demonstrate the pattern in an unaddressed market (personal finance + unboxing). It is NOT a real Danilov or vidIQ case study — flagged in `genius.md` with a provenance note pointing here. The *mechanic* it illustrates (format transplantation into a dry/regulated market) is VERIFIED elsewhere; this specific title/series is not |
| "A Comprehensive Guide to Investing for Beginners" (Anti-Exemplar) | **UNCONFIRMED** | Generic constructed anti-example, not a specific real channel or video from the source material. Used only as an illustrative contrast — flagged in `genius.md` |

### Structural / Authored Content (not source quotes)

| Claim | Status | Note |
|---|---|---|
| Expert-Specific Quality Rubric (4/7/10 anchors table) | LIKELY | Standard extraction-methodology output — operationalizes the VERIFIED patterns above into a scoring rubric. Not a Danilov quote; authored to house style |
| "How to Use This Skill (Model Calibration)" section (added in this repair pass) | LIKELY | Authored guidance modeled on the verified Expertise Constraint / Language Adoption patterns above (esp. the "cosmetic bending" warning, directly derived from the VERIFIED "Do not bend a format you cannot deliver the expertise in" quote) |
| Anti-Patterns (Sourced) section (added in this repair pass) | VERIFIED | Each of the 6 items anchors to a verbatim transcript quote — see quotes inline in `genius.md`, all confirmed present in `extractions/niche-bending/transcript.txt` |
| Recognition Test section (added in this repair pass) | LIKELY | Authored validation gate built on the VERIFIED market/format/expertise/outlier framework; not itself a Danilov quote |

### SKILL.md

| Claim | Status | Note |
|---|---|---|
| "Extracted from a VidIQ deep-dive into his methodology" | VERIFIED | Matches `metadata.json` uploader "vidIQ" and title "The NEW YouTube Strategy Dominating in 2026" |
| Version/workflow count metadata | VERIFIED | Matches actual file count in `skills/tim-danilov-niche-bending/workflows/` (4 files) |
