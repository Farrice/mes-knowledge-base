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
