#!/usr/bin/env python3
"""
Expert Router — Intelligent expert lookup across 96 agents and 15 domains.

Instead of loading the 752-line DOMAIN_REGISTRY.md (7,500+ tokens) into context,
this script provides fast problem-signature → expert routing.

Usage:
    python3 execution/expert_router.py route "write a sales page for my coaching offer"
    python3 execution/expert_router.py route "grow my linkedin audience"
    python3 execution/expert_router.py domain "copywriting"
    python3 execution/expert_router.py expert "luke-iha"
    python3 execution/expert_router.py compounds "product launch with paid ads"
    python3 execution/expert_router.py stats
    python3 execution/expert_router.py domains
"""

import sys
import argparse
from collections import defaultdict

# ─────────────────────────────────────────────────────────
# DOMAIN REGISTRY — Compressed from DOMAIN_REGISTRY.md
# 96 experts across 15 domains
# ─────────────────────────────────────────────────────────

EXPERTS = {
    # Domain 1: Copywriting (Conversion & Sales)
    "harry-dry":        {"domain": "copywriting", "owns": "evaluation", "use": "Auditing copy, Three Rules Test, rewrite discipline", "signals": ["audit", "evaluate", "copy review", "three rules", "rewrite"]},
    "cardinal-mason":   {"domain": "copywriting", "owns": "conversion", "use": "Sales pages, emails, client delivery, business building", "signals": ["sales page", "email sequence", "conversion", "funnel copy"]},
    "alen-sultanic":    {"domain": "copywriting", "owns": "long-form", "use": "Sales letters, VSLs, sophisticated persuasion", "signals": ["vsl", "sales letter", "long-form copy", "sophisticated", "premium long"]},
    "nicolas-cole":     {"domain": "copywriting", "owns": "sentence-craft", "use": "Rhythm, readability, sentence-level polish, digital products", "signals": ["sentence", "rhythm", "readability", "polish", "headline"]},
    "mitch-albom":      {"domain": "copywriting", "owns": "emotional/literary", "use": "Premium narrative, emotion-first, storytelling copy", "signals": ["emotional", "literary", "premium narrative", "story-driven copy"]},
    "bond-halbert":     {"domain": "copywriting", "owns": "direct-response", "use": "Market language excavation, velocity optimization, four-reader types", "signals": ["direct response", "market language", "old-school", "direct mail"]},
    "david-deutsch":    {"domain": "copywriting", "owns": "legendary-copy", "use": "Boring-to-brilliant, musical architecture, loss framing", "signals": ["legendary", "boring-to-brilliant", "musical", "loss framing"]},
    "luke-iha":         {"domain": "copywriting", "owns": "proof-engineering", "use": "Doubt node mapping, 22-type proof arsenal, trust-building", "signals": ["proof", "doubt", "trust", "credibility", "testimonial architecture", "mechanism"]},
    "ward-farnsworth":  {"domain": "copywriting", "owns": "rhetoric", "use": "Classical rhetoric, chiasmus, anaphora, Saxon punch", "signals": ["rhetoric", "chiasmus", "anaphora", "closing lines", "manifesto", "immortal prose"]},
    "joanna-wiebe":     {"domain": "copywriting", "owns": "conversion-optimization", "use": "Copy testing, voice-of-customer, microcopy", "signals": ["copy testing", "voice of customer", "microcopy", "optimization"]},

    # Domain 2: Content Strategy & Viral (Top-of-Funnel)
    "kallaway":         {"domain": "content-strategy", "owns": "psychology", "use": "Dopamine ladder, retention, buyer intent, content systems", "signals": ["content psychology", "dopamine", "retention", "youtube", "buyer intent", "content system"]},
    "seena-rez":        {"domain": "content-strategy", "owns": "tiktok-execution", "use": "PSAEP scripts, hyperdopamine hooks, TikTok commerce", "signals": ["tiktok", "viral", "short-form", "hyperdopamine", "psaep"]},
    "shaan-puri":       {"domain": "content-strategy", "owns": "storytelling", "use": "Frame-first, emotion transfer, narrative structure", "signals": ["story", "narrative", "frame", "emotion transfer", "intention obstacle"]},
    "jun-yuh":          {"domain": "content-strategy", "owns": "personal-brand-content", "use": "Content calendars, formats, silent film method", "signals": ["content calendar", "content format", "silent film", "brand content", "permutation"]},
    "brock-johnson":    {"domain": "content-strategy", "owns": "shareworthy", "use": "Social-first content, shareability engineering", "signals": ["shareable", "shareworthy", "instagram content", "social-first"]},
    "authority-hacker": {"domain": "content-strategy", "owns": "ai-social", "use": "AI production velocity for social", "signals": ["ai social", "ai content", "content velocity"]},
    "grace-andrews":    {"domain": "content-strategy", "owns": "media-company", "use": "Audience-as-city architecture, content portfolio strategy", "signals": ["media company", "content portfolio", "city architecture", "creator business"]},

    # Domain 3: Personal Brand
    "caleb-ralston":    {"domain": "personal-brand", "owns": "differentiation", "use": "Standing out, credibility bank, contrarian positioning", "signals": ["stand out", "differentiation", "credibility", "contrarian"]},
    "tom-noske":        {"domain": "personal-brand", "owns": "authority", "use": "Packaging expertise, LinkedIn dominance", "signals": ["authority", "expertise packaging", "magnetic brand"]},
    "omar-eddaoudi":    {"domain": "personal-brand", "owns": "premium-positioning", "use": "Luxury brands, exclusionary tension, high-status copy", "signals": ["luxury", "premium positioning", "exclusionary", "high-status"]},
    "erica-mallet":     {"domain": "personal-brand", "owns": "magnetism", "use": "Attraction, scroll-stopping, belief architecture", "signals": ["magnetism", "scroll-stopping", "attraction", "brand magnetism"]},
    "lara-acosta":      {"domain": "personal-brand", "owns": "b2b-linkedin", "use": "Engineered virality, high-retention formats, SLAY", "signals": ["linkedin", "slay", "linkedin growth", "linkedin mastery", "b2b linkedin"]},
    "josh-sanders":     {"domain": "personal-brand", "owns": "linkedin-funnels", "use": "B2B lead generation, content funnels, LinkedIn systems", "signals": ["linkedin funnel", "b2b lead", "linkedin system"]},
    "dan-koe":          {"domain": "personal-brand", "owns": "multipassionate", "use": "One-person business, you ARE the niche, multi-interest", "signals": ["multipassionate", "one-person business", "multiple interests", "you are the niche"]},
    "tommy-clark":      {"domain": "personal-brand", "owns": "b2b-founder", "use": "How I narrative pivot, founder-led LinkedIn, stealth hooks", "signals": ["founder content", "how i", "b2b founder", "stealth hook"]},
    "jasmin-alic":      {"domain": "personal-brand", "owns": "linkedin-hooks", "use": "Trapdoor hooks, distributed commenting, mobile-first formatting", "signals": ["linkedin hook", "trapdoor", "commenting strategy", "mobile-first"]},
    "omar-eltakrori":   {"domain": "personal-brand", "owns": "brand-business", "use": "Business Blueprint, challenge launches, high-ticket coaching", "signals": ["challenge launch", "web class", "high-ticket coaching", "brand business"]},
    "diandra-escobar":  {"domain": "personal-brand", "owns": "linkedin-growth-ops", "use": "Algorithm audit, headline engineering, semantic lanes, save-worthy architecture", "signals": ["linkedin algorithm", "linkedin headline", "semantic lane", "save-worthy", "first 50 words"]},

    # Domain 4: Sales & Persuasion
    "jeremy-miner":     {"domain": "sales", "owns": "sales-psychology", "use": "NEPQ, objection handling, identity selling", "signals": ["sales call", "objection", "nepq", "close deal", "sales psychology", "handling objections"]},
    "michael-bernoff":  {"domain": "sales", "owns": "identity-engineering", "use": "Mindset shifts, breakthrough, belief change", "signals": ["identity shift", "mindset", "breakthrough", "identity engineering"]},
    "lindsay":          {"domain": "sales", "owns": "ai-consulting-sales", "use": "Cold outreach, client acquisition, AI services", "signals": ["cold outreach", "ai consulting", "client acquisition"]},
    "ai-chris-lee":     {"domain": "sales", "owns": "zero-proof-sales", "use": "Selling without testimonials, proof building", "signals": ["no testimonial", "zero proof", "no portfolio"]},
    "nate-herk":        {"domain": "sales", "owns": "b2b-lead-gen", "use": "Validation-first outreach, Trojan Horse partnerships", "signals": ["b2b lead", "partnership", "validation-first", "trojan horse"]},
    "jason-fladlien":   {"domain": "sales", "owns": "high-status-closing", "use": "Subtraction heuristic, friction removal, radical candor, empowerment-first", "signals": ["high-status", "friction removal", "subtraction", "empowerment", "radical candor"]},
    "david-mcraney":    {"domain": "sales", "owns": "belief-change", "use": "Deep canvassing, motivational interviewing, tribal bridge building", "signals": ["belief change", "deep canvass", "motivational interviewing", "tribal"]},
    "tobias-allen":     {"domain": "sales", "owns": "real-reason-persuasion", "use": "Excavating the real motivation, not the stated one", "signals": ["real reason", "real motivation", "hidden objection"]},

    # Domain 5: Consumer Research
    "dai-media":        {"domain": "consumer-research", "owns": "consumer-posture", "use": "Individual-first modeling, identity personas", "signals": ["consumer posture", "persona", "avatar", "customer identity", "icp"]},
    "rory-sutherland":  {"domain": "consumer-research", "owns": "behavioral-economics", "use": "Perceived value, psychological reframing, unconventional angles", "signals": ["behavioral economics", "perceived value", "reframing", "unconventional"]},

    # Domain 6: AI & Automation
    "nick-saraev":      {"domain": "ai-automation", "owns": "agentic-workflows", "use": "Sub-agent architecture, self-healing loops, MCP", "signals": ["agentic", "agent architecture", "self-healing", "mcp", "sub-agent"]},
    "boris":            {"domain": "ai-automation", "owns": "ai-productivity", "use": "Claude Code architecture, multi-instance orchestration", "signals": ["claude code", "claude", "ai productivity", "mobile workflow"]},
    "rachel-woods":     {"domain": "ai-automation", "owns": "ai-ops", "use": "CRAFT cycle, process decomposition, team AI adoption", "signals": ["ai ops", "team adoption", "process decomposition", "craft cycle"]},
    "sherwin-wu":       {"domain": "ai-automation", "owns": "ai-engineering", "use": "Agent fleet management, deployment diagnostics", "signals": ["agent fleet", "deployment", "debugging", "ai engineering"]},
    "futurepedia":      {"domain": "ai-automation", "owns": "prompt-engineering", "use": "Expert framework extraction, meta-prompting", "signals": ["prompt engineering", "meta-prompt", "framework extraction"]},
    "nate-b-jones":     {"domain": "ai-automation", "owns": "ai-systems", "use": "Intent engineering, disambiguation, trust architecture", "signals": ["intent engineering", "disambiguation", "trust architecture", "agent reliability"]},
    "darrel-wilson":    {"domain": "ai-automation", "owns": "automation", "use": "Workflow automation, freelancer replacement, AI monetization", "signals": ["workflow automation", "automate", "freelancer replacement"]},
    "mark-kashef":      {"domain": "ai-automation", "owns": "councils", "use": "Multi-agent orchestration, horizontal task splitting", "signals": ["council", "multi-agent", "orchestration", "horizontal"]},
    "andrew-wilkinson": {"domain": "ai-automation", "owns": "vibe-coding", "use": "Rapid AI execution, problem-to-product translation", "signals": ["vibe code", "rapid build", "problem-to-product"]},
    "lance-yichao":     {"domain": "ai-automation", "owns": "context-engineering", "use": "LLM app architecture, context window optimization", "signals": ["context engineering", "context window", "llm app"]},
    "logan-kilpatrick": {"domain": "ai-automation", "owns": "ai-prototyping", "use": "Google AI Studio, speed-over-perfection", "signals": ["ai studio", "google ai", "rapid prototype"]},
    "dr-kriukow":       {"domain": "ai-automation", "owns": "ai-humanization", "use": "Statistical unpredictability, detection avoidance", "signals": ["humanize", "ai detection", "humanization", "depattern"]},

    # Domain 7: Writing & Storytelling
    "dan-wang":         {"domain": "writing", "owns": "analytical", "use": "Long-form, observation, essays", "signals": ["essay", "long-form", "analytical", "observation"]},
    "oscar-hoglund":    {"domain": "writing", "owns": "audio-narrative", "use": "Sound storytelling, emotional umami", "signals": ["audio", "sound storytelling", "podcast", "emotional umami"]},
    "jonathan-franzen": {"domain": "writing", "owns": "literary-fiction", "use": "Character psychology, narrative compression", "signals": ["literary fiction", "character psychology", "narrative compression"]},
    "lucas-alpay":      {"domain": "writing", "owns": "fiction-craft", "use": "Story structure, character development, fiction writing", "signals": ["fiction", "character development", "story structure", "novel"]},
    "fareed-zakaria":   {"domain": "writing", "owns": "argument-structure", "use": "International analysis, argument architecture, essay construction", "signals": ["argument", "geopolitical", "international", "essay construction"]},
    "robert-mack":      {"domain": "writing", "owns": "humor", "use": "Truth-first comedy, wit engineering, comedic timing", "signals": ["comedy", "humor", "funny", "wit", "comedic"]},
    "ocean-vuong":      {"domain": "writing", "owns": "perceptual", "use": "Estrangement, defamiliarization, image-first prose, anti-homogenization", "signals": ["estrangement", "defamiliarize", "perceptual", "anti-homogenization", "original", "species test"]},
    "michael-connelly": {"domain": "writing", "owns": "vivid-writing", "use": "Surgical detail, subtext dialogue, place-as-character", "signals": ["vivid", "detail", "subtext", "dialogue", "place"]},
    "eric-roth":        {"domain": "writing", "owns": "screenwriting", "use": "Cinematic structure, erosion rewriting, visual prose", "signals": ["screenplay", "cinematic", "erosion", "visual prose", "screenwriting"]},
    "steven-pressfield": {"domain": "writing", "owns": "narrative-mastery", "use": "Resistance, narrative physics, turning pro, creative blocks", "signals": ["resistance", "turning pro", "war of art", "narrative physics", "creative block", "procrastination", "blocked", "shipping", "fear of creating", "writer's block"]},
    "wright-thompson":  {"domain": "writing", "owns": "longform-mastery", "use": "Profile writing, detail-as-work, gap tension, interiority", "signals": ["profile writing", "longform", "wright", "interiority", "gap"]},

    # Domain 8: Products & Monetization
    "monk-ai":          {"domain": "products", "owns": "offer-design", "use": "Consulting offer pyramid, pricing tiers, client ascension", "signals": ["offer design", "consulting offer", "pricing tiers", "client ascension"]},
    "samuel-thompson":  {"domain": "products", "owns": "market-validation", "use": "Shadow markets, unit economics, market entry", "signals": ["shadow market", "market validation", "unit economics", "market entry"]},
    "stockton-walbeck": {"domain": "products", "owns": "lead-magnets", "use": "4-type taxonomy, conversion funnels, data-backed lead gen", "signals": ["lead magnet", "conversion funnel", "free resource"]},
    "maria-wendt":      {"domain": "products", "owns": "digital-products", "use": "Product-first business building, course design", "signals": ["course", "digital product", "online course"]},
    "thrivecart":       {"domain": "products", "owns": "rapid-products", "use": "Weekend product standard, pricing psychology", "signals": ["weekend product", "rapid product", "grocery store method"]},
    "sabrina-ramonov":  {"domain": "products", "owns": "ai-monetization", "use": "Distribution before product, community building, Skool", "signals": ["ai monetization", "skool", "community", "distribution first"]},
    "shan-hanif":       {"domain": "products", "owns": "audience-monetization", "use": "Dual engine (audience + product), community architecture", "signals": ["audience monetization", "dual engine", "community architecture"]},
    "tim-danilov":      {"domain": "products", "owns": "niche-bending", "use": "Format innovation, market-format combinations, blue ocean", "signals": ["niche bending", "format innovation", "blue ocean"]},
    "paul-james":       {"domain": "products", "owns": "ai-services", "use": "Zero-cost positioning, modular service design, recurring revenue", "signals": ["ai service", "modular service", "recurring revenue"]},
    "ross-mckay":       {"domain": "products", "owns": "cpg-physical", "use": "Premium at scale, retail distribution, DTC-to-mass", "signals": ["physical product", "cpg", "retail", "dtc"]},
    "vincent-hu":       {"domain": "products", "owns": "info-business-scaling", "use": "Growth ecosystems, 3-yes conversion, coaching/consulting architecture", "signals": ["info business", "coaching business", "consulting business", "growth ecosystem", "3-yes"]},

    # Domain 9: SEO & Search
    "nathan-gotch":     {"domain": "seo", "owns": "seo-mastery", "use": "Technical SEO, keyword strategy, authority building", "signals": ["seo", "keyword", "technical seo", "rank", "google"]},
    "adam-enfroy":       {"domain": "seo", "owns": "affiliate-blog", "use": "Infinite keyword loops, three-tier content funnel, 70% AI production", "signals": ["affiliate", "blog", "niche site", "keyword loop"]},
    "wordsatscale":     {"domain": "seo", "owns": "rapid-ranking", "use": "Competition vacuum strategy, authority arbitrage", "signals": ["rapid ranking", "competition vacuum", "authority arbitrage"]},
    "ethan-smith":      {"domain": "seo", "owns": "answer-engines", "use": "AEO strategy, citation engineering, experimental search", "signals": ["aeo", "answer engine", "citation", "ai search"]},

    # Domain 10: Design & Web
    "oren":             {"domain": "design", "owns": "taste-development", "use": "CEV framework, creative judgment, luxury psychology, visual direction", "signals": ["taste", "cev", "creative direction", "luxury", "visual direction", "creative judgment"]},
    "kittl":            {"domain": "design", "owns": "graphic-design", "use": "Typography, mood-based font selection, AI design prompts", "signals": ["typography", "font", "graphic design", "layout"]},
    "andy-lo":          {"domain": "design", "owns": "premium-web", "use": "Headless CMS, motion design, cinematic web architecture", "signals": ["premium website", "headless cms", "motion design", "cinematic web"]},
    "sam-goddard":      {"domain": "design", "owns": "media-scaling", "use": "Content infrastructure, production systems, agency scaling", "signals": ["content infrastructure", "production system", "agency scaling"]},
    "sean-kochel":      {"domain": "design", "owns": "design-first-build", "use": "Felt problems, UX-driven development, AI business strategy", "signals": ["ux", "design-first", "felt problem"]},
    "alex-copper":      {"domain": "design", "owns": "brand-strategy", "use": "Creative strategy, visual identity systems", "signals": ["visual identity", "brand strategy", "creative strategy"]},

    # Domain 11: Video & Media
    "tao-prompts":      {"domain": "video", "owns": "ai-video", "use": "Deterministic video pipeline, cinematic prompting, storyboard", "signals": ["ai video", "storyboard", "cinematic prompting", "video pipeline"]},
    "pj-accetturo":     {"domain": "video", "owns": "production-grade-ai", "use": "Professional AI video that doesn't look gimmicky", "signals": ["production video", "professional video", "video quality"]},
    "remotion":         {"domain": "video", "owns": "programmatic-video", "use": "React-based video, data-driven video generation", "signals": ["programmatic video", "react video", "data-driven video"]},

    # Domain 12: Strategy & Business Architecture
    "jim-oshaughnessy": {"domain": "strategy", "owns": "cross-domain-synthesis", "use": "Philosopher-financier lens, high-stakes decisions", "signals": ["high-stakes decision", "cross-domain", "philosopher", "long-term strategy"]},
    "april-dunford":    {"domain": "strategy", "owns": "b2b-positioning", "use": "Obviously Awesome framework, competitive context", "signals": ["positioning", "obviously awesome", "competitive context", "b2b positioning"]},
    "daniel-priestley": {"domain": "strategy", "owns": "demand-engineering", "use": "Oversubscribed methodology, Key Person of Influence", "signals": ["oversubscribed", "demand", "key person", "waiting list"]},
    "marc-andreessen":  {"domain": "strategy", "owns": "ai-economics", "use": "Technology philosophy, venture thesis", "signals": ["technology philosophy", "venture", "future of work", "ai economics"]},
    "manus-ai":         {"domain": "strategy", "owns": "intelligence", "use": "McKinsey-grade research, competitive intelligence", "signals": ["research", "competitive intelligence", "strategic brief", "market analysis"]},
    "soowei":           {"domain": "strategy", "owns": "consulting-leverage", "use": "Founder workflow, scale architecture, leverage auditing", "signals": ["consulting", "leverage", "founder workflow", "scale architecture"]},
    "lulu-cheng":       {"domain": "strategy", "owns": "communications", "use": "PR strategy, crisis communications, reputation management", "signals": ["pr", "crisis", "communications", "reputation"]},
    "mike-foutia":      {"domain": "strategy", "owns": "marketing-tools", "use": "Marketing technology landscape, tool selection", "signals": ["marketing tool", "tool selection", "martech"]},

    # Domain 13: Audience & Growth
    "tyler-denk":       {"domain": "audience", "owns": "newsletter", "use": "BDE system, referral engineering, social launch sequences", "signals": ["newsletter", "referral", "subscriber", "beehiiv"]},
    "ali-abdaal":       {"domain": "audience", "owns": "action-bias", "use": "Two-way door thinking, experiment-driven growth", "signals": ["overthinking", "action", "two-way door", "experiment"]},
    "seth-godin":       {"domain": "audience", "owns": "idea-propagation", "use": "Virusworthiness, sneeze-network design, permission marketing", "signals": ["idea virus", "permission marketing", "tribe", "movement", "remarkability"]},

    # Domain 14: Mindset, Messaging & Consciousness
    "jeremy-haynes":    {"domain": "mindset", "owns": "identity-systems", "use": "Identity-governs-everything, mindset rewiring", "signals": ["identity system", "mindset rewiring", "identity governs"]},
    "david-bayer":      {"domain": "mindset", "owns": "presence-performance", "use": "Elevated presence, performance optimization", "signals": ["presence", "performance", "elevated", "elite communication"]},
    "donald-miller":    {"domain": "mindset", "owns": "culture-messaging", "use": "PEACE framework, culture turnaround, strategic messaging", "signals": ["culture", "peace framework", "storybrand", "messaging", "culture turnaround"]},
    "heath-brothers":   {"domain": "mindset", "owns": "idea-stickiness", "use": "SUCCESs framework, schema violation, commander's intent", "signals": ["sticky", "success framework", "schema violation", "stickiness"]},
    "joscha-bach":      {"domain": "mindset", "owns": "consciousness", "use": "Computational phenomenology, identity engineering, phase transition", "signals": ["consciousness", "phenomenology", "phase transition", "mechanism", "philosophy of mind"]},
    "dr-k":             {"domain": "mindset", "owns": "vedantic-psychology", "use": "Samskara, guna diagnosis, emotional processing, dharma, creative blocks", "signals": ["samskara", "guna", "vedantic", "dharma", "emotional processing", "stuck", "blocked", "creative block", "can't focus", "procrastination", "overwhelmed", "paralyzed", "mental block"]},

    # Domain 15: Industry-Specific
    "joshua-smith":     {"domain": "industry", "owns": "real-estate-production", "use": "KPI-driven production, market agnosticism", "signals": ["real estate production", "kpi", "real estate agent"]},
    "enrico-incarnati": {"domain": "industry", "owns": "real-estate-instagram", "use": "Instagram content strategy, lead generation for agents", "signals": ["real estate instagram", "instagram agent", "real estate content"]},
    "jonathan-courtney": {"domain": "industry", "owns": "design-thinking", "use": "UX sprints, design process, product design", "signals": ["ux sprint", "design thinking", "product design"]},
    "sabri-suby":       {"domain": "industry", "owns": "paid-advertising", "use": "AI-powered ads, direct response marketing, campaign scaling", "signals": ["paid ads", "ad campaign", "campaign scaling", "paid advertising"]},
}

