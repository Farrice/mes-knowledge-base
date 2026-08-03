# Fal API Usage Policy (fantastic-posters skill, v2 mode-aware)

> **Wallet**: $20.00 funded, auto-refills when balance drops below $5.00 → effective rolling $15-20 budget per cycle
> **Tracker**: `.agent/fal-usage.json` (v2 schema) | **Guard**: `execution/fal_budget_guard.py` | **Hookify**: `.claude/hookify.fal-budget.local.md`
> Applies to ALL Fal calls: posters (`./gen.sh`), Kling video (`fal_video_kling.py`), Seedance video (`fal_video_seedance.py`), and recipe calls (`generate_media.py`, mode=generic).

> **CAP RAISE (Farrice, 2026-08-02 — "room to play"):** per-day block $6→**$20** (warn $10), per-cycle block $15→**$20** (warn $14); `cost_gate.py` daily hard cap $10→**$20**, session soft $5→**$10**. Older dollar figures below are superseded by `.agent/fal-usage.json` limits — the state file is authoritative. Per-call ceilings and the seedance-1080p hard block are UNCHANGED.

---

## Hard Rule (Non-Negotiable)

**Every Fal call (poster OR video) MUST be preceded by a mode-aware budget guard check, and followed by a budget guard log.** No exceptions, even for "just one quick test."

> **Why `./gen.sh` and not `node generate.js`?** `gen.sh` is the wrapper that sources `FAL_KEY` from the project root `.env` (single source of truth). Same principle for video wrappers — they auto-load FAL_KEY from `.env`.

### Poster (default — backward compatible)
```bash
# 1. PRE-FLIGHT
python3 execution/fal_budget_guard.py check --mode=poster --quality=<low|medium|high> --n=<count>

# 2. RUN
cd "/Users/farricecain/Google Antigravity/skills/fantastic-posters/" && \
  ./gen.sh "<brief>" --quality=<...> --n=<...>

# 3. POST-FLIGHT
python3 execution/fal_budget_guard.py log --mode=poster --quality=<...> --n=<...> --status=success
```

### Kling video
```bash
# 1. PRE-FLIGHT
python3 execution/fal_budget_guard.py check --mode=kling --duration=<3-15> --audio=<off|on|voice_control>

# 2. RUN
python3 execution/fal_video_kling.py --prompt="<motion>" --start-image="<path|url>" --duration=<N> --audio=<...>

# 3. POST-FLIGHT (use --actual-cost from generator output)
python3 execution/fal_budget_guard.py log --mode=kling --duration=<N> --audio=<...> --status=success --actual-cost=<N>
```

### Seedance video
```bash
# 1. PRE-FLIGHT
python3 execution/fal_budget_guard.py check --mode=seedance-720p --duration=<4-15>

# 2. RUN
python3 execution/fal_video_seedance.py --prompt="<motion>" --image="<path|url>" --duration=<N> --resolution=720p --audio=on

# 3. POST-FLIGHT
python3 execution/fal_budget_guard.py log --mode=seedance-720p --duration=<N> --audio=on --status=success --actual-cost=<N>
```

### Edit (image-to-image — fantastic-posters)

Triggered by any of `--input=`, `--refs=`, `--logo=`, `--template=`, or a style flagged `needsPhoto`. Use `--mode=edit` in the guard. Optional `--mask=<url>` constrains the change to a region (white = edit, black = preserve).

```bash
# 1. PRE-FLIGHT
python3 execution/fal_budget_guard.py check --mode=edit --quality=medium --n=1

# 2. RUN — explicit edit on a known URL with optional mask
cd "/Users/farricecain/Google Antigravity/skills/fantastic-posters/" && \
  ./gen.sh "swap the headline to 'TODAY: Lobster Roll $24'" \
    --input=https://v3b.fal.media/files/b/.../poster.png \
    --mask=https://example.com/mask.png \
    --quality=medium

# 3. POST-FLIGHT
python3 execution/fal_budget_guard.py log --mode=edit --quality=medium --n=1 --status=success
```

See `directives/fal-edit-mode-guide.md` for when to edit vs. regenerate, mask format requirements, and ref-URL hosting options.

### Variant batching (cheaper than --n loop)

`--variants=N` (1-4) returns N images in a **single API call**. Total cost is `N × per-image` — same dollars as `--n=N`, but fewer round trips and the per-call ceiling treats it as one request. Use this when you want sibling variants of the same prompt; use `--n=N` when you want the script's per-call diversity nudge.

```bash
# 4 variants in 1 API call — costs 4 × $0.04 = $0.16 at medium
python3 execution/fal_budget_guard.py check --mode=poster --quality=medium --n=4
./gen.sh "boutique wellness retreat" --variants=4 --quality=medium
python3 execution/fal_budget_guard.py log --mode=poster --quality=medium --n=4 --status=success
```

### Background removal — `--rembg`

When `--rembg` is set, after each generated image the script chains a `fal-ai/imageutils/rembg` call (~$0.005) to produce a transparent PNG (`*_alpha.png`) alongside the original. **Two guard cycles fire** — one for generation, one for rembg.

```bash
# Gate generation + rembg separately
python3 execution/fal_budget_guard.py check --mode=poster --quality=medium --n=1
python3 execution/fal_budget_guard.py check --mode=rembg --n=1

# Run with --rembg flag (script handles the chained call)
./gen.sh "logo for a coffee brand on white background" --rembg --quality=medium

# Log both calls
python3 execution/fal_budget_guard.py log --mode=poster --quality=medium --n=1 --status=success
python3 execution/fal_budget_guard.py log --mode=rembg --n=1 --status=success
```

### Large dimensions (up to 3840×2160)

GPT Image 2 supports up to 3840×2160 at ≤ 3:1 aspect, multiples of 16. Use new size presets (`--size=banner-3to1` for 3072×1024, `--size=hero-2to1` for 2560×1280, `--size=poster-xl` for 2048×3072) or pass `--size=WxH` directly. Cost is the same regardless of dimensions — only `--quality` changes the price. Invalid sizes are rejected before the API call with a helpful error.

---

## Multi-Layer Safeguards

The guard enforces independent limits at multiple layers. A call is denied if ANY of them trip:

### Per-call ceilings (mode-aware, v2)

| Mode | Ceiling | What it covers |
|---|---|---|
| `poster` | $1.00 | Catches `--batch=` runaway, `--n=10 --quality=high` mistakes |
| `edit` | $1.00 | Same as poster (similar token cost) |
| `rembg` | $0.10 | Chained `fal-ai/imageutils/rembg` call when `--rembg` flag is set (~$0.005/call) |
| `kling` | $2.00 | ~10s with audio on, ~17s audio off (capped at 15s by API) |
| `seedance-480p` | $1.50 | ~11s at 480p ($0.13/s) |
| `seedance-720p` | $3.00 | ~10s at 720p ($0.30/s) |
| `seedance-1080p` | **HARD-BLOCKED** | $0.68/s — single 15s call ~$10 (50% of wallet). Refused at script level + guard level. |

### Cross-mode caps (single budget, no per-mode allocation)

| Layer | Limit | Why |
|---|---|---|
| **Per-call warn** | $0.30 estimated | Forces conscious choice on expensive single calls |
| **Per-day block** | $6.00 today | Allows 1 video + 1 poster batch per day; caps daily damage |
| **Per-cycle block** | $15.00 cycle | Preserves $5 refill buffer in the wallet |
| **Low-balance cap** | $0.50/call when balance < $5 | Ensures refill threshold isn't burned through |
| **Rate limit** | 5 calls / 5 minutes | Catches accidental retry loops (especially relevant for video) |
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
