---
description: Full go/no-go compliance gate before a health/supplement asset ships — wraps claim-audit, substantiation-map, disclaimer placement, and all three platform-specific passes
---

# /pre-launch-compliance-gate — The Ship/No-Ship Decision

The final gate before any health-brand asset goes live. Wraps `/claim-audit` + `/claim-substantiation-map` outputs, adds disclaimer-placement verification and a platform-by-platform pass (Meta/TikTok/Amazon), and produces a single go/no-go verdict. This is the workflow that should run on EVERY Path A client asset before publish, regardless of how the copy was produced.

## Pre-Flight Gate

**Use this when**:
- An asset is fully drafted (post-rewrite) and about to publish, launch, or go into paid media
- A funded health/wellness/supplement brand deliverable needs a final compliance sign-off
- Any output from `farrice-engine`, `jw-engine`, or `copy-engine` touches a health/supplement claim and hasn't been routed through this skill yet

**Do NOT use this when**:
- Copy hasn't been audited or rewritten yet — run `/claim-audit` → `/compliant-rewrite` (and `/claim-substantiation-map` if evidence is uncertain) first; this gate assumes those passes already happened and verifies the RESULT, it doesn't re-do the diagnostic work from scratch
- The asset has no health/supplement claim at all (pure brand/lifestyle content with zero structure-function or efficacy language) — this gate isn't needed; use standard finalize

## Skill Acquisition

Load before executing:
- `genius.md` — full file (this gate exercises every GP)
- `references/platform-rules.md` — Meta/TikTok/Amazon sections
- `references/red-flag-word-bank.md` — final token scan

## Execution

### Step 1: Confirm Prior Passes Ran

Verify (don't assume) that `/claim-audit` and, if applicable, `/claim-substantiation-map` were run on this asset. If not, halt and run them first — this gate is a verification layer, not a substitute for the diagnostic work.

**Deterministic first pass (optional but recommended)**: before the judgment-based steps below, run the mechanical scanner over the final asset — it catches the same disease-claim/red-flag-word/unqualified-results patterns as a fast, non-negotiable first cut and names the compliant swap for each hit:

```bash
python3 execution/claim_risk_scan.py scan <asset-file> [--json]
```

This is also wired into `chain_runner.py finalize` (auto-fires on health-flavored Content/Client Work/Creative deliverables) — a DISEASE_CLAIM verdict there prints a loud warning at finalize time, so a compliance miss surfaces even if this workflow itself isn't invoked. Treat any DISEASE_CLAIM hit as a hard stop for Step 6; RISKY/WATCH hits still require the judgment passes below.

### Step 2: Disclaimer Verification

Confirm the DSHEA disclaimer is present, verbatim, and correctly placed for the target channel:

> "This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease."

- Meta: must be IN the ad copy itself (2026 requirement), not just linked landing page
- Amazon: required in listing if any reasonable reader could infer FDA review occurred
- Email/landing page: standard footer or claim-adjacent placement is sufficient

### Step 3: Platform-by-Platform Pass

Run the asset through each relevant platform's rules from `references/platform-rules.md` independently — do not assume clearing FTC/FDA clears platform review:

- **Meta**: Personal Attributes check (no second-person symptom framing), restricted-phrase scan, in-copy disclaimer
- **TikTok**: central-claim check (is weight-loss/muscle-gain the headline claim — reframe to wellness if so), documentation-required-phrase scan
- **Amazon**: token-level disease-name + treatment-verb scan across every field (title, bullets, description, A+ content)

Skip platforms the asset isn't running on, but note explicitly which were skipped and why.

### Step 4: Testimonial/Endorsement Final Check

If the asset uses any testimonial, review, or influencer content: confirm typical-results disclosure and material-connection disclosure are both present per genius.md GP-05 — this is a common last-mile miss even after copy-level rewriting is clean.

### Step 5: Two-Experts Final Sign-Off

Explicitly answer both halves of genius.md GP-08 one more time on the FINAL asset (not the draft) — the two-experts test is re-run here because platform-driven edits (Step 3) sometimes reintroduce compliance-theater flatness or, conversely, get edited back toward risk to "make it pop."

### Step 6: Go/No-Go Output

```markdown
# Pre-Launch Compliance Gate — [asset name] — [target platform(s)]

## Prior Passes Confirmed
- /claim-audit: [ran / NOT RUN — halted]
- /claim-substantiation-map: [ran / N/A — no evidence-tier claims present]

## Disclaimer
[present + correctly placed / MISSING / incorrectly placed — specify fix]

## Platform Passes
| Platform | Result | Flags |
|---|---|---|
| Meta | [pass/fail/skipped] | |
| TikTok | [pass/fail/skipped] | |
| Amazon | [pass/fail/skipped] | |

## Testimonial/Endorsement Check
[pass/fail + detail]

## Two-Experts Sign-Off
- Regulatory attorney lens: [pass/fail + why]
- DR copywriter lens: [pass/fail + why]

## VERDICT: [SHIP / HOLD — fix n items / BLOCKED — claim has no compliant version]
```

## Content Type Adaptations

| Asset type | Extra gate step |
|---|---|
| **Paid media (any platform)** | Platform pass is mandatory, not optional — organic content gets more latitude on platform-specific rules (still bound by FTC/FDA) |
| **Amazon listing** | Run the token scan on EVERY field separately — A+ content is commonly missed |
| **Influencer/UGC brief going out to creators** | Gate the BRIEF, not just finished content — creators need the disclaimer and claim-boundary instructions before they film |
| **Email sequence** | Gate each email individually AND the sequence's net impression as a whole (escalating urgency across emails can build an implied claim no single email makes) |

## Output Requirements

1. Explicit confirmation that prior diagnostic passes ran — never silently skip to verdict
2. Disclaimer checked for presence AND placement, not just presence
3. Every relevant platform checked independently with its own pass/fail
4. Two-experts test re-run on the FINAL asset, not inherited from the rewrite step
5. Verdict is one of exactly three states (SHIP/HOLD/BLOCKED) — no vague "looks mostly fine"

## Quality Gate

Full genius.md Quality Rubric applies here — this is the workflow the rubric was built for. Veto rule in effect: criterion 1 (classification) or 5 (disclaimer) below 8 caps the gate at BLOCKED/HOLD regardless of how clean everything else is.

- [ ] No claim in the final asset is Bucket 1/2 (disease claim, express or implied)
- [ ] Disclaimer present and correctly placed for every channel the asset runs on
- [ ] All applicable platform passes completed independently
- [ ] Verdict matches the actual flag count — a single unresolved flag cannot produce SHIP
