# Transcription Receipt — kY-t009NMWU

- Approval: user-approved ceiling of `$0.82`.
- Pricing basis: 136.5 minutes at the [published Whisper rate](https://developers.openai.com/api/docs/models/whisper-1) of `$0.006/minute` (estimated `$0.819`).
- Source audio: local extraction from the 2:16:30 video.
- Provider/model: OpenAI `whisper-1` through the `/watch` skill.
- Chunking: three chunks because the extracted audio exceeded 24 MB.
- Result: `PASS` — 2,088 timestamped segments.
- First attempt: `NO UPLOAD / NO RESULT` due local TLS certificate verification failure.
- Retry: `PASS` after explicitly selecting the installed certificate bundle.
- Persistence limitation: the current `/watch` script printed the full transcript to the runtime report but did not save a transcript file. The source ledger therefore retains only bounded timestamped excerpts used by the system; unlocated case figures remain user-supplied/source-reported.
