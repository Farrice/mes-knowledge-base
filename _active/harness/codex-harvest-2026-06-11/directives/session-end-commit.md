# Session-End Commit Protocol

## Trigger
End of every session, or when the user says "commit", "wrap up", "end session", or similar.

## Steps

1. **Check for uncommitted work**
   - Run `git status --short | wc -l`
   - If 0 changes, skip to step 4

2. **Organize commits by logical grouping**
   - Don't dump everything into one commit
   - Group by: feature/content type, config changes, cleanup
   - Write clear commit messages (what + why, not just "update files")

3. **Offer push to GitHub**
   - Do not push unless the user explicitly approves
   - If the user approves and push fails (secrets, conflicts), report the blocker before retrying

4. **Session handoff note**
   - Write a brief note to `.agent/session-state.md` covering:
     - What was accomplished this session
     - What's in progress or next
     - Any decisions made that future sessions should know

## Commit Frequency During Sessions

- **After each completed task** — offer a commit checkpoint when useful
- **Before switching work types** — offer to separate brand work vs. offer work vs. extractions
- **When the user says "commit this"** or `/commit` — commit after checking status and secrets
- **At session end** — report status and offer a commit when there are meaningful changes

## Commit Message Format

```
type: short description

- Bullet points of what changed
- Keep it scannable

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

Types: `feat` (new content/features), `chore` (cleanup/maintenance), `fix` (corrections), `docs` (documentation)

## Safety Checks

- Never commit `.env`, `credentials.json`, or files with API keys
- Check `.gitignore` covers generated files (node_modules, dist, etc.)

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-11 |

**Update Rule**: When this protocol fires (status checked and commit/push decision handled), update the date and increment count.
- If `git status` shows 100+ changes, organize into multiple commits
- Commit is optional unless the user explicitly asks for it.
- Push always requires explicit user approval.
