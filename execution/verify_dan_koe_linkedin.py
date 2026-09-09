#!/usr/bin/env python3
"""Source-specific verification, separate from human taste and market outcomes."""
import hashlib
import json
from pathlib import Path
import re
import sys
import renaissance_audit
from watch_free import coverage
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'extractions/video-context/MqjmPknAvuw'
SKILL=ROOT/'skills/dan-koe-multipassionate-mastery'

def verify():
    meta=json.loads((SOURCE/'metadata.json').read_text())
    assert meta['id']=='MqjmPknAvuw', 'wrong source'
    capture=json.loads((SOURCE/'acquisition.json').read_text())
    assert capture['paid_api_calls']==0
    assert capture['status']=='CAPTURED_REVIEW_REQUIRED', 'capture is not human review'
    segments=json.loads((SOURCE/'transcript_segments.json').read_text())
    assert segments and coverage(segments,capture['duration_seconds'])['timeline_fraction']>.98
    review=json.loads((SOURCE/'frame-review.json').read_text())
    assert len(review['uniform_frames'])==40 and review['scene_frames_reviewed']==14
    assert all(f['reviewed'] and f['observation'] and (SOURCE/f['path']).is_file() for f in review['uniform_frames'])
    assert len(list((SOURCE/'scene-frames').glob('*.jpg')))==14
    if (SOURCE/'raw/video.mp4').exists():
        assert hashlib.sha256((SOURCE/'raw/video.mp4').read_bytes()).hexdigest()==capture['media_sha256']
    else:
        print('NOTE: full raw media not locally retained; existing source hash cannot be rechecked')
    files=list(SKILL.glob('workflows/linkedin-*.md'))+list(SKILL.glob('references/prompts-v2/linkedin-*.md'))+[SKILL/'references/linkedin-source-method.md']+list(SOURCE.glob('*.md'))
    for f in files:
        text=f.read_text()
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in link or link.startswith('#'): continue
            assert (f.parent/link.split('#')[0]).exists(),f'broken link: {f}: {link}'
    prompts=list(SKILL.glob('references/prompts-v2/linkedin-*.md'))
    assert len(prompts)==3
    for p in prompts: assert not renaissance_audit.audit_file(str(p)),p
    assert 'workflows: 9' in (SKILL/'SKILL.md').read_text()
    for suffix in ['reference-lab','image-caption-studio','distribution-experiment']:
        assert f'linkedin-{suffix}.md' in (SKILL/'SKILL.md').read_text()
    for path in ['.agent/workflows/dan-koe-linkedin-system.md','.claude/commands/dan-koe-linkedin-system.md','.agents/cold-skills/source-command-wrappers/source-command-dan-koe-linkedin-system/SKILL.md']:
        assert (ROOT/path).is_file(),path
    assert '/dan-koe-linkedin-system' in (ROOT/'SLASH_COMMANDS.md').read_text()
    print(f'PASS: source identity/coverage, 54 reviewed frames, {len(files)} linked documents, 3 v2 prompts, 3 bridge layers')
    print('NOT TESTED: independent cold-start, human blind preference, live LinkedIn growth or revenue')

if __name__=='__main__':
    try: verify()
    except (AssertionError,ValueError,OSError) as exc:
        print(f'FAIL: {exc}',file=sys.stderr);sys.exit(1)
