# Solution Card — Parallel Session Lanes (the golden rule, automated)

**Problem.** Running multiple sessions on this repo corrupted the tree repeatedly
(sibling commit-gate sweep 2026-08-04, handoff temp collision 2026-07-25, forge
race 2026-07-15). The golden rule ("one tool per tree") was enforced by human
vigilance + warn-only alarms — and vigilance fails. Worse, worktrees weren't a
real escape hatch: **all 22 hooks died silently in any fresh worktree** (`.venv`
gitignored → exec failure), so a worktree session ran with no routing, no
ledger, no cost gate, no git guards.

**Solution (shipped, E2E-verified).** One writer per tree; lanes are automatic.

- `.claude/hooks/py.sh` — every hook routes through a shim that self-heals
  `.venv` (symlink to main via git-common-dir) and logs any unresolvable
  degradation to `.agent/hook-failures.log`. Silent hook death is extinct:
  prevent (shim) → prove (parity) → watchdog (beacon surfaced every SessionStart).
- `execution/worktree_lane.py` (stdlib-only, bare python3) — `bootstrap`
  (symlinks .env/.venv/.mcp/.memory/settings.local + shared spend trackers,
  fresh per-lane session state, registry, ends with a **parity check** that
  prints `FULL POWER` or names each deficiency), `merge` (seal → drop per-tree
  state from branch tip → gate [tracked-dirty main / fresh foreign writer /
  merge mutex] → `--no-ff` merge with auto-resolve ONLY for generated files +
  jsonl union → **Law-3 added-file audit** → regen indexes → push → teardown;
  conflict = PARK branch + one line), `list` / `doctor --fix` / `teardown`.
- Auto-lane: `concurrent_session_alarm.py` v2 sees siblings across ALL
  worktrees; a new session starting on a busy main gets the AUTO-LANE
  directive (call EnterWorktree before any write); bootstrap fires via
  SessionStart + PostToolUse(EnterWorktree) hooks.
- Closeout: commit gate is lane-aware (never `add -A` on main with a fresh
  sibling — scopes to own ledger paths); final spine step `lane-merge`
  auto-merges the lane when clean (`END_SESSION_NO_AUTOMERGE=1` declines).
- ~35 high-churn `.agent` state files untracked (they re-dirtied main within
  minutes and false-parked every merge); spend/cost files are symlinked into
  lanes — single-source budgets, no double-spend.
- Doctrine: golden rule text evolved in `directives/constitution/shared-blocks.md`
  (compiled to CLAUDE.md + AGENTS.md); Codex lane protocol in AGENTS.md;
  merge-discipline Law 0 updated.

**Gotchas encoded here (each cost a live debugging loop):**
1. Dir-only gitignore patterns (`.venv/`) do NOT match symlinks — lane seal
   committed bootstrap symlinks until bare-name patterns were added.
2. Never drop a branch file that main still tracks (a gitignore pattern can
   shadow a tracked file; the merge would read the drop as a deletion).
3. The merge gate must count TRACKED changes only — untracked telemetry
   false-parked every merge.
4. The merging session's own lock/transcript must not read as a foreign
   writer (`SESSION_LOCK_TOKEN` + `CLAUDE_SESSION_ID` exclusion; lanes.json
   records lane session ids because transcripts stay in main's projects dir).
5. `git worktree remove` needs `--force` after seal (gitignored symlinks
   remain) — safe there and only there.
6. Telemetry untracking is iterative — the merge gate itself is the detector:
   every park names the next churner.

**Live-fire note.** During the build, a sibling session deleted this session's
test worktrees and registry mid-flight (the exact race class). Nothing was
lost: PARK had pushed every branch to origin first. The safety net was
verified by real fire, not just tests.

**Use it:** open as many sessions as you want. Second+ sessions auto-lane.
`python3 execution/worktree_lane.py list` shows every lane; `doctor --fix`
repairs; parked lanes resolve with `merge --lane <branch>`.
