# the briefing room, in premium minimal

> READOUT OS · SYSTEM BRIEF · window: brand system aug 1 · re-skin aug 6, 2026 · lens: design system · reports · agent feeding · sources: premium minimal package + repo inventory · compiled: aug 6, 2026

the report system, re-skinned to your approved brand and enriched into a briefing + playbook object. this brief is also the living reference: every section kind the engine can render appears below, once, doing real work.

## what changed
_THE ONE-MINUTE VERSION_
Your reports now wear your own brand. The tan Codex Antigravity palette is retired; every brief renders in Farrice Cain Premium Minimal — gray off-white canvas, ink black, silver hairlines, one steel-blue accent — the system you designed on the Codex side and named for Kith-grade restraint. The layout and schema you called close-to-perfect are untouched. Around them: seven new section kinds, an automatic agent context pack beside every brief, and a Briefing Room index page that makes the library one click deep.

## by the numbers
- SECTION VOCABULARY: **14 kinds** (7 original + 7 new, all additive)
- PREMIUM MINIMAL PALETTE: **6 neutrals** (+ 1 steel accent, 2 semantic hues)
- LIBRARY RE-RENDERED: **5 briefs** (from preserved JSON, zero edits)
- RUN COST: **$0** (deterministic local python)

## how we got here
- aug 1 · **Premium Minimal born on the Codex side** — Palette, Helvetica Neue system, 12-col grid law, portable token package — approved visual parent P2-01.
- aug 5 · **Research-brief engine ships** — render_brief.py + /briefs + board shelf; briefs become the readout format you actually want to read.
- aug 6 · **Readout OS: re-skin + enrichment** — Brand imported into the repo, template re-tokened, playbook/assets/visual kinds added, context packs and the Briefing Room go live.
- next · **Phase 2, on your word** — COS primer rendered through this engine; pulse/arsenal/assets boards join the same token family.

## the pipeline
author brief JSON → render_brief.py → briefing room → feed any agent
  - author brief JSON: any session, any launchd loop
  - render_brief.py: HTML + md mirror + context.json
  - briefing room: brief_library.py indexes the library
  - feed any agent: context pack = instant grounding

