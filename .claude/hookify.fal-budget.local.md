---
name: fal-budget-check
enabled: true
event: bash
pattern: fantastic-posters|gen\.sh|generate\.js|fal_budget_guard|fal_video_kling|fal_video_seedance
action: warn
---

**Fal Budget Guard — MANDATORY (mode-aware v2)**: Before any Fal call (`./gen.sh`, `fal_video_kling.py`, `fal_video_seedance.py`), run:
```
python3 execution/fal_budget_guard.py check --mode=<poster|edit|kling|seedance-480p|seedance-720p> [--quality=...] [--duration=...] [--audio=...]
```
Only proceed if check returns exit 0. After the call, log spend:
```
python3 execution/fal_budget_guard.py log --mode=<...> ... --status=success [--actual-cost=N]
```
**`mode=seedance-1080p` is HARD-BLOCKED** — guard refuses, wrappers refuse. No runtime override.
Wallet: $20 with $5 refill threshold. Per-call ceilings: poster $1, kling $2, seedance-720p $3. Daily $6, cycle $15. Limits in `.agent/fal-usage.json`. Full policy: `directives/fal-usage-policy.md`.

If you see this hook fire and HAVEN'T run the check first, STOP. Run the check, then proceed only if allowed.
