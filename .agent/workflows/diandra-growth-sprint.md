---
description: End-to-end growth post flywheel
---

# `/diandra-growth-sprint` — The Growth Post Engine

Takes any brand, person, or news event and produces **3 publish-ready LinkedIn growth posts** with hook alternatives, boomerang playbook, and visual briefs — end to end.

**This is not a prompt template. This is an engine that researches, produces, and assembles.**

## When to Use
- You spotted a brand move, person quote, or news event and want to ride the attention
- You want a complete growth post package without manually running research + writing + strategy
- You need multiple post variations to test angles
- You want to trigger the boomerang effect (get the subject to engage)

## Usage

```
/diandra-growth-sprint [brand/person/news event]
/diandra-growth-sprint "Notion just launched AI agents"
/diandra-growth-sprint "Alex Hormozi" --type namejack
/diandra-growth-sprint --find   (auto-discovers trending entities)
```

---

## Phase 1: Entity Intake & Auto-Detection

**Actor**: Orchestrator

### If entity provided:

1. **Classify the jack type**:

| Signal | Jack Type | Workflow Source |
|--------|-----------|----------------|
| Brand name + business decision | **Brandjack** | 01-brandjack-post-generator.md |
| Industry news/event/announcement | **Newsjack** | 02-newsjack-post-generator.md |
| Individual person + their work/POV | **Namejack** | 03-namejack-post-generator.md |
| Consensus belief you disagree with | **Hot Take** | 04-hot-take-post-generator.md |

2. **Confirm with user**:
```markdown
## Entity Detected
- **Entity**: [name]
- **Jack Type**: [type] — [1-line justification]
- **Proceed with this classification?**
```

### If `--find` mode (no entity provided):

1. Run 3 parallel `search_web` queries:
   - `"[user's niche] brand news announcement 2026"` → brand candidates
   - `"[user's niche] trending LinkedIn thought leader"` → person candidates
   - `"[user's niche] industry news breaking 2026"` → news candidates
2. Use `read_url_content` on top 3 results per query
3. Present 5-7 entity candidates ranked by: recognition × recency × ICP overlap

```markdown
## Trending Entities for [Niche]

| # | Entity | Type | Recency | Recognition | Opportunity |
|---|--------|------|---------|-------------|-------------|
| 1 | [name] | Brandjack | [timeframe] | [1-10] | [1-line] |
| 2 | [name] | Newsjack | [timeframe] | [1-10] | [1-line] |
| ... |

**Pick 1-3 entities to produce posts for. Reply with numbers.**
```

**WAIT FOR USER SELECTION.**

---

## Phase 2: Research Gate (MANDATORY)

**Actor**: Orchestrator + research tools

> No research = no post. Diandra's system works because posts contain specific details, not vibes.

### Run the foundation through the unified research engine:

The entity deep-dive MUST go through the unified engine — it returns a Research Receipt and costs $0 on failure, so the GROUNDED label below is earned, not assumed:

```bash
cd "/Users/farricecain/Google Antigravity" && python3 execution/research.py "[entity] [what happened — specific facts, numbers, dates]" --depth standard --task-context "diandra-growth-sprint"
```

(Gemini-first → Perplexity → Tavily bedrock floor. For a heavier dig use `--depth deep`, which fans out via `.agent/workflows/deep-research-swarm.workflow.js`.)

### Supplementary queries (audience reaction, boomerang recon):

**Tool priority**:
- **Priority 1**: `search_web` (free, unlimited) — the workhorse
- **Priority 2**: `read_url_content` (free, unlimited) — read top 3 results in full
- **Priority 3**: `mcp_perplexity-ask_perplexity_ask` — if budget available and topic requires depth

| Query | Purpose |
|-------|---------|
| Entity deep-dive | What exactly happened? Get specific numbers, dates, details |
| Audience reaction | Reddit, X, LinkedIn comments — how are people reacting? |
| ICP relevance | Why would YOUR audience care about this entity? |
| Boomerang recon | Does the entity/person have active LinkedIn presence? |

### Produce Research Brief:

Save to `.tmp/diandra-growth-sprint/research-[slug].md`:

