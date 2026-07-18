# Provenance — sean-kochel-design-first-build repair

All anchors below cite `extractions/sean-kochel/transcript.txt` (17,843 bytes, `wc -c` confirmed) unless noted. Verified programmatically: every quote string tested True for `quote in open(transcript.txt).read()`.

| Anchor location in genius.md | Quote / claim | Verbatim confirmed in |
|---|---|---|
| Pattern 2 (Trinity) added sentence | "there's three pieces to this system. research, design, and finally build" | transcript.txt |
| Pattern 3 (Competitor Mapping) added sentence | "An indirect competitor might be jabbing yourself with a pharmaceutical to lose weight" | transcript.txt |
| Pattern 4 (Competing Hypotheses) added sentence | "efficiency and scaleoriented approach" (note: no space between "scale"/"oriented" as transcribed) | transcript.txt |
| Hidden Knowledge 5 (Image-as-Style-Transfer) added sentence | "it kind of took that essence and turned it into an entirely new thing" | transcript.txt |
| Anti-Patterns item 1 | "you cannot hit a target that you have not defined" | transcript.txt |
| Anti-Patterns item 2 | "Any unanswered question in your plan has to be decided upon by the language model at game time" | transcript.txt |
| Anti-Patterns item 3 | "tends to give you a pretty mid-level design" | transcript.txt |
| Anti-Patterns item 4 | "Both of those approaches kind of sucked to be honest" | transcript.txt |
| Anti-Patterns item 5 | "jabbing yourself with a pharmaceutical to lose weight" | transcript.txt |
| Anti-Patterns item 6 | efficiency-vs-quality-vs-personalization split | transcript.txt (same passage as Pattern 4 anchor) |
| Quality Rubric added sentence | "4/7/10 scale (Acceptable/Good/Savant)" | `references/quality-rubric.md` header table (pre-existing file, not the transcript — a structural fact about the rubric file itself, not attributed to Kochel) |
| Hall of Fame Exemplars provenance note | Flags "SaaS Onboarding Flow," "Claymorphism Conversion Beast," "3x higher conversion rates," and the anti-exemplar as NOT present in transcript.txt or extraction-report-design-first-build.md | Negative-result check: grepped both source files for these strings/figures — absent. Labeled UNCONFIRMED in source-ledger.md rather than invented-verified. |
| "How to Use This Skill (Model Calibration)" section | Original synthesis (not a transcript quote); grounded in transcript's demo-narration tone, not itself a sourced factual claim | Labeled LIKELY in source-ledger.md |

## Absence check (Rule 2 of the envelope — false "unrecoverable" claims are themselves a provenance failure)

Before writing anything, ran:
- `ls extractions/ | grep -i kochel` → found `extractions/sean-kochel/` (shared with sibling skill `sean-kochel-ai-business`, which another worker owns — I only read, did not modify anything under `extractions/`).
- `wc -c extractions/sean-kochel/transcript.txt extractions/sean-kochel/extraction-report-design-first-build.md` → 17,843 bytes and 13,417 bytes respectively — both non-empty, no 0-byte or truncation risk. Full read of both files performed (not skimmed).
- Both files fully read end-to-end; no `_archive/claude-export-2026-07-01.tar.gz` scan was needed because extractions/ was non-empty and sufficient — recorded here per the discipline requirement, not because the archive was searched.
