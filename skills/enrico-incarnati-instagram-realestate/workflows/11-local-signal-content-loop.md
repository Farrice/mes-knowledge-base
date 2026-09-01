---
description: Convert local sources, transferable patterns, and lived observations into original Realtor content that earns qualified local attention and opens human conversations
---

# /enrico-local-signal-loop — Local Signal → Original POV → Conversation

Use this workflow when an agent is stuck recycling market updates, listing announcements, and generic tips—or when they have local ideas but no reliable way to decide what is worth making.

This is an Enrico-owned connected workflow. Enrico conducts the Instagram and hyperlocal strategy. The 2026 Mike Sherrard/Matt Thornburg source contributes the local-signal, creator-fit, sustainable-production, and conversation mechanics. Kallaway is optional and remains cold until relevant first-party performance data exists.

## Usage

```text
/enrico-local-signal-loop ideate --agent "[name]" --market "[market]"
/enrico-local-signal-loop scripts --agent "[name]" --goal "three ready-to-film Reels"
/enrico-local-signal-loop week --agent "[name]" --goal "sustainable weekly plan"
/enrico-local-signal-loop campaign --agent "[name]" --goal "local attention to buyer conversations"
```

## Required context

Read only what the run needs:

1. `skills/enrico-incarnati-instagram-realestate/genius.md`
2. `skills/enrico-incarnati-instagram-realestate/references/prompts-v2/local-signal-content-loop.md`
3. `extractions/video-context/eDGyKfiXsyQ/source-to-skill-brief.md`
4. `skills/mike-sherrard-realtor-branding/genius.md` for positioning and message-to-conversation mechanics
5. For Jen only: `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md` and `skills/jen-santulan-listing-content/references/jen-calibration-log.md`

Do not load Kallaway or an outlier system unless the agent supplies relevant own-channel performance data. Public views from another creator are format evidence at most.

## Operating outcome

Produce content that a specific local person recognizes, the agent can say without performing a borrowed persona, and a human can respond to after the CTA. “Viral” means unusually strong qualified local attention; it does not mean maximum raw reach.

## Phase 1 — Agent Fit Card

Do not ideate until this card is usable:

```yaml
agent_fit_card:
  name: ""
  market: ""
  niche: ""
  target_person: ""
  existing_audience: ""
  voice_markers: []
  genuine_interests: []
  convictions_or_experiences: []
  production_comfort: "talking-head | green-screen | voiceover | faceless | mixed"
  max_posts_per_week: 0
  offer: ""
  human_response_owner: ""
  compliance_boundaries: []
```

### Fit rules

- The target is one plausible local person, not “buyers and sellers.”
- Genuine interests must come from the agent's words, behavior, or approved context—not a generated brand persona.
- Production comfort and weekly capacity set the cadence. Never prescribe daily posting when the card cannot support it.
- If voice samples or convictions are missing, the system may prepare sourced premises and questions but must not invent the agent's final opinion.

## Phase 2 — Signal Pack

Collect at least five candidates so selection is real. Every row needs provenance and an allowed transfer scope.

| Signal type | Evidence requirement | Allowed transfer |
|---|---|---|
| `local_source` | URL, publisher, date, and the factual claim actually supported | Topic and facts with citation; never automatic causation |
| `format_reference` | Source URL or saved-item reference plus what visibly worked | Format only unless topic relevance is separately proven |
| `lived_observation` | Agent-owned note, story, encounter, or repeated client question | Agent's experience and opinion after approval |
| `own_channel_signal` | First-party post and audience/metric context | Pattern input for this agent only |

Each candidate must state:

```yaml
signal:
  id: ""
  source_type: "local_source | format_reference | lived_observation | own_channel_signal"
  source: ""
  date: ""
  evidence_status: "VERIFIED | LIKELY | UNCONFIRMED | SYNTHETIC"
  market: ""
  target_person: ""
  transfer_scope: "topic_and_format | topic_only | format_only | lived_experience"
  original_pov: ""
  supported_by_agent_fit: true
  voice_match: true
  score_inputs:
    local_specificity: 0
    audience_relevance: 0
    creator_conviction: 0
    conversation_potential: 0
    production_fit: 0
```

## Phase 3 — Hard rejection and scoring

Create a temporary JSON payload under `.tmp/` and run:

```bash
python3 execution/realtor_local_signal_engine.py .tmp/[run-slug]-local-signals.json
```

### Hard rejection conditions

Reject before scoring when any condition is true:

