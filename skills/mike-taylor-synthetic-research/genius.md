# Mike Taylor — Unified Genius Context (Synthetic Customer Research)

> Load this before ANY workflow in this skill. This is the thinking, not the terminology.

## Source Thesis

A direct question to a chatbot returns "the stock answer — kind of the average of the internet." It's reasonable, not creative, because a single model instance answering as itself has no reason to surface disagreement. Force the model to generate a **panel of distinct personas first**, let each one answer **independently**, then instruct it to **combine those answers as if the personas had collaborated on one joint anonymous answer** — and the output stops being the average and starts being the range, synthesized. That's the entire mechanism. Everything else in this skill is what makes that mechanism trustworthy enough to act on: how deep to ground it, when to believe the aggregate vs. distrust the individual, and when to stop trusting it at all and go pay for the real $8-12K focus group.

**Provenance**: 1 primary video (33:13, 6,916-word transcript + 20 frames, `extractions/mike-taylor/`), watched not transcript-only. Secondary corroboration (LIKELY band, third-party attribution) from Vexpower/Ask Rally public material. Full claims ledger with VERIFIED/LIKELY labels: `references/source-quotes.md`.

## How to Use This Skill (Model Calibration)

- The panel-then-aggregate move is a **research instrument**, not a copywriting shortcut. Its job is to surface disagreement and directional signal fast, cheap, and before spending real research budget — never to replace real customer contact on a decision that matters. State this boundary in the same breath as any verdict you produce with this method; don't disclaim it once and move on.
- **Ground before you trust.** A cold-generated panel (no real data) and a transcript-grounded panel (real customer calls loaded in) are not the same instrument, even though the prompt shape looks identical. Always state which tier a panel is running at before reporting its verdict as anything more than a directional hunch.
- **Aggregate ≠ individual.** A panel can be highly reliable in the group and completely unreliable naming what one specific person would do. Never let a workflow output collapse this distinction — if a deliverable names a specific individual's predicted behavior, flag it as illustrative, not predictive.
- **Insight, not final copy.** Mike's own discipline: use panel output to find the angle, then write the actual deliverable himself. A workflow that ships the raw persona-aggregate paragraph as finished copy has skipped his last step.
- Texture: casual, demonstrative, generous with the actual artifact ("you guys are free to steal that"), habitually hedges with "directionally correct... I'd love to see if you AB tested it." He narrates live, mid-explanation notices the adjacent business opportunity, and treats every output as disposable/replicable rather than precious IP.

---

## The 17 Genius Patterns

### 1. Roleplay-Then-Aggregate (the core mechanism)
A direct ask gets "the stock answer... it's not very creative." Force persona-diversity BEFORE the answer, aggregation AFTER. "What I found is instead if you ask it to think of a bunch of personas to roleplay as first then you know you get the individual responses from those personas and then you combine that together into a final answer." (~2:43-3:14, VERIFIED) Mechanism: a single model instance answering as "itself" has no structural reason to disagree with itself; forcing N distinct personas to answer independently before synthesis extracts the variance that a single-shot answer collapses.

### 2. The "Joint Anonymous Answer" Aggregation Instruction
The exact closing phrase that makes aggregation work: "as if these people had collaborated in writing a joint anonymous answer." (~4:34-4:38, VERIFIED) Mechanism: this framing tells the model the personas have already reconciled real disagreement into one voice — richer than a plain ask ("you get like the final answer that you would kind of get from ChatGPT except it's got this more rich kind of background and experience and personas backing it up"). Never paraphrase this instruction loosely; the specific "collaborated... joint anonymous answer" framing is load-bearing.

### 3. Two-Step Prompt Architecture: Scene-Set, Then Ask
Never combine persona generation and the real question into one instruction. Step 1: "give me 10 demographic personas just like regular people who would be buyers of [product]." Step 2, separately: "answer this question critically from their experience given their background" — then the actual decision question. (~3:16-3:31, VERIFIED) Skipping the two-step and asking in one breath collapses back toward the stock-answer problem this whole method exists to avoid.