```markdown
## Research Brief: [Entity]
**Jack Type**: [type] | **Provenance**: [see gate result below]

### Entity Facts (Specific Details)
- [Revenue number, campaign detail, strategic decision — NOT vague summaries]
- [Specific quote, data point, timeline]

### Audience Reaction
- "[Verbatim reaction from social media]" — source
- "[Verbatim]" — source

### ICP Connection
- Why [user's audience] cares: [1-2 sentences]

### Boomerang Intel
- LinkedIn presence: [Active / Inactive / Team-managed]
- Estimated followers: [range]
- Recent post engagement: [high / medium / low]
```

### Provenance gate (sets the GROUNDED label — do NOT hardcode it):

```bash
python3 execution/research_quality_gate.py validate .tmp/diandra-growth-sprint/research-[slug].md
```

The label is **conditional on this result** and carries through every later "Research" field:
- **Gate PASS** (real `research.py` receipt + source floor met) → 🟢 GROUNDED
- **Gate FAIL / skipped / engine unavailable / facts unsourced** → 🟡 PROJECTED (post on vibes-not-facts; flag the gap to the user before producing)

Never print 🟢 GROUNDED unless the gate actually passed.

---

## Phase 3: Angle Mining

**Actor**: Orchestrator
**Prerequisite**: Research Brief in context

### Load Diandra's genius patterns:
// turbo
Read `skills/diandra-escobar-linkedin-growth/genius.md` — focus on Pattern 1 (Attention Redirection), Pattern 3 ("So What?" Gate), Pattern 6 (Body-First Writing).

### Generate 3 angles:

Using Diandra's angle framework from workflow 01:
- **Angle 1: The "What They Did Right"** — What can your audience learn from this?
- **Angle 2: The "What They Missed"** — What gap or blind spot exists?
- **Angle 3: The "What This Means For You"** — Direct ICP impact

### Score each angle:

| Angle | Originality (1-10) | ICP Relevance (1-10) | Polarization (1-10) | Boomerang Potential (1-10) | Total |
|-------|--------------------|-----------------------|---------------------|---------------------------|-------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

**Present to user with recommendation.**

> [!IMPORTANT]
> **HALT EXECUTION.** Ask: "Which angle(s) should we produce? I recommend #[X] because [reason]. Pick 1-3." Wait for explicit GO.

---

## Phase 4: Parallel Post Production (3 Sub-Agents)

**Actor**: 3 parallel sub-agents via Task tool
**Prerequisite**: User approved angle(s)

Spawn 3 sub-agents **in a single message**, each producing a different variation of the selected angle:

### Sub-Agent 1: Punchy Text Post
```
You are Diandra Escobar's Writing Engine producing a GROWTH post.

## SKILL ACQUISITION
Read these files IN ORDER:
1. /Users/farricecain/Google Antigravity/skills/diandra-escobar-linkedin-growth/genius.md
2. /Users/farricecain/Google Antigravity/skills/diandra-escobar-linkedin-growth/workflows/09-linkedin-writing-engine.md

## CONTEXT
[Full research brief from Phase 2]
[Selected angle from Phase 3]

## YOUR TASK
Produce a PUNCHY TEXT POST variation (150-250 words):
1. Write the BODY FIRST — 3-5 paragraphs of genuine analysis
2. Include specific details from the research (numbers, names, decisions)
3. Add your expert POV — this is NOT a summary
4. Mine the body for the hook — pull the most surprising/specific line to top
5. Entity name MUST appear in first 2 lines
6. CTA must be GROWTH bucket — invite discussion, not pitch

## QUALITY GATES
- Pass the "So What?" test: position, not summary
- Specificity Score: ≥2 specific numbers/names/examples
- Banned Word Scan: no "landscape", "game-changer", "leverage"

Write to: .tmp/diandra-growth-sprint/variation-1-text.md
```

### Sub-Agent 2: Carousel Outline
```
[Same skill acquisition and context]

## YOUR TASK
Produce a CAROUSEL OUTLINE variation (8-12 slides):
1. Write the body first as a continuous argument
2. Break into slide-by-slide copy (≤40 words per slide)
3. Slide 1 = hook (entity name + surprising claim)
4. Slides 2-10 = value (one idea per slide)
5. Final slide = CTA (growth bucket)
6. Include visual direction notes per slide

Write to: .tmp/diandra-growth-sprint/variation-2-carousel.md
```

