# Context Compression Sprint

> Execute immediate token reduction across system prompts, agent files, and skill context. Apply all five compression vectors. Measure before/after. Validate lossless.

## Prerequisites
- Context Bloat Diagnostic completed (or done inline as Step 0)
- Git or version control for rollback safety
- Token counter or byte counter
- 5 representative test tasks for quality validation

## Steps

### Step 0 — Baseline Measurement
If no diagnostic exists, run a quick measure:
```bash
# Measure key files
wc -c GEMINI.md AGENTS.md
find skills/ -name "SKILL.md" | xargs wc -c | sort -rn | head -20
find skills/ -name "genius.md" | xargs wc -c | sort -rn | head -20
```
Record total bytes. This is your "before" number.

### Step 1 — Vector 1: Instruction Deduplication
**Target**: System instructions that appear in multiple locations.

1. Grep for common instruction patterns across all system-level files:
   ```bash
   grep -rn "slop\|banned\|never mix\|tool calls\|text response" GEMINI.md AGENTS.md directives/ --include="*.md"
   ```
2. For each duplicate found:
   - Identify the **authoritative location** (usually GEMINI.md)
   - Remove the duplicate from other files
   - If a duplication exists for good reason (context-specific variant), annotate why
3. Count tokens/bytes removed

**Expected result**: 15-25% reduction in system instruction tokens.

### Step 2 — Vector 2: Structured Distillation
**Target**: Verbose explanations that can be compressed into rules.

Patterns to compress:
- Paragraph that explains a single rule → single-line rule statement
- Multi-sentence example → one-line example with inline annotation
- Repeated "if X then Y" patterns → table or numbered list
- Historical context that doesn't affect behavior → remove or move to reference doc

Before:
```markdown
When you are producing content, you need to make sure that you load the expert
skill file first. This is very important because without loading the skill file,
the output will not reflect the expert's methodology. You should always load the
SKILL.md file before producing any output.
```

After:
```markdown
**LOAD EXPERT BEFORE PRODUCING.** No expert output without reading SKILL.md first.
```

### Step 3 — Vector 3: Format Optimization
**Target**: Prose instructions that can be expressed as structured data.

Actions:
- Convert paragraph-form tool descriptions → structured schema
- Convert prose rules → numbered lists with clear conditions
- Convert repeated "do X, don't do Y" pairs → table format
- Remove filler words: "you need to", "make sure to", "it is important that"
- Remove soft language: "you might want to", "consider", "perhaps"

### Step 4 — Vector 4: Tiered Loading Enforcement
**Target**: Context loaded at wrong tier (too much loaded too early).

Review current loading behavior:
- Are full genius.md files loaded at Tier 1? Move to Tier 2.
- Are workflow files loaded preemptively? Load only on workflow invocation.
- Are all Tier 0 cards loading? Verify only Hot cards load at Tier 0.
- Is conversation history accumulating without summarization? Add periodic distillation.

### Step 5 — Vector 5: Attention Placement Optimization
**Target**: Critical instructions buried in low-attention positions.

Restructure system prompts:
- **Top 10%**: Core identity, critical guardrails, chain requirements
- **Middle 80%**: Reference material, examples, skill details
- **Bottom 10%**: Final guardrails, output format requirements, critical overrides

Move any rule with compliance issues from middle to top or bottom.

### Step 6 — Quality Validation
Run your 5 representative test tasks through BOTH:
1. The original (pre-compression) context
2. The compressed context

Compare outputs:
- [ ] Task completion parity (both versions complete the task)
- [ ] Instruction compliance parity (both versions follow the same rules)
- [ ] Quality parity (outputs are functionally equivalent)
- [ ] Edge case parity (unusual requests handled the same way)

If any divergence found, restore the minimum tokens needed to recover parity.

### Step 7 — Record Results
```
Before: [X] bytes / [Y] tokens
After:  [X'] bytes / [Y'] tokens
Reduction: [Z]%
Quality Parity: Yes/No (if No, what was restored?)
Vector Breakdown:
  - Deduplication: [a]% reduction
  - Distillation: [b]% reduction
  - Format optimization: [c]% reduction
  - Tiered loading: [d]% reduction
  - Attention placement: [e] instructions relocated
```

### Step 8 — Commit & Monitor
1. Commit compressed files with descriptive commit message
2. Monitor system performance over next 48 hours
3. Track any regression in output quality or instruction compliance
4. If regression detected, rollback and investigate which compression caused it

## Output Format
Deliver as an artifact with:
- Before/after measurements
- Per-vector reduction breakdown
- Quality validation results
- Compression changelog (what was changed, why, and what was preserved)
- Monitoring plan

## Quality Gate

Before shipping the compressed context, confirm:
- [ ] Step 6 quality validation actually ran on all 5 representative test tasks against both original and compressed context — not a subset, not skipped
- [ ] Task completion, instruction compliance, quality, and edge-case parity all passed; any divergence was resolved by restoring the minimum tokens needed, not by accepting the regression
- [ ] Total reduction is ≥15% (the deduplication-alone floor) — if it's lower, name which vector underperformed and why
- [ ] The per-vector breakdown in Step 7 sums to the total reduction claimed; no vector's contribution is asserted without its own before/after number
- [ ] Compressed files are committed with a descriptive message and a named rollback path (Step 8), not shipped as an uncommitted working-tree change
- [ ] The changelog states explicitly what was preserved (expert vocabulary, edge-case rules) and why — silence on what survived is not evidence nothing was lost
