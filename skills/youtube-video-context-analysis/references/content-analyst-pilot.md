# Content analyst: on-demand pilot

Use when Farrice asks for his content analyst, batch teardowns, extracting lessons,
learning his taste, finding promising content or adapting successful techniques.
This is an opt-in extension of the existing video evidence workflow. Codex and
Claude Code read the same file. No extra agent, automation or paid model is started.

## Current capability and boundary

The local budget/state controls work against a simulator. `run` rejects live
execution. Do not call Gemini directly to get around that rejection, treat a
simulation approval as money permission, or assume the generic Gemini quota
entry covers video API usage. Report real video quality as UNTESTED.

The analyst can work NOW from existing evidence packages, supplied screenshots,
transcripts, public metrics already retrieved with authorized tools and explicit
taste verdicts. Use the native model for interpretation; new video perception
requires the future approved trial. Do not call generated fixture text evidence.

## Start with the user's job

Choose one mode, infer it when clear, and preserve the user's own goal:

| Mode | Job | Useful result |
|---|---|---|
| Discover | Find promising examples to study | Ranked shortlist with comparable performance evidence, relevance and uncertainty |
| Taste | Understand what Farrice likes | Specific choices linked to his explicit verdicts; tentative hypotheses kept separate |
| Extract | Learn without hours of passive viewing | Timestamped mechanism, example, decision rule and a small application exercise |
| Adapt | Make something original using useful techniques | One original concept and execution outline grounded in a reference's mechanism |

A mode changes the question, not the spending authority. No unattended discovery.
If discovery needs source search, choose a bounded pool/topic/time window and
use existing read-only tools. Never call a promising example a validated winner
when views, post age and a suitable comparison baseline are missing. Public view
counts do not establish retention, conversions or causal impact. Owned-account
analytics require verified connector access; an installed skill isn't access.

## Source intake and economical routing

1. Reuse an existing source package before fetching again. Cache key includes
   source identity/version, goal, model, processing and prompt version. Reusing
   an upload alone does not eliminate inference charges.
2. YouTube URL: documented direct API route is for public videos; accessibility
   is NOT_CHECKED until fetched. Local video: hash bytes and inspect media before
   any future upload. Never upload unrelated files.
3. TikTok/Instagram/LinkedIn or another page: retrieve accessible content with
   existing tools only inside authorized scope. If inaccessible, report it and
   work from a supplied file; no login bypass, guessed transcript or universal
   URL claim. Articles, images and carousels use their native readers.
4. A speech-led lesson generally needs captions first. A demo, edit or visual
   technique needs video evidence. Use focused local frames to verify tiny text
   or exact cut boundaries. Do not pay to deeply inspect every shortlisted item.
5. Preview exact batch, proposed model, known limits, output size and estimated
   cost. The pilot supports offline planning for videos only. Do not invent a
   price for a missing duration, unsupported model or unbounded agentic run.

## Spend and failure contract

Paid allowance is currently $0. The user confirmed the OFFLINE pilot, not a paid
trial. No hidden retries, fallback model, automatic batch expansion or cron job.

Simulation approval must cite the exact batch hash, decision text, simulated
budget and expiry. It is a local record, not cryptographic proof of human consent.
The main assistant must obtain explicit user authorization before recording any
future paid approval. Approval of one batch never authorizes the next.

Reservations are committed before dispatch and shared across workspace lanes via
one SQLite store. Failed/missing usage and interruptions preserve liability. The
first uncertain call stops the batch. Inspect status; do not delete the ledger,
reapprove a stopped batch, change identifiers to force a retry or clear unknown
charges without independent evidence and a new recovery decision.

## Analysis and evidence

Execution prompt: `skills/youtube-video-context-analysis/references/prompts-v2/content-analyst.md`.
Load only the source material relevant to the chosen mode. Preserve the existing
creative-reference five evidence lanes and multi-video review-parity rule.
For extraction, hand off source passages and timestamps to the existing
source-to-skill workflow; a Gemini summary is not the transcript or source canon.
Taste notes enter the working artifact; persistent personal memory changes still
require Farrice's explicit memory instruction. Never infer a global taste rule
from one liked post. Avoid copying another creator's wording or visual identity.

## Live activation remains a separate milestone

Before any paid pilot: establish billing entitlement and current pricing; verify
actual API fields, model limits, thinking/tool usage accounting and stopping
semantics; implement a single approved transport with no implicit retries; bind
approval to the source, question and maximum liability. If agentic costs cannot
be bounded defensibly, do not enable it under a claimed hard dollar cap.
First trial: a separately approved public video, visual facts absent from
captions, locally checked timestamps, actual usage receipt and native agentic
processing records. No quality or cost-savings claim until that test exists.

Operator commands and controls: `docs/content-analysis-pilot/README.md`.
