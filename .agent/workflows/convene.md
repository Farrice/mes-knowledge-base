---
description: Convene the Collective Genius Council — diverse cross-domain experts deliberate, synthesize, and teach
---

# /convene — Collective Genius Council

The reliable multi-expert orchestrator for ANY creative / intelligence / knowledge work
(use `/deep-research` instead when the job is fact-gathering). Convenes a deliberately
diverse, cross-domain council — experts who don't normally work together — plus **your own
lens** (FARRICE.md), has them genuinely **deliberate** (cross-talk, not just parallel takes),
synthesizes an outcome none could reach alone, and emits a **"How the Masters Thought"**
learning digest so you level up by watching them work. $0 incremental; holds the grounding floor.

## Usage
```
/convene [task or question]
/convene --mode wide  "design the offer + launch narrative for X"
```

## How to run it
This command fronts the reliable engine. Execute it by invoking the **Workflow tool** with:
- `scriptPath`: `.agent/workflows/collective-genius-council.workflow.js`
- `args`: `{ "task": "<the user's task>", "mode": "<mode>" }`

### Modes (the presets all map here)
| Mode | Shape | Fronted by |
|---|---|---|
| `wide` | 12 voices diverge → 6 deliberate (default for big creative problems) | `/convene` |
| `tight` | 6-7 voices → 4 deliberate (focused decision) | `/council`, `/roundtable` |
| `strike` | 3-4 voices, fast, no wide pass | `/strike` |
| `deploy` | 16 voices → 6 deliberate (max breadth) | `/deploy-council` |
| `wide` + multi-deliverable | wide council, then hand execution to `/supercomputer` | `/campaign` |

## What it does (phases)
1. **Convene** — `council_cast.py` selects a diverse roster (relevance + per-domain cap + 1-2
   cross-pollination wildcards) and seats Farrice; resolves each member's `genius.md`.
2. **Diverge** — every voice gives an independent take (no anchoring).
3. **Inner-Council** — selects the most COMPLEMENTARY voices (max productive tension).
4. **Deliberate** — 2 rounds of genuine cross-talk, genius-loaded: build on / challenge /
   cross-pollinate; contradictions PRESERVED (forks surfaced for you), never blended to mush.
5. **Synthesize** — an outcome that exceeds any single voice, built on the net-new principle,
   with forks for you + next moves we make together. Grounding floor checked.
6. **Learn** — a "How the Masters Thought" digest → `knowledge/council-sessions/<date>-<slug>.md`
   + one distilled line appended to the growing `knowledge/council-rubric.md`.

## When NOT to use
- Pure fact-gathering → `/deep-research` (the research swarm).
- Single-expert, clear task → invoke that expert/skill directly.
