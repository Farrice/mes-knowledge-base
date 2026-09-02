# Scrapes Skill Systems — Integration (LIVING)

*Installed 2026-09-02 via `npx @scrapes/installer` v1.3.0 (Skill Systems installer 3.1.0). Agentic OS NOT installed. Owner: Farrice. Update in place.*

## What is on disk
- **36 skills** in `.claude/skills/<name>/` (each with `.installed.json` hashes, `skill-pack/config/sys-config.md` paths, `CHANGELOG.md`).
- **4 workers** in `.claude/agents/`: `ssc-designer`, `ssc-image-generator`, `ssc-template-builder`, `l2s-content-packager`. Standing exception to the no-subagents rule (Farrice, 2026-09-02): these are the product's own, not harness-authored.
- **`brand_context/`** at repo root: `voice-profile.md`, `samples.md`, `icp.md`, `positioning.md`, `design-tokens.md`. Populated from disk canon, not interview. `visual-identity/` is produced by `/mkt-visual-identity` (Farrice's run).
- **`.mcp.example.json`**: Zernio MCP template. Not wired; sends stay human.
- **36 symlinks** `.agents/skills/<name>` → `../../.claude/skills/<name>` so Codex discovers the same folders.

## How to invoke
| Harness | Call | Notes |
|---|---|---|
| Claude Code | `/00-social-content`, `/mkt-brand-voice`, etc. | Native: `.claude/skills/<name>` mounts as `/<name>`. Orchestrators dispatch `.claude/agents/ssc-*` via the Agent tool. |
| Codex | Skill auto-loads from `.agents/skills/<name>/SKILL.md`; or say "use the 00-social-content skill" | Codex has no Claude subagents. Where a SKILL.md says "dispatch ssc-designer", read `.claude/agents/ssc-designer.md` and run it inline as the prompt. Verify discovery once: `codex exec "list the skills you can see whose names start with 00-"`. |
| `/arsenal` and the router hook | indexed as `vendor:<name>`, family `scrapes-skill-systems`, always menu-reachable | `execution/arsenal_index.py` patch, 2026-09-02. |

## Rules
1. **Never edit inside `.claude/skills/<scrapes-skill>/`.** `.installed.json` hashes every file; the updater protects edits by refusing to overwrite them, which strands you on an old version. Extend through `brand_context/`, wrappers in `.agent/workflows/`, or `context/learnings.md` (their own self-improvement hook).
2. **`sys-config.md` paths are absolute to the main checkout** (rewritten from the lane path on install day). If the repo moves, rerun the installer or sed the four path lines.
3. **Publishing stays off.** `tool-publisher`, `tool-zernio-social`, `mkt-short-form-posting` (post step), `tool-video-upload` (upload step). Sends stay human.
4. **`tool-linkedin-scraper` is dead** (Apify retired).
5. **Craft gate and cost gate still apply** to `viz-image-gen`, `viz-hyperframes`, and any paid generation.
6. **Prose classifier runs before anything ships**, including `tool-humanizer` output.
7. **Not committed:** `.npmrc` (token; the global `~/.npmrc` carries it) and the ~30MB face/pose model binaries under `**/models/` (gitignored; they stay on disk).

## Updating
```
npx @scrapes/installer            # menu → Update skill systems
```
Needs a live npm token from the Scrapes classroom (they rotate ~monthly). After any update, rerun `python3 execution/arsenal_index.py build --rebuild` and re-check the four `sys-config.md` path lines. Model binaries are gitignored, so a fresh clone of this repo needs one installer run to restore them.

## Keys the skills look for
Present: `GEMINI_API_KEY`, `ANTHROPIC_API_KEY`, `TAVILY_API_KEY`, `PERPLEXITY_API_KEY`, `FAL_KEY`.
Absent and optional: `OPENAI_API_KEY` (GPT Image path in viz-image-gen; Gemini path works without it), `YOUTUBE_API_KEY` (tool-youtube channel mode only), `UNSPLASH_ACCESS_KEY` / `PEXELS_API_KEY` (tool-image-search paid tiers; free tier works), `SCREENSHOTONE_API_KEY` (tool-web-screenshot has a Playwright fallback).
Absent and stays absent: `ZERNIO_API_KEY`, `APIFY_API_KEY`, `XAI_API_KEY`, `GROQ_API_KEY`, `TELEGRAM_BOT_TOKEN`, `SUPABASE_*`, `HEYGEN_API_KEY`.

## Agentic OS (the other product) — not installed
The installer's "Install Agentic OS" is a git clone of a separate environment: its own CLAUDE.md, hooks, a Telegram supervisor, remote-session scripts, a systemd service. It expects to be the project root. Installing it inside this repo would collide with the harness. If Farrice wants it: run the installer with `--dir ~/scrapes-agentic-os` (a sibling folder, GitHub token at the prompt), read it, then port pieces here deliberately. Never merge it into this tree wholesale.

## Constitution block
`directives/constitution/shared-blocks.md` carries a `shared-scrapes-skill-systems` block. The compiler only fills markers that already exist in CLAUDE.md and AGENTS.md, so the first insert is a one-time script: `python3 _active/harness/scrapes-skill-systems/apply_constitution_block.py` then `python3 execution/constitution_compiler.py sync`.
