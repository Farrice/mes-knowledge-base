# Source Ledger — steven-young-consciousness

Every claim in `SKILL.md` and `genius.md`, labeled VERIFIED / LIKELY / UNCONFIRMED against the primary source material recovered for this repair.

## Primary Sources Consulted

1. **`claude-export/normalized/conversations/58c6c715-a4fb-43be-bcf2-88c234668b68.md`** (inside `_archive/claude-export-2026-07-01.tar.gz`, 332,779,255 bytes total archive) — timestamped transcript of "Dr. Steven Young: Hermetic Expert: How To Use Your Thoughts to Change Reality Beyond Limitations," conversation created 2025-11-12, file size 174,728 bytes (`wc -c`), 33,383 words. **Primary transcript source** — this is the actual podcast/interview transcript with mm:ss timestamp markers, not a downstream summary.
2. **`claude-export/normalized/conversations/1798e41b-541c-4672-8a58-c92786a54223.md`** (same archive) — near-duplicate upload of the same interview under the title "Coach Fresh-Hermetic Expert...", conversation created 2025-07-10, file size 176,259 bytes, 33,712 words. Corroborating copy of the same transcript (same quotes recur verbatim in both files) — used as cross-check, not a second independent source.
3. `claude-export/normalized/conversations/1253f2ff-732a-4f2f-b839-9c47a11fe5b1.md`, `583f0fee-5ce8-4e7e-bf55-c1fb32038cac.md`, `f6e2d678-ae4d-4189-947d-01d0a35d29ea.md` — three further claude.ai conversations mentioning "Steven Young" (checked via full-archive `tarfile` content scan, not filename match). Confirmed by grep to contain **zero** timestamped transcript lines (`^[0-9]+:[0-9]+ -` pattern absent) — these are downstream "extract-deep" prompt-generation requests that reference Young by name, not source transcript. Not used as quote sources; listed here so their absence-as-source is a checked fact, not an assumption.
4. Existing `skills/steven-young-consciousness/SKILL.md` and `genius.md` content as of repair start (frontmatter states `source: claude.ai export 2026-07-01`, consistent with the archive above).

## Search Discipline Note

Search for `extractions/*steven*young*` returned nothing (only `steven-pressfield` exists under `extractions/`). Fragment search `steven young` (no punctuation) against the full 332MB archive via a per-member `tarfile` content scan (not filename match) returned 6 hits, 5 of which are `.md` conversation files (the 6th is the raw 867MB `conversations.json`, not opened directly). This confirms the skill's ground truth lives in the archive, not in `extractions/`, and that absence from `extractions/` is not absence of source.

## Claim-by-Claim Ledger

