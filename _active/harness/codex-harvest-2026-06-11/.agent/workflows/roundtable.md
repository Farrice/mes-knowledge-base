---
description: Tight Collective Genius Council preset for expert roundtables
---

# /roundtable

`/roundtable` is a tight-mode preset of `/convene` for structured expert discussion.

Run:

```bash
python3 execution/convene.py plan "[topic]" --mode tight --json
```

Codex behavior:

- independent opening takes before anchoring
- complementary inner-council selection
- two rounds of cross-talk in the main thread or approved workers
- one integrated synthesis with dissent/forks preserved
- grounding guard for factual claims

Real Codex subagents require explicit approval per run. Without that approval, treat the generated worker packets as briefs for main-thread execution.
