#!/usr/bin/env python3
"""Read-only source and integration checks; never asserts market effectiveness."""
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'extractions/jason-fladlien/delivery-influence-2026-09-09'
S=ROOT/'skills/jason-fladlien-marketing'
checks=[]
def check(name,value):
 checks.append((name,bool(value)))
 print(('PASS' if value else 'FAIL')+' '+name)
segments=json.loads((P/'transcript_segments.json').read_text())
mechanics=json.loads((P/'mechanics.json').read_text())
check('caption timeline covers full source',len(segments)>500 and segments[0]['start']<10 and segments[-1]['start']>2270)
check('seventeen unique timestamped mechanics',len(mechanics)==17 and len({m['id'] for m in mechanics})==17)
for m in mechanics:
 check(m['id']+' has source within its range',any(m['start']<=s['start']<=m['end'] for s in segments))
check('18 reviewed frame objects',len(list((P/'frames').glob('*.jpg')))==18)
hashes=json.loads((P/'source-hashes.json').read_text())
check('preserved source hashes',all((P/n).exists() and hashlib.sha256((P/n).read_bytes()).hexdigest()==h for n,h in hashes.items()))
for mode in ['written','recorded','live','audit']:
 f=S/f'references/prompts-v2/delivery-{mode}.md'; text=f.read_text()
 check(mode+' full execution contract',all('## '+s in text for s in ['Role & Activation','Input Required','Execution Protocol','Output Contract','Output Skeleton','Quality Gate','Deploy When']))
 check(mode+' skill pointer',f'delivery-{mode}.md' in (S/'SKILL.md').read_text())
for path in ['.agent/workflows/fladlien-delivery.md','.agents/skills/source-command-fladlien-delivery/SKILL.md','.claude/commands/fladlien-delivery.md']:
 check(path,(ROOT/path).is_file())
check('slash index entry','`/fladlien-delivery`' in (ROOT/'SLASH_COMMANDS.md').read_text())
for name in ['spoken-copy-live-close-architecture','point-architecture-engine','conversational-persuasion-copy-engine']:
 check(name+' handoff','workflows/delivery-influence.md' in (S/f'workflows/{name}.md').read_text())
proof=(P/'proof-lab.md').read_text()
check('proof keeps real-world uncertainty','UNTESTED' in proof and 'NOT_RUN' in proof and 'hypothetical' in proof)
check('source separates observation and inference','SOURCE-REPORTED' in (P/'uncertainty-report.md').read_text() and 'INFERRED' in (P/'uncertainty-report.md').read_text())
print(f'{sum(v for _,v in checks)}/{len(checks)} structural/source checks passed. Applied proof is editorial; market effect and independent replay remain untested.')
sys.exit(0 if all(v for _,v in checks) else 1)
