#!/bin/sh
# py.sh — python resolver for every hook (parallel-session-lanes build, 2026-08-06).
#
# WHY: all hooks ran "$CLAUDE_PROJECT_DIR"/.venv/bin/python3, and .venv is
# gitignored — so in any fresh git worktree every hook died at exec, SILENTLY
# (no routing, no ledger, no cost gate, no git guards). This shim self-heals:
# in a worktree it symlinks the main tree's .venv (venv python resolves its own
# sys.prefix, so the symlink works), and any degradation it cannot heal is
# logged to <main>/.agent/hook-failures.log — never invisible again.
#
# Policy exits from the hook scripts themselves (0 = pass, 2 = intended hard
# block) pass through untouched; only python-RESOLUTION failures are logged.

ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
PY="$ROOT/.venv/bin/python3"

log_failure() {
  COMMON=$(git -C "$ROOT" rev-parse --path-format=absolute --git-common-dir 2>/dev/null)
  MAIN=$(dirname "$COMMON" 2>/dev/null)
  [ -n "$MAIN" ] && [ -d "$MAIN/.agent" ] || MAIN="$ROOT"
  printf '%s | %s | %s\n' "$(date '+%Y-%m-%dT%H:%M:%S')" "$ROOT" "$1" \
    >> "$MAIN/.agent/hook-failures.log" 2>/dev/null
}

if [ ! -x "$PY" ]; then
  COMMON=$(git -C "$ROOT" rev-parse --path-format=absolute --git-common-dir 2>/dev/null)
  MAIN=$(dirname "$COMMON" 2>/dev/null)
  if [ -n "$MAIN" ] && [ "$MAIN" != "$ROOT" ] && [ -x "$MAIN/.venv/bin/python3" ]; then
    ln -sfn "$MAIN/.venv" "$ROOT/.venv" 2>/dev/null
  fi
fi

if [ ! -x "$PY" ]; then
  log_failure "venv unresolvable — falling back to bare python3"
  PY=$(command -v python3)
fi

if [ -z "$PY" ] || [ ! -x "$PY" ]; then
  log_failure "NO PYTHON FOUND — hook did not run: $*"
  exit 0   # never break the session over a dead hook; the beacon is the alarm
fi

exec "$PY" "$@"
