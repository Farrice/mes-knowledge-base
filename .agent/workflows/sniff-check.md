---
description: Build evaluation criteria for assessing agent output quality without requiring domain expertise — the meta-skill for the agent era
---

# /sniff-check — Agent Output Quality Protocol Builder

Create evaluation protocols that detect agent quality without requiring domain expertise.

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-orchestration-intelligence/SKILL.md` and `skills/nate-b-jones-orchestration-intelligence/genius.md`.

Read `skills/nate-b-jones-orchestration-intelligence/workflows/sniff-check-protocol-builder.md` for the specific workflow.

### Step 2: Gather Evaluation Context
Ask the user:
1. What type of agent output do you need to evaluate? (code, copy, strategy, research, creative)
2. Do you have domain expertise in this area, or are you evaluating outside your expertise?
3. What does "good enough" look like? What are the non-negotiables?
4. How frequently does this evaluation need to happen? (per-output, batch, periodic)

### Step 3: Execute the Sniff-Check Protocol
Build evaluation criteria using the three-layer approach:
1. **Structural Checks** — Does the output have the right shape, length, components?
2. **Consistency Checks** — Does the output contradict itself, the prompt, or known facts?
3. **Gestalt Checks** — Does the output "feel right" to a non-expert? (the sniff test)

### Step 4: Produce Deliverable
Output a sniff-check protocol:
- Checklist of structural validation criteria
- Consistency verification steps
- "Red flag" patterns that indicate low quality
- Confidence calibration guide (when to trust vs. challenge)
- Escalation triggers (when to bring in a domain expert)

### Step 5: Quality Gate
Score against: Intent Alignment, Expert Standard, Adversarial Resilience.
Composite < 7 → retry weakest section.
