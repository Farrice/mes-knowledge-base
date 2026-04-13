---
description: Cross-domain reflection pass — generate synthesis articles from knowledge base patterns
---

# /reflect — Knowledge Reflection Pass

Generate second-order knowledge by finding cross-domain patterns, contradictions, and gaps across the 240+ source knowledge base. Produces synthesis articles that capture inter-concept relationships no single source contains.

This is Phase 2B of the Karpathy LLM Wiki pattern: raw knowledge exists, now the system reflects on it to compound its own intelligence.

## Usage

```
/reflect                        # Full reflection pass (3-7 synthesis articles)
/reflect --domain <domain>      # Focus reflection on a specific domain's connections
/reflect --inventory            # List existing synthesis articles
/reflect --refresh              # Re-read index, check for new synthesis opportunities since last run
```

## When to Run

- **Monthly** (pair with `/compile-knowledge` and `/calibrate`)
- **After 5+ new extractions** (new material creates new cross-domain potential)
- **After evolution cycles** (skill improvements may reveal new pattern connections)
- **On demand** when you notice a cross-domain insight during other work

## Steps

### 1. Load the Living Index

Read `knowledge/index.md` to get the full catalog of sources organized by domain.

Also read `knowledge/compiled/briefing.md` if it exists, for recent activity context.

If `knowledge/synthesis/` exists, read existing synthesis articles to avoid duplication. List them:

```bash
ls knowledge/synthesis/*.md 2>/dev/null || echo "No existing synthesis articles"
```

### 2. Regenerate the Index (if stale)

If the index is more than 7 days old (check the `Updated:` date in line 2), regenerate it first:

```bash
python3 execution/knowledge_compiler.py index
```

Then re-read `knowledge/index.md` to work from fresh data.

### 3. Stage 1 — Cross-Domain Pattern Detection

Scan the index and read summaries/extraction reports across domains. The goal is to detect:

**A. Cross-Cutting Themes** — The same principle operating in 2+ domains under different names.
Examples:
- Proof mechanisms in copywriting (Luke Iha) vs. credibility signals in LinkedIn content (Lara Acosta) — same principle, different execution
- Consumer posture theory (Dai Media) + awareness ladder (Eugene Schwartz) = unified targeting framework
- Belief installation (Lulu Meservey) + identity play (Nicolas Cole) = shared persuasion engine

**B. Contradictions** — Two experts or frameworks that directly conflict.
Examples:
- One expert says "always lead with pain," another says "lead with aspiration"
- A framework optimizes for dwell time while another prioritizes share velocity

**C. Knowledge Gaps** — Domains where the knowledge base has depth but no connective tissue to adjacent domains.
Examples:
- Deep SEO knowledge but no connection to content psychology principles
- Strong copywriting frameworks but no bridge to brand positioning theory

**Method**: Read 15-25 extraction reports and framework files across different domains. Do NOT read every file — sample strategically:
- Pick the 2-3 largest files per domain (these contain the richest frameworks)
- Prioritize recently added files (they create the newest cross-domain potential)
- Focus on files tagged with multiple experts or domains in the index

For each pattern detected, note:
- The domains involved
- The specific source files that evidence the pattern
- Why the connection is non-obvious (if it IS obvious, skip it)
- The actionable implication

### 4. CHECKPOINT: Present Candidate Themes

Present the detected patterns to the user:

```markdown
## Reflection Candidates

### Cross-Cutting Themes
1. **[Theme Name]** — [Domain A] + [Domain B]: [One-line insight]
   Sources: [file1], [file2], [file3]
   Non-obvious because: [why this isn't just restating what the sources say]

2. **[Theme Name]** — ...

### Contradictions Found
1. **[Contradiction Name]** — [Expert A] says X, [Expert B] says Y
   Resolution hypothesis: [how both could be true in different contexts]

### Knowledge Gaps
1. **[Gap Name]** — [Domain] has no connective tissue to [adjacent domain]
   Potential bridge: [what a synthesis article could contribute]

---

Which themes should I develop into full synthesis articles? (Recommend 3-7)
```

Wait for user selection. If the user says "all" or "go ahead," develop all candidates that meet the quality bar (2+ source files, non-obvious connection).

### 5. Stage 2 — Generate Synthesis Articles

For each approved theme, generate a synthesis article. Create the output directory if needed:

```bash
mkdir -p knowledge/synthesis
```

**Each synthesis article must pass these quality checks before writing:**
- [ ] Cites 2+ specific source files (not vague domain references)
- [ ] Identifies a non-obvious connection (the "so what" is clear)
- [ ] Includes concrete examples from each domain (not abstract hand-waving)
- [ ] States an actionable implication (how this changes future work)
- [ ] Does NOT merely restate what individual sources already say

