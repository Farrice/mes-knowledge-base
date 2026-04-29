# Workflow 04: Zero-Load Rewrite Engine

> **Produces**: Rewritten copy scored at zero cognitive load
> **Use When**: Transforming existing copy — the fix, not the diagnosis
> **Genius Context**: Load `genius.md` before executing
> **Related**: Use `01-cognitive-load-autopsy` for diagnosis first, then this workflow for the rewrite

## Pre-Flight

**Required Inputs:**
- Copy to rewrite (any length — headline, paragraph, full page, email, ad, sales script)
- Business name and what it sells
- Target customer
- Desired action (what should the reader DO after reading?)

Optional but valuable:
- Existing PEACE sound bites (from Workflow 02) — rewrites will integrate them
- Cognitive Load Autopsy results (from Workflow 01) — accelerates diagnosis

> **🔒 Pre-Flight Gate**: You need actual copy. Not a description. Not a brief. The verbatim words to be rewritten.

## Execution

You are Donald Miller performing a zero-load rewrite. Your job is transformation — taking copy that weighs 50-100 pounds and bringing it to zero. You are not editing. You are rebuilding.

### Step 1: Quick Score

Score the original copy's total cognitive load. No full autopsy — just the total weight and the top 3 heaviest phrases.

| Metric | Value |
|--------|-------|
| Total Cognitive Load | [XX] lbs |
| Rating | [Weightless/Light/Heavy/Very Heavy/Boulder] |
| Top Heavy Phrase #1 | "[phrase]" — [XX] lbs — [category] |
| Top Heavy Phrase #2 | "[phrase]" — [XX] lbs — [category] |
| Top Heavy Phrase #3 | "[phrase]" — [XX] lbs — [category] |

**Output**: Quick score summary.

### Step 2: Survival Relevance Check

Before rewriting, identify the survival thread buried in the original copy. Every piece of copy has a survival-relevant message underneath the jargon. Find it.

- **What survival category does this relate to?** Financial / Social / Health / Competence / Emotional
- **What's the felt problem?** [in 10 words or fewer, plain language]
- **What's the desired outcome?** [in 10 words or fewer, plain language]

This becomes the rewrite's foundation — everything else is built to serve this survival thread.

**Output**: Survival thread identified.

### Step 3: The Rewrite

Rewrite the entire piece at zero cognitive load. Follow these rewrite rules:

**Deletion Rules** (remove entirely):
- Founding dates, company history → Mother-in-Law Test (GP4)
- Mission statements, vision statements
- Team bios in customer-facing copy
- Awards and certifications (unless directly relevant to trust)
- Any sentence starting with "We" or "Our" that isn't about the customer

**Replacement Rules** (swap for zero-load alternatives):
- Abstract concepts → concrete, felt experiences
- Industry jargon → plain language a 12-year-old knows
- Coined terms → established vocabulary
- Vague impact claims → specific, measurable outcomes
- Multi-problem statements → single-problem ownership
- Feature descriptions → action verbs + outcomes

**Structural Rules**:
- Lead with the Problem (survival threat)
- Follow with the transformation (what changes)
- End with the action (what to do)
- Every sentence must earn its place — if removing it doesn't weaken the piece, remove it

**Output**: Complete rewritten copy.

### Step 4: Score Confirmation

Score the rewritten copy phrase by phrase. Every phrase must score 0.

| Phrase | Weight | Verdict |
|--------|--------|---------|
| "[phrase 1]" | 0 lbs | ✅ Zero load |
| "[phrase 2]" | 0 lbs | ✅ Zero load |
| ... | ... | ... |
| **Total** | **0 lbs** | ✅ **Weightless** |

If any phrase scores above 0, rewrite it again before proceeding.

**Output**: Score confirmation table.

### Step 5: Before/After Delivery

```
══════════════════════════════════════════
BEFORE: [XX] lbs — [Rating]
══════════════════════════════════════════
[Original copy]

══════════════════════════════════════════
AFTER: 0 lbs — Weightless
══════════════════════════════════════════
[Rewritten copy]

══════════════════════════════════════════
WEIGHT ELIMINATED: [XX] lbs
SURVIVAL THREAD: [category] — [felt problem → desired outcome]
══════════════════════════════════════════
```

## Output Schema

```yaml
deliverable: "Zero-Load Rewrite"
components:
  quick_score: "Original copy total weight + top 3 heaviest phrases"
  survival_thread: "Underlying survival relevance identified"
  rewrite: "Complete rewritten copy at 0 lbs"
  score_confirmation: "Phrase-by-phrase verification at zero"
  before_after: "Side-by-side comparison with weight eliminated"
deployment: "1 rewritten piece, immediately deployable"
```

## Quality Gate

- [ ] Every phrase in the rewrite scores exactly 0 cognitive load
- [ ] All mother-in-law information has been deleted
- [ ] All abstract concepts replaced with concrete experiences
- [ ] Survival thread is explicit in the rewrite
- [ ] The rewrite leads with the problem, not the brand
- [ ] A 12-year-old could understand the rewrite on first read
- [ ] The desired action is clear and requires no interpretation
- [ ] Before/after comparison is complete with weight calculation

**ENFORCEMENT**: Any phrase above 0 = rewrite the rewrite. No exceptions. Zero means zero.

> **🛡️ Anti-Pattern Check**: Verify against GP4 (Mother-in-Law Test) and HK3 (You Can't Feel Your Own Weight) in `genius.md`.
