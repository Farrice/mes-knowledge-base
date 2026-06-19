# External Skills Registry

**Purpose**: Governance + catalog for *imported third-party Claude Code skills* — skills authored outside Antigravity, installed globally, and used as their creators intended. These are NOT extracted experts (no MES 3.0, no persona, no genius.md) and they do NOT run through The Chain's 6 steps. They are deterministic utilities invoked explicitly by the user (`/skill-name`) or auto-loaded by the harness when their `description` triggers match.

**Why a separate registry**: `execution/sync_registries.py` scans only the project `skills/` dir, so `SKILL_INDEX.md` / `AGENT_INDEX.md` never see globally-installed skills. This file is the manual index of record for everything installed outside that tree.

**Install scope**: Global → `~/.agents/skills/<name>/` (canonical source) with symlinks fanned out into per-agent dirs (`~/.claude/skills/<name>` for Claude Code, plus Codex / Cursor / Gemini CLI / Copilot). One install, every agent sees it. The harness lists them in the Skill-tool catalog at session start; newly installed skills appear next session (or on reload).

**Do not fork into `skills/`**: Keep imported skills at their global source so `npx skills update` keeps them current. Forking a copy into the project tree breaks the update path and creates drift. Integrate by *reference* (this doc + memory), not by copy.

---

## The `skills` CLI (skills.sh)

The universal installer/manager used for all imported skills.

```bash
npx skills@latest add <owner>/<repo>          # interactive: pick skills + agents
npx skills@latest add <owner>/<repo> --all    # install everything, all agents, -y
npx skills@latest add <owner>/<repo> -s <name> -g   # one skill, global
npx skills@latest list                        # list installed
npx skills@latest update [names...]            # update to latest (alias: upgrade)
npx skills@latest remove [names...]            # uninstall
npx skills@latest use <owner>/<repo>@<skill>  # print the prompt WITHOUT installing (try-before-install)
```

Flags that matter: `-g/--global` (user-level), `-s/--skill <names>` (select skills — note: `skill=foo` is **not** valid, use `-s foo`), `-a/--agent '*'` (all agents), `-y` (skip prompts), `--copy` (copy instead of symlink). `--all` = `-s '*' -a '*' -y`.

> Gotcha observed 2026-06-15: global install of these PromptScript-format skills prints `✗ … PromptScript does not support global skill installation` for the slash-command layer, but the SKILL.md global install still succeeds (`~/.agents/skills/`). The warning is non-fatal — verify on disk, don't trust the red ✗.

---

## Source 1 — Matt Pocock / AI Hero  (`mattpocock/skills`)

- **Repo**: https://github.com/mattpocock/skills · **Site**: https://www.aihero.dev · **Newsletter**: aihero.dev/s/skills-newsletter
- **Philosophy** ("Skills For Real Engineers"): small, composable, model-agnostic, adapt-and-own. Built to fix four agent failure modes — (1) didn't do what I want → *grilling sessions*; (2) too verbose → *shared/ubiquitous language* (CONTEXT.md); (3) code doesn't work → *feedback loops* (TDD, diagnose); (4) ball of mud → *invest in design daily* (improve-codebase-architecture).
- **Installed**: 2026-06-15, all 29 skills, global. Verify: `ls ~/.agents/skills/`.
- **Update**: `npx skills@latest update` · **Setup for engineering suite**: run `/setup-matt-pocock-skills` once per repo to wire the issue tracker (GitHub/Linear/local files) + triage labels + docs path. Required before `/to-prd`, `/to-issues`, `/triage` work correctly.

### His skill-design conventions (use these when WE author native skills, too)
- `description` is the only thing the agent sees when choosing a skill → first sentence = what it does, second = "Use when [specific triggers]". Max 1024 chars, third person.
- SKILL.md under ~100 lines; progressive disclosure (split into REFERENCE.md / EXAMPLES.md / format files only when needed — see `grill-with-docs` shipping `ADR-FORMAT.md` + `CONTEXT-FORMAT.md`).
- Scripts only for deterministic ops (validation/formatting). No time-sensitive info. References one level deep.

### Catalog (29)

