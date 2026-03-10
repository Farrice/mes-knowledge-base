# Cross-Pollination Protocol

> **Trigger**: A skill evolution cycle produces a KEPT improvement, OR user runs `/cross-pollinate`.
> **Inspired by**: Karpathy's SETI@home vision — multiple agents sharing discoveries.
> **Purpose**: Break the isolation between 110+ skills. When one improves, related skills benefit.
> **Depends on**: Phase 1 (Feedback Ratchet) + Phase 2 (Skill Evolution) data.
> **Effective**: 2026-03-10

---

## Core Principle

Skills share pattern DNA. A proof engineering skill and a conversion copy skill both use persuasion patterns. When one discovers that reordering proof elements improves conversion, the other should know about it — not rediscover it independently through 20 more experiments.

---

## Pattern Families

Skills are grouped into families based on the types of patterns they use. A skill can belong to multiple families.

| Family | Description | Example Skills |
|--------|-------------|---------------|
| **Persuasion** | Changing minds, building belief, overcoming objections | Luke Iha, Jeremy Miner, Jason Fladlien |
| **Hooks** | Attention capture, scroll-stoppers, curiosity loops | Seena Rez, Kallaway, Jasmin Alic |
| **Structure** | Content architecture, frameworks, templates | Nicolas Cole, Authority Hacker |
| **Voice** | Tone, rhythm, sentence craft, style | Mitch Albom, Ward Farnsworth, Nicolas Cole |
| **Research** | Analysis, market intelligence, consumer insight | Dai Media, Samuel Thompson, Manus.AI |
| **Conversion** | Turning attention into action — CTAs, funnels | Cardinal Mason, Joanna Wiebe |
| **Storytelling** | Narrative techniques, emotional architecture | Shaan Puri, Mitch Albom, Lucas Alpay |
| **Positioning** | Market positioning, differentiation, category | April Dunford, Caleb Ralston, Omar Eddaoudi |
| **Systems** | AI systems, automation, agent architecture | Nick Saraev, Boris, Rachel Woods |

---

## When to Cross-Pollinate

| Trigger | Condition | Action |
|---------|-----------|--------|
| **Evolution KEPT** | A skill improvement is kept and pattern-based | Auto-check related skills |
| **High performer** | A skill averages 8+/10 quality | Scan for extractable patterns |
| **User request** | `/cross-pollinate <skill>` or `/cross-pollinate --report` | Manual propagation cycle |
| **Monthly review** | First of each month | Full propagation report |

---

## The Cross-Pollination Process

### Step 1: Identify the Improvement

From the Evolution Log entry:
- What pattern changed?
- Is it skill-specific or generalizable?
- What pattern family does it belong to?

**Transferability test**: Would this improvement make sense in a skill that has NEVER seen the original expert's methodology? If yes → transferable. If it relies on the expert's unique framework → skill-specific, do not transfer.

### Step 2: Find Related Skills

```bash
python execution/pattern_propagation.py related <source-skill>
```

This returns skills ranked by pattern family overlap.

### Step 3: Evaluate Candidates

For each candidate skill:

1. **Read its genius.md** — Does it use similar patterns?
2. **Read the target workflow** — Where would the improvement apply?
3. **Check performance** — Is the candidate already strong in this area? (Don't fix what's not broken)

**Transfer criteria** (ALL must be true):
- The candidate uses a related pattern in at least one workflow
- The candidate's performance in the related dimension is < 8/10
- The improvement is generalizable (not expert-specific)
- The candidate's genius.md doesn't contradict the improvement

### Step 4: Generate Transfer

Adapt the improvement for the candidate skill:
- Translate expert-specific language to the candidate's voice
- Integrate with the candidate's existing workflow structure
- Don't overwrite existing patterns — augment them

Create a variant file:
```
skills/[candidate-skill]/workflows/[workflow].variant.md
```

### Step 5: Test via Evolution Protocol

The transfer becomes a standard evolution hypothesis:

```markdown
## Evolution Hypothesis (Cross-Pollination)

**Source**: [source-skill] → [improvement description]
**Target Skill**: [candidate-skill]
**Target Workflow**: [workflow-name]
**Hypothesis**: Applying [pattern improvement] from [source expert] will improve [candidate skill's] [dimension]
**Expected Impact**: +1-2 points on [dimension]
```

Run the standard evolution testing protocol (Phase 2, Steps 5-7).

### Step 6: Log Result

Whether kept or discarded, log to both skills:

**Source skill's genius.md** (Evolution Log):
```markdown
### [Date] — Cross-Pollination: [improvement] → [target-skill]
- **Result**: [TRANSFERRED/REJECTED]
- **Target**: [candidate-skill]
- **Impact**: [Score change at target]
```

**Target skill's genius.md** (Evolution Log):
```markdown
### [Date] — Cross-Pollination: Received from [source-skill]
- **Result**: [KEPT/DISCARDED]
- **Source**: [source-skill] — [improvement description]
- **Impact**: [Score change]
```

---

## Transfer Rules

### DO Transfer

- **Process improvements**: Better sequencing, clearer output contracts, tighter quality gates
- **Pattern upgrades**: Proof ordering, hook structures, CTA placement
- **Structural innovations**: New workflow steps that add value across domains
- **Quality gate refinements**: Better scoring criteria that catch more issues

### DO NOT Transfer

- **Expert-specific frameworks**: NEPQ is Jeremy Miner's — it doesn't belong in Bond Halbert's skill
- **Voice/tone patterns**: Each expert has unique voice; don't homogenize
- **Domain-specific knowledge**: Real estate insights don't transfer to SEO skills
- **Contradictory patterns**: If the improvement conflicts with the target expert's methodology, skip it

---

## Propagation Report

Run monthly or on-demand:

```bash
python execution/pattern_propagation.py report
```

This generates:
- All KEPT evolution improvements
- Related skills for each improvement
- Pattern family map (which skills share which families)
- Transfer candidates prioritized by impact potential

---

## Integration

- **Data source**: Evolution Logs in `skills/*/genius.md`
- **Engine**: `execution/pattern_propagation.py`
- **Testing**: Uses Phase 2 evolution protocol for variant testing
- **Logging**: Performance Log (Notion) + Evolution Logs (genius.md)
- **Triggered by**: Skill Evolution (Phase 2) KEPT results, user request, monthly review

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-09 |

**Update Rule**: When this protocol fires (cross-pollination cycle completed), update the date and increment count.

---

*Created: 2026-03-10 | Phase 3 of Autoresearch Integration*
*Depends on: Phase 1 (Feedback Ratchet) + Phase 2 (Skill Evolution)*
