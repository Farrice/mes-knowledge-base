---
description: Challenge a decision, plan, artifact, or option with contrarian risks, missing evidence, and better alternatives
---

# /devil - Devil's Advocate Pass

Use this command when a plan, option, artifact, or decision needs honest resistance before commitment.

## Usage

```text
/devil
/devil 5
/devil 7 [target or file path]
```

## Pre-Flight

Read `semantic_libraries/antigravity/primitives/daily-operator-command-kit.md`. If the target is a local file path, read the file before critiquing it.

## Behavior

1. Parse `N`; default to 5 and cap at 10 unless explicitly requested.
2. Identify the target being challenged.
3. Find the strongest objections, not easy objections.
4. Separate evidence gaps from taste disagreements.
5. Offer better alternatives or proof gates.
6. End with a verdict: keep, revise, pause, or reject.

## Output

```markdown
# Devil's Advocate

## Target
...

## Strongest Challenges
1. ...

## Better Alternatives
...

## What Would Change My Mind
...

## Verdict
...
```

