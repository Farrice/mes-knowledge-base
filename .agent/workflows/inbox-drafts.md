---
description: Batch-analyze Gmail and produce editable drafts at scale — Riley Brown's highest-leverage skill, drafts only, never send
---

# /inbox-drafts — Email Drafts at Scale

Riley Brown's verdict on his own stack: "this one to me is actually the most useful." The pattern: the agent reads the inbox, finds every thread matching an intent, writes a reply draft for each **in Gmail itself**, and hands back draft links. The human's job collapses to review-and-send. The safety property that makes it work at scale: **the agent never sends — every message passes through human hands.**

**Lineage**: `skills/riley-brown-marketing-automation/` · Gmail MCP (connected) · voice via VOICE-CARD (BLEND default).

## Usage

```
/inbox-drafts [intent]
/inbox-drafts "decline all product-trial pitches from the last 2 months, politely, and pitch ours back"
/inbox-drafts "reply to every unanswered creator-collab inquiry with a personalized response"
/inbox-drafts [single thread/contact]
```

## Steps

### 1. Sweep

`mcp__claude_ai_Gmail__search_threads` with queries derived from the intent (date window, sender patterns, keywords). Page through — a batch is only as good as its recall. List candidate threads with one-line reason each.

### 2. Confirm the batch (batch mode only)

Show Farrice the thread list BEFORE drafting when the batch is >3 threads or touches anything sensitive (clients, money, relationships). Single-thread runs skip this.

### 3. Draft — in his voice, per thread

For each thread: `get_thread` for full context → write the reply.

- Voice layer: `_active/farrice-brand/voice/VOICE-CARD.md`, BLEND dial — these leave in Farrice's name
- Personalization comes from the thread itself (what they said, what they make) — Riley's move: scrape the sender's public content when the reply benefits from knowing their work (pair: `/scrape-creator`)
- No AI-slop: `directives/ai-slop-ban-bank.md` applies; run `prose_classifier.py check` on the batch text
- Riley's caption trick applies to tone: borrow cadence from a named reference when asked, never default template-speak

### 4. Create drafts, return links

`mcp__claude_ai_Gmail__create_draft` per thread (reply-to threading). Deliver a table: recipient · thread subject · one-line summary of the draft's move · draft link. Farrice edits and sends from Gmail.

**Hard rule (Tier 2 / browser-safety analog): this workflow creates drafts only. No send call, ever, even if asked mid-batch — a send request routes back to Farrice's own hands.**

### 5. Self-correction loop (Riley's compounding move)

When Farrice corrects a draft pattern ("never say X", "always CC Y on Z"), append the rule to this workflow's **Standing Corrections** section below in the same session — the skill learns permanently, not per-conversation.

## Standing Corrections

- (none yet — first correction lands here)

## Quality Gate

- Every draft answers the actual thread (no generic replies wearing personalization)
- Batch recall stated honestly: "found N matching, drafted N, skipped M because…"
- Zero sends. Draft links verified working before handoff.
