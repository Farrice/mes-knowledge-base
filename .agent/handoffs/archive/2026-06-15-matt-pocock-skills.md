---
thread: matt-pocock-skills
status: done
resume_hint: /to-issues on .scratch/external-skill-visibility/PRD.md → slice into .scratch/external-skill-visibility/issues/. / /tdd to build external-skill-visibility test-first (setup already done).
pin: false
---

# Handoff — Matt Pocock skills integration (end-of-session)

> Generated 2026-06-15 by `/end-session` → `/handoff`. Disposable working doc (OS temp dir), not workspace documentation.
> **Next session focus:** build the external-skill-visibility feature (PRD ready) via `/to-issues` → `/tdd`; continue importing/exercising Matt Pocock's skills.

## Completed this session
- Installed all 29 `mattpocock/skills` globally (`~/.agents/skills/`, symlinked into `~/.claude/skills/`), updated to latest. Website census confirmed nothing missing.
- Wired the engineering suite for this repo: local-markdown tracker. Config at `docs/agents/{issue-tracker,triage-labels,domain}.md`.
- Installed git-guardrails hook, merged into `.claude/settings.json` `PreToolUse(Bash)` (alongside `cost_gate_hook.py`). Backup in `.claude/backups/`.
- Registered everything in `directives/external-skills-registry.md` (the index of record; constitution files untouched).
- Demoed `/handoff`, `/to-prd` (produced the PRD below), `/grill-me`.
- **Shipped recommendation B:** `/end-session` Step 1 now delegates to `/handoff` (one handoff format). Boundary formalized in `.agent/workflows/end-session.md`.

## Remaining priority
1. `/to-issues` on `.scratch/external-skill-visibility/PRD.md` → slice into `.scratch/external-skill-visibility/issues/`.
2. `/tdd` to build external-skill-visibility test-first (setup already done).
3. (Open) Confirm the PRD's seams (top of the PRD file) before building.

## Key context / gotchas
- **`git push` is hook-blocked** (exit 2). Human pushes, or temporarily bypass. `git commit` is allowed.
- Guardrail matches its patterns as a **substring anywhere in the Bash command** — run verifications mentioning those git phrases from a script file, not inline.
- External (global) skills are invisible to `SKILL_INDEX.md` (`sync_registries.py` scans only `skills/`). Manual index = `directives/external-skills-registry.md`. The PRD aims to close this gap.
- Imported skills BYPASS The Chain (utilities; no DICE/route/finalize).
- session-state-protocol (`.agent/session-state.md`) is the mid-session anti-compaction anchor — separate job, untouched.

## Artifacts (by path — not duplicated here)
- `directives/external-skills-registry.md` — catalog + wiring + discovery + handoff/end-session boundary
- `.agent/workflows/end-session.md` — composed workflow (Step 1 → /handoff)
- `docs/agents/*.md` — engineering-suite config (local tracker)
- `.claude/hooks/block-dangerous-git.sh` — guardrail
- `.scratch/external-skill-visibility/PRD.md` — feature PRD (Status: ready-for-agent)
- Memory: `project_matt-pocock-skills-imported.md` (+ MEMORY.md pointer)
- Approved plan: `~/.claude/plans/thank-you-for-going-robust-harp.md`

## Suggested skills (invoke next session)
- `/to-issues` — slice the PRD into grabbable issues
- `/tdd` — build the feature red-green-refactor
- `/grill-with-docs` — capture domain terms (`CONTEXT.md`) + decisions (`docs/adr/`) while building
- `/triage` — manage the local-markdown issues as they accumulate
- `/handoff` — re-run at the next boundary (or just `/end-session`, which now calls it)
