---
description: "Multi-agent research-and-production engine that turns any raw concept into a production-ready 7-element Mini-Brief. Deploys parallel expert sub-agents via Gemini API, grounded in real market research, with platform optimization and taste validation. Feeds directly into `/ip-flywheel` or `/yt-flywheel`."
---

# `/mini-brief` v2.0 — The Concept Architect (Multi-Agent Engine)

Takes a raw concept and runs it through a **6-phase multi-agent pipeline**: research grounding, concept architecture, parallel expert forging, assembly, and quality validation. Produces a production-ready 7-element Mini-Brief with platform optimization specs.

**This is the bridge between "I have an idea" and "I have a publishable asset."**

**What changed from v1.0**: The brief is no longer brainstormed by one agent. Research data grounds every element. Expert sub-agents forge their assigned elements using their actual skill files (Tier 2 loaded). Platform optimization is built in. Quality is enforced, not hoped for.

---

## When to Use

- You have a concept but don't know how to frame it for maximum impact
- You want to develop a topic into a full flywheel-ready brief before committing to production
- You want to batch-develop 3-5 concepts into briefs for the week ahead
- You're taking output from `/flywheel-ideas` and want to deepen it before running `/ip-flywheel`
- A client conversation, comment, or DM sparked a content idea and you want to capture it while it's hot

## What It Replaces

- Staring at a blank screen trying to figure out "what angle should I take?"
- Writing posts that end up preachy or generic because the concept wasn't researched
- Skipping the narrative and going straight to "teaching" mode
- Hoping the brief is good enough without expert validation

---

## INPUT: What You Give It

| Input Type | Example |
|-----------|---------|
| Raw topic | "Coaches who are great on calls but can't write posts" |
| Problem statement | "My target audience has hired bad ghostwriters" |
| Client quote | "A client told me: 'I have 47 Google Docs but I can't post'" |
| Observation | "I noticed coaches with less experience are outperforming better coaches on LinkedIn" |
| Emotion | "The frustration of knowing you're brilliant but being invisible online" |
| Mini-Brief from `/flywheel-ideas` | [Paste the existing brief for deeper development] |
| Rough post draft | "I wrote this but it reads flat — help me find the real angle" |

If no input is provided, ask: "What's the concept, pain point, or idea you want to develop? Even a single sentence works."

---

## PHASE 0: Intake & Intent Validation

**Actor**: Orchestrator (main agent)

1. **Score intent sharpness 1-5** (per `directives/intent_refiner.md`)
   - If ≤ 3: Ask 2-3 clarifying questions to sharpen the concept
   - If ≥ 4: Proceed directly
   - If input is from `/flywheel-ideas`: Auto-score 5 (pre-validated)

2. **Classify concept mode** — which emotional register does this concept live in?

| Mode | Signals | Example |
|------|---------|---------|
| **Story-driven** | Client transformation, personal narrative, "How I" angles | "A coach DM'd me last month..." |
| **Contrarian** | Challenging a belief, taking a position, naming an enemy | "Everyone says 'just be consistent' — that's wrong" |
| **Recognition** | Making the reader feel seen, emotional resonance | "You know that feeling when you open LinkedIn and close the tab?" |
| **Educational** | Teaching a framework, process, or system | "Here's the actual math behind content deployment" |
| **Authority** | Demonstrating expertise, sharing data, building credibility | "I've worked with 47 coaches. Here's what I've learned." |
| **Vulnerability** | Build-in-public, personal struggle, honest failure | "I almost gave up on this business last month" |

3. **Detect target platform**: LinkedIn (default) | YouTube | Substack | Multi-platform

4. **Output**: Validated intent:
```markdown
## Intent Validated
- **Raw Input**: [user's words]
- **Concept Mode**: [detected mode]
- **Target Platform**: [platform]
- **Sharpness Score**: [1-5]
```

---

## PHASE 1: Research Gate (MANDATORY)

**Actor**: Orchestrator + external research tools
**Directive**: Enforces `directives/quality_assurance.md` Mandate 5 (Perplexity-First)

> **No research = no brief.** The 5 flywheel packages that worked were grounded in real DM conversations, specific pricing ($1,400/month, $2,200/month), and concrete scenes. This phase ensures every brief starts from reality, not imagination.

