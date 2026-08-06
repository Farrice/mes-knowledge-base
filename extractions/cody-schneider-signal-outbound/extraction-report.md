# MES 3.0 Deep Extraction — Cody Schneider

**Source**: Greg Isenberg, "These AI Marketing Agents Get You Customers" (44:00, 2026-08-05) — YouTube podcast, screen-share heavy.
**Artifacts on disk**: `transcript.txt` (8,932 words), `watch/frames/` (100 frames). 16 frames read selectively at the demo timestamps.
**Extracted**: 2026-08-06 · Tier: Deep (forge) · Latitude: 3 (autonomous)

**Expert identity — VERIFIED**: Cody Schneider, founder of **Graphed** (graphed.com) — "we have both the platform solution for this and also we forward-deploy software engineers to do these actual implementations on our platform" [43:0x]. Frame 0069 shows his own LinkedIn profile mid-demo: *"Cody Schneider · Graphed.com - Deploy AI Agents for Marketing"*, 2,894 profile viewers, 36,190 post impressions. Transcript renders the company variously as "graft" and "graph.com" — ASR noise; the frame is authoritative. Previously on the same show for a prior marketing-agent episode (referenced throughout as "last episode"). Most active on X and LinkedIn; publishes a free "go-to-market engineering / marketing engineering" crash course on his own channel and refuses to sell a course: *"There's no gatekeeping here. I despise people that do this. Don't buy a course. Literally DM me."*

---

## Part I — Genius Patterns (18)

### P1. The Hand-Raise Substitution — intent signal replaces firmographics

The founding move. Traditional outbound targets *attributes* (title, headcount, tech stack, industry). Cody targets *behavior on a topic*:

> "The way that we have found that you can stand out is you have to look for signals or triggers that basically show that people are hand raising… saying hey I want this thing, I have an interest in this thing. And a great way to do this is with these LinkedIn engagements. When they like content, that is a hand raise or a signal that I am interested in this specific thing… and not just their firmographics or their demographics or their psychographics, which is what we would traditionally use for outbound. This is specifically like, no, they have a propensity or an interest in this topic and we are going to go get in front of them." [~02:40–03:40]

**Mechanism**: firmographics predict *who could conceivably buy*; engagement predicts *who is thinking about the problem this week*. The second is a much smaller, much hotter set, and — critically — it is timestamped. A like on a post about AI video editing is a dated declaration of active interest. Cold outbound's entire failure mode is arriving without occasion; a hand-raise *is* the occasion.

**Why it matters now, in his framing**: "Right now cold email is getting decimated. Reply rates are down. Everything is down. Actually every marketing channel is down right now. Let's be real. The reason is just because AI slop is flooding the zone and it's becoming just red ocean everywhere." [02:20–02:40] The market's response to AI-scaled outbound is to raise the evidence bar. Signal is the only thing that clears it.

**Anti-example**: buying an Apollo list filtered to "Marketing Directors, 50-200 employees, USA." Every competitor bought the same list this morning.

### P2. The Outlier-Coverage Law — 10–20 creators ≈ 80% of a niche

> "Typically the company knows who is interacting… all you need is typically 10 to 20 of these and you have more than enough to be able to source the lead volume that's necessary to actually make this a viable channel… In reality, there's a handful of outliers within any niche and everybody is engaging with those handful of outliers. If you just monitor those outliers, you're actually going to get 80% surface area coverage for that entire industry. You don't need more than that. The marginal return of trying to go for all of it, it's not there." [~05:30–06:20]

**Mechanism**: attention in any niche is power-law distributed *and the tail engages with the head*. Because engagement is public, monitoring the head gives you a near-complete census of the tail without ever having to find the tail. The law is not "10-20 creators is enough content" — it's "10-20 creators is enough *aperture*." The audience you want walks past those posts.

**The corollary nobody states**: expanding from 20 to 100 creators multiplies cost and dedupe burden while adding the *same people again*. The overlap is the point.

### P3. Feed-as-Oracle sourcing — use the algorithm's answer, don't rebuild it

> "Honestly, I use the For You page — all these algorithms are so good now that it's going to show you the content that's relevant… This is literally a perfect example, first one that comes off: awesome, people trying to do some type of video editing, obviously it's probably for marketing. Everybody that's potentially engaging with this is a target customer." [~04:40–05:10]

Greg pushes: *"And you're doing this manually. Like, you're not using agents to do this. Why?"* Cody's answer is that the company already knows, and the feed already knows. He used to run trending-post searches and abandoned it: "We used to do this where we'd do the search and we'd find the trending posts from that period."

**Mechanism**: the platform has already spent billions solving topical relevance for your account. If your account is inside the niche, the feed is a pre-computed relevance ranking. Rebuilding that with a scraper + classifier is paying to reproduce a free output. **Manual here is not laziness — it's recognizing where the expensive computation was already done for you.**

