# Kallaway Content OS - Skill System Contract

| Field | Contract |
|---|---|
| Source evidence | Ten packages under `extractions/video-context/`: `oRYfJ_yxz6M`, `B9l9TRhu5Vw`, `ImzoNTrgvFg`, `cuVyTmbOZjk`, `bqzd0h0gmU0`, `onQoYdxWXdA`, `a7VjpIqq8Xk`, `SDHKQbKC7gA`, `7pCEsr-0KIw`, `1q__Vs2JqbI`. |
| Objective | Make the existing Kallaway suite operate as one source-backed content OS from strategy through production, retention, articulation, batch learning, and monetization. |
| Components | `kallaway-content-operating-system`, `kallaway-content-system`, `kallaway-content-psychology`, `kallaway-ai-content-engine`, `skills/kallaway-ai-content-engine/workflows/trend-hook-radar.md`, `execution/kallaway_trend_hook_radar.py`, `kallaway-addictive-storytelling`, `kallaway-audience-obsession`, `kallaway-word-mastery`, `kallaway-social-commerce`, `agents/kallaway`, `execution/video_context_ledger.py`, command/workflow routers, validation scripts. |
| Step order | intent lock -> evidence selection -> compliant signal radar when needed -> lane classification -> component chain -> handoffs -> first artifact -> validation -> next use route. |
| Inputs | User goal, target audience, offer or content objective if available, source package paths, existing Kallaway component docs, any draft/content/performance data supplied by the user, and optional compliant CSV/owned/approved public signal rows. |
| Outputs | Route trace, source evidence summary, signal/outlier receipt when relevant, component handoffs, first usable artifact, validation checklist, next command sequence. |
| Handoff summary | Use the Skill System Handoff shape: source evidence, component used, output produced, next input, validation, open risk. |
| Composition rule | The OS layer is the function owner. Kallaway components contribute by lane; Shaan Puri may stack for story-driven viral work, but no extra expert is loaded unless the route needs it. |
| Human checkpoint | Skip for local reversible workspace use. Ask before external publishing, paid/private tooling, broad deletion, or any action outside this workspace. |
| Validation | `sync_registries.py`, `validate_skill.py source-command-kallaway-content-os`, `validate_skill.py source-command-kallaway-trend-hook-engine`, router search for `kallaway content os` and `kallaway trend hook engine`, `verify_codex_authority.py`, `verify_skill_system_contract.py`, `codex_harness_check.py`. |
| Result surface | Rendered conversation output plus local skill/workflow files. The first practical artifact is usually a one-rep brief, batch plan, hook/story package, audit, or monetization map. |
| Context policy | Keep this orchestrator hot and compact. Keep full transcripts cold under `extractions/video-context/`. Load only relevant analyses/ledgers and pass short handoffs between components. |
| Reuse hook | Invoke `/kallaway-content-os` whenever a request asks for the full Kallaway content system. Invoke `/kallaway-trend-hook-engine` when the request asks for Kallaway hook trend analysis, a Sandcastles alternative, social outlier scoring, or compliant trend radar behavior. |

## Default Handoff Shape

```markdown
## Skill System Handoff: [Component] -> [Next Component]
- **Source evidence**: [video package path or timestamp rows]
- **Component used**: [skill/workflow/script/agent]
- **Output produced**: [brief/path/object]
- **Next input**: [what the next component receives]
- **Validation**: [pass/fail/check]
- **Open risk**: [none or exact limitation]
```

## Cold-Start Check

A future agent should be able to start with `/kallaway-content-os`, read `.agent/workflows/kallaway-content-os.md`, load this skill's `SKILL.md`, consult `references/source-evidence-map.md`, and choose the correct Kallaway component chain without relying on hidden conversation context.
