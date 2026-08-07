# Kieran Flanagan — AI Content Team Extraction & System Build

Build a full Antigravity skill + agent + 15 workflow commands from Kieran Flanagan's 11-skill, 5-layer AI Content Team methodology. This transforms Farrice's content creation pipeline with modular audience profiling, writing style cards, lookalike content discovery, content enrichment, and self-improving feedback loops.

## User Review Required

> [!IMPORTANT]
> **15 new workflow commands** are proposed below. Several interact with existing workflows — `/content-sprint`, `/atomize`, `/parallel-content`, `/ip-flywheel`. The new commands **enrich** these existing pipelines (e.g., `/content-enrich` can be called from `/content-sprint`), but none overwrite or modify them.

> [!IMPORTANT]
> **Platform-specific writing style cards** are a new concept. Currently Farrice has voice captures in `_active/linkedin/voice-captures/`. The new `/content-style-card` workflow creates structured per-platform style cards that the existing voice system can optionally reference, but does not replace the ghostwriting voice engine.

---

## Proposed Changes

### Extraction Report

#### [NEW] [extraction-report.md](file:///Users/farricecain/Google%20Antigravity/extractions/kieran-flanagan/extraction-report.md)

Deep-tier MES 3.0 extraction covering:
- **8 Genius Patterns**: Content-Reactive Profiling, Writing Style Modularity, Orchestrator-First Architecture, Lookalike Pattern Mining, Post Enrichment Pipeline, Feedback Loop Self-Improvement, Talking Point Categorization (Educational/Data/Spicy/Story), Vocabulary Library Design
- **6 Hidden Knowledge Items**: Platform-Specific Style Stacking, Messy Data → Profile methodology, Performance Threshold Filtering (top 30%), Enrichment Module Architecture, Autonomous Agent Vision, Identity Vocabulary Mapping
- **Applied Intelligence**: How every pattern maps to Farrice's existing system and what new capabilities it unlocks

---

### Skill Directory

#### [NEW] [SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/kieran-flanagan-content-teams/SKILL.md)

```
skills/kieran-flanagan-content-teams/
├── SKILL.md                    # Completion engine index
├── genius.md                   # Unified genius context
└── workflows/
    ├── 01-content-audience-profile.md
    ├── 02-content-style-card.md
    ├── 03-talking-points.md
    ├── 04-lookalike-content.md
    ├── 05-content-enrich.md
    ├── 06-content-bundle.md
    ├── 07-content-orchestrate.md
    ├── 08-content-feedback.md
    ├── 09-platform-adapt.md
    ├── 10-content-cluster.md
    ├── 11-hook-formula-extract.md
    ├── 12-content-series-plan.md
    ├── 13-competitor-content-spy.md
    ├── 14-content-review-cycle.md
    └── 15-style-from-creator.md
```

#### [NEW] [genius.md](file:///Users/farricecain/Google%20Antigravity/skills/kieran-flanagan-content-teams/genius.md)

Unified genius context merging all 8 patterns + 6 hidden knowledge items into a deployable context block. Structured around Kieran's 5 layers: Foundation (profile + style) → Research (talking points + lookalike) → Creation (platform drafts) → Enrichment (data/stories/quotes) → Optimization (feedback loops).

---

### 15 Workflow Commands

Each becomes a `.md` file in `.agent/workflows/` **and** a workflow inside the skill.

---

#### 1. `/content-audience-profile`
**Produces**: Content-reactive audience profile (not a traditional ICP)
**What it captures**: Jobs to be done, pain points, vocabulary library (what they say/don't say), emotional register, validation hooks, content they react to (based on engagement data)
**Kieran's insight**: "This is not like an ICP. This is content they react to, and it's all based on research and engagement data."
**Enriched by Perplexity research**: Hierarchical audience segmentation with emotional trigger mapping

---

#### 2. `/content-style-card`
**Produces**: Per-platform writing style card scraped from existing content
**What it captures**: Structural DNA (avg length, sections, paragraph style), hook formula, emotional playbook, what works/doesn't, vocabulary patterns
**Key innovation**: Multiple style cards per creator (Substack card ≠ LinkedIn card ≠ X card); can model any creator's style
**Stacks with**: Ghostwriting Voice Engine, Fresh Voice System

---

#### 3. `/talking-points`
**Produces**: Categorized talking points with creative spark labels
**Categories**: Educational, Data Nuggets, Spicy Takes, Story Sparks
**Sources**: Web research (Reddit, X, Perplexity), or user-provided content (YouTube videos, PDFs, articles)
**Output format**: Each talking point includes core insight, application, and recommended post type

---

#### 4. `/lookalike-content`
**Produces**: Content pattern profile + 15-25 new content ideas that match winning patterns
**Process**: Take messy data dump → filter top 30% by performance (if data available) → extract winning patterns (topic clusters, structural DNA, hook formulas, emotional playbook) → generate matching ideas with format recommendations
**Kieran's free skill**: This is the skill he gives away — the most powerful ideation engine in his system

---

#### 5. `/content-enrich`
**Produces**: Enrichment modules for any draft — data points, case studies, stories, quotes, real-world connections
**Process**: Takes a first draft → identifies enrichment opportunities → finds relevant data/examples/quotes → presents enrichment options to user → applies selected enrichments
**Stacks with**: `/content-sprint` Phase 5, `/writers-room`

---

#### 6. `/content-bundle`
**Produces**: Cross-platform content bundle from a single source idea
**Architecture**: One talking point → LinkedIn post + Newsletter section + X article + YouTube script outline
**Key difference from `/atomize`**: `/atomize` breaks existing long-form into derivatives. `/content-bundle` builds from a single idea outward with platform-native approaches.

---

#### 7. `/content-orchestrate`
**Produces**: Full content session using all skills in sequence
**Flow**: Load audience profile + writing style → Choose activity (research / create / enrich / review) → System automatically chains appropriate skills
**Kieran's insight**: "I just talk with the orchestrator and ask it to do things and it goes and uses all the other skills for you."

---

#### 8. `/content-feedback`
**Produces**: Performance analysis report + updated skill recommendations
**Process**: Ingest content performance data (impressions, engagement, saves, comments) → Analyze against created content → Identify winning/losing patterns → Update audience profile and style card recommendations
**System thinking**: "Most people stop here [at creation]. I have feedback loops that actually make the skills better."

---

#### 9. `/platform-adapt`
**Produces**: Platform-optimized version of any content piece
**Adapts for**: LinkedIn (F-shape, mobile-first), Newsletter (long-form, embedded value), X/Twitter (thread or article format), YouTube (script with retention hooks)
**Key difference from `/atomize`**: Deeper platform-native transformation, not just reformatting

---

#### 10. `/content-cluster`
**Produces**: Topic cluster analysis with performance mapping
**Analyzes**: Your content library to find which topic clusters drive the most engagement, which are underexplored, and where to double down
**Output**: Cluster map + gaps + recommended next topics per cluster

---

#### 11. `/hook-formula-extract`
**Produces**: Your personal hook formula library extracted from your best-performing content
**Process**: Analyze top-performing hooks → Classify by type (story, data, spicy, educational, contrarian) → Create reusable hook templates
**Stacks with**: `/hook-forge`, `/placek-hooks`

---

#### 12. `/content-series-plan`
**Produces**: Multi-part content series plan with thread continuity
**Process**: Take one big idea → Break into 5-7 sequential chapters → Map open loops between posts → Schedule across platforms
**Stacks with**: `/serial-arc`, Fresh Voice System

---

#### 13. `/competitor-content-spy`
**Produces**: Competitive content intelligence report
**Process**: Analyze competitor's content patterns (structure, topics, hooks, frequency) → Identify gaps (what they don't cover) → Generate differentiation opportunities
**Stacks with**: `/competitor-intel`

