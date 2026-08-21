# Operator Lesson ledger

`LEDGER.jsonl` is the sink for the one-line `Operator Lesson:` that closes every shipped exchange (`directives/steering-loop.md`) — append-only, one JSON record per lesson (`ts · lesson · type · arena · source · session_id · hash`).

Fed by `execution/operator_ledger.py`: `backfill` scans all episodic exchanges, `daily` re-scans the last 48h (wired into `harvest_memory_daily.py`, so it fires nightly without anyone remembering), `stats` prints one summary line. Dedupe is a sha1 of the normalized text — re-running is always a no-op on already-banked lessons.

Query: `python3 execution/memory_facade.py "<intent>"` surfaces them (mirrored into `.memory/sovereign.db` as `tier='semantic', category='lesson'`), or read the JSONL directly — `jq -r 'select(.arena=="harness-craft") | .lesson' knowledge/lessons/LEDGER.jsonl`.

Reversible: every mirrored row carries `metadata.source = "operator-ledger"`, so `DELETE FROM memories WHERE json_extract(metadata,'$.source')='operator-ledger'` undoes the sovereign mirror exactly, leaving the ledger intact.
