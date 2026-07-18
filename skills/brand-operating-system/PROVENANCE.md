# Brand Operating System — Provenance

**Ship Date**: 2026-05-04 (Resonance reference implementation)  
**Version**: v1 (6-layer architecture, 43-document canonical structure)  
**Status**: Production-ready, reference implementation available

---

## Reference Implementation: Resonance (Andrea DJ)

**Archival Path**: `projects/andrea-dj/brand-operating-system/`  
**Drive Location**: `Andrea DJ Package / 2026-05-04 — Brand Operating System v1/`  
**Delivery Format**: 43 markdown files locally + 43 native Google Docs (pageless) in Drive  
**Quality Score**: Composite 8.3/10 (Adversarial Review 7.6/10, Prose-Doctor PASS)

**Built From**:
- Canonical Inputs: Andrea's Internal Anchor + Manifesto v2
- Discovery Phase: ICP deep-canvass (3 profiles + umbrella)
- Foundation Phase: Brand bible (9 sections), Voice document (30+ paired examples), Positioning one-pager
- Visual Phase: DESIGN.md (50+ tokens), Photography rules, Component library
- Briefs Phase: Master template (10 sections) + 9 per-asset briefs (email, IG post, flyer, venue pitch, press one-sheeter, etc.)
- Marketing Phase: Content pillars (3), Hook library (40+ hooks by format), Channel architecture, Curation system, Crisis comms, Funnel mapping
- AI Handoff Phase: AI Brain Master (3,200 tokens, hard ceiling 4,000), Claude Pro setup, Prompt library (12 prompts), Image formula, Canva spec
- Ops Phase: Update protocol, Change log, Drift signals, Success metrics (13 measurables), Exit interview protocol, Run-of-show

---

## Architecture Genealogy

### Origins

**Brand Operating System** was designed as a response to three failure modes observed in brand-building:

1. **Fragmentation**: Brands have separate voice docs, design systems, content calendars, AI prompts — all independently managed, drifting separately.
2. **Revision Hell**: When the spine changes, amendments cascade across 10+ documents manually, or they don't and drift compounds.
3. **Cold AI**: Without a structured handoff layer (AI Brain Master), pasting brand docs into Claude/ChatGPT produces output that requires 2-3 revisions to align.

**Solution**: A single-source-of-truth system where all 43 documents are linked via inheritance chains. Update the foundation once; all downstream documents inherit the change.

### Conceptual Debts

The architecture draws from four master practitioners:

- **Greg Hoffman (Nike CMO)**: Brand architecture as "Seen → Felt → Proven" progression. Functional purity over aesthetic chasing. Emotional memory as the moat.
- **Oren Klaff**: Operational systems for creatives. The idea that systems compound: a reference repo, content pipeline, weekly update protocol, and team tracker create defensible creative positioning.
- **Ben Watkins**: Storytelling as a sales mechanism. The insight that every message needs emotional grounding, and that "know your audience like a character" beats demographic segmentation.
- **Grace Andrews**: Media company thinking. The notion that brands are trust-pathways (Attention → Discoverability → Connection → Trust → Conversion), and that operational systems (outreach layer mapping, consistency × experimentation, business outcome anchoring) are what scale trust.

### Design Principles

1. **Inheritance Over Repetition**: Master template → per-asset briefs. Master ICP → all downstream content. Update once; cascade everywhere.
2. **Reader-Type Drives Structure**: Each of 6 layers exists because it's consumed by a different professional. Don't merge them or readers have to scan.
3. **Compression Discipline**: AI Brain Master has hard 4K-token ceiling. If you can't compress the spine into it, the Foundation is bloated. Token pressure signals clarity pressure.
4. **Sequence Matters**: Phases are sequential because each phase's output is an input to the next. B needs A. C needs B. Parallelism breaks the contract.
5. **Quality Gates Between Phases**: Halt and resolve between each phase. Foundation drift in Phase B compounds across Phases C-G. Catching it early saves revision hell downstream.

---

## Evolution Path

### v1 (Current — 2026-05-04)

