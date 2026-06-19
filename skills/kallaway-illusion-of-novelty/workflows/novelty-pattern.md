---
description: Mine a creator's own winners-vs-losers to extract niche-specific execution rules (exact words, structures, topics) mapped to the 5 components — Apex Move 2, the calibration loop.
---

# /novelty-pattern — The Bespoke-Execution Loop

Turns a creator's own performance data into a niche-specific execution ruleset: the exact words, sentence shapes, proof types, and topics that separate their winners from their losers, each rule tagged to one of the five components. Fire this AFTER a creator has shipped ~10+ pieces using the framework and wants to know what to double down on and what to stop. The framework is one-size-fits-all; this is how you discover the bespoke half.

## Pre-Flight Gate

Load `../genius.md` if it is not already hot — you map every observed pattern back to the five components (New Reveal, Outcome Mapping / Contrast / Urgency / Bullseye Proof / Protect the Illusion), so the component definitions must be live in context.

Answer before running:

1. **Has the framework actually been in use long enough to have a clean signal?** You need a dated window where the framework was applied. Pre-framework content is noise — it contaminates the comparison. If the creator only has 3–4 in-window pieces, stop: the sample is too thin to separate signal from variance. Tell them to ship more first.
2. **Is the data attributable to the framework, not to a confound?** A post that went viral because the creator was tagged by a large account, ran an ad, or caught an unrelated trend is not evidence about the framework. Flag these and quarantine them before ranking.
3. **What is "performance" for THIS account?** Views for reach-stage accounts; saves/shares for authority accounts; comments for community; reply-rate for email; click-through for ads. Pick the metric that matches the creator's actual goal before you sort — sorting by the wrong metric extracts the wrong rules.
4. **Do you have transcripts or only metrics?** Pattern extraction is qualitative — it needs the words. Metrics alone give you a leaderboard with no diagnosis. If transcripts are missing, recover them first.

## Skill Acquisition

- Always: `../genius.md` (component definitions + the 9-criterion rubric + Apex Move 2 spec).
- Stacks with `kallaway-content-psychology` — this workflow is the **qualitative twin** of their Batched Scientific Testing. Where they A/B variables at scale and read significance, this reads the *storytelling* pattern. Run both: numbers tell you which lever moved, language tells you why. Load that skill's testing protocol if the creator wants to convert extracted rules into a controlled test.
- For converting a winner into the avatar terms that explain WHY it won, pull `kallaway-audience-obsession` (avatar payload) — bullseye-proof patterns only make sense against a known avatar.
- Sibling handoffs: feed extracted rules forward into `./novelty-forge.md` (the rules become its constraints) and `./novelty-campaign.md` (rules scale across the funnel).

## Execution

### 1 — Assemble the data set (tool-agnostic)

The method does not depend on any single tool. Three valid sources, in order of convenience:

- **sandcastles.ai CSV export.** Pull the channel, set the date range to **only the period the framework was in use**, sort by the performance metric from Pre-Flight Q3, hit Export → CSV (transcript + social data per row).
- **Sandcastles Claude MCP.** Same data, queried live — Claude pulls transcripts and metrics directly via the data pipe; no manual export.
- **Manual paste.** A table the creator builds by hand: one row per piece = `{date, hook (verbatim first 2 lines), full transcript or script, metric value, format}`. Slower, fully portable, works for any platform including email and ads.

Minimum viable set: **10 in-window pieces.** Below that, you are reading variance. Quarantine any piece flagged in Pre-Flight Q2 (confounded reach) — note it, exclude it from ranking.

### 2 — Rank and split

Sort descending by the chosen metric. Split into **winners** (top third) and **losers** (bottom third). Drop the murky middle for the first pass — the contrast between extremes is where the pattern is legible. The split is comparative, not absolute: the worst winner must clearly out-perform the best loser, or your sample is flat and you should say so rather than invent a pattern.

### 3 — Section each piece, map to the five components

For each winner and loser, break the script into its functional sections and tag each section to a component:

| Section in the script | Component it serves |
|---|---|
| Opening 1–2 lines | New Reveal + Outcome Mapping (+ Urgency if present) |
| The "you've been told X, but Y" pivot | Contrast Framing |
| The "just happened / closing window" beat | Urgency (note: present or absent) |
| The example / case / "a buddy your age" | Bullseye Proof — and which **rung** (bullseye / warm crowd / third-party) |
| The delivery register throughout | Protect the Illusion (whisper vs. crier; mascot reveals present?) |

Over a clean in-window set, winners' sections should map closer to the five components than losers'. Where a loser's section is **missing** or **mis-mapped** (a naked claim with no contrast anchor, a third-party-only proof, a hedge that takes the mascot's head off) — that absence is itself a finding.

