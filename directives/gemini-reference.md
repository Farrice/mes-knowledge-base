# Gemini Reference — Read On Demand

> This file contains reference material stripped from GEMINI.md to save context budget. Read sections as needed, not upfront.

## Directory Conventions

- **Skills** (`skills/[name]/`): `SKILL.md` + `genius.md` + `workflows/*.md`
- **Agents** (`agents/[name]/`): `AGENT.md` + `memory/` directory
- **Agent framework** (`agents/_framework/`): `invocation-cards.md`, `AGENT_TEMPLATE.md`, `orchestrator.md`
- **Workflows** (`.agent/workflows/`): invoked via `/command`, `@command`, "run command", or bare name

## File Organization

- `.tmp/` — intermediates (never commit)
- `execution/` — deterministic Python scripts
- `directives/` — SOPs and protocols
- `extractions/` — raw extraction reports
- `knowledge/` — organized knowledge base
- `councils/` — council configurations
- `research_outputs/` — research outputs
- `strategy_briefs/` — strategic dossiers
- `deliverables/` — client deliverables
- `products/` — product builds
- `projects/` — active projects

## Execution Scripts

```bash
python execution/notion_api.py query <database_id>
python execution/notion_api.py capture "Title" "Body" --type Task --tags Revenue,Urgent
python execution/parallel_swarm.py "objective"       # --grounded, --research
python execution/generate_image.py "prompt"
python execution/skill_converter.py
python execution/sync_registries.py
```

## Knowledge Sources

- **Local Files**: Skills, agents, directives (primary)
- **Notion Databases**: 5 databases for projects, knowledge vault, content pipeline
- **NotebookLM**: 5 research notebooks (100 queries/month, tracked in `.agent/notebooklm-usage.json`)
- **Perplexity**: Real-time web research ($30/month, tracked in `.agent/perplexity-usage.json`)

**Key files (read on-demand):**
- `COUNCIL.md` — 24 experts + 5 councils
- `DOMAIN_REGISTRY.md` — Expert swim lanes
- `JARVIS.md` — Expert invocation protocol
- `FARRICE.md` — Personal context, identity, voice

## Context Engine Tiers

| Tier | What to Read | When |
|------|-------------|------|
| Hot | Nothing (already loaded) | Expert loaded earlier this conversation |
| 0 — Card | `agents/_framework/invocation-cards.md` | Routing decisions only |
| 1 — Standard | SKILL.md + specific workflow | Single expert, clear task |
| 2 — Deep | + genius.md | Creative/complex work |
| 3 — Sub-Agent | Spawn fresh context | 7+ files loaded, or multi-expert |

Anti-pattern: Re-reading SKILL.md for the same expert twice = ~1,350 wasted tokens.

## Supporting Protocols

| Protocol | Fires During | Directive |
|----------|-------------|-----------|
| Quality Assurance | Step 5 | `directives/quality_assurance.md` |
| Token Efficiency | Every workflow | `directives/token-efficiency-protocol.md` |
| Session State | After Step 4, after 7+ reads | `directives/session-state-protocol.md` |
| Self-Annealing | On any error | `directives/deep_self_annealing.md` |
| Collaboration | Always | `directives/collaboration-protocol.md` |
| Sub-Agent | 7+ files loaded, or 2+ experts | `directives/sub_agent_protocol.md` |
| Content Gate | Step 4, content tasks | `directives/content_creation_gate.md` |

### Budget-Gated
| Protocol | Directive | Gate |
|----------|-----------|------|
| Perplexity | `directives/perplexity-usage-policy.md` | $30/mo |
| NotebookLM | `directives/notebooklm-usage-policy.md` | 100/mo |
