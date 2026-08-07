# Gemini.md Optimization — Multi-Model Antigravity

> **Expert Ensemble**: Boris (AI productivity, CLAUDE.md architecture), Lance & Yichao (context engineering), Nate B. Jones (orchestration intelligence), Nick Saraev (agentic workflows)

## The Problem

Antigravity was built on Claude. `GEMINI.md` is a mirror copy of `CLAUDE.md`. Gemini ignores or partially executes The Chain because it processes instructions differently — the harness assumes Claude's architecture. Result: Gemini runs at maybe 30% of Antigravity's power.

## The Solution: Model-Native Instruction Files

Break the mirror. Create a `GEMINI.md` optimized for how Gemini actually processes instructions, encoding the **same system intent** in a **model-native format**.

> [!IMPORTANT]
> This plan is **thinking and design only** — no code changes until you approve the approach.

---

## Design Principles (Expert Synthesis)

### From Boris — The Bitter Lesson Applied
Boris Pattern #16: *"Refuse to build complex, brittle orchestrators that the next base model will render obsolete."*

**Application**: Don't build a complex multi-file orchestration layer to "fix" Gemini. Instead, create a single `GEMINI.md` that works with how Gemini processes instructions natively. Minimal scaffolding, maximum model leverage.

### From Lance & Yichao — Context Engineering
Pattern #19: *"Too many tools cause context confusion — wrong tool calls or hallucinations."*
Pattern #22: *"Biggest gains from removing features, not adding."*

**Application**: Gemini's issue isn't that it can't follow The Chain — it's that the instruction density + "internalize" directives create context confusion. The fix is reformatting instructions for Gemini's attention patterns, not adding more instructions.

### From Nate B. Jones — Harness Audit Findings
The 7 architectural gaps identified in Phase 1 become the specific translation targets:

| Gap | Claude Reads As | Gemini Reads As | Fix |
|-----|----------------|-----------------|-----|
| No chain step tracker | "Execute mentally" | "Optional" | Add explicit numbered checklist |
| "Internalize" instruction | "Execute silently" | "Skip entirely" | Replace with "Always execute" |
| Competing instruction sources | Prioritizes correctly | Confused priority | Add explicit precedence header |
| No finalize enforcement | Follows from habit | Ignores | Add hard gate language |
| Workflow override ambiguity | Handles gracefully | Skips chain entirely | Add explicit "chain still runs" |

---

## Proposed Architecture

### What Changes

```
BEFORE (Mirror):
  CLAUDE.md ═══ identical ═══ GEMINI.md ═══ identical ═══ AGENTS.md

AFTER (Model-Native):
  CLAUDE.md ─── same intent ─── GEMINI.md ─── same intent ─── AGENTS.md
       │                              │                              │
  Claude-optimized            Gemini-optimized              Default (Claude format)
```

### What Stays the Same
- **System intent**: The Chain, Context Engine, expert routing, quality gates — identical purpose
- **CLAUDE.md**: Untouched. It works perfectly
- **AGENTS.md**: Stays as Claude-format default (for Cursor, Windsurf, etc.)
- **All skills, agents, workflows, directives**: Unchanged — these are model-agnostic

### What Changes in GEMINI.md
Five categories of translation, ordered by impact:

#### 1. Explicit Execution Directives (replaces "internalize" language)
```diff
- Steps 1-2 (SCORE + SHARPEN): Internalized — no file reads required.
+ Steps 1-2 (SCORE + SHARPEN): Execute these steps for EVERY request.
+ Print your score and reasoning before proceeding. Do NOT skip.
```

#### 2. Numbered Checklist Format (replaces prose paragraphs)
```diff
- Complete these 6 steps IN ORDER for every user request...
+ ## THE CHAIN — MANDATORY 6-STEP PROTOCOL
+ For EVERY request that produces a deliverable, execute ALL steps:
+ 
+ □ Step 1: SCORE intent (print score 1-5)
+ □ Step 2: SHARPEN (if Score ≤ 3, ask missing dimensions)
+ □ Step 3: ROUTE to expert (name the expert and why)
+ □ Step 4: LOAD via Context Engine (read the skill files)
+ □ Step 5: PRODUCE output (using loaded expert frameworks)
+ □ Step 6: FINALIZE (run chain_runner.py — NON-NEGOTIABLE)
```

