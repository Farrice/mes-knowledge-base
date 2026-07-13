---
name: "Mark Kashef Silver Platter — Recipe Card Design"
source_prompt: born-v2
skill: mark-kashef-silver-platter-agentic-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are composing a single Silver Platter **recipe card** — the schema the method uses to turn one recurring operator motion into a screenshot-able, build-ready automation card. A recipe is not a feature description; it's the difference between the operator's Monday morning today and their Monday morning after the build exists. The method's own standard: *"Headlines must be operator-screenshot-able. `manual_today` must reference real tools the operator named. `monday_difference` must be specific enough to picture."*

## Input Required

```
[OPERATOR_NAME]
[RECIPE_STARTER] - the recipe row this is built from (from the archetype's starter list), or "operator-volunteered, not on the starter list"
[OPERATOR_TOOLS] - the actual tools involved, from the data map's pantry (real names, not placeholders)
[MANUAL_PROCESS_DETAIL] - how the operator does this by hand today: which app, which day, roughly how long it takes, what artifact they produce (a spreadsheet, an email, an apology)
[TARGET_TIME_OR_SLOT] - when the operator wants the new version to land (e.g. "6am Monday, on his iPad")
[ARCHETYPE_ORCHESTRATOR_AND_SPECIALISTS] - the orchestrator + specialist names already defined for this business (e.g. "EA Orchestrator", "CFO Bot")
[SOURCE_PLATTERS] - which prep silver platters or pantry sources this recipe reads from
```

## Execution Protocol

**Step 1 — Confirm before composing.** If `[RECIPE_STARTER]` is a starter-list row, confirm it against the operator's actual stated pain rather than assuming the headline fits unmodified. If the operator volunteered a recipe not on any starter list, build it from this same schema — don't wait for a matching template to exist.

**Step 2 — Write `manual_today` as a movie scene.** Reference model (from the source material, quoted as the quality bar — do not reuse verbatim, write the operator's own version): *"Marco opens Shopify, Meta Ads Manager, TikTok Ads Manager, and a margin spreadsheet on his laptop every Monday. Pieces it together for ~3 hours before he has a number he trusts."* The operator is at their actual desk. There is a real artifact — the spreadsheet, the email thread, the apology they had to write. No generic "the process is manual and time-consuming."

**Step 3 — Write `monday_difference` as the new ritual.** Reference model (quality bar, do not reuse verbatim): *"Reads the brief on his iPad with coffee at 6am, signs it, eats breakfast. Sam sees the number in Slack by 9."* Specific time, specific device, specific calm — and, where the recipe has a second consumer, name what THEY see and when.

**Step 4 — Write the headline to the locked voice rules:**
- Lead with the OUTCOME, not the process. Not "Weekly P&L" but "Monday P&L brief on your iPad, 10 min instead of 3 hours."
- Include a number or a comparison — time saved, dollars recovered, errors prevented.
- No jargon. "Refund triage" is jargon to a non-technical owner; "Refund replies drafted within an hour, you just hit send" is not.
- Under 12 words.

**Step 5 — Populate `ingredients` / `ingredients_friendly` from the real data map.** `ingredients` is the raw pantry/subagent IDs the recipe touches. `ingredients_friendly` is the plain-English name for each — and the LAST element is always the outcome chip (gets coral styling automatically), so end the list on the thing the operator receives, not the last input consumed.

**Step 6 — Populate `claude_code_stack`** from `[ARCHETYPE_ORCHESTRATOR_AND_SPECIALISTS]` and `[SOURCE_PLATTERS]`: which skills ingest the sources, which subagents (orchestrator + the specialist that owns this domain) touch it, which hooks fire (`SessionStart convert_dropzone.sh` is the default unless the recipe is a post-action draft, in which case `PostToolUse audit_action.sh`), and which rules gate it (path-scoped if any regulated or cross-domain data is involved).

**Step 7 — Write the `walkthrough`** as a literal actor-by-actor sequence: cron trigger, hook, orchestrator routing, specialist reasoning (name what it cross-references and what threshold or comparison it applies), operator action at the end including how they acknowledge it (audit log, Slack, hitting send).

**Step 8 — `before_claude_code` / `after_claude_code`** are one sentence each, status-quo vs after-state, each anchored to a real artifact — not a restatement of the headline.

## Output Contract

One recipe object, complete against the locked schema: `id`, `name`, `headline`, `time_saved_per_week`, `manual_today`, `monday_difference`, `goal`, `ingredients`, `ingredients_friendly`, `claude_code_stack` (`skills`, `subagents`, `hooks`, `rules`), `walkthrough` (array of `{actor, action}`), `before_claude_code`, `after_claude_code`. Headline under 12 words. `manual_today` and `monday_difference` each 1-3 sentences, both naming real tools/devices/times, never the operator's business type as a generic stand-in.

## Output Skeleton

```json
{
  "id": "[snake_case_slug]",
  "name": "[short internal name]",
  "headline": "[outcome-first, <12 words, includes a number or comparison]",
  "time_saved_per_week": "[e.g. ~N hrs/wk OR $N-N/mo recovered]",
  "manual_today": "[2-3 sentence movie scene: operator, real app, real artifact, real duration]",
  "monday_difference": "[1-2 sentence new ritual: specific time, specific device, specific calm]",
  "goal": "[1-sentence operational goal]",
  "ingredients": ["[raw_id_1]", "[raw_id_2]"],
  "ingredients_friendly": ["[plain name 1]", "[plain name 2]", "[outcome chip — last element]"],
  "claude_code_stack": {
    "skills": ["[snake_case_skill_id]"],
    "subagents": ["[Specialist Agent Name]"],
    "hooks": ["[Hook type + script]"],
    "rules": ["[rules/domain.md (path-scoped) or omit if none]"]
  },
  "walkthrough": [
    {"actor": "[Cron/hook/agent/operator, time]", "action": "[what happens, plain English]"}
  ],
  "before_claude_code": "[1-sentence status quo, real artifact]",
  "after_claude_code": "[1-sentence after-state, real artifact]"
}
```

## Quality Gate

- Is the headline under 12 words, outcome-first, and does it include a number or comparison?
- Does `manual_today` name a real tool the operator actually uses and a real artifact — not a generic description of "doing it manually"?
- Is `monday_difference` specific enough that the operator could picture the exact minute it happens?
- Does `ingredients_friendly` end on the outcome chip, not on the last input consumed?
- Does every subagent named in `claude_code_stack` already exist in the business's defined hierarchy, or is a new one explicitly justified?
- If the recipe touches regulated or cross-domain data, is a path-scoped rule present in `claude_code_stack.rules`?

## Creative Latitude

This is the most screenshot-facing artifact in the whole method — push hardest here. The headline is copy, not documentation: try the outcome framed as time AND as dollars and pick whichever lands harder for this specific operator. The movie-scene in `manual_today` is where taste shows — a generic "opens three tabs" beats nothing, but a headline-worthy one has a physical detail (the coffee, the specific spreadsheet tab, the exact apology line) that only this operator's business would produce. Don't force every recipe into the same rhythm as the reference examples; match the beat to the size of the pain.

## Deploy When

A data map exists (or enough pantry/pain detail has been gathered) and the operator wants ONE fully-built, presentable automation card — for confirmation before it goes into the build plan, or as a standalone pitch for a single recurring motion.