### Steps

1. **Check Perplexity budget**: Read `.agent/perplexity-usage.json`

2. **Execute 2-3 targeted queries** (Perplexity if budget available, `search_web` fallback):

| Query | Purpose | Example |
|-------|---------|---------|
| **Social Listening** | Real verbatim pain points from Reddit, LinkedIn, forums | `"[topic] coaches solopreneurs frustration 2026 reddit linkedin"` |
| **Competitive Landscape** | What angles are saturated vs. open | `"[topic] linkedin thought leadership content 2026"` |
| **Buyer Intent** (optional) | Does this pain connect to purchasing behavior? | `"[audience] hiring ghostwriter content help 2026"` |

3. **Log queries** to `.agent/perplexity-usage.json`

4. **Produce Research Brief** (saved to `.tmp/mini-brief-research-[slug].md`):

```markdown
## Research Brief: [Concept]
**Queries Used**: [count] | **Provenance**: 🟢 GROUNDED

### Real Pain Points (Verbatim)
- "[Actual quote from Reddit/LinkedIn/forum]" — source
- "[Actual quote]" — source

### Competitive Saturation Check
- **Saturated angles**: [what everyone is already saying]
- **Open angles**: [what nobody is saying yet]

### Buyer Intent Signal
- [Evidence that this pain connects to purchasing behavior]

### Flawed Common Beliefs (Market Evidence)
- "[Specific advice being repeated]" — where it appears
```

### Research Gate Check

If research reveals the concept has **zero real-world resonance** or is **completely saturated**:
- **HALT**. Present findings to user.
- Recommend pivoting the angle or discarding the concept.
- Do not proceed to Phase 2.

---

## PHASE 2: Concept Architecture

**Actor**: Orchestrator
**Prerequisite**: Phase 1 Research Brief in context

### Step 1: Research-Informed Excavation

Run the 4 Excavation Questions, but now **informed by research data**:

1. **The "So What?" Test**: Why would a busy coach stop scrolling for this? Ground in research verbatims — what are they ACTUALLY saying about this pain?

2. **The Flawed Belief**: What does the market currently believe? Pull directly from research — what specific advice is being repeated that's wrong or incomplete?

3. **The Lived Experience**: What's a specific SCENE? Use research data (DM conversations, Reddit threads, client stories from the data) to find or construct a scene with a person, a place, a feeling.

4. **The Actionable Artifact**: What could you BUILD that lets the reader EXPERIENCE the concept? The research reveals the specific gap — design the tool around that gap.

**If the concept doesn't survive questions 1 and 2 with research backing, HALT and recommend pivoting.**

### Step 2: Expert Constellation Selection

1. Read `agents/_framework/invocation-cards.md` (Tier 0 card check, ~50 tokens each)
2. Use the **Expert-to-Element Assignment Matrix** (below) to auto-select experts based on detected mode
3. Map each expert to their owned elements + specify skill files for Tier 2 loading

### Step 3: Present & Approve

**CHECKPOINT — Present Expert Constellation to user before proceeding:**

```markdown
## Expert Constellation: "[Working Title]"
**Mode**: [detected mode] | **Platform**: [target]
**Research Anchor**: [1-line from research that validates this concept]

| Expert | Owns Element(s) | Framework to Apply |
|--------|-----------------|-------------------|
| [Name] | [Elements] | [Specific framework from their skill] |
| [Name] | [Elements] | [Specific framework] |
| [Name] | [Elements] | [Specific framework] |

**WAIT FOR USER APPROVAL BEFORE PROCEEDING TO PHASE 3.**
```

---

## PHASE 3: Expert Element Forging (Parallel Sub-Agents)

**Actor**: 4-5 expert sub-agents via `execution/parallel_swarm.py`
**Prerequisite**: User approved Expert Constellation from Phase 2

> This is the core engine. Instead of one agent trying to write all 7 elements, **specialized sub-agents each forge their assigned elements using their actual skill files** (Tier 2 loaded: SKILL.md + genius.md + specific workflow).

### Execution Pattern

```
Batch 0 (TRUE PARALLEL — all fire simultaneously):
  [WO1: Pain & Truth Agent] ←→ [WO2: Narrative Hook Agent] ←→ [WO3: Asset Agent] ←→ [WO4: Platform Agent]

Batch 1 (SEQUENTIAL — runs after Batch 0 completes):
  [WO5: Oren Taste Gate]
```

