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

3. **Push to GitHub**
   - Run `git push` after committing
   - If push fails (secrets, conflicts), resolve before ending session

4. **Session handoff note**
   - Write a brief note to `.agent/session-state.md` covering:
     - What was accomplished this session
     - What's in progress or next
     - Any decisions made that future sessions should know

## Commit Frequency During Sessions

- **After each completed task** — don't let work pile up
- **Before switching work types** — brand work vs. offer work vs. extractions
- **When the user says "commit this"** or `/commit`
- **Always at session end** — no exceptions

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
- If `git status` shows 100+ changes, organize into multiple commits
