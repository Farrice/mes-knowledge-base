---
description: Audit an existing Claude Code system (incl. Antigravity itself) against the ladder — level 3/4 mechanics gap list, stacked with boris-claude-code
---

# System Ladder Audit — Apply the Ladder to the Harness Itself

Tier-3 stacking workflow: runs the ladder diagnostic against a *built system* (CLAUDE.md, hooks, routines, skills, memory) rather than a person's habits. Primary internal use: auditing Antigravity's own orchestration layer. Stacks with `boris-claude-code` (philosophy) and `directives/orchestration-doctrine.md` when auditing this repo.

## Pre-Flight Gate

Load `genius.md` + `references/boris-ladder-source.md`. Read the ACTUAL system files (CLAUDE.md, hook configs, routine/cron definitions, lifecycle-adjacent directives) — never audit from memory of the system. For Antigravity: also load `directives/orchestration-doctrine.md` and the hooks table in CLAUDE.md.

## Skill Acquisition

- `genius.md` — all 12 patterns as the checklist source
- `references/boris-ladder-source.md` — L3 tooling column (subagents+worktrees, routines//loop//batch//goal, dynamic workflows, channel monitoring) and L4 column (Agent SDK scheduling, chat-bot ubiquity)

## Execution

1. **Map existing mechanics to ladder cells**: for each of — self-verification loops · automated review with severity routing · capped repair loops · context pull-in (wikis/memory) · loops and routines running unattended · proactive kickoff (Claude kicks off Claude) · monitor-by-exception — record: EXISTS (where) / PARTIAL (gap) / MISSING.
2. **Score the system's level** with the two-test challenge applied to the system's own outputs (do deliverables ship with artifact receipts? is review automated or ritual?).
3. **Find the Ray-shaped upgrades**: which of his mechanisms would close each PARTIAL/MISSING cell — quote the mechanism, name the file/hook it would live in.
4. **Check the trust ledger**: for each autonomous loop already running, is there evidence it earned trust (manual runs, failure maps) or was autonomy granted by optimism? Flag optimism-granted loops.
5. **Rank upgrades by unlock** (Boris's unlock column as the value scale), cap the list at 5 — density over completeness.

## Content Type Adaptations

| System | Adaptation |
|---|---|
| Antigravity (this repo) | Cross-reference orchestration-doctrine seating + wargame failure maps as the trust ledger; flag upgrades as EXTEND-not-rebuild per system memory |
| Client's Claude Code setup | Output doubles as the technical annex of an `adoption-brief` |
| Bare/new setup | Skip audit; route to `level-up-plan` from Level 1 |

## Output Requirements

Audit card: mechanics table (cell · status · where) · system level with two-test evidence · top-5 upgrade list (mechanism → target file → unlock) · optimism-granted-autonomy flags.
Execution prompt: `references/prompts-v2/system-ladder-audit.md` — honor its Output Contract.

## Quality Gate

Reject if: audited from memory instead of files; >5 upgrades (bloat); any upgrade not mapped to a concrete file/hook; trust-ledger check skipped; rebuild proposed where extend suffices.
