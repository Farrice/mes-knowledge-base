# Walkthrough: Fladlien Empowerment & Writing Craft Expansion

## Summary
Expanded the Jason Fladlien expert agent from **19 → 27 workflows** across two new tiers, committed and pushed in two batches.

---

## Tier 4 — Empowerment & Brand Philosophy (commit `f278f0c1`)

| # | Command | Workflow | What It Does |
|---|---------|----------|-------------|
| 20 | `/fladlien-empower` | Empowerment Content Engine | Education IS the selling. "Now are you ready?" daily cadence. Level 4-5 empowerment content. |
| 21 | `/fladlien-book` | Book-as-Sales-Letter Engine | Long-form assets where the reader finishes and begs to buy. Anti-sales-letter architecture. |
| 22 | `/fladlien-info-brand` | Information-to-Brand Conversion | 80/15/5 content split. Free info builds brand equity, not funnels. "Nothing to sell" frame. |
| 23 | `/fladlien-patience` | Patience Marketing System | The tree model. 60+ reasons reservoir. Daily watering protocol. Anti-launch framework. |

**Core principle**: *"I'm educating my audience with information that's empowering to them. That's always going to be to your benefit regardless of the market."*

---

## Tier 5 — Indirect, Hypnotic & Candor Writing (commit `7671a9ff`)

| # | Command | Workflow | What It Does |
|---|---------|----------|-------------|
| 24 | `/fladlien-hypnotic` | Hypnotic Writing Patterns Engine | 6 documented patterns: non-invalidatable statements, embedded commands, presuppositions, self-selection triggers, negative frames, irrefutable logic chains. |
| 25 | `/fladlien-indirect-sell` | Indirect Selling Copy Architecture | 7 indirect selling architectures. Newtonian vs. Einsteinian framework. Direct-to-indirect conversion tables. |
| 26 | `/fladlien-candor-write` | Radical Candor Writing Engine | The "$49 PDF" energy. 6 candor moves. The Brazilian Facebook Test. Platform-specific candor templates. |
| 27 | `/fladlien-conversational` | Conversational Persuasion Copy Engine | Convergence of all three: indirect + hypnotic + candor. Spoken-to-written translation. Template stack for emails, sales, social. |

**Core principle**: *"At the highest levels of persuasion, indirect communication is preferable to direct communication."*

---

## Relationship Between the Two Tiers

**Tier 4** is the **marketing philosophy** — how you think about the relationship between content and revenue.

**Tier 5** is the **writing craft** — how you actually write the sentences that execute that philosophy.

They stack naturally: deploy `/fladlien-empower` to design your content strategy, then `/fladlien-conversational` to write the actual copy.

---

## Final State

| Metric | Count |
|--------|:-----:|
| Total workflows | **27** |
| Total slash commands | **27** |
| Tiers | **5** |
| Files added this session | **16** (8 workflows + 8 slash commands) |
| SKILL.md | Updated (27 workflows, 5 tiers) |
| Git status | Committed and pushed to `main` |

---

## Verification
- `ls workflows/ | wc -l` → 27 ✅
- `ls .agent/workflows/ | grep fladlien | wc -l` → 27 ✅
- SKILL.md header → `## Workflows (27)` ✅
- Both commits pushed to `github.com:Farrice/mes-knowledge-base.git` ✅
