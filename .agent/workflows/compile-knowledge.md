---
description: Compile knowledge base
---

# /compile-knowledge — Knowledge Compilation Workflow

Compile the knowledge base into structured, interlinked output. Inspired by Karpathy's LLM Knowledge Base: raw data → compiler → validator → briefing.

## Usage

```
/compile-knowledge              # Full compilation (all stages)
/compile-knowledge briefing     # Session briefing only
/compile-knowledge stats        # Quick stats
/compile-knowledge stale        # Find stale content
```

## Steps

### 1. Run Compilation

```bash
# Full compilation (inventory + briefing + stale + overlap reports)
python execution/knowledge_compiler.py full

# Or individual stages:
python execution/knowledge_compiler.py stats       # Quick overview
python execution/knowledge_compiler.py inventory   # Full manifest
python execution/knowledge_compiler.py briefing    # Session briefing
python execution/knowledge_compiler.py stale       # Stale content (>30 days)
python execution/knowledge_compiler.py overlap     # Overlapping files
```

### 2. Review Output

Read the generated files in `knowledge/compiled/`:
- `manifest.json` — full inventory with per-file metadata
- `briefing.md` — session start briefing (recent activity, domain coverage, gaps)
- `stale-report.md` — files not touched in 30+ days
- `overlap-report.md` — files covering similar topics

### 3. Act on Findings

Based on the reports:

**Stale content**: Review files flagged as stale. Options:
- Update with recent learnings from extractions
- Consolidate into shorter summaries
- Archive truly obsolete content to `knowledge/archive/`

**Overlaps**: Review overlapping file pairs. Options:
- Merge related files into single comprehensive articles
- Keep both if they serve different purposes (note why)
- Delete the weaker version

**Gaps**: For domains with < 3 files:
- Run extractions to build up thin domains
- Cross-reference with `execution/ground_truth.py gap-report`

### 4. Validate (Optional)

Run the briefing through a quality check:
- Does it accurately reflect current knowledge?
- Are there contradictions between files flagged?
- Do recent extractions introduce new entities that should be tracked?

### 5. Update Evolution Direction

If compilation reveals knowledge gaps that affect skill quality, note them in `directives/evolution-direction.md` under Research Directions.

## When to Run

- **Monthly**: Full compilation to keep knowledge base healthy
- **After extraction sessions**: Briefing refresh to capture new knowledge
- **Before evolution cycles**: Check if knowledge gaps are holding back skill quality
- **Session start**: Read `knowledge/compiled/briefing.md` for context

## Output

All outputs written to `knowledge/compiled/`. No existing files are modified — compilation is additive and safe.
