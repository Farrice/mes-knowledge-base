# Skill Audit — 2026-07-06

**Total skills**: 352
**Tier distribution**: A=53, B=175, C=2, REVIEW=95, UTILITY=27

## Methodology

Tiers assigned by `execution/skill_auditor.py` using:
- **Structure**: SKILL.md + genius.md + workflow count + references/
- **Trace signal**: v2_traces avg score over 60d (≥7.5 = strong)
- **Cross-references**: CLAUDE.md, COUNCIL.md, expert_router.py mentions

Tiers:
- **A** — full structure + (high traces OR cross-referenced) → world-class with real expert thinking
- **B** — partial structure + (some traces OR cross-referenced) → solid framework
- **C** — minimal structure AND no traces AND no cross-references → archive candidate
- **REVIEW** — heuristic conflict, low trace scores, or unused full-structure skills → human judgment

## CORE DRIFT (Production Core entries with zero traces in window)

25 of 35 core entries have no production traces in the last 60d:

- brand-operating-system
- creative-direction
- dai-media-consumer-posture
- david-placek-naming
- design-md
- diandra-escobar-linkedin-growth
- donald-miller-storybrand
- extract-mastery
- jason-fladlien-marketing
- jen-santulan-listing-content
- kallaway-social-commerce
- lara-acosta-linkedin-growth
- lara-acosta-linkedin-mastery
- luke-iha-avatar-machine
- luke-iha-copy-blocks
- luke-iha-vicious-hooks
- luke-iha-vsl-leads
- nate-b-jones-auto-improvement-loops
- nate-b-jones-context-engineering
- nicolas-cole-digital-products
- nicolas-cole-newsletter-flywheel
- rory-sutherland-marketing
- stefan-georgi-dopamine-copy
- strength-conditioning-os
- supercomputer

Action: if an entry stays here 2 consecutive months, demote it from PRODUCTION_CORE.md; promote any long-tail skill with 3+ traces.

## Tier A (53 skills)

