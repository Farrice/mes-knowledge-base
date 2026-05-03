# Subagent Roster — The 12 Real Claude Code Subagents

**Status:** Active as of 2026-04-28. All defined in `.claude/agents/`. Invokable via the Agent tool with `subagent_type: <name>`.

## Why This Exists

This document is the canonical reference for the 12 real Claude Code subagents in this system. They are distinct from the 119 expert personas in `agents/<expert>/` — those are markdown personas loaded as Tier 2 context by the main Claude conversation. The 12 here are real isolated-context subagents with restricted tools, embodied virtuoso identities, and chainable workflows.

The distinction matters because:
- **Personas** = thinking lenses. Loaded as context. Channel through main conversation.
- **Subagents** = repeatable workers. Isolated context. Invoked via Agent tool. Run in parallel.

Both serve the system. They don't compete; they complement.

## The Roster

### Tier 1 — Foundation (used in nearly every workflow)

| Name | Job | When to fire |
|---|---|---|
| `deep-research` | Cross-source research virtuoso | Foundation for any deliverable requiring grounded research. Embodies Stratechery × Bloomberg × a16z. |
| `fact-verifier` | Truth-grounding for any factual deliverable | BEFORE shipping any deliverable with real-world claims. Implements Step 5.5 of the Chain. |
| `prose-doctor` | AI-tell exorcist + voice enforcer | BEFORE publishing any public-facing prose. Catches the 8 banned structural moves. |

### Tier 2 — Production (high-frequency creative/strategy work)

| Name | Job | When to fire |
|---|---|---|
| `expert-extractor` | MES 3.0 extraction virtuoso | When extracting a new expert from source material. Replaces manual /extract workflow. |
| `icp-deep-canvasser` | Audience intelligence virtuoso | When defining or deepening ICP. McRaney × Cimorelli × Invisible Expert canon. |
| `synthesis-engine` | Cross-domain reflection virtuoso | When 2+ inputs (extractions, experts, documents) need cross-pattern synthesis. Generates `knowledge/synthesis/<title>.md`-grade output. |

### Tier 3 — Quality (elevate any deliverable)

| Name | Job | When to fire |
|---|---|---|
| `adversarial-reviewer` | Independent critique virtuoso | BEFORE delivery. Specific stress-test, not vague feedback. |
| `content-finalizer` | Chain finalize virtuoso | AFTER expert deliverable complete. Anchor-cited rubric, prose check, Notion log, revenue tracker. |

### Tier 4 — Outcomes / Specialty (public-facing work)

| Name | Job | When to fire |
|---|---|---|
| `master-copywriter` | Agency-grade copy across formats | Any content/social/campaign/marketing deliverable. ONE version, work-showing. |
| `brand-system-builder` | Brand architecture virtuoso | Full brand system from brief — DESIGN.md v2, voice rules, library entry. |
| `competitive-intel` | Market research virtuoso | Niche/competitor analysis. Real findings, primary sources, no SWOT slop. |
| `swarm-orchestrator` | Multi-expert parallel synthesis | Multi-domain tasks. Compounds 5 expert takes into one coherent deliverable. |

## Invocation Patterns

### Single Subagent

```
Agent({
  subagent_type: "deep-research",
  description: "<3-5 word summary>",
  prompt: "<full self-contained brief — agent has no conversation context>"
})
```

### Parallel Multi-Subagent

For independent work, fire in a single message with multiple Agent tool calls. They run concurrently.

### Chained Workflows (canonical patterns)

**Strategic brief production:**
```
deep-research → synthesis-engine → master-copywriter → prose-doctor → adversarial-reviewer → content-finalizer
```

**LinkedIn post production:**
```
[persona load: Lara] → master-copywriter → prose-doctor → adversarial-reviewer → content-finalizer
```

**Parallax edition (canonical):**
```
[raw take captured] → fact-verifier → [persona load: Cole] → master-copywriter → prose-doctor → adversarial-reviewer → content-finalizer
```

**New expert extraction:**
```
expert-extractor → synthesis-engine (cross with existing) → content-finalizer
```

**Brand launch:**
```
icp-deep-canvasser → competitive-intel → brand-system-builder → master-copywriter (sample copy) → adversarial-reviewer → content-finalizer
```

**Multi-domain swarm (positioning, campaigns, strategic decisions):**
```
swarm-orchestrator (which fires the appropriate sub-subagents in parallel)
```

## Architecture (How These Differ From Personas)

Each subagent file in `.claude/agents/<name>.md` has:

1. **YAML frontmatter** — `name`, `description` (with examples), `tools` (restricted set), `model`
2. **Embodied identity** — specific top-1% practitioners named ("Ben Thompson × Bloomberg standards desk × a16z")
3. **Unfair advantage** — references to user's specific knowledge infrastructure (Recall, extractions, knowledge base)
4. **Hard rules** — anti-patterns from the user's documented past failures (Parallax 02 fabrications, 8 banned structural moves, voice rules)
5. **Process** — concrete steps the subagent runs
6. **Output contract** — exact structure of returned output
7. **Self-check** — final-pass questions the subagent must answer "yes" to
8. **Examples of excellence vs. slop** — contrast pairs specific to the subagent's domain

This architecture is what makes them virtuoso-tier rather than generic LLM wrappers.

## Maintenance

**Adding a new subagent:**
1. Determine if the job is genuinely subagent-shaped (clear input/output, isolated context, repeatable). If not, build a persona or skill instead.
2. Write the `.claude/agents/<name>.md` file using the architecture above.
3. Add to this roster under the appropriate tier.
4. Document chainable patterns if applicable.
5. Commit with descriptive message.

**Updating an existing subagent:**
1. Edit `.claude/agents/<name>.md` directly.
2. If the change affects when/how to invoke, update this roster.
3. Restart Claude Code to pick up frontmatter changes (description, tools, model).

**Deprecating a subagent:**
1. Move the file to `.claude/agents/_archived/` (don't delete — git history preserves but archived dir lets you recover quickly).
2. Update this roster.
3. Update CLAUDE.md if referenced.

## Relationship to Other Subagent Sources

- **Built-in Claude Code subagents:** `Explore`, `Plan`, `general-purpose`, `statusline-setup`. Always available.
- **Plugin subagents:** Installed via Claude Code plugins. Examples: `feature-dev:code-architect`, `jarvis-command-center:workstream-lead`, `claude-code-guide`. Available if plugin installed.
- **Project subagents (this roster):** Defined in `.claude/agents/`. Project-specific.

When invoking, always confirm the subagent name is namespaced correctly. Project subagents use bare names (`deep-research`); plugin subagents use `<plugin>:<name>` form.

## Verification

```bash
# Confirm all 12 files exist
ls .claude/agents/*.md | wc -l   # Should be 12

# Confirm frontmatter is valid (each starts with --- and has name/description)
for f in .claude/agents/*.md; do
  head -1 "$f" | grep -q "^---$" || echo "MISSING FRONTMATTER: $f"
done

# After Claude Code restart, the subagents appear in the available subagent_type list.
```
