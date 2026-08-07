# Andrea DJ Project — Organizational Schema
## How files are organized, dated, and shipped

---

## Google Drive Structure

```
Google Drive/
└── Andrea DJ — Client Work/
    ├── 📁 Packages/                    ← Shipped deliverables (dated)
    │   ├── 📁 2026-04-11 — Monday Package v1/
    │   │   ├── 00-READ-FIRST.docx
    │   │   ├── 01-brand-identity.docx
    │   │   ├── 02-pulse-who.docx
    │   │   ├── 03-launch-60-days.docx
    │   │   ├── 04-content-week-1.docx
    │   │   ├── 05-substack-merge.docx
    │   │   ├── 06-monday-agenda.docx
    │   │   ├── 07-claude-pro-setup.docx
    │   │   └── 08-naming-sprint.docx
    │   └── 📁 [YYYY-MM-DD] — [Package Name]/
    │       └── ...
    │
    ├── 📁 Research/                    ← Original research (from Phase 1)
    │   ├── 00-START-HERE.docx
    │   ├── 01-market-research.docx
    │   ├── 02-brand-naming.docx
    │   ├── 03-event-blueprint.docx
    │   ├── 04-instagram-strategy.docx
    │   └── 05-venue-and-pricing.docx
    │
    ├── 📁 Weekly/                      ← Per-call deliverables
    │   ├── 📁 Week 01 — 2026-04-14/
    │   ├── 📁 Week 02 — 2026-04-21/
    │   └── ...
    │
    ├── 📁 Assets/                      ← Brand assets, templates, images
    │   ├── Brand Guidelines (when created)
    │   ├── IG Templates
    │   └── Venue Pitch Materials
    │
    └── 📁 Notes/                       ← Call recordings, transcripts, Andrea's comments
        ├── 2026-04-07 — Call Transcript.docx
        └── ...
```

## Local File Structure (Farrice's system)

```
_active/clients/andrea-dj/
├── README.md                           ← Project overview (always current)
├── PROJECT-SCHEMA.md                   ← This file
├── research/                           ← Original Phase 1 research (markdown source)
├── deliverables/
│   ├── 2026-04-11-monday-package/      ← Dated package (markdown source)
│   │   ├── *.md                        ← Source files
│   │   └── docx/                       ← Converted .docx (auto-generated)
│   └── [YYYY-MM-DD]-[slug]/           ← Future packages
├── weekly/                             ← Per-call prep and checklists
│   ├── week-01-2026-04-14.md
│   └── ...
├── notes/                              ← Call notes, Andrea's feedback
└── assets/                             ← Brand files, templates
```

## Naming Conventions

| Type | Format | Example |
|------|--------|---------|
| Package folder | `YYYY-MM-DD-[slug]` | `2026-04-11-monday-package` |
| Weekly folder | `week-NN-YYYY-MM-DD` | `week-01-2026-04-14` |
| Deliverable files | `NN-[descriptive-slug].md` | `01-pulse-brand.md` |
| Drive folder | `YYYY-MM-DD — [Human Name]` | `2026-04-11 — Monday Package v1` |
| Call transcripts | `YYYY-MM-DD — Call Transcript` | `2026-04-07 — Call Transcript` |

## Conversion Workflow

**Local (Farrice) → Google Drive (Andrea):**

```bash
# 1. Write/edit markdown files locally
# 2. Convert to .docx (one command)
python execution/md_to_docx.py _active/clients/andrea-dj/deliverables/[package]/

# 3. Re-auth Drive if needed
gws auth login -s drive,gmail,calendar,sheets,docs

# 4. Upload to Drive (manual drag-drop or gws CLI)
# Files go to: Andrea DJ — Client Work/Packages/[dated folder]/
```

**Page breaks are automatic:**
- `---` (horizontal rule) → page break
- `## Heading 2` → page break before each H2
- This means each major section of a document starts on a fresh page

**Andrea's workflow:**
1. Open Google Drive → Andrea DJ — Client Work → Packages → latest folder
2. Open .docx file → Google Docs auto-converts on open
3. Comment in the margins
4. Farrice reviews comments before next call

## Versioning Rules

- **Never overwrite a shipped package.** Create a new dated folder if revisions are substantial.
- **Minor edits** (typo fixes, sentence tweaks) can be applied in-place with a note in the folder name: `2026-04-11 — Monday Package v1.1`
- **Major revisions** (name change, structural rework) get a new package: `2026-04-14 — Monday Package v2`
- **Markdown is the source of truth.** .docx files are generated output. Edit markdown, reconvert, re-upload.
