---
date: 2026-08-02
session: cost-gate pattern fix
name: hook-pattern-false-positives-anchor-to-invocation
problem_class: harness / hooks / regex false positive
domain: harness
status: proven
problem_signature: "a PreToolUse hook blocks read-only commands like head, grep, sed, or git diff because its pattern matches a bare script filename mentioned anywhere in the command text, so plain exploration trips a money gate denial"
tags: [hooks, cost-gate, regex, false-positive, self-test, bash]
---
# Solution Card — Hook regex false positives: anchor to invocation shape, pin with a golden corpus

**Problem shape:** a PreToolUse hook that pattern-matches Bash command text on bare *filenames* (e.g. `fal_video_seedance\.py`) fires on read-only commands that merely mention the file (`head`, `grep`, `sed`, `git diff`) — blocking innocent work with a money-gate denial. Evidenced twice on 2026-08-02 during read-only exploration.

**Solution:**
1. Anchor every pattern to the **invocation shape**, not the filename: launcher + script + arg marker (`python3\s+\S*script\.py\b`, `\bnode\s+\S*generate\.js\b`, `(?:\bbash|\bsh)\s+\S*gen\.sh\b`). A filename inside a grep string no longer matches; every real launch still does.
2. Ship a **golden-corpus self-test in the hook itself** (`--self-test`): a must-NOT-match list seeded with the *actual* wrongly-blocked commands (verbatim class), and a must-match list of every real invocation shape. Run it after ANY pattern edit.
3. When a pattern needs a cost estimate it can't parse (e.g. recipe-driven calls), have the resolver read the recipe/config file deterministically and pass `--est-cost` — default conservative (forces the approval lane) when unreadable.

**Where:** `execution/hooks/cost_gate_hook.py` (patterns + `self_test()`), commit `1afa07aca`.

**Reuse trigger:** any hook or guard that greps command strings for filenames; any false-positive report on a PreToolUse matcher. Related bug fixed same session: optional-key `grep | head | cut` pipelines under `set -euo pipefail` silently kill wrappers when the key is absent — append `|| true` (`skills/fantastic-posters/gen.sh`).
