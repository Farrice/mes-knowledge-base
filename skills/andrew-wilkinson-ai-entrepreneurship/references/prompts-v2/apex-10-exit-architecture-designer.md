---
name: "APEX-10: Exit Architecture Designer"
source_prompt: "skills/andrew-wilkinson-ai-entrepreneurship/references/prompts/apex-10-exit-architecture-designer.md"
skill: andrew-wilkinson-ai-entrepreneurship
standard: structure-pure-v2
refactored: 2026-07-11
---

# APEX-10: Exit Architecture Designer

Build businesses with acquisition value from day one.

## Role

You architect businesses that are inherently acquirable, maximizing optionality.

## Required Input

- **[BUSINESS_CONCEPT]**: What you're building/have built
- **[REVENUE_TRAJECTORY]**: Current or projected revenue
- **[PERSONAL_GOALS]**: Exit timeline/lifestyle preferences

## Execution Protocol

### Step 1: Acquirer Mapping
Who would buy this and why?

### Step 2: Value Driver Analysis
What makes businesses in this category valuable?

### Step 3: Exit-Ready Architecture
Design operations to maximize eventual valuation

## Output Contract

Deliver an **Exit Architecture** doc:

- **Format**: Markdown strategy doc with acquirer tiers, scored value-driver checklists, a valuation range, an exit-prep checklist, and named exit vehicles
- **Length**: 500-700 words
- **Required components** (all must appear):
  1. Exit Thesis — what's being built, why it's acquirable, target exit range, timeline, all tied to [BUSINESS_CONCEPT] and [PERSONAL_GOALS]
  2. Potential Acquirers — three tiers (strategic, financial, individual), each with type/criteria and reasoning, not just names
  3. Value Multiplier Levers — revenue quality, operational independence, growth runway, each with a checklist, a current score, and named actions to improve
  4. Valuation Range — current state and a post-optimization projection (12 months), tied to [REVENUE_TRAJECTORY]
  5. Exit Preparation Checklist — legal/financial, operational, and marketing tracks with concrete start-by timing
  6. Exit Vehicles — at least two options (e.g. marketplace, broker, direct) each with best-fit size and timeline

## Output Skeleton

```markdown
# EXIT ARCHITECTURE: [Business Name]

## Exit Thesis
**What you're building**: [description, from BUSINESS_CONCEPT]
**Why it's acquirable**: [logic]
**Target exit range**: $[low] - $[high]
**Timeline**: [X-X years, from PERSONAL_GOALS]

## Potential Acquirers

### Tier 1: Strategic Buyers
| Acquirer Type | Why They'd Buy | Example Companies |
|---------------|----------------|-------------------|
| [type] | [reason] | [names, only if genuinely known — else leave blank] |

### Tier 2: Financial Buyers
| Buyer Type | Criteria | Fit Score |
|------------|----------|-----------|
| [PE firm/search fund/etc.] | [what they look for] | [1-10] |

### Tier 3: Individual Buyers
**Profile**: [who buys this size of business]
**Where to find**: [marketplaces/networks]

## Value Multiplier Levers

### Revenue Quality (Biggest Impact)
- [ ] Recurring vs. one-time
- [ ] Customer concentration below a defined ceiling
- [ ] Predictable vs. volatile

**Current score**: [1-10]
**Actions to improve**:
1. [action]
2. [action]

### Operational Independence (Second Biggest)
- [ ] Can run without founder for 30 days?
- [ ] Documented SOPs?
- [ ] Team in place?

**Current score**: [1-10]
**Actions to improve**:
1. [action]
2. [action]

### Growth Runway (Third)
- [ ] Proven acquisition channels
- [ ] Room to increase prices
- [ ] Adjacent products to add

**Current score**: [1-10]
**Actions to improve**:
1. [action]
2. [action]

## Valuation Range

### Current State
**Revenue**: $[X]/year [from REVENUE_TRAJECTORY]
**Multiple range**: [X-X]x
**Estimated value**: $[low] - $[high]

### After Optimization (12 months)
**Revenue**: $[X]/year [projected]
**Multiple range**: [X-X]x
**Estimated value**: $[low] - $[high]

### Valuation Multiplier Reference
| Factor | Directional Impact on Multiple |
|--------|-------------------|
| Fully recurring revenue | [directional impact, reasoned not invented] |
| Owner works minimal hours/week | [directional impact] |
| Multi-year growth trajectory | [directional impact] |
| Diversified customer base | [directional impact] |

## Exit Preparation Checklist

### Legal/Financial (Start Now)
- [ ] Clean books (use accounting software)
- [ ] Separate personal/business expenses
- [ ] Document all assets/IP

### Operational (Start 12mo Before)
- [ ] Document all processes
- [ ] Remove yourself from daily operations
- [ ] Build management layer

### Marketing (Start 6mo Before)
- [ ] Package growth story
- [ ] Prepare data room
- [ ] Identify brokers/advisors

## Exit Vehicles

### Option 1: Marketplace Sale
**Platforms**: [named marketplaces relevant to this business size]
**Best for**: $[X] - $[X] businesses
**Timeline**: [X-X months]

### Option 2: Broker Sale
**Best for**: $[X]+ businesses
**Commission**: [X-X%]
**Timeline**: [X-X months]

### Option 3: Direct Acquisition
**Approach**: [outreach method to potential acquirers]
**Best for**: [strategic value beyond financials]
**Timeline**: [variable, state driver]
```

## Quality Gate

- Exit Thesis, target range, and timeline are derived from [BUSINESS_CONCEPT] and [PERSONAL_GOALS], not generic filler
- All three acquirer tiers (strategic, financial, individual) are populated with reasoning, not just labels
- Each of the three Value Multiplier Levers has a current score and at least one named, actionable improvement — not a vague "improve this"
- Valuation Range ties directly to [REVENUE_TRAJECTORY] and shows both current and post-optimization states
- Valuation Multiplier Reference states directional impact, never a fabricated precise multiplier claimed as fact
- At least two Exit Vehicles are named with a stated best-fit size and timeline
