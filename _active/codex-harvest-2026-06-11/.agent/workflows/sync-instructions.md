---
description: Sync system intent changes
---

# /sync-instructions — Legacy Instruction Sync

Use this only when the user explicitly asks to back-port Codex system intent into legacy model reference files. Codex-native changes should start in `AGENTS.md`, `CODEX.md`, `.agent/workflows/`, `semantic_libraries/`, and `execution/` verifiers.

## Prerequisites
- A Codex-native change already exists and has been verified.
- The user explicitly wants legacy `GEMINI.md` or `CLAUDE.md` reference files updated.
- You know what intent changed, not just what text changed.

## Workflow Steps

### 1. Read active authority first
Read `AGENTS.md` and `CODEX.md` first. Then read only the relevant legacy sections of `CLAUDE.md` and `GEMINI.md`.

Understand the structural differences:
- `CODEX.md`: active Codex harness authority
- `CLAUDE.md`: prose-style instructions, implicit execution, "internalize" language
- `GEMINI.md`: checkbox checklists, explicit "YOU MUST" directives, ⛔ hard gates, priority header

### 2. Identify the intent change
Ask yourself: **What BEHAVIOR changed?** Not what text changed. Examples:
- "Added Step 3.5 to The Chain" → behavior: new step in the mandatory sequence
- "Added a new expert to routing" → behavior: new domain→expert mapping
- "Changed finalize command format" → behavior: different CLI invocation

### 3. Translate only for legacy reference
Apply these translation rules only when the user asked for a Gemini legacy reference update:

| Claude format | Gemini translation |
|---------------|-------------------|
| "Internalized — no file reads required" | "Execute this step. Print your output. Do NOT skip." |
| "Complete these steps IN ORDER" | "□ Step N: [action] — YOU MUST [specific output]" |
| Prose paragraph describing behavior | Numbered list with explicit output format |
| "This is non-negotiable" | "⛔ HARD GATE: [specific consequence if skipped]" |
| "The workflow incorporates the chain internally" | "The Chain STILL RUNS. The workflow IS Step 5. Steps 1,3,4,6 still execute." |
| Implicit priority | Explicit numbered priority in INSTRUCTION PRIORITY ORDER section |

### 4. Apply the legacy change
Edit `GEMINI.md` or `CLAUDE.md` only as a reference mirror. Do not make either file primary Codex routing authority.

### 5. Verify structural consistency
After editing, check:
- [ ] `GEMINI.md` still has the INSTRUCTION PRIORITY ORDER header at top
- [ ] All Chain steps still use □ checkbox format
- [ ] All mandatory behaviors use ⛔ or "YOU MUST" language
- [ ] No "internalize" language anywhere in the file
- [ ] Step 6 finalize still has hard gate language

### 6. Verify Codex authority
Run:

```bash
python3 execution/verify_codex_authority.py
```

If this fails, fix the active authority wording before finalizing.

## What NOT to sync
- `AGENTS.md` and `CODEX.md` are Codex-active and should not be overwritten from legacy files.
- Skills, workflows, and directives are model-agnostic unless they explicitly mention a model-specific tool.
- If you're unsure whether something is "intent" vs "formatting," it's formatting. Don't sync it.
