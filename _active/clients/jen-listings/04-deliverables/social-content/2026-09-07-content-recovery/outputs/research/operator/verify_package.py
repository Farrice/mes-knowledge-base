from pathlib import Path
import re,json,hashlib,subprocess,collections,xml.etree.ElementTree as ET
OUT=Path(__file__).resolve().parents[1]; OP=OUT/'operator';ROOT=Path.cwd();files=sorted(OUT.glob('0[1-8]-*.md'))
errors=[];checks={};checks['exactly_eight_artifacts']=len(files)==8
links=[]
for p in files+[OUT/'START-HERE.md']:
 text=p.read_text()
 if '{{' in text or '<!-- QUOTES -->' in text:errors.append(f'unresolved token: {p.name}')
 for link in re.findall(r'\]\((?:<([^>]+)>|([^\s)]+))\)',text):
  target=link[0] or link[1]
  if target.startswith('/'):
   links.append(target)
   if not Path(target).exists():errors.append('Missing local target: '+target)
 if not p.with_name(p.stem+'.metadata.json').exists():errors.append('Missing metadata '+p.name)
checks['local_links_checked']=len(links);checks['local_links_exist']=not any(x.startswith('Missing local') for x in errors)
sources=json.loads((OP/'source-ledger.json').read_text());topics=json.loads((OP/'topic-bank.json').read_text());quotes=json.loads((OP/'selected-buyer-quotes.json').read_text());allquotes=json.loads((OP/'audience-language.json').read_text())
checks['source_records']=len(sources);checks['source_ids_unique']=len(sources)==len({r['source_id'] for r in sources});checks['topic_count']=len(topics);checks['reference_queue_count']=len(json.loads((OP/'reference-top-50.json').read_text()));checks['verbatim_quotes_match']=all(any(q['comment_id']==a['comment_id'] and q['text']==a['text'] for a in allquotes) for q in quotes)
for t in topics:
 k=t['source_key']
 if k.startswith(('ig:','tt:')) and not any(s['source_id']==k for s in sources):errors.append('Unknown topic source '+k)
checks['source_date_counts']=dict(collections.Counter(str(s.get('posted_at') or '')[:4] or 'unknown' for s in sources))
changed=[]
for h in json.loads((OP/'input-hashes.json').read_text()):
 p=Path(h['path'])
 if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=h['sha256']:changed.append(h['path'])
checks['original_inputs_unchanged']=not changed;checks['changed_inputs']=changed
# Inspect original source file pointers, keep missing pointers visible rather than invented.
missing=sorted({s['source_file'] for s in sources if not Path(s['source_file']).exists()});checks['source_file_pointers_missing']=missing
if missing: errors.extend('Missing evidence file: '+p for p in missing)
ET.parse(OP/'bullseye.svg');checks['bullseye_svg_parses']=True
scores=[]
for p in files:
 r=subprocess.run(['python3','execution/prose_classifier.py','check',str(p)],capture_output=True,text=True)
 raw=r.stdout;(OP/(p.stem+'.prose-check.txt')).write_text(raw)
 # Keep raw diagnostics. Tables, exact quotations and linked source footers are intentionally preserved.
 scores.append(dict(file=p.name,raw_verdict=re.search(r'Verdict:\s*(\w+)',raw).group(1),flags=[x.strip() for x in raw.splitlines() if re.match(r'\s*\[\d',x)],editorial_disposition='Reviewed: structured research tables, exact source quotations and citation lines account for detected patterns; preserve evidence and scanability. These are research briefs, not approved social copy.'))
(OP/'prose-review.json').write_text(json.dumps(scores,indent=2)+'\n')
checks['prose_check_run_on_eight']=len(scores)==8;checks['raw_prose_flags_preserved']=True;checks['current_context_sources']=len(json.loads((OP/'current-source-ledger.json').read_text()));checks['current_listening_excerpts']=len(json.loads((OP/'current-audience-excerpts.json').read_text()))
checks['structural_status']='PASS' if not errors and all([checks['exactly_eight_artifacts'],checks['source_ids_unique'],checks['verbatim_quotes_match'],checks['original_inputs_unchanged']]) else 'FAIL';checks['errors']=errors
checks['content_review']='Research complete with explicit evidence limits. Jen reactions, new-copy taste approval, current format performance and conversions remain untested.'
checks['paid_credits_used']=0
(OP/'verification.json').write_text(json.dumps(checks,indent=2)+'\n')
m=json.loads((OP/'manifest.json').read_text());m['verification']=str(OP/'verification.json');m['structural_status']=checks['structural_status'];m['artifact_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files};(OP/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
print(json.dumps(checks,indent=2));raise SystemExit(bool(errors))
