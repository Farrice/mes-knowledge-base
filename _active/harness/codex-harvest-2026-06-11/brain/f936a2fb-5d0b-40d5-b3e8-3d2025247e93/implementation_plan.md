# Grace Andrews Workflow Expansion — 14 New Workflows & Slash Commands

Expanding Grace Andrews from 5 workflows to 13 skill workflows + 6 system-level slash commands that cross-pollinate with marketing, copywriting, social media, and content strategy experts. Includes deep research integration and parallel swarm capabilities.

## Proposed Changes

### Grace Andrews Skill Workflows (8 new → total 13)

These live in `skills/grace-andrews-media-company/workflows/` and follow the completion-engine format (pre-flight check, numbered steps, quality gates, output format).

#### [NEW] `06-content-series-architect.md`
**Produces**: Multi-episode content series plan with narrative arc, cliffhangers, callbacks
**Cross-pollinates**: Shaan Puri (story structure), Kallaway (retention psychology)
Design episodic content series like a TV showrunner — each episode builds on the last, creates anticipation, and compounds audience investment. Uses Grace's city metaphor: each episode is a "bus route" that carries passengers deeper into the city.

#### [NEW] `07-media-company-blueprint.md`
**Produces**: Full creator-to-media-company transition blueprint with deep research enrichment
**Cross-pollinates**: Dan Koe (one-person business), Samuel Thompson (market validation), deep research engine
End-to-end media company architecture. Integrates deep research via Perplexity to ground the blueprint in real market data — comparable creators, revenue benchmarks, format trends. The "master plan" workflow.

#### [NEW] `08-attention-capture-map.md`
**Produces**: Platform-specific attention strategies mapped to city districts
**Cross-pollinates**: Seena Rez (TikTok hooks), Luke Iha (proof hooks), Lara Acosta (LinkedIn hooks), Jasmin Alic (trapdoor hooks)
Maps attention capture across every platform using Grace's districts. Each platform gets its own "street-level" hook strategy informed by the relevant hook expert. Prevents the "one hook style for all platforms" anti-pattern.

#### [NEW] `09-revenue-district-architect.md`
**Produces**: Revenue layer architecture with product ladders, trust thresholds, conversion pathways
**Cross-pollinates**: Nicolas Cole (product vehicles), Monk.AI (offer pyramid), Vincent Hu (growth ecosystem)
Designs the monetization district of the city map. When does content become revenue? What trust threshold must be crossed? What products map to which trust stages?

#### [NEW] `10-brand-voice-districts.md`
**Produces**: Brand voice map across awareness stages — different voice registers for different city "neighborhoods"
**Cross-pollinates**: Ghostwriting voice skills, Tommy Clark (founder voice), Lara Acosta (LinkedIn voice)
Your awareness-stage voice shouldn't sound the same as your trust-stage voice. Maps voice registers (casual → authoritative → intimate → closing) to city districts.

#### [NEW] `11-content-sprint-planner.md`
**Produces**: Weekly/monthly content production sprint with balanced district coverage
**Cross-pollinates**: Kieran Flanagan (content operations), Jun Yuh (content calendars)
Sprint-format content production ensuring balanced coverage across all city districts. Each sprint audits gap coverage and assigns content pieces to underserved districts. Prevents "all attention, no trust" or "all trust, no attention" imbalances.

#### [NEW] `12-competitive-city-analysis.md`
**Produces**: Competitive landscape mapped as rival "cities" with white-space opportunity heat map
**Cross-pollinates**: Parallel swarm (3-5 competing creators analyzed simultaneously), deep research
Uses parallel agents to map 3-5 competitors' content cities simultaneously — their districts, pathways, gaps. Outputs a white-space heat map showing which districts competitors underserve.

#### [NEW] `13-episodic-engine.md`
**Produces**: Recurring episodic content format with pilot episode, series bible, and production playbook
**Cross-pollinates**: Shaan Puri (narrative), Oscar Hoglund (audio narrative), Tao Prompts (video)
Designs recurring "shows" — not one-off content pieces. Produces a series bible (characters, themes, recurring elements), pilot episode script, and production playbook for maintaining quality across episodes.

---

### System-Level Slash Commands (6 new)

These live in `.agent/workflows/` and orchestrate cross-expert pipelines.

#### [NEW] `/grace-city-blueprint` → `.agent/workflows/grace-city-blueprint.md`
**Full end-to-end city build**: Deep research → City Map → Trust Pathways → Revenue District → 30-day calendar. The "one-shot media company" command. Chains workflows 01 + 02 + 09 + 11 with deep research pre-flight.

#### [NEW] `/grace-content-series` → `.agent/workflows/grace-content-series.md`
**Episodic content series from topic**: Research → Series Arc → Episode Plans → Hook Engineering → Production Calendar. Chains Grace's episodic engine + hook experts + content sprint.

#### [NEW] `/grace-vs-competitors` → `.agent/workflows/grace-vs-competitors.md`
**Competitive city analysis via parallel swarm**: Fires parallel agents to map 3-5 competitor content cities simultaneously. Outputs white-space opportunity report. Uses `parallel_swarm.py --grounded`.

#### [NEW] `/grace-to-copy` → `.agent/workflows/grace-to-copy.md`
**Grace → Copy pipeline**: Takes Grace's city strategy and hands off to copywriting experts. City Map districts → Cardinal Mason (email sequences per district), Luke Iha (proof stacking per trust stage), Lara Acosta (LinkedIn execution). The bridge from strategy to execution.

#### [NEW] `/grace-attention-swarm` → `.agent/workflows/grace-attention-swarm.md`
**Attention layer optimization swarm**: Parallel swarm fires Seena Rez (TikTok), Lara Acosta (LinkedIn), Brock Johnson (shareable social), Kallaway (YouTube) simultaneously against Grace's attention district. Each expert optimizes hooks for their platform, anchored in the city map strategy.

#### [NEW] `/grace-media-diagnostic` → `.agent/workflows/grace-media-diagnostic.md`
**Full diagnostic**: Content Portfolio Audit (workflow 04) + deep research on audience behavior + parallel swarm expert review. The "where am I losing people?" diagnostic that combines Grace's audit framework with live research data and multi-expert critique.

---

### Updates to Existing Files

#### [MODIFY] `skills/grace-andrews-media-company/SKILL.md`
Add all 8 new workflows to the workflow table and 6 new slash commands to the slash command table. Update `workflows: 5` to `workflows: 13`.

#### [MODIFY] `.agent/workflows/` (6 new files)
Create 6 new slash command workflow files.

---

## Verification Plan

### Automated Checks
```bash
# 1. Verify all 13 workflow files exist
ls -la skills/grace-andrews-media-company/workflows/

# 2. Verify all 6 slash command files exist
ls -la .agent/workflows/grace-*.md

# 3. Verify SKILL.md references all 13 workflows
grep -c "workflows/" skills/grace-andrews-media-company/SKILL.md

# 4. Re-run sync_registries to verify no index corruption
python3 execution/sync_registries.py
```

### Structural Verification
- Each skill workflow has: YAML frontmatter, pre-flight check, numbered steps, quality gates, output format
- Each slash command has: YAML frontmatter, description, usage example, steps referencing skill workflows
- SKILL.md workflow table has 13 entries, slash command table has 11 entries
- Cross-references between workflows are valid (e.g., workflow 07 references workflow 01)
