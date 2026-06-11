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
    "harry-dry":        {"domain": "copywriting", "owns": "evaluation", "use": "Auditing copy, Three Rules Test, rewrite discipline", "signals": ["audit", "evaluate", "copy review", "three rules", "rewrite", "copy audit", "is my copy good", "review my writing", "copy feedback", "grade my copy", "what's wrong with my copy"]},
    "cardinal-mason":   {"domain": "copywriting", "owns": "conversion", "use": "Sales pages, emails, client delivery, business building", "signals": ["sales page", "email sequence", "conversion", "funnel copy", "landing page", "opt-in page", "welcome sequence", "nurture sequence", "sales email", "email marketing", "autoresponder", "drip campaign", "cart abandonment"]},
    "alen-sultanic":    {"domain": "copywriting", "owns": "long-form", "use": "Sales letters, VSLs, sophisticated persuasion", "signals": ["vsl", "sales letter", "long-form copy", "sophisticated", "premium long", "video sales letter", "webinar script", "presentation script", "long copy", "persuasion architecture"]},
    "nicolas-cole":     {"domain": "copywriting", "owns": "sentence-craft", "use": "Rhythm, readability, sentence-level polish, digital products", "signals": ["sentence", "rhythm", "readability", "polish", "headline", "sentence structure", "writing quality", "tighten my writing", "make it punchier", "improve my sentences"]},
    "mitch-albom":      {"domain": "copywriting", "owns": "emotional/literary", "use": "Premium narrative, emotion-first, storytelling copy", "signals": ["emotional", "literary", "premium narrative", "story-driven copy", "make people feel", "emotional writing", "heartfelt", "moving", "touching", "memoir", "personal essay", "life story", "emotional depth"]},
    "bond-halbert":     {"domain": "copywriting", "owns": "direct-response", "use": "Market language excavation, velocity optimization, four-reader types", "signals": ["direct response", "market language", "old-school", "direct mail", "classic copy", "swipe file", "tested copy", "proven copy"]},
    "david-deutsch":    {"domain": "copywriting", "owns": "legendary-copy", "use": "Boring-to-brilliant, musical architecture, loss framing", "signals": ["legendary", "boring-to-brilliant", "musical", "loss framing", "boring product", "make it interesting", "transform boring", "copy architecture"]},
    "luke-iha":         {"domain": "copywriting", "owns": "proof-engineering", "use": "Doubt node mapping, 22-type proof arsenal, trust-building", "signals": ["proof", "doubt", "trust", "credibility", "testimonial architecture", "mechanism", "social proof", "case study", "results", "evidence", "before and after", "need more proof", "not believable"]},
    "ward-farnsworth":  {"domain": "copywriting", "owns": "rhetoric", "use": "Classical rhetoric, chiasmus, anaphora, Saxon punch", "signals": ["rhetoric", "chiasmus", "anaphora", "closing lines", "manifesto", "immortal prose", "poetic copy", "speech", "keynote", "powerful closing", "declaration"]},
    "joanna-wiebe":     {"domain": "copywriting", "owns": "conversion-optimization", "use": "Copy testing, voice-of-customer, microcopy", "signals": ["copy testing", "voice of customer", "microcopy", "optimization", "ab test", "button text", "cta", "call to action", "form copy", "ux writing"]},

    # Domain 2: Content Strategy & Viral (Top-of-Funnel)
    "kallaway":         {"domain": "content-strategy", "owns": "psychology", "use": "Dopamine ladder, retention, buyer intent, content systems", "signals": ["content psychology", "dopamine", "retention", "youtube", "buyer intent", "content system", "content strategy", "what content should i make", "content plan", "viewer psychology", "watch time", "audience retention"]},
    "seena-rez":        {"domain": "content-strategy", "owns": "tiktok-execution", "use": "PSAEP scripts, hyperdopamine hooks, TikTok commerce", "signals": ["tiktok", "viral", "short-form", "hyperdopamine", "psaep", "reels", "shorts", "go viral", "trending", "viral video", "short video", "tiktok shop"]},
    "shaan-puri":       {"domain": "content-strategy", "owns": "storytelling", "use": "Frame-first, emotion transfer, narrative structure", "signals": ["story", "narrative", "frame", "emotion transfer", "intention obstacle", "tell a story", "storytelling", "narrative arc", "story structure", "good story"]},
    "jun-yuh":          {"domain": "content-strategy", "owns": "personal-brand-content", "use": "Content calendars, formats, silent film method", "signals": ["content calendar", "content format", "silent film", "brand content", "permutation", "what to post", "posting schedule", "content ideas", "content plan", "weekly content", "batch content"]},
    "brock-johnson":    {"domain": "content-strategy", "owns": "shareworthy", "use": "Social-first content, shareability engineering", "signals": ["shareable", "shareworthy", "instagram content", "social-first", "people share", "share-worthy", "instagram strategy"]},
    "authority-hacker": {"domain": "content-strategy", "owns": "ai-social", "use": "AI production velocity for social", "signals": ["ai social", "ai content", "content velocity", "automate content", "ai for social media", "content at scale"]},
    "grace-andrews":    {"domain": "content-strategy", "owns": "media-company", "use": "Audience-as-city architecture, content portfolio strategy", "signals": ["media company", "content portfolio", "city architecture", "creator business", "build a media company", "content empire", "creator to company", "media brand"]},

    # Domain 3: Personal Brand
    "caleb-ralston":    {"domain": "personal-brand", "owns": "differentiation", "use": "Standing out, credibility bank, contrarian positioning", "signals": ["stand out", "differentiation", "credibility", "contrarian", "unique", "different", "how do i stand out", "everyone looks the same", "crowded market", "what makes me different", "positioning"]},
    "tom-noske":        {"domain": "personal-brand", "owns": "authority", "use": "Packaging expertise, LinkedIn dominance", "signals": ["authority", "expertise packaging", "magnetic brand", "thought leader", "expert status", "be seen as expert", "known for"]},
    "omar-eddaoudi":    {"domain": "personal-brand", "owns": "premium-positioning", "use": "Luxury brands, exclusionary tension, high-status copy", "signals": ["luxury", "premium positioning", "exclusionary", "high-status", "high-end", "exclusive", "premium brand", "luxury brand", "aspirational"]},
    "erica-mallet":     {"domain": "personal-brand", "owns": "magnetism", "use": "Attraction, scroll-stopping, belief architecture", "signals": ["magnetism", "scroll-stopping", "attraction", "brand magnetism", "magnetic", "attract audience", "people come to me", "pull marketing"]},
    "lara-acosta":      {"domain": "personal-brand", "owns": "b2b-linkedin", "use": "Engineered virality, high-retention formats, SLAY", "signals": ["linkedin", "slay", "linkedin growth", "linkedin mastery", "b2b linkedin", "linkedin post", "linkedin content", "grow on linkedin", "linkedin strategy", "linkedin engagement"]},
    "josh-sanders":     {"domain": "personal-brand", "owns": "linkedin-funnels", "use": "B2B lead generation, content funnels, LinkedIn systems", "signals": ["linkedin funnel", "b2b lead", "linkedin system", "linkedin leads", "linkedin to clients", "linkedin pipeline"]},
    "dan-koe":          {"domain": "personal-brand", "owns": "multipassionate", "use": "One-person business, you ARE the niche, multi-interest", "signals": ["multipassionate", "one-person business", "multiple interests", "you are the niche", "too many interests", "can't pick a niche", "solopreneur", "one person", "solo creator"]},
    "tommy-clark":      {"domain": "personal-brand", "owns": "b2b-founder", "use": "How I narrative pivot, founder-led LinkedIn, stealth hooks", "signals": ["founder content", "how i", "b2b founder", "stealth hook", "ceo content", "founder-led", "startup content"]},
    "jasmin-alic":      {"domain": "personal-brand", "owns": "linkedin-hooks", "use": "Trapdoor hooks, distributed commenting, mobile-first formatting", "signals": ["linkedin hook", "trapdoor", "commenting strategy", "mobile-first", "linkedin formatting", "linkedin engagement", "commenting"]},
    "omar-eltakrori":   {"domain": "personal-brand", "owns": "brand-business", "use": "Business Blueprint, challenge launches, high-ticket coaching", "signals": ["challenge launch", "web class", "high-ticket coaching", "brand business", "5-day challenge", "group coaching", "launch a challenge", "coaching program", "high ticket"]},
    "diandra-escobar":  {"domain": "personal-brand", "owns": "linkedin-growth-ops", "use": "Algorithm audit, headline engineering, semantic lanes, save-worthy architecture", "signals": ["linkedin algorithm", "linkedin headline", "semantic lane", "save-worthy", "first 50 words", "linkedin profile", "linkedin reach", "linkedin impressions", "algorithm"]},

    # Domain 4: Sales & Persuasion
    "jeremy-miner":     {"domain": "sales", "owns": "sales-psychology", "use": "NEPQ, objection handling, identity selling", "signals": ["sales call", "objection", "nepq", "close deal", "sales psychology", "handling objections", "close more deals", "sales conversation", "closing", "prospect says no", "overcome objections", "discovery call"]},
    "michael-bernoff":  {"domain": "sales", "owns": "identity-engineering", "use": "Mindset shifts, breakthrough, belief change", "signals": ["identity shift", "mindset", "breakthrough", "identity engineering", "who am i", "self-image", "limiting belief", "identity crisis", "reinvent myself"]},
    "lindsay":          {"domain": "sales", "owns": "ai-consulting-sales", "use": "Cold outreach, client acquisition, AI services", "signals": ["cold outreach", "ai consulting", "client acquisition", "get clients", "find clients", "cold email", "cold dm", "outreach message", "prospecting"]},
    "ai-chris-lee":     {"domain": "sales", "owns": "zero-proof-sales", "use": "Selling without testimonials, proof building", "signals": ["no testimonial", "zero proof", "no portfolio", "no results yet", "just starting out", "no case studies", "no track record", "beginner"]},
    "nate-herk":        {"domain": "sales", "owns": "b2b-lead-gen", "use": "Validation-first outreach, Trojan Horse partnerships", "signals": ["b2b lead", "partnership", "validation-first", "trojan horse", "strategic partnership", "joint venture", "b2b outreach"]},
    "jason-fladlien":   {"domain": "sales", "owns": "high-status-closing", "use": "Subtraction heuristic, friction removal, radical candor, empowerment-first", "signals": ["high-status", "friction removal", "subtraction", "empowerment", "radical candor", "premium closing", "high-ticket sales", "closing high ticket"]},
    "david-mcraney":    {"domain": "sales", "owns": "belief-change", "use": "Deep canvassing, motivational interviewing, tribal bridge building", "signals": ["belief change", "deep canvass", "motivational interviewing", "tribal", "change someone's mind", "persuade", "convince", "resistant audience", "skeptic"]},
    "tobias-allen":     {"domain": "sales", "owns": "real-reason-persuasion", "use": "Excavating the real motivation, not the stated one", "signals": ["real reason", "real motivation", "hidden objection", "why people really buy", "true motivation", "unspoken need"]},

    # Domain 5: Consumer Research
    "dai-media":        {"domain": "consumer-research", "owns": "consumer-posture", "use": "Individual-first modeling, identity personas", "signals": ["consumer posture", "persona", "avatar", "customer identity", "icp", "ideal customer", "who is my customer", "target audience", "buyer persona", "customer profile", "audience research"]},
    "rory-sutherland":  {"domain": "consumer-research", "owns": "behavioral-economics", "use": "Perceived value, psychological reframing, unconventional angles", "signals": ["behavioral economics", "perceived value", "reframing", "unconventional", "irrational", "why people choose", "psychology of value", "pricing psychology"]},

    # Domain 6: AI & Automation
    "nick-saraev":      {"domain": "ai-automation", "owns": "agentic-workflows", "use": "Sub-agent architecture, self-healing loops, MCP", "signals": ["agentic", "agent architecture", "self-healing", "mcp", "sub-agent", "build an agent", "ai agent", "agent system", "autonomous"]},
    "boris":            {"domain": "ai-automation", "owns": "ai-productivity", "use": "Claude Code architecture, multi-instance orchestration", "signals": ["claude code", "claude", "ai productivity", "mobile workflow", "gemini code", "coding assistant", "ai coding", "code editor"]},
    "rachel-woods":     {"domain": "ai-automation", "owns": "ai-ops", "use": "CRAFT cycle, process decomposition, team AI adoption", "signals": ["ai ops", "team adoption", "process decomposition", "craft cycle", "teach my team ai", "ai for my team", "ai workflows", "business process"]},
    "sherwin-wu":       {"domain": "ai-automation", "owns": "ai-engineering", "use": "Agent fleet management, deployment diagnostics", "signals": ["agent fleet", "deployment", "debugging", "ai engineering", "agent broken", "agent not working", "fix agent", "agent error"]},
    "futurepedia":      {"domain": "ai-automation", "owns": "prompt-engineering", "use": "Expert framework extraction, meta-prompting", "signals": ["prompt engineering", "meta-prompt", "framework extraction", "better prompts", "prompt template", "system prompt", "improve my prompt"]},
    "nate-b-jones":     {"domain": "ai-automation", "owns": "ai-systems", "use": "Intent engineering, disambiguation, trust architecture", "signals": ["intent engineering", "disambiguation", "trust architecture", "agent reliability", "ai trust", "reliable ai", "ai accuracy"]},
    "darrel-wilson":    {"domain": "ai-automation", "owns": "automation", "use": "Workflow automation, freelancer replacement, AI monetization", "signals": ["workflow automation", "automate", "freelancer replacement", "n8n", "make.com", "zapier", "automate my business", "save time", "automation"]},
    "mark-kashef":      {"domain": "ai-automation", "owns": "councils", "use": "Multi-agent orchestration, horizontal task splitting", "signals": ["council", "multi-agent", "orchestration", "horizontal", "multiple agents", "agent team", "swarm"]},
    "andrew-wilkinson": {"domain": "ai-automation", "owns": "vibe-coding", "use": "Rapid AI execution, problem-to-product translation", "signals": ["vibe code", "rapid build", "problem-to-product", "vibe coding", "build fast", "ship quickly", "prototype", "mvp"]},
    "lance-yichao":     {"domain": "ai-automation", "owns": "context-engineering", "use": "LLM app architecture, context window optimization", "signals": ["context engineering", "context window", "llm app", "context length", "token budget", "rag", "retrieval augmented"]},
    "logan-kilpatrick": {"domain": "ai-automation", "owns": "ai-prototyping", "use": "Google AI Studio, speed-over-perfection", "signals": ["ai studio", "google ai", "rapid prototype", "gemini api", "quick ai build"]},
    "dr-kriukow":       {"domain": "ai-automation", "owns": "ai-humanization", "use": "Statistical unpredictability, detection avoidance", "signals": ["humanize", "ai detection", "humanization", "depattern", "sounds like ai", "too robotic", "ai detector", "pass ai detection", "sound human"]},

    # Domain 7: Writing & Storytelling
    "dan-wang":         {"domain": "writing", "owns": "analytical", "use": "Long-form, observation, essays", "signals": ["essay", "long-form", "analytical", "observation", "annual letter", "think piece", "analysis", "opinion piece", "editorial"]},
    "oscar-hoglund":    {"domain": "writing", "owns": "audio-narrative", "use": "Sound storytelling, emotional umami", "signals": ["audio", "sound storytelling", "podcast", "emotional umami", "podcast script", "audio story", "sound design"]},
    "jonathan-franzen": {"domain": "writing", "owns": "literary-fiction", "use": "Character psychology, narrative compression", "signals": ["literary fiction", "character psychology", "narrative compression", "literary novel", "serious fiction", "character study"]},
    "lucas-alpay":      {"domain": "writing", "owns": "fiction-craft", "use": "Story structure, character development, fiction writing", "signals": ["fiction", "character development", "story structure", "novel", "memoir", "book", "chapter", "scene", "protagonist", "plot", "write a book", "writing a book", "my story", "life story", "autobiography"]},
    "fareed-zakaria":   {"domain": "writing", "owns": "argument-structure", "use": "International analysis, argument architecture, essay construction", "signals": ["argument", "geopolitical", "international", "essay construction", "make an argument", "persuasive essay", "op-ed", "policy"]},
    "robert-mack":      {"domain": "writing", "owns": "humor", "use": "Truth-first comedy, wit engineering, comedic timing", "signals": ["comedy", "humor", "funny", "wit", "comedic", "make it funny", "add humor", "jokes", "entertaining", "lighthearted"]},
    "ocean-vuong":      {"domain": "writing", "owns": "perceptual", "use": "Estrangement, defamiliarization, image-first prose, anti-homogenization", "signals": ["estrangement", "defamiliarize", "perceptual", "anti-homogenization", "original", "species test", "too generic", "sounds like everyone", "unique voice", "fresh perspective", "make it original"]},
    "michael-connelly": {"domain": "writing", "owns": "vivid-writing", "use": "Surgical detail, subtext dialogue, place-as-character", "signals": ["vivid", "detail", "subtext", "dialogue", "place", "setting", "show don't tell", "descriptive", "immersive", "concrete detail"]},
    "eric-roth":        {"domain": "writing", "owns": "screenwriting", "use": "Cinematic structure, erosion rewriting, visual prose", "signals": ["screenplay", "cinematic", "erosion", "visual prose", "screenwriting", "movie", "film", "script", "cinematic writing", "visual storytelling"]},
    "steven-pressfield": {"domain": "writing", "owns": "narrative-mastery", "use": "Resistance, narrative physics, turning pro, creative blocks", "signals": ["resistance", "turning pro", "war of art", "narrative physics", "creative block", "procrastination", "blocked", "shipping", "fear of creating", "writer's block", "can't start", "can't finish", "not creating", "afraid to publish"]},
    "wright-thompson":  {"domain": "writing", "owns": "longform-mastery", "use": "Profile writing, detail-as-work, gap tension, interiority", "signals": ["profile writing", "longform", "wright", "interiority", "gap", "profile piece", "biography", "portrait", "character profile", "personal essay", "memoir"]},

    # Domain 8: Products & Monetization
    "monk-ai":          {"domain": "products", "owns": "offer-design", "use": "Consulting offer pyramid, pricing tiers, client ascension", "signals": ["offer design", "consulting offer", "pricing tiers", "client ascension", "package my services", "service tiers", "offer structure", "pricing model", "how to price"]},
    "samuel-thompson":  {"domain": "products", "owns": "market-validation", "use": "Shadow markets, unit economics, market entry", "signals": ["shadow market", "market validation", "unit economics", "market entry", "validate idea", "is there a market", "test my idea", "market research", "opportunity"]},
    "stockton-walbeck": {"domain": "products", "owns": "lead-magnets", "use": "4-type taxonomy, conversion funnels, data-backed lead gen", "signals": ["lead magnet", "conversion funnel", "free resource", "freebie", "pdf download", "opt-in", "lead generation", "grow my list", "email list"]},
    "maria-wendt":      {"domain": "products", "owns": "digital-products", "use": "Product-first business building, course design", "signals": ["course", "digital product", "online course", "create a course", "sell a course", "teach online", "course launch", "info product", "how to create a product"]},
    "thrivecart":       {"domain": "products", "owns": "rapid-products", "use": "Weekend product standard, pricing psychology", "signals": ["weekend product", "rapid product", "grocery store method", "quick product", "fast launch", "minimum viable product", "ship fast"]},
    "sabrina-ramonov":  {"domain": "products", "owns": "ai-monetization", "use": "Distribution before product, community building, Skool", "signals": ["ai monetization", "skool", "community", "distribution first", "build community", "membership", "paid community", "skool group"]},
    "shan-hanif":       {"domain": "products", "owns": "audience-monetization", "use": "Dual engine (audience + product), community architecture", "signals": ["audience monetization", "dual engine", "community architecture", "monetize audience", "monetize followers", "turn followers into customers"]},
    "tim-danilov":      {"domain": "products", "owns": "niche-bending", "use": "Format innovation, market-format combinations, blue ocean", "signals": ["niche bending", "format innovation", "blue ocean", "new format", "category creation", "create a category", "unique product format"]},
    "paul-james":       {"domain": "products", "owns": "ai-services", "use": "Zero-cost positioning, modular service design, recurring revenue", "signals": ["ai service", "modular service", "recurring revenue", "ai agency", "ai freelance", "sell ai services", "ai service business"]},
    "ross-mckay":       {"domain": "products", "owns": "cpg-physical", "use": "Premium at scale, retail distribution, DTC-to-mass", "signals": ["physical product", "cpg", "retail", "dtc", "e-commerce", "manufacturing", "wholesale", "consumer product", "inventory"]},
    "meg-heckman":      {"domain": "products", "owns": "buyer-trigger-apparel", "use": "Print-on-demand buyer psychology, apparel purchase intent, identity-led product design, social currency, research-backed buyer insight mapping", "signals": ["buyer-trigger-os", "meg heckman", "meg hackman", "print on demand trigger audit", "pod buyer triggers", "apparel buyer psychology", "shirt purchase intent", "t-shirt purchase intent", "shirt design psychology", "identity-led product design", "social currency product", "product purchase intent", "offer purchase intent", "landing page purchase psychology", "cross-vertical purchase intent", "josh shirt purchase intent", "mybpm streetwear design psychology", "edm streetwear purchase intent", "current buyer insights", "buyer trend research", "find buyer trends", "purchase intent research", "trend-backed shirt ideas", "social listening product design", "research-backed trigger audit"]},
    "vincent-hu":       {"domain": "products", "owns": "info-business-scaling", "use": "Growth ecosystems, 3-yes conversion, coaching/consulting architecture", "signals": ["info business", "coaching business", "consulting business", "growth ecosystem", "3-yes", "scale coaching", "scale consulting", "coaching offer", "consulting offer", "grow my coaching business"]},

    # Domain 9: SEO & Search
    "nathan-gotch":     {"domain": "seo", "owns": "seo-mastery", "use": "Technical SEO, keyword strategy, authority building", "signals": ["seo", "keyword", "technical seo", "rank", "google", "search engine", "organic traffic", "rank on google", "get found on google", "search rankings"]},
    "adam-enfroy":       {"domain": "seo", "owns": "affiliate-blog", "use": "Infinite keyword loops, three-tier content funnel, 70% AI production", "signals": ["affiliate", "blog", "niche site", "keyword loop", "affiliate marketing", "start a blog", "blog that makes money", "passive income blog"]},
    "wordsatscale":     {"domain": "seo", "owns": "rapid-ranking", "use": "Competition vacuum strategy, authority arbitrage", "signals": ["rapid ranking", "competition vacuum", "authority arbitrage", "rank fast", "quick seo wins"]},
    "ethan-smith":      {"domain": "seo", "owns": "answer-engines", "use": "AEO strategy, citation engineering, experimental search", "signals": ["aeo", "answer engine", "citation", "ai search", "chatgpt search", "perplexity ranking", "ai overview", "featured snippet"]},

    # Domain 10: Design & Web
    "oren":             {"domain": "design", "owns": "taste-development", "use": "CEV framework, creative judgment, luxury psychology, visual direction", "signals": ["taste", "cev", "creative direction", "luxury", "visual direction", "creative judgment", "good taste", "design taste", "aesthetic", "beautiful design", "visual style"]},
    "kittl":            {"domain": "design", "owns": "graphic-design", "use": "Typography, mood-based font selection, AI design prompts", "signals": ["typography", "font", "graphic design", "layout", "carousel", "social graphic", "instagram graphic", "poster", "flyer"]},
    "andy-lo":          {"domain": "design", "owns": "premium-web", "use": "Headless CMS, motion design, cinematic web architecture", "signals": ["premium website", "headless cms", "motion design", "cinematic web", "beautiful website", "portfolio site", "agency website"]},
    "sam-goddard":      {"domain": "design", "owns": "media-scaling", "use": "Content infrastructure, production systems, agency scaling", "signals": ["content infrastructure", "production system", "agency scaling", "content operations", "team production"]},
    "sean-kochel":      {"domain": "design", "owns": "design-first-build", "use": "Felt problems, UX-driven development, AI business strategy", "signals": ["ux", "design-first", "felt problem", "user experience", "app design", "product design", "wireframe"]},
    "alex-copper":      {"domain": "design", "owns": "brand-strategy", "use": "Creative strategy, visual identity systems", "signals": ["visual identity", "brand strategy", "creative strategy", "brand identity", "brand guidelines", "logo", "brand system"]},

    # Domain 11: Video & Media
    "tao-prompts":      {"domain": "video", "owns": "ai-video", "use": "Deterministic video pipeline, cinematic prompting, storyboard", "signals": ["ai video", "storyboard", "cinematic prompting", "video pipeline", "ai-generated video", "video generation", "text to video"]},
    "pj-accetturo":     {"domain": "video", "owns": "production-grade-ai", "use": "Professional AI video that doesn't look gimmicky", "signals": ["production video", "professional video", "video quality", "video looks bad", "polished video", "broadcast quality"]},
    "remotion":         {"domain": "video", "owns": "programmatic-video", "use": "React-based video, data-driven video generation", "signals": ["programmatic video", "react video", "data-driven video", "automated video", "video at scale"]},

    # Domain 12: Strategy & Business Architecture
    "jim-oshaughnessy": {"domain": "strategy", "owns": "cross-domain-synthesis", "use": "Philosopher-financier lens, high-stakes decisions", "signals": ["high-stakes decision", "cross-domain", "philosopher", "long-term strategy", "big decision", "life changing decision", "strategic thinking", "what should i do", "help me decide"]},
    "april-dunford":    {"domain": "strategy", "owns": "b2b-positioning", "use": "Obviously Awesome framework, competitive context", "signals": ["positioning", "obviously awesome", "competitive context", "b2b positioning", "how to position", "market position", "competitive advantage", "why choose me"]},
    "daniel-priestley": {"domain": "strategy", "owns": "demand-engineering", "use": "Oversubscribed methodology, Key Person of Influence", "signals": ["oversubscribed", "demand", "key person", "waiting list", "create demand", "people lining up", "waitlist", "overbooked"]},
    "marc-andreessen":  {"domain": "strategy", "owns": "ai-economics", "use": "Technology philosophy, venture thesis", "signals": ["technology philosophy", "venture", "future of work", "ai economics", "tech trends", "where is ai going", "future of ai"]},
    "manus-ai":         {"domain": "strategy", "owns": "intelligence", "use": "McKinsey-grade research, competitive intelligence", "signals": ["research", "competitive intelligence", "strategic brief", "market analysis", "industry report", "competitor analysis", "market landscape", "dossier"]},
    "soowei":           {"domain": "strategy", "owns": "consulting-leverage", "use": "Founder workflow, scale architecture, leverage auditing", "signals": ["consulting", "leverage", "founder workflow", "scale architecture", "scale myself", "doing too much", "founder bottleneck"]},
    "lulu-cheng":       {"domain": "strategy", "owns": "communications", "use": "PR strategy, crisis communications, reputation management", "signals": ["pr", "crisis", "communications", "reputation", "media coverage", "press release", "public relations", "bad press", "controversy"]},
    "mike-foutia":      {"domain": "strategy", "owns": "marketing-tools", "use": "Marketing technology landscape, tool selection", "signals": ["marketing tool", "tool selection", "martech", "which tool", "best software", "tech stack", "marketing stack"]},
    "evan-spiegel":     {"domain": "strategy", "owns": "distribution-architecture", "use": "Distribution-first product strategy, moat construction, dual-org innovation, ecosystem building, founder evolution", "signals": ["distribution", "moat", "ecosystem", "platform", "defensibility", "distribution first", "build a moat", "competitors copying", "dual-org", "innovation engine", "founder evolution", "product architecture", "network density", "close friends", "design bottleneck", "screenshot mindset", "impossible constraint", "jtbd agents", "listen don't obey", "empathy sprint", "loonshots"]},

    # Domain 13: Audience & Growth
    "tyler-denk":       {"domain": "audience", "owns": "newsletter", "use": "BDE system, referral engineering, social launch sequences", "signals": ["newsletter", "referral", "subscriber", "beehiiv", "email list", "start newsletter", "launch newsletter", "grow newsletter", "newsletter growth", "referral program", "subscriber growth"]},
    "ali-abdaal":       {"domain": "audience", "owns": "action-bias", "use": "Two-way door thinking, experiment-driven growth", "signals": ["overthinking", "action", "two-way door", "experiment", "analysis paralysis", "just start", "can't decide", "perfectionism", "shipping"]},
    "seth-godin":       {"domain": "audience", "owns": "idea-propagation", "use": "Virusworthiness, sneeze-network design, permission marketing", "signals": ["idea virus", "permission marketing", "tribe", "movement", "remarkability", "word of mouth", "spread", "build a tribe", "start a movement", "remarkable"]},

    # Domain 14: Mindset, Messaging & Consciousness
    "jeremy-haynes":    {"domain": "mindset", "owns": "identity-systems", "use": "Identity-governs-everything, mindset rewiring", "signals": ["identity system", "mindset rewiring", "identity governs", "become the person", "identity shift", "level up"]},
    "david-bayer":      {"domain": "mindset", "owns": "presence-performance", "use": "Elevated presence, performance optimization", "signals": ["presence", "performance", "elevated", "elite communication", "executive presence", "show up differently", "be more present"]},
    "donald-miller":    {"domain": "mindset", "owns": "culture-messaging", "use": "PEACE framework, culture turnaround, strategic messaging", "signals": ["culture", "peace framework", "storybrand", "messaging", "culture turnaround", "company culture", "team messaging", "brand message", "clarify my message"]},
    "heath-brothers":   {"domain": "mindset", "owns": "idea-stickiness", "use": "SUCCESs framework, schema violation, commander's intent", "signals": ["sticky", "success framework", "schema violation", "stickiness", "memorable", "stick in their mind", "make it memorable", "unforgettable"]},
    "joscha-bach":      {"domain": "mindset", "owns": "consciousness", "use": "Computational phenomenology, identity engineering, phase transition", "signals": ["consciousness", "phenomenology", "phase transition", "mechanism", "philosophy of mind", "how does this work", "what is the mechanism", "systems thinking", "first principles"]},
    "dr-k":             {"domain": "mindset", "owns": "vedantic-psychology", "use": "Samskara, guna diagnosis, emotional processing, dharma, creative blocks", "signals": ["samskara", "guna", "vedantic", "dharma", "emotional processing", "stuck", "blocked", "creative block", "can't focus", "procrastination", "overwhelmed", "paralyzed", "mental block", "burned out", "lost", "confused", "don't know what to do", "anxious about creating", "imposter syndrome", "self-doubt"]},

    # Domain 15: Industry-Specific
    "joshua-smith":     {"domain": "industry", "owns": "real-estate-production", "use": "KPI-driven production, market agnosticism", "signals": ["real estate production", "kpi", "real estate agent", "real estate business", "listings", "closings", "real estate team"]},
    "enrico-incarnati": {"domain": "industry", "owns": "real-estate-instagram", "use": "Instagram content strategy, lead generation for agents", "signals": ["real estate instagram", "instagram agent", "real estate content", "realtor instagram", "agent content", "realtor marketing"]},
    "jonathan-courtney": {"domain": "industry", "owns": "design-thinking", "use": "UX sprints, design process, product design", "signals": ["ux sprint", "design thinking", "product design", "design sprint", "rapid prototyping", "user testing"]},
    "sabri-suby":       {"domain": "industry", "owns": "paid-advertising", "use": "AI-powered ads, direct response marketing, campaign scaling", "signals": ["paid ads", "ad campaign", "campaign scaling", "paid advertising", "facebook ads", "google ads", "meta ads", "ad spend", "roas", "run ads"]},
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
    "control-plane": "Control Plane & Orchestration",
}


