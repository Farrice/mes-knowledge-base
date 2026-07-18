# Provenance — knowledge-architecture-studio repair

Anchor → source file + location table for every quote/citation added to `genius.md`.
All sourced from files already committed in `skills/knowledge-architecture-studio/`,
`agents/knowledge-architecture-studio/`, or their references — no external material.

| Anchor text used in repaired genius.md | Source file | Location |
|---|---|---|
| "Draw the graph, not the glossary" | `workflows/01-extract-knowledge-architecture.md` | Phase 2, Layer 3 bullet (line 32) |
| "the template serves the domain's actual shape, not the reverse" | `references/prompts-v2/extract-knowledge-architecture.md` | Creative Latitude paragraph (line 107) |
| "confirm the agent produces expert-grade output with zero external retrieval — all expertise lives in-package" | `references/prompts-v2/architect-domain-agent.md` | Phase 3, "Run the encapsulation audit" bullet (line 54); also `workflows/03-architect-domain-agent.md` line 43 ("Encapsulation audit: confirm the agent produces expert-grade output with **zero external retrieval** — all expertise lives in-package.") | 
| "weight the layers toward what this domain type rewards" | `workflows/01-extract-knowledge-architecture.md` | Phase 3 bullet (line 40) |
| "one with only System 1 is a reckless guesser" | `references/prompts-v2/architect-domain-agent.md` | Phase 1, Component 2 (line 30) |
| "Where the source is silent, mark UNCONFIRMED — never fabricate expertise to fill a template slot" | `workflows/01-extract-knowledge-architecture.md` | Phase 1 closing line (line 26) |
| "outside what I reliably know" | `workflows/03-architect-domain-agent.md` | Quality Gate, "Edge-Case & Boundary Behavior" item (line 58) |
| "it never mistakes explicit content for mastery" | `agents/knowledge-architecture-studio/AGENT.md` | Opening description paragraph (line 9) |
| "if you can't, you treat that as proof the expertise wasn't fully understood yet" | `workflows/02-build-mastery-pathway.md` | Role paragraph (line 10) |
| "Layer 7 specifies both a knowledge-updating mechanism and a paradigm-conflict resolution approach" | `references/prompts-v2/extract-knowledge-architecture.md` | Quality Gate, last item (line 102) |
| "ask one targeted clarifying question; otherwise proceed" | `agents/knowledge-architecture-studio/AGENT.md` | Decision Framework, step 1 (line 26) |
| "sounds knowledgeable and acts like a search engine" | `skills/knowledge-architecture-studio/genius.md` (pre-repair, unchanged by this pass) | Hidden Knowledge, "Cognitive Authenticity Beats Coverage" (line 48) |
| "Never present a domain as a flat list" | `skills/knowledge-architecture-studio/genius.md` (pre-repair, unchanged by this pass) | Genius Patterns, "Structure Knowledge Into Progressive Altitude" (line 14) |
| `source: "claude.ai project export (2026-07-01)"` | `skills/knowledge-architecture-studio/SKILL.md` | Frontmatter (line 7) |
| `refactored: "2026-07-13"` (used as the execution-prompt date anchor) | `references/prompts-v2/extract-knowledge-architecture.md`, `build-mastery-pathway.md`, `architect-domain-agent.md` | Frontmatter of all three files |

All line numbers above are from the pre-repair versions of the files as read during
this repair session (2026-07-18). Quotes reproduce the source wording exactly; where
the source used markdown bold (`**...**`) around part of the phrase, the bold markers
were dropped for inline quoting but no words were added, removed, or changed.
