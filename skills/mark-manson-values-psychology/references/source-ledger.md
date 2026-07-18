# Source Ledger — Mark Manson Values Psychology

Claim-by-claim provenance for the factual/quoted claims in `SKILL.md` and `genius.md` (Genius Patterns, Hidden Knowledge, and the new Anti-Patterns / Model Calibration sections added in this repair, 2026-07-18). Ground truth = raw Merlin-AI video transcripts pasted into two claude.ai conversations during the 2026-07-01 export harvest, extracted from `_archive/claude-export-2026-07-01.tar.gz` for this repair. Local copies of the exact conversation files used are preserved at `raw-sources/*.md` in this repair's output directory so quotes can be checked without re-opening the 332MB tarball.

## Sources Consulted

| Source | Type | Size (`wc -c`) | Status |
|--------|------|------|--------|
| `raw-sources/2a2e8433-feda-477c-ae37-e4f1c49a1f5f.md` — "PT.01-FC/VP-Mark Manson: How to Find and Live by Your Values" (tarball member `claude-export/normalized/conversations/2a2e8433-feda-477c-ae37-e4f1c49a1f5f.md`) | Primary — Merlin-AI transcript of Manson's Solved Podcast episode "How to Find and Live by Your Values" (youtube.com/watch?v=uvXdMPNhp9M), pasted verbatim into a claude.ai conversation dated 2025-07-18 | 298,555 bytes | VERIFIED (extracted from tarball via `tarfile`, read in full, non-empty) |
| `raw-sources/5c9b1db0-a6dc-401d-9ea9-dc2a2dc1f3a9.md` — "SVP-Mark Manson: Your Happiness, Solved Part 1" (tarball member `claude-export/normalized/conversations/5c9b1db0-a6dc-401d-9ea9-dc2a2dc1f3a9.md`) | Primary — Merlin-AI transcript of "Your Happiness, Solved" (youtube.com/watch?v=Wk5jLJcrrM0), dated 2025-08-01 | 260,414 bytes | VERIFIED |
| `raw-sources/61aa7f40-9624-4799-9524-b551f81002c7.md` — "SVP-Mark Manson: Your Happiness, Solved Part 2" (tarball member `claude-export/normalized/conversations/61aa7f40-9624-4799-9524-b551f81002c7.md`) | Primary — continuation of the same episode (chat-limit split), dated 2025-08-01; opens by re-pasting Part 1's full text | 59,064 bytes | VERIFIED |
| `raw-sources/b425a61a-5930-42c5-870a-9ffaaa810c19.md` — "11-8-25 Mark Manson: 7 AI Prompts That Can Change Your Life" (tarball member `claude-export/normalized/conversations/b425a61a-5930-42c5-870a-9ffaaa810c19.md`) | Primary — separate Manson video transcript, dated 2025-11-09 | 37,873 bytes | VERIFIED |
| `agents/mark-manson/memory/context.md` | Derived — agent provenance note naming the same two source episodes | 431 bytes (approx.) | VERIFIED (read in full) |
| Milton Rokeach's self-confrontation research (civil-rights era) | External scholarly claim, Manson's own retelling | N/A | VERIFIED as a claim-in-transcript (see below); the underlying 1960s Rokeach study itself was not independently re-verified against a primary psych-literature source in this repair — the anchor is Manson's retelling, not the original study |

Note on transcript fidelity: these are ASR (speech-to-text, Merlin AI) outputs and contain transcription artifacts — e.g. "Milton Roich" for Milton **Rokeach**, "Scholom Schwarz" / "Shalom Schwarz" for Shalom **Schwartz**, "Droski"/"Drowski" for Kazimierz **Dąbrowski**, "hydonic"/"hidonia" for **hedonic**/hedonia, "udemonia"/"udeimmonia" for **eudaimonia**, "John Height"/"Hype" for Jonathan **Haidt**, "Nikomakian ethics" for **Nicomachean** Ethics. Quotes reproduced in `genius.md` are cleaned to standard spelling for readability where the mis-transcription is a proper noun already named correctly elsewhere in the skill; profanity is bleeped in the transcript source itself ("[ __ ]") and rendered as "[bleep]" in genius.md quotes — this is not an edit to Manson's meaning, only to the pre-bleeped ASR output.

## Claims — Genius Patterns (existing, pre-repair)

