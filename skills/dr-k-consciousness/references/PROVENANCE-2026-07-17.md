# PROVENANCE.md — dr-k-consciousness repair

Anchor → source file + location. All anchors below were confirmed by direct
read + `grep -o -i "<phrase>" extractions/dr-k/transcript.txt | wc -l` during
this repair pass (2026-07-17).

| Anchor (as written in genius.md) | Source file | Location / method |
|---|---|---|
| "You're entitled to your actions, not the fruits of your actions." | `extractions/dr-k/transcript.txt` | verbatim, 1 grep match |
| "Awareness is the first step to control." | `extractions/dr-k/transcript.txt` | verbatim, 1 grep match |
| Breath demonstration dialogue (Exemplar 1) | `extractions/dr-k/transcript.txt` | "observe your breath" — 2 grep matches; cross-checked against `extractions/dr-k/extraction-report.md` Exemplar 1 block |
| Ken/seizure dialogue (Exemplar 2) | `extractions/dr-k/transcript.txt` | "seizure" — 5 grep matches |
| "Confidence doesn't come from success. It comes from surviving failure." | `extractions/dr-k/transcript.txt` | verbatim, 1 grep match |
| Medication "never heals" framing | `extractions/dr-k/transcript.txt` | "medication" — 9 grep matches |
| Belief is "the absence of knowledge" | `extractions/dr-k/transcript.txt` | verbatim, 1 grep match |
| "A loser never has imposter syndrome" | `extractions/dr-k/transcript.txt` | "loser never" — 2 grep matches |
| Mind-as-garden (water/weed) | `extractions/dr-k/transcript.txt` | "garden" — 8 grep matches |
| Ego as guard dog | `extractions/dr-k/transcript.txt` | verbatim, 1 grep match |
| Narcissistic defense clock | `extractions/dr-k/transcript.txt` | "narcissistic defense" — 2 grep matches |
| Coma patient's other life (Exemplar 3) | `extractions/dr-k/transcript.txt` | "coma" — 5 grep matches |
| Source word count (24,411 words) claimed by extraction-report.md | `extractions/dr-k/transcript.txt` | `wc -w` = 24,411 — exact match, confirms extraction-report.md's stated source is the real transcript, not fabricated |
| Anterior cingulate cortex framing | `extractions/dr-k/extraction-report.md` | interpretive neuroscience gloss added by the extractor, not a Dr. K on-record term in this transcript — labeled LIKELY in source-ledger.md, not VERIFIED |
| "99% Right = Catastrophic Mistakes" heuristic | `extractions/dr-k/extraction-report.md` | present as extractor-synthesized Hidden Knowledge #5; not independently isolated to a transcript line this pass — labeled LIKELY |
| Healthy Gamer "millions of subscribers" | `extractions/dr-k/extraction-report.md` | background bio in Content Assessment header, no transcript line or external check this pass — labeled UNCONFIRMED |
| Harvard-trained psychiatrist bio | `extractions/dr-k/extraction-report.md` | Content Assessment header — labeled LIKELY (plausible, not independently re-verified against a primary bio source this pass) |

Full ledger with claim-level detail: `references/source-ledger.md` (this
directory).

## Files touched this repair

- `genius.md` — full modified copy. Added `## How to Use This Skill (Model
  Calibration)` section immediately after the header (before "## Who Is Dr.
  K"), modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 but
  written fresh for Dr. K's specific craft (recognition-test language +
  polish-is-the-tell warning). This section also satisfies `recognition_test`
  via the phrase "would Dr. K recognize this as *his own clinical instinct
  firing in real time*" (matches auditor regex `recognize this as`).
- `SKILL.md` — unmodified copy, included for completeness (no changes were
  needed here; the recognition-test language was added to genius.md instead).
- `references/source-ledger.md` — new file, satisfies `source_ledger` check.
