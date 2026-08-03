# Skill Audit — 2026-08-03

**Total skills**: 388
**Tier distribution**: A=54, B=193, REVIEW=114, UTILITY=27

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

## Heartbeat Checks (`directives/skill-craft-standard.md` — TIER-AFFECTING)

6 checks: anti-patterns ≥5 sourced · ≥3 verbatim exemplars · recognition test · source ledger · named-entity floor · workflow Output Schema+Quality Gate. Failing ≥2 caps the tier at B.

10 skill(s) fail ≥2 checks (0 tier-capped this run):

- `bilawal-sidhu`: anti_patterns_sourced, recognition_test
- `curious-refuge`: anti_patterns_sourced, recognition_test
- `dave-clark`: anti_patterns_sourced, recognition_test
- `diandra-escobar-linkedin-mastery`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts, menu_parity
- `fashion-coupids`: anti_patterns_sourced, recognition_test
- `generate`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts, menu_parity
- `grace-liu`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts, menu_parity
- `mickmumpitz`: anti_patterns_sourced, recognition_test, workflow_contracts
- `nick-st-pierre`: anti_patterns_sourced, recognition_test
- `rory-flynn`: anti_patterns_sourced, recognition_test

## Craft Standard Flags (`directives/skill-craft-standard.md` — advisory, not tier-affecting)

353 skills have at least one cheap deterministic gap:

