# MES 3.0 Skills Index

## Deployable Expertise Skills

Skills are action-oriented capabilities that Claude can execute. Each skill draws from one or more expert extractions to deliver specific outcomes.

---

## 🔍 WIDE RESEARCH SYSTEM

### `wide-research`
**Purpose:** Manus-style parallel subagent research and intelligence gathering
**Full Documentation:** See `WIDE-RESEARCH-SKILL.md`
**Natural Language:** "Research..." / "Find out..." / "What are people saying..."

### Research Modes

| Mode | Natural Language | What Happens |
|------|-----------------|--------------|
| **Survey** | "Research the landscape of..." | Broad mapping, 5-10 scouts |
| **Farm** | "What are people saying about..." | Social listening, exact language |
| **Hunt** | "Find signals/patterns in..." | Weak signal detection |
| **Verify** | "Is it true that..." / "Check if..." | Multi-source fact checking |

### Subagent Stack
- `research-scout` — Focused intelligence gathering
- `social-listener` — Voice-of-customer mining
- `pattern-hunter` — Signal detection + trends
- `verification-agent` — Multi-source fact checking
- `synthesis-engine` — Pattern extraction + insight generation

---

## 🎬 CREATIVE ASSEMBLY SYSTEM

### `creative-assembly`
**Purpose:** Multi-expert creative production with parallel execution, handoffs, and refinement
**Full Documentation:** See `CREATIVE-ASSEMBLY-SKILL.md`
**Natural Language:** "Write me..." / "Create a..." / "I need a..." / "Build me..."

### Two Modes (Auto-Detected)

| Mode | Triggered By | What Happens |
|------|-------------|--------------|
| **Full Assembly** | Default | Experts collaborate → one polished piece |
| **Selection Assembly** | "...show me options" / "...versions" | Multiple versions → you pick → then polished |

### The Production Pipeline

```
DECOMPOSE → ASSIGN EXPERTS → PARALLEL PRODUCE → ASSEMBLE → EDIT → DELIVER
```

### Expert Auto-Assignment

| Task Type | Primary Experts |
|-----------|-----------------|
| Sales email/copy | David Deutsch, Cardinal Mason, Bond Halbert |
| LinkedIn post | Lara Acosta, Kallaway |
| Sales page | David Deutsch, Bond Halbert, Monk AI |
| Video script | Kallaway, Shaan Puri |
| Story/narrative | Jonathan Franzen, Mitch Albom |
| Hooks/headlines | Kallaway, Harry Dry |
| Offer copy | Monk AI, Greg Hickman |
| Email sequence | Kai Lode, Cardinal Mason |
| Visual direction, aesthetics | Oren (creative direction, taste, brand visuals) |
| Brand content strategy | Oren, Kallaway |
| Mood boards, creative briefs | Oren |

### The Complete Loop

```
"Research what's working in [space]"    → Wide Research
"Now write me a [deliverable]"          → Creative Assembly (informed by research)
"Should I [decision]?"                  → Council (informed by both)
```

---

## Content Creation Skills

### `write-hooks`
**Purpose:** Generate attention-grabbing hooks for any platform
**Sources:** Kallaway, Shaan Puri, Nicolas Cole, Harry Dry
**Trigger:** "Write hooks for [topic/platform]"
**Output:** 10-20 hooks with psychological triggers identified

### `write-copy`
**Purpose:** Create conversion-focused copy
**Sources:** Alen Sultanic, Bond Halbert, David Deutsch, Cardinal Mason, Harry Dry
**Trigger:** "Write copy for [product/offer/email]"
**Output:** Complete copy with headline, body, CTA

### `write-story`
**Purpose:** Craft compelling narratives
**Sources:** Mitch Albom, Donald Miller, Lucas Alpay, Shaan Puri, Dan Wang
**Trigger:** "Write a story about [topic/transformation]"
**Output:** Structured narrative with emotional beats

### `write-linkedin`
**Purpose:** Create LinkedIn content
**Sources:** Lara Acosta, Kallaway
**Trigger:** "Create LinkedIn post about [topic]"
**Output:** Platform-optimized post with hook + body + CTA

### `write-script`
**Purpose:** Video/podcast scripts
**Sources:** Oscar Hoglund, Kallaway, Seena Rez
**Trigger:** "Write script for [video type]"
**Output:** Full script with timing, hooks, retention triggers

---

## Strategy Skills

### `build-offer`
**Purpose:** Design irresistible offers
**Sources:** Monk AI, Daniel Priestley, SooWei
**Trigger:** "Build an offer for [service/product]"
**Output:** Complete offer architecture with pricing, positioning, delivery