### Work Order Templates

Each work order receives the **concept skeleton** (from Phase 2) + **research brief** (from Phase 1) as shared context.

#### WO1: Pain & Truth Agent

**Default Agent**: Kallaway (adjusts by mode — see matrix)
**Elements Owned**: 1-Shadow Market Pain, 2-Flawed Common Belief, 3-Contrarian Truth, 4-Stakes
**Tier 2 Files**:
- `skills/kallaway-content-psychology/SKILL.md`
- `skills/kallaway-content-psychology/genius.md`
- `skills/kallaway-content-psychology/workflows/hook-engineering-matrix.md`

**Mandate**:
- Apply the **Dopamine Ladder** (L1-L2: Stimulation → Captivation) to the Shadow Market Pain
- Use **Curiosity Loop Engineering** to forge the Contrarian Truth
- The pain must use **VERBATIM language** from the research brief — not LLM abstractions
- The contrarian truth must **SHATTER** a specific flawed belief identified in research
- Apply **stakes escalation**: emotional AND practical consequences
- Output must pass: "Does this make the reader's stomach drop? Does the truth create a lightbulb moment?"

**Output Format**:
```markdown
### 1. Shadow Market Pain
[Visceral, research-grounded pain. Verbatim language where possible.]

### 2. Flawed Common Belief
[Specific advice being repeated. Framed as a quote they've heard 100 times.]

### 3. Contrarian Truth
[2-3 sentences max. Shatters the belief. Lightbulb moment.]

### 4. Stakes
[Emotional + practical. What they lose if they keep believing the flaw.]

**Patterns Applied**: [list from genius.md]
**Research Verbatims Used**: [count]
```

#### WO2: Narrative Hook Agent

**Default Agent**: Tommy Clark (Story-driven) or Jasmin Alic (Recognition) — see matrix
**Element Owned**: 5-Narrative Hook (3 variations)
**Tier 2 Files** (Tommy Clark example):
- `skills/tommy-clark-linkedin-growth/SKILL.md`
- `skills/tommy-clark-linkedin-growth/genius.md`
- `skills/tommy-clark-linkedin-growth/workflows/founder-narrative-extraction-system.md`

**Mandate**:
- Apply **"How I" Narrative Pivot** (Tommy Clark) or **Trapdoor Hooks** (Jasmin Alic)
- Hook must open with a **SCENE** — a person, a moment, a conversation, a feeling
- Must survive the **3-line truncation test** (LinkedIn mobile cuts at line 3)
- Include a **Stealth Hook** variant (bypasses AI/ad detection filters)
- Produce 3 variations ranked by tension strength

**Output Format**:
```markdown
### 5. Narrative Hook — 3 Variations

**A (Highest Tension)**: [hook — scene-based, demands resolution]
**B (Recognition Play)**: [hook — makes reader feel seen]
**C (Data/Authority)**: [hook — specific number or observation]

**Hook Truncation Test**: [first 3 lines of each — do they survive mobile cut?]
**Patterns Applied**: [list]
```

#### WO3: Asset & Funnel Agent

**Default Agents**: Josh Sanders + Caleb Ralston
**Element Owned**: 6-Recommended Asset (full prompt kit outline)
**Tier 2 Files**:
- `skills/josh-sanders-linkedin-growth/SKILL.md`
- `skills/josh-sanders-linkedin-growth/genius.md`
- `skills/caleb-ralston-personal-brand/SKILL.md`

**Mandate**:
- Design the asset as a **diagnostic or interactive tool** — not a static PDF
- Apply Josh Sanders' **depth-first monetization**: the asset must generate saves, not just likes
- The asset must let the reader **EXPERIENCE** the concept (diagnose, calculate, mine, score)
- Include: asset name, description, keyword CTA, and **3-phase prompt kit outline**
- Apply Caleb Ralston's **credibility architecture**: builds trust AND reveals gap
- Pass: "Could the reader use this WITHOUT hiring Farrice?" (trust) AND "Does using it naturally reveal a gap?" (conversion)

