# PROVENANCE — alen-sultanic-copywriting repair

Anchor → source file + location. Full labels/reasoning in
`references/source-ledger.md`; this table is the quick-lookup index.

| Anchor added in this repair | Source file + location | Label |
|---|---|---|
| Anti-Patterns (Sourced) — all 7 bullets | `genius.md` lines 177-179 (pre-existing "Patterns from claude.ai export... 2026-07-01" source line, Patterns 19-22 + Hidden Knowledge 8, same file) | LIKELY |
| Pattern 4 example quote ("You clock in, you clock out...") | `genius.md` Hall of Fame Exemplar 2 (pre-existing, same file) | UNCONFIRMED (illustrative copy, not Alen's real words — labeled honestly) |
| Pattern 6 example ($9,997 launch) | `genius.md` Hall of Fame Exemplar 1 (pre-existing, same file) | UNCONFIRMED |
| Pattern 9 example ($2,997 masterclass, "unseen mechanics") | `genius.md` Hall of Fame Exemplar 3 (pre-existing, same file) | UNCONFIRMED |
| Pattern 15 example (10% income threshold cross-ref) | `genius.md` Pattern 11 (pre-existing, same file) | UNCONFIRMED |
| Hidden Knowledge 1-5 "Example"/"Metric" additions | `genius.md` Hall of Fame Exemplars 1-3, Pattern 10 (pre-existing, same file) | UNCONFIRMED |
| Big-Idea Trap deploy-line cross-ref | `genius.md` Pattern 3, Pattern 22 (pre-existing, same file) | UNCONFIRMED |
| Expert-Specific Quality Rubric rows | `genius.md` Patterns 1, 3, 19, 22, 23 (pre-existing, same file) — table was structurally broken (header row only, no data rows, no separator); completed it using only patterns already present | UNCONFIRMED (patterns) / structural fix (table itself) |
| Model Calibration section citations | `genius.md` Pattern 1, Pattern 19, Hidden Knowledge 1, Hidden Knowledge 10 (pre-existing, same file) | Same labels as cited patterns |
| Evolution Log cross-pollination claim (untouched, verified as part of audit) | `skills/chris-cimorelli-copywriting/genius.md` line 145 | VERIFIED (confirmed by direct read) |

## What was NOT touched
- All 9 workflow files (`workflow_contracts` already PASS — untouched).
- `SKILL.md` (no failing check required a SKILL.md edit; `recognition_test`
  was satisfied in `genius.md` per the auditor's OR logic).
- Patterns 1-18, Hidden Knowledge 1-7, Hall of Fame Exemplars, Anti-Exemplar,
  Signature Moves text itself — content preserved verbatim; only additive
  "Example"/"Metric" lines were appended for the named-entity floor.

## Absence verification (file reads + `wc -c`, not `wc -l`)
- `extractions/` — no `alen`/`sultanic` match: `ls extractions/ | grep -i sultanic` → empty.
- No raw transcript for "2 Hour Copywriting Masterclass" or "Emily June Wilcox"
  found on disk: `find . -iname "*emily*wilcox*" -o -iname "*2*hour*copywriting*"
  -o -iname "*NHB*" -o -iname "*FastForward*"` → empty (excluding worktrees).
  `_active/claude-export/` index/harvest/triage JSON + `reports/harvest-roadmap.md`
  grepped for "sultanic" → zero matches.
- `agents/alen-sultanic/AGENT.md` — 2,737 bytes, read in full, no source date.
- `research_outputs/ai_authority_architect_agents/alen_sultanic.md` — 9,504
  bytes, read in full — self-flagged UNCONFIRMED by its own 2026-06-02
  grounding-verification note; not used as an anchor.
