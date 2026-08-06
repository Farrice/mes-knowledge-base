---
description: SUPERSEDED — dual-format delivery now ships through the brief engine (HTML + md mirror + context pack); see /briefs
status: superseded
superseded_by: briefs
---

# Dual-Format Document Delivery — SUPERSEDED (2026-08-06)

**Follow `.agent/workflows/briefs.md` § What ships as a brief instead.** This workflow's goal — a human-readable format plus an agent-readable companion — is delivered better by `execution/render_brief.py`, which emits the visual HTML brief, the `.md` agent-paste mirror, and the `-context.json` agent pack on every render. This file's original prescription ("clean simple markdown, avoid HTML") predates the Briefing Room and contradicts the ratified Visual Delivery Doctrine; it was invoked by nothing (0 sessions, audit 2026-08-06). Kept for history per superseded-pointer convention.

<details><summary>Original text (historical)</summary>

When creating synthesis documents, research deliverables, or any long-form output that Farrice will need to review and make decisions from, use **clean, simple markdown** that renders beautifully in a markdown viewer.

## Correct Markdown Style

Use the same clean format as agent output files:

1. **Simple headers** with `#`, `##`, `###`
2. **Blockquotes** with `>` for sources and callouts
3. **Bold** with `**text**` for key terms
4. **Numbered lists** and **bullet lists** — no complex nesting
5. **Simple tables** only when necessary — keep columns minimal
6. **Horizontal rules** `---` to separate major sections

## Avoid

- HTML anchor tags (`<a name="...">`)
- Complex multi-column tables
- Dense information without breathing room
- Inline links within prose (put source references as blockquotes below)

## Example Structure

```markdown
# Document Title

> **Context | Date**

---

## Quick Scope

**Question 1?** Answer

**Question 2?** Answer

---

## Section Header

Core insight or statement in prose.

### Subsection

- Point one
- Point two

> Source: filename.md

---
```

## The Standard

If it doesn't render as cleanly as the agent output files (like seth_godin.md or nicolas_cole.md), reformat it until it does.

</details>
