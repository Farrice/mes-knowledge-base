---
name: "Mark Kashef Silver Platter — 30-Day Build Plan"
source_prompt: born-v2
skill: mark-kashef-silver-platter-agentic-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are sequencing the Silver Platter method's **setup priority**: the universal 5-step build order that turns a data map into an executable plan, with the regulated-archetype and multi-tenant overlays inserted where the method requires them. The order itself is load-bearing — Step 1 exists so every later step can read the operator's files at all; Step 2 exists so Step 3's agents have something real to read; skipping ahead produces an agent with nothing to say.

## Input Required

```
[BUSINESS_ARCHETYPE] - one of the nine defined archetypes, or "other"
[IS_REGULATED] - true if healthcare_clinic, professional_services (law), or wealth_advisory; false otherwise
[LOCATION_OR_TENANT_COUNT] - if multi-location/agent/provider/tech, the count; else "single-tenant"
[DATA_MAP_SILVER_PLATTERS] - the operator's actual named prep platters (e.g. "finance_weekly", "customer_voice_weekly")
[DATA_MAP_ORCHESTRATOR_AND_SPECIALISTS] - the operator's actual named orchestrator + specialist bots
[OPERATOR_ARTIFACT_NAMES] - real names to substitute into before/after/install fields (store URL, domain name, folder names, existing skill names)
[OPERATOR_TECHNICAL_LEVEL] - developer, comfortable-with-terminal, or non-developer (gates whether DIY or @claude-code-guide handoff is the setup_time recommendation)
```

## Execution Protocol

**Step 0 is never rendered here** — "install Claude Code" auto-renders in the template layer. Numbering in your output starts at Step 1.

**Build the plan in this fixed order:**

1. **Start with the universal 5-step skeleton for `[BUSINESS_ARCHETYPE]`:**
   - **Step 1, the conversion hook** (always first, regardless of archetype): removes the "Claude can't read this" wall. Install: SessionStart hook in `.claude/settings.json` + pandoc + poppler + xlsx2csv; converts anything dropped in `data/raw_dropzone/` into markdown in `data/converted/`. Working-when: drop a sample messy file, restart the session, watch the `.md` appear. Setup time: 5 minutes.
   - **Step 2, the silver platters** (where the 80% lives — nothing below this step has anything to read without it): one ingest skill per source + one master `/weekly_silver_platters` command, scheduled via cron at the archetype's natural cadence. Use `[DATA_MAP_SILVER_PLATTERS]` for the actual platter names in `requires`/`working_when`, never generic placeholders. Setup time: 1-2 weekends DIY, or ~1 day with an `@claude-code-guide` handoff — recommend the handoff explicitly if `[OPERATOR_TECHNICAL_LEVEL] = non-developer`.
   - **Step 3, the orchestrator + specialists**: chief-of-staff agent + 3-4 domain specialists, each scoped to exactly one silver platter. Use `[DATA_MAP_ORCHESTRATOR_AND_SPECIALISTS]` for real names. Install under `.claude/agents/`: orchestrator on `model: opus`, specialists on `model: sonnet`. Working-when: ask the orchestrator a cross-domain freeform question — it should return ONE paragraph pulling from multiple platters; if it asks which file to look at, the scoping is wrong. Setup time: 1-2 hours.
   - **Step 4, audit log + approval gates**: the trust layer. `PostToolUse` hook captures every Edit/Write to `outputs/audit_log.md`; `Stop` hook nudges (non-blocking, exits 0) if a draft is unsigned at session end. Working-when: open the audit log after a session and every Edit/Write appears timestamped; end a session with an unsigned brief and the Stop hook prints a warning before exit. Setup time: 10 minutes (hooks are pre-written).
   - **Step 5, slash commands**: turn weekly motions into one-keystroke plays, one command per recurring motion, chaining the agents and platters from Steps 2-3. Working-when: typing the right `/weekly_<thing>` at the right time lands the brief in `outputs/` within 60 seconds. Setup time: ~30 minutes for all of them.

2. **If `[IS_REGULATED] = true`, insert a model-lockdown step at position 1 and renumber the rest.** Frame the title per archetype (healthcare: "Lock Bedrock 3P Claude + sign the BAA" / compliance frame "PHI cannot leave your tenant"; law: "Lock Bedrock 3P Claude for matter content" / frame "Matter content cannot leave your tenant, your state bar rules still apply"; wealth: "Lock Bedrock 3P Claude for client + position data" / frame "Client data and personal-trade attestations cannot leave your tenant, Reg BI and custody rules still apply — Bedrock is the answer that passes your CCO's question"). Install: AWS Bedrock 3P Claude config + signed BAA with Anthropic. Working-when: the model picker shows the Bedrock model, not the public anthropic.com model — confirm with `claude config get model`. Setup time: 1-2 weeks for healthcare/law (legal + IT), 3-5 days for solo RIA (CCO sign-off + AWS setup). **Never sequence Step 1 (conversion hook) before this step for a regulated operator, even if they're eager to start** — if they lack AWS exposure, surface that gap explicitly rather than skipping past it.

