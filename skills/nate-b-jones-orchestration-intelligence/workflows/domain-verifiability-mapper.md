---
description: Classify work domains by AI delegation safety tier to determine appropriate autonomy levels
---

# Domain Verifiability Mapper

Map work domains to delegation safety tiers based on how easily output quality can be verified. This determines the appropriate autonomy level for AI agents in each domain.

## When to Use
- Deciding which tasks to delegate to AI agents
- Designing human-in-the-loop checkpoints
- Building progressive autonomy roadmaps
- Assessing risk of autonomous agent operations

## Workflow

### Phase 1: Domain Inventory

List all work domains under consideration. For each domain, gather:
1. What does "correct" output look like?
2. How do you currently evaluate quality?
3. What are the consequences of errors?
4. How quickly can errors be detected?
5. Can errors be reversed?

### Phase 2: Three-Tier Classification

Classify each domain into one of three verifiability tiers:

#### Tier 1: Hard-Verifiable (Boolean Pass/Fail)
Output can be checked with deterministic logic. There is a correct answer.

**Characteristics:**
- Binary outcome (works/doesn't work, correct/incorrect)
- Automated testing is possible
- Errors are immediately detectable
- Examples: code compilation, data validation, math calculations, format compliance, API responses

**Delegation Safety:** ✅ Safe for full autonomous delegation
**Verification Method:** Automated tests, assertions, type checks

#### Tier 2: Soft-Verifiable (Sniff-Check Required)
Output quality exists on a spectrum. "Good enough" can be assessed by a thoughtful non-expert.

**Characteristics:**
- Quality is a gradient, not binary
- Pattern recognition can detect major issues
- Errors may not be immediately obvious but are detectable with attention
- Examples: copywriting, design review, data analysis summaries, email drafts, marketing strategy

**Delegation Safety:** ⚠️ Safe with sniff-check protocols
**Verification Method:** Sniff-check checklists, structural validation, consistency checks

#### Tier 3: Unverifiable (Domain Expertise Required)
Output quality requires genuine domain expertise or lived experience to evaluate.

**Characteristics:**
- Correct assessment requires deep knowledge
- Errors can masquerade as valid output
- Non-experts cannot reliably distinguish good from bad
- Examples: legal advice, medical decisions, novel research conclusions, ethical judgments, creative breakthrough assessment

**Delegation Safety:** 🛑 Human-in-the-loop required
**Verification Method:** Domain expert review, peer validation

### Phase 3: Autonomy Roadmap

For each domain, design a progression path:

1. **Current State**: Where is each domain today? (manual, assisted, supervised, autonomous)
2. **Target State**: What autonomy level is appropriate given the verifiability tier?
3. **Migration Path**: What needs to change to safely increase autonomy?
4. **Monitoring Plan**: How will you detect quality degradation over time?

### Phase 4: Sniff-Check Design (for Tier 2 domains)

For each soft-verifiable domain, build a sniff-check protocol:
1. **Structural Checks**: Does the output have the right shape, length, components?
2. **Consistency Checks**: Does it contradict itself, the prompt, or known facts?
3. **Red Flag Patterns**: What patterns reliably indicate low quality?
4. **Confidence Calibration**: When should you trust vs. challenge the output?

## Deliverable

Domain verifiability map containing:
- Classification table (domain → tier → current autonomy → target autonomy)
- Sniff-check protocols for each Tier 2 domain
- Human checkpoint requirements for each Tier 3 domain
- Progressive automation roadmap with milestones
- Risk assessment for each domain's planned autonomy level