# ─────────────────────────────────────────────────────────
# COMPOUND COMBINATIONS — Force-multiplier pairings
# ─────────────────────────────────────────────────────────

COMPOUNDS = [
    {"pair": ["jeremy-miner", "michael-bernoff"], "effect": "Identity-first sales — Bernoff rewires self-image, Miner closes with NEPQ", "trigger": ["identity objection", "emotional resistance", "mindset block sales"]},
    {"pair": ["seena-rez", "cardinal-mason"], "effect": "Viral commerce — Rez drives TikTok traffic, Mason converts it", "trigger": ["product launch attention", "tiktok sales", "viral commerce"]},
    {"pair": ["harry-dry", "alen-sultanic"], "effect": "Precision long-form — Dry's rules applied across Sultanic's persuasion", "trigger": ["high-stakes sales letter", "vsl tight"]},
    {"pair": ["shaan-puri", "kallaway"], "effect": "Story-driven viral — Puri's arc + Kallaway's dopamine psychology", "trigger": ["spread and retain", "viral story", "story content"]},
    {"pair": ["lara-acosta", "cardinal-mason"], "effect": "LinkedIn revenue engine — Acosta builds authority, Mason monetizes", "trigger": ["linkedin revenue", "linkedin monetize", "linkedin to sales"]},
    {"pair": ["dan-koe", "jun-yuh"], "effect": "Multipassionate brand — Koe's model + Jun's format strategy", "trigger": ["multiple interests brand", "multipassionate", "cohesive brand"]},
    {"pair": ["nicolas-cole", "mitch-albom"], "effect": "Premium prose — Cole's craft + Albom's emotional architecture", "trigger": ["premium content", "beautiful and moving", "premium prose"]},
    {"pair": ["samuel-thompson", "sabri-suby"], "effect": "Paid product launch — Thompson validates, Suby drives paid traffic", "trigger": ["paid launch", "product launch paid ads", "ad-driven launch"]},
    {"pair": ["monk-ai", "lindsay"], "effect": "Consulting acquisition — Monk builds offer, Lindsay executes outreach", "trigger": ["consulting offer clients", "ai consulting launch"]},
    {"pair": ["tobias-allen", "cardinal-mason"], "effect": "Revenue system — Allen's strategy + Mason's conversion copy", "trigger": ["email revenue", "funnel revenue", "revenue system"]},
    {"pair": ["bond-halbert", "david-deutsch"], "effect": "Legendary direct response — Halbert's language + Deutsch's architecture", "trigger": ["legendary copy", "premium direct response"]},
    {"pair": ["april-dunford", "daniel-priestley"], "effect": "Positioning + Demand — Dunford positions, Priestley engineers demand", "trigger": ["poorly positioned", "b2b positioning demand", "position and sell"]},
    {"pair": ["tyler-denk", "seth-godin"], "effect": "Viral newsletter — Denk's referral mechanics + Godin's network design", "trigger": ["newsletter growth", "viral newsletter", "newsletter spread"]},
    {"pair": ["nick-saraev", "boris"], "effect": "Agent fleet — Saraev's self-healing + Boris's orchestration", "trigger": ["multi-agent", "agent fleet", "complex agent system"]},
    {"pair": ["tao-prompts", "pj-accetturo"], "effect": "Cinema-grade AI video — storyboard + production polish", "trigger": ["professional ai video", "cinema video"]},
    {"pair": ["joscha-bach", "steven-pressfield"], "effect": "Consciousness + Resistance — Bach diagnoses, Pressfield mobilizes", "trigger": ["creative block", "existential block", "resistance diagnosis"]},
    {"pair": ["vincent-hu", "april-dunford"], "effect": "Trust positioning — Hu's ecosystem + Dunford's competitive context", "trigger": ["info business positioning", "coaching positioning"]},
    {"pair": ["vincent-hu", "luke-iha"], "effect": "Ecosystem copy — Hu architects system, Iha writes conversion copy", "trigger": ["info business copy", "coaching funnel copy"]},
    {"pair": ["omar-eltakrori", "luke-iha"], "effect": "Challenge funnel copy — Eltakrori architects challenge, Iha writes ads", "trigger": ["challenge funnel", "challenge ads"]},
    {"pair": ["omar-eltakrori", "lara-acosta"], "effect": "Brand-to-business — Eltakrori maps monetization, Acosta executes LinkedIn", "trigger": ["brand to business", "linkedin monetization architecture"]},
    {"pair": ["ocean-vuong", "mitch-albom"], "effect": "Perceptual emotion — Vuong estranges, Albom lands the feeling", "trigger": ["surprise and move", "perceptual emotion", "estranged prose"]},
    {"pair": ["ocean-vuong", "lara-acosta"], "effect": "Poetic LinkedIn — Vuong's prose + Acosta's SLAY formatting", "trigger": ["poetic linkedin", "linkedin sameness", "original linkedin"]},
    {"pair": ["enrico-incarnati", "joshua-smith"], "effect": "Full-stack real estate — Instagram brand + production KPIs", "trigger": ["real estate full stack", "agent brand and production"]},
    {"pair": ["enrico-incarnati", "luke-iha"], "effect": "Proof-stacked real estate — strategy + proof engineering for leads", "trigger": ["real estate conversion", "real estate proof"]},
    {"pair": ["diandra-escobar", "lara-acosta"], "effect": "LinkedIn mastery stack — Escobar's algorithm + Acosta's virality", "trigger": ["linkedin algorithm growth", "linkedin full stack"]},
    {"pair": ["jason-fladlien", "jeremy-miner"], "effect": "Empowerment closing — Fladlien's indirect + Miner's NEPQ", "trigger": ["empowerment sales", "indirect closing"]},
]