**Output Format**:
```markdown
### 6. Recommended Asset

**Name**: [punchy, descriptive name]
**Type**: [Diagnostic / Calculator / Mining Kit / Scorecard / Template]
**Keyword CTA**: Drop "[WORD]" below and I'll send it
**Description**: [1-2 sentences — what it does for the reader]

**Prompt Kit Outline (3 Phases)**:
- Phase 1: [Setup — what info the user provides]
- Phase 2: [Analysis — what the tool calculates/reveals]
- Phase 3: [Output — what the user receives]

**Trust Test**: [Can reader use without hiring Farrice? Y/N + why]
**Gap Test**: [Does usage reveal a gap Farrice fills? Y/N + how]
**Patterns Applied**: [list]
```

#### WO4: Platform Optimization Agent

**Default Agents**: LinkedIn 2026 Format Arbitrage + Lara Acosta (LinkedIn) | Mode-specific for YouTube/Substack
**Element Owned**: Platform Spec
**Tier 2 Files** (LinkedIn):
- `skills/linkedin-2026-format-arbitrage/SKILL.md`
- `skills/linkedin-2026-format-arbitrage/genius.md`
- `skills/lara-acosta-linkedin-mastery/SKILL.md`

**Mandate**:
- Apply **Niche Bending Formula** (Pattern 1): What format would be novel for this concept?
- Apply **Commitment Escalation Loop** (Pattern 2): If carousel, design slide progression
- Apply **Trapdoor Hook** (Pattern 3): Ensure hook survives 3-line mobile truncation
- Apply **Costly Signaling Theory** (Pattern 4): Recommend visual strategy
- Apply **Comment-to-Download Flywheel** (Pattern 7): Design velocity engineering
- Specify: optimal format, character count, posting time, first-comment strategy, depth metric targets

**Output Format**:
```markdown
### Platform Spec: [LinkedIn / YouTube / Substack]

- **Optimal Format**: [Text post / Carousel / Document / Selfie+text]
- **Why This Format**: [reasoning from format arbitrage patterns]
- **Character Target**: [X characters]
- **Hook Truncation Check**: [first 3 lines — survive mobile cut?]
- **Visual Strategy**: [Costly Signaling recommendation]
- **CTA Architecture**: [Comment keyword → DM → asset → qualifying question]
- **Posting Window**: [day/time]
- **Depth Metric Target**: [saves goal, dwell time strategy]
- **First Comment Strategy**: [what to pin, link strategy]
- **Patterns Applied**: [list]
```

#### WO5: Taste Gate (Batch 1 — AFTER WO1-4)

**Agent**: Oren
**Role**: Quality validator — pass/fail per element
**Tier 2 Files**:
- `skills/oren-repositioning/SKILL.md`
- `skills/oren-repositioning/genius.md`

**Mandate**:
- Run the **Oren Taste Check** on the assembled elements from WO1-4:
  - Does this sound like a **premium thought leader** or a desperate service provider?
  - Is the tone **"unbothered authority"** — calm, diagnostic, slightly detached?
  - Would this concept still be valuable if you **never mentioned your service**?
  - Is there any **template slop** — generic phrases any coach could sign?
- **Pass/fail each element** with specific revision notes if fail

**Output Format**:
```markdown
### Taste Verdict

| Element | Pass/Fail | Notes |
|---------|-----------|-------|
| 1. Shadow Pain | ✅ / ❌ | [specific issue if fail] |
| 2. Flawed Belief | ✅ / ❌ | [specific issue if fail] |
| 3. Contrarian Truth | ✅ / ❌ | [specific issue if fail] |
| 4. Stakes | ✅ / ❌ | [specific issue if fail] |
| 5. Narrative Hook | ✅ / ❌ | [specific issue if fail] |
| 6. Asset | ✅ / ❌ | [specific issue if fail] |
| Platform Spec | ✅ / ❌ | [specific issue if fail] |

**Overall**: PASS / REVISE [list elements to fix]
**Tone Check**: [unbothered authority Y/N]
**Template Slop Check**: [any generic phrases flagged]
```

### Invocation

Run Phase 3 via CLI:
```bash
python execution/parallel_swarm.py \
  --mode mini-brief \
  --agents "kallaway,tommy-clark,josh-sanders,linkedin-2026-format-arbitrage,oren" \
  --context ".tmp/mini-brief-research-[slug].md" \
  "[concept skeleton summary]"
```

