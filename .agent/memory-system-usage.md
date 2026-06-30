# 3-Layer Memory System — Quick Reference

**Status: LIVE & VERIFIED 2026-06-23** | All layers operational, acceptance tests passing

---

## 🎯 The Goal

Replace bloated context windows with a queryable second brain that:
- **Captures** every session automatically (L1 episodic-memory plugin)
- **Distills** sessions into learnings (L2 sovereign.db via episodic_ingest)
- **Surfaces** in Notion as a human-browsable dashboard (L3 Intellectual Library)
- **Retrieves** via a single unified facade across all stores

---

## 📚 The Three Layers

| Layer | What | Where | Query |
|-------|------|-------|-------|
| **L1** | Full conversation history (mechanical capture) | `~/.config/superpowers/conversation-index/db.sqlite` | `memory_facade.py --sources episodic` |
| **L2** | Distilled rules & voice (human-reviewed) | `.memory/sovereign.db` | `memory_facade.py --sources sovereign` |
| **L3** | Browsable knowledge + session logs | Notion Simon Library + local mirror | Open Notion hub or `/library-*` skills |

---

## 🚀 How to Use

### Query Past Sessions (Facade)
```bash
# Find a past conversation about "episodic memory integration"
python3 execution/memory_facade.py "episodic memory integration" --top 10

# Narrow to episodic (L1 only, fast)
python3 execution/memory_facade.py "topic" --sources episodic

# All stores (sovereign + automem + wiki + agents + episodic)
python3 execution/memory_facade.py "topic" --top 10

# JSON output
python3 execution/memory_facade.py "topic" --json
```

### Push a Session to Notion
```bash
# Manually log a session with key decisions + pickup
python3 execution/notion_api.py session-memory "Session Title" \
  --decisions "What we decided" \
  --pickup "What's next"

# Example:
python3 execution/notion_api.py session-memory "Memory System Integration Complete" \
  --decisions "Verified episodic capture + facade retrieval + Notion push" \
  --pickup "Run episodic_ingest weekly to promote sessions to semantic tier"
```

### Run the Weekly Distillation Loop (Full Pipeline)
```bash
# 1. Extract new sessions from episodic index → sovereign.db
python3 execution/episodic_ingest.py preview      # dry-run (default)
python3 execution/episodic_ingest.py run          # write

# 2. Embed new episodic rows for semantic similarity
python3 execution/memory_embed.py

# 3. Propose semantic rules from episodic clusters
python3 execution/memory_distill.py preview       # see proposals
python3 execution/memory_distill.py run           # write to flagged_review

# 4. Human review — approve/reject promotions
python3 execution/memory_review.py
```

---

## 🔑 Key Files & Their Jobs

| File | Job |
|------|-----|
| `execution/memory_facade.py` | **Single retrieval entry.** Query any store via one call. Never writes. |
| `execution/episodic_ingest.py` | **L1→L2 bridge.** Reads recent exchanges, summarizes sessions, stores in sovereign.db. Idempotent. |
| `execution/memory_embed.py` | Embed episodic rows (separate from ingest to avoid surprise LLM cost). |
| `execution/memory_distill.py` | Cluster episodic entries + propose semantic rules via Gemini (WITH human gate). |
| `execution/memory_review.py` | **Human gate.** Approve/reject proposed rules before they enter always-loaded semantic tier. |
| `execution/notion_api.py` | Write to Notion Session Memory DB (allow-list: Title/Date/Mode/KeyDecisions/Pickup). |
| `.memory/sovereign.db` | L2 semantic store. Fed from L1, human-reviewed before promotion. |
| `~/.config/superpowers/.../db.sqlite` | L1 episodic index. 413 project-scoped exchanges. Read-only via facade. |
| Notion Simon Library Hub | L3 browsable second brain. Knowledge Entries + Experts + Sources + Skills + Session Memory. |

---

## 🛡️ Privacy Boundary

| Layer | What flows | What stays local |
|-------|-----------|------------------|
| **L1→L2** | Sessions + PII-redacted summaries | Raw transcripts never stored in semantic |
| **L2→L3** | Distilled decisions only (allow-list) | Client content + personal context NEVER pushed |
| **L3** | Notion hub (integration-owned DBs) | Manual Notion "Personal Context" DB only for sensitive material |

**Rule:** If it contains client names/details or personal material, it stays in local-only tiers. Nothing auto-flows to Notion.

---

## ⚙️ Technical Notes

- **episodic-memory plugin** (superpowers v1.0.15): 413 project exchanges indexed. SessionStart hook fires at every session. No ungated spend. ✅
- **claude-mem NOT installed**: Would add ungated API calls (~$0.05/session). Violates cost-gate principle. Bake-off decision locked in `_active/memory-bakeoff/`. ✅
- **Notion integration gotcha solved**: AI-made DBs use data-source model (linked views); integration can't write. Fix: integration creates its own classic DB under hub. See `reference_notion-ai-database-integration-gotcha.md`. ✅
- **No new 8th memory store**: episodic-memory IS the capture layer. No manual episodic logging needed. ✅

---

## 📊 Current State

- **L1 episodic**: 413 project exchanges indexed, queryable via facade
- **L2 semantic**: 148 memories + 21 voice rules in sovereign.db
- **L3 Notion**: 84 Knowledge Entries + 12 Experts + 12 Sources + 12 Skills (fully seeded + verified)
- **Session Memory DB**: 38849875a89781c0950ef6a48bb28a72 (live + tested)
- **Facade**: 5-store router (sovereign, automem, wiki, agents, episodic)

---

## 🎓 Learning the System

Read these in order:
1. `project_three-layer-memory-system.md` (architecture + rationale)
2. `reference_notion-ai-database-integration-gotcha.md` (the gotcha + fix)
3. `_active/notion-intellectual-library/DEPLOY-RUNBOOK.md` (Notion setup)
4. `_active/memory-bakeoff/bake-off-protocol.md` (why episodic-memory wins)
5. This file (quick reference)

---

## ✅ Acceptance Tests (All Passing)

- **Glance**: Library shows 84 entries, 12 experts, strong Copywriting (19) + Psychology (15) lanes ✓
- **Filter**: `memory_facade.py "episodic" --sources episodic` returns past session snippets ✓
- **Refusal**: (Advisor refusal on uncovered topics — requires grounded advisors, optional Phase 3.4)
- **Session push**: `notion_api.py session-memory "test"` writes to Notion ✓
- **Idempotency**: `episodic_ingest.py run` then re-run = same results, no duplicates ✓

---

**Last Verified:** 2026-06-23 | **Phase 5 Status:** Complete | **Next:** Optional advisor deployment via Notion AI