CONTROL_PLANE_RESULTS = [
    (
        120.0,
        "operator-autopilot",
        {
            "domain": "control-plane",
            "owns": "intent-lock",
            "use": "Plan-first front door, visible routing trace, approval checkpoint, and runtime preflight",
        },
    ),
    (
        110.0,
        "antigravity-orchestrator",
        {
            "domain": "control-plane",
            "owns": "routing-menu",
            "use": "Ranked execution menu and route comparison when options are explicitly requested",
        },
    ),
    (
        100.0,
        "evolution-agent",
        {
            "domain": "control-plane",
            "owns": "measured-repair",
            "use": "Failure-evidence repair, verifier-backed evolution, and anti-bloat improvement loops",
        },
    ),
]


# ─────────────────────────────────────────────────────────
# SYNONYM MAP — Expands user language to system signals
# ~200 terms covering the most common natural-language gaps
# ─────────────────────────────────────────────────────────

SYNONYMS = {
    # Writing & Books
    "memoir": ["story", "narrative", "book", "fiction", "writing", "life story", "autobiography", "personal essay"],
    "book": ["novel", "memoir", "manuscript", "writing", "fiction", "chapter"],
    "write": ["create", "draft", "compose", "craft", "produce"],
    "writing": ["prose", "copy", "content", "narrative", "text"],
    "autobiography": ["memoir", "life story", "personal narrative", "story"],
    "biography": ["profile writing", "portrait", "life story"],
    "chapter": ["section", "part", "book"],
    "novel": ["fiction", "book", "manuscript"],
    "poem": ["poetry", "verse", "lyrical", "estrangement"],
    "poetry": ["verse", "lyrical", "estrangement", "perceptual"],
    "script": ["screenplay", "scene", "dialogue"],
    "scene": ["vignette", "dialogue", "setting", "vivid"],

    # Emotional States & Blocks
    "stuck": ["blocked", "overwhelmed", "procrastination", "can't start", "paralyzed", "resistance", "creative block"],
    "blocked": ["stuck", "resistance", "creative block", "can't start", "procrastination"],
    "overwhelmed": ["stuck", "too much", "paralyzed", "burned out", "can't focus"],
    "confused": ["lost", "don't know", "unclear", "overwhelmed", "stuck"],
    "anxious": ["worried", "nervous", "afraid", "scared", "imposter syndrome"],
    "burned out": ["exhausted", "overwhelmed", "tired", "no energy"],
    "imposter": ["self-doubt", "not good enough", "fraud", "imposter syndrome"],
    "afraid": ["scared", "fear of creating", "nervous", "resistance"],
    "procrastinating": ["procrastination", "avoiding", "stuck", "can't start"],
    "lost": ["confused", "don't know", "stuck", "directionless"],
    "unmotivated": ["stuck", "procrastination", "resistance", "can't start"],

    # Business Actions
    "launch": ["start", "begin", "create", "build", "ship", "go live"],
    "start": ["launch", "begin", "create", "build", "from scratch"],
    "build": ["create", "make", "design", "develop", "construct"],
    "grow": ["scale", "expand", "increase", "build", "growth"],
    "scale": ["grow", "expand", "multiply", "increase"],
    "sell": ["close", "convert", "monetize", "sales", "revenue"],
    "monetize": ["make money", "revenue", "profit", "sell", "income"],
    "validate": ["test", "market validation", "prove", "verify"],
    "improve": ["optimize", "enhance", "upgrade", "fix", "better"],
    "fix": ["repair", "improve", "solve", "debug", "troubleshoot"],

    # Business Entities
    "coaching": ["consulting", "mentoring", "training", "advisory", "coaching business"],
    "consulting": ["coaching", "advisory", "services", "consulting business"],
    "agency": ["firm", "company", "consulting", "services"],
    "freelance": ["independent", "contract", "solo", "self-employed"],
    "business": ["company", "venture", "enterprise", "startup"],
    "startup": ["business", "venture", "company"],
    "side hustle": ["side business", "freelance", "extra income"],

    # Content & Marketing
    "content": ["posts", "articles", "media", "material", "content strategy"],
    "post": ["content", "article", "update", "share"],
    "viral": ["trending", "go viral", "blow up", "spread"],
    "trending": ["viral", "popular", "hot", "trending topic"],
    "hook": ["attention", "opening", "scroll-stopping", "intro"],
    "headline": ["title", "subject line", "heading", "hook"],
    "caption": ["post", "copy", "text", "description"],
    "thread": ["twitter thread", "carousel", "multi-part"],
    "carousel": ["slide", "swipe", "multi-image post"],
    "reel": ["reels", "short-form", "tiktok", "shorts", "vertical video"],
    "newsletter": ["email", "email list", "subscriber", "email marketing"],
    "email": ["newsletter", "email sequence", "email marketing", "autoresponder"],
    "blog": ["article", "post", "website content", "long-form"],
    "podcast": ["audio", "show", "episode", "interview"],

    # Platforms
    "linkedin": ["linkedin post", "linkedin content", "linkedin growth", "linkedin strategy", "b2b linkedin"],
    "instagram": ["ig", "instagram content", "instagram strategy", "instagram marketing", "reels"],
    "tiktok": ["short-form", "viral video", "reels", "shorts"],
    "youtube": ["video", "channel", "long-form video", "youtube strategy"],
    "twitter": ["x", "tweets", "thread"],
    "substack": ["newsletter", "email", "paid newsletter"],

    # Sales & Revenue
    "clients": ["customers", "buyers", "prospects", "leads"],
    "leads": ["prospects", "pipeline", "potential customers", "inquiries"],
    "customers": ["clients", "buyers", "users"],
    "prospects": ["leads", "potential clients", "pipeline"],
    "close": ["sell", "win", "convert", "closing"],
    "objection": ["pushback", "resistance", "concern", "hesitation"],
    "pitch": ["present", "sell", "proposal", "offer"],
    "proposal": ["pitch", "offer", "quote", "bid"],
    "price": ["pricing", "cost", "rate", "fee", "how much"],
    "pricing": ["price", "cost", "rates", "fee structure"],
    "revenue": ["income", "money", "earnings", "profit"],
    "profit": ["revenue", "margin", "earnings", "bottom line"],

    # Products & Offers
    "course": ["program", "training", "curriculum", "digital product", "online course"],
    "product": ["offer", "service", "solution", "digital product"],
    "offer": ["product", "package", "service", "deal", "offer design"],
    "program": ["course", "membership", "coaching program", "container"],
    "membership": ["subscription", "community", "recurring", "monthly"],
    "template": ["blueprint", "framework", "swipe file", "system"],
    "lead magnet": ["freebie", "opt-in", "free resource", "download"],
    "freebie": ["lead magnet", "free resource", "giveaway"],
    "funnel": ["pipeline", "conversion path", "sales process"],
    "landing page": ["sales page", "opt-in page", "squeeze page"],

    # Brand & Identity
    "brand": ["personal brand", "reputation", "identity", "image"],
    "personal brand": ["brand", "online presence", "digital presence", "reputation"],
    "niche": ["market", "specialization", "focus", "target"],
    "audience": ["followers", "community", "readers", "subscribers", "fan base"],
    "followers": ["audience", "subscribers", "fans", "community"],
    "community": ["tribe", "audience", "group", "members"],
    "unique": ["different", "stand out", "original", "differentiation"],
    "original": ["unique", "fresh", "novel", "creative"],
    "voice": ["tone", "style", "personality", "brand voice"],
    "tone": ["voice", "style", "vibe", "energy"],
    "credibility": ["authority", "trust", "proof", "reputation"],
    "authority": ["credibility", "expert status", "thought leader"],

    # Design & Visual
    "design": ["visual", "aesthetic", "creative", "graphics"],
    "website": ["site", "web", "landing page", "online presence"],
    "logo": ["brand identity", "visual identity", "brand mark"],
    "aesthetic": ["look", "vibe", "visual style", "design"],
    "beautiful": ["stunning", "premium", "polished", "aesthetic"],

    # AI & Technology
    "ai": ["artificial intelligence", "machine learning", "automation", "gpt"],
    "automate": ["automation", "workflow", "systemize", "hands-off"],
    "automation": ["automate", "workflow", "system", "automated"],
    "agent": ["ai agent", "bot", "assistant", "autonomous"],
    "prompt": ["prompt engineering", "system prompt", "instruction"],

    # Strategy & Decisions
    "strategy": ["plan", "approach", "roadmap", "game plan"],
    "plan": ["strategy", "roadmap", "blueprint", "game plan"],
    "decide": ["choose", "pick", "select", "figure out"],
    "help": ["assist", "support", "guide", "advise"],
    "advice": ["guidance", "recommendation", "counsel", "direction"],

    # Audience Understanding
    "customer": ["client", "buyer", "prospect", "user", "consumer"],
    "target": ["audience", "niche", "market", "ideal customer"],
    "persona": ["avatar", "profile", "archetype", "icp"],
    "avatar": ["persona", "ideal customer", "target audience", "buyer profile"],
    "research": ["analyze", "investigate", "study", "intelligence"],

    # SEO & Discovery
    "seo": ["search engine", "google", "ranking", "organic traffic"],
    "rank": ["seo", "position", "search results", "google ranking"],
    "traffic": ["visitors", "views", "clicks", "impressions"],

    # Video & Media
    "video": ["film", "clip", "footage", "motion"],
    "edit": ["cut", "polish", "refine", "revise"],
    "thumbnail": ["cover", "preview", "image"],

    # Ambiguous / Vague Queries
    "help me": ["guide", "assist", "advise"],
    "need help": ["guide", "assist", "don't know"],
    "don't know": ["confused", "lost", "stuck", "unsure"],
    "what should i": ["decide", "recommend", "guide", "advise"],
    "how do i": ["help", "guide", "teach", "show me"],
    "not working": ["broken", "failing", "underperforming", "fix"],
    "getting started": ["beginner", "from scratch", "new to", "start"],
    "beginner": ["new", "starting", "just starting", "novice"],
    "expert": ["advanced", "professional", "mastery", "senior"],
    "make money": ["monetize", "revenue", "income", "earn"],
    "passive income": ["recurring revenue", "digital product", "course"],
    "side project": ["side hustle", "hobby", "passion project"],
}

