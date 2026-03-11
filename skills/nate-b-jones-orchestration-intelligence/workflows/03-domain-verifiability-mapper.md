---
description: Classify all work in a domain into machine-checkable, expert-checkable, and unverifiable tiers to determine what can be delegated to agents
---

# Domain Verifiability Mapper

> Load `genius.md` first. This workflow classifies work domains for agent delegation decisions.

## When to Use
- Deciding what work to delegate to agents vs. retain for humans
- Organizational AI adoption planning — mapping which departments/roles are delegation-ready
- Challenging the assumption that "soft work" can't be delegated
- Building the case for agent deployment in non-engineering domains
- Post-deployment: reassessing delegation boundaries as harnesses improve

## Input Required
- **Domain**: The field, department, or role to classify (e.g., "product management," "legal research," "customer success")
- **Work inventory**: List of actual tasks/deliverables produced in this domain (not job descriptions — real work)
- **Expert availability**: Who can serve as sniff-checkers? What experience level?

## Execution

### Phase 1 — Work Inventory Decomposition
1. **List every distinct deliverable** produced in the domain. Not categories — specific outputs.
   - Example (Product Management): PRDs, competitive analysis, roadmap updates, stakeholder emails, sprint planning docs, feature prioritization matrices, user story writing, release notes
2. **For each deliverable, identify**: Who currently produces it? How long does it take? How is quality currently assessed?

### Phase 2 — Verifiability Classification
For each deliverable, classify into one of three tiers:

**Tier 1 — Machine-Checkable** ✅
The deliverable has automated verification criteria.
- Code compiles and tests pass
- Mathematical constraints are satisfied
- Format/structure can be validated programmatically
- Data accuracy can be cross-referenced against sources
- **Delegation verdict**: Fully delegable. Build automated verification and delegate immediately.

**Tier 2 — Expert-Checkable** ⚡
The deliverable can be evaluated by experienced practitioners who reach near-consensus on quality.
- Apply the **3-Expert Test**: Would 3-4 practitioners with 10+ years of experience agree on whether this is correct or incorrect?
- Apply the **Consensus Bandwidth Test**: How wide is the band of "acceptable" outputs? If narrow → highly verifiable. If wide → less verifiable, but still expert-checkable.
- Examples: Product strategies, legal briefs, engineering designs, marketing campaigns, customer emails, project plans
- **Delegation verdict**: Delegable with sniff-check protocol. Build evaluation criteria (see Sniff-Check Protocol Builder) and delegate.

**Tier 3 — Genuinely Unverifiable** ⛔
The deliverable has no consensus criteria even among experts.
- Truly novel creative work with no reference frame
- Strategic bets with no comparable precedent
- Aesthetic judgments where expert opinions genuinely diverge
- **Key constraint**: This tier is almost always <10% of knowledge work. Challenge every item placed here — most "unverifiable" work is actually Tier 2 in disguise.
- **Delegation verdict**: Retain for humans. Use agents for Tier 1/2 components within the work.

### Phase 3 — The Verifiability Surprise Audit
Nate's contrarian insight: most work classified as "unverifiable" is actually expert-checkable. For every item you initially placed in Tier 3, apply:

1. **The Product Strategy Test**: "Bring this to 3-4 different leaders, each with 15-20 years of experience. Their assessment will be remarkably consistent." Does this apply?
2. **The Internalized Pattern Test**: Is there a set of patterns that experienced practitioners have internalized and can apply? If yes, it's Tier 2.
3. **The Anti-Consensus Check**: Is there genuine, irreconcilable expert disagreement? Not "different approaches" (still Tier 2) but fundamental disagreement on what "correct" even means?

Move items from Tier 3 → Tier 2 wherever the evidence supports it.

### Phase 4 — Delegation Roadmap
Produce a phased delegation plan:

| Phase | Tier | Action | Timeline |
|-------|------|--------|----------|
| **Immediate** | Tier 1 | Full delegation with automated verification | Week 1 |
| **Near-term** | Tier 2 (narrow consensus) | Delegation with sniff-check protocol | Weeks 2-4 |
| **Medium-term** | Tier 2 (wide consensus) | Delegation with enhanced evaluation criteria | Months 1-2 |
| **Retain** | Tier 3 | Human execution; agent-assisted components only | Ongoing |

## Output
A Domain Verifiability Map containing:
1. **Complete work inventory** with verifiability tier classification for each deliverable
2. **Tier distribution** (% of work in each tier — flag if Tier 3 > 10%)
3. **Verifiability surprise findings** (items reclassified from Tier 3 → Tier 2)
4. **Sniff-check requirements** for each Tier 2 item (input to Sniff-Check Protocol Builder)
5. **Delegation roadmap** with phased timeline
6. **Human capital reallocation** — what do the people currently doing Tier 1/2 work focus on instead? (Answer: sniff-checking, taste-making, agent infrastructure)
