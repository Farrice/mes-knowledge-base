---
description: "Riley Brown's highest-leverage skill — batch the inbox: the agent finds every thread matching an intent, writes a voice-matched reply draft for each in Gmail, and hands back draft links. Drafts only, never send."
---

# /riley-inbox-drafts — Email Drafts at Scale (never send)

Riley's own verdict on his stack: this one "is actually the most useful." The draft-link primitive (Pattern 9), scaled to the whole inbox (Pattern 10): "I want a draft link for all of these. I don't care how many it is... a few days ago I had to respond to like 20 and it just sent me 20 draft links. All of them sound like me." The safety property that makes it work at scale: **the agent never sends — every message passes through human hands.**

## Pre-Flight Gate

Load `genius.md` first. Proceed if:
- Gmail MCP is connected.
- The intent is a real inbox job (a backlog to clear, a decline-and-pitch sweep, a set of collab inquiries).
- You accept the **hard rule**: this workflow creates drafts only. No send call, ever — even if asked mid-batch.

## Skill Acquisition

- `genius.md` — Patterns 9 (draft-link terminus), 10 (batch-the-inbox); Exemplar 3 (decline-and-pitch)
- `references/source-quotes.md` — Exemplar 3 verbatim + draft output
- Live infra: `.agent/workflows/inbox-drafts.md` (the full drafts-only procedure + Standing Corrections)
- Voice: `_active/farrice-brand/voice/VOICE-CARD.md`, BLEND dial (leaves Farrice's name)

## Execution

Run `/inbox-drafts` — the live workflow implements Riley's exact loop:
1. **Sweep.** `search_threads` with queries from the intent (date window, sender pattern, keywords). Riley's decline-and-pitch: "find all of the emails over the last two months where people have offered me a product." Page through — a batch is only as good as its recall; state it honestly ("found N, drafted N, skipped M because…").
2. **Confirm the batch** (>3 threads or anything sensitive): show Farrice the thread list before drafting.
3. **Draft per thread, in his voice.** `get_thread` for context → write the reply. Riley's decline-and-pitch shape: "politely and with a little bit of pizzazz say Decline... but then say, do you want to try our product? And give them a link." His output tone: "Talia looks sharp, but I'm going to pass on trying it for now. That said, plot twist — want to try our product instead?" VOICE-CARD BLEND + `prose_classifier.py check`; no template-speak.
4. **Create drafts, return links.** `create_draft` per thread (reply-threading). Deliver a table: recipient · subject · one-line move · draft link. Farrice edits and sends — and, like Riley, selectively kills some ("I'm actually not going to send it. That guy seemed like a harmless founder").
5. **Self-correction loop.** When Farrice corrects a pattern ("never say X"), append it to the live workflow's **Standing Corrections** in-session (Pattern 3) — the skill learns permanently.

## Content Type Adaptations

| Intent | Adaptation |
|---|---|
| Decline-and-pitch sweep | Riley's boomerang: decline → pitch ours → link; one prompt, N drafts |
| Creator/collab inquiries | personalize from the thread; scrape their public work via `/scrape-creator` when it sharpens the reply |
| Client/relationship threads | always confirm the batch first; higher care, never auto-batched |
| Single high-stakes reply | skip batch confirm; one thread, full context |

## Output Requirements

- N Gmail **drafts** (zero sends), each answering the actual thread — no generic replies wearing personalization.
- A delivery table with working draft links, verified before handoff.
- Batch recall stated honestly (found/drafted/skipped counts).
- Any correction appended to Standing Corrections.

Execution prompt: references/prompts-v2/batch-email-drafts.md — honor its Output Contract.

## Quality Gate

Zero sends (even if asked)? · Every draft thread-specific? · Voice-matched (BLEND) + slop-checked? · Recall stated honestly? · Draft links verified live? · Corrections written into the workflow, not just this chat?
