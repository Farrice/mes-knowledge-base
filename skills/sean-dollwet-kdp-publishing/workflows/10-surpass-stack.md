---
name: surpass-stack
description: The beat-the-market quality layer. Dollwet's window thesis says quality wins where incumbents are weak — this workflow stacks the operator's OWN expert arsenal (avatar, copy, ghostwriting, cover, content-psychology skills) onto each pipeline stage to out-produce a niche's best book. Every handoff is OPTIONAL — a choice the operator makes per book, never a mandatory step.
produces: a per-stage stacking plan (which expert handoffs to fire, which to skip) that raises one book above its niche's incumbents
expert: Sean Dollwet
load_context: genius.md
---

# Surpass Stack — Out-Produce the Niche's Best Book

## Pre-Flight Gate

**Read this first — it governs the entire workflow: every handoff below is an OPTION the operator picks, NOT a mandatory pipeline step.** The Dollwet-native pipeline (workflows 01–04) already ships a book that beats weak incumbents. This workflow is the *premium* layer for when out-executing a specific competitive niche is worth extra time and cross-skill cost. Firing all five handoffs on a validation-stage sprint book is over-investment and violates the one-week ceiling (Pattern 18). Firing zero on a taste-bearing entry into a defended niche leaves the door-close moat on the table. The operator chooses per stage.

The doctrine that earns this layer (window-thesis / Pattern 12): quality is what gets you *through* the window. "Generic AI input gives you generic AI output. And generic books do not beat the top of a niche… If you're going to skip the quality part, you might as well not even do this." But also: "if you wait, the timing is gone and quality alone won't save you." So — quality is the moat *inside* the window, not a license to over-polish past the ship date.

