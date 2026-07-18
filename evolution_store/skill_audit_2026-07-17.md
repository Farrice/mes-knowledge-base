# Skill Audit — 2026-07-17

**Total skills**: 371
**Tier distribution**: A=11, B=229, C=5, REVIEW=99, UTILITY=27

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

312 skill(s) fail ≥2 checks (6 tier-capped this run):

- `_tmp_audit_diandra`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `adam-enfroy-affiliate-marketing`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `ai-carousel-content-engine`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor, workflow_contracts
- `ai-chris-lee-zero-testimonial-sales`: anti_patterns_sourced, recognition_test, source_ledger
- `alan-aragon-nutrition`: anti_patterns_sourced, recognition_test
- `alen-sultanic-copywriting`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `alex-content-science`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `alex-copper-creative-strategy`: anti_patterns_sourced, recognition_test, source_ledger
- `alex-hormozi-business`: anti_patterns_sourced, recognition_test, source_ledger
- `alex-m-smith-natural-strategy`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `alex-myatt-creative-engine`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `alex-suzuki-digital-product-revenue-os`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor, workflow_contracts
- `ali-abdaal-action-bias`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `andreessen-horowitz-new-media`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, workflow_contracts
- `andrew-dun-vibe-consulting`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `andrew-lane-design-systems`: anti_patterns_sourced, recognition_test, source_ledger
- `andrew-wilkinson-ai-entrepreneurship`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `andy-galpin-training-intelligence`: anti_patterns_sourced, recognition_test, source_ledger
- `andy-lo-premium-websites`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `april-dunford-positioning`: anti_patterns_sourced, recognition_test, source_ledger
- `ash-maurya-founder-systems`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor
- `ash-maurya-lean-metrics`: anti_patterns_sourced, recognition_test, source_ledger
- `attention-hijack-hooks`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `authority-hacker-ai-social-media`: anti_patterns_sourced, recognition_test, source_ledger
- `banana-pro-director`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `benjamin-hardy-identity`: anti_patterns_sourced, recognition_test, source_ledger
- `bitbranding-fashion-shopify`: anti_patterns_sourced, recognition_test, source_ledger
- `bond-halbert-copywriting`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `boris-claude-code`: anti_patterns_sourced, recognition_test, named_entity_floor
- `brad-bonanno-explainer-architecture`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `brand-operating-system`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts **[capped A→B]**
- `brandon-jacoby-taste-mastery`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor
- `brendan-kane-viral-strategy`: anti_patterns_sourced, recognition_test, named_entity_floor
- `brock-johnson-shareworthy-content`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `business-intelligence-audit`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `caleb-ralston-personal-brand`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `cardinal-mason-ai-copywriting`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `chase-hughes-conversational-influence`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `cheri-tree-bank-buyology`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor
- `chief-of-staff-os`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `chris-cimorelli-copywriting`: anti_patterns_sourced, recognition_test, source_ledger
- `chris-do-design-business`: anti_patterns_sourced, recognition_test, source_ledger
- `cinema-worldbuilder-pro`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `cinematic-documentary`: recognition_test, source_ledger, named_entity_floor
- `claim-safe-health-marketing`: anti_patterns_sourced, named_entity_floor
- `coaching-business-os`: anti_patterns_sourced, recognition_test, source_ledger
- `cognitive-engagement-optimizer`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor
- `context-profile-architect`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `corey-mcclain-persona-engineering`: anti_patterns_sourced, recognition_test, named_entity_floor, workflow_contracts
- `craig-clemens-copywriting`: anti_patterns_sourced, recognition_test, named_entity_floor
- `creative-campaign-strategy`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `dai-media-consumer-posture`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `dakota-content-design`: anti_patterns_sourced, recognition_test, source_ledger
- `damon-cart-nlp`: anti_patterns_sourced, recognition_test, source_ledger
- `dan-bolton-coaching-offers`: anti_patterns_sourced, recognition_test, source_ledger
- `dan-koe-ai-leverage`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `dan-koe-multipassionate-mastery`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `dan-martell-business-scaling`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `dan-wang-literary-analysis`: source_ledger, named_entity_floor
- `daniel-pink-writing-structure`: anti_patterns_sourced, recognition_test, source_ledger
- `daniel-priestley-24-assets-os`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor
- `daniel-priestley-oversubscribed`: anti_patterns_sourced, recognition_test, source_ledger
- `daniel-thrasher-affiliate`: anti_patterns_sourced, recognition_test, named_entity_floor
- `dara-denney-meta-ads`: recognition_test, source_ledger
- `darrel-wilson-ai-affiliate`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `darrel-wilson-ai-monetization`: anti_patterns_sourced, recognition_test, source_ledger
- `david-bayer-elite-communication`: anti_patterns_sourced, recognition_test, source_ledger
- `david-deutsch-copywriting`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `david-mcraney-belief-change`: anti_patterns_sourced, recognition_test, named_entity_floor, workflow_contracts
- `david-perell-writing`: anti_patterns_sourced, recognition_test, source_ledger
- `david-placek-naming`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `deliberate`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `deya-business-systems`: anti_patterns_sourced, recognition_test, source_ledger
- `dom-iacovone-multi-company-operator`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor, workflow_contracts
- `donald-miller-business-growth`: anti_patterns_sourced, recognition_test
- `donald-miller-cognitive-load`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `donald-miller-culture-turnaround`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `donald-miller-messaging-evolution`: anti_patterns_sourced, recognition_test
- `donald-miller-storybrand`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `dr-k-consciousness`: recognition_test, source_ledger
- `dr-kriukow-humanization`: anti_patterns_sourced, recognition_test, source_ledger
- `enrico-incarnati-instagram-realestate`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `eric-roth-screenwriting-mastery`: anti_patterns_sourced, source_ledger, workflow_contracts
- `eric-roth-writing-mastery`: anti_patterns_sourced, recognition_test, source_ledger
- `erica-mallet-brand-magnetism`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `ethan-smith-aeo`: anti_patterns_sourced, recognition_test
- `eugene-teo-training`: anti_patterns_sourced, recognition_test, source_ledger
- `evan-spiegel-distribution-architecture`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `expert-assembly-os`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor, workflow_contracts
- `extract-mastery`: anti_patterns_sourced, recognition_test, source_ledger **[capped A→B]**
- `fantastic-posters`: anti_patterns_sourced, verbatim_exemplars, recognition_test, workflow_contracts **[capped A→B]**
- `fareed-zakaria-writing-mastery`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `forge-os`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor, workflow_contracts
- `fraser-cottrell-paid-ads`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `fresh-voice-system`: anti_patterns_sourced, source_ledger, named_entity_floor
- `fryderyk-wiatrowski-ai-employee-os`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor
- `futurepedia-prompt-engineering`: anti_patterns_sourced, recognition_test, named_entity_floor
- `gabe-novotny-fitness-content-business`: anti_patterns_sourced, recognition_test, source_ledger
- `gary-vaynerchuk-attention`: anti_patterns_sourced, recognition_test, source_ledger
- `ghostwriting-voice-engine`: anti_patterns_sourced, recognition_test, source_ledger
- `gpt-image-2-director`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `grace-andrews-media-company`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `greg-hickman-service-scaling`: anti_patterns_sourced, recognition_test, source_ledger
- `greg-hoffman-brand-mastery`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `growth-ecosystems`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `harry-dry-copywriting`: anti_patterns_sourced, recognition_test, named_entity_floor
- `henrik-werdelin-portfolio-entrepreneurship`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `henry-shukman-contemplative-writing`: anti_patterns_sourced, recognition_test, source_ledger
- `higgsfield-creative-studio`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `how-i-write-os`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `jack-roberts-design-mastery`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `james-i-bond-brain-glue`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor
- `jasmin-alic-linkedin-growth`: anti_patterns_sourced, recognition_test, source_ledger
- `jay-hiette-coaching-positioning`: anti_patterns_sourced, recognition_test, source_ledger
- `jeremy-haynes-mindset-systems`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `jeremy-miner-identity-persuasion`: anti_patterns_sourced, recognition_test, workflow_contracts
- `jessica-jensen-platform-intelligence`: anti_patterns_sourced, recognition_test, source_ledger
- `jiang-xueqin-cognitive-autonomy`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `jim-oshaughnessy-philosopher-financier`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `joanna-wiebe-persuasion-mastery`: anti_patterns_sourced, recognition_test, source_ledger
- `joanna-wiebe-writing-careers`: anti_patterns_sourced, recognition_test, named_entity_floor
- `john-whiting-propaganda-machine`: anti_patterns_sourced, recognition_test
- `jonah-berger-contagious`: anti_patterns_sourced, recognition_test, source_ledger
- `jonathan-courtney-marketing`: anti_patterns_sourced, recognition_test, source_ledger
- `jonathan-franzen-storytelling`: anti_patterns_sourced, source_ledger, named_entity_floor
- `joscha-bach-consciousness`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `josh-kaufman-business-fundamentals`: anti_patterns_sourced, recognition_test, source_ledger
- `josh-sanders-linkedin-growth`: anti_patterns_sourced, recognition_test, source_ledger
- `joshua-smith-real-estate`: anti_patterns_sourced, recognition_test, source_ledger
- `jun-yuh-creator-vision`: anti_patterns_sourced, recognition_test, source_ledger
- `jun-yuh-personal-brand`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `justin-welsh-solopreneur`: anti_patterns_sourced, recognition_test, source_ledger
- `kallaway-addictive-storytelling`: anti_patterns_sourced, source_ledger, named_entity_floor
- `kallaway-ai-content-engine`: anti_patterns_sourced, recognition_test, source_ledger
- `kallaway-audience-obsession`: anti_patterns_sourced, recognition_test, source_ledger
- `kallaway-content-operating-system`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor, workflow_contracts
- `kallaway-content-psychology`: anti_patterns_sourced, recognition_test, workflow_contracts
- `kallaway-content-system`: anti_patterns_sourced, recognition_test, named_entity_floor, workflow_contracts
- `kallaway-word-mastery`: anti_patterns_sourced, recognition_test, source_ledger
- `kieran-flanagan-audience-intelligence`: anti_patterns_sourced, recognition_test, source_ledger
- `kieran-flanagan-content-engine`: anti_patterns_sourced, recognition_test, source_ledger
- `kieran-flanagan-content-ops`: anti_patterns_sourced, recognition_test, source_ledger
- `kittl-graphic-design`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `kj-rainey-copywriting`: anti_patterns_sourced, recognition_test, source_ledger
- `knowledge-architecture-studio`: anti_patterns_sourced, recognition_test, named_entity_floor
- `kobi-brown-educational-virality`: anti_patterns_sourced, recognition_test, workflow_contracts
- `kunal-shah-consumer-psychology`: anti_patterns_sourced, source_ledger
- `lamott-allen-really-real-writing`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor, workflow_contracts
- `lamott-craft`: anti_patterns_sourced, source_ledger
- `lance-yichao-context-engineering`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `lara-acosta-content-system`: anti_patterns_sourced, recognition_test, source_ledger **[capped A→B]**
- `liam-mley-ai-brain-builder`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `liam-ottley-linkedin-lead-magnet`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor
- `lindsay-ai-consulting`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `linkedin-2026-format-arbitrage`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `logan-kilpatrick-ai-studio`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `lucas-alpay-storytelling`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `luisa-zhou-coaching`: anti_patterns_sourced, recognition_test, source_ledger
- `luke-alexander-ai-business`: anti_patterns_sourced, recognition_test, source_ledger
- `luke-iha-client-mastery`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `luke-iha-creative-strategy`: anti_patterns_sourced, recognition_test, source_ledger
- `luke-iha-cross-domain`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `luke-iha-insight-vectors`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `luke-iha-million-dollar-mechanisms`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `luke-iha-proof-ladder`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger **[capped A→B]**
- `luke-iha-proof-mechanisms`: anti_patterns_sourced, recognition_test, named_entity_floor
- `luke-iha-unaware-ads`: anti_patterns_sourced, recognition_test, source_ledger
- `lulu-cheng-meservey-communications`: anti_patterns_sourced, source_ledger
- `made-to-stick-messaging`: anti_patterns_sourced, recognition_test, named_entity_floor
- `manus-ai-consulting`: anti_patterns_sourced, recognition_test, source_ledger
- `marc-andreessen-ai-thesis`: anti_patterns_sourced, recognition_test, source_ledger
- `maria-wendt-digital-products`: recognition_test, source_ledger
- `marisa-murgatroyd-course-design`: anti_patterns_sourced, recognition_test
- `mark-forsyth-rhetoric`: anti_patterns_sourced, recognition_test, source_ledger
- `mark-kashef-agent-orchestration`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `mark-kashef-ai-councils`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `mark-kashef-banana-squad`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `mark-kashef-claude-claw`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `mark-kashef-silver-platter-agentic-os`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `mark-kashef-visual-design`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `mark-manson-values-psychology`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `marketing-studio-director`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `matt-mcgarry-newsletters`: anti_patterns_sourced, recognition_test, source_ledger
- `matthew-lakajev-linkedin`: anti_patterns_sourced, recognition_test, source_ledger
- `matthew-volkwyn-copywriting`: anti_patterns_sourced, recognition_test, source_ledger
- `meg-heckman-buyer-trigger-os`: anti_patterns_sourced, recognition_test, workflow_contracts
- `michael-bernoff-identity-engineering`: anti_patterns_sourced, recognition_test, source_ledger
- `michael-connelly-vivid-writing`: anti_patterns_sourced, source_ledger, named_entity_floor
- `michael-israetel-hypertrophy`: anti_patterns_sourced, recognition_test, source_ledger
- `michael-margolis-user-research`: anti_patterns_sourced, recognition_test, source_ledger
- `mike-foutia-marketing-tools`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `mike-sherrard-realtor-branding`: anti_patterns_sourced, recognition_test, source_ledger
- `mitch-albom-writing-mastery`: anti_patterns_sourced, source_ledger, named_entity_floor
- `monk-ai-offer-architecture`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `nate-b-jones-agent-deployment-strategy`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `nate-b-jones-ai-taste-mastery`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `nate-b-jones-auto-improvement-loops`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `nate-b-jones-context-engineering`: anti_patterns_sourced, recognition_test, named_entity_floor, workflow_contracts
- `nate-b-jones-intent-engineering`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `nate-b-jones-orchestration-intelligence`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `nate-b-jones-trust-architecture`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `nate-herk-client-acquisition`: anti_patterns_sourced, recognition_test, source_ledger
- `nathan-gotch-ai-seo`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `nba-betting-edge`: anti_patterns_sourced, recognition_test, source_ledger
- `new-media-ghostwriting`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `new-media-kingmaker`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `nick-saraev-agentic-workflows`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `nick-saraev-bottleneck-thinking`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `nicolas-cole-client-acquisition`: anti_patterns_sourced, recognition_test, workflow_contracts
- `nicolas-cole-edan-writing-mechanics`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor
- `nicolas-cole-niche-positioning`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `nicolas-cole-nonfiction-value-architecture`: anti_patterns_sourced, recognition_test, named_entity_floor
- `nicolas-cole-sales-education-messaging`: anti_patterns_sourced, recognition_test, named_entity_floor
- `nicolas-cole-sentence-craft`: anti_patterns_sourced, source_ledger, named_entity_floor
- `nir-eyal-habit-design`: anti_patterns_sourced, recognition_test, source_ledger
- `noah-hawley-storytelling-mastery`: anti_patterns_sourced, source_ledger
- `ocean-vuong-perceptual-writing`: recognition_test, source_ledger
- `omar-eddaoudi`: recognition_test, source_ledger
- `omar-eddaoudi-premium-ads`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `omar-eddaoudi-scaling-ops`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `omar-eltakrori`: anti_patterns_sourced, recognition_test, workflow_contracts
- `oren-brand-archetypes`: anti_patterns_sourced, recognition_test, workflow_contracts
- `oren-content-team-architecture`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `oren-luxury-psychology`: anti_patterns_sourced, source_ledger, named_entity_floor
- `oren-one-person-ai-marketer`: anti_patterns_sourced, recognition_test, source_ledger
- `oren-operational-systems`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `oren-repositioning`: anti_patterns_sourced, source_ledger, named_entity_floor
- `oren-taste-development`: anti_patterns_sourced, source_ledger
- `oscar-hoglund-sound-storytelling`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `packy-mccormick-writing`: anti_patterns_sourced, recognition_test, source_ledger
- `pat-flynn-passive-income`: anti_patterns_sourced, recognition_test, source_ledger
- `patrick-dang-online-business`: anti_patterns_sourced, recognition_test, source_ledger
- `patrick-debois-cdlc`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `paul-james-ai-automation`: anti_patterns_sourced, recognition_test, named_entity_floor
- `persuasion-story-code`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor, workflow_contracts
- `phil-m-jones-conversational-influence`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor
- `pj-accetturo-ai-video`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `prediction-market-ai-event-analysis`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `prediction-market-making`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `prediction-market-risk-management`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `prediction-market-weather-trading`: anti_patterns_sourced, recognition_test, workflow_contracts
- `product-design-build`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `prosperity-coach-system`: anti_patterns_sourced, recognition_test, source_ledger
- `rachel-woods-ai-operations`: anti_patterns_sourced, recognition_test, source_ledger
- `rafa-conde-fourth-wall-experience-os`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor
- `rafa-conde-memorable-product-design`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor
- `re-compliance-pack`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `reid-hoffman-ai-strategy`: anti_patterns_sourced, recognition_test, source_ledger
- `robert-greene-power-mastery`: anti_patterns_sourced, recognition_test, source_ledger
- `robert-mack-comedy-writing`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `rory-sutherland-marketing`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `ross-mckay-premium-at-scale`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `ross-minchev-digital-products`: anti_patterns_sourced, recognition_test, source_ledger
- `russell-brunson-funnels`: anti_patterns_sourced, recognition_test
- `sabri-suby-ai-advertising`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `sabrina-ramonov-ai-monetization`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `sam-goddard-media-scaling`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `sam-parr-copywriting`: anti_patterns_sourced, recognition_test
- `sam-parr-copywriting-mechanics`: anti_patterns_sourced, verbatim_exemplars, recognition_test, workflow_contracts
- `sam-parr-taste-acquisition`: anti_patterns_sourced, recognition_test, source_ledger
- `samuel-thompson-product-launch`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `sarah-levinger-ad-psychology`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor
- `satori-graphics`: anti_patterns_sourced, recognition_test, named_entity_floor
- `sean-kochel-ai-business`: anti_patterns_sourced, recognition_test, source_ledger
- `sean-kochel-design-first-build`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `sean-mabry-voice-mastery`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `sean-macintyre-persuasion-philosophy`: anti_patterns_sourced, recognition_test
- `seena-rez-tiktok-commerce`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `self-evolving-systems`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor
- `semantic-document-library-os`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `seth-godin-brand`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `seth-godin-ideavirus`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `seth-godin-philosophy`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `shaan-puri-storytelling`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `shan-hanif-audience-monetization`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `sharran-srivatsaa-scaling`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `sherwin-wu-ai-engineering`: anti_patterns_sourced, recognition_test
- `simon-intellectual-library-os`: anti_patterns_sourced, recognition_test
- `sky-tan-format-engine`: anti_patterns_sourced, recognition_test, named_entity_floor
- `soowei-consulting-leverage`: anti_patterns_sourced, recognition_test, source_ledger
- `steven-kotler-flow-performance`: anti_patterns_sourced, recognition_test, source_ledger
- `steven-pressfield-narrative-mastery`: anti_patterns_sourced, recognition_test, source_ledger
- `steven-young-consciousness`: anti_patterns_sourced, recognition_test, source_ledger
- `stockton-walbeck-lead-magnets`: anti_patterns_sourced, recognition_test, source_ledger
- `story-bible-builder`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `story-compass`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `strength-conditioning-os`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `sunny-lenarduzzi-youtube`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `supercomputer`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `sweat-equity-speedrun-social-os`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `taki-moore-lifestyle-business`: anti_patterns_sourced, recognition_test, source_ledger, workflow_contracts
- `tao-prompts-ai-video`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `taylor-welch-wealthy-consultant`: anti_patterns_sourced, recognition_test, source_ledger
- `tess-barclay-social-content`: anti_patterns_sourced, recognition_test, source_ledger
- `thrivecart-digital-products`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `tim-danilov-niche-bending`: anti_patterns_sourced, recognition_test, source_ledger
- `tobi-lutke-business-leadership`: anti_patterns_sourced, recognition_test, source_ledger
- `tobias-allen-marketing-mastery`: anti_patterns_sourced, recognition_test, source_ledger
- `tom-noske-content-creation`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `tom-noske-personal-brand`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `tom-segura-comedy-storytelling`: anti_patterns_sourced, recognition_test
- `tyler-denk-audience-monetization`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger
- `velocity-scaling`: anti_patterns_sourced, recognition_test, source_ledger
- `verticalize`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `vince-nijhof-dtc-operator-system`: anti_patterns_sourced, recognition_test **[capped A→B]**
- `voice-os`: anti_patterns_sourced, verbatim_exemplars, recognition_test, source_ledger, named_entity_floor, workflow_contracts
- `wordsatscale-seo-ranking`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `wright-thompson-mastery`: anti_patterns_sourced, recognition_test, source_ledger
- `writing-depth-layer`: anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor
- `yann-martel-storytelling-mastery`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor
- `youtube-video-context-analysis`: anti_patterns_sourced, verbatim_exemplars, recognition_test, named_entity_floor, workflow_contracts
- `yuri-elkaim-health-coaching-business`: anti_patterns_sourced, recognition_test, source_ledger

