# PROVENANCE — jessica-jensen-platform-intelligence repair

Ground-truth source: `extractions/jessica-jensen/transcript.txt`, 44,903 bytes (confirmed via `wc -c`), single file, single source — the "Uncensored CMO" podcast interview with Jessica Jensen. No other extraction file exists for this expert.

## Anchor → source table (new content added this pass)

| Anchor (genius.md location) | Source | Location |
|---|---|---|
| Anti-Patterns item 1 — "Spec-Sheet Pitch" quote | extractions/jessica-jensen/transcript.txt | ~char 31,866 |
| Anti-Patterns item 2 — "Ramming the Product Message" quote | extractions/jessica-jensen/transcript.txt | ~char 37,463 |
| Anti-Patterns item 3 — "AI-Homogenized Voice" quote | extractions/jessica-jensen/transcript.txt | ~char 20,925 |
| Anti-Patterns item 4 — "Post-and-Disappear" quote | extractions/jessica-jensen/transcript.txt | ~char 18,220 |
| Anti-Patterns item 5 — "Over-Polished Corporate Posture" (Producer James contrast) | extractions/jessica-jensen/transcript.txt | ~char 16,138 / 16,076 |
| Anti-Patterns item 6 — "Assuming B2B Must Stay Boring" quote | extractions/jessica-jensen/transcript.txt | ~char 30,640 / 30,859 |
| Model Calibration — "buy this security feature... I wish them the best" | extractions/jessica-jensen/transcript.txt | ~char 32,774 |
| Model Calibration — "just because LinkedIn is a professional network doesn't mean you can't be fun" | extractions/jessica-jensen/transcript.txt | ~char 16,592–16,900 region |
| Model Calibration — "bring the anxiety down and the meaning up" | extractions/jessica-jensen/transcript.txt | ~char 16,991 |
| Recognition Test section | Written fresh for this repair; grounded in the skill's own SKILL.md framing ("the only platform-owner perspective") and the transcript's institutional-vantage pattern, not a Jensen quote itself — no anchor claimed beyond that framing. |
| source-ledger.md (all 25 rows) | extractions/jessica-jensen/transcript.txt | See per-row offsets in source-ledger.md |

## Verification method
Each quote was located with direct Python string search (`text.lower().find(term)`) against the full transcript file, then confirmed by eye in a ±200-400 character context window before being used as an anchor. Character offsets are approximate (search performed on the raw file, no normalization) but sufficient to relocate the passage. All six new Anti-Patterns bullets and all five Model Calibration bullets were built exclusively from quotes verified this way.

## The one flagged gap
The pre-existing quote "Could AI have written this identically for 50 other people?" (Genius Pattern 10 in the original genius.md, plus three other files: `references/prompts-v2/ai-authenticity-gate.md`, `references/prompts-v2/platform-intelligence-briefing.md`, `workflows/jensen-ai-gate.md`) could NOT be located in the transcript after searching "50 other," "identical," "identically," "sound the same," "duplicate," "interchangeable." It is recorded as UNCONFIRMED in source-ledger.md row 18. This is pre-existing content outside this repair's scope (those files were not part of the failing checks), but per the batch's hard rule ("a claim that sources are absent is itself a provenance claim... false claims caught by adversarial verification"), it is disclosed rather than silently anchored.
