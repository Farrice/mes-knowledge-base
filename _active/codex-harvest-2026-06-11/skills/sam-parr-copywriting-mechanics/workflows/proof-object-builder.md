# Proof Object Builder

## Use When

The copy makes claims without evidence close enough to create belief.

## Inputs

- Draft.
- Claims being made.
- Available proof assets.
- Audience skepticism.
- Desired action.

## Steps

1. Mark every claim asking for belief.
2. Classify each claim as proved, underproved, or unsupported.
3. Choose the strongest proof object:
   - quote,
   - before/after,
   - metric,
   - artifact,
   - test,
   - comparison,
   - visible result.
4. Move the strongest proof near the most important claim.
5. Rewrite the claim around the proof.
6. Name remaining proof gaps.

## Output

```markdown
## Proof Object Builder
- **Claims marked:**
- **Strongest proof object:**
- **Unsupported claims removed or softened:**
- **Rewritten proof-first section:**
- **Behavior delta:**
- **Remaining proof gap:**
```

## Quality Gate

Fail if the proof object is invented, too vague, or not adjacent to the claim it supports.

