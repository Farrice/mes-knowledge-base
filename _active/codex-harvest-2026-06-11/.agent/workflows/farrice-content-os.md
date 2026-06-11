---
description: End-to-end Farrice content operating system for raw concepts, research, brandjacking, hooks, voice, taste, packaging, and engagement
---

# `/farrice-content-os` - Diandra-To-Farrice Content OS

Turn raw concepts, source material, and timely market signals into a nearly publish-ready Farrice content package. This command expands the existing Diandra LinkedIn system instead of replacing it: Diandra is the content infrastructure spine; Farrice's voice, writers' room, taste gates, research standards, and expert stack are the quality floor.

## Use When

- Farrice drops raw thoughts and wants end-to-end content production.
- A source, trend, brand move, or expert idea should become posts, carousels, newsletter sections, short scripts, or offer assets.
- The work needs research, brandjacking, hook engineering, voice calibration, anti-slop protection, and packaging together.
- A LinkedIn-first output should still remain channel-neutral enough to remix across platforms.
- Farrice is deploying The Vibe Tax Diagnostic or The Vibe Tax Brief through `/vibe-tax-deploy`; in that case this OS owns the voice/content composition layer while `/vibe-tax-brief` owns the diagnostic logic.

## Modes

```text
/farrice-content-os setup
/farrice-content-os ingest [raw concept, file path, transcript, URL, or source note]
/farrice-content-os research [topic] [--brandjack|--newsjack|--namejack|--hot-take|--outliers|--audience]
/farrice-content-os sprint --count 20 [--include-brandjacks] [--delegate]
/farrice-content-os week [--include-brandjacks]
/farrice-content-os hook-room [draft id or topic]
/farrice-content-os service-package
/farrice-content-os context-audit
```

Use `--delegate` only when the user explicitly asks for true Codex subagents, parallel agents, or delegated agent work. Without that flag, run the agent roles locally as workflow roles and never imply hidden workers ran.

## Source Authority

Load these sources before drafting or polishing:

1. `FARRICE.md`
2. `_active/farrice-brand/ideation-bank/INDEX.md`
3. Most relevant files under `_active/farrice-brand/identity/`, `_active/farrice-brand/content/`, `_active/farrice-brand/research/`, and `_active/farrice-brand/parallax-design-system/`
4. Existing voice captures and prior storytelling/context documents discovered by `context-audit`
5. `.agent/workflows/writers-room.md`
6. `.agent/workflows/high-taste-writing-os.md`
7. `.agent/workflows/low-cognitive-load-message-gate.md` when a source, product, service, offer, or brand message must be understood before it becomes content
8. `.agent/workflows/voice-first-content.md`
9. `.agent/workflows/anti-slop-audit.md`
10. `.agent/workflows/publishable-copy-gate.md`
11. `.agent/workflows/sam-parr-copywriting-mechanics.md` when the draft needs headline gravity, curiosity, proof-first angle, direct-response rhythm, story desire, or objection-by-detail
12. Diandra source and workflow spine:
    - `.agent/workflows/diandra-linkedin-system.md`
    - `.agent/workflows/diandra-content-engine.md`
    - `.agent/workflows/diandra-growth-sprint.md`
    - `.agent/workflows/diandra-steal-and-remix.md`
    - `skills/diandra-escobar-linkedin-growth/genius.md`
13. Attention hook intelligence layer:
    - `.agent/workflows/attention-hijack-hooks.md`
    - `semantic_libraries/antigravity/primitives/attention-hijack-hook-system.md`
    - `skills/attention-hijack-hooks/SKILL.md`
    - `skills/attention-hijack-hooks/genius.md`

If a source is unavailable, write the gap to `_active/farrice-content-os/context-index.md` and continue with a clearly marked assumption. Do not fabricate missing voice, research, visual, or platform evidence.

## Local State Home

Store the operating system state in `_active/farrice-content-os/`:

| File | Purpose |
|---|---|
| `INDEX.md` | Operator map, mode list, current package status |
| `context-index.md` | Voice, brand, writers' room, and source-context registry |
| `research-ledger.md` | Cited audience, outlier, ICP, market, trend, and factual research |
| `brandjack-board.md` | Brandjack Opportunity Board with ranked brandjack/newsjack/namejack/hot-take opportunities |
| `hook-lab.md` | Hook candidates, hook scores, selected hooks, and rejected generic hooks |
| `content-calendar.md` | Kanban-style content calendar and bucket mix |
| `engagement-list.md` | Recent-activity targets, comment angles, and cadence |
| `content-packs/` | Sprint, weekly, and channel-remix output packages |
| `service-package/` | Client-facing AI Content OS offer assets |
| `templates/content-card-template.md` | Durable content card schema |

## Operating Flow

### 1. Extract

