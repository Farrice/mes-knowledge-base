---
name: "source-command-youtube-video"
description: "Create timestamped YouTube context ledgers that separate transcript evidence, frame evidence, OCR evidence, inference, and uncertainty for extraction, strategy, creative analysis, and claim audits."
---

# source-command-youtube-video

Use this skill when the user asks to run the migrated source command `youtube-video`.

## Command Template

<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/youtube-video-context-analysis/SKILL.md`. Also load `skills/youtube-video-context-analysis/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/youtube-video-context-analysis/workflows/01-quick-transcript-ledger.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
