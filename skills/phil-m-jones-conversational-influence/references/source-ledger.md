# Source Ledger — Phil M Jones (Conversational Influence)

Claim-by-claim provenance for every sourced statement in `SKILL.md` and `genius.md`. Labels: **VERIFIED** (quote confirmed against a local file by direct read), **LIKELY** (consistent with the source but not a direct quote match), **UNCONFIRMED** (no source file located; do not treat as fact).

## Primary Source

- **Expert**: Phil M Jones, author of *Exactly What to Say*, sales trainer.
- **Material**: Jones' own audio-book-style read-through of *Exactly What to Say* plus applied commentary (YouTube video `H4YArR-TMEc`).
- **Local file — VERIFIED**: `_active/codex-harvest-2026-06-11/extractions/phil-m-jones/transcript.txt` — 112,045 characters / ~20,448 words, confirmed present and readable 2026-07-18. **Correction to `references/source-notes.md`**: that file lists the local transcript path as `extractions/phil-m-jones/transcript.txt`. That path does not exist in the current repo (`extractions/` has no `phil-m-jones` directory — verified via directory listing 2026-07-18). The real, readable copy lives under the codex-harvest archive path above. Do not trust the `extractions/phil-m-jones/` path until it is restored; use the codex-harvest path for any future extraction work on this skill.
- **Companion file — VERIFIED**: `_active/codex-harvest-2026-06-11/extractions/phil-m-jones/extraction-report.md` (3,401 bytes) — extraction summary, confirms 20,448-word source and depth tier.

## Claim-by-Claim Table

