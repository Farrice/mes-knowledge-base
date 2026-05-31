# HOOK-DEPLOY — LinkedIn Growth Hooks ONLY

> ⛔ **SCOPE GUARD — read this first.**
> This is a **passive reference**, not a route. Nothing here runs automatically.
> It applies to **LinkedIn growth posts + re-hooking flops, ONLY.**
> It does **NOT** apply to: Parallax, Substack, memoir, client docs, or your
> default LinkedIn voice system (that stays `/ghostwrite` + Lara Acosta + your
> voice rules in `../CLAUDE.md`).
> Fire these commands **only when you choose to.** This file does not change any
> default — your CLAUDE.md routing is untouched.

---

## When this is the right tool

Reach for Diandra's hook system **only** when you've already decided you're shipping a **LinkedIn growth-bucket post** (reaching new people) or **reclaiming a flopped post**. It's a scalpel for hooks, not your content engine. For Parallax, memoir, or your LinkedIn *voice*, ignore this file entirely.

---

## IF → THEN

| IF you're… | FIRE | Back |
|---|---|---|
| Finishing a LinkedIn growth post | `/diandra-post-finisher "topic or body" --bucket Growth` | Ship-ready post + receipts |
| Topic only, no draft | `/diandra-content-engine "topic" --bucket Growth` | Body-first draft |
| Draft done, only need the hook | `/diandra-hook-architect "[full draft]"` | 8-10 validated hooks + top 3 |
| Teaching / framework / data post | `/diandra-save-architect "[draft]"` | Body re-architected for saves |
| Worried the algorithm can't place it | `/diandra-first-50 "[opening]"` | First-50 tuned for AI retrieval |
| Sitting on posts that flopped | `/diandra-rehook-teardown "[1-10 posts]"` | Diagnosis + rebuilds |
| Reach dropped, cause unknown | `/diandra-algorithm-audit` | 6-layer suppression diagnosis |
| Fixing your profile headline | `/diandra-headline-engineer "[current]"` | 5 dual-scored candidates |

---

## The canonical order (if you ever run stages by hand)

```
09 write → 18 saves (ONLY if teaching/data) → 20 hook → 17 signal
```
`/diandra-post-finisher` runs this whole line for you. Never reorder it: 18 rewrites the body, so the hook (20) must be mined after; 17 confirms signal last.

---

## Copy-paste card

```
DEFAULT (growth post): /diandra-post-finisher "draft" --bucket Growth --media none --register formal
TOPIC ONLY:            /diandra-post-finisher "topic" --bucket Growth
HOOK ONLY:             /diandra-hook-architect "[full draft]"
RECLAIM FLOPS:         /diandra-rehook-teardown "[old posts]"
ORDER:                 09 write → 18 saves(if teaching) → 20 hook → 17 signal
PRE-POST:              mobile previewer check, always
```

---

## Don't-break-it rules

1. **Wrong workspace = don't use it.** Parallax/Substack/memoir → this file is off-limits. Those flatten under growth-feed hook mechanics.
2. **Never run `/diandra-save-architect` on a personal/vulnerability post.** Save-architecture is for teaching/data only.
3. **Feed the whole post, never a one-liner** — your best hook is usually buried mid-draft.
4. **Top-3 pick is a starting point, not a verdict.** Your judgment is final.
5. **It won't invent numbers.** No real data point → it changes angle. Don't override.
6. **Single-Line Bomb is rare (~2%).** Not nervous it's too bold → take Punchy+Context.

---

*Full system: `skills/diandra-escobar-linkedin-growth/SKILL.md` → § The Production Line. This card is a convenience menu; the SKILL.md is the source of truth.*