Or orchestrate directly via Claude sub-agents using the SkillExecutor archetype from `directives/sub_agent_protocol.md`.

---

## PHASE 4: Assembly

**Actor**: Orchestrator
**Prerequisite**: All sub-agent outputs received

1. **Merge outputs** into the unified 7-element Mini-Brief format
2. **Integrate platform optimization specs** from WO4
3. **Apply Oren's taste verdict** from WO5:
   - If any element FAILED: revise inline (max 1 revision per element)
   - If overall PASS: proceed to Phase 5
4. **Build Element 7** (Expert Stack) — which expert forged which element and which frameworks were applied
5. **Add provenance tags**:
```markdown
**Provenance**:
RESEARCH: [query count] queries | 🟢 GROUNDED
SKILLS LOADED: [list with file paths]
PATTERNS APPLIED: [list by name]
TASTE CHECK: Oren — [PASS/REVISE]
```

### Assembled Output Format

```markdown
## Mini-Brief: "[Punchy Title — 5-8 words]"
**Platform**: [target] | **Mode**: [mode] | **Research**: 🟢 GROUNDED

### 1. Shadow Market Pain
[Forged by [Agent] using [Framework], grounded in research verbatims]

### 2. Flawed Common Belief
[Forged by [Agent] using market evidence from Phase 1]

### 3. Contrarian Truth
[Forged by [Agent] using [Framework]. 2-3 sentences max.]

### 4. Stakes
[Forged by [Agent]. Emotional + practical.]

### 5. Narrative Hook (3 Variations)
[Forged by [Agent] using [Framework]]
- **A** (highest tension): [hook]
- **B** (recognition): [hook]
- **C** (authority): [hook]

### 6. Recommended Asset
[Forged by [Agent] using [Framework]]
- **Name**: [asset name]
- **Type**: [Diagnostic / Calculator / Mining Kit / Scorecard]
- **Keyword CTA**: Drop "[WORD]" below
- **Prompt Kit Outline**: [3-phase structure]

### 7. Expert Stack
[Which experts will produce the full assets in `/ip-flywheel`, with WHY and which specific frameworks they'll apply. Informed by which experts performed best in Phase 3.]

---

### Platform Spec
[Full spec from WO4]

### Provenance
[Full provenance tags]
```

---

## PHASE 5: Quality Gauntlet & Present

**Actor**: Orchestrator

### Quality Checks

1. **3-Point Quality Gate** (per `directives/quality_gate.md`):
   - **Intent Alignment**: Does this brief match what the user originally asked for?
   - **Expert Standard**: Would Kallaway/Tommy Clark/etc. be proud of these elements?
   - **Adversarial Resilience**: Would a domain expert find something embarrassing?

2. **Narrative Test**:
   - Does the hook open with a SCENE (person, place, moment), not a statement?
   - Could this concept be told as a story from beginning to end?
   - Is there genuine TENSION that demands resolution?

3. **Asset Test**:
   - Could the reader use the prompt kit WITHOUT hiring Farrice? (Trust test)
   - Does using it naturally reveal a gap that Farrice's service fills? (Conversion test)

If any gate fails: revise the failing element only (max 1 retry).

### Present to User

```markdown
> **This Mini-Brief is production-ready.** It can feed directly into:
> - `/ip-flywheel` for full 4-asset LinkedIn package (essay + prompt kit + visual + Substack)
> - `/yt-flywheel` for video-first 6-asset package
>
> **Actions**:
> 1. **Produce** — Run `/ip-flywheel` or `/yt-flywheel` now
> 2. **Tweak** — Adjust any of the 7 elements before production
> 3. **Save** — Store to `_active/content/mini-briefs/[slug].md` for later
> 4. **Next** — (Batch mode) View next concept in the dossier
```

---

## BATCH MODE

When developing 3-5 concepts at once:

1. **Phase 0**: Accept all concepts. Validate each.
2. **Phase 1**: Run research for ALL concepts in a shared session (2-3 queries per concept). Shared research context reduces redundancy.
3. **Phase 2-5**: Process each concept sequentially, but Phase 3 sub-agents run in parallel FOR each concept.
4. **Present as Concept Dossier**:

