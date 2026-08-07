---
description: Generate Operator Coach steering prompts for kickoff, midpoint, or closeout
---

# Steering Compass

## Load

Read:

1. `semantic_libraries/antigravity/primitives/high-floor-operator-os.md`
2. `semantic_libraries/antigravity/primitives/collaborative-steering-compass.md`
3. `semantic_libraries/antigravity/references/no-lazy-path-gate.md`
4. `semantic_libraries/antigravity/primitive-map.md`

## Inputs

- Current objective or artifact.
- Current stage: kickoff, midpoint, closeout, or ad hoc.
- Depth tier: light, standard, deep, or parallel if stated.
- Known outputs, validations, or decisions.
- User's desired speed and depth, if stated.
- Fast approval phrase, if present, such as "go with your verdict" or "do the recommended path."

## Execution

1. Classify the tier: Light, Standard, Deep, or Parallel. Default to Standard unless clearly Light.
2. If Light, answer directly unless the user explicitly asks for steering.
3. For Standard, identify the best-fit workflow/skill/persona stack and one practical risk/opportunity.
4. For Deep, name the full arsenal path, critique/validation step, and quality bar.
5. For Parallel, state that true Codex subagents require explicit delegation and a briefing packet.
6. If the user gives a fast approval phrase, execute the recommended path directly when the prior verdict contains a clear next action; only ask a question when execution would be risky or ambiguous.
7. Name the decision or next action that would speed the session up.
8. Apply the No-Lazy-Path Gate before returning.

## Output Shapes

### Kickoff

```markdown
## Steering
- **Best path:** [workflow/path] - [rationale]
- **Watch:** [risk/opportunity] - [why it matters]
- **Fastest decision:** [decision that improves speed or quality]
```

### Midpoint

```markdown
## Steering Checkpoint
- **What changed:** [state update]
- **Next best fork:** [recommended fork]
- **Tradeoff to watch:** [risk/opportunity]
```

### Closeout

```markdown
## 3 Next Prompts
1. **Use Now**
   - **When to use:** [condition that makes this the right next move]
   - **Why this is recommended:** [leverage, risk, or learning]
   - **Prompt:** `[copy-paste continuation prompt]`
   - **Expected output:** [what gets produced]
   - **Quality bar:** [what makes it worth shipping]
   - **Skip if:** [when this would be overkill or wrong]
   - **Suggested skills/workflows:** [exact routes]
2. **Harden**
   - **When to use:** [condition that makes validation or repair the right next move]
   - **Why this is recommended:** [risk reduced or trust gained]
   - **Prompt:** `[copy-paste continuation prompt]`
   - **Expected output:** [what gets produced]
   - **Quality bar:** [what makes it trustworthy]
   - **Skip if:** [when this would be overkill or wrong]
   - **Suggested skills/workflows:** [exact routes]
3. **Expand**
   - **When to use:** [condition that makes reusable system/product/content expansion right]
   - **Why this is recommended:** [compounding upside]
   - **Prompt:** `[copy-paste continuation prompt]`
   - **Expected output:** [what gets produced]
   - **Quality bar:** [what makes it worth keeping]
   - **Skip if:** [when expansion would distract]
   - **Suggested skills/workflows:** [exact routes]
```

## Quality Gate

If the output is generic, under-routed, longer than needed, or not tied to a concrete prompt/command/artifact/decision, revise before returning it.
