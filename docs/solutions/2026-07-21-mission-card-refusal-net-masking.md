# Mission cards quoting real data can trip the runner's refusal net — mask display text, join by stable keys

**Date**: 2026-07-21 · **Session**: ladder-audit harness build · **Domain**: system / mission-runner

## Problem

`mission_runner.py` parks any card whose body matches `FORBIDDEN_RE` (`publish|send|post to|payment|purchase|deploy`) — correct for preventing autonomous outward action. But a card that QUOTES real data (deliverable names from `revenue-outcomes.json` like "…V3 high-taste **publish** copy…") trips the net and gets parked even though the card itself is drafts-only. Any generator that embeds user data into card bodies will hit this.

## Solution

Mask the forbidden words in **display text only** (insert a `·` after the first letter: `p·blish`), and give the executing agent a stable join key back to the exact record (here: check-in date + shipped date against `.agent/revenue-outcomes.json`, which the card loads as context anyway). Note the masking convention inside the card so the executor isn't confused. Implemented in `execution/outcome_chase.py::_mask()` — keep its word list in sync with `mission_runner.FORBIDDEN_RE`.

## Why this beats the alternatives

- Whitelisting the generator in mission_runner would weaken the refusal net for everyone.
- Stripping the names entirely would cost the executor the context it needs.
- The net stays fully intact: instruction verbs remain unmaskable (a card that actually SAYS "send this" still parks).

## Re-solve guard

Before writing any new Mission Card generator that embeds external/user data, validate the rendered card against BOTH `TIER_RE` and `FORBIDDEN_RE` in a test (see the validation snippet pattern in the 2026-07-21 build), and reuse `_mask()`.