| Claim | Label | Anchor |
|-------|-------|--------|
| Values theory built on Schwartz value theory (trans-situational, ranked strategies) | VERIFIED | `2a2e8433...md` line 230: "the godfather of it is a[n] Israeli researcher named Scholom Schwarz... He's the originator of pretty much all the major value surveys" |
| Six markers of a true value (emotion, motivates action, trans-situational, moral yardstick, ranked, trade-offs) | VERIFIED | `2a2e8433...md` lines 232-244: "there are really six key characteristics of a value... the first one is that they're linked with emotion..." |
| The Sacrifice Test ("your values are what you're willing to give up") | VERIFIED | `2a2e8433...md` lines 636, 875-913: "the more you sacrifice for anything in your life... you are going to sacrifice a lot of other [things]" |
| Desert Island visualization | VERIFIED | `2a2e8433...md` lines 2869-2929 (full quote, see genius.md pattern) |
| Eulogy Filter, incl. "he gave more than he took" | VERIFIED | `2a2e8433...md` lines 2927-2940 |
| Frustration Forensics (incompetence → mastery) | VERIFIED | `2a2e8433...md` lines 3005-3013 |
| Gut-First Forced Ranking (honesty vs. competence gun-to-head) | VERIFIED | `2a2e8433...md` lines 3070-3128 |
| Behavior-first value change / cognitive dissonance | LIKELY | General framing consistent with the podcast's discussion of action-before-belief across the transcript; no single verbatim "act the value, feelings follow" sentence located at one timestamp — synthesized across the episode's back half. Not re-verified as one exact quote in this repair. |
| Three-Layer Happiness Stack (affect / life satisfaction / meaning-purpose) | VERIFIED | `5c9b1db0...md` lines 946-969, 1092-1135 |
| Self-Confrontation (Rokeach, civil-rights era) | VERIFIED | `2a2e8433...md` lines 4139-4172: "the researcher who came up with instrumental and terminal values, Milton Roich [Rokeach]... he took people from both sides... during the civil rights era in the late 60s" |
| Value Vacuum / post-traumatic growth / Dabrowski's positive disintegration | VERIFIED | `2a2e8433...md` lines 3444-3477 (PTG framing), 3630-3664 ("Droski... called this positive disintegration... he did all of this work in the 1950s") |
| Aspirational at the margins / volume knobs (achievement 10→9, community 4→6) | VERIFIED | `2a2e8433...md` lines 3130-3178 (specifically "bring the volume knob down from 10 to a nine and then dial the community up from like a four to a six") |
| Instrumental Masquerade (golf/Tiger Woods) | VERIFIED | `2a2e8433...md` lines 3197-3260 (full story) |
| Aristotle's golden mean / 17 virtues in Nicomachean Ethics | VERIFIED | `2a2e8433...md` lines 1213-1235: "I counted 17 [virtues] and the Nikomakian ethics... he defined a virtue... as a golden mean between two vices" |

## Claims — This Repair's Additions (2026-07-18)

| Addition | Label | Anchor |
|-------|-------|--------|
| Model Calibration section: honesty-vs-competence gut/rider example | VERIFIED | `2a2e8433...md` lines 3070-3090 (147:15-147:24) |
| Anti-pattern: steak/chicken preference-vs-value | VERIFIED | `2a2e8433...md` line 374 (17:11-17:22) |
| Anti-pattern: distrust of value surveys | VERIFIED | `2a2e8433...md` lines 792-794 (36:32-36:44) |
| Anti-pattern: rider/elephant post-hoc justification, Haidt's *The Righteous Mind* (2012) | VERIFIED | `2a2e8433...md` lines 2500-2517 (book + year), 3075-3090 (self-catch quote) |
| Anti-pattern: golf/Tiger Woods instrumental grind | VERIFIED | `2a2e8433...md` lines 3197-3249 |
| Anti-pattern: happiness stack worked backwards | VERIFIED | `5c9b1db0...md` lines 1120-1135 (49:38-50:07) |
| Anti-pattern: eulogy exercise producing a status/validation answer (golf-swing bit) | VERIFIED | `2a2e8433...md` lines 2972-3005 (142:10-143:14) |
| Desert Island section enrichment quote | VERIFIED | `2a2e8433...md` lines 2919-2925 (139:19-139:34) |
| Frustration Forensics section enrichment quote | VERIFIED | `2a2e8433...md` lines 3005-3013 (143:21-143:53) |
| Three-Layer Happiness Stack section enrichment quote | VERIFIED | `5c9b1db0...md` lines 1112-1128 (49:20-50:07) |

## Labeling Key

- **VERIFIED** — quote or fact located verbatim (or with only ASR-spelling variance) in a primary source file extracted and read during this repair.
- **LIKELY** — consistent with the source material and the episode's overall argument, but not independently pinned to one exact verbatim sentence in this repair pass.
- **UNCONFIRMED** — not used in this repair; every claim touched had a locatable transcript anchor. If a future pass adds a claim without one, it must be labeled UNCONFIRMED here, not silently anchored.
