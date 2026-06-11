---
description: Turn design or visual feedback into controlled adjustment parameters, preview guidance, and a patch plan
---

# /tweak - Visual Adjustment Pass

Use this command when a visual, webpage, slide, card, design prompt, or UI needs controlled adjustment rather than open-ended redesign.

## Usage

```text
/tweak [target]
/tweak [file path]
```

## Pre-Flight

Read:

1. `semantic_libraries/antigravity/primitives/daily-operator-command-kit.md`
2. The target file if a local path is provided
3. Relevant design/workflow files only when the target is visual or web-shaped

## Behavior

1. Confirm the visual target.
2. If the target is not visual or web-shaped, redirect to `/align`, `/burst`, or `/devil`.
3. Identify 4-8 adjustable parameters such as hierarchy, density, contrast, spacing, type scale, color temperature, emphasis, motion, or crop.
4. Provide recommended settings and a patch plan.
5. Create an interactive preview only when the target is already visual/web-shaped or the user explicitly asks for one.
6. If code or design files are changed, verify with the smallest relevant visual check.

## Output

```markdown
# Tweak

## Adjustable Parameters
1. ...

## Recommended Settings
...

## Patch Plan
...

## Verification
...
```

