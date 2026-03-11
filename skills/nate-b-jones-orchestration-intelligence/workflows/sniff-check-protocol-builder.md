---
description: Build evaluation criteria for assessing agent output quality without requiring domain expertise
---

# Sniff-Check Protocol Builder

Create evaluation protocols that detect agent output quality without requiring domain expertise. This is the critical human skill for the agent era — the ability to assess whether AI output is "right enough" even when you're not an expert in the domain.

## When to Use
- Evaluating agent output in domains outside your expertise
- Building quality gates for automated pipelines
- Training team members to spot low-quality agent output
- Designing monitoring systems for production agents

## Workflow

### Phase 1: Output Characterization

Before building the protocol, understand the output:
1. What type of output is being produced? (code, copy, strategy, research, design, data)
2. What does a "perfect" output look like? (get examples if possible)
3. What does a clearly bad output look like? (get anti-examples)
4. Who is the end consumer of this output?
5. What's the cost of shipping a bad output?

### Phase 2: Three-Layer Evaluation Stack

Build the protocol as three progressive layers:

#### Layer 1: Structural Checks (5 minutes, anyone can do this)
These are Boolean checks that require zero domain expertise:

- **Completeness**: Does the output contain all requested components?
- **Length**: Is it in the expected range? (too short = shallow, too long = rambling)
- **Format**: Does it follow the specified structure?
- **References**: Does it cite sources when claimed?
- **Specificity**: Does it name specific things vs. vague generalities?
- **Actionability**: Can you actually DO what it recommends without asking follow-ups?

#### Layer 2: Consistency Checks (10 minutes, moderate attention)
These catch logical and factual issues:

- **Internal Consistency**: Does the output contradict itself?
- **Prompt Alignment**: Does it actually address what was asked?
- **Factual Baseline**: Are verifiable claims actually true? (spot-check 2-3)
- **Tone Match**: Does the voice/tone match the intended audience?
- **Confidence Calibration**: Does it express appropriate uncertainty? (Watch for overconfidence)
- **Novelty Check**: Is this generic boilerplate or actually tailored?

#### Layer 3: Gestalt Check (5 minutes, honest gut feeling)
The intuitive sniff test:

- **First Impression**: If you saw this without context, would you trust it?
- **"Would I Send This?"**: Would you forward this to a smart colleague without edits?
- **Expert Simulation**: If a real expert saw this, what would they critique?
- **Red Flag Scan**: Any phrases that sound like AI slop? ("In today's world...", "It's important to note...", "Let's dive in...")
- **Value Test**: Does this give the reader something they didn't already know?

### Phase 3: Red Flag Catalog

Build a domain-specific red flag list:

| Red Flag | What It Indicates | Severity |
|----------|------------------|----------|
| Generic opening line | Template-mode, not tailored | Medium |
| No specific names/numbers | Fabrication risk | High |
| Contradicts known facts | Hallucination | Critical |
| Excessive hedging | Low confidence, padding | Low |
| Perfect structure, no substance | Form over content | High |
| Cites sources that don't exist | Hallucination | Critical |

### Phase 4: Confidence Calibration Guide

Help the evaluator know when to trust vs. challenge:

| Signal | Trust Level | Action |
|--------|------------|--------|
| Output matches your existing knowledge | High | Accept |
| Output teaches you something new but plausible | Medium | Spot-check one claim |
| Output contradicts your intuition | Low | Deep verify before accepting |
| Output makes extraordinary claims | Very Low | Require external validation |
| Output includes verifiable specifics | Increases trust | Verify 1-2 specifics |

### Phase 5: Escalation Triggers

Define when to bring in a domain expert:

1. **Score below threshold** on Layer 1 or 2
2. **Critical red flags** detected (fabrication, contradiction)
3. **High-stakes decision** depends on this output
4. **Repeated failures** on the same type of task
5. **Evaluator uncertainty** — when you genuinely can't tell if it's good

## Deliverable

Sniff-check protocol document containing:
- Customized three-layer evaluation checklist
- Domain-specific red flag catalog
- Confidence calibration guide
- Escalation trigger definitions
- Quick-reference scorecard (pass/flag/fail)
- Estimated time per evaluation
