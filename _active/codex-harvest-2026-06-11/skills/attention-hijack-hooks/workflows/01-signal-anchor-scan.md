# Signal Anchor Scan

## Role

Find attention anchors before drafting. The anchor can be a brand, news item, person, trend, claim, artifact, number, or body insight that already has recognition with the target audience.

## Inputs

1. Topic, draft, source, or content goal.
2. Target audience or ICP.
3. Platform or output type.
4. Optional source list, trend list, brand list, or recent news.
5. Approval for public web research if live external source fetching is needed.

## Workflow

### Step 1: Classify Anchor Type

Choose one or more:

- Brandjack
- Newsjack
- Namejack
- Trendjack
- Claimjack
- Draftjack

### Step 2: Score Anchor Fit

| Check | Score | Notes |
|---|---:|---|
| Recognition with target reader | 1-10 | |
| Timeliness | 1-10 | |
| ICP overlap | 1-10 | |
| Payload fit | 1-10 | |
| Boomerang or discussion potential | 1-10 | |
| Originality room | 1-10 | |
| Evidence availability | 1-10 | |

### Step 3: Extract Point Of View

For each viable anchor, answer:

- What are most people saying about this?
- What does our reader expect?
- What can we credibly claim instead?
- What does this reveal about our domain?
- What should the reader do or believe differently?

### Step 4: Build Opportunity Board

Return 5 to 10 ranked anchors.

## Output Schema

```markdown
## Signal Anchor Board

| Rank | Anchor | Type | Reader Recognition | Payload Fit | Gap | Risk | Next Hook Route |
|---:|---|---|---:|---:|---|---|---|

## Recommended Anchor
- **Anchor**:
- **Why this one**:
- **Curiosity gap**:
- **Evidence needed**:
- **Next step**: `/attention-hijack-hooks generate ...`
```

## Quality Gate

Reject anchors that are recognizable but irrelevant. A famous entity is not useful unless it lets the creator say something the reader cares about.