#### 3. Priority Headers (resolves competing instruction ambiguity)
```
## INSTRUCTION PRIORITY ORDER
1. THE CHAIN (Steps 1-6) — overrides everything below
2. Workflow commands — execute workflow, chain runs inside it
3. Context Engine tiers — load experts before producing
4. Supporting protocols — fire at their trigger points
```

#### 4. Hard Gate Language (enforces finalize)
```diff
- This is non-negotiable.
+ ⛔ HARD GATE: You MUST run chain_runner.py finalize after Step 5.
+ If you produce expert output without finalize, the task is INCOMPLETE.
+ Do not present output to the user until finalize has been run.
```

#### 5. Workflow-Chain Clarification
```diff
- The workflow incorporates the chain internally.
+ When a workflow is invoked, read and execute the workflow file.
+ The Chain STILL RUNS — the workflow is Step 5 (PRODUCE).
+ Steps 1, 3, 4, and 6 still execute around the workflow.
```

---

## Maintenance Solution: `/sync-instructions` Workflow

To prevent operational drift when you update The Chain:

### Proposed Workflow: `/sync-instructions`

**What it does**: When you change system intent (add a step to The Chain, add a new expert, modify routing), this workflow:
1. Reads the changed `CLAUDE.md` 
2. Identifies what intent changed
3. Translates the change into Gemini-native format
4. Updates `GEMINI.md` with the translated version
5. Shows you a diff for approval

**Where it lives**: `.agent/workflows/sync-instructions.md`

### Proposed Workflow: `/test-model-compliance`

**What it does**: Tests whether a model instruction file actually works:
1. Simulates 3 test requests through The Chain
2. Checks if all 6 steps execute
3. Reports which steps were skipped or partially executed
4. Grades compliance (A/B/C/F)

**Where it lives**: `.agent/workflows/test-model-compliance.md`

---

## Future-Proofing (Boris Pattern #16)

### Adding New Models Later
The same translation process applies to any model:
- `CLAUDE.md` — Claude-optimized (current, working)
- `GEMINI.md` — Gemini-optimized (this project)
- `GPT.md` — GPT-optimized (future, if needed)
- `AGENTS.md` — Default format for other AI tools

Each file encodes **identical system intent** in **model-native format**.

### Adding New Experts/Extractions
When you add new skills:
1. Skills themselves are model-agnostic (no change needed)
2. If routing tables change → run `/sync-instructions` to update all model files
3. If new slash commands are added → they appear in all files automatically (they're in the workflow list, not the instruction body)

---

## Execution Plan (When Approved)

| Phase | What | Effort |
|-------|------|--------|
| 1 | Create `GEMINI.md` v2 with all 5 translation categories applied | ~1 hour |
| 2 | Build `/sync-instructions` workflow | ~30 min |
| 3 | Build `/test-model-compliance` workflow | ~30 min |
| 4 | Test: Run 3 sample requests through Gemini with new `GEMINI.md` | You test |

> [!NOTE]
> Phase 4 requires you to test in Gemini since I'm Claude — I can't run Gemini to verify. You'd open a Gemini session, give it a test request, and see if The Chain executes.

## Verification Plan

### Manual Testing (Phase 4)
1. Open a new Gemini session in your workspace
2. Give it a simple expert-domain request: *"Write me 3 LinkedIn hooks for my AI consulting offer"*
3. **Check**: Does Gemini SCORE the intent? Does it ROUTE to Lara Acosta? Does it LOAD the skill? Does it run FINALIZE?
4. Give it a workflow command: *"/recommend I need to figure out my first product"*
5. **Check**: Does it execute the workflow AND The Chain wrapper?
6. Grade: A = all steps execute, B = most execute, C = only some, F = skips chain

### Regression Check
- Verify `CLAUDE.md` is completely untouched
- Verify all existing skills/workflows still work (they're model-agnostic)
