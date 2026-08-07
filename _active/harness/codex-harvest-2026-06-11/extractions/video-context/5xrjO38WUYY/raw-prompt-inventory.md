# Raw Prompt Inventory

## Archive Summary

Source archive: `/Users/farricecain/Downloads/Mark Kashef-Raw Text Prompts.zip`

SHA-256: `a33039e627e0782886186d05353e0d364e7397b894c9e3967d077145ff01ebe3`

The archive contains five usable `.txt` prompt files and five macOS resource-fork files under `__MACOSX/`. Only the usable prompt files are inventoried below.

## Prompt Files

| File | Size | Lines | Role | Main target | Proof artifact | Stop shape |
|---|---:|---:|---|---|---|---|
| `01_clean_audit.txt` | 2,644 bytes | 45 | Audit and prune an agentic OS | `~/.claude/skills/`, `.claude/rules/`, `CLAUDE.md` | `AUDIT_REPORT.md` | Skill count under target, report present, no rule contradictions, or 25-turn cap |
| `02_sharpen_skill.txt` | 2,207 bytes | 43 | Improve one skill against tests | Target `SKILL.md`, `rubric.md`, `test_inputs.md` | `ITERATION_LOG.md` | 5 tests score 5/5 with progression log, or 15-turn cap |
| `03_revive_backlog.txt` | 2,358 bytes | 44 | Diagnose dormant projects | `~/Projects` subfolders | `ALIVE.md` | Every dormant folder gets a verdict, or 30-turn cap |
| `04_forge_skills.txt` | 2,573 bytes | 44 | Generate skills from repeated session patterns | Recent `~/.claude/projects/` transcripts | `FORGE.md`, generated `SKILL.md`, `SMOKE_TEST.md` | Three new skill folders exist with proof files, or 25-turn cap |
| `05_maintain_heartbeat.txt` | 2,282 bytes | 44 | Run recurring OS upkeep | `/loop 30m /goal` over `~/.claude` | `MAINTENANCE_LOG.md` | New maintenance entry and no contradictions, or 8 turns per cycle |

## Shared Prompt Pattern

Across the files, the package repeatedly uses the same control pattern:

1. A concrete filesystem target.
2. Per-item criteria.
3. A state-changing action.
4. A written proof artifact.
5. A measurable stop condition.
6. A turn cap or cycle cap.

That pattern also appears in the PDF cookbook's custom prompt template.

## Risk And Safety Notes

- `01_clean_audit.txt` and `05_maintain_heartbeat.txt` move/archive files. The source text prefers archive over deletion; downstream Codex workflows should preserve that boundary.
- `02_sharpen_skill.txt` edits a live skill. Use a rubric plus regression check before applying to important skills.
- `03_revive_backlog.txt` can modify project dependencies and READMEs. It explicitly avoids commits; keep that as a proof-first diagnostic boundary.
- `04_forge_skills.txt` creates new skill folders from transcript patterns. Treat generated skills as drafts until validated with smoke tests.
- `05_maintain_heartbeat.txt` is recurring. Do not enable a heartbeat without a visible pause/exit path and a scoped write boundary.

## PDF Companion Map

The companion PDF is 11 pages and aligns with the raw prompt files:

| PDF page | Section | Evidence use |
|---:|---|---|
| 1 | Cover / companion positioning | Establishes the cookbook as companion material to the self-improving agentic OS video |
| 2 | How to use the cookbook | Defines the six-anchor model for reliable `/goal` prompts |
| 3 | Warmup | Adds a hello-world safety test not present in the raw prompt zip |
| 4-5 | Clean | Matches `01_clean_audit.txt` |
| 6 | Sharpen | Matches `02_sharpen_skill.txt` |
| 7 | Revive | Matches `03_revive_backlog.txt` |
| 8 | Forge | Matches `04_forge_skills.txt` |
| 9 | Maintain | Matches `05_maintain_heartbeat.txt` |
| 10 | Build your own `/goal` | Generalizes the five examples into a reusable template |
| 11 | Community CTA | Promotional close; not an implementation primitive |

## Evidence Boundary

This inventory summarizes source structure and operational roles. It does not reproduce the full prompt bodies. Use the local zip file as the exact-text source when exact wording matters.

