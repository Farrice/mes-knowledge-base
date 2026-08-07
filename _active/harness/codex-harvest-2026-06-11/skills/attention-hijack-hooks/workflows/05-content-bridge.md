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

## Handoff Shape

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

The hook is not the deliverable. It is the entrance. The next route must preserve the argument, not merely repeat the opening line.
