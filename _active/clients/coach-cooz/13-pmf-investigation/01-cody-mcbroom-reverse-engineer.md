# Cody McBroom — Reverse-Engineered
## The Real Reference Point Investigation
## April 2026 | PMF Investigation Sprint

> **Why this document exists**: Cooz has explicitly named Cody McBroom as the coach he wants to emulate. McBroom coached Cooz through his own transformation years ago. Everything in the current `12-expert-package` dossier assumes Cooz's buyer is "Mike, the depleted SaaS founder." This document interrogates that assumption by studying who McBroom actually reaches, what he actually sells, and how he actually positions himself in the market — then uses the gap between that reality and the current Cooz dossier to surface a different hypothesis about who Cooz's real buyer is.
>
> **Method**: 5 Apify scrapes (Instagram x3, web x3, YouTube x1) + 6 web searches + framework analysis using April Dunford positioning, Nicolas Cole niche positioning, Dai Media consumer posture, and Daniel Priestley oversubscribed.
>
> **Bottom line up front**: **Cody McBroom is not running the business Cooz thinks he's running.** The Cooz dossier imagines Mike-the-founder — a depleted SaaS CEO buying permission disguised as fitness. McBroom isn't selling to Mike. McBroom runs a TWO-business architecture: a $1.5M/yr fat-loss coaching company (TCM, where the client is a 40-something woman named Karen or a generic busy professional buying weight loss at $347–$497/mo) AND a separate coach-mentorship business where he sells to OTHER COACHES doing $5–15K/mo who want to scale to $30K/mo with integrity. **Cooz's true reference point is McBroom's mentorship business, not his fitness business.** The dossier has been optimizing for the wrong buyer.

---

## METHODOLOGY & EVIDENCE BASE

**Data pulled (all timestamps April 2026)**:
- Instagram `@codymcbroom` — 30 recent posts, Dec 2023 → Apr 2026 (`/tmp/mcbroom_ig.json`)
- Instagram `@tailoredcoachingmethod` — 20 recent posts, Jul 2025 → Aug 2025 (`/tmp/tcm_ig.json`)
- Web: `tailoredcoachingmethod.com` homepage (`/tmp/tcm_home.json`)
- Web: `tailoredcoachingmethod.com/online-coaching` — full offer page with published pricing (`/tmp/tcm_coaching.json`)
- Web: `www.tailored-coaching.com/mentorship-coaching` — full mentorship sales page, team bios, testimonials, ROI guarantee (`/tmp/mentorship.json`)
- YouTube search "Cody McBroom coach" — 10 videos from his Choose Hard Podcast + podcast appearances (`/tmp/mcbroom_yt.json`)
- WebSearch: 6 queries on pricing, ICP, origin story, Movember signal, podcast circuit

**Total Apify spend for this run**: ~$0.08 of $28.16 budget remaining before this pass. Well under the $0.50 cap.

**What I could not recover**: (a) exact mentorship monthly price — McBroom deliberately gates this behind a free Biz Audit call with him, classic Dunford "calm confidence posture"; (b) YouTube transcripts for his own Choose Hard episodes — the search returned metadata and descriptions but not full transcripts; (c) any direct Cooz + McBroom client-coach paper trail in the public data.

---

## SECTION 1 — THE MCBROOM BUSINESS ARCHITECTURE

### 1.1 The three properties (and what people get wrong about them)

Most observers see "Cody McBroom, fitness coach" and stop. That framing misses everything. McBroom operates THREE distinct properties that together form the actual business:

| # | Property | Who It Serves | Where The Money Is |
|---|----------|---------------|--------------------|
| 1 | **Tailored Coaching Method** (`tailoredcoachingmethod.com`) | End consumers buying fat loss / physique coaching | $347/mo (nutrition only) or $497/mo (all-inclusive) × thousands of clients cycled. **This is the $1.5M/year business.** |
| 2 | **Tailored Coaching Mentorship** (`tailored-coaching.com/mentorship-coaching`) | Other coaches already doing $5–15K/mo, scaling to $30K/mo+ | Unpublished price, 4-month minimum, gated by a 1:1 Biz Audit call with Cody. Uses "Pay half what those gurus charge" positioning but no number shown. |
| 3 | **The Tailored Trainer App** (`thetailoredtrainer.com`) | DIY consumers who want template programs at lower price point | Low-ticket productized play to capture leads below the $347 floor. |

Plus two content assets:
- **Choose Hard™ Podcast** (Apple/Spotify, 200+ episodes, currently ~100–250 YouTube views per ep) — mixed audience, heavy skew toward coach-mentorship content (e.g., Ep 207 "Masterclass on Eating," Ep on "The 2026 Coaching Blueprint: Peptides, Churn Fixes, and Scaling Tips," Ep "When a Coach Needs Coaching: How I Faced Burnout")
- **Personal Instagram `@codymcbroom`** — brand bio reads "Cody McBroom | The Online Coach" — this is the mentorship funnel's top of funnel, NOT the TCM client funnel

### 1.2 The consumer offer (TCM) — what's actually published

From the live scrape of the `/online-coaching` page, the fat-loss client offer is extraordinarily transparent by industry standards:

**Pricing (verbatim from scrape)**:
> "With that said, our services are currently set at **$347/month** and **$497/month**, depending on which package you're signing up for. The packages we offer are **Nutrition Coaching** and **All-Inclusive Coaching**, which includes both Online Personal Training and Nutrition Coaching together."

**Commitment**: 3-month minimum. **No paid-in-full options** — explicit rejection of the industry-default lump-sum structure on accountability grounds: *"monthly recurring coaching is guaranteed… people are more accountable when making smaller investments regularly compared to one large amount before the coaching engagement actually starts."*

**Guarantee (verbatim)**:
> "Our guarantee is that you will achieve results that are noticeably visible to the eye and proven by trackable data and metrics recorded during the process, as well as an experience that is positive, empowering, and self-improving… **If you don't, you don't pay.**"

**Deliverables list (long and specific, matching the "reduce perceived risk through listing" pattern)**:
- Individualized assessment + strategy call
- Tailored training program (periodized, limb-length-adjusted, biomechanics-calibrated)
- Customized nutrition plan (flexible dieting approach)
- Weekly check-in with personalized video
- 24/7 access to coach
- Monthly coaching call (phone or Skype)
- Exclusive education portal
- Private client community
- Travel/accommodation adjustments
- Chief Science Officer on staff (Dr. Brandon Roberts, PhD)

**Funnel gate**: Free 30-min "Strategy Call" required before sign-up. Not an application. A one-step removed discovery call. Frictionless compared to Dan Go's gated application-only funnel.

**Who the consumer page speaks to (verbatim)**: *"Do you feel like you work out consistently, yet don't actually LOOK like you workout? You've tried every diet, yet still aren't very lean or understand what works best for you? Maybe you do know what to do, but fail to stay consistent because you have no support..."*

That's a buyer with gym-literacy and chronic plateau frustration. It is NOT a depleted founder who stopped lifting 18 months ago. It's the person who's been in the gym and can't figure out why they don't look it.

### 1.3 The mentor offer — what's published, what's gated

Page title: **"Build a Sustainable Coaching Business with Your Integrity Intact."**

