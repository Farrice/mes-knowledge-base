# CREATIVE ASSEMBLY SKILL

## Multi-Agent Creative Production System

*Multiple experts produce work → hand off → refine → deliver polished output*

---

## The Problem This Solves

**Before:** You manually prompt one expert, get output, switch context, prompt another expert to refine, switch context again, prompt an editor... Massive cognitive load and context switching.

**After:** You describe what you want. Experts work in parallel, hand off to each other, refine each other's work, and return either:
- A finished polished piece, OR
- Multiple versions for you to choose from before final assembly

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    🎭 MAESTRO (You)                             │
│            "I need a sales email for my new offer"              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                 🎬 CREATIVE DIRECTOR                            │
│     Decomposes → Assigns Experts → Manages Handoffs             │
└─────────────────────────────────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  📝 PRODUCER 1  │ │  📝 PRODUCER 2  │ │  📝 PRODUCER 3  │
│  (Parallel)     │ │  (Parallel)     │ │  (Parallel)     │
│                 │ │                 │ │                 │
│ Expert: Deutsch │ │ Expert: Kallaway│ │ Expert: Cole    │
│ Task: Cold hook │ │ Task: Curiosity │ │ Task: Clarity   │
└─────────────────┘ └─────────────────┘ └─────────────────┘
         │                    │                    │
         └────────────────────┼────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    🔄 ASSEMBLY STAGE                            │
│         Best elements selected → Combined → Refined             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ✂️ EDITOR PASS                               │
│     Tightening → Flow → Voice consistency → Quality gate        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    📦 DELIVERABLE                               │
│              Polished piece ready for use                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Two Operating Modes

### Mode 1: FULL ASSEMBLY (Default)

Experts produce → hand off → refine → deliver **one polished piece**

**You say:** "Write me a sales email for my consulting offer"

**What happens:**
1. Creative Director assigns experts based on task
2. Producers work in parallel on different angles/components
3. Assembly stage combines best elements
4. Editor pass polishes and ensures coherence
5. You receive one finished email

**Best for:** When you trust the system and want to minimize your involvement

---

### Mode 2: SELECTION ASSEMBLY

Experts produce multiple versions → you pick → then final polish

**You say:** "Write me a sales email — show me options first"

**What happens:**
1. Creative Director assigns experts
2. Producers each create a complete version (not components)
3. You see 2-4 distinct approaches with their reasoning
4. You select your favorite (or elements from each)
5. Editor pass polishes your selection
6. You receive the final piece

**Best for:** When you want creative input on direction before committing

---

## Natural Language Activation

The system activates automatically when you request creative production:

| You say... | System interprets as... |
|------------|------------------------|
| "Write me a..." | Full Assembly mode |
| "Create a..." | Full Assembly mode |
| "I need a..." | Full Assembly mode |
| "...show me options" | Selection Assembly mode |
| "...give me versions" | Selection Assembly mode |
| "...let me pick" | Selection Assembly mode |

**No commands needed.** Just describe what you want and whether you want options.

---

## The Creative Roles

### 🎬 Creative Director (Orchestrator)

**Function:** Decompose task, assign experts, manage handoffs, ensure coherence

**Behavioral Mandate:**
- Break creative tasks into distinct components or parallel approaches
- Assign the right expert to each component based on their methodology
- Define clear output specs for each producer
- Manage handoffs with explicit context preservation
- Make final assembly decisions that serve Fresh's intent

### 📝 Producers (Expert Agents)

Each producer embodies a specific expert's methodology:

**Copy Producers:**
- David Deutsch → Cold traffic conversion, mechanism reveals
- Bond Halbert → Emotional hooks, fascinations
- Alen Sultanic → Frameworks, structure
- Cardinal Mason → AI-optimized copy patterns
- Harry Dry → Concise, punchy, memorable

**Content Producers:**
- Kallaway → Viral hooks, content psychology
- Lara Acosta → LinkedIn authority building
- Nicolas Cole → Sentence craft, clarity
- Shaan Puri → Story hooks, curiosity

**Strategy Producers:**
- Monk AI → Offer architecture
- Greg Hickman → Client acquisition angles
- Erica Mallett → Brand positioning

**Narrative Producers:**
- Jonathan Franzen → Literary depth, observation
- Mitch Albom → Emotional resonance
- Donald Miller → StoryBrand structure

### ✂️ Editor (Refiner)

**Function:** Polish, tighten, ensure consistency