These are the system's strongest skills. Prioritize for promotion, ground-truth benchmarking, and revenue tracking.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `andreessen-horowitz-new-media` | 4 | ✓ | 1 (avg 8.3) |  | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces) |
| `brock-johnson-shareworthy-content` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `dan-koe-ai-leverage` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `dan-koe-multipassionate-mastery` | 6 | ✓ | 1 (avg 8.3) | ✓ | full structure (6 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `dan-wang-literary-analysis` | 13 | ✓ | 1 (avg 8.3) | ✓ | full structure (13 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `daniel-priestley-oversubscribed` | 7 | ✓ | 1 (avg 8.3) | ✓ | full structure (7 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `david-placek-naming` | 6 | ✓ | 1 (avg 9.3) | ✓ | full structure (6 workflows + genius.md); trace avg 9.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `diandra-escobar-linkedin-growth` | 22 | ✓ | 1 (avg 9.0) | ✓ | full structure (22 workflows + genius.md); trace avg 9.0 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `erica-mallet-brand-magnetism` | 5 | ✓ | 1 (avg 8.3) | ✓ | full structure (5 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `fareed-zakaria-writing-mastery` | 5 | ✓ | 1 (avg 7.7) | ✓ | full structure (5 workflows + genius.md); trace avg 7.7 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `fresh-voice-system` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `ghostwriting-voice-engine` | 4 | ✓ | 1 (avg 8.3) |  | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces) |
| `grace-andrews-media-company` | 18 | ✓ | 1 (avg 8.3) | ✓ | full structure (18 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `jack-roberts-design-mastery` | 15 | ✓ | 1 (avg 8.7) |  | full structure (15 workflows + genius.md); trace avg 8.7 ≥ 7.5 (1 traces) |
| `jasmin-alic-linkedin-growth` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `jason-fladlien-marketing` | 30 | ✓ | 1 (avg 8.0) | ✓ | full structure (30 workflows + genius.md); trace avg 8.0 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `jeremy-haynes-mindset-systems` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `jeremy-miner-identity-persuasion` | 11 | ✓ | 1 (avg 8.3) | ✓ | full structure (11 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `joshua-smith-real-estate` | 4 | ✓ | 1 (avg 8.0) | ✓ | full structure (4 workflows + genius.md); trace avg 8.0 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `lara-acosta-linkedin-growth` | 6 | ✓ | 1 (avg 8.3) | ✓ | full structure (6 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `lara-acosta-linkedin-mastery` | 9 | ✓ | 1 (avg 8.3) | ✓ | full structure (9 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `lindsay-ai-consulting` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-proof-ladder` | 14 | ✓ | 1 (avg 8.3) | ✓ | full structure (14 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-proof-mechanisms` | 6 | ✓ | 1 (avg 8.3) | ✓ | full structure (6 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-unaware-ads` | 7 | ✓ | 1 (avg 8.3) | ✓ | full structure (7 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-vsl-leads` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `made-to-stick-messaging` | 4 | ✓ | 1 (avg 8.3) |  | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces) |
| `mark-kashef-agent-orchestration` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `mark-kashef-banana-squad` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `mark-kashef-claude-claw` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `mark-kashef-visual-design` | 5 | ✓ | 1 (avg 8.3) | ✓ | full structure (5 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nate-b-jones-auto-improvement-loops` | 8 | ✓ | 2 (avg 8.8) | ✓ | full structure (8 workflows + genius.md); trace avg 8.8 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nate-b-jones-context-engineering` | 6 | ✓ | 1 (avg 9.0) | ✓ | full structure (6 workflows + genius.md); trace avg 9.0 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nate-b-jones-intent-engineering` | 4 | ✓ | 1 (avg 8.7) | ✓ | full structure (4 workflows + genius.md); trace avg 8.7 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nate-b-jones-orchestration-intelligence` | 12 | ✓ | 1 (avg 8.3) | ✓ | full structure (12 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nate-b-jones-trust-architecture` | 5 | ✓ | 1 (avg 8.3) | ✓ | full structure (5 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nick-saraev-agentic-workflows` | 7 | ✓ | 1 (avg 8.0) | ✓ | full structure (7 workflows + genius.md); trace avg 8.0 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nicolas-cole-digital-products` | 3 | ✓ | 2 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `oscar-hoglund-sound-storytelling` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `paul-james-ai-automation` | 4 | ✓ | 1 (avg 9.0) | ✓ | full structure (4 workflows + genius.md); trace avg 9.0 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `pj-accetturo-ai-video` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `prediction-market-weather-trading` | 3 | ✓ | 1 (avg 9.3) |  | full structure (3 workflows + genius.md); trace avg 9.3 ≥ 7.5 (1 traces) |
| `rachel-woods-ai-operations` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `sabrina-ramonov-ai-monetization` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `sam-goddard-media-scaling` | 5 | ✓ | 1 (avg 8.3) | ✓ | full structure (5 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `seena-rez-tiktok-commerce` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `sherwin-wu-ai-engineering` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `soowei-consulting-leverage` | 4 | ✓ | 1 (avg 8.3) |  | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces) |
| `stockton-walbeck-lead-magnets` | 3 | ✓ | 1 (avg 8.5) | ✓ | full structure (3 workflows + genius.md); trace avg 8.5 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `taki-moore-lifestyle-business` | 6 | ✓ | 1 (avg 8.3) |  | full structure (6 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces) |
| `thrivecart-digital-products` | 4 | ✓ | 1 (avg 8.3) |  | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces) |
| `tobias-allen-marketing-mastery` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `wright-thompson-mastery` | 13 | ✓ | 1 (avg 8.4) | ✓ | full structure (13 workflows + genius.md); trace avg 8.4 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |

## Tier B (175 skills)

Solid skills that are working. Candidates for B→A promotion via genius.md enrichment or workflow expansion.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `adam-enfroy-affiliate-marketing` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ai-chris-lee-zero-testimonial-sales` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alen-sultanic-copywriting` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-content-science` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-copper-creative-strategy` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-hormozi-business` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-m-smith-natural-strategy` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-myatt-creative-engine` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-suzuki-digital-product-revenue-os` | 17 | ✓ | - | ✓ | full structure (17 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ali-abdaal-action-bias` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `andrew-dun-vibe-consulting` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `andrew-lane-design-systems` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `andrew-stanton-audience-engineering` | 21 | ✓ | - | ✓ | full structure (21 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `andrew-wilkinson-ai-entrepreneurship` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `andy-lo-premium-websites` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `april-dunford-positioning` | 16 | ✓ | - | ✓ | full structure (16 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ash-maurya-founder-systems` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ash-maurya-lean-metrics` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `attention-hijack-hooks` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `authority-hacker-ai-social-media` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `bond-halbert-copywriting` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `boris-claude-code` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `brand-operating-system` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `business-intelligence-audit` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `caleb-ralston-personal-brand` | 11 | ✓ | - | ✓ | full structure (11 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `cardinal-mason-ai-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `chris-cimorelli-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `chris-do-design-business` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `cinematic-documentary` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `coaching-business-os` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `context-profile-architect` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `creative-campaign-strategy` | 17 | ✓ | - | ✓ | full structure (17 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dai-media-consumer-posture` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-bolton-coaching-offers` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-martell-business-scaling` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-pink-writing-structure` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-priestley-24-assets-os` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-thrasher-affiliate` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `darrel-wilson-ai-affiliate` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `darrel-wilson-ai-monetization` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-bayer-elite-communication` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-deutsch-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-mcraney-belief-change` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-perell-writing` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dom-iacovone-multi-company-operator` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `donald-miller-business-growth` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `donald-miller-cognitive-load` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `donald-miller-culture-turnaround` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `donald-miller-messaging-evolution` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `donald-miller-storybrand` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dr-kriukow-humanization` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `enrico-incarnati-instagram-realestate` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `eric-roth-screenwriting-mastery` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `eric-roth-writing-mastery` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ethan-smith-aeo` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `evan-spiegel-distribution-architecture` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `extract-mastery` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `fantastic-posters` | 5 |  | - | ✓ | 5 workflows but no genius.md; cross-referenced (no trace data) |
| `futurepedia-prompt-engineering` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `growth-ecosystems` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `harry-dry-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `how-i-write-os` | 0 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `james-i-bond-brain-glue` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jim-oshaughnessy-philosopher-financier` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joanna-wiebe-persuasion-mastery` | 11 | ✓ | - | ✓ | full structure (11 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joanna-wiebe-writing-careers` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `john-whiting-propaganda-machine` | 19 | ✓ | - | ✓ | full structure (19 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jonathan-courtney-marketing` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `jonathan-franzen-storytelling` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joscha-bach-consciousness` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `josh-kaufman-business-fundamentals` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `josh-sanders-linkedin-growth` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jun-yuh-creator-vision` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jun-yuh-personal-brand` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-addictive-storytelling` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-ai-content-engine` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-audience-obsession` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-content-psychology` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-content-system` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-illusion-of-novelty` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-social-commerce` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-word-mastery` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kittl-graphic-design` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `knowledge-architecture-studio` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kobi-brown-educational-virality` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lance-yichao-context-engineering` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lara-acosta-content-system` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `linkedin-2026-format-arbitrage` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `logan-kilpatrick-ai-studio` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lucas-alpay-storytelling` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-alexander-ai-business` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-avatar-machine` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-client-mastery` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-copy-blocks` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-creative-strategy` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-cross-domain` | 4 |  | - | ✓ | 4 workflows but no genius.md; cross-referenced (no trace data) |
| `luke-iha-insight-vectors` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-million-dollar-mechanisms` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-vicious-hooks` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lulu-cheng-meservey-communications` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `manus-ai-consulting` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `marc-andreessen-ai-thesis` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `maria-wendt-digital-products` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-forsyth-rhetoric` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-ai-councils` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-manson-values-psychology` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `matt-mcgarry-newsletters` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `michael-bernoff-identity-engineering` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `michael-connelly-vivid-writing` | 16 | ✓ | - | ✓ | full structure (16 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `michael-israetel-hypertrophy` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `michael-margolis-user-research` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mike-foutia-marketing-tools` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mitch-albom-writing-mastery` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `monk-ai-offer-architecture` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-b-jones-agent-deployment-strategy` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `nate-b-jones-ai-taste-mastery` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-herk-client-acquisition` | 1 | ✓ | 1 (avg 8.3) | ✓ | has genius.md but <3 workflows; 1 traces, avg 8.3 |
| `nathan-gotch-ai-seo` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `new-media-kingmaker` | 3 |  | - | ✓ | 3 workflows but no genius.md; cross-referenced (no trace data) |
| `nick-saraev-bottleneck-thinking` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-client-acquisition` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-edan-writing-mechanics` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-newsletter-flywheel` | 17 | ✓ | - | ✓ | full structure (17 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-niche-positioning` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-nonfiction-value-architecture` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-sales-education-messaging` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-sentence-craft` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `noah-hawley-storytelling-mastery` | 20 | ✓ | - | ✓ | full structure (20 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ocean-vuong-perceptual-writing` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `omar-eddaoudi` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `omar-eddaoudi-premium-ads` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `omar-eddaoudi-scaling-ops` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `omar-eltakrori` | 17 | ✓ | - | ✓ | full structure (17 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `pat-flynn-passive-income` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `paul-harding-lyric-prose` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `persuasion-story-code` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `phil-m-jones-conversational-influence` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `product-design-build` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `robert-mack-comedy-writing` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `rory-sutherland-marketing` | 20 | ✓ | - | ✓ | full structure (20 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ross-mckay-premium-at-scale` | 1 | ✓ | 1 (avg 8.3) | ✓ | has genius.md but <3 workflows; 1 traces, avg 8.3 |
| `ross-minchev-digital-products` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sabri-suby-ai-advertising` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sam-parr-copywriting` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sam-parr-copywriting-mechanics` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sam-parr-taste-acquisition` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `samuel-thompson-product-launch` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sean-kochel-ai-business` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sean-kochel-design-first-build` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `self-evolving-systems` | 1 | ✓ | 3 (avg 8.97) | ✓ | has genius.md but <3 workflows; 3 traces, avg 8.97 |
| `semantic-document-library-os` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `seth-godin-brand` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `seth-godin-ideavirus` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `seth-godin-philosophy` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `shaan-puri-storytelling` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `shan-hanif-audience-monetization` | 2 | ✓ | 1 (avg 8.3) | ✓ | has genius.md but <3 workflows; 1 traces, avg 8.3 |
| `stefan-georgi-dopamine-copy` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `steven-kotler-flow-performance` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `steven-pressfield-narrative-mastery` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `steven-young-consciousness` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `story-compass` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `supercomputer` | 0 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `tao-prompts-ai-video` | 2 | ✓ | 1 (avg 8.3) | ✓ | has genius.md but <3 workflows; 1 traces, avg 8.3 |
| `tim-danilov-niche-bending` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tobi-lutke-business-leadership` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-noske-content-creation` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-noske-personal-brand` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-segura-comedy-storytelling` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tommy-clark-linkedin-growth` | 2 | ✓ | 1 (avg 8.3) | ✓ | has genius.md but <3 workflows; 1 traces, avg 8.3 |
| `tyler-denk-audience-monetization` | 2 | ✓ | 1 (avg 8.3) | ✓ | has genius.md but <3 workflows; 1 traces, avg 8.3 |
| `velocity-scaling` | 18 | ✓ | - | ✓ | full structure (18 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `vince-nijhof-dtc-operator-system` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ward-farnsworth-rhetorical-mastery` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `writing-depth-layer` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `youtube-video-context-analysis` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |

## Tier REVIEW (95 skills)

Heuristics conflict — these need human eyes before tier finalization.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `ai-carousel-content-engine` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `alan-aragon-nutrition` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `andy-galpin-training-intelligence` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `benjamin-hardy-identity` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `bill-browder-high-stakes-narrative` | 13 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `bitbranding-fashion-shopify` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `brad-bonanno-explainer-architecture` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `brandon-jacoby-taste-mastery` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `brendan-kane-viral-strategy` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `chase-hughes-context-engineering` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `chase-hughes-conversational-influence` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `cheri-tree-bank-buyology` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `chief-of-staff-os` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `cognitive-engagement-optimizer` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `corey-mcclain-persona-engineering` | 20 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `craig-clemens-copywriting` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `dakota-content-design` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `damon-cart-nlp` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `dara-denney-meta-ads` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `deliberate` | 0 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `deya-business-systems` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `dr-k-consciousness` | 11 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `eugene-teo-training` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `fraser-cottrell-paid-ads` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `gabe-novotny-fitness-content-business` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `gary-vaynerchuk-attention` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `gpt-image-2-director` | 0 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `greg-hickman-service-scaling` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `greg-hoffman-brand-mastery` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `henrik-werdelin-portfolio-entrepreneurship` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `henry-shukman-contemplative-writing` | 13 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jay-hiette-coaching-positioning` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jen-santulan-listing-content` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jenny-hoyos-shorts` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jessica-jensen-platform-intelligence` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jiang-xueqin-cognitive-autonomy` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jonah-berger-contagious` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `justin-welsh-solopreneur` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kallaway-content-operating-system` | 1 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `kieran-flanagan-audience-intelligence` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kieran-flanagan-content-engine` | 8 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kieran-flanagan-content-ops` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kj-rainey-copywriting` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kunal-shah-consumer-psychology` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `lamott-allen-really-real-writing` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `lamott-craft` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `liam-mley-ai-brain-builder` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `liam-ottley-linkedin-lead-magnet` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `luisa-zhou-coaching` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `marisa-murgatroyd-course-design` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `mark-kashef-silver-platter-agentic-os` | 0 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `marketing-studio-director` | 0 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `matthew-lakajev-linkedin` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `matthew-volkwyn-copywriting` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `meg-heckman-buyer-trigger-os` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `mike-sherrard-realtor-branding` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `nba-betting-edge` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `new-media-ghostwriting` | 1 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `nir-eyal-habit-design` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-brand-archetypes` | 0 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `oren-content-team-architecture` | 15 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-luxury-psychology` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-one-person-ai-marketer` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-operational-systems` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-repositioning` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-taste-development` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `packy-mccormick-writing` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `patrick-dang-online-business` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `patrick-debois-cdlc` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-ai-event-analysis` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-making` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-risk-management` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prosperity-coach-system` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `rafa-conde-fourth-wall-experience-os` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `rafa-conde-memorable-product-design` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `reid-hoffman-ai-strategy` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `robert-greene-power-mastery` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `russell-brunson-funnels` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sarah-levinger-ad-psychology` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `satori-graphics` | 14 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sean-dollwet-kdp-publishing` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sean-mabry-voice-mastery` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `sean-macintyre-persuasion-philosophy` | 17 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sharran-srivatsaa-scaling` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `simon-intellectual-library-os` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sky-tan-format-engine` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `strength-conditioning-os` | 2 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `sunny-lenarduzzi-youtube` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `susan-orlean-narrative-nonfiction` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sweat-equity-speedrun-social-os` | 9 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `taylor-welch-wealthy-consultant` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `tess-barclay-social-content` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `wordsatscale-seo-ranking` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `yann-martel-storytelling-mastery` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `yuri-elkaim-health-coaching-business` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |

## Tier C (2 skills)

Archive candidates. Low evidence of value. **Do not delete — move to `_archive/skills/` for provenance.** Review individually before archiving (some may be load-bearing user domain skills).

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `higgsfield-creative-studio` | 0 |  | - |  | minimal structure (SKILL.md only) AND no traces AND no cross-references |
| `verticalize` | 0 |  | - |  | minimal structure (SKILL.md only) AND no traces AND no cross-references |

## Tier UTILITY (27 skills)

Anthropic-provided or system utility skills. Provide infrastructure (file conversion, design scaffolding, code utilities) rather than expert thinking. **Do not archive** — these are kept for usage. Update `UTILITY_SKILLS` in `skill_auditor.py` to add new entries.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `algorithmic-art` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `asset_generator` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `brand-guidelines` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `canvas-design` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `consumer-posture-research` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `creative-assembly` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `creative-direction` | 0 | ✓ | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `design-md` | 7 | ✓ | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `doc-coauthoring` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `docx` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `frontend-design` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `gemini-api-dev` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `internal-comms` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `market_intelligence` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `mcp-builder` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `pdf` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `pptx` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `react-components` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `remotion-video-creation` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `skill-creator` | 1 | ✓ | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `slack-gif-creator` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `stitch-loop` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `swarm-commander` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `theme-factory` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `web-artifacts-builder` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `webapp-testing` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `xlsx` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |

## Next steps

1. **Review the REVIEW bucket manually** — these are the highest-information items.
2. **Spot-check 3-5 A-tier classifications** — confirm the heuristics aren't generous.
3. **Spot-check 3-5 C-tier classifications** — confirm nothing valuable is being archived.
4. Run `python3 execution/skill_auditor.py archive --tier C --apply` to move C-tier (with confirmation prompt).
5. Run `python3 execution/skill_auditor.py update-index --apply` to annotate SKILL_INDEX.md.

Machine-readable records: `evolution_store/skill_audit_2026-07-06.jsonl`
