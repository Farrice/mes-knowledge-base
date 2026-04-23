# Google API Setup Checklist — Browser Actions

> **For Farrice. One-time setup, ~15 minutes.** Complete these before running `/deep-research-gemini` for the first time.
>
> **Why**: Three layers of defense guarantee maximum possible spend = $10. See `directives/google-api-usage-policy.md` for the architecture.

---

## Before You Start

**You'll need:**
- Your Google account that owns the Gemini AI Ultra subscription
- A browser logged into that account
- Access to the `.env` file at `/Users/farricecain/Google Antigravity/.env`

**What you're doing:**
1. Link Ultra subscription to AI Studio (primary billing path)
2. Confirm pay-as-you-go is disabled (prevents overflow)
3. Load $10 prepaid balance (absolute ceiling)
4. Generate an API key from the Ultra-linked account
5. Add the key to `.env` as `GOOGLE_AI_STUDIO_KEY`

---

## Layer 1: Link Ultra Subscription to AI Studio

1. Open https://aistudio.google.com/
2. Sign in with the same Google account that owns your Gemini AI Ultra subscription
3. Click the **gear icon** (Settings) in the top right
4. Under "Subscription" or "Plan," look for **"Link Google AI Plan"** or **"Connect subscription"**
5. Complete the linking flow — confirm in-browser
6. Refresh AI Studio. Look for your tier badge — should say **"Google AI Ultra"** or show Ultra-tier limits

**How to verify:** AI Studio → Settings → Usage dashboard should show Ultra-tier daily/monthly limits, not free-tier limits.

✅ **Done when**: Tier badge or usage dashboard confirms Ultra.

---

## Layer 2: Disable Pay-as-You-Go (Critical Safety)

1. Still in AI Studio → Settings → **Billing** tab
2. Look for **"Billing account"** or **"Pay-as-you-go"** or **"Cloud billing"**
3. If a billing account is attached for overflow:
   - Click **Remove** / **Detach** / **Unlink**
   - Confirm the detachment
4. The state you want: **"No billing account attached"** OR **"Free tier + subscription only"** — NO pay-as-you-go billing

**Why this matters:** Without this step, if your Ultra limit is hit, API calls would overflow-bill to the attached account. With this step disabled, hitting the Ultra limit just causes API calls to fail — which is what we want.

✅ **Done when**: Billing tab shows no billing account OR explicitly shows "no overflow billing."

---

## Layer 3: Load $10 Prepaid Balance (Absolute Ceiling)

1. AI Studio → Settings → **Billing** or **Credits**
2. Look for **"Prepaid"** or **"Add credits"**
3. Click **Add $10** (or enter $10 as the amount — $10 is the minimum)
4. Complete the purchase

