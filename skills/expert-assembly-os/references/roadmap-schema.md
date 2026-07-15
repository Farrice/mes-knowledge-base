# Expert Assembly OS — Roadmap Output Contract

Complete roadmap structure emitted at Synthesize phase (expert-assembly.workflow.js Phase 7). Every section is present. No placeholders.

---

## 1. Panel (Labeled)

```
**Expert Assembly Panel** [for: {TASK}]

- **[Name]** [Domain] — {Role/Covers_Domain}
  *Methodology: [One-line core method]*
  Signature move: [Stealable contribution from Diverge]
  
- **[Name]** [Domain] — {Bespoke Composite}
  *Methodology: [Synthetic method blend]*
  Formed because: [Why this domain was thin/absent in roster; this person's specific thesis]
  
- **Farrice (Function Owner)** [Taste & Alignment]
  *Taste gate + cross-domain pattern synthesis*
```

**Labeling Rule**: All synthetic panelists explicitly marked `[Bespoke Composite]`. Real extracted experts marked `[Roster]`. No ambiguity.

---

## 2. Claims Grounding Table

Required if the deliverable section contains ANY factual claim (statistics, market data, methodology attributions, etc.).

```
| Claim | Source / Grounding | Confidence |
|-------|-------------------|-----------|
| "X% of Y market..." | URL / Study / Assumption | VERIFIED / LIKELY / UNCONFIRMED |
| "According to Z methodology..." | Reference + brief | VERIFIED / LIKELY / UNCONFIRMED |
```

**Rule**: Every row is explicit. No "per Step X research" abstractions. If a claim is unconfirmed, label it. If grounding is assumed, say so.

---

## 3. Synthesis

Exact structure from council deliberation:

```
**The Crux** (the one real tension that matters):
[One paragraph naming the central disagreement or trade-off the panel surfaced]

**Net-New Principle** (what emerged ONLY from combination):
[One paragraph: the insight no single expert articulated alone; the transferable mental model]

**Forks for Farrice** (genuine either/or choices only you should make):
- Fork A: [Choice A detail] — Tradeoff: [what you gain / what you sacrifice]
- Fork B: [Choice B detail] — Tradeoff: [what you gain / what you sacrifice]
```

---

## 4. Roadmap — Three Horizons

**Strategic (6–12 months)**: Shift in position/market/capability.
**Tactical (1–6 months)**: Concrete deliverables and early wins.
**Operational (0–30 days)**: Launch phase; moves you make this week/next.

Each move follows the observable doctrine (CLAUDE.md Law 2):

```
### OPERATIONAL (0–30 days)

**Move 1: [Title]**
- Owner: [Person or role]
- Action: [Concrete, one-sentence]
- Success criteria: [Observable; not "improve X" but "X reaches Y by DATE"]
- Dependencies: [Blockers or pre-reqs]

**Move 2: [Title]**
[Same structure]

---

### TACTICAL (1–6 months)

**Deliverable 1: [Title]**
- Owner: [Team or person]
- Scope: [What it covers; what it excludes]
- Success criteria: [Observable metrics or outcomes]
- Dependencies: [What must be done first]

[Repeat per deliverable]

---

### STRATEGIC (6–12 months)

**Initiative: [Thesis]**
- North Star: [The change you want in the market/org/customer perception]
- Phases: [High-level sequence]
- Leading indicator: [What you watch to know if this is working]
- Owner: [Who drives this]
```

---

## 5. Composition Ledger

Transparency on panel construction. Why each seat exists and how it was filled.

```
| Seat | Expert | Filled By | Coverage | Notes |
|------|--------|-----------|----------|-------|
| Spine | [Name] | Roster / Bespoke | [Domain] | [Why this person or synthesis] |
| Mechanism | [Name] | Roster / Bespoke | [Domain] | [Rationale] |
| Differentiator | [Name] | Roster / Bespoke | [Domain or cross-domain] | [Rationale] |
| Craft | [Name] | Roster / Bespoke | [Domain] | [Rationale] |
| Risk Gate | [Name] | Roster / Bespoke | [Domain] | [Rationale] |
| Function Owner | Farrice | Always | Taste & Alignment | Final gate |
```

---

## 6. Next Moves Together

The panel's final guidance on execution (what they're recommending Farrice do beyond the roadmap).

```
**What We Built Together**
[One paragraph: the outcome delivered; why it exceeds any single voice]

**What Comes Next (Our Advice)**
- [Specific, actionable point 1; grounded in deliberation]
- [Specific, actionable point 2]
- [Specific, actionable point 3]

**What We Didn't Explore** (But You Should):
- [Domain or approach the panel agreed was in scope but ran out of cycles for]
- [Risk category or upside the panel didn't have time to model]

**The Blind Spot We Flagged**
[One paragraph: the thing the panel noticed it might be missing; not a weakness, a risk-awareness note]
```

---

## 7. Blind Spots the Panel Flagged

Explicit meta-awareness. The panel's acknowledgment of what it doesn't know or where it might be wrong.

```
**Blind Spot 1: [Category or domain]**
- Why: [Why the panel can't see this clearly]
- Risk: [What goes wrong if this is misread]
- Mitigation: [How Farrice should compensate]

**Blind Spot 2: [Category or domain]**
[Same structure]
```

---

## Quality Validation

Roadmap passes Synthesize only if:

- [ ] Panel clearly labeled (Roster vs Bespoke, composite disclosure)
- [ ] Claims table present if any factual claims in deliverable
- [ ] Crux, Net-New Principle, Forks all filled (no placeholders)
- [ ] All three roadmap horizons present (operational, tactical, strategic)
- [ ] Each roadmap move has Owner and Observable Success Criteria
- [ ] Composition Ledger shows why each seat was filled
- [ ] Next Moves Together is specific, not generic
- [ ] Blind Spots are authentic (not template checklist items)
- [ ] Grounding Guard passes (`execution/grounding_guard.py --task-type Strategy`)
