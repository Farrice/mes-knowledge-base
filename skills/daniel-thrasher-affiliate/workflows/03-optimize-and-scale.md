---
name: "Optimize and Scale"
produces: "A tracking architecture with parameterized links per placement, 1-3 north-star metrics, a split-test plan, an email-layer go/no-go decision, and an AI/automation opportunity map"
expert: "Daniel Thrasher"
load_context: "genius.md"
---

# Optimize and Scale

## Role

You are running the back half of Thrasher's skill ladder on a live campaign: analytics (skill #5), email marketing (skill #6), and AI/automation (skill #7). The governing rules: gut-feel strategies are worthless without measurement; email is a second-act channel that can flip a profitable funnel into a flop if added too early; and AI/automation amplify competence — they never substitute for it.

## Input Required

1. **Live campaign state** — offer, bridge page(s), traffic channel, and every placement where a tracking link appears (popup, sidebar, in-article, ad, bio link…)
2. **Current numbers** — traffic, clicks, conversions/sales to date, per placement if available
3. **Analytics access** — what's already set up (network reporting, Google Analytics, page-builder stats, platform dashboards)
4. **Primary channel status** — growing, plateaued, or declining (drives the email decision)
5. **Operator's workflow** — the step-by-step process they run for this campaign (needed for the automation map)

## Workflow

### Phase 1 — Instrument Everything

1. Create a parameterized tracking link per placement — traffic source, traffic type, campaign, creative, ad. Each distinct placement (popup vs. sidebar vs. in-article banner) gets its own tracking ID so every click and commission traces to its origin.
2. Layer analytics per funnel stage: platform/ad dashboards for the traffic source; Google Analytics or page-builder stats for the bridge page (views, conversion rate); network reporting for hops and sales.
3. Pick **1-3 north-star metrics** the whole campaign optimizes toward (e.g., search traffic + page conversion rate + commissions). Every other metric is diagnostic. The true north star is whether the campaign makes money.
4. Design the split-test queue for the bridge page: one element at a time (headline → hero image → CTA wording → colors), judged on visits, conversions, and statistical significance against the page's own past performance. Pages should perform better over time, not just today.

### Phase 2 — Email Layer Decision

1. **Gate first**: Is the primary traffic channel maxed out or plateaued? If not — defer email; spreading thin between mastering a channel and building a list is the classic mistake. Record the revisit trigger.
2. If GO, design with friction eyes open: an opt-in step mid-funnel trades first-touch conversions (often the best chance, especially with cold paid traffic) for owned-audience lifetime value; expect ~20% open rates, meaning most subscribers miss any given send.
3. Build plan: opt-in forms (name + email minimum), a welcome series that introduces the operator and brand while plugging the initial offer, deliverability and sender-score monitoring, ongoing pruning/segmentation of unengaged subscribers.
4. Map the cross-sell runway: brainstorm the avatar's adjacent pain points (overall health, relationships, hobbies, career) and list complementary offers the same list can monetize — email is also the hedge against the single-point-of-failure risk of one traffic channel.

### Phase 3 — AI and Automation Map

1. Break the campaign's operating workflow into individual steps (e.g., keyword research → outline → draft → edit → publish → track).
2. Flag steps that cost the most **time** or the most **money** (e.g., outsourced writing).
3. Assign AI only to steps the operator already does competently: research, ideation, outlining, angle-coverage checks, editorial feedback on drafts, concept mockups.
4. Assign automation to repetitive grunt work that needs no judgment: no-code tools (Make, Zapier), scripts, and — first — the automation features already inside tools the operator owns (ESP triggers/segments, scheduler features).
5. Place a human-in-the-loop checkpoint on every AI/automation output for quality and tone. Never automate a step that hasn't been done manually first.

## Output Contract

- **Tracking architecture**: table of placements → tracking IDs/parameters → what each reveals
- **North-star metrics**: 1-3, named, with current baseline and the money metric explicit
- **Split-test queue**: ordered element list with success criteria (visits, conversions, significance)
- **Email decision**: GO/DEFER with the gate evidence; if GO, the opt-in + welcome-series + hygiene plan and cross-sell runway; if DEFER, the revisit trigger
- **AI/automation map**: workflow steps → time/cost flags → AI or automation assignment → human checkpoint

## Quality Gate

- [ ] Every placement has its own tracking ID — no aggregate-only reporting
- [ ] North-star metrics number 1-3 and include the money metric
- [ ] Split tests change one element at a time with a significance standard
- [ ] Email decision explicitly checks the primary-channel-plateau gate before recommending a list
- [ ] No AI/automation assignment on a step the operator hasn't demonstrated manually
- [ ] Every automated output has a named human checkpoint
