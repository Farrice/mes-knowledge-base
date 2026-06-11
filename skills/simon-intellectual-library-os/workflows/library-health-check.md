---
description: "Run the 7-stage knowledge-base health check — contradictions, orphans, provenance, coverage, staleness, writing rules, new-entry candidates — report then action menu."
---

# Library Health Check

Monthly quality control + growth engine for any KB. The audit isn't hygiene — stage 7 (suggested new entries) is where the real value is.

## Pre-Flight Gate
- Load `genius.md` §7-Stage Health Check.
- Identify target KB (one per run; stagger multiple KBs across days for cost).
- Read the KB's schema file, changelog (what's been processed since last check), writing-rules guide, and outputs created since last check — BEFORE auditing.

## Skill Acquisition
Read `genius.md` + the target KB's own CLAUDE.md/spec.

## Execution
Phase 1 — **Audit** (report only, change nothing yet):
1. **Contradictions**: entries/articles asserting incompatible claims (name both sides, e.g., effort vs effortlessness).
2. **Broken links & orphans**: backlinks pointing nowhere; entries nothing links to.
3. **Provenance**: claims with no source; attribution drift (idea credited to the wrong thinker); studies cited without the underlying study.
4. **Coverage**: raw/ items never processed; sources marked in-progress but stalled; unaccounted files (PDFs, images).
5. **Staleness**: entries >90 days untouched — still true? Still relevant to the focus themes?
6. **Writing rules**: AI-tell violations, banned words, spelling-locale drift in the wiki layer.
7. **Growth**: suggested new entries based on gaps vs the focus themes (with reputable-source candidates) + connections between entries not yet drawn.

Produce the report into outputs/: findings per stage, severity, and a quick verdict ("unusually clean for an early-stage KB" honesty included).

Phase 2 — **Action menu**: list every actionable finding as a numbered menu. Interactive: ask which to action. Non-interactive/scheduled: action the safe ones (link fixes, writing rules, registry updates), QUEUE the judgment ones (contradiction resolution, deprecations, new entries) for approval.
Then: apply approved actions, draft approved new entries (schema-conformant, Confidence=Untested), update index/views, write the changelog entry.

## Content Type Adaptations
| KB substrate | Adaptation |
|---|---|
| Files (raw/wiki/outputs) | Orphan scan over md links; report = outputs/ page |
| Notion DB | Orphans = entries with no relations; provenance = empty Source property; report = page in hub |
| Antigravity `knowledge/` or Notion logs | First run = mostly stage 4+7 (huge unprocessed backlog → entry candidates) |

## Output Requirements
The 7-stage report + action menu + (post-approval) applied fixes, new entries drafted, changelog updated. Always state credit/token cost honestly if running scheduled.

## Quality Gate
`genius.md` §Anti-Patterns: a health check that only fixes and never grows the library = mediocre (stage 7 mandatory). Rubric Self-Maintenance ≥8 = audit yielded new-entry candidates AND nothing flagged last cycle recurs.
