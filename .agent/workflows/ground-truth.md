---
description: Manage expert benchmark samples and run blind comparisons
---

# /ground-truth — Expert Benchmark Calibration

Compare AI output against real expert work. The system's quality gate is self-referential (AI scoring AI) — this grounds it in reality.

## Usage

```
/ground-truth                    # Show gap report (what's covered, what's missing)
/ground-truth add <domain>       # Add a new expert sample
/ground-truth compare <domain>   # Run blind comparison (AI vs expert)
/ground-truth domains            # List all registered domains
```

## Steps

### 1. Check Current Coverage

Run the gap report to see where expert samples exist and where they're missing:

```bash
python execution/ground_truth.py gap-report
```

Domains: copywriting, linkedin, brand-strategy, seo, screenwriting, sales-psychology, content-strategy.

### 2. Add Expert Samples

When you have real expert output (from genius.md Hall of Fame, extractions, or web research):

```bash
python execution/ground_truth.py add <domain> <file_path> \
    --expert <name> --source <url> --type <output-type> \
    --notes "What makes this expert-level" --title "Sample title"
```

Or programmatically:

```python
from execution.ground_truth import add_sample
add_sample("copywriting", content, expert="luke-iha", output_type="hook",
           source="skills/luke-iha-vicious-hooks/genius.md",
           notes="All 8 Genius Patterns activated")
```

### 3. Run Blind Comparison

To test whether AI output matches expert quality:

```bash
python execution/ground_truth.py compare <domain> <path-to-ai-output>
```

This generates a blind comparison file in `knowledge/expert-benchmarks/_comparisons/` with:
- Output A and Output B (randomly ordered, unlabeled)
- Scoring dimensions (Craft Quality, Persuasion Power, Voice Authenticity, Would-Buy Factor)
- After scoring, reveal the key: `python execution/ground_truth.py reveal <filename>`

### 4. Interpret Results

- **Expert scored higher** → Real gap to close. Focus evolution cycles on this domain.
- **AI scored higher** → Skill is well-calibrated for this output type.
- **Scores are close** → Focus on voice authenticity (the hardest dimension to nail).

## Integration Points

- **Feedback Ratchet**: Ground truth comparisons feed into the performance log
- **Skill Evolution**: Gap data triggers targeted variant testing
- **Quality Gate**: Blind comparison scores validate Expert Standard dimension
- **Expert Benchmarks**: `knowledge/expert-benchmarks/` (7 domains, 16 experts registered)

## Priority Domains (Revenue-Adjacent)

1. **Copywriting** — Luke Iha, Cardinal Mason, Stefan Georgi
2. **LinkedIn** — Lara Acosta, Nicolas Cole
3. **SEO** — Nathan Gotch, Ethan Smith
4. **Brand Strategy** — Oren John, Grace Beverley, David Placek
