# PROVENANCE — chase-hughes-conversational-influence repair (Wave 3 Lane 4 Batch 3)

Anchor → source file + location. All line numbers verified via `grep -n` / `sed -n` against
`extractions/chase-hughes/transcript.txt` (103,949 bytes / 1,287 lines, confirmed with `wc -c`
and `wc -l`) during this repair pass — not carried forward from unread prior claims.

| Anchor (as it appears in repaired files) | Source File | Location | Verified This Pass |
|---|---|---|---|
| "Anything that comes from within our own mind, we cannot resist" | `extractions/chase-hughes/transcript.txt` | line 188 | Yes — verbatim match |
| "I bet those things snap together like two little Legos" | `extractions/chase-hughes/transcript.txt` | line 186 | Yes — verbatim match |
| "A local Austin woman found missing today...arguing with her boyfriend...details after the break" | `extractions/chase-hughes/transcript.txt` | lines 190-191 | Yes — verbatim match |
| "The only two things I've ever told my kids should terrify them" + secret-keeping line | `extractions/chase-hughes/transcript.txt` | lines 196-198 | Yes — verbatim match |
| Bumper-sticker/Subaru/marathon/Ron Jon Surf Shop empathy drill | `extractions/chase-hughes/transcript.txt` | lines 113, 120, 135-143 | Yes — verbatim match |
| Daughter's age ("about 9 years old") | `extractions/chase-hughes/transcript.txt` | line 112 | Yes — verbatim match |
| "I don't have to mention David and Goliath" / DMV lines / walk down the hill | `extractions/chase-hughes/transcript.txt` | lines 390-396 | Yes — verbatim match |
| "I I never I never ever ever talk about how the story ends because your brain already knows" | `extractions/chase-hughes/transcript.txt` | line 398 | Yes — verbatim match |
| "it's never going to be in the school hallway...not going to be over a a a brunch" | `extractions/chase-hughes/transcript.txt` | lines 416-417 | Yes — verbatim match |
| "we are deeply internally craving a Steven Spielberg ending" / "We don't get the Spielberg ending" | `extractions/chase-hughes/transcript.txt` | lines 421, 430 | Yes — verbatim match |
| Anti-Exemplar (direct-argumentation paragraph) | `skills/chase-hughes-conversational-influence/genius.md` (pre-existing) | "Anti-Exemplar — The Direct Argumentation Approach" section | Pre-existing content, additive-preserved; cross-referenced against transcript.txt:391-398 for consistency |
| "Theater Reflex," "Special vs Important," psychedelic-seizure healing claims | `skills/chase-hughes-conversational-influence/genius.md` (pre-existing, "Hidden Knowledge" section) | Not re-located verbatim in transcript.txt during this pass | No — labeled UNCONFIRMED in `references/source-ledger.md`, left in place (additive-first boundary; not deleted) |
| Out-of-scope file check | `extractions/chase-hughes/transcript-modernwisdom-behaviorsuite.txt` | whole file | Confirmed 125,792 bytes via `wc -c` (non-empty, single-line export, 0 via `wc -l`) — read but NOT used as a source for this skill; belongs to sibling skill `chase-hughes-context-engineering`, out of batch scope |

## Method

1. `ls extractions/ | grep -i hughes` → confirmed `extractions/chase-hughes/` is the ground-truth source tree.
2. `find extractions/chase-hughes -type f -exec wc -c {} \;` → recorded every file's byte size before making any absence/presence claim (per envelope rule 2).
3. For every new quote used in `genius.md` (Anti-Patterns section, How to Use This Skill section) and every workflow Quality Gate, ran `grep -n "<exact phrase>" extractions/chase-hughes/transcript.txt` and cross-checked the surrounding lines with `sed -n` before citing a line number.
4. Corrected two line-number citations mid-repair after a first-pass grep mix-up (Austin-woman quote initially mis-cited at 139-141, corrected to 190-191; "never talk about how the story ends" initially mis-cited at 399-400, corrected to 398) — both fixed in the final files before delivery.
5. Two pre-existing genius.md claims could not be re-located verbatim in the available transcript within this pass's scope; rather than delete (additive-first) or silently leave unlabeled, they are named and downgraded to UNCONFIRMED in `references/source-ledger.md`.