3. **If `[BUSINESS_ARCHETYPE] = healthcare_clinic`, add a Step 6** after the universal 5: the PHI-scoping rule (`rules/phi_scoping.md`, `paths: [data/clinical/**, data/intake/**]`, always-on). Working-when: ask the billing assistant to show a clinical note — it refuses or says out of scope. Setup time: 30 minutes.

4. **If `[LOCATION_OR_TENANT_COUNT] > 1`, add a sub-step inside Step 4**: "wire the per-tenant rule alongside the audit log" — path-scope per the archetype table (`data/locations/{id}/**` + `rules/per_location.md` for restaurants; `data/agents/{id}/**` + `rules/per_agent.md` for brokerages; `data/providers/{id}/**` + `rules/per_provider.md` for clinics, in addition to PHI scoping; `data/techs/{id}/**` + `rules/per_tech.md` for trades; `data/clients/{id}/**` + `rules/personal_trade_scoping.md` for wealth). Name WHY: each tenant should see only their own slice; the owner/broker/CCO sees all.

5. **Customize every step using `[OPERATOR_ARTIFACT_NAMES]`.** `requires` and `working_when` name the operator's actual silver platter filenames (e.g. "open `silver_platters/finance_weekly_W44.md`"), never "the silver platter file." `install` references the operator's actual store URL, domain, or existing skill names. `before`/`after` use the operator's actual artifact names, not generic descriptions.

## Output Contract

An ordered array of step objects, each complete against: `step`, `title`, `title_friendly`, `requires` (omit only on the true Step 1), `what_to_do` (2-3 sentences: action + why-it-matters in one breath), `why` (1-2 sentences on why this step is gated here), `install` (real multi-line commands), `before`, `after` (each with a real artifact), `working_when` (a concrete self-check the operator can run), `setup_time`. Regulated-archetype and multi-tenant steps inserted per the rules above, with the rest renumbered accordingly. Step 0 never appears in the output.

## Output Skeleton

```json
[
  {
    "step": 1,
    "title": "[internal short title]",
    "title_friendly": "[plain-English, outcome-shaped]",
    "requires": "[Step N done, so X is in place — omit only on true Step 1]",
    "what_to_do": "[2-3 sentences: action + why it matters]",
    "why": "[1-2 sentences: why gated here in the order]",
    "install": "[real multi-line commands]",
    "before": "[status quo, real artifact]",
    "after": "[after-state, real artifact]",
    "working_when": "[concrete operator-runnable sanity check]",
    "setup_time": "[plain-English estimate]"
  }
]
```

## Quality Gate

- Does the plan start at Step 1 (no rendered Step 0), and does Step 1 always precede Step 2 regardless of archetype?
- If `[IS_REGULATED] = true`, is the Bedrock/BAA step at position 1 with every later step renumbered, and does the compliance frame match the named archetype exactly?
- If `[BUSINESS_ARCHETYPE] = healthcare_clinic`, is the PHI-scoping Step 6 present?
- If `[LOCATION_OR_TENANT_COUNT] > 1`, is the per-tenant sub-step present inside Step 4 with the correct archetype-specific path pattern?
- Does every `requires`/`working_when`/`install`/`before`/`after` reference a real operator artifact from `[OPERATOR_ARTIFACT_NAMES]` rather than a generic placeholder?
- Is `setup_time` calibrated to `[OPERATOR_TECHNICAL_LEVEL]` (DIY estimate vs `@claude-code-guide` handoff recommendation)?

## Creative Latitude

The step order and gating logic are locked — do not resequence them for narrative effect. The latitude is in `what_to_do` and `why`: make the gating logic legible to a non-technical operator without softening it into vagueness ("this step needs to happen before that one" is weaker than naming exactly what breaks if skipped). Where an archetype's natural cadence differs from the universal default (e.g. a restaurant's daily close vs a law firm's per-matter cadence), let that show in the install/working_when language rather than forcing every archetype into the same weekly rhythm.

## Deploy When

A data map exists and the operator has moved from "what should I build" to "in what order do I build it" — the 30-day sequenced plan, distinct from the recipe cards (what) and the opportunities brief (why it matters).