| Claim / quote used in genius.md | Location cited | Label | Notes |
|---|---|---|---|
| "I'm not sure if it's for you, but" (Rejection-Free Introduction, Pattern 1) | transcript.txt, ~word 1,506 | VERIFIED | Exact substring found by direct string search. |
| "How open-minded would you be" (Identity-Safe Agreement, Pattern 2) | transcript.txt, ~word 1,775 | VERIFIED | Exact substring found. |
| 90/10 odds claim ("shifts you from having 50/50 odds... to odds of more like 9010 in your favor") | transcript.txt, ~word 1,775 area | VERIFIED | Transcript renders the ratio as "9010" (speech-to-text artifact for "90-10"); reproduced faithfully in genius.md as Jones's own phrasing. |
| "What do you know" (Soft Certainty Challenge, Pattern 3) | transcript.txt, ~word 25 | VERIFIED | Appears in the video's cold-open recap and again at the full Pattern 3 explanation. |
| "How would you feel if" (Future-Feeling Trigger, Pattern 4) | transcript.txt, ~word 29 | VERIFIED | Exact substring found. |
| "Just imagine" (Mental Movie Installation, Pattern 5) | transcript.txt, ~word 3,786 | VERIFIED | Exact substring found. |
| "When would be a good time?" (Assumptive Timing Frame, Pattern 6) | transcript.txt, ~word 4,538 | VERIFIED | Exact substring found. |
| "I'm guessing you haven't got around to" (Face-Saving Follow-Up, Pattern 7) | transcript.txt, ~word 5,142 | VERIFIED | Exact substring found (clean, no transcription stutter at this occurrence). |
| "the psychology behind this technique, which involves turning an open questioning into a closed one, results in you receiving a guaranteed outcome or answer" (One-Word Swap Control, Pattern 8) | transcript.txt, ~word 5,900 | VERIFIED | Exact substring found. |
| "As I see it," you have three options (Three-Option Decision Design, Pattern 9) | transcript.txt, ~word 7,020 | VERIFIED | Exact substring found. |
| "there are two types of people in this world" (Social Category Mirror, Pattern 10) | transcript.txt, ~word 8,110 | VERIFIED | Exact substring found. |
| "I bet you're a bit like me." (Likeness Bridge, Pattern 11) | transcript.txt, ~word 8,341 | VERIFIED | Exact substring found. |
| "If I can, will you?" (Conditional Commitment Close, Pattern 12) | transcript.txt, ~word 14,603 | VERIFIED | Exact substring found. |
| "Just one more thing." (Columbo Add-On, Pattern 13) | transcript.txt, ~word 16,673 | VERIFIED | Exact substring found. |
| "just out of curiosity" (Curiosity Recovery, Pattern 14) | transcript.txt, ~word 19,106 | VERIFIED | Exact substring found. |
| "the primary job description of all sales professionals is to be decision catalysts in the lives of their customers and prospects" (Identity section) | transcript.txt, ~word 7,949 | VERIFIED | Exact substring found. |
| "It's a tool to do a job. It is a technique to help create an outcome." (Hidden Knowledge) | transcript.txt, ~word 10,110 | VERIFIED | Exact substring found. |
| "I'm not saying that people should feel rushed into decisions." (Hidden Knowledge / Anti-Patterns) | transcript.txt, ~word 19,138 | VERIFIED | Exact substring found. |
| "One is pushy and the other is pulley." (Exemplar 1 / Anti-Patterns) | transcript.txt, ~word 1,547 | VERIFIED | Exact substring found. |
| `"I'm not sure if it's for you, but would you like to buy X?"` (Exemplar 1) | transcript.txt, ~word 1,506 | VERIFIED | This exact string is already inside quote marks in the source transcript — Jones is quoting his own "pushy" example. |
| "curiosity is the fuel to great conversation. And it's more than an idea. It's a principle. It's one of our four cornerstones." (Signature Moves) | transcript.txt, ~word 13,686 | VERIFIED | Exact substring found. |
| "People hate to feel manipulated and nearly always want to feel like they made the final decision." (Verbatim Exemplars / Anti-Patterns) | transcript.txt, ~word 6,977 | VERIFIED | Exact substring found. |
| "To overcome an objection, you must first understand what an objection really is." (Verbatim Exemplars / Anti-Patterns) | transcript.txt, ~word 13,154 | VERIFIED | Exact substring found. |
| "How open-minded is a is an open-ended question, whereas a would you be open-minded is a is a closed question." (Verbatim Exemplars / Anti-Patterns) | transcript.txt, ~word 1,927 | VERIFIED | Exact substring found; transcription disfluency ("is a is an") preserved verbatim rather than smoothed, per the no-fabrication rule. |
| "So be careful of understanding the method behind the madness. the why behind the what." (Model Calibration / Anti-Patterns) | transcript.txt, ~word 10,116 | VERIFIED | Exact substring found; the mid-sentence lowercase "the" is a transcription artifact, reproduced as-is. |
| "without feeling forced, without feeling like you're doing something to somebody, without feeling like what you're doing is you're manipulating" (Anti-Patterns) | transcript.txt, ~word 9,537 | VERIFIED | Exact substring found. |
| "if one option is too prescriptive and two options feels right and wrong and too many options feels overwhelming" (Anti-Patterns) | transcript.txt, ~word 7,557 | VERIFIED | Exact substring found. |
| Book title *Exactly What to Say* and video ID `H4YArR-TMEc` | source-notes.md (pre-existing, this skill) | LIKELY | Carried over from the original extraction record; not independently re-verified against YouTube in this repair pass (no live web check performed). |
| 23 sequence-family count | transcript.txt, multiple locations (e.g. ~word 14,603 "let's do 19", ~word 19,106 "23. ... this is the final sequence") | VERIFIED | Jones numbers the sequences aloud through the transcript; count of 23 confirmed by his own closing tally. |

## Method

Every quote above was located with a direct Python string search (`str.find`) against the full transcript file, then confirmed by reading the surrounding ~250-500 characters of context before use. No quote was invented or paraphrased into quotation marks. Where the source transcript itself contains a speech-to-text disfluency (repeated words, missing capitalization), it is reproduced verbatim rather than cleaned up, so a verifier opening the same file will find an exact string match.
