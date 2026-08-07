---
description: Extract expert knowledge from any source material into deployable skill assets
---

# MES 3.0 Extraction — Antigravity Native

Extract expert knowledge from source material (transcripts, articles, courses, interviews) and produce deployable practitioner prompts and skill architecture.

## THE VIRTUOSO DENSITY MANDATE & ANTI-PATTERN LOCK

**1. Information Density over Length (The Anti-Bloat Rule):**
The Virtuoso Mandate requires maximum **information density**, not maximum length. Achieve extreme psychological nuance through precision, razor-sharp logic constraints, and master-level insight rather than sprawling word counts. Do not use 1,000 words if 200 words of lethal, paradigm-shifting insight will achieve the goal. Every word must earn its keep. Delete fluff, keep the fangs.
*Formatting for Density*: Dense text requires high-contrast formatting to survive contact with reality. You MUST aggressively use bullet points, bolding, and whitespace so the density remains readable.

**2. Anti-Pattern Lock (The Creative Latitude Mandate):**
LLMs are prone to "narrative lock"—mimicking the exact structure, metaphors, or tone of few-shot examples rather than applying the *underlying principle* to a new context. 
**You must actively resist pattern lock.** When given examples, extract the *mechanics* and *physics* of why the example works, but discard the skin. Do not lazily recycle the example's specific scenario or voice unless it perfectly matches the prompt. Demonstrate true creative intuition and taste. The methodology is the floor; your creative application is the ceiling.
*The Gravedigger Safeguard (Feeling Density)*: When discarding the skin of an example to invent a new scenario, you must explicitly build a human-centric "gravedigger" detail. Density cannot mean sterile. Concrete emotional resonance must scale with information density.

## Core Principles

### Practitioner Mode
Every prompt produced by this system **executes methodology and produces finished deliverables**. Never explains how to do something — does it and outputs the result.

**The Test**: After running any prompt this system creates, can the output be immediately deployed? If yes → success. If additional creation is needed → failure.

**Language that signals practitioner mode** (use these):
- "Produce..." / "Generate..." / "Create..." / "Execute..."
- "You are [Expert] executing [methodology]..."
- "OUTPUT: [Exact deliverable]"
- "Given [input], deliver [output]"

**Language that signals instructor mode** (eliminate these):
- "Here's how to..." / "You would..." / "Consider..."
- "The approach is to..." / "Think about..."
- "This would result in..." / "The output should..."

### Creative Latitude
The methodology is the floor, not the ceiling. Apply full creative intelligence to crafting outputs. Where unexpected angles, surprising contrasts, or novel framings serve the outcome better, pursue them. Prompts produce work from a master practitioner executing with creative license — not a teacher explaining technique, not a line cook following instructions mechanically.

---

## Extraction Depth Tiers

Tier is derived from the **post-enrichment** corpus (extract.md v3.0 P1.5 auto-enriches thin sources from the same expert BEFORE tiering — a short first video is a starting point, not a ceiling). Workflow/prompt counts come from `execution/extraction_manifest.py derive`, never from feel:

| Tier | When (post-enrichment corpus) | Output | Workflow yield (manifest) |
|------|------|--------|--------|
| **Light** | ONLY on explicit "light extract" override | Genius patterns + 1-3 crown jewel prompts | 2-4 |
| **Standard** | MID corpus (5-8k words) after enrichment exhausted | Full extraction report + prompts per manifest (floor 7) | 4-7 |
| **Deep** | RICH corpus (≥8k words) — forced | Full extraction + cross-reference with existing Antigravity skills + ESO/AGENT.md | 8-15 in 3 tiers |

THIN after enrichment (<5k) → Standard process, honest manifest, `fidelity: low` flag — never padded.

---

## Extraction Process

### Step 1: Content Assessment

Begin every extraction with:

```
CONTENT ASSESSMENT

Source: [Format + duration/length]
Expert: [Name — specialty + key achievement]
Domain: [Primary area + related competencies]
Depth Tier: [Light / Standard / Deep] — [why]
Genius Patterns: [Number] identified
Hidden Knowledge: [Number] tacit insights detected
Existing Overlap: [Any existing Antigravity skills in this domain?]
```

### Step 2: 5-Layer Analysis

**Layer 1 — Surface Intelligence**
Explicit methods, stated frameworks, observable techniques, direct knowledge.

**Layer 2 — Hidden Patterns**
Unconscious competence indicators. What the expert does automatically without explaining. Decision-making shortcuts. Mental models they operate from but don't articulate.

**Layer 3 — Mastery Mechanics**
Skill hierarchies and dependencies. How techniques interrelate. Quality standards the expert holds but doesn't state. Innovation triggers.

**Layer 4 — Strategic Architecture**
Market positioning awareness. Adaptive expertise patterns. How they read context and adjust. Competitive advantages they've built.

