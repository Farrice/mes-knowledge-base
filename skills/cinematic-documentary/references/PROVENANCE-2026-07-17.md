# Provenance — cinematic-documentary repair

Anchor table: every new/changed sentence added in this repair, mapped to its source file + location. All quotes below were located by direct `grep`/Python string search against `extractions/david-gelb/transcript.txt` (72,419 bytes, 13,946 words) during this session — none from training memory.

| Added text (genius.md) | Source | Location in source |
|---|---|---|
| "People care about people." | `extractions/david-gelb/transcript.txt` | char offset ~41,291 |
| "information versus emotion" | `extractions/david-gelb/transcript.txt` | char offset ~40,496 |
| "if things are not what you thought it was, you just go into what it actually is." | `extractions/david-gelb/transcript.txt` | char offset ~18,946 |
| "over the top and it just doesn't work, it's... cheesy or trying too hard" / "we're not leaning into the truth" | `extractions/david-gelb/transcript.txt` | char offset ~24,198–24,335 |
| "too many notes" (Amadeus/patron anecdote) | `extractions/david-gelb/transcript.txt` | char offset ~56,889 |
| "Each minute costs $10 million." (Cameron/Avatar studio-note anecdote) | `extractions/david-gelb/transcript.txt` | char offset ~58,077 |
| "2 weeks" (Chef's Table shoot duration) | `extractions/david-gelb/transcript.txt` | char offset ~7,541 |
| "what you give, that's the energy that you get back" | `extractions/david-gelb/transcript.txt` | char offset ~9,214 |
| "forming a squad of people that are kind of at a similar level, that have similar taste" (Ryan Coogler advice) | `extractions/david-gelb/transcript.txt` | char offset ~12,376 |
| "Once you watch it with someone else you will learn so much. It is pretty astonishing." | `extractions/david-gelb/transcript.txt` | char offset ~46,433 |
| "information docs that are based on information like Planet Earth" | `extractions/david-gelb/transcript.txt` | char offset ~69,415 |

All existing (unchanged) genius.md content — the 14 numbered Genius Patterns, 8 Hidden Knowledge items, 3 Hall of Fame Exemplars, Signature Moves, Quality Rubric — was already present and passing `verbatim_exemplars` (23/23) before this repair; not re-verified line-by-line here beyond the source-ledger.md claim table, which cross-checks every one against the same transcript file.

## How to Use This Skill section
Model calibration section (recognition_test fix) is original synthesis written for this repair, not a source quote — it draws its two embedded verbatim anchors ("if things are not what you thought it was..." and "over the top and it just doesn't work... cheesy or trying too hard") from the transcript locations above. Structural model (headers, tone, "polish is the tell" framing) follows `skills/ben-watkins-storytelling/genius.md` lines 7-16 per envelope instruction — content is new and specific to Gelb's own texture (Spider-Man/Titanic/Fog of War reference-density, "lean into the truth" fidelity standard), not copied from the Watkins file.

## source-ledger.md
Built from a direct file read of `extractions/david-gelb/transcript.txt` in full (not sampled) plus `grep`/`wc` checks against `skills/cinematic-documentary/SKILL.md` and `agents/david-gelb/AGENT.md`. Two claims (Chef's Table "6 seasons"; *Neat* whiskey documentary) were searched for in the transcript and confirmed absent — both labeled UNCONFIRMED rather than deleted (additive-only scope) or asserted (no invented provenance).
