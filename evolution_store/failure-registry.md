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

### [ROTTING]: stale_slash_commands
- **Added:** 2026-08-04
- **What Happened:** open for 7 days with no decision
- **Root Cause:** 9 workflows missing from SLASH_COMMANDS.md, and the generator cannot fix it: `generate_slash_commands.py --check` reports 2,398 to append bu
- **Prevention Rule:** Decide stale_slash_commands or explicitly park it. An escalation nobody answers is indistinguishable from a check nobody runs.
- **Occurrences:** 9
- **Last Triggered:** 2026-08-05
- **Status:** ACTIVE
- **Source:** deterministic, from .agent/health/self-heal.jsonl (execution/failure_learning.py) — no human invocation required

### [RECURRING]: born_intent_drift
- **Added:** 2026-08-05
- **What Happened:** repaired 6 times over 8 days — the repair holds but the cause regenerates
- **Root Cause:** upstream producer re-dirties this state after each repair
- **Prevention Rule:** Treat recurring born_intent_drift as a symptom. Find what re-dirties it between runs and fix THAT; a healer firing every day is a workaround, not a solution.
- **Occurrences:** 7
- **Last Triggered:** 2026-08-05
- **Status:** ACTIVE
- **Source:** deterministic, from .agent/health/self-heal.jsonl (execution/failure_learning.py) — no human invocation required
