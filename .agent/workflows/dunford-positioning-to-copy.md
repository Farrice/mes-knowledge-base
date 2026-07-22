---
description: "Translate finished positioning into structured copy briefs for downstream experts (Wiebe, Sultanic, Kallaway)"
---

# /dunford-positioning-to-copy

Run the April Dunford Positioning-to-Copy Bridge workflow.

## Steps

### Step 1: Load Expert Context
// turbo
```bash
echo "Loading April Dunford positioning-to-copy bridge context..."
```

Read `skills/april-dunford-positioning/genius.md` for full extraction intelligence.

### Step 2: Execute Workflow
Read and execute `skills/april-dunford-positioning/workflows/dunford-positioning-to-copy.md`

Collect all required inputs from the user before executing.

**Execution prompts**: before producing the deliverable, check `skills/april-dunford-positioning/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