Ingest raw concepts, transcripts, calls, notes, files, prior assets, or the Diandra source video `ZAqIUNAvXXo`.

Output:

- Raw source summary.
- Content argument candidates.
- Missing context or evidence ledger.
- Suggested bucket and first route.

### 2. Context Lock

Before drafting, load the Farrice context base and write a compact context lock:

| Field | Requirement |
|---|---|
| Voice evidence | Phrases, beliefs, interests, and anti-language from Farrice context |
| Writing floor | Relevant `/writers-room`, high-taste, anti-slop, and prior storytelling standards |
| Reader | Specific reader and current mental state |
| Belief movement | Old belief to new belief |
| Refusal | What this piece refuses to sound like or say |
| Source proof | What evidence exists and what is unavailable |

Fail the draft if it skips this step.

### 2.5 Low-Cognitive Message Gate

Run `/low-cognitive-load-message-gate` before Hook Room or content packaging when the input includes a product, service, offer, brand message, source-to-offer idea, or client-facing promise.

The gate does not write the post. It produces a `Low-Cognitive-Load Handoff`:

- locked reader problem
- heavy phrases to rewrite
- hero/guide correction
- repeatability lock
- evidence limits
- PASS / REVISE / REWORK

If the verdict is `REWORK`, do not proceed to hooks, high-taste polish, or publishable copy scoring until the one-problem lock is fixed.

### 3. Research

Research is built in, not optional decoration.

Use a local-first research posture: local context first, then public research when needed. Public web, private account access, paid tools, scraping, publishing, commenting, or external writes require approval when policy or sandbox requires it.

Research lanes:

- Audience psychology and ICP reality.
- Outlier content patterns.
- Market/category shifts.
- Brandjack, newsjack, namejack, and hot-take opportunities.
- Platform mechanics and engagement behavior.
- Factual claims and source citations.

Every research-backed output must include either citations or an explicit unavailable-state note.

### 4. Architect

Map each content argument into Diandra's four-bucket funnel:

| Bucket | Default Share | Job |
|---|---:|---|
| Growth | 35% | Reach new people through attention anchors, brandjacks, newsjacks, namejacks, hot takes, and shareable recognition |
| Authority | 35% | Prove depth, taste, and real operating judgment |
| Conversion | 20% | Create pipeline, service demand, audit interest, or DM movement |
| Personal | 10% | Make Farrice memorable, trusted, and human |

For a 20-post sprint, default to 7 Growth, 7 Authority, 4 Conversion, and 2 Personal posts. At least 3 Growth posts should use brandjack/namejack/newsjack mechanics when `--include-brandjacks` is active.

### 5. Draft

Use Diandra's body-first method:

1. Choose intent and bucket.
2. Write the body first.
3. Mine the strongest, most specific body insight for the hook.
4. Add visual support only when it helps the idea land.
5. Match CTA to bucket.

Drafts must be channel-neutral content arguments first, then adapted for LinkedIn, carousel, newsletter, X/Threads, short script, or service asset.

### 6. Hook Room

No serious post advances without Hook Room.

Run `/attention-hijack-hooks` logic inside Hook Room when the draft needs brand/news/name/trend hijacking, draft rehooking, above-fold fit, first-50 signal, or universal platform adaptation.

Generate at least 10 hooks and rank the top 3. Score each hook against:

- Diandra 2026 format fit: Dense, Punchy plus Context, Single-Line Bomb, Stacked, or Hybrid.
- Curiosity gap: does it open expectation-versus-claim tension?
- First-window fit: can the hook survive the relevant platform fold?
- Mobile cutoff: can it work in the first 8 words or two short lines?
- Curiosity: does it create a real question?
- Belief tension: does it challenge a private assumption?
- Specificity: does it contain a name, number, image, consequence, or precise claim?
- Farrice voice: would he say this, or is it copywriter cosplay?
- Platform pull: does it create dwell, comments, saves, profile clicks, or a real reply?
- Anti-slop: does it avoid generic AI texture, symmetrical slogans, and empty urgency?

Required lenses: Diandra, Kallaway, Lara Acosta, Jasmin Alic, Shaan Puri, Nicolas Cole, and the Publishable Copy Gate.

Use the local mechanical check for serious LinkedIn hooks when there is a concrete candidate:

```bash
python3 execution/attention_hijack_hooks.py --hook "[hook]" --platform linkedin --terms "[topic terms]"
```

Add the Sam Parr Copywriting Mechanics lens when the best hook is still a label, the draft needs a curiosity gap, the proof is abstract, the rhythm is flat, humor needs a fit check, or a conversion post needs story-led desire before the offer appears. Use it as a bounded Hook Room pass, not as the voice owner. Require changed lines and a behavior delta.

### 7. Enhance

Run the writers' room and high-taste writing stack in this order:

