---
description: Build evaluation criteria, quality gates, and fast "is this correct?" frameworks for agent-delegated work in any domain
---

# Sniff-Check Protocol Builder

> Load `genius.md` first. This workflow produces evaluation protocols for agent work.

## When to Use
- You've decided to delegate Tier 2 (expert-checkable) work to agents and need evaluation criteria
- Building the meta-skill layer that makes agent delegation safe
- Training team members to evaluate agent output instead of producing output directly
- Establishing quality gates for any agentic workflow
- Complementary to: Oren's Taste Mastery (CEV evaluation framework)

## Input Required
- **Domain**: What field this protocol covers
- **Work type**: Specific deliverable being evaluated (e.g., "product strategy document," "customer email response," "marketing campaign brief")
- **Expert benchmarks**: What does excellence look like? What are common failure modes?
- **Time constraint**: How fast must the sniff-check be? (Target: <2 minutes for routine work)

## Execution

### Phase 1 — Expert Consensus Extraction
1. **Identify the implicit quality criteria** that experienced practitioners apply without articulating:
   - What makes them say "this is right" in <10 seconds?
   - What makes them say "this is wrong" in <10 seconds?
   - What are the 3-5 non-negotiable markers of quality?
   - What are the 3-5 instant-fail indicators?

2. **Build the Expert Pattern Matrix**:

| Marker | Correct Signal | Failure Signal | Check Time |
|--------|---------------|----------------|------------|
| [Quality marker 1] | [What it looks like when right] | [What it looks like when wrong] | [Seconds] |
| [Quality marker 2] | ... | ... | ... |
| [Quality marker 3] | ... | ... | ... |

### Phase 2 — Build the Sniff-Check Protocol
Structure a fast evaluation framework:

**Layer 1 — The 10-Second Scan** (eliminates obvious failures)
- Does it have the right structure/format?
- Does the scope match what was requested?
- Is there anything obviously wrong, missing, or contradictory?
- **Pass**: Proceed to Layer 2. **Fail**: Reject immediately for re-iteration.

**Layer 2 — The 60-Second Read** (evaluates substance)
- Does the core argument/recommendation hold up?
- Do the details support the conclusion?
- Would an experienced practitioner nod along reading this?
- Are the non-negotiable markers present?
- Are any instant-fail indicators present?
- **Pass**: Proceed to Layer 3 (if applicable). **Fail**: Reject with specific failure point for re-iteration.

**Layer 3 — The Edge Case Check** (stress-tests)
- What's the weakest point?
- What would the most critical stakeholder find wrong?
- Is there a subtle error that passes surface inspection?
- **Pass**: Accept. **Fail**: Reject with edge case annotation.

### Phase 3 — Calibration Protocol
Build internal consistency:
1. **Benchmark set**: Collect 3-5 examples of excellent output and 3-5 examples of failed output
2. **Blind test**: Can the sniff-checker correctly classify all 6-10 examples?
3. **Inter-rater reliability**: If 3 sniff-checkers evaluate the same output, do they reach the same conclusion >80% of the time?
4. **Speed test**: Can the complete sniff-check (all 3 layers) be completed in the target time (<2 minutes)?

### Phase 4 — Feedback Loop Design
Connect sniff-check results to agent improvement:
1. **Failure taxonomy**: Categorize sniff-check failures (structural, substantive, edge case)
2. **Agent prompt update**: For each failure category, what prompt modification would prevent it?
3. **Iteration protocol**: When sniff-check fails, what specific instruction does the agent receive for the next iteration?
4. **Success tracking**: What % of agent outputs pass sniff-check on first attempt? Track over time.

## Output
A complete sniff-check protocol containing:
1. **Expert Pattern Matrix** (quality markers, correct/failure signals, check times)
2. **3-Layer Evaluation Protocol** (10-second scan → 60-second read → edge case check)
3. **Calibration benchmark set** (good examples, bad examples, blind test)
4. **Speed target** with confirmed timing
5. **Failure taxonomy** with agent improvement feedback loops
6. **Deployment instructions** (who runs it, when, how often, escalation path)

## Stacking Note
This workflow stacks naturally with **Oren's Taste Mastery** — the CEV (Creation, Evaluation, Verification) framework provides the aesthetic and creative judgment layer, while this protocol provides the domain-specific correctness layer. Together: "Is this right?" (sniff-check) + "Is this excellent?" (taste gate).