Frame 0038 shows the counter-demonstration live: he searches "wordpress development" on LinkedIn and openly calls it: *"This might actually be a terrible category… this is probably going to be a lot of just not good signal."* Then pivots to "AI marketing." Public failure of his own example, corrected in real time.

### P4. The Creator-Selection Test — one question, no criteria list

> "It's really just: is the content that's being served what your target customer would be interacting with? That's what you're trying to get down to here."

Not follower count. Not engagement rate. Not posting cadence-as-quality. The only test is whether *your buyer* would stop on it. Two consequences he states explicitly:
- **Business accounts qualify.** "It can even be business accounts, and I think this is the thing that people don't realize — if there's business accounts that the people would be interacting with that would be your target customer, that can work as well. It can be literally Clay."
- **Too-broad topics disqualify.** "MCP — it's probably too broad." Breadth destroys signal purity: everyone engages with MCP, so engaging with MCP tells you nothing.

The selection axis is **specificity of implied intent**, not size of audience.

### P5. Human Creators as the Entropy Source (the loop-collapse fix)

The pattern generalizes past outbound, and this is where his thinking is most original:

> "This is the same idea with — we do this a lot, we try to solve this entropy problem within ads, paid ads in particular, where it's like if you just have the agent go in this loop, it'll just kind of make the same ideas over and over again. How do you solve for that? Well, you find human creators, like 10 of them on Instagram, and you track the content that they're publishing. You look for the outliers, and then from that you typically can get signal of like, oh, here's this new hook format, or here's this new topic, and I can just pull that, I can remix that." [~06:20–06:50]

**Mechanism**: an LLM loop with no external input converges — it re-samples its own distribution and the output flattens. The fix is not a better prompt or a temperature knob; it's **an external live stream of human novelty**. Ten tracked humans are a renewable entropy supply. Note the identical structure to P2: monitor a small set of outliers, take the outliers-within-the-outliers.

This single pattern explains why the signal doctrine and the organic engine (P13-P15) are the same system pointed in two directions. Both are: *monitor humans → extract outliers → remix.*

### P6. The Agent Definition — code, a thinking loop, a live data stream

Greg asks the load-bearing question: *"What makes this an agent versus a marketing automation?"*

> "The agent component of this is that it is running on a cron job daily, and then you're going to have an agent that later on we'll have it responding to the inbox… What is an agent? People ask me this every sales call. How I think about it personally is it's something that's doing a job to be done… In reality though, what is a marketing agent? It's code. It's maybe some thinking loop, and it's a live data stream. That is really how this functions." [~12:40–13:20]

And the deflationary restatement, later: **"When I say agent — it's literally just code under the hood. It's code under the hood with an LLM attached. That is an agent. You don't have to overcomplicate this. You don't have to have God in a box managing an email inbox."** [~29:30]

Three components, all required, none mystical:
1. **Code** — deterministic steps, on a schedule (cron).
2. **A thinking loop** — *optional and localized*; an LLM call at the one step where judgment lives.
3. **A live data stream** — the thing that makes it an agent rather than a script: it wakes up to new facts.

**The falsifiable line**: if it has no live data stream, it's a script. If it has no judgment step, it's automation. If the judgment step spans the whole job, you've built God in a box and it will fail (P7).

### P7. God-in-a-Box is the Wrong Decomposition

> "Everybody tried to put God in a box and give it access to a Facebook ads account, and we realized that is not the right way to do this whatsoever. The right way to do this is: what was the human doing? They were running this very specific process with media buying. They were researching ad creative angles. They were making new ad creative. They were testing the new ad creative, and then they were pruning the losers, promoting the winners. That is what a top media buyer does. Okay — how do we go and make a piece of software that does that exact same thing?" [~13:40–14:20]

**The method, generalized**: (1) name the role, (2) watch the excellent human do it, (3) write the process as a numbered list of concrete actions, (4) build software that performs that list, (5) insert inference *only* at steps that require judgment. He does this twice in 44 minutes — once for the media buyer, once for the social media manager (P15) — which is what makes it a method rather than an anecdote.

**Why the naive version fails**: an autonomous agent with account write access has an enormous action space and no ground truth about which actions are catastrophic. "If you have Hermes try to run your Facebook ads, high likelihood it might just absolutely nuke the account. But if you build a piece of custom software for yourself that's running based off of a system that a real human would run — totally different outcomes that you're going to get from that, that are probably higher quality."

### P8. Token Parsimony — buy the software, not the inference

His stated obsession, and the most contrarian position in the episode:

