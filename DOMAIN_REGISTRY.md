# Domain Registry

> Authoritative routing guide for expert orchestration. Defines swim lanes, routing logic, and handoff protocols.
> **94 agents across 14 domains.** Some agents appear in multiple domains.

---

## How This Works

When you make a request, I route to the right expert using this registry. I will **explicitly announce** which expert I'm using and why, so you can redirect if needed.

**Format**: "**[Routing to @expert-name]** — Reason for selection. Override if you'd prefer a different approach."

---

## Domain 1: Copywriting (Conversion & Sales)

> **Exclusivity Boundary**: This domain owns Bottom-of-Funnel (BoFu) and Middle-of-Funnel (MoFu) text. If the primary goal is CONVERSION (sales, signups, opt-ins), route here. If the goal is AUDIENCE BUILDING or VIRAL ENGAGEMENT, route to Domain 2.

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Harry Dry** | EVALUATION | Auditing copy, Three Rules Test, rewrite discipline |
| **Cardinal Mason** | CONVERSION | Sales pages, emails, client delivery, business building |
| **Alen Sultanic** | LONG-FORM | Sales letters, VSLs, sophisticated persuasion |
| **Nicolas Cole** | SENTENCE-CRAFT | Rhythm, readability, sentence-level polish |
| **Mitch Albom** | EMOTIONAL/LITERARY | Premium narrative, emotion-first, storytelling copy |
| **Bond Halbert** | DIRECT RESPONSE | Market language excavation, velocity optimization, four-reader types |
| **David Deutsch** | LEGENDARY COPY | Boring-to-brilliant, musical architecture, loss framing, screenwriter thinking |
| **Luke Iha** | PROOF ENGINEERING | Doubt node mapping, 22-type proof arsenal, trust-building |
| **Ward Farnsworth** | RHETORIC | Classical rhetoric, chiasmus, anaphora, Saxon punch, immortal prose |
| **Joanna Wiebe** | CONVERSION OPTIMIZATION | Copy testing, voice-of-customer, microcopy |

### Routing Logic

```
"Write copy for [X]"
├── Email sequence → Cardinal Mason
├── Sales page (standard) → Cardinal Mason
├── Sales page (premium/long) → Alen Sultanic
├── VSL script → Alen Sultanic
├── Headline polish → Nicolas Cole
├── Story-driven/emotional → Mitch Albom
├── Direct response / old-school → Bond Halbert
├── Legendary/premium long-form → David Deutsch
├── Closing lines/manifestos → Ward Farnsworth
└── Proof-heavy sales page → Luke Iha

"Evaluate/audit my copy"
├── General audit → Harry Dry (Three Rules Test)
├── Proof gaps → Luke Iha (doubt node mapping)
└── Sentence quality → Nicolas Cole

"Rewrite this sentence"
├── Rhythm/readability → Nicolas Cole
└── Power/rhetoric → Ward Farnsworth
```

---

## Domain 2: Content Strategy & Viral (Top-of-Funnel)

> **Exclusivity Boundary**: This domain owns Top-of-Funnel (ToFu) media. If the primary goal is ATTENTION, VIRALITY, or AUDIENCE BUILDING (social posts, videos, threads), route here. If the goal is DIRECT SALES or EMAIL SEQUENCES, route to Domain 1.

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Kallaway** | PSYCHOLOGY | Dopamine ladder, retention, buyer intent, content systems |
| **Seena Rez** | TIKTOK EXECUTION | PSAEP scripts, hyperdopamine hooks, TikTok commerce |
| **Shaan Puri** | STORYTELLING | Frame-first, emotion transfer, narrative structure |
| **Jun Yuh** | PERSONAL BRAND CONTENT | Content calendars, formats, silent film method |
| **Brock Johnson** | SHAREWORTHY | Social-first content, shareability engineering |
| **Authority Hacker** | AI SOCIAL | AI production velocity for social — packaging thinking, not replacing it |

### Routing Logic

```
"Create viral content"
├── TikTok → Seena Rez
├── YouTube → Kallaway
├── Story-driven → Shaan Puri
├── Personal brand → Jun Yuh
├── Shareable social → Brock Johnson
└── AI-accelerated social → Authority Hacker

"Write a hook"
├── TikTok hook → Seena Rez (hyperdopamine)
├── YouTube hook → Kallaway (curiosity loop)
├── Story hook → Shaan Puri (frame + intention)
└── Copy hook → Harry Dry (evaluation) or Cardinal Mason (conversion)

"Content strategy"
├── Buyer-focused → Kallaway
├── Personal brand build → Jun Yuh
├── Storytelling angle → Shaan Puri
├── TikTok commerce → Seena Rez
└── AI social media → Authority Hacker
```

