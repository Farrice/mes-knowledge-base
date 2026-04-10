---
description: Time-boxed, fixed-iteration improvement sprint
---

# Proposer Sprint

> Load `skills/self-evolving-systems/genius.md` first. This is the fast, focused evolution workflow.

## When to Use
- You want quick improvement on a specific component
- You have 15-30 minutes for a focused optimization session
- You know what to improve but want to test multiple approaches
- Quick A/B testing of prompt variants or workflow structures

## Input Required
- **Target**: What to improve (single workflow, prompt section, or gate)
- **Iterations**: 5-10 (keep it tight — this is a sprint)
- **Metric**: Single metric to optimize (pick one, not three)
- **Test examples**: 3-5 representative examples to evaluate against

## Execution

### Sprint Protocol
1. **Read** the current target — understand the baseline
2. **Score** the baseline on test examples → record score
3. **For each iteration**:
   a. Read prior iteration results (if any)
   b. Propose ONE targeted change (not multiple simultaneous changes)
   c. Apply the change
   d. Score against test examples
   e. Record: change description, score, delta from baseline
   f. If worse than baseline, revert and try a different approach
4. **After all iterations**:
   a. Identify the single best-performing variant
   b. Diff against baseline
   c. Present: what changed, why it works, confidence level

### Sprint Rules
- **One change per iteration** — isolate variables for clean causal attribution
- **Revert on regression** — never compound a bad change
- **Time-box** — don't exceed the iteration count, even if you see potential
- **Log everything** — even failed iterations have diagnostic value

## Output
1. **Best variant** with score and delta from baseline
2. **Sprint log**: Each iteration's change, score, and verdict
3. **Top insight**: The single most impactful discovery from the sprint
4. **Deploy recommendation**: Swap or keep iterating?
