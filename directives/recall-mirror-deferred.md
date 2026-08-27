# Recall Mirror — Deferred (Sprint 3 Decision, 2026-05-25)

> Why Recall is NOT being mirrored into sovereign sqlite, and what replaces it.

## Decision

Recall (3,000+ saved cards — YouTube transcripts, articles, extractions) is **not mirrored** into the sovereign `notion_mirror` equivalent. Notion's operational databases and the five integration-owned Simon Intellectual Library databases are mirrored by `execution/mirror_notion.py`. The mirror-staleness HALT/WARN gate in `execution/chain_runner.py` therefore only enforces freshness for `notion_mirror`, not for Recall.

## Why deferred

**Recall MCP is agent-layer only.** The `mcp__recall__*` tools (`search`, `get_document_content`, `explore_kb`, `filter_by_metadata`) are exposed via MCP and only callable from within a Claude Code conversation. There is no documented Python SDK, no public REST endpoint we have credentials for, and no way to invoke MCP from a launchd cron job.

A mirror cron would either need:
1. **Headless Claude Code session** to call MCP tools — fragile, adds latency, burns tokens, requires the daemon to stay alive
2. **Reverse-engineer the Recall API** — not authorized, fragile to vendor changes, breaks Terms

Neither is worth ~3K rows of secondary-source grounding when the primary use case (Tier 1.5a Recall grounding during The Chain Step 4) already works in agent context.

## What replaces it

`execution/recall_logger.py` is already wired into `chain_runner.finalize` (commit `a35ae51a`, 2026-05-03 — closed the "AI-Memory-Dependent Observability" failure class). Every Recall search attempt is logged to `evolution_store/traces/recall_grounding.jsonl` with status (fired/skipped/failed). Observability of Recall behavior is preserved without mirroring its content.

For grounding-relevant tasks, Recall continues to fire **live during agent context** per `directives/recall-grounding-protocol.md`. The card content is fetched fresh per query — staler than a mirror, but always primary.

## When to revisit

Revisit if any of:
- Recall ships a public Python SDK or webhook
- A future workflow needs Recall content in a non-agent context (cron-driven distillation, batch analysis, periodic reports)
- The sovereign retrieval cascade (`memory_retrieve.py`) measurably degrades from missing Recall context

Until then: **Recall stays primary, Notion gets mirrored, sovereign sqlite is the cross-session compounding layer.**

## Mirror-staleness gate scope

`execution/memory_ops.py::check_mirror_freshness()` checks these sources:

| Source | Tracked via | WARN at | HALT at |
|---|---|---|---|
| `sovereign_db` | file mtime of `.memory/sovereign.db` | 36h | 72h (WARN only — not a true mirror) |
| `notion_mirror` | `MAX(mirrored_at)` from `notion_mirror` table | 36h | 72h (BLOCKING — Sprint 3) |
| ~~`recall_mirror`~~ | n/a — deferred | n/a | n/a |

If `mirror_notion.py` fails to run for 3 days, chain_runner.finalize will return a BLOCKING error rather than silently producing output against a stale view of Notion.

---

*Created: 2026-05-25 (Sprint 3 of Antigravity Memory System rollout)*
