---
description: Tight Collective Genius Council preset for focused decisions
---

# /council

`/council` is a tight-mode preset of `/convene` for decisions that need multiple perspectives without maximum breadth.

Run:

```bash
python3 execution/convene.py plan "[decision or question]" --mode tight --json
```

Use the normal `/convene` contract: convene, diverge, inner council, deliberate, synthesize, learn. Keep real Codex subagents approval-gated; compile worker packets first and let the main Codex thread integrate.

For pure fact-gathering, use `/deep-research-os` or:

```bash
python3 execution/kimi_swarm.py plan "[research question]" --mode research --depth standard --json
```
