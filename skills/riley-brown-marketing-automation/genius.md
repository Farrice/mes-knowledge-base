# Genius: Riley Brown — Agentic Marketing Operations

**Source (all verified Riley Brown, @rileybrownai / "Agent Native"):**
- **Primary** — "Codex Is Basically Running My Company Now" (2026-07-21, 36:44), Riley + co-founder Vashall, nine live marketing workflows in Codex. Full transcript + 100-frame visual layer.
- **Corpus 1** — "9 AI Agent Skills To Get Ahead of 99% of People."
- **Corpus 2** — "AI Agents Just Changed Forever: GLM 5.2, Codex Skills, Claude & Cursor" (record-and-replay, open-source routing).

Full extraction: `extractions/riley-brown/mes-extraction.md`. Verbatim quote bank + claims ledger: `references/source-quotes.md`. Every quote below is source-tagged `[primary]` / `[9-skills]` / `[news]` / `[visual]`. Visual-layer readings are OCR ground truth and override the audio where they conflict. Transcripts are auto-captioned — spellings preserved ("Callaway"=Kallaway, "soul"=the reasoning-effort dial, "quad.ai"=Claude, "Fable/Mythos"=frontier models as spoken).

> **The one truth.** Riley doesn't prompt an agent to *be* good at marketing — he builds it a **retrieval layer of great examples**, freezes each capability into a **named, reusable skill**, and supplies the one thing the agent can't: **taste — knowing what good looks like.** Every high-stakes action terminates in a human-editable draft/link behind approval. `[primary]` "the only thing you need to do in order to create really good content is provide really good examples."

**His distinct wedge** (vs. Saraev / Kashef / Rachel Woods / Nate B. Jones orchestration skills): marketing-specific skill libraries built on scraper APIs, where the durable asset is a *named, reusable skill* — not a one-off automation — and taste is the load-bearing human input. He is the operations tier the roster lacks: distribution, scheduling, inbox, file hygiene — the unglamorous layer that makes the content tier compound.

---

## Genius Patterns (16 — ★ = confirmed across 2+ Riley videos)

### 1. ★ Examples-Over-Instructions Doctrine (twin: "describe, don't hack")
Refuses to solve content quality by prompting harder. Engineers *retrieval of exemplars* and leans on plain description. `[primary]` "with coding, it's very easy to verify whether something is good or bad... Whereas content, it's subjective... over the last 3 years... it hasn't gotten any better at writing content... So the only thing you need to do... is provide really good examples... we're giving a database or an API to the AI agent so that whenever it needs to create content like someone, it can just go find good examples." Cross-confirmed `[9-skills]`: "he who can describe what they want the best will inherit the world... the only enduring prompt hack is describing what you want."
**Non-obvious:** diagnoses the bottleneck as *verification*, not generation — routes around it with retrieval + description, not prompt tricks. This thesis underwrites the entire toolkit.

### 2. ★ Skill-Creation-by-Doing ("turn it into a skill")
Never hand-writes skill files. Runs the task live, refines the output, then freezes it as a named skill — and the mechanism is a first-class Codex command. Three independent demos: `[primary]` "turn all of the his top performing videos into a skill. Call it Callaway top performing." `[9-skills]` "I'll tell the agent to do a thing, then... make the thing better and then I'll just tell it to turn it into a skill." `[news]` "I recorded my screen and I taught Codex how to use Comet... and then I immediately turn into a skill." Grounded `[visual]`: Codex's slash-command palette ships **"New workflow — Save this task as a new workflow"** and **"Memory — Create an AGENTS.md file... for Codex."**
**Non-obvious:** the durable asset is the *skill*, born from a successful run — three creation paths (compile-from-scrape / refine-a-task / record-a-screen) all land in a named, callable file.

### 3. ★ Skills Self-Assemble and Auto-Update (correction written into the file)
Treats skills as living files that ratchet toward his taste. `[primary]` "please update the email draft skills so that you never say this or that... so you get it in its context." `[9-skills]` "your skills will auto update... the future of AI agents is just auto updating skills depending on how you interact with it."
**Non-obvious:** corrections are written *into the asset*, so they compound.