### 4. Product-Category Substitution for Unknown Brands
If the model already knows the brand (HubSpot), name it directly — training data carries brand-specific buyer knowledge. If the brand is obscure, name the **product category** instead: "if your product isn't as well known then you might need to describe what type of product you are... because it's been trained on the entire internet it can know that small business owners quite often buy CRMs." (~5:00-5:08, VERIFIED) Test which regime you're in before writing the prompt.

### 5. Persona List as a Targeting-Discovery Byproduct
The generated persona list is itself a deliverable, independent of the downstream question — it surfaces segments the operator hadn't considered: "I come up with new targeting options... I didn't really think about nonprofits, for example, nonprofit directors, they also need to buy CRM." (~5:23-5:41, VERIFIED) Always report the persona list as a standalone finding, not just scaffolding for the aggregate answer.

### 6. The Grounding Ladder — Three Accuracy Tiers
(LIKELY, TwoSetAI corroboration) **Tier 1**: a pre-built panel of real interviewed people, calibrated (via optimization, e.g. DSPy) until AI responses match real response style and substance — reaches "high 70s to 80%" accuracy. **Tier 2**: custom personas built from uploaded real transcripts — accuracy scales with transcript quality, "consistently outperforms generic personas." **Tier 3**: pure cold-generated personas, no real data — approximately 60% accuracy. Rule: never report a Tier-3 panel's verdict with Tier-1 confidence language. State the tier explicitly in every output.

### 7. The Self-Consistency Ceiling
(LIKELY, TwoSetAI corroboration) "If you gave someone the same survey twice, they won't even agree with themselves 90% of the time." Synthetic research has a hard accuracy ceiling around 85-90% — a **human biological constraint**, not a fixable product limitation. Reframes "why isn't this 100% accurate" as the wrong question; the real benchmark is real-human self-consistency, not perfection.

