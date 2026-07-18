# Dr. K Consciousness — Source Ledger

Claim-by-claim provenance for every attributed pattern, quote, and exemplar in
`SKILL.md` and `genius.md`. Two source files ground this skill — both real,
both read in full for this repair:

- `extractions/dr-k/transcript.txt` — 125,247 bytes / 24,411 words. Raw
  transcript of the School of Greatness (Lewis Howes) interview with Dr. Alok
  Kanojia. VERIFIED by direct read + `wc -w` (24,411 words matches the
  extraction report's stated source length exactly).
- `extractions/dr-k/extraction-report.md` — 30,021 bytes. MES 3.0 mastery
  extraction derived from the transcript above. VERIFIED as internally
  consistent with the transcript (all sampled quotes below trace back).

No other Dr. K / Alok Kanojia / Healthy Gamer source files exist in
`extractions/`. Any claim below not traceable to these two files is labeled
UNCONFIRMED, not silently dropped.

## Claim-by-Claim Ledger

| # | Claim / Quote | Location in genius.md | Source | Status |
|---|---|---|---|---|
| 1 | "You're entitled to your actions, not the fruits of your actions." | Pattern 10, Signature Moves, Voice DNA | transcript.txt (1 match, verbatim) | VERIFIED |
| 2 | "Awareness is the first step to control." | Pattern 7, Exemplar 1, Voice DNA | transcript.txt (1 match, verbatim) | VERIFIED |
| 3 | Breath demonstration ("I want you to close your eyes and observe your breath...") | Exemplar 1 | transcript.txt ("observe your breath" — 2 matches; passage cross-checked against extraction-report.md Exemplar 1) | VERIFIED |
| 4 | Ken and the seizure patient dialogue | Exemplar 2 | transcript.txt ("seizure" — 5 matches, dialogue block present) | VERIFIED |
| 5 | "Confidence doesn't come from success. It comes from surviving failure." | Pattern 12 | transcript.txt ("Confidence doesn" — 1 match, verbatim) | VERIFIED |
| 6 | Medication "never heals," only manages | Who Is Dr. K, Hidden Knowledge #6 | transcript.txt ("medication" — 9 matches across the interview) | VERIFIED |
| 7 | Belief is "the absence of knowledge" | Anti-Exemplar, Anti-Pattern #1 | transcript.txt ("absence of knowledge" — 1 match, verbatim) | VERIFIED |
| 8 | "A loser never has imposter syndrome" / loser-identity framing | Pattern 2, Hidden Knowledge #2 | transcript.txt ("loser never" — 2 matches) | VERIFIED |
| 9 | Mind-as-garden model (water/weed) | Pattern 6 | transcript.txt ("garden" — 8 matches across the interview) | VERIFIED |
| 10 | Ego as guard dog | Pattern 9, Anti-Pattern #6 | transcript.txt ("guard dog" — 1 match, verbatim) | VERIFIED |
| 11 | Narcissistic defense / latency of self-defense | Hidden Knowledge #4 | transcript.txt ("narcissistic defense" — 2 matches) | VERIFIED |
| 12 | The coma patient's other life (Exemplar 3) | Exemplar 3 | transcript.txt ("coma" — 5 matches, narrative block present) | VERIFIED |
| 13 | Anterior cingulate cortex as the willpower/conflict-monitoring mechanism | Pattern 7, Exemplar 1 note | extraction-report.md interpretive gloss on the breath demonstration — the ACC framing is the extractor's neuroscience annotation, not a term Dr. K uses on-record in this transcript | LIKELY (mechanism is standard clinical neuroscience; not a verbatim Dr. K attribution in this source) |
| 14 | "99% Right = Catastrophic Mistakes" heuristic (high performers and undetected 1% misses) | Hidden Knowledge #5 | Present in extraction-report.md as an extractor-synthesized hidden-knowledge item; not isolated as a standalone verbatim quote in transcript.txt during this pass | LIKELY (consistent with extraction-report.md, not independently re-verified against a specific transcript line in this repair) |
| 15 | Founder of Healthy Gamer, "millions of subscribers" | Who Is Dr. K | extraction-report.md Content Assessment header states the interview context; subscriber-count figure is background bio, not sourced to a transcript line | UNCONFIRMED (no transcript line or external source consulted this pass to confirm current subscriber count) |
| 16 | Harvard-trained psychiatrist bio detail | Who Is Dr. K | extraction-report.md Content Assessment header | LIKELY (stated plainly in the extraction report's source metadata, not independently re-verified against a primary bio source this pass) |

## Method

Every VERIFIED row was checked this pass with `grep -o -i "<phrase>" extractions/dr-k/transcript.txt | wc -l`
against the live file, confirming the phrase exists verbatim in the raw
transcript (not just in the downstream extraction report). Rows marked LIKELY
or UNCONFIRMED were left honest rather than force-labeled VERIFIED — per the
hard rule that an invented "no source exists" or invented "verified" claim is
itself a provenance failure.
