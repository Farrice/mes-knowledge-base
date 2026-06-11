# The Knowledge Base Schema — Canonical Spec

The substrate-independent atom + structures. Use this when designing any library, KB, or porting between substrates.

## The Entry (atom)

| Property | Type | Rule |
|---|---|---|
| Title/Topic | text | One idea per entry. If "and" joins two ideas, split. |
| Type | select | Principle · Framework · Case Study · Example · Quote · Pattern · Study |
| Category | select | Domain search lane (e.g., Positioning, Pricing, Audience, Retention). Agents filter by lane. |
| Key Insight | text | 1-2 sentences, actionable at a glance. Not a summary of the chapter — the IDEA. |
| When to Apply | text | Trigger conditions. The property that converts reference → decision support. |
| Confidence | select | Proven · Tested · Untested. New material enters Untested until validated. |
| Source | relation/text | Book/video/study + locator. Unsourced = flagged at health check. |
| Linked Entries | self-relation | Cross-source connections ("X says something similar"). |
| Date Added | date | Feeds stale-entry detection (>90d review). |
| Status | select | Active · Needs Review · Deprecated |

## Entry body template (page content)

```
**What it is**: [the idea, 2-4 sentences]
**Why it works**: [mechanism]
**How to apply**: [concrete steps or decision rule]
**Examples**: [from source]
**Connections**: [links to related entries, including other sources]
```

## Required views (Notion) / index sections (files)

1. **By Category** — agents' search lanes
2. **By Confidence** — trust triage; what needs validation
3. **Board by Type** — shape of the library at a glance
4. **Recently Added** — what's new since last health check
5. **Hub dashboard** — linked views of all KBs + counts

## File substrate mapping (raw/wiki/outputs)

```
<parent>/                  # holds multiple KBs
  CLAUDE.md                # how KBs are created/structured here
  <kb-name>/
    CLAUDE.md              # schema, focus themes, behavior rules, health-check spec
    changelog.md           # doubles as memory: what was processed when
    raw/                   # junk drawer — never organized, md files preferred
    wiki/                  # AI-written only; index.md first, one md per topic, linked
    outputs/               # answers/briefings; presented as clickable pages; fed back in
```

CLAUDE.md must define: folder roles · entry schema · ingestion process (incl. guided mode) · the outputs rule (every question's answer is written to outputs/) · health-check spec · writing rules pointer · memory/changelog behavior · focus themes (3-5).

## Advisor instruction page (the grounding gate)

Must contain, early: purpose/north star → **mandatory step: read the linked KB view before answering anything** → boundaries/handoffs to other modes → working method (classify → read KB → invoke skill → apply → validate) → anti-drift protocol → memory/live-notes section. Keep to one page; run token-slim after drafting.

## Acceptance tests

1. **Empty-KB refusal**: real question, empty KB → agent states it cannot answer from the KB (ungrounded fallback must be labeled).
2. **Grounded answer**: post-ingestion → answer cites specific entries AND applies them to the user's actual context.
3. **Glance test**: a human can state library size, strongest lanes, and weakest confidence areas in <30 seconds from the dashboard.
