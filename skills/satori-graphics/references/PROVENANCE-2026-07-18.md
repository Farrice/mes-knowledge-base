# PROVENANCE — satori-graphics repair (Wave 3 Lane 4 Batch 15)

Anchor → source file + location. All quotes are reused from material already inside the shipped skill/extraction tree (`extractions/satori-graphics/` and `skills/satori-graphics/references/source-quotes.md`) — no new source material was consulted or invented.

## Anti-Patterns section (genius.md, items 1–16)

| # | Anchor quote (truncated) | Source file | Location | Confidence |
|---|---|---|---|---|
| 1 | "throwing confetti at a layout..." | `references/source-quotes.md` | "On Why-Before-What" | LIKELY (no raw v1 Video 2 transcript survives) |
| 2 | "Things like shields, arrows, mountains..." | `references/source-quotes.md` | "Verb-Not-Noun" | LIKELY (Video 3, no raw transcript) |
| 3 | "The logo is just one part of a much bigger brand system." | `references/source-quotes.md` | "Logo as Memory Hook" | LIKELY (Video 3, no raw transcript) |
| 4 | "AI can give you the clean version every time..." | `references/source-quotes.md` | "On Anti-AI-Slop" | LIKELY (Video 1, no raw transcript) |
| 5 | "Speed is useful, obviously..." | `extractions/satori-graphics/transcript.txt` | Video 4 | VERIFIED (exact substring match) |
| 6 | "more layers, more effects, or more details..." | `extractions/satori-graphics/transcript.txt` | Video 4 | VERIFIED (exact substring match) |
| 7 | "already convinced, already interested..." | `references/source-quotes.md`; also `.../vid5-transcript.txt` | "On Predictive Empathy" / v2 Video 5 | VERIFIED (recurring line, confirmed in vid5) |
| 8 | "The meaning should come way, way before the aesthetic..." | `references/source-quotes.md` | "On Why-Before-What" | LIKELY (Video 2, no raw transcript) |
| 9 | "the exact same layout and structure..." | `references/source-quotes.md` | "Presentation Standardization" | LIKELY (Video 3, no raw transcript) |
| 10 | "That comfort is where most designers stop improving." | `extractions/satori-graphics/transcript.txt` | Video 4 | VERIFIED (exact substring match) |
| 11 | "Apple starts with a communication problem first..." | `.../expansion-2026-07-04/vid1-transcript.txt` | v2 Video 1 | VERIFIED (exact substring match) |
| 12 | "what this color is trying to achieve." | `.../expansion-2026-07-04/vid3-transcript.txt` | v2 Video 3 | VERIFIED (exact substring match) |
| 13 | "understanding a specific audience deeply enough to speak their language." | `.../expansion-2026-07-04/vid4-transcript.txt` | v2 Video 4 | VERIFIED (exact substring match) |
| 14 | "Information tells people what to think..." | `.../expansion-2026-07-04/vid4-transcript.txt` | v2 Video 4 | VERIFIED (exact substring match) |
| 15 | "Aesthetics are subjective, but confusion isn't..." | `.../expansion-2026-07-04/vid5-transcript.txt` | v2 Video 5 | VERIFIED (exact substring match) |
| 16 | "little to no money at disposal." | `.../expansion-2026-07-04/vid1-transcript.txt` | v2 Video 1 | VERIFIED (exact substring match) |

## Named-entity-floor injections (17 zero-entity sections repaired)

