# Token Efficiency Audit — Antigravity System

**Date**: 2026-04-02 | **Requested by**: Farrice

---

## System Footprint Snapshot

| Component | Size | Files | Notes |
|-----------|------|-------|-------|
| **Skills** | 63 MB | 5,017 | Core knowledge base |
| **Workflows** | 1.9 MB | 399 | Slash commands |
| **Directives** | 388 KB | 47 | SOPs and protocols |
| **Agents** | 1.1 MB | 224 | Agent profiles + memory |
| **System Instructions** | 38 KB | 10 | CLAUDE.md, GEMINI.md, rules/ |
| **Total Markdown** | **46.8 MB** | **5,687** | Full system |

---

## Where Tokens Get Burned

### 1. Per-Request Fixed Cost (~38KB = ~9,500 tokens)

Every single message you send loads the system instruction files automatically:
- `AGENTS.md` / `CLAUDE.md`: ~12KB each
- `GEMINI.md` + `.gemini/rules/*.md`: ~14KB combined

**This is unavoidable** — it's the operating system. But it's well-optimized at 38KB.

### 2. Expert Loading (Variable: 1,350–31,000+ tokens per expert)

| Load Tier | What's Read | Avg Token Cost |
|-----------|-------------|----------------|
| Tier 0 (Card) | Invocation card | ~50 tokens |
| Tier 1 (SKILL.md) | SKILL.md + workflow | ~1,350 tokens |
| Tier 2 (Deep) | SKILL.md + genius.md + workflow | **~9,200 tokens** |
| Tier 3 (Sub-agent) | Spawns fresh context | ~300 tokens in main |

**Key finding**: Your 157 `genius.md` files average **31,309 bytes (~7,800 tokens)** each. The largest ones hit **149KB (~37,000 tokens)**. A single Tier 2 load of your biggest experts (Nicolas Cole Niche Positioning, NBA Betting Edge, Luke Iha Copy Blocks) consumes **~37,000 tokens** just for the genius file alone.

### 3. Workflow Execution

| Size Bucket | Count | % of Total |
|-------------|-------|------------|
| Under 5KB | 359 | 90% |
| 5–10KB | 24 | 6% |
| 10–20KB | 14 | 3.5% |
| Over 20KB | 2 | 0.5% |

**Good news**: 90% of your 399 workflows are lean (under 5KB / ~1,250 tokens). The workflow layer is efficient.

### 4. Skill Directory Heavyweights

| Skill | Total Size | Approx Tokens |
|-------|-----------|---------------|
| Lucas Alpay Storytelling | 2.0 MB | ~500K |
| Nick Saraev Agentic Workflows | 1.97 MB | ~490K |
| Erica Mallet Brand Magnetism | 1.92 MB | ~480K |
| Omar Eddaoudi Premium Ads | 1.7 MB | ~425K |
| Rory Sutherland Marketing | 1.38 MB | ~345K |

These are *total* skill directories — not everything gets loaded at once. But when running deep Tier 2 loads or conversions, these generate significant burn.

---

## Token Burn Patterns (Where You're Spending Most)

### 🔴 High Burn: Extraction Workflows (`/extract`, `/extract-forge`)

A full extraction session typically consumes:
- Source material analysis: 2,000–10,000 tokens (depends on transcript length)
- Expert routing + loading: 1,350–9,200 tokens
- Genius.md generation: 15,000–37,000 tokens (output)
- SKILL.md + workflows: 10,000–25,000 tokens (output)
- Verification + registration: 2,000–5,000 tokens

**Total per extraction: 30,000–85,000 tokens**

This is inherently expensive because it's producing large, high-quality artifacts. There's limited room to optimize without reducing output quality.

### 🟡 Medium Burn: Multi-Expert Content Production

When running `/parallel-content`, `/launch-day`, `/council`, or `/swarm`:
- Each expert load (Tier 1-2): 1,350–9,200 tokens
- 3-5 experts: 4,050–46,000 tokens just for loading
- Plus production output

**Optimization opportunity**: Use Tier 0 cards for routing, Tier 1 for execution when possible. Only load genius.md when the output demands creative depth.

### 🟢 Low Burn: Single-Expert Tasks

When running focused workflows like `/hook-forge`, `/storybrand`, `/proof-audit-360`:
- One expert load (Tier 1): ~1,350 tokens
- One workflow read: ~500–1,250 tokens
- Production: varies

**These are efficient.** The tiered loading system works well for focused tasks.

---

## Recommendations

### 1. Genius.md Size Control (HIGH IMPACT)

> [!IMPORTANT]
> Your genius.md files are your biggest controllable expense.

**Current state**: 157 files averaging 31KB. Top files hit 149KB.

**Recommendation**: Establish a **50KB hard cap** for genius.md files. Files over 50KB should be refactored into:
- `genius.md` — Core patterns, voice DNA, quality rubric (under 50KB)
- `references/deep-patterns.md` — Extended examples and case studies (loaded only at Tier 3)

This would cut Tier 2 load costs by 40-60% for your heaviest experts without losing any knowledge.

### 2. Conversation Discipline (MEDIUM IMPACT)

**Biggest controllable factor**: How many experts you load per conversation.

| Practice | Token Impact |
|----------|-------------|
| Loading 1 expert at Tier 1 | ~1,350 tokens |
| Loading 3 experts at Tier 2 | ~27,600 tokens |
| Loading 5 experts at Tier 2 | ~46,000+ tokens |

**Recommendation**: For routine content tasks, stay at Tier 1. Reserve Tier 2 for creative/complex work. Reserve multi-expert sessions for dedicated production sprints.

### 3. Workflow Efficiency (ALREADY GOOD)

Your workflow layer is lean. 90% of files are under 5KB. No action needed.

### 4. System Instruction Optimization (LOW IMPACT, HIGH EFFORT)

At 38KB, your system instructions are substantial but not bloated for a system this complex. The SLASH_COMMANDS list in your instructions is the largest single component, but it's essential for routing.

**Minor optimization**: The 399 workflow descriptions in your slash command list consume significant space. Consider creating a `SLASH_COMMANDS_INDEX.md` file that the system reads on-demand instead of embedding all descriptions in the system instructions.

### 5. Session Boundaries (BEHAVIORAL)

**The most impactful change is behavioral, not architectural:**

| Instead of... | Do this... | Savings |
|---------------|------------|---------|
| One long session doing 5 different things | Focused sessions with one domain | 30-50% fewer expert re-loads |
| Exploratory "try all angles" prompts | Sharp, scored intent (The Chain) | Fewer clarification rounds |
| Re-explaining context each session | Use `/session-kickoff` to restore state | Eliminates repeat loading |

---

## Summary: Your System Is Already Well-Optimized

The Antigravity system has strong token efficiency architecture:
- ✅ Tiered loading chain (Tier 0→3) prevents unnecessary file reads
- ✅ Hot context cache prevents re-reading same expert twice
- ✅ Internalized routing for known domains saves ~2,200 tokens/request
- ✅ Handoff summaries compress chain boundaries
- ✅ 90% of workflows are under 5KB

**The three highest-ROI improvements are:**
1. **Genius.md size cap** (50KB) — reduces Tier 2 costs by 40-60% for heaviest experts
2. **Session discipline** — focused single-domain sessions vs. multi-expert marathons
3. **Tier discipline** — default to Tier 1, escalate to Tier 2 only when creative depth is genuinely needed

> [!TIP]
> The mark of mastery isn't avoiding token use — it's ensuring every token earns its place. Your system already embodies this. The main risk is *behavioral* (loading too many experts per session), not *architectural*.