# ─────────────────────────────────────────────────────────
# DOMAIN LABELS
# ─────────────────────────────────────────────────────────

DOMAIN_LABELS = {
    "copywriting": "Copywriting (Conversion & Sales)",
    "content-strategy": "Content Strategy & Viral (Top-of-Funnel)",
    "personal-brand": "Personal Brand",
    "sales": "Sales & Persuasion",
    "consumer-research": "Consumer Research",
    "ai-automation": "AI & Automation",
    "writing": "Writing & Storytelling",
    "products": "Products & Monetization",
    "seo": "SEO & Search",
    "design": "Design & Web",
    "video": "Video & Media",
    "strategy": "Strategy & Business Architecture",
    "audience": "Audience & Growth",
    "mindset": "Mindset, Messaging & Consciousness",
    "industry": "Industry-Specific",
}


def _stem(word):
    """Minimal suffix-strip stemmer for signal matching."""
    for suffix in ("ing", "tion", "ness", "ally", "ment", "ive", "ity", "ly", "ed", "er", "es", "s"):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            return word[: -len(suffix)]
    return word


def route(query, top_n=5):
    """Route a problem description to the best expert(s)."""
    query_lower = query.lower()
    query_words = query_lower.split()
    query_stems = [_stem(w) for w in query_words]
    # Build bigrams from adjacent query words
    query_bigrams = [f"{query_words[i]} {query_words[i+1]}" for i in range(len(query_words) - 1)]

    scored = []

    for name, info in EXPERTS.items():
        score = 0

        for signal in info["signals"]:
            # 1. Exact substring match (strongest)
            if signal in query_lower:
                score += len(signal.split()) * 3
                continue

            # 2. Bigram overlap: check if query bigrams match signal
            signal_words = signal.split()
            if len(signal_words) >= 2:
                for bigram in query_bigrams:
                    bigram_stems = [_stem(w) for w in bigram.split()]
                    signal_stems = [_stem(w) for w in signal_words]
                    # If both stems overlap across bigram<>signal, count it
                    overlap = sum(1 for bs in bigram_stems if any(bs in ss or ss in bs for ss in signal_stems if len(ss) > 2))
                    if overlap >= 2:
                        score += len(signal_words) * 2
                        break

            # 3. Individual signal-word overlap (weakest, fractional)
            for sw in signal_words:
                if len(sw) < 3:
                    continue
                sw_stem = _stem(sw)
                for qs in query_stems:
                    if len(qs) < 3:
                        continue
                    if sw_stem in qs or qs in sw_stem:
                        score += 0.5
                        break

        # Also check if any query words appear in name, owns, or use
        for word in query_words:
            if len(word) < 3:
                continue
            if word in name:
                score += 2
            if word in info["owns"]:
                score += 1
            if word in info["use"].lower():
                score += 0.5

        if score >= 2.0:
            scored.append((score, name, info))

    scored.sort(key=lambda x: -x[0])
    return scored[:top_n]


