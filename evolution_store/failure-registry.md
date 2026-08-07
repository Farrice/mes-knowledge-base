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
- **Last Triggered:** 2026-08-06
- **Status:** ACTIVE
- **Source:** deterministic, from .agent/health/self-heal.jsonl (execution/failure_learning.py) — no human invocation required

### [RECURRING]: born_intent_drift
- **Added:** 2026-08-05
- **What Happened:** repaired 6 times over 8 days — the repair holds but the cause regenerates
- **Root Cause:** upstream producer re-dirties this state after each repair
- **Prevention Rule:** Treat recurring born_intent_drift as a symptom. Find what re-dirties it between runs and fix THAT; a healer firing every day is a workaround, not a solution.
- **Occurrences:** 11
- **Last Triggered:** 2026-08-06
- **Status:** ACTIVE
- **Source:** deterministic, from .agent/health/self-heal.jsonl (execution/failure_learning.py) — no human invocation required

### [ROTTING]: stale_registries
- **Added:** 2026-08-06
- **What Happened:** open for 9 days with no decision
- **Root Cause:** detector raised TimeoutExpired
- **Prevention Rule:** Decide stale_registries or explicitly park it. An escalation nobody answers is indistinguishable from a check nobody runs.
- **Occurrences:** 9
- **Last Triggered:** 2026-08-06
- **Status:** ACTIVE
- **Source:** deterministic, from .agent/health/self-heal.jsonl (execution/failure_learning.py) — no human invocation required
### CONTROL-PROMOTION OVERSCOPE: Optional depth heuristic became artifact-wide authorization
- **What Happened:** Reality Before Rhetoric moved from optional source recovery into keyword- and route-triggered activation, mandatory content-card fields, artifact tiers, and whole-artifact drafting authority, constraining safe supported work.
- **Root Cause:** Structural validation and benchmark success were treated as permission for enforcement before safe-task false-block rates, question burden, and creative-range retention had been tested.
- **Prevention Rule:** Every new quality, depth, or source heuristic begins in OPEN or SHADOW mode. It may reach enforcement only when it maps to a hard truth, proof, privacy, or permission veto; has three independent production receipts and a blind comparison; blocks zero frozen safe controls; preserves creative range; names the smallest affected unit and nearest safe continuation; and receives Farrice's explicit approval. No mandatory schema may exist solely to prove the heuristic ran.
- **Last Triggered:** 2026-08-04
- **Occurrences:** 1
### SUPERSEDED-AUTHORITY DRIFT: Historical implementation artifacts contradicted restored runtime
- **What Happened:** After active RBR wiring was removed, four earlier mission documents still described mandatory activation, source packets, artifact tiers, and whole-artifact holds as if they remained current.
- **Root Cause:** Restoration review initially covered executable and canonical contract surfaces but did not include a semantic deprecation sweep over authoritative-looking historical artifacts.
- **Prevention Rule:** Any rollback, demotion, or contract replacement must search for prior documents asserting the superseded behavior, mark them clearly as historical or superseded in the same patch, publish the current authority order in the implementation receipt, and fail validation when an unlabeled document contradicts active behavior.
- **Last Triggered:** 2026-08-04
- **Occurrences:** 1
### [ROTTING]: born_intent_drift
- **Root Cause:** 1 anchor(s) changed with NO commit trail since the last bless — that silence is the loss signal: skill:david-perell-writing
- **Prevention Rule:** Decide born_intent_drift or explicitly park it. An escalation nobody answers is indistinguishable from a check nobody runs.
- **Occurrences:** 12
- **Root Cause:** 13 anchor(s) changed with NO commit trail since the last bless — that silence is the loss signal: prompt:sean-dollwet-kdp-publishing/book-do
