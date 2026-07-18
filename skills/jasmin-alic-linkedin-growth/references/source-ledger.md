# Source Ledger — Jasmin Alic: LinkedIn Organic Growth

Every claim, pattern, and quote in this skill traced to a source file, labeled
VERIFIED (quote/claim confirmed verbatim against the cited file), LIKELY
(claim consistent with cited material but not verbatim-matched line-for-line),
or UNCONFIRMED (no locatable source — flagged, never anchored as fact).

## Primary Sources

| Source | Type | Status |
|---|---|---|
| `extractions/Jasmin_Alic_Extraction.md` | YouTube transcript distillation (23,906 words, ~1h30m interview) — read in full for this repair | VERIFIED |
| `skills/jasmin-alic-linkedin-growth/references/genius-patterns.md` | Mirrors extraction's Genius Patterns §, read in full | VERIFIED |
| `skills/jasmin-alic-linkedin-growth/references/hidden-knowledge.md` | Mirrors extraction's Hidden Knowledge §, read in full | VERIFIED |
| `skills/jasmin-alic-linkedin-growth/genius.md` § "Patterns from claude.ai export — LinkedIn 2025 Jasmin Alic System (project c10c06cd)" (pre-existing, lines 120-145 of the shipped file) | Second-source patterns (Content-to-Client Pathway, Pinned Self-Comment Revenue Engine, Expertise Signposting, High-Ticket Authority Positioning) already resident in the shipped skill | LIKELY — the raw claude.ai export/project file was not locatable anywhere else in the repo during this repair pass (searched `extractions/`, project ID `c10c06cd`, repo-wide grep). Content is internally consistent with the rest of the skill and pre-dates this repair, so it is treated as an existing skill claim, not re-verified against a primary transcript. Not labeled UNCONFIRMED because it is not a bare assertion of absence — it is pre-existing shipped content this pass did not author. |

## Claim-by-Claim: New Anti-Patterns Section (added this repair pass)

| Anti-pattern item | Quote used | Source anchor | Status |
|---|---|---|---|
| Generic Engagement Comment | "Great post! So much value here. Really resonated with me. Keep up the good work!" | `genius.md` § Hall of Fame Exemplars → Anti-Exemplar (pre-existing in shipped file, itself sourced from `extractions/Jasmin_Alic_Extraction.md`) | VERIFIED |
| Standalone Sales Post | "Marketers default to isolating pitches into standalone 'sales posts' which the algorithm heavily penalizes for low initial engagement" | `extractions/Jasmin_Alic_Extraction.md`, Hidden Knowledge — "The 'Un-Salesy' Mid-Post Tag" | VERIFIED |
| Comments Treated as a Chore | "People treat comments as chores or forced engagement rather than a place for rapid hypothesis testing of copywriting hooks" | `extractions/Jasmin_Alic_Extraction.md`, Hidden Knowledge — "The Comment Laboratory" | VERIFIED |
| Cold DM Pitch | "Never DM-pitch a stranger and never post a 'sales post' (the algorithm suppresses low-engagement pitches)" | `genius.md` § Patterns from claude.ai export, pattern 1 — The Content-to-Client Pathway | LIKELY (see project c10c06cd note above) |
| Unfounded / Generic Transformation Claim | "anchor... in real, named specificity and quantified stakes, never generic transformation" | `genius.md` § Patterns from claude.ai export, pattern 4 — High-Ticket Authority Positioning | LIKELY (see project c10c06cd note above) |
| Four-Line Post (Truncation Miss) | "Must stop before line 4 so it naturally truncates on all devices" | `extractions/Jasmin_Alic_Extraction.md`, Methodology → Level 2: Hook Architecture | VERIFIED |
| Generic, Demanding CTA | "DM me to learn more" | `genius.md` § Expert-Specific Quality Rubric, "Engagement Intent (Post)" row (pre-existing) | VERIFIED |

## Claim-by-Claim: Model Calibration Section (added this repair pass)

| Claim | Source anchor | Status |
|---|---|---|
| Voice register — "Hear me out," "See how different these two are?," "Boom." | `extractions/Jasmin_Alic_Extraction.md`, Agent Configuration → Voice & Style | VERIFIED |
| "Recognition test" framing (would Jasmin Alic recognize this as his own cadence) | Written for this skill, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 structure per Wave 3 repair mandate — not a source quote, a calibration instruction | N/A (instructional, not a factual claim) |

## Absence Notes (per envelope rule 2 — verified, not assumed)

- No dated/timestamped raw transcript file exists under `extractions/` for Jasmin Alic — confirmed via `ls -la extractions/Jasmin_Alic_Extraction.md` (8,268 bytes, 108 lines) and repo-wide search for `*jasmin*` files. The extraction file itself carries no publish date; anti-pattern anchors above cite section/heading, not calendar date, for this reason.
- No `project c10c06cd` claude.ai export file exists anywhere in the repo (checked `extractions/`, full repo-wide grep for the literal string). This is a genuine absence, verified by search, not assumed.
