# Strategy Anchor: System Cohesion Silver Platter Audit

Created: 2026-05-11
Mission: system-cohesion-silver-platter-audit

## Root Strategy
The system should feel like one visible control plane, not a large shelf of isolated workflows. The right move is to make the existing roots compose better: `/autopilot` chooses, `/orchestrate` compares, `/mission` governs, `/system-audit` proves, `/silver-platter` maps the back-of-house data layer, `/expert-composition-governor` prevents expert soup, `/knowledge-librarian` prevents duplicate work, `/routing-intelligence` records feedback, and `/self-evolve` proposes supervised improvements.

## Why This Mission Exists
Farrice's current friction is not lack of assets. The workspace already has a large command, skill, workflow, agent, routing, and verification substrate. The lived failure is that the user still has to know which piece to pick up, and strong workflows can behave as separate islands unless a root route, evidence layer, and composition layer make them operate as one system.

## Strategic Constraints
- Do not create another standalone command or parallel OS as the first move.
- Keep global Codex rules read-only in this pass.
- Keep connector writes, external publishing, destructive cleanup, and real Codex subagents out of scope unless explicitly approved later.
- Treat written output as a Rendered Conversation Document plus a Local Markdown Source, not an HTML, `.docx`, Google Doc, Canva, or Notion export.
- Prefer verifiable route behavior, activation telemetry, and mission artifacts over abstract system diagrams.

## Library Decision
| Asset | Decision | Use in this mission |
|---|---|---|
| `docs/solutions/expert-composition-standard.md` | Adapt directly | Use one owner, bounded specialist slots, and a Composition Ledger for the unified tree. |
| `docs/solutions/routing-governor-self-compounding-workspace.md` | Adapt directly | Treat failed natural-language route tests as structured misroutes and future router-fix evidence. |
| `docs/solutions/mission-engineering-artifact-contract.md` | Apply directly | Keep this as a Mission OS engineering artifact chain instead of a new orchestration layer. |
| `docs/solutions/knowledge-librarian-solution-surfacing.md` | Apply directly | Make solution reuse explicit before new planning. |
| `docs/solutions/copy-gate-score-calibration.md` | Reference only | Useful for future copy-quality work, not central to this system-cohesion pass. |
| `docs/solutions/high-taste-writing-os.md` | Reference only | Relevant when output quality is the bottleneck, not this first control-plane audit. |
| `docs/solutions/notion-dns-local-first-sync.md` | Reference only | Explains local-first telemetry when Notion/network sync is unavailable. |

## Users / Beneficiaries
- Farrice as the operator, who should not need to remember every route, skill, or workflow.
- Future Codex runs, which need a clear root node and evidence path before changing the system.
- System maintainers, who need an issue ledger that separates broken routing from dormant activation.

## Success Standard
- The first pass names the unified operating tree and owner layer.
- The issue ledger distinguishes broken route behavior, dormant activation, blocked evolution, and low-risk hygiene.
- The audit preserves the current front-door architecture instead of adding route-selection burden.
- Validation evidence is attached to the artifact chain.
