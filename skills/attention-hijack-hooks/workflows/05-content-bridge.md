# Content Bridge

## Role

Carry the selected hook into full content generation without losing the payload, evidence, or voice.

## Inputs

1. Selected hook and two alternates.
2. Payload Lock.
3. Source/evidence paths.
4. Target output type.
5. Voice and quality gates.

## Routing

| Output Need | Route |
|---|---|
| Farrice end-to-end content package | `/farrice-content-os` |
| LinkedIn-specific Diandra post | `/diandra-content-engine` |
| Full LinkedIn operating plan | `/diandra-linkedin-system` |
| First-50 semantic audit | `/diandra-first-50` |
| High-taste rewrite | `/high-taste-writing-os` |
| Public copy clearance | `/publishable-copy-gate` |
| Conversion or offer copy | `master-copywriter` or `/publishable-copy-gate` |

## Output Schema

The deliverable is a hook-to-content handoff block, not the finished piece — this workflow's contract is the transfer, so nothing that made the hook win (source, gap, rejected alternates) can silently disappear at the boundary.

```markdown
## Attention Hook Handoff
- **Source evidence**:
- **Attention anchor**:
- **Payload lock**:
- **Selected hook**:
- **Format**:
- **Curiosity gap**:
- **Platform fit notes**:
- **Rejected hooks**:
- **Next route**:
- **Open risk**:
```

## Quality Gate

The hook is not the deliverable. It is the entrance. The next route must preserve the argument, not merely repeat the opening line. Reject a handoff if any of these hold:

- **Selected hook** is filled in but **Curiosity gap** is blank or restates the hook instead of naming what tension it opens.
- **Next route** points to a downstream workflow whose deliverable the hook cannot actually pay off (for example, routing a Single-Line Bomb hook meant for a hot take into a `/diandra-first-50` audit built for full-post semantic density).
- **Rejected hooks** is empty — per genius.md Pattern 6 (Judgment Over Automation), a handoff with no rejected alternates means no judgment was exercised, only generation.
