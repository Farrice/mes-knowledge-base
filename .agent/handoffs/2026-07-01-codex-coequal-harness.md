---
thread: codex-coequal-harness
status: ready
resume_hint: Farrice: codex mcp login recall + Desktop hook confirm + fresh Codex /system-audit smoke test
unfinished: 3 interactive steps (recall OAuth, Desktop toggle, smoke test); optional: lock-hook wiring, --platform field, drift gate
branch: main
pin: true
---

# Handoff: Codex Co-Equal Harness — Repaired, Verified, Pushed

**Date:** 2026-07-01 · **Repo:** `/Users/farricecain/Google Antigravity` · **Branch:** `main` @ `dc8d3882` (synced with `origin/main`, tree clean)

## Where things stand (TL;DR)

The full Codex co-equal harness repair is **done, verified 10/10 green, committed, and pushed to origin**. Claude Code and Codex now run as peer drivers on the one canonical repo. What remains is (a) three interactive steps only Farrice can do, and (b) optional hardening items that were deliberately deferred.

## What was accomplished (this session + its predecessors, all on `main`)

1. **Root cause found:** the "fix one thing, another breaks" failure was TWO concurrent writers — a live Codex session mutating the tree during repairs. Now guarded by the ⚠️ GOLDEN RULE block at the top of both `CLAUDE.md` and `AGENTS.md` (one tool per working tree at a time; hand off via clean `git status`/commit).
2. **Control plane restored:** 125 execution scripts + 27 primitives + `CODEX.md` + operator-autopilot agent promoted from `_active/codex-harvest-2026-06-11/` (the 2026-06-11 harvest had only half-installed them).
3. **Peer-constitution model locked:** `CLAUDE.md` = canon (the fork-era "LEGACY REFERENCE" demotion was reverted; never re-apply it). `verify_codex_authority.py` adapted accordingly.
4. **Routing fixed twice:** (i) ≥90-confidence control classifications beat literal `source-command-X` token matches; (ii) this session — the claude.ai-export-harvest's uncommitted edits let routing_governor suppress a 96-confidence classification (`/self-evolve` misroute); reconciled in `execution/workflow_router.py` ~line 645 (governor wins <90 confidence, classifier wins ≥90). Commit `98846e92`.
5. **Codex parity:** all 6 hooks trusted+enabled in `~/.codex/config.toml` (incl. dangerous-git), Perplexity key wired, 6 stale f859 worktree entries removed, f859 worktree retired, 20 broken `~/.codex/skills` ports quarantined to `~/.codex/_retired-skills-2026-06-30/` (4 shims preserved).
6. **4 fork-era verifiers adapted** to the canonical single-tree repo (never recreate the 32-hot/700-cold sprawl or `/Users/farricecain/Codex Antigravity/...` fork paths to satisfy a verifier).
7. **Docs + guards:** operator guide at `docs/OPERATING-CODEX-AND-CLAUDE.md`; warn-only concurrent-tool guard built+tested at `execution/hooks/active_tool_lock.py` (NOT wired — needs Farrice's authorization to touch agent configs).
8. **Housekeeping:** platform hashes re-blessed (drift `[]`, 2026-07-01); plain `git push` unblocked in `.claude/hooks/block-dangerous-git.sh` (ports ratified `c482616f`; force-push/reset --hard/clean -fd still blocked); remote housekeeping-audit commits merged (union log resolution).

## Verification state (all as of push)

10/10 green: `verify_google_operator_core`, `verify_codex_authority`, `verify_autopilot_runtime_preflight`, `verify_skill_system_contract`, `verify_subagent_approval_language`, `verify_operator_lesson`, `codex_harness_check`, `codex_live_surface_audit --strict`, `operator_core_status --json --strict`, `platform_compiler lint` (`{"failures": []}`).

## NEXT FOCUS — Farrice's 3 interactive steps (only he can do these)

1. **`codex mcp login recall`** — browser OAuth at getrecall.ai. Verify: `codex mcp list --json` → recall `auth_status: o_auth`. (Note: `codex doctor` shows green even when recall is unlogged — don't trust it.) This is the biggest live gap: until done, Codex has no 3,000-card grounding.
2. **Codex Desktop → Hooks** — confirm dangerous-git (and all 6) show trusted + ON for this repo's `.codex/hooks.json`. Config says enabled; the UI is ground truth.
3. **Fresh Codex session smoke test** — open Codex in the repo, run `/system-audit`, expect green canonical baseline. A ready-made checklist prompt for this was given to Farrice (search this session's transcript or just re-derive: run the 6 canonical verifiers + count surfaces + `codex mcp list --json`).

## Optional hardening (deferred, pre-approved shapes)

- **Active-tool lock wiring:** hook exists + tested; wiring instructions are in guide §10 step 4 (needs Farrice's OK — auto-mode classifier blocks self-modification of `.claude/settings.json`; Codex side needs Desktop re-trust after `hooks.json` hash change).
- **`--platform` field** on `execution/chain_runner.py finalize` (structured platform tag; currently soft convention `| platform: codex` in `--notes`).
- **CLAUDE↔AGENTS drift gate:** extend `platform_compiler.py` to semantically diff the two constitutions (the memory_facade drift went unnoticed; this prevents the next one).
- **2 pre-existing red verifiers** (out of scope by design): `verify_global_autopilot_source_truth`, `verify_operator_core_ai_employee_os` — red at baseline, greening requires recreating retired structure.

## Landmines / rules for the next agent

- **GOLDEN RULE:** confirm no Codex session is live before editing (check file mtimes advancing / `.cpython-314.pyc` appearing in `__pycache__` = Codex's Python 3.14 importing modules).
- **Never** re-demote CLAUDE.md, recreate fork paths, or restore the cold-skill quarantine to green a verifier.
- Session-state churn (`.agent/sessions/`, `observe-log.jsonl`) dirties the tree during work — commit it with the repo's `chore(state):` convention.
- zsh word-splitting: unquoted `$var` loops don't split — use `while read` loops in Bash tool calls.
- Backups if reverts needed: `~/.codex/config.toml.bak-pre-coequal-2026-06-30`, `~/.codex/_retired-skills-2026-06-30/`.

## Key artifacts (by reference)

- Operator guide: `docs/OPERATING-CODEX-AND-CLAUDE.md`
- Memory: `~/.claude/projects/-Users-farricecain-Google-Antigravity/memory/project_codex-coequal-harness.md`
- Key commits: `765e9db1` (control-plane restore), `78b911e0` (Phase 5 parity), `98846e92` (routing precedence fix), `95f6c537` (push unblock), `dc8d3882` (merge + push tip)
- Plan file: `~/.claude/plans/i-ve-been-trying-to-sprightly-stardust.md`

## Suggested skills

- `/system-audit` — if anything control-plane feels off, this is the owner route (now green end-to-end)
- `/resume` — surfaces this thread by name (pinned as `codex-coequal-harness`)
- `/health-check` — lighter status read than a full audit
- `superpowers:verification-before-completion` — before declaring any follow-up repair done
- `/repeatability-spine` — if output quality regresses vs. this session's standard