> "You should not be paying Anthropic. You should not be paying ChatGPT to do an API call. You should be paying them to make the software that uses CPU to do the API call. Why are you paying this tax on tokens every time that you're trying to do this marketing activity? That's ridiculous. Build the software that does the solution for you, not tokens burning every time that you're trying to do the action." [~14:20–14:50]

> "Everybody's just like, 'oh, token abundance, I'm going to token-max.' I'm actually probably the opposite of that. It just feels wasteful. Do the thing that is the simpler thing that has less likelihood of breaking… Only use inference when you need it." [~31:00]

**Mechanism**: inference is a *per-execution* cost with *per-execution* variance. Code is a one-time cost with zero variance. Every step you move from inference to code reduces both marginal cost and failure surface simultaneously. The LLM's highest-value use is as a **compiler** — it converts your intent into the cheap deterministic thing, once.

His co-founder's compression: **"Max always says this — the only agent is a coding agent. Everything else is software that's being made by the coding agent."**

### P9. Waterfall Enrichment — cheapest-and-most-accurate first, cascade the misses

The mechanic, with his own worked numbers:

> "When I say a waterfall enrichment — we're taking that list of 50. Say we have 50 LinkedIn URLs that we found, and on [the first provider] maybe we only find 32 emails of those people. So that next cohort, those other 18 that are left, I'm then going to send those 18 to [the second]. So of those 18 that I send, maybe I only find 10. And then those 8, that's when I would send that to something else… The reasoning behind this is you're starting with what is the cheapest, most accurate, and then moving your way down into the more expensive validation tools. From this you can pull out from a list — this is the way that you get to an 80% find rate. And you can chain as many of these together as you want. It just depends on your budgets that are available." [~21:40–23:00]

**The math, laid out**: 50 in → 32 (64%) → +10 of 18 (56% of remainder) → 42/50 = **84%**, with 8 sent to a third tier. Each stage is progressively more expensive *per successful lookup*, which is exactly why order matters: you never pay premium prices for the records the cheap tier would have resolved.

**The ordering principle is cost-per-marginal-hit, not cost-per-call.** A tool that's twice the price but resolves the hard residual belongs at the bottom, not off the list.

**Aggregators exist and change the build/buy call**: "There's also aggregators of this… you can just send them a LinkedIn profile and it's going to waterfall through the options that are available." You outsource the cascade and lose per-stage cost visibility. Trade knowingly.

### P9b. The Verification Gate — validate before you send, always

> "Once I found each of these individuals and the emails, from there what I'm then going to do is validate these emails… enables me to check if the email is good, risky or bad — more technical terms would be good, catchall, risky. The reason you want to do this is the emails that come out of these providers… do the second verification. You're basically only wanting to send cold email to valid emails, because if you send to invalid emails, you're going to run into deliverability problems." [~19:30–20:40]

Enrichment providers optimize for *coverage*; you need *validity*. The two objectives conflict, so the verification pass is a separate, non-negotiable stage — and it protects the asset (deliverability), not the campaign.

### P10. The ICP-Fit Gate Goes BEFORE the Spend

The most easily missed instruction in the episode, and the one that decides unit economics:

> "The thing that you can extend this further with is who you're outbounding to. You want it to basically do an ICP fit or target-customer-segment fit. So **before it even does this enrichment** that we're about to do, you would be like: okay agent, research this person and the company that they're at — how many employees do they have, all of these things. And then based off of what we find, if it fits this customer profile — you're going to have the agent basically think through that, using an LLM — if it fits this customer profile, then it goes into this enrichment. Then we're actually going to cold email them." [~13:20–13:40]

**Mechanism**: enrichment is metered; judgment is cheap relative to a cascade of paid lookups. Gating first means you never pay three providers to find the email of someone you'd never contact. **This is also the canonical placement of P6's "thinking loop"** — one LLM call, at the one step that requires judgment, positioned where it saves the most money. Cody demonstrates his own doctrine here without flagging it.

### P11. Four-Lane Domain Separation — protect the asset

> "When you're buying these emails, what you're really doing is buying inboxes and domains that are burner domains that enable you to send cold email not from your core domain. And the reason that you have to do this is so that you don't burn the deliverability of your core domain. If you send from your exact domain and say we send 10,000 cold emails from that, we will nuke the deliverability of the business URL — the actual domain that we use to run our company. You don't want to do that. So typically what you want to do on the marketing side is have this separation: you have domains that are for your cold email, you have domains that are for your email marketing, you have domains that are for your transactional email — this would be email being sent directly from the product to a customer, imagine like a password reset — and then you want to have your business domain email, which is what your team actually uses to run the company." [~25:38–27:00]

Four lanes, four risk profiles:

