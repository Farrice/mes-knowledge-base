# Quality Gates & Anti-Patterns

> Enforce during Step 5 (PRODUCE). These are non-negotiable.

## Anti-Patterns (Automatic Failure)

- ❌ **Entity classification** — Deploy it, don't describe it
- ❌ **Phantom research** — Don't cite what you didn't read (USE TOOLS TO ACTUALLY READ IT)
- ❌ **Template slop** — No generic filler
- ❌ **AI slop vocabulary** — Banned: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy. Rewrite if caught.

## Quality Checks

- **Copy Calibration:** ICP on phone, 2 seconds — do they know (a) it's for them, (b) what you do, (c) what's in it for them?
- **AI-Prose Cap:** AI-shaped prose cannot score above 6. If output could've been produced WITHOUT the skill files, Expert Standard ≤ 4.
- **Show > Tell:** Describing = TELL (dead). Demonstrating through a moment = SHOW (alive).

## Finalize Gate (Step 6)

Score on 3 dimensions (1-10 each):
- **Intent Alignment**: Does it match what the user actually asked for?
- **Expert Standard**: Would the real expert recognize this as quality work?
- **Adversarial Resilience**: Would it survive critical scrutiny?

If composite < 7 or any dimension < 6: retry weakest section, re-finalize.
Step 6 fires only when expert output was produced in Step 5.
Quick answers, system commands, and conversations do NOT require finalize.