```markdown
# CONCEPT DOSSIER — [Date]

## Mini-Brief 1: "[Title]" 🟢 GROUNDED
[Full 7-element brief with platform spec]
**Production Priority**: [High / Medium / Low]
**Recommended Engine**: `/ip-flywheel` or `/yt-flywheel`

## Mini-Brief 2: "[Title]" 🟢 GROUNDED
[Full 7-element brief with platform spec]
**Production Priority**: [High / Medium / Low]
...

---
**Which briefs should we produce first? Reply with the numbers.**
```

**Cost estimate** (5-concept batch via Gemini):
- 5 concepts x 4 parallel agents + 5 Oren checks = 25 Gemini calls
- At ~$0.03/call: ~$0.75
- Plus 10-15 Perplexity queries: ~$0.50-1.00
- **Total: ~$1.25-1.75**

---

## EXPERT-TO-ELEMENT ASSIGNMENT MATRIX

Use this matrix to auto-select experts based on the detected concept mode from Phase 0:

| Element | Story-driven | Contrarian | Recognition | Educational | Authority | Vulnerability |
|---------|-------------|------------|-------------|-------------|-----------|---------------|
| **1. Shadow Pain** | Tommy Clark (operational) | Kallaway (neurological) | Jasmin Alic (emotional) | Josh Sanders (pipeline gap) | Caleb Ralston (buyer-level) | Jasmin Alic (emotional) |
| **2. Flawed Belief** | Kallaway (dopamine trap) | Erica Mallet (category) | Dan Koe (identity trap) | Kallaway (dopamine trap) | Caleb Ralston (contrarian) | Caleb Ralston (contrarian) |
| **3. Contrarian Truth** | Kallaway (thesis) | Kallaway (thesis) | Erica Mallet (belief) | Harry Dry (density) | Caleb Ralston (credibility) | Kallaway (thesis) |
| **4. Stakes** | Tommy Clark (business) | Erica Mallet (enemy) | Dan Koe (opportunity) | Josh Sanders (pipeline) | Tommy Clark (business) | Jasmin Alic (personal) |
| **5. Hook** | Tommy Clark (gravedigger) | Kallaway (curiosity loop) | Jasmin Alic (emotional) | Harry Dry (visualization) | Caleb Ralston (authority) | Caleb Ralston (vulnerability) |
| **6. Asset** | Kallaway (demand) | Josh Sanders (save-value) | Kallaway (demand) | Josh Sanders (save-value) | Caleb Ralston (credibility) | Kallaway (demand) |
| **7. Stack** | Kallaway + Tommy + Lara | Kallaway + Erica + Caleb | Jasmin + Dan + Lara | Josh + Harry + Kallaway | Caleb + Kallaway + Josh | Caleb + Jasmin + Tommy |
| **Platform** | LI 2026 + Lara | LI 2026 + Lara | LI 2026 + Jasmin | LI 2026 + Josh | LI 2026 + Caleb | LI 2026 + Lara |
| **Taste Gate** | Oren | Oren | Oren | Oren | Oren | Oren |

### How to Read the Matrix

1. Detect concept mode in Phase 0
2. Read the column for that mode
3. The **WO1 Pain & Truth Agent** uses the experts listed for Elements 1-4
4. The **WO2 Hook Agent** uses the expert listed for Element 5
5. The **WO3 Asset Agent** uses the expert listed for Element 6 + the Josh/Caleb pairing
6. The **WO4 Platform Agent** uses the experts listed for Platform row
7. **WO5 Taste Gate** is always Oren

---

## WORKFLOW CHAIN

```
Raw idea / topic / observation
        ↓
  PHASE 0: Validate intent, classify mode, detect platform
        ↓
  PHASE 1: Research Gate (Perplexity/search_web — MANDATORY)
        ↓
  PHASE 2: Concept Architecture + Expert Constellation
        ↓  [USER APPROVAL CHECKPOINT]
  PHASE 3: Parallel Expert Forging (4 sub-agents via Gemini)
        ↓  + Sequential Oren Taste Gate
  PHASE 4: Assembly → 7-element Mini-Brief + Platform Spec
        ↓
  PHASE 5: Quality Gauntlet → Present
        ↓
  /ip-flywheel (4-asset package)
  OR /yt-flywheel (video-first package)
        ↓
  Published content + prompt kit
        ↓
  Engagement → DMs → Proof Run → Revenue
```

