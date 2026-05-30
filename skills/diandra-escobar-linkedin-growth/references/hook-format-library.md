# The Hook Format Library

**Source**: Diandra Escobar's 2026 hook system — taught in her hook video (the *why*) and operationalized in her own `linkedin-hook-writer.skill` (the *how*). This file merges both.
**Companion files**:
- [hook-examples-library.md](hook-examples-library.md) — her 131 annotated hooks (44 Dense / 76 Punchy+Context / 3 Bomb / 8 Stacked) + the Width Scoring Guide
- [hook-writing-rules.md](hook-writing-rules.md) — her 40 named writing rules (cited by number throughout the examples)
**Companion to**: [genius.md](../genius.md) Patterns 19-22. Loaded by workflow [20-five-format-hook-architect](../workflows/20-five-format-hook-architect.md).

---

## The One Mechanism Underneath All Four

Every format does the same psychological thing: it opens a **gap** between what the reader expects and what you're claiming. That gap is curiosity. Curiosity is the click.

> "The format is just packaging. The gap is the engine. If your hook doesn't open a gap, no format will save it. If it opens a real gap, even a weak format will work."

The hook has **one job with humans**: get the "see more" click. Not summarize. Not explain. Not set up the post. And **one job with the algorithm**: 360 Brew reads your first 40-50 words *before* deciding distribution and tracks whether people *stop and read*. When a hook fails, human curiosity and algorithmic reach die together.

