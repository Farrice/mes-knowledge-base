# MES 3.0 Deep Extraction — Kallaway, "Content Growth System" (strategy + Claude-workflow layer)

**Corpus (two videos, treated as one):**

| # | Video | ID | Published | Length | Views @ pull |
|---|---|---|---|---|---|
| A | *How to Use Claude To Grow From 0 to 100K Followers (Full Course)* | `vwlK6MbdAto` | 2026-08-27 | 49:10 | 6,715 |
| B | *5 Claude Skills To Grow Faster Than 99% of People on Social Media* (Anthropic-sponsored) | `Cnk9NQ8JpCs` | 2026-07-08 | 23:14 | 84,232 |

**Speaker:** Kallaway (Ankur Nagpal — no; see note). Channel `@Kallaway`, IG `@kallawaymarketing`. Transcript renders his name as "Callaway"; the correct spelling is **Kallaway** (confirmed by on-screen artifact titles "Dr. Kallaway", "Kallaway Marketing engines v1.0", frame `t0740.jpg`, `t4000.jpg`). *Note: the Finder sidebar in `frame_0018.jpg` shows a home folder named `ankur` — UNCONFIRMED whether that is his legal first name or a shared machine.*

**Citation convention.** `[A 36:46]` = video A at 36:46 (verified against the deduplicated VTT). `[FRAME …]` = read from a rendered frame; source frames live in `extractions/kallaway-growth-system/frames/` and my crop-and-upscale renders in `.tmp/zoom/` (the video ships at 640×360 max — PO-token-gated, no higher format exists — so all on-screen text below was recovered by 4–8× lanczos upscaling of the native frame; anything I could not read cleanly is bracketed or marked UNCONFIRMED).

**Chapters (A):** Intro 0:00 · Workflow Overview 0:24 · Setup 1:00 · Strategy & Positioning Skills 2:10 · Niche Interview 3:58 · Unique Positioning Builder 7:49 · Bullseye Builder 16:38 · Topic Scanner 24:12 · Format Finder 27:39 · Video Production Workflow 31:41 · Content System Learning Loop 45:06 · Summary 47:47

**Related on-disk material (context only, not re-extracted):** `extractions/kallaway/source-skills/strategy-bundle/PROVENANCE.md` — the 5 free `.skill` files + orchestrator, acquired 2026-08-27. Load-bearing fact from that file: **the free bundle is strategy-phase only.** `engine-builder`, `topic-brainstormer`, `video-maker`, `channel-coach` — every skill in the production and learning loop — are demoed on screen in video A but are **not distributed**. Everything in the "Video Production Workflow" and "Learning Loop" sections of this report is therefore *observed output with no source code*, which makes the artifact ledger below the only spec that exists.

---

## 1. Genius patterns

### P1 — The data layer is the anti-slop mechanism, not the prompt

His entire thesis about AI content quality is that quality is a **data-availability** problem, not a prompting problem.

> "If you don't have the social media data in Claude, that's where you get AI slop. Claude is just guessing. It has no context on you. It doesn't know what videos are working. Doesn't know how the competitors are posting. And so it just generates absolute trash." `[A 01:39–01:50]`

> "This combination of Claude and Sandcastles, the data loop is really why I've been able to grow so much faster than most people." `[A 01:57–02:03]`

**Mechanism.** Every one of his skills has a mandatory external-data precondition and a *degraded* mode. He never writes a "better prompt" to fix slop — he widens the evidence set. The niche interviewer's own output declares this explicitly: after producing a 7-attribute positioning table it writes *"Remember: this is a hypothesis from self-knowledge — the next step (Unique Positioning Builder) crosses it against what LA facial surgeons are actually posting to find the real white space. Don't treat it as settled."* `[FRAME t0740.jpg, ~07:40]`

Corollary he states outright: the pre-data pass is **openly labelled a guess**. "This is before it hits the sand castle's data. It's just guessing based on the level of depth that you provide." `[A 07:33–07:36]`

### P2 — Interview depth is the compounding input; he demonstrates the standard rather than describing it

> "I want you to replicate the level of detail that we have here." `[A 05:18]`
> "This is critical to have this much depth. Again, the more you give, the better the targeting will be. And I'll show you how that ripples downstream. So, you really want to spend like 5 10 minutes answering these." `[A 06:28–06:38]`

**Mechanism.** He doesn't tell you to be specific — he shows a ~350-word answer to a single question on screen for 40 seconds (see Exemplar E1). The instruction *is* the artifact. And he names the compounding: "it generates automatically as long as you answer the niche interviewer stuff. That's why this system is so cool. You answer those questions and it kind of like trickles down." `[A 19:03–19:11]`

The interview is only 5–6 questions, and the question set is fixed: (1) business context / what you sell / who pays / revenue mix, (2) **the chair test** — one viewer in a chair, demographic + psychographic + beliefs, (3) her dream outcome, (4) her pain points, (5) target authority statement in one sentence, (6) unfair advantage. `[A 04:20–07:14]`

The prompts themselves are engineered to *provoke* ramble, not to be answered tidily — the last one ends with a one-word instruction:

> "Last question — what's your unfair advantage? Unique experiences, results, stories, credentials, or a way of communicating that most people in your space can't honestly claim. Anything: training lineage, case volume, revision work you fix from other surgeons, filler-removal cases, your own family, how you talk in the room, why you stopped injecting. **Ramble.**" `[FRAME t0710.jpg, ~07:03]`

### P3 — Positioning is a seven-attribute lattice you *multiply*, not a single slot you pick

The seven differentiation attributes `[A 08:08–09:42]`:

1. **Topic selection** — talk about things not typically covered in the niche
2. **Substance depth** — common topics, uncommon granularity/tactics
3. **Unique stories or proof** — "most people can't say they've done without lying"
4. **Avatar specificity** — serve an underserved slice
5. **Delivery style** — voice, rhythm, tone, how you articulate
6. **Storytelling formats** — structures nobody else uses
7. **Visual format** — how it's shot/typeset (e.g. transparent overlay vs hype edit)

> "Your goal really in this stage — and you don't have to solve it in one day — is to figure out where in those buckets of seven is there a white space in the niche that your unique background and expertise can help you fill. And you can kind of **take multiple of those and multiply them together**. And that's how you craft your own lane to grow faster." `[A 09:42–09:57]`
> "You don't have to have your own lane from day one, but the more you can carve a differentiated niche, the faster you will grow **if the content is good**." `[A 09:59–10:05]`

**Mechanism.** Seven binary-ish attributes → 127 non-empty combinations. Nobody has to win an attribute outright; they need an *unoccupied intersection*. This is why the rendered wheel says "No wedge is fully green in this niche — the open lanes live [inside the] wedges" `[FRAME t1600.jpg]`. The claim is falsifiable per attribute against real competitor data, which is what makes it a lattice rather than a vibe.

### P4 — Rings are derived by *which constraint you relax*, not by "getting broader"

This is the highest-value non-obvious mechanic in the corpus and **he never says it out loud.** The bullseye artifact's left-hand table is headed `Constraint relaxed | Size | Converts | Competition`, and each ring card carries the field **`CONSTRAINT RELAXED VS. THE RING INSIDE`** `[FRAME t1820.jpg, ~18:20]`:

| Ring | Constraint relaxed vs. inside | Size | Converts | Competition |
|---|---|---|---|---|
| 1 Elizabeth | — | tiny | very high | ~empty (Pennington only, in Shreveport) |
| 2 Filler-fatigued women 45–65 | geography + income | ~5–10× | high | light (Chesnut, Mustoe touch it) |
| 3 Women considering facial surgery | injectable history | ~5–10× more | medium-high | crowded (Nayak, Sadati, Talei, Karam, Kassir) |
| 4 Women 35+ aging-face curious | surgical intent | ~5–10× more | low-medium | very crowded (Ourian, Karam, Barrett, every derm) |
| 5 All beauty & skincare | gender + age + intent — everything | huge | ~zero | saturated (Yoon, Linkov, …) |

**Mechanism.** "Go one ring broader" is unactionable; "drop the income filter" is a decision. Because each ring is a named constraint, the ring set is *auditable* — you can argue about whether income or geography should come off first. And the last row's constraint reads "**everything**", which is why Ring 5 is a trap rather than a tier. Compare his spoken version, which is much vaguer: "One ring outside might just be B2B tech sales. One ring outside that might just be B2B sales…" `[B 11:50–12:10]`.

### P5 — The 3-2-1 mix: virality is a *deliberately budgeted minority* of the batch

> "The content mix that I recommend all business owners run is called the 321 content strategy. You have three buckets. Assume you make seven videos in a week… Of those seven, you have three buckets of two and then one random one which I call the chaos agent." `[A 19:27–19:42]`

Allocation: **1 broad bucket × 2 videos (Ring 4) + 2 narrow buckets × 2 videos each (Rings 2–3) + 1 chaos dart = 7.** `[A 19:42–20:00]`

> "The broad bucket… it's really meant to like step-change your traffic to bring a lot of new eyes onto the page." `[A 20:02–20:18]`
> "The chaos agent can be anything from red to light blue. You still don't want to go broad dark blue because if you do that and **you go viral on accident, you could mess up the page. You'll bring in a lot of people that are not fits and the algorithm will get confused.**" `[A 20:36–20:49]`

**Mechanism.** Going viral is modelled as a *risk with a blast radius* — an accidental Ring-5 hit poisons the classifier that decides who your channel is for. Reach is therefore rationed to 2/7 and fenced at Ring 4. The rendered artifact enforces this typographically: a red band across the outermost ring reads **"RING 5 · TOO BROAD — DANGER: viral with the wrong avatar"** and the centre reads **"RING 1 · too narrow"** `[FRAME t2315.jpg]`.

### P6 — The chaos agent is a hypothesis with a stated learning payoff, not a random idea

The chaos table has three columns: `Chaos idea | Kind of wild | **A win teaches you**` `[FRAME t2230.jpg, ~22:30]`. Framing line, verbatim: *"Now the chaos agent — one rogue video per batch, any Ring 1–4, any format, never Ring 5. Five candidates, each wild in a different way; pick one for batch 1, the rest go in the reserve."*

