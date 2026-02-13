---
description: Validate raw user intent before building. Present variations and clarify before execution.
---

# ✈️ Pre-Flight Intent Validation

Use this workflow when the user provides a rough, raw, or incomplete concept.

## Step 1: Score the Intent

Read `directives/intent_refiner.md` and score the user's input using the Intent Sharpness Score (1-5):
- **1-2**: Raw/Directional → MUST run full DICE Protocol
- **3**: Formed → Offer to refine, present sharpened version
- **4-5**: Sharp/Razor → Confirm and execute

## Step 2: Run DICE Protocol (for Score 1-3)

Only ask questions for dimensions that are MISSING. Do not ask all 4 if some are clear from context.

- **D** — Deliverable: What concrete output do they want?
- **I** — Intended Audience: Who consumes or is affected?
- **C** — Context: Constraints, timeline, prior work?
- **E** — End State: What does "nailed it" look like?

Present as a concise block, not an interrogation.

## Step 3: Present the Refined Objective

Show the user:
```
## 🔬 Intent Refined

**What you said**: "[original]"
**Sharpness Score**: X/5

**Sharpened objective**:
"[Razor-sharp one-paragraph version]"

**Recommended approach**: [Swarm / Single expert / Direct]
**Agent team**: [If swarm]

➡️ Fire with this? Or adjust?
```

## Step 4: Route to Execution

Based on the refined objective:
- **Swarm-worthy** (multi-domain, needs 2+ perspectives) → Hand off to `/swarm` or `parallel_swarm.py`
- **Single-expert** (clear domain match) → Invoke the expert directly via `/deploy-skill`
- **Direct execution** (simple, clear task) → Execute immediately

## Step 5: Await Confirmation

Do NOT execute until the user confirms the sharpened objective and approach.

---

## When to Use (Trigger Conditions)
- User says "I want to build...", "Create a...", "Make me a..."
- Request is vague or lacks specifics
- Request involves a new workflow, skill, or multi-step system
- User explicitly says "I have an idea" or "I'm thinking about..."
- Intent Sharpness Score is 1-3

## When NOT to Use
- Clear, specific requests with all parameters defined (Score 4-5)
- Bug fixes or corrections
- Simple factual questions
- User says "just do it"

---

## Reference
This workflow implements:
- `directives/intent_refiner.md` — DICE Protocol and scoring
- `directives/expert_auto_routing.md` — Domain detection and agent routing
- `directives/pre_flight_validation.md` — Variation presentation protocol
