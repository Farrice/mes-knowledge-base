---
description: "The delivery upgrade that makes a folder of markdown feel like a $1000s product — a branded, clickable KB UI (markdown file browser + graph-narrator, styled via Claude design, built on free OSS graph packages) AND the anti-slop voice charter shipped inside every brand KB (three-word voice, 'what it's NOT', Hard Rule: No AI Writing Tropes + banned list). Abstracts the scary chat box for non-technical buyers."
---

# Workflow 07 — ve-client-ui-layer

> **Produces**: TWO delivery artifacts — (A) a **branded client KB UI spec** (markdown file browser + relationship-narrator knowledge graph, Claude-design-styled, on free OSS graph packages) and (B) the **anti-slop voice charter** (`voice-and-tone.md`) shipped inside the brand KB. Together they turn a markdown folder into a product a non-technical client can navigate and trust.
> **Load first**: [genius.md](../genius.md)
> **Stacks**: `oren-anti-slop-classifier` + `execution/prose_classifier.py` (voice-charter enforcement).

## Role
You are Adam Sandler packaging the KB so a non-technical buyer doesn't freeze at a chat box. Adam: *"there's an abstraction for people who are not as experienced with AI... you put a chat box and you're just like, 'Type slash this.' A lot of people are going to be confused because it's just not how people are used to working."* The UI is the price-justifier; the voice charter is what keeps the output from reading like slop.

## Pre-Flight Gate
- Trigger check: delivering a KB to a non-technical client, or upgrading a bare markdown/chat delivery into a product.
- You need the built KB (the canonical body) and, for the voice charter, the brand's actual voice.

## Skill Acquisition
Read `genius.md` §Pattern 7 (Client UI + Graph-Narrator) + §Pattern 8 (Anti-Slop Voice Charter) + §Hidden Knowledge (the UI is the price-justifier).

## Execution — FROM THE SOURCE

### A. The branded KB UI
1. **Pull the client's style via Claude design** — Adam: *"I'll use Claude design and pull a style guide for them. And then I'll use that style guide to style and design all of the collateral for that relationship."* Brand the UI to the client.
2. **Build a markdown file browser** — Adam: *"Effectively, it could be a markdown file browser... a way for the client themselves to click through their documents."* The client navigates by clicking, not by typing slash commands.
3. **Add the relationship-narrator knowledge graph** (demo t=11:54) — not just a graph, a NARRATOR. A left panel walks numbered entity PAIRS, each with a sentence on WHY they connect. Demo pairs: *1. Keyword Assessment — ICPs · 2. Messaging Framework — Positioning · 3. Content Pillars — Positioning · 4. Post Media Profile — Differentiation Strategy · 5. Company Profile — Positioning · 6. Visual Identity — Company Profile · 7. Brand Profile — Voice & Tone* — then the AI offers: *"Want me to proceed through all seven in this order?"* Competitor nodes render red; clicking one (e.g. Jasper) opens a competitive-relevance panel. Use free/OSS graph packages: *"there's a lot of free and open source packages out there that have knowledge graphs. So, you can just pull something down and implement it yourself into your own app."*
4. **Add the ACCEPT/EDIT recommendation lane** (demo t=11:16) — autonomous agents surface brand-drift/competitive recommendations as cards the client triages with ACCEPT / EDIT.

### B. The anti-slop voice charter (`voice-and-tone.md`, ships inside the KB)
5. **Three-word voice** — demo: *"Voice in Three Words: Direct. Grounded. Unhurried."* Set three for this brand.
6. **What the voice is NOT** — demo: *"Not a cheerleader... Not 'game-changer.' Not AI-hype."* Name the anti-voice explicitly.
7. **Hard Rule: No AI Writing Tropes** + banned list — demo bans: *game-changing, revolutionary, "AI-powered" (standalone), seamless, robust, leverage, unlock, synergy.* Extend with `directives/ai-slop-ban-bank.md`.
8. **On-brand / off-brand sample passages** — show the same message written both ways.
9. **Wire enforcement** — content generated from the KB must pass `execution/prose_classifier.py check`; route to `oren-anti-slop-classifier` for the deeper pass.

## Content Type Adaptations
| Client | Adaptation |
|---|---|
| Non-technical marketing client | Full UI (browser + graph-narrator) + voice charter; hide the chat entirely |
| Technical client | Lighter UI; keep MCP/chat access; still ship the voice charter |
| Content-producing KB | Voice charter is MANDATORY (prevents slop output) |
| Reference-only KB | Voice charter optional; UI browser still valuable |

## Output Requirements
Deliver BOTH: **(A) UI spec** — Claude-design brand style + markdown file browser + relationship-narrator graph (numbered pairs with why-they-connect sentences, red competitor nodes, OSS graph package named) + ACCEPT/EDIT recommendation lane. **(B) voice-and-tone.md** — three-word voice + "what it's NOT" + Hard Rule: No AI Writing Tropes + banned list + on/off-brand samples + `prose_classifier.py` enforcement note. The client can click through their own KB, and its output passes a slop check.

Execution prompt: references/prompts-v2/client-kb-ui-and-voice-charter.md — honor its Output Contract.

## Quality Gate
- Does the UI abstract the chat box (clickable file browser + graph), not just wrap it?
- Is the knowledge graph a NARRATOR (numbered pairs + why-they-connect sentences), not a bare node cloud?
- Is it styled to the CLIENT's brand (Claude design pull), on free/OSS graph packages?
- Does the voice charter have all four parts (three-word voice / what-it's-NOT / Hard Rule + banned list / on-off samples)?
- Is enforcement wired to `prose_classifier.py` + `oren-anti-slop-classifier`?
- Anti-Pattern check (`genius.md`): no bare chat box for a non-technical buyer; no shipping a content KB without the voice charter.
