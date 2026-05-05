# Phase F — AI Handoff

**Duration**: ~half-day. Sequential. This is THE layer the BOS exists to power.

## Required inputs

The entire upstream stack. AI Handoff compresses everything from Phases B + C + D + E.

## Steps

### F1 — AI Brain Master

Run `/ai-brain-context` (skill: `skills/ai-brain-context/`):

> Compress the brand bible + voice document + ICP master + non-negotiables into a single paste-in document. Hard ceiling: 4,000 tokens. Working ceiling: 3,200 tokens.
>
> 8 sections:
> 1. Spine line (verbatim, ≤30 tokens)
> 2. Brand bible compressed (1 paragraph, ~200 tokens)
> 3. ICP umbrella + 3 profiles (3 sentences each, ~300 tokens)
> 4. Voice rules + 6 named patterns (1 example each, ~600 tokens)
> 5. Banned phrases (top 5, ~100 tokens)
> 6. Non-Negotiables (12 lines compressed, ~400 tokens)
> 7. Hell-yes filter / decision triage (7-point checklist, ~200 tokens)
> 8. Visual register (3 sentences, ~100 tokens)
>
> Total target: ~1,930 tokens. If past 3,200, sharpen the foundation. If past 4,000, hard-cut.
>
> Header note: "Last updated: [date]. Status: canonical. If anything in here drifts from the foundational docs, the foundational docs win and this file gets amended."

Output: `04-ai-handoff/00-ai-brain-master.md`.

**Verification**:
```bash
# Token count check (rough approximation: words × 1.3)
WORDS=$(wc -w < <output>/04-ai-handoff/00-ai-brain-master.md)
TOKENS=$((WORDS * 13 / 10))
echo "Approx tokens: $TOKENS"
[ $TOKENS -lt 4000 ] || echo "OVER BUDGET — sharpen or cut"
```

### F2 — AI Brain Deploy informs F3-F5

Run `/ai-brain-deploy` (skill: `skills/ai-brain-deploy/`):

> Generate the AIOS Deployment Blueprint — the plan for HOW the AI Brain Master gets used in practice. Informs the prompt library structure, image prompt formulas, and Canva spec.

Output: internal blueprint informing F3-F5 (not delivered as a standalone doc).

### F3 — Claude Pro Project Setup

Run `/4c-architect` (skill: `skills/4c-architect/`):

> Exact provisioning guide for the founder's Claude Pro Project:
> - Project name
> - Custom instructions (paste-in)
> - Knowledge files to upload (which BOS docs)
> - Custom slash commands (project-scoped)
> - Default model
> - Memory configuration

Output: `04-ai-handoff/01-claude-pro-project-setup.md`.

### F4 — Prompt Library

Invoke `agents/master-copywriter/` (main-thread save):

> 15-25 ready-to-paste prompts covering common asset/decision tasks. Each prompt:
> - Name
> - When to use
> - Required pre-paste docs (e.g., "Paste 03-voice-document.md first, then this prompt")
> - The prompt itself (paste-in)
> - Expected output format
> - Self-check questions
>
> Categories to cover:
> - Asset production (per asset type from Phase D)
> - DM triage (Hunter / Performer / Real one)
> - Voice-check on draft
> - Sponsor offer decision triage
> - Crisis response drafting
> - Storyboard + visual prompts (handoff to F5)

Output: `04-ai-handoff/02-prompt-library.md`.

### F5 — Image prompts + Canva spec

Run `/creative-prompt` (Creative Director skill: `skills/creative-direction/`):

Two outputs:

1. **Image prompt formulas** — Midjourney/Sora/Imagen scaffolds tuned to the brand's visual mechanic. Format: `[mechanic anchor] + [scene] + [lighting per photography rule] + [style modifiers] + [aspect ratio]`. Include 5-10 worked examples.

2. **Canva component spec** — locked Canva templates (size, font, color, photo treatment) so any AI-generated copy from the prompt library drops straight in. Include template links, font slot conventions, color slot conventions.

Output:
- `04-ai-handoff/03-image-prompt-formulas.md`
- `04-ai-handoff/04-canva-component-spec.md`

## Quality gate (Phase F → G)

Before advancing to Phase G:
- [ ] AI Brain Master is ≤4000 tokens (approximate via word count × 1.3)
- [ ] AI Brain Master 8 sections all present
- [ ] AI Brain Master header includes update protocol clause
- [ ] Claude Pro setup has copy-paste blocks for instructions + knowledge file list
- [ ] Prompt library has ≥15 prompts across ≥5 categories
- [ ] Image prompt formulas have ≥5 worked examples
- [ ] Canva spec has font/color slot conventions

**Cold-start test**: Open a fresh Claude conversation. Paste only `04-ai-handoff/00-ai-brain-master.md`. Ask: "Draft an IG caption announcing [first cycle/event/product] for [Profile #1]." Output should hit the spine frame, mechanism, voice patterns, and ICP language without re-prompting. If output reads generic, the AI Brain Master is leaking — sharpen and re-test.