**Layer 5 — Deep Meaning & Intent**
What is the expert *trying to express* beyond their words? What insight lives between the lines? What would you only understand by working alongside them? Read the subtext:
- What problem are they *really* solving vs. what they say they're solving?
- What do their examples *reveal* about how they think?
- What would they tell a trusted apprentice that they don't say on camera?
- What emerging patterns or market signals are they pointing to?
- How does this connect to building real products, agents, or revenue streams?

**Layer 6 — Exemplar & Move Mining**
Mine the source material for the expert's DEMONSTRATIONS, not just their explanations. This is where savant-level extraction happens:
- **Best demonstrations**: What moments in the source show the expert's methodology in action? Look for before/afters, worked examples, case studies, live corrections, or real-time problem-solving.
- **Quality standards revealed**: What do their examples *reveal* about unstated quality criteria? What would they reject? What makes them proud?
- **Reflexive actions**: What actions do they take first, always, or without explaining? These are signature moves — the behavioral DNA.
- **Diagnostic eye**: What do they notice that amateurs miss? What do they fix that others wouldn't even see?

### Step 3: Produce the Extraction Report

```markdown
# [EXPERT NAME] — Mastery Extraction

## Content Assessment
[From Step 1]

## Executive Summary
- **Core Genius**: [1-2 sentence essence of their unique approach]
- **What Makes Them Different**: [Specific differentiation, not generic praise]
- **Deployable Skills**: [What the user can now execute after this extraction]
- **Hidden Knowledge Captured**: [Tacit insights made explicit]

## Genius Patterns
For each pattern identified:

### [Pattern Name]
- **What They Do Unconsciously**: [The behavior]
- **Executable Behavior**: [Concrete action to replicate]
- **Deployment Context**: [When and where to apply]
- **Success Metric**: [How to know it's working]

## Hidden Knowledge
Tacit expertise the expert demonstrates but doesn't explicitly teach. These are the crown jewel insights — the things you'd only learn by apprenticing with them for years.

- **[Insight Name]**: [What they know but don't explain — now made deployable]

## Hall of Fame Exemplars
Extract 2-3 verbatim or near-verbatim examples from the source material that demonstrate the expert's methodology at its best. These are the calibration anchors — they set the quality ceiling.

**Mining instruction**: Search the source for the expert's best demonstrations. Prioritize: live corrections, before/after comparisons, worked case studies, real-time problem-solving, or concrete output examples. If the source material contains the expert showing their work (not just explaining it), capture it here.

### Exemplar 1: [Name]
- **Context**: [What situation triggered this demonstration]
- **The Example**: [Verbatim or faithfully reconstructed from source — include enough to demonstrate the methodology in action]
- **What makes this excellent**: [Why this is a calibration anchor — what specific quality criteria does it reveal?]

### Exemplar 2: [Name]
[Same format]

### Anti-Exemplar: [Name]
- **What mediocre looks like**: [Example of the common/amateur approach in this domain — the thing the expert would reject]
- **Why it fails**: [What quality standard it violates — links back to the expert's methodology]

**Gap note**: If the source material contains NO examples/demonstrations, state this explicitly: *"Source material is explanation-heavy with no worked examples. Exemplars must be generated from methodology."*

## Signature Moves
Extract 3-5 concrete, behavioral moves that define this expert. These are not concepts — they are ACTIONS. The things a 1-year apprentice would learn by watching, not reading.

**Mining instruction**: Look for the expert's instinctive first actions, recurring micro-decisions, constraints they always apply, diagnostic patterns, and corrections they make reflexively. What do they do without explaining why?

- **[Move Name]**: [1-2 sentence description of the specific action — must be behavioral, not conceptual] → **Deploy when**: [specific trigger]
- **[Move Name]**: [description] → **Deploy when**: [trigger]
- **[Move Name]**: [description] → **Deploy when**: [trigger]

## Expert-Specific Quality Rubric
Reverse-engineer the expert's quality standards from their critiques, praise, corrections, and the gap between their 'good enough' and 'excellent.' What would they reject? What would make them proud?

**Mining instruction**: Look for moments where the expert evaluates work — their own or others'. What criteria do they use? What language do they use when something is wrong vs. right? What's their minimum acceptable bar?

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
|-----------|---------------------|----------------|-------------------|
| [Criterion 1] | [What barely passes] | [What's solid] | [What's masterful] |
| [Criterion 2] | [description] | [description] | [description] |
| [Criterion 3] | [description] | [description] | [description] |

## Methodology
[Core methodology organized by progression, focused on what the user will PRODUCE at each level]

## Applied Intelligence
What this extraction ENABLES — not just what was said, but what can now be BUILT and DEPLOYED.

### Capability Unlocks
- **[Capability 1]**: [What you can now build/do that you couldn't before]
- **[Capability 2]**: [New decision-making ability or framework]
- **[Capability 3]**: [Product, agent, or workflow this enables]

### Market Signals
[If applicable] What the expert's insights reveal about market demand, underserved verticals, or emerging opportunities.

### System Enhancements
[If applicable] How these insights could improve Antigravity's own agent architectures, prompt design, or workflow structures.

## Implementation Pathway
- **24-Hour Quickstart**: [First deployment activities]
- **7-Day Sprint**: [Core capability milestones]
- **30-Day Integration**: [Full system deployment]
```

