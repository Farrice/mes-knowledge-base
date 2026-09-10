# Cross-Domain Patterns — Nate B Jones Manager Loop

Where the manager loop meets what already exists in this harness, and what each side lends.

| Nate's move | Antigravity counterpart | What we keep | What we changed |
|---|---|---|---|
| Recipe card | `docs/solutions/` cards (`/extract-approach`) | Auto-resurfacing, the "never re-solve a carded problem" rule | Solution cards map a PROBLEM; recipe cards map a JOB. Recipes live in `recipes/`, no date prefix, ratcheted in place |
| Manager interview | `/go` Stage 0 questions gate; INTENT BRIEF (fresh-pen protocol) | One confirm beat before spend | For job-shaped asks the instantiated card IS the brief — the hook suppresses the second brief |
| Lanes + dependencies | `mission_control.py` activation queue; wargame Moves; Ray's fan-out coordinator | The queue as state; expected-vs-observed ledger | Added `after` deps and a runnable rule (`job_board.py next`) |
| "Keep going on the unblocked" | Worker envelope; fleet doctrine | Quarantined writes, provenance-or-UNCONFIRMED | Made the turn-end rule physical: MAY END or the turn continues |
| Decision packets | `/park` reasons; pending-decisions hook; AskUserQuestion checkpoints | One decision per ask, tappable | Packets batch; irreversibility and default named every time |
| Four closeout questions | `/go` Stage 3 verdict ask; chain_runner finalize | The templated last-line verdict ask | Closeout answers Nate's four with receipts before the verdict |
| "Copy it into any manager agent" | `raw_intent_run_packet.py` → `portable.md` | Paste-anywhere packets | `job_board.py handoff --to codex\|claude\|chat` carries lanes + packets + answers, so either harness runs alone or together |
| Chief-of-staff agent | `/cos`, Maestro conductor ladder | Conductor conducts, executors execute | Fable manages and writes; Sonnet seats are read-only lanes; Astra is one seat that runs lanes in order |
| Agent supervision | Verify-fleet, Blind Bar, verification spine | Sabotage both directions before calling a check verified | The Stop-hook observer logs the hand-back instead of blocking it (compass doctrine) |

Read across the table: Nate supplies the relationship and the form factor; the harness already had the machinery. The build is the joint.
