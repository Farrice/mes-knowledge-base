---
name: "Stitch Build Loop — Site Constitution Setup"
source_prompt: born-v2
skill: stitch-loop
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are setting up the "Long-Term Memory" a Stitch build loop depends on: `SITE.md`, the project vision and constitution every future loop iteration reads before touching a single page. Every generation, integration, and next-baton decision in the loop traces back to what this document says the project is, who it's for, and what's still left to build. Get this wrong and every downstream iteration inherits the drift.

## Input Required

```
[PROJECT_NAME] — the site/product name
[STITCH_PROJECT_ID] — existing Stitch project ID, or "to be created on first iteration"
[MISSION] — one to two sentences on what the site achieves
[TARGET_AUDIENCE] — who uses this site
[VOICE] — tone/personality descriptors
[VIBE_PRIMARY] / [VIBE_SECONDARY] / [VIBE_TERTIARY] — aesthetic adjectives, ranked
[KNOWN_PAGES] — any pages that already exist (for Section 4), or "none — greenfield"
[ROADMAP_ITEMS] — known upcoming pages/features, tagged High or Medium priority, or "none yet"
[CREATIVE_FREEDOM_IDEAS] — optional backlog of loosely-scoped page ideas for when the roadmap runs dry
```

## Execution Protocol

Build the document as seven sections, in this order, matching the project's established template exactly:

1. **Core Identity** — Project Name, Stitch Project ID, Mission, Target Audience, Voice. This is the one-paragraph identity a fresh agent instance needs to act consistently without any other context.

2. **Visual Language (Stitch Prompt Strategy)** — state plainly: *strictly adhere to these descriptive rules when prompting Stitch; do NOT use code.* List the "Vibe" as Primary/Secondary/Tertiary adjectives (each with a short parenthetical unpacking what it means in practice — e.g. "Minimal (Clean layouts, breathing room, gallery-like)"). If a color philosophy exists (from `DESIGN.md` or given inputs), state it here semantically, by role (Background/Accent/Text), not just as a hex dump.

3. **Architecture & File Structure** — Root path (`site/public/` unless the project overrides it), the asset flow (Stitch generates to `queue/` → validate → move to `site/public/`), and the Navigation Strategy (what belongs in the global header and footer).

4. **Live Sitemap (Current State)** — a checklist of every page: `[x]` for pages that exist with a one-line description, `[ ]` for pages that are planned but not yet built. Note explicitly: *the agent MUST update this section when a new page is successfully merged* — this is a standing instruction inside the document, not just a description of it.

5. **The Roadmap (Backlog)** — split into High Priority and Medium Priority, each a checklist of concrete, buildable page/feature descriptions. State: *if `next-prompt.md` is empty or completed, pick the next task from here.*

6. **Creative Freedom Guidelines** — the rules for when the roadmap runs dry: stay on-brand (fit the stated vibe), enhance the core (support the mission, don't wander), and use a lowercase/descriptive naming convention. Follow with an "Ideas to Explore" checklist of loosely-scoped page concepts, each with the instruction: *pick one, build it, then REMOVE it from this list.*

7. **Rules of Engagement** — the closing, numbered list of hard rules the loop must never break: don't recreate pages already in Section 4; always update `next-prompt.md` before completing; consume ideas from Section 6 when used; keep the loop moving.

Note the bootstrap dependency: if `[STITCH_PROJECT_ID]` is "to be created," the first loop iteration is responsible for creating the project and persisting the ID to `stitch.json` — don't fabricate a placeholder ID here. If no `DESIGN.md` exists yet, flag it as an open dependency (generate it via the `design-md` skill from an existing Stitch screen, or draft one manually) — SITE.md and DESIGN.md are companion documents; the loop cannot run consistently on one without the other.

## Output Contract

One complete `SITE.md` document: all seven sections present, in order, with the AGENT INSTRUCTION callout at the top ("Read this file before every iteration... If `next-prompt.md` is empty, pick the highest priority item from Section 5 OR invent a new page that fits the project vision"). Every checklist item in Sections 4, 5, and 6 must be a concrete, nameable page or task — no bare "[ ] TBD" entries.

## Output Skeleton

```
---
stitch-project-id: {id or "pending"}
---
# Project Vision & Constitution

> **AGENT INSTRUCTION:** Read this file before every iteration. It serves as the project's "Long-Term Memory." If `next-prompt.md` is empty, pick the highest priority item from Section 5 OR invent a new page that fits the project vision.

## 1. Core Identity
* **Project Name:** {name}
* **Stitch Project ID:** {id or "to be created"}
* **Mission:** {mission}
* **Target Audience:** {audience}
* **Voice:** {voice descriptors}

## 2. Visual Language (Stitch Prompt Strategy)
*Strictly adhere to these descriptive rules when prompting Stitch. Do NOT use code.*
* **The "Vibe" (Adjectives):**
    * *Primary:* {adjective} ({what it means in practice})
    * *Secondary:* {adjective} ({...})
    * *Tertiary:* {adjective} ({...})
* **Color Philosophy (Semantic):** {background / accent / text roles, or "pending DESIGN.md"}

## 3. Architecture & File Structure
* **Root:** `site/public/`
* **Asset Flow:** Stitch generates to `queue/` → Validate → Move to `site/public/`
* **Navigation Strategy:** {header/footer contents}

## 4. Live Sitemap (Current State)
* [x]/[ ] `{page}.html` - {description}
[repeat per known page]

## 5. The Roadmap (Backlog)
### High Priority
- [ ] {task}
### Medium Priority
- [ ] {task}

## 6. Creative Freedom Guidelines
1. Stay On-Brand: ...
2. Enhance the Core: ...
3. Naming Convention: ...
### Ideas to Explore
- [ ] `{page}.html` - {description}

## 7. Rules of Engagement
1. Do not recreate pages in Section 4.
2. Always update `next-prompt.md` before completing.
3. Consume ideas from Section 6 when you use them.
4. Keep the loop moving.
```

## Quality Gate

- Are all seven sections present, in the documented order, with the AGENT INSTRUCTION callout at the top?
- Does Section 3 state the root as `site/public/` and the asset flow as `queue/` → validate → move?
- Is every Section 4/5/6 entry a concrete, nameable page or task rather than a placeholder?
- Does Section 7 explicitly instruct updating `next-prompt.md` before completing and not recreating existing pages?
- If no Stitch project ID or DESIGN.md exists yet, is that flagged as an open bootstrap dependency rather than papered over with an invented value?

## Creative Latitude

The vibe adjectives, Voice descriptors, and the Roadmap/Creative Freedom idea lists are the real design surface of this document — they're what keeps every future page on-brand without a human re-explaining the project each time. Push for adjectives and ideas specific enough to hand directly to a baton-authoring pass without further clarification (a Creative Freedom idea like "gallery.html - Customer homes featuring our furniture" is usable; "gallery.html - a gallery page" is not). Avoid generic SaaS-template language ("modern, clean, professional") unless it's genuinely what distinguishes this project.

## Deploy When

Deploy once, at the start of a new Stitch build loop project, before the first baton is ever written — or when retrofitting SITE.md onto a project that already has pages but no constitution document yet (in that case, populate Section 4's sitemap from what actually exists on disk, not from assumption).
