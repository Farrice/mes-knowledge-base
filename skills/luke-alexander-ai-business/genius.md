# Luke Alexander — Genius Context

## Genius Patterns

### Pattern: Service Layer Arbitrage
The AI stack has three layers: LLMs (hundreds of billions to build — "you're probably a decade late"), software (capital-heavy, technically complex, hard distribution — Luke does this with Kendo but explicitly does NOT recommend it), and services on top. Like the early internet, the people who made "insane money" first were the ones selling applications of the new infrastructure (emails, funnels, ads), not building the infrastructure. The service layer is where a solo operator with no capital wins.
**Execute**: Refuse to build LLMs or SaaS first. Start a service business that uses AI to do the delivery. Graduate to software only after the service reveals a repeatable problem worth productizing (Luke's own path: agency → info → Kendo).
**Success Metric**: Business started with near-zero capital; first revenue inside 30-60 days instead of a 12-month build.

### Pattern: Problem-First Battle Selection
"You're only selling things based on problems you solve." Never start from "I'll do an agency for dentists." Start from one of three evergreen business needs — sales, marketing, automation — then pick the niche where money is flowing fastest right now (info products: "guys are literally buying cars and posting them online and making a million dollars"). High-income local (roofing, HVAC) works, but info owners understand the value faster.
**Execute**: Pick ONE problem class (sales / marketing / automation-as-systematization — never "AI automation agency," which Luke calls a commodity). Then pick ONE niche with dense money flow. Define the specific expensive sub-problems: closers, CRO (show rate, close rate, funnel), assets (VSLs, landing pages, emails, YouTube, copy), manual workflows.
**Success Metric**: You can name the exact metric you fix and what that metric is worth in dollars to the client before you ever pitch.

### Pattern: Upside Economics (Less Clients, More Upside)
The 2018 agency model — $3-5K retainers stacked across many clients — mathematically cannot reach $83,333/month without operational collapse. Luke's model: 1-3 clients max, priced as setup fee + percentage of upside over the current baseline. His proof: $25K setup fee + upside percentage on a trading-space info client = ~$300-400K over 4 months, $200K paid in a single week, $4.5M collected for the client.
**Execute**: Charge a setup fee for the manual build work ($5K-$25K by business size). Then take 15-20% of everything ABOVE their current monthly baseline: "You're doing $100K/month. I'm not taking money you've already earned — I want 20% of everything additional I make you."
**Success Metric**: A single $100K/month client yields ~$24K/month recurring; three such clients = the $83K/month that equals $1M/year.

### Pattern: Conversion Lever Math (Double the Business with No New Traffic)
Businesses are multiplication chains: audience × opt-in rate × lead-to-booking × show rate × close rate × price. Small lifts on 3 levers compound into a doubled business without any new traffic. Luke's worked example: show rate 30%→50%, close rate 20%→40%, VSL-lead-to-booking 3%→5% takes overall CVR from 2% to 5% — a $400K/month business becomes $1M/month. "We fixed show rate. We fixed close rate. No new traffic. We're not running ads."
**Execute**: Audit the chain and get real numbers for each stage. Identify the 2-3 weakest levers. Fix them with concrete assets: better VSL, offer repositioning, pre-call/post-call assets, booking notifications, better emails — nearly all producible with AI. Model the compounded revenue before pitching.
**Success Metric**: Projected revenue lift computed from the client's own numbers; post-engagement metrics moving to standard KPI bands (show rate ~50%, close rate ~40%).

### Pattern: Sell the Outcome, Bury the Engine
"AI" in front-facing copy now gets WORSE results — it's become buzzword slop. Business owners don't care that it's done with AI; they care about better results, faster delivery, lower cost. "AI is the engine that powers your vehicle. Your vehicle is sold as a vehicle." The Ferrari buyer doesn't want a lecture on cylinders and alloys.
**Execute**: Strip GPT/AI/automation jargon from every pitch. Use normal business language: "response system," "sales process management," "I will fix your show-up rate, fix your close rate, and manage your sales team for X% per month." Start from their pain (time wasted, low meetings, inconsistent output), position the fix, anchor to ROI.
**Success Metric**: Prospect never asks "what AI tools do you use?" — they ask "how fast can you start?"

### Pattern: Information Asymmetry Is the Margin
"If they knew what you know, they wouldn't pay you. They would just do it with AI because it's so easy." The entire margin of the AI operator model is that you know context profiles, prompting architecture, and which levers to pull — and the client doesn't. Keep your cards to your chest; sell outcomes, deliver with AI at 2% of the manual time cost (Luke: world-class VSLs in 30-60 minutes vs. weeks by hand).
**Execute**: Never educate prospects on your AI stack during sales. Deliver work product only. Invest continuously in the asymmetry itself — prompting skill, context engineering, new tools — because the moat decays as the market learns.
**Success Metric**: Delivery time at a fraction of manual (VSL in an hour, not weeks) while the client attributes the result to your expertise, not a tool they could buy.

### Pattern: Strengths-to-Offer Mapping
People fail by copying whatever business they saw someone else doing. Luke's four-question inventory: What are you curious about? What track record do you have? What experience have you learned the hard way? What are you actually good at? Map the answers onto the four core business needs — creative (ads, sites, funnels, video), automation (workflows, systematization), marketing (funnels, VSLs, copy, ads, webinars), sales (staffing, management, process, CRM) — and offer only where they intersect.
**Execute**: Answer the four questions honestly in writing. Then define the offer with four more: Who am I helping and why? What am I doing for them? How expensive is this problem? How will I fulfill and get results (answer: with AI, invisibly)? Technical people go technical; sellers and speakers go sales/marketing.
**Success Metric**: Offer sits at the intersection of proven strength and expensive problem — you can fulfill from day one without faking competence.

### Pattern: The 4x Retention Rule
The point of pricing is that the client keeps paying every month. Rule of thumb: they must get ~4x back on their investment. "If I'm giving you a dollar and getting $4 back, I will always give you that dollar. If I get $1.50 back, I start to question things" — because the owner pays taxes and expenses on top.
**Execute**: Before proposing any fee, compute the client's return: fee × 4 ≤ projected upside you control. Pick the pricing vehicle by the work's shape: one-time setup ($2-10K+) for builds, retainer only for genuinely ongoing upkeep, revenue share for performance levers, hybrid (setup + rev share) for the big engagements.
**Success Metric**: Client retention measured in months-to-years; renewal conversations are about expansion, not justification.

### Pattern: Context Profile System (Quality of Context > Quantity)
"90% of people fail" with AI because they information-dump raw text and assume the model remembers. Luke's delivery infrastructure is a structured context profile with five layers: identity & role, project DNA, working files & assets, immediate context, output specifications. Three memory tiers govern the setup: working memory (the context window), session memory (platform persistence), infinite memory (RAG/vector DB — Pinecone/Supabase-class for elite use). "99% of the time it's about the quality of your context rather than the quantity."
**Execute**: For every recurring deliverable, build a project with uploaded key documents and detailed instructions written ONCE and reused. Structure context as organized profiles (JSON-formatted works measurably better). Avoid the four mistakes: information dumping, assuming retention, ignoring token efficiency, starting from scratch each session.
**Success Metric**: New chat sessions produce expert-grade output immediately with zero re-explaining; 100x output quality vs. "write me a VSL" prompting.

### Pattern: Context Handoff Protocol
Context windows fill up ("think of it as a water bottle") and a fresh chat is a stranger. Luke's fix: before the window dies, have the model compress the conversation into a portable profile that the next session ingests.
**Execute**: At context limit, prompt: "Create a comprehensive, detailed summary of our conversation including [the main context areas] so I can talk to a new chat with the same expertise as you. Format it as a JSON context profile." Feed that profile to the new session as message one.
**Success Metric**: Zero fidelity loss across session resets; multi-week client projects run in AI without ever "starting over."

## Hidden Knowledge

### Insight: The Boring Layer Is Where the Money Was Always Made
**Insight**: Luke attributes outperforming everyone — in the Zapier/funnel era and now in AI — to the boring technical plumbing nobody sits through: "I look at my channel and the most viewed videos are the least important. The most important are the least viewed... we paid attention to these little things everyone breezes over."
**Deploy**: When choosing what to learn next, deliberately weight the unglamorous infrastructure skill (context engineering, funnel plumbing, data hygiene) over the trending surface tactic. That's the durable edge precisely because competitors won't sit through it.

### Insight: Info Product Owners Are Whales Who Don't Know What They're Doing
**Insight**: "Every kid that launches an info product and buys a car is doing $100K a month and they all have no idea what they're doing." They don't know how to write a VSL, understand consumer psychology, or construct an offer — and their problems are worth hundreds of thousands to millions per year.
**Deploy**: Target info/creator businesses at ~$100K/month as the beachhead: highest problem-density, highest AI-deliverability (assets and copy), fastest to understand a performance deal. One landed whale ≈ $24K/month.

### Insight: Staffing Is the One Human Bottleneck
**Insight**: In Luke's entire service map, everything can be done with AI except one item: sales staffing. "Finding closers has to be done manual. That's kind of hard or just tedious." AI isn't replacing salespeople yet — but it can already do DM setting and chat optimization.
**Deploy**: Price the human-labor components into the setup fee (that's what the $25K setup covered — recruiting and training closers). Keep the recurring percentage attached to the levers AI maintains cheaply.

### Insight: The Ladder Has Three Rungs — Enter at Your Level
**Insight**: Three ways to make money with AI: freelancer (Upwork, minor n8n jobs — for true beginners, beats appointment setting), operator (the growth-partner model — for anyone who's made their first $10K), and SaaS (only with capital, a team, and technical depth; "it's burnt a lot of cash of mine"). The operator rung is the deliberate recommendation for almost everyone.
**Deploy**: Diagnose the user's stage before prescribing: no track record → freelance small AI jobs to build proof; some money made → operator model with performance deals; capital + team + validated problem → only then software.

### Insight: The Service Business Is the R&D Lab for the Software Business
**Insight**: Luke is doing the identical playbook at both layers: "I'm picking a niche, picking the experience I have — sales — I know the problems that niche had, and I built a software to do the service for me." The service engagements revealed the repeatable problem Kendo now productizes; a member sold $20K upfront of "context profile systems" to government contracting agencies the same way.
**Deploy**: Treat every service client as problem-discovery. When the same fix has been sold 3+ times as a service, that's the software (or productized-service) candidate — with revenue, case studies, and domain knowledge already banked.
