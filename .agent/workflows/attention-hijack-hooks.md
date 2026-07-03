---
description: Universal attention-anchor, brand/news/name/trend hijack, and hook-generation system for content, copy, social, LinkedIn, newsletters, scripts, ads, and end-to-end content routing
---

# `/attention-hijack-hooks` - Universal Attention Hook System

Turn a source, draft, trend, brand move, news item, person, raw thought, offer, or content brief into platform-fit hooks and a handoff into full content generation.

This workflow is a companion layer. It does not replace `/diandra-content-engine`, `/diandra-hook-architect`, `/kallaway-trend-hook-engine`, `/high-taste-writing-os`, or `/publishable-copy-gate`.

## Use When

- A draft has good substance but weak hook pull.
- A brand, news item, person, trend, or claim should become a post angle.
- The user asks for brand tracking, newsjacking, brandjacking, namejacking, or attention hijacking.
- The output must work beyond LinkedIn: social posts, newsletters, short scripts, ads, carousels, landing pages, or client content.
- The user wants end-to-end content after hook selection.

## Modes

```text
/attention-hijack-hooks scan [topic/source/brand/news/person/trend]
/attention-hijack-hooks extract [draft/source/offer/raw thought]
/attention-hijack-hooks generate [payload + reader + platform]
/attention-hijack-hooks rehook [draft or published post]
/attention-hijack-hooks audit [hook]
/attention-hijack-hooks content [selected hook + output type]
/attention-hijack-hooks plugin-readiness
```

Use `--delegate` only when the user explicitly asks for true Codex subagents, parallel agents, or delegated agent work. Without that flag, run the agent roles locally and state that no real subagents were spawned.

## Source Authority

Load only the context needed for the current step:

1. `semantic_libraries/antigravity/primitives/attention-hijack-hook-system.md`
2. `skills/attention-hijack-hooks/SKILL.md`
3. `skills/attention-hijack-hooks/genius.md`
4. `extractions/video-context/Zc4E_K48v48/analysis.md` (unavailable until re-extracted — run `/watch Zc4E_K48v48`)
5. `extractions/video-context/Zc4E_K48v48/uncertainty-report.md` (same — unavailable until re-extracted)
6. `skills/diandra-escobar-linkedin-growth/genius.md` when using Diandra borrowed-attention formats
7. `.agent/workflows/diandra-content-engine.md` when the hook should become a LinkedIn content package
8. `.agent/workflows/diandra-hook-architect.md` when the hook work is part of the full Diandra hook system

Do not claim visual or on-screen evidence from the Diandra video unless a later source package contains frames or OCR rows.

## Skill System Contract

| Field | Required Output |
|---|---|
| Source evidence | URL or local source path, plus uncertainty limits |
| Objective | One specific hook/content outcome |
| Components | Attention skill, Diandra source, local auditor, target content workflow, quality gate |
| Step order | signal scan -> hookable extraction -> format generation -> platform fit -> content bridge |
| Inputs | source/draft, reader, platform, payload, evidence, voice constraints |
| Outputs | anchor board, payload lock, hook table, selected hook, audit, handoff |
| Handoff summary | Attention Hook Handoff from skill workflow 05 |
| Composition rule | Attention Hook System owns hook decision; downstream workflow owns final content |
| Human checkpoint | Required before external research, scraping, posting, publishing, client delivery, or real subagents |
| Validation | `attention_hijack_hooks.py`, `verify_attention_hijack_hooks.py`, command/workflow router checks |
| Result surface | Hook Room report or Content Bridge handoff in conversation or local content card |
| Context policy | Keep command and primitive compact; load transcript only on demand |
| Reuse hook | Use inside `/diandra-content-engine` Hook Room and `/diandra-hook-architect` hook bottlenecks |

## Operating Flow

### 1. Signal Scan

If the input is a topic, market signal, brand, news item, or person, run Workflow 01.

Return a Signal Anchor Board with ranked anchor options and a recommended anchor.

### 2. Payload Lock

