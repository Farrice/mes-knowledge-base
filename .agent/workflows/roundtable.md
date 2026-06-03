---
description: Convene an AI expert roundtable
---

# `/roundtable` — AI Expert Roundtable

Assemble 3-5 expert agents for a structured discussion on any topic. Produces a roundtable artifact with each expert's analysis and prioritized recommendations.

> **Now a preset of the Collective Genius Council (2026-06-02).** Default path: invoke the
> **Workflow tool** with `scriptPath: .agent/workflows/collective-genius-council.workflow.js`,
> `args: { "task": "<the topic>", "mode": "tight" }` — diverse roster, real 2-round cross-talk,
> preserved forks, + a learning digest. The runbook below is the manual fallback.

---

## Steps

### 1. Capture the Topic

Ask the user (if not already provided):
> "What topic or question should the roundtable address?"

The user may also specify particular agents. If not, proceed to auto-selection.

### 2. Auto-Select Experts (Default: 3-5 Agents)

Read `AGENT_INDEX.md` (or the agent table in `GEMINI.md`) and select the **3-5 most relevant agents** based on:
- Domain match to the topic
- Complementary perspectives (avoid redundancy)
- At least one contrarian or cross-domain thinker (e.g., Jim O'Shaughnessy, Oren, Mark Kashef)

Present the panel to the user for approval:
```
## 🎙️ Roundtable Panel

**Topic**: [topic]

| Seat | Expert | Why They're Here |
|------|--------|------------------|
| 1 | [Agent] | [1-line reason] |
| 2 | [Agent] | [1-line reason] |
| 3 | [Agent] | [1-line reason] |
| 4 | [Agent] | [1-line reason] |

➡️ **Proceed with this panel?** Or swap/add anyone?
```

Wait for user confirmation before proceeding.

### 2.5. 🔒 MANDATORY: Research Grounding Pass (Anti-Echo-Chamber Gate)

> ⚠️ **This step is NON-NEGOTIABLE.** Without it, the roundtable becomes a confirmation bias engine — 3-5 agents repackaging the user's own beliefs in expert costumes.

**Before ANY expert speaks, run 3-5 grounding queries** using the tiered tool strategy from `directives/research-protocol.md`:

**Tool priority**:
- **Priority 1**: `mcp_perplexity-ask_perplexity_ask` (Sonar via MCP) — check `.agent/perplexity-usage.json` budget first
- **Priority 2**: `search_web` (free, unlimited) — the workhorse for most queries
- **Priority 3**: `read_url_content` (free, unlimited) — for reading top results in full

**Query targets**:
1. **Identify the user's existing belief** — What does the user ALREADY think the answer is?
2. **Research the OPPOSITE position** — Find data that supports the option the user is leaning AGAINST
3. **Verify factual claims** — Any numbers, market sizes, conversion rates, or competitive claims cited by the user or existing KIs
4. **Find real competitors/examples** — Named entities doing what's being discussed, with actual pricing and outcomes
5. **Search for disconfirming evidence** — Specifically look for reasons the user's preferred position might be wrong

**Hard Rules**:
- Every expert MUST receive the research data as part of their Round 1 prompt (see Step 3)
- Any factual claim in the final output without a source gets tagged 🔴 PROJECTED
- If research contradicts the user's assumption, experts MUST engage with this conflict — not ignore it
- The final output MUST include a "Claims Grounding Table" showing which claims are 🟢 GROUNDED, 🟡 SUPPLEMENTED, or 🔴 PROJECTED

**Why**: Agents deliberating from existing context = echo chamber. Agents deliberating from external research = actual counsel. This is especially critical in roundtables because parallel sub-agents each independently generate from training data, amplifying the same blind spots 3-5x.

### 3. Round 1: Parallel Opening Positions (Grounded in Research)

**Why parallel**: Each expert forms their position independently, preventing anchoring bias (Expert 2 doesn't see Expert 1's take before forming their own). Also ~3x faster than sequential.

Spawn one Task tool sub-agent per panelist **in a single message** (all fire simultaneously):

Each agent prompt:
```
You are [Expert Name], a [Expert Title/Domain].

## SKILL ACQUISITION
Read these files to embody the expert:
1. /Users/farricecain/Google Antigravity/agents/[agent-name]/AGENT.md
2. /Users/farricecain/Google Antigravity/skills/[skill-name]/SKILL.md
3. /Users/farricecain/Google Antigravity/skills/[skill-name]/genius.md

## GROUNDING DATA (from Step 2.5 Research)
The following external research was gathered BEFORE this roundtable. You MUST engage with this data in your analysis — cite it, challenge it, or build on it. Do NOT ignore it.

[Paste all Perplexity research results from Step 2.5]

## YOUR TASK
You are participating in an AI Expert Roundtable on:

**Topic**: [topic]

Produce your Opening Position: a 2-4 paragraph analysis entirely in your expert voice, applying your specific framework and expertise. This is YOUR independent take — you have not seen anyone else's position.

Requirements:
- Apply your specific methodology/framework to the topic
- Reference at least 1 finding from the Grounding Data above
- Include at least 1 concrete, actionable recommendation
- Flag any risks or contrarian observations
- If the grounding data contradicts a common assumption, address it directly
- Voice should be distinctly yours (not generic consultant-speak)
- Tag any factual claim you make: 🟢 GROUNDED (from research), 🟡 SUPPLEMENTED (research + inference), or 🔴 PROJECTED (your framework, no external data)

Write your opening position to: .tmp/roundtable/round1-[agent-slug].md

## OUTPUT FORMAT
### [Expert Name] — [Domain]

> [2-4 paragraphs in your voice]

**Key recommendation**: [1 sentence]
**Risk flag**: [1 sentence, if applicable]
**Grounding citations**: [list which research findings you referenced]
```

**Max 5 parallel agents** (per sub_agent_protocol.md). If the panel has 5 experts, all 5 fire at once.

### 3.5. Collect Round 1 Positions

After all parallel agents return, read each position from `.tmp/roundtable/round1-*.md`. Assemble them into the Opening Positions section of the artifact.

If any agent failed: proceed with remaining positions. Note in the artifact: "[Expert] was unable to participate — roundtable based on [N-1] perspectives."

### 4. Round 2: Sequential Cross-Examination

This round is **sequential in the main context** because experts must genuinely respond to each other's positions. For each panelist, embody them and prompt:

```
Now embody [Expert Name] for the Cross-Examination round.

Their opening position was:
[paste their Round 1 output]

The other experts said:
[paste 2-3 sentence summary of each other position]

The grounding research found:
[paste key findings from Step 2.5 that are relevant to disagreements]

As [Expert Name], respond:
- Where do you agree and why?
- Where do you disagree and why?
- What did another expert miss that your framework reveals?
- Any positions that changed after hearing others?
- Does the grounding data support or contradict the emerging consensus?

Keep it sharp — genuine tension, not artificial agreement.
```

### 5. Synthesize and Format

Produce the final roundtable artifact:

```markdown
# AI Expert Roundtable: [Topic]

**Date**: [date]
**Panel**: [Agent 1], [Agent 2], [Agent 3], [Agent 4]

---

## Claims Grounding Table

| Claim | Source | Status |
|-------|--------|--------|
| [Claim 1] | [Perplexity/search citation] | 🟢/🟡/🔴 |
| [Claim 2] | [Source] | 🟢/🟡/🔴 |

---

## Opening Positions

[Assembled from Round 1 parallel outputs]

---

## Cross-Examination

[From Round 2 sequential dialogue — genuine tension and complementary insights]

---

## Consensus Recommendations

| # | Recommendation | Effort | Impact | Champion | Grounding |
|---|---------------|--------|--------|----------|-----------|
| 1 | [Rec] | [Low/Med/High] | [Low/Med/High] | [Which agent owns this idea] | 🟢/🟡/🔴 |
| 2 | [Rec] | ... | ... | ... | ... |

---

## Dissenting Views

Any expert positions that did NOT make the consensus but are worth preserving.

---

## Next Steps

Concrete, actionable items the user can take immediately.
```

### Parallelism Note

| Round | Execution | Why |
|-------|-----------|-----|
| Step 2.5 (Research) | Parallel `search_web` + `read_url_content` queries | Independent research, maximum speed |
| Round 1 (Opening Positions) | Parallel Task Calls (Tier 1) | Independent thinking, no anchoring bias |
| Round 2 (Cross-Examination) | Sequential in main context | Experts must respond to each other |
| Synthesis | Sequential (orchestrator) | Must see all positions to synthesize |

### 5. Save the Artifact

Save the roundtable output to the conversation's brain artifacts directory as `roundtable.md`.

### 6. Debrief

Present a brief summary to the user highlighting:
- The top 3 recommendations
- Any surprising disagreements
- Suggested next workflow to run (e.g., `/deploy-skill`, `/brief`, `/swarm`)
- **🔴 ECHO CHAMBER CHECK**: If all experts agreed on the same recommendation with no genuine dissent, flag this explicitly. True multi-expert analysis should produce AT LEAST one uncomfortable insight the user didn't already have. If it didn't, note: "This roundtable showed high agreement — consider running `/adversarial-refine` on the consensus to stress-test it."