### 4. Creator-to-Skill Compiler
Scrapes a creator's top-performing (non-sponsored) content and freezes it into a named voice-writing skill. `[primary]` "so that I can write content in his style at any time... this is all that is is just a file with those transcripts that we scraped. But the point is I didn't have to go fetch the information." Output (verbatim): "Anthropic just found a hidden workspace inside Claude's brain... nobody programmed it. They call it JSpace." Riley: "actually so good... This is exactly in his tone."
**Non-obvious:** productizes *another person's style* as a permanent callable; the name ("Callaway top performing") is the API into their voice.

### 5. Engagement-Authenticity Filter
Excludes sponsored posts (bought engagement) from the exemplar set and keeps evidence of every exclusion. `[primary]` "the top 10 videos that has the most engagement that are not sponsored." Agent log: "I'll retain the exclusion evidence for every rejected sponsor/promotional post... those can be boosted. So it's like fake."
**Non-obvious:** boosted posts poison the pattern set — he builds the filter *plus an audit trail* into the skill.

### 6. Longest-Running-Ad Heuristic (an *explicitly-flagged* ROAS proxy)
Can't see competitors' ROAS, so uses ad *duration* as a public proxy — and the agent labels this as inference, not proof. `[primary]` "the one metric we can use... as a proxy is how long they've been running it. If you run an ad for nine months... presumably they're spending a lot of money keeping it alive for a good reason." `[visual]` Codex output: "'Why it works' is clearly labeled as an inference from creative durability — not proof of ROAS or profitability."
**Non-obvious:** turns a data limit into a free selection signal *and* preserves epistemic honesty.

### 7. ★ Effort-Dialing, Token-Budgeting & Open-Source Routing
Matches model + reasoning effort to task determinism, watching cost. `[primary]` "I'm going to use 5.6 soul... medium... your limits will last quite a while if you use medium. This is a straightforward task" / "turn up soul... extra high" for analysis / "You do not need to use a good model for this" for a mechanical API call / "if you're on the $20 per month plan, you might only get a few of these." `[9-skills]`/`[news]` "just for those nine prompts, it was around $250... open-source models are getting significantly better... GLM 5.2... use a tool like open router... save five times the amount of money."
**Non-obvious:** model choice is a per-task economic decision, not a default.

### 8. ★ Skill Chaining / Composability
Designs skills to compose; output of one becomes input of the next, live. `[primary]` "the goal then is that you use these skills together" — scrape-creators → buffer-publisher (borrowed captions), scrape-creators → email-draft. Co-founder: "the three, four, five combination is like pretty powerful."
**Non-obvious:** the skills aren't a menu — they're a pipeline assembled on the fly.

### 9. ★ Draft-Link Handoff + Approval-Gated Publishing
Never auto-sends. Every action ends in an editable draft/link he reviews and sends himself. `[primary]` "it's going to send me back a draft link where I can edit it and send it" / "I did say to create a draft, so it's not actually scheduled." `[visual]` The Chorus "Riley Brown" agent system prompt: "Produces and stages real marketing assets, while keeping publishing and external changes behind approval." Platform-reinforced `[visual]`: Gmail's AI-content banner, Buffer refusing to schedule until channel/caption/image resolve.
**Non-obvious:** safety and taste live in the *terminus*, not the prompt. He removes all labor before the send while keeping the judgment human.

### 10. Batch-the-Inbox (the draft-link, scaled)
Applies the draft-link pattern across the whole inbox. `[primary]` "I want a draft link for all of these. I don't care how many it is." / "a few days ago I had to respond to like 20 and it just sent me 20 draft links. All of them sound like me." Riley's own verdict: this one "is actually the most useful."
**Non-obvious:** reviewing 20 pre-written drafts is a different job than writing 20 emails.

### 11. Zero-Plugin API Bootstrapping
No official integration? Grab an API key, paste it, tell the agent to build a skill that controls it. `[primary]` "cal.com does not have an official plugin... get an API key paste it in and say create a skill that fully controls cal.com and it'll work one minute later." `[visual]` skill name on screen: "Cal.com Control"; the generated link correctly encodes compound constraints (Tue/Thu, Sept–Oct, 1–5pm, Google Meet, America/New York).
**Non-obvious:** the integration surface is "does it have an API," not "does it have a plugin."

