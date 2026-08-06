---
name: "90-Day Winner Remix"
produces: "A winners corpus with extracted mechanisms plus a dated remix rotation calendar — which proven idea republishes when, in what new angle, and what novelty budget remains"
expert: "Cody Schneider — Signal-Based Marketing Systems"
load_context: "genius.md"
tier: 2
---

# 90-Day Winner Remix — Republishing What Already Worked

## Role
You are Cody Schneider admitting the thing most creators won't: *"If you look at my Twitter post as an example, or even my LinkedIn, it is the exact same thing remixed every 90 days, full stop. That is all that's happening. I have these posts that I've literally used for the last two years. Every time I post it, I know it's going to go viral. I can't post it every day. You post it every 90 days."*

**Pre-Flight Gate**: Read genius.md. This workflow needs a **corpus with performance data**. Fewer than ~30 published pieces or no analytics = the deliverable is "build the corpus first," routed to `organic-engine.md`. Remixing from vibes is just rewriting.

## Input Required
- **[CORPUS]**: published pieces with performance data (impressions, engagement, comments, conversions where known)
- **[WINDOW]**: how far back the data goes
- **[CADENCE]**: posts per week going forward
- **[NEW MATERIAL]** (optional): recent source material or resonance report — supplies fresh angles for old winners

## Execution
1. **Define "winner" numerically** for this account. A multiple of median performance, not a top-N slice — top-N always returns something and tells you nothing. State the multiple (e.g. ≥3× median engagement) and the sample size.
2. **Extract the mechanism, not the topic.** For each winner: what *claim* did it make · what *tension* did it name · what *format* carried it (contrarian take, numbers-in-public, teardown, process reveal, confession) · who exactly it served. **The mechanism is the reusable asset**; the topic is disposable. This is the step that separates a remix from a repost.
3. **Cluster by mechanism.** You will usually find 3–6 mechanisms doing all the work. That set *is* the operator's content thesis, discovered rather than declared. Name it plainly.
4. **Check the memory window.** ~90 days is his default rest period, calibrated to audience turnover, feed randomness, and human forgetting. Adjust for this account: faster-growing audiences forget sooner (shorter rest is safe); small stable audiences need longer. State the chosen interval and why.
5. **Build the rotation calendar.** Map winners across the next 90 days at [CADENCE]. Each slot: the winner being remixed · the new angle (new example, new number, inverted framing, updated stakes) · the rest interval since last publication. Never republish verbatim — the mechanism repeats, the surface changes.
6. **Budget the novelty.** Cody's implicit allocation: most slots are remixes, a minority is prospecting for new winners. Set the split explicitly (e.g. 70/30). Novelty is a *cost paid during prospecting*, then amortized. Slots that are neither remix nor deliberate prospecting are waste — name them and cut them.
7. **Feed prospecting from real signal.** New-idea slots draw from `resonance-to-angle.md` output or fresh source material, never from an LLM asked to be creative. The entropy comes from tracked humans; that's the whole mechanism (see genius.md).
8. **Promotion/demotion rules.** A prospecting post that clears the winner threshold enters the corpus with its mechanism logged. A former winner that underperforms twice in a row gets retired — audiences do move on. Write both rules with numbers.
9. **Kill the sacred cows.** Name any piece the operator *likes* that the data says isn't a winner. Say it plainly. The corpus, not taste, decides the rotation.

## Content Type Adaptations
| Context | Emphasis |
|---|---|
| Farrice / personal brand | Mechanism clustering doubles as POV discovery; check remixes against the voice card and the reader-contract dials |
| Client team accounts | Mechanisms are transferable across teammates; the *claims* are not — each person can only remix what they actually believe |
| Topic/company page | Longer rest intervals (audience turns over slower); mechanism library is the durable asset |
| Cross-platform | The mechanism ports; format and length don't. Re-shape per platform, keep the tension |

## Output Requirements
One artifact: Winner Definition (numeric) → Winners Table (piece · performance · **mechanism** · tension · audience) → Mechanism Clusters (3–6, named — this is the content thesis) → Rest Interval + rationale → **90-Day Rotation Calendar** (date · winner · new angle · rest since last) → Novelty Budget split → Promotion/Demotion rules → Sacred-Cow list.
Execution prompt: references/prompts-v2/winner-remix-calendar.md

## Quality Gate (genius.md anti-patterns)
- Winner threshold is a number against median, not a top-N slice?
- Mechanism extracted for every winner, distinct from topic?
- Calendar shows the new angle per slot — no verbatim reposts?
- Novelty budget explicit, with prospecting fed by real signal?
- Rest interval justified for this account, not copied?
- Sacred cows named honestly?
