# PROVENANCE — phil-m-jones-conversational-influence repair

Anchor → source file + location. Full claim-by-claim table (with VERIFIED/LIKELY/UNCONFIRMED labels) lives in `references/source-ledger.md`; this file is the compact anchor index for the adversarial verifier.

**Ground-truth source**: `_active/codex-harvest-2026-06-11/extractions/phil-m-jones/transcript.txt` (112,045 chars / ~20,448 words). Confirmed present and readable by direct read on 2026-07-18. This is a different, correct path from the one recorded in the skill's pre-existing `references/source-notes.md` (`extractions/phil-m-jones/transcript.txt`, which does not exist — see the Path Correction note appended to that file).

Companion: `_active/codex-harvest-2026-06-11/extractions/phil-m-jones/extraction-report.md` (3,401 bytes) — original extraction summary.

| Anchor (as used in genius.md) | Word position in transcript.txt | Verified |
|---|---|---|
| "I'm not sure if it's for you, but" | ~1,506 | Yes — `str.find` exact match |
| "How open-minded would you be" | ~1,775 | Yes |
| "What do you know" | ~25 | Yes |
| "How would you feel if" | ~29 | Yes |
| "Just imagine" | ~3,786 | Yes |
| "When would be a good time?" | ~4,538 | Yes |
| "I'm guessing you haven't got around to" | ~5,142 | Yes |
| "the psychology behind this technique, which involves turning an open questioning into a closed one, results in you receiving a guaranteed outcome or answer" | ~5,900 | Yes |
| "As I see it," you have three options | ~7,020 | Yes |
| "there are two types of people in this world" | ~8,110 | Yes |
| "I bet you're a bit like me." | ~8,341 | Yes |
| "If I can, will you?" | ~14,603 | Yes |
| "Just one more thing." | ~16,673 | Yes |
| "just out of curiosity" | ~19,106 | Yes |
| "the primary job description of all sales professionals is to be decision catalysts in the lives of their customers and prospects" | ~7,949 | Yes |
| "It's a tool to do a job. It is a technique to help create an outcome." | ~10,110 | Yes |
| "So be careful of understanding the method behind the madness. the why behind the what." | ~10,116 | Yes |
| "I'm not saying that people should feel rushed into decisions." | ~19,138 | Yes |
| "One is pushy and the other is pulley." | ~1,547 | Yes |
| "I'm not sure if it's for you, but would you like to buy X?" | ~1,506 | Yes — already inside quote marks in source (Jones quoting himself) |
| "curiosity is the fuel to great conversation. And it's more than an idea. It's a principle. It's one of our four cornerstones." | ~13,686 | Yes |
| "People hate to feel manipulated and nearly always want to feel like they made the final decision." | ~6,977 | Yes |
| "To overcome an objection, you must first understand what an objection really is." | ~13,154 | Yes |
| "How open-minded is a is an open-ended question, whereas a would you be open-minded is a is a closed question." | ~1,927 | Yes — disfluency preserved verbatim |
| "without feeling forced, without feeling like you're doing something to somebody, without feeling like what you're doing is you're manipulating" | ~9,537 | Yes |
| "if one option is too prescriptive and two options feels right and wrong and too many options feels overwhelming" | ~7,557 | Yes |

## Method note

Every quote was located with Python `str.find` against the raw transcript text (a single-line, 112,045-character file with no internal newlines), then confirmed by printing ~250-500 characters of surrounding context to check the quote reads correctly in situ before use. Word positions are computed as `len(text[:idx].split())` — an approximation for citation readability, not a claim of exact line/word numbering (the file has no line breaks to number against). Nothing below was invented: every string in the table above is a verbatim substring of the transcript file, confirmed by direct read, not reconstructed from memory or training data.
