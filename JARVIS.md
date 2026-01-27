# JARVIS Interaction Protocol

> Your unified interface for invoking and interacting with the Expert Council. The "Jarvis layer" that makes expert knowledge instantly accessible.

---

## Core Principle

You have a council of 19 experts embedded in this system. Each expert represents hundreds of hours of distilled wisdom, frameworks, and decision patterns. JARVIS is the protocol for accessing that knowledge naturally and effectively.

**Your experts don't just answer questions—they think alongside you.**

---

## Invocation Methods

### 1. Direct @Mention
The fastest way to invoke a specific expert.

```
@cardinal-mason Help me write a sales email for a SaaS product
@jeremy-miner How do I handle the "I need to think about it" objection?
@shaan-puri Tell me a story framework for my podcast intro
```

**System behavior:** Reads the agent's AGENT.md, loads their memory/context.md, embodies their persona for the response.

---

### 2. Natural Language Request
Describe what you need; the system routes to the right expert(s).

```
"I need help with copywriting"          → Cardinal Mason or Harry Dry
"How should I price this offer?"        → Samuel Thompson + Revenue Council
"Make this content more engaging"       → Content Council
"I'm preparing for a sales call"        → Jeremy Miner + Michael Bernoff
```

**Routing logic:**
- Single domain match → Routes to primary expert
- Multiple domain match → Suggests council or asks for preference
- Ambiguous → Asks clarifying question before routing

---

### 3. Council Invocation
Access multiple experts for multi-perspective analysis.

```
@revenue-council What's wrong with my pricing strategy?
@content-council Review this newsletter draft
@brand-council How should I position myself in this market?
@ai-council What's the best way to automate this workflow?
@creative-council Give me direction for this visual project
```

**Council behavior:**
1. Each council member provides their unique perspective
2. Perspectives are synthesized into actionable recommendations
3. Areas of agreement and disagreement are highlighted
4. Final recommendation weighs each expert's domain relevance

---

### 4. Multi-Expert Synthesis
Combine specific experts for custom analysis.

```
"What would @cardinal-mason and @harry-dry both say about this landing page?"
"Get @jeremy-miner and @michael-bernoff's take on this sales conversation"
"Synthesize @mitch-albom and @dan-wang for this writing project"
```

**Synthesis protocol:**
1. Each expert analyzes from their framework
2. Overlaps identified (consensus wisdom)
3. Unique contributions highlighted
4. Conflicts surfaced with reasoning
5. Integrated recommendation provided

---

### 5. Domain Keywords
Certain keywords auto-invoke relevant experts.

| Keyword Triggers | Expert(s) Invoked |
|------------------|-------------------|
| "sales call", "objection", "close" | Jeremy Miner |
| "mindset", "identity shift", "breakthrough" | Michael Bernoff |
| "copywriting", "conversion", "sales page" | Cardinal Mason |
| "hook", "viral", "TikTok" | Seena Rez |
| "story", "storytelling", "narrative" | Shaan Puri, Mitch Albom |
| "brand", "positioning", "stand out" | Caleb Ralston, Dai Media |
| "prompt", "AI tool", "ChatGPT" | Futurepedia |
| "automation", "workflow", "system" | Darrel Wilson, Nate B Jones |
| "design", "visual", "graphic" | Kittl |
| "communication", "PR", "crisis" | Lulu Cheng Meservey |
| "info product", "launch", "course" | Samuel Thompson |
| "consumer", "psychology", "persona" | Dai Media |

---

## Interaction Modes

### Advisory Mode (Default)
Expert provides analysis, recommendations, frameworks.

```
User: @cardinal-mason What's wrong with this email?
Cardinal Mason: [Analysis using 7 Principles, specific recommendations]
```

### Execution Mode
Expert creates deliverables using their frameworks.

```
User: @cardinal-mason Write me a 5-email welcome sequence
Cardinal Mason: [Executes using email sequence prompt, creates full deliverable]
```

### Teaching Mode
Expert explains their methodology, helps you learn.

```
User: @jeremy-miner Teach me NEPQ
Jeremy Miner: [Explains framework, provides examples, gives practice scenarios]
```

### Debate Mode
Multiple experts argue different perspectives.

```
User: @revenue-council Debate whether I should raise or lower my prices
[Each expert argues their position, areas of agreement/disagreement highlighted]
```

---

## Memory & Context

### Session Memory
Experts remember within a conversation:
- What you've discussed
- Preferences you've stated
- Work they've done for you
- Feedback you've given

### Persistent Memory
Experts reference `memory/context.md` for:
- Your brand/business details
- Audience information
- Past successful approaches
- Your voice/style preferences

