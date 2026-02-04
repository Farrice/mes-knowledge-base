---
description: Always create both a markdown file and a readable plain-text version of synthesis/research documents
---

# Dual-Format Document Delivery

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
