# Pod Architecture Blueprint — Reference

The 7-pod creative production system that runs Oak Brand Group's $20M/month brand. Adaptable from 1-pod startup → 7-pod scale.

## Core Principle: Pod = Unit of Leverage

A "pod" is a self-contained creative production unit that can ideate, produce, brief, and ship ad concepts without dependencies on other pods. Scaling creative output ≠ hiring more strategists. Scaling = adding pods.

Why it works:
- Each pod has clear ownership (KPIs land on pod, not individual)
- Pods compete + compound learning (winners share, losers iterate)
- Strategists don't get bottlenecked by creator comms (coordinator handles)
- Editors don't waste time hunting B-roll (database serves)

## Standard Pod Composition

A full pod = 4 roles:

### 1. Creative Strategist (1 per pod)
- **Job**: Ideation. Net-new concepts. Net-new angles. Translate data bank insights into briefs.
- **Doesn't do**: Talk to creators. Edit videos. Manage content production logistics.
- **KPI**: 60-80 concepts/month (statics) OR 15-25 concepts/month (VSSLs)
- **Hire signal**: Has shipped winning ads inside another brand. Not "creative" generally — specifically performance creative with attribution data.

### 2. Video Editors (2 per pod, ideal)
- **Job**: Bridge ideation → execution. Make the concept come alive as the strategist envisioned.
- **Doesn't do**: Originate concepts. Talk to creators about concepts (only logistics).
- **KPI**: Cycle time per concept (days from brief to ship-ready), concept fidelity score (does it match strategist intent)
- **Hire signal**: Strong portfolio + can self-source B-roll. Tier-2 hire = AI-augmented (Runway, Higgsfield, Arc database fluent).

### 3. Creative Coordinator (1 per pod, can flex across pods)
- **Job**: Creator communication. Brief delivery to creators. Content collection. UGC database tagging.
- **Doesn't do**: Ideate. Edit. Make creative judgments.
- **KPI**: Creator response rate, brief-to-content cycle time, % of UGC properly tagged for database
- **Hire signal**: Operational ops experience. Comfortable with high-volume comms. Detail-oriented on tagging discipline.

### 4. Pod Lead / Senior Strategist (1 per pod, often = the strategist at small scale)
- **Job**: Quality gate before ship. Final feedback loop. Performance review.
- **Doesn't do**: Day-to-day production.
- **KPI**: Pod's blended ROAS, ship rate, kill rate (95% of concepts should die before launch)

## Stage-by-Stage Pod Architecture

### Stage 0 — The Founder Pod ($0-500K revenue)
- **Composition**: 1 person doing everything (founder is strategist + editor + creator + coordinator)
- **KPI**: Survive. Find first messaging-market-fit signal.
- **Tools**: AI for everything possible (Claude for copy, Higgsfield/Runway for video, free B-roll libraries)
- **Don't hire yet**: Until you've shipped at least 3 winning concepts you understand.

### Stage 1 — The Solo Strategist + Freelance Editor Pod ($500K-2M)
- **Composition**: 1 strategist (founder OR first hire) + 1-2 freelance editors + occasional creator commission
- **KPI**: 20 concepts/month, 2-3 winners
- **Tools**: Same as Stage 0 + first AI projects (Claude per workflow)
- **Don't hire yet**: A creative coordinator. The strategist can still handle creator comms at this volume.

### Stage 2 — The 1-Pod ($2-5M)
- **Composition**: 1 strategist + 1-2 dedicated editors + creative coordinator (can be part-time / shared with ops)
- **KPI**: 40-60 concepts/month, 4-6 winners
- **Tools**: B-roll database starts. Data bank starts. AI projects per workflow live.
- **Hire signal for Stage 3**: Pod is hitting KPI ceiling, winners are clustering — time to add diversity via second pod.

### Stage 3 — The 3-Pod ($5-15M)
- **Composition**: 3 full pods. Each runs a different angle hypothesis (e.g., pod 1 = top-of-funnel VSSL, pod 2 = static testing, pod 3 = creator-led mid-funnel).
- **KPI**: 150-200 concepts/month aggregate, 15-20 winners, blended ROAS holds at scale
- **Tools**: Notion-based command center. Cross-pod weekly review. Shared data bank refreshed monthly.
- **Hire signal for Stage 4**: Pods are hitting their own ceilings, brand is at $10M+ omnichannel-ready.

### Stage 4 — The 5-7 Pod ($15M+)
- **Composition**: 5-7 full pods. Specialized: top-of-funnel VSSL pod, middle-of-funnel UGC pod, retention/CRM pod, AppLovin pod, TikTok pod, etc.
- **KPI**: 300-500 concepts/month aggregate, blended ROAS optimization, channel diversification
- **Tools**: Full company command center, AI insights layer, automated B-roll database, dedicated retention CRM pod
- **Hire signal**: Different brands → different pod compositions. Some brands need 7 pods, some need 5.

## Cross-Pod Coordination

### Weekly Pod Review (mandatory)
- Each pod presents: concepts shipped, concepts killed, top performer, biggest learning
- Cross-pollinate: what worked in pod 3 might inform pod 1's next batch
- Single shared dashboard (Notion or custom) showing all pod outputs

### Monthly Data Bank Refresh
- Coordinator pulls new reviews / tickets / DMs
- Strategists from all pods get fresh angle seeds
- Tag any new emotion themes that emerged

### Quarterly Pod Architecture Review
- Are pods specialized correctly?
- Is any pod underperforming structurally vs. people-wise?
- Should we add / merge / split pods?

## Anti-Patterns

- ❌ **Strategist-talks-to-creator role mixing** — kills throughput by 50%+. Specialize roles.
- ❌ **Editor originates concepts** — bypasses data bank, produces variation-not-innovation
- ❌ **Pod without a coordinator** — strategist drowns in logistics, KPI misses
- ❌ **Adding strategists without adding editors** — concept ideation outpaces execution, briefs pile up unused
- ❌ **Single pod trying to cover all funnel stages** — top-of-funnel VSSL and bottom-of-funnel UGC require different production cadence
- ❌ **No kill rate discipline** — pod that ships 100% of concepts is over-shipping mediocrity
- ❌ **Hiring "creative" generally** — specify performance creative with attribution data

## Compensation Norms (Vince-implied)

- **Strategist**: salary tied to pod blended ROAS + bonus on individual winners
- **Editor**: salary + cycle-time bonuses + winner attribution bonuses
- **Coordinator**: salary + creator response rate bonuses
- **AI Certificate Bonus**: any role completing Anthropic / OpenAI / etc. foundation certificate gets pay raise (Vince standard)

## When to Break Pod Structure

- **Patent moat product launch**: dedicated single-pod for 6 months around launch
- **New brand within holdco**: starts at Stage 0, NOT inheriting parent brand's full pod system
- **Crisis recovery (out-of-stock, supply chain)**: pause new pod additions, maintain existing
- **Channel expansion (e.g., into AppLovin)**: dedicated pod for new channel, NOT a tab on existing pod