| Section | Anchor quote added | Source | Confidence |
|---|---|---|---|
| ## The Underlying Belief | "The meaning should come way, way before the aesthetic..." | `references/source-quotes.md` "On Why-Before-What" | LIKELY |
| GP-09 | "the design is already guided in the right direction from the very beginning." | `references/source-quotes.md` "Concept-Direction-First" | LIKELY |
| HK-01 | "hire actual human designers do so for their thinking..." | `references/source-quotes.md` "On Anti-AI-Slop" | LIKELY |
| HK-04 | "exact same layout and structure..." | `references/source-quotes.md` "Presentation Standardization" | LIKELY |
| HK-05 | "difference between good friction and bad friction." | `references/source-quotes.md` "Friction & Flow" | LIKELY |
| HK-07 | "Speed is useful, obviously..." | `extractions/satori-graphics/transcript.txt` Video 4 | VERIFIED |
| HK-08 | "evaporated from your memory." | `.../expansion-2026-07-04/vid5-transcript.txt` | VERIFIED |
| HK-10 | "unimportant things quieter or just completely disappeared." | `.../expansion-2026-07-04/vid1-transcript.txt` | VERIFIED |
| HK-11 | "understanding a specific audience deeply enough..." | `.../expansion-2026-07-04/vid4-transcript.txt` | VERIFIED |
| HK-12 | "ushered along by hierarchy, by contrast, placement..." | `.../expansion-2026-07-04/vid3-transcript.txt` | VERIFIED |
| HOF-02 | "transformed into a metaphor. Music becomes emotion..." | `.../expansion-2026-07-04/vid5-transcript.txt` | VERIFIED |
| HOF-03 | "body-shaped absence. It instantly triggers a psychological reaction..." | `.../expansion-2026-07-04/vid5-transcript.txt` | VERIFIED |
| HOF-04 | "The Nike swoosh or the Apple logo..." (illustrative reuse of GP-10's quote, not an exact-example quote — labeled as such) | `references/source-quotes.md` "Logo as Memory Hook" | LIKELY |
| HOF-06 | "ask yourself what the real problem is. What's the consequence?..." | `.../expansion-2026-07-04/vid4-transcript.txt` | VERIFIED |
| HOF-07 | "taking one strong idea and pushing it further than everybody else would." | `.../expansion-2026-07-04/vid4-transcript.txt` | VERIFIED |
| HOF-10 | "noticing tiny details that everybody else just overlooks." | `.../expansion-2026-07-04/vid4-transcript.txt` | VERIFIED |
| ## When NOT to Use Satori Tools | "10,652 words" / "~7,800 words" scope note | `extractions/satori-graphics/extraction-report.md` (header) + `genius.md` own header (lines 7-8, pre-existing) | VERIFIED (word counts already stated in the shipped skill) |

## Recognition-test language (genius.md, new "## How to Use This Skill (Model Calibration)" section)

Not a sourced claim about Satori's material — this is repair-worker-authored calibration guidance (per ENVELOPE instruction, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16, written fresh for Satori's own craft texture: rent/eviction/confetti metaphors, low-vs-high-level-designer contrast, audience-first framing). Contains the literal phrase "recognize this as" required by the `recognition_test` heartbeat check.

## Absence-claim verification (per ENVELOPE rule 2)

Before writing the "known gap" note in `references/source-ledger.md`, I confirmed absence by direct action, not assumption:
1. `ls extractions/ | grep -i satori` → one directory: `extractions/satori-graphics/`.
2. `find extractions/satori-graphics -type f` → 7 files (`extraction-report.md`, `transcript.txt`, 5× `expansion-2026-07-04/vidN-transcript.txt`). All confirmed non-empty via `wc -c` (sizes 7,505–20,288 bytes — see source-ledger.md table).
3. `transcript.txt` word count (1,853, via `wc -w`) matches extraction-report.md's stated Video-4 word count exactly — confirms it is Video 4 only, not all 4 v1 videos combined.
4. Grepped for v1-Video-2/3-specific quotes ("pay rent", "confetti", "exact same layout and structure") across every file in `extractions/satori-graphics/` — zero hits outside `extraction-report.md`'s own embedded quotes.
5. Per SOURCE-SEARCH DISCIPLINE, ran a Python `tarfile` per-member content scan of `_archive/claude-export-2026-07-01.tar.gz` (332MB) for `"dangerously creative designer"`, `"pay rent"`, `"Satori Graphics"`, `"throwing confetti"` — scanned 7,720 members (time-bounded); hits were in prior Claude Code conversation exports (this project's own past sessions discussing/building this skill), not an independent raw-transcript source. This corroborates the quotes pre-date this repair (no fabrication) without providing a stronger primary source than what `extraction-report.md`/`source-quotes.md` already carry.

Conclusion: the v1-Video-1/2/3 raw-transcript absence is real, not unread. Anchors drawing on those videos are labeled LIKELY, not VERIFIED, throughout this repair's output — never given a false VERIFIED anchor.
