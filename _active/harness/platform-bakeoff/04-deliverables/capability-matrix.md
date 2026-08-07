# Platform Capability Matrix — 2026-06-11

Truth probes run live (Codex via `codex exec --sandbox read-only`; Gemini/IDE via filesystem inventory). Re-probe after any constitution change: `python3 execution/platform_compiler.py report`.

## The matrix

| Capability | Claude Code | Codex CLI/Desktop 0.133.0 | Antigravity IDE | Gemini CLI |
|---|---|---|---|---|
| Installed | ✅ | ✅ (`~/.npm-global/bin/codex`, Codex.app) | ✅ (`~/.gemini/antigravity*`) | ❌ NOT INSTALLED |
| Constitution auto-loads | ✅ CLAUDE.md | ✅ AGENTS.md (**proven live 2026-06-11**) | ⏳ `.agent/rules/constitution.md` created — needs GUI probe | n/a (would read GEMINI.md) |
| Follows file pointers | ✅ | ❌ **proven**: "GEMINI.md is referenced, not loaded" → fixed by making AGENTS.md self-contained | unknown | unknown |
| Canary token | n/a | ✅ `ANTIGRAVITY-CODEX-3J8R` **CONFIRMED live re-probe 2026-06-11** | `ANTIGRAVITY-IDE-9Q2M` (manual probe owed) | `ANTIGRAVITY-GEMINI-7X4K` |
| The Chain known cold | ✅ | ✅ **CONFIRMED** — all 6 steps incl. 5.5 + manual-gates rule, answered with no tools (was ❌ this morning) | ⏳ | ⏳ |
| Hooks / enforcement | ✅ physical (4 gates) | ❌ — manual-gate section in AGENTS.md | ❌ — manual-gate section in rules | ❌ |
| Bash + Python backbone | ✅ | ✅ (sandbox modes; repo is `trust_level = "trusted"`) | ✅ (IDE terminal) | ✅ |
| MCP: recall | ✅ | wired in `~/.codex/config.toml` 2026-06-11 — **needs interactive re-auth** (probe showed expired bearer on a URL server) | ❌ global `~/.gemini/settings.json` has only tavily+pencil | wired in repo `.gemini/settings.json` |
| MCP: perplexity | ✅ | wired 2026-06-11 (needs PERPLEXITY_API_KEY in env) | ❌ | wired in repo `.gemini/settings.json` |
| Sovereign memory (`memory_retrieve.py`) | ✅ | ✅ plain Python — works anywhere | ✅ | ✅ |
| `chain_runner.py finalize` | ✅ + Stop-hook | ✅ CLI (manual) | ✅ CLI (manual) | ✅ CLI (manual) |
| Sub-agent spawning | ✅ | ❌ sequential only | ❌ | ❌ |
| Skills access | ✅ native Skill tool | repo `skills/` readable; **`~/.codex/skills/` ports BROKEN** (probe log: dozens of YAML failures — missing frontmatter/description) | repo files readable; IDE knowledge store holds stale `antigravity_expert_*` items | repo files readable |
| Models | Fable 5 / Sonnet / Haiku (Opus = capacity-flaky, never pin) | gpt-5.5 reasoning=xhigh | Gemini 3.x + Claude (subject to capacity — source of "Opus not available" errors) | Gemini 3.x |

## Fork inventory (the actual transfer disease)

| Fork | State | Disposition |
|---|---|---|
| `/Users/farricecain/Codex Antigravity/` | Full divergent clone; May-era CLAUDE.md (33KB, pre-optimization); `.memory` touched 2026-06-11 08:02 (ACTIVE today) | **Harvest then retire.** Diff for unique work, pull anything valuable into this repo, then archive the folder. Codex already trusts THIS repo — no parallel copy needed. |
| `~/.codex/skills/` (~200 ports) | Many fail Codex skill validation (YAML frontmatter errors, proven in probe log) | Stop maintaining. AGENTS.md now points Codex at repo `skills/` as source of truth. Optionally delete broken ports later. |
| `~/.gemini/antigravity/knowledge/` (`antigravity_expert_*`) | Hand-pushed expert summaries, no sync | Leave as cache; repo files are canonical per `.agent/rules/constitution.md`. |

## Manual probes still owed (5 min, Farrice)

1. **Antigravity IDE**: open this workspace → new conversation → ask "What is the verify token in your workspace rules?" Expect `ANTIGRAVITY-IDE-9Q2M`. If absent: IDE isn't reading `.agent/rules/` → paste constitution into the IDE's global rules UI instead.
2. **Codex recall auth**: in a Codex session, trigger the recall MCP server and complete re-auth when prompted (probe showed an expired/invalid bearer token).
3. **Gemini CLI** (optional lane): only if wanted — `npm install -g @google/gemini-cli`, then cold-ask for the canary (expect `ANTIGRAVITY-GEMINI-7X4K`).