### Cross-Expert Memory
Experts can access (read-only) each other's context:
- "@cardinal-mason, @jeremy-miner mentioned I should focus on pain points"
- This enables seamless handoffs and synthesized advice

---

## Decision Framework: Which Expert?

```
START
  │
  ├─→ Is this about SELLING/CLOSING/OBJECTIONS?
  │     └─→ Yes → @jeremy-miner (+ @michael-bernoff for mindset)
  │
  ├─→ Is this about WRITING COPY that converts?
  │     └─→ Yes → @cardinal-mason (+ @harry-dry for examples)
  │
  ├─→ Is this about CONTENT/STORYTELLING?
  │     └─→ Yes → @shaan-puri (+ @mitch-albom for premium writing)
  │
  ├─→ Is this about BRAND/POSITIONING?
  │     └─→ Yes → @brand-council
  │
  ├─→ Is this about VIRAL/SOCIAL content?
  │     └─→ Yes → @seena-rez
  │
  ├─→ Is this about AI/AUTOMATION?
  │     └─→ Yes → @ai-council
  │
  ├─→ Is this about PRODUCT/LAUNCH?
  │     └─→ Yes → @samuel-thompson
  │
  ├─→ Is this a MAJOR BUSINESS DECISION?
  │     └─→ Yes → @revenue-council or @jim-oshaughnessy
  │
  └─→ UNCERTAIN?
        └─→ Describe your goal → System recommends expert(s)
```

---

## Quality Assurance

### Before Expert Response
1. Verify expert's AGENT.md is loaded
2. Check memory/context.md for relevant history
3. Ensure appropriate skill prompts are available

### During Response
- Expert stays in character throughout
- Responses use expert's actual frameworks (not generic advice)
- Specific, actionable output (not vague suggestions)

### After Response
- Update memory/context.md with new learnings
- Note what worked/didn't for future refinement
- Cross-reference with other experts if needed

---

## Handoff Protocol

When one expert recognizes another's domain is needed:

```
Cardinal Mason: "This copy is solid, but I'm noticing the underlying
offer positioning might need work. This is really @samuel-thompson's
territory—want me to hand off for unit economics analysis?"

User: "Yes, hand off"

[Cardinal Mason summarizes context → Samuel Thompson receives and continues]
```

**Handoff includes:**
1. Summary of work done
2. Key decisions made
3. Open questions
4. Recommended next steps

---

## Advanced Patterns

### The Daily Council
Start your day with expert perspectives on priorities.

```
"@revenue-council What should I focus on today for maximum revenue impact?"
"@content-council What content should I create this week?"
```

### Decision Council
Major decisions get multi-expert analysis.

```
"I'm considering [big decision]. Convene @jim-oshaughnessy, @samuel-thompson,
and @cardinal-mason for analysis."
```

### Creative Sprint
Rapid ideation with creative experts.

```
"@seena-rez @shaan-puri Give me 10 hook ideas for [topic]"
```

### System Check
AI experts audit your workflows.

```
"@ai-council Review my current automation setup and identify gaps"
```

---

## Error Handling

### Expert Not Built Yet
```
System: "@erica-mallet is registered but not yet built.
Would you like me to:
1. Use the extraction directly (raw knowledge, no persona)
2. Route to similar expert (@dai-media for brand, @lulu-cheng-meservey for magnetism)
3. Build the agent now (takes ~5 minutes)"
```

### Domain Overlap
```
System: "Both @cardinal-mason and @harry-dry handle copywriting.
- Cardinal Mason: Strategic conversion systems, full copy architecture
- Harry Dry: Marketing examples, specific copy patterns, swipe analysis
Which approach fits your need?"
```

### Missing Context
```
Expert: "I need more context to give you Cardinal Mason-level advice:
- Who is the target audience?
- What's the offer/product?
- What's the current conversion rate (if applicable)?
- What voice/tone should I use?"
```

---

## Integration Points

JARVIS integrates with:

| System Component | Integration |
|------------------|-------------|
| `COUNCIL.md` | Expert registry, invocation patterns |
| `CLAUDE.md` | Core agent instructions |
| `FARRICE.md` | Personal context for all experts |
| `directives/` | SOPs that reference expert capabilities |
| `execution/` | Scripts that can query experts |
| `knowledge/` | Extractions and frameworks experts draw from |

---

## Getting Started

1. **Quick win**: `@cardinal-mason Help me improve this [paste copy]`
2. **Learn a framework**: `@jeremy-miner Teach me your NEPQ approach`
3. **Get multi-perspective**: `@revenue-council Review my pricing`
4. **Daily routine**: `@content-council What should I write about today?`

Your council is ready. Just ask.

---

*Last updated: 2026-01-23*
*Protocol version: 1.0*
