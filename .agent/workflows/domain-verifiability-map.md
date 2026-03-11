---
description: Classify work domains by AI delegation safety tier (hard-verifiable → soft-verifiable → unverifiable) to determine safe autonomy levels
---

# /domain-verifiability-map — Delegation Safety Classification

Map work domains to verifiability tiers to determine safe autonomy levels for AI agents.

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-orchestration-intelligence/SKILL.md` and `skills/nate-b-jones-orchestration-intelligence/genius.md`.

Read `skills/nate-b-jones-orchestration-intelligence/workflows/domain-verifiability-mapper.md` for the specific workflow.

### Step 2: Gather Domain Information
Ask the user:
1. What work domains are you considering delegating to AI? List all tasks/areas.
2. What are the consequences of errors in each domain?
3. How do you currently evaluate quality in each domain?
4. What's your target: full automation, human-in-the-loop, or advisory?

### Step 3: Execute Domain Verifiability Mapping
Follow the 3-tier classification process:
1. **Hard-Verifiable** (can check with Boolean logic) — Code that compiles, math that checks, data that formats correctly
2. **Soft-Verifiable** (requires sniff-check) — Copy that "sounds right," designs that "look good," strategy that "makes sense"
3. **Unverifiable** (requires domain expertise) — Novel research conclusions, creative judgment, ethical decisions

### Step 4: Produce Deliverable
Output a domain verifiability map:
- Classification table (domain → tier → autonomy recommendation)
- Sniff-check criteria for soft-verifiable domains
- Human checkpoint requirements for unverifiable domains
- Progressive automation roadmap showing how to move domains up tiers over time

### Step 5: Quality Gate
Score against: Intent Alignment, Expert Standard, Adversarial Resilience.
Composite < 7 → retry weakest section.