---

## Domain 3: Personal Brand

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Caleb Ralston** | DIFFERENTIATION | Standing out, credibility bank, contrarian positioning |
| **Tom Noske** | AUTHORITY | Packaging expertise, LinkedIn dominance |
| **Omar Eddaoudi** | PREMIUM POSITIONING | Luxury brands, exclusionary tension, high-status copy |
| **Jun Yuh** | CONTENT | Content calendars, formats, daily execution |
| **Erica Mallet** | MAGNETISM | Attraction, scroll-stopping, belief architecture |
| **Lara Acosta** | B2B LINKEDIN | Engineered virality, high-retention formats, SLAY |
| **Josh Sanders** | LINKEDIN FUNNELS | B2B lead generation, content funnels, LinkedIn systems |
| **Dan Koe** | MULTIPASSIONATE | One-person business, "you ARE the niche", multi-interest monetization |
| **Tommy Clark** | B2B FOUNDER | "How I" narrative pivot, founder-led LinkedIn, stealth hooks |
| **Jasmin Alic** | LINKEDIN HOOKS | Trapdoor hooks, distributed commenting, mobile-first formatting |

### Routing Logic

```
"Build my personal brand"
├── Positioning/differentiation → Caleb Ralston
├── Premium/Luxury Positioning → Omar Eddaoudi
├── Content calendar → Jun Yuh
├── Authority building → Tom Noske
├── Visual magnetism → Erica Mallet
├── LinkedIn dominance/growth → Lara Acosta
├── LinkedIn lead funnels → Josh Sanders
├── Multiple interests → Dan Koe
├── B2B founder content → Tommy Clark
└── LinkedIn hook writing → Jasmin Alic

"Stand out in my niche"
└── Caleb Ralston

"Create brand content"
└── Jun Yuh → Kallaway (if strategy needed)
```

---

## Domain 4: Sales & Persuasion

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Jeremy Miner** | SALES PSYCHOLOGY | NEPQ, objection handling, identity selling |
| **Michael Bernoff** | IDENTITY ENGINEERING | Mindset shifts, breakthrough, belief change |
| **Lindsay** | AI CONSULTING SALES | Cold outreach, client acquisition, AI services |
| **AI Chris Lee** | ZERO-PROOF SALES | Selling without testimonials, proof building |
| **Nate Herk** | B2B LEAD GEN | Validation-first outreach, Trojan Horse partnerships |
| **Jason Fladlien** | HIGH-STATUS CLOSING | Subtraction heuristic, friction removal, radical candor |
| **David McRaney** | BELIEF CHANGE | Deep canvassing, motivational interviewing, tribal bridge building |
| **Tobias Allen** | REAL-REASON PERSUASION | Excavating the real motivation, not the stated one |

### Routing Logic

```
"Help with sales"
├── Sales calls/objections → Jeremy Miner
├── Identity/mindset blocks → Michael Bernoff
├── AI consulting outreach → Lindsay
├── No testimonials yet → AI Chris Lee
├── B2B lead generation/partnerships → Nate Herk
├── High-ticket closing / friction → Jason Fladlien
├── Belief change / tribal resistance → David McRaney
└── Deep motivation mapping → Tobias Allen

"Handle objection"
├── Standard objection → Jeremy Miner
├── Identity-level resistance → Michael Bernoff
└── Belief-level resistance → David McRaney

"Build proof/testimonials"
└── AI Chris Lee
```

---

## Domain 5: Consumer Research

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Dai Media** | CONSUMER POSTURE | Individual-first modeling, identity personas |
| **Kallaway** | BUYER PSYCHOLOGY | Buyer profiles, intent validation, workflow mapping |
| **Samuel Thompson** | MARKET VALIDATION | Shadow markets, unit economics |
| **Rory Sutherland** | BEHAVIORAL ECONOMICS | Perceived value, psychological reframing, unconventional angles |

### Routing Logic

