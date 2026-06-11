# Token Efficiency Protocol

> **Purpose**: Minimize token consumption and context pollution. Push deterministic work to code, only show the model what it needs to reason about.
> **Status**: ACTIVELY ENFORCED — fires on every workflow.

---

## Rule 1: Handoff Summaries

At chain boundaries, compress to handoff summary — NOT full upstream output:

```markdown
## Chain Handoff: [Step] → [Next Step]
**Expert**: [Name] | **Domain**: [1-line]
**Patterns Found**: [count] — [names]
**Files Created**: [paths] | **Next Step Needs**: [specific files]
```

Applies to: any workflow chain with 2+ steps, multi-file ops, sub-agent handoffs.

## Rule 2: Push Deterministic Work to Scripts

LLM should NOT: count files, cross-reference lists, validate totals, generate boilerplate, check registrations. Use `execution/` scripts instead.

| Task | Script |
|------|--------|
| Search experts | `python3 execution/search_experts.py "keyword"` |
| Validate skill | `python3 execution/validate_skill.py skill-name` |

If same mechanical task 3+ times → create a script in `execution/`.

## Rule 3: Invocation Cards (Lazy Loading)

Don't read full skill files until needed. Start with invocation cards (~50 tokens each) in `agents/_framework/invocation-cards.md` (Tier 0). Full reads only when executing methodology or generating deliverables.

## Rule 4: Tiered Loading

Start at Tier 0. Escalate only when needed. Full protocol: `directives/agent-loading-protocol.md`.

## Rule 5: Chain Step Internalization

Steps 1-3 of The Chain (SCORE/SHARPEN/ROUTE) execute in-head for routine tasks. Known domains (LinkedIn→Lara, Copywriting→Luke, SEO→Nathan, Brand→Oren/Grace, Ghostwriting→Cole, Content Psych→Kallaway, Consumer→Dai, Agentic→Saraev) skip file reads. Ambiguous requests → read `DOMAIN_REGISTRY.md`.

## Rule 6: Hot Context Cache

Don't re-read expert files already loaded in current conversation. Hot at T1→skip reads (save ~1,350). Hot at T1, need T2→read only genius.md. Hot at T2→skip all (save ~2,550).

## Rule 7: Codex Prompt Hygiene

Workflow descriptions ≤8 words. `AGENTS.md` + `CODEX.md` should stay compact and non-duplicative. `GEMINI.md` and `CLAUDE.md` are legacy references, not active Codex prompt authority. If workflows >400 -> quarterly audit for dormant ones.

---

## Anti-Patterns

- ❌ Read 3 skill files to pick expert → ✅ Check invocation cards
- ❌ Keep full extraction in context → ✅ Handoff summary
- ❌ Manually count/cross-check → ✅ Run scripts
- ❌ Re-read SKILL.md same expert → ✅ Hot Context Stack
- ❌ Read intent-pipeline.md for routine → ✅ Internalized formula

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-04-03 |
| **Activation Count** | 2 |

*Created: 2026-02-18 | Compressed: 2026-04-13*
