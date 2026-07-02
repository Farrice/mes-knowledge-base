---
description: Build the avatar-language answer key — the qualified-survey engine plus the three-page, word-capped Offer Optimizer grid — so every piece of content, copy, and collateral is written in the perfect client's own words before a single line gets drafted.
tier: atom
expert: john-whiting
stacks_with: [luke-iha, april-dunford]
---

# The Offer Optimizer — Get the Answer Key, Stop Guessing

> "It's like if you're going to go take a test, you have two options. You can study real hard and guess... or you can just go to the teacher and get the answer key. This is the answer key to attracting your perfect ideal client." — John Whiting

`jw-one-best-client` extracts ONE person's language from history. This workflow industrializes it: an always-on survey engine that harvests the qualified collective's words at every opportunity, compressed into a three-page document with hard word caps that the operator re-reads before creating ANYTHING. Genius patterns #21 (Qualified-Survey Engine) and #22 (Offer Optimizer), built on #12 (One Best Client) and the "sell them what they want, give them what they need" philosophy.

---

## Pre-Flight Gate

1. **Is there a One Best Client on file?** The optimizer is seeded from their onboarding form, call transcripts, and DMs (Whiting built his entire document from Justin Saunders's 4-year-old onboarding form). No named best client → run `jw-one-best-client` Step 1–2 first, then return.
2. **Is there a list or audience to survey?** The engine needs respondents — an email list, a client base, a warm following, even a small one. Zero audience → seed from the One Best Client's artifacts alone and mark the survey layer as "install at first promotion."
3. **Will the operator enforce qualification filtering?** The whole edge is optimizing copy ONLY for qualified respondents ("I don't want to optimize my copy and positioning for people that aren't qualified"). If every response gets averaged in, the language bank regresses to the broad market and the document optimizes for people who can't buy.
4. **Run `jw-ethics-gate` intent check.** Their words get regurgitated back to them — the mechanisms and outcomes attached to those words must be real, deliverable, and defensible under oath. Using their pain language to sell something that doesn't fix the pain fails gate #3.

If all four pass, build.

## Skill Acquisition

Load `genius.md` (full). Core patterns: **#21 The Qualified-Survey Engine**, **#22 The Offer Optimizer**, seeded by **#12 One Best Client**. Supporting: Core Philosophy #4 (*sell what they want, give what they need* — the grid's desire language is the bait; the mechanisms are the switch) and Hidden Knowledge *"you can't say the right things to the wrong people, and you can't say the wrong things to the right people."* Honor the **VOICE REFERENCE** (word caps keep it punchy, Mode A/B decides the edge) and the **ETHICS GATE**.

---

## The Build (6 steps)

### Step 1 — Install the survey instrument
One form (Typeform/Jotform/Google Form), deployed at every promotion, onboarding, and launch, incentivized ("fill this out and get the discount / priority access / bonus"):
- **Identity:** name, email, phone.
- **Radio-button qualifiers:** the 1–2 fields that separate qualified from not (Whiting: business type + revenue level). These exist so you can FILTER, not to be polite.
- **Three long-form text questions** — their typed words, verbatim: (1) *"When it comes to [big goal], what are your biggest goals?"* (2) *"...what are your biggest challenges?"* (3) *"What are the top 3 things you want to learn as it relates to [big goal]?"*

### Step 2 — Filter, then compress
Cut every unqualified response BEFORE synthesis. Dump the qualified set into an LLM: *"Extract the most frequent verbatim phrases for desires, challenges, and learning wants. Preserve exact wording — no paraphrase, no marketing-speak. Rank by frequency."* Output = the **collective language bank**, merged with the One Best Client's verbatim phrases (their words outrank the collective's on ties — the document is optimized around one person, and the collective corroborates).

### Step 3 — Page 1: the offer grid (word caps are load-bearing)
Fill gray cells only with bank language:
- **Big desire, ≤4 words.** (His: "seven figure freedom.")
- **Top-3 obstacles** standing between them and it — their phrasing ("no time," "stressed out," "inconsistent profit").
- **Each obstacle flipped into a want** — caps ~6/3/4 words, "punchy, concise" ("a business that runs on autopilot," "peace of mind every day," "wealth growing every month").
- **Per want: a named mechanism → outcome → benefit**, and every chain must flow visibly back to the big desire. A mechanism that doesn't ladder up to the ≤4-word desire is a feature, not an offer component — cut or re-chain it.