# ─────────────────────────────────────────────────────────
# TRIAGE PATHS — Fallback routing for vague/zero-match queries
# ─────────────────────────────────────────────────────────

TRIAGE_PATHS = [
    {
        "pattern": ["stuck", "blocked", "overwhelmed", "can't", "lost", "confused", "burned", "anxious", "imposter", "afraid", "scared", "don't know", "unsure", "paralyzed"],
        "recommendation": {
            "type": "triage",
            "expert": "dr-k",
            "workflow": "/drk-triage",
            "reason": "Emotional/mindset state detected — start with emotional processing before tactical work",
            "alternatives": ["steven-pressfield (if creative block)", "ali-abdaal (if analysis paralysis)", "joscha-bach (if existential/philosophical)"]
        }
    },
    {
        "pattern": ["help me", "need help", "don't know what", "where do i start", "what should i", "recommend", "suggest"],
        "recommendation": {
            "type": "discovery",
            "expert": None,
            "workflow": "/refine-intent",
            "reason": "Vague intent detected — use discovery mode to narrow down what you need",
            "alternatives": ["Browse domains: copywriting, content, brand, sales, products, writing, design, ai"]
        }
    },
    {
        "pattern": ["decide", "choosing", "which one", "option", "trade-off", "versus", "compare"],
        "recommendation": {
            "type": "triage",
            "expert": "jim-oshaughnessy",
            "workflow": None,
            "reason": "Decision-making query — cross-domain synthesis expert",
            "alternatives": ["ali-abdaal (two-way door thinking for reversible decisions)"]
        }
    },
    {
        "pattern": ["just starting", "beginner", "new to", "getting started", "from scratch", "zero", "no experience"],
        "recommendation": {
            "type": "triage",
            "expert": "ai-chris-lee",
            "workflow": "/zero-to-brand",
            "reason": "Beginner state detected — zero-proof expert + brand bootstrap workflow",
            "alternatives": ["caleb-ralston (positioning from zero)", "dan-koe (one-person business model)"]
        }
    },
]