```
"Understand my customer"
├── Deep persona → Dai Media
├── Buyer journey → Kallaway
├── Market opportunity → Samuel Thompson
└── Behavioral angle → Rory Sutherland

"Validate my niche"
└── Samuel Thompson → Kallaway (for content fit)

"Why do people buy [X]?"
├── Identity reasons → Dai Media
├── Psychological reasons → Rory Sutherland
└── Economic reasons → Samuel Thompson
```

---

## Domain 6: AI & Automation

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Nick Saraev** | AGENTIC WORKFLOWS | Sub-agent architecture, self-healing loops, MCP |
| **Boris** | AI PRODUCTIVITY | Claude Code architecture, multi-instance orchestration, mobile workflows |
| **Rachel Woods** | AI OPS | CRAFT cycle, process decomposition, team AI adoption |
| **Sherwin Wu** | AI ENGINEERING | Agent fleet management, deployment diagnostics, debugging |
| **Futurepedia** | PROMPT ENGINEERING | Expert framework extraction, meta-prompting |
| **Nate B Jones** | AI SYSTEMS | Intent engineering, disambiguation, trust architecture |
| **Darrel Wilson** | AUTOMATION | Workflow automation, freelancer replacement, AI monetization |
| **Mark Kashef** | COUNCILS | Multi-agent orchestration, horizontal task splitting |
| **Andrew Wilkinson** | VIBE CODING | Rapid AI execution, problem-to-product translation |
| **Lance & Yichao** | CONTEXT ENGINEERING | LLM app architecture, context window optimization |
| **Logan Kilpatrick** | AI PROTOTYPING | Google AI Studio, speed-over-perfection, rapid deployment |
| **Dr. Kriukow** | AI HUMANIZATION | Statistical unpredictability, detection avoidance, structural depatterns |

### Routing Logic

```
"AI help"
├── Prompt optimization → Futurepedia
├── Agent reliability → Nate B Jones
├── Agent architecture → Nick Saraev
├── Claude Code / CLAUDE.md → Boris
├── AI ops / team adoption → Rachel Woods
├── Agent deployment / debugging → Sherwin Wu
├── Workflow automation → Darrel Wilson
├── Multi-agent systems → Mark Kashef
├── Rapid AI building → Andrew Wilkinson
├── Context window optimization → Lance & Yichao
├── Google AI Studio → Logan Kilpatrick
└── Humanize AI text → Dr. Kriukow

"Build an AI agent"
├── Architecture → Nick Saraev
├── Fleet management → Sherwin Wu
└── Council design → Mark Kashef

"Make AI text sound human"
└── Dr. Kriukow (but NOT after strong writer agents — see card)
```

---

## Domain 7: Writing & Storytelling

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Mitch Albom** | LITERARY | Premium writing, emotional architecture |
| **Shaan Puri** | STORY STRUCTURE | Frame, intention+obstacle, emotion |
| **Dan Wang** | ANALYTICAL | Long-form, observation, essays |
| **Oscar Hoglund** | AUDIO NARRATIVE | Sound storytelling, emotional umami |
| **Jonathan Franzen** | LITERARY FICTION | Character psychology, narrative compression |
| **Lucas Alpay** | FICTION CRAFT | Story structure, character development, fiction writing |
| **Fareed Zakaria** | ARGUMENT STRUCTURE | International analysis, argument architecture, essay construction |
| **Robert Mack** | HUMOR | Truth-first comedy, wit engineering, comedic timing |

### Routing Logic

```
"Write a story"
├── Structure/frame → Shaan Puri
├── Premium prose → Mitch Albom
├── Long-form essay → Dan Wang
├── Audio dimension → Oscar Hoglund
├── Literary fiction → Jonathan Franzen
├── Fiction/character → Lucas Alpay
└── Funny/humor → Robert Mack

"Newsletter writing"
├── Analytical → Dan Wang
├── Emotional → Mitch Albom
└── International/geopolitical → Fareed Zakaria

"Make this funnier"
└── Robert Mack
```

---

## Domain 8: Products & Monetization

