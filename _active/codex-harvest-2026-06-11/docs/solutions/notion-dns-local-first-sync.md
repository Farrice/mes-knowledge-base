# Notion DNS Local-First Sync

Use this systems pattern when Notion logging, retrieval, workflow automation, agent feedback loops, or self-improvement checks fail from Codex even though the Notion integration exists.

## Problem

Sandbox DNS/network failures to `api.notion.com` can look like a broken Notion integration. If the harness treats local fallback as successful remote sync, self-improvement dashboards and retrieval checks become misleading.

## Trigger

- Notion calls fail with name-resolution or DNS errors.
- `/knowledge-search --scope=notion` returns nothing unexpectedly.
- Performance Log entries exist locally but cannot be found in Notion.
- System health reports inactive or stale feedback loops because remote logging failed.

## Working Solution

Keep the Codex wiki local-first and use Notion as a metadata/search mirror.

Use:

```bash
python3 execution/notion_api.py status
python3 execution/log_performance.py sync-status
python3 execution/log_performance.py sync-pending --dry-run
python3 -m execution.notebooklm_knowledge_retrieval "query" notion
```

Only run real sync after confirming it is acceptable to create Notion pages:

```bash
python3 execution/log_performance.py sync-pending --limit 20
```

## Why It Works

It separates three states that used to blur together: missing credentials, sandbox network failure, and real API/schema problems. Local JSONL and `knowledge/` remain the source of truth, while Notion becomes a recoverable mirror when network access is available.

## Prevention Rule

Never report Notion logging as remotely successful unless a Notion URL was captured. If DNS is unavailable, report `network_unavailable`, keep local evidence, and queue sync through `sync-pending`.
