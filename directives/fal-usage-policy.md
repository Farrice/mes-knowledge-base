# Fal API Usage Policy (fantastic-posters skill)

> **Wallet**: $20.00 funded, auto-refills when balance drops below $5.00 → effective rolling $15-20 budget per cycle
> **Tracker**: `.agent/fal-usage.json` | **Guard**: `execution/fal_budget_guard.py` | **Hookify**: `.claude/hookify.fal-budget.local.md`
> Applies to ALL invocations of `./gen.sh` in `skills/fantastic-posters/`.

---

## Hard Rule (Non-Negotiable)

**Every `./gen.sh` call MUST be preceded by a budget guard check, and followed by a budget guard log.** No exceptions, even for "just one quick test."

> **Why `./gen.sh` and not `node generate.js`?** `gen.sh` is the wrapper that sources `FAL_KEY` from the project root `.env` (single source of truth). Direct `node generate.js` calls fail with "FAL_KEY missing" unless you manually export it. Always use the wrapper.

```bash
# 1. PRE-FLIGHT — gate the call
python3 execution/fal_budget_guard.py check --quality=<low|medium|high> --n=<count>

# 2. RUN — only if check returned exit code 0
cd "/Users/farricecain/Google Antigravity/skills/fantastic-posters/" && \
  ./gen.sh "<brief>" --quality=<...> --n=<...>

# 3. POST-FLIGHT — record actual spend (status=success or failed)
python3 execution/fal_budget_guard.py log --quality=<...> --n=<...> --status=success
```

---

## Multi-Layer Safeguards

The guard enforces six independent limits. A call is denied if ANY of them trip:

| Layer | Limit | Why |
|---|---|---|
| **Per-call ceiling** | $1.00 estimated | Catches `--batch=` runaway and `--n=10 --quality=high` mistakes |
| **Per-call warn** | $0.30 estimated | Forces conscious choice on expensive single calls |
| **Per-day block** | $4.00 today | Prevents same-day bursts (max ~3 high-quality + medium calls) |
| **Per-cycle block** | $15.00 cycle | Preserves $5 refill buffer in the wallet |
| **Low-balance cap** | $0.50/call when balance < $5 | Ensures refill threshold isn't burned through |
| **Rate limit** | 5 calls / 5 minutes | Catches accidental retry loops |
| **Failure circuit** | 2 consecutive failures → halt | Prevents wasted spend on config errors |

---

## Quality Defaults by Use Case

Use the cheapest quality that meets the deliverable bar. Defaults are codified in workflow files:

| Use case | Default quality | Cost/image | Why |
|---|---|---|---|
| **Style exploration / first draft** | `low` | $0.011 | Cheap iteration, see if style fits before committing |
| **My.BPM streetwear posters** | `medium` | $0.040 | Social-grade output, multiple variants for selection |
| **Parallax Substack covers** | `medium` | $0.040 | Substack header quality bar |
| **Jen's listing posters (client-facing)** | `high` | $0.170 | Client deliverable; print-quality matters |
| **Strategy brief / deliverable covers** | `high` | $0.170 | Premium signal, client-facing |
| **Internal experiments / A/B tests** | `low` | $0.011 | Volume over polish |

**When in doubt, start at `low`. You can re-render the winner at `high` after picking.**

---

## Workflow Patterns

### Style exploration (cheap)
```bash
# Generate 3 low-quality variants to find the style that fits
python3 execution/fal_budget_guard.py check --quality=low --n=3
./gen.sh "<brief>" --n=3 --quality=low
python3 execution/fal_budget_guard.py log --quality=low --n=3 --status=success
# Cost: ~$0.033
```

### Final render (after style locked in)
```bash
# Once you've picked the style + brief, render high-quality single
python3 execution/fal_budget_guard.py check --quality=high --n=1
./gen.sh "<brief>" --style=<picked-style> --quality=high
python3 execution/fal_budget_guard.py log --quality=high --n=1 --status=success
# Cost: ~$0.17
```

### Batch (e.g., Jen's listings) — extra caution
```bash
# Estimate batch size first. Multiply n × per-image. Refuse if > $1.00.
# Example: 5 listings at high = 5 × $0.17 = $0.85. Allowed.
# Example: 20 listings at high = 20 × $0.17 = $3.40. BLOCKED — split into chunks.
python3 execution/fal_budget_guard.py check --quality=high --n=5
./gen.sh --batch=listings.json --quality=high
python3 execution/fal_budget_guard.py log --quality=high --n=5 --status=success
```

---

## Failure Modes & Recovery

### "DENIED: per-call ceiling exceeded"
- Lower `--quality` from high → medium (4× cheaper) or medium → low (3.6× cheaper)
- Reduce `--n` (split into multiple smaller calls)
- Re-run the check after adjusting

### "DENIED: cycle cap reached"
- Stop generating until refill happens
- Run `python3 execution/fal_budget_guard.py status` to see current state
- After Fal auto-refill confirms (check fal.ai dashboard), run:
  ```bash
  python3 execution/fal_budget_guard.py refill-confirm
  ```
- This resets the cycle counter and wallet estimate

### "HALTED: 2 consecutive failures"
- DO NOT keep retrying. Diagnose first.
- Check: FAL_KEY valid? Brief well-formed? Style ID correct? Network connectivity?
- After fixing, run:
  ```bash
  python3 execution/fal_budget_guard.py reset-failures
  ```

### "Rate limit (5 calls / 5 min)"
- Wait 5 minutes — the timestamps prune automatically
- Investigate: was this a loop? Add a guard at the orchestration layer

### Failed call but Fal billed us
- Add `--fal-billed` flag to the log command:
  ```bash
  python3 execution/fal_budget_guard.py log --quality=high --n=1 --status=failed --fal-billed
  ```

---

## Status Commands

```bash
# Quick check anytime
python3 execution/fal_budget_guard.py status

# Confirm refill happened (call after fal.ai dashboard shows fresh $20)
python3 execution/fal_budget_guard.py refill-confirm

# Clear halt state (only after diagnosing the cause)
python3 execution/fal_budget_guard.py reset-failures
```

---

## Why These Limits

The user's wallet is $20 with auto-refill at $5 — meaning the *available* budget is always $15-20, and there's no protection at the Fal layer. Every dollar burned on misuse, errors, or fail modes is a dollar of real money, not a free credit.

Limits are calibrated so that:
- **Worst single mistake costs ≤ $1.00** (per-call ceiling)
- **Worst single day costs ≤ $4.00** (daily cap = 20% of wallet)
- **Cycle exhaustion preserves $5 buffer** so refill timing isn't critical
- **Loops can't run away** (rate limit + failure circuit)

If usage patterns prove the limits are too tight, raise them deliberately by editing `.agent/fal-usage.json` `limits` block. **Never raise them mid-task to push a call through.**
