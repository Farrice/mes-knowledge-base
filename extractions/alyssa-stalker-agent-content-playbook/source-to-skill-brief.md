# Source-to-Skill Brief: Alyssa Stalker × The Broke Agent — 2026 Agent Content Playbook

## Verdict

**Build shape:** new component skill with explicit stacking hooks into Enrico (formats), Jen (voice + production), and Kallaway (post-outlier cloning).

**Reason:** The roster covers *how to make realtor content*. It did not cover *how to get an already-posting agent unstuck from their own data* or *connection-first content for an over-lectured audience*. The source's author and thesis are distinct enough that wiring it into Enrico's body would be voice-stacking.

## Objective

Move a stuck agent from "200 to 500 view jail" to content one specific person feels seen by, in seven fireable moves.

## Evidence-to-system map

| Source mechanic (timestamp) | System behavior |
|---|---|
| "It's not a consistency problem... they aren't speaking to anyone specific" [02:44–02:57] | Every run begins with the person, never the format |
| Outlier audit as first move [02:17–02:44], worked examples [03:43–04:20], [16:25–17:12] | `01-outlier-audit` produces an attribute-named hypothesis before any content |
| "Too broad" demographics; pickleball Friday vs. couch rot weekend [05:09–08:03] | `02-one-person-niche` writes the person as a scene |
| One-slide reverse-engineer [06:29–06:36] | `02` includes the one-slide test |
| Topic + Who + Lens reframe [12:12–13:29]; 24-hour interest test [12:35–13:05] | `03-hook-reframe` appends who + lens to any broad hook and states the distribution rationale |
| Comfort creator; feel seen; connection > transactional [16:35–21:40] | `04-comfort-content-engine` builds feeling-first carousels with permission-as-offer |
| Consumer flip "you're not behind, that's exactly who I help" [20:10–20:51] | `04` payoff-slide rule |
| Ricky Carruth create-mode posts; tweet-screenshot-post [22:04–23:13] | `05-create-mode-text-post` |
| Share-to-stories test [23:36–24:42] | Quality gate in `04`, `05`, `06` |
| Local / Listing / Authority mix by goal; authority ≈ monthly; expectations per post [25:50–28:06] | `07-content-mix-planner` goal-tags every slot |
| Review hook-line; green-screen news; breaking-news frame; closing-day capture; different-question reel [29:12–34:02] | `06-authority-as-story` |
| One message, 20–30 seconds [25:40–25:49] | Quality gate across all workflows |
| Lo-fi > produced; AI reframes, never writes [10:09–10:20], [36:19–37:18] | Production rule in `04`/`05`; AI-use rule in SKILL.md |
| Get data, then pivot or double down; avoid five things at once [35:48–36:03], [38:29–38:39] | `01` and `07` hold one experiment for a declared data window |

## Deployed components

| Component | Path | Role |
|---|---|---|
| Skill manifest | `skills/alyssa-stalker-agent-content-playbook/SKILL.md` | Routing, tiers, stacking, recognition test |
| Genius context | `skills/alyssa-stalker-agent-content-playbook/genius.md` | Patterns, exemplars, anti-patterns, heuristics, rubric |
| Workflows 01–07 | `skills/alyssa-stalker-agent-content-playbook/workflows/` | One deliverable each |
| Prompts-v2 | `skills/alyssa-stalker-agent-content-playbook/references/prompts-v2/` | Deterministic output contracts |
| References | `references/source-ledger.md`, `references/hook-reframe-bank.md`, `references/comfort-content-exemplars.md` | Evidence + calibration banks |
| Agent | `agents/alyssa-stalker/AGENT.md` | Persona for the front-door command |
| Behavior proof | `extractions/alyssa-stalker-agent-content-playbook/behavior-proof.md` | Jen before/after |
| Blind pass | `extractions/alyssa-stalker-agent-content-playbook/reference-corpus/`, `blind-pass/` | Real pieces vs. generated |

## Context policy

- Hot only on `/alyssa-stalker-*` invocation. Load genius.md + one workflow + its prompt.
- Transcript and extraction report stay cold behind paths.
- Jen voice files (`skills/jen-santulan-listing-content/genius.md`, `_active/clients/jen-listings/CLAUDE.md`) load for Jen runs only.

## First use

```text
/alyssa-stalker-outlier-audit --agent "Jen Santulan" --window "last 6 months" --posts [metrics table or descriptions]
```

Then `/alyssa-stalker-hook-reframe` on the next three planned local posts. Stop for missing metrics or missing agent voice rather than inventing either.
