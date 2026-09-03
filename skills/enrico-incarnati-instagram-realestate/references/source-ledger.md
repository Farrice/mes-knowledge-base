# Source Ledger — Enrico Incarnati Instagram Real Estate Skill

Every claim in this skill traced to its source, labeled VERIFIED / LIKELY / UNCONFIRMED. Compiled during Wave 3 Lane 4 repair pass (2026-07-17).

## Sources Consulted

| Source | Path | Size | Status |
|---|---|---|---|
| Primary transcript | `extractions/enrico-incarnati/transcript.txt` | 18,909 bytes | Read in full — confirmed non-empty, single continuous YouTube transcript |
| Codex harvest audit | `_active/harness/codex-harvest-2026-06-11/brain/121fe594-3b12-4ae1-9339-c14ac503ee83/enrico_audit_jiing.md` | present, read in full | Secondary artifact — a `/enrico-audit` deliverable run against @_jiing, not a source of Enrico's own teaching; used only to confirm the workflow's output shape matches what a real deployment produced |
| claude-export tarball | `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) | checked via `tar -tzf ... | grep -i enrico` | Zero matches — no additional Enrico source material found in the tarball. Absence confirmed by listing, not assumed. |
| codex-harvest directory-wide | `_active/harness/codex-harvest-2026-06-11/` | checked via `find -iname "*enrico*"` | Only the one audit deliverable file found (above) — no additional raw source material |

**Conclusion**: `extractions/enrico-incarnati/transcript.txt` is the ONLY primary source for Enrico Incarnati's teaching in this system. No second transcript, article, or course exists in the codebase as of this repair pass.

## Connected Source Expansion: Marie Lee Transaction Stories (2026-09-03)

This source does not alter claims attributed to Enrico. It supplies an additive, source-labeled workflow under Enrico's existing Instagram-for-real-estate ownership.

| Source | Evidence captured | Allowed transfer | Boundary |
|---|---|---|---|
| The Broke Agent interview with Marie Lee, `https://www.youtube.com/watch?v=LO3NwPogTjQ` | Full native-caption review, 53-frame scene scan, 30 targeted frame checks, timestamped synthesis | Transaction case capture, format routing, proof ordering, production economy, trust-vs-demand distinction | Performance and causal claims remain `SOURCE_REPORTED`; no result guarantee or persona imitation |

Source-specific mechanics and timestamps: `references/marie-lee-transaction-story-mechanics.md`. Inspectable extraction package: `extractions/video-context/LO3NwPogTjQ/`.

## Claim-by-Claim Ledger

