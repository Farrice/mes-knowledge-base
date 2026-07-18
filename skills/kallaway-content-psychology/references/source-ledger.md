# Source Ledger — kallaway-content-psychology

Every source consulted for the Wave 3 Lane 4 Batch 8 repair, labeled claim-by-claim. This is additive to the skill's existing (weakly-passing) source signal — see REPAIR-NOTES.md for why a formal ledger was written anyway.

## Sources on disk

| File | Size | Role |
|---|---|---|
| `extractions/kallaway-content-system/transcript.txt` | 43,221 bytes | PRIMARY for this repair — cleaned transcript of "I Hated Social Media... Until I Learned THIS System" (yt=B9l9TRhu5Vw), acquired 2026-05-07. Source of all 6 new Anti-Patterns quotes below. |
| `extractions/kallaway-content-system/B9l9TRhu5Vw.en-orig.vtt` | 398,725 bytes | Raw caption file, same video. Not needed — transcript.txt already verbatim-matches. |
| `extractions/kallaway-content-system/extraction-report.md` | 4,963 bytes | Extraction summary for the above video. Not quoted directly in this repair. |
| `extractions/kallaway-content-system/integrity-patch.md` | 5,108 bytes | Prior integrity fix notes on this extraction. Read, not cited. |
| `extractions/kallaway/transcript.txt` | 34,072 bytes | "Illusion of Novelty" video transcript. Read for context; no quotes pulled for this repair (already mined by sibling skill kallaway-illusion). |
| `extractions/kallaway/internet-money-machine-transcript.txt` | 24,657 bytes | Internet Money Machine source. Read; already the basis for existing Patterns 2, 22, 24 (not touched this repair). |
| `extractions/kallaway/internet-money-machine-extraction.md` | 12,864 bytes | Structured extraction of the above. Read, not newly cited. |
| `extractions/kallaway/word-mastery-extraction.md` | 16,292 bytes | Separate extraction. Read; no overlap with items fixed here. |
| `extractions/kallaway/extraction-report.md` | 6,971 bytes | Contains the "one standard deviation" / "Unfair Advantage" language behind existing Patterns 30/32 hall-of-fame material (pre-existing, not modified this repair). |

## Claims added this repair (6 Anti-Pattern items, genius.md)

| Claim | Label | Anchor |
|---|---|---|
| "I don't recommend combining multiple creators here... speaking patterns are like fingerprints... it'll confuse the writer and make it generic." | VERIFIED | `extractions/kallaway-content-system/transcript.txt:688-692` |
| "Don't copy some other creator if you already have your own voice dialed." | VERIFIED | `extractions/kallaway-content-system/transcript.txt:684-686` |
| "...don't ever pay that person for services because they don't actually know what they're talking about." | VERIFIED | `extractions/kallaway-content-system/transcript.txt:426-428` |
| "...you should not be editing. You cannot be editing." | VERIFIED | `extractions/kallaway-content-system/transcript.txt:802-804` |
| "I don't think this is very premium yet... I wouldn't put all the eggs in this basket." | VERIFIED | `extractions/kallaway-content-system/transcript.txt:788-794` |
| "...none of them are great at writing scripts out of the box. You'll never find one without tuning it that's good enough." | VERIFIED | `extractions/kallaway-content-system/transcript.txt:646-648` |

All six were located verbatim by direct grep + line-range read against the file above on this repair pass — not paraphrased from memory.

## Pre-existing genius.md content NOT touched this repair (honest status, not re-verified here)

Patterns 31–33 ("6 Content Mistakes Diagnostic," "8 Psychology Principles for Viewer Trust," "Game Theory Framework") carry quoted lines (e.g. "the algorithm will nuke the video," "the BS detector") that do **not** appear verbatim in any local `extractions/kallaway*` file. SKILL.md attributes the v3 pattern set (1–37) to "NotebookLM upgrade" against Notebook ID `30579fcb-089b-4c38-a56e-a53b5c437fa5` — an external corpus this repair pass had no access to. Status: **UNCONFIRMED against local files** (not verified false, not verified true — the local extraction set simply doesn't contain these lines). This repair did not add, remove, or re-label those claims; flagging here for the conductor/adversarial pass rather than silently leaving it unaddressed.

## Legend
VERIFIED = quote located verbatim in a named file at a named line. LIKELY = paraphrase consistent with sourced material but not verbatim-matched. UNCONFIRMED = claim exists in the skill but no local source file was found to confirm or deny it.
