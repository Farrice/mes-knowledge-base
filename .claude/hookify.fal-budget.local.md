---
name: fal-budget-check
enabled: true
event: bash
pattern: fantastic-posters|gen\.sh|generate\.js|fal_budget_guard
action: warn
---

**Fal Budget Guard — MANDATORY**: Before any `./gen.sh` (or `node generate.js`) call, run:
```
python3 execution/fal_budget_guard.py check --quality=<low|medium|high> --n=<count>
```
Only proceed if check returns exit 0. After the call, log spend:
```
python3 execution/fal_budget_guard.py log --quality=<...> --n=<...> --status=success
```
Wallet: $20 with $5 refill threshold. Limits in `.agent/fal-usage.json`. Full policy: `directives/fal-usage-policy.md`.

If you see this hook fire and HAVEN'T run the check first, STOP. Run the check, then proceed only if allowed.