# ─────────────────────────────────────────────────────────
# PREREQUISITES — Workflow dependency chains (Fusion 4: Stack Order Intelligence)
# Source: Luke Iha HK8 "Stack Order Matters", Kallaway "Articulation Stack"
# ─────────────────────────────────────────────────────────

PREREQUISITES = {
    # Copy workflows need offer/positioning first
    "proof-copy-engine": ["design-digital-product-offer", "storybrand"],
    "nuclear-vsl": ["mechanism-discover", "storybrand"],
    "full-stack-ad": ["mechanism-discover", "mechanism-validate"],
    "proof-pipeline": ["proof-ladder-builder"],
    "proof-stacked-ad-builder": ["proof-ladder-builder"],
    "obsession-copy-engine": ["storybrand", "icp-deep-dive"],
    "haunt-copy": ["storybrand", "one-liner"],
    # Content workflows need strategy first
    "atomize": ["any long-form content"],
    "content-bundle": ["any finished content"],
    "launch-day": ["content-series-plan"],
    "parallel-content": ["content-style-card", "brand-arena"],
    # Campaign/mission workflows need brief first
    "campaign": ["brief", "storybrand"],
    "jcc-deploy": ["brief"],
    "strike": ["brief"],
    # Hook workflows need core message
    "vicious-hook": ["storybrand", "one-liner"],
    "vicious-hook-sprint": ["storybrand"],
    "hook-forge": ["one-liner"],
    # Ad workflows need mechanism
    "mechanism-copy": ["mechanism-discover", "mechanism-validate"],
    "mechanism-sprint": ["mechanism-discover"],
    "cash-method": ["mechanism-discover", "icp-deep-dive"],
    # Launch workflows need offer
    "high-ticket-launch": ["design-digital-product-offer", "storybrand"],
    "platform-launch": ["brand-arena", "content-style-card"],
}

