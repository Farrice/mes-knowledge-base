---
job: source-to-skill-harvest
name: Source → skill system harvest
family: harvest-research
tier_default: T1
runs: 1
last_ratchet: 2026-09-09
---

## The job
Turn a video, podcast, book, or article into a deployable skill (SKILL.md + genius.md + workflows + v2 prompts), registered so it fires from `/` in Claude Code and Codex, with the concept it teaches wired into the harness where it changes behavior.

## Sub-jobs / lanes
- L1 Source acquisition — transcript + visual context into `extractions/<expert>/` (`execution/fetch-transcript.py`, `execution/fetch-video-context.py`, `/watch`) [parallel]
- L2 Arsenal + expert ID — `python3 execution/arsenal.py "<topic>"`, `AGENT_INDEX.md` check; existing expert = Extension Mode [parallel]
- L3 Corpus gate + enrichment — `extraction_manifest.py corpus`; thin source (<8k words) → ≤4 free same-expert sources, quotes only (Sonnet seat) [after: L1]
- L4 Deep extraction (MES 3.0) — `directives/mes-3.0-extract.md`; manifest derive → `.tmp/manifest-<slug>.json` [after: L2, L3]
- L5 Build the skill — SKILL.md, genius.md, references/{source-quotes,genius-patterns,hidden-knowledge,cross-domain-patterns}.md, workflows/, prompts-v2 (≥5) [after: L4]
- L6 Register — `sync_registries.py` → `generate_slash_commands.py` → `mint_menu_wrappers.py --scope skill <name> --apply`; `.agents/skills/<name>` symlink for Codex [after: L5]
- L7 Wire the behavior — where the concept changes how the harness acts (hook card, directive, front door, dialect line), extend the existing mechanism; never a parallel one [after: L5]
- L8 Verify — `renaissance_audit.py`, `skill_auditor.py check --skill`, `prompt_library.py build`, sabotage any new check both directions [after: L6, L7]

## Ask me first
- Q: Is this a new expert or a new layer on one we have? · look first: `AGENT_INDEX.md`, `skills/<expert>-*`
- Q: Which of YOUR jobs should this concept plug into first? · look first: `.agent/missions.jsonl` open missions, `MEMORY.md` active projects
- Q: Behavior wanted every turn, on call, or hook-fired on a pattern? · look first: `directives/steering-loop.md`, `execution/hooks/steering_loop_hook.py` mode cards

## Handles alone
Fetching, transcript cleanup, enrichment reads, arsenal checks, MES extraction, skill files, prompts, registration scripts, wrappers, symlinks, verifiers, lane worktree, memory note draft.

## Comes back when
- The source contradicts a standing rule in `CLAUDE.md`/memory (packet: adopt / adapt / reject)
- Two plausible homes for the behavior (hook vs front door vs directive) with different costs
- A paid enrichment source would help (cost gate — never assumed)
- Any T2 action the wiring implies (publishing, sending, spending)

## Needs approval
Paid API calls (Gemini Deep Research, Perplexity, Apify — Apify is retired) · editing `.codex/hooks.json` (trust hashes) · anything in `~/.codex` or `~/.claude` global config beyond thin trigger bridges.

## Needs
Source URL or file · `.venv` python · `yt-dlp`/`ffmpeg` (for video) · `~/.config/watch/.env` for `/watch` · a worktree lane (main is integration-only).

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| captions missing / login-gated | `fetch-video-context.py`, Whisper via `/watch`, Playwright per `directives/browser-automation-safety.md` | all routes fail |
| source is paywalled (e.g., a paid guide) | extract the concept from the free source; seed OUR assets from OUR jobs, never fabricate the paid content | never — say so in the card |
| thin corpus (<8k words) | auto-enrich ≤4 free same-expert sources, quotes only | enrichment would need a paid pull |
| expert already exists | Extension Mode: new topic skill beside siblings, extend `agents/<expert>/` | the existing skill already covers the topic (packet: extend vs skip) |
| parity minter refuses (foreign file collision) | rename the workflow slug; never hand-write a wrapper | two renames fail |
| verifier fails | fix the artifact, rerun | the same check fails twice |

## Done means
`skills/<name>/` complete with ≥5 prompts-v2 · `renaissance_audit.py` 0 fail · `/name` shim exists in `.claude/commands/` and `.agent/workflows/` · `.agents/skills/<name>` symlink · behavior wiring verified by a sabotage test both directions · `extractions/<expert>/<topic>-extraction.md` record · memory note + `MEMORY.md` pointer.

## Ratchet log
- 2026-09-09 — first run (dogfood): worktree guard rejects heredocs and the word complete in a Bash string — patches go in script files; lane names cannot contain hyphens (parser); handoff_store status vocabulary is fixed (use mid-build, target in hint); verifiers must skip the handoff store on a temp root
