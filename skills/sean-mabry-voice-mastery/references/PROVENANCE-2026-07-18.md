# Provenance — sean-mabry-voice-mastery repair pass (2026-07-18)

Anchor → source file + location for every new claim/quote added in this
repair pass. Full claim-by-claim status for the *entire* skill (pre-existing
content included) lives in `references/source-ledger.md`. This file covers
only what was newly written.

## New Anti-Patterns (genius.md, `## Anti-Patterns (Sourced)`)

| # | Anchor text (as it appears in genius.md) | Source file | Location | Verification method |
|---|---|---|---|---|
| 1 | "I didn't try to go from taking an hour to taking 15 minutes. That's insane... you're just going to spin out." | `extractions/sean-mabry/transcript.txt` | ~word 5,509 of ~18,827 (offset ~28,653 of 97,575 bytes) | Confirmed via Python `in` substring search, exact match |
| 2 | "I've never met anyone really who's willing to settle for 80%." | `extractions/sean-mabry/transcript.txt` | ~word 4,149 (offset ~21,746) | Confirmed via Python `in` substring search, exact match |
| 3 | "this is something I see a lot of young copyriters... 'Oh, be polarizing... you got to be abrasive.'" | `extractions/sean-mabry/transcript.txt` | ~word 2,365 (offset ~12,536) | Confirmed via Python `in` substring search, exact match |
| 4 | "a lot of times people want to start with a book that's like super tactical... no fluff... And the problem with that is it ignores the reality of what people are looking for in a book." | `extractions/sean-mabry/transcript.txt` | ~word 15,051 (offset ~77,942) | Confirmed via Python `in` substring search, exact match |
| 5 | "hey, I bought this pack of templates, right? ... to the degree that that was ever a viable strategy which is very debatable um not in 2026." | `extractions/sean-mabry/transcript.txt` | ~word 12,079 (offset ~62,646) | Confirmed via Python `in` substring search, exact match |
| 6 | "I didn't handwrite sales letters... I didn't really find handwriting helped me so much when I was learning the fundamentals of copyrightiting." | `extractions/sean-mabry/transcript.txt` | ~word 3,308 (offset ~17,392) | Confirmed via Python `in` substring search, exact match |

Extraction date used in citations (2026-03-15) = the date both
`extractions/sean-mabry/transcript.txt` and `extraction-report.md` were added
to the repo, per `git log --diff-filter=A --date=short`.

## Model Calibration Section (genius.md, `## How to Use This Skill (Model Calibration)`)

Modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines
7-16 (read once, per ENVELOPE.md instruction), but every specific claim about
Mabry's craft is drawn from patterns already sourced elsewhere in this file:
the "sounds like me" recognition test comes from the "no edits" milestone
(Pattern 6, VERIFIED); the prediction-commitment guidance comes from Pattern
1 (VERIFIED); the "measured, not hyped" texture note comes from the
transcript's overall register (a working ghostwriter interview, not a
promotional pitch — no source file location beyond the transcript as a
whole); the polish-is-the-tell warning is derived from
`workflows/01-voice-dna-capture.md`'s own Quality Gate test ("Could you swap
this voice profile's surface layer with someone else's").

## Output Schema (workflows/01-voice-dna-capture.md)

Not a new factual claim — restates the workflow's own pre-existing Phase 6
"Voice DNA Document Assembly" (9 numbered components, unchanged) as a formal
schema paragraph, matching the house style found in
`skills/ai-carousel-content-engine/workflows/01-ai-carousel-engine.md`
(`## Output Schema` section, read for format reference only — no content
borrowed).
