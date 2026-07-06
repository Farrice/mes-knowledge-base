# Thought-Bank — INDEX

> **Personal ideation + voice bank.** Raw thoughts, hooks, POV anchors. Feeds Parallax / daily-flywheel / voice-first-content / ghostwrite / serial-arc workflows with voice-true material.

**Last captured**: 2026-05-05 (parenting-as-marketing thesis + JJ outburst observation; +taste calibration of 3 variants → A:7 / B:8 / C:2; +new POV anchor #4 banning cheap question signoffs)
**Total entries**: 1 inbox dump · 4 hooks in bank · 4 POV anchors active
**See also**: [README.md](README.md) for the capture/process loop.

---

## How capture works now (2026-07-06)

Capture used to depend on the model remembering to write here mid-conversation
— that's why there was exactly one entry in two months. It's now a
deterministic pipeline with a physical backstop at every hop:

1. **`/dump`** (COS front door) → its Capture Discipline step for content
   sparks shells `python3 execution/thought_bank.py capture "<text>" --theme <t> --source dump`
   (or the equivalent `cos_prep.py capture --route inbox`, which now delegates
   to the same function). Appends `## HH:MM — <first 8 words>` + body +
   `*Theme:*` / `*Source:*` tags to `inbox/YYYY-MM-DD.md` (one file per day,
   append-only), and mirrors the entry into `.memory/sovereign.db`
   (`tier=episodic, category=milestone, source=thought_bank`) so it flows into
   the existing weekly distill pipeline.
2. **Nightly backstop** — `execution/harvest_memory_daily.py` (launchd daily)
   scans the last 24h of raw episodic exchanges for user turns opening with
   `/dump`, `thought:`, `note to self`, or `capture this`, and appends any not
   already in today's inbox file (deduped by normalized first-60-chars). This
   is what guarantees capture even when a `/dump` session happened but the
   CLI call got skipped conversationally.
3. **Weekly distill** — the sovereign-mirrored entries cluster and get
   proposed as semantic rules the same way every other episodic record does;
   nothing auto-promotes, `memory_review.py` stays the human gate.
4. **Themes stay human-curated.** Routing a raw entry into a `themes/*.md`
   file (or promoting a stub theme to active) is still a deliberate editorial
   pass, not automated — the deterministic layer only guarantees the raw
   material lands in the inbox, not that it gets processed.

CLI: `python3 execution/thought_bank.py capture "<text>" [--theme T] [--source S]`
· `list [--days N]` · `stats`.

---

## Active themes (have entries)

| Theme | Last entry | Source |
|---|---|---|
| [parenting-as-marketing](themes/parenting-as-marketing.md) — Master class in marketing, persuasion, influence | 2026-05-05 | [inbox/2026-05-05.md](inbox/2026-05-05.md) |
| [empathy-vs-manipulation](themes/empathy-vs-manipulation.md) — Empathy is doing what it takes, with positive intent | 2026-05-05 | [inbox/2026-05-05.md](inbox/2026-05-05.md) |
| [presence-vs-screens](themes/presence-vs-screens.md) — The discipline: work when he sleeps, presence when he's awake | 2026-05-05 | [inbox/2026-05-05.md](inbox/2026-05-05.md) |

## Stub themes (mapped to FARRICE.md interest stack — awaiting entries)

| Theme | FARRICE.md rank |
|---|---|
| [father-wound-generational](themes/father-wound-generational.md) — Generational pattern breaking | #1 (9.3) |
| [anti-guru-crusade](themes/anti-guru-crusade.md) — Systemic critique with solutions | #2 (9.7) |
| [prompt-engineering-craft](themes/prompt-engineering-craft.md) — MES 3.0, context engineering | #3 (9.7) |
| [gaming-anime-metaphors](themes/gaming-anime-metaphors.md) — RPG/training-arc analogies | #4 (8.3) |
| [spirituality-manifestation](themes/spirituality-manifestation.md) — Neville, Dispenza, shadow work | #5 (8.3) |
| [biracial-identity](themes/biracial-identity.md) — "I've never fit one box" | #6 (8.7) |
| [general-observations](themes/general-observations.md) — Catchall (promote at 3+ entries) | n/a |

---

## Reusable artifacts

| Artifact | Count | File |
|---|---|---|
| Hooks (deployable one-liners) | 1 active + 9 candidates | [hooks-bank.md](hooks-bank.md) |
| POV anchors (voice rules) | 3 active | [pov-anchors.md](pov-anchors.md) |

---

## Inbox (raw, date-stamped, voice-preserved)

| Date | Topics |
|---|---|
| [2026-05-05](inbox/2026-05-05.md) | JJ outburst → cheap dopamine wake-up · presence-vs-screens commitment · parenting-as-marketing thesis · "I just manipulated my 2-year-old son" hook · empathy-vs-manipulation reframe |

---

## Theme → Workflow routing (suggested defaults)

| Theme | Best workflow | Output |
|---|---|---|
| parenting-as-marketing | `daily-flywheel` or `parallax --quick` | 3 LinkedIn variants OR Substack edition |
| empathy-vs-manipulation | `voice-first-content` or `parallax --quick` | Psychology-first LinkedIn / Substack |
| presence-vs-screens | `voice-first-content` or `daily-flywheel` | Personal voice-led content |
| father-wound-generational (stub) | `voice-first-content`, `serial-arc` | Voice-led / multi-chapter |
| anti-guru-crusade (stub) | `daily-flywheel`, `jackpost` | LinkedIn critique / borrowed-attention |
| prompt-engineering-craft (stub) | `voice-first-content`, `parallax --quick` | Authority content |
| gaming-anime-metaphors (stub) | `daily-flywheel`, `parallax --quick` | High-vulnerability content (after trust) |
| spirituality-manifestation (stub) | `voice-first-content`, `parallax --quick` | Long-form synthesis |
| biracial-identity (stub) | `voice-first-content`, `parallax --quick` | Identity-led content |

---

## Promotion criteria

- **Stub → active**: 1+ entry routes to that theme
- **General observation cluster → new theme**: 3+ entries cluster around a recognizable pattern; create a dedicated theme file, migrate entries, update this INDEX
- **Hook candidate → deployable hook**: passes voice test ("would Farrice say this to a friend?"), gets dated entry in `hooks-bank.md`
- **POV anchor**: new entry whenever a captured reframe is identity-level (not topical)
