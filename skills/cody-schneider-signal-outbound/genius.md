# Genius Context — Cody Schneider: Signal-Based Marketing Systems

Source: Greg Isenberg, "These AI Marketing Agents Get You Customers" (44:00, 2026-08-05) — transcript + 100 frames, watched at the demo timestamps, extracted 2026-08-06. Full dossier: `extractions/cody-schneider-signal-outbound/extraction-report.md`.

**Cody Schneider**: founder of Graphed (graphed.com) — platform plus forward-deployed engineers who implement marketing agents for fast-growing companies. Screen-shares his own terminal on camera, gives the entire stack away for free, and refuses to sell a course: *"There's no gatekeeping here. I despise people that do this."*

## The Core Thesis

Every channel is degrading because AI flooded it — *"cold email is getting decimated… AI slop is flooding the zone and it's becoming just red ocean everywhere."* The only thing that still cuts through is **evidence of intent**. Someone engaging with a topic on a public platform is hand-raising: a dated, specific, checkable declaration that they're thinking about this problem right now. That beats every firmographic filter, because firmographics tell you who *could* buy and signal tells you who is *currently thinking about it*.

The second thesis is architectural: **"a marketing agent is code, maybe some thinking loop, and a live data stream"** — and the thinking loop is a scalpel, not a blanket.

## The Signal Loop (canonical order — workflows implement slices)

1. **Aperture** — 10-20 creators/company accounts in the niche, chosen off your own feed. Test: *"is the content being served what your target customer would be interacting with?"* Stop at 20; the outliers cover ~80% of the industry's surface area and the rest is the same people again.
2. **Pull** — net-new posts daily → reactions + comments per post → dedupe by public profile. Commenters outrank reactors.
3. **Read** — before treating anyone as a lead, read the *resonance*: which topics and hooks pulled hand-raises, and in what words. That report is content intelligence and ICP verbatim, not just a list.
4. **Gate** — one LLM judgment call per name (person + company vs ICP) **before** any metered enrichment. Non-fits exit free.
5. **Resolve** — waterfall: cheapest-and-most-accurate provider first, misses cascade down to progressively pricier tiers, validity check before use. ~50 → 32 → +10 → 8 residual ≈ 84%.
6. **Protect** — four separated domain lanes (cold · marketing · transactional · business). Never send volume from the asset you can't replace.
7. **Converse** — positive-reply webhook → an agent with one goal and a booking link → calendar as ground truth → programmed re-touch at ~6 months.
8. **Broadcast** — the same listening pointed outward: real human source material → extracted insights → voice-true drafts → schedule → analytics return → 90-day remix of proven winners.

## Load-Bearing Laws

- **Engagement is a hand-raise.** Target behavior on a topic, not attributes of a company.
- **Monitor the outliers, get the industry.** *"There's a handful of outliers within any niche and everybody is engaging with those handful of outliers."* Aperture inflation costs money to re-find the same people.
- **Use the feed, don't rebuild it.** The algorithm already solved topical relevance for your account; scraping + classifying to reproduce it is paying for a free output. Manual here is judgment, not laziness.
- **Judgment goes exactly one place — before the expensive step.** Everything else is deterministic code.
- **Token parsimony**: *"You should not be paying Anthropic to do an API call. You should be paying them to make the software that uses CPU to do the API call."* The LLM's best use is as a compiler — once.
- **Decompose the human, don't deify the agent.** What was the excellent human actually doing, in concrete verbs? Build that. *"Everybody tried to put God in a box and give it access to a Facebook ads account, and we realized that is not the right way to do this whatsoever."*
- **Cheapest-first, cascade the misses.** Ordering is by cost-per-marginal-hit, and per-stage hit rates get logged so it can be re-derived.
- **Blast-radius isolation for reputation.** Highest-risk sending gets disposable infrastructure so it cannot reach the irreplaceable domain.
- **Never ask an LLM to have the idea.** Asked to generate, it regresses to the mean — *"the most mid thing."* Asked to extract from a real conversation, it's doing retrieval on material with actual information content. Same model, categorically different output.
- **Human creators are the entropy source.** Agent loops converge and repeat themselves; ten tracked humans are a renewable supply of novelty. Look for the outliers-within-the-outliers.
- **Winners repeat on a 90-day clock.** *"If you look at my Twitter or even my LinkedIn, it is the exact same thing remixed every 90 days, full stop."* Novelty is a cost paid during prospecting, then amortized.
- **Market-pull over invention.** *"What does the market want to buy? Can I build it and can I sell it to them?"* Same law for content, offers, and product.

## Hidden Knowledge (apprentice-only)

- **Reactions come back obfuscated.** Live demo: 61 unique engagers = 52 reactors + 9 commenters, and **all 52 reactor rows had obfuscated/no-slug URNs** requiring a second resolution pass. Comments return usable profiles; reactions largely don't. Plan lead volume off commenters or you'll overstate pipeline ~5×.
- **The profile URL is B2B's universal join key.** *"As long as you have the LinkedIn profiles, this is done — game over."* Every enrichment vendor resolves from it, so all the difficulty is upstream in getting the right profiles; everything after is purchasable commodity.
- **The compliance split, three ways**: acquiring broker data is legal · what you *do* with it is the regulated surface · jurisdiction changes the answer (US ≠ EU). He volunteers "take this with a grain of salt" and "do your own research" — carry that forward.
- **The lost-deal reason is the best content seed in any company.** A real buyer explaining exactly what was missing. Nobody publishes it because it's uncomfortable; that's why it performs.
- **Agent frameworks are usually bloat** for finite pipelines with known steps — abstraction and dependencies bought for orchestration you aren't using.
- **Vendor selection = maintenance evidence, not feature list.** Scrapers rot as platforms change; pick the maintainer with a public reliability record.
- **Reads from the warehouse, writes through the API** (on-screen architecture slide, editorial recap of his prior episode; corroborated in passing here). And the ban myth: *"The agent is not the reason it got banned. They pulled hundreds of millions of rows. That is a TOS violation, not an agent problem."*

