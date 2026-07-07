# Skill Architecture — mark-kashef-wargame-os

**Checkpoint 2 artifact** · forge Phase 4 · 10 workflows, 3 tiers, prefix `/wargame-*`

## Core Files

- `SKILL.md` — manifest, workflow table, stacking guide, quick reference
- `genius.md` — unified genius context (patterns, hidden knowledge, exemplars, signature moves, quality rubric)
- `references/eight-point-standard.md` — the SUCCESS.md rubric, annotated (what each point catches, how to grade)
- `references/mission-brief-library.md` — the 10 domain briefs adapted to Antigravity conventions (placeholders → system pointers, e.g. ICP → deep-icp profile)
- `references/source-quotes.md` — verbatim ledger (embodiment standard requirement)
- `assets/wargame-folder-template/` — the folder contract (tasks/, wargames/, SUCCESS.md, LEDGER.md) adapted: mission dirs live under `.agent/missions/<name>/wargames/`

## Workflow Table

| # | Workflow | Tier | Produces | Stacks with |
|---|---|---|---|---|
| 1 | `wargame-order` | 1 Foundation | A complete wargame order (template + mission brief) from any goal — the front door | — |
| 2 | `wargame-run` | 1 Foundation | The fought-on-paper wargame file: moves, observations, failures, counter-moves, forks, RECON NEEDED, aborts, verification runs | routing: frontier/highest-tier model does this step |
| 3 | `wargame-grade` | 1 Foundation | Point-by-point grade vs 8-point standard + red-team pass + patches, logged to ledger | mark-kashef-ai-councils (red-team as council) |
| 4 | `wargame-execute` | 1 Foundation | Execution by a cheaper model with the wargame as its route; ledger entry on completion | Opus-fallback policy; Workflow engine |
| 5 | `wargame-batch` | 2 Practitioner | Laundry-list → all missions drafted before any polished (the /goal contract), then refinement loop | /loop |
| 6 | `wargame-recon` | 2 Practitioner | Knowns/unknowns elicitation — pull unknown-knowns (tacit) + unknown-unknowns (unasked questions) before the wargame is written | — |
| 7 | `wargame-executor-fit` | 2 Practitioner | Wargame tailored to a named executor model via its docs/system card | claude-code-guide agent |
| 8 | `wargame-brief` | 2 Practitioner | A mission brief that passes the executable-blind bar (self-interest copy discipline for the executor: outcome, constraints, verification paths, "simplest thing that works") | luke-iha briefs, copy-engine |
| 9 | `wargame-mission` | 3 Stacking | Wargame layer as optional pre-flight on a /swarm / /supercomputer mission | swarm, supercomputer (option, never forced) |
| 10 | `wargame-client` | 3 Stacking | Client-deliverable wargame: sold work simulated once at frontier tier, executed repeatedly at cheap tier | jen-santulan, andrea, mybpm CLAUDE.md contexts |

## Slash Wrappers

`.agent/workflows/wargame-<name>.md` for all 10. No collisions found (`grep -i wargame` clean).

## Registration

- `AGENT_INDEX.md`: mark-kashef row gains "wargame OS" capability note
- `SKILL_INDEX.md`: new entry `mark-kashef-wargame-os`
- `agents/mark-kashef/AGENT.md`: Available Skills table + Skill Integration additions
- `agents/mark-kashef/memory/context.md`: expansion note

## Build Delegation Plan (orchestrator mode)

- **Opus subagent**: MES 3.0 deep extraction → genius.md raw material (patterns, hidden knowledge, exemplars, signature moves, rubric)
- **Sonnet subagent A**: Tier 1 workflows (1-4) from genius.md + templates
- **Sonnet subagent B**: Tier 2+3 workflows (5-10) + references
- **Fable (me)**: SKILL.md, genius.md final synthesis, registration, verification, blind-pass, finalize
- Sequencing: extraction → genius.md synthesis → parallel builders (contracts pinned in genius.md first, per solution card 2026-07-07-parallel-builders-stale-contracts: builders read finished genius.md + this architecture file, not each other)
