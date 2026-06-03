# Skill Invocation & Routing — System Contract

> **Status:** LIVE as of 2026-06-02. This is the source-of-truth for how skills become reachable and how the system routes to them. Built to close the gap where 241 of 244 skills had no slash command and routing depended entirely on Claude remembering.

## The problem this fixed

Two halves that were supposed to be one system:
- **Workflows** had 598 slash commands. **Skills** had 3. So `/parallax` worked but `/david-bayer` didn't exist.
- **Routing to skills was 100% Claude-discretionary** — no prompt-time trigger, no script. The only "backstop" fired *after* the response, could only warn (not block), and was blind to the "no skill loaded at all" case. This violated the project's own rule: never ship infra that depends on Claude remembering (`feedback_ai-memory-dependent-observability`).

Result: the user kept re-explaining which expert to use, because nothing deterministically surfaced them.

## The three pillars (all live)

### 1. INVOKE — every skill has a slash command
`execution/sync_registries.py` → `sync_skill_commands()` generates one `.claude/commands/<name>.md` per skill.
- **Naming:** short 2-token name where unique (`/david-bayer`); full slug where the short collides (the 12 `luke-iha-*`, 7 `nate-b-jones-*`, etc. keep full slugs). Deterministic via `compute_command_names()`.
- **Each command loads Tier 2:** SKILL.md **+ genius.md** (the methodology lives in genius.md; SKILL.md alone under-loads — this was a verified failure mode).
- **Clobber-safe:** never overwrites a file lacking `GEN_MARKER`. Your 598 workflow shims are physically untouchable by this generator. 3 skills whose names collide with existing workflows are skipped (reachable by name / `/find-skill`).
- **Manifest:** writes `.agent/skill-commands.json` (command→skill map) for the router + docs.

### 2. ROUTE — deterministic suggestion on every prompt
`execution/skill_router_hook.py`, wired in `.claude/settings.local.json` → `hooks.UserPromptSubmit`.
- Runs `find_skill.py` (BM25) on every substantive prompt **before Claude reasons**, injects top matches + slash commands as context.
- **Fail-safe:** any error → exit 0, inject nothing. Never breaks a prompt.
- **Quiet on trivial:** skips prompts <18 chars / <3 words, slash/`@` commands, greetings, confirmations.
- **Relevance floor:** injects nothing if top score <3.0; shows only matches ≥45% of top score.
- **Suggests, doesn't force:** Claude still decides; top-3 shown to hedge against a wrong #1.

### 3. MAINTAIN — it stays cohesive
- `sync_skill_commands()` is wired into the `sync_registries.py` main block. Run `python execution/sync_registries.py` after adding any skill → it auto-gets a command and enters routing. Idempotent (re-run = 0 created, all unchanged).
- **Adding a skill:** drop `skills/<slug>/SKILL.md` (+ genius.md) → run sync → done. Command + routing automatic.

## The matcher engine (`find_skill.py`) — shared by hook AND `/find-skill`

Upgraded 2026-06-02 for recall:
- **Hyphen-split tokenizer:** compounds like `spoken-communication`, `authenticity-as-status` now split into subtokens (kept WITH the whole compound). This was the #1 recall killer — "communication" never matched "spoken-communication" before. Fixing it moved Bayer from *absent* to *#1 (33.7)* on his own domain.
- **Light stemming:** `communication`~`communicate`, `authentic`~`authenticity`.
- **SYNONYMS map:** the high-leverage curation surface. When routing whiffs, add the user's natural phrasing here pointing at words in the target skill's description. Clusters added: spoken/presence/persuasion, copywriting, positioning, memoir/literary, brand/luxury/design.

**When routing sends you to the wrong expert:** edit `SYNONYMS` in `find_skill.py`, then `python3 execution/find_skill.py --rebuild-index "x"`. That single map fixes both the hook and `/find-skill`.

## How to invoke a skill (for the user)

| Want | Do |
|---|---|
| A specific expert | `/david-bayer` (or `/luke-iha-vicious-hooks` for multi-skill experts) — OR name them in plain English |
| Not sure which expert | Just describe the job — the UserPromptSubmit hook now surfaces the right skills automatically |
| Search explicitly | `/find-skill <natural language>` → ranked matches + slash commands |
| A full pipeline | `/parallax`, `/writers-room`, `/autopilot` (workflows that load skills inside) |

## Files

| File | Role |
|---|---|
| `execution/sync_registries.py` | Generates SKILL_INDEX, AGENT_INDEX, **+ 241 skill commands** |
| `execution/find_skill.py` | BM25 matcher (hook + `/find-skill` share it) |
| `execution/skill_router_hook.py` | UserPromptSubmit deterministic routing backstop |
| `.claude/settings.local.json` | Registers the hook |
| `.agent/skill-commands.json` | command→skill manifest (generated) |
| `.agent/skill-index.json` | BM25 index cache (auto-rebuilds on skill mtime change) |