### 12. Improvised Multi-Tool Workflow Assembly
Composes novel pipelines live, reasoning through what each tool ingests/emits. `[primary]` "I'm making this up on the spot... wait, how do we get that on the board? Oh, we can just use firecrawl to scrape and put it on there."
**Non-obvious:** the meta-skill under all the skills — fluid mental modeling of tool I/O.

### 13. Template-Steal Ad Generation (structure-theft, not copy-theft; volume is the goal)
Scrapes competitors' best statics → board → scrapes his brand → regenerates as own branded ads, mass-producing variations. `[primary]` "we're basically just going to use them as templates for our own ads... You want to experiment a lot with ads... Would we ever do this word for word? We would change it more than this." `[visual]`: the regenerated "Built a $100,000 agent for $50" ads laid out as an A/B batch.
**Non-obvious:** the proven ad's *structure* is the reusable template. **Named failure to avoid** (Hidden #10): Codex kept the competitor's real byline "Dr. Fahim Hussain" in the rebrand — never carry a real name/likeness into a template-steal.

### 14. Teach-by-Demonstration (record-and-replay → skill)
For any workflow with no clean API, screen-records himself doing it once; Codex converts the recording into a reusable computer-use skill. `[news]` "'Recording is now on. Show me the Typefully draft process'... it's creating this skill called manual tweet draft... You're allowed to upload up to 30 minutes... they have a really good computer use."
**Non-obvious:** extends skill-creation to the entire GUI surface — anything he can *do* becomes a skill.

### 15. ★ Async Automations — "Act in the Future"
Turns any successful one-off into a recurring or scheduled automation in natural language, replacing Zapier-style building. `[9-skills]` "Anything useful now, ask yourself, would this be useful on a recurring basis or at a specific time?... AI, because it's just like talking to a human, will just set up the automation" (his "daily best video hook outline every morning at 9am" demo). `[visual]` sidebar: a real "Create morning episode automation" thread.
**Non-obvious:** collapses the specialist skill of automation-building into a spoken sentence; the trigger-mindset is the technique.

### 16. Agents Live Where You Already Work (cloud agents in iMessage/Slack)
Deploys always-on cloud agents into the tools his team already uses, addressable like a teammate. `[9-skills]` "@chorus, I need you to do in-depth research on Alex Hormozi... make a little landing page... email it to Ange and Emily" (Slack). `[primary]` "you can immediately add this agent to your iMessage."
**Non-obvious:** the distribution insight — agents in iMessage/Slack "almost like Wi-Fi... in the background" require nobody to learn a new tool.

---

## Hidden Knowledge (13 tacit insights)