| Lane | Traffic | Failure cost if burned |
|---|---|---|
| Cold outbound | Unsolicited, highest complaint rate | Low — burners are consumable |
| Email marketing | Opted-in, medium volume | Medium — list value |
| Transactional | Product-triggered, must arrive | **Catastrophic** — password resets fail silently |
| Business/team | Human correspondence | **Catastrophic** — you stop being reachable |

The principle is **blast-radius isolation applied to reputation**: the highest-risk activity gets disposable infrastructure so that its inevitable damage cannot reach the irreplaceable asset. Transactional is the lane most people forget, and its failure mode is invisible until support tickets pile up.

### P12. The Reply Agent — webhook + goal prompt + calendar truth, and the long tail is the alpha

> "They have an API and that API allows for you to monitor and manage the entire account… But the bigger thing here is they also have webhooks. So when a positive reply happens, you can send that webhook confirmation back to your agent that's hosted on some cloud server, and that agent — you give it a base prompt of like, you're the goal, here's all the context that you need, and your goal is to try to get people to schedule demos on this link. It can manage that inbox, answer questions, push people deeper." [~28:00–29:00]

> "But the thing that gets really fascinating and really powerful with this is it can do these follow-ups like months later. So it's like, okay, every six months I want to program that in to re-reach out to these people that went cold. I can also plug it into my scheduling application… give the agent access to see: okay, did this person that we reached out to actually schedule a discovery call? Did they actually produce the action that we're trying to optimize for?" [~29:00–29:30]

Three design notes worth more than the tooling: **(a)** the trigger is a *positive-reply webhook*, so inference only fires on qualified conversation; **(b)** the agent is given one goal and a link, not a persona essay; **(c)** the calendar is the ground-truth oracle — outcome is read from the booking system, not inferred from the conversation. The six-month re-touch is the part humans never do and software never forgets; it is the cheapest incremental pipeline in the system.

### P13. Source Material Doctrine — never ask an LLM to have the idea

The organic engine's founding constraint, stated as a law:

> "So you get source material. Why do you have to get source material? The reason is because if you go and you try to just have the agent think about this — you're like, 'write good LinkedIn content' — it's going to be the most mid thing. You're going to waste the person's time on the other side. Or you're going to get flagged for AI slop by LinkedIn's new feature that just released this morning. The better way to do this is source this from real human conversation, because that's where these original ideas are coming from." [~34:00–34:40]

**Mechanism**: an LLM asked to generate an insight regresses to the distributional mean of everything ever written about the topic — which is precisely the definition of "mid." An LLM asked to *extract* an insight from a real conversation is doing retrieval and compression, tasks it's excellent at, on material with genuine information content. **Same model, same prompt quality, categorically different output — the difference is entirely the input.** (This is the identical mechanism as P5's entropy fix, applied to writing instead of ads.)

The pipeline as he runs it: "I have a weekly one-on-one call with the people that we're doing this for — 'just tell me everything that you've learned in the last week.' I just basically interview them, have a conversation. It doesn't have to be anything focused. It's just: what are the things that jumped out at you after being in these sales calls, or whatever your job is. You can do this for technical people as well."

### P14. The Trapped-Context Mine — the best content already exists inside the company

> "It also doesn't have to be an interview. It can just be sales calls or internal comms… so much context is happening within their Notion, within their codebase, within their Slack. You can use one of these agents to query those data sources — query the sales channel, or query the Gong transcripts, and that's where you can pull these insights from. And honestly, a lot of the times you find that it's really good content that's trapped in there. Like, a potential customer said this, and it was why they didn't buy the product — and that can turn into an unbelievable piece of content." [~35:00–35:40]

**The hidden gem inside the gem**: the *lost-deal reason* is named as the highest-value content seed. It's the most honest sentence any company possesses — a real buyer explaining, unprompted, exactly what was missing. Nobody publishes it because it's uncomfortable. That discomfort is the entire reason it performs.

Also: any transcript works, including someone else's. "Another example of this is literally this podcast. You could extract all the insights from the transcript and that can be used as social content. This is a strategy I use for myself. But it doesn't have to be just your own — it can be a podcast with Naval. The source material can be anything."

### P15. The Social-Media-Manager Decomposition + the 90-Day Remix

He runs P7's decomposition method on a second role, live:

> "When you look at what a social media manager did previously — a good one that was actually excellent at their job — they would prospect for ideas. They would make content about those ideas. They would publish it. They would look at the data to see which got the most impressions, and then they would turn that into a recurring content calendar where they're like, okay, I'm just remixing these same ideas over and over again." [~38:30–39:10]

> "**If you look at my Twitter post as an example, or even my LinkedIn, it is the exact same thing remixed every 90 days, full stop. That is all that's happening.** And when you get enough information — a big enough corpus — you basically understand what's already going to go viral. I have these posts that I've literally used for the last two years. Every time I post it, I know it's going to go viral. I can't post it every day. You post it every 90 days." [~39:10–39:40]

