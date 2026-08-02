---
description: /generate — in-house pay-as-you-go creative generation front door (image/video/audio via model recipes; Higgsfield replacement). Routes, quotes, generates, logs, refreshes the asset board.
---

# /generate — Creative Generation Front Door

Read and follow `skills/generate/SKILL.md` (the behavior contract: binding-lane deference,
quote-before-paid-video, prompt-level budgets, comparison runs, index-after-wrapper).

Quick reference:

```bash
python3 execution/creative_router.py route --task "<brief>"     # binding lanes first
python3 execution/generate_media.py models                       # live model registry
python3 execution/generate_media.py quote --model <id> --prompt "…"   # never spends
python3 execution/generate_media.py run --model <id> --prompt "…" [--run-id gen-X --run-budget 3.00] [--project <slug>]
python3 execution/generate_media.py index --file <out> --model <id> --prompt "…" [--cost N]
```

Hard rules (from SKILL.md, non-negotiable): paid video quotes first and waits for Farrice's
explicit go · seedance-1080p never runs · prompt budgets are ceilings Farrice set · one code
path per model (wrapper-backed recipes refuse `run` and print the wrapper command).

Results land on the Asset Command Center — `/assets-board` or `open .agent/assets/assets-board.html`.