- A factual local claim has no traceable source.
- The language steers by protected class or uses fair-housing danger phrases.
- The candidate copies wording or a creator persona instead of transferring a topic or format.
- No plausible local target person is named.
- The opinion is not supported by the Agent Fit Card.
- The draft is generic AI voice or has not reached the agent checkpoint.
- A nonlocal high-reach topic is being imported as topic evidence rather than format-only research.

### Qualified-local-attention score

Score surviving candidates 0–2 on:

1. Local specificity
2. Audience relevance
3. Creator conviction
4. Conversation potential
5. Production fit

Rank by total. Ties go to creator conviction, then production fit. Reach evidence annotates a qualified candidate; it never reverses a rejection.

## Phase 4 — Build Local Content Cards

Produce the requested number of cards from the highest-ranked candidates. Each card must contain:

```yaml
local_content_card:
  title: ""
  target_person: ""
  recognizable_tension: ""
  source: ""
  evidence_status: ""
  original_pov: ""
  hook: ""
  beat_map: []
  visual_plan: ""
  cta: ""
  human_response_path: ""
  real_estate_memory: ""
  attention_metrics: []
  pipeline_metrics: []
  voice_approved: false
  cadence: ""
```

### Card construction rules

- **Recognizable tension:** name a private question, tradeoff, or local change the target person already feels.
- **Original POV:** the agent's interpretation is the creative center. If it is not approved, mark `[AGENT POV NEEDED]` and stop short of ready-to-post status.
- **Hook:** use local specificity and a clear question or thesis. Do not manufacture outrage or certainty.
- **Beat map:** write conversational beats before a polished script. A script is a toolbelt, not a performance the agent must imitate.
- **Visual plan:** choose the easiest credible format for this agent: phone talking head, foreground cutout over local B-roll, voiceover, faceless field footage, or mixed.
- **Real-estate memory:** the content may lead with local life, but the viewer must still understand why following this agent helps with a real-estate decision.
- **CTA:** use a low-pressure next step that a real human is prepared to answer.

## Phase 5 — Voice and compliance checkpoint

The agent or approved voice owner must confirm:

1. “I would actually say this.”
2. “This opinion is mine.”
3. “The factual source still supports the line.”
4. “The piece describes property, place, or process—not the protected identity of who belongs there.”
5. “Someone owns the reply after the CTA.”

Until all five pass, set `voice_approved: false` and label the card `DRAFT / NOT READY TO PUBLISH`.

## Phase 6 — Conversation bridge

Every approved card specifies the post-response path:

```text
Content gift → low-pressure CTA → one routing question → human reply → need-discovery question → CRM next action
```

- Automation may deliver a promised resource or ask one routing question.
- Human conversation owns nuance, need discovery, and any advice.
- Do not force a property pitch into a content-only conversation. Ask, listen, and preserve consent.

## Phase 7 — Learning receipt

Track two separate ledgers:

| Attention evidence | Pipeline evidence |
|---|---|
| Local reach, watch behavior, saves, shares, profile visits | DMs, qualified conversations, appointments, clients, collected revenue |

- Never call attention evidence a lead.
- Record absent publication or distribution as `NO EVENT`.
- Use Kallaway only when the agent has enough relevant first-party rows to compare cohorts or patterns. Until then, keep performance conclusions `UNTESTED`.

## Output contract

1. Completed Agent Fit Card
2. Signal Pack with provenance and transfer scope
3. Accepted ranking table
4. Explicit rejection receipts
5. Requested Local Content Cards
6. Voice/compliance checkpoint status
7. Conversation bridge
8. Separate attention and pipeline measurement plan
9. Evidence limits and next proof gate

## Skill-system handoffs

### Intake → Selection

- **Source evidence:** Agent Fit Card and Signal Pack paths
- **Output:** validated candidates and rejected rows
- **Open risk:** missing source, voice, or local target

### Selection → Creation

- **Source evidence:** accepted rows only
- **Output:** Local Content Cards
- **Open risk:** agent POV remains human-owned

### Creation → Conversation

- **Source evidence:** voice-approved cards
- **Output:** CTA and human response path
- **Open risk:** no lead claim before actual conversation evidence

### Conversation → Learning

- **Source evidence:** first-party attention and pipeline events
- **Output:** separated learning receipt
- **Open risk:** `NO EVENT` or thin sample remains visibly thin

## Stop conditions

Stop and surface the exact missing input when:

- a local factual claim cannot be sourced,
- the Agent Fit Card cannot support an opinion,
- the only available idea requires fair-housing steering,
- no one owns the CTA response,
- or the requested cadence exceeds the agent's declared capacity.

Publishing, outreach, DM automation activation, and external writes require separate authorization.

**Execution prompt:** `skills/enrico-incarnati-instagram-realestate/references/prompts-v2/local-signal-content-loop.md`
