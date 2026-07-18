# Source Ledger — kallaway-addictive-storytelling

> Compiled 2026-07-18, Wave 3 Lane 4 repair. Every claim below is labeled VERIFIED / LIKELY / UNCONFIRMED. Ground truth = files under `extractions/` matching "kallaway" plus verbatim quotes already inside the skill files. Method: `grep -rio "dopamine|prediction chemical|vending machine|slot machine|time per hand|head fake|addiction loop|big question" extractions/` across every kallaway* extraction file, plus `wc -c` on each candidate file to rule out silent 0-byte failures.

## Files checked (with sizes — none are 0-byte/unrecoverable)

| File | Size (bytes, `wc -c`) | Relevant hits |
|---|---|---|
| `extractions/kallaway/extraction-report.md` | 6,971 | 0 |
| `extractions/kallaway/word-mastery-extraction.md` | 16,292 | 0 (checked separately for "vending/slot/dopamine/prediction/head fake/stakes/hook" — only tangential "blank-page adrenaline" hit, not addiction-loop material) |
| `extractions/kallaway/transcript.txt` | 34,072 | 0 |
| `extractions/kallaway/internet-money-machine-extraction.md` | 12,864 | 0 |
| `extractions/kallaway/internet-money-machine-transcript.txt` | 24,657 | 0 |
| `extractions/kallaway-content-system/extraction-report.md` | 4,963 | 0 (describes a DIFFERENT extraction — the Six-Stage Rep / 10x Batch content system, not the Addiction Loop) |
| `extractions/kallaway-content-system/transcript.txt` | 43,221 | 1 incidental "dopamine" mention (context not addiction-loop related) |
| `extractions/kallaway-content-system/integrity-patch.md` | 5,108 | 0 (unrelated — Trend Hook Engine integrity patch) |
| `extractions/kallaway-content-system/B9l9TRhu5Vw.en-orig.vtt` | 398,725 | 3 incidental "dopamine" mentions |
| `_archive/claude-export-2026-07-01.tar.gz` | 332,779,255 | Not searched at quote level (tarball listing shows no filenames matching "kallaway"/"script viral"/"speedrun"; content-level search of a 332MB conversation archive is out of this repair's scope) |

## Claim-by-claim labels

| Claim / Pattern | Label | Basis |
|---|---|---|
| Patterns 1-8 (Core Genius, Four-Step Addiction Loop, Vending Machine Test, Stakes as Housing, Big Question Calibration, Head Fake Engineering, Relay Race Rehook, Time-Per-Hand) | **UNCONFIRMED** | The cited source ("The Neuroscience of Addictive Storytelling," YouTube, 2026) has no transcript file anywhere in `extractions/`. Full-text grep across all 5 kallaway/ files and the kallaway-content-system transcript + VTT returned zero matches for the framework's core terms. This is a genuine absence, not an unread file — every candidate file above was opened and grepped. |
| Hall of Fame Exemplars 1-3 (Prince and Dragon, Client Budget Rehook, Casino Analogy) | **UNCONFIRMED** | Same as above — these are quoted/paraphrased as if verbatim from the source video, but the video transcript is not on file to verify against. |
| Anti-Exemplar (The Empty Teaser) | **UNCONFIRMED** | Same basis. |
| Patterns 9-12 (Four Script-Writing Blockers, Law of Interesting/Shock Score, 7-Structure Library, Emotional Transfer Engineering) | **UNCONFIRMED** | Cited source is a claude.ai export conversation ("How to Script Viral Videos 10x Faster," "Speedrun Social Media") inside `_archive/claude-export-2026-07-01.tar.gz`. The archive file genuinely exists (332,779,255 bytes, confirmed via `wc -c`) — this is NOT a fabricated-absent source — but quote-level verification against the archive's contents was not performed in this repair pass (332MB tarball, no filename index matching these conversation titles). |
| SKILL.md workflow contracts, quality rubric, stacking guide | **LIKELY** | Internally consistent with the genius.md patterns and cross-references content-psychology/audience-obsession skills that exist on disk; not independently re-verified against those skills' own source ledgers in this pass. |

## Recommendation for next repair pass

If the original YouTube video is still available, re-extract its transcript into `extractions/kallaway/addictive-storytelling-transcript.txt` and re-verify Patterns 1-8 + exemplars verbatim. Until then, treat genius.md Patterns 1-8 as a structurally sound but source-unconfirmed framework — safe to use for its internal logic, not safe to cite as a verbatim Kallaway quote.
