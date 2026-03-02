---
description: On-demand intent refinement — sharpen a raw idea, redirect a drifting conversation, or re-align mid-task at any point
---

# Refine Intent (On-Demand, Mid-Flight)

Use this **at any point** in a conversation to sharpen what you're working on. Unlike `/validate-intent` (pre-flight), this works mid-flight — when you've drifted, when a new idea hits, or when you want to redirect.

## Execute the Intent Pipeline

Read and follow `directives/intent-pipeline.md`. Same 4 stages, but start from current context:

1. **SCORE** — Rate current intent sharpness 1-5
2. **SHARPEN** — If Score ≤ 3, run DICE on missing dimensions only
3. **ROUTE** — Check if new/different experts are needed
4. **PRESENT** — Show refined objective, await confirmation

## After Refinement

- **If the session goal changed** → Update `.agent/session-state.md`
- **If new experts are needed** → Re-route via the pipeline
- **If swarm-worthy** → Suggest `/swarm` or `/parallel-swarm`
- **If same direction, just sharper** → Continue execution with refined objective

Do NOT execute the refined objective until the user confirms.

---

## When to Use
- You've been talking for a while and want to re-center
- A new idea or direction just emerged
- Current output isn't quite what you wanted
- You want to pivot the session
- Conversation has drifted from the real goal

## How This Differs from /validate-intent

| | `/validate-intent` | `/refine-intent` |
|---|---|---|
| **When** | Start of task (pre-flight) | Any time mid-conversation |
| **Purpose** | Catch raw intent before work begins | Re-center, redirect, or sharpen mid-work |
| **Tone** | "Let me understand before we start" | "Let me make sure we're still on target" |
