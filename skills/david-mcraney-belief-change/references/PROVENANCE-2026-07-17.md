# PROVENANCE — david-mcraney-belief-change repair (Wave 3 Lane 4 Batch 4)

Anchor → source file + location table for every quote/claim added during this repair. All quotes were verified verbatim (`grep -F`) against the cited source file before use — see the terminal check log summarized below.

| Anchor (as it appears in genius.md) | Source file | Location | Verified verbatim? |
|---|---|---|---|
| "The better your argument, the *more* the other person assimilates it into their existing framework without changing." | `references/hidden-knowledge.md` | Item #1, Tacit Insight line | YES — `grep -F` match |
| "the hardest skill isn't what to say — it's learning when to stop talking." | `references/hidden-knowledge.md` | Item #6, Why Others Miss This line | YES — `grep -F` match |
| "how did you arrive at this?" (process question) vs "why do you believe this?" (content question) | `references/spencer-greenberg-interview-notes.md` | Item 3, "Metacognition as Master Mechanism" | YES — `grep -Fi` match |
| "Transparency fixes technique rebuttals but looks desperate on topic rebuttals. Evidence fixes topic rebuttals but confirms suspicion on technique rebuttals." | `references/spencer-greenberg-interview-notes.md` | Item 2, "Technique Rebuttal vs Topic Rebuttal", Critical insight line | YES — `grep -F` match |
| "If you've hit 30% evidence and nothing's changing, STOP adding evidence. The barrier is social/identity cost, not information deficit." | `references/spencer-greenberg-interview-notes.md` | "The 30% Tipping Point" item, Operational implication line | YES — `grep -F` match |
| "you can't remove a load-bearing belief without either replacing it with something equally strong or restructuring the entire system it supports." | `references/hidden-knowledge.md` | Item #7, Why Others Miss This line | YES — `grep -F` match |
| "Focus groups are especially bad — people perform for each other." | `references/hidden-knowledge.md` | Item #5, Why Others Miss This line | YES — `grep -F` match |
| Pattern 13's "Empirical calibration" note (30% baseline, 70-80%+ in tribal/identity-fused contexts) — reused in Pattern 16 and Pattern 1 additions as a self-consistent cross-reference, not a new claim | `skills/david-mcraney-belief-change/genius.md` (pre-existing, untouched text) | Pattern 13 body | YES — pre-existing in the graded file, not introduced by this repair |
| 12 "Example" / "Diagnostic Question" additions to entity-floor-failing sections (Patterns 1, 4, 12, 16, 24; Hidden Knowledge 2, 3, 5, 6, 7, 9, 10) | Authored illustrative scenarios, same house style as pre-existing Pattern 9 ("$X in 3 months") and accommodation-audit.md ("$10-50K") examples | N/A — craft illustration, not a factual claim | N/A (no source needed; flagged in source-ledger.md as N/A) |
| "How to Use This Skill (Model Calibration)" section | Modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per the ENVELOPE's explicit instruction; content is original craft-calibration prose for McRaney specifically | N/A — instructional prose, not a factual claim | N/A |
| 10 new "## Output Schema" sections in workflows/*.md | Each describes only that workflow's own pre-existing Output/Phase blocks (re-read in full before writing) | Within each workflow file itself | YES — self-referential, no external claim |

## Absence claims (verified, not assumed)

| Claim | How verified |
|---|---|
| No `extractions/` folder or file matches "mcraney" (repo root or `_active/codex-harvest-2026-06-11/extractions/`) | `ls extractions/ \| grep -i mcraney` (empty) + repo-wide `grep -ril "mcraney" . \| grep -v skills/david-mcraney-belief-change/` (only hit: `_active/codex-harvest-2026-06-11/agents/david-mcraney/AGENT.md`, a derivative persona file, read in full, not a raw transcript) |
| No McRaney content in `_archive/claude-export-2026-07-01.tar.gz` | `tar -tzf _archive/claude-export-2026-07-01.tar.gz \| grep -i mcraney` against the full 332,779,255-byte archive's file index — zero matches, exit 0 (command succeeded, list was empty, not a failure being misread as absence) |

## Files read in full before repair (source-grounding pass)

- `skills/david-mcraney-belief-change/SKILL.md`
- `skills/david-mcraney-belief-change/genius.md` (original, pre-repair)
- `skills/david-mcraney-belief-change/references/genius-patterns.md`
- `skills/david-mcraney-belief-change/references/hidden-knowledge.md`
- `skills/david-mcraney-belief-change/references/spencer-greenberg-interview-notes.md`
- `skills/david-mcraney-belief-change/references/prompts-v2/5_pluralistic_ignorance_breaker.md` (house-style reference for Output Contract/Skeleton/Quality Gate pattern)
- All 14 files in `skills/david-mcraney-belief-change/workflows/` (full content, to confirm which 4 already passed and to build accurate Output Schema sections for the 10 that didn't)
- `_active/codex-harvest-2026-06-11/agents/david-mcraney/AGENT.md` (cross-check only, not used as a repair source)
- `execution/skill_auditor.py` (heartbeat_checks function + all six regex definitions, to target fixes precisely rather than guess)