**Article format** — write to `knowledge/synthesis/[theme-slug].md`:

```markdown
---
type: synthesis
domains: [domain1, domain2]
sources: [list of source file paths that informed this]
generated: YYYY-MM-DD
---

# [Theme Title]

## Cross-Domain Pattern
[What connects these domains — the insight nobody manually made.
This should be 2-4 sentences that a reader could act on immediately.]

## How It Manifests
### In [Domain 1]
[Specific examples from that domain — cite the source file and the specific
framework/concept. Use quotes or paraphrases, not vague references.]

### In [Domain 2]
[Specific examples from that domain — same standard of specificity.]

[Add more domain sections if 3+ domains are involved.]

## Contradiction or Tension (if applicable)
[Where these domains seem to disagree, and how both can be true.
Delete this section if there is no meaningful tension.]

## Actionable Implication
[How this insight should change future work. Be specific:
- Which skills or workflows benefit from knowing this?
- What should be done differently in production?
- Does this suggest a new workflow, a skill evolution target, or a gap to close?]

## Source Files
- `[path/to/file1.md]` — [what it contributed to this synthesis]
- `[path/to/file2.md]` — [what it contributed to this synthesis]
- `[path/to/file3.md]` — [what it contributed to this synthesis]
```

**Naming convention**: `knowledge/synthesis/[theme-slug].md`
- Use lowercase kebab-case: `proof-mechanisms-across-domains.md`
- Keep slugs under 50 characters
- No date prefix (the frontmatter carries the date)

### 6. Post-Write Quality Audit

After writing all synthesis articles, review them as a batch:

**Diversity check**: Do the articles cover different domain pairs, or are they all connecting the same 2 domains? If 3+ articles connect the same pair, consolidate or cut the weakest.

**Depth check**: Does each article contain at least one insight that would surprise someone who had read all the source files individually? If not, the synthesis is too shallow — revise or cut.

**Overlap check**: Does any new synthesis article substantially overlap with an existing one in `knowledge/synthesis/`? If so, either merge them or sharpen the distinction.

### 7. Update Wiki Infrastructure

After all synthesis articles are written and quality-checked:

**A. Log each synthesis article:**
```bash
python3 execution/knowledge_compiler.py log reflect "[Article Title]" --domain "[primary-domain]" --notes "Domains: [domain1]+[domain2]. Sources: [count] files. Insight: [one-line summary]"
```

**B. Regenerate the living index** (so synthesis articles appear in future index reads):
```bash
python3 execution/knowledge_compiler.py index
```

**C. Regenerate the session briefing** (so future sessions know about new synthesis):
```bash
python3 execution/knowledge_compiler.py briefing
```

### 8. Report

Present the final summary:

```markdown
## Reflection Pass Complete

**Date**: YYYY-MM-DD
**Articles Generated**: [N]
**Domains Connected**: [list of unique domains touched]
**Source Files Referenced**: [total unique files cited across all articles]

### Synthesis Articles
| # | Title | Domains | Sources | Key Insight |
|---|-------|---------|---------|-------------|
| 1 | [Title](knowledge/synthesis/slug.md) | A + B | N files | [One line] |
| 2 | ... | ... | ... | ... |

### Contradictions Surfaced
[List any meaningful contradictions found, even if not turned into articles]

### Knowledge Gaps Identified
[List gaps that suggest future extractions or research]

### Recommended Follow-Ups
- [ ] `/skill-evolution` on [skill] — informed by [synthesis article]
- [ ] `/extract` from [source] — to close [gap]
- [ ] `/compile-knowledge` — if stale content was found during reflection
```

## Design Principles

**Actionable over academic.** Every synthesis article must change how the system works, not just observe an interesting parallel. "Copywriting and LinkedIn both use proof" is observation. "Proof mechanisms should be loaded as a cross-skill pattern in the routing layer" is actionable.

**Non-obvious over comprehensive.** 3 genuinely surprising connections beat 7 surface-level ones. The test: "Would someone who read all the source files individually have noticed this connection?" If yes, it is too obvious.

**Cite or cut.** Every claim in a synthesis article must point to a specific source file. Vague domain-level references ("copywriting experts say...") are not synthesis — they are hand-waving.

**Compound, don't repeat.** Synthesis articles should build on each other over time. The second reflection pass should reference insights from the first. The knowledge base gets smarter with each cycle.

## Protocol Reference

Knowledge compiler: `execution/knowledge_compiler.py`
Living index: `knowledge/index.md`
Session briefing: `knowledge/compiled/briefing.md`
Synthesis output: `knowledge/synthesis/`
Knowledge log: `knowledge/log.md`
Evolution direction: `directives/evolution-direction.md`