## Anti-Patterns (reject on sight)

- **God in a box** — one agent, broad write access, no decomposition. *"High likelihood it might just absolutely nuke the account."*
- **Firmographic-only lists** in a red-ocean channel — you bought what everyone else bought this morning. His alternative is the whole Agent-1 chapter: engagement-as-hand-raise targeting (source video 02:27–04:26, 2026-08-05).
- **Enriching before qualifying** — paying three providers for people you'd never contact. Gate before spend: *"Once I have those contacts, this is done, man — game over"* — but only after the judgment gate (transcript, engager-extraction demo ~10:59).
- **"Write good LinkedIn content"** with no source material — *"you're like, 'write good LinkedIn content' — it's going to be the most mid thing"* (transcript, organic-engine chapter 31:41).
- **Sending from the core domain** — *"we will nuke the deliverability of the business URL — the actual domain that we use to run our company"* (transcript, infra chapter 25:38).
- **Skipping the validity gate**, then blaming copy for the reply rate — Million Verifier sits before every send precisely so invalid addresses never burn the inboxes (waterfall chapter 21:40).
- **Aperture inflation** — 100 creators instead of 20; past 10–20 the marginal audience overlap collapses (creator-sourcing chapter 04:26).
- **Novelty for its own sake** — *"it is the exact same thing remixed every 90 days, full stop"* (transcript, earned-media chapter ~39:34).
- **Volume greed** — hundreds of millions of rows is a TOS violation, not an agent problem.
- **Tool-first thinking** — naming a vendor before naming the judgment step. Every tool in this domain has a ~12-month half-life (`references/era-bound-2026-08-stack.md`).

## Quality Rubric (score before shipping any signal deliverable)

| Criterion | 4 — Acceptable | 7 — Good | 10 — Savant |
|---|---|---|---|
| Signal quality | Firmographic list | Topic-adjacent audience | Every name is a dated, topic-specific hand-raise you can cite |
| Aperture sizing | Arbitrary count | 10-20 relevant creators | Chosen for buyer-stop-rate; overlap confirms coverage; nothing past diminishing return |
| Judgment placement | Inference sprayed everywhere | LLM at the writing step | One judgment call, before the expensive step; the rest deterministic |
| Cost architecture | Tokens per action, unmeasured | Some caching | Code does the work, inference compiles it; per-run cost known and small |
| Cascade discipline | One provider, accept the gap | Two-stage waterfall | Cheapest-first by marginal-hit cost, per-stage rates logged, validity gate before use |
| Asset protection | One domain for everything | Cold split from business | Four lanes isolated; transactional treated as sacred |
| Source-material honesty | LLM asked for ideas | Some human input | Every published idea traceable to a real human sentence with a timestamp |
| Loop closure | Publish and hope | Analytics reviewed manually | Performance returns to the writing step; winners on a dated remix rotation |

## House Constraint (binding for every workflow in this skill)

**Listening only. Farrice sends nothing automatically** (decision 2026-08-06 — reputation and distribution stay human). The listening half is implemented as `execution/signal_scout.py` (creators file → engager roster + resonance report, Apify-budget-guarded, never contacts anyone). Workflows produce intelligence and human-reviewed drafts; nothing in this skill dispatches a message. Outbound-infrastructure workflows are **design-and-diagnose**, deployable for clients, never auto-fired here.

## Recognition Test

Would Cody recognize this as his? Concretely: does it name a specific number the way he does mid-sentence ("maybe you only find 32")? Does it put judgment at exactly one step and prove the rest is code? Does it deflate something the reader thinks is complicated? Does it show a discarded option, not just the chosen one? If it reads like an agency deck about "AI-powered pipeline generation," he wouldn't recognize it — start again from the terminal.

## Voice Notes (for embodiment)

Deflationary — his signature move is puncturing mystique ("it's literally just code under the hood with an LLM attached"; "a server is just a computer that is on all the time somewhere else"). Numbers arrive casually mid-sentence and he never announces that he's being specific. Named process verbs, not jargon nouns: *prospect for ideas · prune the losers, promote the winners · snowball or remix · waterfall down to*. Corrects himself on camera ("this might actually be a terrible category"). Self-limits on expertise ("take this with a grain of salt," "I don't know as much about this"). Re-summarizes the spine unprompted: "again, just to reiterate this, because I know I've talked through a lot…" Keep some spoken texture — polish is the tell.

## Era Notes (dated appendix — durable craft above is the core)

Every vendor, actor, price, and platform behavior named in the source is quarantined in `references/era-bound-2026-08-stack.md`, dated 2026-08 and marked with his disclosed partnerships. Workflow bodies name *roles* (sourcing API, first-tier enricher, verifier, sending platform), never vendors. Verify anything in the appendix before citing externally — the half-life is roughly a year.
