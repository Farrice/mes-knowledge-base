---
description: Convert external practitioner-mode prompts into completion-engine skills with genius extraction and agent registration
---

# /convert-prompt — Practitioner Prompt → Completion Engine Skill

Convert battle-tested prompts from chatbot environments (claude.ai, ChatGPT, etc.) into properly structured completion-engine skills. The prompt's methodology becomes permanently loadable, composable with existing agents, and integrated with the full context engine.

**Key difference from `/extract`**: Prompts contain explicit, already-crystallized methodology. This is a *reformatting* operation, not an *extraction* operation — the knowledge is on the surface, not buried in raw material.

## Usage

```
/convert-prompt [paste prompt, provide file path, or reference a folder of related prompts]
```

**Flags:**
- `--plan-only` — Analyze and present conversion plan without creating files
- `--add-to [skill-name]` — Skip routing; add workflow(s) directly to a named existing skill
- `--force-new` — Skip existing-expert check; always create a new skill

---

## Step 0: Receive Prompt Input

Accept the practitioner prompt in one of three ways:

| Input | Action |
|-------|--------|
| Pasted directly in chat | Capture full prompt text |
| File path (e.g., `~/Desktop/my-prompt.md`) | Read the file |
| Folder of related prompts | Read all `.md` / `.txt` files, treat as a prompt corpus from the same expert |

If multiple prompts are provided, treat them as a corpus — merge genius patterns (dedup) and each prompt becomes a workflow candidate.

---

## Step 1: Prompt Anatomy Analysis

Four sub-analyses. This is where the intelligence happens.

### 1a. Identity Extraction

Extract from the prompt:
- **Expert name** — if stated (e.g., "You are Alex Hormozi..."). If none stated, flag as **synthetic expert** and derive a name from the domain (e.g., `saas-onboarding-email`).
- **Domain** — the specific area of expertise
- **Core methodology** — the named or unnamed framework the prompt deploys
- **Credibility markers** — specific achievements, experience, track record mentioned
- **Voice characteristics** — tone, style, vocabulary patterns

### 1b. Topology Classification

Classify the prompt's structural type:

| Type | Signal | Handling |
|------|--------|----------|
| **Single Expert** | One persona, one methodology, one domain | Standard Path A or B |
| **Expert-with-Techniques** | One primary expert borrowing specific techniques from other domains | Fold borrowed techniques into primary expert's genius.md |
| **True Fusion** | Multiple named experts staffed together, each contributing distinct methodology | Path C: fused skill (follow `skills/ghostwriting-voice-engine/` pattern) |

### 1c. Genius Pattern Mining

For each distinct technique/framework in the prompt, extract:

