# Ambient Interface And Event Handling

## Event Ledger

Ambient work surfaces create events, not just messages. The employee must know what each event means before it turns it into context.

| Event | Required Interpretation |
|---|---|
| New message | New input or task candidate. |
| Thread reply | Continue scoped context unless thread drift is detected. |
| New DM after a thread | Check whether it continues prior context or starts a new task. |
| Edit | Re-evaluate downstream work that depended on the prior text. |
| Delete | Stop, cancel, or ask before continuing if the deleted message was task-critical. |
| Reaction | Treat as weak signal unless the workflow defines reaction semantics. |
| Mention | Consider whether the employee is being summoned or only referenced. |
| File change | Determine whether it is source update, output artifact, or irrelevant noise. |
| Recurring trigger | Run only inside the scheduled scope and current permission state. |

## Linearization Rule

Before calling the model, convert ambient events into a compact event sequence:

```text
surface -> event type -> actor -> scope -> referenced context -> action implication -> risk
```

## Progress Rule

Long-running tasks need progress surfaces:

- Accepted the task.
- Current phase.
- Waiting on approval or missing input.
- Finished output.
- What changed since the last status.
