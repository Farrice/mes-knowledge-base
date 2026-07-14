# NotebookLM Pro Outputs (Manual Invocation)

> **Status as of 2026-04-23**: NotebookLM's Pro-tier output features (Mind Maps, Audio Overviews, Infographics) are NOT exposed by the current Chrome-automation integration. The `notebooklm_client.py` wrapper supports query operations only.
>
> **This directive documents when to generate these outputs manually in the browser.** Extending the automation is a future-phase decision — see plan `.claude/plans/i-think-all-the-buzzing-blum.md (ephemeral plan-mode artifact, expired)`.

---

## What Ultra Unlocks in NotebookLM

Per Google AI Ultra subscription:
- **Mind Maps** — visual concept maps auto-generated from notebook sources
- **Audio Overviews** — AI-generated podcast-style conversations about the notebook content (1-2 hosts discussing the source material)
- **Infographics** — visual summaries of key findings
- **Study Guides** — structured Q&A pulled from source material
- **Briefing Docs** — executive summary format
- **Timeline** — chronological view of events across sources

All higher limits/outputs are included in Ultra. No marginal cost.

---

## When to Generate Each Output Type

### Mind Map

**Use for:**
- New expert extraction — map the methodology as a visual graph before writing the skill file
- Research briefs — see where sub-topics connect
- Strategy docs — spot gaps in your argument structure

**Workflow:** After `/extract` or `/deep-research-gemini` finishes, open the notebook (or create one with the output as a source), generate Mind Map, export PNG, attach to the deliverable.

### Audio Overview

**Use for:**
- Long-form deliverables the user wants to consume passively (commute, workout, while doing other work)
- Jen's real estate listing research — turn a neighborhood brief into a 10-min audio for her to listen to
- Parallax editions — generate companion audio for paid subscribers
- Your own knowledge review — Audio Overviews on the 7 registered notebooks as a weekly review ritual

**Workflow:** Generate in NotebookLM browser, download MP3, share via the deliverable Google Drive folder.

### Infographic

**Use for:**
- Client-facing strategy summaries
- Premium deliverable packages (per `/package-deliverable`)
- LinkedIn / social content where a visual summary outperforms text

**Workflow:** Generate in browser, export as image, include in deliverable or repurpose as social asset.

### Study Guide / Briefing Doc / Timeline

**Use for:**
- Onboarding a collaborator or VA to a body of research
- Preparing for a client meeting — "here's what I learned this week"
- Archiving research in a reference-friendly format

---

## Integration With Existing Workflows

These manual outputs pair naturally with:

| Workflow | Suggested Pro Output |
|---|---|
| `/extract` → expert knowledge extraction | Mind Map of the methodology |
| `/deep-research-gemini` or `/deep-research` → strategic research | Briefing Doc for the client, Mind Map for yourself |
| `/parallax` → Substack edition | Audio Overview as companion content for paid subscribers |
| `/ghostwrite` → LinkedIn content from a coach | Study Guide for the coach to review their own methodology |
| `/package-deliverable` → premium package | Infographic for the client |

---

## Manual Invocation Steps

1. Open https://notebooklm.google.com
2. Navigate to the target notebook (or create new from the registry at `mcp-servers/notebooklm/notebooks.md`)
3. Upload source material if needed (research output, transcript, extraction)
4. Click **Audio Overview** / **Mind Map** / **Study Guide** / etc. from the notebook UI
5. Wait for generation (30s-3min depending on output type)
6. Download or copy to the relevant deliverable folder

---

## Budget Note

All outputs are covered by Ultra subscription — **zero marginal cost per output**.

Only the query operations (exposed via `notebooklm_client.py`) count against the 100 query/month budget tracked in `.agent/notebooklm-usage.json`. Generating a Mind Map does NOT count as a query.

---

## Future: Automation

Extending the Chrome automation in `mcp-servers/notebooklm/` to click the Mind Map / Audio Overview buttons programmatically is feasible but not cheap. Current integration uses Playwright + Chrome profile — the buttons exist in the DOM. Extending would require:

- UI element selectors for each output type (fragile — Google ships UI changes often)
- Output capture and download handling
- Integration into existing `notebooklm_client.py` as new methods (e.g., `generate_mind_map(notebook_id)`)

**Recommendation**: Use manually for 30 days. If you find yourself generating the same output type repeatedly (>5x/month), justify the automation investment. Otherwise, manual is fine.

---

*Created: 2026-04-23 | Related: `directives/notebooklm-usage-policy.md`, `mcp-servers/notebooklm/README.md`*
