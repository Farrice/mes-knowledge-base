# Thought-Bank — Operating Manual

This is Farrice's **personal ideation + voice bank**. Raw thoughts, observations, POV-anchors, and hooks land here as they arrive — then feed downstream content workflows (Parallax, daily-flywheel, voice-first-content, ghostwrite) with authentic, voice-true raw material instead of generic AI angles.

The whole point: content that comes faster, more authentically, more uniquely, and truer to me — because the seeds were mine.

---

## How it works

### Capture (no slash command needed)

Just dump your thought anywhere in conversation with Claude. Voice-to-text, paragraphs, fragments, tangents — whatever. Claude will:

1. Append the raw dump verbatim to `inbox/YYYY-MM-DD.md` (timestamped, never overwritten)
2. Auto-route it to one or more `themes/` files (Claude reads the dump, decides which theme(s) it belongs to — or creates a new one if it doesn't fit existing themes)
3. Extract any obvious **hooks** to `hooks-bank.md`
4. Extract any obvious **POV anchors** (reframes, voice rules) to `pov-anchors.md`
5. Update `INDEX.md` with the new last-captured timestamp

**Voice preservation rule**: The verbatim dump in `inbox/` keeps Farrice's exact words. Theme files can paraphrase + cross-link, but the inbox is the source of truth.

### Process (when you want to make content)

When a theme has reached signal-density (3+ entries, or one strong-enough single entry), route to a content workflow:

| Theme signal | Best workflow | Output |
|---|---|---|
| Personal story + emotional weight | `daily-flywheel` | 3 LinkedIn variants |
| Single crystallized insight | `parallax --quick` or `insight-elaborate` | 800-1200w Substack edition / 8-beat elaboration |
| Voice/POV reframe with stakes | `voice-first-content` | Psychology-first LinkedIn post |
| Multi-chapter narrative arc forming | `serial-arc` | 5-7 chapter series plan |
| Hook-only (no full thought yet) | `vicious-hook` or save for later | Hook bank entry |
| Cultural moment + your POV intersect | `jackpost` | Borrowed-attention post |

Workflows pull source material from `inbox/<date>.md` (verbatim voice), `themes/<name>.md` (cross-cuts and recurring patterns), and `pov-anchors.md` (voice rules to enforce).

### Optional: Notion mirror

For mobile-searchable indexing, mirror an entry to the Notion Captures DB:

```bash
python3 execution/notion_api.py capture "<title>" "<body>" --type Idea --tags <theme>
```

Not auto-fired. Use when you want a thought searchable from your phone.

---

## Folder map

```
thought-bank/
├── README.md           # This file
├── INDEX.md            # Living dashboard — themes, hook count, last-captured
├── inbox/              # Date-stamped raw dumps (append-only, voice-preserved)
├── themes/             # Categorized cross-cuts mapped to FARRICE.md interest stack
├── hooks-bank.md       # One-line content hooks (specific, deployable)
└── pov-anchors.md      # Voice/POV reframes (general, identity-level)
```

**Themes are mapped to FARRICE.md interest stack** — same vocabulary as the rest of brand work, no parallel taxonomy. New themes can emerge organically; just create a new file in `themes/` and add it to INDEX.md.

---

## What this is NOT

- **Not a journal** — no daily-required entry, no "morning pages." Capture only when there's signal.
- **Not a deliverable** — no chain finalize, no quality gate. Raw material doesn't get scored.
- **Not a content draft folder** — drafts live in `_active/farrice-brand/content/`. The thought-bank is upstream.
- **Not a Notion replacement** — the local files are the source of truth. Notion is an optional mirror for mobile.

---

## When this pays off

You walk into a content session and you're not staring at a blank page asking "what should I write about?" — you open INDEX.md, scan the theme files, find the entry that has the most heat, and the workflow does the rest. The voice is already yours because you put it there.