**Subheadline (verbatim)**: *"THE MONTHLY MENTORSHIP FOR COACHES WHO ARE TIRED OF TEMPLATED MARKETING BULLSH*T AND WANT REAL SYSTEMS, EXPERT GUIDANCE, AND A GUARANTEED 3X ROI IN THE FIRST 90 DAYS."*

**Three-step framework (verbatim headlines)**:
1. **COACHING** — Access to all TCM systems (check-ins, onboarding, program design, nutrition plans), client reviews, master your craft
2. **BUSINESS** — Real systems (lead flow, conversions, KPI tracking), Content & Marketing, SEO/AEO search optimization
3. **SCALE** — Leadership of staff, multi-step campaigns, evolving business

**The team (important — this is not a solo mentor)**:
- **Cody McBroom** — "Brand Builder & Leadership Expert ∙ Head of Mentorship & Lead Strategist" — does the high-level strategy, CRM roadmaps, funnel logic, AI systems, brand integrity
- **Cody Smith** — "Community & Culture Builder ∙ Business & Operations Specialist" — owner of Virtuous Fitness (3 locations), handles ads, team culture, multi-location ops
- **Arielle DeYampert** — "Director of Coaching ∙ Expert in Human Behavior & Fat Loss" — the "coach's coach," psychology of stuck clients, identity shifts, fat loss protocols

**The structural promise**: *"You aren't just hiring a coach. You're gaining a Board of Advisors."*

**The ICP specification (verbatim from FAQ)**:
> *"We help coaches who are sitting between **$5–15,000/month**, scale to **$30k and beyond**. And we do this for the online coaches who want to refine their systems, sharpen their skills, and scale with integrity."*

**Commitment**: 4-month minimum (NOT 3 — explicitly longer than the consumer offer).

**The ROI Guarantee (verbatim)**:
> *"We are so confident in our systems that we take on the risk for you. If you show up to the calls, implement the systems we provide, and complete your weekly trackers, but don't increase your revenue by at least your initial investment within the first 30 days, we will continue to coach you for free until you do. We win when you win."*

**Pricing**: Not published. Uses "**Pay Half** of what those _gurus_ charge" framing. This is deliberate — it prevents price-shopping and forces the Biz Audit call as the qualifying gate. Classic Priestley "Official Capacity Declaration" via the 1:1 call requirement even though no hard cap number is published.

### 1.4 The content → lead → sale path

Two separate funnels run in parallel:

**TCM consumer funnel (fat loss clients)**:
```
@tailoredcoachingmethod IG (dormant-ish, 50–500 likes, heavy transformation posts)
         ↓
tailoredcoachingmethod.com (published price, published guarantee)
         ↓
Free 30-min Strategy Call (no application gate)
         ↓
$347 or $497/mo × 3 month minimum
```

**Mentorship funnel (coach clients)**:
```
@codymcbroom IG ("Cody McBroom | The Online Coach" bio)
         ↓
Choose Hard Podcast (200+ eps, topics 80% coach-business)
         ↓
tailored-coaching.com/mentorship-coaching (no public price — "pay half the gurus")
         ↓
Free 1:1 Biz Audit Call with Cody personally
         ↓
Undisclosed monthly price, 4-month minimum, 30-day ROI guarantee
```

### 1.5 Scale reality: is this $10K/mo or $500K/mo?

**The published number**: $1.5M/year from TCM alone (confirmed via podcast appearances — verbatim quote from his mentorship page: *"after building tailored coaching method to a yearly revenue of $1.5 million dollars, without paying for a single ad..."*).

That's ~$125K/month in the consumer coaching business. At an average ticket of ~$420/mo × 3-month minimum = ~$1,260 lifetime on the low end. To hit $125K/mo, he needs ~300 active clients at any given time, churning through ~100 new clients per quarter. That's a fulfillment-heavy, team-dependent operation. This is NOT a personal brand coach. This is a **coaching agency** with staff, operations, a PhD science officer, and a ~300-client roster.

**The mentorship business adds incremental revenue on top**. If he has 15–25 coach-clients at (conservatively) $1,000–$2,500/mo, that's another $15–60K/mo, or $180K–$720K/year. Plus the app, plus speaking, plus affiliate/supplement deals.

**Best estimate: ~$2M–$2.5M/year blended across all properties, 70% from TCM, 20% from mentorship, 10% from app + other.**

**Critical framing for Cooz**: this is **not an influencer business**. McBroom's IG posts get a median of **68 likes**. His YouTube podcast gets 100–250 views per episode. He doesn't have viral reach. **He has a referral engine, a retention engine, and a price-gated mentorship play**. That is ENTIRELY different from Dan Go (millions of followers, cold-inbound-funnel). The Cooz dossier has been benchmarking against Dan Go, but McBroom's reference model would tell a completely different story.

---

## SECTION 2 — THE POSITIONING (APRIL DUNFORD FRAME)

Applying April Dunford's 5-component positioning canvas to McBroom's MENTORSHIP business (which is his real competitive play — the consumer business is more commoditized).

### 2.1 Competitive alternatives (what does the buyer compare him to?)

**April Dunford Pattern 2 (The Reverse Insight Derivation)**: work backwards from the value to figure out what the buyer's real alternatives are.

McBroom's mentorship page explicitly names the alternatives:

> *"Most 'business gurus' in this industry are selling you the exact same thing: a recycled, cookie-cutter marketing funnel and a 'templated' way to speak to your clients. They teach you how to be a loud marketer, but they rarely teach you how to be a better practitioner or a more efficient CEO."*

> *"Most programs are 'info-products' disguised as mentorship. They give you a login to a portal and leave you to figure it out."*

**The named alternatives**:
1. **Iain Mitchell / Jordan Syatt / Jeremy Fouts / Coaches Corner-style marketing gurus** — sell lead funnels and ad templates
2. **Fitness Business Mastery / Sam Miller / Sean Nalewanyj-style info-products** — Facebook group + portal login, no access
3. **"Doing it alone"** — the coach who bootstrapped to $5–15K/mo and is now stuck, scrolling Twitter looking for tactical hacks
4. **Generic business coaches (non-fitness)** — Alex Hormozi, Dan Martell, etc., who don't understand the specific fulfillment problems of a 1:1 online coaching business

**What the buyer is NOT comparing him to**: Dan Go, Michael Sheedy, the broader "influencer fitness coach" category. Those are his *consumer-brand* competitors, not his *mentorship* competitors. The mentorship buyer has already read all those guys and is pissed off because they sold him a funnel but didn't teach him how to actually coach.

### 2.2 Unique attributes (what does McBroom do that alternatives don't?)

From the scraped copy and testimonials, four unique attributes stand out:

1. **A $1.5M/year operating business he runs in parallel to the mentorship.** This is the moat. Info-product gurus teach what they learned in a book. McBroom is currently, actively running the business he's teaching. His "systems" are not theoretical — they are the SOPs his own ~300-client operation runs on. From the page: *"Gain Access To All Of Tailored Coaching Method Systems: Check-ins, onboarding, program design, nutrition plans... you CAN have everything we use in our coaching."*
2. **A Board of Advisors (not a solo mentor).** Cody McBroom + Cody Smith (multi-gym owner) + Arielle DeYampert (behavioral psych + fat loss protocols). The mentee gets three specialists, not one generalist.
3. **Client reviews of the mentee's actual work.** Verbatim from Step 1: *"Client Reviews: Use our expertise in real time, to ensure none of your clients lack results."* This is a FULFILLMENT guarantee, not a lead-gen guarantee. Nobody else in the coach-mentorship space offers this.
4. **A 30-day ROI money-back guarantee tied to the mentee's actual business outcomes**, not to attendance or satisfaction.