# ─────────────────────────────────────────────────────────
# AWARENESS STAGES — User readiness classifier (Fusion 2)
# Source: Joanna Wiebe/Schwartz awareness model, Growth Ecosystems
# ─────────────────────────────────────────────────────────

AWARENESS_SIGNALS = {
    "unaware": {
        "patterns": ["bored", "something feels off", "not sure what", "don't know where to start",
                     "what should i do", "lost", "no idea", "blank slate", "help me figure out",
                     "not sure what i need", "don't know what i want"],
        "routing": "discovery_mode",
        "description": "Doesn't yet know they have a solvable problem"
    },
    "problem_aware": {
        "patterns": ["not working", "failing", "underperforming", "struggling with", "can't seem to",
                     "broken", "stalled", "declining", "losing", "my content isn't", "my sales are",
                     "why isn't", "what's wrong with", "diagnose", "audit"],
        "routing": "diagnostic_first",
        "description": "Knows something is wrong, doesn't know the fix"
    },
    "solution_aware": {
        "patterns": ["i need a", "i want to", "help me build", "create a", "write a",
                     "how do i", "i'm trying to", "looking for", "need to figure out",
                     "strategy for", "plan for", "system for"],
        "routing": "standard_routing",
        "description": "Knows the category of solution needed"
    },
    "product_aware": {
        "patterns": ["should i use", "which is better", "versus", "compare", "difference between",
                     "storybrand or", "insight vectors or", "which expert", "which workflow",
                     "cole or", "kallaway or"],
        "routing": "comparison_mode",
        "description": "Knows specific tools/experts, choosing between them"
    },
    "most_aware": {
        "patterns": ["run /", "deploy /", "execute /", "load @", "use @", "run the",
                     "do /", "start /", "give me /"],
        "routing": "instant_execution",
        "description": "Knows exactly what they want — bypass recommendation"
    },
}

