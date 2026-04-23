# Google AI API Usage Policy

> **Three layers of defense against overspend.** Applies to Gemini API, Deep Research API, and any future Google AI Studio integration.
>
> State tracked in `.agent/gemini-api-usage.json` | Reset: 1st of month

---

## The Three-Layer Defense

Surprise bills are physically impossible. Three independent systems must all fail simultaneously for any charge to exceed the user's chosen ceiling.

### Layer 1 — Ultra Subscription Coverage (Primary)

- Google AI Studio usage is covered by the Google AI Ultra subscription ($249.99/mo) via "AI Plan Linking" (enabled April 20 2026)
- Ultra provides increased AI Studio usage limits vs free tier
- **Deep Research API** (`deep-research-preview-04-2026`, `deep-research-max-preview-04-2026`) calls should route through this coverage
- When Ultra daily/monthly limit is reached, API returns 429 (rate limit) — request fails, nothing is billed

### Layer 2 — Pay-as-You-Go Explicitly Disabled

- AI Studio account MUST NOT have an active billing account attached for overflow
- If Ultra quota exhausts, requests fail. They do NOT overflow to paid billing.
- Verified by: AI Studio → Settings → Billing → "No billing account attached"

### Layer 3 — Prepaid Balance as Defense-in-Depth

- A **$10 prepaid balance** is loaded on AI Studio as a last-resort ceiling
- Prepaid is physically incapable of overspending — when balance hits $0, all API requests stop instantly with no grace period
- This only matters if Layers 1 and 2 have an undetected gap
- If Ultra coverage works as expected, prepaid balance never depletes

**Maximum possible spend, all layers considered:** $10 one-time, unless user manually refills.

---

## Environment Variable Conventions

| Variable | Purpose | Billing Path |
|---|---|---|
| `GEMINI_API_KEY` | Legacy — Gemini SDK calls in `execution/gemini_client.py` (used by `parallel_swarm.py`, `extraction_swarm.py`, etc.) | Whatever the original account uses |
| `GOOGLE_AI_STUDIO_KEY` | **NEW** — Deep Research API via `execution/deep_research_client.py` | Ultra subscription → prepaid $10 backup |
| `GOOGLE_CLOUD_PROJECT` | Project ID for Vertex AI / Cloud credits | $100/mo Cloud credits (unused) |

**Keys are NOT interchangeable.** Deep Research MUST use `GOOGLE_AI_STUDIO_KEY` only.

---

## When to Use

**As of 2026-04-23: Gemini Deep Research is the PRIMARY research tool for foundation/strategic work.** Perplexity is demoted to fallback + quick-facts role. See `directives/perplexity-usage-policy.md` for Perplexity's new scope.

| Tool | Use When |
|---|---|
| **Deep Research Max** (`deep-research-max-preview-04-2026`) | **PRIMARY** for foundation research, strategic intelligence, any research whose output becomes the basis for high-stakes decisions. Highest quality (93.3% DeepSearchQA) |
| **Deep Research** (`deep-research-preview-04-2026`) | **PRIMARY** for Standard-tier research, faster than Max, suitable when Max is overkill |
| **Gemini SDK (legacy)** | Existing Python automation — NOT changed by this policy |
| **Perplexity** | Fallback ONLY — fires when Deep Research errors, rate-limits, or prepaid is exhausted. Also used for quick single-fact verification (sonar-pro / ask). |

---

## Guardrails

**Pre-query (MANDATORY):**
1. Read `.agent/gemini-api-usage.json`
2. If `prepaid_balance_usd < 0.50` → raise `BudgetExhaustedError`, caller MUST fall back to Perplexity
3. Check per-task cap (max 5 Deep Research queries per task — these are heavy)
4. Check per-minute cap (max 2 queries/60s — Deep Research is slow, rate-limiting prevents accidental loops)

**Post-query:**
- Log query, model, estimated cost, task context
- Deduct from tracked prepaid balance
- If Ultra covers call → cost = 0 but log the query anyway for volume tracking

---

## Cost Model (Estimates)

| Model | Est. Cost Per Query | Notes |
|---|---|---|
| `deep-research-preview-04-2026` | ~$0.25-0.50 | Fast variant |
| `deep-research-max-preview-04-2026` | ~$0.50-1.50 | Max comprehensiveness, slower |

**Assumption**: Ultra Plan Linking covers most calls at $0 marginal cost. Prepaid balance only consumed if Ultra quota exhausted.

If Ultra does NOT cover Deep Research (pending verification in Phase 0):
- $10 prepaid → 7-20 queries before stopping
- System falls back to Perplexity sonar-deep-research (~$0.25/query, $30/mo budget)

---

## Fallback Behavior (Non-Negotiable)

When Deep Research is unavailable for ANY reason (budget, rate limit, API error, network):

```
1. Log the failure to .agent/gemini-api-usage.json
2. Silently fall back to Perplexity sonar-deep-research via perplexity_client.py
3. Tag the output with source: "Perplexity (Deep Research fallback)"
4. Never silently return empty results
```

---

## Verification Protocol

Before relying on this policy, verify all three layers:

1. **Layer 1 check**: Sign into AI Studio. Account settings show "Google AI Ultra" tier. Usage dashboard shows Ultra limits.
2. **Layer 2 check**: AI Studio → Settings → Billing shows **no billing account attached** for overflow. (If one is attached, remove it.)
3. **Layer 3 check**: AI Studio → Settings → Prepaid balance shows **$10.00** remaining.

Run all three checks before first Deep Research call. Re-verify monthly (1st of month) as part of budget review.

---

## Usage Tracking

| Field | Value |
|---|---|
| **Last Activated** | *Not yet activated — pending Phase 0 browser setup* |
| **Activation Count** | 0 |

*Created: 2026-04-23*