## what this stands on
- **The palette is your approved brand, verbatim** [VERIFIED] — canvas #F3F3F0, paper #FAFAF8, ink #101010, graphite #555553, line #D8D8D3, stone #8C8C82 — copied from the portable package's design-tokens.json into the template as oklch. (file:///Users/farricecain/Google%20Antigravity/_active/farrice-brand/premium-minimal/package/tokens/design-tokens.json)
- **Kith restraint is the system's own stated reference** [VERIFIED] — “Kith-like restraint applied to business communication” — a taste principle, not a copy instruction. Mood: restrained, contemporary, decisive. (file:///Users/farricecain/Google%20Antigravity/_active/farrice-brand/premium-minimal/package/02-DESIGN-CONTRACT.md)
- **The italic-serif accent word survives as a sanctioned report dialect** [VERIFIED] — Brand law prohibits serif/italic on outward assets; you kept the signature move for internal reports. Documented with rationale and scope. (file:///Users/farricecain/Google%20Antigravity/_active/farrice-brand/premium-minimal/REPORT-DIALECT.md)
- **There was never blue in the approved system — steel blue is a report-dialect addition** [VERIFIED] — The remembered blue was the rejected Midnight Editorial direction (regression evidence). Steel ≈#3D5A94 was chosen fresh as the single functional accent. (APPROVAL-STATE.json · excluded_branches)

## when to reach for which section
- **DIGEST · FAST**: summary (the one-minute version), stats (big numbers first), bars (shape comparisons)
- **DIGEST · DEEP**: evidence (claims with chips + sources), timeline (how we got here), matrix (this thing)
- **ACT · NOW**: deploy (copy-paste blocks), playbook (plays with receipts), decision (the ranked opening)
- **ACT · NEXT**: related (swing links), assets (the rail), caveats (what this isn't)

## the library so far
- aug 5: 2
- aug 6: 4
_briefs rendered per day since the engine shipped_

## how to use it
the report is now the default readout surface. in order:
1. **Open the Briefing Room, not folders** — deliverables/research-briefs/index.html lists everything newest-first with md + ctx one click away.
2. **Ask for any readout “as a brief”** — research, audits, mission close-outs, build reports — the engine renders them all; night-shift proved the mission-report shape.
3. **Feed agents the context pack, not prose** — every brief ships <slug>-context.json — paths with roles — so a fresh session grounds itself in seconds.
4. **Say the word for Phase 2** — COS primer through this engine + the boards re-themed to the same tokens; parked, named, ready.

## the playbook
1. **Render (or re-render) a brief** — Any brief JSON becomes the full four-artifact set.
```
python3 execution/render_brief.py deliverables/research-briefs/<slug>/<slug>-brief.json --open
```
   touches: execution/render_brief.py · templates/research-brief/template.html
   receipt: console prints OK/md/ctx lines; browser opens the brief
2. **Refresh the Briefing Room** — After new briefs land, rebuild the index.
```
python3 execution/brief_library.py --open
```
   touches: execution/brief_library.py · deliverables/research-briefs/index.html
   receipt: count line at the top matches the number of brief folders
3. **Re-skin everything after a token change** — Tokens live in ONE place now — change them there, re-render the library.
```
for j in deliverables/research-briefs/*/*-brief.json; do python3 execution/render_brief.py "$j"; done && python3 execution/brief_library.py
```
   touches: templates/research-brief/template.html
   receipt: all briefs + index show the new tokens; no tan anywhere

## the rail
- **Premium Minimal brand guide (12-page field guide)** [BRAND GUIDE] `_active/farrice-brand/premium-minimal/package/templates/field-guide/Farrice-Cain-Premium-Minimal-Brand-System-V1.pdf` — the approved system, as a book
- **Machine-readable design tokens** [TOKENS] `_active/farrice-brand/premium-minimal/package/tokens/design-tokens.json` — single source of truth for palette + type
- **Report template (implementation of record)** [TEMPLATE] `templates/research-brief/template.html` — all report CSS lives here, never inline
- **Report dialect decision record** [DOCTRINE] `_active/farrice-brand/premium-minimal/REPORT-DIALECT.md` — why serif accent + steel blue are sanctioned

## swings to
- [BRIEF] night shift build report — the mission-report shape — deliverables/research-briefs/night-shift-2026-08-06/night-shift-2026-08-06-brief.html
- [BRIEF] ai marketing agents: hype vs. harness — the exemplar you named — deliverables/research-briefs/ai-marketing-agents-hype-vs-harness/ai-marketing-agents-hype-vs-harness-brief.html
- [LIBRARY] the briefing room (all briefs) — deliverables/research-briefs/index.html
- [WORKFLOW] /briefs — authoring + rendering doctrine — .agent/workflows/briefs.md

## deploy blocks
**open the briefing room**
```
python3 execution/brief_library.py --open
```
**ask for any readout in this format**
```
render that as a research brief (brief JSON → execution/render_brief.py) and refresh the briefing room
```

## what this isn't
_CAVEATS WORTH KEEPING_
This is the internal report dialect, not the outward brand: LinkedIn, banners, and client assets still follow the strict Premium Minimal law (no serif, no added hues) and the package's approval state still reads 0.9-review with external action unauthorized. The steel accent value is a first pass — if it reads too cool or too loud after a week of real briefs, it is one token in one file. And the brand system's only fully-approved asset remains the banner; everything else in the package is review-state.

## Source ledger
1. Farrice Cain Premium Minimal portable package v0.9-review (imported from Codex scratch 2026-08-06) — file:///Users/farricecain/Google%20Antigravity/_active/farrice-brand/premium-minimal/package/MANIFEST.json (retrieved 2026-08-06, VERIFIED; used for: palette, typography, grid law, prohibitions, approval state)
2. Repo exploration — brief engine + every HTML surface inventoried — file:///Users/farricecain/Google%20Antigravity/execution/render_brief.py (retrieved 2026-08-06, VERIFIED; used for: template/token architecture, section renderer map, re-theme surface list)

## Context pack (agent feed)
- `_active/farrice-brand/premium-minimal/REPORT-DIALECT.md` — report dialect doctrine
- `execution/brief_library.py` — briefing room generator
- `.agent/workflows/briefs.md` — authoring workflow
- `_active/farrice-brand/premium-minimal/package/tokens/design-tokens.json` — design-tokens.json
- `_active/farrice-brand/premium-minimal/package/02-DESIGN-CONTRACT.md` — design contract
- `execution/render_brief.py` — playbook · Render (or re-render) a brief
- `templates/research-brief/template.html` — playbook · Render (or re-render) a brief
- `deliverables/research-briefs/index.html` — playbook · Refresh the Briefing Room
- `_active/farrice-brand/premium-minimal/package/templates/field-guide/Farrice-Cain-Premium-Minimal-Brand-System-V1.pdf` — asset · BRAND GUIDE
- `deliverables/research-briefs/night-shift-2026-08-06/night-shift-2026-08-06-brief.html` — related · BRIEF
- `deliverables/research-briefs/ai-marketing-agents-hype-vs-harness/ai-marketing-agents-hype-vs-harness-brief.html` — related · BRIEF
- `_active/farrice-brand/premium-minimal/package/MANIFEST.json` — Farrice Cain Premium Minimal portable package v0.9-review (imported from Codex scratch 2026-08-06)

_run cost $0.00 — stack: render_brief.py · brief_library.py · premium-minimal tokens_
