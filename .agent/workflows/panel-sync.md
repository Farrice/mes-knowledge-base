---
description: Reload a pinned expert panel and reconvene for follow-up deliberation
---

# /panel-sync — Reload & Reconvene

Reload a previously pinned expert panel from a `/assemble` session and reconvene the same voices for follow-up deliberation, refinement, or a new angle on the same task.

This is your "I want the same panel back" command. No re-synthesis. Same roster + bespoke personas. New deliberation.

## Usage
```
/panel-sync "Now let's refine the offer architecture piece"
/panel-sync --session "competitive-sailing-rigging-optimization" "What about durability tradeoffs?"
```

## How to run it

This command reloads and reconvenes the pinned panel. Execute it by:
1. Reading the pinned session from `.agent/handoffs/assemble-<slug>.md` (auto-discovered from recent sessions or specified via `--session`).
2. Loading panel metadata + synthesized personas from `.tmp/assemble/<slug>/`.
3. Reconvening for new deliberation on your follow-up query.

Optional args:
- `session`: slug of a prior `/assemble` session (auto-discovered if omitted; picks the most recent).
- `task`: the follow-up task or refinement question.

## What it does

1. **Reload** — fetch the pinned panel metadata + all synthesized personas from the prior `/assemble` session.
2. **Status** — display panel composition (roster + bespoke members), domains covered, and net-new principle from the original deliberation.
3. **Diverge (refinement)** — all panelists give takes on the follow-up question, reusing their original methodology + voice.
4. **Deliberate** — 1 round of cross-talk on the refinement; contradictions preserved.
5. **Converge** — updated crux + next moves for the refinement.
6. **Learn** — brief digest: how the panel adapted their thinking + what shifted.

## When to use

- **Follow-up refinement** after `/assemble`: "Now let's stress-test the positioning against objections."
- **New angle, same domain**: "How would this shift if we target a different ICP?"
- **Multi-turn deliberation**: "Pause, pivot, continue with the same voices."

## When NOT to use

- **New task, different domains** → use `/assemble` (fresh panel cast).
- **Single-expert follow-up** → invoke that expert directly.
- **Panel composition shift** → `/assemble` for a new cast.

## Output Location

Follow-up deliberation is appended to the session record in `.agent/handoffs/assemble-<slug>.md`. Personas remain in `.tmp/assemble/<slug>/` (unchanged).

---

See also:
- **Original assembly**: `/assemble`
- **Skill home**: `skills/expert-assembly-os/SKILL.md`