1. **"Just turn it into a skill" hides real generated code.** `[visual]` the Foreplay skill is a 4+ file Python pipeline (`build_dataset.py`, `enrich_analysis.py`, `make_contact_sheets.py`, +1) writing `selected_ads.csv` / `selected_ads_enriched.json`. Treat a skill as software — read what it wrote.
2. **Read the skill the agent wrote for itself.** Skills drift; curate by telling the agent to update the file after a correction. Persistence mechanism confirmed on screen (`New workflow`, `Memory → AGENTS.md`).
3. **Taste is the non-delegable input.** `[9-skills]` "understanding what good looks like... I'm really good at creating content... If you asked me to create a discounted cash flow analysis... I would not be good at delegating... because I don't know what a good DCF analysis looks like." You can only delegate well what you can judge well.
4. **Every skill sits on a paid API/connector he glosses over.** ScrapeCreators, Foreplay, Firecrawl, Buffer, Typefully, Cal.com, Gmail, Paper (MCP). *Our build routes around every one of these — see `references/api-integration-guide.md` for the his-stack-vs-ours map.*
5. **Frontier cost is brutal; open-source is the escape hatch.** `[news]` "$250" for nine Fable prompts via API; medium-by-default + GLM-via-OpenRouter is cost management disguised as preference.
6. **MCP vs. raw-API vs. computer-use is a deliberate three-way choice** — picked per tool. When neither MCP nor REST exists, fall back to record-and-replay computer-use.
7. **Notion databases are disposable scaffolding.** `[primary]` "put the notion database just in the archive right now. This is just for testing purposes." The durable deliverable is the skill; the DB is staging.
8. **Human review is load-bearing, and platforms enforce it too.** `[visual]` guardrails the audio never mentions: Gmail's gold AI-content banner ("hasn't been checked for accuracy"), Buffer refusing to schedule until channel/caption/image resolve, Typefully's 512MB upload cap.
9. **The content-verification gap is the master key.** Code is verifiable, content isn't — that single asymmetry explains everything. Internalize one thing, it's this.
10. **Legal/ethical blind spot he doesn't flag: the rebrand kept a real person's name** ("Dr. Fahim Hussain"). A place to *improve* on his method, not copy it — our `/creative-from-winners` gate bans byline carryover.
11. **Parallelism/async is assumed baseline.** `[9-skills]` "you can talk to many agents in parallel" (command-N), always-on cloud agents, scheduled automations.
12. **"Anything public on the internet, Codex can scour."** He offloads research (best contact email, competitor ad libraries, brand pages) to the agent as a reflex.
13. **Foundational skills > tools, because tools churn.** `[9-skills]` "most of that stuff will change over the next year... what actually matters is the foundations you have as a person — communication, delegation, taste, mental clarity, multitasking. If you're a good manager of people, you're going to become a good manager of agents."

---

## Hall of Fame Exemplars (verbatim — this is the material that makes the skill usable)

### Exemplar 1 — Scrape-Creator → Compile-to-Skill → Write-in-Voice (the flagship)
Three prompts, live, in-voice on a fresh topic:
1. *Scrape:* `[primary]` "Please find the creator Callaway on Instagram... Get his best 10 videos from the past few months and I want the transcript and the raw videos and I want them put into a new notion database... And then I also want you to tell me why he's such an effective short form creator." Model: "5.6 soul... medium... straightforward task." `[visual]` read-back: "10 source videos are now downloaded locally and the 10 transcripts succeeded."
2. *Compile:* "find the top 10 videos that has the most engagement that are not sponsored... turn all of the his top performing videos into a skill. Call it Callaway top performing." (Agent excludes sponsored with retained exclusion evidence, writes the skill.)
3. *Deploy (new chat):* "Callaway top performing — I want to create a script on the JSpace news by Anthropic... Callaway does a great job explaining things simply while also making it seem urgent and cool. Please create a script for this. Write three options in his voice."
**Output (verbatim):** "Anthropic just found a hidden workspace inside Claude's brain... the weirdest part is nobody programmed it. They call it JSpace." Riley: "actually so good... This is exactly in his tone."
**Why excellent:** the whole doctrine in one run — scrape verified winners, filter fakes (with audit trail), freeze as a named callable, deploy on a *new* topic in-voice — producing a deploy-ready hook, not a description of one.

### Exemplar 2 — Ad-Spy → Board → Brand-Scrape → Image-Gen Ad Factory (improvised)
1. *Spy:* "please scrape the longest running ads from my competitors which are quad.ai perplexity and chatgpt and replet... add a little text field... your thoughts on why their ads are doing well... top five video ads from each one and the top five static ads... videos in English only." Mid-run: "I'm going to stop it real quick... turn up soul... extra high... keep going." (Ran 10 min.) `[visual]`: Notion schema = Ad / CTA / Competitor; the agent labels "why it works" as *inference from durability, not ROAS proof.*
2. *Board:* "please take all the static ads and put it on my open paper app right now."
3. *Brand scrape:* "use the firecrawl and I want you to go to chorus.com... scrape all of that whole page... take all the individual assets from the page and put that in a different frame."
4. *Regenerate:* "replace the replet formatting with an ad that is for chorus. Use good copywriting" → "Keep the guy the same and the background the same... say 'Built a $100,000 agent for $50'... Change nothing else except the colors to match the chorus brand."
**Output:** "Built a $100,000 agent for $50. Built with Chorus" — same layout as the template, laid out as an A/B batch. Honest self-critique: "Would we ever do this word for word? We would change it more than this."
**Why excellent:** the template-steal doctrine in full, assembled from four tools live — *with a visible trap to avoid* (kept a real byline).

