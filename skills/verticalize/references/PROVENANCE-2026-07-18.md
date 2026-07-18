# PROVENANCE — skills/verticalize repair (Wave 3 Lane 4 Batch 17)

Anchor → source file+location table. Full claim-by-claim detail lives in `references/source-ledger.md`; this is the compact index for the conductor.

| Anchor (as it appears in genius.md / workflow files) | Source file | Location | Status |
|---|---|---|---|
| "the calibration cost of un-validated ground truth is permanent" | `skills/verticalize/SKILL.md` | line 106 | VERIFIED |
| "Don't auto-edit `routing_enforcer.py`..." | `skills/verticalize/SKILL.md` | line 107 | VERIFIED |
| "Don't ship a vertical with fewer than 5 PASS-marked samples..." | `skills/verticalize/SKILL.md` | line 108 | VERIFIED |
| "Don't duplicate brand bibles in the per-project CLAUDE.md." | `skills/verticalize/SKILL.md` | line 109 | VERIFIED |
| "Don't run /verticalize in parallel for 5+ verticals." | `skills/verticalize/SKILL.md` | line 110 | VERIFIED |
| "If fewer than 5 samples reach user-approved PASS, halt..." | `.agent/workflows/verticalize.md` | lines 140-141, Phase 3 stop condition | VERIFIED |
| "Do not auto-advance. Wait for explicit user signal." | `.agent/workflows/verticalize.md` | line 112, Phase 2.5 | VERIFIED |
| "the skip flag must be passed explicitly — not inferred" | `.agent/workflows/verticalize.md` | line 114, Phase 2.5 skip syntax | VERIFIED |
| "Does NOT support 'verticalize at scale' (5+ verticals in parallel) in v1..." | `.agent/workflows/verticalize.md` | line 234 | VERIFIED |
| slug regex `^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$` | `execution/ground_truth.py` | line 146, `init_domain()` | VERIFIED |
| Class 10 resolver, "2026-05-25" | `execution/intent_to_package.py` | lines 203, 657-702 | VERIFIED |
| "Anti-pattern: rubber-stamp gates ('Looks good, proceed?')..." | `directives/workflow-gate-convention.md` | line 22 | VERIFIED |
| "the skip flag must be passed explicitly — not inferred" (source of the workflow file's own citation) | `directives/workflow-gate-convention.md` skip-syntax rule | referenced, not directly quoted | VERIFIED |
| "the system averages toward the model's own preferences and calls that 9/10" | `feedback_auto-evolution-cant-substitute-for-ground-truth.md` (user memory store, outside repo) | body, dated 2026-05-03 | VERIFIED |
| "94-99% of finalize traces scored 8+" (2026-04-24 audit) | same card | body | VERIFIED |
| "Farrice (30-year Chicago resident) rated them 2/10... worse than a bad name is a bad name presented as a great one" | `feedback_naming-cultural-connotation-failure.md` (user memory store, outside repo) | body, dated 2026-04-11 | VERIFIED |
| "NEVER present names for a geographically-rooted brand without validating cultural connotation..." | same card | line 7 | VERIFIED |
| "Confidence must track output quality, not process adherence." | same card | how-to-apply §4 | VERIFIED |
| Plan file `i-think-the-biggest-virtual-emerson.md` exists at the path SKILL.md cites | `skills/verticalize/SKILL.md` "Related primitives" / "v1 status" | — | UNCONFIRMED — checked directly with `ls`, file absent. SKILL.md's own citation is stale; flagged in `genius.md`'s closing section and `references/source-ledger.md`, not repeated as fact. |
| Archive export contains prior discussion of this skill | `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) | full tarfile content scan, 7,720 members | UNCONFIRMED (absence) — 13 substring hits on "verticaliz," all unrelated ("verticalization" as a generic business term in other conversations). No hit discusses this skill. |

No claim in `genius.md` or the 4 workflow files lacks a row above or a corresponding entry in `references/source-ledger.md`.
