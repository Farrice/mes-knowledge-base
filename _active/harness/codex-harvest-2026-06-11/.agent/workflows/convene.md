---
description: Collective Genius Council - Codex-native council casting, deliberation packets, synthesis, grounding, and learning digest
---

# /convene - Collective Genius Council

Use `/convene` for creative, strategic, judgment-heavy, or general-purpose intelligence work where several expert lenses should become one integrated outcome.

Do not use it as a competing super-router. `/virtuoso` remains the orchestration composer, `/deep-research-os` owns pure research, and `/convene` owns collective-genius/general council work.

## Codex-Native Execution

Compile the council packet plan:

```bash
python3 execution/convene.py plan "[task]" --mode wide --json
```

Equivalent Kimi bridge:

```bash
python3 execution/kimi_swarm.py plan "[task]" --mode general --convene-mode wide --json
```

Real Codex subagents are approval-gated. By default, this workflow prepares worker packets and a delegation receipt; the main Codex thread integrates the final result.

## Contract

1. **Convene** - `execution/council_cast.py` selects diverse experts, caps domains, adds wildcards, seats Farrice's lens, and resolves `genius.md` references.
2. **Diverge** - each voice gives an independent take before seeing other voices.
3. **Inner Council** - choose the most complementary voices, preserving productive tension.
4. **Deliberate** - run two rounds of build, challenge, cross-pollination, and fork preservation.
5. **Synthesize** - produce one integrated outcome and run `execution/grounding_guard.py` on factual strategy output.
6. **Learn** - write a "How the Masters Thought" digest to `knowledge/council-sessions/` and append one reusable mental model to `knowledge/council-rubric.md`.

## Modes

| Mode | Use For | Presets |
|---|---|---|
| `wide` | Default big creative or strategy problem | `/convene`, `/campaign` first pass |
| `tight` | Focused decision or roundtable | `/council`, `/roundtable` |
| `strike` | Fast focused 3-4 voice pass | `/strike` |
| `deploy` | Maximum breadth before synthesis | `/deploy-council`, `/jcc-deploy` |

## Output Standard

The synthesis must include:

- The Outcome
- Why It Is More Than The Parts
- Forks For Farrice
- Next Moves We Make Together
- What We Would Have Missed
- Grounding Guard verdict when factual claims appear
- Learning digest path and rubric update when a full council run completes

## Compatibility Source

The original Claude Workflow source is preserved at `.agent/workflows/collective-genius-council.workflow.js` with the Codex workspace root. Codex-native execution uses `execution/convene.py` and `execution/kimi_swarm.py`.