| Field | Source |
|-------|--------|
| **Pattern Name** | Descriptive label for the technique |
| **What It Does** | The behavior described in the prompt |
| **Executable Behavior** | Concrete steps (often directly lifted from the prompt's instructions) |
| **Deploy When** | Context triggers (inferred from stated use cases) |
| **Success Metric** | How to know it worked (inferred from quality criteria or output spec) |

Also identify **hidden knowledge** — things the prompt assumes but does not explain. These are structural gaps that an AI might fill with generic behavior unless explicitly documented.

Count the genius patterns — this feeds the workflow sizing rules.

### 1d. Deliverable Analysis

| Field | Extract From |
|-------|-------------|
| **Primary deliverable** | What the prompt's main output is |
| **Secondary deliverables** | Any supporting artifacts |
| **Input requirements** | What the user needs to provide |
| **Quality criteria** | Any stated evaluation standards |

---

## Step 2: System Mapping

Cross-reference the analysis against the existing Antigravity system.

### 2a. Expert Match Check

Read `agents/_framework/invocation-cards.md` (~50 tokens per expert) and scan for:
- **Exact name match** — e.g., "April Dunford" matches `april-dunford`
- **Domain overlap** — e.g., a new "LinkedIn content" prompt overlaps with Lara Acosta, Jasmin Alic, Josh Sanders

If `--add-to` flag was set, skip this step and go directly to Path A with the named skill.
If `--force-new` flag was set, skip this step and go directly to Path B.

### 2b. Decision Tree

```
PROMPT ANALYZED
├── Named expert EXISTS in system?
│   ├── YES + adds new capability → PATH A: Add workflow to existing skill
│   └── YES + already covered → ABORT: "This capability already exists at [path]"
├── Named expert NOT in system?
│   ├── Domain strongly overlaps existing expert → Present options, user decides
│   │   ├── User: "add to existing" → PATH A
│   │   └── User: "create new" → PATH B
│   └── Unique domain → PATH B: Create new skill + agent
└── Multi-expert fusion?
    ├── Expert-with-Techniques → PATH A or B (primary expert), fold borrowed techniques into genius
    └── True Fusion → PATH C: Create fused skill
```

**Three paths:**

| Path | When | Creates |
|------|------|---------|
| **A: Add Workflow** | Expert exists, prompt adds new capability | New workflow file(s) in existing skill, updated SKILL.md, updated genius.md |
| **B: New Expert** | Expert is new to the system | Full skill directory + agent directory + invocation card |
| **C: Fused Skill** | Multi-expert fusion | Fused skill directory with per-expert genius sections |

---

## Step 3: CHECKPOINT 1: Conversion Plan

**This is a user decision point.** Present:

```markdown
## Conversion Plan

**Source**: [Pasted prompt / file path]
**Expert**: [Name] — [Domain]
**Topology**: [Single / Expert-with-Techniques / True Fusion]
**Path**: [A: Add to existing / B: New expert / C: Fused skill]

### Genius Patterns Identified: [N]
1. [Pattern name] — [1-line description]
2. [Pattern name] — [1-line description]
...

### Hidden Knowledge Identified: [N]
1. [Insight] — [1-line description]
...

### Proposed Workflows: [N]
| # | Name | Produces | Derived From |
|---|------|----------|--------------|
| 01 | [name] | [deliverable] | [Which parts of the prompt] |

### Files to Create/Modify:
- [ ] `skills/[name]/genius.md` — [create / update]
- [ ] `skills/[name]/workflows/0N-[slug].md` — [create]
- [ ] `skills/[name]/SKILL.md` — [create / update]
- [ ] `agents/[name]/AGENT.md` — [Path B/C only]
- [ ] `agents/[name]/memory/context.md` — [Path B/C only]
- [ ] `agents/_framework/invocation-cards.md` — [Path B/C only]

### Overlap Notes:
[Any existing skills/agents in adjacent domains — for user awareness]
```

**Wait for user approval/adjustment before proceeding.**

If `--plan-only` flag was set, **stop here**.

---

## Step 4: Create Skill Files

// turbo

### 4a. Directory Creation

**Path A** (existing skill): No new directories needed.

**Path B** (new expert):
```bash
mkdir -p skills/[skill-name]/workflows agents/[expert-name]/memory
```

**Path C** (fused skill):
```bash
mkdir -p skills/[fused-name]/workflows
```

**Naming conventions:**
- Skills: `skills/[firstname-lastname-domain]/` (e.g., `skills/alex-hormozi-offer-creation/`)
- Fused skills: `skills/[descriptive-name]/` (e.g., `skills/saas-cold-email-engine/`)
- Synthetic experts: `skills/[domain-slug]/` (e.g., `skills/saas-onboarding-email/`)
- Agents: `agents/[firstname-lastname]/` (e.g., `agents/alex-hormozi/`)

### 4b. Create / Update genius.md

**Path A** (add to existing): Read existing `genius.md`. Append new patterns under a labeled section:

```markdown
---

### Patterns from [Source Prompt Description]

### [New Pattern Name]
**Execute**: [Concrete behavior]
**Success Metric**: [Measurable outcome]
```

**Path B** (new expert): Create fresh genius.md:

```markdown
# [Expert Name] — Genius Context

> Load this file before executing any workflow. It contains the
> methodology extracted from [source description] — patterns and
> knowledge that make this expert's output actually work.

## Genius Patterns

### Pattern 1: [Name]
**Execute**: [Concrete steps]
**Success Metric**: [How to measure]

---

### Pattern 2: [Name]
**Execute**: [Concrete steps]
**Success Metric**: [How to measure]

---

## Hidden Knowledge

### 1: [Insight Name]
**Insight**: [The tacit knowledge]
**Deploy**: [How to operationalize it]

---
```

**Path C** (fused skill): Create genius.md with labeled sections per expert, following the pattern in `skills/ghostwriting-voice-engine/genius.md`:

```markdown
# [Fused Skill Name] — Genius Patterns & Hidden Knowledge

> Load this file before executing any workflow. It contains unified
> intelligence from [N] expert domains — [list domains] — synthesized
> into a single deployable system.

---

## Genius Patterns

### [Domain 1] Patterns (from [Expert Name])

| Pattern | What It Does | Executable Behavior | Deploy When | Success Metric |
|---------|-------------|---------------------|-------------|----------------|
| ... | ... | ... | ... | ... |

---

### [Domain 2] Patterns (from [Expert Name])

| Pattern | What It Does | Executable Behavior | Deploy When | Success Metric |
|---------|-------------|---------------------|-------------|----------------|
| ... | ... | ... | ... | ... |
```

### 4c. Generate Workflow Files

**Workflow sizing rules** (from `/convert-extraction`):
- Prompt represents 1 deliverable → 1 workflow
- Prompt represents 2-3 related deliverables → 1-2 workflows
- Prompt is a comprehensive system (10+ techniques) → 2-3 workflows

For each workflow, create `skills/[skill-name]/workflows/[NN]-[slug].md`:

```markdown
---
name: "[Workflow Name]"
produces: "[Specific deliverable]"
expert: "[Expert Name]"
load_context: "genius.md"
---

# [Expert] — [Workflow Name]

## Role
[Expert identity + credibility — 2-3 sentences. Derived from the prompt's persona instructions.]

**Before executing**: Read genius.md for full extraction intelligence.

## Input Required
- **[Field 1]**: [Description]
- **[Field 2]**: [Description]
[3-6 essential inputs — derived from what the original prompt requires]

## Workflow

[Integrated end-to-end flow. Embed genius patterns INLINE where they apply.
Each phase builds on the previous. Preserve the original prompt's methodology
but restructure into phased workflow format.]

### Phase 1: [Phase Name]
[Steps with embedded genius context]

### Phase 2: [Phase Name]
[Steps building on Phase 1]

### Phase 3: [Phase Name]
[Steps producing final deliverable]

## Output Contract

The user receives:
- **[Component 1]**: [Exact specification]
- **[Component 2]**: [Exact specification]
[Derived from the prompt's stated output — what it actually produces]

Format: [Markdown / table / document structure]
Length: [Approximate scope]

## Quality Gate

[Expert-specific criteria — derived from the prompt's quality standards]

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]
```

The workflow content should **preserve the original prompt's methodology** but restructure it. The goal is decomposition into the Role/Input/Workflow/Output/Quality architecture while keeping the genius intact.

### 4d. Write / Update SKILL.md

**Path A** (existing skill): Update the workflow table and workflow count in frontmatter.

**Path B/C** (new skill): Create using completion engine format:

```markdown
---
name: "[Expert] — [Domain]"
description: "[1-2 sentence value prop derived from the prompt]"
version: "2.0"
format: "completion-engine"
workflows: [N]
---

# [Expert] — [Domain]

[2-3 sentence expert context + core genius statement.]

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| 01 | [Name](workflows/01-slug.md) | [Deliverable] | [Trigger] |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Source**: Converted from practitioner prompt ([date])
```

For **Path C** (fused skill), also add the Expert Stack table following `skills/ghostwriting-voice-engine/SKILL.md`:

```markdown
## Expert Stack

| Agent | Role | Deployed In |
|-------|------|-------------|
| **[Expert 1]** | [Role] | Workflow 01 |
| **[Expert 2]** | [Role] | Workflow 01, 02 |
```

---

## Step 5: Create Agent Files (Path B and C only)

// turbo

Skip entirely for Path A — the existing expert already has an agent.

### 5a. AGENT.md

Generate using the template at `agents/_framework/AGENT_TEMPLATE.md`:

```markdown
---
name: [agent-name]
expert: [Expert Name]
domain: [domain-description]
skill: [linked-skill-name]
---

# [EXPERT NAME] Agent

[One paragraph: who they embody, unique expertise, credibility markers from the prompt.
Should feel like introducing a trusted advisor.]

## Core Competencies

[5 competencies derived from the genius patterns]

1. **[Competency 1]**: [Brief description]
2. **[Competency 2]**: [Brief description]
3. **[Competency 3]**: [Brief description]
4. **[Competency 4]**: [Brief description]
5. **[Competency 5]**: [Brief description]

## Available Skills

| Capability | Workflow | When Used |
|------------|---------|-----------|
| [Capability 1] | [01-workflow.md] | [Trigger] |

## Decision Framework

1. **First**: [What they assess first — from the prompt's methodology]
2. **Then**: [What they do next]
3. **Finally**: [How they deliver]

## Activation Triggers

- [When to invoke this agent]
- [Another appropriate situation]
- [When to use a different expert instead]

## Handoff Protocol

| Situation | Hand off to | What to transfer |
|-----------|-------------|------------------|
| [Adjacent domain 1] | [Existing Antigravity expert] | [Context] |
| [Adjacent domain 2] | [Existing Antigravity expert] | [Context] |

## Memory Reference

This agent's persistent context is stored in `memory/context.md`.
```

Cross-reference `DOMAIN_REGISTRY.md` and `invocation-cards.md` for the Handoff Protocol — identify which existing experts handle adjacent domains.

### 5b. memory/context.md

```markdown
# [Agent Name] Memory

## Active Projects
(None yet)

## User/Brand Context
(To be populated as work proceeds)

## Learnings
(To be populated from completed work)

## Past Work Reference
(To be populated from completed work)
```

### 5c. Invocation Card

Append to `agents/_framework/invocation-cards.md`:

```
AGENT: [Name]
DOMAIN: [Domain description]
CORE METHOD: [Method name] — [1-line description]
BEST FOR: [2-4 use cases]
ENTRY PROMPT: skills/[skill-name]/SKILL.md
PAIRS WITH: [2-3 existing experts + why]
```

---

## Step 6: CHECKPOINT 2: Quality Verification

**User reviews the primary workflow** to confirm quality meets expectations.

Present:
- The primary workflow file (full content)
- Workflow count and names
- Quick comparison: what the original prompt does vs. what the converted skill preserves

**Optional A/B test**: Run the original prompt and the converted skill's primary workflow against the same test input. Compare outputs side-by-side.

If quality passes, proceed to registration. If not, iterate on specific issues.

---

## Step 7: Register

// turbo

### 7a. Sync registries
```bash
python execution/sync_registries.py
```

### 7b. Update DOMAIN_REGISTRY.md (Path B/C only)
Add the new expert to the appropriate domain's swim lane.

### 7c. Report

```markdown
## Conversion Complete

- **Source**: [Original prompt description]
- **Path**: [A: Added workflow / B: New expert / C: Fused skill]
- **Expert**: [Name] — [Domain]
- **Genius Patterns**: [N] extracted
- **Hidden Knowledge**: [N] identified
- **Workflows Created**: [N] — [list names]
- **Files Created/Modified**: [list paths]
- **Registered In**: [indexes updated]

### How to Use
Load via: `skills/[skill-name]/SKILL.md`
Or invoke: @[agent-name]
```

---

## Edge Cases

| Scenario | Handling |
|----------|----------|
| **Prompt is one deliverable** (e.g., "generate a LinkedIn post") | Create exactly 1 workflow. Don't stretch to 3-5. |
| **No named expert** ("You are an expert in X") | Synthetic name from domain (e.g., `saas-onboarding-email`). Mark agent as "Synthetic Expert" in AGENT.md. |
| **Overlaps multiple existing experts** | Present overlap at CHECKPOINT 1 with links to existing skills. User decides. |
| **Multiple related prompts from same expert** | Treat as corpus. Merge genius (dedup). Each prompt → workflow candidate. |
| **Meta-system prompt** ("You are a prompt engineer") | Flag as meta/tool skill. Place in system management section, not domain expert section. |
| **Prompt with Do/Don't guardrails** | Capture as guardrails in genius.md (following `ghostwriting-voice-engine` pattern). |

---

## Philosophy

This workflow exists because your best thinking shouldn't be trapped in chatbot prompts. Every practitioner prompt you've battle-tested contains genuine methodology — expert knowledge crystallized into instructions that work. The conversion preserves that intelligence while making it composable, loadable, and integrated with the rest of Antigravity.

The prompt is the extraction. We just need to reformat the gold you already mined.