def find_compounds(query):
    """Find matching compound combinations for a query."""
    query_lower = query.lower()
    query_stems = [_stem(w) for w in query_lower.split()]
    matches = []
    scored_compounds = []

    for compound in COMPOUNDS:
        best_score = 0
        for trigger in compound["trigger"]:
            trigger_words = [w for w in trigger.split() if len(w) > 2]
            if not trigger_words:
                continue
            # Count how many trigger words have a stem match in the query
            matched = sum(
                1 for tw in trigger_words
                if any(_stem(tw) in qs or qs in _stem(tw) for qs in query_stems if len(qs) > 2)
            )
            # Require at least 60% of trigger words to match
            ratio = matched / len(trigger_words) if trigger_words else 0
            if ratio >= 0.6:
                best_score = max(best_score, matched)
        if best_score > 0:
            scored_compounds.append((best_score, compound))

    # Sort by match quality and return
    scored_compounds.sort(key=lambda x: -x[0])
    return [c for _, c in scored_compounds]


def domain_lookup(domain_key):
    """Get all experts in a domain."""
    domain_key = domain_key.lower().replace(" ", "-")
    results = []
    for name, info in EXPERTS.items():
        if info["domain"] == domain_key:
            results.append((name, info))
    return results


def expert_lookup(expert_name):
    """Get details for a specific expert."""
    expert_name = expert_name.lower()
    if expert_name in EXPERTS:
        return EXPERTS[expert_name]
    # Fuzzy match
    for name, info in EXPERTS.items():
        if expert_name in name:
            return {**info, "_matched_name": name}
    return None


