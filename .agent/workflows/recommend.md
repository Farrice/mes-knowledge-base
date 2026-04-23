---
description: Contextual skill recommendation
---

# /recommend — Autonomous Orchestration Engine

Analyze what Farrice is currently working on and deploy the exact right experts, workflows, and execution chains — then offer to execute immediately. This engine uses predictive intent, awareness classification, emotional subtext detection, prerequisite intelligence, and revenue proximity scoring to produce world-class recommendations.

## Usage

```
/recommend [describe what you're working on or trying to accomplish]
/recommend --discovery  (interactive narrowing mode)
```

Examples:
- `/recommend I'm writing a sales page for my coaching offer`
- `/recommend I need to figure out my first product to launch`
- `/recommend I'm stuck on my LinkedIn content strategy`
- `/recommend I want to build an agent that does X`
- `/recommend --discovery` (I don't know what I need)

---

## Steps

### 0. Most-Aware Bypass Check

**Before anything else**, check if the user already knows exactly what they want:

If the query contains explicit workflow/expert references (e.g., "run /proof-copy-engine", "use @david-deutsch", "deploy /storybrand"), **skip the entire recommendation engine** and go straight to execution:

> "You know exactly what you need. Loading @[expert] and deploying /[workflow] now. Give me [any needed inputs]."

Detect via pattern: query starts with "run", "deploy", "execute", "load", "use", "do", "start" followed by a `/command` or `@expert` reference. If in doubt:

// turbo
```bash
python3 execution/expert_router.py awareness "[user's query]"
```

If result = `MOST_AWARE` with `instant_execution` routing → bypass. Otherwise continue.

---

### 1. Anti-Hoarding Recall (Capability Check)

Before recommending new work, check if Farrice already has deployed assets for this:

// turbo
```bash
python3 execution/memory_store.py search "[user's query]" 2>/dev/null || echo "No memory hits"
```

Also mentally scan: Has this exact expert/workflow combination been used in a recent session? If so:

```
🔄 CAPABILITY RECALL
You already have this:
- @[expert-name] + /[workflow] (used [N]x)
- Deliverable: [description] (conversation [id])
→ Want me to re-run with updates, or are you looking for something different?
```

This is the antidote to the "1,000 extractions, forgot to use them" pattern. The system remembers so Farrice doesn't have to.

**If the user confirms they want the existing asset**: Load and re-deploy. **Skip remaining steps.**
**If the user wants something different**: Continue to Step 2.

---

### 2. Intelligence Diagnostic (Pre-Routing)

Run the full intelligence diagnostic to classify the query before routing:

// turbo
```bash
python3 execution/expert_router.py diagnose "[user's query]"
```

This produces three intelligence layers simultaneously:
- **Awareness Stage**: Where the user is in their journey (Unaware → Most Aware)
- **Emotional Subtext**: Hidden emotional states disguised as tactical questions
- **Revenue Proximity**: How close matched experts are to income generation

**Read the output and apply these routing rules:**

#### Awareness-Based Routing

| Stage | Routing Behavior |
|-------|-----------------|
| **Unaware** | Jump to Step 3 (Discovery Mode) |
| **Problem Aware** | Prioritize diagnostic/audit workflows first |
| **Solution Aware** | Standard routing (continue to Step 4) |
| **Product Aware** | Switch to comparison mode — show side-by-side expert capabilities |
| **Most Aware** | Should have been caught in Step 0 — execute immediately |

#### Emotional Subtext Gate

If the diagnostic detects emotional subtext, the recommendation becomes a **two-phase protocol**:

```
⚠️ EMOTIONAL INTELLIGENCE GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I notice [matched patterns]. Before we deploy tactical expertise,
let's process this first:

Phase 1: @[pre_expert] → /[pre_workflow]
  → [message — why this comes first]

Phase 2: THEN your tactical request
  → [original expert/workflow recommendation]

This sequence matters. [Expert source] found that emotional processing
must precede cognitive change for lasting results.

Want to start with Phase 1, or override and go straight to tactical?
```

**Hard rule**: Never suppress the emotional gate. Always surface it. The user can override, but we always flag it.

---

### 3. Discovery Mode (Interactive Narrowing)

**Trigger**: User says `/recommend --discovery`, query is too vague (Awareness = `unaware`), or the router returns zero matches.

Instead of asking "what do you want?", use the **Intent Signal Field** (Nate B. Jones) to generate a prediction:

```
🔍 DISCOVERY MODE — Predictive Intent

Based on [what I observed], here's what I think you need:

📌 Prediction: [Predicted deliverable/workflow]
   Why I think this: [Signal evidence — emphasis, omission, contradiction]

Is this close? Tell me what's wrong with my prediction, and I'll
sharpen it in one correction round.

If you're truly blank, quick diagnostic:

1. What are you trying to produce?
   □ Written content (copy, posts, scripts, emails)
   □ A strategy or plan (business, brand, launch)
   □ A product or offer (digital product, service, funnel)
   □ Clarity on a decision (what to do, which path, priorities)
   □ Something else: ___

2. Where are you in the process?
   □ Starting from zero — I need direction
   □ I have a rough idea — I need a framework
   □ I have a draft — I need to improve it
   □ I'm blocked — something's stopping me

3. What's the emotional temperature?
   □ Energized — I'm ready to build
   □ Overwhelmed — too many options
   □ Stuck — I can't move forward
   □ Frustrated — something isn't working
```

Based on answers, re-run Steps 4-7 with a sharpened query. If emotional temperature is "Stuck" or "Overwhelmed", trigger the Emotional Subtext Gate from Step 2.

---

### 4. Layer 1: Expert Match (Intelligent Routing)

// turbo
Run the expert router with synonym expansion:
```bash
python3 execution/expert_router.py route "[user's query]" -n 5
```

This engine:
- Expands natural language through a 200-term synonym map
- Scores 96 experts across 15 domains
- Falls back to triage paths for vague queries (emotional blocks → Dr. K, decisions → Jim O'Shaughnessy, beginner → AI Chris Lee)

**Capture the top 3-5 expert matches and their domains.**

---

### 5. Layer 2: Workflow Match (Precision Commands)

// turbo
Cross-reference against the 630+ available workflows:
```bash
python3 execution/workflow_router.py search "[user's query]"
```

From the results:
- Surface the **top 3-5 most relevant `/command` workflows**
- Prioritize workflows that produce tangible deliverables over diagnostic/audit workflows
- Note any workflow that belongs to a matched expert (these are highest-signal)

---

### 6. Layer 3: Compound Detection

// turbo
Check for force-multiplier expert pairings:
```bash
python3 execution/expert_router.py compounds "[user's query]"
```

Compounds = two experts whose combined output is greater than the sum of parts. When detected, this triggers the **Mission Blueprint** in the output (Step 7).

---

### 7. Layer 4: Context Retriever (Semantic Deep Search)

// turbo
Search the full knowledge base for relevant chunks:
```bash
python3 execution/context_retriever.py search "[user's query]"
```

This searches 3,200+ indexed chunks across all skills, agents, and genius files. Use the results to:
- Surface **specific prompts** within a SKILL.md that match the intent
- Identify genius-file patterns that apply to this task
- Find prior work or methodology that's relevant but wouldn't be found by keyword matching

---

### 8. Prerequisite & Revenue Check

For the top recommended workflows, check prerequisites and revenue distance:

// turbo
```bash
python3 execution/expert_router.py prereqs "[top recommended workflow]"
```

// turbo
```bash
python3 execution/expert_router.py revenue "[top expert match]"
```

If prerequisites are detected, **automatically prepend them** to the execution chain. Do not recommend a workflow without its required precursors.

---

### 9. Produce Recommendation

Synthesize all layers into a single actionable brief. The output format depends on complexity:

#### Standard Output (Solution Aware, no compounds)

```
🎯 SKILL DEPLOYMENT RECOMMENDATION

## What You're Doing
[Restate the task in clear terms — demonstrate you understood the real intent]

## Awareness Level
[Stage] — [description of what this means for routing]

## Primary Expert
**@[expert-name]** → [specific skill/prompt to use]
- **Why this one**: [What makes it the right tool — not just domain match, but WHY]
- **What it produces**: [Expected deliverable]
- **Revenue Distance**: [0-3] — [label: e.g., "Direct revenue" or "Two steps from revenue"]

## Recommended Workflows
1. `/[workflow-1]` — [what it does] ⭐ Primary
2. `/[workflow-2]` — [what it adds as a stacking option]
3. `/[workflow-3]` — [quality gate or polish step]

## Execution Chain (Prerequisite-Aware Order)
[If prerequisites detected:]
⚠️ This workflow has prerequisites. Full chain:
1. **Prerequisite**: `/[prereq-1]` → produces [output]
2. **Prerequisite**: `/[prereq-2]` → produces [output]
3. **Primary**: `/[main-workflow]` → produces [deliverable]
4. **Enhance**: `/[support-workflow]` → adds [dimension]
5. **Validate**: `/[quality-gate]` → catches [failure modes]

[If no prerequisites:]
1. **Start**: Deploy `/[primary-workflow]` → produces [output]
2. **Enhance**: Run `/[support-workflow]` on the output → adds [dimension]
3. **Validate**: Run `/[quality-gate]` → catches [failure modes]
4. **Deploy**: [Final output step]

## ⚠️ Pre-Mortem Check
- **What could go wrong**: [e.g., "Running /proof-copy-engine before your offer is designed
  will produce beautiful copy for the wrong product"]
- **Prerequisite check**: [Already addressed above, or "All clear — no missing prerequisites"]
- **Reversibility**: [Two-way door: can redo cheaply | One-way door: needs more validation]

## Deep Knowledge Surfaced
📚 Context retriever found: [relevant chunk from genius file or methodology]
→ Key insight: "[specific principle or framework that applies]"

## Support Experts (Stack For Better Results)
1. **@[expert-2]** → [what they add] (Revenue Distance: [N])
2. **@[expert-3]** → [what they add] (Revenue Distance: [N])
```

#### Compound Pipeline Output (When compounds detected)

When compounds are detected, replace the standard "Compound Pairing" section with a **Mission Blueprint**:

```
## ⚡ MISSION BLUEPRINT: [Goal]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 1: [ROLE]          @[expert-1] → [deliverable]
  Handoff: [What Phase 2 receives from Phase 1]

Phase 2: [ROLE]          @[expert-2] → [deliverable]  
  Handoff: [What Phase 3 receives from Phase 2]

Phase 3: [ROLE]          @[expert-3] → [deliverable]
  Handoff: [What Phase 4 receives from Phase 3]

Phase 4: [ROLE]          @[quality-gate] → [validation]
  Handoff: Final validated output

Estimated workflow count: [N] | Swarm candidate: [YES/NO]
Revenue Distance: [lowest distance in chain] — [label]
```

---

### 10. Offer Immediate Execution

Don't just recommend — offer to **DO it**:

> "Want me to deploy this now? I'll load the expert context, embody the methodology, and produce the deliverable. Just give me [any needed inputs]."

If the task is suitable for a swarm (3+ experts needed):

> "This is a swarm candidate. I can deploy @[agent-1], @[agent-2], and @[agent-3] simultaneously. Want me to run `/swarm` on this?"

If handoff chains apply:

> "This is a multi-step mission. Recommended chain: @[expert-1] → @[expert-2] → @[expert-3]. Want me to run `/campaign` or `/strike` to coordinate?"

If emotional subtext was detected but overridden:

> "You overrode the emotional gate. That's fine — but if you hit a wall during execution, circle back to @[pre_expert] for Phase 1 processing."

---

## Matching Priority Logic

When multiple skills could apply, prioritize:

1. **Revenue proximity** — Closer to revenue beats further from revenue (tie-breaker #1, not #4)
2. **Prerequisite completeness** — A workflow whose prerequisites are already met beats one that requires new work
3. **Specificity** — A workflow designed for exactly this task beats a general skill
4. **Practitioner mode** — Skills that PRODUCE the deliverable beat skills that advise on it
5. **Compound potential** — Skills that compound with others create more value
6. **Recency** — Recently forged or evolved skills may have deeper coverage

## Error Handling

| Scenario | Action |
|---|---|
| Zero expert matches + zero triage | Offer Discovery Mode |
| Expert match but no workflow match | Load that expert's SKILL.md and recommend manually |
| All matches feel tangential | Ask one clarifying question, then re-route |
| User says "that's not what I meant" | Switch to Discovery Mode immediately |
| Emotional subtext + user overrides | Flag and continue, but note the override |
| Prerequisite missing + user insists | Execute but add pre-mortem warning |
| Memory store unavailable | Skip Anti-Hoarding gracefully, proceed with routing |
