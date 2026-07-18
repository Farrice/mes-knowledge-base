# PROVENANCE — skills/deliberate repair (Wave 3 Lane 4 Batch 4)

Anchor → source file + location table. Every anchor below was read directly by this worker; none inferred.

| Anchor (as it appears in the repaired files) | Source file | Location | Verified how |
|---|---|---|---|
| "'Both make good points' is not synthesis — it's avoidance. Name a winner or explain the synthesis condition." | `skills/deliberate/SKILL.md` | Anti-Patterns item 1, line 131 | Read tool, verbatim compare |
| "Confirmation bias dressed as deliberation. If Claude wins 5 in a row, audit your synthesis for self-favoring." | `skills/deliberate/SKILL.md` | Anti-Patterns item 2, line 132 | Read tool, verbatim compare |
| "Reverse bias. Same audit needed." | `skills/deliberate/SKILL.md` | Anti-Patterns item 3, line 133 | Read tool, verbatim compare |
| "Adding `--grounding` to a judgment-call prompt makes Gemini fetch web context that pollutes the deliberation. Use grounding only when factual surface exists." | `skills/deliberate/SKILL.md` | Anti-Patterns item 6, line 136 | Read tool, verbatim compare |
| "If the decision's marginal value is under $100 or you've already made up your mind, single-model is fine. Don't burn the deliberation overhead." | `skills/deliberate/SKILL.md` | Anti-Patterns item 5, line 135 | Read tool, verbatim compare |
| "Skipping Step 2's 'strongest argument against' — false confidence enters Step 3." | `.agent/workflows/deliberate.md` | Anti-Patterns (workflow FAIL) item 1, line 197 | Read tool, verbatim compare |
| "Silently falling back to Claude-only when Gemini fails — defeats the entire point. Always surface the failure to user." | `.agent/workflows/deliberate.md` | Anti-Patterns (workflow FAIL) item 5, line 201 | Read tool, verbatim compare |
| Commit `30a0d6345`, 2026-05-25, "feat(deliberate+anchor-memory): multi-model deliberation + mission templates + visual board" | git history | `git log --follow -- skills/deliberate/SKILL.md` | Bash tool, command run directly, tail of output |
| Commit `8ae51279c`, 2026-07-13, "feat(wiring): forge wave 3 — 161 born-v2 prompts across 25 skills (0 fidelity-low)" | git history | `git log --follow -- skills/deliberate/SKILL.md` | Bash tool, command run directly, head of output |
| Output Contract section shape (`## Output Contract` / `## Output Skeleton` / `## Quality Gate`) that `workflows/deliberate.md`'s new sections were modeled on | `skills/deliberate/references/prompts-v2/deliberation-synthesis.md` | lines 79-130 | Read tool, structure referenced (not copied verbatim — new prose written specific to the workflow file's own deliverable) |
| Model Calibration section template ("would [X] recognize this as... or as someone using [X] vocabulary? If it's the second, rebuild.") | `skills/ben-watkins-storytelling/genius.md` | lines 7-16, per envelope instruction | Read tool, structure referenced (not copied — rewritten for /deliberate's own craft: post-hoc agreement, verbatim-rendering discipline, adversarial-not-diplomatic texture) |
| Trace file `trace_20260525_081832_deliberate.json` is a schema smoke test, not real usage | `evolution_store/v2_traces/trace_20260525_081832_deliberate.json` | full file, 1,067 bytes | Read tool, `notes`/`expert`/`factual_grounding` fields inspected directly |
| No `extractions/` folder matches "deliberate" | `extractions/` directory listing | `ls extractions/ \| grep -i deliberate` | Bash tool, empty result confirmed directly |
| No `docs/solutions/` card is specific to `/deliberate` | `docs/solutions/` | `grep -rl "deliberate" docs/solutions/` (2 hits, both read and confirmed incidental) | Bash + Read tools |

No quote in the repaired files is used without a row in this table or in `references/source-ledger.md`. The one UNCONFIRMED-labeled external claim (Perplexity's "model council" feature) was already self-hedged by the skill's original authors — this repair did not manufacture new certainty around it.
