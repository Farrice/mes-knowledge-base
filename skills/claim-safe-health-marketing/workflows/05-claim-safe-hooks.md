---
description: Generate hooks/headlines for health-brand content that are claim-safe by construction — compliance front-loaded into ideation, not retrofitted after the fact
---

# /claim-safe-hooks — Front-Loaded Compliant Ideation

Generate hooks, headlines, and openers for health/supplement/wellness content that never touch disease-claim territory in the first place. This is the workflow to run BEFORE drafting, not after — it stacks with `farrice-engine`/`jw-engine`/`copy-engine` hook generation as the compliance-aware front door for health-brand work.

## Pre-Flight Gate

**Use this when**:
- Starting hook/headline ideation for a health, wellness, or supplement brand from a blank page
- `jw-engine` or `copy-engine` is producing hooks for a health-brand client and needs the claim-safe filter applied at generation time, not as a post-hoc audit
- A creative brief needs 10-15 hook options where all of them are pre-cleared, not just the ones that happen to survive an audit

**Do NOT use this when**:
- Copy already exists — that's `/claim-audit` (diagnose) then `/compliant-rewrite` (fix), not this workflow
- The brand/product has no supplement or health-outcome claim dimension at all (pure lifestyle/brand content) — standard hook workflows apply without this filter

## Skill Acquisition

Load before executing:
- `genius.md` — GP-01 (Taxonomy), GP-07 (Rewrite Patterns — used here as GENERATION patterns, not just fixes), GP-09 (Gut Check auto-fails)
- `references/red-flag-word-bank.md` — to know which hook territory to avoid from the start

## Execution

### Step 1: Identify the Real Selling Point (Not the Claim)

Before writing any hook, separate the brand's actual differentiator into one of three buckets:
- **Ingredient/formulation specificity** (a real, nameable difference — e.g., glycinate vs. oxide, specific dose, delivery mechanism)
- **Experience/emotion** (what a real customer feels, described without disease-outcome framing)
- **Mechanism/how-it-works** (a genuine physiological story that doesn't promise a disease outcome)

Every hook in this workflow must originate from one of these three, never from an outcome-guarantee or disease-claim frame — this is the front-loading move: start from what's compliantly true, not from the most dramatic possible claim and then walk it back.

### Step 2: Generate Hooks by Bucket

For each of the three buckets in Step 1, generate 3-5 hooks using genius.md GP-07 moves:
- **Mechanism-led hooks** (Move 1): open with the specific, nameable mechanism/ingredient difference
- **Experience-led hooks** (Move 2): open with the real customer feeling/moment, stripped of disease-outcome language
- **Social-proof-led hooks** (Move 3): open with a specific, verifiable number (review count, years formulating, ingredient sourcing detail) rather than a guaranteed-outcome promise

### Step 3: Auto-Fail Screen (genius.md GP-09)

Before presenting any hook, screen against the FTC Gut Check absolute-claim patterns for weight-loss-adjacent categories — these patterns are auto-fail regardless of how they're phrased:
- Any hook implying substantial weight loss without diet/exercise
- Any hook implying a worn/applied product causes weight loss
- Any hook using outcome-stacking language even in a "soft" frame ("finally feel confident" is fine; "finally lose the weight without trying" is not)

Discard and regenerate any hook that fails this screen — do not soften-and-keep.

### Step 4: Present with Rationale

For each hook delivered, state which bucket (Step 1) and which GP-07 move it came from — this makes the compliance reasoning visible to whoever picks the winning hook, so a non-compliant edit doesn't get introduced downstream without anyone noticing why the original was safe.

### Step 5: Output

```markdown
# Claim-Safe Hooks — [brand/product/category]

## Selling Point Inventory
- Ingredient/formulation: [...]
- Experience/emotion: [...]
- Mechanism: [...]

## Hooks
| # | Hook | Bucket | GP-07 move | Platform fit |
|---|---|---|---|---|
| 1 | "..." | Mechanism | Move 1 | Meta / TikTok / Amazon / all |
| ... | | | | |

## Auto-Fail Screen
[confirm: all hooks screened against GP-09; n discarded and regenerated]

## Recommended next step
Route winning hook(s) through /compliant-rewrite if expanding to full copy, or /pre-launch-compliance-gate if going straight to a platform.
```

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| **Weight-management category** | Heaviest GP-09 screening load — default to experience/emotion bucket (confidence, energy, how clothes fit) over any outcome-implying frame |
| **TikTok-first content** | Weight to wellness framing (energy/recovery/balance) per `references/platform-rules.md` TikTok section — central-claim weight-loss hooks will fail platform review even if FTC-clean |
| **Amazon listing headlines** | Run every hook candidate through a manual disease-name-token check — a mechanism hook can accidentally include a disease word in an aside |
| **Influencer brief hooks** | Include the claim-boundary rationale IN the brief handed to creators, not just the hook — creators need to know why a hook is safe so they don't "improve" it into a violation |

## Output Requirements

1. Every hook traceable to a real selling point (Step 1), never to an invented outcome
2. Every hook labeled with its bucket and GP-07 move
3. Auto-fail screen explicitly run and reported (count discarded/regenerated)
4. Hooks fit for purpose (platform noted) so downstream routing doesn't require re-diagnosis

## Quality Gate

- [ ] No hook implies an outcome the brand's selling-point inventory doesn't actually support
- [ ] GP-09 auto-fail screen was run on every hook, not spot-checked
- [ ] Rationale is visible per hook (bucket + move), not just a bare list
- [ ] At least one hook per selling-point bucket delivered (mechanism/experience/social-proof) — don't over-index on the easiest bucket

If any check fails, regenerate the failing hooks before presenting the set.