> **Exclusivity Boundary**: This domain owns product design, pricing, and monetization strategy. If the goal is BUILDING or PRICING a product/service, route here. If the goal is SELLING it, route to Domain 4.

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Nicolas Cole** | PRODUCT VEHICLES | Product format selection, pricing psychology, digital product launches |
| **Monk.AI** | OFFER DESIGN | Consulting offer pyramid, pricing tiers, client ascension |
| **Samuel Thompson** | MARKET VALIDATION | Shadow markets, unit economics, market entry |
| **Stockton Walbeck** | LEAD MAGNETS | 4-type taxonomy, conversion funnels, data-backed lead gen |
| **Maria Wendt** | DIGITAL PRODUCTS | Product-first business building, course design |
| **Thrivecart** | RAPID PRODUCTS | Weekend product standard, pricing psychology, grocery store method |
| **Sabrina Ramonov** | AI MONETIZATION | Distribution before product, community building, Skool design |
| **Shan Hanif** | AUDIENCE MONETIZATION | Dual engine (audience + product), community architecture |
| **Tim Danilov** | NICHE BENDING | Format innovation, market-format combinations, blue ocean |
| **Paul James** | AI SERVICES | Zero-cost positioning, modular service design, recurring revenue |
| **Darrel Wilson** | AI AUTOMATION SERVICES | Warm lead philosophy, tool-over-opinion, AI service monetization |
| **Ross McKay** | CPG/PHYSICAL PRODUCTS | Premium at scale, retail distribution, DTC-to-mass transition |
| **Vincent Hu** | INFO BUSINESS SCALING | Growth ecosystems, 3-yes conversion, hybrid offers, trust-first positioning, coaching/consulting business architecture |

### Routing Logic

```
"Build a product"
├── Digital product/course → Maria Wendt or Nicolas Cole
├── AI consulting offer → Monk.AI
├── Lead magnet → Stockton Walbeck
├── Weekend MVP → Thrivecart
├── Physical product → Ross McKay
└── Format innovation → Tim Danilov

"How to price [X]"
├── Consulting tiers → Monk.AI
├── Digital products → Nicolas Cole or Thrivecart
├── Physical → Ross McKay
└── Unit economics → Samuel Thompson

"Monetize my [audience/AI skills/content]"
├── AI tools → Sabrina Ramonov
├── AI services → Paul James or Darrel Wilson
├── Audience → Shan Hanif
├── Niche opportunity → Tim Danilov
├── Community → Sabrina Ramonov
└── Info/coaching/consulting business → Vincent Hu

"Validate my idea"
└── Samuel Thompson → Kallaway (content fit)
```

---

## Domain 9: SEO & Search

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Nathan Gotch** | SEO MASTERY | Technical SEO, keyword strategy, authority building |
| **Adam Enfroy** | AFFILIATE/BLOG | Infinite keyword loops, three-tier content funnel, 70% AI production |
| **Wordsatscale** | RAPID RANKING | Competition vacuum strategy, authority arbitrage, LSI bypass |
| **Ethan Smith** | ANSWER ENGINES | AEO strategy, citation engineering, experimental search methodology |

### Routing Logic

```
"Help with SEO"
├── Technical SEO / keyword strategy → Nathan Gotch
├── Affiliate blog / niche site → Adam Enfroy
├── Quick ranking wins → Wordsatscale
└── AI search / answer engines → Ethan Smith

"Get found on Google"
├── Organic SEO → Nathan Gotch
├── Content volume → Wordsatscale
└── Answer engine optimization → Ethan Smith

"Start a blog that makes money"
└── Adam Enfroy
```

---

## Domain 10: Design & Web

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Oren** | TASTE DEVELOPMENT | CEV framework, creative judgment, luxury psychology, visual direction |
| **Kittl** | GRAPHIC DESIGN | Typography, mood-based font selection, AI design prompts, layout |
| **Andy Lo** | PREMIUM WEB | Headless CMS, motion design, cinematic web architecture |
| **Sam Goddard** | MEDIA SCALING | Content infrastructure, production systems, agency scaling |
| **Sean Kochel** | DESIGN-FIRST BUILD | Felt problems, UX-driven development, AI business strategy |
| **Alex Copper** | BRAND STRATEGY | Creative strategy, visual identity systems |

### Routing Logic

```
"Design help"
├── Visual direction / taste → Oren
├── Typography / graphic design → Kittl
├── Premium website → Andy Lo
├── Content production system → Sam Goddard
├── UX / design-first product → Sean Kochel
└── Brand visual identity → Alex Copper

"Build a website"
├── Premium/cinematic → Andy Lo
├── UX-driven → Sean Kochel
└── Media/content site → Sam Goddard

"Improve my visual taste"
└── Oren
```

---

