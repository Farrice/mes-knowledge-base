# Adam Sandler (The Viable Edge) — MES 3.0 Extraction Notes

> **Disambiguation**: This is Adam Sandler, founder of **The Viable Edge** (viableedge.com) — an AI second-brain / knowledge-base practitioner. **Not the actor.** Marketing background, 20+ years in the workforce, non-engineer.

## Content Assessment
- **Source**: Ryan Doser "AI Rabbit Holes" interview — "He Sells AI Second Brains to Businesses (For $1000s)", published 2026-07-14, 32:51. Transcript (`extractions/transcripts/NNbuknlK8fs.txt`, 6,034 words) + 99-frame visual context + 35-frame demo zoom (11:00–15:30).
- **Domain**: SELL-SIDE go-to-market for AI second-brain/knowledge-base services — how a non-engineer practitioner packages, prices, pitches, sequences, scales, and delivers KB engagements to small businesses and marketing teams.
- **Depth tier**: Standard. One interview, sell-side scoped. The BUILD mechanics (audit internals, tier architecture, ingest, install) already exist in the system (Simon + Liam Mley); this extraction owns the GTM layer that sits on top.
- **Coverage discipline**: NET-NEW only. Build-side machinery is stacked, never duplicated.

## The wedge (what Adam adds that no existing expert does)
Every KB expert in the system (Simon/Kieran, Liam Mley) teaches how to BUILD the brain. Adam is the first who teaches how to **SELL** it as a foot-in-the-door offer to non-technical small businesses — KB-first offer sequencing, paid-audit entry mechanics, department-scale trust wedge, provider-portability sales language, and the delivery upgrades (branded client UI, anti-slop voice charter) that make a markdown folder feel like a $1000s product. His positioning insight — context-engineering tooling targets engineers, leaving knowledge work wide open — is the whitespace claim the whole offer sits in.

## NET-NEW patterns (own fully)

1. **KB-first offer sequencing** — the bottleneck realization. Verbatim: *"frequently I would run into an issue where the information that was needed to power this workflow... was not easily accessible... eventually it occurred to me that this should just be the first step... develop a knowledge base or a second brain."* Prospects ask for the agent/fractional-CMO; Adam refuses to build agents on no substrate. KB = step 1A/1B. Recurring-relationship math: *"once you have a knowledge base, building agents or tools on top of it... becomes much more straightforward... you're setting yourself up for more business."*

2. **Paid audit as the entry offer** — *"when these engagements are beginning, there's a huge opportunity for an audit."* The spine question: *"what is sort of like their core spine... What is the one thing that everything else in the business sort of like ladders up to? And usually that is a goal or an objective."* Kickoff line: *"Okay, let's talk about your spine... what is the driving force of this company? And that can be a conversation that generates an audit."* Baseline schema: *"I do have some material that lays out a baseline set of schema. There's seven different data points, basically. And this is usually enough to get going."* The audit surfaces three things: *"you might surface things that are on fire... you might surface things that are outdated... you might surface connections that were not obvious."* Real example: brand guideline from 2020, another older — *"the audit can sort of like help just scrub out all of the old stuff."*

3. **Department-scale wedge AS SALES TACTIC** — *"I'm working with clients now where we're doing department-level knowledge bases... there's sort of like a hierarchy and these knowledge bases can also have integrations with each other."* The tactic: *"You don't have to bite off the entire piece of the company right away. You can come in with a smaller engagement to get your feet wet, to develop trust, and something that could be a little bit more like manageable."* An SEO second brain ≠ an accounting second brain; hierarchy + cross-KB integrations come later.

4. **Provider-portability pitch** — *"if you hitch your wagon to a knowledge base and not to Anthropic's ecosystem or OpenAI's ecosystem, you're not stuck there if suddenly that service becomes... untenable."* / *"it sort of unshackles you from one provider's ecosystem and allows you to travel to different ecosystems. It makes you portable."* Sales close: *"We're going to make you ready for AI. We're going to future-proof your business for AI readiness and you're not stuck with one provider."* Tangible proof = the 7-surface output menu (demo t=13:10): *Copy as Claude system prompt · Download MCP instructions · Download Cursor rules · Copy CLAUDE.md snippet · Copy Obsidian vault command · Download brand JSON pack · brand book* — "Use your brand skills anywhere." One body of info, many exports.

5. **Markdown→Supabase scaling path (no RAG/vector for small biz)** — *"you don't really have to worry about the tech stack... a knowledge base at its most basic form is a folder of documents... a lot of small businesses simply don't have the amount of information that would necessarily require a sophisticated rag or vector database."* Scale gate: *"at a certain point, if you want to scale, Superbase or something like it is a great next step... inexpensive... integrates really well."* Also eyeing Convex. The reassurance: *"you don't even need a stack to provide major value with something like a knowledge base."*

6. **Cross-silo insight harvesting as a named deliverable** — *"the magic for clients is when you connect different sources of information and discover new insights."* Real client: a call center whose transcripts *"typically operates in somewhat of a silo... they use them for coaching, for Q&A, and that's really about it"* — Adam adds *"what can marketing learn from this body of work, from all of these customer calls, from the language and the words they use... trending topics... seasonality... that connectivity was not there for this company in the past."* His 12-month prediction is this same move at scale.

