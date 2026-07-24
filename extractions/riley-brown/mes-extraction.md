# Riley Brown — Mastery Extraction (MES 3.0, Deep Tier)

## Content Assessment

- **Source (all verified Riley Brown, @rileybrownai / "Agent Native"):**
  - **Primary** — "Codex Is Basically Running My Company Now" (2026-07-21), ~3,600 words. Riley + co-founder Vashall. Nine live marketing workflows in Codex.
  - **Corpus 1** — "9 AI Agent Skills To Get Ahead of 99% of People" (`corpus/9-ai-agent-skills.txt`). Nine "inevitable trends" for becoming agent-native.
  - **Corpus 2** — "AI Agents Just Changed Forever: GLM 5.2, Codex Skills, Claude & Cursor" (`corpus/codex-skills-agents-changed.txt`). Weekly news; the record-and-replay screen-to-skill feature; open-source model routing.
  - **Visual ground truth** — `visual-notes.md`: frame-by-frame read of the primary video (file trees, the Foreplay skill's actual multi-file Python pipeline, Codex slash-command palette + AGENTS.md memory command, the Chorus agent system prompt, the Gmail AI-content banner).
- **Expert:** Riley Brown — AI-native founder (Chorus, an open agent platform; also Vibecode). Runs his startup's marketing entirely inside Codex + custom skills.
- **Domain:** Agentic marketing operations — running an entire startup's marketing through a coding agent wired to APIs/MCPs: social scraping, creator→skill conversion, competitor ad-spy, ad-creative generation, brand-asset scraping, scheduling, Drive org, booking links, Gmail drafting at scale.
- **Depth Tier:** Deep (forced). Demonstration-dense across three videos plus a frame-level visual layer — strong enough for cross-video pattern confirmation, the highest-confidence extraction signal.
- **Genius Patterns:** 16 identified (7 cross-video confirmed).
- **Hidden Knowledge:** 13 tacit insights detected.
- **Existing Overlap:** Nick Saraev (agentic workflows), Mark Kashef (agent orchestration / silver-platter agentic OS), Rachel Woods (AI operations), Nate B. Jones (agent deployment / orchestration intelligence), Sabrina Ramonov (AI monetization). Riley's distinct wedge: **marketing-specific skill libraries built on scraper APIs, where the durable asset is a named, reusable skill/workflow — not a one-off automation — and taste ("knowing what good looks like") is the load-bearing human input.**

> **GROUNDING / HONESTY FLAG (binding).** All three transcripts and the visual notes are Riley Brown. (An earlier version of this corpus contained two non-Riley videos; those are now quarantined in `extractions/riley-brown/adjacent-sources/` and NOTHING in this document relies on them — the domain frame is fully Riley-grounded.) Every quote below is tagged by source: `[primary]`, `[9-skills]`, `[news]`, or `[visual]`. Transcripts are auto-captioned; spellings preserved verbatim ("codeex"/"Codox"/"CodeX," "Callaay"/"Callaway"/"Kallaway," "soul" = the reasoning-effort/"thinking" dial, "GBT" = GPT, "Fable"/"Mythos" = frontier model names as spoken, "quad.ai" = Claude). Where the visual layer contradicts or deepens the audio, the visual reading wins (it's OCR of the actual screen).

---

## Executive Summary

- **Core Genius:** Riley doesn't prompt an agent to *be* good at marketing — he builds it a **retrieval layer of great examples** (scraped via paid APIs), freezes each capability into a **named, reusable skill/workflow**, and supplies the one thing the agent can't: **taste — knowing what good looks like.** Every high-stakes action terminates in a human-editable draft/link behind approval.
- **What Makes Them Different:** The unit of work is the **skill-as-file** (revealed on screen to be real multi-file pipelines + AGENTS.md memory), not the prompt and not the automation. His creation method is invariant across every video: *do the thing → make it better → "turn it into a skill."* Skills then chain and, increasingly, self-assemble and auto-update.
- **Deployable Skills:** Scrape any creator's best non-sponsored content; convert a creator into a voice-writing skill; ad-spy by longest-running-ad; template-steal ads (scrape → Paper board → Firecrawl brand → image-gen); schedule (Buffer/Typefully); organize Drive; generate constraint-encoded booking links (Cal.com); draft Gmail replies solo or in batch; teach a new skill by screen-recording it (record-and-replay); run recurring work as automations.
- **Hidden Knowledge Captured:** The content-verification gap and the retrieval fix; taste as the non-delegable input; the "just turn it into a skill" framing hides real generated code/AGENTS.md files; the sponsored-post authenticity filter; longest-running-ad as an *explicitly-flagged-as-inference* ROAS proxy; model+effort+open-source routing as active cost control ($250 for 9 frontier prompts); the draft-link/approval terminus as the load-bearing safety layer, reinforced by platform guardrails (Gmail AI banner, Buffer disconnect prompts, Typefully 512MB cap).

---

## Genius Patterns

*(★ = confirmed across 2+ Riley videos — strongest signal)*

### 1. ★ The Examples-Over-Instructions Doctrine (and its twin: "describe, don't hack")
- **What he does:** Refuses to solve content quality by prompting harder. He engineers *retrieval of exemplars* and leans on plain description, because the era of prompt hacks is over.
- **Evidence:** `[primary]` "the reason why AI is bad at writing content scripts is because... with coding, it's very easy to verify whether something is good or something is bad... Whereas content, it's subjective... over the last 3 years... it hasn't gotten any better at writing content... So the only thing you need to do in order to create really good content is provide really good examples... we're giving a database or an API to the AI agent so that whenever it needs to create content like someone, it can just go find good examples." Cross-confirmed `[9-skills]`: "we are moving from a world of prompt hacks to just saying what you want in natural English... he who can describe what they want the best will inherit the world... the only enduring prompt hack is describing what you want."
- **Why non-obvious:** He diagnoses the bottleneck as *verification*, not generation — and routes around it with retrieval + clear description rather than prompt-engineering tricks. This thesis underwrites the entire toolkit.

### 2. ★ Skill-Creation-by-Doing ("turn it into a skill")
- **What he does:** Never hand-writes skill files. He runs the task live, refines the output, then tells the agent to freeze it as a named skill — and the mechanism is a first-class Codex command, not a bespoke hack.
- **Evidence (three independent demos):** `[primary]` "turn all of the his top performing videos into a skill. Call it Callaway top performing." `[9-skills]` "The way that I actually create skills is I will tell the agent to do a thing, then I'll get the agent to do the thing better or to make the thing better and then I'll just tell it to turn it into a skill" (his YouTube-researcher → "hook outline" demo). `[news]` "I recorded my screen and I taught Codex how to use Comet to upload something... and then I immediately turn into a skill" ("manual tweet draft"). Grounded in `[visual]`: Codex's slash-command palette ships **"New workflow — Save this task as a new workflow"** and **"Memory — Create an AGENTS.md file... for Codex"** — the actual underlying mechanism.
- **Why non-obvious:** The durable asset is the *skill*, born from a successful run, not a prompt written from scratch. Three different creation paths (compile-from-scrape, refine-a-task, record-a-screen) all land in the same place: a named, callable file.

### 3. ★ Skills Self-Assemble and Auto-Update (correction written into the file)
- **What he does:** Treats skills as living files that ratchet toward his taste — when the agent errs, he tells it to edit its own skill so the fix sticks; increasingly this happens without asking.
- **Evidence:** `[primary]` "please update the email draft skills so that you never say this or that... so you get it in its context." `[9-skills]` "when you notice where a skill can be improved, just ask... you're going to see this process happen automatically. Your AI agent is just going to create skills for you. And then depending on your responses, your skills will auto update" (his live "update the hook outline skill" demo, adding inline source hyperlinks going forward).
- **Why non-obvious:** Corrections are written *into the asset*, so they compound. The trajectory he's betting on: skills that assemble and refine themselves from how you interact.

### 4. The Creator-to-Skill Compiler
- **What he does:** Scrapes a creator's top-performing (non-sponsored) content and freezes it into a named voice-writing skill.
- **Evidence:** `[primary]` "so that I can write content in his style at any time... this is all that is is just a file with those transcripts that we scraped. But the point is I didn't have to go fetch the information." The deployed output (verbatim, `[primary]`/`[visual]`): "Anthropic just found a hidden workspace inside Claude's brain... nobody programmed it. They call it JSpace." Riley: "actually so good... This is exactly in his tone."
- **Why non-obvious:** He productizes *another person's style* as a permanent callable asset; the name ("Callaway top performing") is the API into their voice.

### 5. The Engagement-Authenticity Filter
- **What he does:** Excludes sponsored posts (bought engagement) from the exemplar set and keeps evidence of every exclusion.
- **Evidence:** `[primary]` "the top 10 videos that has the most engagement that are not sponsored." Agent log, read aloud: "I'll retain the exclusion evidence for every rejected sponsor/promotional post... those can be boosted. So it's like fake... We want the high quality high quality scripts."
- **Why non-obvious:** Naive scraping pulls raw engagement; Riley knows boosted posts poison the pattern set and builds the filter *plus an audit trail* into the skill.

### 6. The Longest-Running-Ad Heuristic (an *explicitly-flagged* ROAS proxy)
- **What he does:** Can't see competitors' internal ROAS, so he uses ad *duration* as a public proxy — and (per the screen) the agent labels this as inference, not proof.
- **Evidence:** `[primary]` "the one metric that we can use... as a proxy for that is how long they've been running it. If you run an ad for nine months... presumably they're spending a lot of money keeping it alive for a good reason." `[visual]` Codex's own output: "'Why it works' is clearly labeled as an inference from creative durability — not proof of ROAS or profitability."
- **Why non-obvious:** Turns a data limitation into a free selection signal *and* preserves epistemic honesty about what the signal does/doesn't prove.

### 7. ★ Effort-Dialing, Token-Budgeting & Open-Source Routing
- **What he does:** Matches model + reasoning effort to task determinism, watching cost — and escapes frontier pricing via open-source models through one OpenRouter key.
- **Evidence:** `[primary]` "I'm going to use 5.6 soul... medium. I found that your limits will last quite a while if you use medium. This is a straightforward task" / "turn up soul... extra high" for analysis / "You do not need to use a good model for this" for a mechanical API call / "if you're on the $20 per month plan, you might only get a few of these props with this model." Cross-confirmed `[9-skills]`/`[news]`: "frontier AI agents are getting way more expensive, and it's time to token budget... just for those nine prompts, it was around $250... open-source models are getting significantly better... GLM 5.2... use a tool like open router so that you get access to all of the different models... save five times the amount of money."
- **Why non-obvious:** Model choice is a per-task economic decision, not a default — down to routing mechanical work to cheap/open models.

### 8. ★ Skill Chaining / Composability
- **What he does:** Designs skills to compose; output of one becomes input of the next, live.
- **Evidence:** `[primary]` "the goal then is that you use these skills together" — scrape-creators → buffer-publisher (Greg Eisenberg captions), scrape-creators → email-draft (personalized outreach). Co-founder's verdict: "the three, four, five combination is like pretty powerful." Reinforced `[9-skills]` trend 5: the higher skill is *delegation/orchestration* across these.
- **Why non-obvious:** The skills aren't a menu — they're a pipeline he assembles on the fly.

### 9. ★ The Draft-Link Handoff + Approval-Gated Publishing
- **What he does:** Never auto-sends. Every action ends in an editable draft/link he reviews and sends himself; his own product encodes this as doctrine.
- **Evidence:** `[primary]` "it's going to send me back a draft link where I can edit it and send it" / "I did say to create a draft, so it's not actually scheduled" / (batch) "I'm actually not going to send it. That guy seemed like a harmless founder." `[visual]` The Chorus "Riley Brown" agent system prompt: "Produces and stages real marketing assets, while keeping publishing and external changes behind approval." Platform reinforcement `[visual]`: Buffer asks for missing details before scheduling; Gmail fires an AI-content safety banner on the drafted reply.
- **Why non-obvious:** The safety and taste live in the *terminus*, not the prompt. He removes all labor before the send while keeping the judgment human — and codifies it into the agent he ships.

### 10. Batch-the-Inbox (the draft-link, scaled)
- **What he does:** Applies the draft-link pattern across the whole inbox — agent finds everything needing a reply, returns N editable drafts.
- **Evidence:** `[primary]` "I want a draft link for all of these. I don't care how many it is." / "a few days ago I had to respond to like 20 and it just sent me 20 draft links. All of them sound like me." `[visual]` confirms five saved-and-unsent drafts, each following a "declines product, pitches Chorus, asks for feedback" template.
- **Why non-obvious:** Same primitive, linear leverage — reviewing 20 pre-written drafts is a different job than writing 20 emails.

### 11. Zero-Plugin API Bootstrapping
- **What he does:** No official integration? Grab an API key, paste it, tell Codex to build a skill that controls it.
- **Evidence:** `[primary]` "cal.com does not have an official plugin directly inside codeex. But all you have to do... go to cal.com get an API key paste it in and say create a skill that fully controls cow.com and it'll work one minute later." `[visual]` the skill's real name on screen is "Cal.com Control," and the generated link correctly encodes compound constraints (Tue/Thu, Sept–Oct only, 1–5pm, Google Meet, America/New York).
- **Why non-obvious:** The integration surface is "does it have an API," not "does it have a plugin."

### 12. Improvised Multi-Tool Workflow Assembly
- **What he does:** Composes novel pipelines live, reasoning through what each tool ingests/emits.
- **Evidence:** `[primary]` "I'm making this up on the spot... I actually just thought of it on the spot" → "wait, how do we get that on the board? Oh, wait. We can just use firecrawl to scrape and put it on there."
- **Why non-obvious:** Reveals the meta-skill under all the skills: fluid mental modeling of tool I/O so new pipelines assemble on demand.

### 13. Template-Steal Ad Generation (structure-theft, not copy-theft; volume is the goal)
- **What he does:** Scrapes competitors' best statics → Paper board → scrapes his brand (Firecrawl) → regenerates as his own branded ads, mass-producing variations.
- **Evidence:** `[primary]` "we're basically just going to use them as templates for our own ads... You want to experiment a lot with ads... Would we ever do this word for word? We would change it more than this." `[visual]`: the regenerated "Built a $100,000 agent for $50" ads are laid out as a side-by-side A/B batch — but Codex kept the *original competitor's real byline* ("Dr. Fahim Hussain"), swapping only logo/brand copy (see Hidden Knowledge #10).
- **Why non-obvious:** The proven ad's *structure* is the reusable template; brand-swap + image-gen turns one winner into a test batch.

### 14. Teach-by-Demonstration (record-and-replay → skill)
- **What he does:** For any workflow with no clean API, screen-records himself doing it once, and Codex converts the recording into a reusable computer-use skill.
- **Evidence:** `[news]` "you could just tell Codex by using this record and replay skill that you want to show them how to do something... 'Recording is now on. Show me the Typefully draft process'... it automatically enters I'm done recording... it's creating this skill called manual tweet draft... You're allowed to upload up to 30 minutes... they have a really good computer use."
- **Why non-obvious:** Extends skill-creation to the entire GUI surface — anything he can *do* on screen becomes a skill, not just anything with an API. (Bridges to computer-use, `[9-skills]` trend 7.)

### 15. Async Automations — "Act in the Future"
- **What he does:** Turns any successful one-off into a recurring or scheduled automation in natural language, replacing Zapier-style workflow building.
- **Evidence:** `[9-skills]` "Anything that's useful now, you should automatically think to yourself, would this be useful on a recurring basis or... at a very specific time?... AI, because it's just like talking to a human, will just set up the automation" (his "daily best video hook outline every morning at 9am" demo). `[visual]` sidebar shows a real "Create morning episode automation" thread.
- **Why non-obvious:** Collapses the old specialist skill of automation-building into a spoken sentence; the trigger-mindset ("act in the future") is the real technique.

### 16. Agents Live Where You Already Work (cloud agents in iMessage/Slack)
- **What he does:** Beyond computer-side super apps, he deploys always-on cloud agents into the tools his team already uses, addressable like a teammate.
- **Evidence:** `[9-skills]` "I have Claude Code and Codox directly inside Chorus... this is my content agent... Pulling your latest 20 now and building a sponsor-ready page" (iMessage); "@chorus, I need you to do in-depth research on Alex Hormozi... make a little landing page... email it to Ange and Emily" (Slack). `[primary]` "you can immediately add this agent to your iMessage."
- **Why non-obvious:** The distribution insight — agents that live in iMessage/Slack "almost like Wi-Fi... in the background" don't require anyone to learn a new tool, which is his whole Chorus thesis.

---

## Hidden Knowledge

1. **"Just turn it into a skill" hides real generated code.** The `[visual]` layer shows the Foreplay skill is a **4+ file Python pipeline** (`build_dataset.py`, `enrich_analysis.py`, `make_contact_sheets.py`, +1) writing `selected_ads.csv` / `selected_ads_enriched.json` that Codex reads back into Notion and Paper. The breezy "just say turn it into a skill" framing conceals that Codex is writing/maintaining actual code and AGENTS.md memory under the hood. *Deployable takeaway: a skill = named instructions that may spawn a real code pipeline; treat it as software, read what it wrote (see #2).*

2. **Read the skill the agent wrote for itself.** Skills drift. Riley curates by telling the agent to update the skill file after a correction. The visual palette confirms the persistence mechanism (`New workflow`, `Memory → AGENTS.md`). *Takeaway: after any skill is auto-created, open it — the value is a named, inspectable file, not a black box.*

3. **Taste is the non-delegable input.** The deepest layer under the exemplar doctrine: he can only delegate well what he can *judge* well. `[9-skills]` "understanding what good looks like... you need to become an industry expert... I'm really good at creating content. That's kind of my superpower... If you asked me to create a discounted cash flow analysis... I would not be good at delegating... because I don't know what a good DCF analysis looks like." Everything else in the system serves a human who knows good from bad.

4. **Every skill sits on a paid API/connector he glosses over.** ScrapeCreators, Foreplay, Firecrawl, Buffer, Typefully, Cal.com, Gmail, Paper (MCP). Real setup: sign up → API key → paste → "create a skill that controls X." Budget for keys before replicating.

5. **Frontier cost is brutal; open-source is the escape hatch.** `[news]` "$250" for nine Fable prompts via API; his medium-by-default habit and GLM-5.2-via-OpenRouter routing are cost management disguised as preference. On the $20 plan, extra-high buys only a few runs.

6. **MCP vs. raw-API vs. computer-use is a deliberate three-way choice.** Paper via MCP; Cal.com/others wrapped over REST; and when neither exists, `[news]`/`[9-skills]` he falls back to **computer use / record-and-replay** ("not every task... has a perfect plugin"). He picks the integration path per tool.

7. **Notion databases are disposable scaffolding.** `[primary]` "put the notion database just in the archive right now. This is just for testing purposes." The durable deliverable is the skill; the DB is a throwaway staging surface. `[visual]` even shows the reusable schema (Ad / CTA / Competitor) — clean, but still staging.

8. **Human review is load-bearing, and platforms enforce it too.** Nothing auto-sends. `[visual]` surfaces guardrails the audio never mentions: Gmail's gold AI-content banner ("this AI-generated content... hasn't been checked for accuracy"), Buffer refusing to schedule until channel/caption/image are resolved, Typefully's 512MB upload cap ("I need to upgrade... video was just too big"). The friction is real and he designs around it with the draft terminus.

9. **The content-verification gap is the master key.** Code is verifiable, content isn't — that single asymmetry explains why he invests in exemplar retrieval + taste rather than prompt craft. Internalize one thing, it's this.

10. **Legal/ethical blind spot he doesn't flag: the rebrand kept a real person's name.** `[visual]` the regenerated Chorus ad retained the competitor ad's actual byline "Dr. Fahim Hussain," swapping only the logo/brand. Using a real (or real-adjacent) named person as an ad template is a risk he never surfaces — a place to *improve* on his method, not copy it.

11. **Parallelism/async is assumed baseline.** `[9-skills]` "you can talk to many agents in parallel" (command-N multitasking), plus always-on cloud agents and scheduled automations. Long-running background work is default, not a feature reveal.

12. **"Anything public on the internet, Codex can scour."** `[primary]` He offloads research (best contact email, competitor ad libraries, brand asset pages, `[9-skills]` competitor YouTube analysis) to the agent as a reflex — the open web is a queryable input.

13. **Foundational skills > tools, because tools churn.** `[9-skills]` "most of that stuff will change over the next year and likely will become irrelevant... what actually matters is... the foundations that you have as a person" — communication, delegation, taste, mental clarity, multitasking. "If you're a good manager of people, you're going to become a good manager of agents." The skill library is downstream of these.

---

## Hall of Fame Exemplars

### Exemplar 1: Scrape-Creator → Compile-to-Skill → Write-in-Voice (the flagship)
- **Context:** Riley wants to write in Kallaway's style on demand, live, in three prompts.
- **The Example (verbatim, in order):**
  1. *Scrape:* "Please find the creator Callaway on Instagram... Get his best 10 videos from the past few months and I want the transcript and the raw videos and I want them put into a new notion database... And then I also want you to tell me why he's such an effective short form creator." Model: "5.6 soul... medium... straightforward task." (~2–3 min; `[visual]` confirms the read-back "10 source videos are now downloaded locally and the 10 transcripts succeeded.")
  2. *Compile:* "find the top 10 videos that has the most engagement that are not sponsored... turn all of the his top performing videos into a skill. Call it Callaway top performing." Agent pages back to 2023, excludes sponsored posts with retained exclusion evidence, writes the skill.
  3. *Deploy:* (new chat) "Callaway top performing — I want to create a script on the JSpace news by Anthropic... Callaway does a great job explaining things simply while also making it seem urgent and cool. Please create a script for this. Write three options in his voice."
- **The output (verbatim):** "Anthropic just found a hidden workspace inside Claude's brain... And the weirdest part is nobody programmed it. They call it JSpace." Riley: "actually so good... This is exactly in his tone."
- **What makes this excellent:** The whole doctrine in one run — scrape verified winners, filter fakes (with audit trail), freeze as a named callable, deploy on a *new* topic in-voice — producing a deploy-ready hook, not a description of one.

### Exemplar 2: Ad-Spy → Paper Board → Firecrawl Brand → Image-Gen Ad Factory (improvised)
- **Context:** Scrape competitors' longest-running ads, then invent a pipeline live to convert them into own-branded ads.
- **The Example (verbatim fragments):**
  1. *Spy:* "please scrape the longest running ads from my competitors which are quad.ai perplexity and chatgpt and replet... add a little text field... your thoughts on why their ads are doing well... top five video ads from each one and the top five static ads... videos in English only." Mid-run escalation: "I'm going to stop it real quick... turn up soul... extra high... keep going." (Ran 10 min.) `[visual]`: this skill is the real `foreplay-competition/*.py` pipeline; Notion schema = Ad / CTA / Competitor; the agent labels "why it works" as *inference from durability, not ROAS proof.*
  2. *Board:* "please take all the static ads and put it on my open paper app right now" (Paper MCP). `[visual]`: board "Static ad swipe file," grouped by competitor, badge "20 running ads," done in 3m 30s.
  3. *Brand scrape:* "use the firecrawl and I want you to go to chorus.com... scrape all of that whole page... put it on the paper board right next to this... take all the individual assets from the page and put that in a different frame." `[visual]`: pixel-faithful landing page + asset library (logo, wordmark, icon, "10" stat).
  4. *Regenerate:* "replace the replet formatting with an ad that is for chorus. Use good copywriting" → then targeted variant: "Keep the guy the same and the background the same... have it say chorus instead of replet... say 'Built a $100,000 agent for $50'... Change nothing else except the colors to match the chorus brand."
- **The output:** "Built a $100,000 agent for $50. Built with Chorus" — same layout as the stolen template, laid out as a side-by-side A/B batch.
- **What makes this excellent:** The template-steal doctrine in full (proven structure + brand-swap + volume) assembled from four tools wired together on the spot, with honest self-critique ("we would change it more than this") — and a visible trap to avoid (kept a real byline).

### Exemplar 3: Batch Email — Decline-and-Pitch at Scale
- **Context:** Two months of "want to try our product?" pitches → N branded rejections that boomerang into his own pitch.
- **The Example (verbatim):** "find all of the emails over the last two months where people have offered me a product... politely and with a little bit of pizzazz say Decline... but then say, do you want to try our product? And give them a link... I want a draft link for all of these. I don't care how many it is."
- **The output (verbatim draft):** "Talia looks sharp, but I'm going to pass on trying it for now. That said, plot twist — want to try our product instead?" Five saved-and-unsent drafts (`[visual]`); Riley selectively sends ("I'm actually not going to send it. That guy seemed like a harmless founder").
- **What makes this excellent:** Maximal leverage on the draft-link primitive — one prompt, N voice-matched drafts, human taste applied only at the send decision.

### Exemplar 4: Screen-Record → Skill (record-and-replay)
- **Context:** `[news]` No clean way to script a Typefully draft, so he teaches Codex by demonstration.
- **The Example (verbatim):** "Please make a skill called manual tweet draft... 'Recording is now on. Show me the Typefully draft process.'" He performs the steps (new tab → typefully.com → switch to Riley Brown → type draft → upload image), hits stop; Codex auto-detects completion and builds the skill. Later: "manual tweet draft — Hey, can you please upload the latest video to Typefully as a draft? It's in my downloads."
- **The output:** A computer-use skill that drives Comet to create the draft (it hit Typefully's 512MB cap on the real upload — an honest failure kept in the video).
- **What makes this excellent:** Proves skill-creation extends to the entire GUI, not just API-having tools — "I recorded my screen and I taught Codex... and then I immediately turn into a skill." The kept-in failure models honest capability boundaries.

### Exemplar 5 (bonus): Cal.com Constraint-Encoded Booking Link
- **Context:** Booking a high-value guest who needs a constrained window.
- **The Example (verbatim):** "the only days that should be available are in September and October... stick with this Tuesday, Thursday schedule... create a document... write the intro... draft an email for me with that Cal AI link."
- **The output:** `[visual]` a live Cal.com page — Tuesdays only, September, 1–5pm slots, Google Meet auto-attached, America/New York — plus a ready outreach draft.
- **What makes this excellent:** Zero-plugin API bootstrap producing a real asset that correctly parses compound constraints from one natural-language prompt.

### Anti-Exemplar: The Naive Marketing Agent
- **What mediocre looks like:** Prompt-engineering a voice from scratch; scraping raw top engagement without excluding sponsored; presenting durability as *proof* of ROAS; auto-sending/auto-scheduling with no review terminus; cloning a competitor ad word-for-word (or leaving its real byline in); treating each task as a fresh prompt instead of a saved skill; leaving corrections in chat where they evaporate; delegating work in a domain where you can't judge good from bad.
- **Why it fails:** Ignores the verification gap, poisons the pattern set, overclaims epistemically, removes the human safety/taste terminus, courts legal risk, never compounds, and delegates blind. Riley's system inverts every one.

---

## Signature Moves

- **"Turn it into a skill."** After any successful run, name it and freeze it (`New workflow`/AGENTS.md). → **Deploy when:** the task will recur. *Evidence: `[primary]`/`[9-skills]`/`[news]` — all three videos.*
- **Record-and-replay to teach.** Screen-record a GUI workflow once; Codex converts it to a computer-use skill. → **Deploy when:** the tool has no clean API/plugin. *Evidence: `[news]` "Show me the Typefully draft process."*
- **Describe, don't hack.** Speak plainly what you want; skip "act as," @-mentions, and parameter tricks. → **Deploy when:** always, on modern agents. *Evidence: `[9-skills]` "the only enduring prompt hack is describing what you want."*
- **Voice-dictate the long prompt.** Whisper Flow instead of typing. → **Deploy when:** the instruction is long/exploratory. *Evidence: `[primary]` "I'm just going to use Whisper Flow."*
- **Fire-and-multitask across parallel threads.** Fire a task, command-N the next, return when done. → **Deploy when:** tasks run minutes. *Evidence: `[9-skills]` "you can talk to many agents in parallel."*
- **Mid-run effort escalation.** Stop, raise the reasoning dial, resume with "keep going." → **Deploy when:** you realize a task needs analysis, not retrieval. *Evidence: `[primary]` "turn up soul... extra high."*
- **Downgrade the model for mechanical tasks.** Cheap/open model for API-only actions. → **Deploy when:** "put image, hit API, done." *Evidence: `[primary]` "You do not need to use a good model for this."*
- **Stage in the archive.** Route test outputs to a disposable Notion archive, never production. → **Deploy when:** validating a new skill. *Evidence: `[primary]` "This is just for testing purposes."*
- **Name the skill on creation.** Explicit memorable slash-name = the API. → **Deploy when:** the workflow recurs. *Evidence: `[primary]` "Call it Callaway top performing."*
- **Always demand links back.** Bake "return a link" into the skill for instant review. → **Deploy when:** any skill that creates/edits a doc, draft, folder, post. *Evidence: `[primary]` "it always provides a link."*
- **Scrape with a 'why it works' column.** Collect *and* analyze (flagged as inference). → **Deploy when:** the scrape should also teach. *Evidence: `[primary]`/`[visual]`.*
- **Act in the future.** Ask "would this be useful recurring or scheduled?" and make it an automation. → **Deploy when:** a one-off proves useful. *Evidence: `[9-skills]` "act in the future."*

---

## Expert-Specific Quality Rubric

How Riley would judge whether an agentic marketing workflow is good:

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
|---|---|---|---|
| **Example-groundedness** | Prompts a style abstractly | Feeds a few exemplars in-prompt | Agent auto-retrieves verified top-performers from a live scraped skill/DB |
| **Taste / "know what good looks like"** | Delegates in a domain the operator can't judge | Operator can spot-check output | Operator is a domain expert; delegation + judgment are tight |
| **Engagement authenticity** | Uses raw top-engagement | Manually avoids obvious sponsored | Programmatic sponsored-exclusion *with retained evidence* |
| **Epistemic honesty** | Presents inference as proof | Hedges verbally | Output self-labels inference vs. proof ("durability, not ROAS") |
| **Reusability (skill-as-asset)** | One-off prompt, re-explained | Saved template | Named skill/workflow that compounds via written-in corrections |
| **Human-in-loop terminus** | Auto-sends/auto-posts | Confirms before acting | Every action ends in an editable draft/link, publishing behind approval |
| **Model + cost fit** | One model for everything | Bumps model for hard tasks | Per-task effort dial + open-source routing tuned to plan economics |
| **Composability** | Isolated single-tool task | Two tools chained manually | Skills chain fluidly; new pipelines assembled live |
| **Deployability of output** | A draft needing rework | Usable with light edits | Deploy-ready asset that survives Riley reading it aloud |
| **Integration-path fit** | Forces one method | API when available | Right path per tool: MCP / REST / computer-use-via-record-and-replay |
| **Return-and-verify** | No link; must go hunt | Returns a link sometimes | "Always return a link" baked into the skill |

**Riley's minimum bar, in his own verdicts:** an output must survive being read aloud — "actually so good... exactly in his tone." Rejection tells: "fake... not real engagement" (sponsored); "Would we ever do this word for word? We would change it more than this" (lazy cloning); passing the "vibe check" `[news]` (a model that benchmarks well but flops in real use fails). Good enough = deploy-ready and voice-true; excellent = it also self-labels its epistemic status and became a reusable skill.

---

## Methodology (progression)

1. **Diagnose the verification gap.** Content is subjective/unverifiable; build a retrieval layer of verified winners, not a cleverer prompt.
2. **Own the taste.** Only delegate what you can judge; become the domain expert who knows good from bad.
3. **Scrape verified exemplars.** Scraper APIs with authenticity filters (exclude sponsored; longest-running as *flagged-inference* proxy) and a "why it works" field.
4. **Turn it into a skill.** Freeze any successful run as a named skill/workflow (via New workflow / AGENTS.md / record-and-replay); read what it wrote.
5. **Chain skills into pipelines.** Compose live; pick the integration path per tool (MCP / REST / computer-use).
6. **Terminate in a draft/link, publish behind approval.** Never auto-send.
7. **Dial model + effort + open-source per task**, watching plan economics.
8. **Correct into the file; automate the recurring.** Write fixes into the skill so they compound; promote useful one-offs to scheduled automations ("act in the future").

---

## Applied Intelligence

### Capability Unlocks
- **Marketing skill library on scraper APIs** — creators, competitors, tools as callable Antigravity skills.
- **Draft-link/approval operating pattern** — a reusable primitive for any outbound action that keeps taste at the terminus.
- **Three-path integration** — API-key bootstrapping *and* record-and-replay computer-use for tools without plugins.
- **Cost-routing discipline** — per-task effort + open-source (OpenRouter) as a default cost lever.

### Market Signals
- Riley's bet: the marketing bottleneck moved from *generation* to *taste-verified retrieval + orchestration*. Co-founder: "the incremental value from doing marketing is just higher now than it is for engineering." Underserved wedge: **marketing-specific skill packs on paid scraper APIs, shipped as named slash-commands / hireable agents that live in iMessage/Slack.**
- Distribution insight: he ships the skills themselves as the lead magnet ("every single skill... in the description") and an agent-as-product (Chorus). The skill IS the marketing.

### System Enhancements (for Antigravity)
- **Adopt the exclusion-evidence + epistemic-labeling pattern** in any scraping/research skill: retain proof of rejections; have outputs self-label inference vs. proof.
- **Bake "return a link / artifact path" into every producing skill** for instant reviewability.
- **Effort-dial + open-source routing** maps onto Antigravity's model routing / Opus-fallback policy: cheap/open for mechanical, high for cross-data analysis, explicit cost awareness.
- **Draft-terminus + approval as a generalized safety primitive** aligns with existing human-gate patterns (client content, posting gates): produce editable artifact + link, never auto-execute.
- **"Read the skill the agent wrote"** = a governance rule for any auto-generated workflow (it may be a real code pipeline).

## Implementation Pathway
- **24-Hour Quickstart:** Pick one creator. Wire a scraper API. Run the three-prompt pipeline (scrape non-sponsored + "why effective" → turn into a named skill → deploy on a fresh topic, 3 options). Ship one hook.
- **7-Day Sprint:** Add ad-spy (longest-running, inference-labeled) → template-steal one ad via board + brand-scrape. Add the email draft-link skill; batch one inbox sweep. Teach one GUI-only tool via record-and-replay. Bake "return links," "exclude sponsored," and "publish behind approval" into every skill.
- **30-Day Integration:** Full marketing OS — scraped exemplar library (the knowledge layer), connections (Buffer/Typefully, Drive, Cal.com), all recurring asks turned into skills, useful ones promoted to automations, corrections written into files. Route mechanical work to open-source via OpenRouter.

## Cross-Domain Connections
- **Skill Stacking (Antigravity):** Compounds with Nick Saraev (agentic workflows/bottleneck thinking), Mark Kashef (orchestration, silver-platter agentic OS), Rachel Woods (AI operations), Nate B. Jones (agent deployment/orchestration). Riley's scraper-fed *exemplar retrieval + taste* is the missing input layer those orchestration skills assume. Pair the creator-to-skill compiler with any voice expert (Lara Acosta, Nicolas Cole) to auto-source their exemplar sets.
- **Domain Transfer:** The examples-over-instructions doctrine + draft-link terminus generalizes to any subjective-output, hard-to-verify domain (sales, recruiting, PR, design briefs). The longest-running-ad heuristic transfers to any "no internal data, but persistence is public" signal (evergreen SEO pages, repeat sponsorships).
- **Revenue Applications:** (1) Sell marketing skill packs as installable slash-commands. (2) Ghostwriting-at-scale: creator-to-skill + batch draft-links as a service. (3) Ad-factory service: ad-spy → template-steal → variation batches, priced per test volume. (4) Agent-as-product living in iMessage/Slack (his Chorus play).

---

## Expert Operating System (Deep Tier — AGENT.md-ready)

```markdown
# Riley Brown — Agent Configuration

## Identity
- **Who You Are:** An AI-native founder who runs a startup's marketing inside a coding agent (Codex) wired to scraper APIs, MCPs, and computer-use. You build named, reusable skills — not one-off prompts — and you supply taste. You are fast, cost-aware, and you never auto-send.
- **Core Philosophy:** AI can't verify content quality the way it verifies code, so the job is feeding the agent verified examples on demand, judging output with real taste, and freezing every capability into a skill that compounds.
- **Signature Advantage:** You productize creators, competitors, and tools into callable skills (scrape/refine/record → name → chain), route model+cost per task, and terminate every action in a human-editable draft behind approval.

## Expertise Architecture
- Core capabilities (ranked): (1) exemplar-retrieval design via scraper APIs; (2) skill-creation-by-doing (compile/refine/record); (3) competitor ad-spy by longest-running heuristic (inference-labeled); (4) template-steal ad generation across chained tools; (5) draft-link outbound ops at scale; (6) async automations + cloud agents in iMessage/Slack.
- Unconscious competence: fluid tool-I/O modeling; per-task model+effort+open-source routing; disposable-scaffolding instinct (Notion DB = staging, skill = asset); taste as the delegation gate.
- Mental models: verification gap; examples/describe > instructions; sponsored = fake engagement; duration = free (flagged) ROAS proxy; skills are living files that self-assemble; foundations > tools.

## Execution Standards
- SOP: diagnose → own the taste → scrape verified exemplars (exclusion evidence + inference labels) → turn into a named skill → chain (right integration path per tool) → draft-link terminus behind approval → correct into the file → automate the recurring.
- Quality self-check: Would this survive being read aloud? Authentic engagement? Inference labeled as inference? Editable draft/link, not a send? Reusable named skill? Right model+cost? Can I actually judge this domain?
- Non-negotiables: never auto-send; always return a link/path; exclude sponsored; name every recurring skill; read the skill the agent wrote; write corrections into it.

## Voice & Style
- Communication DNA: fast, casual, hands-on demo energy. Fires tasks and multitasks ("fire this off"). Reacts honestly ("actually so good"; "fake... not real engagement"). Marks improvisation openly ("I'm making this up on the spot"). Cost-transparent ("$250 for nine prompts"; "$20 plan... only a few"). Trend-literate, vibe-check pragmatic.
- Adapts: high effort + analysis narration for cross-data tasks; terse cheap/open-model handling for mechanical calls; record-and-replay when no API exists.

## Skill Integration
- Compounds with: agentic-workflow/orchestration skills (Saraev, Kashef, Nate B. Jones), AI-operations (Rachel Woods), and any voice/ghostwriting expert (feed their exemplar sets via the creator-to-skill compiler).
- Deployment scenarios: marketing skill packs as slash-commands; ghostwriting/outreach at scale; competitor ad-factory service; agent-as-product in iMessage/Slack.
```

---

## Direct Quotes Bank

*(15–25 verbatim quotes worth preserving; source-tagged, with context)*

1. `[primary]` "I run my entire startup inside Codeex and I use GBT 5.6... to do basically everything." — thesis / cold open.
2. `[primary]` "with coding, it's very easy to verify whether something is good or something is bad... Whereas content, it's subjective." — the verification gap (master key).
3. `[primary]` "over the last 3 years, even though AI's gotten so much smarter, it hasn't gotten any better at writing content." — why prompting isn't the fix.
4. `[primary]` "the only thing you need to do in order to create really good content is provide really good examples." — the doctrine, one line.
5. `[primary]` "we're giving a database or an API to the AI agent so that whenever it needs to create content like someone, it can just go find good examples." — retrieval layer.
6. `[primary]` "turn all of the his top performing videos into a skill. Call it Callaway top performing... so that I can write content in his style at any time." — creator-to-skill.
7. `[primary]` "this is all that is is just a file with those transcripts that we scraped." — skills are just files (the demystifier).
8. `[primary]` "I'll retain the exclusion evidence for every rejected sponsor/promotional post... those can be boosted. So it's like fake." — authenticity filter.
9. `[primary]` "the one metric that we can use... as a proxy for that is how long they've been running it. If you run an ad for nine months... presumably they're spending a lot of money keeping it alive for a good reason." — longest-running heuristic.
10. `[visual]` "'Why it works' is clearly labeled as an inference from creative durability — not proof of ROAS or profitability." — Codex's own epistemic honesty.
11. `[primary]` "I found that your limits will last quite a while if you use medium. This is a straightforward task." — effort-dialing.
12. `[primary]` "if you're on the $20 per month plan, you might only get a few of these props with this model." — cost reality.
13. `[primary]` "cal.com does not have an official plugin... get an API key paste it in and say create a skill that fully controls cow.com and it'll work one minute later." — zero-plugin bootstrapping.
14. `[primary]` "it's going to send me back a draft link where I can edit it and send it." — draft-link terminus.
15. `[primary]` "I want a draft link for all of these. I don't care how many it is." — batch-the-inbox.
16. `[primary]` "Would we ever do this word for word? We would change it more than this." — structure-theft, not copy-theft.
17. `[primary]` "please update the email draft skills so that you never say this or that... so you get it in its context." — correction written into the file.
18. `[9-skills]` "he who can describe what they want the best will inherit the world... the only enduring prompt hack is describing what you want." — describe, don't hack.
19. `[9-skills]` "I will tell the agent to do a thing, then... to make the thing better and then I'll just tell it to turn it into a skill." — skill-creation-by-doing.
20. `[9-skills]` "your skills will auto update... the future of AI agents is just auto updating skills depending on how you interact with it." — self-assembling skills.
21. `[9-skills]` "you need to become an industry expert... I understand what good looks like." — taste as the non-delegable input.
22. `[9-skills]` "If you're a good manager of people, you're going to become a good manager of agents." — foundations > tools.
23. `[9-skills]` "just for those nine prompts, it was around $250." — frontier cost / token budgeting.
24. `[news]` "I recorded my screen and I taught Codex how to use Comet... and then I immediately turn into a skill." — record-and-replay.
25. `[news]` "this model... does not pass the vibe check... this was not one of those times." — the vibe-check standard for evaluating models.

---

## Usage Note
Extraction performed per `directives/mes-3.0-extract.md`, Deep tier (forced), rev. 2 after corpus correction. All sources are verified Riley Brown; the earlier non-Riley corpus files are quarantined and unused. Cross-video-confirmed patterns marked ★. Visual-layer readings tagged `[visual]` are OCR ground truth and override the audio where they conflict. Inferences marked inline. Fidelity: high across all three videos and the visual layer.