If the input is a draft, source, offer, or raw thought, run Workflow 02.

Write:

```text
This content earns attention because it shows [reader] that [specific claim] using [proof/source/story/mechanism].
```

### 3. Format Generation

Run Workflow 03.

Generate and score:

- Dense
- Punchy plus Context
- Single-Line Bomb
- Stacked
- Hybrid, only if it beats the core formats

### 4. Platform Fit

Run Workflow 04 and the deterministic local auditor when possible:

```bash
python3 execution/attention_hijack_hooks.py --hook "[hook]" --platform linkedin --terms "[topic terms]"
```

Use LinkedIn pixel-width logic for LinkedIn. For other platforms, adapt to first-screen constraints:

| Platform | First Window |
|---|---|
| LinkedIn | first 40 to 50 words, mobile fold, line breaks |
| X/Threads | first sentence and first screen of the post |
| Newsletter | subject line plus first sentence |
| Short script | first 3 seconds |
| Ad | first line plus proof/mechanism |
| Carousel | cover text plus slide 1 |
| Landing page | headline plus subhead |

### 5. Content Bridge

Run Workflow 05.

Route by final output:

- Farrice content package -> `/diandra-content-engine` (farrice-content-os not present in canonical)
- LinkedIn post -> `/diandra-content-engine`
- LinkedIn hook system -> `/diandra-hook-architect`
- First-50 audit -> `/diandra-first-50`
- Public copy -> `/publishable-copy-gate`
- High-taste rewrite -> `/high-taste-writing-os`

## Agent And Subagent Design

Main-thread owner:

- `agents/attention-hijack-hooks/AGENT.md`

Optional delegated worker spec:

- `.claude/agents/attention-hijack-hook-auditor.md`

Delegation slots, if explicitly authorized:

| Slot | Job | Output |
|---|---|---|
| Signal Scout | Find and score brand/news/name/trend anchors | Signal Anchor Board |
| Hook Architect | Generate format-specific hooks from the payload lock | Hook Room table |
| Fit Auditor | Run platform fit and risk checks | PASS/REVISE audit |

Real Codex subagents require explicit authorization and a Delegation Receipt. Expert names or agent files are not proof that workers ran.

## Plugin Ladder

This workflow can become a repo-local plugin candidate only after repeated fresh-thread use proves that the workflow, skill, auditor, and bridges reduce reconstruction burden.

Run:

```bash
python3 execution/plugin_readiness_audit.py --stdout attention-hijack-hooks farrice-content-os diandra-linkedin-system
```

Do not build or recommend a plugin if the score says improve first or keep as workflow.

## Output Schema

```markdown
## Attention Hijack Hook Report

### Route
- Owner:
- Mode:
- Source evidence:
- Downstream route:
- Real subagents spawned:

### Signal / Payload
- Attention anchor:
- Payload lock:
- Curiosity gap:
- Reader:
- Platform:

### Hook Room
| Hook | Format | Score | Keep/Cut Reason |
|---|---|---:|---|

### Winner
[selected hook]

### Platform Fit
- Verdict:
- Mechanical notes:
- Human judgment note:

### Content Bridge
- Next route:
- Handoff:
- Open risk:
```

## Verification

After changing this workflow or its bridge, run:

```bash
python3 execution/verify_attention_hijack_hooks.py
python3 execution/validate_skill.py attention-hijack-hooks
python3 execution/command_menu.py search "brand tracking newsjacking hook hijack universal content"
python3 execution/workflow_router.py search "rehook draft Diandra hook formats attention hijack"
python3 execution/plugin_readiness_audit.py --stdout attention-hijack-hooks diandra-content-engine diandra-hook-architect
```

## Starter Routes

```text
/attention-hijack-hooks scan "AI operating partners for visible experts"
/attention-hijack-hooks rehook "[paste draft]" --platform linkedin
/attention-hijack-hooks generate "reader: consultants; payload: generic AI content kills trust; platform: newsletter"
/attention-hijack-hooks content "selected hook: ..." --route diandra-content-engine
```
