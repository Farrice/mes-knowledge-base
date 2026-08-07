# PROVENANCE — dakota-content-design repair

## Ground truth located (extractions/ was a false negative, not a true absence)

`extractions/` has zero Dakota entries (`ls extractions/ | grep -ic dakota` → 0;
recursive `grep -ril` across `extractions/` → 0 hits). But the envelope's rule
2 requires verifying absence, not asserting it — so before writing UNCONFIRMED
labels, the archived export was searched: `_active/harness/claude-export/harvest/census-full.json`
entry `{"expert": "Dakota", "count": 3, "ids": [...]}` names three conversation
IDs. Those IDs resolved inside `_archive/claude-export-2026-07-01.tar.gz` at
`claude-export/normalized/conversations/<id>.md` — raw Claude.ai sessions
where Dakota's own YouTube transcripts were pasted and MES-extracted. Extracted
and read in full (sizes below are `wc -c`, not estimates):

| File | Bytes | Video |
|---|---|---|
| `a718e600-4edb-4832-a55a-ebb02bc64932.md` | 63,508 | youtube.com/watch?v=kzu-QSaskK4, "everything I know about creating viral carousels in 29 minutes" |
| `141e8809-3391-4d56-8257-a753b1633182.md` | 55,234 | same video, re-run |
| `13b7362e-f27b-444d-a0a7-b51143f48786.md` | 62,862 | youtube.com/watch?v=N7iz-3UCJrY, "what I learned from 20 million views on Instagram in 90 days" |

Full claim-by-claim VERIFIED/LIKELY/UNCONFIRMED table: `references/source-ledger.md`.

## Anchor → source table (genius.md additions)

| Anchor in genius.md | Source location |
|---|---|
| "it kind of does this little test out on a few of your followers... which I think is just stupid" | `a718e600`, human turn, ~line 15-28 (transcript paste), "carousels reach your actual followers" paragraph |
| "flip the script and say how I, how I lost 10 pounds" | `a718e600`, same paragraph, hook-strategy tangent |
| "if it's like five things you should do and you're like tip number four do this, no one's really going to share just tip number four" | `a718e600`, same paragraph, revelational-vs-informative explanation |
| "I've had posts get a lot a lot a lot of views and do almost nothing for me" + "indicates something to us much different than views or likes" | `13b7362e`, human turn, opening third of transcript |
| "24,000 people who have unfollowed me, but that's a net growth of 8,000 followers... If you unfollow me, cool. Don't care" | `13b7362e`, human turn, ~two-thirds through transcript, 90-day readout section |
| Wendy's Diner rule / "stop making pancakes all together and go try to be a French restaurant" | `13b7362e`, human turn, Wendy's Diner analogy block |
| "I don't own the rights to the photos... no, I will not make prints" | `13b7362e`, human turn, closing production section |
| "would Dakota recognize this as..." recognition-test language | New — written for this repair, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per envelope instruction, calibrated to Dakota's own texture (spoken/self-deprecating quotes below it are from `a718e600`: "super hard math," "I'm not coherent enough to be doing math this quickly") |

All other genius.md content (Genius Patterns, Hidden Knowledge sections) was
pre-existing and untouched — those patterns trace to the same two transcripts
per the AI's own extraction summary inside `a718e600`/`13b7362e`, now made
auditable via the source-ledger rather than left as an asserted `source:`
frontmatter tag.

## Absence verified, not assumed

`skills/dakota-content-design/references/` had no ledger/source file before
this repair (`ls skills/dakota-content-design/references/` → `prompts-v2/`
only, confirmed by directory listing). `agents/dakota-thiefofboredom/memory/context.md`
(440 bytes) is explicitly a stub ("To be populated...") and contributed no
claims.
