# Darrel Wilson — AI-Powered Affiliate Marketing Agent Pipeline

Build a complete expert agent from two Darrel Wilson YouTube videos, enriched with parallel swarm research, producing a deployable completion-engine skill with 5 end-to-end workflows and 5+ slash commands.

## Source Material

| Video | Title | Words | Key Topics |
|-------|-------|-------|------------|
| 1 | Affiliate Marketing for Beginners Is Now EASY | 3,882 | Affiliate fundamentals, program selection, traffic strategies, niche analysis, parasite SEO |
| 2 | 5 Clever Ways To Make Money Online With AI | 2,663 | AI lead gen, utility affiliate sites, selling AI websites, workflow monetization, AI apps |

**Expert**: Darrel Wilson — 10+ years affiliate marketing, $50-60K/month commissions, $500K+ earned from single programs, web design + AI automation specialist.

## Research Enrichment (Completed)

3 parallel Perplexity research swarms completed:
1. **Affiliate marketing best practices 2025-2026** — niches, commission rates, traffic ROI, funnels, email automation, scaling strategies
2. **AI monetization methods** — n8n workflows, micro-SaaS, AI website selling, workflow selling, lead gen systems
3. **Advanced affiliate strategies** — parasite SEO, content-to-tool pivots, white-label opportunities

---

## Proposed Changes

### Extraction Report
#### [NEW] [extraction-report.md](file:///Users/farricecain/Google%20Antigravity/extractions/darrel-wilson-affiliate-marketing/extraction-report.md)
Full MES 3.0 Standard extraction merging both videos + research enrichment. Includes genius patterns, hidden knowledge, applied intelligence analysis.

---

### Skill: `darrel-wilson-ai-affiliate`

#### [NEW] [SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/darrel-wilson-ai-affiliate/SKILL.md)
Completion engine skill file with expert context, workflow table, and quick reference.

#### [NEW] [genius.md](file:///Users/farricecain/Google%20Antigravity/skills/darrel-wilson-ai-affiliate/genius.md)
Unified genius context merging all patterns from both videos + research enrichment.

#### [NEW] 5 Workflow Files

| # | Workflow | Produces | Trigger |
|---|---------|----------|---------|
| 01 | `affiliate-program-selector` | Ranked list of optimal affiliate programs for any niche, with commission analysis + join strategy | "Which affiliate programs should I join?" |
| 02 | `ai-utility-site-builder` | Complete AI-powered utility website architecture (like currency converter, crypto analyzer) with embedded affiliate monetization | "Build me an affiliate site that's actually useful" |
| 03 | `ai-lead-gen-system` | Ready-to-deploy n8n/Make workflow for scraping RFPs, job boards, and leads with AI scoring | "Set up AI lead generation for my business" |
| 04 | `affiliate-traffic-engine` | Multi-channel traffic strategy with long-form video scripts, parasite SEO posts, and short-form content plan | "How do I get traffic to my affiliate offers?" |
| 05 | `ai-website-sales-pipeline` | Complete local business outreach system: AI site demos, pricing packages, email templates, and recurring revenue model | "Help me sell AI websites to local businesses" |

---

### Agent: `darrel-wilson`

#### [NEW] [AGENT.md](file:///Users/farricecain/Google%20Antigravity/agents/darrel-wilson/AGENT.md)
Full agent configuration with identity, competencies, decision framework, and workflow mapping.

#### [NEW] [memory/context.md](file:///Users/farricecain/Google%20Antigravity/agents/darrel-wilson/memory/context.md)
Initialized memory file.

---

### Slash Commands (5 new workflows)

| Command | Description |
|---------|-------------|
| `/affiliate-select` | Select optimal affiliate programs for any niche with commission analysis |
| `/ai-affiliate-site` | Design and architect an AI utility website with embedded affiliate monetization |
| `/ai-lead-scraper` | Build an AI lead generation workflow (n8n/Make) for any industry |
| `/affiliate-traffic` | Generate a complete multi-channel traffic strategy for affiliate offers |
| `/sell-ai-websites` | Build a local business AI website sales pipeline with outreach templates |

---

### Registration

#### [MODIFY] [AGENT_INDEX.md](file:///Users/farricecain/Google%20Antigravity/AGENT_INDEX.md)
Add Darrel Wilson agent entry.

#### [MODIFY] [SKILL_INDEX.md](file:///Users/farricecain/Google%20Antigravity/SKILL_INDEX.md)
Add `darrel-wilson-ai-affiliate` skill entry.

#### [MODIFY] [SLASH_COMMANDS.md](file:///Users/farricecain/Google%20Antigravity/SLASH_COMMANDS.md)
Add 5 new slash commands under appropriate category.

---

## Verification Plan

### Automated
- Confirm all new directories and files exist via `find`
- Verify SKILL.md has correct completion-engine frontmatter
- Verify all 5 workflow files follow the completion-engine format
- Grep AGENT_INDEX.md, SKILL_INDEX.md, and SLASH_COMMANDS.md for new entries

### Manual (User Review)
- **CHECKPOINT 1**: Review extraction report + proposed workflows (before building)
- **CHECKPOINT 2**: Review one sample workflow file for quality
- **Final**: Verify agent invocation works by describing an affiliate marketing task