### 8. Distribution vs. Individual Accuracy Split
At aggregate scale (Ask Rally: ~1,000 personas), group-level predictions reach 80-90% accuracy. Individual persona predictions remain "speculative" and can hallucinate plausible-but-false specifics — a cloned persona "described buying a lightsaber kit at 2 a.m. — it never occurred in real life but was perfectly consistent with the real person's personality." (LIKELY, secondary corroboration; the underlying split itself is also implied VERIFIED in-video — see Pattern 12/13's individual-personalization caveats). Rule: trust panels for aggregate/directional calls, never for a single named individual's literal predicted action.

### 9. The Sycophancy/Bias Trap
(LIKELY, TwoSetAI corroboration) Ungrounded LLM personas skew toward politeness: "It will always tell you your ideas are great." An unguarded simulation had personas vote 90% for the "most polite candidate" and prefer *La La Land* over *Transformers* despite real box-office reality. Correction: adversarial framing or real grounding data — the same failure mode Geoff Woods' Pattern 8 (anti-sycophancy) names independently. A suspiciously unanimous or flattering panel result is itself a diagnostic signal, not a clean verdict.

### 10. The "Vegan Problem" — Thread Contamination
(LIKELY, TwoSetAI corroboration) When multiple personas answer inside ONE shared conversation thread, their traits drift toward each other as the exchange continues. Fix: isolate each persona generation in a separate thread/context; merge only at the aggregation step, never let personas "see" each other's answers while forming their own.

### 11. Real-Transcript Roleplay — the Voice-of-Customer Engine
Record every customer call (Grain/Granola/Zoom), load transcripts into a RAG-capable tool (NotebookLM in his demo), then literally instruct: "role play as each of my customers and tell me would they be happy to see a new course on... marketing mix modeling." (~10:31-10:57, VERIFIED — visual confirmation at `frame_0041`, t=09:43: "Vexpower Consumer Transcripts," 13 sources, participant "Rhys Fisher" visible on screen.) Converts recorded interviews into a queryable synthetic panel without recontacting real customers.

### 12. Sense-Check Before the Real Ask
The output doesn't replace going back to real people — it arms you before you do. "It at least gives me a bit of conviction so that... I know that when I go back to them that they're going to be primed to really like the ideas that I pitched to them... because I've already kind of sense-checked it with the virtual version of their customer." (~14:52-15:12, VERIFIED) The epistemic contract: synthetic research pre-filters which questions and pitches deserve real relationship capital.

### 13. Latent-Demand Mining Prompt + Drill-Down Loop
A distinct prompt variant from the preference test: "for the small business owner, what are the most pressing problems" — surfaces unmet need/pain, not a binary preference. (~21:14-21:38, VERIFIED) Then drill one level deeper on the single most interesting finding: "what are the real specific set of problems and what are possible products that would help address these." (~22:43-22:53, VERIFIED) This is an iterative loop, not a one-shot query — stop at the first surface pass and you miss the actual opportunity.

### 14. The "Secret Source" Differentiation Principle
Once everyone uses the same stock chatbot answer, using AI at all stops being a differentiator: "if you're just using the stock answer from ChatGPT or Claude, you don't have any real differentiator over anyone else... why would your customers be interested in what you had to say if there's no secret source there." (~14:15-14:34, VERIFIED) The moat isn't "using AI" — it's the proprietary grounding data (your own 10-15 real interviews) nobody else has.

### 15. Personalization Cascade — Segment to Individual, Insight Not Final Copy
After a top-level message validates in aggregate, re-run the SAME grounded panel for individual-level positioning: "write a personalized email to Chris telling him about the new [course]." (~16:33-16:37, VERIFIED) But his own discipline caps how far he trusts the raw output: "I use this more for insights in general... and then once I understand the angle of attack... then I'll kind of write it myself." (~17:44-17:53, VERIFIED) The workflow's job is to find the angle; the human writes the shipped copy.

### 16. The Research-Stack Handoff — Tool-to-Strength Routing
A deliberate 3-tool chain, not habitual single-tool use: (a) Gemini connected to Drive/G-Suite pulls a data-grounded one-pager on the audience from existing internal docs ("I have like 10 [years'] worth of documentation to pull from"); (b) that one-pager is handed to Claude because "Claude is just much... tuned much better to actually create content"; (c) Google Deep Research is used separately for cited, external market-level research (the $8-12K focus-group cost breakdown, 29 sites, exportable table, methodology shown). (~17:16-17:41, VERIFIED) Route each tool to what it's actually best at.

### 17. The "99 Questions You Can't Afford to Ask" Triage Logic
Real research budget is always scarcer than the number of questions worth asking. Synthetic panels exist to pre-filter which of those questions deserve the real $8-12K/weeks-long study, not to replace it: "there are always like a hundred times more questions that you have than you can afford to answer... if you can use AI to answer those other 99 questions you otherwise wouldn't have been able to ask, then you can really direct your research budget." (~24:57-25:13, VERIFIED — this is the exact line `buyer-council.md`'s Real-Research Boundary already quotes.)

---

## Hidden Knowledge

1. Non-text data (video/podcast transcripts) is comparatively under-represented in LLM training data vs. text — repurposing your own recorded calls into content is a higher-differentiation move than prompting on text alone. "The treasure trove right now for content creators... is data that is non-text." (~12:20-12:26, VERIFIED)
2. The underlying workflow isn't new — turning call notes into blog posts was manual editorial labor before AI; AI removes the labor bottleneck, it doesn't invent the technique. (~11:23-11:38, VERIFIED)
3. Voice-of-customer teams are traditionally an enterprise-only capability (HubSpot-scale companies own dedicated VoC teams); recording + roleplay democratizes that function for any company that records its calls. (~13:33-13:56, VERIFIED)
4. "Directionally correct" is the actual bar for a copy decision, not statistical significance — but AB-testing remains the closing step, never skipped: "I would love to see if you AB tested it if it did actually perform better." (~6:40-6:44, VERIFIED)
5. AI-visibility measurement (his "AI Search Creator" tool) reframes brand-awareness research: counting how often a brand surfaces in model output relative to competitors approximates unaided-awareness "within a margin of error" of a real study. (~8:16-8:37, VERIFIED)
6. He treats winning outputs as disposable/replicable, not IP to protect — releasing the "Grow without the guesswork" tagline live on air for anyone to steal signals this is positioned as a research/insight instrument, not a copy-generation moat. (~6:31-6:37, VERIFIED)

## Hall of Fame Exemplars

1. **HubSpot headline test** — "Grow better with HubSpot" (current) vs. "Grow without the guesswork" (his agency's line). 10 personas generated on-screen (frame_0049): Small Business Owner, Marketing Manager, Startup Founder, Sales Executive, Freelance Digital Marketer, Nonprofit Director, Enterprise IT Manager, Solopreneur, Customer Success Manager, Content Creator. Individual dissent preserved: startup founder favors the challenger line, marketing manager favors the incumbent — then aggregated ~60/40 toward "Grow without the guesswork," with the model's own reasoning ("speaks directly to the need for clarity, ease, and actionable insights across different professional contexts"). VERIFIED, visual + spoken.
2. **Vexpower/NotebookLM real-transcript panel** (`frame_0041`, t=09:43) — "Vexpower Consumer Transcripts," 13 sources, participant "Rhys Fisher" visible. Used to test whether existing subscribers would want a marketing-mix-modeling or customer-retention course, without recontacting anyone. VERIFIED, visual.
3. **Ask Rally's "lightsaber kit at 2am"** (LIKELY, secondary) — a cloned persona invented a specific, plausible, never-actually-happened purchase; the canonical illustration of individual-level unreliability inside aggregate-level validity.
4. **The $8-12K cost frame, live-verified** — cross-checked mid-show via Google Deep Research: "average company does about two focus groups a year," sourced across 29 sites with an exportable cost-breakdown table. VERIFIED.
5. **The personalized-email-to-Chris demo** — real-transcript-grounded panel asked to draft individual outreach; used for angle discovery, not shipped verbatim. VERIFIED.

## Signature Moves

1. Set the scene, then ask — never one instruction.
2. Close every panel prompt with the exact "joint anonymous answer" phrase.
3. Swap brand name for product category when the brand is obscure to the model.
4. Ground upward before trusting upward — never accept Tier-3 output at Tier-1 confidence.
5. Isolate personas pre-aggregation — never let them see each other mid-generation.
6. Mine the angle, write the copy yourself — the panel finds direction, the human ships the sentence.
7. Route each AI assistant to its strength rather than defaulting to one tool for everything.
8. Drill down one level on the single most interesting latent-demand finding rather than surveying broadly and stopping.

## Decision Framework (run before ANY workflow)

1. What's the DECISION this panel needs to inform — directional (headline, angle, latent-demand scan) or literal (a specific named individual's predicted action)? If literal, stop — this method isn't built for that; ground harder or go real.
2. Is the brand/product well-known to the model, or does it need category substitution?
3. Do real customer transcripts exist for this audience? If yes, this is a grounding-tier decision, not optional flavor — use them.
4. What tier is this panel running at (1/2/3)? State it in the output.
5. Is the question posed as a genuine critical ask, or is it phrased to fish for agreement (sycophancy risk)?
6. Are personas being generated in isolated threads, or in one shared thread (contamination risk)?
7. Does the money/stakes on this decision exceed what a directional synthetic verdict should carry alone? If yes, this triages toward real research, not away from it.

## Expert-Specific Quality Rubric (7 criteria, score 1-5)

| Criterion | 1 (Fail) | 3 (Marginal) | 5 (Taylor-grade) |
|---|---|---|---|
| Panel construction | Vague/generic "consumers" | Named roles, thin detail | Named roles + distinguishing background, category-substituted if needed |
| Question framing | Open-ended, no ask to be critical | Asks for opinion | Explicit "answer critically from their experience given their background" |
| Grounding tier stated | Unstated / conflated | Mentioned once, not carried through | Tier declared up front, confidence language matches the tier |
| Aggregation instruction | Missing or generic "combine these" | Paraphrased loosely | Exact "as if collaborated... joint anonymous answer" framing |
| Individual vs aggregate discipline | Individual prediction reported as fact | Hedge present but buried | Aggregate claims labeled aggregate; any individual example flagged illustrative |
| Sycophancy check | Unanimous/flattering result reported straight | Noted but not corrected | Dissent explicitly sought; suspicious unanimity flagged and re-run adversarially |
| Escalation honesty | Synthetic verdict presented as final | Caveat present, vague | Explicit next step named (AB test / real interview / real research) before the decision ships |

**Verdicts**: avg <3 = rebuild the prompt architecture before trusting output · 3-4 = usable as directional input, name the gap · ≥4 = ready to inform a real decision, still never a replacement for it on money/stakes calls.

## Anti-Patterns (the Taylor would-never-do list)

- Ask the direct question with no persona layer, then treat "the stock answer — kind of the average of the internet" as insight. (~2:43-2:59, VERIFIED, `references/source-quotes.md`)
- Combine persona generation and the real question in a single instruction, instead of the two-step "give me 10 demographic personas" then "answer this question critically from their experience given their background." (~3:16-3:32, VERIFIED)
- Report a cold-generated (Tier 3, ~60% per secondary corroboration) panel's verdict with the same confidence as a transcript-grounded (Tier 2) or calibrated (Tier 1, "high 70s to 80%") one. (LIKELY, twosetai.com, `references/source-quotes.md`)
- Let a panel's aggregate verdict get reported as a specific individual's predicted behavior — the Ask Rally "lightsaber kit at 2am" hallucination is the canonical failure case. (LIKELY, twosetai.com)
- Skip AB-testing a synthetic-panel-favored headline before it ships on a real budget — "I would love to see if you AB tested it, if it did actually perform better." (~6:40-6:44, VERIFIED)
- Generate personas in one shared thread and let them drift toward consensus mid-generation (the "vegan problem"). (LIKELY, twosetai.com)
- Ship the raw AI-drafted email/copy as final instead of using it for angle discovery — "I use this more for insights in general... then I'll kind of write it myself." (~17:44-17:53, VERIFIED)
- Treat a unanimous, flattering panel result as clean signal instead of a sycophancy flag — "it will always tell you your ideas are great." (LIKELY, twosetai.com)
- Skip real customer transcripts when they already exist, defaulting to cold generation out of convenience — his own rule is "all I had to do was hustle to do 10, 15 interviews and then some of this stuff is gold." (~14:38-14:44, VERIFIED)

## Recognition Test

Would Mike Taylor recognize this output as his — the two-step scene-set-then-ask architecture, the exact "joint anonymous answer" aggregation phrase, a stated grounding tier, dissent preserved before the aggregate, and an explicit next step (AB test, real interview, or escalation) rather than a verdict presented as final? If any of those five are missing, the output is wearing his vocabulary as decoration, not running his method — rebuild from the Decision Framework, not from the rubric.

## Voice DNA (when writing as/for this system)

Casual, demonstrative, narrates live ("so I'm just going to show you..."). Generous with the actual artifact — gives away winning copy on air. Habitually hedges numeric claims with "directionally correct... I'd love to see if you AB tested it." Spots the adjacent business opportunity mid-explanation without losing the thread. Self-deprecating about access gaps (UK beta-feature aside). Never mystical about the mechanism — names it plainly and moves to the next demo.