**What this guarantees:** Even if Layers 1 and 2 have a gap (e.g., Ultra doesn't cover Deep Research specifically, or our understanding of billing is wrong), the prepaid balance is a hardware limit. When it hits $0, all API requests stop instantly. You cannot be charged more than $10 through this path — ever.

**If you cannot find prepaid option:** It may only be available after Layer 1 is complete. Try refreshing or checking in a different section (e.g., "Billing" vs "Plans & pricing").

✅ **Done when**: You see "$10.00 prepaid balance" somewhere in your AI Studio billing settings.

---

## Step 4: Generate the API Key

1. AI Studio → **Get API key** (button in the left sidebar or top nav)
2. Click **Create API key**
3. If prompted for a project, select or create one (any project works — billing goes through the Ultra link, not the project)
4. Copy the key — it starts with `AIza...`
5. **Important**: This key should say "Ultra subscription" or show no separate billing account when you view its details

⚠️ **Critical**: If the key shows "Pay-as-you-go" or is attached to a separate billing account, Layer 2 is not working. Stop and re-verify Layer 2 before continuing.

✅ **Done when**: You have an API key starting with `AIza...` copied to clipboard.

---

## Step 5: Add Key to .env

Open `/Users/farricecain/Google Antigravity/.env` in your editor.

Add this line (replace `AIza...` with your actual key):

```
GOOGLE_AI_STUDIO_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**Do NOT change `GEMINI_API_KEY`** — that's the legacy key used by `parallel_swarm.py` etc. Keep it as-is. `GOOGLE_AI_STUDIO_KEY` is a new, separate variable.

Save `.env`.

✅ **Done when**: `.env` contains `GOOGLE_AI_STUDIO_KEY=...` as a new line.

---

## Verification Tests

After completing steps 1-5, run these to confirm everything works.

### Test 1: Environment loaded

```bash
cd "/Users/farricecain/Google Antigravity"
python3 -c "from execution.deep_research_client import load_env, DeepResearchClient; load_env(); c = DeepResearchClient(); print('✅ Client initialized. Budget remaining:', c.budget_remaining())"
```

Expected: `✅ Client initialized. Budget remaining: 10.0`

If you see `ValueError: GOOGLE_AI_STUDIO_KEY not found`, Step 5 wasn't saved — double-check `.env`.

### Test 2: First Deep Research call (small test)

```bash
cd "/Users/farricecain/Google Antigravity"
python3 execution/deep_research_client.py "What is the Claude Code fork subagent feature?" --mode standard --task-context "setup-verification-test"
```

Expected:
- Prints "Starting Deep Research (standard)"
- Waits 1-5 minutes
- Returns research report with citations
- Prints usage summary showing 1 query logged

**Budget check after this call:**

```bash
cat .agent/gemini-api-usage.json | python3 -m json.tool | head -20
```

Expected: `total_queries: 1`, `estimated_cost_usd: 0.5` (our estimate — actual may differ)

### Test 3: Confirm Ultra is covering the call

Open https://aistudio.google.com/ → Usage dashboard. You should see a recent API call logged under Ultra usage, NOT under prepaid consumption.

If prepaid was consumed: Ultra is NOT covering Deep Research. The $10 ceiling is now doing its job. Either accept the $0.50/query cost (good for up to ~20 queries) or stop using Deep Research API until Ultra coverage expands.

---

## What To Do If Something Goes Wrong

| Problem | What it means | What to do |
|---|---|---|
| API returns 402 "payment required" | Ultra didn't cover, and prepaid isn't loaded | Verify Step 3 (prepaid) completed |
| API returns 403 "forbidden" | Ultra Plan Linking didn't complete | Re-do Step 1 |
| API returns 429 "rate limit" | Hit Ultra daily quota | Wait 24h or use Perplexity fallback |
| Client throws BudgetExhaustedError | Prepaid below $0.50 | Refill prepaid OR use Perplexity |
| Research takes >15 min | Expected for Max mode; normal | Wait or cancel with Ctrl+C and use standard mode |

---

## After Setup: Next Steps

Once the 5 steps above are complete and Test 2 passes:

1. **Run the pilot comparison** (from the plan):
   - Pick an actual upcoming research question you'd run `/deep-research` on
   - Run it via `/deep-research-gemini` AND `/deep-research` in parallel
   - Compare outputs — cite count, depth, accuracy
   - Do this 5-10 times over the next 2 weeks

2. **Decide at 30 days** (per Phase 4 of the plan):
   - Deep Research wins decisively → make it the default, reallocate Perplexity budget
   - Even → keep both
   - Worse → abandon, you've spent at most $10 learning

3. **Don't do these things** (they'll break the safety):
   - ❌ Enable pay-as-you-go on any API key
   - ❌ Auto-refill prepaid without a manual check
   - ❌ Use `GEMINI_API_KEY` for Deep Research (uses legacy billing)
   - ❌ Set `GOOGLE_AI_STUDIO_KEY` on an account not linked to Ultra

---

## Optional: $100 Google Cloud Budget (Phase 0 Layer 4)

This is separate from the AI Studio setup above. Only do this if you want to prepare for potential future Vertex AI usage.

1. Open https://console.cloud.google.com/billing
2. Select your project (memory references `jarvis-v2-488418`)
3. Go to **Budgets & alerts** → **Create budget**
4. Set **Amount**: $100/month
5. Under **Actions**, enable **"Disable billing on cap"** — this programmatically kills paid API access when the cap hits
6. Add email alerts at 50%, 80%, 100%

This ensures the $100 Cloud credits included in Ultra cover any accidental Vertex AI use, with hard kill-switch at cap.

**Skip this for now if you're not planning to use Vertex AI.** Not needed for Deep Research.

---

*Created: 2026-04-23 | Related: `directives/google-api-usage-policy.md`, `.agent/workflows/deep-research-gemini.md`*
