# Godin AI Permission Layer

> **Expert**: Seth Godin | **Skill**: seth-godin-brand | **Tier**: Stacking
> **Produces**: AI Permission Layer Design
> **Slash Command**: `/godin-ai-permission`

---

## Purpose

Design AI integrations that DEEPEN brand permission rather than cheapen service. Move from the current "cost reduction" cycle to the opportunity cycle — AI that makes your brand worth MORE, not less.

---

## Inputs Required

1. **Business/Brand** — What brand is integrating AI?
2. **Current AI Usage** — How are you using AI today? (If at all)
3. **Brand Promise** — What do customers expect from you?
4. **Customer Data** — What do you already know about your customers?

---

## Workflow

### Step 1: The Fork Diagnosis

Godin identifies two AI paths:

| Path | Description | Outcome |
|------|-------------|---------|
| **Cost Reduction** (current cycle) | Use AI to cut people, spend less, automate away service | "You can't cost-reduce yourself to greatness" |
| **Permission Deepening** (opportunity) | Use AI to make service harder but more valuable | "Be welcome. Be missed if you're not there" |

**Audit your current AI usage**:

| AI Application | Cost Reduction? | Permission Deepening? | Verdict |
|---------------|----------------|----------------------|---------|
| | | | |

If >50% of your AI usage is cost reduction → you're on the wrong path.

### Step 2: The Techlas Vision

Godin's model: Upload photos of your entire tool chest to a trusted brand. When working on a project, ask the brand's AI: "I need piece X." It responds: "It's next to the widgets" or "You don't have that. Want it by tomorrow?"

**The Permission Escalation**: "The more I teach it, the happier I am. The more I teach it, the more their brand is worth to me, the more likely it is that I don't go to Amazon and buy the cheap one."

**Design YOUR Techlas moment**:
1. What could customers TEACH your AI about themselves?
2. What would your AI know that makes switching costs psychological, not contractual?
3. How does each interaction make the brand MORE valuable, not more annoying?
4. What service could your AI provide that would be MISSED if it disappeared?

### Step 3: The "Welcome and Missed" Test

> AI integration passes if the customer would be: (a) WELCOME it showing up, and (b) MISS it if it were gone.

For each proposed AI feature:

| Feature | Would Customer Welcome It? | Would Customer Miss It? | Pass/Fail |
|---------|--------------------------|------------------------|-----------|
| | | | |

**Anti-patterns** (Godin's "skulking around"):
- ❌ AI that spies on behavior without providing value
- ❌ AI that replaces human service customer didn't want automated
- ❌ AI that makes you an "unpaid doobie" for the platform
- ❌ "Due to unusually heavy call volume" = trust destruction

### Step 4: The AI Buyer Defense

> "When AI is the buyer, you're going to lose. It just goes and buys the cheap one."

**Assess your vulnerability**:
1. Could an AI procurement agent replace your customer's decision-making?
2. If yes — what makes your brand worth more than the cheapest option?
3. How do you make the VALUE unmeasurable by AI? (Stories, trust, relationship, status)

**The Defense**: Build brand value in dimensions AI buyers can't evaluate — trust, emotional connection, community, consistency, status.

### Step 5: The Summer Intern Model

> Godin: "Here is this squadron of summer interns who work for almost free. They're not that good, but they're very eager."

**Design your AI workforce**:
- What tasks get delegated to the "interns"?
- What tasks NEVER get delegated? (Godin: "My writing I do myself")
- How do you be a "good boss of an AI"?
- What's the line between AI-augmented and AI-replaced?

### Step 6: AI Permission Layer Output

```
AI PERMISSION LAYER DESIGN
=============================

Brand: [Name]

CURRENT STATE:
- Cost Reduction: [X]% of AI usage
- Permission Deepening: [X]% of AI usage
- Verdict: [Wrong path / Right path / Mixed]

TECHLAS VISION:
- Customer teaches AI: [what data/preferences]
- AI provides: [what personalized service]
- Switching cost: [psychological, not contractual]
- "Missed if gone": [what specific value disappears]

WELCOME & MISSED TEST:
- Features that pass: [list]
- Features that fail: [cut or redesign]

AI BUYER DEFENSE:
- Vulnerability: [high/medium/low]
- Unmeasurable value: [what AI can't evaluate]
- Defense strategy: [how to protect]

SUMMER INTERN BOUNDARIES:
- Delegate: [tasks for AI]
- Protect: [tasks humans keep]
- Boss protocol: [how to manage AI well]
```

---

## Output Schema

| Field | Type | Required | Notes |
|---|---|---|---|
| `Current State` | 2 percentages + 1 verdict enum | Yes | Cost-reduction % and permission-deepening % must sum toward 100; verdict is Wrong path / Right path / Mixed, not freeform. |
| `Techlas Vision` | 4 short answers | Yes | Must include at least one concrete "missed if gone" value — a feature with no missed-if-gone answer has failed Step 2. |
| `Welcome & Missed Test` | pass-list + fail-list | Yes | Every proposed feature from Step 3's table must appear in exactly one list. |
| `AI Buyer Defense` | vulnerability enum (high/medium/low) + 2 free-text fields | Yes | Unmeasurable-value field cannot be empty if vulnerability is medium or high. |
| `Summer Intern Boundaries` | delegate-list + protect-list + 1 protocol line | Yes | Protect-list must be non-empty — a design with nothing protected has skipped Step 5. |

---

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Fork Assessment | Clear cost-reduction vs. permission-deepening ratio |
| Techlas Moment | At least 1 AI feature that customers would MISS |
| Welcome Test | All proposed features pass welcome + missed |
| Buyer Defense | Unmeasurable value clearly articulated |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/godin-brand-promise` | AI deepens the specific promise, not generic service |
| `/ai-brain` | AI Brain architecture designed with permission-first philosophy |
| `/godin-better-not-louder` | AI serves the Gajist number, not infinite scale |
| `/jensen-gotch-retrieval` | AI retrieval optimization + AI permission = full AI strategy |