### 4 — Pattern extraction (the exact prompt to run)

Feed the sectioned data and `../genius.md` (or the framework doc) into an LLM. AI beats humans at this specific task — pattern-detection across many documents is arguably its strongest capability. Run this prompt (vary the wording, never the structure):

> *"I am giving you N of my own [videos / posts / emails], split into WINNERS and LOSERS, each with the verbatim transcript and its performance metric. I am also giving you the framework doc they were written against (five components: New Reveal, Outcome Mapping, Contrast Framing, Urgency, Bullseye Proof, Protect the Illusion). Find the pattern in the storytelling of the WINNERS that is different from ALL the losers — go component by component: how do the winners open their New Reveal differently, how do they anchor Contrast, do they use real Urgency or skip it, what rung of the Trust Ladder do their proofs sit on, what is their delivery register. Tell me the exact words, sentence structures, and topics that recur in winners and are absent in losers. Then give me very specific instructions for what to do, and what to stop doing, moving forward. Quote real lines from my transcripts as evidence — do not generalize without a quote."*

The two load-bearing constraints in that prompt: **(a) map to components** (so the output is structural, not vibes), and **(b) demand verbatim quotes as evidence** (so the rules are grounded in what the creator actually wrote, not invented). An unquoted "rule" is a hallucination — reject it.

### 5 — Output the niche-specific execution ruleset

Convert the extracted patterns into a usable ruleset, split into DOUBLE DOWN and STOP, every rule tagged to a component and backed by a quoted line:

- **Winning words / phrases** — the recurring openers, verbs, and frames in the winners.
- **Winning sentence structures** — e.g. "winners front-load the outcome before the reveal; losers bury it."
- **Winning topics / angles** — the subject matter that lands for THIS account.
- **Winning proof types** — which rung of the Trust Ladder this audience actually trusts (often more specific than the general theory predicts).
- **Stop list** — the moves present only in losers (mascot reveals, third-party-only proof, single-job hooks, bolted-on urgency).

This ruleset is the deliverable. It becomes the constraint set for the creator's next batch and the input to `./novelty-forge.md`.

### Worked mini-example — a gutter-cleaning account (fresh; not water/root-canal)

A residential gutter-cleaning business shipped 12 short videos over 8 weeks using the framework. Sorted by saves (their goal: bookings, and saves correlate). Top third vs. bottom third surfaced this:

**A winner (147 saves):**
> "You've been told to clean your gutters twice a year — turns out the calendar isn't the problem, the *roof pitch* is. Steep roofs dump debris faster, so yours might be overflowing in 4 months while your neighbor's is fine at 12. Lady three streets over swore hers were clear, sent me a photo, two inches of shingle grit. One clean and the water stopped sheeting down her siding."

Sectioning: New Reveal = "roof pitch, not the calendar" (new angle on the oldest topic in the trade) → Outcome = "no overflow / no siding damage" → Contrast = "twice a year is wrong, pitch is the variable" (true opposite of the held belief) → Urgency = honestly skipped → Proof = "lady three streets over" (bullseye — a viewer-mimic neighbor, not a stat) → delivered low-key.

**A loser (11 saves):**
> "Did you know clogged gutters cause $X billion in home damage every year? Cleaning them regularly protects your foundation. Book your appointment today!"

