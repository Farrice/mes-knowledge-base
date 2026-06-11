---
description: Universal excellence gate for anti-slop, taste, depth, originality, proof, and revise-before-final quality control
---

# /excellence-gate - Universal Excellence Gate

This is the shared quality floor for the Living Operator System. It exists to prevent generic AI output, shallow competence, false confidence, hollow frameworks, weak proof, derivative taste, and merely average work from reaching Farrice as final.

## Usage

```bash
/excellence-gate [draft/output/context]
/excellence-gate --domain copy [draft]
/excellence-gate --domain design [draft]
/excellence-gate --factual [draft]
/excellence-gate --client-facing [draft]
```

## Inputs

- Draft, artifact, or planned output.
- Intended audience and use case.
- Producing agent/workflow if known.
- Domain lens: ideation, content, marketing, design, copy, writing, positioning, revenue, delivery, proof, research, data, system.
- Stakes: internal, publishable, client-facing, factual, revenue-critical, system-changing.

## Required Checks

Score 1-10 on each applicable dimension:

| Dimension | What to Check |
|-----------|---------------|
| Specificity | Could this only have been produced for this goal, audience, and context? |
| Taste and judgment | Does it show selection, restraint, emphasis, and a real point of view? |
| Originality | Does it avoid template thinking, category cliches, and mimetic AI structure? |
| Depth when needed | Does it go deep where the work requires depth, without bloating? |
| Craft quality | Is the execution strong in the domain, not just conceptually plausible? |
| Strategic usefulness | Does it change what Farrice should do, ship, say, sell, or build? |
| Proof and grounding | Are claims supported, labeled, or routed for verification? |
| Anti-slop | Does it avoid generic AI language, inflated abstraction, and smooth emptiness? |

## Mandatory Tool Checks

Use relevant local checks when applicable:

```bash
python3 execution/prose_classifier.py check [file]
python3 execution/command_menu.py search "anti slop taste quality judgment"
```

For factual, client-facing, or research outputs, follow `directives/verification-agent-protocol.md` before final delivery.

For expert-standard uncertainty, route to `/ground-truth-agent` or `/ground-truth`.

For high-stakes outputs, route to `/red-team-agent` or `/adversarial-review`.

## Verdicts

- **PASS**: average score 8+, no high-impact weakness, no unverified factual claim presented as fact.
- **REVISE**: average score 6-7 or a fixable weakness. Revise before final.
- **REWORK**: below 6, generic core, weak premise, unsupported claims, or wrong expert stack. Restart with a better route.

## Revise-Before-Final Rule

If verdict is REVISE or REWORK, do not present the weak output as final. Produce the revision or return a clear rework path. The user should not become the quality gate for obvious AI slop.

## Output Schema

```markdown
# Excellence Gate: [Artifact]

## Verdict
PASS / REVISE / REWORK

## Scorecard
| Dimension | Score | Evidence | Required Fix |
|-----------|-------|----------|--------------|

## Revision Applied Before Final
[What changed, or why rework is required]

## Remaining Risk
[Known limitation or verification need]
```