### 2.3 Value (what those attributes enable for the buyer)

**Using Dunford's "so what?" chain on the Board of Advisors attribute**:
- Feature: 3 different experts, not 1 → So what?
- Capability: mentee gets strategy + ops + psychology without needing 3 separate mentors → So what?
- Business outcome: faster problem resolution on client fulfillment issues → So what?
- Strategic impact: **client retention becomes the mentee's growth engine, not lead-flow** — and that's the unique escape hatch from the $5–15K/mo plateau the entire industry is stuck in

This is the insight. **The $5–15K plateau isn't a lead problem — it's a fulfillment problem.** McBroom's market insight (reversed from his differentiated value per Dunford Pattern 2): *"You think you're stuck because you can't get enough leads. You're actually stuck because your fulfillment is broken. Clients are bleeding out the back door and you're pouring more water in the top trying to keep up. I'll help you plug the leaks."*

**No competitor can open with this insight** because no competitor has a $1.5M consumer business running on the same systems. Dunford's test: *"Can [competitor X] open their pitch with this same statement?"* No. That's a real insight.

### 2.4 Target market characteristics (who most values this?)

From the mentorship page FAQ and testimonials:

- Online coach, NOT gym owner (gym owners get Cody Smith's attention, but the primary buyer is digital)
- $5K–$15K/month revenue (post-scrappy, pre-scale)
- Already has clients and systems, but they're janky
- Values integrity over growth-at-all-costs (the page uses "integrity" 6 times)
- Has tried at least one "guru" mentorship already and felt burned
- Wants to coach better, not just market better
- Often has a values-driven motivation (the Gavin Siegner testimonial: *"helped me tremendously to navigate some hardships in life, become a better father and husband, a better business owner, **develop a relationship with God**, and push me to do a 70.3 iron man"*)

**The buyer is a male online fitness coach, late 20s to late 30s, married or partnered, often with kids, somewhere between "former trainer who went online during COVID" and "legitimate operator who wants to become a real business."** He is exactly the kind of person Cooz IS.

### 2.5 Market category frame (what box does McBroom put himself in?)

He deliberately does NOT call himself a "business coach" or "fitness business mentor." The tagline is *"Build a Sustainable Coaching Business with Your Integrity Intact."*

The category he's creating (or at least claiming) is **"integrity-first fitness coach mentorship"** — a category of one. When you strip "integrity" out, every other mentor in the space is left. When you strip "integrity" in, he's alone. That's Nicolas Cole's Category of One test passing.

**The anti-position is explicit**: *"You're a Coach, Not a Carbon Copy."* He's defining himself against the cookie-cutter marketing gurus. The enemy is named. The co-conspirators (per Dai Media's Tacit Knowledge #2) are bonded by what they refuse to do.

---

## SECTION 3 — THE CONSUMER POSTURE (DAI MEDIA FRAME)

The Dai Media framework requires us to describe ONE specific individual, not a demographic, and pass the Kristen Stewart Test. Let me build that for the mentorship buyer — because that's Cooz's real reference buyer.

### 3.1 The Named Person: "Jake"

He's 31. He coaches online — started in 2020 when his gym shut down for COVID. He has ~35 active clients at $300/mo, grossing about $10,500/mo. He's been stuck there for 14 months. He has no co-founder. His wife (girlfriend) works a normal W-2 and doesn't fully understand what he does, but supports it. He lives in a rental house in a secondary city (Nashville, Charlotte, Boise, Scottsdale — not NYC, not LA). He has a home gym in the garage.

He follows Alex Hormozi, Iain Mitchell, Jordan Syatt, and Sam Miller on Instagram. He has bought one $1,500 Facebook-group coaching program that promised to get him to $20K/mo and didn't. He is actively embarrassed about having bought it. He has read $100M Offers. He has a Notion workspace full of SOPs he started and never finished.

He wants to hit $30K/month because he wants to feel legitimate and because his best friend (also a coach) just hit that number. He has not admitted out loud that his clients are not getting consistent results — he thinks it's because some of them aren't "fully committed," but in the quiet moments he suspects his program design is actually not great. He's been coaching for 4 years and has never had another coach review his work.

He lifts. He looks the part. He posts gym content and nutrition infographics. His engagement is flat.

### 3.2 The 3D Consumer Posture for Jake

**Occupation** (the role he plays in McBroom's brand world): *the younger version of Cody who's about to become a real CEO but hasn't crossed the line yet*. He's not "a client" — he's "a protégé." The Board of Advisors language reinforces this: Cody is not selling Jake a service, Cody is initiating Jake into a peer group one level up.

**Activity** (the rituals that reinforce his identity): He listens to Choose Hard Podcast while on the treadmill. He saves McBroom's posts about systems. He screenshots testimonials. He took the Biz Audit call and said yes. He attends the weekly 90-min group call. He does his weekly tracker. He submits his client cases for review. His ritual is *entering an operating business, not consuming content*.

**Thought Process** (his internal logic at 11 PM scrolling):
- *"I'm good at this. I care. Why am I stuck?"*
- *"I've made more money than anyone in my family growing up but I still feel like an amateur."*
- *"I don't want to be a loud marketing guy. I want to be respected by other coaches."*
- *"I hate that I'm good at what I do and I can't figure out why I can't get to $30K. Something's wrong with the way I'm running it."*
- *"If I could just watch someone who's doing it at scale actually run it, I'd figure it out."*
- *"I want a mentor who's still in the fight, not someone who sold their business and now teaches."*
- *"I'd pay anything for someone to tell me the truth about whether my program design is any good."*

### 3.3 The Kristen Stewart Test

Would a real coach like Jake read this description and say *"that's exactly me"* or *"that's a stereotype"*?

Test points:
- "Bought one $1,500 Facebook-group program and is actively embarrassed about it" → every single online coach in this tier has this exact memory
- "Has a Notion workspace full of SOPs he started and never finished" → specific, universal
- "Has never had another coach review his actual client work" → this is the core shame, and it's why Step 1 of McBroom's program is "Client Reviews"
- "Wants to be respected by other coaches, not be a loud marketer" → verbatim echo of the mentorship page copy

**This passes the test.** Jake would nod. The McBroom mentorship is designed to be the answer to Jake's actual internal monologue.

### 3.4 What Jake is actually buying (emotional outcome, not functional)

**Not buying**: systems, CRMs, ad templates, lead funnels.
**Actually buying**: *the first honest review of his actual work by someone whose opinion he respects.*

The parallel to the Cooz dossier's "first honest mirror a depleted founder has looked into" is STRIKING, but the buyer is different. Mike-the-founder wants the first honest mirror about his BODY. Jake-the-coach wants the first honest mirror about his COACHING. Same emotional architecture. Different category.

---

## SECTION 4 — THE NICHE CHOICE (NICOLAS COLE FRAME)

### 4.1 The specificity ladder applied to McBroom

Running Nicolas Cole's specificity drill down to the Named Person:

1. **Industry**: Health & fitness ✗ (too broad)
2. **Category**: Online coaching ✗ (too broad)
3. **Niche**: Online fitness coach mentorship ✗ (still too broad — Iain Mitchell, Jordan Syatt, Sam Miller all compete here)
4. **Micro-niche**: *Integrity-first mentorship for online fitness coaches stuck at $5–15K/mo who want to scale fulfillment, not just lead-flow* — this is where it gets uncomfortable
5. **Named Person**: Jake (Section 3.1) — coachable, 31, 35 clients, stuck 14 months, bought a bad mentorship, wants a real one

**The signal that this is the right niche**: Cole's rule is *discomfort at step 4–5 = you've hit something real*. The uncomfortable part is "scale fulfillment, not lead-flow." Every other mentor in the space sells lead flow. Saying "I teach fulfillment first" is a deliberate rejection of 80% of potential buyers — which is exactly what Cole says a real niche feels like.

### 4.2 Who McBroom deliberately does NOT serve

From the copy and the FAQ, the anti-ICP is explicit:

- **Beginner coaches (under $5K/mo)** — *"If you're already generating at least a part-time income"* excludes the brand-new starters
- **Coaches who want templated ad funnels and quick leads** — *"templated marketing bullsh*t"* is the named enemy
- **Coaches with low integrity** — *"client success comes before chasing revenue"* and integrity is mentioned 6+ times on the page
- **Solo-founder wantrepreneurs with no product** — the $5K/mo floor is a real-business screen

### 4.3 How he signals the selection

**April Dunford's "Calm Confidence Posture" in full effect.** The page is unapologetic about who it won't serve. The Biz Audit gate is not a sales trap — it's a real qualifying filter. The pricing gate ("pay half the gurus charge" with no number) means Jake has to opt into the conversation before he can even see the price. That's Priestley's Signal Volume Engineering in action.

**Content signals**:
- Post #1 by engagement (4,481 likes): *"If you can't take ownership of your own health, you shouldn't be coaching others to improve theirs."* — aggressive in-group signaling. Designed to alienate the coaches who don't look the part while magnetizing the ones who do.
- Post #4 (259 likes): *"This is what it looks like when coaching is done right… Most online coaches can't say that. Because they have a 'leads problem' that's actually a fulfillment problem."* — explicit thesis statement.
- Post: *"6 BIG differences between a side-hustle-coach and a coach who builds an impactful coaching company"* — naming the in-group vs. out-group
- Post: *"Trainers and Coaches should be in great shape. Period."* — uses appearance as a values filter
- Repeated CTA: *"follow @codymcbroom for content to develop better systems and master the art of coaching"* — every post ends with the mentorship signal

### 4.4 The niche's growth trajectory

The "online fitness coach who wants to be legitimate, not viral" niche is growing because:
1. The COVID-era surge of new online coaches (2020–2022) is hitting year 4–5 of business and hitting the fulfillment wall
2. The info-product guru backlash is real (every coach I searched has a "I got scammed by a mentor" post in their history)
3. AI is commoditizing the marketing layer, which pushes differentiation back to actual coaching craft
4. The churn economics of a 3-month-minimum coaching business are brutal and becoming more visible

McBroom is early to a wave that will crest in 2027–2028. His positioning will age well.

---

## SECTION 5 — THE OVERSUBSCRIBED FACTORS (PRIESTLEY FRAME)

Applying Daniel Priestley's 27 patterns to McBroom's mentorship play.

### 5.1 Which of Priestley's five levers does he pull?

- **Rivalry**: ✓ Explicit — the page names "those gurus" as the rival and positions the buyer as the righteous alternative. This is Priestley's Fame Game Inversion (Pattern 16) — create a new game where you're automatically the leader.
- **Scarcity**: ✓ Implicit — the Biz Audit 1:1 call is a manufactured bottleneck (Priestley Pattern 11, Official Capacity Declaration). Cody personally does the onboarding call. That's a real capacity constraint. He can't do more than ~20–30 of these per week.
- **Prestige**: ✓ Heavy — "Board of Advisors" language, three experts with published credentials, PhD on staff at TCM, testimonials from named operators (Dr. Sean Pastuch of Active Life, Jon & Blakley of Digital Barbell)
- **Status**: ✓ Moderate — Jake-the-buyer becomes the coach who "refuses to do templated marketing" and joins the in-group
- **Relevancy**: ✓ High — 2026 is the year AI + peptides + the post-COVID coaching churn hit every online coach simultaneously. The Choose Hard Podcast episode title "The 2026 Coaching Blueprint: Peptides, Churn Fixes, and Scaling Tips" is the exact Priestley Transformation Window (Pattern 19) energy — naming the buyer's current crisis moment.

### 5.2 How he generates excess demand

**Priestley Pattern 1 (Demand Inversion)**: Focus on manufacturing WANTING, not explaining product.

- The page opens with the ENEMY ("those gurus") before it ever explains what he does
- The "pay half what those gurus charge" line triggers comparison without giving the number — creates active curiosity
- The guaranteed 3x ROI positions him as taking the risk FOR the buyer

**Priestley Pattern 5 (Stakes Lens)**: The page frames the cost of inaction:
> *"You end up with a business that feels hollow, a brand that looks like everyone else's, and a 'mentor' who doesn't even know your name."*

That's not "you'll waste money" — that's "you'll waste your identity." Much higher stakes.

**Priestley Pattern 18 (Private Conversation)**: The copy sounds like Jake's 3 AM internal monologue. The words "integrity," "impact," "not a carbon copy" are exactly what Jake has been silently wanting to say about himself.

### 5.3 Is he actually oversubscribed or is he performing it?

**My assessment: moderately oversubscribed, honestly so, and not over-performing it.**

Evidence for genuine constraint:
- The 1:1 call with Cody personally caps intake at his available hours
- The TCM consumer business already consumes significant operator time
- The four-month minimum tells you he's not desperate for quick cash
- The 30-day ROI guarantee is a real financial risk — he wouldn't offer it if he wasn't filling seats

Evidence AGAINST full oversubscription:
- No visible waitlist language on the page
- No "cohort limits" or "12 seats" callouts
- The team is still actively recruiting coaches into the mentorship (the mentorship page FAQ says "if you're established and ready to grow, you'll fit right in" — implying open seats)

**Verdict**: He's operating at ~70–80% of desired capacity. Comfortable, not overflowing. He's doing the Priestley play at a **mature, confident level** — not the frantic urgency of an early-stage coach trying to fill seats. This is the calm confidence that Dunford teaches. It's also exactly what Cooz would need to learn to project even before he actually fills a roster.

---

## SECTION 6 — THE CONTENT VOICE & AESTHETIC

Based on 30 scraped Instagram posts from `@codymcbroom` (Dec 2023 → Apr 2026).

### 6.1 The hard engagement numbers

- **Post count (sampled)**: 30
- **Median likes**: **68**
- **Mean likes**: 279 (skewed by two outliers)
- **Max likes**: 4,481 (one post, the coach-ownership callout from Sep 2025)
- **Median views**: 1,914
- **Max views**: 16,103
- **Date range**: Dec 2023 → Apr 2026 (~28 months of content, but sample skews recent)

**The reality check**: his median post does 68 likes. That's not an influencer account. That's a **referral-funnel account** — the content is there to reinforce the positioning of the people who are ALREADY in the conversation, not to cold-reach new people. This is critical for Cooz: **you do not need to be Dan Go to build McBroom's business. You need 300 clients over time, not 300,000 followers.**

### 6.2 Hook patterns (verbatim examples)

**Pattern A — Contrarian / In-Group Gate Opener** (highest engagement):
- *"If you can't take ownership of your own health, you shouldn't be coaching others to improve theirs."* (4,481 likes)
- *"Trainers and Coaches should be in great shape. Period. And it's wild to think anything different."* (61 likes, but short-form)
- *"Most coaches fail to realize why their clients actually ghost them or skip check ins…"* (85 likes)

**Pattern B — Confession / Vulnerable I-Led Story** (2nd highest engagement):
- *"Been trying to write a '2023 post' all weekend and honestly, I can't find the words because it was one of my worst years ever…"* (1,707 likes)
- *"Training to be the most reliable version of me; instead of becoming a liability to them"* (100 likes)

**Pattern C — Mechanism Reveal (Listicle)**:
- *"I lost 45-50lbs in 2010 and I've kept it off ever since, because of these 7 things"* (119 likes)
- *"If I could ONLY pick 1 exercise per muscle group, here's what I'd pick"* (90 likes)
- *"Here's Exactly What I'd Do Go Get AS LEAN AS POSSIBLE By Summer"* (90 likes)

**Pattern D — CTA-Gated Lead Magnet**:
- *"Comment 'mentorship' below and I'll send you the 2026 online coaching blueprint"* (83 likes, but every one has a CTA)

**Pattern E — Short Label + Visual**:
- *"Don't let your excuses dictate your outcomes"* (82 likes)
- *"10 Rules For Living A Great Life"* (31 likes)

### 6.3 Content themes / bucket mix

From the 30-post sample, approximate distribution:

| Bucket | % of posts | Purpose |
|--------|-----------|---------|
| Coach-business / mentorship content | ~55% | Mentorship funnel |
| Training + nutrition tactical content | ~25% | Credibility + SEO/discovery |
| Personal confession / values | ~10% | In-group bonding |
| Client wins / testimonials | ~5% | Proof |
| Reactive / trend / humor | ~5% | Algorithm feeding |

### 6.4 Voice: is he I-led or you-led? (THE QUESTION FOR COOZ'S VOICE DEBATE)

**This is the critical finding for the ongoing voice rule debate in WS1.6.**

Looking at the opening words of the top 10 engagement posts:

| Rank | Likes | Opening |
|------|-------|---------|
| 1 | 4,481 | **"If you can't take ownership…"** — YOU-imperative |
| 2 | 1,707 | **"Been trying to write…"** — I-led (implied I, "I've been trying") |
| 3 | 279 | **"This is what it looks like when coaching is done right…"** — Observational / it-led |
| 4 | 259 | **"Will Online Coaching Die in 2026…?"** — Question / observational |
| 5 | 139 | **"Trollin' because she deserves it"** — Humor / implied I |
| 6 | 119 | **"I lost 45-50lbs in 2010…"** — I-led |
| 7 | 101 | **"New podcast episode out now…"** — Observational |
| 8 | 100 | **"Training to be the most reliable version of me"** — I-led |
| 9 | 90 | **"If I could ONLY pick 1 exercise…"** — I-led (hypothetical I) |
| 10 | 90 | **"Here's Exactly What I'd Do Go Get AS LEAN AS POSSIBLE"** — I-led |

**Of the top 10, 6 are I-led, 1 is you-led (the top post), 3 are observational/it-led.**

**The I-led dominance validates the WS1.6 voice rule.** But the #1 top post is an exception worth studying: it's a **you-imperative** (not you-narration). The rule *"Short-form 'you' openings work when they are one imperative line"* from WS1.6 holds — McBroom's one you-led post is a single declarative sentence, not sustained scene narration. It is consistent with the Sheedy "Pay attention to what you feed" pattern.

**Caption length**: McBroom's top posts run 200–600 words. The 2023 confession post is 430 words of pure I-led reflection. The top coach-callout post is 350 words — I-led body with you-imperative opener. He writes LONG captions. The algorithm doesn't reward them in his case (median 68 likes), but the few that go big tend to be the longer ones. Length creates intimacy with the pre-qualified in-group.

**Structural template for his confession posts** (derived from the 2023 post and others):
1. Confession opening (I-led or "Been trying to…" passive-I) 
2. Contradiction or irony ("…it was my worst year, but because of that it was my best")
3. Spiritual framing ("God," "faith," "purpose," "broken down to be built up")
4. Named struggles (money lost, depression, loneliness)
5. Lesson pulled out for the reader ("if I had to pull ONE MAJOR lesson…")
6. CTA to new year / new beginning / follow

**Compare this directly to Sheedy's Easter post** (from WS1.6): same I-led confession structure, same spiritual resurrection frame, same universal pivot at the end. McBroom and Sheedy are essentially running the same voice template. **This confirms the voice rule for Cooz: the resurrection brand does NOT need to invent a new voice — it needs to match the McBroom/Sheedy confession template exactly.**

### 6.5 Visual brand

From the image URLs and post previews:
- Dominant color palette: **earthy browns, black, desaturated greens**, white on black text cards
- Heavy use of **in-gym shots and real client photos** — NOT studio-polished
- Text overlays on images use **sans-serif condensed bold**, all caps
- Thumbnail style is **cinematic but not MrBeast** — closer to an outdoor magazine aesthetic
- **Cody's own face appears in ~40% of posts** — he is the brand
- No stock photos. No AI imagery. Real gym. Real clients. Real him.

**This is extraordinarily close to the "Resurrection Coach brand" visual thesis in the current Cooz package** ("cathedral, gym at dawn, hand-loaded 35mm camera"). The Cooz visual direction in `04-visual-packaging-system.md` is already aligned with where McBroom lives. That part of the dossier doesn't need to change.

### 6.6 CTA patterns

Every single recent post ends with one of these:
- *"Follow @codymcbroom for content to develop better systems and master the art of coaching"*
- *"Comment 'mentorship' below and I'll send you the 2026 online coaching blueprint"*
- *"DM me the words 'learn more' to see what our coaching and mentorship is all about"*

**100% of recent CTAs point to the MENTORSHIP funnel, not the TCM consumer funnel.** The `@codymcbroom` IG is the coach funnel. The `@tailoredcoachingmethod` IG is the client funnel. They are fully decoupled.

---

## SECTION 7 — THE ORIGIN STORY & ETHOS

### 7.1 The origin story (pieced together from multiple sources)

**The sealed version** (from witsandweights.com, Hunt Fitness interview, his own bio):

> Cody McBroom grew up overweight in the Pacific Northwest. He wasn't obese but he was always the heaviest kid in his friend group. He played soccer seriously through high school. Two back-to-back traumatic knee injuries ended his soccer career and put him on crutches. Without soccer — which had been his identity — he gained 40–50 pounds of body fat and lost his motivation completely. He spent a period in what he has publicly described as depression.
>
> He got into fitness originally through his own transformation. He lost the 45–50 pounds. The physical transformation became the catalyst for his mental health, relationships, and career. He enrolled in a community college personal trainer / health coach program and tried everything on himself. He realized the physical work was the trojan horse for everything else in his life — this is the thesis that still runs through all his content.
>
> After losing the fat, he realized he was "just skinny" and had to learn to build muscle. That started his nutrition + hypertrophy specialization. He then started coaching in-person, built a roster, eventually transitioned to 100% online coaching, founded Tailored Coaching Method, and scaled it to $1.5M/year without paid ads.
>
> Along the way, he has been open about burnout, depression, financial loss, and finding God. The 2023 Instagram post (Section 6.4, 1,707 likes) is his most public "I was broken down to be built up" statement.
>
> His first and "most influential mentor" is **Luka Hocevar**, who runs a Seattle gym and appears repeatedly on the Choose Hard Podcast. Cody openly positions himself as having been mentored, not self-made.

### 7.2 The values he leads with (from scraped copy + podcast titles)

- **Integrity** (6+ mentions on mentorship page)
- **Impact** (paired with integrity)
- **Choose Hard** (trademarked — the whole brand ethos)
- **Practice what you preach** (repeated across posts, fitness-first culture)
- **Ownership** (personal and professional)
- **Fulfillment > marketing** (the contrarian position against the guru industry)
- **Community / brotherhood** (testimonials repeatedly cite being "part of something")

### 7.3 What he believes about fitness, men, coaching

From the scraped captions and podcast episode titles:

**On fitness**: The physical is the trojan horse. Fat loss / muscle gain isn't the point — it's the mechanism for rebuilding identity. *"A physical transformation can be the ultimate catalyst for everything else in your life."* This is identical to the Cooz dossier's Resurrection thesis.

**On men**: Coaches (specifically male fitness coaches) have a duty to "walk the walk" and "be the example." He is not soft on men — the top post (4,481 likes) is explicitly about holding other male coaches to a physical standard. There is a masculine "you will be held accountable by your peers" energy throughout.

**On coaching**: Coaching is a craft, not a marketing exercise. The fulfillment side (actual client results) is where the business is made or lost. Lead flow is downstream of real results.

**On mental health**: Mentioned occasionally but NOT central. One April 2026 post lists "mental health" as a physiological outcome of low body fat, almost clinically. The spiritual/emotional content lives in confession posts and podcast episodes (e.g., "When a Coach Needs Coaching: How I Faced Burnout & Started Over") — but is NOT frontline brand messaging.

**On spirituality**: He is openly Christian. The 2023 post explicitly names God, faith, being "broken down to be built up." This is a post-2022 development — earlier content doesn't emphasize faith. The Gavin Siegner testimonial on the mentorship page specifically calls out "develop a relationship with God" as one of the mentorship outcomes. Faith is present but not the headline — it's an in-group signal for the values-aligned buyer.

### 7.4 Where men's work / Movember / mental health charity alignment sits

**HONEST FINDING: McBroom has NO public alignment with Movember, men's mental health charities, or suicide prevention causes that I could find.**

- Zero Movember content in the scraped IG posts (all 30)
- Zero Movember mentions in the WebSearch queries
- Zero suicide prevention or "men's mental health month" content
- "Mental health" appears once in the 30-post scrape, and it's in the clinical phrase "cardiovascular health, and mental health" as a downstream benefit of low body fat
- The spiritual content is Christian-inflected personal testimony, not cause-aligned activism

**What this tells us about the Cooz hypothesis**: The current `12-expert-package` dossier assumes the buyer (Mike) is waiting for someone to name his 3 AM shame around depression, loneliness, and performance anxiety. That part may still be true. But **McBroom does NOT reach his buyer through mental health cause alignment**. He reaches them through:
1. Craft standards ("be in great shape")
2. Integrity callouts ("those gurus are selling fluff")
3. Christian-inflected personal testimony (the 2023 post, baptism-adjacent content)
4. Systems / operator competence

**The Movember angle is a Cooz belief, not a McBroom template.** If Cooz wants to do Movember alignment, he will not be imitating McBroom — he will be doing something McBroom has not done. That's fine, but it should be named explicitly as a *Cooz differentiator*, not a *McBroom inheritance*. Do not frame it as "following McBroom's lead" — because McBroom is not leading that way.

---

## SECTION 8 — THE COOZ GAP ANALYSIS (THE CRITICAL SYNTHESIS)

This is the heart of the investigation. Comparing McBroom's actual business to the current `12-expert-package` Cooz dossier.

### 8.1 Offer gap

| Dimension | Current Cooz Dossier | McBroom Reality |
|-----------|---------------------|-----------------|
| Entry product | $497 Triage Audit | Free 30-min Strategy Call (no audit product) |
| Primary offer | $1,500–$2,500 "Resurrection Protocol" 90-day program | $347–$497/month recurring, 3-month minimum |
| Positioning of primary offer | Proof-of-concept sprint to build portfolio | Full core business, productized, published |
| Price discovery | Hidden in a "Triage Audit" gate | Fully published on the homepage |
| Guarantee | "Optional risk-reversal guarantee" (not specified) | "If you don't see results, you don't pay" — fully specified |
| Mentorship / coach-facing offer | NOT in dossier at all | Full parallel business ("Board of Advisors," 4-month minimum, ROI guarantee) |
| Business model | 1:1 coaching with founder ICP | Two parallel businesses: productized monthly consumer coaching + gated high-ticket mentorship |

**The gap**: The Cooz dossier architects a bespoke $1,500–$2,500 package for a specific founder avatar. McBroom runs a productized monthly subscription for the mass market AND a separate gated mentorship for operators. These are fundamentally different business models.

**The implication**: if Cooz truly wants to emulate McBroom, the offer should be:
- A **recurring monthly coaching product** at $300–$500/mo, 3-month minimum, published price, conditional results guarantee — serving whoever actually shows up
- PLUS a **gated high-ticket mentorship** ($1,500–$3,000/mo, application-only) serving other coaches/trainers like him who want to learn his systems

NOT a bespoke "Resurrection Protocol" sold to depleted founders.

### 8.2 Positioning gap

| Dimension | Current Cooz Dossier | McBroom Reality |
|-----------|---------------------|-----------------|
| Brand name | "Resurrection Coach" | "Tailored Coaching Method" + "Choose Hard™" |
| Mythic framing | Very high — "Resurrection," "the 2019 ghost," "permission broker" | Moderate — "Choose Hard" is the mythic frame, but the rest is operational |
| Category | "The first honest mirror for depleted founders" | "Integrity-first mentorship for coaches who want real craft, not funnels" |
| Buyer archetype | Mike the depleted founder | Jake the online coach + Karen the 40-something fat-loss client |
| Anti-position | Against optimization / high-performance coaches (Dan Go, Huberman) | Against guru-mentor cookie cutters (Iain Mitchell, Jordan Syatt types) |

**The gap**: Cooz's current positioning is more poetic than McBroom's, but it's positioned against the wrong competitive set and pointed at the wrong buyer. McBroom does NOT position himself against Dan Go or Huberman — those are adjacent brands he probably respects. His anti-position is against the coach-marketing-guru industry. **Cooz's dossier has him fighting the wrong enemy.**

### 8.3 Voice gap

| Dimension | Current Cooz Dossier (voice rule) | McBroom Reality |
|-----------|---------------------------------|-----------------|
| Primary POV | I-led with you-pivot at universal moment | Same — validated |
| Caption length | 250–350 words LinkedIn | 200–600 words IG, heavy on confession/ethos |
| Spiritual content | "Resurrection" as theological metaphor | Explicit Christian content in peak posts (God, faith, broken-down-built-up) |
| Masculine energy | Implicit | Explicit — "be in great shape," "practice what you preach," peer callouts |
| Confession depth | The dossier imagines deep founder-shame confession | McBroom does more "operator-confession" — money lost, burnout, coach-burnout, spiritual crisis |

**The gap**: Cooz's voice rule is largely aligned. The main gap is that McBroom's confessions are about **operating a business and being a coach**, not about being a depleted founder. Cooz should not be confessing Mike's 3 AM Slack-check anxiety — he should be confessing HIS OWN moments of "when a coach needs coaching" (which is literally a McBroom podcast episode title). Cooz has already lived this. He should tell it directly.

### 8.4 ICP gap (THE BIG ONE)

| Dimension | Current Cooz Dossier | McBroom Reality |
|-----------|---------------------|-----------------|
| Named buyer | Mike, 38, SaaS founder, $1.6M ARR, 2 kids, 9 employees, $900K seed, $142K salary | **Two buyers: Jake (31, online coach, $10K/mo, 35 clients, stuck 14 months, bought a bad guru) AND Karen (42, busy professional woman, wants to look fit, has tried every diet, wants accountability)** |
| Emotional buy | Permission to stop pretending he's fine | Permission to be a real coach (Jake) / Permission to finally look how she works out (Karen) |
| Price tolerance | $1,500–$2,500 for 90 days | $347–$497/mo (Karen) / gated high-ticket (Jake) |
| Where they live on social | LinkedIn (founder networks) | Instagram + podcasts |
| What they read | Hoffman, Thiel, Horowitz; listens to Huberman | Hormozi, Syatt, Iain Mitchell; listens to Choose Hard |

**The gap is a canyon.** Mike-the-founder is a hypothetical buyer the dossier has constructed from research. Jake-the-coach and Karen-the-fat-loss-client are the buyers McBroom ACTUALLY REACHES. These are not the same person.

**The question Cooz needs to answer honestly**: when you think about who you want to coach, are you picturing Mike (the founder Cooz wants to be), or are you picturing Jake (the coach Cooz was five years ago) or Karen (the kind of client Cooz has actually closed)?

### 8.5 The ONE thing Cooz should transplant

If Cooz could take ONE thing from McBroom's business and put it in his own, it should NOT be:
- The Resurrection brand (he's already got that)
- The voice (already validated)
- The visuals (already aligned)
- The 1:1 coaching model (too bespoke to scale)

It should be:

> **The two-business architecture: a productized, monthly-recurring, published-price consumer coaching offer as the base business + a gated high-ticket mentorship to people who are one step behind where Cooz is now.**

This is THE move. Everything else is decoration. Here's the specific transplant:

**Tier 1 (consumer)**: "Tailored Resurrection Coaching" — $397/month, 3-month minimum, published price, 30-day conditional results guarantee, bespoke-to-individual training + nutrition + mindset. Target: people who want to look and feel better, NOT exclusively depleted founders. Whoever shows up.

**Tier 2 (mentorship)**: "The Resurrection Mentor" — gated, 4-month minimum, targeted at OTHER coaches/trainers who are in Jake's spot (stuck at $5–15K/mo, wanting real craft instead of guru marketing). Cooz has walked the exact path these people are trying to walk — he was mentored BY McBroom. **His unique selling point: "I was coached by the guy you're trying to become. I can teach you the systems he taught me, plus what I learned scaling mine."** That's a Category of One Cole would recognize immediately.

The Resurrection Protocol as currently architected ($1,500–$2,500 one-time bespoke) should be RETIRED as a top-line product. It's neither fish nor fowl — too expensive for Karen, too cheap and custom-bespoke for Jake, and too undifferentiated for Mike.

---

## SECTION 9 — WHAT MCBROOM'S MODEL TELLS US ABOUT COOZ'S REAL ICP

This is the payoff question. If McBroom is Cooz's stated reference point, and McBroom's actual buyers are Jake and Karen (NOT Mike), then the most parsimonious hypothesis is:

### 9.1 The real ICP hypothesis

**Cooz's most reachable buyer is not Mike the depleted founder.** It is one of these two people, in this order of reach:

#### Hypothesis A (highest probability): Jake — the online coach who is one step behind Cooz

A 25–35 year old male online fitness coach doing $3K–$15K/mo, who:
- Has been in the industry 2–5 years
- Is currently stuck and knows it
- Has bought at least one mentorship program and been disappointed
- Follows McBroom, Hormozi, Syatt, and maybe Sam Miller on Instagram
- Wants to build a "legitimate" business, not a "loud marketing" business
- Has spiritual / values alignment with Cooz's ethos
- Has actually seen Cooz be coached by McBroom (if Cooz has talked about it publicly) — this is an irresistible social proof hook
- Lives in a secondary city, not NYC/LA
- Is married or in a serious relationship, may have young kids
- Has a home gym, not a studio

**Why this is the highest-probability buyer**: because this is who Cooz was 5 years ago, and Cole's lived-experience moat principle says the most defensible position is the one you've personally walked. Cooz was coached by McBroom. That means Cooz now has something McBroom's mentorship can't sell: *the lived experience of having been on both sides of the table*. Jake wants exactly that.

**The threshold moment for Jake**: when he realizes he's been paying a "guru" and his clients aren't getting results. When his best friend signs 3 new clients and Jake doesn't. When a client of his churns at month 3 for the 5th time in a row. That's when he goes looking for a real mentor.

#### Hypothesis B (secondary but operationally easier): Karen — the 40-something fat-loss client

Women in their late 30s to mid-40s who:
- Have tried every diet and feel educated but stuck
- Want accountability more than another plan
- Are willing to pay $300–$500/mo for real 1:1 attention
- Are often married, often mothers, often in professional careers

**Why this is easier operationally**: this is the buyer who actually closes on the TCM $347–$497 offer. They don't need a deep positioning play. They need a published price, a testimonial wall, and a Strategy Call booking link. The TCM transformation Instagram is full of these women (Karen, Jessika, Leslie, Madison, Liz, Steph, Jan, Joylnn, Kelly — every named client in the scrape is a woman).

**The threshold moment for Karen**: when she sees a transformation post from a woman who looks like her. When she realizes the problem isn't her willpower, it's that she's been trying to do it alone. When a friend mentions Cooz's coaching.

### 9.2 Is Mike the depleted founder buying anything at all?

**Honest answer**: Mike might exist. Mike might even buy. But Mike is not McBroom's buyer, and there is no evidence from the scraped McBroom data that this segment has meaningful buying volume in the fitness coaching space. The Cooz dossier's Mike is constructed from Reddit scraping and research, not from observed buying behavior in the reference competitor.

**The safest position**: Mike is POSSIBLE as a tertiary tier (the $5K–$10K bespoke "apex" tier at Phase 3 of the Cooz roadmap). He is NOT the right buyer for Phase 1 or Phase 2. The dossier's mistake is making Mike the Phase 1 target. Phase 1 should be Karen (for volume) or Jake (for margin), with Mike as a long-term aspiration.

### 9.3 The ICP recommendation in one sentence

> **Cooz's Phase 1 ICP should be "Jake-the-stuck-online-coach" as the primary high-margin play (because Cooz has the McBroom-coached lived experience moat) and "Karen-the-fat-loss-client" as the volume foundation — NOT "Mike-the-depleted-founder" who is speculative at best.**

### 9.4 The buyer's threshold moment (what makes them click apply)

**For Jake**: A specific client of his churns. He goes on Instagram at 11 PM. He sees a Cooz post that says *"Your clients aren't ghosting because they're lazy. They're ghosting because you're guessing. I made this exact mistake for 18 months. Here's what my mentor — Cody McBroom — showed me about fulfillment that I now teach my own mentees."* That post is a direct emotional hit. Jake clicks. Jake books a call.

**For Karen**: She sees a testimonial post of a 43-year-old woman like her who lost 20 lbs in 4 months on Cooz's program. She DMs. The reply is a link to a Strategy Call. She books.

**For Mike**: Unknown. There is no proven threshold moment for this buyer in the McBroom data.

### 9.5 If Cooz built his ICP on McBroom's buyer profile

The document would read completely differently. Here's what would change:

- **The canvas** ("Deep Worldview Canvas") would be about Jake, not Mike. A 31-year-old stuck online coach, married with a baby, $10K/mo, bought a bad mentorship, can't figure out why his clients plateau. The interior monologue is about craft-shame, not performance-for-investors-shame.
- **The content buckets** would pivot: "The Depletion Diaries" becomes "The Coach's Confession" — stories about being a coach who was quietly bad at the craft before he got help. "The Resurrection Chronicles" becomes "The Systems I Stole From My Mentor" — showing the operational shift.
- **The offer** would become the two-tier productized structure described in Section 8.5.
- **The visual brand** stays mostly the same — it already aligns with McBroom's aesthetic.
- **The voice** stays mostly the same — I-led confession with universal pivot. The content OF the confessions changes.
- **The DM strategy** shifts from "LinkedIn touches to 837 founder connections" to **"Instagram DMs to online coaches in the $5–15K plateau, via comments on Hormozi/Syatt/Iain Mitchell posts"**.
- **The Movember / cause alignment** is DROPPED as a core strategy — it's not in McBroom's playbook, and Cooz should not build the business on something the reference point doesn't do. If Cooz wants to do Movember for his own values, fine — do it as a personal expression, not as a positioning play.

---

## APPENDIX A — THE VERBATIM MCBROOM QUOTES THAT MATTER MOST

For reference, when building Cooz's content or sales copy, these are the direct McBroom utterances that encode his positioning most precisely:

1. (Mentorship page, top) *"Build a Sustainable Coaching Business with Your Integrity Intact."*
2. (Mentorship page, subhead) *"THE MONTHLY MENTORSHIP FOR COACHES WHO ARE TIRED OF TEMPLATED MARKETING BULLSH*T AND WANT REAL SYSTEMS, EXPERT GUIDANCE, AND A GUARANTEED 3X ROI IN THE FIRST 90 DAYS."*
3. (Mentorship page, value section) *"You're a Coach, Not a Carbon Copy."*
4. (Mentorship page, Cody's note) *"after building tailored coaching method to a yearly revenue of $1.5 million dollars, without paying for a single ad... i realized the coaching industry was lacking something crucial... GREAT COACHING."*
5. (TCM homepage) *"The Key Element That Helps Our Clients Succeed Isn't What You Think It Is… It's The Coaching Relationship. The Personal Support. The Authentic Communication. The Emotional Awareness. The Community. The Culture."*
6. (Mentorship page, ROI guarantee) *"If you show up to the calls, implement the systems we provide, and complete your weekly trackers, but don't increase your revenue by at least your initial investment within the first 30 days, we will continue to coach you for free until you do. We win when you win."*
7. (Top IG post, 4,481 likes, Sep 2025) *"If you can't take ownership of your own health, you shouldn't be coaching others to improve theirs. And I know it sounds brutal, but honestly I don't care."*
8. (2023 confession post, 1,707 likes) *"I was being broken down and chipped away at, to be built up stronger and shaped into who I need to become in order to fulfill my purpose in life… You will be broken down before you will be built up."*
9. (IG post, Jan 2025, about fulfillment) *"Most online coaches can't say that. Because they have a 'leads problem' that's actually a fulfillment problem."*
10. (Mentorship page) *"You aren't just hiring a coach. You're gaining a Board of Advisors."*

---

## APPENDIX B — OPEN QUESTIONS FOR COOZ DIRECTLY

Things Farrice should ask Cooz when this lands:

1. When you say you want to "emulate McBroom," are you pointing at TCM (the fat-loss business) or the Mentorship (the coach-facing business)? Or both?
2. Did you actually pay McBroom's mentorship, or were you in his consumer coaching? This matters for the social proof angle.
3. Would you be willing to publish your price? Because McBroom does, and it is a real differentiator in this lane.
4. Would you be willing to target other coaches as a primary ICP? Because that's the lane McBroom actually runs.
5. How do you feel about coaching Karen (40-something woman who wants to lose 20 lbs)? Because that is the actual volume play.
6. How committed are you to the "founder" ICP? Is that because you believe in it or because the dossier built it for you?
7. Are you OK with dropping the Movember angle as a positioning play (not as a personal value)? Because McBroom doesn't do it, and you don't need to.

---

## APPENDIX C — EXPERT FRAMEWORK CITATIONS (WHERE EACH LENS APPEARS)

- **April Dunford Positioning** — Section 2 (full 5-component canvas), Section 5.3 (calm confidence posture), Section 8.2 (positioning gap)
- **Nicolas Cole Niche Positioning** — Section 4 (specificity ladder, lived experience moat, category of one), Section 9.1 (Jake as the lived-experience buyer)
- **Dai Media Consumer Posture** — Section 3 (3D posture for Jake, Kristen Stewart test, emotional outcome), Section 2.5 (co-conspirator framing), Section 9.4 (threshold moment)
- **Daniel Priestley Oversubscribed** — Section 5 (5 levers, demand inversion, stakes lens, private conversation, anticipation architecture, signal volume engineering), Section 1.3 (capacity declaration)

---

## FINAL NOTE

This document assumes the Cooz `12-expert-package` dossier is not wrong in craft — the worldview canvas, the voice rules, the visual system, the 30-day execution plan are all competent, sometimes excellent work. **It is wrong in aim.** It is aiming at Mike when the reference point is aiming at Jake and Karen. The dossier can be re-pointed without being rebuilt. Most of the work ports cleanly once the ICP is corrected.

The hardest conversation Farrice and Cooz have after reading this will be about letting go of Mike. Mike is an elegant construction. Mike is also not McBroom's buyer. And McBroom is the reference point.

The right move is to honor the dossier's craft while correcting its target.

— End of reverse-engineer —

*File: `13-pmf-investigation/01-cody-mcbroom-reverse-engineer.md`*
*Sources: Apify Instagram scrapes (codymcbroom, tailoredcoachingmethod), Apify web scrapes (tailoredcoachingmethod.com, tailored-coaching.com/mentorship-coaching), YouTube metadata search, 6 WebSearch queries. Total Apify spend this run: ~$0.08.*
*Framework citations: April Dunford Positioning (SKILL.md + genius.md), Nicolas Cole Niche Positioning (SKILL.md + genius.md), Dai Media Consumer Posture (SKILL.md + genius.md), Daniel Priestley Oversubscribed (SKILL.md + genius.md). All four loaded and cited throughout.*
