# /spiegel-empathy — Customer Empathy Sprint

> Listen deeply, then ignore the request. Extract the emotional substrate, then invent something customers didn't know they needed.

## When to Use
- Building something new and need to understand customers deeply
- Processing customer feedback and tempted to build exactly what they asked for
- Product/service feels misaligned with what customers actually want
- Pre-development research phase for any new offer

## Inputs Required
1. Customer segment or problem space
2. Existing customer feedback/requests (if any)
3. Access to 3-5 current or potential customers for deep listening
4. Current assumptions about what customers want

## Execution Steps

### Step 1: Deep Listening Protocol Design
Create your interview guide (NOT a survey):
- **Duration**: 1-2 hours per session. Short sessions yield surface-level data.
- **Opening**: "Tell me about how [technology/product category] fits into your daily life."
- **Core questions**: Focus on feelings, frustrations, and desires — NOT features
  - "What frustrates you most about [current solution]?"
  - "When do you feel [negative emotion] using [product category]?"
  - "Describe a moment when [product category] made you feel great."
  - "If you could change one thing about how you [activity], what would it be?"
  - "Walk me through yesterday — when did [product/technology] come up?"
- **Never ask**: "What features do you want?" (They'll tell you anyway.)

### Step 2: Dual-Track Logging
During each session, maintain two separate logs:

**Track A — Explicit Requests** (what they literally ask for)
| Customer | Explicit Request | Feature Implied |
|---|---|---|
| | | |

**Track B — Emotional Substrate** (what they actually feel)
| Customer | Feeling Expressed | Underlying Need | Trigger Situation |
|---|---|---|---|
| | | | |

### Step 3: Substrate Synthesis
After all sessions, synthesize Track B:
1. Cluster emotions by theme (pressure, frustration, desire, anxiety, delight)
2. Identify the 2-3 dominant emotional substrates across all customers
3. Write each substrate as: "Customers feel [emotion] when [trigger] because [underlying need]"
4. Cross-reference with Track A: do the explicit requests actually address these substrates?

### Step 4: The Invention Brief
Using the substrates, NOT the feature requests:
1. **Design constraint**: "This solution must address [substrate] without implementing [explicit request]"
2. **Emotional target**: "After using this, customers should feel [desired emotion] instead of [current emotion]"
3. **The Stories Test**: Could this become a format/experience that others copy? (If yes, you're inventing. If no, you're iterating.)

### Step 5: Rapid Prototyping Direction
Generate 10+ concepts that address the substrates:
- Use GP-7 (Velocity-of-Ideation): volume kills preciousness
- None of the 10 should be the explicit feature request
- Score each against the emotional target from Step 4
- Select top 3 for prototyping

## Output Format
```
## EMPATHY SPRINT — [Customer Segment]

### Sessions Conducted: X

### Explicit Requests (Track A)
[List of what customers literally asked for]

### Emotional Substrates (Track B)
1. "Customers feel ___ when ___ because ___"
2. "Customers feel ___ when ___ because ___"
3. "Customers feel ___ when ___ because ___"

### The Gap
[How explicit requests fail to address the real substrates]

### Invention Brief
- Design constraint: [address substrate without implementing request]
- Emotional target: [desired feeling vs. current feeling]
- Stories Test: [Is this inventive enough to be copied?]

### Top 3 Concepts
[Brief descriptions with substrate alignment scores]

### Recommended Next Workflow
[/spiegel-offer for full pipeline, /spiegel-distribution for launch planning]
```

## Quality Gate
- Must conduct actual deep sessions (1-2 hours), not surveys or 15-minute calls
- Dual-track logging must be maintained separately — no mixing requests with feelings
- At least 2 dominant substrates must be identified
- Invention brief must explicitly EXCLUDE the literal feature requests
- Top concepts must NOT be what customers asked for

## Stacking
- **× Dai Media (Consumer Posture)** → 3D consumer identity for deeper substrate extraction
- **× Kallaway (Audience Obsession)** → Obsession engineering on discovered substrates
- **× ICP Deep Dive** → Pre-empathy market intelligence for targeted sessions
