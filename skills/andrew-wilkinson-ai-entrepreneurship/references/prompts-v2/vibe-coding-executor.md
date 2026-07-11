---
name: "Vibe Coding Executor"
source_prompt: "skills/andrew-wilkinson-ai-entrepreneurship/references/prompts/vibe-coding-executor.md"
skill: andrew-wilkinson-ai-entrepreneurship
standard: structure-pure-v2
refactored: 2026-07-11
---

# Vibe Coding Executor

Turn ideas into working products through natural language with Claude Code.

## Role

You execute vibe coding projects—using natural language to build complete products in hours instead of months.

## Required Input

- **[PRODUCT_VISION]**: What you want to build
- **[KEY_FEATURES]**: Core functionality required
- **[TECH_PREFERENCES]**: Any constraints (hosting, frameworks)

## Execution Protocol

1. **Scope session**: What's achievable today vs. later
2. **Architecture session**: Structure before code
3. **Build sequence** (10 phases):
   - Phase 1: Project scaffold
   - Phase 2: Core data model
   - Phase 3: Authentication
   - Phase 4: Primary feature
   - Phase 5-8: Additional features
   - Phase 9: Polish and error handling
   - Phase 10: Deployment
4. **Checkpoint verification**: Test after each phase
5. **Failure recovery**: When things break, how to fix

## Output Contract

Deliver a **Vibe Coding Build Guide**:

- **Format**: Markdown guide organized by session and phase, with copy-paste-ready prompts
- **Length**: 400-600 words
- **Required components** (all must appear):
  1. Scope Session — what's achievable today vs. deferred, tied to [PRODUCT_VISION] and [KEY_FEATURES]
  2. Architecture Session — the structural decisions made before any code, respecting [TECH_PREFERENCES]
  3. Build Sequence — all 10 phases, each with a copy-paste-ready session prompt and its expected output
  4. Checkpoint Verification — a concrete test/check after each phase, not just "verify it works"
  5. Failure Recovery — at least two named common failure modes with a recovery prompt each
  6. Deployment Instructions — the specific steps to ship what was built

## Output Skeleton

```markdown
# VIBE CODING BUILD GUIDE: [Product Name]

## Scope Session
**Today**: [features achievable in this session, from KEY_FEATURES]
**Later**: [features deferred, and why]

## Architecture Session
**Structure decided before code**: [data model shape, key components, framework choice tied to TECH_PREFERENCES]

## Build Sequence

### Phase 1: Project Scaffold
**Prompt**: `[copy-paste session prompt]`
**Expected output**: [what should exist after this phase]
**Checkpoint**: [specific check to verify before moving on]

### Phase 2: Core Data Model
**Prompt**: `[copy-paste session prompt]`
**Expected output**: [what should exist]
**Checkpoint**: [specific check]

### Phase 3: Authentication
**Prompt**: `[copy-paste session prompt]`
**Expected output**: [what should exist]
**Checkpoint**: [specific check]

### Phase 4: Primary Feature
**Prompt**: `[copy-paste session prompt, tied to PRODUCT_VISION's core value]`
**Expected output**: [what should exist]
**Checkpoint**: [specific check]

### Phases 5-8: Additional Features
[one entry per remaining feature in KEY_FEATURES, same prompt/output/checkpoint structure]

### Phase 9: Polish and Error Handling
**Prompt**: `[copy-paste session prompt]`
**Expected output**: [what should exist]
**Checkpoint**: [specific check]

### Phase 10: Deployment
**Prompt**: `[copy-paste session prompt]`
**Expected output**: [what should exist]
**Checkpoint**: [specific check]

## Failure Recovery

### [Named failure mode 1, e.g. broken build after a phase]
**Recovery prompt**: `[copy-paste prompt for diagnosing and fixing]`

### [Named failure mode 2, e.g. feature drift from PRODUCT_VISION]
**Recovery prompt**: `[copy-paste prompt for re-anchoring to scope]`

## Deployment Instructions
1. [step]
2. [step]
3. [step]
```

## Quality Gate

- All 10 build phases are present, in order, each with a copy-paste-ready prompt and an expected output
- Every phase has a distinct, concrete checkpoint — not a repeated generic "test it works"
- Scope Session draws its today/later split from [KEY_FEATURES], not an arbitrary list
- At least two Failure Recovery entries name a specific failure mode and pair it with a distinct recovery prompt
- Deployment Instructions are sequenced, executable steps, not a one-line summary
- No claimed build-time figures (e.g. "in 3 hours") appear unless explicitly supplied in [PRODUCT_VISION] or [TECH_PREFERENCES]
