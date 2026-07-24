---
status: closed
type: research
blocked_by: []
claimed_by: loop-eng-frontier-2026-07-24
---

# 0001 — Canon research: what loop/compound engineering actually is, proven vs. hype

## Question

What is the actual, evidenced canon of "loop engineering" and "compound engineering" as of mid-2026 — and which patterns are proven in production versus discourse hype?

Cover at minimum: compound engineering (Kieran Klaassen / Every / Cora lineage — every unit of work makes the next unit easier; plan→work→review→compound cycles), agentic loop design patterns (self-improving harnesses, learnings fed back into instructions/skills/hooks), and whoever else the evidence says matters. For each pattern, record: the claim, the receipt (who runs it in production, with what result), and a proven/plausible/hype label.

**Scope widened (Farrice, 2026-07-24):** beyond the headline canon, dig specifically for **lesser-known / underrated loop patterns** practitioners actually run but that aren't in every thread — and document **how Boris Cherny (creator of Claude Code) uses compound engineering** in his own workflow, with receipts.

AFK — deep-research agent + `execution/research.py`, Recall grounding pass first. Deliverable: markdown summary saved as a linked asset in `_active/loop-engineering-integration/`, Receipt-carrying. Do NOT map onto our system yet — that is ticket 0003's job.

## Resolution

Full report (4,501 words, receipt-carrying): [`../../research/2026-07-24-canon-proven-vs-hype.md`](../../research/2026-07-24-canon-proven-vs-hype.md)

**Top findings:**
1. **Two canons, wrongly fused in the discourse.** Compound engineering (Every/Klaassen, Jan 2026: Plan→Work→Review→Compound, 80/20 rule) is a *learning* loop. Loop engineering (Steinberger 2026-06-07 → Osmani named it 2026-06-08 → Boris Cherny corroborated) is an *autonomy* loop. Cherny never says "compound engineering" — citing him for it is a category error.
2. **Verification, not compounding, is the load-bearing primitive** — now first-party Anthropic doctrine and shipped product (`/goal` judge, `/loop`, Stop hooks, verification subagents).
3. **Hardest receipt in the field:** OpenAI harness-engineering (~Feb 2026): ~1M LOC, ~1,500 merged PRs, 3→7 engineers, 5 months, 0 hand-written lines. PROVEN throughput; quality unmeasured.
4. **Cherny's 2–3x verification claim = self-report only (PLAUSIBLE).** Real Anthropic N=400k sessions: verified success 15% novice → 28–33% expert.
5. **METR misquoted in both directions**; any 2026 speedup number = UNCONFIRMED.

**3 most underrated loops found:**
- **Metric-ratchet loop (autoresearch)** — only pattern with independent replication (Karpathy, Lütke, Shopify Eng `pi-autoresearch`, 40+ metrics). Caveat: overfit + "ugly hacks."
- **"Map, not encyclopedia" rules-file loop** — OpenAI (~100-line AGENTS.md as index) and Anthropic ("bloated CLAUDE.md causes Claude to ignore instructions") converged independently. Directly contradicts append-every-failure compounding.
- **Official ralph-wiggum plugin ≠ Ralph** — Anthropic's plugin re-prompts in the same session (context accumulates); Huntley's original is fresh-context re-anchoring from disk. Opposites.
