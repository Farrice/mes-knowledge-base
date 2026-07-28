---
description: Build the Executive Editor — a get-to-yes evaluator for high-stakes upward/outward communication (exec emails, client updates, launch-date asks), instantiating her worked example end to end
---

# hg-exec-editor — The Get-to-Yes Editor

Her canonical tool, rebuilt for any operator: paste a high-stakes message → pass/fail per criterion → what to improve → suggested rewrites — tuned to get a yes/green-light from the specific reader. The teaching example is deliberately "silly" (internal email) because the downside is asymmetric: "Is it cool if we move the launch date?" → "No. Not even a little." One bad exec email detonates a day.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md` §Crown Jewel.
- Scope: WHOSE messages, to WHICH reader class, for WHAT outcome (default: exec/decision-maker × get a yes). This is `hg-judgment-encode` specialized — if edit pairs exist, use them; this workflow also carries her four mined criteria as the cold-start floor.

## Skill Acquisition

- `genius.md` §Crown Jewel + §Anti-Patterns
- `references/source-quotes.md` §The pipeline, §The stakes story

## Execution

1. **Corpus first** (when available): run the Column A/B mining on the operator's own high-stakes messages → operator-specific criteria. **Cold start**: begin from her four (below), then re-mine after 10 real uses.
2. **Criteria floor** (hers, verbatim-derived):
   - **Leads with the message** — the ask/news in the very first sentence, not paragraph three
   - **Actionable** — the reader knows exactly what's being asked of them and by when
   - **Tone right** — calibrated to the reader and the stakes; no hedging, no drama
   - **Every word adds clarity** — nothing that introduces ambiguity survives
   Plus the get-to-yes layer: anticipates the reader's first objection and answers it in-line; frames change (launch-date class) with impact + mitigation + recommendation, never as an open question ("Is it cool if...?" is the fail case).
3. **Write the pass/fail rubric** in plain English, one concrete pass and fail example per criterion (fail examples from the operator's corpus where possible; hers as fallback).
4. **Compose the system prompt**: role (whose judgment, which reader class, get-to-yes outcome) → evaluate each criterion pass/fail quoting the evidence line → improvements in priority order → suggested rewrites of failed spans in the operator's register → return the message to the author; never send-ready-rewrite the whole thing.
5. **Validate** on 2 real past messages — including at least one that historically went wrong. The tool must catch what actually detonated.
6. **Ship** with deploy note: run before every message to [reader class]; a PASS is not a send order — the author's final read is the judgment seat.

## Content Type Adaptations

| Message class | Get-to-yes layer becomes |
|---|---|
| Exec email / launch-date ask | Impact + mitigation + recommendation framing; no open-ended asks |
| Client status update | Confidence + control signal: what happened, what we're doing, when you'll hear next |
| Investor/board note | Headline number first; asks separated from FYIs |
| Cold outreach / DM | (Route to copy-engine instead — this tool is for readers who must keep trusting you tomorrow) |

## Output Requirements

- Deliverable: rubric + paste-ready system prompt + validation report + deploy note.
- Named in the grammar: "[Reader] Editor — get to yes."
- Execution prompt: `references/prompts-v2/exec-editor.md`

## Quality Gate

genius.md rubric: purpose specificity, pass/fail legibility, feedback actionability, teaching residue (criteria visible, work returned to author). Anti-patterns: whole-message rewriting, generic "professional tone" criteria, tool scoped wider than one reader class.