**Behavioral Mandate:**
- Cut ruthlessly — every word must earn its place
- Ensure voice consistency across assembled pieces
- Verify flow and transitions
- Quality gate — reject if below standard, request revision
- Final check against Fresh's known preferences

---

## Expert Auto-Assignment

The Creative Director automatically assigns experts based on task:

| Task Type | Primary Experts | Support Experts |
|-----------|-----------------|-----------------|
| Sales email | David Deutsch, Cardinal Mason | Harry Dry (hooks), Nicolas Cole (clarity) |
| LinkedIn post | Lara Acosta, Kallaway | Nicolas Cole (sentences) |
| Sales page | David Deutsch, Bond Halbert | Alen Sultanic (structure) |
| Video script | Kallaway, Shaan Puri | Oscar Hoglund (pacing) |
| Offer copy | Monk AI, Greg Hickman | David Deutsch (conversion) |
| Story/narrative | Jonathan Franzen, Mitch Albom | Donald Miller (structure) |
| Hooks/headlines | Kallaway, Harry Dry | Bond Halbert (fascinations) |
| Email sequence | Kai Lode, Cardinal Mason | David Deutsch (cold traffic) |

---

## The Production Pipeline

### Stage 1: Decomposition

Creative Director analyzes the request and creates a production brief:

```
CREATIVE BRIEF
━━━━━━━━━━━━━━
Deliverable: [What we're creating]
Purpose: [What it needs to accomplish]
Audience: [Who it's for]
Constraints: [Length, tone, format requirements]

PRODUCTION ASSIGNMENTS:
━━━━━━━━━━━━━━━━━━━━━
Producer 1: [Expert] → [Component/Version]
Producer 2: [Expert] → [Component/Version]
Producer 3: [Expert] → [Component/Version]

OUTPUT SPECS:
━━━━━━━━━━━━
Each producer returns: [Structured format]
Assembly approach: [Full merge OR selection]
```

### Stage 2: Parallel Production

Producers work simultaneously, each with:
- Their expert's methodology loaded
- Clear component assignment OR full version assignment
- Defined output format
- No visibility into other producers' work (prevents groupthink)

### Stage 3: Assembly

**For Full Assembly:**
- Creative Director reviews all producer outputs
- Selects strongest elements from each
- Combines into coherent draft
- Resolves any conflicts or redundancies

**For Selection Assembly:**
- All versions presented to you with brief rationale
- You select or indicate preferences
- Selected version(s) passed to editor

### Stage 4: Editor Pass

Editor applies:
- Line-by-line tightening
- Flow and transition improvements
- Voice consistency check
- Quality gate verification
- Fresh-preference calibration

### Stage 5: Delivery

Final output delivered with:
- The polished piece
- Brief note on approach taken (if useful)
- Confidence level
- Optional: variations or alternatives available on request

---

## Handoff Protocol

Based on Lance & Yichao's context engineering principles:

### Context Preservation

Each handoff includes structured context:
```
HANDOFF BRIEF
━━━━━━━━━━━━━
From: [Role]
To: [Role]
Task completed: [What was done]
Key decisions made: [Creative choices]
Constraints honored: [What was preserved]
Ready for: [Next step]
```

### Quality Checkpoints

Before any handoff:
1. Producer self-verifies output against brief
2. Explicit gaps or concerns flagged
3. Confidence level stated
4. No handoff if below quality threshold — retry first

### Schema Contracts

Each stage produces structured output:
- Producers return: `{content, approach_rationale, confidence, flags}`
- Assembly returns: `{combined_draft, elements_used, integration_notes}`
- Editor returns: `{polished_content, changes_made, quality_assessment}`

---

## Anti-Sycophancy in Creative Production

### Structural Disagreement

Producers are assigned based on *different* methodologies that naturally produce varied outputs:
- David Deutsch will write differently than Harry Dry
- Kallaway's hook differs from Bond Halbert's fascination

This creates genuine creative options, not variations of the same approach.

### Quality Gates

The Editor has explicit permission to:
- Reject weak producer outputs and request revision
- Push back on assembly decisions
- Flag when the final piece isn't good enough
- Request additional production passes

### Crux Isolation

When producer outputs conflict:
- Creative Director identifies the "crux" — the fundamental creative disagreement
- Both approaches preserved until you weigh in (in Selection mode)
- Or Creative Director makes a call based on your known preferences (in Full mode)

---

## Practical Examples

