# Intent Pipeline (MANDATORY)

> **Purpose**: Single pipeline for processing every user request — from raw thought to expert execution.
> **Replaces**: The 3-way collision between `intent_refiner.md`, `pre_flight_validation.md`, and `expert_auto_routing.md`.
> **Effective**: 2026-03-02

---

## The Pipeline (4 Stages, Always in Order)

### Stage 1: SCORE

Rate intent sharpness 1-5. Award 1 point for each:

- [ ] Has a specific **deliverable** type (copy, strategy, research, system, content)
- [ ] Has a defined **audience** (who consumes this)
- [ ] Has **context** or constraints stated
- [ ] Has a clear **end state** / success criteria
- [ ] Uses **specific language** (numbers, names, concrete nouns) vs. abstract

| Score | Label | Next Step |
|-------|-------|-----------|
| **1** | Raw thought | → Stage 2 (full DICE) |
| **2** | Directional | → Stage 2 (2-3 DICE questions) |
| **3** | Formed | → Stage 2 (present sharpened version, confirm) |
| **4** | Sharp | → Stage 3 (confirm briefly, route) |
| **5** | Razor | → Stage 3 (execute immediately) |

### Stage 2: SHARPEN

Run DICE on **missing dimensions only**. One round of questions max.

- **D — Deliverable**: "What concrete thing do you want in your hands when this is done?"
- **I — Intended Audience**: "Who specifically will consume or be affected?"
- **C — Context**: "Any constraints, deadlines, or prior work?"
- **E — End State**: "What does 'nailed it' look like?"

**Rules:**
- Do NOT ask all 4 if some are already clear from context
- Fill in what you can infer, then confirm: "Here's what I heard — is this right?"
- If Score 1-2 and multiple valid interpretations exist, present 2-3 options (from pre-flight pattern)
- Anti-interrogation: one concise block, not a 20-question survey

**After sharpening**, present:
```
## Intent Refined

**What you said**: "[original]"
**Score**: X/5 → Y/5

**Sharpened objective**:
"[One-paragraph razor-sharp version]"

Ready to route? Or adjust?
```

### Stage 3: ROUTE

Match the sharpened intent to the right experts. Use the domain detection table below.

**Step 1 — Domain match:**

| Request Type | Signals | Default Experts | Registry Domain |
|:---|:---|:---|:---|
| Research/Intelligence | "analyze", "research", "find out", "market" | Manus.AI + domain expert | 12 |
| Content Creation | "write", "create", "draft", "content" | Appropriate content expert(s) | 2, 7 |
| Strategy/Decision | "should I", "what's the best", "how do I approach" | Jim O'Shaughnessy + domain experts | 12 |
| Copywriting | "sales page", "email", "headline", "convert" | Cardinal Mason + Harry Dry | 1 |
| Personal Brand | "LinkedIn", "positioning", "brand", "authority" | Lara Acosta + Caleb Ralston | 3 |
| Ghostwriting | "ghostwrite", "write as", "voice capture", "proof run" | Ghostwriting Voice Engine (`/ghostwrite`) | — |
| Product/Offer | "product", "offer", "pricing", "launch" | Nicolas Cole + Monk.AI | 8 |
| Sales/Persuasion | "objection", "close", "persuade", "sell" | Jeremy Miner + Jason Fladlien | 4 |
| Storytelling | "story", "narrative", "hook", "engage" | Shaan Puri + Lucas Alpay | 7 |
| Video/Media | "video", "TikTok", "cinematic", "storyboard" | Seena Rez + Tao Prompts | 11 |
| AI/Automation | "automate", "workflow", "agent", "AI", "Claude" | Nick Saraev + Boris | 6 |
| SEO/Search | "rank", "SEO", "keywords", "traffic", "answer engine" | Nathan Gotch + Ethan Smith | 9 |
| Design/Visual | "design", "visual", "aesthetic", "website", "typography" | Oren + Kittl + Andy Lo | 10 |
| Audience/Growth | "grow", "newsletter", "subscriber", "community" | Tyler Denk + Dan Koe | 13 |
| Mindset/Messaging | "stuck", "blocked", "mindset", "messaging", "movement" | Jeremy Haynes + Heath Brothers | 14 |
| Consumer Research | "customer", "persona", "buyer", "psychology" | Dai Media + Kallaway | 5 |
| Monetization | "monetize", "revenue", "recurring", "service" | Paul James + Sabrina Ramonov | 8 |
| Advertising | "ads", "paid", "campaign", "Facebook", "Google Ads" | Sabri Suby | 15 |
| Real Estate | "real estate", "listing", "property" | Joshua Smith | 15 |
| Launch/Innovation | "launch", "validate", "early adopter" | Seena Rez + Samuel Thompson | 8, 12 |

> **Full routing trees**: See `DOMAIN_REGISTRY.md` (15 domains, 94 agents with swim lanes).

**Step 2 — Determine mode (Output vs. Expertise):**

