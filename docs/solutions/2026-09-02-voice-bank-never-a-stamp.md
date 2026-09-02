---
title: A verbatim voice line is a bank, never a stamp
date: 2026-09-02
tags: [voice, jen, content-system, lint, order-of-operations]
problem: Content in a client's voice degrades into a template when the system applies the client's best verbatim line to every post; three competing engines with no single front door let research, voice, and amplification fire in any order.
solution: One routable workflow with a receipt per step (LOAD → READ → RESEARCH → WRITE → AMPLIFY → CHECK → RENDER → DELIVER → LEARN), a stamp-lint that fails a week where any sentence repeats across posts, and a bank rule (each verbatim line at most once per week).
status: solved
verified_by: execution/jen_stamp_lint.py selftest; the shipped weeks 1–3 copy FAILS (close 8× across posts, "my DMs are open" 9×); the re-run week 1 PASSES
---

# A verbatim voice line is a bank, never a stamp

## The problem, as it appeared

Jen Santulan's content system had real research (a dated facts ledger, an outlier audit, a weekly pulse), a real voice source (a scraped profile plus five voice memos), and a real render path. It still produced what Farrice called "sloppy messes." Three faults were on disk:

1. Three engines claimed the pipeline (`jen-engine`, `jen-shortform-carousel-engine`, `ENGINE-V2.md`) and none was the front door. The auto-loaded client `CLAUDE.md` still encoded the voice the reset had retired.
2. Her best verbatim line ("i'm here for you. that's my job…") appeared on 9 of 9 shipped posts. The calibration log had called it "THE CTA register"; the system heard "put it on everything." That is the Coffee & Contracts failure (generic caption + local nouns) inverted: the client's own sentence as the swap-in.
3. The outlier audit (life-first hooks win; property-first flatlines) ran after weeks 1–3 were written, in a different lane. The content contradicted the research because the research came second.

## The solution

- **One front door.** `.agent/workflows/jen.md` is the order: nine steps, a receipt line after each, and the next step does not start without the previous receipt. Competing skills archived by frontmatter (`status: archived`, `superseded_by`), the listing skill demoted to `routing: long-tail` and scoped to one district.
- **The bank rule.** Verbatim lines are a bank: each drawn at most once per week, twice per month. A post with no bank line is normal.
- **Stamp-lint.** `execution/jen_stamp_lint.py <COPY.md|captions.txt>` splits posts on `### ` or `=== ` headings, normalizes sentences of six words or more, and FAILS if any sentence appears in more than one post. It WARNS when a bank line exceeds its per-file max. `selftest` sabotages both directions.
- **Mix from the extractions.** `06-system/CONTENT-MIX.md` states shares with citations (Alyssa Stalker, Enrico Incarnati, Mike Sherrard, Gemini deep research, her own outlier audit) and one hook rule: every post opens on her or the reader's situation; the house is beat 2.
- **Amplify defined.** Farrice: "enhanced and improved with our best copywriters and experts." Six expert seats critique, one pen integrates, the client-as-herself seat vetoes last.

## Why it generalizes

Any voice-driven content system with a "signature line" will drift to stamping it, because the line scores well in isolation and every generator is rewarded per post, not per week. The fix is a per-week check, not a per-post rule. Same for order: a doc that states the order is not an order; only a workflow whose steps refuse to run without the previous receipt is.

## Reuse

- Copy `jen_stamp_lint.py` for any client; edit `BANK` and the post-split regex.
- The nine-step shape (load → read → research → write → amplify → check → render → deliver → learn) transfers to any done-for-them content client.
