# Scrapes Skill Systems — Resume Brief (LIVING; update in place)

*Last updated 2026-09-02 (end of the integration session). Paste the "Kickoff prompt" at the bottom into a fresh session to start hot.*

## Where we are, in one breath
Scrapes' 36 skills and 4 workers are vendored and on main. Farrice's brand context is built from canon. The OpenAI GPT Image path is keyed and capped at $15/month. Jen has a sibling brand context and one carousel through the system (cover A chosen, v2 copy awaiting his verdict, a Claude Design canvas live). The routing layer does NOT yet know the Scrapes skills exist, and Jen's real Scrapes execution run (template factory → designer → image generator) has not happened because her six brand inputs are not in yet.

## Before the next real run (do in this order)
1. **Land the lane.** On main: `git merge --abort`, then `python3 execution/worktree_lane.py merge --lane codex/scrapes-trial`. Six commits ride in it (budget guard, Jen brand context + intake pack, both Jen runs, canvas source, precedence-map routing rule).
2. **Wire the router (≈20 min, one lane).** Add bindings so intent reaches the Scrapes front doors AND our pens:
   - `directives/routing-bindings.md` + `execution/routing_enforcer.py BINDINGS`: "carousel / social post / repurpose / slides / video to shorts / youtube to ebook" → the matching Scrapes skill, with the craft-room seats named (Alyssa + Luke for Jen; VOICE-CARD + Luke for Farrice).
   - A thin front-door workflow `.agent/workflows/social-carousel.md` that runs 00-social-content's phases and hands the copy seams to our pens (the table in PRECEDENCE-MAP.md "Craft-room routing"). The per-prompt router scores `.agent/workflows/*.md` stems, so a workflow is what makes it fireable; Scrapes skills alone are invisible to it.
   - `execution/skill_router_hook.py`: teach it to read `vendor:` entries from the arsenal index so `/00-*`, `/mkt-*`, `/viz-*` show up as routing suggestions.
3. **Jen's six inputs.** Forward `_active/clients/jen-listings/brand_context/INTAKE-PROMPT-PACK.md` (from "hey jen" down). Nothing in step 4 is honest without them.
4. **The real run for Jen (the blind bar, one sitting with Farrice's approvals):** mkt-visual-identity Import (tokens from `valley-editions/DESIGN.md`, refs classified inspiration) → ssc-template-builder ×6 → Template Studio approve → 00-social-content on the same "still renting" topic → ssc-designer → ssc-image-generator → Content Studio. Judge it against the v2 canvas. Cost: templates $0; any AI slide is pre-flighted by the guard and stated before it runs.
5. **Farrice's own first run:** `/mkt-visual-identity` is done (Premium Minimal imported, brand book v1). Next is the template pool from `premium-minimal/package/templates/*.svg`, then `/00-social-content` on one supplement teardown, judged against the current LinkedIn carousel path.

## Verdicts still open (his)
- v2 copy (cover A): 9 or not? Which frame is short?
- Precedence map: any FLIP / KEEP he disagrees with.
- Sprint as door three: alive or dead (positioning.md keeps it as door three).
- Journal lane `codex/health-performance-evidence-journal`: 40 conflicts in generated research-brief HTML; needs its own sitting.

## Do NOT rebuild
Brand context (both), the arsenal index patch, the constitution block, the budget guard, the precedence map, the canvas artboards (`projects/00-social-content/2026-09-02/jen-priced-out/v2/canvas/`), the intake pack. Extend, never regenerate.

## Files
`_active/harness/scrapes-skill-systems/{PRECEDENCE-MAP,INTEGRATION,RESUME-BRIEF}.md` · `brand_context/` (Farrice) · `_active/clients/jen-listings/brand_context/` (Jen) · `directives/openai-usage-policy.md` · `.agent/handoffs/2026-09-02-jen-canvas.md` · canvas https://claude.ai/code/artifact/084b1bd6-f6b0-4a4a-b1dd-9ddb6d611fb1

## Kickoff prompt (paste into the new session)
```
Resume thread jen-canvas. Read _active/harness/scrapes-skill-systems/RESUME-BRIEF.md first, then PRECEDENCE-MAP.md and .agent/handoffs/2026-09-02-jen-canvas.md. Step 2 of the brief first: wire the router so the Scrapes skills are fireable and hand their copy seams to our pens (Alyssa + Luke for Jen, VOICE-CARD + Luke for me). Then, if Jen's six inputs are in, run step 4 end to end with me approving in the Studios; if not, run step 5 on my brand. State cost before any AI image call. No Chain ceremony until something ships.
```