Sectioning: New Reveal = none (a fact everyone has heard) → Contrast = none (naked claim) → Proof = third-party stat only → register = town crier with an exclamation-point CTA → and a soft mascot reveal in "regularly" (admits there's nothing new).

**Extracted ruleset for this account:**

| Rule | Component | Evidence |
|---|---|---|
| DOUBLE DOWN: open on a *hidden variable* ("the real problem is X, not the obvious thing") | New Reveal + Contrast | "the calendar isn't the problem, the roof pitch is" |
| DOUBLE DOWN: proof = a named local neighbor with a photo, never a national stat | Bullseye Proof (top rung) | "lady three streets over… sent me a photo" |
| DOUBLE DOWN: skip urgency on evergreen maintenance topics | Urgency | winners with no deadline out-saved the "book today" ones |
| STOP: opening on a damage statistic | New Reveal | the $X-billion line — zero novelty, sat in the loser set |
| STOP: exclamation CTAs | Protect the Illusion | "Book your appointment today!" reads as a sale, kills the whisper |
| STOP: the word "regularly" / "routine" | Protect the Illusion | signals nothing-new = mascot reveal |

The owner now writes every hook as a hidden-variable contrast, leads proof with a named-neighbor photo, and has banned the damage-stat opener and the exclamation CTA. The framework was identical to the dentist's; the *execution rules* are unique to gutter buyers — which is the whole point of this loop.

## Content-Type Adaptations

The loop is identical; the data unit, the metric, and the section map shift per asset.

| Asset | What changes in this workflow |
|---|---|
| **Short-form video script** | Data unit = the spoken transcript. Metric = views (reach stage) then saves/shares (authority). Section by the spoken beats; the hook is the first 3 seconds verbatim. The native case — Sandcastles export works directly. |
| **LinkedIn post** | Data unit = full post text. Metric = saves + meaningful comments over raw likes. Watch the **first two lines before "see more"** — that is the hook zone; extract winning truncation points, not just openers. Topics that win here skew toward contrarian-reframe of an industry belief. |
| **X/Twitter thread** | Data unit = the lead tweet + thread body separately. Metric = bookmarks + lead-tweet impressions. Winners almost always carry the whole New Reveal + Contrast in tweet 1; mine the *first tweet* pattern hardest. Proof rung tends to skew bullseye-as-self (the author's own result). |
| **Email** | Data unit = subject line + body, ranked **separately**. Subject-line metric = open rate; body metric = click/reply rate. Two extractions: subject patterns (New Reveal + Contrast compressed to ~7 words) and body patterns (where the proof rung sits). The whisper register matters most here — salesy subjects tank opens. |
| **Ad / VSL** | Data unit = the script + the hook frame. Metric = thumb-stop rate then CTR/ROAS — **not** vanity views. Extract by spend-efficiency, not reach. Urgency is the most-audited component: confirm winning-ad urgency is real, because fake urgency is also the fastest ad-account trust-burn and the fastest way to get reported. |
| **Sales / landing page** | Data unit = section blocks (headline, sub, proof block, CTA). Metric = conversion rate, section-scoped via scroll/heatmap if available. Extract which *proof block* converts (testimonial that mirrors the visitor vs. logo wall) and which headline contrast lands. Pattern is block-level, not sentence-level. |
| **Long-form article** | Data unit = title + opening + section headers. Metric = read-through / dwell time, not just clicks. Title carries New Reveal + Contrast; mine title patterns against dwell. Winners sustain the whisper across length — flag any section where a loser hedges mid-body and loses readers (the mascot reveal at scale). |
| **Ghostwritten thought-leadership** | Data unit = post text tagged by *which client voice* and which ghostwriter wrote it. Metric per the client's authority goal (saves, DMs, inbound). Extract the pattern **per voice** — the bespoke ruleset is the client's signature, the deliverable a ghostwriter hands the next ghostwriter. Cross-client patterns are framework; per-client patterns are the moat. |

## Output Requirements

Return one **Bespoke Execution Ruleset** artifact containing:

1. **Header** — account, platform, date window analyzed, performance metric used, N in-window pieces, N quarantined (with reason).
2. **Winners-vs-losers table** — each ranked piece, its metric, and a one-line section map; quarantined pieces marked.
3. **The extraction prompt actually run** (so the loop is reproducible next quarter).
4. **DOUBLE DOWN ruleset** — rules tagged to component, each with a verbatim quoted line as evidence (see worked table above).
5. **STOP ruleset** — loser-only moves, tagged and quoted.
6. **Next-batch directive** — the 3–5 rules to apply to the very next pieces, and the date to re-run this loop.

No rule ships without a quoted line behind it. If the sample was too thin or too flat to extract a real pattern, say exactly that and recommend more reps — do not manufacture rules to fill the template.

## Quality Gate

Score against `../genius.md` rubric, weighted to the criteria this loop owns:

- **Domain Fit (criterion 9)** — the ruleset must be specific to this account's words/topics/proof types, not a restatement of the universal framework. Generic output (rules any account could have produced) caps at 6 — that means the extraction failed.
- **Trust-Ladder Height (criterion 5)** — the proof-pattern finding must name the *actual rung* this audience trusts, evidenced by the winners, not assumed from theory.
- **Contrast Integrity (criterion 3)** — when crediting a winner's contrast, confirm it was a true opposite of the held belief, not a strawman that happened to perform.
- **Anti-patterns to catch in the data, not just avoid in output:** the STOP list must surface any mascot reveals, third-party-only proof, single-job hooks, and bolted-on urgency found in the loser set — those are the highest-value findings.

**HONESTY SPINE (non-negotiable):** this loop discovers which *manufactured-novelty* moves win for this account — it never licenses fabricating the underlying facts, urgency windows, or proof. If the data shows that fake urgency or invented stats correlated with views, the rule is "those reads burn trust over the lifetime of the account," not "do more of them." Every extracted rule must be backed by a real quoted line from the creator's real content; an unquoted rule is a hallucination and gets cut. The illusion is of novelty only.

**One-line self-check:** *Could a competitor in a different niche use this ruleset verbatim?* If yes, it is framework, not bespoke execution — re-extract until the rules only fit this account, every one anchored to a quoted line and a named component.
