# Creative Strategy Learning Ledger

The live append-only evidence ledger is `.agent/creative-strategy-learning-events.jsonl`. This directory documents its contract; it does not create a parallel memory store.

Each line is one immutable record:

- `event`: finalized artifact, project, strategist, workflow, hypothesis, mechanic, audience, format, sources, outcome target, and `NO_EVENT` state;
- `outcome`: metric, value, baseline, window, test design, proof state, proposed lesson, and contradiction pointer;
- `feedback`: explicit human verdict, exact note, and project-scoped candidate lesson.

Current state is folded by `execution/creative_intelligence.py`. Human-approved candidates are promoted through `execution/memory_review.py` into sovereign semantic memory, where both Claude and Codex can retrieve them.

Useful commands:

```bash
python3 execution/creative_intelligence.py status
python3 execution/creative_intelligence.py synthesize
python3 execution/creative_intelligence.py synthesize --run
python3 execution/memory_review.py list
python3 execution/creative_intelligence.py recall "trigger event" --project <slug>
```