### `create-funnel`
**Purpose:** Map customer journey
**Sources:** Monk AI, Sabri Suby, ThriveCart
**Trigger:** "Design funnel for [business type]"
**Output:** Full funnel with touchpoints, copy angles, conversion triggers

### `position-brand`
**Purpose:** Develop brand positioning
**Sources:** Erica Mallett, Lara Acosta, Jun Yuh, Tom Noske, Caleb Ralston
**Trigger:** "Position my brand for [market/audience]"
**Output:** Positioning statement, enemy identification, belief architecture

### `plan-content`
**Purpose:** Create content strategy
**Sources:** Kallaway, Lara Acosta, Jun Yuh
**Trigger:** "Plan content strategy for [platform/goal]"
**Output:** Content calendar, pillar topics, format mix

### `optimize-seo`
**Purpose:** SEO and AI discoverability
**Sources:** Nathan Gotch, WordAtScale
**Trigger:** "Optimize for [keyword/topic]"
**Output:** SEO strategy with AI ranking considerations

---

## Sales Skills

### `conduct-sale`
**Purpose:** Structure sales conversations
**Sources:** Jeremy Miner, Monk AI
**Trigger:** "Help me sell [offer] to [prospect type]"
**Output:** NEPQ-based conversation framework, objection handling

### `write-proposal`
**Purpose:** Create winning proposals
**Sources:** Monk AI, SooWei, Daniel Priestley
**Trigger:** "Write proposal for [project/client]"
**Output:** Complete proposal with value anchoring

### `handle-objections`
**Purpose:** Overcome sales resistance
**Sources:** Jeremy Miner, Monk AI
**Trigger:** "Handle objection: [specific objection]"
**Output:** Response framework with psychological reframes

---

## AI & Automation Skills

### `build-agent`
**Purpose:** Design AI agent systems
**Sources:** Mark Kashef, JARVIS Protocol, Lindsay, Andrew Wilkinson
**Trigger:** "Build an agent for [task/workflow]"
**Output:** Agent configuration with prompts and workflows

### `engineer-prompt`
**Purpose:** Create effective prompts
**Sources:** Futurepedia, Cardinal Mason
**Trigger:** "Create prompt for [task]"
**Output:** Structured prompt with examples

### `automate-workflow`
**Purpose:** Design AI automations
**Sources:** Darrel Wilson, Paul James, Sabri Suby
**Trigger:** "Automate [process]"
**Output:** Automation blueprint with tool recommendations

### `sell-ai-services`
**Purpose:** Package and sell AI offerings
**Sources:** Ai Chris Lee, Lindsay, Samuel Thompson
**Trigger:** "Help me sell AI services"
**Output:** Offer packaging, pricing, pitch framework

---

## Business Skills

### `build-consulting`
**Purpose:** Structure consulting business
**Sources:** Monk AI, SooWei, Daniel Priestley
**Trigger:** "Build consulting offer for [expertise]"
**Output:** Offer pyramid, delivery model, pricing

### `create-digital-product`
**Purpose:** Design digital products
**Sources:** ThriveCart, Samuel Thompson, Adam Enfroy
**Trigger:** "Create digital product about [topic]"
**Output:** Product architecture, delivery, launch plan

### `go-viral`
**Purpose:** Engineer viral content
**Sources:** Kallaway, Seena Rez, Jun Yuh
**Trigger:** "Make [content] go viral"
**Output:** Viral engineering strategy with specific tactics

### `grow-audience`
**Purpose:** Build engaged following
**Sources:** Kallaway, Lara Acosta, Jun Yuh, Tom Noske
**Trigger:** "Grow audience on [platform]"
**Output:** Growth strategy with content + engagement tactics

---

## Mindset Skills

### `shift-mindset`
**Purpose:** Break through mental barriers
**Sources:** Michael Bernoff, Donald Miller, Jim O'Shaughnessy
**Trigger:** "Help me overcome [block/challenge]"
**Output:** Reframe + action steps

### `think-strategically`
**Purpose:** High-level strategic thinking
**Sources:** Jim O'Shaughnessy, Seth Godin, Dan & Chip Heath
**Trigger:** "Think through [decision/strategy]"
**Output:** Strategic analysis with frameworks

---

## Persona Skills

### `profile-audience`
**Purpose:** Deep audience understanding
**Sources:** Dai Media, Erica Mallett, Monk AI
**Trigger:** "Profile audience for [offer/content]"
**Output:** Identity persona with psychology, triggers, language

### `create-avatar`
**Purpose:** Build customer avatar
**Sources:** Dai Media, Lara Acosta
**Trigger:** "Create avatar for [business/offer]"
**Output:** Complete persona with demographics + psychographics + identity

---