| # | Chaos idea | Kind of wild | A win teaches you |
|---|---|---|---|
| C1 | "The $200,000 face." Anonymized composite of what Elizabeth's 15 years of injectables actually cost, item by item, and what it bought her. | Deeper than Ring 1 — insider content only true buyers feel in their stomach | Whether naming the money out loud is a magnet or a repellent for the invisible-by-choice woman |
| C2 | The mirror lecture, no cuts. One take at the consult mirror with a marker, drawing where a SMAS lift vs a deep plane lift actually moves tissue. Two minutes, no b-roll, no music. | Format experiment — nobody in the niche does long, unedited teaching | Whether your signature visual can carry a video alone (**this decides B1's future**) |
| C3 | "Why I stopped injecting." Off-duty, on why you gave up bodies eight years ago. | Personality / behind-the-scenes swing | Whether Elizabeth wants the man, or only the doctor |
| C4 | The Kris Jenner effect, re-aimed. Not her face — the phenomenon. | Trend hijack aimed back at Ring 2–3 | Whether cultural moments can be borrowed without importing [the wrong audience] |

**Mechanism.** Each chaos slot is pre-committed to answering ONE question, and the questions are orthogonal (money-frame tolerance / format viability / parasocial appetite / trend-hijack safety). One video per week × four orthogonal questions = a designed experiment, not a lottery. C2's payoff even names a downstream dependency ("this decides B1's future") — the test result changes another bucket's fate.

### P7 — The two-zone sourcing rule: topics are altitude-bound, craft is altitude-free

The **Inspiration Sourcing Map** artifact `[FRAME t2405.jpg, ~24:05]`, header verbatim:

> "**Inspiration Sourcing Map** · who to study, and for what
> The two-zone rule. **Topics** come from the ring your bucket sits on (Rings 1–3 for the narrow buckets, Ring 4 for the broad one). **Craft** — formats, hooks, storytelling, editing, pacing — ca[n] come from anywhere on the board, including Ring 5 and other niches entirely. Ring 5 is craft-only: **sourcing topics there is how a surgeon's channel drifts into being a beauty channel.**"

Zone labels on the graphic: outer hatched band = "CRAFT ZONE · whole board · formats · hooks · storytelling · editing — from anywhere"; footer = "Ring 5 = craft inspiration ONLY. **Never source topics here.**"

**Mechanism.** This resolves the standard creator contradiction ("study the big accounts" vs "stay in your niche") by splitting the two things you copy. It also supplies a causal story for niche drift — drift is not a discipline failure, it's a *sourcing* failure, and it has a specific point of entry. Nowhere in the spoken track does he state this rule; it exists only inside the rendered artifact.

### P8 — Screen before you spend: free triage, then a stated credit bill

The Topic Scanner splits into a free stage and a paid stage, and reports both `[FRAME t2535.jpg, ~25:35]`:

> "**Stage 1 done (free).** Scanned 400 watchlist videos from the last 180 days, re-sorted by outlier score, screened the top 130 by hand: **73 qualify ✓, 57 excluded ✗** (removed-channel leftovers 15, lifestyle/vlog 18, breast/body 11, Ring-5 skincare 8, misc 5). The full ✓/✗ table with reasons goes into `top-50.md` **so you can overrule any call.**"
> "**The credit bill.** The working set is the top 50 ✓ by outlier (down to ~6.5×). 13 are already analyzed (free). **Deep-analyzing the remaining 37 costs up to 37 credits** (you have 10,320)."

His spoken framing `[A 25:19–25:32]`: "if Dr. Mendez is in his Ferrari going up the coast on a vlog weekend with his wife. That's not relevant for me… So, it just screens that out. **It doesn't charge me a credit to run it and it doesn't waste compute to do it.**"

Video B's Hook Machine uses the same pattern in a different position — it states the balance *before* asking for scope: "You currently have **9,999 Sandcastles credits remaining** (resets [date])" then asks which channels, how many videos, what period `[FRAME d1928.jpg, B ~19:28]` — and closes with "The only thing that costs credits is when you deep analyze a video. The more videos you analyze, the better [the] insights."

**Mechanism.** Three moves stacked: (1) exclusion is free and reversible, (2) exclusion reasons are *itemized by category with counts*, (3) the spend is quoted against balance before it happens. The exclusion table ships in the artifact so the human can overrule — the screen is a recommendation, not a filter.

### P9 — Name the trap inside the artifact that would otherwise cause the misread

The Topic Scanner's ranked-bucket chart ends in a red-bordered callout `[FRAME t2615.jpg, ~26:15]`:

> "**Two traps, said plainly.** Rhinoplasty at 52× is one channel (Kassir) with influencer patients on TikTok — **a person winning, not a topic.** Facelift Patient Journeys is the biggest bucket (15 videos) and it's not white space — it's the *format* you deliver your buckets through, **not a fourth bucket.**"

The Format Finder legend does the same in miniature: its top colour band is labelled `≥20× (Kassir-inflated)` `[FRAME t3020.jpg]` — the legend itself carries the caveat about the channel distorting the scale.

Video B's channel-analysis artifact carries the inverse — a **`Retire this one`** amber pill on an underperforming pattern: "The 'you're doing it wrong' problem hook — Opening on the viewer's failure ('The reason your videos are flopping…', '3 mistakes you're making') consistently lands **below** baseline (0.6×). Same author, same niche — the negative frame is the drag. Flip these to a summit frame ('Here's how to win') before posting." `[FRAME d1636.jpg, B ~16:36]`

**Mechanism.** "A person winning, not a topic" is a reusable epistemic distinction: outlier scores conflate topic effect, format effect, and *celebrity/credential effect*, and the third is non-transferable. The artifact pre-empts the exact wrong conclusion the chart invites. Same-author/same-niche controls make the negative finding causal rather than correlational.

### P10 — The four-altitude reference ladder, with the fifth tier skipped and the skip reported

Verbatim from the Video Maker's closing narration `[FRAME t3630.jpg, ~36:30]`:

> "References were pulled at **four altitudes**: your own analyzed videos first (Modern Story Arc 9.9x, Dopamine Addiction Loop 18.5x, Triple Hook 17x, Double Tap 4x), then the realskytan 74.5x source, then two adjacent Top-50 rows (bonusfootage rhythm, peter.visuals tension), then the library (rico's U-Turn Hook). **Global Sandcastles had no analyzed matches and the unanalyzed hits were off-topic, so I spent zero credits there.**"

| Altitude | Source | Why it ranks there |
|---|---|---|
| 1 | Your own analyzed winners | "his words, safe to use" — zero voice risk, zero attribution risk |
| 2 | The single outlier being remixed | the format you're explicitly modelling |
| 3 | Adjacent Top-50 rows (same niche) | proven in-niche craft, different topic |
| 4 | The library / Collections (cross-niche) | pure craft transfer per the two-zone rule (P7) |
| (5) | Global Sandcastles search | costs credits; skipped, and the skip is *reported* |

The Substance Sheet then labels its first section **"Own-channel substance reused (Altitude 1 — his words, safe to use)"** `[FRAME t3620.jpg]`. Altitude is a first-class field in the artifact, not a footnote.

**Mechanism.** Ordering by *provenance distance from the author's own voice* means voice fidelity degrades monotonically as you descend, and the artifact can tell you exactly how far it had to go. It also makes the credit spend legible: altitudes 1–4 are free, altitude 5 is paid, so "I spent zero credits" is a quality claim (nothing worth buying) rather than a cost-saving.

### P11 — The rinsed-phrase strikethrough: an anti-self-plagiarism device

The Power Phrase Cloud is headed `POWER PHRASE CLOUD — SIZED BY PERFORMANCE · GOLD = OWN · **STRUCK = RINSED (USED IN THE LAST ~60 DAYS)**` `[FRAME t4000.jpg, ~40:00]`. Struck through on screen: ~~scientifically impossible to skip~~, ~~social media machine~~, ~~Claude just changed social media forever~~, ~~30 days of content in 30 minutes~~. Live: "get people addicted to your content", "most people don't know this, but you can just…", "cracked out brains", "hypnotize a viewer", "physically cannot scroll away", "the opposite of slop".

The Video Maker then acts on it `[FRAME t3630.jpg]`:

> "**Two things I deliberately did NOT do.** I didn't reuse 'scientifically impossible to skip' — you've run it twice in ~60 days, **it's rinsed for your audience** — so Hook 2 remixes the construction instead ('neurologically unable to scroll away')."

**Mechanism.** Every hook engine in the wild optimizes for *what works*, which converges every account onto its own three best phrases until they die. The rinse window (~60 days) makes recency a *penalty* term and forces construction-level remix (keep the mechanism: absolute-impossibility + physiological verb; change the surface). This is the only implementation I have seen where the phrase bank actively kills its own winners on a clock.

### P12 — Script templates rendered as time-budgeted beat timelines

`SCRIPT TEMPLATES — BEAT TIMELINES (SECONDS PER BEAT)` `[FRAME t4018.jpg, ~40:18]`. Each template is a horizontal stacked bar where **segment width = median seconds from the cited winners** and each segment is labelled with that beat's *job*:

- **S1 Named-Method Steps ⭐** · 20.4× · 18.5× · 17× · 74.5× · 89.8× · ~80s → `Hook/name it 5s | [credibility] anchor | Step 1 basic 16s | Step 2 where most mess up 18s | Step 3 where the money's made 18s | Cap combo | The ask 8s`
- **S2 Tool-Machine Reveal ⭐** · 60.8× · 311.8× · 98.4× · 4.9× · 4.7× · ~63s → `[Promise] bridge 6s | The receipt 7s | Scale play 18s | Secret layer 6s | Enable it 10s | Authority tag 8s | The ask 7s`
- **S3 Paradigm Flip** · ~62s → `[Gnosis] hook | Old model named 7s | Why it broke 7s | [New] model named | Mechanics w/ numbers 24s | Modern-era reframe | The ask 10s`
- **S4 Metric Case Study** · 111.2× · 92.5× · 26.9× · 23.7× · 20.1× · ~52s → `Metric hook 5s | Show the clip 5s | Trigger 1 + psychology 8s | Trigger 2 + psychology 16s | Replication proof 8s | Steal it 4s | The ask 5s`
- **S5 Levels Ladder ⭐** · ~135s → `Hook + name | Levels 1–3 42s | [skip] | Levels 4–6 58s | The ask 10s`
- **S6 Ultimatum Checklist** · 149.7× · 37.8× · 16× · 9.8× · ~60s → `Ultimatum hook 4s | Item 1 8s | Item 2 8s | Item 3 8s | Item 4 9s | Item 5 + the ask 9s`

Footer: "⭐ = own hero structures. Widths are median seconds from the cited winners. Full beat jobs, transitions and cited lines live in `engine-scripts.md`."

**Mechanism.** A beat list tells you the order; a beat *timeline* tells you the budget. "Step 2, where most mess up, 18s" is simultaneously a slot, a job description, and a duration constraint you can film against. "The ask" is a fixed terminal beat in every single template. Note S2's cited outliers (60.8×, 311.8×, 98.4×, 4.9×, 4.7×) — the template is built from a mixed-performance set, not a cherry-picked one, which is what makes the *median* meaningful.

### P13 — Spoken hooks are shipped paired with their on-screen text, as phone mockups

Section header in the Video Maker output: `SPOKEN HOOKS · WITH THEIR ON-SCREEN TEXT` `[FRAME t3722.jpg, ~37:22]`. Layout: large white spoken line on the left, two phone-shaped cards on the right showing the paired text-hook options typeset as they would appear.

> HOOK 1 — "Hook. Lock-in zone. Block one. Re-hook. Block two. Close. That's the script architecture that fires dopamine twice in sixty seconds." → text cards: *"The script architecture that fires dopamine twice"* / *"The 2x2 Script — two dopamine hits per video"*
> HOOK 2 — "Here's how to structure a script so a viewer is neurologically unable to scroll away." → text cards: *"How to script a Reel viewers can't scroll away from"* / *"Script structure that hypnotizes [the scroll]"*

And the Text tab records his typographic constants as machine parameters: "**Own defaults:** premium-but-clear typography · top third · 2 lines · **separate from the spoken line.** 16 stragglers pending (title animates in later) — see `engine-hooks-text.md` §2." `[FRAME t4012.jpg, ~40:12]`

**Mechanism.** In his older canon (`kallaway-hook-mastery`) the triple-hook is a *principle*. Here it's an **output schema**: you physically cannot receive a spoken hook without its text partner. "Separate from the spoken line" is the rule that stops the text hook being a subtitle — it must add a second, non-redundant frame. Every existing hook tool ships a list; this ships a pairing.

### P14 — He publicly caps the AI's ceiling, three times, and designs around the cap

> "One-shotting writing with Claude is the **final frontier**. I do not believe Claude is able to write as good as a human today. So, the goal really with this is getting 80 to 90% of the way there and then you manually tweaking it. You tweak it, you feed in the tweaked version, it hones itself, you do that 20 or 30 times, and then it starts to get close to the level that you want." `[A 36:46–37:06]`
> "**Now again, I'll say this for the third time.** This is not exactly where I'd want it to be on day one. And that's because there isn't enough reinforcement learning on the writing." `[A 40:16–40:25]`
> "**Nobody's using AI to one-shot these scripts.** I wanted to show you the skills to build a hook engine and a script machine so you can improve it over time with your vernacular in your language. It's just not there today." `[A 42:52–43:03]`

And then he shows what he *actually* does instead — `[A 43:00–44:10]`: sort own channel by outlier score → read the transcript of the nearest-topic winner with `show sections` on → open the Hooks tab, filter to own channel, sort by outlier, **turn off the images so only words show** → scan for power phrases → hand-write, hand-delete ("too corny. Delete. Too long-winded. Delete. It's the sync, but I'm not sure what it means. Delete.")

> "I will never word for word take what someone's saying. But I can look at the rhythm and the flow and the way the sentences are laid out and how the points are sequentially moving." `[A 43:13–43:22]`

**Mechanism.** The system is explicitly designed for a *sub-human writer*: AI owns everything up to and including the substance sheet; the human owns the last mile; the engine files (`engine-*.md`) exist to close the gap over 20–30 iterations. The honest ceiling is what licenses the architecture — if he claimed one-shot scripts, the whole `engine-builder` / diff / paste-back loop would be pointless. Note the offered feedback loop: "**Paste your rewrite back whenever you're done editing and I'll diff it and update the template.**" `[FRAME t3630.jpg]`

### P15 — The Learning Loop closes as a machine-readable brief, not a report

The Channel Coach's final section is titled **"Batch bias for the next 7 videos"** with the subtitle **"What the topic-brainstormer will read as its marching orders."** `[FRAME t4725.jpg, ~47:25]` Seven colour-coded slot cards:

| Slot | Assignment | Colour |
|---|---|---|
| 1–3 | Claude / Sandcastles tutorial · specific-outcome hook | green (proven) |
| 4–5 | Hook formula word-by-word + labeled example | green (proven) |
| 6 | Resource / database roundup · **test** | amber (test) |
| 7 | Chaos agent · anything off map | grey (chaos) |

Footer: "**0 slots:** multi-step storytelling frameworks · content-strategy myth-busts (0.85× avg). Every script: payoff in the first two sentences, real numbers over hypotheticals, CTA that continues a numbered open loop."

Three cadences, stated plainly: "It's the initial strategy that you do **once every 30 days**. It's the topic workflow that you do **every video**. And then it's the content coach that you do **every 7 days**." `[A 47:34–47:45]`

**Mechanism.** The loop closes because the coach writes an *input file* for the next skill, not a summary for a human. "0 slots" is the load-bearing invention — it names the losers and their average (0.85×) so the demotion is explicit and reversible. And the three prescriptions at the bottom are style constraints propagated from the tactics chart into the next batch's briefs.

### P16 — Two-question topic triage, screened on camera as an overlay

His triage gate appears as an on-screen title card `[FRAME t3320.jpg, ~33:20]`:

> "Do I have something interesting to say for this topic?
> Would it be relevant and valuable for the person [I'm] trying [to attract]?"

Applied live down a top-50 list `[A 32:20–33:30]`: "AI presentation generation… That's not going to drive people to SFA or Sandcastle. So I'm going to skip. Number two and number three were off topic. Number four, Instagram profile optimization — too transactional. I can't say anything different. I don't like it. Next. Viral video psychology… This could work, but he's probably using examples. Can I find something unique to say? I'm not sure." → lands on #11.

> "You might say, 'Whoa, you just skipped through the top 10.' Well, the reality is **I only need one to make today and I need seven to make per week.** So, if this is a top 50, I need seven from here and I can run this next week with all fresh videos and go again. **So, you're allowed to pass on a bunch of stuff that's not a fit. You don't have to pick the highest ranked stuff on the top.**" `[A 33:35–33:55]`

**Mechanism.** Rank is a *pool ordering*, not a priority queue. The binding constraint is 7 usable ideas per 50 (14% hit rate), which makes a 70% pass rate correct behaviour rather than procrastination. Both gate questions are about *the author's edge* and *the reader's fit* — neither is about the metric that produced the ranking. The scoring system's job ends the moment the pool is built.

### P17 — Naming the mechanism is treated as a measurable variable, controlled for

From video B's analysis artifact `[FRAME d1636.jpg, B ~16:36]`, under "Hidden Insights — what a scroll would miss":

> "**Naming the mechanism is your single biggest lever.** Every top non-AI video hands the idea a proprietary name: Triple Hook Method (12.3×), Double Tap (3.3×), Modern Content Stack (1.4×), the 'Series' framework (2.5×). The ones that describe a problem instead — 'Skip Rate Ruiners,' '3 mistakes' — sit at 0.6×. **Identical creator, identical topic depth. The packaging is the variable.**"

And it becomes a production requirement inside the Video Maker: "I coined it 'The 2x2 Script' (two dopamine hits, two ahas) — **swap the name if you have a better one, but it needs one; every winner in your Storytelling bucket has a coined term.**" `[FRAME t3630.jpg]` The Substance Sheet then reserves a whole section for it: `Coined name (proposed)` — *"'The 2x2 Script' — two dopamine hits, two ahas. Alternate: 'The Lock-In Architecture.' Kallaway picks."*

The Channel Coach corroborates independently: "Coined proprietary term (n=7) — **1.43×**" in the script-tactics chart `[FRAME t4725.jpg]`.

**Mechanism.** Same-creator/same-depth controls turn a stylistic preference into a causal finding. Then the finding becomes a hard slot in the output schema with a human veto and a stated alternate — the machine proposes, the human picks, but the *slot cannot be empty*.

### P18 — Instant payoff beats setup by 2.4× against every other tactic on his channel

Channel Coach, "Script tactics that separate winners — Average outlier of videos using each tactic. **Instant payoff is the single strongest driver on the channel.**" `[FRAME t4725.jpg]`

| Tactic | n | Avg outlier |
|---|---|---|
| Instant payoff before any setup | 6 | **4.08×** |
| Comment-gated CTA that continues an open loop | 5 | 1.72× |
| Numbered step-by-step delivery | 8 | 1.68× |
| Coined proprietary term | 7 | 1.43× |
| Concrete before/after number swap | 5 | 1.40× |
| Hypothetical example walkthrough | 4 | 1.18× |
| Rule-of-three / contrast list | 4 | 1.05× |
| Self-demonstrating meta technique | 2 | 1.00× |

**Mechanism.** The gap between #1 (4.08×) and #2 (1.72×) is larger than the gap between #2 and #8. That's not a ranked list — it's one dominant variable with seven rounding errors, and the coach says so in the subtitle rather than letting the bar chart imply eight equal levers. Note that "self-demonstrating meta technique" scores **1.00×** (baseline) — yet the Video Maker still recommends Script 1 *because* it demonstrates itself ("Script 1 practices what it preaches… which is your bucket's demonstrate-inside-the-script rule" `[FRAME t3630.jpg]`). He keeps a positioning commitment that the data says is performance-neutral. That is a deliberate identity-over-metric override.

### P19 — Formats are deflated on purpose

> "When I say format, formats are a little overblown as a term. It's just a combination of **how you structure the information and how you visualize it.** Those together make a format. People are always like, 'Oh, I need to find all the hidden formats.' Formats are a helpful way to structure your information, but I find it can be a bit overwhelming to try to hunt for like the optimal format. **Typically, there's a couple that you like making and you just run that back and forth.**" `[A 27:51–28:15]`
> "In this first phase, if you're just starting out with content, you want to be able to **wildly experiment.** So, I like picking ones that have either worked really well or find the white space where you think you have a unique advantage." `[A 30:05–30:20]`
> "Typically you're going to pick like two or three every single round of seven… and then most people will get comfortable with one or two that they like making over and over." `[A 29:50–30:05]`

**Mechanism.** He definitionally reduces "format" to a 2-tuple (structure × visual), which is *exactly* the matrix he then renders — the deflation is what makes the artifact possible. And the search is bounded: explore 2–3 per batch of 7, converge to 1–2 permanently. Format hunting is a finite phase, not a practice.

### P20 — He runs the whole strategy demo as a persona he explicitly cannot fake

> "I'm going to pretend like I'm a plastic surgeon… I'm a plastic surgeon in LA that's trying to use content to drive leads and clients for my practice. Call me Dr. Callaway. And you can tell I'm obviously not a real plastic surgeon. I would have fixed this nose a long time ago." `[A 02:43–02:59]`
> "I want to prove that anybody, **even if you don't know what you're doing with content**, can run this workflow and get insane insights." `[A 03:03–03:11]`

Then he switches back for production: "Dr. Callaway is retiring and I'm going back to my social media growth side… **I don't know anything about plastic surgery.** So, amazing for the strategy if I'm trying to go from scratch. But if you're an actual plastic surgeon, you'll be able to give real context on these videos." `[A 31:44–32:02]`

**Mechanism.** The persona split is a demonstration of the system's *boundary*. Strategy transfers to a domain he knows nothing about (proof of generality); production does not (proof that substance must come from the operator). Both halves of the credibility claim are stronger for being split. Also note the persona is a **high-ticket, non-tech, local-service** business — deliberately the hardest possible case for "AI content strategy", and the one his actual buyer (SFA business owners) resembles.

### P21 — Every artifact declares its own consumers

The `top-50.md` header block, verbatim `[FRAME t2645.jpg, ~26:45]`:

> *"Step 1.4 of the 0→100K Growth System. Created 2026-08-16. Source: Sandcastles watchlist 'Plastic Surgeon Clinic,' 180-day lookback, sorted by outlier score. **Read by: topic-brainstormer, format-finder, spoken-hook-machine, text-hook-machine.** Full analysis payloads live in Sandcastles (click 'analysis'); the merged JSON export is `top-50-analysis.json`."*
> "★ = one of the 3 chosen buckets. ✓/✗ = qualifies for Elizabeth's niche (✗ rows carry the reason). **Outlier = N× that channel's normal.**"

And the handoff paragraph at the end of the Bullseye step `[FRAME t2315.jpg, ~23:15]`:

> "Step 1.3 done. `growth-system/bullseye-map.md` saved with the center, five rings, chosen trio + bench, chaos reserve, sample batch 1, calibration tracker, sourcing rules, and the Ring 5 trap list. The 3-2-1 mix is pinned to your artifact gallery so you can swap buckets later **without re-running anything**.
> The one-line summary of what you now have: you speak to Elizabeth in every video, you aim at Rings 2–4 through Filler Reckoning / Why It Failed / How Faces Age, you fire one violet chaos dart per batch, and after 2–3 batches **the numbers — not the vibes — decide** what gets a third dart and what goes to the bench.
> Next is step 1.4, the **Topic Scanner** — the last strategy step. It takes your 18-channel watchlist and the ~44 analyzed videos, builds `top-50.md` (**the shared data core every production skill reads**), and validates the three buckets against what actually performs in the niche. **Say 'go' and I'll route you.**"

**Mechanism.** Four separate contracts in one paragraph: (1) numbered step ID, (2) named file with an itemized manifest of its contents, (3) one-line state summary in plain English, (4) explicit next-step routing with a one-word trigger. The `Read by:` line makes the file's interface explicit — you can change `top-50.md` and know exactly what breaks. And "Outlier = N× that channel's normal" defines the metric inline so the reader never has to look it up.

---

## 2. Hidden knowledge — what he does but doesn't say

**H1. The bullseye ring numbering silently inverted between July and August.** Video B's rendered bullseye labels the *centre* "LEVEL 5" and the *outermost* "LEVEL 1" with a ✗ on it `[FRAME d1249.jpg, B ~12:49]`. Video A's labels the centre "1 · Elizabeth" and the outermost "5 · All beauty & skincare" `[FRAME t1730.jpg]`. He never mentions the change. The new direction is correct — "Ring 5" now reads as *distance from bullseye*, matching the dartboard metaphor and making "never Ring 5" a natural sentence. UNCONFIRMED whether this was deliberate.

**H2. "3-2-1" and "322" are different models sharing a similar name.** B: *"I recommend most people start with a **322**. Three videos in the bullseye, two videos between level two and three, and two videos at level four."* `[B 12:30–12:44]` — that allocates 7 videos across *altitudes*. A: 3 buckets × 2 videos + 1 chaos — that allocates 7 videos across *named topic buckets*, with altitude as a property of the bucket. The unit of planning moved from altitude to bucket, which is what makes bucket-level promotion/demotion possible in the Learning Loop. Not flagged as a revision.

**H3. The Bullseye Builder went from data-free to data-fed.** B: *"Workflow number two **does not require the Sandcastle's MCP**… It doesn't require any cost or anything to run."* `[B 11:22, 13:33]` A's bullseye consumes the positioning doc, the 18-channel watchlist, and analyzed competitor videos, and emits competitor names per ring ("crowded (Nayak, Sadati, Talei, Karam, Kassir)"). The same-named skill changed category.

**H4. The interview questions are engineered to defeat marketing-speak.** "The chair test" forces a singular person. "Ramble" (P2) defeats the tidy bullet reflex. Q1 asks "what procedures make up most of your revenue?" — revenue mix, not offer list. The answers he models back are almost aggressively unpolished ("She'd be horrified if anyone knew she was here"). None of this is stated as technique.

**H5. `[NEED]` markers — the machine refuses to invent numbers and says which number it refused to invent.** The Substance Sheet ships a `Gaps` section `[FRAME t3630.jpg]`: *"[NEED] A real number for how many outlier videos Kallaway has reverse-engineered (used as the credibility anchor in Script 1's lock-in zone; placeholder 'hundreds')."* / *"[NEED] Optional: a retention-curve screenshot to show the second-hit bump on screen."* And in the narration: *"I didn't invent numbers: the one amber line in Script 1 … is flagged [NEED] for your real count."* The credibility anchor is the one slot where a hallucinated number would be maximally damaging, and it is the one slot the machine hard-refuses. Never discussed.

**H6. Research fills carry a `Plain-English:` gloss.** Every `[R]` citation is followed by a translation `[FRAME t3630.jpg]`: *"[R2] TikTok for Business (widely cited): 63% of the highest click-through videos hook the viewer within the first 3 seconds. **Plain-English: everyone optimizes the first 3 seconds; almost nobody designs seconds 3-12 (the lock-in zone).**"* The gloss is where the *argument* lives — the statistic is neutral, the plain-English turns it into his position. This is the single most transferable craft move in the artifact set.

**H7. Research is toggleable at the script level, and he says the tie-breaker is your ear.** The scripts panel has `context only | with research` pills `[FRAME t3735.jpg]`, and the narration closes: *"Both versions read clean; **toggle and see what your ear prefers.**"* Citations are an option, not an upgrade.

**H8. "Villain =" is a required field.** Substance Sheet, under `Customer language / beliefs to overcome`: *"**Villain = the flat middle (confusion/boredom), never the viewer's talent.**"* `[FRAME t3630.jpg]` Combined with B's "Retire this one" finding (blaming the viewer scores 0.6×), the villain slot is a structural guard against the highest-performing-looking, worst-performing frame in the category.

**H9. He measures at a maturity window and says so only in passing.** Coach callout: *"Also: don't judge the text-hook-machine video (1.4×) at 24 hours."* `[FRAME t4725.jpg]` A one-line rule that prevents the most common false demotion in the entire loop.

**H10. The coach states its own blind spot before its conclusion.** `What the dashboard can't tell you`: *"No comments / DM / lead data in the report — check manually that the people commenting 'hook' and 'audit' match your avatar **before crowning tutorials as the conversion winner.** Report is a combined IG + TikTok dashboard; all numbers above are the IG channel isolated (TikTok mirrored the same outlier ordering, so no contradicting signal)."* `[FRAME t4725.jpg]` It names the metric it *cannot* see, the wrong conclusion that gap invites, and the cross-check it ran to rule out contradiction.

**H11. Artifacts are pinned to the gallery so they can be edited without re-running the pipeline.** *"The 3-2-1 mix is pinned to your artifact gallery so you can swap buckets later without re-running anything"* `[FRAME t2315.jpg]`; *"[Artifact] saved to your artifact gallery as 'channel-[coach]' [so you can re]place each week rather than living only in [chat]"* `[FRAME t4725.jpg]`. State lives in named, replaceable artifacts — the chat is a terminal, not a database.

**H12. The skill remembers his personal ship-rules and asks about them by name.** Video Maker's second and final question: *"Lead-magnet trigger word for the CTA close (**your scripts never ship without one**)?"* → answer: `SCRIPT`. `[FRAME t3455.jpg, ~34:55]` It doesn't ask *whether* he wants a CTA; it asks which word, because the rule is already encoded.

**H13. He turns the images off to read hooks as text.** *"I sort the hooks by outlier score… and I **turn off this** so I can see the actual words."* `[A 43:47–43:55]` Reading hooks with thumbnails attached lets visual craft contaminate the judgment of the line. He strips the modality he isn't currently evaluating.

**H14. He recommends the most expensive model, unprompted, and names the reason.** *"For everything we do, we're going to run with Fable 5. That is the most expensive but the best model in Claude. You can probably run with Opus 5 as well. **I just want the best insights we can get.**"* `[A 02:16–02:24]` Confirmed on screen — the model selector reads `Fable 5 High` in every Claude frame (`t1600`, `t3722`, `t4725`). He also specifies **co-work mode**, not chat `[A 03:47]`.

**H15. He teaches the competitor-list escape hatch before anyone hits the wall.** Three ways to extend the watchlist beyond Claude's auto-populated 8–12: keyword+platform+size search, the `»` "resort our entire database closest to [this creator]" button, and paste-a-URL import ("If they're not in Sandcastles, we will import them in over 15 minutes") — plus the manual play of opening a known-good competitor's *following* list to harvest colleagues `[A 11:50–14:00]`. Honest about the corpus limit: "Sandcastles has hundreds of thousands of the top creators, but we don't have billions."

**H16. The Format Finder invents matrix rows that don't exist in the niche.** The structure axis ends with two rows labelled **"Case Autopsy (new)"** and **"Consult Room (new)"** whose cells all read `open` `[FRAME t3020.jpg]`. These are his chosen topic buckets promoted into *structural* candidates. The matrix isn't a survey of what exists — it's a survey plus a proposal, with the proposal visually distinguished.

**H17. Recording and editing are declared un-automatable and handed to a model-and-mimic loop.** *"There are no clawed skills or claude workflows for recording and editing. You don't really need them."* → model an existing video in your target format: angles, camera distance, lighting, who's on which side, where the text hook sits relative to the subject, cadence, rhythm; then match timing, pacing, sequencing in the edit `[A 44:12–44:45]`. On the tools: *"People can talk about how there are Remotion and like different auto editing templates. **They're all pretty trash.**"* `[A 44:36–44:41]` — note this directly contradicts video B, where he calls Remotion *"the world's best AI editing skill inside of Claude right now"* `[B 21:10]`, having disclosed he *"hasn't gone down the rabbit hole"* on it. **Seven weeks, opposite verdicts; the August one is the tested one.**

**H18. The whole thing is a funnel with exactly one CTA.** Short-Form Academy is pitched twice `[A 30:40–31:15, 48:08–48:26]`, the artifacts embed `shortform.academy` in their own footers (*"This bullseye is one piece of the full short-form system — the rest lives at https://shortform.academy"* `[FRAME t2315.jpg]`; *"Full system: shortform.academy"* `[FRAME t4725.jpg]`), and the free bundle stops precisely where production begins (PROVENANCE.md). The artifacts are the sales asset.

---

## 3. Hall of Fame exemplars

### E1 — The Chair Test answer (the depth standard, ~350 words for one question)

`[FRAME t0604_upper/c/b.jpg, A ~06:02–06:20]` — Q2, verbatim from screen:

> *"[Block 2: the Chair Test.] Picture the perfect viewer-turned-patient — the one who wrote you a $130K [check] and you'd clone ten of — sitting in the chair across from you at consult. Who is she (or he)? Age, what her life looks like day to day, what she's already tried that didn't work (filler, thread lifts, a 'mini lift' elsewhere, a botched primary rhino), what she's afraid of, and what she said in the consult that made you know she was your patient."*

His answer:

> "Okay, real person. She's 52. She lives in Brentwood or the Palisades, could be Calabasas or Hidden Hills. Married, husband's in entertainment finance or he's a partner somewhere, two kids, one's in college and one's about to leave. Household's clearing seven figures but she is not a celebrity and she does not want to be. **She'd be horrified if anyone knew she was here.** She does Pilates four times a week, she's been on the same dermatologist's schedule for 15 years, she has spent, and I'm not exaggerating, somewhere between $80,000 and $200,000 on Botox, filler, Ultherapy, Thermage, lasers, radiofrequency microneedling, all of it. And here's the thing: **it stopped working around 48. It might have started working against her.** She has migrated filler under her eyes that's been there six years and she thinks it's fat. She lost 30 pounds on a GLP-1 and now the lower third of her face fell.
>
> What she does all day: she's on Instagram at 11pm reading comments on other people's before-and-afters. She's on RealSelf. She's in a private Facebook gro[up]. Has a Notes app list of three surgeons. She's been 'researching' for two and a [half] years and hasn't booked a consult, because **the thing she's actually afraid of isn't the money and it isn't the pain. It's walking into school pickup and having someone go 'you look… different.' She'd rather look tired forever than look done.** She's watched a friend come back from a facelift looking pulled and windswept and it terrified her.
>
> What she's already tried that failed: more filler. That's the big one. She kept buying syringes hoping it would substitute for surgery and now her face is heavy and she can't tell if she's aging or if it's the product. She also tried the non-invasive machines. She'll tell you Ultherapy did nothing for $4,000 and she's still angry about it.
>
> What she believes: that a facelift is a last resort for old ladies, that it will look obvious, that everyone will know, and that surgeons will 'sell her' something. **She trusts other women more than she trusts doctors. She's smart, she's read a lot, and about 40% of what she's read is wrong.**"

*Why it's Hall of Fame:* four separate lines are directly reusable as content angles ("it might have started working against her", "she'd rather look tired forever than look done", "40% of what she's read is wrong", the GLP-1 face). Every downstream artifact in the video traces back to a phrase in this block — the ring names, the bucket names, the chaos ideas, even the wheel's synthesis. And it is answering a question that most people answer with "women 45–65, affluent."

### E2 — The Video Maker's closing narration (the production-skill voice, complete)

`[FRAME t3630.jpg + t3722.jpg, A ~36:30–37:22]` — verbatim:

> "Done — the artifact and the four files are above. Here's the short version so you can film without opening the data section.
>
> **What I built it from.** Your brain dump is the substance, untouched. I coined it **'The 2x2 Script'** (two dopamine hits, two ahas) — swap the name if you have a better one, but it needs one; every winner in your Storytelling bucket has a coined term. References were pulled at four altitudes: your own analyzed videos first (Modern Story Arc 9.9x, Dopamine Addiction Loop 18.5x, Triple Hook 17x, Double Tap 4x), then the realskytan 74.5x source, then two adjacent Top-50 rows (bonusfootage rhythm, peter.visuals tension), then the library (rico's U-Turn Hook). Global Sandcastles had no analyzed matches and the unanalyzed hits were off-topic, so I spent zero credits there.
>
> **The recommended combo.** Film Hook 1 + Text A + Script 1 (Architecture Walkthrough) first. Hook 1 is the realskytan format remixed onto your parts — 'Hook. Lock-in zone. Block one. Re-hook. Block two. Close. That's the script architecture that fires dopamine twice in sixty seconds.' — and Script 1 practices what it preaches: it's built on the 2x2 skeleton and tells the viewer so mid-script ('that's what these last three lines were doing to you'), which is your bucket's demonstrate-inside-the-script rule. Script 2 is the paradigm-flip shape from your Modern Story Arc (hook-value-CTA is the old skeleton, it flatlines after one dopamine moment, here's the 2x2). Two formats, same substance, **pick by gut.**
>
> **Two things I deliberately did NOT do.** I didn't reuse 'scientifically impossible to skip' — you've run it twice in ~60 days, it's rinsed for your audience — so Hook 2 remixes the construction instead ('neurologically unable to scroll away'). And I didn't invent numbers: the one amber line in Script 1 ('almost every outlier video I've reverse-engineered') is flagged [NEED] for your real count. The research toggle adds two cited fills only — the UC Davis curiosity/dopamine study (Gruber 2014) into Script 1's re-hook line, and TikTok's '63% of top videos hook inside 3 seconds' into Script 2's old-model line. Both versions read clean; toggle and see what your ear prefers.
>
> **Machine status.** The engines (Engine Builder) aren't built for this workspace yet, so this run leaned on the references plus your `kallaway-script-buckets` Storytelling template directly. It's personalized, but running `engine-builder` once will make the next twenty videos faster and sharper. Paste your rewrite back whenever you're done editing and I'll diff it and update the template.
>
> **Sources:** realskytan — The perfect scripting structure (Sandcastles) · Kallaway Marketing top-50 (this session) · Gruber, Gelman & Ranganath 2014, Neuron · TikTok hook performance statistics (Clouted) · Curiosity and reward — APA / Loewenstein lineage · Curious Shorts — CHI 2025"

*Why it's Hall of Fame:* it is the complete grammar of a trustworthy AI production report in five headed paragraphs — provenance ladder, one recommended path with the reason, **an explicit negative-space section**, honest machine-state with an upgrade offer, and a source list. The "Two things I deliberately did NOT do" heading is the move nobody else makes. Note also the two-word close on a genuinely subjective fork: *"pick by gut."*

### E3 — His actual writing process, unglamorised

`[A 41:43–43:03]` — verbatim, lightly punctuated:

> "I've done this thousands of times, so like it comes second nature to me. But really, **studying individual transcripts of videos you like that are mapped to a similar topic is the fastest way to get better at scripting.** … I go to the hooks tab. I type in my channel, Kallaway Marketing. I sort the hooks by outlier score. These are all my hooks. And I turn off this so I can see the actual words. And I literally just scan down. 'This is how you turn Claude into a social media machine.' 'Here's how to plan your next 30 days of content in 30 minutes.' 'Scientifically impossible to skip.' 'You're using the wrong story arc.' 'Addicted to your storytelling.' Like, I'm trying to look for these psychology-driven power phrases. And then I'm going to ask myself, well, what actually applies to the topic I'm talking about? So, in this case, it's a script writing structure. So, it's like, 'here's how to write so good it's basically unskippable.' So, I could kind of adjust this like 'here's how to build a script so that nobody scrolls by' or 'here's how to write a script so good it is basically impossible to skip' or 'it is basically impossible to ignore.' I'm just like playing with these phrases and I'm writing them down. I'm reading it. **I'm like, eh, too corny. Delete. Eh, too long-winded. Delete. Eh, it's the sync, but I'm not sure what it means. Delete.** That is really the process of script writing. **Nobody's using AI to one-shot these scripts.**"

*Why it's Hall of Fame:* it is a live demonstration of remix-at-the-construction-level (P11) — he takes his own 4.8× hook "Here's how to write a hook so good, it is basically unskippable" `[FRAME t4245.jpg]` and generates four variants that preserve the *mechanism* (here's-how + absolute-impossibility) while swapping the surface, then rejects three of them on gut with a named reason each. The three rejection reasons — corny / long-winded / vague — are a complete rubric.

### E4 — The Two Traps callout (honourable mention, 44 words)

`[FRAME t2615.jpg, A ~26:15]`

> "**Two traps, said plainly.** Rhinoplasty at 52× is one channel (Kassir) with influencer patients on TikTok — a person winning, not a topic. Facelift Patient Journeys is the biggest bucket (15 videos) and it's not white space — it's the *format* you deliver your buckets through, not a fourth bucket."

*Why:* "a person winning, not a topic" is a five-word tool for a mistake that costs creators months.

---

## 4. Signature moves

**SM1 — Hypothesis, then falsification, and the artifact says which one it is.** Every strategy skill emits a *guess* and labels it: "This is before it hits the sand castle's data. It's just guessing" `[A 07:33]`; "this is a hypothesis from self-knowledge… Don't treat it as settled" `[FRAME t0740.jpg]`. The next skill's whole job is to cross the hypothesis against data — the wheel's synthesis reports the audit result as a score: *"[of] your seven claimed edges: four confirmed, one contested-then-confirmed…"* `[FRAME t1600.jpg]`.

**SM2 — Free stage first, paid stage quoted, exclusions itemized and overrulable.** P8. Applies to the Topic Scanner (`73 qualify / 57 excluded`, then `37 credits (you have 10,320)`) and to the Hook Machine (balance stated before scope). Corollary rule from B: *"this workflow doesn't actually cost any credits… so you can pretty much run this infinitely"* `[B 15:20]` — free workflows are labelled as such so they can be scheduled.

**SM3 — Name the trap inside the chart.** P9. Every ranked visual he ships carries an adjacent callout naming the wrong conclusion it invites: `Two traps, said plainly` / `≥20× (Kassir-inflated)` / `Retire this one` / `What the dashboard can't tell you` / `don't judge … at 24 hours`.

**SM4 — Give it a name; the name slot is mandatory, the name itself is not.** P17. "Swap the name if you have a better one, **but it needs one**." The machine proposes plus an alternate ("The 2x2 Script" / "The Lock-In Architecture"), the human picks, the slot cannot be empty. Same shape in the bucket names (The Filler Reckoning, Why It Failed, The Consult Room, Recovery Honestly) and the chaos names (The $200,000 face, The mirror lecture, The Kris Jenner effect re-aimed).

**SM5 — One dominant recommendation with the reason, plus a bench.** Every skill's output has a starred pick and a reserve: *"The recommended combo. Film Hook 1 + Text A + Script 1 first… it mirrors the 74.5x reference format most closely"* `[FRAME t3722.jpg]`; ⭐ on 2 of 6 narrow buckets with the rest labelled "bench"; "pick one for batch 1, the rest go in the reserve"; ⭐ gold-ring on exactly 3 cells in the format matrix. He never presents a menu without a pick and never presents a pick without the losers kept warm.

**SM6 — Ship a numbered state summary and a one-word next trigger.** P21. `Step 1.3 done` → manifest → one-line English state → `Next is step 1.4…` → **"Say 'go' and I'll route you."** The user's cost of continuing is one word.

**SM7 — Demonstrate the standard instead of describing it.** P2, P20. He shows a 350-word interview answer rather than saying "be specific." He runs the whole strategy half as a plastic surgeon rather than saying "this generalizes." He renders his own hook-scan on screen rather than saying "study your winners."

**SM8 — Cap the tool's ability out loud, then design for the cap.** P14. Three separate disclaimers in six minutes, followed by the manual last-mile demo and the `engine-builder` diff loop. The honest ceiling is load-bearing architecture, not modesty.

**SM9 — Every number is an outlier multiple, and the denominator is stated.** `Outlier = N× that channel's normal` `[FRAME t2645.jpg]`. This normalizes across a 51K-follower surgeon and a 4.18M-follower surgeon in the same table, which is the only reason the Top-50 can mix them.

**SM10 — Colour is the same everywhere.** Ring red→orange→amber→light blue→dark blue in the bullseye; the *same* colours re-used to tint bucket bars in the Topic Scanner, dart zones in the 7-video batch, and slot cards in the Channel Coach. Green = white space / open lane / proven, amber = contested / test, red = crowded / danger. One palette across six artifacts, so a colour read in one is legible in all.

---

## 5. Quality rubric — how a Kallaway strategy artifact is judged

Derived from what he praises, what his artifacts enforce, and what he corrects. Nine criteria; 1–5 each; **any single 1 is a fail regardless of total.**

| # | Criterion | Fail (1) | Pass (3) | Kallaway-grade (5) |
|---|---|---|---|---|
| **R1** | **Evidence provenance** — every claim traceable to a named source with a number | Assertions with no source ("this format works well") | Sources named | Every row carries channel + outlier + views + a deep link; altitude of each reference declared; skipped tiers reported with the reason (P10) |
| **R2** | **Falsifiability** — the artifact can be wrong in a stated way | Unfalsifiable synthesis | Claims are checkable in principle | Claims scored against data ("four confirmed, one contested-then-confirmed"), exclusion rows carry reasons, human can overrule any call (SM1, P8) |
| **R3** | **Named mechanism** — the concept has a coined term the operator can own | Descriptive label ("3 mistakes creators make") | A memorable name | A coined term + an alternate + a human veto; name earned by a controlled finding, not taste (P17, SM4) |
| **R4** | **Actionability at the beat level** — an operator can film from it without asking a question | "Use a strong hook" | Ordered structure | Named beat + its job + median seconds from cited winners; recommended combo stated; pairing rule given (P12, P13) |
| **R5** | **Anti-misread guard** — the artifact names the wrong conclusion it invites | None | A caveat somewhere | Adjacent, plain-language trap callout inside the visual, plus a stated blind spot section (P9, H10, SM3) |
| **R6** | **Cost/effort honesty** — the operator knows what this costs before committing | Silent spend | Cost mentioned | Free stage vs paid stage separated, bill quoted against balance, zero-spend decisions reported as findings (P8, SM2) |
| **R7** | **Anti-hallucination discipline** — no invented numbers, ever | Plausible numbers filled in | Uncertainty hedged | `[NEED]` markers on the exact slots refused, with the placeholder shown and why the slot matters; `Gaps` section shipped (H5) |
| **R8** | **Freshness / anti-self-plagiarism** — output does not repeat the operator's own recent surface | Recycles the operator's last winner | Some variety | Rinse window enforced (~60 days), rinsed phrases struck through in the bank, remix happens at construction level, and the omission is *reported* (P11) |
| **R9** | **Handoff contract** — the next step knows what to read | Ends with prose | Names a next step | Numbered step ID, named file, itemized manifest, `Read by:` consumer list, one-line English state, one-word continue trigger (P21, SM6) |

**Two override rules he demonstrates:**
- *Identity beats a neutral metric.* He keeps "self-demonstrating meta technique" (1.00×, i.e. baseline) as a bucket rule because it is his positioning `[FRAME t4725.jpg + t3630.jpg]`. A metric that says "no effect" does not veto a positioning commitment; a metric that says "0.6×" does.
- *Maturity window before demotion.* No verdict on a video at 24 hours (H9).

---

## 6. On-screen artifact ledger

*This is the surpass spec. Everything below is read from rendered frames; my upscaled crops are in `.tmp/zoom/`. Bracketed text = partially legible.*

### 6.0 — Setup surface

**Skill delivery** `[frame_0018.jpg, t=03:56]` — macOS Finder, window title **"Strategy & Positioning"**, five files with the Claude starburst icon: `niche-interviewer.skill`, `unique-positioning-builder.skill`, `bullseye-builder.skill`, `topic-scanner.skill`, `format-finder.skill`. Dragged into a Claude chat as attachments; a sixth (`growth-system.skill`, the orchestrator) is added in the chat `[A 03:21–03:34]`. Sidebar shows Downloads selected; user folder `ankur`. Zoomed detail at `[FRAME t0752.jpg]` shows the `.skill` package icon at full size (red/orange starburst on a document sheet).

**Kickoff prompt** `[A 03:35–03:50]` — *"I want to run the content growth system. I am a [avatar] … that wants to use content to drive leads and clients for my practice."* Model: **Fable 5**, mode: **co-work**. Every subsequent Claude frame shows `Fable 5  High` in the composer footer.

---

### 6.1 — Niche Interviewer

**Format.** Pure conversation in the Claude thread — serif body type for the assistant, grey rounded bubbles right-aligned for the user's answers, with a `Show more` / `Show less` expander on long answers `[FRAME t0604_upper.jpg, t0604_b.jpg]`. Six question blocks, each labelled (`Block 2: the Chair Test`). Questions run 60–90 words and end in an instruction verb (`Ramble.`).

**Output artifact — the 7-attribute self-assessment table** `[FRAME t0740.jpg / t0746.jpg, ~07:40–07:50]`.

Preamble: *"Here's the 7-attribute self-assessment drafted from everything you said. One round of corrections, then I write the doc. Remember: this is a hypothesis from self-knowledge — the next step (Unique Positioning Builder) crosses it against what LA facial surgeons are actually posting to find the real white space. Don't treat it as settled."*

Three columns — **Attribute | Strength | Evidence** — seven rows, verbatim:

| Attribute | Strength | Evidence |
|---|---|---|
| Topic selection | **Strong** | Failure/revision, filler-as-anti-facelift, ghost surgery, "too young" myth, GLP-1 face — topics the sellers avoid |
| Substance depth | **Strong** | Fellowship-trained, published on deep plane, teaches it; can explain anatomy, not hand-wave |
| Unique stories / proof | **Strong** | ~1/3 revision practice = decade-long library of how facelifts and noses fail; 8 yrs face-only |
| Avatar specificity | **Strong** | Elizabeth is person-level; most surgeons talk to "everyone" |
| Delivery style | **Possible** | "Draws on the mirror," patients say "first person who made it make sense" — untested on camera |
| Storytelling format | **Possible** | Case-story / "why this failed" narratives are natural; no format proven yet |
| Visual format | **No (yet)** | No content history; mirror-drawing could become a signature visual, unproven |

**Craft notes.** Three-value ordinal scale (`Strong` / `Possible` / `No (yes)`) rather than a numeric score — it maps to "already have evidence" / "plausible, untested" / "would have to build." Evidence cells are compressed clauses lifted from his own answers, not paraphrase. The two `Possible` rows both end in "untested on camera" / "no format proven yet" — the scale's meaning is *what kind of proof is missing*, not *how good it is*.

---

### 6.2 — Unique Positioning Builder

**(a) The competitor watchlist table** `[FRAME t1050.jpg, ~10:50]`. Columns: `# | @handle | platform | followers | why-they-matter`. Tier A rows 1–8, then a Tier B block `[A 10:57]`. Verbatim rows 1–7:

| # | Handle | Plat | Followers | Note |
|---|---|---|---|---|
| 1 | @drkevinsadati | IG | 265K | OC facial plastic surgeon; deep plane, neck, brow, eyes; testimonials + recovery journeys. **Closest analog.** |
| 2 | @drkassir | TikTok | 266K | NY facial plastic; deep plane + rhino + celeb case analysis. Rhino overlap. |
| 3 | @drradyrahban | IG | 239K | Beverly Hills plastic surgeon; candid, anti-trend, "how to research a surgeon," names *filler fatigue*. **Nearest to your "honest explainer" lane.** |
| 4 | @drbentalei | IG | 568K | Beverly Hills; facial rejuvenation, filler long-term implications. Big local incumbent. |
| 5 | @penningtonfacialplastics | IG | 52K | Female facial plastic surgeon; deep plane vs SMAS, filler fatigue, neck aging, "not overdone." **Small but talks exactly to Elizabeth.** |
| 6 | @chesnut.md | TikTok | 51K | Facial rejuvenation surgeon; surgery vs filler comparisons, natural results. |
| 7 | @drgarylinkov | YT Shorts | 1.19M | NY facial plastic; celeb facelift/rhino breakdowns. **Proves the celeb-analysis format at scale.** |

The note column is doing three different jobs across rows — nearest analog, nearest *lane* competitor, and format proof point — each stated in ≤12 words with the relational verdict bolded in effect. Claude writes this list into a Sandcastles watchlist via MCP without being asked `[A 11:24–11:38]`.

**(b) The Positioning Wheel** `[FRAME t1505.jpg / t1600.jpg / t1620.jpg / t1525.jpg / t1532.jpg, ~14:50–16:35]`. Dark navy (#0f1730-ish) interactive HTML, rendered in Claude's artifact pane.

- **Title:** "**Positioning Wheel** · Dr. Kallaway · facial plastic surgery · **18 channels studied**"
- **Standfirst:** *"Seven wedges = the seven ways a creator can stand out. Each bubble is a competitor who is **strong** in that wedge (size = followers). Red = crowded, green = open lane. The star marks where the data says you should plant your flag. Tap a wedge to learn what it means, who's there, and what it means for you."*
- **Legend (2×2):** ● Crowded — hard to stand out (red) · ● Contested — someone's there, beatable (amber) · ● White space — open lane (green) · ★ = claim this
- **Honest caveat line:** *"No wedge is fully green in this niche — the open lanes live [inside the] wedges; tap one to see them."*
- **The chart:** a 7-wedge radial sunburst. Wedges (clockwise from top-right): **Topic selection · Substance depth · Unique proof · Audience specificity · Delivery style · Storytelling format · Visual format.** Each wedge label carries a sub-line "N of 18 competitors here". Wedge *fill* encodes saturation (deep red = crowded, olive/gold = contested). Centre hub is a dark disc labelled **"Dr. Kallaway / face-only · [BH]"**. Inside each wedge: competitor bubbles, radius ∝ follower count, fill = that competitor's status in that wedge (red/amber/green/violet). Hovering a bubble shows a black tooltip `@drkevinsadati · 265K` and **dims every bubble outside the hovered wedge** `[FRAME t1620.jpg]`. A gold ★ badge sits in each wedge where he should plant.
- **Below the chart — "Start here":** *"Tap any wedge. Or, if you're new to all this: a 'positioning attribute' is simply one lever you can pull to be different from every other surgeon on Instagram — what you talk about, how deep you go, what proof you show, who you talk to, how you come across, the shape…"*
- **Wedge detail panel** (one per wedge, appears below on tap): wedge name + ⭐; a pill-shaped status badge `CONTESTED — someone's there, beatable · 8/18` (amber; red and green variants exist); then five numbered sections in letterspaced small caps:
  - `1 · WHAT THIS EVEN IS` — plain-language definition with a concrete contrast. Substance depth: *"How far past the surface the explanation goes. Surface = 'trust the process.' Deep = 'here is the layer under the muscle and why pulling skin alone stretches back.'"* Visual format: *"How it's shot and edited — raw selfie in the office, polished podcast clip, inside the operating room, before/after slideshow, drawing on a whiteboard."*
  - `2 · THE FULL MENU OF OPTIONS` — italic, middot-separated enumeration. Substance depth: *"Motivational/surface · disease philosophy · tactical how-it-works · mechanism/anatomy · complication protocol."* Visual format: *"Office talking head · patient two-shot · before/after slideshow · in-OR/POV · podcast clip · greenscreen + photos · vlog/day-in-life · faceless clinical close-up · drawing on mirror/glass · text-on-screen · trend-audio reveal."*
  - `3 · WHAT WE'RE SEEING IN YOUR NICHE` — prose naming who owns what, then a row of coloured @handle chips. Substance depth: *"Most channels are surface-to-mid (procedure lists, rankings, reassurance). Depth leaders: Chesnut (mechanistic), Nayak (technique detail), Rahban (decision-trees), Dharb (complications), Mustoe (one clean concept, repeated). **Nobody draws anatomy for a patient. Nobody explains the failure mechanism.**"* Chips: ● @chesnut.md ● @nayakplasticsurgery ● @drradyrahban ● @dr[saj]dharb ● @drthomasmustoe. Visual format: *"Talking head + before/after + patient two-shot is the default. Podcast clips: Talei, Ourian, Chesnut, Rahban. OR/POV: Chesnut, Kassir, Sadati, Tripathi. Greenscreen celeb: Mustoe. Vlog: Karam, Fairchild. Faceless clinical close-up: Dharb (9.9×)."*
  - `4 · THE WHITE SPACE` — [partially legible]
  - `5 · [WHAT IT MEANS FOR YOU]` — UNCONFIRMED
- **Left pane (Claude prose synthesis)** `[FRAME t1600.jpg]`, partially legible: *"[of] your seven claimed edges: four confirmed, one contested-then-confirmed (proof — [revision is] table stakes, but the revision library is an [edge])… delivery: 'honest' is already claimed by [Rahban]'s load — your open register is calm teacher… [recovery] diaries are saturated — your open shapes are [the consult room]. **Angle:** the Beverly Hills face-only surgeon who [explains] visually, and without selling — to the woman [on filler] and is quietly wondering. Elizabeth has [nobody] speaking to her by name (Pennington, 9K views, [nobody in the] pool touches revision-of-others'-work, ghost [surgery], 'too young,' or GLP-1 face. … [Rahb]an (4.18M, Kris Jenner beside him) is telling [celebrity] surgery. Talei is the local deep-plane brand. [Ches]nut owns the anti-filler concept nationally. … you're the only one who shows her why, layer [by layer, and something she'd] send to her friend in the private Facebook [group]…"*
- **Export row:** `Download and open` (Chrome icon) and `Google Drive`.

**Why this is the surpass target.** The wheel is not a chart with a caption — it is a *teaching object*. Five numbered sections per wedge, in a fixed order that goes definition → option space → current occupancy → gap → implication. A reader who has never heard the word "positioning" can use it, and a reader who has can audit it against named handles.

---

### 6.3 — Bullseye Builder

**(a) The Elizabeth Bullseye** `[FRAME t1730.jpg / t1820.jpg, ~17:30–18:30]`.

- **Title:** "**The Elizabeth Bullseye** · Dr. Kallaway · face-only, Beverly Hills" — *named after the avatar, not the framework.*
- **Standfirst:** *"Ring 1 is the one person you speak to in every video. You **aim** your videos at Rings 2–4, where the audiences are real but still recognize themselves. The algorithm watches who engages, learns who your channel is for, and expands your reach outward for you. **Define. Hit. Expand.**"*
- **The chart:** five concentric filled circles, labels on the ring band itself, dark navy field:
  `5 · All beauty & skincare` (dark blue) → `4 · Women 35+ aging-face curious` (light blue) → `3 · Women considering facial surgery` (amber) → `2 · Filler-fatigued women 45–65` (orange) → `1 · Elizabeth` (red, centre, with a ✓ glyph)
  Three white dart markers (white ring + black centre) land in rings 2, 3 and 4.
- **Animation caption:** *"Tap a ring for its card. Watch: dot pulses into Ring 1 (Define), darts land on Rings 2–4 (Hit), rings light up outward (Expand)."* — the animation literally performs the three-word thesis.
- **Ring card (below, updates on tap):** ring number in the ring's colour + ring name; one-line definition (*"Women [40]–65 actively considering any facial surgery — facelift, neck, eyes, nose, revision"*); then:
  - `CONSTRAINT RELAXED VS. THE RING INSIDE` → **Injectable history**
  - `RELATIVE AUDIENCE SIZE` → amber horizontal meter
  - `CONVERSION PROXIMITY (HOW CLOSE TO A $500 CONSULT)` → green meter
  - `COMPETITION DENSITY` → red meter, with a text tail: *"Crowded — Nayak, Sadati, Talei, Karam, Kassir"*
  Ring 5's card reads: *"The whole beauty internet — skincare, makeup, anti-aging, any age, gender, or i[ntent]"* / constraint relaxed: **"Gender + age + intent — everything."**
- **Left pane table:** `Constraint relaxed | Size | Converts | Competition` (reproduced in P4).

Three meters, each labelled with the *business* meaning rather than the metric name — "conversion proximity (how close to a $500 consult)" is the parenthetical that makes the meter mean something.

**(b) The topic-bucket tables** `[FRAME t2135.jpg / t2230.jpg, ~21:35–22:35]`.

*Narrow buckets* — columns `# | Bucket | Ring | Job | Example topics`. IDs `N1…N6`, ★ on the two chosen:

| # | Bucket | Ring | Job | Example topics |
|---|---|---|---|---|
| N1 ★ | **The Filler Reckoning** — what years of injectables actually did to your face | 2 | Speaks to Elizabeth's exact history; converts the "surgery or more filler?" woman | *"The under-eye 'fat' you've had for six years might be filler"* · *"Why your face got heavier, not younger, after 45"* |
| N2 ★ | **Why It Failed** — anonymized revision autopsies: how facelifts and noses go wrong | 3 | Your unfair advantage; nobody runs it; builds trust through failure honesty | *"This is what a pulled facelift looks like — here's the layer that got skipped"* · *"Why revision rhino has half the tissue and twice the work"* |
| N3 | **How to Vet a Surgeon** — credentials, anesthesia, facility, ghost surgery | 3 | Consumer-protection authority; unclaimed lane; high trust | *"'Board-certified cosmetic surgeon' vs 'plastic surgeon' — one can be a weekend course"* · *"Ask who's actually holding the scalpel"* |
| N4 | **The Consult Room** — what she asked me, and the question under the question | 2 | Reenacts Elizabeth's real fears in her language | *"'Will I look like myself?' is the only question"* · *"What to tell your husband, your kids, and school pickup"* |
| N5 | **Recovery, Honestly** — what two weeks really means | 3 | Table stakes the niche rewards (Sadati 15.6×, Fairchild 30×); needed for proof | *"Two weeks is when you can hide it, not when you're healed"* · *"Day 3 is the day everyone panics"* |
| N6 | ["too young"] | — | — | — |

Broad buckets `B1…B4` (How Faces Actually Age ★, The Surgical Read: doctor vs influencer, machines & money, celebrity read) `[A 21:50–22:20, recap at FRAME t2230.jpg]`.

*Chaos table* — columns `# | Chaos idea | Kind of wild | A win teaches you` (reproduced in P6).

The `Job` column is the invention: it states *what the bucket is for in the funnel*, separate from what it's about. N5's job is explicitly "table stakes the niche rewards … needed for proof" — a bucket kept for credibility, not conversion, and labelled as such.

**(c) The 3-2-1 mix / 7-video batch** `[FRAME t2315.jpg, ~23:15]`.

- **Header:** "…7-video batch — *Two narrow buckets on Rings 2–3 (trust + conversion), one broad bucket on Ring 4 (reach), and one violet chaos dart that can land anywhere in Rings 1–4 — never Ring 5. Run it for 2–3 batches, then let the data rebalance it.*"
- **Tabs:** `Batch 1 plan` | `After 2–3 batches (example rebalance)`
- **The chart:** the same 5-ring bullseye, but with **bucket zones** drawn as irregular blobs overlapping rings, each labelled with its bucket name and containing numbered darts (1, 2) for its two videos: *The Filler Reckoning* (red blob, Rings 1–2), *Why It Failed* (amber blob, Rings 2–3), *How Faces Actually Age* (blue blob, Ring 4), plus one violet dart floating alone.
- **Two warning bands:** across the top of the outer ring, in red caps: **"RING 5 · TOO BROAD — DANGER: viral with the wrong avatar"**. In the centre disc: **"RING 1 · too narrow"**.
- **Footer:** *"Tap a bucket zone or dart."*
- **Chat-side deliverables list:** `Bullseye 321 mix — Code · HTML → Download and open` · `Bullseye sourcing map — Code · HTML → Download and open` · `Bullseye map — Document · MD → Google Drive`. Above them: `Created artifact: bullseye-321-mix-dr-kallaway`.

**(d) Inspiration Sourcing Map** `[FRAME t2405.jpg, ~24:05]` — reproduced in full at P7. Same 5-ring geometry, re-labelled by *sourcing permission*: an outer hatched "CRAFT ZONE" band overlapping everything, "RING 4 · topics for the BROAD bucket (re-aimed [at Ring 3])", "RINGS 1–3 · topics for the NARROW buckets", footer "Ring 5 = craft inspiration ONLY. Never source topics here." Reusing the exact same graphic with a different legend is the design move — one mental model, three read-outs (audience / batch plan / sourcing rights).

---

### 6.4 — Topic Scanner

**(a) Stage report** `[FRAME t2535.jpg, ~25:35]` — reproduced in P8. Note the Claude activity line above it: *"Updated tasks, used a skill, ran an agent."*

**(b) Topic Scanner HTML — ranked topic buckets** `[FRAME t2615.jpg, ~26:15]`. Dark navy. Each row: bucket name (⭐ prefix if chosen) + sub-line `Ring N · M channels` + a colour-coded horizontal bar (bar colour = the bucket's ring colour) + outlier multiple + `N vids · X.XM` views. Selected buckets get a lighter card background and a border.

| Bucket | Ring · channels | Outlier | Volume |
|---|---|---|---|
| ⭐ How Faces Actually Age | Ring 4 · 3 channels | 16.7× | 3 vids · 4.3M |
| Surgeon Philosophy & Vetting | Ring 3 · 4 channels | 12.1× | 5 vids · 3.4M |
| Recovery, Honestly | Ring 3 · 3 channels | 12.1× | 6 vids · 1.6M |
| The Surgical Read (celeb) | Ring 4 · 2 channels | 11.7× | 3 vids · 1.6M |
| ⭐ The Filler Reckoning | Ring 2 · 4 channels | 11.1× | 6 vids · 1.7M |
| Facelift Patient Journeys | Ring 3 · 4 channels | 10.9× | 15 vids · 3.7M |
| Am I Too Young? | Ring 3 · 2 channels | 9.1× | 2 vids · 0.4M |
| ⭐ Why It Failed (revision) | Ring 3 · 2 channels | 7.8× | 3 vids · 0.3M |

Rows expand to show their constituent videos as `outlier · @handle · title-fragment`, e.g. *"17.8× · @tonyyounmd · Why can't you just put a stitch in to lift the face? Here's…"* / *"16.7× · @drjohndiaz · Aging isn't just skin deep. Deeper tissue layers descend — t…"* / *"8× · @drwmkaram · Ranking the 10 biggest contributors to facial aging"*.

Below: the red-bordered **Two traps, said plainly** callout (P9), then a `Format buckets` section (same treatment for formats).

Note: he selects two buckets that are *not* the top performers (Filler Reckoning 11.1×, Why It Failed **7.8×** — the lowest row on the board) because they're the ones his unfair advantage supports. Performance ranks the pool; positioning picks from it.

**(c) `top-50.md`** `[FRAME t2645.jpg / t2710.jpg, ~26:45–27:15]`. Rendered as a document in the artifact pane, serif body.

- **Header block (italic):** *"Step 1.4 of the 0→100K Growth System. Created 2026-08-16. Source: Sandcastles watchlist 'Plastic Surgeon Clinic,' 180-day lookback, sorted by outlier score. Read by: topic-brainstormer, format-finder, spoken-hook-machine, text-hook-machine. Full analysis payloads live in Sandcastles (click 'analysis'); the merged JSON export is `top-50-analysis.json`."*
- **Key line:** *"★ = one of the 3 chosen buckets. ✓/✗ = qualifies for Elizabeth's niche (✗ rows carry the reason). Outlier = N× that channel's normal."*
- **Section head:** "The top 50 ✓ (working set)"
- **Table columns:** `# | ✓ | Topic bucket | Video | Channel | Views | Outlier | Link | Analysis` — last two columns are live hyperlinks (`video` → the platform, `analysis` → the Sandcastles deep-analysis page).

| # | ✓ | Bucket | Video | Channel | Views | Outlier |
|---|---|---|---|---|---|---|
| 1 | ✓ | Surgeon Philosophy & Vetting | Straight to Why podcast: artistry meets anatomy; invented the modern facelift | laradevganmd | 894,633 | 171.5× |
| 2 | ✓ | Rhinoplasty (celeb) | A nose that needs no introduction… Cast removal couldn't come quick enough, I we… | drkassir | 829,000 | 152.0× |
| 3 | ✓ | Rhinoplasty (celeb) | Throwback Thursday pink hair… Brianna LaPaglia's nose transformation one week po… | drkassir | 690,200 | 128.1× |
| 4 | ✓ | Facelift Patient Journeys | "This was the best decision I ever made" 63yo patient 13 months after full facia… | drkassir | 647,600 | 105.8× |
| … | | | | | | |
| 9 | **✗ too broad: hot take** | — | — | — | — | — |
| 12 | ✓ | Facelift Patient Journeys | My AuraLyft story from start to finish (Tricia) | drbentalei | 744,792 | 21.7× |
| 13 | ✓ | The Surgical Read (celeb) | Celebs are sometimes lucky (Ali Larter at 50) | drpreemtripathi | 384,900 | 21.4× |
| 15 | ✓ | ★ How Faces Actually Age | Why can't you just put a stitch in to lift the face? Here's the answer! | tonyyounmd | 3,241,217 | 17.8× |
| 16 | ✓ | ★ How Faces Actually Age | Aging isn't just skin deep. Deeper tissue layers descend — the lift is structura… | drjohndiaz | 83,754 | 16.7× |
| 17 | ✓ | Facelift Patient Journeys | At 72 years young, this biological scientist is still actively working… Preserv… | drkevinsadati | 97,251 | 15.7× |
| 18 | ✓ | Recovery, Honestly | Day 1 with patient Debbie after deep plane… | drkevinsadati | 97,415 | 15.6× |

Excluded rows are **struck through** with the reason in the ✓ column (`✗ too broad: hot take`). Row 15 vs row 16 is instructive: 3.2M views at 17.8× and 84K views at 16.7× sit adjacent, because the outlier normalization strips channel size.

His own-niche version `[A 32:00–32:30]` is identical in structure with buckets `AI × Content ≠ SEO / Storytelling & Scripting ★ / On-Camera Presenting` and rows like `#11 ✓ Storytelling & Scripting — realskytan "The perfect scripting structure" (74.5×, 699K)`.

**(d) Bullseye placement view** `[A 26:10–26:22]` — a toggle in the same artifact that re-plots each of the top-50 buckets onto the 5-ring bullseye, so you can see at a glance which winners sit in Ring 5 (avoid) vs Rings 2–4 (usable). UNCONFIRMED on exact styling — I did not capture a clean frame.

---

### 6.5 — Format Finder

**(a) Sandcastles Collections** `[FRAME t2820.jpg, ~28:20]`. Header: "**Collections** / Browse curated collections of standout videos grouped by format, hook, and story structure." + `Search collections`. Grid of gradient tiles (green→black and blue→black diagonal gradients), each carrying: a small category pill on the tile (`VISUAL HOOKS` / `FORMATS`), the collection name set large, bold, centred in white; and beneath the tile: a letterspaced breadcrumb (`VISUAL HOOKS · SUBJECT MOTION`, `FORMATS`, `VISUAL HOOKS · PATTERN INTERRUPT / …`), the collection title, and a video-count pill. Visible collections: **3P Crash Zoom** (2 videos) · **About Me** (12 videos) · **Anticipated/Impending Disaster** (3 videos) · **A vs B Comparison** (12 videos) · **Beat Match Visual Switch** (11 videos) · **Breakdowns / Explainers** (11 videos). Clicking through gives examples across niches with transcript, analysis and playback `[A 28:40–29:05]`. This is Altitude 4 in P10.

**(b) The Format Finder matrix** `[FRAME t3020.jpg, ~30:20]`. Dark navy heatmap grid.

- **Legend line (above the grid):** *"Rows = storytelling structure (how the words are organized). Columns = visual layout (how it's shot). Cell = median outlier of the winners that live there (count in small). Green dashed = empty and worth a bet. Gold ring = your three test picks. Tap a cell."*
- **Columns (visual execution):** `V1 talking head · V2 podcast clip · V3 surgeon+patient · V4 marking on face · V5 macro close-up · V6 POV/OR · V7 greenscreen · V8 B-roll/stills`
- **Rows (storytelling structure):** `S1 case study / journey · S2 Q&A / conversation · S3 problem→solution FAQ · S4 myth-kill / contrarian · S5 anatomy breakdown · S6 celebrity read · S7 silent macro · S8 ranking · S9/10 reveals` — **then two invented rows: `Case Autopsy (new)` and `Consult Room (new)`, whose cells all read `open`.**
- **Cells:** filled cells show `N.N×` over `M vid(s)`; empty cells show `–`; white-space cells show `open` on a green dashed outline; picks carry a gold ring and a ⭐.
- **Colour scale (footer legend):** `≥20× (Kassir-inflated)` red · `10–20×` orange · `<10×` gold · `white space` green dashed · `your pick` gold ring
- **Footer:** *"Tap a cell to see the model videos."*

Sample readings: S3×V1 = 29.8× (1 vid, gold-ringed pick) · S4×V1 = 37.5× (2 vids) · S9/10×V4 = 47× (1 vid) · S3×V6 = 30× (1 vid) · S1×V3 = 10.9× (12 vids — the crowded default) · Case Autopsy × V3 and × V4 = ⭐ open.

The 12-vid cell at 10.9× versus the 1-vid cell at 47× is exactly the read the artifact is built for: volume and multiple are separate axes, and white space is *adjacent to* the high-multiple/low-volume cells.

---

### 6.6 — Video Maker (production loop)

**(a) The interview** `[FRAME t3455.jpg, ~34:55]`. His brain dump (grey bubble, `Show more` expander), verbatim opening:

> "Alright, let's take number 11 from realskytan about the video scripting architecture. Here are my raw thoughts on this idea. I think the ultimate scripting architecture goes as follows: 1. You have the hook. 2. You have the lock-in zone. The hook is one line, and the lock-in zone is two to four lines where you build and compound trust. You have some credibility anchor. You basically justify why the upcoming information is going to be valuable. 3. You have the first block, which is one contrarian statement or some…"

The skill's reply — a locked-row echo plus exactly two questions:

> "Row #11 locked: realskytan 'The perfect scripting structure' (74.5x, 699K) → Storytelling & Scripting ★ (your Storytelling bucket). One question before I build: **work only from your brain dump, or research too?**" → `Research too`
> "**Lead-magnet trigger word for the CTA close (your scripts never ship without one)?**" → `SCRIPT`

Then: `Ran 10 commands, updated tasks, searched the web · 1 note` with two dark artifact thumbnails.

**(b) `Substance sheet — The 2x2 Script`** `[FRAME t3620.jpg / t3630.jpg, ~36:14–36:45]`. Rendered as an MD document (title bar `Substance  MD`, `Google Drive` export button).

- **Source line:** *"Source: Kallaway brain-dump (2026-08-17), row #11 of growth-system/top-50.md (realskytan 'The perfect scripting structure', 74.5x). Mode: research too. **Research lines are marked [R]; everything [else is yours].**"*
- **`Core claims (Kallaway)`** — 8 numbered items, his brain dump normalized into declarative claims:
  1. The ultimate short-form script architecture has six parts in order: **Hook → Lock-in zone → Block 1 → Re-hook 1 → Block 2 → (Path A: conclusion + CTA | Path B: Re-hook 2 → Block 3 → CTA).**
  2. Hook = ONE line.
  3. Lock-in zone = 2–4 lines that build and compound trust; a credibility anchor + a justification of why the upcoming information will be valuable.
  4. Block 1 = one contrarian statement (or interesting fact) + 3–4 supporting sentences.
  5. Re-hook 1 = the transition between Block 1 and Block 2.
  6. Block 2 = one contrarian statement + 3–4 supporting sentences proving it.
  7. Two exits: short video → conclusion → CTA; longer video → Re-hook 2 → Block 3 → CTA.
  8. **WHY it works: two dopamine moments (hook, re-hook 1) + two ahas (one per block).**
- **`Coined name (proposed)`** — *"'The 2x2 Script' — two dopamine hits, two ahas. Alternate: 'The Lock-In Architecture.' Kallaway picks."*
- **`Own-channel substance reused (Altitude 1 — his words, safe to use)`** — each bullet = concept name, outlier score, and the reusable line:
  - Modern Story Arc (9.9×): start at 70/100, spike to 90/100 in the first 5–10s, then peak-release-peak; *"re-hooking as long as you can."*
  - Double Tap (4×): *"the reason people swipe away is because they get confused"*; brain releases the most dopamine right before an answer is revealed.
  - Dopamine Addiction Loop (18.5×): stakes → big question → headfake → rehook; *"great stories have cascading loops."*
  - Triple Hook (17×): content → lean → contrarian snapback.
- **`Research fills [R] (used only in the "with research" toggle; each cited)`** — each with a `Plain-English:` gloss (H6):
  - `[R1]` Curiosity states activate the dopaminergic midbrain and hippocampus, and boost memory for what comes next — Gruber, Gelman & Ranganath, *Neuron* (2014). *Plain-English: the brain rewards the anticipation of an answer, and remembers what follows.*
  - `[R2]` TikTok for Business (widely cited): 63% of the highest click-through videos hook the viewer within the first 3 seconds. *Plain-English: everyone optimizes the first 3 seconds; almost nobody designs seconds 3–12 (the lock-in zone).*
  - `[R3]` Information-gap theory of curiosity — Loewenstein (1994): curiosity is the felt gap between what you know and what you want to know; the re-hook manufactures that gap on purpose.
- **`Customer language / beliefs to overcome`** — belief → reframe pairs, plus the villain:
  - *Belief: "hook, value, CTA" is the whole structure. → Reframe: that has ONE dopamine moment and then flatlines.*
  - *Belief: after the hook you should dump value fast. → Reframe: seconds 3–12 are for compounding trust (lock-in), not value.*
  - *Villain = the flat middle (confusion/boredom), never the viewer's talent.*
- **`Gaps`** — `[NEED]` items (H5).

**(c) The Output HTML** `[FRAME t3722.jpg / t3735.jpg, ~37:20–38:20]`. Dark navy, title bar `Output  HTML`, `Download and open`.

- **Title:** "**The 2x2 Script — the ultimate short-form script architecture**"
- **Meta block (three labelled lines):**
  - `Bucket:` Storytelling & Scripting ★ (channel bucket: Storytelling — sub-shape C, named principle + psychology + live demo; Script 2 borrows sub-shape A, paradigm flip)
  - `Trigger word:` SCRIPT
  - `Pairing:` Film Hook 1 with Text A and Script 1 (the Architecture Walkthrough) first — it mirrors the 74.5× reference format most closely.
- **`SPOKEN HOOKS · WITH THEIR ON-SCREEN TEXT`** — three hook blocks. Each: `HOOK N` label in small caps, the spoken line set very large in white on the left, and **two phone-shaped mock cards on the right** rendering the paired text-hook options in their real typographic treatment, each captioned `Text A` / `Text B`. (Reproduced in P13.)
- **`SCRIPTS · READ THEM THE WAY YOU'D READ ON SET`** — a toggle pill pair `context only` (active, red) / `with research`, then **two side-by-side script cards**:
  - Left: **Architecture Walkthrough** (amber title). Body set in short paragraph beats, one thought per line, generous leading — readable off a teleprompter. One line carries an olive/gold **highlight**: *"I call it the 2x2 Script, and it's underneath almost every outlier video I've reverse-engineered — whether the creator knows it or not."* (This is the `[NEED]`-flagged line — the highlight IS the flag.)
  - Right: **Paradigm Flip (Old skeleton vs the 2x2)** (amber title). *"The reason people watch your hook and still scroll is you have no lock-in zone. / Everyone teaches the same skeleton: hook, value, CTA. / And it kind of works — right up until second three, when the hook is over. / Because that structure has exactly one dopamine moment, and then it flatlines. / So instead, use this: the 2x2 Script. Two dopamine hits, two ahas. / The hook stays one line. It breaks the pattern, that's it. / But right after it comes the lock-in zone — two to four lines where you compound trust. / A credibility anchor, then a reason the next thirty seconds are worth their time. No value yet. Just lock them in. / Then block one: a contrarian statement plus three or four lines proving it. First aha."*
- **File shelf (chat side):** `Output — Code · HTML → Download and open` · `Script architecture walkthrough — Document · MD → Google Drive` · `Script paradigm flip — Document · MD → Google Drive` · `Substance — [MD] → Google Drive`.

**The Video Maker contract in one line:** *substance sheet → 4-altitude reference pull → 3 spoken hooks each paired with 2 text hooks → 2 full scripts (research-toggleable) → one HTML artifact + four MD files + a narration that says what it refused to do.*

**(d) `See the machine — Kallaway Marketing engines v1.0`** `[FRAME t4000.jpg / t4012.jpg / t4018.jpg, ~39:30–41:30]`.

- **Provenance sub-line:** *"96 videos in: 32 own winners · 14 own losers · 50 niche top-50 · 16 spoken formats · 9 text formats · 8 script templates · built 2026-08-17"* — note **own losers are an input.** (Corroborated in B: *"I like to analyze my entire channel so it has both the winners and losers to differentiate the insights from the winners"* `[B 06:12]`.)
- **Tabs:** `Spoken` | `Text` | `Scripts`

*Spoken tab:* `SPOKEN HOOK FORMATS — WEIGHTED SCORE (MEDIAN OUTLIER × EVIDENCE) · TAP A BAR`. Sixteen rows `F1…F16`, each `ID + name (⭐ if own) | bar | N.N× med · n=N`. Bar colour: orange/red for own formats, slate for niche formats. Ranked: F7 Rapid list-as-hook 42.6× (n=3) · F5 Ultimatum warning + N fix 37.8× (n=3) · F14 Demo-as-hook 33.5× (n=2) · F2 Metric-first case study 19.5× (n=11) · F10 High-stakes scenario 18.2× (n=3) · F1 Stop-doing-it callout 14.5× (n=3) · F12 X is dead / X works now 11.6× · F8 Big result, tiny time + method ⭐ 11.7× (n=2) · F13 Numbered curated list 11.5× (n=4) · F3 Scientific-absolute promise + named method ⭐ 10.9× (n=4) · F6 Absolutely-insane update 10.6× (n=9) · F9 The diagnosis ⭐ 9.9× (n=3) · F16 Insider-authority anecdote 9.3× (n=3) · F11 Addiction promise + ladder ⭐ 5.8× (n=2) · F4 Tool-into-machine reveal ⭐ 4.6× (n=6) · F15 You-can-now capability ⭐ 3.5× (n=3).
Then `POWER PHRASE CLOUD — SIZED BY PERFORMANCE · GOLD = OWN · STRUCK = RINSED (USED IN THE LAST ~60 DAYS)` (P11).

*Text tab:* `TEXT HOOK FORMATS — WEIGHTED BY PERFORMANCE`. Nine rows `T1…T9`, **names written as fill-in templates**: T1 `[Tool] Just Changed [Domain] Forever` 40.8× top (n=7) · T5 `Warning / dated ultimatum` 37.8× (n=3) · T6 `Metric proof + contrast` 26.9× (n=3) · T2 `Result in tiny time / range` 20.4× (n=3) · T3 `How to make your [X] [charged adj]` 18.5× (n=3) · T4 `Named method's parts / coined name` 17× (n=6) · T8 `A vs B / dead-vs-works` 14.7× (n=4) · T7 `Numbered resource + outcome` 11.3× (n=5) · T9 `Superlative resource` 4.5× (n=2).
Then `TOP 5 WINNING TITLES AS PHONE FRAMES` — five vertical phone cards, each with the title typeset as it appeared and the outlier beneath: *"Claude Just Changed Social Media Forever"* 40.8× · *"DON'T POST IN 2026"* 149.7× · *"30 days of content in 30 minutes"* 20.4× · *"How to make your Storytelling addictive"* 18.5× · *"THEY PULLED 30 MILLION VIEWS WITHOUT USING ADS"* 26.9×.
Footer: *"Own defaults: premium-but-clear typography · top third · 2 lines · separate from the spoken line. 16 stragglers pending (title animates in later) — see `engine-hooks-text.md` §2."*

*Scripts tab:* `SCRIPT TEMPLATES — BEAT TIMELINES (SECONDS PER BEAT)` — reproduced in full at P12.

**(e) Sandcastles Videos tab** `[FRAME t4120.jpg, ~41:20]` — header "Videos / Analyze videos from your channels to unlock deep insights and find your next idea", `Showing 100 of 105`. Left filter rail: Channels · Keywords (search captions and titles) · Outlier score (0×–100×) · Views (0–10,000,000) · Engagement (0%–100%) · Posted in last (N Months) · Platform · Browsing mode · `Save filter`. Grid cards: green `Analyzed` pill top-left, platform avatar top-right, **the thumbnail with its real on-screen text hook legible**, title, `@handle` + age, and a three-metric strip — outlier (green, e.g. `60.8×`), views (blue, `719K`), engagement (pink, `7%`). Video B's version adds a `Status: [x] Analysed [x] Unanalysed` filter and header buttons `Customize channels · Add video URL · Bulk Analyze · Filters · Sort by · Export` `[FRAME d0819.jpg, B ~08:19]`, and left nav: Research (Videos / Ideas ▸1616 / Hooks / Collections) · Create (Scripts / Projects / Exports) · Setup (Channels / Persona / Automations / Settings).

**(f) Sandcastles Hooks tab** `[FRAME t4245.jpg, ~42:45]` — a scannable list, one row per hook: thumbnail · **the hook line verbatim** · `Inspired by @handle` · a hook-type pill (`Tutorial` / `Problem` / `Authority` / `Secret Reveal Breakdown`) · outlier (green) · views (blue) · save-heart · a `Copy hook` button on hover. His own top rows, verbatim (also a voice sample):

| Hook | Type | Outlier | Views |
|---|---|---|---|
| The reason your videos don't hold attention is because you're using the wrong story arc. | Problem | 5.9× | 183K |
| This is how you get people addicted to your storytelling. | Secret Reveal Breakdown | 6.5× | 127K |
| Here's how to get people actually addicted to your content. | Tutorial | 5.1× | 97K |
| This is the best database in the world for short-form video references. | Authority | 4.9× | 95K |
| This is how you turn Claude into a social media machine. | Tutorial | 4.9× | 110K |
| Here's how to write a hook so good, it is basically unskippable. | Tutorial | 4.8× | 94K |
| Most people don't know this, but you can just turn Claude into a social media machine. | Secret Reveal Breakdown | 4.7× | 95K |
| You can now connect all your social media data directly into Claude. | Tutorial | 4.6× | 85K |
| The CEO of Instagram just gave the entire playbook for how to hack the algorithm in 2026. | Authority | 4.5× | 4.4K |

Plus a `show sections` toggle on the transcript view that segments a script into its structural blocks `[A 42:20–42:40]`.

---

### 6.7 — Learning Loop

**(a) Sandcastles Dashboard — Content Strategy Audit** `[FRAME t4550.jpg, ~45:50]`.
Top half: a daily-views bar chart + a cumulative-followers line chart + a top-videos list (thumbnail, title, platform · age, view count, a `Featured` pill).
Bottom half — the audit card: avatar + "**Content Strategy Audit** / Generated 2d ago for @kallawaymarketing" + `View report ›`.
- **Left pane:** `Performance by [Hooks ▾]` (dropdown also offers Topics / Formats / Script tactics `[A 45:35–45:45]`), sub-line *"How the videos open. Grouped by hook and broken down into reusable patterns that you can apply to your next video."* Ranked list with bars and multiples: **Tutorial 2.35×** (selected, dark green) · Secret Reveal Breakdown 1.94× · Question 1.8× · Authority 1.56× · Problem 1.18× (amber) · Trap Mistake 1.15× (amber) · List 0.9× (amber). Green above baseline, amber below.
- **Right pane:** `● SELECTED HOOKS` + the hook name, then three analytical bullets and a `SUPPORTING VIDEOS` thumbnail row. Verbatim for Tutorial:
  - *"Tutorial hooks framed as 'here's how to do X with Claude/AI tool' consistently rank among the highest performers on the channel, with several videos hitting 2.4×–4.6×, far above the channel's problem or authority hooks."*
  - *"The common thread across the best tutorial videos is a specific tool name (Claude, Sandcastles) plus a concrete slash-command or step-by-step setup, giving viewers something immediately actionable rather than abstract advice."*
  - *"Tutorials that walk through manual step-by-step processes unrelated to AI tools (like the 532 content planning method) also outperform strongly, suggesting **the step-by-step promise itself, independent of AI, drives high completion and shares.**"*

  Note the third bullet's shape: it isolates the *variable* by finding cases where the obvious explanation (AI hype) is absent and the effect persists.
- **Report config:** `Reports` tab → cadence (every 30 / 7 / 1 days) and window (last 30 / 50 videos) `[A 45:52–46:05]`. Handoff button: **`Continue with MCP`** — copies a payload that pulls the report into Claude `[A 46:40–46:50]`.

**(b) Channel Coach artifact in Claude** `[FRAME t4725.jpg, ~47:25]`. Light document, sectioned cards.
- A yellow-bordered callout above: *"…which was the fluke. **Also: don't judge the text-hook-machine video (1.4×) at 24 hours.**"*
- **`Script tactics that separate winners`** + sub-line *"Average outlier of videos using each tactic. Instant payoff is the single strongest driver on the channel."* — eight blue bars with `n=` and multiple (table at P18).
- **`Batch bias for the next 7 videos`** + sub-line *"What the topic-brainstormer will read as its marching orders."* — seven `SLOT N` cards, green/amber/grey (table at P15). Footer with the `0 slots:` line and the three per-script style constraints.
- **`What the dashboard can't tell you`** — the blind-spot paragraph (H10) + a collapsible `▶ Table view of all chart data`.
- **Document footer:** *"Coach log appended · `growth-system/coach-log.md` · Full system: shortform.academy"*
- **Chat side:** his prompt *"Can you visualize this for me?"*, the coach's offer *"[I can set up a] scheduled task (e.g., Monday 8am ET) that [runs the] comparison, writes the verdict and batch bias, [and delivers it]. Say yes and I'll create it,"* and *"[Artifact] saved to your artifact gallery as 'channel-[coach]' [so you can re]place each week rather than living only in [chat]."*

---

### 6.8 — Video B artifacts (delta reference)

- **Deep channel analysis output** `[B 07:47–08:20]` — "a dynamic visual web page" opened in Chrome; thumbnails load live and each links back to its Sandcastles page. Sections: best topics, hooks, formats, and **non-obvious patterns**.
- **Hook-pattern report** `[FRAME d1636.jpg, B ~16:36]` — numbered pattern sections, each: `N` badge + pattern name + a category pill (`authority`); an explanatory paragraph that names *why* it works ("works because it implies insider data the viewer doesn't have yet"); a **`Template:`** blockquote with slotted variables (*"'[format/strategy] is outperforming everything else.' / 'This is the modern playbook for [big outcome].'"*); evidence thumbnails with quoted hook + outlier + views + `View on Sandcastles →`; then negative sections carrying a **`Retire this one`** pill; then **`Hidden Insights — what a scroll would miss`** ("Second-order patterns across all 21 videos — the stuff you only see by studying the month at once") containing the naming-the-mechanism finding (P17). *UNCONFIRMED which of the five skills emitted this — it is on screen during the Outlier Video Pulse chapter but reads like the deep-channel-analysis output; likely b-roll.*
- **Old bullseye** `[FRAME d1249.jpg, B ~12:49]` — inverted numbering, `LEVEL 5` at centre, ✗ on `LEVEL 1`, with individual **video thumbnails plotted as dots** inside the rings (rather than bucket zones + darts). No competitor names, no constraint column, no meters.
- **Hook Machine intake** `[FRAME d1928.jpg, B ~19:28]` — declares its three deliverables up front (**hook format library**, **personalized grading rubric**, **hook generation engine**), offers the grade-my-hook loop (*"you can also drop in your own hook and I'll grade it, rank it against the [rubric], and give you 3 improved versions with explanations for why each is stronger"*), then states the credit balance and reset date, then asks for channels / count / window with a recommendation (**"at least 15 videos per channel"**).

---

## 7. Delta — what's NEW vs the existing `kallaway-*` roster

Current roster (10 skills): `addictive-storytelling` · `ai-content-engine` · `audience-obsession` · `content-operating-system` · `content-psychology` · `content-system` · `hook-mastery` · `illusion-of-novelty` · `social-commerce` · `word-mastery`. Those cover retention neurochemistry, hook craft, novelty manufacture, word/rhythm craft, monetization, and an end-to-end orchestrator. **None of them contains competitive positioning against real competitor data, an altitude model, a Claude-workflow design philosophy, or an artifact design language.**

**NEW — strategy & positioning (whole domain, currently absent):**
1. **The 7-attribute positioning lattice** with per-attribute saturation scoring against a named competitor set, and the multiply-attributes rule. (P3)
2. **The niche interview** — six fixed questions incl. the chair test and the "Ramble" unfair-advantage prompt, with the depth standard demonstrated. (P2, E1)
3. **Hypothesis→falsification staging** — self-assessment first, labelled a guess, then crossed against data with a confirmed/contested tally. (SM1)
4. **Competitor watchlist construction** — auto-discovery, Tier A/B, plus three manual escape hatches and the "follow the follows" harvest. (H15)
5. **The constraint-relaxation ring derivation** — rings defined by which filter comes off, with size/converts/competition per ring. **The single most valuable pattern in the corpus, and it exists only in the artifact.** (P4)
6. **3-2-1 batch allocation** with virality budgeted at 2/7 and fenced at Ring 4, plus the algorithm-confusion rationale for the Ring 5 ban. (P5)
7. **Chaos agent as designed experiment** — `A win teaches you` column, orthogonal questions, reserve bench. (P6)
8. **The two-zone sourcing rule** — topics altitude-bound, craft altitude-free, niche drift explained as a sourcing failure. (P7)
9. **Format = structure × visual, deflated and bounded** — a 2-axis matrix with median-outlier cells, white-space cells, and invented rows. (P19, H16)
10. **Two-question topic triage with an explicit 14% hit-rate mandate.** (P16)

**NEW — Claude + data workflow design philosophy (whole domain, absent):**
11. **MCP-as-data-layer anti-slop thesis** — quality is an evidence problem, and every skill declares a degraded mode. (P1)
12. **Free-stage / paid-stage separation with an itemized, overrulable exclusion table and a quoted credit bill.** (P8, SM2)
13. **The four-altitude reference ladder**, with the paid fifth tier skipped and the skip reported. (P10)
14. **Shared data core + declared consumers** (`top-50.md`, `Read by:`), numbered step IDs, one-line state summaries, one-word routing triggers, artifact-gallery persistence. (P21, SM6, H11)
15. **`[NEED]` refusal markers and a `Gaps` section** — the anti-hallucination discipline made structural at exactly the credibility-anchor slot. (H5)
16. **The honest-ceiling doctrine** — three explicit "AI can't one-shot this" statements plus the `engine-builder` diff/paste-back loop designed around the cap. (P14, SM8)
17. **Folder-as-memory setup** (`<name>-co/context/{how-i-talk, how-you-work, who-i-am, claude.md}` + `work/<stream>/{archive,assets,references,skills,videos}`), Whisper Flow voice-first input, and the interview-skill that generates the context files. `[B 00:40–06:00]`
18. **Cadence architecture** — strategy every 30 days, topic workflow every video, coach every 7 days. (P15)

**NEW — production loop shape (absent as a schema):**
19. **The Video Maker contract** — substance sheet → 4-altitude pull → 3 spoken hooks each paired with 2 text hooks → 2 research-toggleable scripts → one HTML + four MDs + a narration with a mandatory negative-space section.
20. **Spoken/text hook pairing as an output schema** (not a principle) with rendered phone frames and codified typographic defaults. (P13)
21. **Beat timelines** — script templates as time-budgeted stacked bars with per-beat jobs and median seconds. (P12)
22. **The rinse window (~60 days) with strikethrough** — anti-self-plagiarism enforced at the phrase-bank level. (P11)
23. **Substance-sheet anatomy** — Core claims / Coined name (+alternate, human picks) / Altitude-1 reuse with outlier scores / `[R]` research fills with `Plain-English:` glosses / belief→reframe pairs + `Villain =` / `Gaps`. (E2, H6, H8)

**NEW — learning loop (absent):**
24. **Batch bias as marching orders** — seven typed slot cards, colour-coded, plus a `0 slots:` demotion line with the losing average. (P15)
25. **Blind-spot declaration + cross-check** and the **24-hour maturity rule.** (H9, H10)
26. **Trap callouts inside charts** — "a person winning, not a topic", "Kassir-inflated" legend, "Retire this one" pills. (P9, SM3)

**NEW — artifact design language (entirely absent, and the reason this extraction is worth doing):**
27. A **shared palette** across six artifacts (red/orange/amber/light-blue/dark-blue for altitude; green/amber/red for open/contested/crowded), so a colour read in one is legible in all. (SM10)
28. **Same geometry, different legend** — the bullseye is redrawn three ways (audience / batch plan / sourcing rights) instead of introducing three diagrams. (§6.3)
29. **Teaching panels with a fixed 5-beat order** inside every interactive wedge — definition → option menu → current occupancy → white space → implication. (§6.2)
30. **Highlight-the-money-line** in rendered scripts; **phone-frame mockups** for anything that will appear on screen; **`Tap a …`** micro-instructions on every interactive; **export row** (`Download and open` / `Google Drive`) on every artifact.

**Corrections / conflicts to record:**
- **Remotion verdict reversed** — "the world's best AI editing skill inside of Claude right now" `[B 21:10]` → "they're all pretty trash" `[A 44:36]`. Seven weeks apart. The August verdict is the tested one; B explicitly disclosed he hadn't used it.
- **Bullseye numbering inverted** and **322 → 3-2-1** without acknowledgement (H1, H2).
- **Bullseye Builder went from MCP-free to data-fed** (H3).
- **Follower-count discrepancy, UNCONFIRMED:** he claims "@kallawaymarketing on Instagram went from 0 to 75,000 followers in like 4 months, drove 30,000 email subs and over $100,000 in attributable revenue" `[A 48:31–48:41]`, while the Channel Coach's own narration appears to isolate "IG's 12.6K followers" `[FRAME t4725.jpg, low-confidence read]`. Possible explanations: different channel, a scoped report, or a stale figure. **Do not repeat either number as fact without a live check.**
- The video is titled *0 to 100K Followers* but the stated result is 75K `[A 48:34]`. Title is aspirational/rounded.
- Anthropic sponsored video B `[B 00:35]`; video A carries no sponsorship disclosure but promotes Sandcastles (his own product) and SFA throughout.

**Where the surpass wedge is.** Per PROVENANCE.md, the free bundle ships the *strategy* half only, and every strategy skill degrades to a manual fallback labelled "unvalidated by performance data" when Sandcastles is absent. Meanwhile the four skills that produce the best artifacts in this corpus — `engine-builder`, `topic-brainstormer`, `video-maker`, `channel-coach` — are demoed on camera and never distributed. **Sections 6.6 and 6.7 of this ledger are therefore the only public specification of those four skills that exists.** That, plus a data layer that isn't Sandcastles, is the whole opening.

---

*Extraction: 2026-08-27. Sources: `extractions/kallaway-growth-system/{transcript.txt,visual-context.md,download/video.{en.vtt,info.json,mp4}}` and `extractions/kallaway-data-skills/{...}`. Frame renders: 41 crop-and-upscale passes via `.tmp/zoom.py` (two-stage accurate seek, 4–8× lanczos + unsharp) over the 640×360 source — no higher-resolution format is available (PO-token gated).*
