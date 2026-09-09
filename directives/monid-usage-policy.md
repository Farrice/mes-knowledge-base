# Monid Usage Policy

> **Workspace allowance: $10 per calendar month.**
> Quote every paid run. Default quote: $0.50. Approval above $0.50.
> Absolute task or tranche cap: $3.00. Last updated: 2026-09-03.

## The Rule

Monid discovery, endpoint inspection, identity, and balance checks are free. A
paid Monid run must follow:

1. Discover the exact tool.
2. Inspect its current price and input limits.
3. Quote the expected total cost locally.
4. Run only when the quote is approved.
5. Log the actual cost returned by Monid.

```bash
python3 execution/monid_client.py quote \
  --task "Instagram archive inventory" \
  --estimated-cost 0.15
```

If no reliable estimate is available, the quote defaults to `$0.50`. Do not
interpret that default as proof the provider will charge no more than $0.50;
inspect the tool first.

## Decision Boundaries

| Estimated task cost | Decision |
|---:|---|
| `$0.00-$0.50` | Local guard passes |
| `>$0.50-$3.00` | Explicit Farrice approval required |
| `>$3.00` | Hard stop; split or narrow the task |
| Projected month `>$10.00` | Hard stop |

The monthly warning begins at `$7.50`.

## Commands

```bash
# Read-only status
python3 execution/monid_client.py budget-status

# Pre-run quote; exits 0=pass, 2=approval required, 1=denied
python3 execution/monid_client.py quote \
  --task "Instagram comment tranche" \
  --estimated-cost 3.00

# Record the actual price returned after a run
python3 execution/monid_client.py log \
  --query "Instagram comment tranche" \
  --cost 2.85 \
  --results 1900
```

For a shell-based `monid run`, the workspace cost hook also applies the `$0.50`
default, `$3` task cap, and `$10` monthly stop. Connector/MCP calls do not pass
through the shell hook, so the quote command is the required manual preflight.

## Best-Fit Uses

Use Monid for bounded queries where provider access is materially better than
open-web research. Bulk extraction is allowed only with a measured pilot,
resumable checkpoints, and tranches at or below $3.

Do not use Monid for unbounded exploration, or when the remaining budget cannot
complete the next declared tranche. Apify is not an active fallback.

## Fallback

If a quote is denied or Monid fails:

1. Narrow the task or result count.
2. Use native web research for open-web evidence.
3. Report the evidence gap instead of silently spending more.

## Override Boundary

Increasing the `$3` task cap or `$10` monthly allowance is a policy change and
requires Farrice's explicit approval plus a workspace patch. Do not edit the
tracker to bypass a denial.
