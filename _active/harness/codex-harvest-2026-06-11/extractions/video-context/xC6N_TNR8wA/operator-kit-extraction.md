# Operator Kit Extraction: Seven Daily Commands

## Core Thesis

The useful pattern is not the creator's exact private files. The useful pattern is a small daily command layer that makes agents easier to steer, coordinate, critique, branch, and improve without re-explaining context every time.

## Hidden Mechanics

1. **Learning loop over static prompts**
   The session does not end as disposable chat. Corrections, frustration, preferences, and repeated errors become proposed improvements.

2. **Shared project memory over ad hoc restarts**
   Multi-session work needs a project home with context and logs. Otherwise every new session pays the context tax again.

3. **Onboarding as a first-class action**
   A fresh agent/session should not be expected to infer project state. It should read a compact project brief and return what it thinks the next move is.

4. **Intent alignment before execution**
   The agent should ask bounded clarifying questions when intent changes the output. Lettered options reduce user effort.

5. **Contrarian pressure against sycophancy**
   LLMs tend to agree. A daily command that challenges the current path catches weak evidence, hidden assumptions, and better alternatives.

6. **Parallel options as search**
   Asking for several distinct variants lets the user pick the closest target and continue from there instead of iterating one narrow answer.

7. **Tweakable parameters for visual work**
   Design feedback is often easier through adjustable parameters than vague prose. The useful abstraction is controlled change plus a patch, not generic design advice.

## Antigravity Build Decisions

- Build seven direct commands because the user explicitly selected direct daily access.
- Keep command bodies compact and route back to a shared primitive for common safety and output rules.
- Install both project-local command bridges and global operator skills.
- Preserve existing `/calibrate` and avoid modifying `/mission`.
- Keep writes local and reversible by default.
- Do not publish, message, scrape private dashboards, or run external actions from these commands.

## Quality Bar

The commands are worth keeping only if they reduce repeated explanation and improve daily agent steering. If they become ceremony, they should be folded into `/autopilot`, `/end-session`, or cold workflows instead of remaining hot.