There are **four core formats** (plus Hybrid once you've mastered them). Every hook uses exactly one.

---

## Sizing: Pixel-Width *Is* the Truth — Character Limits Are How You Hit It

This is the reconciliation most people miss. The video says *"don't count characters, LinkedIn renders by pixels."* That's the **mental model** (the *why*). Her actual skill operationalizes it two ways, because an AI can't see pixels but can count:

**1. The Width Scoring Model (the real pixel math)** — each character has a horizontal footprint. One mobile line ≈ **110 width units** before it wraps. Score every hook line with this and you know how it actually renders. Full table in [hook-examples-library.md § Width Scoring Guide]; the load-bearing values:

| Char class | Width | | Char class | Width |
|---|---|---|---|---|
| `i l 1 ! . , ; : ' j f t r` | 1.0 | | Uppercase regular `A-H K N-V X-Z` | 2.6 |
| Space | 1.2 | | Uppercase wide `M W` | **4.0** |
| Uppercase narrow `I J L` | 1.5 | | Wide lowercase `m w` | 2.8 |
| Punctuation `- ( ) ? $ & @ "` | 1.5 | | Regular lowercase / numbers | 2.2 |

This is why `W` (4.0) eats ~4× the space of `i` (1.0), and why a 30-char ALL-CAPS line can fill a line a 90-char narrow line doesn't.

**2. Character ceilings (the fast guardrails)** — practical limits that approximate the width budget per format (below). Use these for speed; use width-scoring when a line is borderline.

**Universal limits** (apply to all formats):
- **Max total hook: 210 characters.** Over 210 is too long.
- **Max single line: 75 characters.** Lines over 75 wrap awkwardly on mobile.
- **Line breaks count as a full visible line** — adding one costs an entire line of the 3-line above-the-fold window. A line break is a major formatting decision, not a cosmetic one.
- For posts **>300 characters**, end the hook with `?`, `:`, `…`, `.`, or `...` so the truncation feels intentional.

**Final check is always visual**: paste into a mobile post-previewer (Diandra uses Cleo's), check *mobile first* (mobile-optimized ⇒ desktop-optimized, not the reverse). A blank canvas (Notion/Docs) lies about how it renders in-feed.

> **Note on the examples file**: the 131 real-world hooks in [hook-examples-library.md] are often *longer* than these generation ceilings — they illustrate *format and principle*, not target length. The character limits here always override example lengths when *generating* a hook.

---

## Format 1 — DENSE

**Shape**: All visible lines used as continuous text, no line breaks. Maximum information per pixel. Packs a complete tension loop into the visible space — enough context to feel the stakes, not enough resolution to move on.

**Use when**: The hook *needs context to land* — a data point, a story setup, or a claim that requires a full sentence. Best for technical/data-driven/proof-heavy content (algorithm changes, research, launches, contrarian takes). Lean here for **text-only posts**.

**Rules**:
- Length: **140–160 characters total.** No exceptions either end.
- **Zero line breaks.** Continuous text only.
- Must span 2–3 visible mobile lines (what 140+ chars produces).
- Under 140 chars = not Dense. **Rewrite longer, don't relabel.**

**Example** (her skill):
> An 8k-follower account hit 58,666 impressions on a post our designer begged us not to ship. The reason has nothing to do with design.

---

## Format 2 — PUNCHY + CONTEXT  *(the workhorse, highest hit rate)*

**Shape**: Line 1 = a bold short claim or pattern interrupt → blank line → Line 2 = the rehook (parenthetical, teaser, or reason to keep reading). Line 1 creates a reaction; the line break is a micro-pause; Line 2 promises the payoff is behind "see more."

**Use when**: Default here unless the idea clearly wants another shape. Best for contrarian takes, hot openers, headline-style first lines. Strong for text-only and strong-media posts.

**Rules**:
- Two lines separated by a real blank line (never a slash or same-line text).
- **Line 1 ≤ 50 characters. Line 2 ≤ 50 characters.** Over 50 = format broken → rewrite shorter or change format.
- **Rotate sub-variants** across a hook set — never use the same one for every Punchy+Context hook.

**Sub-variants** (rotate, don't repeat):
- **Plain** — Line 2 is a direct teaser/claim, no special treatment.
- **Parenthesis wrap on Line 2** — wrap Line 2 in parens to make it a quiet aside/self-aware admission. Best when Line 2 is a confession or contradiction.
- **Strategic ALL CAPS on one word in Line 1** — one high-stakes word capitalized for weight. One word per hook, never a whole line.
- **After-Stack Setup** — both lines are setup (no punch/rehook split). Each begins "After [cost/sacrifice/obstacle]…" and ends with trailing dots. Best when media is attached.

**Mechanic**: Line 1 **provokes**. Line 2 **earns the click**. The most common failure is an overloaded Line 1 that explains, summarizes, AND hedges — it kills the gap.

**Example** (her skill):
> We deliberately made a client post look ugly.
>
> 58,666 impressions. (Our designer was pissed.)

---

## Format 3 — SINGLE-LINE BOMB

**Shape**: One short, charged sentence, then "see more" cuts in almost immediately. Maximum curiosity gap. An incomplete thought the brain can't leave unfinished.

**Use when**: Only when the line is genuinely strong enough to stand alone — a take too good to dilute. High risk, high reward; when it lands, it lands hardest. Lean here for **strong-media or video posts** (the media is the second layer of unresolved context).

**Rules**:
- Length: **≤ 50 characters total.** One line, zero line breaks.
- Over 50 = not a Bomb. **Rewrite shorter, don't relabel.**

**Bomb-check**: if you're not nervous it's too bold, it's probably not bomb-grade — downgrade to Punchy+Context and leave the bomb slot empty.

**Example** (her skill):
> SEO has been dying since 1997.

---

## Format 4 — STACKED QUOTES / LIST HOOK

**Shape**: 2–3 short lines, each on its own visible line separated by blank lines, forming a pattern the reader wants to see broken or completed. Triggers completion bias; the implied contrast between entries creates tension without stating it. **Not free-form — must follow a sub-variant.**

**Use when**: The idea is naturally a *series* — before/after, escalating numbers, parallel regrets, jargon stacks.

**Rules**:
- 2–3 lines, each ≤ **60 characters** (looser than Punchy+Context to allow dates/metrics) — *except sub-variant E lines ≤ 50.*
- 2-line versions: contrast / before-after. 3-line versions: problem-cost-twist or problem-problem-solution where line 3 forces the click.

**Sub-variants** (pick one per hook):
- **A. Before/After Timeline** — two compressed lines: `[year]: [state]. [metric]. [one emotional phrase].` Power is in the compression; no explanation of *how*, just the gap. *(e.g. "2023: 0 followers. $0 made. Felt invisible. / 2026: 317k followers. $2M+ made. Forbes featured me.")*
- **B. Parallel Regret Stack** — 2–3 lines, same grammatical structure, each naming an avoidance behavior + a one-word emotional cause.
- **C. Data-Question Opener** — a question pointing to attached visual data; line 2 delivers the buried insight. **The only format where a question mark is allowed**, and ONLY when a chart/graph/infographic is attached.
- **D. Stacked Jargon Repetition (Cut-Off)** — three lines, identical structure, in-group terminology (TOFU/MOFU/…), third line cuts off before completing.
- **E. Problem-Cost-Twist (3-line)** — line 1 problem, line 2 cost/contradiction, line 3 payoff/reveal. Each ≤ 50 chars. Best for product/case-study/contrarian; worst for emotional narrative (rhythm feels mechanical).

**Dies when**: the lines are random. Each must be part of a predictable series — if the reader can't predict the rhythm, the structure fails.

---

## Format 5 — HYBRID / CUSTOM

Once the four are internalized, you stop thinking in templates and think in **tension** — shaping a gap and letting structure follow. **Earned, not for beginners**: master the four first, then break the rules on purpose because you know why they existed.

---

## Rewrite Before Relabel

When a hook violates its format's length rules, the default is **rewrite to fit**, not relabel to another format. Relabeling is a last resort (only when the hook genuinely can't be expanded/compressed without padding or losing the angle). After 2 failed rewrites, **drop it** and write a different hook on a different angle. The user never sees "OVER LIMIT" warnings, "reclassified" labels, or broken counts — only the final valid set.

---

## Register & Tone (match to the author's voice)

- **Formal / B2B** (standard capitalization, data-first): thought leaders in SaaS, GTM, SEO, marketing strategy (Jake Ward, Anthony Pierri, Maja Voje). Best for data, frameworks, evidence-backed contrarian takes. **Default register.**
- **Informal / social-native** (fully lowercase, intimate): creators/personal brands whose audience expects authenticity over polish (Sophie Miller, Lara Acosta product posts). Best for vulnerability, POV, behind-the-scenes, personal announcements.

**Rule**: never apply lowercase unless the author's voice is consistently informal — lowercase in B2B reads as careless; formal caps in a personal brand reads as stiff. When in doubt, match the post body's register. **Explicit user capitalization preferences always override.**

---

## Post-Type Hook Angles

| Post type | Hook from… | Reader's question | Never… |
|---|---|---|---|
| **Data / framework** | most surprising number, counterintuitive claim, or reframe | "does this apply to me?" | lead with methodology |
| **Personal narrative** | emotional contrast, unexpected cost, before/after gap | "have I felt this too?" | lead with credentials |
| **Sponsored / partnership** | pre-empt skepticism via disclaimer parenthetical / identity disclaimer | "is this just an ad?" | open with the brand/product name |
| **Announcement / launch** | origin story, problem it solves, anti-hype admission | "why does this exist?" | open with "I'm excited to share" |
| **Thought leadership / opinion** | most contrarian or specific claim; "Hot Take:"; result credential | "do I agree?" | open with a hedge |

---

## Media → Format Bias (length rules stay fixed)

- **Text-only**: hook carries everything → Dense or Punchy+Context.
- **Strong media (image/video/infographic)**: image adds a second unresolved layer → Single-Line Bomb or Punchy+Context; leave more unresolved.
- **Data viz (chart/graph/table)**: Format 4C (Data-Question Opener); prime the reader to look at the image first.
- **Video**: hook competes with the autoplay thumbnail → Single-Line Bomb or short Punchy+Context; give the video context, not a summary.

---

## Hard Bans (non-negotiable)

1. **No questions in hooks** — they invite mental answering and scroll-on. Statements/incomplete thoughts force the click. *Only exception: Format 4C with data viz attached.* (Rule 9)
2. **No em dashes** — use commas, periods, semicolons, colons, or rephrase. *(Aligns with Farrice's own AI-tells ban — this is a natural stacking point.)*
3. **No emojis** in hooks.
4. **No banned LinkedIn clichés**: "game-changer," "deep dive," "let that sink in," "read that again," "this changed everything," "they called me crazy," "here's the thing," "the truth is," "then it hit me," "I'm excited to share."
5. **No filler**: actually, basically, very, just, really, literally, honestly.
6. **No stranger-blind hooks** — the hook must work for someone seeing the post for the first time, with no idea who the author is.
7. **Never fabricate** numbers, stats, or claims. No real data point → use a different angle. (Rule 11)

---

## The Wallpaper Effect (why the right format keeps changing)

Psychology always wins. When a format gets too consistent across the feed, the eye treats it as **wallpaper** and stops registering it. That's why what works keeps shifting: 2023 ≠ 2024 ≠ 2026. Dense hooks emerged *because* everyone saturated Punchy+Context. **A two-year-old hook playbook isn't just outdated — it's actively hurting you.** Watch what the feed over-uses and lean into the format that breaks the pattern.

---

## Format-Selection Cheat Sheet

| If the idea is… | Use | Because |
|---|---|---|
| A claim needing context / a data setup | **Dense** (140–160) | Stakes need the full sentence to land |
| A clean hard claim with a twist | **Punchy + Context** (lines ≤50) | Workhorse; the blank line opens the gap |
| A single line too good to dilute | **Single-Line Bomb** (≤50) | High variance; lands hardest |
| A series (before/after, escalating, list) | **Stacked** (lines ≤60) | Symmetry + implied final line = the click |
| You've mastered all four | **Hybrid** | Think in tension, not templates |

**Always, every format**: (1) Is there a real gap? (2) Does it pass the character ceiling AND width-score on *mobile*? (3) Does the first/only line provoke rather than explain? (4) For bomb/stacked, are the manual line breaks correct? (5) Does it obey the hard bans?