- **6-layer architecture** (Foundation, Visual, Briefs, Marketing, AI Handoff, Ops)
- **43-document canonical structure** (each layer has a defined doc count and output contract)
- **7-phase orchestration** (Discovery, Foundation, Visual, Briefs, Marketing, AI Handoff, Wrap)
- **Quality gates between phases** (Phase A→B gate, Phase B→C gate, etc.)
- **Reference implementation shipped** (Resonance for Andrea)
- **Adversarial review + prose-doctor quality bar** (Composite ≥7/10)

### v1.1 (Candidate — Not Yet Shipped)

Deliberate gaps identified in v1, ready to address in v1.1:

- **Founder-story voice memo capture** (currently placeholders marked PENDING)
- **Post-event story production at scale** (exit interviews → Substack longform / carousel workflows)
- **Subscription/recurring-revenue cohort planning** (brand as evolving vessel for community, not one-time system)
- **Founder bandwidth awareness** (run-of-show with hours-budget, sustainability layer)

### v2.0 (Future — 2-3 years)

- **Multi-brand franchise management** (BOS for sub-brands that inherit from master BOS)
- **Automated amendment cascade** (tool that updates master template and propagates to 9 briefs, not manual)
- **Notion integration** (live sync between BOS docs and Notion databases for teams)
- **Predictive drift detection** (ML model that flags when brand output is drifting before human eye catches it)

---

## Maintenance & Amendment Protocol

See `directives/brand-operating-system-protocol.md` for full protocol. Summary:

**When the Skill Amends** → Resonance reference gets back-applied or explicitly diverged in changelog.  
**When Resonance Amends** → Template gets back-applied or explicitly diverged in changelog.  
**They march together.** Template is derivative of Resonance, not parent. Resonance is the proof the architecture works.

---

## Cross-Skill Stacking

The Brand Operating System is designed to compose with other skills:

| Stack | Context |
|-------|---------|
| BOS + `/design-md` | DESIGN.md (Phase C1) is authored by design-md expert, then embedded in the Visual layer |
| BOS + `/voice-document` | Voice document (Phase B3) is authored by voice-document expert, then embedded in Foundation |
| BOS + `/icp-deep-dive` | ICP Master (Phase A2, B4) is deepened by icp-deep-dive, then inherited across all layers |
| BOS + `/creative-brief-gen` | Master Creative Brief Template (Phase D0) is scaffolded by creative-brief-gen, then cloned 9 times |
| BOS + `/convene` | Phase G (Wrap) uses `convene` to assemble adversarial review council (if multi-expert review needed) |

None of these are required; they're optional enhancements. A solo founder can execute the full BOS build without invoking sub-skills, though quality typically improves with expert composition.

---

## Known Constraints

1. **No Automation of Amendment Cascade** (v1). When master brief changes, you manually update 9 child briefs or use a search-replace. v2 will automate this.
2. **Drive Upload Requires Explicit Opt-In** (`--drive-parent` flag). v1 ships local-first; Drive is optional.
3. **Single Founder Assumption** (v1). If a brand has 2+ co-founders with different voice preferences, BOS Phase B becomes contentious. v1.1 candidate: founder adjudication protocol.
4. **No Multi-Language Support** (v1). BOS is authored in English. Localization is v2.0 territory.
5. **Discovery Interview Not Yet Fully Scripted** (v1). Phase A discovery is "invoke agents/synthesis-engine/" — the interview script exists but hasn't been formalized into a locked template. v1.1 candidate.

---

## Quality Assurance

All claims in this file are verified against:

1. **Resonance Reference Build** (`projects/andrea-dj/brand-operating-system/`)
2. **Expert Extractions** (Hoffman, Klaff, Watkins, Andrews in `extractions/`)
3. **Genius.md Architecture Reasoning** (`skills/brand-operating-system/genius.md`)
4. **Workflow Execution Specs** (`skills/brand-operating-system/workflows/*.md`)

See `references/source-ledger.md` for full verification status (VERIFIED / LIKELY / UNCONFIRMED).

---

**Curator**: Brand Operating System Skill Team  
**Last Verified**: 2026-07-17  
**Next Review**: 2026-08-17 (monthly cadence)
