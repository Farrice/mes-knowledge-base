# Phase E — Marketing & Content System

**Duration**: ~half-day. 3 substeps in parallel possible.

## Required inputs

From Phase B + C + D — entire upstream stack (briefs vocabulary feeds hook library).

## Steps

### E1 — Content Pillars

Run `/content-cluster` (skill: `skills/content-cluster/`):

> 5-7 content pillars with proportions + posting frequency. Pillars are DOMAINS the brand has authority to talk about, not topics. For Resonance: Spine, Story, Curation, Singles Reality, Music, Chicago, BTS.
>
> Each pillar has: name, definition, example posts (3-5), proportion of total content (e.g., 30% Spine, 20% Story...), default channel, default voice patterns it leans on.

Output: `03-marketing/01-content-pillars.md`.

### E2 — Hook Library

Run `/hook-bank` + `/hook-forge` (skills: `skills/hook-bank/`, `skills/hook-forge/`):

> 30+ hook patterns matched to pillar + ICP profile. Built around the brand's out-loud-asking questions (the things the ICP is already asking themselves).
>
> Format: Pattern name + structure + example + which pillar(s) + which profile(s) + which channel(s) it works on.

Output: `03-marketing/02-hook-library.md`.

### E3 — Operational marketing docs

Invoke `agents/master-copywriter/` (with main-thread save pattern):

Six docs to produce:
- **03-channel-architecture.md** — IG primary, email secondary, word-of-mouth tertiary; cadence map for pre/during/post each cycle
- **04-curation-mechanics.md** — invite flow, decline scripts, waitlist management, gatecrasher policies
- **05-crisis-comms.md** — playbooks for: Hunter slip-through, bad press, key partner cancels, attendance shortfall
- **06-why-gate-mechanics.md** — the application question (e.g., "Why do you want to be in the room?") + adjudication criteria + decline scripts
- **07-funnel.md** — top-of-funnel through hell-yes confirmation flow + hand-off points
- **08-offer-card.md** — what's available now, at what price, with what proof, for what ICP profile

Output: 6 files in `03-marketing/`.

### E4 — Ops docs (subset that flows from canonical inputs)

Direct port from `_source/`:

- **05-ops/03-drift-signals.md** — verbatim port of founder's named drift signals + readback ritual
- **05-ops/04-success-metrics.md** — first-cycle target + horizon metrics (per-quarter, per-year, per-5-year) + kill condition
- **05-ops/05-exit-interview-protocol.md** — question bank + capture method + permission rules

Output: 3 files in `05-ops/`.

## Output Schema

**Inputs**: 
- `00-foundation/*` — Foundation (ICP, voice, positioning, non-negotiables)
- `01-visual/*` — Visual (DESIGN.md, photography rules)
- `02-briefs/*` — Briefs (master template + per-asset briefs for reference)

**Outputs**:
- `03-marketing/01-content-pillars.md` — 5-7 content pillars (domain-based, not topic-based) with definition, example posts, proportion of content %, default channel, voice patterns. Proportions sum to 100%. Each pillar has explicit posting cadence.
- `03-marketing/02-hook-library.md` — 40+ hook patterns matched to pillar + ICP profile + channel. Format: pattern name, structure, example, pillar tags, profile tags, channel tags. Sourced from brand's out-loud-asking language.
- `03-marketing/03-channel-architecture.md` — Channel stack (primary/secondary/tertiary) with cadence map for pre-event/during/post-event cycles. Audience overlap map. Cross-promotion rules per channel pair.
- `03-marketing/04-curation-system.md` — How to evaluate content for publishing. Invite flow, decline scripts, waitlist mechanics, gatecrasher policies. Decision framework for "Is this on-brand?"
- `03-marketing/05-crisis-comms.md` — Pre-drafted response playbooks for 5-7 likely crisis scenarios (e.g., partner cancellation, bad press, attendance shortfall). Template responses + escalation paths.
- `03-marketing/06-why-gate.md` — Decision triage protocol. The screening question (e.g., "Why do you want to be in the room?"). Adjudication criteria with examples. Decline scripts. Appeal process if any.
- `03-marketing/07-funnel-architecture.md` — Awareness → Interest → Consideration → Purchase sequence with named hand-off points (not vague "convert"). Each funnel stage has entrance criteria, content strategy, exit criteria.
- `03-marketing/08-offer-stack.md` — Tiered offerings (free, low-cost, premium, VIP) with proof points, target ICP profile, pricing strategy, availability windows.
- `05-ops/03-drift-signals.md` — Founder's drift signals (verbatim port from `_source/`) + readback ritual encoded (how often + who + when to review).
- `05-ops/04-success-metrics.md` — First-cycle target (specific, measurable), horizon metrics (per-quarter, per-year, per-5-year), kill condition (when to pivot/halt).
- `05-ops/05-exit-interview-protocol.md` — Question bank (≥6 questions), capture method (audio/transcript/live-note), permission rules, analysis synthesis method.

**Purpose**: Lock the marketing and ops layer. Content pillars + hook library enable consistent voice across all channels. Channel architecture + funnel + offer stack provide operational structure. Crisis comms + why-gate + curation system provide decision frameworks. Phase F (AI Handoff) compresses this layer into the AI Brain Master (≤4K tokens).

**Quality Gate Checkpoint**:
- [ ] Content pillars: 5-7 with proportions summing to 100%, frequencies named, examples concrete
- [ ] Hook library: ≥40 hooks, each tagged with pillar + profile + channel
- [ ] Channel architecture: cadence map for full cycle (pre/during/post) — not just "post weekly"
- [ ] Crisis comms: ≥5 named scenarios with response templates
- [ ] Why-gate: actual application question + adjudication criteria + decline scripts
- [ ] Funnel: every step has named hand-off point (not vague "convert")
- [ ] Drift signals: verbatim from canonical + readback ritual encoded
- [ ] Success metrics: first-cycle target + horizons (Q, Y, 5Y) + kill condition
- [ ] Exit interview: question bank ≥6 questions + capture method + permission rules

If any unchecked, halt. Phase F (AI Handoff) needs this layer locked because the AI Brain Master compresses it.

---

## Quality gate (Phase E → F)

Before advancing to Phase F:
- [ ] Content pillars: 5-7 with proportions summing to 100%, frequencies named, examples concrete
- [ ] Hook library: ≥30 hooks, each tagged with pillar + profile + channel
- [ ] Channel architecture: cadence map for full cycle (pre/during/post) — not just "post weekly"
- [ ] Crisis comms: ≥3 named scenarios with response templates
- [ ] Why-gate: actual application question + adjudication criteria
- [ ] Funnel: every step has named hand-off (not vague "convert")
- [ ] Drift signals: verbatim from canonical + readback ritual encoded
- [ ] Success metrics: first-cycle + horizons + kill condition
- [ ] Exit interview: question bank ≥6 questions

If any unchecked, halt. Phase F (AI Handoff) needs this layer locked because the AI Brain Master compresses it.
