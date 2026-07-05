---
thread: claude-video-watch-update
status: ready
resume_hint: Restart to load watch 0.2.0; confirm Codex fully closed before working this tree
unfinished: Verify /watch=0.2.0 in fresh session; ~15 pre-existing modified files + Codex WIP left uncommitted
branch: main
pin: true
---

# Handoff — claude-video `/watch` skill: v0.1.2 → v0.2.0 update

**Date:** 2026-07-04 · **Driver:** Claude Code (Opus 4.8) · **Status:** ✅ Complete & pushed
**Repo:** `/Users/farricecain/Google Antigravity` · **Branch:** `main` @ `3b645b95` (== origin/main)

## What this session did
Replaced/updated the installed `watch@claude-video` plugin (the `/watch` skill) everywhere it lives, from **v0.1.2 (flat layout)** to **v0.2.0 (HEAD `83da59f`, nested `skills/watch/scripts/` layout)**, then pinned a safe default and committed the workspace-side fix.

Trigger: user gave the repo `github.com/bradautomates/claude-video` + demo video `https://www.youtube.com/watch?v=9psY4d-JjLY` and asked to update the already-installed skill "across all cases within our harness and system and workspace."

## Completed (all verified)
- **Claude Code plugin → v0.2.0.** `claude plugin marketplace update claude-video` (clone pulled to `83da59f`) + `claude plugin update watch@claude-video`. `installed_plugins.json` now points at `~/.claude/plugins/cache/claude-video/watch/0.2.0`, SHA `83da59fa78c3`. Cache validated (full `skills/watch/scripts/`, `config.py`, `hooks/`, SKILL.md byte-identical to HEAD).
- **Parity confirmed:** Claude Code **and** Codex both at v0.2.0 / `83da59f`.
- **Workspace wrapper fix — committed `3b645b95`:**
  - `execution/fetch-video-context.py` — `find_watch_script()` now resolves **both** the v0.2.0 nested (`skills/watch/scripts/watch.py`) and v0.1.x flat layouts, across Claude Code + Codex caches, newest-mtime wins. (Without this the 0.2.0 restructure silently breaks video-vision for all 23 downstream extraction/content workflows.)
  - `directives/video-vision-protocol.md` — plugin contract refreshed to v0.2.0 entry point + new `--detail` / `--timestamps` / `--no-dedup` args.
- **Default detail pinned.** `~/.config/watch/.env`: `WATCH_DETAIL=balanced` (100-frame cap, controlled tokens) + `SETUP_COMPLETE=true`, **keyless by user's choice** (no Groq/OpenAI key — native-captions only, no more setup nag). `setup.py --check` exits 0 silently.
- **Acceptance test passed** on the demo video: 17 frames + 249-seg caption transcript in 14.5s, $0; report showed v0.2.0-only behavior (`1 near-duplicate dropped`). Test artifact `extractions/brad-test/` was cleaned up (regenerable).

## ⚠️ Next-session focus / open items
1. **Restart to load 0.2.0.** This session still holds v0.1.2's `/watch` in memory. A fresh Claude Code session picks up v0.2.0. *Verify:* `Read ~/.claude/plugins/cache/claude-video/watch/0.2.0/skills/watch/SKILL.md` resolves, and `claude plugin details watch@claude-video` shows 0.2.0. (The deterministic wrapper `fetch-video-context.py` already uses 0.2.0 regardless of session state.)
2. **GOLDEN RULE — concurrent Codex.** A Codex session was actively editing this same tree during this session (it authored the `fetch-video-context.py` fix at 07:47 and committed to `main` — the push fast-forwarded through its commits). **Confirm Codex is fully closed before further work here.** Two drivers in one tree = corruption risk per `CLAUDE.md` GOLDEN RULE. Codex `app-server` processes remaining are just the IDE being open (harmless); the risk is only an *active agent run*.
3. **Uncommitted tree is intentional.** ~15 pre-existing modified files (`control_intent.py`, `verify_codex_claude_parity.py`, etc. — likely Codex parity WIP) + 109 untracked items (mostly `.agent/` churn) were **deliberately left untouched**. Do not blanket-commit them without knowing whose work they are.

## Key artifacts (by ref — don't duplicate)
- Commit: `git show 3b645b95`
- Plugin: `~/.claude/plugins/cache/claude-video/watch/0.2.0/` · config: `~/.config/watch/.env`
- Contract doc: `directives/video-vision-protocol.md` (§ Plugin contract)
- Upstream: `github.com/bradautomates/claude-video` (CHANGELOG.md has full 0.2.0 notes)

## Suggested skills for next session
- **`/watch`** — dogfood in a fresh session to confirm 0.2.0 loads (e.g. `/watch <short-url>`).
- **`/resume`** — this handoff is pinned; surfaces the thread by name.
- **`git-guardrails-claude-code`** — if committing any of the remaining tree, to keep Codex WIP separate.
