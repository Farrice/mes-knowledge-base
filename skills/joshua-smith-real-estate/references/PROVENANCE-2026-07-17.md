# PROVENANCE — joshua-smith-real-estate repair (Wave 3 Batch 4, Lane 3)

Ground truth source: `extractions/joshua-smith/extraction-report.md` (19,766
bytes, 234 lines — the only file under `extractions/` matching this expert;
`ls extractions/ | grep -i smith` also returns `Alex Smith` and
`ethan-smith`, both unrelated). This file's own header states: "Source:
YouTube interview (Mike Sherrard channel), ~45 min, 10,268 words." No raw
transcript exists on disk for this expert.

| New content this pass | Anchor | Label |
|---|---|---|
| "Anti-Patterns (Sourced — extraction-report.md)" section, 6 bullets, `genius.md` | Bullet 1: `extraction-report.md` line 25-26 · Bullet 2: line 113-115 · Bullet 3: line 129 · Bullet 4: line 45 · Bullet 5: line 51 · Bullet 6: line 73-74 | VERIFIED (all 6) |
| "How to Use This Skill (Model Calibration)" section, `genius.md` | Craft/voice guidance authored this pass, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 (structure only, content is Smith-specific); one embedded quote ("who is the market good FOR?") anchors to `extraction-report.md` line 26 | N/A (authored guidance) / VERIFIED (embedded quote) |
| `references/source-ledger.md` | New file, full claim-by-claim table against `extractions/joshua-smith/extraction-report.md` | — |
| Evolution Log entry "2026-07-17 — Wave 3 Batch 4 repair pass" appended to `genius.md` | Self-documenting | — |

## Flagged pre-existing UNCONFIRMED provenance (not introduced this pass)

Two attributions already inside `genius.md` before this repair (added during
an earlier, undated enrichment pass — `genius.md` file mtime is 2026-04-09,
`extraction-report.md` mtime is 2026-02-16) could not be traced to the source
file:

1. Warren Buffett "swimming naked" quote, attached to Hidden Knowledge #6
   (Complacency as the Real Addiction). Not present in `extraction-report.md`.
2. "Mentor Darren Harding" quote, attached to Hidden Knowledge #7 (The "What
   Am I Going to Do?" Diagnostic). The name "Darren Harding" does not appear
   anywhere in `extraction-report.md`.

Per the batch envelope's hard rule ("a quote you cannot find in a source file
gets an UNCONFIRMED label, never an anchor"), both are labeled UNCONFIRMED in
`references/source-ledger.md` and left in place (additive-first — never
delete passing/pre-existing content). They were not invented by this repair
pass; this pass is the first to surface and label them.

Three quoted fragments inside the pre-existing "Anti-Exemplar" paragraph
("research," "a few times," "they weren't serious") are likewise UNCONFIRMED
against `extraction-report.md` — flagged in the ledger, left in place, and
deliberately NOT reused in the new sourced Anti-Patterns section.

## Verification method

`extractions/joshua-smith/extraction-report.md` was read in full this session
(234 lines) and cross-checked line-by-line against every claim in `genius.md`
before writing the ledger. `grep -n` was run against the source file for each
candidate quote before it was marked VERIFIED (commands used: searches for
"serious", "What should I do today", "need more leads", "research",
"swimming naked", "committed to paper", "Darren Harding", "Warren Buffett",
"tiny hinges"). No claim was marked VERIFIED without a positive grep/read
match in `extraction-report.md`.