## Domain 11: Video & Media

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Tao Prompts** | AI VIDEO | Deterministic video pipeline, cinematic prompting, storyboard architecture |
| **PJ Accetturo** | PRODUCTION-GRADE AI | Professional AI video that doesn't look gimmicky |
| **Remotion** | PROGRAMMATIC VIDEO | React-based video, data-driven video generation |
| **Seena Rez** | SHORT-FORM | TikTok scripts, viral hooks (also in Domain 2) |
| **Stockton Walbeck** | VIDEO LEAD MAGNETS | Video-based lead magnets and conversion content |

### Routing Logic

```
"Create a video"
├── AI-generated cinematic → Tao Prompts
├── Production-grade AI → PJ Accetturo
├── Programmatic/data-driven → Remotion
├── TikTok/short-form → Seena Rez
└── Lead magnet video → Stockton Walbeck

"AI video production"
├── Storyboard/multi-shot → Tao Prompts
├── Professional quality → PJ Accetturo
└── Automated generation → Remotion
```

---

## Domain 12: Strategy & Business Architecture

> **Exclusivity Boundary**: This domain owns high-level strategic thinking, business architecture, and cross-domain synthesis. If the goal is a STRATEGIC DECISION or BUSINESS MODEL question, route here. If the goal is SALES EXECUTION, route to Domain 4.

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Jim O'Shaughnessy** | CROSS-DOMAIN SYNTHESIS | Philosopher-financier lens, high-stakes decisions, long-term strategy |
| **April Dunford** | B2B POSITIONING | Obviously Awesome framework, competitive context, market category creation |
| **Daniel Priestley** | DEMAND ENGINEERING | Oversubscribed methodology, Key Person of Influence |
| **Marc Andreessen** | AI ECONOMICS | Technology philosophy, venture thesis, future of work |
| **Manus.AI** | INTELLIGENCE | McKinsey-grade research, competitive intelligence, strategic briefs |
| **SooWei Goh** | CONSULTING LEVERAGE | Founder workflow, scale architecture, leverage auditing |
| **Rory Sutherland** | BEHAVIORAL STRATEGY | Perceived value, psychological reframing, unconventional marketing |
| **Lulu Cheng Meservey** | COMMUNICATIONS | PR strategy, crisis communications, reputation management |
| **Vincent Hu** | INFO BUSINESS ARCHITECTURE | Growth ecosystems, trust-first scaling, revenue reverse-engineering, coaching/consulting |
| **Mike Foutia** | MARKETING TOOLS | Marketing technology landscape, tool selection, trend analysis |

### Routing Logic

```
"Help me decide"
├── High-stakes / multi-domain → Jim O'Shaughnessy
├── B2B positioning → April Dunford
├── Demand engineering → Daniel Priestley
├── AI/tech strategy → Marc Andreessen
├── Consulting business → SooWei Goh
└── Info/coaching/consulting scaling → Vincent Hu

"Research [market/competitor]"
└── Manus.AI → Jim O'Shaughnessy (synthesis)

"PR / communications strategy"
└── Lulu Cheng Meservey

"Which marketing tools?"
└── Mike Foutia
```

---

## Domain 13: Audience & Growth

> **Exclusivity Boundary**: This domain owns audience building, newsletter growth, and community architecture. If the goal is GROWING an audience or community, route here. If the goal is MONETIZING it, route to Domain 8.

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Tyler Denk** | NEWSLETTER | BDE system, referral engineering, social launch sequences |
| **Dan Koe** | CREATOR BUSINESS | One-person business, past-self avatar, content multiplication |
| **Jasmin Alic** | LINKEDIN GROWTH | Trapdoor hooks, distributed commenting, organic growth |
| **Ali Abdaal** | ACTION BIAS | Two-way door thinking, experiment-driven growth, productivity |
| **Brock Johnson** | SHAREWORTHY | Social-first content, shareability engineering |
| **Seth Godin** | IDEA PROPAGATION | Virusworthiness, sneeze-network design, permission marketing |
| **Adam Enfroy** | BLOG GROWTH | Niche blog strategy, affiliate funnels, content velocity |

### Routing Logic

```
"Grow my audience"
├── Newsletter → Tyler Denk
├── LinkedIn → Jasmin Alic or Lara Acosta (from Domain 3)
├── Blog/SEO → Adam Enfroy
├── Community → Sabrina Ramonov (from Domain 8) or Shan Hanif
├── Ideas that spread → Seth Godin
└── Social shareability → Brock Johnson

"Start a newsletter"
└── Tyler Denk

"I'm overthinking / can't start"
└── Ali Abdaal (two-way door thinking)
```

