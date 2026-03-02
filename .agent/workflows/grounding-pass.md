---
description: Run a Grounding Pass on agent outputs or research documents — validate factual claims against Perplexity research data and tag provenance
---

# /grounding-pass Workflow

Validate and ground any set of documents against live research data. Corrects inflated claims, injects real competitor/market data, adds Reddit verbatims, and tags every factual assertion with provenance.

## Usage

```
/grounding-pass [path to directory or specific files]
/grounding-pass --research-first [path]   # Run Perplexity research BEFORE grounding
```

### Flags

| Flag | Effect |
|------|--------|
| `--research-first` | Execute Perplexity research queries before the grounding pass (for documents that don't already have a `perplexity_findings.md`) |
| (default) | Assumes `research_data/perplexity_findings.md` already exists in or near the target directory |

## Steps

### 1. Locate Research Data

Find the grounding source — the verified research file:
- Look for `research_data/perplexity_findings.md` in/near the target directory
- If `--research-first` flag is set, execute Perplexity research first (see Phase 2.5 in `/swarm` workflow)
- If no research data exists and `--research-first` is not set, **STOP** and notify user

### 2. Inventory Target Files

List all files to be grounded. For each file, classify:
- **Research-heavy** (market intel, competitive analysis, buyer profiles) → Full pass
- **Framework-heavy** (methodology, psychology, identity) → Light pass (numbers + claims only)
- **Pure synthesis** (brand strategy, positioning) → Targeted pass (verify only cited data)

### 3. Execute Grounding Pass (per file)

For EACH target file:

#### 3a. Scan for Factual Claims
Identify every:
- Dollar amount, percentage, or market size
- Named competitor, platform, or tool
- Growth rate or trend assertion
- Behavioral claim ("X% of executives...")
- Quoted statistic or research finding

#### 3b. Cross-Reference Against Research Data
For each claim found:
- **Matches research data** → Tag 🟢 GROUNDED, add inline citation
- **Directionally correct but imprecise** → Tag 🟡 SUPPLEMENTED, correct with real data, preserve original in context
- **Cannot be verified** → Tag 🔴 PROJECTED, flag for user review
- **Wrong/inflated** → Correct the claim, note the correction

#### 3c. Inject Missing Intelligence
Add data that SHOULD be in the document but isn't:
- Real competitor names and pricing (replace generic references)
- Reddit/forum verbatim quotes (replace hypothetical pain language)
- Corrected market data (actual CAGRs, TAM figures)
- Sentiment data and specifics from social listening

#### 3d. Add Grounding Summary Header
Insert at top of each file:
```
> **Grounding Pass**: ✅ Complete | [DATE]
> **Claims Verified**: X/Y | **Corrections Made**: Z
> **Research Source**: [path to perplexity_findings.md]
```

### 4. Quality Gate Verification

After all files are grounded, verify:
- [ ] Every file has the Grounding Summary header
- [ ] Every factual claim is tagged (🟢/🟡/🔴)
- [ ] No 🔴 claims remain without user acknowledgment
- [ ] Corrections are clearly marked (original → corrected)
- [ ] Missing intelligence has been injected where applicable

### 5. Report to User

Present a summary table:

```
| File | Claims Found | 🟢 Grounded | 🟡 Corrected | 🔴 Projected | Key Changes |
|------|-------------|-------------|--------------|--------------|-------------|
```

---

## When to Use This Workflow

- **After a `/swarm` deployment** — Phase 3.5 uses this same process
- **Before handing off documents** to a client or for downstream work
- **When reviewing old outputs** that were created before Perplexity research was available
- **After receiving new research data** that should update existing documents
- **Anytime a document will become a FOUNDATION** for downstream strategy or copy

## Notes

- This workflow is also embedded in `/swarm` as Phase 3.5
- Research data must exist BEFORE running (use `--research-first` if needed)
- Respects the Adaptive Research Tiering system (see `directives/perplexity-usage-policy.md`)
- Cost: $0 if research data already exists (grounding is LLM-only cross-referencing)
