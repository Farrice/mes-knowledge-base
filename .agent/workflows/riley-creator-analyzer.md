---
description: "/riley-creator-analyzer — The surpass-Riley analysis pass — take a scraped creator corpus and write a per-post 'why it works' verdict grounded in a named hook lens, excluding sponsored posts with retained evidence. Riley's workflow stops at raw data; this adds the judgment."
---

# /riley-creator-analyzer — Why-It-Works Analysis Pass

Thin wrapper — the full methodology lives in the skill.

## Steps
1. Load the spine: read `skills/riley-brown-marketing-automation/genius.md` (patterns, signature moves, Anti-Patterns, Recognition Test).
2. Read and execute `skills/riley-brown-marketing-automation/workflows/riley-creator-analyzer.md` exactly as documented — honoring the execution prompt `skills/riley-brown-marketing-automation/references/prompts-v2/creator-why-it-works-analysis.md`.
3. Run the workflow's Quality Gate before delivering.
