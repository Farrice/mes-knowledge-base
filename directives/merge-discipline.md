# Merge Discipline — Concurrent Work Without Silent Loss

**Status: BINDING (Wave 0, Frontier Elevation Program, 2026-07-17).**
Codifies `docs/solutions/2026-07-15-concurrent-session-race-accept-repair-dedupe.md` and
`docs/solutions/2026-07-15-ours-merge-absorbs-silently-drop-branch-content.md` into the
standing SOP those cards proved. The lock is the brake; this discipline is the seatbelt.

## Law 0 — Main is integration-only; every writer gets a lane (updated 2026-08-30)

- **Lanes are the authoring mechanism** (`execution/worktree_lane.py`): every ordinary
  Claude Code or Codex session takes a git worktree lane before its first write, including
  the first session. Read-only inspection may remain on main. Claude sessions get the
  AUTO-LANE directive at SessionStart; Codex follows the lane protocol in AGENTS.md. A
  lane is **single-writer by construction** — `session_lock.py claim/check` auto-clear
  there. Main stays clean and available for audited integration.
- Main is reserved for `worktree_lane.py merge`, lane reconciliation, and existing
  lock-aware scheduled maintenance. Ordinary build/forge/fleet/content sessions do not
  claim main and write there; they take a lane.
- A fresh foreign main lock means integration or scheduled maintenance is active. Lanes
  may continue independently, but merge-back waits until the lock clears.
- Opt-in locks don't fire — claiming is part of the kickoff ritual in `/go`,
  `/extract-forge`, and `/swarm` (wired 2026-07-17).
- **Lane merge-back is mechanized**: `worktree_lane.py merge` seals, gates (dirty main /
  fresh writer / merge mutex), merges `--no-ff`, runs the Law-3 added-file audit,
  regenerates generated indexes (never hand-merges them), pushes, tears down. Conflicts
  PARK the branch + surface one line. Parked-lane SLA: resolve within 7 days
  (`doctor` nudges; the divergence alarm lists parked lanes without alarming).

## Law 1 — Fleet writes are quarantined (hook-enforced since 2026-07-17)

**Physical enforcement**: at fleet dispatch the conductor writes
`.agent/fleet-active.json` (`{"mission","claimed":<epoch>,"protected":["skills/"],
"ttl_min":90}`); `execution/hooks/fleet_write_guard.py` (PreToolUse Edit|Write) then
hard-blocks direct edits to protected paths for every session/subagent on the tree.
Delete the sentinel at fleet close; stale sentinels (>ttl) never block. Conductor
merges via shell `cp` are unaffected by design.

Dispatched workers (subagents, fleet executors, parallel builders) write **only** to
`.tmp/<session>/<worker>/` — never to canonical paths. The conductor merges serially,
and a deterministic gate (`renaissance_audit.py` 0-fail, heartbeat 6/6, or the relevant
domain audit) arbitrates every merge. A worker's SUMMARY is never trusted; the gate runs
on the actual file (file-not-summary).

## Law 2 — When a race happens anyway: Accept → Repair → Dedupe → Fidelity-check

1. **Accept** — never revert a live writer's files mid-race. Reverting fights a live
   session, and foreign work often carries real improvements (the 07-15 race's foreign
   prompt won its dedupe on merit).
2. **Repair to spec** — run the domain audit (`renaissance_audit.py`) after ANY
   unexplained file change; restore missing required sections; fix header levels the
   audit keys on (`## `).
3. **Resolve dangling pointers** — diff wrappers vs. targets; write the missing target if
   the deliverable is real, rather than deleting the wrapper.
4. **Dedupe per deliverable** — one prompt/asset per deliverable; keep the stronger
   candidate on the gate's verdict, rewire pointers, re-run the audit to 0-fail.
5. **Fidelity-check foreign inventions** — merged content can smuggle in numbers the
   corpus never stated; label them "operator heuristic," never expert claim.

Diagnostic tell for a live race: context-aware changes you didn't write + fresh sibling
transcripts in `~/.claude/projects/<project>/` with same-minute mtimes. A daemon/linter
does not author 300-line prompts.

## Law 3 — Divergence is settled by TREES, not ancestry

`git rev-list --count` measures SHA reachability, not content — after ANY merge
(including `-s ours`) it reads 0 whether or not the content arrived. Therefore:

- **Never use `git merge -s ours` to clear a divergence alarm** until a tree-level
  content audit proves main holds every file and ledger line the branch created.
  The audit: files the branch itself ADDED
  (`git diff --diff-filter=A --name-only $(git merge-base main ref) ref`) must exist on
  current main (`git cat-file -e main:path`); append-only ledgers get a line-level pass
  (`comm -23 <(git show ref:file | sort) <(sort file)`).
- Restore whole files with `git show <ref>:<path> > <path>`; merge ledger lines by
  sort-union and validate every line as JSON before committing.
- Prune branches only after recovery is committed AND pushed.
- Same-day filename collisions from parallel runs get suffixed (`-cloud.md`), never
  overwritten — both are real content.
- The empty-absorb detector in `divergence_alarm_hook.py` is the deterministic backstop;
  a silent alarm is not evidence of a clean merge. **The silence IS the failure mode.**

## Weaker-model trap (verbatim from the solution card)

Sees the divergence alarm, runs `git merge -s ours` because a memory card says "diverged
branches = recover files + merge -s ours" — executing the second half of the recipe
without the first, then treating the now-silent alarm as success. Never.