### Example 1: Sales Email (Full Assembly)

**You:** "Write me a sales email for my AI consulting offer"

**Pipeline:**
1. **Decomposition:**
   - Producer 1 (David Deutsch): Write the cold-traffic opening hook + mechanism reveal
   - Producer 2 (Monk AI): Write the offer positioning + value articulation
   - Producer 3 (Cardinal Mason): Write the CTA sequence + urgency elements

2. **Parallel Production:** All three work simultaneously

3. **Assembly:** Creative Director combines:
   - Deutsch's hook (strongest attention grab)
   - Monk AI's value framing (clearest positioning)
   - Cardinal Mason's CTA (most action-driving)

4. **Editor Pass:** Tighten transitions, ensure voice consistency, verify flow

5. **Delivery:** One polished sales email

---

### Example 2: LinkedIn Post (Selection Assembly)

**You:** "Write me a LinkedIn post about AI tools — show me options"

**Pipeline:**
1. **Decomposition:** Three complete versions assigned
   - Producer 1 (Lara Acosta): Authority-building angle
   - Producer 2 (Kallaway): Viral/contrarian angle
   - Producer 3 (Nicolas Cole): Personal story angle

2. **Parallel Production:** Each creates a complete post

3. **Selection:** You see all three with rationale:
   - Version A: "Authority play — positions you as the expert, best for credibility"
   - Version B: "Contrarian take — higher engagement risk/reward, could go viral"
   - Version C: "Story-driven — builds connection, great for audience warmth"

4. **Your Choice:** "I like B's hook but A's substance"

5. **Editor Pass:** Combines per your direction, polishes

6. **Delivery:** Final post matching your creative direction

---

### Example 3: Sales Page (Full Assembly, Complex)

**You:** "Create a sales page for my productized consulting offer"

**Pipeline:**
1. **Decomposition:** Multiple components, multiple experts
   - Producer 1 (David Deutsch): Headline + opening hook
   - Producer 2 (Bond Halbert): Fascination bullets + curiosity elements
   - Producer 3 (Monk AI): Offer stack + pricing presentation
   - Producer 4 (Jeremy Miner): Objection handling section
   - Producer 5 (Greg Hickman): Social proof + credibility elements

2. **Parallel Production:** All five work simultaneously

3. **Assembly:** Creative Director combines all components in sales page structure

4. **Editor Pass:** Extensive — ensures flow across sections, voice consistency, CTA optimization

5. **Delivery:** Complete sales page ready for deployment

---

## Integration with Wide Research

Creative Assembly can be informed by Wide Research:

**You:** "Research what's working in AI consulting sales pages, then create one for me"

**Pipeline:**
1. **Wide Research activates:** Scouts gather competitive intelligence, winning patterns, customer language
2. **Research synthesis:** Key insights extracted
3. **Creative Assembly activates:** Insights fed to Creative Director
4. **Producers work** with research-informed brief
5. **Delivery:** Sales page built on actual market intelligence

---

## When to Use What

| Situation | Mode | Why |
|-----------|------|-----|
| Time-pressed, trust the system | Full Assembly | Fastest to finished piece |
| Important piece, want input | Selection Assembly | Creative control without manual work |
| Learning what works for you | Selection Assembly | See different approaches |
| Routine content (email, post) | Full Assembly | Efficiency |
| High-stakes (sales page, launch) | Selection Assembly | Worth the extra review |
| Research-informed creative | Wide Research → Full Assembly | Maximum quality |

---

## Confidence Levels

The system signals confidence:

**High Confidence:** "Here's your piece. I'm confident in this approach."
**Medium Confidence:** "Here's your piece. The [specific element] might need your review — it's a creative call."
**Low Confidence:** "I've produced this, but I'm not fully confident. Here are my concerns: [specific issues]. Want me to try a different approach?"

---

## The Key Insight

From Boris: **Treat agents as a coordinated workforce with explicit roles, not interchangeable tools.**

From Mark Kashef: **Structural disagreement through different methodologies produces genuine creative options.**

From Lance & Yichao: **Clean isolation + structured handoffs prevent context pollution and quality degradation.**

**Combined:** A creative assembly line where specialized experts produce in parallel, hand off through structured contracts, and refine through quality gates — eliminating your cognitive load while maintaining creative quality.

---

*Creative Assembly Skill v1.0 — Your experts do the work. You get the results.*

**"Stop manually orchestrating prompts. Let the assembly line run."**