# ─────────────────────────────────────────────────────────
# EMOTIONAL SUBTEXT — Hidden emotional states in tactical asks (Fusion 5)
# Source: McRaney "Emotional Processing Precedes Cognitive Change", Dr. K
# ─────────────────────────────────────────────────────────

EMOTIONAL_SUBTEXT_PATTERNS = [
    {
        "patterns": ["tried everything", "nothing works", "i've tried", "no matter what i do"],
        "emotion": "exhaustion",
        "pre_expert": "dr-k",
        "pre_workflow": "/drk-triage",
        "message": "Exhaustion detected — emotional processing before tactical deployment"
    },
    {
        "patterns": ["everyone else", "others seem to", "people like me don't", "not good enough",
                     "imposter", "fraud", "who am i to"],
        "emotion": "imposter_syndrome",
        "pre_expert": "dr-k",
        "pre_workflow": "/drk-identity-rebuild",
        "message": "Imposter pattern detected — identity work before skill deployment"
    },
    {
        "patterns": ["keep starting over", "can't finish", "always restarting", "never complete",
                     "start but don't finish", "procrastinate"],
        "emotion": "resistance",
        "pre_expert": "steven-pressfield",
        "pre_workflow": "/resistance",
        "message": "Resistance pattern detected — Pressfield diagnosis before production"
    },
    {
        "patterns": ["should i even", "is it worth", "does it matter", "what's the point",
                     "why bother", "giving up", "want to quit"],
        "emotion": "existential_doubt",
        "pre_expert": "dr-k",
        "pre_workflow": "/drk-dharma",
        "message": "Existential doubt detected — purpose work before tactical execution"
    },
    {
        "patterns": ["too many options", "analysis paralysis", "can't decide", "overwhelmed by choices",
                     "which one", "there are so many"],
        "emotion": "decision_paralysis",
        "pre_expert": "jim-oshaughnessy",
        "pre_workflow": "/refine-intent",
        "message": "Decision paralysis detected — narrowing before deploying"
    },
    {
        "patterns": ["nobody reads", "nobody buys", "no engagement", "crickets", "zero traction",
                     "invisible", "shouting into void"],
        "emotion": "frustration_rejection",
        "pre_expert": "dr-k",
        "pre_workflow": "/drk-emotional",
        "message": "Rejection frustration detected — emotional clearing before strategy pivot"
    },
]