1. Structural compression.
2. Emotional and psychological engineering.
3. Platform pull-through.
4. Voice authenticity.
5. Low-cognitive-load gate when the message carries an offer, service, product, or brand promise and has not already passed.
6. Anti-slop audit.
7. Publishable-copy gate when public, revenue-facing, or conversion-oriented.

One composer owns the final voice. Experts are scalpels, not co-authors. Do not concatenate expert outputs.

### 8. Elevate

Use the expert stack only when the output needs that lens:

| Need | Stack |
|---|---|
| System spine | Diandra Escobar |
| Voice and writing floor | Farrice context, `/writers-room`, ghostwriting voice engine, `/high-taste-writing-os`, `/anti-slop-audit` |
| Hooks and reader pull | Kallaway, Lara Acosta, Jasmin Alic, Shaan Puri, Nicolas Cole |
| Psychology and audience | Dai Media, Kieran Flanagan, Rory Sutherland, Erica Mallet, Dan Koe |
| Social and personal brand | Lara Acosta, Josh Sanders, Authority Hacker, Seth Godin, Jensen Brand Physics, `/content-brand-forge` |
| Conversion | Copywriting Agent, Joanna Wiebe, Cardinal Mason, Luke Iha, `/publishable-copy-gate` |
| Direct-response mechanics | Sam Parr Copywriting Mechanics for headline gravity, proof object, curiosity gap, visual proof, rhythm, story-led desire, objection-by-detail, humor fit, and before/after behavior proof |

The final content must show changed lines, stronger argument, and taste evidence. Expert names alone are not proof.

### 9. Package

Produce the output requested by mode:

- `sprint`: 20-post sprint with bucket balance, research anchors, Hook Lab, visual briefs, CTAs, engagement notes, and content cards.
- `week`: weekly batch with calendar, hooks, CTAs, visual notes, and engagement prompts.
- `service-package`: client-facing AI Content OS package, offer promise, intake, audit, delivery steps, proof plan, and reusable assets.
- `research`: cited brief, opportunity board, and next content moves.
- `hook-room`: hook candidates, selected hook, rejected hooks, and revision instructions.
- `context-audit`: context inventory, missing assets, stale assets, and recommended source registration.

## Brandjacking And Research Rules

Growth posts support:

- Brandjack: named brand or company decision.
- Newsjack: timely industry news or platform shift.
- Namejack: notable person, quote, POV, or public move.
- Hot take: consensus belief Farrice can challenge with substance.

Brandjacking must study mechanics and attention anchors, not copy posts. Every remix needs:

- Originality note.
- Farrice-specific point of view.
- ICP relevance.
- Boomerang or engagement potential.
- Citation or unavailable-state note.

## Content Card Interface

Every produced asset uses this durable card shape:

```yaml
id:
raw_source:
bucket:
primary_channel:
secondary_formats:
research_anchor:
brandjack_anchor:
body_draft:
hook_candidates:
chosen_hook:
voice_evidence:
writer_room_pass:
taste_evidence:
visual_brief:
cta:
engagement_plan:
status:
```

Allowed statuses:

`captured -> researched -> queued -> drafted -> hook_pass -> taste_pass -> copy_gate -> visual_ready -> weekly_ready -> service_ready -> archived`

## Quality Gate

Reject or revise if:

- Farrice context was not loaded.
- Research claims lack citations or unavailable-state notes.
- The hook is generic, clever-but-foggy, or not mobile-legible.
- The body was not written before the hook.
- The draft sounds like AI, a template, or a generic LinkedIn strategist.
- The piece uses Diandra mechanics without Farrice's voice and worldview.
- Brandjacking copies an idea instead of extracting a mechanic.
- The hook uses a format but does not create a real curiosity gap.
- The writers' room, taste pass, anti-slop audit, or copy gate is skipped for public/revenue content.
- The status is advanced without the required evidence.

## Verification

Before calling the OS implemented or a package ready, run:

```bash
python3 execution/validate_skill.py source-command-farrice-content-os
python3 execution/verify_farrice_content_os.py
python3 execution/command_menu.py search "Farrice content OS raw concepts voice taste brandjacking hooks"
python3 execution/workflow_router.py search "content done end to end Farrice writers room anti slop Diandra"
```

Use artifact/export guards for substantial written deliverables:

```bash
python3 execution/artifact_router.py classify [artifact path]
python3 execution/artifact_router.py enforce [artifact path]
python3 execution/artifact_frontmatter_guard.py [artifact path]
python3 execution/artifact_surface_guard.py [artifact path]
python3 execution/export_format_guard.py [artifact path]
```

## Starter Route

Use this first when Farrice wants content done end to end:

```bash
/farrice-content-os setup
/farrice-content-os research "AI operating partner for visible experts" --brandjack
/farrice-content-os sprint --count 20 --include-brandjacks
```
