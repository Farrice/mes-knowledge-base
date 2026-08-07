# Failure Registry

Prevention rules derived from real failures. **Written automatically** by
`execution/failure_learning.py` off `.agent/health/self-heal.jsonl` — no
`/aar` invocation, no human memory required.

History: this registry lived in a plugin directory and sat empty from
2026-04-04 to 2026-07-27 because its only writer was a slash command
nobody remembered to run. 115 days of failures taught the system nothing.

One rule per failure signature. Repeat occurrences update `Last Triggered`
and `Occurrences` in place — rules are never duplicated or rewritten.

---

<!-- Rules below this line -->

### [ROTTING]: born_intent_drift
- **Added:** 2026-08-04
- **What Happened:** open for 7 days with no decision
- **Root Cause:** 1 anchor(s) changed with NO commit trail since the last bless — that silence is the loss signal: skill:david-perell-writing
- **Prevention Rule:** Decide born_intent_drift or explicitly park it. An escalation nobody answers is indistinguishable from a check nobody runs.
- **Occurrences:** 7
- **Last Triggered:** 2026-08-04
- **Status:** ACTIVE
- **Source:** deterministic, from .agent/health/self-heal.jsonl (execution/failure_learning.py) — no human invocation required