### Step 4 — Page 2: you and the company
The identity layer the content communicates on repeat: your **north-star question** (his: "what does the data say to do?"), **what you're known for**, **mission**, **vision**, your **thesis/main argument** (his: knowledge gets you to six figures; wisdom gets you to seven-figure freedom), **what you're FOR and what you're AGAINST** (the polarization spec — repel lines live here), and **credibility** (real, verifiable — Ethics Gate #2). This page is why the same beliefs show up in every asset: it's re-read before each one.

### Step 5 — Page 3: avatar motivations, now/future
A 2×2 in their words: what they **want today** / are **frustrated by today** / **fear will happen tomorrow** if the frustrations continue / **aspire to tomorrow**. Collateral rule: lead with today (the felt problem), sell tomorrow (the aspiration + averted fear). "First we fix the offer today, so you avoid those fears and get those aspirations tomorrow."

### Step 6 — Install it as the answer key
The document is not a deliverable that gets filed — it's a pre-write ritual: *"Every time I make a piece of content, I review this document and I know who I'm talking to. I'm only talking to Justin four years ago."* Wire it into the operator's content SOP (and, if the propaganda machine is running, into `jw-objection-arsenal` + `jw-content-cadence-engine` as the language source). Refresh the language bank at every survey deployment; re-run the grid when the One Best Client changes.

---

## Content Type Adaptations

| Deliverable | How the optimizer adapts |
|---|---|
| **Coaching / high-ticket offer (Authority Flywheel)** | Hero use case: the grid IS the offer architecture — desire, flipped wants, named mechanisms, benefit chains — and the sales page is assembled from its cells almost verbatim. |
| **LinkedIn-native (× Lara Acosta)** | Page 3's "frustrated today" cells are the hook bank; Page 2's for/against is the polarization line in every post. The ≤4-word big desire becomes the profile tagline test. |
| **Newsletter / Substack (× Nicolas Cole)** | The three survey questions run as a reader survey each quarter; subject lines come from the "want today" column; the thesis (Page 2) is the publication's through-line. |
| **Paid ads (× Luke Iha)** | The language bank feeds hooks directly — their words convert because they wrote them. Word caps map cleanly onto ad-headline constraints; the mechanism names carry the curiosity load. |
| **Client work (Mode B)** | Build the client's optimizer from THEIR best client + THEIR survey — never transplant your own language bank. Spine test every for/against line before it ships publicly. |

## Output Requirements

Deliver an **Offer Optimizer Pack**:
1. **The survey instrument** — fields, qualifiers, the three long-form questions phrased for this operator's market, the incentive, and where it deploys.
2. **The language bank** — qualified-only, verbatim phrases ranked by frequency, One Best Client phrases flagged.
3. **Page 1 grid** — big desire (≤4 words), 3 obstacles → wants (capped), mechanism/outcome/benefit chains, each chain's line back to the desire shown.
4. **Page 2** — north-star question, known-for, mission, vision, thesis, for/against, credibility (verifiable claims only).
5. **Page 3** — the now/future motivation 2×2.
6. **The install rule** — where the pre-write ritual lives in the operator's process, and the refresh cadence. **Ethics Gate sign-off.**

## Quality Gate

Score against the genius.md rubric (1–10). Load-bearing dimensions:
- **Reverse-engineered? (#2)** — Every cell traces to a verbatim source (survey response, onboarding form, transcript). A cell the operator "wrote because it sounded right" is a guess wearing the answer key's clothes — fail.
- **Self-selecting? (#4)** — Page 2's for/against must actually repel. If the AGAINST column reads like generic values ("we're against mediocrity"), it filters no one.
- **Edge intact? (#5)** — Word caps force punchy, but punchy ≠ sanded. Run the spine test on the for/against lines and the flipped wants.
- **One big domino? (#8)** — The thesis (Page 2) and the big desire (Page 1) must be the same belief seen from two sides. Two unrelated stories = two documents fighting.
- **Ethics Gate passed? (#7)** — Mechanisms deliver what the desire language promises; credibility claims are real; no pain language borrowed to sell an unrelated thing.

**Optimizer-specific failure modes:** skipping the qualification filter and averaging in broke respondents (fails #4 — you optimized for people who can't buy); paraphrasing survey language into marketer-speak (destroys the only asset the survey produced); blowing the word caps ("comprehensive" cells = template slop); building the whole thing from imagination because surveying felt slow (fails #2 outright — that's an avatar doc, not an answer key).

If any dimension <6, rebuild that step once and re-score.