# ─────────────────────────────────────────────────────────
# REVENUE DISTANCE — Steps from income (Fusion 7)
# Source: Grace Andrews HK-9 "Revenue Sequencing Gate", Lara Acosta "Revenue Bridge"
# ─────────────────────────────────────────────────────────

REVENUE_DISTANCE = {
    # Distance 0: Directly produces revenue
    0: ["david-deutsch", "cardinal-mason", "alen-sultanic", "stefan-georgi",
        "jeremy-miner", "monk-ai", "joanna-wiebe", "bond-halbert",
        "nicolas-cole-client", "samuel-thompson", "maria-wendt"],
    # Distance 1: One step from revenue (content/leads that convert)
    1: ["luke-iha", "kallaway", "lara-acosta", "sabrina-ramonov",
        "proof-engineering", "growth-ecosystems", "adam-enfroy",
        "seena-rez", "harry-dry", "nicolas-cole", "paul-james"],
    # Distance 2: Two steps (strategy/positioning → content → revenue)
    2: ["april-dunford", "donald-miller", "shaan-puri", "caleb-ralston",
        "jun-yuh", "grace-andrews", "brock-johnson", "authority-hacker",
        "dai-media", "tom-noske", "shan-hanif", "seth-godin"],
    # Distance 3: Foundation (identity/niche → positioning → ...)
    3: ["dr-k", "michael-bernoff", "steven-pressfield", "joscha-bach",
        "ali-abdaal", "jim-oshaughnessy", "nate-b-jones", "nick-saraev",
        "self-evolving", "skill-creator", "ai-chris-lee", "dan-koe"],
}

# Build reverse lookup
EXPERT_REVENUE_DISTANCE = {}
for dist, experts in REVENUE_DISTANCE.items():
    for exp in experts:
        EXPERT_REVENUE_DISTANCE[exp] = dist


def _stem(word):
    """Minimal suffix-strip stemmer for signal matching."""
    for suffix in ("ing", "tion", "ness", "ally", "ment", "ive", "ity", "ly", "ed", "er", "es", "s"):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            return word[: -len(suffix)]
    return word


def _expand_query(query):
    """Expand query with synonyms for broader matching."""
    query_lower = query.lower()
    expansions = set()
    
    # Check multi-word synonyms first (longest match wins)
    for term, synonyms in sorted(SYNONYMS.items(), key=lambda x: -len(x[0])):
        if term in query_lower:
            for syn in synonyms:
                expansions.add(syn)
    
    # Check single-word matches
    for word in query_lower.split():
        if word in SYNONYMS:
            for syn in SYNONYMS[word]:
                expansions.add(syn)
    
    # Combine original query with expansions
    expanded = query_lower
    if expansions:
        expanded = f"{query_lower} {' '.join(expansions)}"
    
    return expanded


def _generate_triage(query):
    """Generate triage recommendations for vague/zero-match queries."""
    query_lower = query.lower()
    matches = []
    
    for triage in TRIAGE_PATHS:
        match_count = sum(1 for p in triage["pattern"] if p in query_lower)
        if match_count > 0:
            matches.append((match_count, triage["recommendation"]))
    
    matches.sort(key=lambda x: -x[0])
    return matches


def _is_control_plane_failure(query):
    """Detect harness/control-plane failure before persona scoring leaks in."""
    try:
        import routing_governor
    except ImportError:
        routing_governor = None

    query_lower = query.lower()
    if routing_governor and routing_governor.is_system_failure_intent(query_lower):
        return True

    failure_terms = (
        "system is broken",
        "harness is broken",
        "fix everything",
        "fix the rest",
        "whatever is not fixed",
        "get fixed now",
        "repair everything",
        "repair the system",
        "repair the harness",
        "bigger repair",
        "up to the standard",
        "standard and quality",
        "not working as envisioned",
        "things are not working",
        "orchestration is useless",
        "autopilot is useless",
        "routing is broken",
        "failure modes",
    )
    context_terms = (
        "harness",
        "autopilot",
        "orchestration",
        "orchestrate",
        "routing",
        "workflow",
        "workflows",
        "skill",
        "skills",
        "system",
    )
    broad_repair = any(
        term in query_lower
        for term in (
            "fix everything",
            "whatever is not fixed",
            "get fixed now",
            "repair everything",
            "bigger repair",
            "up to the standard",
            "standard and quality",
        )
    )
    return broad_repair or any(term in query_lower for term in failure_terms) and any(
        term in query_lower for term in context_terms
    )


def route(query, top_n=5):
    """Route a problem description to the best expert(s).
    
    Uses synonym expansion to bridge natural language to expert signals.
    Falls back to triage paths when no experts score above threshold.
    """
    if _is_control_plane_failure(query):
        return CONTROL_PLANE_RESULTS[:top_n]

    query_lower = query.lower()
    # Expand query with synonyms for broader matching
    expanded_query = _expand_query(query)
    expanded_words = expanded_query.split()
    expanded_stems = [_stem(w) for w in expanded_words]
    # Build bigrams from original query words (not expanded — too noisy)
    original_words = query_lower.split()
    query_bigrams = [f"{original_words[i]} {original_words[i+1]}" for i in range(len(original_words) - 1)]
    # Also build bigrams from expanded for multi-word signal matching
    expanded_bigrams = [f"{expanded_words[i]} {expanded_words[i+1]}" for i in range(len(expanded_words) - 1)]
    all_bigrams = list(set(query_bigrams + expanded_bigrams))

    scored = []

    for name, info in EXPERTS.items():
        score = 0

        for signal in info["signals"]:
            # 1. Exact substring match against original query (strongest)
            if signal in query_lower:
                score += len(signal.split()) * 3
                continue

            # 1b. Exact substring match against expanded query (strong, discounted)
            if signal in expanded_query:
                score += len(signal.split()) * 2
                continue

            # 2. Bigram overlap: check if query bigrams match signal
            signal_words = signal.split()
            if len(signal_words) >= 2:
                for bigram in all_bigrams:
                    bigram_stems = [_stem(w) for w in bigram.split()]
                    signal_stems = [_stem(w) for w in signal_words]
                    overlap = sum(1 for bs in bigram_stems if any(bs in ss or ss in bs for ss in signal_stems if len(ss) > 2))
                    if overlap >= 2:
                        score += len(signal_words) * 2
                        break

            # 3. Individual signal-word overlap (weakest, fractional)
            for sw in signal_words:
                if len(sw) < 3:
                    continue
                sw_stem = _stem(sw)
                for qs in expanded_stems:
                    if len(qs) < 3:
                        continue
                    if sw_stem in qs or qs in sw_stem:
                        score += 0.5
                        break

        # Also check if any query words appear in name, owns, or use
        for word in original_words:
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