**⭐ Productivity — session & thinking utilities (highest value for our flow)**
| Skill | What it does | Use when |
|---|---|---|
| `handoff` | Compacts the current conversation into a portable handoff doc (saved to OS temp dir) with a "suggested skills" section; redacts secrets; references artifacts by path not copy | Splitting work across sessions/agents; spinning off an out-of-scope sub-session without polluting the current context |
| `grill-me` | Interviews you relentlessly about a plan/design, resolving each decision branch until shared understanding | Before building anything — stress-test intent (his #1 most-used) |
| `grill-with-docs` | `grill-me` + builds CONTEXT.md ubiquitous language and ADRs inline as decisions crystallise | Same, when you want the alignment captured as durable docs |
| `caveman` | Ultra-compressed comms mode (~75% fewer tokens, drops filler/articles, keeps technical accuracy) | "caveman mode" / token thrift on long sessions |
| `teach` | Teaches you a new skill/concept within the workspace | Learning a concept hands-on |
| `write-a-skill` | Authoring guide for new skills (structure, progressive disclosure, description triggers) | Writing any new skill (ours or imported-style) |

**Engineering — real-codebase dev loop** (`/setup-matt-pocock-skills` first)
| Skill | What it does |
|---|---|
| `tdd` | Red-green-refactor loop with guidance on good vs bad tests |
| `diagnose` | Disciplined hard-bug / perf-regression loop: reproduce → minimise → hypothesise → instrument → fix → regression-test |
| `prototype` | Throwaway prototype to flesh out a design (terminal app for logic, or toggleable UI variations) |
| `to-prd` | Turn current conversation into a PRD, publish to issue tracker |
| `to-issues` | Break a plan/PRD into independently-grabbable issues (tracer-bullet vertical slices) |
| `triage` | Issue triage via a role-driven state machine |
| `zoom-out` | Agent gives broader/higher-level context on unfamiliar code |
| `improve-codebase-architecture` | Find deepening/refactor opportunities, informed by CONTEXT.md + ADRs |
| `setup-matt-pocock-skills` | One-time per-repo setup: issue tracker + triage labels + docs path |

**Misc — repo guardrails & scaffolding**
| Skill | What it does |
|---|---|
| `git-guardrails-claude-code` | Installs Claude Code hooks blocking dangerous git (push, reset --hard, clean, branch -D) |
| `setup-pre-commit` | Husky + lint-staged (Prettier) + typecheck + tests pre-commit hooks |
| `migrate-to-shoehorn` | Migrate test `as` assertions → @total-typescript/shoehorn |
| `scaffold-exercises` | Course exercise dir structures (sections/problems/solutions/explainers) |

**Personal / Writing**
| Skill | What it does |
|---|---|
| `edit-article` | Restructure/clarify/tighten article drafts |
| `obsidian-vault` | Search/create/manage Obsidian notes with wikilinks + index notes |

**In-progress — writing pipeline (experimental)**
| Skill | What it does |
|---|---|
| `writing-shape` | Shape raw-material markdown into an article conversationally (openings, growth, format debate) |
| `writing-fragments` | Mine you for heterogeneous writing fragments → one raw-material doc |
| `writing-beats` | Assemble an article as a journey of beats, choose-your-own-adventure style |
| `review` | Review changes since a fixed point on Standards + (second axis) |

**Deprecated (installed, but Matt has retired — prefer the replacements above)**: `qa`, `request-refactor-plan`, `design-an-interface`, `ubiquitous-language`.

### How these coexist with Antigravity
- **Invoked explicitly or trigger-loaded — they bypass The Chain.** No DICE scoring, no expert routing, no finalize() for a `/handoff` or `/grill-me` run. They are tools, not deliverables.
- **`handoff` vs our session tooling (composed, decided 2026-06-15)**: three distinct jobs, one handoff format. **`/handoff`** owns the canonical portable handoff doc (temp dir, cross-tool). **`/end-session`** is the system close-down ritual and now **calls `/handoff`** for its handoff-generation step (Step 1), then adds conversation-index update + commit offer + optional `--deep` cleanup — the things `/handoff` doesn't do. **session-state-protocol** (`.agent/session-state.md`, auto) is a mid-session anti-compaction anchor, NOT a handoff. Reach for `/handoff` directly for mid-session spin-offs / cross-tool jumps; run `/end-session` to close down (it gives you the same handoff doc plus hygiene). Boundary lives in `.agent/workflows/end-session.md`.
- **Writing skills** (`writing-*`, `edit-article`) are Matt's general-purpose drafting loops; our voice/craft roster (writers-room, Hawley, Roth, Lamott, depth-stack) remains primary for brand/content work. Reach for Matt's only for quick structural drafting, not voice-critical deliverables.

---

## Engineering suite — per-repo wiring (this repo, 2026-06-15)

`/setup-matt-pocock-skills` was run for the Antigravity repo. Because CLAUDE.md is deliberately slim and AGENTS.md/GEMINI.md are canary-protected + drift-gated (`platform_compiler.py`), the `## Agent skills` block lives **here** (the scoped directive) instead of being injected into any constitution file. The operational config is at `docs/agents/*.md` (the standard path Matt's skills reference). This is the **index of record** for that wiring.

**Discovery note (Claude Code):** Claude Code auto-loads CLAUDE.md, not this directive or AGENTS.md — so the block below is NOT in always-on context. When you invoke `/to-prd`, `/to-issues`, `/triage`, `/diagnose`, `/tdd`, `/improve-codebase-architecture`, or `/zoom-out` and the skill says "config should have been provided — run `/setup-matt-pocock-skills`", the config already exists: **read `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, `docs/agents/domain.md`.** Do NOT re-run setup.

### The `## Agent skills` block (canonical)

```markdown
## Agent skills

### Issue tracker
Local markdown — issues/PRDs live as files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Triage labels
Five canonical roles recorded as a `Status:` line per issue file (defaults; role name == status). See `docs/agents/triage-labels.md`.

### Domain docs
Single-context. `CONTEXT.md` + `docs/adr/` created lazily by `/grill-with-docs`. See `docs/agents/domain.md`.
```

### git-guardrails (installed 2026-06-15)
`git-guardrails-claude-code` hook installed at `.claude/hooks/block-dangerous-git.sh`, MERGED into `.claude/settings.json` `PreToolUse(Bash)` **alongside** `cost_gate_hook.py` (not replacing it). Blocks `git push` (incl. `--force`), `reset --hard`, `clean -f[d]`, `branch -D`, `checkout .`, `restore .` → exit 2 + BLOCKED message. To customize, edit the `DANGEROUS_PATTERNS` array in the script. Backup of pre-merge settings: `.claude/backups/settings.json.*.bak`. `setup-pre-commit` was deliberately skipped (Husky/Prettier/JS — poor fit for this Python+markdown repo).