def format_route_output(results, compounds=None):
    """Format routing results for display."""
    if not results:
        print("No matching experts found.")
        return

    print(f"Top {len(results)} expert matches:\n")
    for score, name, info in results:
        domain_label = DOMAIN_LABELS.get(info["domain"], info["domain"])
        print(f"  @{name:25s} [{domain_label}]")
        print(f"    Owns: {info['owns']}  |  {info['use']}")
        print()

    if compounds:
        print("⚡ Compound Combinations (force-multiplier pairings):\n")
        for c in compounds:
            print(f"  @{c['pair'][0]} + @{c['pair'][1]}")
            print(f"    → {c['effect']}")
            print()


def show_stats():
    """Show routing statistics."""
    domain_counts = defaultdict(int)
    for info in EXPERTS.values():
        domain_counts[info["domain"]] += 1

    print(f"Total experts indexed:  {len(EXPERTS)}")
    print(f"Total compounds:       {len(COMPOUNDS)}")
    print(f"Total domains:         {len(DOMAIN_LABELS)}")
    print()
    print("Expert distribution by domain:")
    for domain, label in sorted(DOMAIN_LABELS.items(), key=lambda x: x[1]):
        count = domain_counts.get(domain, 0)
        print(f"  {label:45s} {count:3d} experts")


