---
description: Sync system intent changes from CLAUDE.md to GEMINI.md without breaking model-native formatting
---

# /sync-instructions — Cross-Model Instruction Sync

When you change system intent in `CLAUDE.md` (add a chain step, modify routing, update architecture), this workflow translates the change into each model's native format.

## Prerequisites
- A change has been made to `CLAUDE.md`
- You know what intent changed (not just what text changed)

## Workflow Steps

### 1. Read both files
Read `CLAUDE.md` and `GEMINI.md` in full. Understand the structural differences:
- `CLAUDE.md`: prose-style instructions, implicit execution, "internalize" language
- `GEMINI.md`: checkbox checklists, explicit "YOU MUST" directives, ⛔ hard gates, priority header

### 2. Identify the intent change
Ask yourself: **What BEHAVIOR changed?** Not what text changed. Examples:
- "Added Step 3.5 to The Chain" → behavior: new step in the mandatory sequence
- "Added a new expert to routing" → behavior: new domain→expert mapping
- "Changed finalize command format" → behavior: different CLI invocation

### 3. Translate to Gemini format
Apply these translation rules to the changed intent:

| Claude format | Gemini translation |
|---------------|-------------------|
| "Internalized — no file reads required" | "Execute this step. Print your output. Do NOT skip." |
| "Complete these steps IN ORDER" | "□ Step N: [action] — YOU MUST [specific output]" |
| Prose paragraph describing behavior | Numbered list with explicit output format |
| "This is non-negotiable" | "⛔ HARD GATE: [specific consequence if skipped]" |
| "The workflow incorporates the chain internally" | "The Chain STILL RUNS. The workflow IS Step 5. Steps 1,3,4,6 still execute." |
| Implicit priority | Explicit numbered priority in INSTRUCTION PRIORITY ORDER section |

### 4. Apply the change to GEMINI.md
Edit `GEMINI.md` with the translated version. Do NOT copy-paste from `CLAUDE.md`.

### 5. Verify structural consistency
After editing, check:
- [ ] `GEMINI.md` still has the INSTRUCTION PRIORITY ORDER header at top
- [ ] All Chain steps still use □ checkbox format
- [ ] All mandatory behaviors use ⛔ or "YOU MUST" language
- [ ] No "internalize" language anywhere in the file
- [ ] Step 6 finalize still has hard gate language

### 6. Show diff for approval
Present the before/after of `GEMINI.md` for user approval before saving.

## What NOT to sync
- `AGENTS.md` stays as Claude-format default (for Cursor, Windsurf, other AI tools)
- Skills, workflows, and directives are model-agnostic — no sync needed
- If you're unsure whether something is "intent" vs "formatting," it's formatting. Don't sync it.
