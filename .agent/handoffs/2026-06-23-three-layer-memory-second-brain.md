---
thread: three-layer-memory-second-brain
status: ready
resume_hint: Commit the uncommitted memory-system + Notion Library work; then optionally extend the Library
unfinished: Commit changes; (optional) extend Library — more experts / Linked Entries / grounded advisors — + run weekly memory loop (episodic_ingest→embed→distill→review)
branch: main
pin: true
---

# Handoff — 3-Layer Memory System + Populated Notion Intellectual Library
_2026-06-23 · thread: `three-layer-memory-second-brain`_

## What this session shipped (two linked threads)

### Thread A — 3-layer memory stack (LIVE)
Origin: a Simon Scrapes video (`4iMZA1omCkM`) on Claude Code memory. Key reframe: the video's category (mechanical hook-driven session auto-capture, ~claude-mem) is already owned by a SUPERIOR live instance — the superpowers `episodic-memory` plugin (133k indexed exchanges, 23k this project, local embeddings, $0). So this was activate + wire + consolidate, NOT integrate a new repo. **Do NOT install claude-mem** (ungated spend + double PostToolUse hook → disqualified by the cost-gate principle).

Architecture: **L1 episodic capture** (superpowers plugin → `~/.config/superpowers/conversation-index/db.sqlite`, `exchanges` table) → **L2 semantic** (`.memory/sovereign.db`) → **L3 second brain** (Notion + local). Front door = `execution/memory_facade.py`.

Changes (all verified):
- `execution/memory_facade.py` — added `episodic` source (read-only project-scoped LIKE on `exchanges`, never `vec_exchanges`). Query: `python3 execution/memory_facade.py "<topic>" --sources episodic`. Now part of default `ALL_SOURCES`. ~0.43s.
- `execution/episodic_ingest.py` (NEW) — L1→L2 bridge: session summaries → sovereign episodic tier (`preview` default / `run`), idempotent, PII-redacted, deterministic (no LLM at ingest). 15 sessions already ingested. Complete the loop with `memory_embed.py` → `memory_distill.py preview` → `memory_review.py` (human gate; nothing auto-promotes).
- `execution/notion_api.py` — added `session_memory` DB id + `push_session_memory()` (allow-listed: Title/Date/Mode/Key-Decisions/Pickup only, never raw transcripts) + `session-memory` CLI subcommand.
- `_active/memory-bakeoff/04-deliverables/bake-off-protocol.md` (NEW) — locked decision rule; incumbent episodic-memory wins; hard DQ for ungated paid calls. Fast-path (adopt incumbent directly) recommended.
- `CLAUDE.md` — facade now spans 5 stores incl. episodic; added the 3-layer memory-stack summary + Knowledge Sources episodic entry.

### Thread B — Notion Intellectual Library (DEPLOYED + POPULATED)
Hub: https://app.notion.com/p/78a6e794605947a7b864c9a358e87d92

- The Notion-AI-built DBs were unwritable by the integration token (data-source/linked-view trap). Fix: created INTEGRATION-OWNED classic DBs under the hub (writable via `notion_api.py`, no sharing maze). See memory `reference_notion-ai-database-integration-gotcha`.
- Seeded via workflow (atomize 12 A-tier experts from their `genius.md`) → `notion_api.py` bulk-write: **84 Knowledge Entries + 12 Experts + 12 Sources + 12 Skills**, all Expert/Source relations wired, all 9 categories, 69 Proven / 15 Tested. Added By-Category / By-Confidence views. Archived the 5 empty AI-made shells (in Notion trash 30d). Hub cleaned.
- Integration-owned DB ids: Knowledge Entries `38849875a897812cb693c7b35e7530a6` · Experts `38849875a89781d78ed5f5731ce0d1c1` · Sources `38849875a897811585f2f1a30e2291a4` · Skills `38849875a897813da451fdb32c7121f2` · Session Memory `38849875a89781c0950ef6a48bb28a72` (this last is in `.env` as `NOTION_DB_SESSION_MEMORY`).

## State / gotchas for the next agent
- `.env` has `NOTION_DB_SESSION_MEMORY` set to the working (integration-owned) id — do not revert to the AI-made `46dc…` id (unwritable).
- Everything I created in Notion is reversible (archived DBs recoverable from trash 30 days).
- Uncommitted repo changes exist (see Remaining).
- Build scripts live in the session scratchpad (`build_library.py`, `lib_full.json`, `lib_ids.json`) — re-runnable to EXTEND the Library with more experts (matched by name; appends).

## Remaining priority (next session)
1. **Commit** the uncommitted work (offered at end of /end-session): `execution/memory_facade.py`, `execution/notion_api.py`, `execution/episodic_ingest.py`, `CLAUDE.md`, `.env`, `_active/memory-bakeoff/`, `_active/notion-intellectual-library/04-deliverables/DEPLOY-RUNBOOK.md`.
2. (Optional) Extend the Library: more of the 223 `genius.md` experts; draw `Linked Entries` cross-connections; wire grounded advisors (Simon Prompt 2) now that there's substance for filter/refusal tests.
3. Run the weekly memory loop: `episodic_ingest.py run` → `memory_embed.py` → `memory_distill.py preview` → `memory_review.py`.

## Suggested skills
- `/simon-intellectual-library-os` — Library operations (ingest, advisors, monthly health check).
- `/library-extraction-bridge` (workflow) — atomize an extraction into ready-to-paste Knowledge Entries.
- `/resume` — pick this thread back up.
- `/extract` or `/extract-forge` — if adding NEW experts before seeding them into the Library.

## Core context to load
- Plan: `/Users/farricecain/.claude/plans/https-www-youtube-com-watch-v-4imza1omck-delightful-hennessy.md`
- Memory: `project_three-layer-memory-system.md`, `reference_notion-ai-database-integration-gotcha.md` (in the project auto-memory dir)
- `_active/notion-intellectual-library/04-deliverables/DEPLOY-RUNBOOK.md`
