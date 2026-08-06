---
title: "Era-Bound Stack Appendix — Cody Schneider, 2026-08"
status: DATED — verify before use or citation
half_life: "~12 months. Vendors, actors, prices, and platform behaviors in this file WILL move."
rule: "Workflow bodies name ROLES, never vendors. This file is the only place vendor names live."
source: "Greg Isenberg × Cody Schneider, 'These AI Marketing Agents Get You Customers', 44:00, 2026-08-05 — transcript + frames 0060/0077/0080/0091/0095/0100/0112/0120"
---

# Era-Bound Stack — as of 2026-08

**Read this second.** The durable craft is in `genius.md`: signal doctrine, aperture sizing, judgment placement, cascade logic, lane separation, the organic loop. That material survives every vendor on this page. What follows is the 2026-08 instantiation — useful for building *this month*, worthless as doctrine.

**Disclosure**: Cody names several of these as commercial partners on camera. Marked ⚠︎ below. Treat those endorsements as disclosed-interest signals, not neutral benchmarks.

---

## Role → 2026-08 instantiation

| Role in the loop | What he named | Notes |
|---|---|---|
| **Sourcing API** | **Apify** (`apify.com`) | One API key, many scrapers ("actors"), multi-platform (LinkedIn, X, etc.). Transcript ASR renders it "ampify." |
| **LinkedIn actor suite** | **apimaestro** on Apify | Frame 0060: profile posts · profile details · posts search · company posts · **post reactions** · **post comments** · mass profile scraper · reactions/company/employee actors. Profile shows ~20 public actors, ~98–99% success rates, "<99% runs succeeded," "linear profile." His stated criterion: *"the challenge is finding good ones that are actually being monitored and being maintained."* |
| **Actors actually used** | `post reactions` + `post comments` (engager pull); `profile posts` (net-new post discovery) | Both required. Reactions give volume; comments give resolvable profiles + language. |
| **Coding harness** | **Claude Code** or **Codex** | Used to write the pull scripts against the API. He also references his own free "go-to-market engineering / marketing engineering" crash course (~10 min setup) on his channel. |
| **Enricher — tier 1** | **GetLeads.io** | Frame 0080: "Unlimited verified B2B contacts for your AI · Claude/ChatGPT/API access to 402 million B2B contacts · people search, email & phone enrichment, LinkedIn lookups · 5,000 contacts free." His tier-1 cheapest-first slot. |
| **Enricher — tier 2** | **Apollo** | The classic fallback for tier-1 misses. |
| **Enricher — tier 3** | **Origami** ⚠︎ (`origami.chat`) / **Prospeo** | Frame 0077: "Find your perfect customers… leads you can't find in Apollo, ZoomInfo, or Clay. Describe your perfect lead, then have our AI scour the web and reach out for you. #1 Product of the Day." **Also an aggregator** — send a LinkedIn profile and it runs the waterfall internally. Praise on camera: "their team is just doing awesome work… Finn and his whole team is incredible." ASR renders Prospeo as "Prospio." |
| **Phone enrichment** | **LeadMagic** | "One that we use a lot for mobile phones in particular." |
| **Email verification** | **MillionVerifier** | Returns good / risky / bad (technically: valid / catchall / risky). Non-negotiable stage — "you're basically only wanting to send cold email to valid emails." |
| **Inbox + domain infrastructure** | **Hypertide** ⚠︎ · **Inbox Kit** · Instantly's own inboxes | Frame 0100: "Automated Cold Email Infrastructure Across Google, Microsoft, and Entra — high-deliverability inboxes connected to your favorite sending tool in hours." ~**$100/mo for ~10,000 sends/mo** of inbox capacity; comparable across providers; Inbox Kit "runs sales all the time." |
| **Sending platform** | **Instantly** (`instantly.ai`) | Frames 0095/0112/0120 — pricing tiers visible: **Growth $47/mo · Hypergrowth $97/mo · Light Speed $358/mo · Enterprise custom**. API + **webhooks** (positive-reply webhook is the reply agent's trigger). Frame 0095 shows product nav including "Create Sales Agent / Create Reply Agent / Find Leads." |
| **All-in entry cost** | **~$200/mo** | ~$100 inboxes + ~$97 sending tier ≈ $200 to run ~10k sends/month. His figure, entry tier. |
| **LinkedIn DM sending** | **HeyReach** · **BotDog** | Both have APIs. He also notes people "using LinkedIn InMail for this and seeing incredible success right now." ASR: "hey reach," "Bot Dog." |
| **Post scheduling (organic)** | **Ordinal** ⚠︎ | API + **MCP**. Multiple LinkedIn accounts on one workspace, accounts can interact with each other, and it surfaces **per-post analytics per account** — the return path that closes the loop. |
| **Drafting model** | **Claude Sonnet** | "We've even used just Claude Sonnet as an example and it's probably good enough on the writing side." |
| **Hosting** | **Railway** · **Heroku** | "A server is just a computer that is on all the time somewhere else that you're putting code onto." |
| **Data pipeline / warehouse** | **Airbyte** → **ClickHouse** | Frame 0134 slide (editorial recap of his prior episode): sources (Facebook Ads, Google Analytics, PostHog, HubSpot CRM, Stripe) → Airbyte (open source, self-host, pre-built connectors, "Claude Code sets it up") → ClickHouse ("every source in context, ties the ad to revenue") → the agent (Heroku or Railway). **"Reads come from the warehouse. Writes go through the API. That is the rule."** |
| **Booking / ground truth** | **Calendly** or **Cal.com** | Agent gets read access so outcome is *observed*, not inferred. ASR renders Calendly as "Kalanley." |
| **Media generation (aside)** | Nano-banana-class image gen; **Seedance**-class avatar video; **Kling** for image→video | Mentioned only as evidence for "marketing is just code" — a JSON prompt and an API call under the hood. |

## Waterfall reference numbers (his worked example)

```
50 LinkedIn profile URLs in
 → tier 1 (GetLeads)   : 32 found        (64%)
 → tier 2 (Apollo)     : +10 of 18       (56% of remainder)
 → tier 3 (Origami/Prospeo/LeadMagic) : 8 residual passed down
 = ~84% cumulative, "this is the way that you get to an 80% find rate"
 → MillionVerifier on everything before a single send
```

## Live-demo output shape (frame 0071, ~11:30)

```
● 61 unique engagers extracted • api…
    Counter({'reactor': 52, 'commenter': 9})
    obfuscated/no-slug: 52
  - All 52 reactor rows have obfuscated [URNs]
  - that's normal for the reactions [endpoint]
  Next step: src/resolve-linkedin-urls-exa.ts
  - Exa-resolve reactor URNs to public [profiles] → Verifier
  Sauntered for 34s
```
Narrated as "63 raw" deduped by public profiles → 61 unique. **~85% of a reaction pull needs a second resolution pass** (he uses Exa). Comments resolve cleanly. This is the reference standard for `blind-pass-log.md`.

## Platform behaviors claimed (2026-08, verify before relying on)

- **UNCONFIRMED** — LinkedIn shipped an AI-slop detection/flagging feature "this morning" (i.e. ~2026-08-05).
- **UNCONFIRMED** — LinkedIn average paid CPM ≈ **$22 per 1,000 impressions**, used for his earned-media arithmetic. Real CPMs vary widely by targeting and season.
- **UNCONFIRMED** — the "~80% niche surface-area coverage from 10-20 creators" heuristic. Stated from practice, no methodology given. Working heuristic, not a measurement.
- **Legal, as he states it** (not legal advice, and he says so twice): buying contact data from brokers is legal in the US; *use* is regulated (CAN-SPAM checklist for cold email and newsletters); EU rules differ materially. "Take this with a grain of salt." "Do your own research."

## Farrice-house note

None of the sending stack is live here. `execution/signal_scout.py` uses only the **sourcing API + apimaestro reactions/comments actors**, through `apify_client.run_actor` (monthly $29 guard, $5/run cap). Default scope (≤10 creators × 3 posts) runs well under $2. Everything from "enricher" down in the table above exists in this skill as **client-facing design knowledge**, not as installed infrastructure.
