# Walkthrough: Multi-Model Antigravity — GEMINI.md Optimization

## What Was Done

### Phase 1: Harness Audit
Ran Nate B. Jones harness audit methodology against the instruction file architecture. Found 7 gaps where Claude's implicit instruction processing differs from Gemini's explicit requirements.

### Phase 2: Expert Ensemble Assembly
Loaded Tier 2 context for 3 experts:
- **Boris** → Bitter Lesson for Product: minimal scaffolding, one file, don't over-engineer
- **Lance & Yichao** → Context Engineering: reduce instruction density, not add more
- **Nate B. Jones** → 7 harness gaps as specific translation targets

### Phase 3: GEMINI.md Rewrite
Applied 5 translation categories to create a Gemini-native instruction file:

| Category | Before (Claude mirror) | After (Gemini-native) |
|----------|----------------------|----------------------|
| Execution directives | "Internalized — no file reads" | "YOU MUST print your score" |
| Chain format | Prose paragraphs | □ Step N: checkbox format |
| Priority | Implicit | Explicit numbered precedence header |
| Finalize enforcement | "Non-negotiable" | ⛔ HARD GATE with consequences |
| Workflow override | "Incorporates chain internally" | Separate section: "Chain STILL RUNS" |

### Phase 4: Maintenance Workflows
Created 2 new workflows to prevent future drift:
- `/sync-instructions` — translation table + verification checklist for keeping `GEMINI.md` aligned with `CLAUDE.md` intent changes
- `/test-model-compliance` — 3 test prompts + A/B/C/F grading to verify Chain compliance

## Files Changed

| File | Change | Lines |
|------|--------|-------|
| [GEMINI.md](file:///Users/farricecain/Google%20Antigravity/GEMINI.md) | Complete rewrite — model-native format | 264 |
| [CLAUDE.md](file:///Users/farricecain/Google%20Antigravity/CLAUDE.md) | Comment only — sync note replaces mirror note | 217 |
| [AGENTS.md](file:///Users/farricecain/Google%20Antigravity/AGENTS.md) | Comment only — sync note replaces mirror note | 217 |
| [sync-instructions.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/sync-instructions.md) | NEW — maintenance workflow | 52 |
| [test-model-compliance.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/test-model-compliance.md) | NEW — compliance test workflow | 62 |

## Verification Results

- ✅ `CLAUDE.md` body untouched (only sync comment updated)
- ✅ `AGENTS.md` body untouched (only sync comment updated)
- ✅ `GEMINI.md` rewritten with all 5 translation categories
- ✅ Both maintenance workflows created
- ⏳ **Pending**: You running `/test-model-compliance` in a live Gemini session

## Next Step for You

Open a fresh Gemini session in your workspace and run `/test-model-compliance`. This tests whether the new `GEMINI.md` actually produces Chain compliance. I can't verify this from Claude — you need to test in Gemini.