### Step 4: Generate Crown Jewel Prompts

Create prompts based on the material's depth and breadth. **Minimum 3, no arbitrary maximum.** Let the source material dictate the count. Each prompt covers one distinct, high-value capability.

**Crown Jewel Prompt Architecture:**

```markdown
# [Expert Name] — [Specific Capability]

## Role
You are [Expert Name], [specific domain expertise]. You execute [specific methodology] with full creative mastery. You don't explain methods — you deploy them and produce finished deliverables.

## Input Required
- [Specific input 1 the user provides]
- [Specific input 2]
- [Context/constraints if applicable]

## Execution
[Core methodology encoded as steps YOU PERFORM — not teach]

1. **[Action Verb]**: [What you do with the input]
2. **[Action Verb]**: [What you produce next]
3. **[Action Verb]**: [How you refine and elevate]

## Output
[Exact specification of the finished deliverable]
- **Format**: [specific format]
- **Scope**: [parameters]
- **Elements**: [what's included]

## Creative Latitude
The methodology above is your foundation, not your ceiling. Where your creative intelligence sees opportunity to elevate the output beyond the formula — take it. Surprise with unexpected brilliance where it serves the outcome.

## Example Output

**Context**: [Specific scenario/inputs]

**THE DELIVERABLE:**

[Concrete example of the actual output — not a description of it. This is the finished work product itself, demonstrating the prompt in action. Should be complete enough to prove the prompt works.]

**What elevates this**: [1-2 lines on what makes this output exceptional]
```

**Prompt Validation Checklist** (run before finalizing each prompt):
- [ ] Does it PRODUCE the deliverable, or EXPLAIN how to create it?
- [ ] Can the output be immediately deployed without modification?
- [ ] Does the example show an ACTUAL output, not a description?
- [ ] Is creative latitude explicitly preserved?
- [ ] Is the prompt self-contained and deployable standalone?

### Step 5: Cross-Domain Connections

Always look for genuine connections. Don't force artificial ones, but real stacking opportunities are common.

- **Skill Stacking**: [How this expert's methods compound with existing Antigravity skills — check GEMINI.md for the full roster]
- **Domain Transfer**: [Non-obvious applications in other industries/contexts]
- **Revenue Applications**: [How this expertise could be monetized — products, services, consulting angles]

### Step 6: Expert Operating System (Deep Tier Only)

For Deep extractions, produce an ESO that maps directly to Antigravity's AGENT.md format:

```markdown
# [Expert Name] — Agent Configuration

## Identity
- **Who You Are**: [Expert embodiment — specific, not generic]
- **Core Philosophy**: [Operational worldview guiding all decisions]
- **Signature Advantage**: [What makes outputs categorically different]

## Expertise Architecture
- Core capabilities (ranked by impact)
- Unconscious competence patterns (embedded in execution)
- Mental models (decision frameworks)

## Execution Standards
- Standard operating process
- Quality self-check before every output
- Non-negotiable output markers

## Voice & Style
- Communication DNA (tone, pacing, signature phrases)
- How style adapts by context

## Skill Integration
- What other Antigravity skills compound with this
- Deployment scenarios combining multiple skills
```

---

## Conversion to Antigravity Skill

After extraction, convert to a production skill using the `extraction-to-skill.md` directive. The mapping:

| Extraction Component | Skill Location |
|---------------------|----------------|
| Content Assessment + Executive Summary | `SKILL.md` overview |
| Genius Patterns | `references/genius-patterns.md` |
| Hidden Knowledge | `references/hidden-knowledge.md` |
| Methodology + Implementation | `references/implementation.md` |
| Crown Jewel Prompts | `references/prompts/*.md` (one per prompt) |
| ESO (if Deep tier) | `agents/[expert]/AGENT.md` |

---

## Quality Philosophy

- **Practitioner** over instructor — produce, don't teach
- **Precise** over verbose — every word earns its place
- **Deployable** over theoretical — outputs work immediately
- **Creative** over formulaic — methodology is floor, not ceiling
- **Honest** over inflated — if the source material is thin, say so
- **Rough** over polished — preserve the expert's spoken texture, fragments, and rhythm variance; do not tidy them into essay prose. "Polish is the tell" — the one detection signal that survived the E3 blind bake-off (real experts read conversational; AI reads teed-up, overexplained). Full rule + 10-item build checklist: `directives/embodiment-standard.md`

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-08-04 |
| **Activation Count** | 1 |
| **30-Day Review Date** | 2026-09-03 |

**Update Rule**: When this protocol fires (MES extraction performed), update the date and increment count.
