# PROVENANCE — josh-sanders-linkedin-growth repair (Wave 3 Lane 4 Batch 7)

Anchor → source file + location, for every new claim/quote added in this
repair (genius.md's "How to Use This Skill" and "Anti-Patterns" sections).
Full claim-by-claim ledger for pre-existing content is in `source-ledger.md`.

| Anchor (as written in genius.md) | Source file | Location / verbatim match |
|---|---|---|
| "we'll never do paragraph blocks" | `extractions/josh-sanders/transcript.txt` | "We'll never do paragraph blocks. We want to make it so easy for people to read the content. We don't want to see a massive paragraph and I can't be bothered to read this and then scroll on." |
| "318,842" ugly-number example | `extractions/josh-sanders/transcript.txt` | "I've studied over 318,842 LinkedIn posts. That sounds like a weird amount of hosts... that genuinely that was the data set" |
| "other people can't share that" (over-personal content) | `extractions/josh-sanders/transcript.txt` | "that's where a lot of people go wrong. They go super personal things and it's like other people can't share that." |
| "a lot of where most entrepreneurs go wrong is they don't necessarily want to uh brag about it or talk about their achievements" | `extractions/josh-sanders/transcript.txt` | Same phrase, About-section discussion |
| "this is where most people go wrong. They will think about posting one kind of format... post that repeatedly and repeatedly" | `extractions/josh-sanders/transcript.txt` | Content-funnel discussion, immediately follows the "broader vs. conversion posts" exchange |
| "A lot of people actually don't even have a banner or it would just be like some generic one with their logo in the bottom corner" | `extractions/josh-sanders/transcript.txt` | Banner/profile-as-landing-page section |
| "a lot of the LinkedIn gurus were saying like um you shouldn't have uh links in your post. You shouldn't be going taking people off platform... we were like straight on it" | `extractions/josh-sanders/transcript.txt` | Format-arbitrage / link-shortener origin story |

Verification method: every quote above was located by direct Python
substring search over the raw transcript text (not `grep -n`, since the file
is a single unbroken line — `wc -l` = 0, `wc -c` = 104,542) during this
repair session. No quote in the new sections was taken from memory or
inferred; each was pulled from the actual returned substring, trimmed only
for leading/trailing whitespace.

Ingestion date (git-add date for the extraction files, used as the source
anchor date where a date is needed): 2026-03-02
(`git log --diff-filter=A --format="%ad %h %s" --date=short --
extractions/josh-sanders/transcript.txt`).
