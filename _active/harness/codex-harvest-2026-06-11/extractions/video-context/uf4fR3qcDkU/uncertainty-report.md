# Uncertainty Report

## Evidence Counts
- `inferred_context`: 0
- `observed_onscreen_text`: 0
- `observed_spoken`: 3988
- `observed_visual`: 0
- `uncertain_or_unavailable`: 3

## Limitations
- yt-dlp metadata fetch failed: WARNING: [youtube] HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known). Retrying (1/3)...
WARNING: [youtube] HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known). Retrying (2/3)...
WARNING: [youtube] HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known). Retrying (3/3)...
WARNING: [youtube] Unable to download webpage: HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known) (caused by TransportError("HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known)")). Giving up after 3 retries
WARNING: [youtube] HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known). Retrying (1/3)...
WARNING: [youtube] HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known). Retrying (2/3)...
WARNING: [youtube] HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known). Retrying (3/3)...
ERROR: [youtube] uf4fR3qcDkU: Unable to download API page: HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known) (caused by TransportError("HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known)"))
- Frame extraction skipped because mode is transcript.
- OCR skipped because mode is transcript.

## Evidence Rule
Inferred context must not be merged into observed rows. Visual claims require a frame, OCR result, human note, or vision adapter output.