## Craft Standard Flags (`directives/skill-craft-standard.md` — advisory, not tier-affecting)

338 skills have at least one cheap deterministic gap:

- `_tmp_audit_diandra`: no genius.md, zero workflows
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
- `banana-pro-director`: no genius.md, zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `ben-watkins-storytelling`: frontmatter missing when_to_use
- `benjamin-hardy-identity`: frontmatter missing domain, frontmatter missing when_to_use
- `bill-browder-high-stakes-narrative`: frontmatter missing when_to_use
- `bitbranding-fashion-shopify`: frontmatter missing when_to_use
- `bond-halbert-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `boris-claude-code`: frontmatter missing domain, frontmatter missing when_to_use
- `brad-bonanno-explainer-architecture`: frontmatter missing when_to_use
- `brand-operating-system`: frontmatter missing domain, frontmatter missing when_to_use, hardcoded score pattern in 07-wrap.md
- `brandon-jacoby-taste-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `brendan-kane-viral-strategy`: frontmatter missing domain, frontmatter missing when_to_use
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
- `cinema-worldbuilder-pro`: no genius.md, zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `cinematic-documentary`: frontmatter missing when_to_use
- `coaching-business-os`: frontmatter missing domain, frontmatter missing when_to_use
- `cognitive-engagement-optimizer`: frontmatter missing when_to_use
- `context-profile-architect`: frontmatter missing domain, frontmatter missing when_to_use
- `corey-mcclain-persona-engineering`: frontmatter missing when_to_use
- `craig-clemens-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `creative-campaign-strategy`: frontmatter missing when_to_use
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
- `david-bayer-elite-communication`: frontmatter missing domain, frontmatter missing when_to_use
- `david-deutsch-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `david-mcraney-belief-change`: frontmatter missing domain, frontmatter missing when_to_use
- `david-perell-writing`: frontmatter missing domain, frontmatter missing when_to_use
- `david-placek-naming`: frontmatter missing when_to_use
- `deliberate`: zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `deya-business-systems`: frontmatter missing domain, frontmatter missing when_to_use
- `diandra-escobar-linkedin-growth`: frontmatter missing when_to_use
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
- `expert-assembly-os`: no genius.md, zero workflows, frontmatter missing when_to_use
- `extract-mastery`: frontmatter missing when_to_use
- `fantastic-posters`: frontmatter missing domain, frontmatter missing when_to_use
- `fareed-zakaria-writing-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `forge-os`: no genius.md, zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `fraser-cottrell-paid-ads`: frontmatter missing domain, frontmatter missing when_to_use
- `fresh-voice-system`: frontmatter missing domain, frontmatter missing when_to_use
- `fryderyk-wiatrowski-ai-employee-os`: no genius.md, frontmatter missing domain, frontmatter missing when_to_use
- `futurepedia-prompt-engineering`: frontmatter missing domain, frontmatter missing when_to_use
- `gabe-novotny-fitness-content-business`: frontmatter missing domain, frontmatter missing when_to_use
- `gary-vaynerchuk-attention`: frontmatter missing domain, frontmatter missing when_to_use
- `ghostwriting-voice-engine`: frontmatter missing domain, frontmatter missing when_to_use
- `gpt-image-2-director`: no genius.md, zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `grace-andrews-media-company`: frontmatter missing when_to_use
- `greg-hickman-service-scaling`: frontmatter missing domain, frontmatter missing when_to_use
- `greg-hoffman-brand-mastery`: frontmatter missing when_to_use
- `growth-ecosystems`: frontmatter missing when_to_use
- `harry-dry-copywriting`: frontmatter missing domain, frontmatter missing when_to_use
- `henrik-werdelin-portfolio-entrepreneurship`: frontmatter missing domain, frontmatter missing when_to_use
- `henry-shukman-contemplative-writing`: frontmatter missing when_to_use
- `higgsfield-creative-studio`: no genius.md, zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `how-i-write-os`: zero workflows, frontmatter missing when_to_use
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
- `kallaway-content-operating-system`: no genius.md, frontmatter missing when_to_use
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
- `luke-iha-cross-domain`: no genius.md, frontmatter missing when_to_use
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
- `mark-kashef-silver-platter-agentic-os`: no genius.md, zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `mark-kashef-visual-design`: frontmatter missing domain, frontmatter missing when_to_use, hardcoded score pattern in 05-visual-taste-gate.md
- `mark-manson-values-psychology`: frontmatter missing domain, frontmatter missing when_to_use
- `marketing-studio-director`: no genius.md, zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `matt-mcgarry-newsletters`: frontmatter missing domain, frontmatter missing when_to_use
- `matthew-lakajev-linkedin`: frontmatter missing domain, frontmatter missing when_to_use
- `matthew-volkwyn-copywriting`: frontmatter missing domain, frontmatter missing when_to_use, hardcoded score pattern in 01-audit-copy.md
- `meg-heckman-buyer-trigger-os`: frontmatter missing when_to_use
- `michael-bernoff-identity-engineering`: frontmatter missing domain, frontmatter missing when_to_use
- `michael-connelly-vivid-writing`: frontmatter missing when_to_use, hardcoded score pattern in momentum-audit.md
- `michael-israetel-hypertrophy`: frontmatter missing domain, frontmatter missing when_to_use
- `michael-margolis-user-research`: frontmatter missing domain, frontmatter missing when_to_use
- `mike-foutia-marketing-tools`: frontmatter missing when_to_use
- `mike-sherrard-realtor-branding`: frontmatter missing domain, frontmatter missing when_to_use
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
- `new-media-ghostwriting`: no genius.md, frontmatter missing when_to_use
- `new-media-kingmaker`: no genius.md, frontmatter missing when_to_use
- `nick-saraev-agentic-workflows`: frontmatter missing domain, frontmatter missing when_to_use
- `nick-saraev-bottleneck-thinking`: frontmatter missing domain, frontmatter missing when_to_use
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
- `oren-brand-archetypes`: zero workflows, frontmatter missing when_to_use
- `oren-content-team-architecture`: frontmatter missing domain, frontmatter missing when_to_use
- `oren-identity-brand-os`: frontmatter missing domain, frontmatter missing when_to_use
- `oren-luxury-psychology`: frontmatter missing when_to_use
- `oren-one-person-ai-marketer`: frontmatter missing when_to_use
- `oren-operational-systems`: frontmatter missing domain, frontmatter missing when_to_use
- `oren-repositioning`: frontmatter missing domain, frontmatter missing when_to_use
- `oren-taste-development`: frontmatter missing when_to_use
- `oscar-hoglund-sound-storytelling`: frontmatter missing domain, frontmatter missing when_to_use
- `packy-mccormick-writing`: frontmatter missing domain, frontmatter missing when_to_use
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
- `reid-hoffman-ai-strategy`: frontmatter missing domain, frontmatter missing when_to_use
- `robert-greene-power-mastery`: frontmatter missing domain, frontmatter missing when_to_use
- `robert-mack-comedy-writing`: frontmatter missing when_to_use
- `rory-sutherland-marketing`: frontmatter missing domain, frontmatter missing when_to_use
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
- `story-bible-builder`: no genius.md, zero workflows, frontmatter missing domain, frontmatter missing when_to_use
- `story-compass`: frontmatter missing when_to_use
- `strength-conditioning-os`: frontmatter missing when_to_use
- `sunny-lenarduzzi-youtube`: frontmatter missing domain, frontmatter missing when_to_use
- `supercomputer`: zero workflows, frontmatter missing domain, frontmatter missing when_to_use
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
- `verticalize`: no genius.md, zero workflows, frontmatter missing when_to_use
- `vince-nijhof-dtc-operator-system`: frontmatter missing when_to_use
- `voice-os`: no genius.md, zero workflows, frontmatter missing when_to_use
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

## Tier A (11 skills)

These are the system's strongest skills. Prioritize for promotion, ground-truth benchmarking, and revenue tracking.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `adam-sandler-second-brain-gtm` | 8 | ✓ | 1 (avg 8.33) | ✓ | full structure (8 workflows + genius.md); trace avg 8.33 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `andrew-stanton-audience-engineering` | 21 | ✓ | 4 (avg 7.52) | ✓ | full structure (21 workflows + genius.md); trace avg 7.52 ≥ 7.5 (4 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `ben-watkins-storytelling` | 18 | ✓ | 1 (avg 8.33) | ✓ | full structure (18 workflows + genius.md); trace avg 8.33 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `jenny-hoyos-shorts` | 13 | ✓ | 5 (avg 8.67) |  | full structure (13 workflows + genius.md); trace avg 8.67 ≥ 7.5 (5 traces) |
| `jeremy-haynes-cold-offer` | 13 | ✓ | 2 (avg 8.33) | ✓ | full structure (13 workflows + genius.md); trace avg 8.33 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `kallaway-illusion-of-novelty` | 14 | ✓ | 6 (avg 7.6) | ✓ | full structure (14 workflows + genius.md); trace avg 7.6 ≥ 7.5 (6 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-copy-blocks` | 14 | ✓ | 18 (avg 7.62) | ✓ | full structure (14 workflows + genius.md); trace avg 7.62 ≥ 7.5 (18 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-vicious-hooks` | 14 | ✓ | 2 (avg 8.84) | ✓ | full structure (14 workflows + genius.md); trace avg 8.84 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-vsl-leads` | 4 | ✓ | 3 (avg 7.72) | ✓ | full structure (4 workflows + genius.md); trace avg 7.72 ≥ 7.5 (3 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `seth-godin-marketing-mind` | 15 | ✓ | 2 (avg 8.33) | ✓ | full structure (15 workflows + genius.md); trace avg 8.33 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `tommy-clark-linkedin-growth` | 6 | ✓ | 1 (avg 8.33) | ✓ | full structure (6 workflows + genius.md); trace avg 8.33 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |

## Tier B (229 skills)

Solid skills that are working. Candidates for B→A promotion via genius.md enrichment or workflow expansion.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `adam-enfroy-affiliate-marketing` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ai-chris-lee-zero-testimonial-sales` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alen-sultanic-copywriting` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-content-science` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-copper-creative-strategy` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-hormozi-business` | 3 | ✓ | 1 (avg 7.25) | ✓ | 1 traces, avg 7.25 |
| `alex-m-smith-natural-strategy` | 5 | ✓ | 1 (avg 7.25) | ✓ | 1 traces, avg 7.25 |
| `alex-myatt-creative-engine` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `alex-suzuki-digital-product-revenue-os` | 17 | ✓ | 19 (avg 6.96) | ✓ | 19 traces, avg 6.96 |
| `ali-abdaal-action-bias` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `andrew-dun-vibe-consulting` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `andrew-lane-design-systems` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `andrew-wilkinson-ai-entrepreneurship` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `andy-lo-premium-websites` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `april-dunford-positioning` | 16 | ✓ | - | ✓ | full structure (16 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ash-maurya-founder-systems` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ash-maurya-lean-metrics` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `attention-hijack-hooks` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `authority-hacker-ai-social-media` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `bond-halbert-copywriting` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `boris-claude-code` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `brand-operating-system` | 7 | ✓ | 5 (avg 7.6) | ✓ | full structure (7 workflows + genius.md); trace avg 7.6 ≥ 7.5 (5 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `brock-johnson-shareworthy-content` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `business-intelligence-audit` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `caleb-ralston-personal-brand` | 11 | ✓ | - | ✓ | full structure (11 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `cardinal-mason-ai-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `chase-hughes-context-engineering` | 10 | ✓ | 3 (avg 7.25) |  | 3 traces, avg 7.25 |
| `chief-of-staff-os` | 4 | ✓ | 5 (avg 7.47) |  | 5 traces, avg 7.47 |
| `chris-cimorelli-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `chris-do-design-business` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `cinematic-documentary` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `claim-safe-health-marketing` | 5 | ✓ | 5 (avg 7.02) | ✓ | 5 traces, avg 7.02 |
| `coaching-business-os` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `context-profile-architect` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `creative-campaign-strategy` | 17 | ✓ | - | ✓ | full structure (17 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dai-media-consumer-posture` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-bolton-coaching-offers` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-koe-ai-leverage` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-koe-multipassionate-mastery` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-martell-business-scaling` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dan-wang-literary-analysis` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-pink-writing-structure` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-priestley-24-assets-os` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-priestley-oversubscribed` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-priestley-sll-engine` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `daniel-thrasher-affiliate` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `darrel-wilson-ai-affiliate` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `darrel-wilson-ai-monetization` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-bayer-elite-communication` | 3 | ✓ | 3 (avg 7.25) | ✓ | 3 traces, avg 7.25 |
| `david-deutsch-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-mcraney-belief-change` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-perell-writing` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `david-placek-naming` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `deliberate` | 0 | ✓ | 1 (avg 7.08) |  | has genius.md but <3 workflows; 1 traces, avg 7.08 |
| `diandra-escobar-linkedin-growth` | 22 | ✓ | 3 (avg 7.25) | ✓ | 3 traces, avg 7.25 |
| `dom-iacovone-multi-company-operator` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `donald-miller-business-growth` | 7 | ✓ | 1 (avg 7.25) | ✓ | 1 traces, avg 7.25 |
| `donald-miller-cognitive-load` | 8 | ✓ | 1 (avg 7.25) | ✓ | 1 traces, avg 7.25 |
| `donald-miller-culture-turnaround` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `donald-miller-messaging-evolution` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `donald-miller-storybrand` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `dr-k-consciousness` | 11 | ✓ | 1 (avg 7.25) |  | 1 traces, avg 7.25 |
| `dr-kriukow-humanization` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `enrico-incarnati-instagram-realestate` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `eric-roth-screenwriting-mastery` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `eric-roth-writing-mastery` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `erica-mallet-brand-magnetism` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ethan-smith-aeo` | 3 | ✓ | 2 (avg 6.71) | ✓ | 2 traces, avg 6.71 |
| `evan-spiegel-distribution-architecture` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `extract-mastery` | 3 | ✓ | 7 (avg 7.81) | ✓ | full structure (3 workflows + genius.md); trace avg 7.81 ≥ 7.5 (7 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `fantastic-posters` | 14 | ✓ | 1 (avg 8.67) | ✓ | full structure (14 workflows + genius.md); trace avg 8.67 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `fareed-zakaria-writing-mastery` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `fresh-voice-system` | 3 | ✓ | 3 (avg 7.25) | ✓ | 3 traces, avg 7.25 |
| `futurepedia-prompt-engineering` | 6 | ✓ | 6 (avg 7.25) | ✓ | 6 traces, avg 7.25 |
| `geoff-woods-ai-thought-partner` | 16 | ✓ | - | ✓ | full structure (16 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `grace-andrews-media-company` | 18 | ✓ | - | ✓ | full structure (18 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `growth-ecosystems` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `harry-dry-copywriting` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `how-i-write-os` | 0 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `james-i-bond-brain-glue` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jasmin-alic-linkedin-growth` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jason-fladlien-marketing` | 31 | ✓ | 1 (avg 7.25) | ✓ | 1 traces, avg 7.25 |
| `jen-santulan-listing-content` | 3 | ✓ | 9 (avg 7.13) |  | 9 traces, avg 7.13 |
| `jeremy-haynes-mindset-systems` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jeremy-miner-identity-persuasion` | 11 | ✓ | - | ✓ | full structure (11 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jim-oshaughnessy-philosopher-financier` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joanna-wiebe-persuasion-mastery` | 11 | ✓ | - | ✓ | full structure (11 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joanna-wiebe-writing-careers` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `john-whiting-propaganda-machine` | 19 | ✓ | 2 (avg 7.25) | ✓ | 2 traces, avg 7.25 |
| `jonathan-courtney-marketing` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `jonathan-franzen-storytelling` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joscha-bach-consciousness` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `josh-kaufman-business-fundamentals` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `josh-sanders-linkedin-growth` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `joshua-smith-real-estate` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jun-yuh-creator-vision` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `jun-yuh-personal-brand` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `justin-welsh-solopreneur` | 3 | ✓ | 1 (avg 7.25) |  | 1 traces, avg 7.25 |
| `kallaway-addictive-storytelling` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-ai-content-engine` | 5 | ✓ | 1 (avg 6.08) | ✓ | 1 traces, avg 6.08 |
| `kallaway-audience-obsession` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-content-psychology` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-content-system` | 9 | ✓ | - | ✓ | full structure (9 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-social-commerce` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kallaway-word-mastery` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kittl-graphic-design` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `knowledge-architecture-studio` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `kobi-brown-educational-virality` | 10 | ✓ | 4 (avg 7.23) | ✓ | 4 traces, avg 7.23 |
| `lance-yichao-context-engineering` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lara-acosta-content-system` | 4 | ✓ | 1 (avg 9.0) | ✓ | full structure (4 workflows + genius.md); trace avg 9.0 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `lara-acosta-linkedin-growth` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lara-acosta-linkedin-mastery` | 9 | ✓ | 7 (avg 7.18) | ✓ | 7 traces, avg 7.18 |
| `lindsay-ai-consulting` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `linkedin-2026-format-arbitrage` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `logan-kilpatrick-ai-studio` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lucas-alpay-storytelling` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-alexander-ai-business` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-avatar-machine` | 13 | ✓ | 3 (avg 7.25) | ✓ | 3 traces, avg 7.25 |
| `luke-iha-client-mastery` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-creative-strategy` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-cross-domain` | 4 |  | - | ✓ | 4 workflows but no genius.md; cross-referenced (no trace data) |
| `luke-iha-insight-vectors` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-million-dollar-mechanisms` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-proof-ladder` | 14 | ✓ | 2 (avg 8.84) | ✓ | full structure (14 workflows + genius.md); trace avg 8.84 ≥ 7.5 (2 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `luke-iha-proof-mechanisms` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `luke-iha-unaware-ads` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `lulu-cheng-meservey-communications` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `manus-ai-consulting` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `marc-andreessen-ai-thesis` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `maria-wendt-digital-products` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-forsyth-rhetoric` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-agent-orchestration` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-ai-councils` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-banana-squad` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-claude-claw` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-visual-design` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-kashef-wargame-os` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mark-manson-values-psychology` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `matt-mcgarry-newsletters` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `meg-heckman-buyer-trigger-os` | 12 | ✓ | 5 (avg 7.25) |  | 5 traces, avg 7.25 |
| `michael-bernoff-identity-engineering` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `michael-connelly-vivid-writing` | 16 | ✓ | - | ✓ | full structure (16 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `michael-israetel-hypertrophy` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `michael-margolis-user-research` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mike-foutia-marketing-tools` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `mitch-albom-writing-mastery` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `monk-ai-offer-architecture` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-b-jones-agent-deployment-strategy` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `nate-b-jones-ai-taste-mastery` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-b-jones-auto-improvement-loops` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-b-jones-context-engineering` | 6 | ✓ | 2 (avg 7.21) | ✓ | 2 traces, avg 7.21 |
| `nate-b-jones-intent-engineering` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nate-b-jones-orchestration-intelligence` | 12 | ✓ | 3 (avg 6.89) | ✓ | 3 traces, avg 6.89 |
| `nate-b-jones-trust-architecture` | 5 | ✓ | 1 (avg 7.25) | ✓ | 1 traces, avg 7.25 |
| `nate-herk-client-acquisition` | 1 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `nathan-gotch-ai-seo` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `new-media-kingmaker` | 3 |  | - | ✓ | 3 workflows but no genius.md; cross-referenced (no trace data) |
| `nick-saraev-agentic-workflows` | 7 | ✓ | - | ✓ | full structure (7 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nick-saraev-bottleneck-thinking` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-client-acquisition` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-digital-products` | 3 | ✓ | 1 (avg 7.25) | ✓ | 1 traces, avg 7.25 |
| `nicolas-cole-edan-writing-mechanics` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `nicolas-cole-newsletter-flywheel` | 17 | ✓ | 4 (avg 6.98) | ✓ | 4 traces, avg 6.98 |
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
| `oren-brand-archetypes` | 0 | ✓ | 1 (avg 7.25) |  | has genius.md but <3 workflows; 1 traces, avg 7.25 |
| `oren-operational-systems` | 3 | ✓ | 9 (avg 6.1) |  | 9 traces, avg 6.1 |
| `oscar-hoglund-sound-storytelling` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `pat-flynn-passive-income` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `paul-harding-lyric-prose` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `paul-james-ai-automation` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `persuasion-story-code` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `phil-m-jones-conversational-influence` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `pj-accetturo-ai-video` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `product-design-build` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `rachel-woods-ai-operations` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `robert-mack-comedy-writing` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `rory-sutherland-marketing` | 20 | ✓ | - | ✓ | full structure (20 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `ross-mckay-premium-at-scale` | 1 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `ross-minchev-digital-products` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sabri-suby-ai-advertising` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sabrina-ramonov-ai-monetization` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sam-goddard-media-scaling` | 5 | ✓ | - | ✓ | full structure (5 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sam-parr-copywriting` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sam-parr-copywriting-mechanics` | 14 | ✓ | - | ✓ | full structure (14 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sam-parr-taste-acquisition` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `samuel-thompson-product-launch` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sean-kochel-ai-business` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sean-kochel-design-first-build` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `seena-rez-tiktok-commerce` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `self-evolving-systems` | 1 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `semantic-document-library-os` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `seth-godin-brand` | 10 | ✓ | - | ✓ | full structure (10 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `seth-godin-ideavirus` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `seth-godin-philosophy` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `shaan-puri-storytelling` | 6 | ✓ | - | ✓ | full structure (6 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `shan-hanif-audience-monetization` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `sherwin-wu-ai-engineering` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `sky-tan-format-engine` | 12 | ✓ | 2 (avg 7.25) |  | 2 traces, avg 7.25 |
| `stefan-georgi-dopamine-copy` | 12 | ✓ | 2 (avg 7.25) | ✓ | 2 traces, avg 7.25 |
| `steven-kotler-flow-performance` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `steven-pressfield-narrative-mastery` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `steven-young-consciousness` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `stockton-walbeck-lead-magnets` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `story-compass` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `strength-conditioning-os` | 2 | ✓ | 5 (avg 8.11) |  | has genius.md but <3 workflows; 5 traces, avg 8.11 |
| `supercomputer` | 0 | ✓ | 7 (avg 6.97) | ✓ | has genius.md but <3 workflows; 7 traces, avg 6.97 |
| `tao-prompts-ai-video` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `tim-danilov-niche-bending` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tobi-lutke-business-leadership` | 3 | ✓ | - | ✓ | full structure (3 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tobias-allen-marketing-mastery` | 3 | ✓ | 1 (avg 7.25) | ✓ | 1 traces, avg 7.25 |
| `tom-noske-content-creation` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-noske-personal-brand` | 4 | ✓ | - | ✓ | full structure (4 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tom-segura-comedy-storytelling` | 12 | ✓ | - | ✓ | full structure (12 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `tyler-denk-audience-monetization` | 2 | ✓ | - | ✓ | has genius.md but <3 workflows; cross-referenced (no trace data) |
| `velocity-scaling` | 18 | ✓ | - | ✓ | full structure (18 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `vince-nijhof-dtc-operator-system` | 14 | ✓ | 1 (avg 7.5) | ✓ | full structure (14 workflows + genius.md); trace avg 7.5 ≥ 7.5 (1 traces); cross-referenced from CLAUDE/COUNCIL/router |
| `ward-farnsworth-rhetorical-mastery` | 15 | ✓ | - | ✓ | full structure (15 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `wright-thompson-mastery` | 13 | ✓ | - | ✓ | full structure (13 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |
| `writing-depth-layer` | 12 | ✓ | 1 (avg 7.25) | ✓ | 1 traces, avg 7.25 |
| `youtube-video-context-analysis` | 8 | ✓ | - | ✓ | full structure (8 workflows + genius.md); cross-referenced but no trace evidence yet — promote to A on first ≥7.5 trace |

## Tier REVIEW (99 skills)

Heuristics conflict — these need human eyes before tier finalization.

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `ai-carousel-content-engine` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `alan-aragon-nutrition` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `andreessen-horowitz-new-media` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `andy-galpin-training-intelligence` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `benjamin-hardy-identity` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `bill-browder-high-stakes-narrative` | 13 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `bitbranding-fashion-shopify` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `brad-bonanno-explainer-architecture` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `brandon-jacoby-taste-mastery` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `brendan-kane-viral-strategy` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `chase-hughes-conversational-influence` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `cheri-tree-bank-buyology` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `cinema-worldbuilder-pro` | 0 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `cognitive-engagement-optimizer` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `corey-mcclain-persona-engineering` | 20 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `craig-clemens-copywriting` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `dakota-content-design` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `damon-cart-nlp` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `dara-denney-meta-ads` | 17 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `deya-business-systems` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `eugene-teo-training` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `expert-assembly-os` | 0 |  | 4 (avg 8.42) | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `forge-os` | 0 |  | 4 (avg 8.58) | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `fraser-cottrell-paid-ads` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `gabe-novotny-fitness-content-business` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `gary-vaynerchuk-attention` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `ghostwriting-voice-engine` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `gpt-image-2-director` | 0 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `greg-hickman-service-scaling` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `greg-hoffman-brand-mastery` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `henrik-werdelin-portfolio-entrepreneurship` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `henry-shukman-contemplative-writing` | 13 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jack-roberts-design-mastery` | 15 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jay-hiette-coaching-positioning` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jessica-jensen-platform-intelligence` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jiang-xueqin-cognitive-autonomy` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `joey-cinema-os` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `jonah-berger-contagious` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kallaway-content-operating-system` | 1 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `kieran-flanagan-audience-intelligence` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kieran-flanagan-content-engine` | 8 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kieran-flanagan-content-ops` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kj-rainey-copywriting` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `kunal-shah-consumer-psychology` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `lamott-allen-really-real-writing` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `lamott-craft` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `liam-mley-ai-brain-builder` | 5 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `liam-ottley-linkedin-lead-magnet` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `luisa-zhou-coaching` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `made-to-stick-messaging` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `marisa-murgatroyd-course-design` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `mark-kashef-silver-platter-agentic-os` | 0 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `marketing-studio-director` | 0 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `matthew-lakajev-linkedin` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `matthew-volkwyn-copywriting` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `mike-sherrard-realtor-branding` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `nba-betting-edge` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `new-media-ghostwriting` | 1 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `nir-eyal-habit-design` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-content-team-architecture` | 15 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-identity-brand-os` | 14 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-luxury-psychology` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-one-person-ai-marketer` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-repositioning` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `oren-taste-development` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `packy-mccormick-writing` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `patrick-dang-online-business` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `patrick-debois-cdlc` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-ai-event-analysis` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-making` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-risk-management` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prediction-market-weather-trading` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `prosperity-coach-system` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `rafa-conde-fourth-wall-experience-os` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `rafa-conde-memorable-product-design` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `re-compliance-pack` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `reid-hoffman-ai-strategy` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `robert-greene-power-mastery` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `russell-brunson-funnels` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sarah-levinger-ad-psychology` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `satori-graphics` | 20 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sean-dollwet-kdp-publishing` | 10 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sean-mabry-voice-mastery` | 1 | ✓ | - |  | partial structure (intentional but unused) — review priority |
| `sean-macintyre-persuasion-philosophy` | 17 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sharran-srivatsaa-scaling` | 7 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `simon-intellectual-library-os` | 15 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `soowei-consulting-leverage` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `story-bible-builder` | 0 |  | - | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `sunny-lenarduzzi-youtube` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `susan-orlean-narrative-nonfiction` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `sweat-equity-speedrun-social-os` | 9 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `taki-moore-lifestyle-business` | 6 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `taylor-welch-wealthy-consultant` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `tess-barclay-social-content` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `thrivecart-digital-products` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `voice-os` | 0 |  | 3 (avg 6.75) | ✓ | minimal structure but used — enrich with genius.md/workflows |
| `wordsatscale-seo-ranking` | 4 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `yann-martel-storytelling-mastery` | 12 | ✓ | - |  | full structure but never used (no traces, no cross-references) |
| `yuri-elkaim-health-coaching-business` | 3 | ✓ | - |  | full structure but never used (no traces, no cross-references) |

## Tier C (5 skills)

Archive candidates. Low evidence of value. **Do not delete — move to `_archive/skills/` for provenance.** Review individually before archiving (some may be load-bearing user domain skills).

| Skill | Workflows | Genius | Traces | Cross-ref | Reasoning |
|---|---|---|---|---|---|
| `_tmp_audit_diandra` | 0 |  | - |  | MISSING SKILL.md — likely orphan or backup folder |
| `banana-pro-director` | 0 |  | - |  | minimal structure (SKILL.md only) AND no traces AND no cross-references |
| `fryderyk-wiatrowski-ai-employee-os` | 1 |  | - |  | minimal structure (SKILL.md only) AND no traces AND no cross-references |
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
| `creative-direction` | 0 | ✓ | 8 (avg 6.42) | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `design-md` | 7 | ✓ | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `doc-coauthoring` | 0 |  | - | ✓ | system/Anthropic utility skill — not graded against expert rubric |
| `docx` | 0 |  | - |  | system/Anthropic utility skill — not graded against expert rubric |
| `frontend-design` | 0 |  | 1 (avg 8.33) |  | system/Anthropic utility skill — not graded against expert rubric |
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
| `swarm-commander` | 0 |  | 3 (avg 8.56) |  | system/Anthropic utility skill — not graded against expert rubric |
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

Machine-readable records: `evolution_store/skill_audit_2026-07-17.jsonl`
