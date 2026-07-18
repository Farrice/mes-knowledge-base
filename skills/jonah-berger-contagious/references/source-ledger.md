# Source Ledger — jonah-berger-contagious

Compiled during Wave 3 Lane 4 repair pass (2026-07-18). Every claim in
`SKILL.md`/`genius.md` labeled VERIFIED / LIKELY / UNCONFIRMED. This skill
ships with **no primary transcript file anywhere in this repo** — the search
below was run by content, not filename, before writing that conclusion down
(per the batch's hard rule against false "unrecoverable" claims).

## Search record (file reads + sizes, not assumption)

| Location checked | Method | Result |
|---|---|---|
| `extractions/` | `ls extractions/ \| grep -i berger` | 0 matches — no berger/jonah/contagious file exists |
| `agents/jonah-berger/` | Read `AGENT.md`, `memory/context.md` | Persona + activation card only, no source transcript, no verbatim quotes beyond what's already in genius.md |
| `_active/codex-harvest-2026-06-11/` | `find ... -iname "*berger*"` | 0 matches |
| `_archive/claude-export-2026-07-01.tar.gz` | File exists, 332,779,255 bytes, 3,864 entries (`tar tzf` count). `tar tzf ... \| grep -i jonah`, `grep -i berger`, `grep -i contagio` | 0 matches on all three terms — the export this skill's frontmatter cites (`source: claude.ai export 2026-07-01`) does not contain a Jonah Berger file |
| Repo-wide grep | `grep -rl "STEPPS\|Trojan-horse\|REDUCE.*Reactance\|Valuetainment"` across `.md/.txt/.json`, excluding the skill itself and worktree mirrors | Only hits: `SLASH_COMMANDS.md`, `.claude/commands/jonah-berger-contagious.md`, `agents/_framework/invocation-cards.md`, `agents/jonah-berger/AGENT.md`, `.agent/prompt-index.json`, `agents/jonah-berger/memory/context.md` — all downstream references to this skill, not an independent primary source |

**Conclusion**: the skill's own frontmatter provenance claim ("claude.ai export
2026-07-01") and genius.md's header claim ("Valuetainment interview...
transcript fully read") cannot be verified against any file in this
repository. Neither claim is retracted here (an original author may have
worked from a transcript that was never checked into this repo), but neither
is treated as VERIFIED. Content quality is assessed instead against
independently checkable public facts about Berger's published work.

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| Jonah Berger is a Wharton marketing professor, PhD Stanford GSB | VERIFIED | Well-established public biographical fact, independently checkable, not dependent on the missing transcript |
| *Contagious: Why Things Catch On* published 2013 | VERIFIED | Public, independently checkable bibliographic fact |
| *The Catalyst: How to Change Anyone's Mind* published 2020 | VERIFIED | Public, independently checkable bibliographic fact |
| STEPPS = Social currency, Triggers, Emotion, Public, Practical value, Stories | LIKELY | Matches the well-documented public framework from *Contagious*; no in-repo primary transcript to confirm this skill's specific phrasing is verbatim Berger |
| REDUCE = Reactance, Endowment, Distance, Uncertainty, Corroborating evidence | LIKELY | Matches the well-documented public framework from *The Catalyst*; same caveat |
| Specific interview source: "Valuetainment, 'How Marketers Create Billion Dollar Trends'" | UNCONFIRMED | No transcript file located anywhere searched (see table above); cannot confirm this specific interview is the origin of the quoted lines |
| "source: claude.ai export 2026-07-01" (SKILL.md frontmatter) | UNCONFIRMED | The cited export tarball was opened and searched by content; zero matches for jonah/berger/contagio |
| Blendtec "Will It Blend?" video example (single-kernel demonstration) | LIKELY | Blendtec's viral campaign is well-documented public case history; framing/attribution to this specific interview is UNCONFIRMED |
| Freemium examples: Dropbox, Pandora, Zappos free shipping/returns | LIKELY | Publicly documented business practices; specific Berger commentary on them is UNCONFIRMED without the transcript |
| Obama (hope/inspiration) vs. Trump (anger/anxiety) emotional-valence contrast | LIKELY | Consistent with publicly discussed political-messaging analysis; verbatim attribution UNCONFIRMED |
| Individual verbatim-styled lines inside genius.md ("that's interesting, but who needs it?", "why hasn't this person changed already?", "that's just you", "which do I prefer?") | UNCONFIRMED as verbatim Berger quotes | No primary transcript to check word-for-word; treated in genius.md as illustrative paraphrase of his known argument style, not confirmed verbatim |
| Workflow content (`workflows/01-03`) — STEPPS audit / REDUCE diagnosis / kernel-story structure | LIKELY | Operationalizes the same LIKELY-labeled framework claims above; no independent verification beyond internal consistency |

## What this means for downstream use

Treat this skill as a well-constructed, framework-accurate operationalization
of Berger's real, public work — not as a verbatim transcript extraction.
Anyone who locates the actual source interview/transcript should replace the
LIKELY/UNCONFIRMED labels above with VERIFIED once quotes are checked
word-for-word, and update `SKILL.md` frontmatter accordingly.
