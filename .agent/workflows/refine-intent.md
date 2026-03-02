---
description: On-demand intent refinement — sharpen a raw idea, redirect a drifting conversation, or re-align mid-task at any point
---

# 🔬 Refine Intent (On-Demand)

Use this **at any point** in a conversation to sharpen what you're working on. Unlike `/validate-intent` (which is pre-flight), this command works mid-flight — when you've drifted, when a new idea hits, or when you want to redirect the conversation.

## When to Use

- You've been talking for a while and want to **re-center**
- A new idea or direction just emerged and it's still raw
- You realize the current output isn't quite what you wanted
- You want to **pivot** the session to a different objective
- You're doing a raw brain dump and need it shaped into something executable
- Conversation has drifted and you want to **snap back** to the real goal

## Step 1: Capture the Raw Input

// turbo
Take whatever the user just said — raw dump, half-formed thought, verbal stream of consciousness — and identify the core signal.

Read `directives/intent_refiner.md` for the full protocol. Key question: **What is the actual outcome they want?**

## Step 2: Score & DICE

// turbo
**Score the intent** (1-5 scale):

| Score | Label | Action |
|-------|-------|--------|
| **1** | Raw thought | Ask ALL missing DICE questions |
| **2** | Directional | Ask 2-3 targeted DICE questions |
| **3** | Formed | Present sharpened version, ask "Is this right?" |
| **4** | Sharp | Confirm briefly, proceed |
| **5** | Razor | Execute immediately |

**DICE Protocol** — only ask what's MISSING:
- **D** — Deliverable: What concrete thing do you want in your hands?
- **I** — Intended Audience: Who consumes or is affected?
- **C** — Context: Constraints, timeline, prior work?
- **E** — End State: What does "nailed it" look like?

**Anti-interrogation rule**: Present missing questions as a concise block, not a 20-question survey. One round max.

## Step 3: Present the Refined Objective

```
## 🔬 Intent Refined

**What you said**: "[original raw input]"
**Sharpness Score**: X/5 → [Label]

**Sharpened objective**:
"[Razor-sharp, one-paragraph version ready for execution]"

**What changed**: [1 sentence on what was clarified, tightened, or redirected vs. where the conversation was heading]

**Recommended approach**: [Swarm / Single expert / Direct execution]
**Agent team**: [If applicable — use the combo reference table from intent_refiner.md]

➡️ **Fire with this?** Or adjust?
```

## Step 4: Re-Route if Needed

After refinement:
- **If the session goal changed** → Update the conversation label (from `/session-kickoff`)
- **If new experts are needed** → Run `/recommend` to surface the right skills
- **If swarm-worthy** → Suggest `/swarm` or `/parallel-swarm`
- **If same direction, just sharper** → Continue execution with the refined objective

## Step 5: Await Confirmation

Do NOT execute the refined objective until the user confirms. One "fire?" prompt, then move.

---

## How This Differs from /validate-intent

| | `/validate-intent` | `/refine-intent` |
|---|---|---|
| **When** | Start of task (pre-flight) | Any time mid-conversation |
| **Purpose** | Catch raw intent before work begins | Re-center, redirect, or sharpen mid-work |
| **Scope** | Full pre-flight + routing | Quick refinement + optional re-routing |
| **Tone** | "Let me understand before we start" | "Let me make sure we're still on target" |

Both use `directives/intent_refiner.md` as their engine. The difference is timing and context.

---

## Reference
This workflow implements:
- `directives/intent_refiner.md` — DICE Protocol, scoring, and agent recommendation
- `directives/expert_auto_routing.md` — Domain detection for re-routing