**Mechanism**: a winning post is not consumed by one publication. Audience turnover, feed randomness, and human forgetting mean the same idea can be re-monetized indefinitely — the only binding constraint is **the memory window of the people who saw it last time**, which he prices at 90 days. Novelty is a cost, not a virtue; you pay it during prospecting and amortize it forever after.

The stance that follows: "Have this mentality of I'm prospecting for ideas, I'm prospecting for winners. Once I find those, I'm trying to use those as often as I can, because I know that that's what's going to work. That is what the audience is resonating with."

His verdict on the role: "I actually think the social media manager job, full stop — I think it's already dead… If you're listening to this, please learn how to make and manage content at scale across multiple accounts with agents, because that's the real meta now: how can a single person manage 10, 20, 100 accounts across all of these different channels."

### P16. The Analytics Return Path — the loop only closes if data flows back

> "[The scheduler] also has the analytics data that pulls in from your LinkedIn posts. So we can see the breakdown of which content is actually performing well… and that data stream can go back to the agent so that it understands: okay, this is what's getting impressions, this is what's doing well. Let's go do more content like that. When it does its cycles of writing, that can influence the next round of creative. So topics like this perform better based off of the source material we pulled. How can we snowball or remix — **use those specific words, snowball or remix** — to have it go further. And this is where the LLM is thinking on top of that data stream." [~37:00–38:00]

