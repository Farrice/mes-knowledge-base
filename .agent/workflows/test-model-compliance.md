---
description: Test whether a model instruction file (CLAUDE.md or GEMINI.md) actually produces Chain compliance
---

# /test-model-compliance — Model Instruction Compliance Test

Run this after creating or modifying any model instruction file to verify it actually works.

## Prerequisites
- The instruction file exists (`CLAUDE.md`, `GEMINI.md`, etc.)
- You have access to the model you're testing (Gemini for GEMINI.md, Claude for CLAUDE.md)

## The Test Protocol

### Test 1: Simple Expert Request
**Prompt**: "Write me 3 LinkedIn hooks for my AI consulting offer"

**Check for** (all must appear):
- [ ] Score printed (Step 1 executed)
- [ ] Expert named — should route to Lara Acosta (Step 3 executed)
- [ ] Skill file read — `skills/lara-acosta-linkedin/SKILL.md` (Step 4 executed)
- [ ] Output uses Lara's frameworks, not generic advice (Step 5 executed)
- [ ] `chain_runner.py finalize` command was run (Step 6 executed)

### Test 2: Workflow Command
**Prompt**: "/recommend I need to figure out my first digital product"

**Check for** (all must appear):
- [ ] Score printed (Chain still runs around workflow)
- [ ] Workflow file read — `.agent/workflows/recommend.md`
- [ ] Expert(s) routed and loaded (Chain Step 3-4 ran)
- [ ] `chain_runner.py finalize` was run (Chain Step 6 ran)

### Test 3: Trivial-Seeming Expert Request
**Prompt**: "Give me a one-liner for my business"

**Check for** (this is the trap — tests if "trivial" skipping is prevented):
- [ ] Score printed (NOT skipped despite seeming simple)
- [ ] Expert routed — should hit StoryBrand/Donald Miller or copywriting
- [ ] Skill files loaded (NOT skipped)
- [ ] `chain_runner.py finalize` was run (NOT skipped)

## Grading Scale

| Grade | Criteria |
|-------|----------|
| **A** | All 3 tests pass — all Chain steps visible in output |
| **B** | 2/3 tests pass, or all pass but some steps are implicit (not printed) |
| **C** | 1/3 tests pass, or Chain runs but steps are frequently skipped |
| **F** | Chain is ignored — model produces output without scoring, routing, or loading |

## Post-Test Actions

| Grade | Action |
|-------|--------|
| A | Done. File is working. |
| B | Identify which steps were implicit, add more explicit "YOU MUST print" language |
| C | Major revision needed — compare against working file (CLAUDE.md) for structural gaps |
| F | Start over — the instruction format is fundamentally incompatible with this model |

## Running This Test

1. Open a **new, fresh session** with the target model
2. Do NOT prime the model with context — the instruction file must work cold
3. Run all 3 tests in sequence
4. Grade each test and log overall grade
5. If grade < A, iterate on the instruction file and re-test
