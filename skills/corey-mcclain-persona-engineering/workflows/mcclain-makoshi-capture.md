---
name: Makoshi State Capture
command: /mcclain-makoshi-capture
expert: Corey McClain
category: Foundation
description: State capture and preservation — Makoshi protocol for maintaining expert intelligence
inputs: Active agent or conversation session with high-quality outputs
outputs: Makoshi construct file — portable, reusable expert intelligence state
---

# Makoshi State Capture

Capture and preserve the intelligence state of an AI agent at peak performance. Named after the Cyberpunk 2077 concept — a portable shrine housing a digitized mind. When an agent is producing exceptional work, the Makoshi protocol captures that state as a reusable construct, preventing the quality fluctuation that degrades performance across sessions.

## Workflow

### Step 1 — Peak State Identification

Determine if the current state is worth capturing:
- Is the agent producing outputs above its normal baseline?
- Have refinements, corrections, or context accumulated that improve quality?
- Would losing this conversation state meaningfully degrade future output?
- Is there tacit knowledge in the session that isn't documented elsewhere?

**Decision**: If yes to 2+ questions → proceed with capture. Otherwise, standard memory logging is sufficient.

### Step 2 — Intelligence Extraction

Extract the components that define the current state:

**Behavioral Patterns Observed**:
- What decisions is the agent making consistently that weren't in the original instructions?
- What quality standards has it internalized through feedback?
- What corrections has it absorbed and now applies automatically?

**Context Accumulated**:
- What domain knowledge has been built through the conversation?
- What preferences, constraints, or standards have been established?
- What examples has the agent seen that now calibrate its output?

**Voice State**:
- How has the agent's communication style refined during the session?
- What tone, vocabulary, or structural choices has it settled into?

### Step 3 — Construct Assembly

Write the Makoshi construct file:

```markdown
# [Agent Name] — Makoshi Construct
## Captured: [Date]
## Context: [What the agent was doing when captured]

### Behavioral DNA
[List the internalized behaviors — decisions it makes without being told]

### Accumulated Intelligence
[Domain knowledge, preferences, standards built through interaction]

### Calibration Anchors
[Specific examples or outputs that represent the quality ceiling]

### Voice State
[Current communication style — tone, vocabulary, cadence, texture]

### Refinement History
[Key corrections or adjustments made during the session]

### Reconstruction Instructions
[How to restore this state in a new session — what to load, in what order]
```

### Step 4 — Portability Test

Verify the construct works:
1. Start a fresh session with no conversation history
2. Load the Makoshi construct file
3. Run the same type of task the agent was performing when captured
4. Compare output quality — it should approach (not necessarily match) the peak state

### Step 5 — Version Management

Track construct evolution:
- Date and context of each capture
- What changed between versions
- Which version produces the highest quality for which task types
- Archive older versions, don't delete — they may be useful for different contexts

---

## Quality Gate

- [ ] Construct captures behavioral patterns, not just knowledge
- [ ] Calibration anchors include actual output examples
- [ ] Reconstruction instructions are specific enough for a cold start
- [ ] Portability test shows quality improvement vs. baseline
- [ ] Version is tagged with date and context
