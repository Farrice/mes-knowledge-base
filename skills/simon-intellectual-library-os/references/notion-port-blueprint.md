# Notion Port Blueprint — The Antigravity Intellectual Library

The mapping from Simon's architecture to Farrice's Notion. This is the design source for `/library-notion-port` and the deployment prompt pack in `_active/notion-intellectual-library/`.

## The problem this solves

Antigravity's Notion logs are append-only prose — readable to Claude, nearly unusable to Farrice. Simon's architecture makes the same knowledge **glanceable** (humans scan views/dashboards in seconds) and **searchable by lane** (agents filter by category/confidence instead of reading everything).

## Target architecture (one hub, five databases)

```
🏛 Intellectual Library (hub page — dashboard of linked views)
├── 📚 Knowledge Entries   (DB1 — the atomized library; the heart)
├── 🧠 Experts             (DB2 — the roster: who the knowledge comes from)
├── 📖 Sources             (DB3 — books/videos/courses + ingestion status)
├── ⚙️ Skills & Playbooks  (DB4 — process pages usable as Notion AI skills)
└── 💬 Session Memory      (DB5 — chat-history entries for cross-session context)
plus: 📋 Advisor Instructions (pages — one per specialist, each with a grounding gate)
plus: 🧭 Context Map (page — who-Farrice-is + map of key databases, loaded by advisors)
```

### DB1 — Knowledge Entries (properties)
Title · Type (Principle/Framework/Case Study/Example/Quote/Pattern/Study) · Category (Content, Copywriting, Brand, Buyer Psychology, Storytelling, Systems & AI, Audience Growth, Offers & Pricing, Personal/Voice) · Key Insight (text, 1-2 sentences) · When to Apply (text) · Confidence (Proven/Tested/Untested) · Expert (relation→DB2) · Source (relation→DB3) · Linked Entries (self-relation) · Status (Active/Needs Review/Deprecated) · Date Added.
**Views**: By Category · By Confidence · Board by Type · By Expert · Recently Added.
Page body uses the entry template (What it is / Why it works / How to apply / Examples / Connections).

### DB2 — Experts
Name · Domain · Tier (A/B/C) · One-line Genius · Skill Path (local `skills/...` pointer) · Entry Count (rollup from DB1) · Status.
This mirrors AGENT_INDEX.md — the Notion-glanceable roster.

### DB3 — Sources
Title · Type (Book/Video/Course/Article/Podcast) · Author/Creator · URL · Ingestion Status (Not Started/Mapped/In Progress/Complete) · Chapter Map (page body) · Date Ingested.

### DB4 — Skills & Playbooks
Name · For Advisor (relation) · Trigger ("use when…") · Status. Page body = the step-by-step playbook. In Notion these are configured as actual AI skills (page → Use with AI → use as skill).

### DB5 — Session Memory
Title · Date · Advisor/Mode · Key Decisions (text) · Pickup Prompt (text). Simon's chat-history pattern — Notion's substitute for cross-session memory.

### Advisor Instruction pages (the grounded board of advisors)
One page per specialist. Required sections, in order: Purpose & north star → **Mandatory entry gate: "Before answering anything, read your linked Knowledge Entries view (filtered to your categories)"** → linked DB1 view (filtered) → boundaries & handoffs → working method (classify → read KB → invoke skill → apply → validate) → anti-drift rules → memory notes. One page max; token-slimmed.

### Global instructions page
Orchestration layer listing all advisor modes: what it does / when to pick / when NOT to pick. New advisors get registered here (Simon's "mode" table pattern).

## Mapping Antigravity → Library

| Antigravity asset | Library destination |
|---|---|
| `extractions/*/extraction-report.md` genius patterns | DB1 entries (Type=Pattern, Expert linked, Confidence=Tested) |
| `skills/*/genius.md` hidden knowledge | DB1 entries (Type=Principle) |
| Hall of Fame exemplars | DB1 entries (Type=Case Study/Example) |
| Source videos/books per extraction | DB3 rows |
| Skill workflows | DB4 playbooks (selectively — only ones useful inside Notion) |
| AGENT_INDEX.md roster | DB2 rows |
| Chain Step 6 finalize logs | DB1 entries when they contain a reusable lesson (Type=Pattern, Category=Systems & AI) — otherwise stay in the log DB |

**Bridging rule** (from `/library-extraction-bridge`): an extraction is NOT copied wholesale. Each genius pattern/hidden insight becomes ONE atomized entry with When-to-Apply and Confidence. 16 patterns = 16 entries, glanceable, filterable.

## Maintenance loops (port of his loops)

- **Compounding**: any Notion AI answer worth keeping → saved as DB1 entry (Confidence=Untested) or DB5 session memory.
- **Monthly health check**: a DB4 skill page implementing the 7-stage audit over DB1 (contradictions, orphaned relations, missing sources, unbridged extractions, stale >90d, writing-rule violations, suggested new entries + undrawn links). Triggered manually in personal-agent chat (economic routing — no scheduled credit burn).

## Build paths (two options)

1. **Notion AI builds it** (Simon's way, recommended — it exercises the system immediately): paste the deployment prompts from `_active/notion-intellectual-library/notion-ai-deployment-prompts.md` into Notion AI (best model available, e.g. Claude Opus-class).
2. **Claude builds it via Notion MCP/API**: `execution/notion_api.py` (pinned 2022-06-28) creating the DBs directly — deterministic but skips Notion AI's native view/dashboard assembly. Use when Notion AI access is unavailable.

## Acceptance tests (port-specific)
1. Glance test: Farrice opens the hub and can state library size, strongest lanes, weakest-confidence areas in <30s.
2. Filter test: an advisor answers a question by filtering Category + Confidence, citing entries by name.
3. Refusal test: a freshly-created advisor with an empty filtered view says so instead of answering generically.