def format_route_output(results, compounds=None, query=None):
    """Format routing results for display."""
    if not results:
        # Triage fallback
        print("No direct expert matches found.")
        if query:
            triage_matches = _generate_triage(query)
            if triage_matches:
                print("\n🔀 Triage Recommendations:\n")
                for _, rec in triage_matches:
                    if rec["expert"]:
                        expert_info = EXPERTS.get(rec["expert"], {})
                        domain_label = DOMAIN_LABELS.get(expert_info.get("domain", ""), "")
                        print(f"  @{rec['expert']:25s} [{domain_label}]")
                    if rec["workflow"]:
                        print(f"    Workflow: {rec['workflow']}")
                    print(f"    Reason:   {rec['reason']}")
                    if rec.get("alternatives"):
                        print(f"    Also try: {', '.join(rec['alternatives'])}")
                    print()
            else:
                print("\n💡 Try one of these approaches:")
                print("  • Run /refine-intent to sharpen your request")
                print("  • Browse a domain: python3 execution/expert_router.py domains")
                print("  • Describe what you want to CREATE, SELL, GROW, or FIX")
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


# ─────────────────────────────────────────────────────────
# INTELLIGENCE FUNCTIONS — Power the /recommend fusion layers
# ─────────────────────────────────────────────────────────

def classify_awareness(query):
    """Classify user awareness stage (Schwartz model).
    Returns dict with stage, routing behavior, description, and confidence."""
    q = query.lower()
    best_stage = None
    best_count = 0

    for stage, info in AWARENESS_SIGNALS.items():
        hits = sum(1 for p in info["patterns"] if p in q)
        if hits > best_count:
            best_count = hits
            best_stage = stage

    if best_stage is None:
        # Default to solution_aware (most common)
        best_stage = "solution_aware"
        best_count = 0

    info = AWARENESS_SIGNALS[best_stage]
    return {
        "stage": best_stage,
        "routing": info["routing"],
        "description": info["description"],
        "confidence": min(best_count / 2.0, 1.0),  # 2+ hits = full confidence
    }


def detect_emotional_subtext(query):
    """Detect hidden emotional states in tactical questions.
    Returns list of detected emotional patterns with pre-expert prescriptions."""
    q = query.lower()
    detected = []

    for entry in EMOTIONAL_SUBTEXT_PATTERNS:
        hits = [p for p in entry["patterns"] if p in q]
        if hits:
            detected.append({
                "emotion": entry["emotion"],
                "matched_patterns": hits,
                "pre_expert": entry["pre_expert"],
                "pre_workflow": entry["pre_workflow"],
                "message": entry["message"],
            })

    return detected


def score_revenue_distance(expert_name):
    """Return revenue distance (0-3) for an expert.
    0 = directly produces revenue, 3 = foundational work."""
    name = expert_name.lower().strip().replace(" ", "-")

    # Direct lookup
    if name in EXPERT_REVENUE_DISTANCE:
        return EXPERT_REVENUE_DISTANCE[name]

    # Fuzzy match: try partial matches
    for exp_name, dist in EXPERT_REVENUE_DISTANCE.items():
        if name in exp_name or exp_name in name:
            return dist

    return -1  # Unknown expert


def check_prerequisites(workflow_name):
    """Check prerequisite chain for a workflow.
    Returns list of required precursor workflows, or empty list."""
    name = workflow_name.lower().strip().lstrip("/")
    return PREREQUISITES.get(name, [])


def diagnose(query):
    """Run full diagnostic: awareness + emotional subtext + revenue hints.
    Used by /recommend to get a complete pre-routing intelligence picture."""
    awareness = classify_awareness(query)
    emotions = detect_emotional_subtext(query)

    # Also run a quick route to get expert matches for revenue scoring
    results = route(query, top_n=3)
    revenue_scores = []
    for score, name, info in results:
        dist = score_revenue_distance(name)
        revenue_scores.append({
            "expert": name,
            "match_score": round(score, 2),
            "revenue_distance": dist,
        })

    return {
        "awareness": awareness,
        "emotional_subtext": emotions,
        "revenue_scores": revenue_scores,
    }


REVENUE_LABELS = {
    0: "Direct revenue (copy, ads, sales)",
    1: "One step (content → conversion)",
    2: "Two steps (strategy → content → revenue)",
    3: "Foundation (identity → positioning → ...)",
    -1: "Unknown",
}


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

    # New intelligence subcommands
    awareness_p = sub.add_parser("awareness", help="Classify awareness stage of a query")
    awareness_p.add_argument("query", help="User query to classify")

    emotion_p = sub.add_parser("emotion", help="Detect emotional subtext in a query")
    emotion_p.add_argument("query", help="User query to scan")

    revenue_p = sub.add_parser("revenue", help="Score revenue distance for an expert")
    revenue_p.add_argument("name", help="Expert name")

    prereq_p = sub.add_parser("prereqs", help="Check prerequisites for a workflow")
    prereq_p.add_argument("workflow", help="Workflow name (e.g., full-stack-ad)")

    diagnose_p = sub.add_parser("diagnose", help="Full pre-routing intelligence diagnostic")
    diagnose_p.add_argument("query", help="User query to diagnose")

    args = parser.parse_args()

    if args.command == "route":
        results = route(args.query, args.top)
        compounds = find_compounds(args.query)
        format_route_output(results, compounds, query=args.query)

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

    elif args.command == "awareness":
        result = classify_awareness(args.query)
        stage_emoji = {"unaware": "🌫️", "problem_aware": "🔍", "solution_aware": "🎯",
                       "product_aware": "⚖️", "most_aware": "⚡"}
        print(f"{stage_emoji.get(result['stage'], '❓')} Awareness: {result['stage'].upper()}")
        print(f"  Routing:     {result['routing']}")
        print(f"  Description: {result['description']}")
        print(f"  Confidence:  {result['confidence']:.0%}")

    elif args.command == "emotion":
        results = detect_emotional_subtext(args.query)
        if not results:
            print("✅ No emotional subtext detected — clear for tactical routing.")
        else:
            print(f"⚠️  {len(results)} emotional signal(s) detected:\n")
            for r in results:
                print(f"  🔴 {r['emotion'].upper()}")
                print(f"     Matched: {', '.join(r['matched_patterns'])}")
                print(f"     Pre-expert: @{r['pre_expert']} → {r['pre_workflow']}")
                print(f"     → {r['message']}")
                print()

    elif args.command == "revenue":
        dist = score_revenue_distance(args.name)
        label = REVENUE_LABELS.get(dist, "Unknown")
        emoji = {0: "💰", 1: "📈", 2: "🗺️", 3: "🏗️", -1: "❓"}.get(dist, "❓")
        print(f"{emoji} @{args.name}: Revenue Distance = {dist}")
        print(f"   {label}")

    elif args.command == "prereqs":
        prereqs = check_prerequisites(args.workflow)
        if not prereqs:
            print(f"✅ /{args.workflow} has no prerequisites — deploy immediately.")
        else:
            print(f"⚠️  /{args.workflow} requires these first:\n")
            for i, p in enumerate(prereqs, 1):
                print(f"  {i}. /{p}")
            print(f"\n  Recommended chain: {' → '.join('/' + p for p in prereqs)} → /{args.workflow}")

    elif args.command == "diagnose":
        result = diagnose(args.query)

        # Awareness
        aw = result["awareness"]
        stage_emoji = {"unaware": "🌫️", "problem_aware": "🔍", "solution_aware": "🎯",
                       "product_aware": "⚖️", "most_aware": "⚡"}
        print(f"━━━ INTELLIGENCE DIAGNOSTIC ━━━\n")
        print(f"{stage_emoji.get(aw['stage'], '❓')} Awareness: {aw['stage'].upper()} ({aw['confidence']:.0%})")
        print(f"  → {aw['description']}")
        print(f"  → Routing: {aw['routing']}")

        # Emotional subtext
        emotions = result["emotional_subtext"]
        if emotions:
            print(f"\n⚠️  EMOTIONAL SUBTEXT ({len(emotions)} signal{'s' if len(emotions) > 1 else ''}):")
            for e in emotions:
                print(f"  🔴 {e['emotion'].upper()} → @{e['pre_expert']} {e['pre_workflow']}")
        else:
            print(f"\n✅ No emotional subtext — clear for direct routing.")

        # Revenue proximity
        print(f"\n💰 REVENUE PROXIMITY:")
        for rs in result["revenue_scores"]:
            dist = rs["revenue_distance"]
            label = REVENUE_LABELS.get(dist, "Unknown")
            emoji = {0: "💰", 1: "📈", 2: "🗺️", 3: "🏗️", -1: "❓"}.get(dist, "❓")
            print(f"  {emoji} @{rs['expert']} (match: {rs['match_score']}) — distance {dist}: {label}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
