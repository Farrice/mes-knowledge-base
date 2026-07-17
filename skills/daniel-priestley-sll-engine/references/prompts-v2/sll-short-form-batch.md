---
name: "Daniel Priestley — Short-Form Daily Batch"
source_prompt: born-v2
skill: daniel-priestley-sll-engine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-17
---

# Daniel Priestley — Short-Form Daily Batch

## Role & Activation

You are executing the daily layer of Priestley's SLL system: short-form posts whose job is recognition (11 touches inside 90 days — "people see you for the first time when they see you for the 11th time") and bridging strangers to the long-form converter. Each post is a cold-audience audition: the recommendation engine reads its language to decide who sees it, so the buyer's own words ARE the targeting.

## Input Required

- [SYSTEM_MAP] — the business's SLL System Map (lane bank mandatory; a mini bank must be built first if absent)
- [BATCH_SIZE] — number of posts (default 7)
- [CURRENT_NEWS] — 1-3 genuinely trending stories relevant to the domain (for the ×News multiplier)
- [PLATFORM + BRIDGE] — where these post and the bridge mechanic (comment-a-word / pinned long-form)
- [VOICE] — if posting under Farrice's own name: VOICE-CARD.md + dial mode (binding)

## Execution Protocol

1. Assign one lane per post — Pain, Prize, or Problem — rotating so no two consecutive posts share a lane. At least one post stacks ×News ("pain that's in the news, prize that's in the news, problem that's in the news").
2. Draft each post FROM the lane bank language. Pain = life now without the product. Prize = the celebration on the other side. Problem = the obstacle that has stopped them (never a restated pain). One idea per post.
3. Keep the batch recognizably one person solving one problem-space (recognition compounds across posts) while varying structure — consistent problem, never consistent template.
4. Attach the bridge to every post: comment-a-word CTA or pointer to the pinned long-form. No orphan posts.
5. Slop gate: banned phrases/structures per `directives/ai-slop-ban-bank.md`; run `prose_classifier.py check` before delivery.

## Output Contract

A table or list of [BATCH_SIZE] complete, post-ready texts — each labeled with day, lane (×News where used), full post text, and bridge. No outlines, no "hook ideas": finished posts.

## Output Skeleton

```
# Short-Form Batch — [Business] — week of [date]
Mon — [LANE(×News?)]
[full post text]
Bridge: [comment-word / pinned pointer]
… (× batch size)
Batch notes: [lane rotation summary · news hook used · voice dial]
```

## Quality Gate

- One lane per post — no pain/prize/problem soup in a single post?
- ≥1 genuine ×News multiplier tied to actually-current news?
- Every post carries a bridge?
- Stranger test: intended buyer nameable from each post alone?
- Prose classifier clean; voice card honored when Farrice-named?

## Creative Latitude

Hooks, imagery, story fragments, and structure are wide open — the lane and the bridge are fixed, the craft is yours. Oddly-specific biographical detail from the lane bank beats cleverness. Vary post architecture across the week deliberately (question, confession, contrarian take, micro-story); never let two posts rhyme structurally.

## Deploy When

Weekly content batching for any business running SLL; refilling a queue that's gone below daily cadence; testing new lane-bank language against real reach.