Two things: the **live data stream** from P6 is instantiated here as performance analytics (that's what upgrades the content pipeline from script to agent), and he hands over the literal prompt vocabulary — *snowball* and *remix* — as terms that reliably steer an LLM toward extension-of-a-winner rather than new invention.

### P17. Market-Pull Over Invention (the same law, applied to product)

> "A lot of first-time founders spend time thinking about 'I'm trying to get the market to buy this,' and in reality the pros at this are like: what does the market *want* to buy? Can I build it and can I sell it to them? That is actually how you start a business. For some reason it's this flipped thing where they're like, 'oh, I'm trying to invent a new idea.' I don't want to invent a new idea at all. I want to be like: what do people want to buy that currently they can't buy, and can I go figure out the way to build that thing? Then I know the market is going to be receptive to it. And you need to think about content in the same way — what is the content that the market is currently receptive to? By mining content from other sources that has already had a viral moment, this is a way to leapfrog, to identify that, and then you're putting your own spin, your own angle on this." [~40:00–40:50]

This is the **unifying principle of the entire episode**. Signal targeting = let the market show you who. Outlier mining = let the market show you what. Winner remixing = let the market show you what again. Product = let the market show you what to build. In every case: *evidence of existing demand precedes creation*. Invention is repositioned as a last resort, not a virtue.

### P18. Earned-Media Arithmetic — organic reach priced as media spend

> "I'll talk to founders or people that run bigger companies and they'll be like, 'why would you invest in social?' And I'm like — look at the earned media. If you were paying for those impressions on platform, for example on LinkedIn, it's like $22 per thousand impressions is the average. So every post that you get, even with an account that's 500 followers, you can get 1,000 impressions. That's like $20 that you just put into your pocket for free… **I get paid to build lead pipeline.**" [~41:30–42:30]

**Mechanism**: converting organic reach into its paid-equivalent cost reframes content from "brand activity with fuzzy ROI" into "media purchased at a 100% discount," which survives a CFO conversation. Frame 0069 shows his own scoreboard mid-demo: **36,190 post impressions** — at his own quoted $22 CPM that's ~$796 of LinkedIn media in one period, unpaid. He argues the ledger of his own claim without saying so.

*(CPM figure is his assertion — flag: UNCONFIRMED, LinkedIn CPMs vary widely by targeting and season.)*

---

## Part II — Hidden Knowledge (apprentice-only)

**HK1. Reactor rows come back obfuscated — this is the failure mode nobody warns you about.**
Frame 0071 (terminal, live demo) shows what the polished version of this advice never mentions:
```
● 61 unique engagers extracted • api…
    Counter({'reactor': 52, 'commenter': 9})
    obfuscated/no-slug: 52
  - All 52 reactor rows have obfusca[ted URNs]
  - that's normal for the reactions [endpoint]
  Next step in the chain: … resolve-linkedin-urls-exa…
  - Exa-resolve reactor URNs to publi[c profiles] → Verifier
```
Reactions return internal URNs, not public profile slugs. **Roughly 85% of a reaction pull is unresolvable without a second resolution step** (he uses a search-API resolution pass). Comments return usable profiles; reactions largely do not. Practical consequence: *comment engagers are worth several times reaction engagers* — not only because commenting is stronger intent, but because a commenter is immediately actionable and a reactor costs another lookup. Anyone who plans lead volume off raw reaction counts will overstate their pipeline by ~5×.

**HK2. Dedupe by public profile, and expect the raw number to shrink.**
"Right now, as you can see, the duped-by-public-profiles, there's 63 raw and it's about to pull all of those contacts out." 63 raw → 61 unique. Small shrink on one post; across 20 creators × daily posts, the overlap is where P2's coverage law shows up as *cost savings* — the same people keep appearing, which is confirmation the aperture is correctly sized.

**HK3. "As long as you have the LinkedIn profiles, this is done — game over."**
His actual words: *"Once I have those contacts, this is done, man — game over. As long as you have the LinkedIn profiles, you can go and find the email addresses of them, you can find the phone numbers of them, you can find everything that you need."* The strategic implication: **the LinkedIn profile URL is the universal join key of B2B data.** Every enrichment vendor accepts it and resolves from it. So the whole system's difficulty is concentrated in step one (getting the right profile URLs) — everything after is a solved, purchasable commodity. Spend your thinking upstream.

**HK4. The compliance line, drawn precisely.**
Greg asks the uncomfortable question directly. Cody's answer separates two things most people conflate:
> "It is fully legal to get these emails. What you do with those — that's where things from a compliance standpoint change. You can cold email technically in the United States. You can also add people to an email newsletter and be CAN-SPAM compliant. There's tons of things — you basically have a checklist of things that you have to do. On the cold email side and the contact lookup, you're basically just buying data from a data broker, which is legal… On the spectrum of black hat to white hat, [this is] pretty far on that white hat side."
Plus the disclaimers he volunteers unprompted: *"Take this with a grain of salt"* · *"there's different compliance rules within the United States versus the EU"* · Greg: *"I don't think anyone would mistake you for a lawyer."*
**Acquisition is legal; use is regulated; jurisdiction changes the answer.** Anyone teaching this without that three-part split is teaching it wrong.

**HK5. Agent frameworks are usually bloat.**
> "I also get asked this question a lot: do you need to use some agent framework under the hood? A lot of the times you don't need it. It's just bloat. You can have a very simple solution for these finite problems. It doesn't have to be this overcomplicated or overengineered thing."
For **finite problems** — a fixed pipeline with known steps — a framework adds abstraction, dependencies, and failure surface for orchestration you aren't using.

**HK6. Local-first is the deployment test.**
> "If you can build it in Claude Code and have some type of local system that you're running, you can probably deploy that to a server somewhere and have that run on an hourly cadence or a daily cadence."
Working locally is the *gate* for deployment, not a rehearsal for it. And the demystification: *"When I say server — what is that, for the uninitiated? It's just a computer that is on all the time somewhere else that you're putting code onto."* Also: *"Everything that I'm doing right now, this is all just going to be code under the hood. And once it's code, I can deploy that into a cloud system… and then you're just there basically jockeying the agent."* **The human's steady-state role is jockey, not operator.**

**HK7. Reads from the warehouse, writes through the API.**
Frame 0134 shows an on-screen architecture slide — `PIPELINE → WAREHOUSE → AGENT → BACK`: sources (ads platforms, analytics, product analytics, CRM, payments) → open-source data pipeline → columnar warehouse ("every source in context, ties the ad to revenue") → the agent ("reads the warehouse, publishes, pauses, promotes the winners"), hosted on a simple app platform. Two panels:
- **THE BAN MYTH** — "The agent is not the reason it got banned. They pulled hundreds of millions of rows. That is a TOS violation, not an agent problem. Marketing API = WRITES ONLY: publish · pause · promote."
- **FREE UPGRADE** — conversational analytics over the same warehouse ("we can't make payroll, what is going wrong?" → "your accounts receivable"), custom dashboards off the same data.
- Bottom line, verbatim: **"Reads come from the warehouse. Writes go through the API. That is the rule."**

*Attribution note: this is an editorial recap graphic (summarizing his prior episode's agent), not spoken in this conversation. The transcript corroborates the architecture in passing — "use something like ClickHouse to create your data pipeline and your data warehouse so you have that data stream for the agent to make those decisions, and then you have to have some server." Treated as VERIFIED-visual, spoken-partial.*

**HK8. Sourcing tools are the bottleneck, not the API.**
> "The challenge with [the scraping marketplace] is finding good ones that are actually being monitored and being maintained."
Frame 0060 shows how he resolves it: he picked one maintainer with a full LinkedIn actor suite and a public reliability record (~98% success rate, ~99% "runs succeeded," response-time badge visible on the profile). **Vendor selection criterion = maintenance evidence, not feature list.** A scraper that worked last quarter is worthless; the platform changes and only maintained actors track it.

**HK9. He teaches with the failure in frame.** Twice he demos a search, watches it produce junk, and says so on camera before pivoting ("this might actually be a terrible category"). The pedagogical choice — showing the discard step rather than a curated result — is *why* the method transfers. The judgment being taught is "recognize bad signal," which can only be taught by showing bad signal.

**HK10. Free-course-as-moat.** "There's no gatekeeping here. I despise people that do this. Don't buy a course. Literally DM me. I'll teach you anything. I'll just make a public video for everybody." He gives away the entire stack list on camera and sells implementation (forward-deployed engineers) instead. The method is not the scarce asset; the willingness and time to run it is. Note this is *itself* a lead-gen strategy — the video is the top of his funnel.

---

## Part III — Hall of Fame Exemplars

**E1. The 63→61 live pull.** One post URL → Claude Code with a scraping API key → post-reactions + post-comments actors → deduped by public profile. Terminal output (frame 0071): `61 unique engagers extracted`, `Counter({'reactor': 52, 'commenter': 9})`, `obfuscated/no-slug: 52`, runtime ~34 s. Narrated: *"Right now, as you can see, the duped-by-public-profiles, there's 63 raw and it's about to pull all of those contacts out. Once I have those contacts, this is done, man — game over."* This is the gold standard the flagship workflow is blind-passed against.

**E2. The waterfall ledger.** 50 LinkedIn URLs → tier 1 returns 32 → the 18 misses go to tier 2 → 10 more → the remaining 8 go to tier 3. 84% cumulative, cheapest-first ordering, then a validity check on everything before a single send. Stated as an ~80% find-rate expectation.

**E3. The four-lane split.** Cold / marketing / transactional / business domains, with the explicit rationale that 10,000 cold sends from the company domain "will nuke the deliverability of the business URL." ~10,000 sends/month for roughly $100 in inbox infrastructure plus roughly $100 in sending software — about $200/month all-in at the entry tier.

**E4. The team organic engine.** Weekly unstructured 1:1 interview per teammate ("just tell me everything you've learned this week") → transcript → insight extraction → drafted posts in the teammate's voice → scheduled across multiple connected accounts → analytics return to the agent → next cycle biased toward what performed. Built because clients asked how a seven-person sales team posts daily with non-duplicate ideas.

**E5. The topic-page alternative** *(Greg's contribution, not Cody's)*: Julian Shapiro ran his growth agency's audience through **@GrowthTactics**, not @DemandCurve — a topic page people follow for the topic, which then routes them to the company. Cody's endorsement of the underlying move: attention aggregated around a subject doesn't require a personal brand. Attributed to Greg Isenberg.

---

## Part IV — Signature Moves (8)

**SM1. The Feed Harvest.** Open your own For You feed inside the niche. Pull 10–20 creators or company accounts whose posts your buyer would stop on. Stop at 20. Reject topics too broad to imply intent.

**SM2. The Hand-Raise Pull.** For each monitored creator, get net-new posts on a daily cadence; for each new post, pull reactions *and* comments; dedupe by public profile. Weight commenters above reactors (intent + resolvability, per HK1).

**SM3. The Judgment Gate Before the Spend.** One LLM call per lead — researching person + company against the ICP — *before* any metered enrichment. Non-fits exit free.

**SM4. The Cheapest-First Cascade.** Order providers by cost-per-marginal-hit. Pass only the misses down. Log per-stage hit rate so the ordering can be re-derived, not assumed. Validity-check the survivors before use.

**SM5. The Four-Lane Split.** Cold, marketing, transactional, business — separate domains, permanently. Highest-risk traffic gets disposable infrastructure.

**SM6. The Decompose-the-Human Pass.** Name the role → list what the excellent human actually does, in concrete verbs → build code for the list → insert inference only where judgment is unavoidable. Run before building any agent.

**SM7. The Trapped-Context Mine.** Query existing conversational corpora (call transcripts, sales channels, docs) for insight, prioritizing lost-deal reasons and objections. Never brief an LLM to invent the idea.

**SM8. The 90-Day Remix.** Maintain a winners corpus with performance data. Re-publish proven ideas on a ~90-day rotation with new angles. Reserve novelty budget for prospecting, not for every post.

---

## Part V — Quality Rubric (8 criteria)

| Criterion | 4 — Acceptable | 7 — Good | 10 — Savant |
|---|---|---|---|
| **Signal quality** | Firmographic list | Topic-adjacent audience | Every name is a dated, topic-specific hand-raise you can cite |
| **Aperture sizing** | Arbitrary creator count | 10–20 relevant creators | 10–20 chosen for buyer-stop-rate; overlap confirms coverage; nothing added past diminishing return |
| **Judgment placement** | Inference sprayed across the pipeline | LLM at the writing step | One judgment call, positioned before the expensive step; everything else deterministic |
| **Cost architecture** | Tokens per action, unmeasured | Some caching | Code does the work, inference compiles the code; per-run cost is known and small |
| **Cascade discipline** | One provider, accept the gap | Two-stage waterfall | Cheapest-first ordering by marginal-hit cost, per-stage hit rates logged, validity gate before use |
| **Asset protection** | One domain for everything | Cold split from business | Four lanes isolated; transactional deliverability treated as sacred |
| **Source-material honesty** | LLM asked for ideas | Some human input | Every published idea traceable to a real human sentence with a timestamp |
| **Loop closure** | Publish and hope | Analytics reviewed manually | Performance data returns to the writing step; winners enter a dated remix rotation |

## Part VI — Voice Profile (for embodiment)

- **Deflationary about the magic.** His signature rhetorical move is puncturing: "it's literally just code under the hood," "it's just a computer that is on all the time somewhere else," "you don't have to overcomplicate this." He removes mystique from things people find mystical.
- **Numbers arrive mid-sentence, casually.** "Maybe you only find 32," "$22 per thousand impressions," "10 to 20 of these," "about $200 to get started," "every 90 days." He is unusually specific for a podcast guest and never announces that he's being specific.
- **Named process verbs, no jargon nouns.** "Prospect for ideas," "prune the losers, promote the winners," "snowball or remix," "waterfall down to." He names *actions*, not frameworks.
- **Interrupts himself to correct on camera.** "This might actually be a terrible category." "MCP — probably too broad." "I don't know much about this."
- **Self-limiting on expertise.** Volunteers "take this with a grain of salt," "do your own research," "I don't know as much about this."
- **Anti-gatekeeping to the point of irritation.** "There's no gatekeeping here. I despise people that do this. Don't buy a course."
- **Repeats the spine deliberately.** "Again, just to reiterate this, because I know I've talked through a lot: I'm pulling the lead list from LinkedIn…" He re-summarizes the pipeline twice, unprompted.
- **Filler and speech texture**: "right?", "like", "man", "G" (addressing Greg), "full stop," "game over." Keep some. Polish is the tell.

## Part VII — Anti-Patterns (reject on sight)

1. **God in a box** — one agent with broad account write access and no decomposition. "High likelihood it might just absolutely nuke the account."
2. **Firmographic-only targeting** in a market where "every marketing channel is down" — buying the same list as everyone else.
3. **Token-max architecture** — paying inference per execution for work that is deterministic.
4. **"Write good LinkedIn content"** with no source material — "it's going to be the most mid thing."
5. **Sending from the core domain** — one campaign, permanent damage to an irreplaceable asset.
6. **Skipping validation** — sending to unverified emails and blaming copy for the reply rate.
7. **Enriching before qualifying** — paying three providers for people you'd never contact.
8. **Novelty for its own sake** — inventing a new post when a proven one is 90 days rested.
9. **Aperture inflation** — 100 creators instead of 20, paying more to re-find the same people.
10. **Framework-first agent builds** — orchestration abstractions over a finite, known pipeline.
11. **Volume without limit** — the ban myth (HK7): pulling hundreds of millions of rows is a TOS violation, not an agent problem. The agent didn't get you banned; the greed did.

## Part VIII — Recognition Test

Would Cody Schneider recognize this output as his? Concretely: does it name a *specific* number he'd have said mid-sentence? Does it put judgment at exactly one step and prove the rest is code? Does it deflate something the reader thinks is complicated? Does it show a discarded option, not just the chosen one? If the output reads like an agency deck about "AI-powered pipeline generation," he would not recognize it — start again from the terminal.

## Part IX — Flags & Unconfirmed

- **UNCONFIRMED**: "$22 per thousand impressions" LinkedIn CPM — his assertion, unverified; real CPMs vary widely.
- **UNCONFIRMED**: "LinkedIn's new feature that just released this morning" flagging AI slop — not independently verified as of extraction.
- **UNCONFIRMED**: the ~80% niche-coverage figure — stated from practice, no methodology given. Treat as a working heuristic, not a measurement.
- **DISCLOSED INTEREST**: several named vendors are explicitly his partners ("they're a partner of ours," "we have a partnership with them"). Tool endorsements are not neutral. Captured in the era-bound appendix with the disclosure attached.
- **ASR noise corrected**: "ampify"→Apify · "API maestro"→apimaestro · "Prospio"→Prospeo · "git leads"→GetLeads · "hey reach"→HeyReach · "Kalanley"→Calendly · "graft"/"graph.com"→Graphed (frame 0069) · "seed dance"→Seedance · "Greg Eisingberg"→Greg Isenberg.
- **GESTURED, NOT TAUGHT**: hosting/deployment specifics, LinkedIn DM tooling depth, full compliance checklist. He says outright: "we don't have time today to go into all the finite details here." Not extrapolated.
