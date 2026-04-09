# AGENTS.md — Antigravity

## Env
`.env` at root = `NOTION_API_KEY`. Python: `python-dotenv`, `requests`. Notion: ONLY `execution/notion_api.py` (pins `2022-06-28`), never JS client. DB schemas: `directives/notion-databases.md`. Scripts from root; check `execution/` first.

## Layout
`skills/[name]/`: SKILL.md+genius.md+workflows | `agents/[name]/`: AGENT.md+memory | `.agent/workflows/`: `/cmd`→reads file | `execution/` `directives/` `extractions/` `knowledge/` `councils/` `deliverables/` `.tmp/`(no commit)

## Artifact Rule
User-facing deliverable = conversation artifact (`brain/<id>/`, IsArtifact:true). Workspace copy optional. System files exempt.

# The Chain — Every Deliverable

1. **SCORE** 1-5: +Deliverable +Audience +Context +End-state +Specificity
2. **SHARPEN** if≤3: DICE dimensions, 1 round (`directives/intent-pipeline.md`)
3. **ROUTE**: LI→Lara|Copy→Luke|SEO→Gotch|Brand→Oren/Grace|Ghost→Cole|Psych→Kallaway|Consumer→Dai|Agentic→Saraev. Multi: `directives/expert_auto_routing.md`
4. **LOAD**: T0→T1(SKILL+workflow)→T2(+genius)→T3(sub-agent). Hot=skip. Content: 2+ files. Never produce unloaded.
5. **PRODUCE**: Expert thinking not terminology. `directives/quality_assurance.md`
6. **FINALIZE**: `python3 execution/chain_runner.py finalize "[output]" --expert X --skill X --workflow X --type X --intent X --expert-score X --adversarial X --notes "X"` — composite<7 or dim<6 → retry

**Narrow:** ≥4 skip S2. Follow-up reuse S3. No deliverable=no chain. Trivial≠skip. Tier 1 default.

## Arch
L1 directives → L2 you (route/decide) → L3 execution (Python). Sources: local|Notion(5 DBs)|NotebookLM(5nb,100/mo,`/query-notebook`)|Perplexity. On-demand: COUNCIL.md DOMAIN_REGISTRY.md JARVIS.md FARRICE.md

## Context
Hot(0)→T0(cards,80)→T1(SKILL+wf,1350)→T2(+genius,2550)→T3(subagent,300). Hot first. Hot@T1+needT2=only genius.md. Never re-read same expert.

## Directives
`directives/` — fire at trigger, don't preload. Key: quality_assurance, quality_gate, content_creation_gate, agent-loading-protocol, intent-pipeline, session-state-protocol. Session: `.agent/session-state.md` after intent/deploy/decisions/10+reads. Read post-compaction.
