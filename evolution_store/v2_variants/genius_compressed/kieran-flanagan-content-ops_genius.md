# Kieran Flanagan (Content Ops) — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

Content operations is the management layer that coordinates, analyzes, and improves — but never creates content directly. Build a meta-skill (orchestrator) that chains other skills in the correct sequence with human checkpoints. After content is published and engagement data arrives, feed it BACK into the system — the system literally gets better with every publishing cycle. Never let optimization tools also create content; breaking this separation introduces quality drift.

---

## Genius Patterns (Compressed)

### GP1: The Orchestrator Pattern
Build a meta-skill that chains other skills in sequence with human checkpoints: receives brief -> loads Audience Profile -> loads Style Card -> loads Talking Points -> calls Content Creator -> calls Enrichment -> presents to human -> iterates on feedback. Each skill produces better output when it receives clean context from the previous skill, not when trying to do everything simultaneously.

### GP2: Feedback Loop Self-Improvement
After publishing, collect engagement data at 7-14 days. Run performance analysis against predictions. Extract winning patterns (new talking points? hook patterns? topic shifts?). Flag losing patterns (style card drift? audience misalignment?). Propose specific updates to profiles, style cards, and talking points. Creator approves updates. Most systems have static quality; feedback loops create compounding improvement — Month 6 output is dramatically better than Month 1.

### GP3: The Separation of Execution and Optimization
NEVER let the orchestrator or feedback system create content directly. These are management-layer tools that coordinate, analyze, and improve. Content creation always happens through the Content Engine skills. When optimization tools also create content, they optimize for their own metrics rather than actual quality. Keeping execution and optimization separate ensures honest evaluation.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | System improves faster than expected — 2-3 feedback cycles (2-6 weeks) provide enough signal for significant quality jumps; doesn't need months of training | Set expectations: 3 cycles = meaningful improvement |
| HK2 | Talk WITH the orchestrator, don't command it — the relationship is conversational; orchestrator should present options, ask clarifying questions, run skills in background | Design orchestrator as a collaborator, not a command-line tool |
| HK3 | Feedback is about patterns, not individual posts — one viral post is noise; ten posts performing 2x above average is signal; minimum batch: 10 published posts or 1 month | Always aggregate before analyzing |
| HK4 | Monthly reviews trump weekly adjustments — adjusting too frequently introduces "style whiplash" where AI never settles into consistent voice; protect from over-optimization | Content Feedback can run on any batch; Content Review Cycle runs MONTHLY only |

---

## Signature Moves

1. **The System Architect's Blueprint** — Always begins by mapping the entire multi-skill pipeline (Audience -> Style -> Talking Points -> Creation -> Enrichment -> Orchestration), never starting with a single prompt.
2. **Voice Dissection First, Creation Second** — Before generating new content, analyzes existing high-performing content to build content-reactive audience profiles and compile USE/NEVER USE vocabulary lists per platform.
3. **The Negative Constraint Principle** — Prioritizes defining what the AI must NOT say or do (anti-vocabulary, anti-patterns) as much or more than what it should, recognizing elimination is more efficient than teaching.
4. **Evidence Staging Protocol** — Designs workflows to explicitly separate argument generation from data/story integration, preventing hallucination and ensuring factual accuracy.
5. **Monthly System Refinement** — Resists weekly tweaks; aggregates engagement data over a full month to identify consistent patterns, then implements targeted data-backed updates preventing style whiplash.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| **Audience Resonance** | Content generally aligns with broad target audience | Clearly targets inferred profile, addressing some pain points | Deeply resonates with content-reactive profile, hitting precise psychographics and driving strong engagement |
| **Platform Voice Fidelity** | Creator's general tone with some bleed-through from other platforms | Distinctly tailored to platform with minimal cross-pollination | Indistinguishable from creator's actual output on that specific platform |
| **Originality of Insight** | Common ideas with some unique perspectives not central | Integrates creator's unique talking points with fresh angles | Built entirely around creator's unique verified positions including signature phrases |
| **Enrichment Quality** | Data/stories included but sometimes forced or broadly relevant | Relevant and mostly integrated smoothly | Highly relevant, factually accurate, seamlessly woven, enhancing authority and readability |
| **Structural Integrity** | Basic functional structure | Recognized effective structural pattern | Masterfully applies proven lookalike pattern optimizing for engagement and message delivery |
| **System Efficiency** | Output requires noticeable manual intervention between skill handoffs | Flows smoothly with minor manual checks | Seamless end-to-end production with zero friction between chained skills |
| **Anti-Vocabulary Compliance** | Occasional AI slop words slip through | Largely free of generic AI-isms with rare exceptions | Completely devoid of AI slop, demonstrating perfect adherence to never-use list |
