---
name: codex-hooks-config-present-not-firing
problem_signature: "harness looks fully wired (hooks trusted+enabled, verifiers green) but is silently broken at runtime — stale CLI hard-fails the model, a hook fails anonymously every session, config state was treated as proof"
domain: system
tags: [codex, hooks, parity, live-fire, control-plane]
date: 2026-07-13
status: active
session: "3fa9a146-580b-4932-9020-ad931ef598c5"
---

# Config presence is not proof — live-fire verification for cross-platform hooks

**Date:** 2026-07-13 · **Domain:** harness / control plane / platform parity · **Thread:** codex-parity

## Problem

The Codex harness looked fully wired — hooks trusted + `enabled = true` in `~/.codex/config.toml`, `verify_google_operator_core.py` 10/10 green, platform constitutions in sync — yet was silently broken at runtime: the 0.133.0 CLI hard-failed against the configured model (`gpt-5.6-sol` requires a newer CLI, so EVERY real session died at the first model call), and one SessionStart hook failed on every launch with no visible culprit. Config state and static verifiers were treated as proof of runtime behavior.

## Root Cause

Three stacked causes, none visible from config inspection: (1) stale CLI version vs current model requirements — a total outage that throws no local error until a session actually runs; (2) Codex's hook-output validation is stricter than Claude Code's — `hookSpecificOutput` REQUIRES `"hookEventName"`, so the JCC SessionStart hook "failed" every session despite exiting 0 with valid JSON; (3) the constitution (AGENTS.md) still said "No hooks on Codex," written before the 2026-07-11 hooks.json wiring, so no one expected runtime behavior to check.

## Approach That Worked

1. **Live-fire, don't inspect.** One controlled probe: `codex exec --skip-git-repo-check --sandbox read-only "Run exactly one shell command: echo probe. Then stop."` — the CLI prints `hook: <Event>` / `Completed|Failed` per hook. Config review answers "registered?"; only the probe answers "fires?". (Claude-side equivalent: read a SKILL.md, watch for the PostToolUse injection.)
2. **Upgrade the CLI first when the model call itself fails** (`npm install -g @openai/codex@latest`, 0.133.0 → 0.144.3), then re-probe — the firing map is only meaningful on a CLI that can run its model.
3. **Bisect anonymous hook failures via `enabled = false`** on individual `[hooks.state]` entries in `~/.codex/config.toml` (flip → probe → restore; back up config.toml first). Hook failures carry no name in Codex output or session transcripts, so bisection is the only attribution tool.
4. **Fix the strict-contract failure at the script**, not hooks.json: added `"hookEventName": "SessionStart"` to `session-start.sh` in all three plugin copies (Codex cache, CC cache, CC installed). Editing hooks.json would invalidate trust hashes and silently disable everything until Desktop re-trust.
5. **Rewrite the constitution to the verified firing map**: SessionStart, UserPromptSubmit, PreToolUse/PostToolUse on shell (Codex maps shell → `Bash` matcher), Stop. Native file reads fire NO tool hooks — cover Read/Skill-matcher behavior with constitution clauses instead.

## Dead Ends

- Grepping Codex session transcripts and `RUST_LOG=debug/trace` output for the failing hook's name — Codex does not record which hook failed anywhere.
- Removing the stale `hooks-codex.json` trust entry (a ghost from superpowers pre-6.1.0) — harmless cleanup, but the failure persisted; the ghost was not the cause.
- Trusting pre-June-2026 research about platform capabilities — Gemini CLI was EOL'd 2026-06-18; sources predating a shutdown still describe the platform as alive. Verify platform liveness before writing port specs.

## Verification

Re-probe after each fix: `hook: SessionStart Completed` ×2 (was 1 Failed), full chain `SessionStart / UserPromptSubmit ×3 / PreToolUse ×3 / PostToolUse / Stop` all Completed on 0.144.3; `verify_raw_intent_run_packet.py` and `verify_control_intent.py` (27/27) green; `platform_compiler.py check` in sync after re-bless; golden-brief A/B (`_active/harness/codex-parity-2026-07-13/proof/JUDGMENT.md`) confirms gates hold on both platforms.

## Weaker-Model Trap

A weaker session reads `enabled = true` + green verifiers and reports "hooks are wired and working" without ever running a probe — exactly the report that hid this outage. It also patches hooks.json directly (killing all hooks via trust-hash invalidation) or declares the first plausible suspect (the ghost entry) the root cause without a confirming re-probe. Rule: no "it works" claim about hooks/automation without a live-fire receipt in the same session, and never edit hooks.json when the target script can carry the fix.

## Pointers

- Probe pattern + firing map: `CODEX.md` § "Deterministic Hook Layer" · `AGENTS.md` § "Hooks on Codex"
- Hook runner + targets: `.codex/hooks.json`, `.codex/tools/codex_hook_runner.py`
- Fixed script (3 copies): `~/.codex/plugins/cache/jcc-local/jarvis-command-center/1.0.3/hooks/session-start.sh`, `~/.claude/plugins/installed/...`, `~/.claude/plugins/cache/...`
- Config backups: `~/.codex/config.toml.bak-pre-parity-2026-07-13`
- A/B proof: `_active/harness/codex-parity-2026-07-13/proof/` (take-a, take-b, JUDGMENT.md)
- Sibling card: `docs/solutions/2026-07-07-parallel-builders-stale-contracts.md` (stale-state family)
