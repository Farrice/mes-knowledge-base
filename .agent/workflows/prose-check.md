---
description: Check text file AI-prose patterns before delivery
---

# /prose-check — AI Prose Detection

Automated "does this read like AI?" check. The quality gate caps Expert Standard at 6 if prose reads AI-generated — this makes that check objective instead of vibes-based.

## Usage

```
/prose-check <file>              # Check a specific file
/prose-check --text "paste here" # Check inline text
/prose-check scan <directory>    # Scan all files in a directory
```

## Steps

### 1. Check a Deliverable

Before finalizing any expert-domain output:

```bash
python execution/prose_classifier.py check deliverables/MyBPM-SEO-AEO-Optimization.md
```

### 2. Interpret Results

| Verdict | AI Score | Meaning | Action |
|---------|----------|---------|--------|
| CLEAN | 0-2 | Passes prose check | Expert Standard uncapped |
| WARNING | 2-4 | Some AI patterns | Review flagged patterns, fix before delivery |
| FLAGGED | 5+ | Reads AI-generated | Expert Standard capped at 6. Rewrite. |

### 3. Fix Flagged Patterns

The classifier detects 7 signal types:

1. **Banned vocabulary** — Replace: delve, tapestry, landscape, leverage, robust, comprehensive, transformative, groundbreaking, cutting-edge, etc.
2. **Hedging phrases** — Delete: "it's worth noting", "arguably", "potentially", "in many ways"
3. **AI transitions** — Cut: "furthermore", "moreover", "additionally", "that being said"
4. **Empty openers** — Rewrite: "In the world of...", "When it comes to...", "In today's fast-paced..."
5. **Rhythm uniformity** — Vary sentence length: mix 5-word punches with 20-word builds
6. **Adjective stacking** — Unstack: "comprehensive, strategic, data-driven" → pick one, make it specific
7. **Parallel structure overuse** — Break patterns: don't start 3+ consecutive lines the same way

### 4. Scan Deliverables Directory

```bash
python execution/prose_classifier.py scan deliverables/
```

### 5. Batch Scan (Before Session End)

Run on all recent output to catch any AI-prose that slipped through:

```bash
python execution/prose_classifier.py scan deliverables/ --ext .md
```

## Integration Points

- **chain_runner.py**: Prose check runs automatically during `finalize()` — warns if Expert Standard may be inflated
- **Quality Gate**: FLAGGED verdict caps Expert Standard at 6 per `directives/quality_gate.md`
- **Content Creation Gate**: Pre-delivery check before shipping any content
- **Feedback Ratchet**: Prose scores feed into pattern detection

## The Test

The quickest self-check: read any sentence aloud. If it sounds like a corporate LinkedIn post or a ChatGPT response, rewrite it. The prose classifier automates this intuition.
