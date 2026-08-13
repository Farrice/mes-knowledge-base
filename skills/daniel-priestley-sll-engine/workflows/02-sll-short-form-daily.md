# Workflow: Short-Form Daily Batch

**Produces**: a batch of daily short-form posts (default 7 = one week), each in exactly one lane (Pain / Prize / Problem, optionally × News), each carrying a bridge to the long-form.

## Load Context

1. Read `../genius.md` (mandatory) — especially patterns 1, 4, 5, 9.
2. Read the business's SLL System Map (workflow 01). No map = run workflow 01 first, or at minimum build a mini lane bank before drafting.
3. **Voice layer (binding)**: if these post under Farrice's own name, load `_active/farrice-brand/voice/VOICE-CARD.md` + dial mode (default BLEND) before drafting.

## Steps

1. **Assign lanes across the week.** Rotate — never two consecutive days in the same lane. Scan current trending news for ≥1 lane × News multiplier this week ("the recommendation engine is always looking for trending news").
2. **Draft each post from the lane bank language**, not from scratch. The customer's own words are the targeting signal. One idea per post.
3. **Recognition math check**: the batch exists to hit 11 touches / 90 days — every post must be recognizably from the same person solving the same problem (consistent problem-space, not consistent template).
4. **Attach the bridge** to every post: comment-a-word ("Comment SCORE and I'll send you...") or pointer to the pinned long-form. No orphan posts.
5. **Prose gate**: `python3 execution/prose_classifier.py check <file>` before delivery (slop ban applies to short-form hardest).

Output step — Execution prompt: `references/prompts-v2/sll-short-form-batch.md` — honor its Output Contract.

## Output Schema

```
# Short-Form Batch — [Business] — week of [date]
| Day | Lane (×News?) | Post (full text) | Bridge |
Each post: hook line → body in buyer language → bridge CTA.
```

## Example Output (2 of 7, independent ecommerce brand)

> **Mon — PAIN**: "The expensive candle smelled perfect in the shop. At home, it turned the room into a perfume counter in twelve minutes. We made a three-question scent-strength guide for people who want atmosphere—not a headache. Comment GUIDE and we'll send it."
> **Wed — PROBLEM × NEWS**: "[Verified story about stricter fragrance-disclosure rules] More labels will not solve the real buying problem: scent names like 'midnight library' tell you nothing about how strong a candle is in a 300-square-foot room. Our room-size test is pinned on the profile."

**What makes this excellent**: Monday is pure pain-lane in the buyer's lived buying experience (stranger test passes instantly); Wednesday stacks Problem × News, names the obstacle (missing decision information, not lack of desire), and each post ends on a distinct bridge mechanic. No lane bleed or generic filler.

## Quality Gate

- [ ] One lane per post; no post is pain AND prize AND problem soup
- [ ] ≥1 News multiplier in the batch, tied to genuinely current news
- [ ] Every post has a bridge (comment-word or pinned pointer)
- [ ] A stranger could name the intended buyer from any single post
- [ ] Prose classifier pass; voice card honored if Farrice-named
