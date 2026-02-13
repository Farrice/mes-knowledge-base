---
description: Contextual skill recommendation — analyzes what you're working on right now and deploys the right experts
---

# /recommend — Contextual Skill Deployment

Analyze what Farrice is currently working on and recommend which skills, agents, and prompts to deploy — then offer to execute immediately.

## Usage

```
/recommend [describe what you're working on or trying to accomplish]
```

Examples:
- `/recommend I'm writing a sales page for my coaching offer`
- `/recommend I need to figure out my first product to launch`
- `/recommend I'm stuck on my LinkedIn content strategy`
- `/recommend I want to build an agent that does X`

## Steps

### 1. Parse Intent
Understand what Farrice is trying to accomplish. Don't just match keywords — read the deeper intent:
- What is the **actual outcome** he wants?
- What **decision** is he trying to make?
- What **deliverable** does he need to produce?
- Is this a **thinking** problem or an **execution** problem?

### 2. Skill Match
// turbo
Read `GEMINI.md` to scan the full skill and agent roster. For each potentially relevant skill:

- Read the `SKILL.md` to confirm relevance
- Check the prompt arsenal for the most applicable prompt
- Assess stacking opportunities with other skills

### 3. Produce Recommendation

```
SKILL DEPLOYMENT RECOMMENDATION

## What You're Doing
[Restate the task in clear terms]

## Primary Skill
**[Skill Name]** → [specific prompt to use]
- **Why this one**: [What makes it the right tool]
- **What it produces**: [Expected deliverable]
- **Read first**: `skills/[skill]/references/prompts/[prompt].md`

## Support Skills (Stack For Better Results)
1. **[Skill 2]** → [prompt] — [what it adds]
2. **[Skill 3]** → [prompt] — [what it adds]

## Recommended Execution Order
1. First: Deploy [primary skill/prompt] to produce [output]
2. Then: Run [support skill] on that output to [enhance/validate/expand]
3. Finally: [Polish/deploy step]

## Agent Mode (Optional)
If you want the full expert persona instead of just the prompt:
> Invoke @[agent-name] — they'll approach this as [expert] would, using [methodology]
```

### 4. Offer Immediate Execution

Don't just recommend — offer to DO it:

> "Want me to deploy this now? I'll read the skill files, embody the expert, and produce the deliverable. Just give me [any needed inputs]."

If the task is suitable for a swarm (multiple experts needed in parallel):

> "This is a good swarm candidate. I can deploy @[agent-1], @[agent-2], and @[agent-3] simultaneously. Want me to run `/swarm` on this?"

## Matching Logic

When multiple skills could apply, prioritize:

1. **Specificity** — A prompt designed for exactly this task beats a general skill
2. **Practitioner mode** — Skills that PRODUCE the deliverable beat skills that advise on it
3. **Stacking potential** — Skills that compound with others create more value
4. **Revenue proximity** — If multiple skills match equally, prefer the one closer to generating income

## Anti-Hoarding Check

If Farrice is asking about something where he already has a deployed skill but might not remember it, lead with:

> "You already have this! [Skill name] has a prompt called [prompt] that does exactly this. Want me to run it?"

This is the antidote to the "1,000 extractions, forgot to use them" pattern. The system remembers so Farrice doesn't have to.
