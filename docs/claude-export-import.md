# claude.ai Web Export — Import & Enrichment Pipeline

Imports Farrice's full **claude.ai web/desktop/mobile** history (chat conversations, Projects,
and Claude's built-in memory) into the sovereign memory system, and surfaces the prompts /
experts he built in-chat as deployable Claude Code skills.

This corpus is **separate** from the superpowers episodic-memory plugin (which only captures
Claude **Code/Codex CLI** history). The web export is a net-new body of ~3,700 dense working
sessions that had never touched this repo.

> **Privacy:** raw transcripts live only under git-ignored `.tmp/claude-export/`; derived JSON
> under git-ignored `_active/harness/claude-export/`. Redaction (email/phone/6+digit) runs at parse and
> ingest. Nothing from this import is committed, and it never writes to Notion. The `.zip`s in
> `~/Downloads/` are the irreplaceable backup-of-record (the export URLs are single-use).

## Corpus (this export)

| Item | Count |
|------|-------|
| Conversations | 3,711 (3,511 non-empty · 40,741 messages · median ~8,800 words) |
| Messages with pasted attachments | 3,063 (where a lot of the built prompts live) |
| Projects | 142 (112 with custom instructions, 33 with docs) |
| Claude built-in memory | 1 (already-distilled profile of "Fresh") |

## Components (`execution/claude_export_*.py`)

| File | Role |
|------|------|
| `claude_export_state.py` | Shared atomic checkpoint (`_active/harness/claude-export/state.json`) — makes every stage resumable. Also the single source of path constants. |
| `claude_export_parser.py` | Streams the 1.37 GB of `conversations.json` with `ijson`, normalizes conversations/projects/memories → redacted markdown + `index.json`. Captures `attachments[].extracted_content`. |
| `claude_export_ingest.py` | Normalized conversations → sovereign `episodic/milestone` rows (workspace `claude-export`); + built-in memory; + (optional) 112 project prompts as `procedural/template`. Dedup by conversation uuid. |
| `claude_export_triage.py` | Stage A heuristic (all convs, $0) → Stage B Gemini classify (high-value subset, paced) → `rollup` → ranked deployables `menu`. |

Plus a minimal, backward-compatible guard in `execution/memory_distill.py`: the weekly distill
cron **excludes** the `claude-export` workspace by default (opt in with `--include-export` or
`ANTIGRAVITY_DISTILL_INCLUDE_EXPORT=1`) so thousands of imported rows can't flood the O(n²)
clustering / human-review queue unattended.

## Runbook

```bash
# 0. Raw data is staged at .tmp/claude-export/raw/{batch-0000 (symlink), batch-0001/}.
#    To re-stage from the Downloads zips:  unzip the batch-000N.zip into raw/batch-000N/.

# 1. PARSE  (deterministic, ~20s, $0)
python3 execution/claude_export_parser.py parse
python3 execution/claude_export_parser.py stats

# 2. TRIAGE
python3 execution/claude_export_triage.py heuristic                 # Stage A, all convs, $0
python3 execution/claude_export_triage.py classify --dry-run-cost    # estimate
python3 execution/claude_export_triage.py classify --top 500 --rpm 14   # paced (free-tier safe)
python3 execution/claude_export_triage.py rollup
python3 execution/claude_export_triage.py menu                       # → reports/extraction-menu.md
python3 execution/claude_export_triage.py stats

# 3. INGEST  (all conversations + built-in memory + project prompts)
python3 execution/claude_export_ingest.py preview
python3 execution/claude_export_ingest.py run --include-projects

# 4. EMBED  (cost-gated; enables vector recall through memory_facade)
python3 execution/memory_embed.py backfill --dry-run
python3 execution/memory_embed.py backfill --max-rows 500            # cap; re-run to continue

# 5. DISTILL  (OPTIONAL enrichment — deliberate, small, reviewed batches ONLY)
ANTIGRAVITY_DISTILL_INCLUDE_EXPORT=1 python3 execution/memory_distill.py run --days 1 --max-clusters 20
python3 execution/memory_review.py list          # human gate — nothing auto-promotes

# 6. DEPLOY  (human picks from the ranked menu)
#    open _active/harness/claude-export/reports/extraction-menu.md, then per pick:
/convert-prompt .tmp/claude-export/normalized/projects/<uuid>.md      # project prompt → skill
/extract-forge  .tmp/claude-export/normalized/conversations/<uuid>.md # rich dialogue → skill
```

## Free-tier rate limits (important)

The default `GEMINI_API_KEY` is **free tier**, with two separate quota buckets:

| Op | Model | Free-tier limit | Impact here |
|----|-------|-----------------|-------------|
| Classify | `gemini-3.1-flash-lite` (generate) | ~15 req/min | paced sequential; focus on `--top N` densest |
| Embed | `gemini-embedding-001` | 100/min **and 1,000/day** | only ~1,000 rows embed per day |

Because embedding is capped at **1,000/day**, the full corpus embeds over ~4 days of re-runs
(`memory_embed.py backfill` is idempotent — it resumes from unembedded rows each day). **This does
not block retrieval:** the facade's `fts_fallback` keyword path surfaces *every* imported row
immediately; embeddings only add vector/semantic recall on top. To finish embedding in one shot,
add a paid Gemini key (removes the daily cap) and re-run backfill.

The two buckets are independent, so `classify` and `backfill` can run at the same time.

## Retrieval

Everything is queryable through the existing unified door — no facade change:

```bash
python3 execution/memory_store.py recall --workspace claude-export --top 5
python3 execution/memory_store.py search "<keyword>" --top 5          # FTS5, works pre-embedding
python3 execution/memory_facade.py "<topic>" --sources sovereign      # vector (needs embeddings)
```

## Resume / idempotency

Every stage checks `state.json` and dedups by conversation uuid, so any stage can be killed and
re-run — it continues from the last completed item. `parse --force` rewrites markdown; `ingest`
re-runs are no-ops for already-ingested conversations.
