# System Efficiency Benchmark

Generated: 2026-08-13 11:04

## Verdict

- Selective packaging is worth testing for the operator core, but broad packaging still needs proof.
- Do not package the whole Antigravity system in this pass.
- Treat plugin packaging as one optimization beside router weighting, metadata cleanup, skill description tightening, deterministic checks, and workflow consolidation.
- Archive nothing from this report alone; cold workflows need usage evidence before removal.

## Benchmark Summary

- Prompt cases: 10
- First-choice route hits: 8/10
- Reconstruction burden: 2/10 cases were not clean first-choice wins.
- Command menu average latency: 1917.8 ms
- Workflow router average latency: 183.8 ms
- Current quality score: 8.7/10
- Router/metadata cleanup projection: 9.3/10
- Operator-core plugin projection: 10.0/10

## Variant Comparison

| Variant | Quality | Speed Expectation | Reconstruction Burden | Recommendation |
|---|---:|---|---|---|
| Current state | 8.7/10 | Measured: 1917.8 ms menu, 183.8 ms router | 2/10 | Keep as baseline |
| Router/metadata cleanup only | 9.3/10 | Same or slightly faster | Lower where expected routes already exist | Do first |
| Plugin-packaged bundle | 10.0/10 | Not assumed faster | Helps only bundled operator-core routes | Test selectively |

## Route Results

| Case | Expected | Command Top | Cmd Rank | Router Top | Router Rank | Current | Cleanup | Plugin |
|---|---|---|---:|---|---:|---:|---:|---:|
| messy raw context | /autopilot | /autopilot | 1 | /autopilot | 1 | 10 | 10 | 10 |
| revenue sprint | /first-10k, /revenue-offer-agent, /client-acquire, /zero-to-client-sprint, /service-first-productization | /first-10k | 1 | /first-10k | 1 | 10 | 10 | 10 |
| extraction source | /extraction-governor-agent, /extract-forge, /convert-extraction, /compile-knowledge | /extraction-governor-agent | 1 | /extraction-governor-agent | 1 | 10 | 10 | 10 |
| creative brief | /creative-brief-gen, /design-brief, /creative-design-agent, /higgsfield-studio | /creative-brief-gen | 1 | /belief-creative-brief | 2 | 10 | 10 | 10 |
| client audit | /client-delivery-agent, /24-assets-client-audit, /client-interview, /draft-proposal | /create | miss | /24-assets-client-audit | 1 | 10 | 10 | 10 |
| system health | /health-check | /health-check | 1 | /health-check | 1 | 10 | 10 | 10 |
| plugin readiness | /plugin-readiness-audit | /system-audit | miss | /system-audit | miss | 0 | 3 | 10 |
| command bloat | /system-efficiency-benchmark, /bloat-optimizer, /context-audit, /system-hygiene | /bloat-optimizer | 1 | /growth-intelligence-scaling-system | miss | 10 | 10 | 10 |
| self evolution | /self-evolve, /routing-intelligence | /autopilot | 2 | /autopilot | 3 | 7 | 10 | 10 |
| knowledge retrieval | /knowledge-librarian, /knowledge-search, /compile-knowledge | /knowledge-librarian | 1 | /knowledge-librarian | 1 | 10 | 10 | 10 |

## Context Footprint

- Workflows: 2761
- Claude source commands: 3381
- Codex command skills: 2548
- Root skills: 400
- Repo-local plugins: 1
- `.agent/workflows` size: 4.7 MB
- `.agents/skills` size: 2.3 MB
- `skills` size: 147.3 MB
- `plugins` size: 92.2 KB

## Feedback Coverage

- Routing decisions logged: 0
- Feedback entries logged: 0
- Feedback coverage: 0.0%
- Performance log entries: 0
- Broad packaging should stay blocked until routing feedback is meaningfully higher.

## Bundle Readiness

| Bundle | Avg | Package Now | Improve First | Missing | Recommendation |
|---|---:|---:|---:|---:|---|
| `client` | 22.9 | 0 | 0 | 1 | keep as workflows |
| `content` | 24.0 | 0 | 0 | 1 | keep as workflows |
| `creative` | 27.4 | 0 | 0 | 1 | keep as workflows |
| `extraction` | 42.6 | 2 | 0 | 0 | keep as workflows |
| `operator-core` | 87.4 | 8 | 0 | 0 | package candidate |
| `revenue` | 22.6 | 0 | 0 | 0 | keep as workflows |
| `system` | 59.9 | 7 | 0 | 2 | keep as workflows |

## Hot/Cold Tier Recommendation

- Hot surfaced workflows: /24-assets-client-audit, /agentic-market-intelligence-briefing, /autopilot, /belief-creative-brief, /bloat-optimizer, /client-acquire, /client-ascension-framework, /client-interview, /compile-knowledge, /context-audit, /convert-extraction, /create, /creative-brief-gen, /design-brief, /draft-proposal, /extract, /extract-forge, /extraction-governor-agent, /first-10k, /fourth-wall-client-experience, /generate, /growth-intelligence-scaling-system, /health-check, /higgsfield-studio, /knowledge-librarian, /knowledge-search, /mission, /orchestrate, /revenue-offer-agent, /routing-intelligence, /self-evolve, /service-first-productization, /source-to-skill-system, /system-audit, /system-hygiene, /verify, /zero-to-client-sprint
- Warm bundle candidates still on disk: 22
- Cold workflow count: 2702
- Cold sample: /10x-diagnostic, /24-assets-agent-system-design, /24-assets-brand-market-builder, /24-assets-build-roadmap, /24-assets-business-design, /24-assets-council-sprint, /24-assets-culture-funding-builder, /24-assets-heatmap-diagnostic, /24-assets-ip-builder, /24-assets-product-system-builder, /24-assets-productized-service, /24-assets-zero-finder, /4c-architect, /aar, /accommodation-audit, /accuracy-without-clickbait, /ad-opinion-reps, /ad-script, /ad-spy, /ad-to-funnel, /adapt, /add-notebook, /addiction-copy-engine, /addiction-loop-architect, /addiction-loop-diagnostic

Recommendation: keep hot workflows surfaced, leave cold workflows on disk, and do not archive until routing logs or repeated benchmark misses prove they are dead weight.

## Next Optimization Order

1. Tighten router metadata for missed or low-rank benchmark cases.
2. Improve `knowledge-librarian` before packaging more bundles.
3. Log feedback on real routing outcomes so cold-tier decisions stop being guesswork.
4. Re-run this benchmark after metadata cleanup.
5. Package only a bundle that beats the cleanup-only projection.
