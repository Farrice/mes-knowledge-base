# System Efficiency Benchmark

Generated: 2026-05-23 21:09

## Verdict

- Current routing is functional; the next bottleneck is feedback coverage, not packaging volume.
- Do not package the whole Antigravity system in this pass.
- Treat plugin packaging as one optimization beside router weighting, metadata cleanup, skill description tightening, deterministic checks, and workflow consolidation.
- Archive nothing from this report alone; cold workflows need usage evidence before removal.

## Benchmark Summary

- Prompt cases: 10
- First-choice route hits: 10/10
- Reconstruction burden: 0/10 cases were not clean first-choice wins.
- Command menu average latency: 1152.4 ms
- Workflow router average latency: 308.6 ms
- Current quality score: 10.0/10
- Router/metadata cleanup projection: 10.0/10
- Operator-core plugin projection: 10.0/10

## Variant Comparison

| Variant | Quality | Speed Expectation | Reconstruction Burden | Recommendation |
|---|---:|---|---|---|
| Current state | 10.0/10 | Measured: 1152.4 ms menu, 308.6 ms router | 0/10 | Keep as baseline |
| Router/metadata cleanup only | 10.0/10 | Same or slightly faster | Lower where expected routes already exist | Already achieved |
| Plugin-packaged bundle | 10.0/10 | Not assumed faster | Helps only bundled operator-core routes | Hold; fresh-session test only |

## Route Results

| Case | Expected | Command Top | Cmd Rank | Router Top | Router Rank | Current | Cleanup | Plugin |
|---|---|---|---:|---|---:|---:|---:|---:|
| messy raw context | /autopilot | /autopilot | 1 | /autopilot | 1 | 10 | 10 | 10 |
| revenue sprint | /first-10k, /revenue-offer-agent, /client-acquire, /zero-to-client-sprint, /service-first-productization | /revenue-offer-agent | 1 | /first-10k | 1 | 10 | 10 | 10 |
| extraction source | /extraction-governor-agent, /extract-forge, /convert-extraction, /compile-knowledge | /extraction-governor-agent | 1 | /source-to-skill-system | 2 | 10 | 10 | 10 |
| creative brief | /creative-brief-gen, /design-brief, /creative-design-agent, /higgsfield-studio | /creative-brief-gen | 1 | /creative-brief-gen | 1 | 10 | 10 | 10 |
| client audit | /client-delivery-agent, /24-assets-client-audit, /client-interview, /draft-proposal | /client-delivery-agent | 1 | /client-delivery-agent | 1 | 10 | 10 | 10 |
| system health | /health-check | /health-check | 1 | /health-check | 1 | 10 | 10 | 10 |
| plugin readiness | /plugin-readiness-audit | /plugin-readiness-audit | 1 | /plugin-readiness-audit | 1 | 10 | 10 | 10 |
| command bloat | /system-efficiency-benchmark, /bloat-optimizer, /context-audit, /system-hygiene | /system-efficiency-benchmark | 1 | /system-efficiency-benchmark | 1 | 10 | 10 | 10 |
| self evolution | /self-evolve, /routing-intelligence | /self-evolve | 1 | /self-evolve | 1 | 10 | 10 | 10 |
| knowledge retrieval | /knowledge-librarian, /knowledge-search, /compile-knowledge | /knowledge-librarian | 1 | /knowledge-librarian | 1 | 10 | 10 | 10 |

## Context Footprint

- Workflows: 1053
- Claude source commands: 819
- Codex command skills: 24
- Root skills: 251
- Repo-local plugins: 1
- `.agent/workflows` size: 2.1 MB
- `.agents/skills` size: 818.7 KB
- `skills` size: 155.1 MB
- `plugins` size: 4.2 KB

## Feedback Coverage

- Routing decisions logged: 33
- Feedback entries logged: 24
- Feedback coverage: 72.7%
- Performance log entries: 20
- Broad packaging should stay blocked until routing feedback is meaningfully higher.

## Bundle Readiness

| Bundle | Avg | Package Now | Improve First | Missing | Recommendation |
|---|---:|---:|---:|---:|---|
| `client` | 23.9 | 0 | 0 | 0 | keep as workflows |
| `content` | 22.9 | 0 | 0 | 0 | keep as workflows |
| `creative` | 27.9 | 0 | 0 | 0 | keep as workflows |
| `extraction` | 39.1 | 2 | 0 | 0 | keep as workflows |
| `operator-core` | 88.1 | 8 | 0 | 0 | package candidate |
| `revenue` | 24.9 | 0 | 0 | 0 | keep as workflows |
| `system` | 62.5 | 7 | 0 | 0 | keep as workflows |

## Hot/Cold Tier Recommendation

- Hot surfaced workflows: /24-assets-client-audit, /ai-employee-os, /ash-dan-martell-handshake, /ash-risk-map, /autopilot, /bloat-optimizer, /client-acquire, /client-delivery-agent, /client-interview, /command-menu, /compile-knowledge, /context-audit, /convert-extraction, /creative-brief-gen, /creative-design-agent, /design-brief, /draft-proposal, /end-session, /extract-forge, /extraction-governor-agent, /first-10k, /fladlien-self-select, /fourth-wall-client-experience, /health-check, /higgsfield-studio, /knowledge-librarian, /knowledge-search, /mission, /nijhof-paid-scale-audit, /orchestrate, /plugin-readiness-audit, /pmj-magic-words, /repeatability-spine, /research-intelligence-agent, /revenue-offer-agent, /routing-intelligence, /satori-brand-system-check, /self-evolve, /service-first-productization, /source-to-skill-system
- Warm bundle candidates still on disk: 25
- Cold workflow count: 984
- Cold sample: /10x-diagnostic, /24-assets-agent-system-design, /24-assets-brand-market-builder, /24-assets-build-roadmap, /24-assets-business-design, /24-assets-council-sprint, /24-assets-culture-funding-builder, /24-assets-heatmap-diagnostic, /24-assets-ip-builder, /24-assets-product-system-builder, /24-assets-productized-service, /24-assets-zero-finder, /4c-architect, /aar, /accommodation-audit, /ad-script, /ad-to-funnel, /adapt, /add-notebook, /addiction-copy-engine, /addiction-loop-architect, /addiction-loop-diagnostic, /addictive-perception-content, /adversarial-refine, /adversarial-review

Recommendation: keep hot workflows surfaced, leave cold workflows on disk, and do not archive until routing logs or repeated benchmark misses prove they are dead weight.

## Next Optimization Order

1. Log feedback on real routing outcomes so cold-tier decisions stop being guesswork.
2. Fresh-session test `antigravity-operator-core` before expanding packaging.
3. Re-run this benchmark after at least 10 new routing decisions with feedback.
4. Keep revenue, creative, content, and client bundles as workflows until usage evidence changes.
5. Use this benchmark as the regression gate before future router or plugin changes.