## NEW: Client Acquisition Skills

### `get-first-clients`
**Purpose:** Acquire first 5 paying clients for a new productized offer
**Sources:** Greg Hickman
**Trigger:** "Help me get my first clients for [offer]"
**Output:** Warm pipeline activation strategy, direct outreach templates, productized offer positioning

### `monetize-audience`
**Purpose:** Convert email lists and audiences into revenue
**Sources:** Kai Lode (8M+ subscriber methodology)
**Trigger:** "Monetize my [list/audience]"
**Output:** Segmentation strategy, quiz funnel architecture, permission-based selling sequences

### `launch-digital-product`
**Purpose:** Create and launch digital products systematically
**Sources:** ThriveCart ($5B+ tracked sales methodology)
**Trigger:** "Launch a digital product about [topic]"
**Output:** Product architecture, pricing strategy, funnel sequence, 90-day launch plan

---

## NEW: Advanced Copywriting Skills

### `convert-cold-traffic`
**Purpose:** Write copy that converts ice-cold audiences
**Sources:** David Deutsch ($1B+ direct response results)
**Trigger:** "Write cold traffic copy for [offer]"
**Output:** Mechanism reveals, psychological precision copy, fascination bullets, cold-to-sold sequences

### `write-fascinations`
**Purpose:** Create irresistible curiosity bullets that demand clicks
**Sources:** David Deutsch, Bond Halbert, Alen Sultanic
**Trigger:** "Write fascinations for [topic/offer]"
**Output:** 20-50 fascination bullets with psychological triggers identified

---

## NEW: AI Operating System Skills

### `build-daily-os`
**Purpose:** Design AI-powered daily operating systems
**Sources:** Alex Finn, Boris (Claude Cowork creators)
**Trigger:** "Build my AI daily operating system"
**Output:** Claude Cowork configuration, morning briefing prompts, proactive AI partnership setup

### `engineer-context`
**Purpose:** Design optimal context architecture for AI agents
**Sources:** Lance & Yichao (context engineering methodology)
**Trigger:** "Optimize context for [AI system/agent]"
**Output:** Memory system design, instruction architecture, context loading strategies

---

## NEW: Narrative & Story Skills

### `architect-story`
**Purpose:** Build complete story architecture with emotional precision
**Sources:** Jonathan Franzen, Mitch Albom, Donald Miller
**Trigger:** "Help me craft [story/narrative]"
**Output:** Story architecture, character development, scene construction, emotional beat mapping

### `write-literary`
**Purpose:** Create literary-quality prose and essays
**Sources:** Jonathan Franzen, Dan Wang, Nicolas Cole
**Trigger:** "Write [essay/article/literary piece] about [topic]"
**Output:** Eloquent, insightful, timeless prose with observation-driven detail

---

## NEW: Mindset & Energy Skills

### `clear-counterintention`
**Purpose:** Identify and clear hidden blocks to success
**Sources:** Kevin Trudeau (possibility psychology)
**Trigger:** "Clear my blocks around [goal]"
**Output:** Counterintention identification, energy clearing protocol, mindset reframe

### `energize-marketing`
**Purpose:** Add energetic dimension to marketing
**Sources:** Kevin Trudeau ($20B+ marketing results + energetics)
**Trigger:** "Add energy to my marketing for [offer]"
**Output:** Dual-domain strategy (tactical + energetic), authentic enthusiasm protocols

---

## NEW: Investment & Opportunity Skills

### `detect-trends`
**Purpose:** Identify investment opportunities through social arbitrage
**Sources:** Chris Camillo ($20K→$2M methodology)
**Trigger:** "Find investment opportunities in [trend/signal]"
**Output:** Information asymmetry identification, trend detection framework, conviction level assessment

### `find-asymmetric-bets`
**Purpose:** Locate opportunities with asymmetric risk/reward
**Sources:** Chris Camillo, Jim O'Shaughnessy
**Trigger:** "Find asymmetric opportunities in [domain]"
**Output:** Risk/reward analysis, signal vs noise assessment, timing framework

---

## How to Use Skills

### In Claude Code (Mobile or Desktop)

Simply reference the skill naturally:
- "Use the write-hooks skill to create hooks for my coaching offer"
- "Deploy build-offer to design my consulting package"
- "Run conduct-sale for a discovery call with a marketing agency"

### Skill Stacking

Combine skills for compound results:
- `profile-audience` → `write-hooks` → `write-copy` = Targeted sales page
- `position-brand` → `plan-content` → `write-linkedin` = Authority-building content
- `build-offer` → `write-proposal` → `conduct-sale` = Complete sales system

---

*Skills execute at virtuoso level, drawing from 82+ expert extractions*
