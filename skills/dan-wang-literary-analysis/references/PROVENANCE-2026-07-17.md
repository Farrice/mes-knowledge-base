# Provenance — genius.md entity-grounding insertions

Every insertion made to `genius.md` to clear `named_entity_floor` is a real quote or number pulled from `extractions/dan-wang/transcript.txt` (110,739 chars, single-line ASR transcript of the *How I Write* / David Perell interview with Dan Wang). Full claim-by-claim table with labels: `references/source-ledger.md`. This file maps each specific insertion to its exact anchor.

| genius.md section | Inserted text (quoted portion) | Source anchor (transcript.txt) |
|---|---|---|
| Pattern 2: Flower Inspection | "like looking at a flower... new levels of beauty" (Perell, describing Wang's prose) | ~char 9844–9990 |
| Pattern 3: Texture Over Tectonic Plates | "tectonic plate movements" / "a soup that you had in Kuning" | ~char 24925–25010 |
| Pattern 6: Single Beautiful Sentence Method | "absolutely valid to try to construct an entire essay around a single beautiful sentence" (Wang) | ~char 15600–15760 |
| Pattern 7: Outsider Error-Correction | "I have felt myself an outsider in various ways" + city of Quinning (Wang) | ~char 67960–68080 |
| Pattern 8: Zoom In/Zoom Out Oscillation | "the more that I zoom in to your writing, the better it gets" (Perell) | ~char 10320–10420 |
| Pattern 9: Meal-Structured Travel | "the three or four eateries" / "the corner noodle shop" (Wang) | ~char 30260–30340 |
| Pattern 11: Qualm-Collected-Canadian Mantra | "a qualcom collected Canadian" (Wang) | ~char 22970–23060 |
| Pattern 12: Genre Transcendence Identification | "Yale University Press or Stanford University Press or Oxford University Press" (Wang) | ~char 40300–40420 |
| Pattern 13: Ironic Beauty Layering | "the musical line that runs from Mozart, his three Italian operas" / opera buffa "ornament for its own sake" (Wang) | ~char 8380–8460 |
| Pattern 14: Score-Copying Apprenticeship | "porting over a method...from trying to understand music and composition" / clarinet (Wang) | ~char 104590–104900 |
| Pattern 15: Network Effects of Knowledge | "the Silicon Valley model of network effects in which growth can accelerate" (Wang) | ~char 108280–108420 |
| Tacit 3: Writing Retreats | "writing in Austin" / "Daang in Vietnam" / "proposal in Barcelona" (Wang) | ~char 95560–95900 |
| Tacit 4: Mom-Level Feedback Value | "Son, you look terrible. What's going on?" / *Morning Joe* (Wang's mother, via Wang) | ~char 98438–98620 |
| Tacit 5: AI as Tyler-in-Your-Pocket | "a very Tyler-like creature...in my pocket" (Wang) | ~char 62560–62700 |
| Tacit 6: Visa Uncertainty as Editorial Freedom | "the Chinese Ministry of Foreign Affairs can have a good long think" (Wang) | ~char 88630–88760 |
| Tacit 7: The Cover Photo Strategy | "a woman standing below a giant structure that looks a lot like the Tower of Sauron" / editor Caroline (Wang) | ~char 97181–97800 |
| "Dan Wang Would Never..." (Anti-Patterns intro) | he will "never take any of...ChatGPT's generally super flat sentences...into something that I would ever write myself" (Wang) | ~char 62800–63050 |
| AN-7: Just-So Smoothness | "every event feels kind of impossible before it takes place and then...it feels obvious and necessary" (Wang) | ~char 50050–50260 |
| Quality Rubric pointer | "Score 4 (Acceptable), Score 7 (Good), Score 10 (Savant)" | `references/quality-rubric.md`, table header (verified in-repo, not the transcript) |

## Method

1. Ran the auditor's own `_sections_zero_entity` logic (imported from `skill_census.py`) against the original `genius.md` to get the exact list of 19 zero-entity sections (matches the audit's reported 43 sections / 0.44 ratio exactly).
2. `grep`/Python-searched `extractions/dan-wang/transcript.txt` for terms matching each section's topic (e.g., "Mozart", "visa", "Yale", "Tyler", "cover photo").
3. Pulled the exact character span for each hit, read 400–900 chars of surrounding context, and selected a short verbatim (or near-verbatim, noting ASR artifacts) quote genuinely on-topic for that pattern.
4. Inserted one sourced sentence per section, appended to the existing `**Execute**`/tacit body — additive only, no existing sentence removed or reworded.
5. Re-ran `_sections_zero_entity` against the patched file: 43 sections, 0 zero-entity, ratio 0.00 (max allowed 0.2).
6. Re-ran the auditor's actual `heartbeat_checks()` function against a scratch copy of the full skill directory (patched `genius.md` + new `references/source-ledger.md`, all other files unchanged) — all 6 checks now PASS. Command used is reproducible: import `execution/skill_auditor.py`, call `fingerprint_skill()` + `heartbeat_checks()` on the skill path.