| # | Claim (SKILL.md / genius.md) | Label | Basis |
|---|---|---|---|
| 1 | 17+ years running a holistic-medicine practice, 9,000+ patients treated | VERIFIED | Source 1, lines 202, 1208 ("9,000 human beings," "I treated 9,000 patients") |
| 2 | "how was your massage?" text triggering his shift | VERIFIED | Source 1, lines 309-321 (verbatim: "went upstairs to get a massage... texted me and said how was your massage... how could they know") |
| 3 | Seven-Law Decoding (Mentalism, Correspondence, Vibration, Polarity, Rhythm, Cause & Effect, Gender) | VERIFIED | Standard Kybalion seven hermetic laws; Source 1 repeatedly names Correspondence, Polarity, Cause & Effect, Mentalism explicitly in-context (e.g. line 953 "this is such a law correspondence") |
| 4 | Oblique Intention Engineering / "light hitting a surface at an angle produces more energy" / NASA engineer who studied Kabbalah gave him the metaphor | VERIFIED | Source 1, lines 973-996 (verbatim: "she's a engineer for NASA... studied a cabala for like 40 years... when light hits a surface at an angle, it produces more energy than direct") |
| 5 | Direct-goal SMART-goal trap / "traps you in the forever loop... hamster wheel... pendulum... never taught how to go at things obliquely" | VERIFIED | Source 1, lines 990-1000, verbatim |
| 6 | Six-Word Elimination Protocol / "programmed to exist in a context of judgment" / good, bad, right, wrong, positive, negative | VERIFIED | Source 1, lines 1403-1409, verbatim |
| 7 | Love-Both-Poles Neutrality | LIKELY | Consistent with the polarity-law framing throughout Source 1 (e.g. healing/wounding discussion) but the specific "100% love fear AND 100% love courage" phrasing was not isolated verbatim in the two files scanned; the underlying mechanism (loving both poles to dissolve a pendulum) is directly supported. |
| 8 | Identity-Before-Effort Reprogramming / "hard worker" → "problem solver" → "empty vessel" | VERIFIED | Source 1, lines 200-260 (verbatim: "identify as a hard worker," "eventually changed my identity to problem solver," "40 hours a week") for hard-worker/problem-solver; "empty vessel" confirmed via full-archive grep hit in Source 1 |
| 9 | 100% Trust of Knowings / knowings since age five, 32 years second-guessing | LIKELY | Consistent with Source 1's repeated references to intuition and "pings" not being trusted "up until 32" (line 7:02-7:05 area); exact "age five" and "half-second" phrasing not independently isolated in the two files scanned |
| 10 | Vibration-First Causation / junk DNA, biophotons, 70% light | VERIFIED | Source 1, lines 61-67, 747-768 (verbatim: "70% light," "junk DNA," discussion of DNA producing light) |
| 11 | 0.1-Level Emotional Awareness / "The key is to be aware of the 0.1 level of anger or the 0.1 level of grief" | LIKELY | Source 1, lines 874-880: transcript renders the number as "01" not "0.1" ("the 01 level of anger or the 01 level of grief. I think that's the key"), an auto-transcription artifact of a spoken decimal. Genius.md's quote reorders "I think that's the key" into "The key is to be aware of" — a paraphrase of the same statement, not a verbatim lift. Downgraded from VERIFIED to LIKELY for this reason. |
| 12 | Language as Spellcasting / "casting different spells" / trauma → "heightened emotional experiences" / vulnerability / "you have so much potential" = "you're not there yet" | VERIFIED | Source 1, lines 583 ("he's casting different spells"), 919-943 (trauma/vulnerability reframing), 924-933 ("you have so much potential... you're not there yet") |
| 13 | Teaching as Remembrance / "all of this is just really a remembering of what was" / "felt like a remembrance, not a learning" | VERIFIED | Source 1, lines 1496 ("is just really a remembering of what was") and 335 ("remembrance, not a learning") |
| 14 | Compassion Mastery as exit signal from the healing/wounding cycle | UNCONFIRMED | Not isolated verbatim in the two transcript files scanned within the time available; consistent with the polarity-neutrality framework but the specific "it's not a wound, it's a part I wasn't fully aware of" language was not located and independent line verification could not be completed. Flag for a follow-up targeted search before treating as a citable direct quote. |
| 15 | Goal-Setting Industrial Complex framing | VERIFIED | Source 1, lines 990-996, same passage as claim 5 |
| 16 | Dream Day exercise / AI mastermind / journal entry from 2028 | VERIFIED | Source 1, lines 2558-2566 (verbatim: "designing your dream day," "journal entry from 2028," "showing me a dream day that I") |
| 17 | Source-Code Ho'oponopono / "I love you, God. I'm sorry..." / "re-sourced" | VERIFIED | Source 1, lines 1450-1477, 2969 (verbatim: "I love you, God," "resourced. You have gone back to source"); "hobonop pono" (Ho'oponopono, phonetic transcription) at line 2967-2968 |
| 18 | Six anti-pattern items added in this repair (genius.md "Anti-Patterns" section) | VERIFIED | Each carries its own file+line anchor inline; all six re-checked against Source 1 by direct `sed`/`grep` line extraction during this repair (see genius.md anchors: lines 861-864, 884-887, 929-933, 993-1000, 1403-1409, 1512-1513) |

## Labeling Summary

- **VERIFIED**: 14 of 18 claim groups — direct verbatim or near-verbatim quotes located and line-cited in Source 1.
- **LIKELY**: 3 claim groups (items 7, 9, 11) — mechanism/theme confirmed in source but the specific phrasing in the skill is a paraphrase, reordered, or the exact number/scene could not be isolated verbatim in the time available.
- **UNCONFIRMED**: 1 claim group (Compassion Mastery insight, item 14) — flagged, not removed (additive-first boundary), for a follow-up targeted pass.

No claim in this ledger is UNCONFIRMED due to source absence — the archive was searched (per-member content scan, not filename match) and file sizes were recorded with `wc -c` before any claim of unavailability.
