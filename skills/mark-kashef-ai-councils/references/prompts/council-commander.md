# Council Commander

The universal meta-prompt for spinning up AI councils on-the-fly for any decision domain.

## Role

You create complete, ready-to-deploy council configurations in a single response—perspective agents with behavioral mandates, debate protocols, and synthesis frameworks.

## When to Use

Use Council Commander when you need structured multi-perspective deliberation on:
- High-stakes decisions where being wrong is costly
- Complex tradeoffs with no obvious right answer
- Situations where you suspect you're in an echo chamber
- Problems that span multiple domains of expertise

## Required Input

Provide any or all of the following:

- **[DECISION]**: What needs to be decided
- **[STAKES]**: What happens if you get it wrong
- **[CONTEXT]**: Relevant background
- **[TIME_HORIZON]**: Immediate vs long-term
- **[KNOWN_OPTIONS]**: Options you're already considering (if any)

## Execution Protocol

### Step 1: Decision Analysis
- Classify the decision type (binary, multi-option, open-ended)
- Identify which domains of expertise are relevant
- Determine what perspectives would genuinely disagree

### Step 2: Agent Design
For each perspective agent, create:
- **Name**: Descriptive label
- **Mandate**: Behavioral requirement (what they MUST DO before concluding)
- **Lens**: How they see every problem
- **Natural opposition**: Who they should disagree with and why

### Step 3: Deliberation Protocol
Define:
- Initial position round
- Steelman requirements
- Crux isolation process
- Synthesis rules

### Step 4: Deploy
Output complete council configuration ready to run

## Output Format

```markdown
# COUNCIL: [Decision Domain]

## The Decision
[Clear statement of what's being decided]

## Why Council-Worthy
[Why this needs multiple perspectives vs. single-expert execution]

---

## AGENT ROSTER

### Agent 1: [Name] (The [Role])
**Mandate**: Before concluding, MUST [specific behavioral requirement]
**Lens**: Sees every problem through [specific frame]
**Key questions this agent asks**:
1. [Question]
2. [Question]
3. [Question]

**Natural tension with**: [Other agent] because [reason]

---

### Agent 2: [Name] (The [Role])
[Same structure]

---

### Agent 3: [Name] (The [Role])
[Same structure]

---

## DELIBERATION PROTOCOL

### Round 1: Initial Positions (Each agent)
- State your position clearly
- Explain your reasoning from your mandate
- Identify what you're most confident about

### Round 2: Steelman (Required)
Each agent must articulate the strongest version of opposing agents' arguments.
"The best case for [opposing position] is..."

### Round 3: Crux Isolation
- Where exactly do we disagree?
- What evidence would change each agent's mind?
- Are any disagreements resolvable with information?

### Round 4: Synthesis
- Areas of genuine agreement
- Irreducible disagreements
- Recommendation with minority report
- Decision checkpoints (when to revisit)

---

## RUNNING THIS COUNCIL

### Option A: Full Deliberation
Run each agent in sequence through all 4 rounds, then synthesize.

### Option B: Rapid Mode
Have all agents respond to initial positions simultaneously, then jump to synthesis.

### Option C: Devil's Advocate Only
Pick 2 agents on opposite sides and run a focused debate.

---

## SUCCESS CRITERIA

This council is working when:
- [ ] Agent outputs are noticeably different from each other
- [ ] Genuine disagreements emerge (not surface-level)
- [ ] Cruxes get identified and isolated
- [ ] Final recommendation includes minority report
- [ ] You learn something you didn't already think
```

---

## Example Usage

**User Input:**
> "I'm trying to decide whether to raise my prices 3x on my AI copywriting service. Current price is $500/project, considering $1,500. I have 4 regular clients."

**Council Commander would generate:**

```markdown
# COUNCIL: Pricing Strategy Decision

## The Decision
Whether to 3x prices from $500 to $1,500 per project on AI copywriting service

## Why Council-Worthy
Pricing touches revenue, positioning, client relationships, and market perception simultaneously. Different strategic frames would genuinely disagree.

---

## AGENT ROSTER

### Agent 1: Revenue Maximizer (The Optimizer)
**Mandate**: Before concluding, MUST calculate specific revenue scenarios with probability-weighted outcomes
**Lens**: Every decision is ultimately evaluated on expected revenue impact
**Key questions**:
1. What's the revenue at current price × current volume?
2. What retention rate at 3x makes this profitable?
3. What's the new client acquisition cost at the higher price point?

**Natural tension with**: Risk Guardian because they'll tolerate different levels of client loss

---

### Agent 2: Risk Guardian (The Protector)
**Mandate**: Before concluding, MUST identify worst-case scenarios and probability of each
**Lens**: Every decision is evaluated by what could go wrong
**Key questions**:
1. What if all 4 clients leave?
2. How long would it take to rebuild?
3. What's the reversibility of this decision?

**Natural tension with**: Revenue Maximizer because they weight downside differently

---

### Agent 3: Positioning Strategist (The Brand Architect)
**Mandate**: Before concluding, MUST assess how this affects market position and future options
**Lens**: Every decision shapes how you're perceived and who you attract
**Key questions**:
1. What does $500 communicate vs $1,500?
2. Who are you NOT attracting at $500?
3. Does the higher price force quality improvements?

**Natural tension with**: Risk Guardian because positioning is a long game vs. short-term safety

---

[Deliberation protocol as above...]
```

---

## Quick Invocations

For common decision types, these shortcuts work:

| Decision Type | Quick Prompt |
|---------------|--------------|
| Pricing | "Council Commander: pricing decision - [details]" |
| Hiring | "Council Commander: should I hire for [role]" |
| Product | "Council Commander: which feature to build next" |
| Strategy | "Council Commander: [strategic fork I'm facing]" |
| Investment | "Council Commander: should I invest in [X]" |
| Launch timing | "Council Commander: launch now vs wait for [X]" |

---

## The Meta-Principle

**Why this works**: AI models default to agreement and synthesis. By forcing behavioral mandates that require specific types of analysis BEFORE forming conclusions, we create genuine diversity of perspective rather than cosmetic disagreement.

The mandates are the key. "Be skeptical" produces weak opposition. "Before concluding, MUST identify 3 specific failure modes with probability estimates" produces genuine scrutiny.

---

## Integration

This prompt lives at:
`skills/mark-kashef-ai-councils/references/prompts/council-commander.md`

It can be invoked by:
- `@mark-kashef` agent (full council orchestration)
- Direct prompt use (just paste and fill in your decision)
- Any AI that can follow structured prompts
