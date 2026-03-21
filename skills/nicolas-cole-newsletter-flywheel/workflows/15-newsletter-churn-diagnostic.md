# Newsletter Churn Diagnostic

Diagnose why subscribers leave. Maps churn to root cause: faucet problem (wrong tangible asset) vs. execution problem (right asset, bad delivery). Based on Hidden Knowledge #3: "Retention is solved at conception, not execution."

## When to Use

- Churn rate exceeding 3% per month
- Sudden subscriber loss after specific editions
- "I keep losing subscribers and don't know why"
- Before pivoting a newsletter's tangible asset
- Comparing two time periods to understand decline

## Inputs Required

- Newsletter name, tangible asset, audience
- Churn data: monthly unsubscribe count for last 3-6 months
- Unsubscribe survey responses (if available)
- Last 8-12 edition summaries with tangible asset delivered per edition
- Engagement metrics per edition: open rate, click rate, reply count
- Any direct subscriber feedback (emails, comments, DMs)

## Execution

### Phase 1: Churn Classification

Every churn event has one of four root causes:

| Type | What It Means | Signal | Fix Path |
|------|-------------|--------|----------|
| **Faucet Failure** | Wrong tangible asset entirely | Churn is constant regardless of content quality | `/tangible-faucet` redesign |
| **Faucet Drift** | Started with tangible assets, drifted to essays | Churn increases over time | Tangible asset checklist enforcement |
| **Delivery Failure** | Right asset, poor execution | Low marks on specific editions, not pattern-wide | Writing/formatting improvement |
| **Audience Mismatch** | Right asset, wrong subscribers | High churn among subscribers from one acquisition channel | Acquisition channel audit |

### Phase 2: The Forensic Audit

**Step 1 — Edition-Level Churn Map:**
For each of the last 12 editions, mark:
- Did it deliver a tangible asset? (Yes/No)
- What type of tangible asset?
- Open rate vs average
- Churn after this edition vs average

Plot: Editions WITH tangible assets should have lower churn. If they don't → Faucet Failure (wrong asset type entirely).

**Step 2 — The Departure Interview:**
Analyze unsubscribe survey data (if available). Classify each response:
- "Not relevant to me" → Audience Mismatch
- "Too many emails" → Frequency problem (cosmetic, not structural)
- "Content wasn't useful" → Delivery Failure OR Faucet Failure
- "Found better alternatives" → Faucet Failure (competitors have better tangible)
- "Not what I signed up for" → Faucet Drift

**Step 3 — The Faucet Test Replay:**
Take the newsletter's current tangible asset and re-run Cole's tests:
- **Wine Club Test**: "It's like a _____ club but for _____." Does it still work?
- **Faucet Test**: "Do you ever want this faucet to turn off?" Honest answer?
- **Noun Test**: Can a subscriber describe what they GET in one noun?

If any test fails → the tangible asset has degraded. Original concept may have been sound, but the execution drifted.

### Phase 3: Diagnosis Report

Based on the evidence, classify the churn:

**Faucet Failure Diagnosis:**
```
VERDICT: The tangible asset is wrong.
Evidence: [specific data points]
Prescription: Run /tangible-faucet with current audience data.
Timeline: Redesign in 2 weeks, test for 4 weeks, evaluate.
```

**Faucet Drift Diagnosis:**
```
VERDICT: The newsletter started strong but drifted to essays.
Evidence: Tangible asset delivery rate: [X]% (should be 80%+)
Editions without tangible assets: [list]
Prescription: Create a pre-publish checklist:
  □ This edition delivers a [specific noun]
  □ The subscriber can save/bookmark the asset
  □ The asset is distinct from last week's asset
Timeline: Immediate enforcement, re-audit in 30 days.
```

**Delivery Failure Diagnosis:**
```
VERDICT: The right tangible asset, delivered poorly.
Evidence: Churn spikes on specific low-quality editions, not pattern-wide
Prescription: Stack with /newsletter-flywheel for production quality.
  Consider: Is the commentary layer present? (Hidden Knowledge #6)
  The asset alone isn't enough — the expert perspective on the asset is what retains.
Timeline: Improve next 4 editions, re-audit in 30 days.
```

**Audience Mismatch Diagnosis:**
```
VERDICT: Right newsletter, wrong subscribers finding it.
Evidence: Churn concentrated among subscribers from [channel]
Prescription: Audit acquisition channels. Run /newsletter-growth-audit.
  The newsletter may be excellent for its INTENDED audience but promoted to the wrong one.
Timeline: Adjust acquisition targeting, re-audit in 60 days.
```

## Output

```markdown
# Churn Diagnostic — [Newsletter Name] — [Date]

## Churn Classification: [Faucet Failure / Faucet Drift / Delivery Failure / Audience Mismatch]

## Evidence
[Edition-level data, survey analysis, faucet test results]

## Root Cause
[Specific diagnosis with supporting data]

## Prescription
[Ranked action items with specific workflows to run]

## Re-Audit Date
[30 or 60 days from now]
```

## Quality Gate

- [ ] Churn classified into one of the four categories with evidence?
- [ ] Diagnosis based on data patterns, not gut feeling?
- [ ] Faucet tests re-run with honest assessment?
- [ ] Prescription points to specific next workflows (not generic advice)?
- [ ] Re-audit date set to verify the fix worked?
