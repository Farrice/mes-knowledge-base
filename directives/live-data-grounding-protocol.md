# Live-Data Grounding Protocol

> **Goal**: content decisions start from what's provably working THIS WEEK, not from
> training memory or blank-page ideation. **Scar**: Apify sat at 2-3% utilization for
> months while Farrice ideated from scratch ("we keep trying to come from scratch when
> there are proven formulas" — 2026-08-05); the pulse sub-budget existed since
> 2026-07-16 and was never once used. Sibling protocol: `directives/recall-grounding-protocol.md`
> (same shape — this is its live-web twin). Compass doctrine applies: this NUDGES and
> auto-fires; it never blocks. Suppression flag: `--no-live`.

## Trigger (all three, mirrors Recall grounding)
1. Chain Step 3 routed to an expert whose domain is grounding-relevant (content, copy,
   brand, voice, hooks, storytelling, positioning, strategy, sales, marketing,
   persuasion, comms, attention, audience, creative).
2. The deliverable benefits from market freshness (posts, hooks, angles, campaigns,
   offers, zeitgeist questions). Pure memoir/voice work does not.
3. No `--no-live` in the request.

## The ladder (cheapest first — stop at the first rung that lands)
1. **Today's zeitgeist brief** ($0): freshest `deliverables/research-briefs/zeitgeist-<lane>-*/`
   ≤48h for the matching lane. Its evidence rows + decision layer are the live signals.
   Agent-paste form: the sibling `*-brief.md` / `*-brief.json`.
2. **One cheap pull** (~$0.01-0.05): `python3 execution/apify_client.py twitter|threads-search
   "<topic>" --limit 30 --pulse-mode`. `fallback: true` or `pulse_skipped` → silent skip
   to rung 3; never retry, never block (the wrapper's contract).
3. **Search synthesis** (existing Stage 2): Recall → Perplexity recency → research.py.
4. **Monid** (cross-provider, ~$0.03, requires funded wallet): only when the question
   spans 3+ platforms in one shot; governed by `directives/monid-usage-policy.md`.

## Output contract
Signals cite receipts — source URL + engagement numbers + retrieved date + a
VERIFIED/LIKELY/UNCONFIRMED label. A signal without a receipt is an idea, not a signal.

## Silent-skip table (all normal, none block)
| Condition | Behavior |
|---|---|
| No fresh brief + budget yellow/red | rung 3 only, note "live pull skipped (budget)" in one line |
| Actor returns `fallback: true` | continue to rung 3, no retry |
| `--no-live` | rungs 1-2 skipped entirely |
| Non-grounding domain (code, system work, diagnostics) | protocol does not fire |

## Where it's wired
`/create` Stage 2 step 0 (universal content conductor) · writers-room Layer 0 ·
router suggestion `content_production_live_grounding` (`routing_enforcer.py`) ·
session-start utilization line (`session_ledger_hook.py`) · weekly-closeout Step 3.
