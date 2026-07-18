# Source Ledger — chase-hughes-conversational-influence

Every claim/quote used in `SKILL.md`, `genius.md`, and `workflows/*.md`, labeled by
confidence. Ground truth is the single source this skill is honestly scoped to: the
Unlearn podcast appearance (Adam Lane Smith × Cal × Chase Hughes), extracted
2026-05-03. File sizes recorded with `wc -c` (bytes), not `wc -l`, per the batch
instruction that line counts can mislead on single-line transcript exports.

## Primary Source

| File | Bytes (`wc -c`) | Lines (`wc -l`) | Role |
|---|---|---|---|
| `extractions/chase-hughes/transcript.txt` | 103,949 | 1,287 | Primary transcript — Unlearn podcast |
| `extractions/chase-hughes/transcript-unlearn-podcast.txt` | 103,949 | 1,287 | Identical duplicate of the above (byte-for-byte same size; not re-verified line-by-line, treated as the same source) |
| `extractions/chase-hughes/chunks/chunk_01.txt`–`chunk_06.txt` | 20,030 / 20,022 / 20,018 / 20,020 / 20,000 / 3,850 | — | Chunked re-split of the same primary transcript (v1 chunking pass) |
| `extractions/chase-hughes/chunks-v2/chunk_01.txt`–`chunk_06.txt` | 21,376 / 20,837 / 21,077 / 21,166 / 20,456 / 20,785 | — | Chunked re-split of the same primary transcript (v2 chunking pass, larger chunks) |
| `extractions/chase-hughes/_forge-output/01-extraction-report.md` | 47,904 | — | Derived extraction-report synthesis (not independently verified against transcript line-by-line; treated as LIKELY unless a specific claim is cross-checked) |
| `extractions/chase-hughes/_forge-output/02-architecture.md` through `07-verification.md` | 8,809 / 6,328 / 5,389 / 3,202 / 5,250 / 17,292 | — | Derived forge-pipeline artifacts (architecture, workflow proposals, sub-agent roles, unlocks, verification pass) — LIKELY confidence, downstream of the transcript |

**Out of scope, confirmed present but NOT used for this skill**: `extractions/chase-hughes/transcript-modernwisdom-behaviorsuite.txt` (125,792 bytes, 0 newlines — single-line export, file reads non-empty). Per `SKILL.md`'s honest-scope note, this skill covers only the Unlearn-podcast conversational-influence techniques, not BSuite. This file belongs to the sibling skill `chase-hughes-context-engineering`, which is explicitly out of scope for this repair (batch boundary, not touched).

## Claim-by-Claim Ledger

| Claim / Quote | Location Used | Source Anchor | Label |
|---|---|---|---|
| "Anything that comes from within our own mind, we cannot resist" (core mechanic) | genius.md Core Genius, Pattern 4 | `transcript.txt:188` (verbatim) | VERIFIED |
| Two-Legos / "snap together" framing for Pattern 4 | genius.md Pattern 4 | `transcript.txt:186` (verbatim: "I bet those things snap together like two little Legos") | VERIFIED |
| "A local Austin woman was found missing today..." news-lede example | genius.md Pattern 3, `workflows/hughes-two-ideas-detector.md` example | `transcript.txt:190-191` (verbatim: "A local Austin woman found missing today. neighbors report that earlier today she was seen arguing with her boyfriend details after the break.") | VERIFIED |
| "The only two things I've ever told my kids should terrify them" + secret-keeping warning | genius.md Hidden Knowledge, Anti-Patterns | `transcript.txt:196-198` (verbatim) | VERIFIED |
| Bumper-sticker empathy drill with his daughter (Subaru, marathon sticker, Ron Jon Surf Shop), daughter's age (~9, confirmed "until they were about 9 years old" at line 112) | genius.md Exemplar 1, Pattern 1 | `transcript.txt:112-113,120,135-143` | VERIFIED |
| "I never mention David and Goliath... I'll never say David and Goliath directly" trial-consulting passage | genius.md Exemplar 2, Pattern 5, Anti-Patterns | `transcript.txt:391-398` (verbatim core lines) | VERIFIED |
| "I I never I never ever ever talk about how the story ends because your brain already knows" | genius.md Anti-Patterns, How to Use This Skill | `transcript.txt:398` (verbatim) | VERIFIED |
| Story-arc conflict diagnosis — "it's never going to be in the school hallway... it's not going to be over a brunch" | genius.md Hidden Knowledge, Anti-Patterns | `transcript.txt:416-420` | VERIFIED |
| Spielberg-ending trap — "we are deeply internally craving a Steven Spielberg ending... we don't get the Spielberg ending" | genius.md Hidden Knowledge, Anti-Patterns | `transcript.txt:421` and `transcript.txt:430` (verbatim, two separate lines in the same passage) | VERIFIED |
| ~7-12 story archetypes wired into cognition, predating language, supported by Jung/Campbell | genius.md Pattern 5 "Why it works" | Jung/Campbell attribution is the extraction's framing of Hughes's claim, not a verbatim Hughes citation of those names in this transcript excerpt reviewed — the archetype-count claim ("basic story arc types," "identical things... told from time immemorial") is confirmed around `transcript.txt` archetype passage (same block as line 391 region); the specific "7-12" count and named theorists (Jung, Campbell) are the extraction team's synthesis | LIKELY |
| "Theater Reflex" — mentally tagging news/media as theater, took a year of deliberate practice | genius.md Hidden Knowledge | Not independently re-located verbatim in the 1,287-line transcript during this repair pass; consistent with the extraction report's characterization but not re-verified against a specific line number | LIKELY |
| "Special vs Important" distinction (identity-inflated vs contribution-anchored) | genius.md Hidden Knowledge | Not independently re-located verbatim during this repair pass; carried forward from the existing (pre-repair) genius.md content, which predates this batch | UNCONFIRMED — no specific transcript line was re-verified for this exact phrasing during this repair; flagged for a future pass rather than deleted, since it was already shipped content, not newly authored here |
| Psychedelic healing of Hughes's own temporal-lobe seizures, attributed to perspective-shift | genius.md Pattern 2 "Why it works" | Not independently re-located verbatim during this repair pass; carried forward from existing genius.md | UNCONFIRMED — same caveat as above |
| Extraction word count ("20,103 words") and extraction date (2026-05-03) | SKILL.md / genius.md frontmatter | `extractions/chase-hughes/_forge-output/01-extraction-report.md` (word count is a derived metric, not independently recounted in this repair pass) | LIKELY |
| Workflow file existence and structure (6 workflows, Output Format sections) | SKILL.md Workflow Table | Direct file read of `skills/chase-hughes-conversational-influence/workflows/*.md` during this repair pass | VERIFIED |

## Notes on This Repair Pass

- This repair (Wave 3 Lane 4 Batch 3) added the Anti-Patterns section, the How to Use This Skill section, and this source ledger. It did not re-verify every pre-existing claim in genius.md line-by-line against the transcript — only the claims newly cited (Anti-Patterns section, How to Use section) were freshly checked against `transcript.txt` with exact line numbers via `grep -n`.
- Two pre-existing claims ("Theater Reflex" practice duration, "Special vs Important," psychedelic-seizure healing) could not be re-located verbatim in the primary transcript during this pass and are labeled UNCONFIRMED rather than silently carried forward as VERIFIED. They were not deleted (additive-first boundary) — a future pass should either locate the exact line or downgrade the claim's confidence in the prose itself.
- No claim in this ledger is sourced to the out-of-scope `transcript-modernwisdom-behaviorsuite.txt` file — confirmed by file read (125,792 bytes, non-empty) and by scope note in `SKILL.md`.