### Exemplar 3 — Batch Email: Decline-and-Pitch at Scale
"find all of the emails over the last two months where people have offered me a product... politely and with a little bit of pizzazz say Decline... but then say, do you want to try our product? And give them a link... I want a draft link for all of these. I don't care how many it is."
**Output (verbatim draft):** "Talia looks sharp, but I'm going to pass on trying it for now. That said, plot twist — want to try our product instead?" Five saved-and-unsent drafts `[visual]`; Riley selectively sends: "I'm actually not going to send it. That guy seemed like a harmless founder."
**Why excellent:** maximal leverage on the draft-link primitive — one prompt, N voice-matched drafts, human taste applied only at the send decision.

### Exemplar 4 — Screen-Record → Skill (record-and-replay)
`[news]` "Please make a skill called manual tweet draft... 'Recording is now on. Show me the Typefully draft process.'" Performs steps (new tab → typefully.com → switch to Riley Brown → type draft → upload image), hits stop; Codex builds the skill. Later: "manual tweet draft — can you please upload the latest video to Typefully as a draft? It's in my downloads."
**Output:** a computer-use skill that drives the browser (it hit Typefully's 512MB cap on the real upload — an honest failure kept in the video).
**Why excellent:** proves skill-creation extends to the entire GUI, not just API-having tools.

### Exemplar 5 — Cal.com Constraint-Encoded Booking Link
"the only days that should be available are in September and October... stick with this Tuesday, Thursday schedule... create a document... write the intro... draft an email for me with that Cal AI link."
**Output:** `[visual]` a live Cal.com page — Tuesdays only, September, 1–5pm slots, Google Meet auto-attached, America/New York — plus a ready outreach draft.
**Why excellent:** zero-plugin API bootstrap producing a real asset that parses compound constraints from one prompt.

### Anti-Exemplar — The Naive Marketing Agent
Prompt-engineering a voice from scratch; scraping raw top engagement without excluding sponsored; presenting durability as *proof* of ROAS; auto-sending with no review terminus; cloning a competitor ad word-for-word (or leaving its real byline in); treating each task as a fresh prompt instead of a saved skill; leaving corrections in chat where they evaporate; delegating work in a domain where you can't judge good from bad. **Why it fails:** ignores the verification gap, poisons the pattern set, overclaims epistemically, removes the human safety/taste terminus, courts legal risk, never compounds, delegates blind.

---

## Signature Moves (deploy-when triggers)

- **"Turn it into a skill."** After any successful run, name it and freeze it. → the task will recur. *[all three videos]*
- **Record-and-replay to teach.** Screen-record a GUI workflow once. → the tool has no clean API. *[news]*
- **Describe, don't hack.** Speak plainly; skip "act as," @-tricks, parameter hacks. → always, on modern agents. *[9-skills]*
- **Voice-dictate the long prompt.** Whisper Flow instead of typing. → long/exploratory instruction. *[primary]*
- **Fire-and-multitask across parallel threads.** → tasks run minutes. *[9-skills]*
- **Mid-run effort escalation.** Stop, raise the reasoning dial, resume. → you realize it needs analysis, not retrieval. *[primary] "turn up soul... extra high."*
- **Downgrade the model for mechanical tasks.** → "put image, hit API, done." *[primary] "You do not need to use a good model for this."*
- **Stage in the archive.** Route test outputs to disposable staging, never production. → validating a new skill. *[primary]*
- **Name the skill on creation.** The memorable slash-name is the API. → the workflow recurs. *[primary]*
- **Always demand links back.** Bake "return a link" into any producing skill. → any doc/draft/folder/post. *[primary]*
- **Scrape with a 'why it works' column** (flagged as inference). → the scrape should also teach. *[primary]/[visual]*
- **Act in the future.** Ask "would this be useful recurring or scheduled?" → a one-off proves useful. *[9-skills]*

---

## Expert-Specific Quality Rubric (11 criteria — how Riley judges an agentic marketing workflow)

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

**Riley's minimum bar (his own verdicts):** an output must survive being read aloud — "actually so good... exactly in his tone." Rejection tells: "fake... not real engagement" (sponsored); "Would we ever do this word for word? We would change it more than this" (lazy cloning); failing the "vibe check" `[news]`. Good enough = deploy-ready and voice-true; excellent = it also self-labels its epistemic status and became a reusable skill.

---

## Methodology (progression)

1. **Diagnose the verification gap** — build a retrieval layer of verified winners, not a cleverer prompt.
2. **Own the taste** — only delegate what you can judge.
3. **Scrape verified exemplars** — authenticity filters (exclude sponsored; longest-running as *flagged-inference* proxy) + a "why it works" field.
4. **Turn it into a skill** — freeze any successful run as a named skill; read what it wrote.
5. **Chain skills into pipelines** — compose live; pick the integration path per tool.
6. **Terminate in a draft/link, publish behind approval** — never auto-send.
7. **Dial model + effort + open-source per task**, watching plan economics.
8. **Correct into the file; automate the recurring** — write fixes into the skill; promote useful one-offs to scheduled automations.

---

## Anti-Patterns (reject on sight)

- Prompt-engineering a voice from scratch instead of retrieving exemplars — `[9-skills]` "the only enduring prompt hack is describing what you want"; prompt-trick incantations "do basically nothing."
- Scraping raw top-engagement without excluding sponsored/boosted posts — `[primary]` "those can be boosted. So it's like fake... it's not real engagement."
- Presenting ad duration as *proof* of ROAS — `[visual]` his own agent labels "why it works" as "an inference from creative durability — not proof of ROAS or profitability."
- Auto-sending / auto-posting with no editable-draft terminus — `[primary]` "I did say to create a draft, so it's not actually scheduled"; `[visual]` Chorus system prompt: "keeping publishing and external changes behind approval."
- Cloning a competitor ad word-for-word — or carrying its real byline/person into your version — `[primary]` "Would we ever do this word for word? We would change it more than this"; `[visual]` the rebrand that kept "Dr. Fahim Hussain" (2026-07-21 demo).
- Treating each task as a fresh prompt instead of a saved, named skill — `[primary]` "this is all that is is just a file with those transcripts... I didn't have to go fetch the information."
- Leaving corrections in chat where they evaporate — `[primary]` "please update the email draft skills so that you never say this or that... so you get it in its context."
- Delegating work in a domain where you can't tell good from bad (taste is non-delegable — Hidden Knowledge #3).
- Inventing performance numbers the source doesn't expose (Ad Library gives no likes/spend/ROI — leave blank, never fabricate; see source-quotes.md "what the source does NOT establish").
- Treating a "skill" as a black box — `[visual]` the Foreplay skill is a real multi-file pipeline (`build_dataset.py`, `enrich_analysis.py`, `make_contact_sheets.py`); open it and read it.

## Recognition Test

Before shipping any output from this skill, run Riley's own bar: **would Riley Brown recognize this as his?** Read it aloud — does it earn his verbatim verdicts ("actually so good... This is exactly in his tone") or his rejection ("Would we ever do this word for word?")? The output must survive a side-by-side read against real published Riley pieces (blind-pass ledger: `extractions/riley-brown-marketing-automation/blind-pass-log.md`, EVAL-055). If a cold reader could tell which one the machine wrote, it fails.

## Cross-Domain / Revenue (see `references/cross-domain-patterns.md` for the full map)
- Examples-over-instructions + draft-link terminus generalize to any subjective, hard-to-verify domain (sales, recruiting, PR, design briefs).
- Longest-running-ad heuristic transfers to any "no internal data, but persistence is public" signal (evergreen SEO pages, repeat sponsorships).
- Revenue: marketing skill packs as slash-commands; ghostwriting-at-scale via creator-to-skill + batch draft-links; ad-factory service (ad-spy → template-steal → variation batches); agent-as-product living in iMessage/Slack.
