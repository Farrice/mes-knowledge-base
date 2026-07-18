# Source Ledger — Corey McClain / Persona Engineering

Repair pass 2026-07-17 (Wave 3 Lane 4 Batch 3). Ground truth verified by direct
file read + `wc -c` byte count before any claim of absence was made.

## Sources Consulted

| Source | Path | Size (bytes, `wc -c`) | Status |
|---|---|---|---|
| Course transcript (video 2 of playlist — LLMP framework, Makoshi origin, Aar Vance A/B) | `extractions/corey-mcclain/transcript.txt` | 29,994 | VERIFIED — read in full, single source file for this expert (`ls extractions/ | grep -i mcclain` returns exactly one directory, one file) |
| Existing skill genius.md (pre-repair) | `skills/corey-mcclain-persona-engineering/genius.md` | — | VERIFIED — read in full; all Genius Patterns / Hidden Knowledge / Exemplars already carried real transcript quotes, preserved as-is |
| Existing skill workflows (pre-repair, 20 files) | `skills/corey-mcclain-persona-engineering/workflows/*.md` | — | VERIFIED — read in full; internal step templates (Report Template, Construct Assembly, Identity Profile Assembly, etc.) used as the grounding basis for each new Output Schema section rather than invented boilerplate |
| `skills/ben-watkins-storytelling/genius.md` lines 7-16 | (reference only, not a claim source) | — | VERIFIED — read as the house-style model for the Model Calibration section per repair-fleet envelope instruction |

## Claim-by-Claim Labels (new/changed content only)

| Claim | Label | Anchor |
|---|---|---|
| "if thinking about it as a layer is not helpful, it may be more helpful to think about it as a container" | VERIFIED | transcript.txt, persona-as-container passage |
| "the thing about setting these up in workspaces is the fact that they just get better, right?" | VERIFIED | transcript.txt, steady-state installation passage |
| "I can take two different people with two different world views and give them the same problem and the results you get will be completely different, they're going to reach completely different audiences" | VERIFIED | transcript.txt, worldview passage |
| "Maybe it's the first thing it references, maybe it's the last thing it references. That's your choice." | VERIFIED | transcript.txt, router-integration passage |
| "quality control every single time" | VERIFIED | transcript.txt, Library-layer passage (source has a transcription artifact — "fot prompting" — rendered here as the surrounding verbatim clause only, not the garbled word) |
| "not the memory that Open AI, Claude or Gemini gives you, but your own personal memory base with its own tagging system" | VERIFIED | transcript.txt, Memory-layer passage |
| "It's almost like a booster pack that just improves the performance of the logic in the library." | VERIFIED | transcript.txt, Persona-layer passage |
| Aar Vance freestyle took ~60 seconds, zero planning | VERIFIED | transcript.txt + pre-existing genius.md Exemplar 2 ("created in 60 seconds with zero planning") |
| Prada.com $6,500 floral-print dress, materials/measurements only | VERIFIED | transcript.txt, Prada Principle passage; also pre-existing in genius.md Genius Pattern 9 |
| "You are a graphic designer... women 25 to 35" marketing-asset task framing | VERIFIED | transcript.txt, Transistory Freestyle passage |
| "I've deleted both conversations so that we can't be tainted by the image that was generated" | VERIFIED | transcript.txt, Controlled Delete passage |
| "the logic, the library are obviously more important than anything else... then the memory and then finally the personality profile was installed on top of that" | VERIFIED | transcript.txt, LLMP build-order passage |
| "Not act as a social media manager, not act as a YouTube channel manager, not act as a business consultant, but actually this is who you are" | VERIFIED | transcript.txt, identity-vs-role-play passage |
| "Claw never talks about his personality when it responds to you" [rendered "Claude" in genius.md prose] | VERIFIED | transcript.txt, persona-leakage passage (source transcription renders "Claude" as "Claw"/"Clawude" throughout — a transcription artifact of the source video, not an invented claim) |
| "The persona document is NEVER compressed... compressing it destroys the container effect." | VERIFIED | `skills/corey-mcclain-persona-engineering/workflows/mcclain-nate-full-agent.md`, Step 5 (pre-existing skill content, not transcript-sourced — labeled as an in-skill cross-reference, not an expert quote) |
| "if I was creating a persona for a marketing agent, then that persona would be generated in a fashion that the marketing assets... is going to appeal to that audience" | VERIFIED | transcript.txt, worldview-audience-alignment passage (also pre-existing in genius.md Hidden Knowledge #6, quoted there in full) |
| Output Schema sections (17 workflow files) | VERIFIED (structural) | Each schema is a restatement of that workflow's own pre-existing step templates/output lines (e.g., Report Template, Construct Assembly, Identity Profile Assembly, Architecture Presentation) — no new claims invented, only the missing `## Output Schema` heading added to make the existing contract explicit |

## Absence Verification

No claim of "source absent" was made in this repair. The transcript
(`extractions/corey-mcclain/transcript.txt`, 29,994 bytes, confirmed via
`wc -c`) is a single, sufficient, non-empty source for every anchor above —
its adequacy was confirmed by a full read, not assumed.

## UNCONFIRMED

None. Every claim above traces to either the transcript or pre-existing,
already-shipped skill content (workflow step templates / cross-references).
No invented provenance was introduced.
