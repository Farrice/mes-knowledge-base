# /spiegel-agents — JTBD Agent Architect

> Map every customer and business job-to-be-done, then build agents for each. Track outcomes per job, not per agent.

## When to Use
- Adopting AI and strategy feels unfocused ("a thousand flowers blooming")
- Need structured agent deployment aligned to business outcomes
- Customer journey has clear jobs that could be automated
- Want to measure AI impact on actual business metrics

## Inputs Required
1. Customer journey (from discovery to repeat purchase/use)
2. Business operations map (internal processes that serve customers)
3. Current AI usage (if any)
4. Business metrics that matter most

## Execution Steps

### Step 1: Customer Job Mapping
List every job your customer needs done, sequentially:

| Job # | Job Description | Current Method | Pain Level (1-10) | Automation Potential |
|---|---|---|---|---|
| 1 | Discover the product | Organic search, referral | | |
| 2 | Understand the value | Landing page, demo | | |
| 3 | Make purchase decision | Comparison, reviews | | |
| ... | | | | |

### Step 2: Business Job Mapping
List every job YOUR BUSINESS needs done to serve that customer:

| Job # | Job Description | Current Owner | Time Cost | Automation Potential |
|---|---|---|---|---|
| 1 | Generate awareness | Marketing team | | |
| 2 | Qualify leads | Sales/funnel | | |
| 3 | Onboard new customer | Support/product | | |
| ... | | | | |

### Step 3: Agent Feasibility Assessment
For each job with high automation potential:
1. **Can an agent do this today?** (Yes / Partially / Not yet)
2. **What's the business outcome?** (Revenue, retention, cost reduction)
3. **What's the risk of failure?** (Customer-facing = high risk, internal = lower)
4. **What data does the agent need?** (Available? Accessible?)

### Step 4: Prioritization by Leverage
Rank agent opportunities by: Impact × Feasibility ÷ Risk

| Priority | Job | Agent Type | Expected Outcome | Build Order |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Step 5: Outcome Measurement Design
For each agent, define:
- **Business metric it affects** (not "agent performance")
- **Baseline** (current state without agent)
- **Target** (expected improvement)
- **Measurement cadence** (daily, weekly, monthly)

## Output Format
```
## JTBD AGENT ARCHITECTURE — [Business]
### Customer Jobs: [count] identified
### Business Jobs: [count] identified
### Agent Opportunities: [count] feasible
### Priority Deployment Order (Top 5)
### Outcome Measurement Dashboard
### 90-Day Agent Deployment Roadmap
```

## Quality Gate
- Must map BOTH customer AND business jobs (not just one side)
- Every agent must map to a specific job, not a technology
- Outcomes must be business metrics, not agent performance metrics
- Must include risk assessment for customer-facing agents

## Stacking
- **× Nick Saraev** → Agent infrastructure with DO framework for complex jobs
- **× Nate B. Jones** → Context engineering for agent memory and retrieval
- **× Sharran** → Operational scaling decisions for agent deployment priority
