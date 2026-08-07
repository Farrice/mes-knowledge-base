# Four-Format Hook Generator

## Role

Generate hook candidates in the four core Diandra formats plus a guarded Hybrid option.

## Inputs

1. Payload Lock from Workflow 02.
2. Hookable elements.
3. Target reader.
4. Platform.
5. Voice constraints or banned phrases.

## Workflow

### Step 1: Choose Default Format

Use this decision table:

| Condition | Default Format |
|---|---|
| Context is needed before the gap lands | Dense |
| A sharp first line needs one setup line | Punchy plus Context |
| One sentence is unusually strong | Single-Line Bomb |
| A series, contrast, before/after, regrets, or escalation creates rhythm | Stacked |
| The four core formats are too rigid for the payload | Hybrid |

### Step 2: Generate Candidate Set

Produce:

- 3 Dense hooks.
- 4 Punchy plus Context hooks.
- 2 Single-Line Bomb hooks.
- 3 Stacked hooks.
- 1 Hybrid hook only if it beats the best core-format option.

### Step 3: Score

| Hook | Format | Signal | Gap | Specificity | Platform Fit | Voice Fit | Risk | Score |
|---|---|---:|---:|---:|---:|---:|---|---:|

### Step 4: Select Winner

Pick one winner and two alternates. Explain why rejected hooks lost.

## Output Schema

```markdown
## Hook Room

### Winner
[selected hook]

### Why This Wins
- Signal:
- Gap:
- Format:
- Platform fit:
- Voice:

### Candidate Table
| Hook | Format | Score | Keep/Cut Reason |
|---|---|---:|---|

### Next Step
Run `/attention-hijack-hooks audit` or `python3 execution/attention_hijack_hooks.py`.
```

## Quality Gate

Do not ship a hook dump. Ship a decision. The operator should know what to use now and what not to use.
