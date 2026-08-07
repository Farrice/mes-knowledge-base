# Hybrid Path Validation Pack Export Trace

Date: 2026-05-09

Method: local `gws` workflow through `execution/md_to_gdoc.py`.

Google Drive plugin used: no.

## Result

Drive folder:

https://drive.google.com/drive/folders/1NJiVfHi865CDonLbTw46z7MVns-VUrFO

Uploaded:

- 11 native Google Docs
- 1 native Google Sheet

## Verification

- Local artifact metadata guard checked: no visible `IsArtifact` or `Artifact type` frontmatter found.
- Local HTML preview conversion completed for all 11 Markdown docs.
- Initial upload created the Drive folder but failed because temp files were outside the accepted upload path.
- Rerun succeeded by forcing temp files into `.tmp/gdoc-upload`.
- Folder listing verified through local `gws`.
- One Google Doc body verified through local `gws`.
- Google Sheet metadata and values verified through local `gws`.

## Local Source

Local staging folder:

`/Users/farricecain/Codex Antigravity/brain/hybrid-path-validation-pack-v1`

Mirror record:

`DRIVE-MIRROR.json`