---

## Domain 14: Mindset, Messaging & Consciousness

> **Exclusivity Boundary**: This domain owns belief change, identity transformation, message architecture, and philosophy of mind. Route here when the problem is INTERNAL (mindset blocks, identity, messaging failures, existential stuckness) rather than external (market, product, sales).

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Jeremy Haynes** | IDENTITY SYSTEMS | Identity-governs-everything, mindset rewiring |
| **David Bayer** | PRESENCE/PERFORMANCE | Elevated presence, performance optimization |
| **Michael Bernoff** | IDENTITY ENGINEERING | Reset frame, language rewiring, limiting identity interrupts |
| **David McRaney** | BELIEF SCIENCE | Deep canvassing, motivational interviewing, belief change |
| **Donald Miller** | CULTURE & MESSAGING | PEACE framework, culture turnaround, strategic messaging |
| **Heath Brothers** | IDEA STICKINESS | SUCCESs framework, schema violation, commander's intent |
| **Seth Godin** | MOVEMENT BUILDING | Tribes, permission marketing, idea viruses |
| **Joscha Bach** | CONSCIOUSNESS / PHILOSOPHY OF MIND | Computational phenomenology, identity engineering, system coherence, phase transition design |

### Routing Logic

```
"I'm stuck / blocked"
├── Identity/mindset → Jeremy Haynes or Michael Bernoff
├── Performance → David Bayer
├── Belief-level → David McRaney
└── Existential / consciousness / "how does this really work?" → Joscha Bach

"My messaging isn't working"
├── Message stickiness → Heath Brothers (SUCCESs)
├── Brand messaging/culture → Donald Miller (PEACE)
├── Movement/tribe building → Seth Godin
└── Real-reason excavation → Tobias Allen (from Domain 4)

"How does [X] actually work?" / "What's the mechanism?"
└── Joscha Bach (computational phenomenology)

"Design my identity / who should I become?"
├── Identity instruments → Joscha Bach
├── Identity rewiring → Michael Bernoff
└── Identity-first business → Dan Koe (from Domain 3)

"Build a movement"
└── Seth Godin + Erica Mallet (from Domain 3)

"Something needs to click / cohere"
└── Joscha Bach (phase transition design)
```

---

## Domain 15: Industry-Specific

### Swim Lanes

| Expert | Owns | Use For |
|--------|------|---------|
| **Joshua Smith** | REAL ESTATE | KPI-driven production, market agnosticism, conversion optimization |
| **Jonathan Courtney** | DESIGN THINKING | UX sprints, design process, product design |
| **Sabri Suby** | PAID ADVERTISING | AI-powered ads, direct response marketing, campaign scaling |

### Routing Logic

```
"Real estate help"
└── Joshua Smith

"Design sprint / UX"
└── Jonathan Courtney

"Run paid ads"
└── Sabri Suby
```

---

## Standard Handoff Chains

### TikTok Content Creation
```
1. [Kallaway] → Buyer psychology, concept validation
2. [Seena Rez] → PSAEP script, hook engineering
3. [Harry Dry] → Copy audit (optional)
```

### Sales Page Creation
```
1. [Dai Media] → Consumer posture research
2. [Kallaway] → Buyer journey mapping
3. [Cardinal Mason] or [Alen Sultanic] → Copy
4. [Luke Iha] → Proof audit
5. [Harry Dry] → Final evaluation
```

### Personal Brand Build
```
1. [Caleb Ralston] → Positioning, differentiation
2. [Jun Yuh] → Content calendar, formats
3. [Kallaway] → Buyer-focused optimization
4. [Lara Acosta] or [Tommy Clark] → LinkedIn execution
```

### Product Launch
```
1. [Samuel Thompson] → Market validation, unit economics
2. [Nicolas Cole] or [Thrivecart] → Product design
3. [Stockton Walbeck] → Lead magnet
4. [Kallaway] → Content strategy
5. [Seena Rez] or [Cardinal Mason] → Content/copy
6. [Jeremy Miner] → Sales optimization
```

### AI Business Launch
```
1. [Manus.AI] → Market intelligence
2. [Monk.AI] → Offer architecture
3. [Paul James] or [Darrel Wilson] → Service design
4. [Lindsay] → Client acquisition
5. [Boris] → System architecture
```