---

#### 14. `/content-review-cycle`
**Produces**: Monthly content system audit + skill updates
**Process**: Pull all content created this month → Analyze performance → Identify what the system got right/wrong → Propose specific skill updates → Execute approved updates
**Kieran's vision**: "A skill that improves my skills"

---

#### 15. `/style-from-creator`
**Produces**: Writing style card for any creator you want to learn from
**Process**: Scrape their public content (Substack, blog, X) → Analyze structural DNA, vocabulary, hook patterns → Create a reusable style card
**Use case**: "I create a writing style for me, but if you haven't created much content, you can create a writing style around someone you like and adjust it."

---

### Agent

#### [NEW] [AGENT.md](file:///Users/farricecain/Google%20Antigravity/agents/kieran-flanagan/AGENT.md)

Kieran Flanagan agent persona: HubSpot SVP of Marketing, systems thinker, content operations architect. Core competencies: content team architecture, audience profiling, feedback loop design, platform-native content strategy, autonomous content systems.

#### [NEW] [context.md](file:///Users/farricecain/Google%20Antigravity/agents/kieran-flanagan/memory/context.md)

Empty memory template, ready for project context.

---

### Registry Updates

#### [MODIFY] [AGENT_INDEX.md](file:///Users/farricecain/Google%20Antigravity/AGENT_INDEX.md)

Add Kieran Flanagan entry with skill link, domain, and available workflows.

#### [MODIFY] [SKILL_INDEX.md](file:///Users/farricecain/Google%20Antigravity/SKILL_INDEX.md)

Add `kieran-flanagan-content-teams` with 15 workflows, completion engine format.

---

## How This Stacks With Existing System

| Existing Workflow | Enhancement From Kieran |
|---|---|
| `/content-sprint` | Can now call `/content-enrich` in Phase 5 for automated data/story enrichment |
| `/atomize` | `/content-bundle` provides the complementary direction (idea → multi-platform vs. long-form → derivatives) |
| `/ip-flywheel` | `/content-orchestrate` can serve as the daily content operations layer feeding the IP Flywheel |
| `/parallel-content` | `/content-audience-profile` ensures all parallel outputs target the same audience identity |
| `/writers-room` | `/content-enrich` adds the data/case study enrichment layer the writers' room doesn't currently cover |
| `/hook-forge` | `/hook-formula-extract` mines YOUR hooks specifically, feeding `/hook-forge` with personalized data |
| `/serial-arc` | `/content-series-plan` extends serial planning to multi-platform series |
| `/watch-and-remix` | `/lookalike-content` is the data-driven version — pattern match from YOUR data, not just viral content |

---

## Verification Plan

### Automated Checks
1. **File structure verification**: Run `find skills/kieran-flanagan-content-teams -type f | wc -l` to confirm 17 files created (SKILL.md + genius.md + 15 workflows)
2. **Workflow registration**: `grep -c "content-audience-profile\|content-style-card\|talking-points\|lookalike-content\|content-enrich" .agent/workflows/*.md` to confirm all 15 workflow files exist
3. **Agent registration**: `grep "kieran-flanagan" AGENT_INDEX.md SKILL_INDEX.md` to confirm registry entries

### Manual Verification
1. **User reviews extraction report** at `extractions/kieran-flanagan/extraction-report.md` for accuracy and depth
2. **User selects one workflow** (recommend `/lookalike-content` as most impactful) to dry-run with real data
3. **User confirms no naming conflicts** with existing 255 workflow commands
