---
description: Ask numbered clarifying questions with lettered options and recommended defaults before meaningful execution
---

# /align - Intent Alignment Questions

Use this command when the next action depends on user intent, tradeoffs, constraints, audience, quality bar, or scope.

## Usage

```text
/align
/align 5
/align 3 [goal]
```

## Pre-Flight

Read:

1. `semantic_libraries/antigravity/primitives/daily-operator-command-kit.md`
2. `semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md`

## Behavior

1. Parse `N`; default to 5 and cap at 10 unless the user explicitly asks for more.
2. Build the Co-Creative Launchpad Packet first: predicted need, center, edges, what good looks like, missing inputs, route bias, and pause/run decision.
3. Ask only questions whose answers change route, artifact, scope, risk, taste, or proof.
4. Give 2-4 lettered options for each question.
5. Mark one option as recommended when there is a clear default.
6. Explain why each question changes execution.
7. Stop after the questions. Do not execute until the user answers or explicitly says to use defaults.

## Output

```markdown
# Align

1. **[Question]**
   - A. [Option] (Recommended) - [impact]
   - B. [Option] - [impact]
   - Why this matters: ...
```