7. **Client-facing branded KB UI / graph-narrator** — the delivery upgrade that abstracts the scary chat box. *"there's an abstraction for people who are not as experienced with AI... you put a chat box and you're just like, 'Type slash this.' A lot of people are going to be confused."* Fix: *"you can create a UI fairly quickly these days... one that's branded for your client... Effectively, it could be a markdown file browser... a way for the client themselves to click through their documents, similar to how I showed the knowledge graph. There's a lot of free and open source packages out there that have knowledge graphs. So, you can just pull something down and implement it yourself into your own app."* Style via Claude design: *"I'll use Claude design and pull a style guide for them. And then I'll use that style guide to style and design all of the collateral."* The graph is a RELATIONSHIP NARRATOR (demo t=11:54–12:43): left panel walks numbered entity PAIRS each with a WHY-they-connect sentence — 1. Keyword Assessment — ICPs · 2. Messaging Framework — Positioning · 3. Content Pillars — Positioning · 4. Post Media Profile — Differentiation Strategy · 5. Company Profile — Positioning · 6. Visual Identity — Company Profile · 7. Brand Profile — Voice & Tone — then "Want me to proceed through all seven in this order?" Competitor nodes red; clicking Jasper shows a competitive-relevance panel.

8. **The anti-AI-slop voice charter shipped INSIDE the KB** (demo t=13:37–14:20) — a standard delivery artifact. Structure: *"Voice in Three Words: Direct. Grounded. Unhurried."* / *"What the Voice Is Not: Not a cheerleader... Not 'game-changer.' Not AI-hype."* / *"Hard Rule: No AI Writing Tropes"* / Language Rules with a banned list (game-changing, revolutionary, "AI-powered" as standalone, seamless, robust, leverage, unlock, synergy) / Sample Passages (On brand / Off brand). This is what makes KB output not read as slop.

9. **Scrappy connector workarounds** — *"Calendly, I set up a skill in Claude code that it will go and use the browser control to pull down text files of all of the transcripts since the last time it captured transcripts... once a day I'll run this skill... because there's no integration to pull transcripts from Calendly, which is a major frustration."* Doctrine: *"getting a little bit scrappy, rolling up your sleeves and having an arsenal to implement things like browser control and develop specialized skills is definitely a skill that is going to help a ton."*

10. **Knowledge-work positioning whitespace** — *"A lot of the context engineering solutions... are very much targeting engineers and software development, not so much knowledge work. So I think there's right now an opportunity and a gap for this delivery for non-software related practices."* This is the market claim the whole offer occupies.

## Signature framing (voice DNA)
- KB as **flywheel organism**: *"it's an organism. It grows."* / *"part of the knowledge base... is creating a flywheel-like system that can manage the information... How is information being ingested? How is it being synthesized and processed? And how is older information... being archived or pulled out of what's relevant right now."*
- **Messy pool**: *"you're jumping into a messy pool and you got to clean it all up."* / *"most companies they're a mess. They're a chaotic mess. Their stuff's all over the [place]."*
- **Overload, not lack**: *"It's the overload of information, not the lack thereof... Not all of this can be true at the same time."*
- **Decision log** as an unseen-in-20-years practice: *"within a knowledge base, there's an opportunity to create a decision log... I've been in the workforce for over two decades. I've never really seen a business practicing that sort of thing with that level of specificity."*
- **Least-privilege orchestration**: *"I'll have an orchestrator agent that might leverage sub agents for different jobs... the sub agents who do the best works are the ones who have very limited access to the things they don't need."*
- **Hot context**: *"hot context, which is relevant context right now, might be summaries of calls that I've had over the last 2 weeks... I don't need to tell the AI where to find it... in practice, it kind of feels like magic."*
- **Hates the word "easy"**: repeatedly self-corrects — *"I don't want to say becomes easy... it becomes much more straightforward"* / *"I hate using the word easy. It's straightforward."*

## Coverage delta — DO NOT DUPLICATE (stack instead)
- Technical audit mechanics → `skills/simon-intellectual-library-os/workflows/library-retrieval-audit.md`
- Tier architecture → `skills/simon-intellectual-library-os/workflows/library-brain-ladder.md`
- Ingest curation → `skills/simon-intellectual-library-os/workflows/library-ingest-triage.md`
- The install build → `skills/liam-mley-ai-brain-builder/workflows/05-second-brain-substrate-install.md`
- Discovery interview → `skills/liam-mley-ai-brain-builder/workflows/01-ai-brain-discovery.md`

## Workflow map (8)
Tier 1 (offer): ve-audit-offer · ve-kb-first-sequencing · ve-department-wedge
Tier 2 (delivery/proof): ve-portability-pitch · ve-insight-harvest · ve-scaling-path · ve-client-ui-layer
Tier 3 (positioning): ve-knowledge-work-positioning

## Source ledger (honesty)
- All quotes above are VERBATIM from the transcript (`NNbuknlK8fs.txt`) unless marked as demo-frame decode.
- Demo-frame text (7-surface menu, relationship-narrator pairs, voice charter) is LIKELY-accurate (decoded from 512px frames; the on-screen structure is legible, exact fine-print wording is reconstructed from conductor decode + frame reads).
- Pricing "For $1000s" comes from the video TITLE (Ryan Doser's framing), not a number Adam states — treat as UNCONFIRMED specific pricing; Adam never quotes a dollar figure on camera.
- No corpus beyond this one interview yet; his YouTube/X/viableedge.com content is collectable later for a blind-pass corpus.
