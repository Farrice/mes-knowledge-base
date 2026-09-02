# Skill System Contract — alyssa-stalker-agent-content-playbook

| Field | Value |
|---|---|
| Source evidence | `extractions/alyssa-stalker-agent-content-playbook/raw/transcript.md` (7,963 words, auto-captions, timestamped), `raw/transcript.vtt`, `raw/metadata.json`. Limits in `uncertainty-report.md`: transcript-only, no frame pass; several proper nouns are ASR variants. |
| Objective | Give a posting-but-stuck real estate agent (Jen first) a repeatable path from "500 view jail" to content one specific person feels seen by: outlier diagnosis → one-person aim → who+lens hooks → comfort/connection content → goal-tagged mix. |
| Components | NEW skill `skills/alyssa-stalker-agent-content-playbook/` (SKILL.md, genius.md, 7 workflows, 3 references, 7 prompts-v2); NEW agent `agents/alyssa-stalker/AGENT.md`; minted wrappers via `mint_menu_wrappers.py`; EXISTING: `enrico-incarnati-instagram-realestate` (formats, local signal loop), `jen-engine` (production pipeline), `jen-santulan-listing-content` (voice), `kallaway` (clone-don't-copy after outlier), `prose_classifier.py`, `skill_auditor.py`, `blind_pass.py`. |
| Step order | 01 outlier-audit → 02 one-person-niche → 03 hook-reframe → (04 comfort-content-engine ‖ 05 create-mode-text-post ‖ 06 authority-as-story) → 07 content-mix-planner → jen-engine Stage 3/4 for production. 03 depends on 02's person card; 07 depends on 01's hypothesis. 04–06 are parallel and optional per month. |
| Inputs | 01: 6 months of posts with metrics or descriptions. 02: agent's own words about who they connect with + personal signals. 03: a broad hook or topic + person card. 04/05: person card + the private feeling. 06: a review/award/ranking + the transaction story. 07: goal (grow/convert/nurture) + outlier hypothesis + capacity. |
| Outputs | 01 Outlier Audit Card · 02 One-Person Niche Card · 03 Hook Reframe Set · 04 Comfort Carousel Pack · 05 Create-Mode Text Post Set · 06 Authority Story Pack · 07 Goal-Tagged 30-Day Plan. All Markdown, copy-paste ready, fair-housing checked. |
| Handoff summary | Each workflow ends with a `## Handoff` block: what was produced, the one line the next step needs, open risk. Never pass the transcript downstream; pass the card. |
| Composition rule | Alyssa owns diagnosis, aim, framing, and connection content. Enrico owns format mechanics and profile. Jen genius owns voice. Kallaway is cold until first-party outlier data exists. One author per body of copy. |
| Human checkpoint | Agent voice approval before any post is marked ready ("would I say this?"); fair-housing check on every consumer-facing piece; Farrice verdict on Jen deployments. No external posting from this system. |
| Validation | `python3 execution/skill_auditor.py check --skill alyssa-stalker-agent-content-playbook` (7 heartbeat checks) · `python3 execution/renaissance_audit.py` (0 fail) · `python3 execution/blind_pass.py prepare/record --expert alyssa-stalker-agent-content-playbook` · `python3 execution/prose_classifier.py check` on generated copy · `python3 execution/sync_registries.py --check` before write. |
| Behavior-changing proof | `behavior-proof.md`: before/after transformation of a Jen local post and a Jen FTHB education post using workflows 03 and 04, with diagnosis, source mechanic, behavior delta, proof object, proof gap, next gate. |
| Result surface | Cards in conversation; files under the skill and extraction folders; Jen pieces flow into `jen-engine` Stage 3/4 and the existing SEND shape. |
| Context policy | Hot: SKILL.md when a `/alyssa-stalker-*` command fires. Warm: genius.md + the one workflow + its prompt. Cold: transcript, extraction report, vision, uncertainty report. Jen voice files load only for Jen runs. |
| Reuse hook | Hook grammar (Topic + Who + Lens) and goal tags (grow/convert/nurture) are portable to any local-content or content-calendar skill; cite this skill rather than re-deriving. |
| Goal packet | Not required — no self-improvement or maintenance behavior changes. |
| Agentic engineering packet | Not required — no context policy, review loop, dependency, or launch behavior changes. |

## Handoff shape used inside the workflows

```markdown
## Skill System Handoff: [step] -> [next step]
- Source evidence: [timestamp rows used]
- Component used: [workflow]
- Output produced: [card]
- Next input: [one line]
- Validation: [pass/fail + check]
- Open risk: [exact limitation]
```

## Quality gate applied to this build

- Not a mega-skill: 7 workflows, one deliverable each.
- Existing routes checked: `command_menu.py search` returned Enrico, Sherrard, Kallaway, Maria Wendt — none own the six gap capabilities in `vision.md`.
- Source grounded: every genius pattern carries a timestamp; ASR variants labeled in `uncertainty-report.md`.
- Behavior proof present: `behavior-proof.md`.
- No hidden chat context: every card is file-backed.
