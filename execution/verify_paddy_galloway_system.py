#!/usr/bin/env python3
"""Read-only source/command integrity checks; not an expert-quality or model-accuracy verdict."""
import json
import sys
from pathlib import Path
from renaissance_audit import audit_file
ROOT=Path(__file__).resolve().parents[1]
S='skills/paddy-galloway-youtube-strategy'
E='extractions/paddy-galloway/youtube-masterclass'

def verify(root=ROOT, hidden=frozenset()):
    failures=[]
    def exists(rel): return rel not in hidden and (root/rel).is_file()
    def read(rel): return (root/rel).read_text() if exists(rel) else ''
    workflows=sorted((root/S/'workflows').glob('*.md'))
    if len(workflows)!=14: failures.append('workflow count')
    for w in workflows:
        slug=w.stem; rel=str(w.relative_to(root)); p=f'{S}/references/prompts-v2/{slug}.md'
        for target in [rel,p,f'.agent/workflows/{slug}.md',f'.claude/commands/{slug}.md']:
            if not exists(target): failures.append('missing '+target)
        if rel not in read(f'.agent/workflows/{slug}.md'): failures.append('unreachable '+slug)
        if f'.agent/workflows/{slug}.md' not in read(f'.claude/commands/{slug}.md'): failures.append('Claude bridge '+slug)
        if f'.agent/workflows/{slug}.md' not in read(f'.agents/skills/{slug}/SKILL.md'): failures.append('Codex direct entry '+slug)
        if exists(p) and audit_file(root/p): failures.append('prompt contract '+slug)
    if 'agents/paddy-galloway/AGENT.md' not in read('.agents/skills/paddy-galloway/SKILL.md'): failures.append('Paddy named entry')
    if 'primary_workflow: pg-creative-sprint' not in read(f'{S}/SKILL.md'): failures.append('full sprint default')
    for rel in ['.agent/workflows/paddy-galloway.md','.claude/commands/paddy-galloway.md']:
        if f'{S}/workflows/pg-creative-sprint.md' not in read(rel): failures.append('wrong flagship '+rel)
    handoff=read('skills/youtube-video-context-analysis/references/content-analyst-pilot.md')
    if f'{S}/SKILL.md' not in handoff: failures.append('missing conditional analyst handoff')
    if not (root/'.agents/skills/paddy-galloway-youtube-strategy').resolve().samefile(root/S): failures.append('Codex skill link')
    seg=json.loads(read(f'{E}/transcript_segments.json'))
    if seg[0]['start_seconds']>1 or seg[-1]['end_seconds']<9907: failures.append('full source endpoints')
    if len(list((root/E).glob('chapter-*.txt')))!=24: failures.append('chapter coverage')
    recovery=json.loads(read(f'{E}/gemini-recovery-receipt.json'))
    if recovery['paid_attempts']!=1 or recovery['provider_status']!='completed': failures.append('live receipt')
    if recovery['agentic']!='NOT_RUN' or recovery['invoice_status']!='NOT_VERIFIED': failures.append('false proof promotion')
    return failures

def main():
    live=verify()
    broken_command=verify(hidden=frozenset({'.agent/workflows/pg-title-lab.md'}))
    broken_handoff=verify(hidden=frozenset({'skills/youtube-video-context-analysis/references/content-analyst-pilot.md'}))
    result={'structural_checks':'PASS' if not live else 'FAIL','failures':live,
            'negative_control_missing_command':any('pg-title-lab' in x for x in broken_command),
            'negative_control_missing_handoff':'missing conditional analyst handoff' in broken_handoff,
            'restored_original_passes':not verify(),
            'behavioral_demonstration':E+'/applied-production-packet.md',
            'demonstration_judge':'main agent; not independent/human blind pass',
            'video_precision_quality':'FAIL; see gemini-quality-review.md'}
    print(json.dumps(result,indent=2))
    return int(bool(live) or not result['negative_control_missing_command'] or not result['negative_control_missing_handoff'])
if __name__=='__main__':sys.exit(main())
