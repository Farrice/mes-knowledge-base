---
description: Generate materially distinct options or variations, compare tradeoffs, and recommend the best next move
---

# /burst - Option Burst

Use this command when one answer is too narrow and the user needs several credible paths, variants, hooks, designs, titles, workflows, offers, or implementation options.

## Usage

```text
/burst
/burst 3
/burst 5 [target]
```

## Pre-Flight

Read `semantic_libraries/antigravity/primitives/daily-operator-command-kit.md`.

## Behavior

1. Parse `N`; default to 3 and cap at 10 unless explicitly requested.
2. Generate `N` materially different options.
3. Name the strategy behind each option.
4. Include tradeoffs, best use case, and failure mode.
5. Recommend one option and give the next action.

Do not create shallow synonyms. If the options are not meaningfully different, revise before presenting.

## Output

```markdown
# Burst

## Options
1. **[Option Name]**
   - Use when:
   - Tradeoff:
   - Failure mode:

## Recommendation
...

## Continue From Here
...
```