### Sub-Agent 3: Long-Form Analysis
```
[Same skill acquisition and context]

## YOUR TASK
Produce a LONG-FORM ANALYSIS variation (300-500 words):
1. Write the body first — deep analysis with multiple supporting points
2. Include data from research, quotes, specific strategic details
3. Structure: Hook → Context → Analysis → Implication → CTA
4. This is the "LinkedIn article in a post" format
5. Mine for hook — entity name in first 2 lines

Write to: .tmp/diandra-growth-sprint/variation-3-longform.md
```

---

## Phase 5: Hook Mining + Boomerang Strategy

**Actor**: Orchestrator
**Prerequisite**: All 3 sub-agent outputs received

### Hook Refinement

For each variation, generate 3 additional hook candidates:
1. **Data hook**: Lead with the most specific number from research
2. **Contrarian hook**: Lead with the unexpected take
3. **Scene hook**: Lead with a moment or conversation

### Boomerang Strategy

If entity has active LinkedIn presence (from Phase 2 research):

Read `skills/diandra-escobar-linkedin-growth/workflows/05-boomerang-effect-orchestrator.md` and produce:

1. **Viability Score**: Subject Activity × Post Substance × Emotional Trigger × Respectful Challenge
2. **Tag Strategy**: Direct tag / indirect reference / post-to-reply
3. **Timing Recommendation**: When to post relative to news cycle
4. **Post-Publication Protocol**: 2-hour engagement checklist
5. **Capture Plan**: How to use the boomerang result for future content

---

## Phase 6: Quality Gate + Deliver

### Quality Checks (per genius.md Quality Rubric):

| Criterion | Check |
|-----------|-------|
| Attention Redirection | Entity IS the hook mechanism? |
| "So What?" Gate | Position, not summary? |
| Entity-in-Hook | Brand/person name in first 2 lines? |
| Body-First | Hook genuinely mined from body? |
| Specificity | ≥2 specific numbers/names/examples per variation? |
| Voice | No banned words, sounds like the creator? |
| Anti-Exemplar | Does NOT look like genius.md Anti-Exemplar? |

### Deliver

```markdown
# 🚀 GROWTH SPRINT: [Entity Name]

**Jack Type**: [type] | **Research**: [🟢 GROUNDED if Phase 2 gate passed, else 🟡 PROJECTED]
**Date**: [date]

---

## Selected Angle: [angle description]

---

## VARIATION 1: Punchy Text Post
[Full post — hook + body + CTA]

### Hook Alternatives
- A: [data hook]
- B: [contrarian hook]  
- C: [scene hook]

### Visual Brief
[1-sentence image recommendation]

---

## VARIATION 2: Carousel
[Slide-by-slide copy with visual notes]

---

## VARIATION 3: Long-Form Analysis
[Full post — hook + body + CTA]

---

## BOOMERANG PLAYBOOK
- **Viability Score**: [X/10]
- **Tag Strategy**: [recommendation]
- **Post Timing**: [window]
- **2-Hour Protocol**: [checklist]
- **If They Engage**: [response strategy]

---

## PROVENANCE
- Research: [query count] queries via `research.py` | [🟢 GROUNDED if `research_quality_gate.py` passed, else 🟡 PROJECTED]
- Skills Loaded: Diandra Escobar genius.md + workflows 01/05/09
- Patterns Applied: [list]
```

Save complete package to `.tmp/diandra-growth-sprint/sprint-[slug]-[date].md`.

### Next Steps

```
> **Ready to go?** Pick your favorite variation and post it.
>
> **Want more?**
> - Run `/diandra-growth-sprint` again with a different entity
> - Run `/growth-format-sprint` to batch 3-5 growth posts for the week
> - Run `/diandra-content-engine` for an authority or conversion post next
```

---

## Output Files

```
.tmp/diandra-growth-sprint/
  research-[slug].md
  variation-1-text.md
  variation-2-carousel.md
  variation-3-longform.md
  sprint-[slug]-[date].md   (assembled final package)
```

## Error Handling

- If research finds no relevant entity news: suggest alternate entities or switch to `--find` mode
- If sub-agent fails: present available variations, offer to regenerate the failed one
- If boomerang viability < 5: skip boomerang strategy, focus on organic reach

**Execution prompts**: before producing the deliverable, check `skills/diandra-escobar-linkedin-growth/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
