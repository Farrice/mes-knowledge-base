---
description: Decompose any phenomenon into its engineering specs using Bach's 4-step method — function, mechanism, substrate test, phase transition
---

# Computational Phenomenology

> Bach's core analytical method. Takes any concept, system, or experience and reduces it from "mysterious" to "mechanism" through 4 engineering-grade steps.

## When to Use

- A concept seems important but you can't explain WHY it works
- You're designing a system and need to understand what you're actually building
- Something works in practice but nobody can articulate the mechanism
- You want to strip mystery from a domain without losing its power

## The 4-Step Protocol

### Step 1: Functional Decomposition

**Question**: "What function does [X] serve? What would break if [X] didn't exist?"

Map the phenomenon to its functional role. Don't describe what it looks like — describe what it does. What problems does it solve? What would happen to the system if this phenomenon vanished?

**Output**: A clear statement of function — "X exists because it solves Y problem for the system."

**Example**: "Brand loyalty exists because it solves the reacquisition cost problem — the brand doesn't have to convince the customer from scratch each time."

### Step 2: Minimum Viable Mechanism

**Question**: "What is the simplest program that would produce this function?"

Design — don't describe — the minimum viable mechanism. Fewer moving parts than the phenomenon you're modeling, yet reproducing its key behaviors.

This is Bach's Engineering Stance: "The advantage of the engineering perspective is that you can constrain your design in ways that you cannot from the purely observational, purely descriptive method."

**Output**: A mechanism with the fewest possible components that still produces the observed behavior.

**Example**: "Brand loyalty = (positive reinforcement loop) + (identity attachment) + (switching cost amplifier). Three components, same behavior."

### Step 3: Substrate Independence Test

**Question**: "Can this mechanism run on different hardware? If yes, the mystery dissolves. If no, what's substrate-dependent?"

Test whether the mechanism is a pattern (software) or a property of a specific substrate (hardware). If it can run on different substrates, it's a "spirit" in Bach's framework — a self-organizing causal pattern.

**Output**: Classification as substrate-independent (software/spirit) or substrate-dependent (hardware-bound), with identified persistence conditions.

**Example**: "Brand loyalty runs on physical stores, websites, social media, word of mouth — it's substrate-independent. It's a spirit. Its persistence conditions are: consistent positive reinforcement + identity resonance + perceived switching cost."

### Step 4: Phase Transition Mapping

**Question**: "What are the ignition conditions? Not gradual — what's the spark that makes it coherent?"

Identify the phase transition — the moment components stop being independent and become a coherent system. This isn't incremental. It's "the phase transition that happens when consciousness ignites."

**Output**: Ignition conditions — what must be true for the system to achieve coherence.

**Example**: "Brand loyalty ignites when the customer stops evaluating and starts identifying. The phase transition requires: 3+ positive experiences + 1 identity-resonant moment + 1 social validation. Before this: consideration. After this: loyalty."

---

## Output Format

```
PHENOMENON: [What you're analyzing]

1. FUNCTION: [What it does, what breaks without it]
2. MECHANISM: [Simplest program that produces it]
3. SUBSTRATE: [Independent/dependent, persistence conditions]
4. IGNITION: [Phase transition conditions]

ENGINEERING SPEC: [One-paragraph synthesis — how to build or deploy this]
```

## Quality Gate

- Does the mechanism have fewer moving parts than the phenomenon?
- Can you explain each component of the mechanism independently?
- Did you test substrate independence by moving it to at least 2 different substrates?
- Did you identify a specific phase transition, not a gradual accumulation?

If any answer is no, iterate.

## Cross-Stack

- Pair with **Postmodernist Trap Audit** to verify your mechanism against ground truth
- Feed into **Phase Transition Design** when you want to engineer the ignition conditions you identified
- Use before **Dan Koe's Knowledge Alchemy** to understand WHAT you're extracting before compressing it
