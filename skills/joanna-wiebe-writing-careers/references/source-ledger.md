# Source Ledger — joanna-wiebe-writing-careers

> Claim-by-claim provenance for the Wave 3 Lane 4 repair (2026-07-17/18). Ground
> truth = `extractions/joanna-wiebe/` (repo root) + verbatim quotes already inside
> the skill's own files. Labels: VERIFIED (quote/claim found verbatim or as direct
> paraphrase in a source file, file+line cited) / LIKELY (consistent with sourced
> material but not verbatim-matched) / UNCONFIRMED (no primary source file exists;
> the only anchor is the skill's own prior provenance trail).

## Files consulted
- `extractions/joanna-wiebe/writing-career-monetization-extraction.md` (12,986 bytes, `wc -c`) — primary ground truth for this skill (writer career monetization domain). Read in full.
- `extractions/joanna-wiebe/transcript.txt` (15,223 bytes) — read in full; confirmed this is the raw transcript for the **9 Psychological Writing Triggers** video, not "7 Proven Ways To Make Money As A Writer in 2026" (this skill's cited source). No raw transcript file for the writing-careers source video exists in the repo.
- `extractions/joanna-wiebe/authority-craft-extraction.md` (11,353 bytes) and `extractions/joanna-wiebe/9-psychological-writing-triggers-extraction.md` (10,849 bytes) — read for domain-boundary check only. Both are explicitly scoped to `joanna-wiebe-persuasion-mastery` (sentence-level/funnel-trigger craft), not this skill. Not used as sources for writing-careers claims — out of scope per the sibling-skill boundary.
- `skills/joanna-wiebe-writing-careers/genius.md` (pre-repair, 245 lines) — read in full; several Hidden Knowledge items (Brand Voice Consistency Test, Science-First Creative Process, Book as Authority Shortcut, Story Structure Detection Skill, Dual Skill Couple) do not appear in any extraction file and could not be traced to a primary source. These were pre-existing content, left untouched (additive-first boundary), but not cited as sourced in any new anchor added by this repair.

## New Anti-Patterns section — claim-by-claim

| # | Claim | Label | Anchor |
|---|---|---|---|
| 1 | "Position yourself as a consultant, never as a freelancer." | VERIFIED | `writing-career-monetization-extraction.md`, Hidden Knowledge #1, line 76 |
| 2 | "emphasize measurable outcomes, not post count" | VERIFIED | `writing-career-monetization-extraction.md`, 24-Hour Quickstart, line 142 |
| 3 | "Newsletters are relationship building machines at scale" / "blogging with email" | VERIFIED | `writing-career-monetization-extraction.md`, Hidden Knowledge #4, line 85 |
| 4 | Manuscript-and-leave vs. bundling adjacent services (book launch PR, Amazon ads, profile optimization) | VERIFIED | `writing-career-monetization-extraction.md`, Genius Pattern 7, lines 65-66 |
| 5 | "neutral is invisible" (bottled-water label study, Liquid Death) | UNCONFIRMED | No raw transcript for "This Is Why You DON'T Need Original Ideas" exists in `extractions/joanna-wiebe/`. Anchor is `genius.md`'s own 2026-07-01 dated section, not a primary source. Underlying claim treated as LIKELY, not VERIFIED. |
| 6 | "Companies that might devalue writing will still pay six figures for messaging strategy or brand consulting" | UNCONFIRMED | Business logic (reframing captures a different price point) is VERIFIED against Executive Summary + Genius Pattern 4 (lines 20-22, 47-51). This exact sentence does not appear verbatim in any extraction file — flagged as an UNCONFIRMED paraphrase. |

## Other entity-floor additions
| Addition | Label | Anchor |
|---|---|---|
| "7 Proven Ways To Make Money As A Writer in 2026," ~13-min, 2,222-word transcript | VERIFIED | `writing-career-monetization-extraction.md`, Content Assessment block, line 6 |
| "outperform those who don't by orders of magnitude" (Awareness Stage Navigation) | VERIFIED | `writing-career-monetization-extraction.md`, Hidden Knowledge #2, line 79 |

## Recognition-test and Model Calibration language
New (not a factual claim requiring a source label) — modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7-16, written fresh for Joanna Wiebe's actual patterns (consultant framing, plumbing/clog metaphor, outcome-mechanism honesty). No provenance risk.