Run this when:
- The target niche is competitive or premium (Door B obsolescence rather than Door A empty-review — window-thesis), and beating incumbents needs more than Dollwet-native execution.
- The book is taste-bearing (the operator's brand, a flagship, a high-price niche) where a quality edge converts.
- The operator explicitly wants to stack their own skill arsenal onto a book.

Do NOT run this when: the book is a validation-stage sprint (just prove the niche converts first), the niche is a soft Door-A target (low reviews — Dollwet-native quality already wins), or the operator is pre-proof (get one book to $1k/mo the native way before adding cost). In those cases, say so in one line and route back to the native pipeline.

## Skill Acquisition

Load before executing:
- `genius.md` — Pattern 12 (review-moat door-close), Pattern 9 (three-force window — quality is what gets you through), Pattern 16 (tedium is the moat), Pattern 6 (AI drafts / human elevates); Signature Move 6 (decouple two things the audience conflates); Quality Rubric item 5 (quality-moat logic present).
- `references/window-thesis.md` — the review-moat door-close mechanic and the timing-vs-quality sequencing law.
- The genius.md files of any handoff skill the operator elects to fire (loaded only for the stages chosen — do not pre-load all five).

## Execution

For each pipeline stage, present the handoff as a choice: the cross-skill option, WHEN it earns its cost, and WHEN Dollwet-native is already enough. The operator selects; you fire only the selected ones.

### Stage 1 — Review-mining data → identity-level reader profile
- **Native (workflow 01/02):** mine competitor reviews for "loved / wish they'd covered" patterns; narrow to one problem, one audience.
- **Optional handoff → `/avatar-machine` or an ICP deep-dive.** Feed the review-mining corpus into an identity-level reader profile *before* outlining — not just a demographic but the reader's felt wound, self-talk, and buying-state. This deepens the pain-point selection (prompt-chain Prompt 2) into a genuine avatar the whole book speaks to.
- **Earns its cost when:** the niche is emotionally loaded (self-help, healing, relationships — where the second-person wound-accusation hook lives, Hidden Knowledge 12) and the winning angle is identity, not information. A sharper avatar changes title, subtitle, AND chapter selection.
- **Native is enough when:** the niche is utility/reference (air fryer recipes, a study guide) where the buyer wants a task done, not an identity mirrored. Review-mining alone suffices.

### Stage 2 — Title / subtitle / listing copy → benefit-stack beyond category norm
- **Native (Pattern 4/5):** keyword-main-title + benefit-stacked subtitle; taste-test (clarity breaks ties).
- **Optional handoff → `/copy-engine` + hook engines.** Run the subtitle and A+ listing copy through a conversion-copy pass so the benefit stack exceeds the category norm — a listing that visibly out-sells page-one peers on the buyer's cover→title→Look-Inside scan path (window-thesis door-close mechanic).
- **Earns its cost when:** the niche's incumbents have generic titles (Door B) and the operator can win share on listing copy alone; or the price sits above category norm and must *visibly* convey extra value (Hidden Knowledge 3 — a doubled price demands conveyed doubled value).
- **Native is enough when:** the Dollwet keyword+flair+benefit-stack formula already out-executes the page (most low-review Door-A niches). Don't gild a subtitle that already wins.

### Stage 3 — Manuscript → nonfiction value architecture + prose quality gates
- **Native (Pattern 6/7):** AI drafts one subchapter at a time; human humanizes, adds stories, fact-checks, Grammarly. Value = organization + time-saved.
- **Optional handoff → `nicolas-cole` nonfiction value architecture + prose quality gates.** Impose a deliberate value-per-chapter structure and a prose bar so the book *reads better than page one* of the niche — a book a reader finishes and reviews five stars, which feeds the review sprint. Run the operator's slop-ban / prose gates on the humanized draft.
- **Earns its cost when:** the book is high-content in a niche where incumbents are stale (Door B), and reading-quality itself is the differentiator that earns organic reviews and word-of-mouth. This is where "tedium is the moat" (Pattern 16) pays — competitors ship degraded AI slop; you ship a book that reads.
- **Native is enough when:** the book is a simple list/reference (dad jokes, prompts) where plain structure suffices — Dollwet says plain output can be fine there. Don't architect a joke book.

### Stage 4 — Cover direction → visual-tool routing
- **Native (prompt-chain Prompt 6):** GPT-Image/Gemini two-pass (realistic → text-forward), pick by current trend; or $10–20 Fiverr.
- **Optional handoff → `/fantastic-posters` / creative-router pre-flight.** Run the visual-tool routing pre-flight (`creative_router.py`) so the cover is directed, not just generated — winning the 3-second snap-test line-up against incumbents whose covers "look like they were designed in 2002." (Cost-gated: any paid generation is human-triggered.)
- **Earns its cost when:** the cover is the primary attack surface (Door B — dated incumbent covers) and the operator is beating the niche on the first thing the buyer sees. The cover carries the most conversion weight on the buyer's scan path.
- **Native is enough when:** a $10–20 Fiverr gig or a clean text-forward GPT-Image cover already stands out — validation-stage books don't need art direction. Never clone a competitor's design either way.

### Stage 5 — TikTok hooks → content psychology
- **Native (organic-taxonomy):** 7-type taxonomy, faceless book-showcase / one-page-read, volume game, second-person wound-accusation hooks, clone the winner 10×.
- **Optional handoff → `kallaway` content psychology.** Layer psychological hook engineering onto the text-overlay hooks so the scroll-stop rate on the volume game rises — sharper "you" wound-accusations, stronger open-loop framing (the overlay text IS the product, organic-taxonomy).
- **Earns its cost when:** the operator is running the organic engine hard (workflow 06) and marginal hook quality compounds across hundreds of videos; or the niche's emotional stakes reward a psychologically precise hook (the 70M-view Shadow Work one-page-read).
- **Native is enough when:** the format is doing the work (faceless book-showcase converts on the object, not the copy) or the operator is still in the pure-volume "buy lottery tickets" phase where cadence beats per-hook polish.

### Stage 6 — Close the door (the payoff play)
Whatever stages the operator stacked, the endgame is the same two-moat close (Pattern 12 / window-thesis): **superior quality + a fast review sprint = both moats held at once.** AI (and the stacked skills) give the quality; speed (the 90-day sprint, workflow 04) gives the reviews. An incumbent beatable on cover/title/content becomes uncompetable once you enter with quality AND stack reviews — "there's no weak spot left to attack, the door closes behind you." The surpass-stack builds the quality half; it only pays if paired with the review sprint. Name that pairing explicitly in the output.

## Content Type Adaptations

| Content tier | Highest-leverage handoff | Usually-native stage | Door-close note |
|---|---|---|---|
| **High-content nonfiction** | Stage 3 (Cole value architecture + prose gates) — reading quality earns organic reviews | Stage 4 if a clean text cover already wins | Quality half is strongest; pair with the review sprint for both moats |
| **Low-content journals/planners** | Stage 4 (cover/visual routing) + Stage 5 (hooks) — design and scroll-stop carry it | Stage 3 (little prose to architect) | Beat on aesthetics + reviews; content isn't the lever |
| **Medium-content coloring/activity** | Stage 4 (visual routing — model Coco Wyo trend) | Stages 1–3 | Trend-current design + review base = the moat |
| **Emotionally-loaded self-help** | Stage 1 (avatar) + Stage 5 (content psychology) — identity is the angle | Stage 2 if the keyword formula already wins | Wound-accusation hooks + a book that reads = door closes hard |

## Output Requirements

Deliver a **surpass-stack plan** containing:
- **The explicit framing line:** these handoffs are options for THIS book, not mandatory steps — stated up front.
- **Per-stage decision:** for all five stages — FIRE (which skill) or SKIP (Dollwet-native), each with a one-line reason tied to the niche's attack surface (Door A vs Door B) and whether the book is taste-bearing vs sprint.
- **For each FIRED handoff:** the specific deliverable it produces and how it out-executes the named incumbent(s) on that stage of the buyer's scan path.
- **The door-close pairing:** an explicit statement that the stacked quality only converts to a moat when paired with the 90-day review sprint (workflow 04) — quality half + reviews half = both moats.
- **A cost/time honesty line:** the added time each fired handoff costs, checked against the ship-date discipline (don't blow the window polishing).

## Quality Gate (pass/fail — references genius.md Rubric + anti-patterns)

- [ ] The output states explicitly that every handoff is OPTIONAL — the operator's choice per book, never a forced pipeline step.
- [ ] Each stage carries a FIRE/SKIP decision with a reason tied to the niche's attack surface and taste-bearing-vs-sprint status — no blanket "do all five."
- [ ] Sprint / validation-stage / pre-proof / Door-A books are steered toward SKIP (native), protecting the one-week ceiling and the $1k-first-proof sequence.
- [ ] Every FIRED handoff names the specific incumbent weakness it out-executes on the buyer's cover→title→Look-Inside→content path (Rubric 5).
- [ ] The door-close pairing is explicit: stacked quality is only a moat when paired with the review sprint (Pattern 12) — quality alone is named as insufficient.
- [ ] Added time is checked against the ship date — "if you wait, the timing is gone and quality alone won't save you"; no over-polishing past the window.
- [ ] Handoff skills are loaded only for the stages actually fired — no pre-loading all five (context discipline).