**Alternative entry points:**
```
/flywheel-ideas → /mini-brief → /ip-flywheel or /yt-flywheel
Client conversation → /mini-brief → /ip-flywheel
Trending topic → /mini-brief → /ip-flywheel
```

**Chain contract** (see `directives/workflow-chains.md` Chain 5):
- `/mini-brief` output maps directly to `/ip-flywheel` Step 2 (Creative Brief)
- Elements 1-4 → "Core Hook & Stakes (Kallaway)"
- Element 3 → "Contrarian Angle (Dan Koe)"
- All 7 → "Outline/Beat Sheet"
- Platform Spec → format selection in Asset 1
- Element 7 → which experts to deploy for asset generation

---

## EXAMPLE

### Input
"Coaches who organize everything in Notion but still can't write a post"

### Phase 0 Output
- **Mode**: Recognition | **Platform**: LinkedIn | **Sharpness**: 4/5

### Phase 1 Research (abbreviated)
- Reddit r/coaching: "I have 15 frameworks documented and still freeze at the blank editor"
- LinkedIn comment: "Organization is my procrastination disguised as productivity"
- Saturated angle: "Just start writing" / "Done is better than perfect"
- Open angle: Storage skill vs. translation skill distinction

### Phase 3 Expert Outputs (assembled)

> **Mini-Brief: "The 47 Google Docs Trap"** 🟢 GROUNDED
>
> **1. Shadow Market Pain** (Kallaway — Dopamine Ladder L1):
> Coaches who invested in knowledge management — color-coded Notion, the Tiago Forte book, 47 Google Docs — and still freeze at the blank LinkedIn editor. They did the hard work. The hard work didn't work.
>
> **2. Flawed Common Belief** (Kallaway — market evidence):
> "If I organize all my knowledge, content creation will be easy." Repeated in every BASB course, every Notion template, every productivity guru's funnel.
>
> **3. Contrarian Truth** (Kallaway — Curiosity Loop):
> Organizing knowledge and deploying knowledge are completely different cognitive operations. Your system can store information — but it can't think like you. You have a warehouse full of IP and no delivery trucks.
>
> **4. Stakes** (Kallaway — stakes escalation):
> Every framework in your Notion is a month of content not working for you. Every week of invisibility is a week where less-organized but more-deployed coaches capture the clients you should be serving.
>
> **5. Narrative Hook** (Jasmin Alic — Trapdoor Hook):
> - **A**: "You have 47 Google Docs. Don't pretend you don't know the exact number."
> - **B**: "She had the most beautiful Notion workspace I'd ever seen. And this morning she stared at LinkedIn for 12 minutes and closed the tab."
> - **C**: "12 frameworks. 0 LinkedIn posts. I asked her to describe framework #4 the way she'd explain it to a client at minute 30."
>
> **6. Recommended Asset** (Josh Sanders + Caleb Ralston):
> - **Name**: "The Deployment Gap Calculator"
> - **Type**: Calculator / Diagnostic
> - **Keyword CTA**: Drop "DEPLOY" below
> - **Outline**: Phase 1: List frameworks + one-line descriptions → Phase 2: Calculate content potential (8 posts per framework) → Phase 3: Generate first 5 post concepts from highest-converting framework
> - **Trust Test**: ✅ Usable without hiring Farrice
> - **Gap Test**: ✅ Reveals they need translation help, not more organization
>
> **7. Expert Stack**: Kallaway (dopamine of organization vs. deployment) + Jasmin Alic (recognition rhythm — "you know who you are") + Lara Acosta (F-shape formatting, SLAY structure for the LinkedIn essay)
>
> **Platform Spec**: Text post | ~2,300 chars | F-shape formatting | CTA: "DEPLOY" | Posting: Tue-Thu 8-10am EST | Depth target: 50+ saves
>
> **Provenance**: 3 queries 🟢 GROUNDED | Kallaway genius.md + hook-engineering-matrix.md, Jasmin Alic genius.md, Josh Sanders genius.md | Oren taste check: PASS
