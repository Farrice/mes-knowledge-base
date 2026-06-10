# Skill Audit — 2026-06-09

**Total skills**: 246
**Tier distribution**: A=23, B=161, C=1, REVIEW=34, UTILITY=27

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

23 of 33 core entries have no production traces in the last 60d:

- brand-operating-system
- creative-direction
- dai-media-consumer-posture
- david-placek-naming
- design-md
- diandra-escobar-linkedin-growth
- donald-miller-storybrand
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
- supercomputer

Action: if an entry stays here 2 consecutive months, demote it from PRODUCTION_CORE.md; promote any long-tail skill with 3+ traces.

## Tier A (23 skills)

These are the system's strongest skills. Prioritize for promotion, ground-truth benchmarking, and revenue tracking.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `andrew-dun-vibe-consulting` | 15 | ✓ | 1 (avg 8.7) | ✓ | full structure (15 workflows + genius.md); trace avg 8.7 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `brand-operating-system` | 7 | ✓ | 6 (avg 7.78) | ✓ | full structure (7 workflows + genius.md); trace avg 7.78 ≥ 7.5 (6 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `corey-mcclain-persona-engineering` | 20 | ✓ | 1 (avg 8.7) |  | full structure (20 workflows + genius.md); trace avg 8.7 ≥ 7.5 (1 traces) |
| `creative-campaign-strategy` | 17 | ✓ | 1 (avg 8.3) | ✓ | full structure (17 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `dai-media-consumer-posture` | 3 | ✓ | 2 (avg 8.65) | ✓ | full structure (3 workflows + genius.md); trace avg 8.65 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `david-placek-naming` | 6 | ✓ | 1 (avg 9.3) | ✓ | full structure (6 workflows + genius.md); trace avg 9.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `diandra-escobar-linkedin-growth` | 22 | ✓ | 3 (avg 7.98) | ✓ | full structure (22 workflows + genius.md); trace avg 7.98 ≥ 7.5 (3 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `donald-miller-storybrand` | 8 | ✓ | 1 (avg 8.3) | ✓ | full structure (8 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `erica-mallet-brand-magnetism` | 5 | ✓ | 1 (avg 8.3) | ✓ | full structure (5 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `jack-roberts-design-mastery` | 15 | ✓ | 1 (avg 8.7) |  | full structure (15 workflows + genius.md); trace avg 8.7 ≥ 7.5 (1 traces) |
| `kallaway-social-commerce` | 5 | ✓ | 1 (avg 8.7) | ✓ | full structure (5 workflows + genius.md); trace avg 8.7 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `lara-acosta-linkedin-growth` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `lara-acosta-linkedin-mastery` | 9 | ✓ | 2 (avg 8.2) | ✓ | full structure (9 workflows + genius.md); trace avg 8.2 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-copy-blocks` | 12 | ✓ | 6 (avg 7.61) | ✓ | full structure (12 workflows + genius.md); trace avg 7.61 ≥ 7.5 (6 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-vicious-hooks` | 14 | ✓ | 1 (avg 8.67) | ✓ | full structure (14 workflows + genius.md); trace avg 8.67 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-vsl-leads` | 4 | ✓ | 3 (avg 7.72) | ✓ | full structure (4 workflows + genius.md); trace avg 7.72 ≥ 7.5 (3 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nate-b-jones-auto-improvement-loops` | 8 | ✓ | 2 (avg 8.8) | ✓ | full structure (8 workflows + genius.md); trace avg 8.8 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nate-b-jones-context-engineering` | 6 | ✓ | 3 (avg 7.81) | ✓ | full structure (6 workflows + genius.md); trace avg 7.81 ≥ 7.5 (3 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nicolas-cole-digital-products` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `nicolas-cole-newsletter-flywheel` | 17 | ✓ | 2 (avg 9.35) | ✓ | full structure (17 workflows + genius.md); trace avg 9.35 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `prediction-market-weather-trading` | 3 | ✓ | 1 (avg 9.3) |  | full structure (3 workflows + genius.md); trace avg 9.3 ≥ 7.5 (1 traces) |
| `rory-sutherland-marketing` | 17 | ✓ | 2 (avg 8.7) | ✓ | full structure (17 workflows + genius.md); trace avg 8.7 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `vince-nijhof-dtc-operator-system` | 14 | ✓ | 1 (avg 7.5) | ✓ | full structure (14 workflows + genius.md); trace avg 7.5 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |

## Tier B (161 skills)

Solid skills that are working. Candidates for B→A promotion via genius.md enrichment or workflow expansion.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `adam-enfroy-affiliate-marketing` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ai-chris-lee-zero-testimonial-sales` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alen-sultanic-copywriting` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-content-science` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-copper-creative-strategy` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-m-smith-natural-strategy` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-myatt-creative-engine` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ali-abdaal-action-bias` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `andrew-wilkinson-ai-entrepreneurship` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `andy-lo-premium-websites` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `april-dunford-positioning` | 16 | ✓ | - | ✓ | full structure (16 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `authority-hacker-ai-social-media` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `bond-halbert-copywriting` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `boris-claude-code` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `brock-johnson-shareworthy-content` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `business-intelligence-audit` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `caleb-ralston-personal-brand` | 11 | ✓ | - | ✓ | full structure (11 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `cardinal-mason-ai-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `chase-hughes-context-engineering` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `chase-hughes-conversational-influence` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `chris-cimorelli-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `cinematic-documentary` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-koe-ai-leverage` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-koe-multipassionate-mastery` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-martell-business-scaling` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-wang-literary-analysis` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `daniel-priestley-oversubscribed` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `darrel-wilson-ai-affiliate` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `darrel-wilson-ai-monetization` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-bayer-elite-communication` | 3 | ✓ | 3 (avg 7.25) | ✓ | 3 traces, avg 7.25 |
| `david-deutsch-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-mcraney-belief-change` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `deliberate` | 0 | ✓ | 1 (avg 7.08) | ✓ | has genius.md but <3 workflows; 1 traces, avg 7.08 |
| `donald-miller-business-growth` | 6 | ✓ | 1 (avg 7.25) | ✓ | 1 traces, avg 7.25 |
| `donald-miller-cognitive-load` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `donald-miller-culture-turnaround` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `donald-miller-messaging-evolution` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dr-kriukow-humanization` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `enrico-incarnati-instagram-realestate` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `eric-roth-screenwriting-mastery` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `eric-roth-writing-mastery` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ethan-smith-aeo` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `evan-spiegel-distribution-architecture` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `fantastic-posters` | 5 |  | - | ✓ | 5 workflows but no genius.md; cross-referenced (no trace data) |
| `fareed-zakaria-writing-mastery` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `fresh-voice-system` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `futurepedia-prompt-engineering` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `grace-andrews-media-company` | 18 | ✓ | - | ✓ | full structure (18 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `growth-ecosystems` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `harry-dry-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jasmin-alic-linkedin-growth` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jason-fladlien-marketing` | 27 | ✓ | - | ✓ | full structure (27 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jen-santulan-listing-content` | 3 | ✓ | 5 (avg 7.41) |  | 5 traces, avg 7.41 |
| `jeremy-haynes-mindset-systems` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jeremy-miner-identity-persuasion` | 11 | ✓ | - | ✓ | full structure (11 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jim-oshaughnessy-philosopher-financier` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joanna-wiebe-persuasion-mastery` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joanna-wiebe-writing-careers` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `john-whiting-propaganda-machine` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jonathan-courtney-marketing` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `jonathan-franzen-storytelling` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joscha-bach-consciousness` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `josh-sanders-linkedin-growth` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joshua-smith-real-estate` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jun-yuh-creator-vision` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jun-yuh-personal-brand` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-addictive-storytelling` | 11 | ✓ | - | ✓ | full structure (11 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-ai-content-engine` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-audience-obsession` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-content-psychology` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-word-mastery` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kittl-graphic-design` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lance-yichao-context-engineering` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lara-acosta-content-system` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lindsay-ai-consulting` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `linkedin-2026-format-arbitrage` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `logan-kilpatrick-ai-studio` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lucas-alpay-storytelling` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-avatar-machine` | 13 | ✓ | 3 (avg 7.25) | ✓ | 3 traces, avg 7.25 |
| `luke-iha-client-mastery` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-creative-strategy` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-cross-domain` | 4 |  | - | ✓ | 4 workflows but no genius.md; cross-referenced (no trace data) |
| `luke-iha-insight-vectors` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-million-dollar-mechanisms` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-proof-ladder` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-proof-mechanisms` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-unaware-ads` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lulu-cheng-meservey-communications` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `manus-ai-consulting` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `marc-andreessen-ai-thesis` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `maria-wendt-digital-products` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-agent-orchestration` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `mark-kashef-ai-councils` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-banana-squad` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-claude-claw` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-visual-design` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `michael-bernoff-identity-engineering` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `michael-connelly-vivid-writing` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mike-foutia-marketing-tools` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mitch-albom-writing-mastery` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `monk-ai-offer-architecture` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-b-jones-agent-deployment-strategy` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `nate-b-jones-ai-taste-mastery` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-b-jones-intent-engineering` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-b-jones-orchestration-intelligence` | 11 | ✓ | - | ✓ | full structure (11 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-b-jones-trust-architecture` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-herk-client-acquisition` | 1 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `nathan-gotch-ai-seo` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `new-media-kingmaker` | 3 |  | - | ✓ | 3 workflows but no genius.md; cross-referenced (no trace data) |
| `nick-saraev-agentic-workflows` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nick-saraev-bottleneck-thinking` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-client-acquisition` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-niche-positioning` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-sentence-craft` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `noah-hawley-storytelling-mastery` | 20 | ✓ | - | ✓ | full structure (20 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ocean-vuong-perceptual-writing` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `omar-eddaoudi` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `omar-eddaoudi-premium-ads` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `omar-eddaoudi-scaling-ops` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `omar-eltakrori` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `oren-brand-archetypes` | 0 | ✓ | 1 (avg 8.7) |  | has genius.md but <3 workflows; 1 traces, avg 8.7 |
| `oscar-hoglund-sound-storytelling` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `paul-james-ai-automation` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `pj-accetturo-ai-video` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `product-design-build` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `rachel-woods-ai-operations` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `robert-mack-comedy-writing` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ross-mckay-premium-at-scale` | 1 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `sabri-suby-ai-advertising` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sabrina-ramonov-ai-monetization` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sam-goddard-media-scaling` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sam-parr-copywriting` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sam-parr-taste-acquisition` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `samuel-thompson-product-launch` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sean-kochel-ai-business` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sean-kochel-design-first-build` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `seena-rez-tiktok-commerce` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `self-evolving-systems` | 1 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `seth-godin-brand` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `seth-godin-ideavirus` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `seth-godin-philosophy` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `shaan-puri-storytelling` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `shan-hanif-audience-monetization` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `sherwin-wu-ai-engineering` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sky-tan-format-engine` | 12 | ✓ | 1 (avg 7.25) |  | 1 traces, avg 7.25 |
| `stefan-georgi-dopamine-copy` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `steven-pressfield-narrative-mastery` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `stockton-walbeck-lead-magnets` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `story-compass` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `supercomputer` | 0 | ✓ | 5 (avg 7.29) | ✓ | has genius.md but <3 workflows; 5 traces, avg 7.29 |
| `tao-prompts-ai-video` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `tim-danilov-niche-bending` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tobias-allen-marketing-mastery` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-noske-content-creation` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-noske-personal-brand` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-segura-comedy-storytelling` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tommy-clark-linkedin-growth` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `tyler-denk-audience-monetization` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `velocity-scaling` | 18 | ✓ | - | ✓ | full structure (18 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ward-farnsworth-rhetorical-mastery` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `wright-thompson-mastery` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |

## Tier REVIEW (34 skills)

Heuristics conflict — these need human eyes before tier finalization.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `andreessen-horowitz-new-media` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `bitbranding-fashion-shopify` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `brad-bonanno-explainer-architecture` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `dara-denney-meta-ads` | 5 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `dr-k-consciousness` | 11 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `ghostwriting-voice-engine` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `greg-hoffman-brand-mastery` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jessica-jensen-platform-intelligence` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kieran-flanagan-audience-intelligence` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kieran-flanagan-content-engine` | 8 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kieran-flanagan-content-ops` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `lamott-craft` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `liam-mley-ai-brain-builder` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `made-to-stick-messaging` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `nba-betting-edge` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `new-media-ghostwriting` | 1 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `oren-content-team-architecture` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-luxury-psychology` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-one-person-ai-marketer` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-operational-systems` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-repositioning` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-taste-development` | 5 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `patrick-debois-cdlc` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-ai-event-analysis` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-making` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-risk-management` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `satori-graphics` | 14 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sean-mabry-voice-mastery` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `sean-macintyre-persuasion-philosophy` | 17 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sharran-srivatsaa-scaling` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `soowei-consulting-leverage` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `taki-moore-lifestyle-business` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `thrivecart-digital-products` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `wordsatscale-seo-ranking` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |

## Tier C (1 skills)

Archive candidates. Low evidence of value. **Do not delete — move to `_archive/skills/` for provenance.** Review individually before archiving (some may be load-bearing user domain skills).

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
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
| `creative-direction` | 0 | ✓ | 4 (avg 8.11) | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `design-md` | 7 | ✓ | 2 (avg 8.85) | ✓ | system/Anthropic utility skill — not graded against expert rubric |
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
| `skill-creator` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `slack-gif-creator` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `stitch-loop` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `swarm-commander` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
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

Machine-readable records: `evolution_store/skill_audit_2026-06-09.jsonl`