def list_domains():
    """List all domains."""
    domain_counts = defaultdict(int)
    for info in EXPERTS.values():
        domain_counts[info["domain"]] += 1

    for domain, label in sorted(DOMAIN_LABELS.items(), key=lambda x: x[1]):
        count = domain_counts.get(domain, 0)
        print(f"  {domain:25s} ({count:2d} experts) — {label}")


def main():
    parser = argparse.ArgumentParser(description="Expert Router — Route problems to experts")
    sub = parser.add_subparsers(dest="command")

    route_p = sub.add_parser("route", help="Route a problem to the best expert(s)")
    route_p.add_argument("query", help="Problem description")
    route_p.add_argument("-n", "--top", type=int, default=5, help="Number of results")

    domain_p = sub.add_parser("domain", help="List experts in a domain")
    domain_p.add_argument("name", help="Domain key (e.g., copywriting, sales, design)")

    expert_p = sub.add_parser("expert", help="Look up a specific expert")
    expert_p.add_argument("name", help="Expert name (e.g., luke-iha)")

    compound_p = sub.add_parser("compounds", help="Find compound expert combinations")
    compound_p.add_argument("query", help="Problem description")

    sub.add_parser("stats", help="Show routing statistics")
    sub.add_parser("domains", help="List all domains")

    args = parser.parse_args()

    if args.command == "route":
        results = route(args.query, args.top)
        compounds = find_compounds(args.query)
        format_route_output(results, compounds)

    elif args.command == "domain":
        results = domain_lookup(args.name)
        if not results:
            print(f"No experts in domain '{args.name}'")
            print("\nAvailable domains:")
            list_domains()
            return
        domain_label = DOMAIN_LABELS.get(args.name.lower().replace(" ", "-"), args.name)
        print(f"{len(results)} experts in '{domain_label}':\n")
        for name, info in results:
            print(f"  @{name:25s} [{info['owns']}] — {info['use']}")

    elif args.command == "expert":
        info = expert_lookup(args.name)
        if not info:
            print(f"Expert '{args.name}' not found.")
            return
        matched = info.pop("_matched_name", args.name)
        domain_label = DOMAIN_LABELS.get(info["domain"], info["domain"])
        print(f"Expert: @{matched}")
        print(f"Domain: {domain_label}")
        print(f"Owns:   {info['owns']}")
        print(f"Use:    {info['use']}")
        print(f"Signals: {', '.join(info['signals'])}")

        # Show compounds involving this expert
        expert_compounds = [c for c in COMPOUNDS if matched in c["pair"]]
        if expert_compounds:
            print(f"\n⚡ Compound combinations ({len(expert_compounds)}):")
            for c in expert_compounds:
                partner = c["pair"][1] if c["pair"][0] == matched else c["pair"][0]
                print(f"  + @{partner}: {c['effect']}")

    elif args.command == "compounds":
        matches = find_compounds(args.query)
        if not matches:
            print(f"No compound combinations match '{args.query}'")
            return
        print(f"{len(matches)} compound combinations:\n")
        for c in matches:
            print(f"  @{c['pair'][0]} + @{c['pair'][1]}")
            print(f"    → {c['effect']}")
            print(f"    Triggers: {', '.join(c['trigger'])}")
            print()

    elif args.command == "stats":
        show_stats()

    elif args.command == "domains":
        list_domains()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