### Newsletter Launch
```
1. [Tyler Denk] → Strategy, referral architecture
2. [Dan Wang] or [Mitch Albom] → Writing voice
3. [Lara Acosta] → Distribution (LinkedIn)
4. [Stockton Walbeck] → Lead magnet
```

### Premium Content Pipeline
```
1. [Oren] → Visual direction, taste
2. [Kittl] → Design execution
3. [Andy Lo] → Web build
4. [Oscar Hoglund] or [Mitch Albom] → Emotional writing layer
```

---

## Compound Combinations

Certain expert pairings produce force-multiplier results that exceed what either expert delivers alone. Use these when the trigger condition matches.

| Combination | Compound Effect | Trigger Condition |
|-------------|----------------|-------------------|
| **Jeremy Miner** + **Michael Bernoff** | Identity-first sales — Bernoff rewires self-image, Miner closes with NEPQ | Prospect has emotional resistance or identity-level objections |
| **Seena Rez** + **Cardinal Mason** | Viral commerce — Rez drives TikTok traffic, Mason converts it | Product launch needing both attention and revenue |
| **Harry Dry** + **Alen Sultanic** | Precision long-form — Dry's concrete rules applied across Sultanic's persuasion architecture | High-stakes sales letter or VSL that must be both tight and long |
| **Shaan Puri** + **Kallaway** | Story-driven viral content — Puri's narrative arc + Kallaway's dopamine psychology | Content that needs to spread AND retain (not just one) |
| **Lara Acosta** + **Cardinal Mason** | LinkedIn revenue engine — Acosta builds authority, Mason monetizes it | Professional service providers moving to creator-led growth |
| **Dan Koe** + **Jun Yuh** | Multipassionate brand — Koe's one-person business model + Jun's content format strategy | Creators with multiple interests who need a cohesive brand |
| **Nicolas Cole** + **Mitch Albom** | Premium prose — Cole's sentence-level craft + Albom's emotional architecture | Premium content that must read beautifully AND move people |
| **Samuel Thompson** + **Sabri Suby** | Paid product launch — Thompson validates the shadow market, Suby drives paid traffic to it | Info product launch where organic alone won't hit revenue targets |
| **Monk.AI** + **Lindsay** | Consulting acquisition — Monk builds the offer architecture, Lindsay executes outreach | New AI consulting offer that needs both a compelling package and clients |
| **Tobias Allen** + **Cardinal Mason** | Revenue system — Allen's direct response strategy + Mason's conversion copy | Building end-to-end email/funnel revenue systems |
| **Bond Halbert** + **David Deutsch** | Legendary direct response — Halbert's market language + Deutsch's musical architecture | High-stakes direct mail or long-form that must convert AND impress |
| **April Dunford** + **Daniel Priestley** | Positioning + Demand — Dunford positions the product, Priestley engineers demand for it | B2B product that's well-built but poorly positioned |
| **Tyler Denk** + **Seth Godin** | Viral newsletter — Denk's referral mechanics + Godin's sneeze-network design | Newsletter that needs both organic spread and subscriber growth |
| **Nick Saraev** + **Boris** | Agent fleet — Saraev's self-healing architecture + Boris's orchestration methodology | Complex multi-agent system builds |
| **Tao Prompts** + **PJ Accetturo** | Cinema-grade AI video — Tao's storyboard architecture + PJ's production polish | AI video that needs to look professional, not gimmicky |
| **Joscha Bach** + **Steven Pressfield** | Consciousness + Resistance — Bach diagnoses the mechanism of the block, Pressfield mobilizes the war against it | Creative blocks that need both diagnosis AND mobilization |
| **Vincent Hu** + **April Dunford** | Trust positioning + competitive context — Hu's trust-first ecosystem + Dunford's positioning sharpens how info businesses differentiate | Info business positioning that needs both market context and trust architecture |
| **Vincent Hu** + **Luke Iha** | Ecosystem copy — Hu architects the growth system, Iha writes the conversion copy within it | Info business needing both system design and high-converting copy |

> [!TIP]
> When a task matches a compound trigger, route to **both** experts — either via council or sequential handoff. The lead expert (listed first) sets strategy; the second expert executes their specialty within that frame.

---

## Override Protocol

If I route to an expert and you prefer a different approach:

**Say**: "Use @different-expert instead" or "I want [X]'s approach"

I will immediately switch and apply the requested expert's methodology.

---

*Last updated: 2026-03-03*
*95 agents across 15 domains (some dual-listed)*