| Claim | Location in skill | Status | Basis |
|---|---|---|---|
| "Over 1.8 million real estate agents on Instagram" | transcript.txt opening line | VERIFIED (Enrico said it) / UNCONFIRMED (as objective fact) | Enrico's own opening stat, not independently fact-checked against a third-party source in this pass |
| Enrico is "Director of Social" for a top-3 global podcast reaching 40M+ daily | genius.md header, SKILL.md Expert Identity | VERIFIED (self-reported in transcript) / UNCONFIRMED (external verification not performed — no WebSearch run this pass) | transcript.txt: "I am the director of social for one of the fastest growing personal brands and the third largest podcast in the entire world where we reach over 40 million people every single day" |
| Enrico has "300,000+ followers" | SKILL.md Expert Identity | VERIFIED (self-reported in transcript) / UNCONFIRMED (external verification not performed) | transcript.txt: "I've grown to over 300,000 plus followers" |
| Core philosophy quote: "If your name were to be removed from the content, would it change at all? If the answer is 'no,' you don't have a brand — you have a billboard." | SKILL.md line 12 | **UNCONFIRMED — could not locate this exact sentence in transcript.txt** | This precise formulation does not appear verbatim in the source transcript. The transcript's actual billboard framing is the three-mistakes breakdown (static photo + price + caption). This looks like a paraphrase/synthesis presented as a direct quote. Flagged for downstream correction — should be reworded as a synthesized principle, not a quoted line, or removed. |
| Trent Miller, Lisa Dubois, Tampa Brie, Margie Morasco, Eric Thurwood (Hall of Fame exemplars) | genius.md, references/signature-format-examples.md | VERIFIED (named by Enrico in transcript with described format) / UNCONFIRMED (their real Instagram handles/existence not independently verified — no browser check performed) | All five names and their format descriptions (sprinting through homes, hide-and-seek tours, comedy, viral-trend energy, 3-second hooks) appear verbatim in transcript.txt Mistake #1 section |
| Nava Realy, Your New Texas Home (proximity play exemplars) | genius.md Pattern 4, Hall of Fame table | VERIFIED (named by Enrico with specific claims: Plano mall demolition, Goldman Sachs office in Dallas) / UNCONFIRMED (claims about what these accounts covered not independently verified) | transcript.txt Mistake #3 section |
| Ryan Sirhan (day-in-life vlog reference) | transcript.txt only — not currently named in genius.md Hall of Fame table | VERIFIED (named in transcript) | transcript.txt: "take a page out of Ryan Sirhan's book. Do a day in the life vlog..." — likely a phonetic transcription of "Ryan Serhant," a well-known real estate media figure; transcript renders it "Sirhan." Preserved as transcribed; flagged as a probable ASR (speech-to-text) spelling variant, not corrected without a second source. |
| Freddy (Visual Math reference) | transcript.txt only | VERIFIED (named in transcript, no surname or handle given) | transcript.txt: "Much like Freddy, he does a great job breaking down all of this." No further identifying detail in source — cannot be linked to a specific public account. |
| Adrienne and Tom (SEO name examples) | transcript.txt only | VERIFIED (named in transcript as SEO-name examples) / UNCONFIRMED (no surnames, handles, or markets given in source) | transcript.txt Mistake #4 section |
| Virginia golf-format client anecdote | genius.md Pattern 1, SKILL.md Key Patterns | VERIFIED (told by Enrico as a first-person coaching story in transcript) / UNCONFIRMED (client's identity, whether the reel "became one of his most engaging reels ever" — a claim made by Enrico, not independently verified) | transcript.txt Mistake #1 section, full anecdote |
| Stan Store, ManyChat as recommended tools | genius.md Pattern 5/7, all lead-gen workflows | VERIFIED (named by Enrico in transcript, including "free 14-day trial" / "free trial to Many Chat Pro for 30 days" claims) / LIKELY (both are real, existing SaaS products — general knowledge, not re-verified via live web check this pass) | transcript.txt, profile-optimization and lead-magnet sections |
| @_jiing audit data (follower/post counts, scores) | `enrico_audit_jiing.md` (codex-harvest) | VERIFIED as a prior system-generated deliverable | This is NOT a source for Enrico's teaching — it's a downstream `/enrico-audit` output run against Farrice's wife's account on 2026-04-03. Included in this ledger only because it's the one other file the batch envelope's "check codex-harvest by content" instruction surfaced. |
| Enrico's methodology has exactly "five pillars" / "12 genius patterns" | genius.md structure | This is the extraction team's organizing synthesis, not a claim Enrico makes about his own framework in the transcript — labeled as **synthesis**, not sourced to a direct quote. The underlying content (signature format, expansion pack, proximity play, curb appeal, lead capture) is VERIFIED against the transcript; the "5 pillars / 12 patterns" packaging is this skill's structure. |

## Gap Named

The SKILL.md "Core Philosophy" quote (line 12) is the one claim in this skill that could not be traced to the source transcript verbatim. It has NOT been corrected in this repair pass — the batch envelope scopes changes to the six failing heartbeat checks (anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts), and SKILL.md line 12 is a content-accuracy issue outside that scope, tracked here per the "false absence/unverified quote" rule rather than silently left unflagged.