- `adam-enfroy-affiliate-marketing`: frontmatter missing domain, frontmatter missing when_to_use
- `adam-sandler-second-brain-gtm`: frontmatter missing domain, frontmatter missing when_to_use
- `ai-carousel-content-engine`: frontmatter missing when_to_use
- `ai-chris-lee-zero-testimonial-sales`: frontmatter missing when_to_use
- `alan-aragon-nutrition`: frontmatter missing domain, frontmatter missing when_to_use
- `alen-sultanic-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `alex-content-science`: frontmatter missing when_to_use
- `alex-copper-creative-strategy`: frontmatter missing domain, frontmatter missing when_to_use
- `alex-hormozi-business`: frontmatter missing domain, frontmatter missing when_to_use
- `alex-m-smith-natural-strategy`: frontmatter missing when_to_use, hardcoded score pattern in 02-sacred-truth-inventory.md
- `alex-myatt-creative-engine`: frontmatter missing when_to_use
- `alex-suzuki-digital-product-revenue-os`: frontmatter missing when_to_use
- `ali-abdaal-action-bias`: frontmatter missing domain, frontmatter missing when_to_use
- `andreessen-horowitz-new-media`: frontmatter missing domain, frontmatter missing when_to_use
- `andrew-dun-vibe-consulting`: frontmatter missing when_to_use
- `andrew-lane-design-systems`: frontmatter missing domain, frontmatter missing when_to_use
- `andrew-stanton-audience-engineering`: frontmatter missing when_to_use
- `andrew-wilkinson-ai-entrepreneurship`: frontmatter missing domain, frontmatter missing when_to_use
- `andy-galpin-training-intelligence`: frontmatter missing when_to_use
- `andy-lo-premium-websites`: frontmatter missing when_to_use
- `april-dunford-positioning`: frontmatter missing domain, frontmatter missing when_to_use
- `ash-maurya-founder-systems`: frontmatter missing domain, frontmatter missing when_to_use
- `ash-maurya-lean-metrics`: frontmatter missing domain, frontmatter missing when_to_use
- `attention-hijack-hooks`: frontmatter missing domain, frontmatter missing when_to_use
- `authority-hacker-ai-social-media`: frontmatter missing domain, frontmatter missing when_to_use
- `banana-pro-director`: frontmatter missing domain, frontmatter missing when_to_use
- `ben-watkins-storytelling`: frontmatter missing when_to_use
- `benjamin-hardy-identity`: frontmatter missing domain, frontmatter missing when_to_use
- `bilawal-sidhu`: frontmatter missing domain, frontmatter missing when_to_use
- `bill-browder-high-stakes-narrative`: frontmatter missing when_to_use
- `bitbranding-fashion-shopify`: frontmatter missing when_to_use
- `bond-halbert-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `boris-claude-code`: frontmatter missing domain, frontmatter missing when_to_use
- `brad-bonanno-explainer-architecture`: frontmatter missing when_to_use
- `brand-operating-system`: frontmatter missing domain, frontmatter missing when_to_use, hardcoded score pattern in 07-wrap.md
- `brandon-jacoby-taste-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `brendan-kane-viral-strategy`: frontmatter missing domain, frontmatter missing when_to_use
- `briar-cochran-content-science`: frontmatter missing when_to_use
- `brock-johnson-shareworthy-content`: frontmatter missing domain, frontmatter missing when_to_use
- `business-intelligence-audit`: frontmatter missing domain, frontmatter missing when_to_use
- `caleb-ralston-personal-brand`: frontmatter missing domain, frontmatter missing when_to_use
- `cardinal-mason-ai-copywriting`: frontmatter missing domain, frontmatter missing when_to_use, hardcoded score pattern in 05-performance-optimization-proof.md
- `chase-hughes-context-engineering`: frontmatter missing when_to_use
- `chase-hughes-conversational-influence`: frontmatter missing when_to_use
- `cheri-tree-bank-buyology`: frontmatter missing domain, frontmatter missing when_to_use
- `chief-of-staff-os`: frontmatter missing when_to_use
- `chris-cimorelli-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `chris-do-design-business`: frontmatter missing domain, frontmatter missing when_to_use
- `cinema-worldbuilder-pro`: frontmatter missing domain, frontmatter missing when_to_use
- `cinematic-documentary`: frontmatter missing when_to_use
- `coaching-business-os`: frontmatter missing domain, frontmatter missing when_to_use
- `cognitive-engagement-optimizer`: frontmatter missing when_to_use
- `context-profile-architect`: frontmatter missing domain, frontmatter missing when_to_use
- `corey-mcclain-persona-engineering`: frontmatter missing when_to_use
- `craig-clemens-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `creative-campaign-strategy`: frontmatter missing when_to_use
- `curious-refuge`: frontmatter missing domain, frontmatter missing when_to_use
- `dai-media-consumer-posture`: frontmatter missing domain, frontmatter missing when_to_use
- `dakota-content-design`: frontmatter missing domain, frontmatter missing when_to_use
- `damon-cart-nlp`: frontmatter missing domain, frontmatter missing when_to_use
- `dan-bolton-coaching-offers`: frontmatter missing domain, frontmatter missing when_to_use
- `dan-koe-ai-leverage`: frontmatter missing when_to_use
- `dan-koe-multipassionate-mastery`: frontmatter missing when_to_use
- `dan-martell-business-scaling`: frontmatter missing domain, frontmatter missing when_to_use
- `dan-wang-literary-analysis`: frontmatter missing when_to_use
- `daniel-pink-writing-structure`: frontmatter missing domain, frontmatter missing when_to_use
- `daniel-priestley-24-assets-os`: frontmatter missing domain, frontmatter missing when_to_use
- `daniel-priestley-oversubscribed`: frontmatter missing when_to_use
- `daniel-priestley-sll-engine`: frontmatter missing domain, frontmatter missing when_to_use
- `daniel-thrasher-affiliate`: frontmatter missing domain, frontmatter missing when_to_use
- `dara-denney-meta-ads`: frontmatter missing when_to_use
- `darrel-wilson-ai-affiliate`: frontmatter missing when_to_use
- `darrel-wilson-ai-monetization`: frontmatter missing domain, frontmatter missing when_to_use
- `dave-clark`: frontmatter missing domain, frontmatter missing when_to_use
- `david-bayer-elite-communication`: frontmatter missing domain, frontmatter missing when_to_use
- `david-deutsch-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `david-mcraney-belief-change`: frontmatter missing domain, frontmatter missing when_to_use
- `david-perell-writing`: frontmatter missing domain, frontmatter missing when_to_use
- `david-placek-naming`: frontmatter missing when_to_use
- `deliberate`: frontmatter missing domain, frontmatter missing when_to_use
- `deya-business-systems`: frontmatter missing domain, frontmatter missing when_to_use
- `diandra-escobar-linkedin-growth`: frontmatter missing when_to_use
- `diandra-escobar-linkedin-mastery`: no genius.md, zero workflows, frontmatter missing when_to_use
- `dom-iacovone-multi-company-operator`: frontmatter missing when_to_use
- `donald-miller-business-growth`: frontmatter missing domain, frontmatter missing when_to_use
- `donald-miller-cognitive-load`: frontmatter missing domain, frontmatter missing when_to_use
- `donald-miller-culture-turnaround`: frontmatter missing domain, frontmatter missing when_to_use
- `donald-miller-messaging-evolution`: frontmatter missing domain, frontmatter missing when_to_use
- `donald-miller-storybrand`: frontmatter missing domain, frontmatter missing when_to_use
- `dr-k-consciousness`: frontmatter missing domain, frontmatter missing when_to_use
- `dr-kriukow-humanization`: frontmatter missing when_to_use
- `enrico-incarnati-instagram-realestate`: frontmatter missing domain, frontmatter missing when_to_use
- `eric-roth-screenwriting-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `eric-roth-writing-mastery`: frontmatter missing when_to_use
- `erica-mallet-brand-magnetism`: frontmatter missing domain, frontmatter missing when_to_use
- `ethan-smith-aeo`: frontmatter missing domain, frontmatter missing when_to_use
- `eugene-teo-training`: frontmatter missing domain, frontmatter missing when_to_use
- `evan-spiegel-distribution-architecture`: frontmatter missing when_to_use
- `expert-assembly-os`: frontmatter missing when_to_use
- `extract-mastery`: frontmatter missing when_to_use
- `fantastic-posters`: frontmatter missing domain, frontmatter missing when_to_use
- `fareed-zakaria-writing-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `fashion-coupids`: frontmatter missing domain, frontmatter missing when_to_use
- `forge-os`: frontmatter missing domain, frontmatter missing when_to_use
- `fraser-cottrell-paid-ads`: frontmatter missing domain, frontmatter missing when_to_use
- `fresh-voice-system`: frontmatter missing domain, frontmatter missing when_to_use
- `fryderyk-wiatrowski-ai-employee-os`: frontmatter missing domain, frontmatter missing when_to_use
- `futurepedia-prompt-engineering`: frontmatter missing domain, frontmatter missing when_to_use
- `gabe-novotny-fitness-content-business`: frontmatter missing domain, frontmatter missing when_to_use
- `gary-vaynerchuk-attention`: frontmatter missing domain, frontmatter missing when_to_use
- `generate`: no genius.md, zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `ghostwriting-voice-engine`: frontmatter missing domain, frontmatter missing when_to_use
- `gpt-image-2-director`: frontmatter missing domain, frontmatter missing when_to_use
- `grace-andrews-media-company`: frontmatter missing when_to_use
- `grace-liu`: zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `greg-hickman-service-scaling`: frontmatter missing domain, frontmatter missing when_to_use
- `greg-hoffman-brand-mastery`: frontmatter missing when_to_use
- `growth-ecosystems`: frontmatter missing when_to_use
- `harry-dry-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `henrik-werdelin-portfolio-entrepreneurship`: frontmatter missing domain, frontmatter missing when_to_use
- `henry-shukman-contemplative-writing`: frontmatter missing when_to_use
- `higgsfield-creative-studio`: frontmatter missing domain, frontmatter missing when_to_use
- `hilary-gridley`: frontmatter missing domain, frontmatter missing when_to_use
- `how-i-write-os`: frontmatter missing when_to_use
- `jack-roberts-design-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `james-i-bond-brain-glue`: frontmatter missing domain, frontmatter missing when_to_use
- `jasmin-alic-linkedin-growth`: frontmatter missing domain, frontmatter missing when_to_use
- `jason-fladlien-marketing`: frontmatter missing when_to_use
- `jay-hiette-coaching-positioning`: frontmatter missing domain, frontmatter missing when_to_use
- `jeremy-haynes-cold-offer`: frontmatter missing when_to_use
- `jeremy-haynes-mindset-systems`: frontmatter missing domain, frontmatter missing when_to_use
- `jeremy-miner-identity-persuasion`: frontmatter missing when_to_use
- `jessica-jensen-platform-intelligence`: frontmatter missing when_to_use
- `jiang-xueqin-cognitive-autonomy`: frontmatter missing domain, frontmatter missing when_to_use
- `jim-oshaughnessy-philosopher-financier`: frontmatter missing when_to_use
- `joanna-wiebe-persuasion-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `joanna-wiebe-writing-careers`: frontmatter missing domain, frontmatter missing when_to_use
- `joey-cinema-os`: frontmatter missing domain, frontmatter missing when_to_use
- `john-whiting-propaganda-machine`: frontmatter missing domain, frontmatter missing when_to_use
- `jonah-berger-contagious`: frontmatter missing domain, frontmatter missing when_to_use
- `jonathan-courtney-marketing`: frontmatter missing domain, frontmatter missing when_to_use
- `jonathan-franzen-storytelling`: frontmatter missing when_to_use
- `joscha-bach-consciousness`: frontmatter missing when_to_use
- `josh-kaufman-business-fundamentals`: frontmatter missing domain, frontmatter missing when_to_use
- `josh-sanders-linkedin-growth`: frontmatter missing domain, frontmatter missing when_to_use
- `joshua-smith-real-estate`: frontmatter missing domain, frontmatter missing when_to_use
- `jun-yuh-creator-vision`: frontmatter missing domain, frontmatter missing when_to_use
- `jun-yuh-personal-brand`: frontmatter missing domain, frontmatter missing when_to_use
- `justin-welsh-solopreneur`: frontmatter missing domain, frontmatter missing when_to_use
- `kallaway-addictive-storytelling`: frontmatter missing when_to_use
- `kallaway-ai-content-engine`: frontmatter missing when_to_use
- `kallaway-audience-obsession`: frontmatter missing when_to_use
- `kallaway-content-operating-system`: frontmatter missing when_to_use
- `kallaway-content-psychology`: frontmatter missing when_to_use
- `kallaway-content-system`: frontmatter missing when_to_use
- `kallaway-illusion-of-novelty`: frontmatter missing when_to_use, hardcoded score pattern in novelty-forge.md
- `kallaway-social-commerce`: frontmatter missing when_to_use
- `kallaway-word-mastery`: frontmatter missing domain, frontmatter missing when_to_use, hardcoded score pattern in articulation-mastery-sprint.md
- `kieran-flanagan-audience-intelligence`: frontmatter missing domain, frontmatter missing when_to_use
- `kieran-flanagan-content-engine`: frontmatter missing domain, frontmatter missing when_to_use
- `kieran-flanagan-content-ops`: frontmatter missing domain, frontmatter missing when_to_use
- `kittl-graphic-design`: frontmatter missing domain, frontmatter missing when_to_use
- `kj-rainey-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `knowledge-architecture-studio`: frontmatter missing when_to_use
- `kobi-brown-educational-virality`: frontmatter missing when_to_use
- `kunal-shah-consumer-psychology`: frontmatter missing domain, frontmatter missing when_to_use
- `lamott-allen-really-real-writing`: frontmatter missing when_to_use
- `lamott-craft`: frontmatter missing when_to_use
- `lance-yichao-context-engineering`: frontmatter missing domain, frontmatter missing when_to_use
- `lara-acosta-content-system`: frontmatter missing domain, frontmatter missing when_to_use
- `lara-acosta-linkedin-growth`: frontmatter missing domain, frontmatter missing when_to_use
- `lara-acosta-linkedin-mastery`: frontmatter missing when_to_use
- `liam-mley-ai-brain-builder`: frontmatter missing domain, frontmatter missing when_to_use
- `liam-ottley-linkedin-lead-magnet`: frontmatter missing domain, frontmatter missing when_to_use
- `lindsay-ai-consulting`: frontmatter missing when_to_use
- `linkedin-2026-format-arbitrage`: frontmatter missing domain, frontmatter missing when_to_use
- `logan-kilpatrick-ai-studio`: frontmatter missing domain, frontmatter missing when_to_use
- `lucas-alpay-storytelling`: frontmatter missing when_to_use
- `luisa-zhou-coaching`: frontmatter missing domain, frontmatter missing when_to_use
- `luke-alexander-ai-business`: frontmatter missing domain, frontmatter missing when_to_use
- `luke-iha-avatar-machine`: frontmatter missing when_to_use
- `luke-iha-client-mastery`: frontmatter missing when_to_use
- `luke-iha-copy-blocks`: frontmatter missing when_to_use
- `luke-iha-creative-strategy`: frontmatter missing when_to_use
- `luke-iha-cross-domain`: frontmatter missing when_to_use
- `luke-iha-insight-vectors`: frontmatter missing when_to_use
- `luke-iha-million-dollar-mechanisms`: frontmatter missing domain, frontmatter missing when_to_use
- `luke-iha-proof-ladder`: frontmatter missing domain, frontmatter missing when_to_use
- `luke-iha-proof-mechanisms`: frontmatter missing when_to_use
- `luke-iha-unaware-ads`: frontmatter missing when_to_use
- `luke-iha-vicious-hooks`: frontmatter missing when_to_use
- `luke-iha-vsl-leads`: frontmatter missing when_to_use
- `lulu-cheng-meservey-communications`: frontmatter missing when_to_use, hardcoded score pattern in lulu-conviction-copy.md
- `made-to-stick-messaging`: frontmatter missing domain, frontmatter missing when_to_use
- `manus-ai-consulting`: frontmatter missing when_to_use
- `marc-andreessen-ai-thesis`: frontmatter missing domain, frontmatter missing when_to_use
- `maria-wendt-digital-products`: frontmatter missing domain, frontmatter missing when_to_use
- `marisa-murgatroyd-course-design`: frontmatter missing domain, frontmatter missing when_to_use
- `mark-forsyth-rhetoric`: frontmatter missing domain, frontmatter missing when_to_use
- `mark-kashef-agent-orchestration`: frontmatter missing domain, frontmatter missing when_to_use
- `mark-kashef-ai-councils`: frontmatter missing when_to_use
- `mark-kashef-banana-squad`: frontmatter missing domain, frontmatter missing when_to_use
- `mark-kashef-claude-claw`: frontmatter missing domain, frontmatter missing when_to_use
- `mark-kashef-silver-platter-agentic-os`: frontmatter missing domain, frontmatter missing when_to_use
- `mark-kashef-visual-design`: frontmatter missing domain, frontmatter missing when_to_use, hardcoded score pattern in 05-visual-taste-gate.md
- `mark-manson-values-psychology`: frontmatter missing domain, frontmatter missing when_to_use
- `marketing-studio-director`: frontmatter missing domain, frontmatter missing when_to_use
- `matt-mcgarry-newsletters`: frontmatter missing domain, frontmatter missing when_to_use
- `matthew-lakajev-linkedin`: frontmatter missing domain, frontmatter missing when_to_use
- `matthew-volkwyn-copywriting`: frontmatter missing domain, frontmatter missing when_to_use, hardcoded score pattern in 01-audit-copy.md
- `meg-heckman-buyer-trigger-os`: frontmatter missing when_to_use
- `michael-bernoff-identity-engineering`: frontmatter missing domain, frontmatter missing when_to_use
- `michael-connelly-vivid-writing`: frontmatter missing when_to_use, hardcoded score pattern in momentum-audit.md
- `michael-israetel-hypertrophy`: frontmatter missing domain, frontmatter missing when_to_use
- `michael-margolis-user-research`: frontmatter missing domain, frontmatter missing when_to_use
- `mickmumpitz`: frontmatter missing domain, frontmatter missing when_to_use
- `mike-foutia-marketing-tools`: frontmatter missing when_to_use
- `mike-sherrard-realtor-branding`: frontmatter missing domain, frontmatter missing when_to_use
- `mike-taylor-synthetic-research`: frontmatter missing domain, frontmatter missing when_to_use
- `mitch-albom-writing-mastery`: frontmatter missing when_to_use
- `monk-ai-offer-architecture`: frontmatter missing when_to_use
- `nate-b-jones-agent-deployment-strategy`: frontmatter missing domain, frontmatter missing when_to_use
- `nate-b-jones-ai-taste-mastery`: frontmatter missing when_to_use
- `nate-b-jones-auto-improvement-loops`: frontmatter missing when_to_use
- `nate-b-jones-context-engineering`: frontmatter missing when_to_use
- `nate-b-jones-intent-engineering`: frontmatter missing domain, frontmatter missing when_to_use
- `nate-b-jones-orchestration-intelligence`: frontmatter missing when_to_use
- `nate-b-jones-trust-architecture`: frontmatter missing domain, frontmatter missing when_to_use
- `nate-herk-client-acquisition`: frontmatter missing domain, frontmatter missing when_to_use
- `nathan-gotch-ai-seo`: frontmatter missing domain, frontmatter missing when_to_use
- `nba-betting-edge`: frontmatter missing domain, frontmatter missing when_to_use
- `new-media-ghostwriting`: frontmatter missing when_to_use
- `new-media-kingmaker`: frontmatter missing when_to_use
- `nick-saraev-agentic-workflows`: frontmatter missing domain, frontmatter missing when_to_use
- `nick-saraev-bottleneck-thinking`: frontmatter missing domain, frontmatter missing when_to_use
- `nick-st-pierre`: frontmatter missing domain, frontmatter missing when_to_use
- `nicolas-cole-client-acquisition`: frontmatter missing domain, frontmatter missing when_to_use
- `nicolas-cole-digital-products`: frontmatter missing domain, frontmatter missing when_to_use
- `nicolas-cole-edan-writing-mechanics`: frontmatter missing when_to_use
- `nicolas-cole-newsletter-flywheel`: frontmatter missing when_to_use, hardcoded score pattern in 01-newsletter-flywheel.md
- `nicolas-cole-niche-positioning`: frontmatter missing when_to_use
- `nicolas-cole-nonfiction-value-architecture`: frontmatter missing when_to_use
- `nicolas-cole-sales-education-messaging`: frontmatter missing when_to_use
- `nicolas-cole-sentence-craft`: frontmatter missing domain, frontmatter missing when_to_use
- `nir-eyal-habit-design`: frontmatter missing when_to_use
- `noah-hawley-storytelling-mastery`: frontmatter missing when_to_use
- `ocean-vuong-perceptual-writing`: frontmatter missing when_to_use
- `omar-eddaoudi`: frontmatter missing domain, frontmatter missing when_to_use
- `omar-eddaoudi-premium-ads`: frontmatter missing domain, frontmatter missing when_to_use
- `omar-eddaoudi-scaling-ops`: frontmatter missing domain, frontmatter missing when_to_use
- `omar-eltakrori`: frontmatter missing when_to_use
- `oren-brand-archetypes`: frontmatter missing when_to_use
- `oren-content-team-architecture`: frontmatter missing domain, frontmatter missing when_to_use
- `oren-identity-brand-os`: frontmatter missing domain, frontmatter missing when_to_use
- `oren-luxury-psychology`: frontmatter missing when_to_use
- `oren-one-person-ai-marketer`: frontmatter missing when_to_use
- `oren-operational-systems`: frontmatter missing domain, frontmatter missing when_to_use
- `oren-repositioning`: frontmatter missing domain, frontmatter missing when_to_use
- `oren-taste-development`: frontmatter missing when_to_use
- `oscar-hoglund-sound-storytelling`: frontmatter missing domain, frontmatter missing when_to_use
- `packy-mccormick-writing`: frontmatter missing domain, frontmatter missing when_to_use
- `paolo-trivellato-lead-magnet-engine`: frontmatter missing domain, frontmatter missing when_to_use
- `pat-flynn-passive-income`: frontmatter missing domain, frontmatter missing when_to_use
- `patrick-dang-online-business`: frontmatter missing domain, frontmatter missing when_to_use
- `patrick-debois-cdlc`: frontmatter missing when_to_use
- `paul-harding-lyric-prose`: frontmatter missing when_to_use
- `paul-james-ai-automation`: frontmatter missing domain, frontmatter missing when_to_use
- `persuasion-story-code`: frontmatter missing domain, frontmatter missing when_to_use
- `phil-m-jones-conversational-influence`: frontmatter missing when_to_use
- `pj-accetturo-ai-video`: frontmatter missing domain, frontmatter missing when_to_use
- `prediction-market-ai-event-analysis`: frontmatter missing when_to_use
- `prediction-market-making`: frontmatter missing domain, frontmatter missing when_to_use
- `prediction-market-risk-management`: frontmatter missing when_to_use
- `prediction-market-weather-trading`: frontmatter missing domain, frontmatter missing when_to_use
- `product-design-build`: frontmatter missing domain, frontmatter missing when_to_use
- `prosperity-coach-system`: frontmatter missing domain, frontmatter missing when_to_use
- `rachel-woods-ai-operations`: frontmatter missing domain, frontmatter missing when_to_use
- `rafa-conde-fourth-wall-experience-os`: frontmatter missing when_to_use
- `rafa-conde-memorable-product-design`: frontmatter missing domain, frontmatter missing when_to_use
- `ray-amjad-agentic-ladder`: frontmatter missing domain, frontmatter missing when_to_use
- `reid-hoffman-ai-strategy`: frontmatter missing domain, frontmatter missing when_to_use
- `riley-brown-marketing-automation`: frontmatter missing when_to_use
- `robert-greene-power-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `robert-mack-comedy-writing`: frontmatter missing when_to_use
- `rory-flynn`: frontmatter missing domain, frontmatter missing when_to_use
- `rory-sutherland-marketing`: frontmatter missing when_to_use
- `ross-mckay-premium-at-scale`: frontmatter missing domain, frontmatter missing when_to_use
- `ross-minchev-digital-products`: frontmatter missing domain, frontmatter missing when_to_use
- `russell-brunson-funnels`: frontmatter missing domain, frontmatter missing when_to_use
- `sabri-suby-ai-advertising`: frontmatter missing domain, frontmatter missing when_to_use
- `sabrina-ramonov-ai-monetization`: frontmatter missing when_to_use
- `sam-goddard-media-scaling`: frontmatter missing domain, frontmatter missing when_to_use
- `sam-parr-copywriting`: frontmatter missing when_to_use
- `sam-parr-copywriting-mechanics`: frontmatter missing domain, frontmatter missing when_to_use
- `sam-parr-taste-acquisition`: frontmatter missing when_to_use
- `samuel-thompson-product-launch`: frontmatter missing domain, frontmatter missing when_to_use
- `sarah-levinger-ad-psychology`: frontmatter missing domain, frontmatter missing when_to_use
- `satori-graphics`: frontmatter missing when_to_use
- `sean-dollwet-kdp-publishing`: frontmatter missing domain, frontmatter missing when_to_use
- `sean-kochel-ai-business`: frontmatter missing domain, frontmatter missing when_to_use
- `sean-kochel-design-first-build`: frontmatter missing domain, frontmatter missing when_to_use
- `sean-mabry-voice-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `sean-macintyre-persuasion-philosophy`: frontmatter missing when_to_use
- `seena-rez-tiktok-commerce`: frontmatter missing domain, frontmatter missing when_to_use
- `self-evolving-systems`: frontmatter missing when_to_use, hardcoded score pattern in trajectory-ratchet.md
- `semantic-document-library-os`: frontmatter missing when_to_use
- `seth-godin-brand`: frontmatter missing when_to_use
- `seth-godin-ideavirus`: frontmatter missing when_to_use
- `seth-godin-marketing-mind`: frontmatter missing when_to_use
- `seth-godin-philosophy`: frontmatter missing when_to_use
- `shaan-puri-storytelling`: frontmatter missing domain, frontmatter missing when_to_use
- `shan-hanif-audience-monetization`: frontmatter missing domain, frontmatter missing when_to_use
- `sharran-srivatsaa-scaling`: frontmatter missing when_to_use
- `sherwin-wu-ai-engineering`: frontmatter missing domain, frontmatter missing when_to_use
- `simon-intellectual-library-os`: frontmatter missing when_to_use
- `sky-tan-format-engine`: frontmatter missing when_to_use
- `soowei-consulting-leverage`: frontmatter missing when_to_use
- `stefan-georgi-dopamine-copy`: frontmatter missing when_to_use
- `steven-kotler-flow-performance`: frontmatter missing domain, frontmatter missing when_to_use
- `steven-pressfield-narrative-mastery`: frontmatter missing when_to_use
- `steven-young-consciousness`: frontmatter missing domain, frontmatter missing when_to_use
- `stockton-walbeck-lead-magnets`: frontmatter missing domain, frontmatter missing when_to_use
- `story-bible-builder`: frontmatter missing domain, frontmatter missing when_to_use
- `story-compass`: frontmatter missing when_to_use
- `strength-conditioning-os`: frontmatter missing when_to_use
- `sunny-lenarduzzi-youtube`: frontmatter missing domain, frontmatter missing when_to_use
- `supercomputer`: frontmatter missing domain, frontmatter missing when_to_use
- `susan-orlean-narrative-nonfiction`: frontmatter missing when_to_use
- `sweat-equity-speedrun-social-os`: frontmatter missing domain, frontmatter missing when_to_use
- `taki-moore-lifestyle-business`: frontmatter missing domain, frontmatter missing when_to_use
- `tao-prompts-ai-video`: frontmatter missing domain, frontmatter missing when_to_use
- `taylor-welch-wealthy-consultant`: frontmatter missing domain, frontmatter missing when_to_use
- `tess-barclay-social-content`: frontmatter missing domain, frontmatter missing when_to_use
- `thrivecart-digital-products`: frontmatter missing domain, frontmatter missing when_to_use
- `tim-danilov-niche-bending`: frontmatter missing domain, frontmatter missing when_to_use, hardcoded score pattern in blue-ocean-market-identification.md
- `tobi-lutke-business-leadership`: frontmatter missing domain, frontmatter missing when_to_use
- `tobias-allen-marketing-mastery`: frontmatter missing when_to_use
- `tom-noske-content-creation`: frontmatter missing when_to_use
- `tom-noske-personal-brand`: frontmatter missing domain, frontmatter missing when_to_use
- `tom-segura-comedy-storytelling`: frontmatter missing when_to_use
- `tommy-clark-linkedin-growth`: frontmatter missing domain, frontmatter missing when_to_use
- `tyler-denk-audience-monetization`: frontmatter missing domain, frontmatter missing when_to_use
- `velocity-scaling`: frontmatter missing when_to_use
- `verticalize`: frontmatter missing when_to_use
- `vince-nijhof-dtc-operator-system`: frontmatter missing when_to_use
- `voice-os`: frontmatter missing when_to_use
- `ward-farnsworth-rhetorical-mastery`: frontmatter missing when_to_use
- `wordsatscale-seo-ranking`: frontmatter missing domain, frontmatter missing when_to_use
- `wright-thompson-mastery`: frontmatter missing when_to_use
- `writing-depth-layer`: frontmatter missing when_to_use
- `yann-martel-storytelling-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `youtube-video-context-analysis`: frontmatter missing when_to_use
- `yuri-elkaim-health-coaching-business`: frontmatter missing domain, frontmatter missing when_to_use

## CORE DRIFT (Production Core entries with zero traces in window)

26 of 36 core entries have no production traces in the last 60d:

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
- voice-os

Action: if an entry stays here 2 consecutive months, demote it from PRODUCTION_CORE.md; promote any long-tail skill with 3+ traces.

## CONTEXT SIZE RATCHET (always-on files — shrink free, grow flagged)

- CLAUDE.md: 15,207B (≤ last scan — ratchet holds)
- MEMORY.md: 0B (≤ last scan — ratchet holds)

## Tier A (54 skills)

These are the system's strongest skills. Prioritize for promotion, ground-truth benchmarking, and revenue tracking.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `andreessen-horowitz-new-media` | 4 | ✓ | 1 (avg 8.3) |  | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces) |
| `brock-johnson-shareworthy-content` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `dan-koe-ai-leverage` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `dan-koe-multipassionate-mastery` | 6 | ✓ | 1 (avg 8.3) | ✓ | full structure (6 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `dan-wang-literary-analysis` | 13 | ✓ | 1 (avg 8.3) | ✓ | full structure (13 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `daniel-priestley-oversubscribed` | 9 | ✓ | 1 (avg 8.3) | ✓ | full structure (9 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `david-placek-naming` | 6 | ✓ | 1 (avg 9.3) | ✓ | full structure (6 workflows + genius.md); trace avg 9.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `diandra-escobar-linkedin-growth` | 22 | ✓ | 1 (avg 9.0) | ✓ | full structure (22 workflows + genius.md); trace avg 9.0 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `erica-mallet-brand-magnetism` | 5 | ✓ | 1 (avg 8.3) | ✓ | full structure (5 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `fareed-zakaria-writing-mastery` | 5 | ✓ | 1 (avg 7.7) | ✓ | full structure (5 workflows + genius.md); trace avg 7.7 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `fresh-voice-system` | 3 | ✓ | 1 (avg 8.3) | ✓ | full structure (3 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `ghostwriting-voice-engine` | 4 | ✓ | 1 (avg 8.3) |  | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces) |
| `grace-andrews-media-company` | 18 | ✓ | 1 (avg 8.3) | ✓ | full structure (18 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `jack-roberts-design-mastery` | 15 | ✓ | 1 (avg 8.7) |  | full structure (15 workflows + genius.md); trace avg 8.7 ≥ 7.5 (1 traces) |
| `jasmin-alic-linkedin-growth` | 4 | ✓ | 1 (avg 8.3) | ✓ | full structure (4 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `jason-fladlien-marketing` | 36 | ✓ | 1 (avg 8.0) | ✓ | full structure (36 workflows + genius.md); trace avg 8.0 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
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
| `tommy-clark-linkedin-growth` | 6 | ✓ | 1 (avg 8.3) | ✓ | full structure (6 workflows + genius.md); trace avg 8.3 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `wright-thompson-mastery` | 13 | ✓ | 1 (avg 8.4) | ✓ | full structure (13 workflows + genius.md); trace avg 8.4 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |

## Tier B (193 skills)

Solid skills that are working. Candidates for B→A promotion via genius.md enrichment or workflow expansion.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `adam-enfroy-affiliate-marketing` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `adam-sandler-second-brain-gtm` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ai-chris-lee-zero-testimonial-sales` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alen-sultanic-copywriting` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-content-science` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-copper-creative-strategy` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
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
| `april-dunford-positioning` | 17 | ✓ | - | ✓ | full structure (17 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ash-maurya-founder-systems` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ash-maurya-lean-metrics` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `attention-hijack-hooks` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `authority-hacker-ai-social-media` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ben-watkins-storytelling` | 18 | ✓ | - | ✓ | full structure (18 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `bond-halbert-copywriting` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `boris-claude-code` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `brand-operating-system` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `business-intelligence-audit` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `caleb-ralston-personal-brand` | 11 | ✓ | - | ✓ | full structure (11 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `cardinal-mason-ai-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `chris-cimorelli-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `chris-do-design-business` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `cinema-worldbuilder-pro` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `cinematic-documentary` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `claim-safe-health-marketing` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `coaching-business-os` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `context-profile-architect` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `creative-campaign-strategy` | 23 | ✓ | - | ✓ | full structure (23 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dai-media-consumer-posture` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-bolton-coaching-offers` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-martell-business-scaling` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-pink-writing-structure` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-priestley-24-assets-os` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-priestley-sll-engine` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-thrasher-affiliate` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `darrel-wilson-ai-affiliate` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `darrel-wilson-ai-monetization` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-baldacci-books-that-sell` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
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
| `expert-assembly-os` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `extract-mastery` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `forge-os` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `futurepedia-prompt-engineering` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `geoff-woods-ai-thought-partner` | 17 | ✓ | - | ✓ | full structure (17 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `gpt-image-2-director` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `grace-liu` | 0 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `growth-ecosystems` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `harry-dry-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `how-i-write-os` | 1 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `james-i-bond-brain-glue` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jeremy-haynes-cold-offer` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
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
| `kallaway-content-operating-system` | 1 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `kallaway-content-psychology` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-content-system` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-illusion-of-novelty` | 17 | ✓ | - | ✓ | full structure (17 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
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
| `luke-iha-cross-domain` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-insight-vectors` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-million-dollar-mechanisms` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-vicious-hooks` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lulu-cheng-meservey-communications` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `manus-ai-consulting` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `marc-andreessen-ai-thesis` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `maria-wendt-digital-products` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-forsyth-rhetoric` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-ai-councils` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-silver-platter-agentic-os` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-wargame-os` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-manson-values-psychology` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `marketing-studio-director` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
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
| `nathan-gotch-ai-seo` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `new-media-ghostwriting` | 1 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `new-media-kingmaker` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nick-saraev-bottleneck-thinking` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nick-st-pierre` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-client-acquisition` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-edan-writing-mechanics` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-newsletter-flywheel` | 17 | ✓ | - | ✓ | full structure (17 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-niche-positioning` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-nonfiction-value-architecture` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-sales-education-messaging` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-sentence-craft` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `noah-hawley-storytelling-mastery` | 21 | ✓ | - | ✓ | full structure (21 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
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
| `rory-sutherland-marketing` | 25 | ✓ | - | ✓ | full structure (25 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
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
| `seth-godin-marketing-mind` | 16 | ✓ | - | ✓ | full structure (16 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `seth-godin-philosophy` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `shaan-puri-storytelling` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `shan-hanif-audience-monetization` | 2 | ✓ | 1 (avg 8.3) | ✓ | has genius.md but <3 workflows; 1 traces, avg 8.3 |
| `stefan-georgi-dopamine-copy` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `steven-kotler-flow-performance` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `steven-pressfield-narrative-mastery` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `steven-young-consciousness` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `story-bible-builder` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `story-compass` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tao-prompts-ai-video` | 2 | ✓ | 1 (avg 8.3) | ✓ | has genius.md but <3 workflows; 1 traces, avg 8.3 |
| `tim-danilov-niche-bending` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tobi-lutke-business-leadership` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-noske-content-creation` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-noske-personal-brand` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-segura-comedy-storytelling` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tyler-denk-audience-monetization` | 2 | ✓ | 1 (avg 8.3) | ✓ | has genius.md but <3 workflows; 1 traces, avg 8.3 |
| `velocity-scaling` | 18 | ✓ | - | ✓ | full structure (18 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `vince-nijhof-dtc-operator-system` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `voice-os` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ward-farnsworth-rhetorical-mastery` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `writing-depth-layer` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `youtube-video-context-analysis` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |

## Tier REVIEW (114 skills)

Heuristics conflict — these need human eyes before tier finalization.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `ai-carousel-content-engine` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `alan-aragon-nutrition` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `andy-galpin-training-intelligence` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `banana-pro-director` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `benjamin-hardy-identity` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `bilawal-sidhu` | 2 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `bill-browder-high-stakes-narrative` | 13 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `bitbranding-fashion-shopify` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `brad-bonanno-explainer-architecture` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `brandon-jacoby-taste-mastery` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `brendan-kane-viral-strategy` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `briar-cochran-content-science` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `chase-hughes-context-engineering` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `chase-hughes-conversational-influence` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `cheri-tree-bank-buyology` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `chief-of-staff-os` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `cognitive-engagement-optimizer` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `corey-mcclain-persona-engineering` | 20 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `craig-clemens-copywriting` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `curious-refuge` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `dakota-content-design` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `damon-cart-nlp` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `dara-denney-meta-ads` | 26 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `dave-clark` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `deliberate` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `deya-business-systems` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `diandra-escobar-linkedin-mastery` | 0 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `dr-k-consciousness` | 11 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `eugene-teo-training` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `fantastic-posters` | 14 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `fashion-coupids` | 2 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `fraser-cottrell-paid-ads` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `fryderyk-wiatrowski-ai-employee-os` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `gabe-novotny-fitness-content-business` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `gary-vaynerchuk-attention` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `generate` | 0 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `greg-hickman-service-scaling` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `greg-hoffman-brand-mastery` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `henrik-werdelin-portfolio-entrepreneurship` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `henry-shukman-contemplative-writing` | 13 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `higgsfield-creative-studio` | 2 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `hilary-gridley` | 13 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jay-hiette-coaching-positioning` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jen-santulan-listing-content` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jenny-hoyos-shorts` | 14 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jessica-jensen-platform-intelligence` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jiang-xueqin-cognitive-autonomy` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `joey-cinema-os` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jonah-berger-contagious` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `justin-welsh-solopreneur` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kieran-flanagan-audience-intelligence` | 5 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kieran-flanagan-content-engine` | 9 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kieran-flanagan-content-ops` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kj-rainey-copywriting` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kunal-shah-consumer-psychology` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `lamott-allen-really-real-writing` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `lamott-craft` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `liam-mley-ai-brain-builder` | 5 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `liam-ottley-linkedin-lead-magnet` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `luisa-zhou-coaching` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `marisa-murgatroyd-course-design` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `matthew-lakajev-linkedin` | 13 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `matthew-volkwyn-copywriting` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `meg-heckman-buyer-trigger-os` | 17 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `mickmumpitz` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `mike-sherrard-realtor-branding` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `mike-taylor-synthetic-research` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `nba-betting-edge` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `nir-eyal-habit-design` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-brand-archetypes` | 8 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-content-team-architecture` | 15 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-dara-ad-psychology` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-identity-brand-os` | 14 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-luxury-psychology` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-one-person-ai-marketer` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-operational-systems` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-repositioning` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-taste-development` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `packy-mccormick-writing` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `paolo-trivellato-lead-magnet-engine` | 11 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `patrick-dang-online-business` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `patrick-debois-cdlc` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-ai-event-analysis` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-making` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-risk-management` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prosperity-coach-system` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `rafa-conde-fourth-wall-experience-os` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `rafa-conde-memorable-product-design` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `ray-amjad-agentic-ladder` | 9 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `re-compliance-pack` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `reid-hoffman-ai-strategy` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `riley-brown-marketing-automation` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `robert-greene-power-mastery` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `rory-flynn` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `russell-brunson-funnels` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sarah-levinger-ad-psychology` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `satori-graphics` | 26 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sean-dollwet-kdp-publishing` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sean-mabry-voice-mastery` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `sean-macintyre-persuasion-philosophy` | 17 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sharran-srivatsaa-scaling` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `simon-intellectual-library-os` | 15 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sky-tan-format-engine` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `strength-conditioning-os` | 2 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `sunny-lenarduzzi-youtube` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `supercomputer` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `susan-orlean-narrative-nonfiction` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sweat-equity-speedrun-social-os` | 9 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `taylor-welch-wealthy-consultant` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `tess-barclay-social-content` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `verticalize` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `wordsatscale-seo-ranking` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `yann-martel-storytelling-mastery` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `yuri-elkaim-health-coaching-business` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |

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
| `mcp-builder` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
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

Machine-readable records: `evolution_store/skill_audit_2026-08-03.jsonl`
