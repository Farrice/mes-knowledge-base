# Hookable Elements Extractor

## Role

Extract the pieces of a draft, source, offer, transcript, or raw thought that deserve to appear above the fold.

## Inputs

1. Draft, source note, transcript excerpt, offer, idea, or content brief.
2. Target reader.
3. Intended payload or belief movement.
4. Platform and output type.

## Workflow

### Step 1: Payload Lock

Summarize the actual payload in one sentence:

```text
This content earns attention because it shows [reader] that [specific claim] using [proof/source/story/mechanism].
```

### Step 2: Extract Hookable Elements

Identify:

- Specific numbers.
- Named entities.
- Before/after shifts.
- Unexpected claims.
- Private reader fears or desires.
- Contradictions.
- Useful mistakes.
- Strong body lines that can move to the top.
- Proof objects.
- Visual or story moments.

### Step 3: Sort By Hook Role

| Element | Role | Why It Pulls | Source Location |
|---|---|---|---|
| Signal | brand, person, news, trend, claim, or number | Recognition | |
| Gap | expectation versus claim | Curiosity | |
| Stakes | consequence or opportunity | Urgency | |
| Proof | example, data, source, result | Trust | |
| Voice | line only this creator would say | Authenticity | |

### Step 4: Select Top 3 Hook Payloads

Each payload must be able to support a real body, not just a clickable line.

## Output Schema

```markdown
## Hookable Elements

### Payload Lock
[one sentence]

### Extracted Elements
| Element | Type | Pull | Evidence |
|---|---|---|---|

### Top Hook Payloads
1. **[payload]**
   - Gap:
   - Best format:
   - Risk:
2. ...
```

## Quality Gate

Reject any hookable element that is catchy but disconnected from the body. The best hooks are mined from substance, not pasted on top of it.