| Mode | Signals | Effect |
|:---|:---|:---|
| **OUTPUT** | "write me", "create", "build", "draft", "make" — wants a deliverable | Load at Tier 1-2, produce the artifact |
| **EXPERTISE** | "how should I", "what's the best way", "advise me", "review" — wants thinking | Load at Tier 0-1, present expert analysis/recommendations |
| **HYBRID** | "help me with" — could go either way | Ask: "Do you want me to produce [X] or advise on the approach?" |

This distinction prevents over-producing when the user wants advice, and under-delivering when they want an artifact.

**Step 3 — Multi-domain?** If request spans 2+ domains, select an ensemble. Reference `DOMAIN_REGISTRY.md` for compound combinations and force-multiplier pairings.

**Step 3b — Gap Check (after domain match):**

After matching intent to domain, verify expert coverage exists:
1. Scan `agents/_framework/invocation-cards.md` for relevant experts
2. If no match: scan `DOMAIN_REGISTRY.md` swim lanes
3. If still no match: **trigger Expertise Gap Protocol** (`directives/expertise-gap-protocol.md`)
   - Classify severity (Low / Medium / High)
   - Execute appropriate mode (Advisory / Guided / Autonomous)
   - If extraction resolves the gap, re-run ROUTE with the new expert loaded

**When to skip Gap Check**: user said "just do it", one-off factual question, existing expert is close enough (>70% domain overlap), follow-up within approved plan, system/meta tasks.

**Step 4 — Load experts via Context Engine:**
1. **Tier 0**: Read invocation cards (~50 tokens each) for routing confirmation
2. **Tier 1**: Read SKILL.md + specific workflow (~1,350 tokens) for clear tasks
3. **Tier 2**: Add genius.md (~2,550 tokens) for creative/complex work
4. **Tier 3**: Spawn sub-agent for 3+ experts or 10+ files loaded

Full loading protocol: `directives/agent-loading-protocol.md`

### Stage 4: PRESENT

For complex or multi-step requests, present before executing:

```
## Expert Recommendation

**Domain**: [detected domain(s)]

| Expert | Role |
|:---|:---|
| **[Expert 1]** | [1-line reason] |
| **[Expert 2]** | [1-line reason] |

**Approach**: [How this will be tackled]

Proceed? Or swap anyone?
```

**Skip this block for**: simple single-expert tasks, follow-ups in an established flow, "just do it."

---

## Skip Conditions (Don't Run Pipeline)

- Clear, specific instruction with all parameters (Score 5)
- Bug fixes or corrections with clear scope
- Simple factual questions
- Follow-up within an already-approved plan
- User says "just do it", "go ahead", "execute"
- Trivial single-line tasks

---

## Proactive Deployment (From FARRICE.md)

Don't wait for slash commands. When conversational cues match a domain:

| Cue | Auto-Action |
|-----|-------------|
| Mentions LinkedIn, posts, content, hooks | Route to content/brand experts (Domain 2, 3, 13) |
| Working on sales page, offer page, email | Route to copywriting experts (Domain 1) |
| Asks about positioning, brand, differentiation | Route to brand experts (Domain 3, 12) |
| Discusses products, pricing, monetization | Route to product experts (Domain 8) |
| Mentions SEO, ranking, traffic, blog | Route to SEO experts (Domain 9) |
| Discusses video, TikTok, AI video | Route to video/content experts (Domain 11, 2) |
| Mentions AI tools, automation, agents, Claude | Route to AI experts (Domain 6) |
| Says "I'm stuck", mindset, blocked, afraid | Route to mindset experts (Domain 14) |
| Discussing design, website, visual identity | Route to design experts (Domain 10) |
| Pastes transcript or mentions "I watched this video" | Run `/extract` |
| Says things feel broken, cluttered, slow | Run `/system-audit` |
| Excited, firing off ideas without clear deliverable | Pause → reflect intent → sharpen → execute |

**Fallback**: When unsure which workflow, run `/recommend`.

---

## Mid-Flight Refinement

This pipeline also works mid-conversation (what `/refine-intent` triggers):
- Same 4 stages, but start from current context, not fresh
- If the session goal changed, update session state
- If new experts needed, re-route

---

## Reference Docs (for deep protocol details)

| Detail | Reference |
|--------|-----------|
| DICE protocol specifics | `directives/intent_refiner.md` |
| Domain swim lanes (15 domains, 94 agents) | `DOMAIN_REGISTRY.md` |
| Compound combinations & handoff chains | `DOMAIN_REGISTRY.md` |
| Domain detection signals (quick-match) | `directives/expert_auto_routing.md` |
| McKinsey-grade output standard | `directives/expert_auto_routing.md` |
| Expert loading tiers | `directives/agent-loading-protocol.md` |
| Expertise gap self-healing | `directives/expertise-gap-protocol.md` |
| Combo reference table | `directives/intent_refiner.md` (Step 3) |

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-01 |

**Update Rule**: When this pipeline fires (scoring + routing), update the date and increment count.

---

*Created: 2026-03-02 | Replaces: intent_refiner (routing), pre_flight_validation (entirely), expert_auto_routing (intent handling)*
*Classification: Mandatory Orchestration Protocol*
