from pathlib import Path
import json,csv,re,hashlib,collections
ROOT=Path.cwd(); OUT=Path(__file__).resolve().parents[1]; OP=OUT/'operator'
P=ROOT/'_active/clients/jen-listings/04-deliverables/social-content/2026-09-06-vidiq-production-run';L=P/'faithful-rebuild/reel-format-lab'
raw=json.loads((P/'sources.json').read_text()); comments=json.loads((P/'audience-comments.json').read_text())
files=[P/'sources.json',P/'audience-comments.json',L/'BENCHMARKS.json',L/'broll-resonance-pass/evidence/vidiq-research.json',L/'broll-resonance-pass/evidence/full-caption-reading-notes.json']
files+=list((P/'faithful-rebuild/sources').glob('*.md'))
files += [ROOT/'_active/clients/jen-listings/brand_context/CREATIVE-DIRECTION.md',ROOT/'skills/jen-santulan-listing-content/references/jen-real-voice-profile.md',ROOT/'_active/clients/jen-listings/06-system/content-intelligence/Jen First-Time Buyer ICP Options.md',ROOT/'_active/clients/jen-listings/06-system/content-intelligence/Jen First-Time Buyer ICP Source Ledger.md']
def writej(name,data): (OP/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def bucket(s):
 t=' '.join(str(s.get(k,'')) for k in ['concept','original_hook','caption_excerpt','format']).lower()
 if any(k in t for k in ['inspection','maintain','maintenance','repair','renovat','blinds','moving in','unpack','first meal']): return 'P2: What the home asks of you'
 if any(k in t for k in ['payment','mortgage','down payment','afford','income','closing cost','interest','budget','loan','house poor','financ']): return 'P1: Money you can live with'
 if any(k in t for k in ['question','client','realtor','agent','offer','contract','escrow']): return 'P3: Someone on your side'
 if any(k in t for k in ['valley','neighborhood','commute','northridge','los angeles','tarzana','burbank','reseda','train','rails']): return 'P4: Life around the home'
 if any(k in t for k in ['home','house','kitchen','room','bedroom','listing','condo']): return 'P5: Seeing through the listing'
 return 'CRAFT: Adjacent or unrelated'
rows=[]
for s in raw:
 r=dict(s);r['pillar']=bucket(s);r['source_file']=str(P/s['evidence']);r['snapshot_context']='Saved September 6 production research; individual capture times not uniformly recorded'
 r['baseline_kind']='creator_median_reported_by_provider' if s.get('median') else None
 r['freshness']='DATED_POST' if s.get('posted_at') else 'PUBLICATION_DATE_MISSING'
 r['paid_status']='UNKNOWN';r['conversion_status']='NOT_SUPPLIED'
 c=s.get('cohort'); r['editorial_use']='OWNED_VOICE' if c=='OWNED_PROXY' else 'BUYER_LANGUAGE' if c=='AUDIENCE_LANGUAGE' else 'TOPIC_REVIEW' if c=='TOPIC_CANDIDATE' else 'CRAFT_ONLY' if c=='FORMAT_ONLY' else 'COMPARATOR_REVIEW'
 if r['pillar'].startswith('CRAFT') and r['editorial_use']=='TOPIC_REVIEW':r['editorial_use']='CRAFT_ONLY'
 r['hygiene_status']='REVIEW: dates, paid status and engagement incomplete; not conversion proof'
 rows.append(r)
extra=[
 ('ig:DaTREfOhA3C','rachaelnovak','POV: You just closed on your new home... Before you unpack a single box, do these 10 things.',1800000,71.2,10.8,'broll-rachael.json','P2: What the home asks of you'),
 ('ig:DaF9sXJAY6p','natesoetaert.realestate',"Don't cook your first meal after moving in...",1800000,20.2,9.16,'broll-nate.json','P2: What the home asks of you'),
 ('tt:7663981949198929183','logan_the_lender','What are the steps to buying a house?',95700,110.4,41.7,'yap-logan.json','P3: Someone on your side'),
 ('ig:DbIuZQ_oeCb','tripsmortgagetips','Paper-reveal worked mortgage example',88900,19.9,50,'yap-trips.json','P1: Money you can live with'),
]
for sid,creator,hook,views,mult,dur,fn,pillar in extra:
 f=L/'evidence'/fn; files.append(f);v=json.loads(f.read_text())['result']
 rows.append(dict(source_id=sid,creator=creator,url=v['canonicalUrl'],platform=v['platform'],original_hook=hook,hook_status='provider transcription except Trips description; inspect source before quoting',views=views,outlier=mult,median=None,baseline_kind='creator_median_multiple_reported; exact denominator unavailable',duration_seconds=dur,source_file=str(f),review='SAVED_VIDEO_ANALYSIS_READ',pillar=pillar,editorial_use='TOPIC_REVIEW',paid_status='UNKNOWN',conversion_status='NOT_SUPPLIED',snapshot_context='Saved September 7 reel lab; views rounded provider display',freshness='PUBLICATION_DATE_MISSING'))
for pair in json.loads((L/'BENCHMARKS.json').read_text()):
 for key in ['higher','lower']:
  s=pair[key];sid='ig:'+s['url'].strip('/').split('/')[-1]
  rows.append(dict(source_id=sid,creator='natesoetaert.realestate' if 'short B-roll' in pair['pair'] else 'tripsmortgagetips',url=s['url'],platform='Instagram',original_hook=s['hook'],views=s['plays'],likes=s['likes'],comments=s['comments'],posted_at=s['date'],duration_seconds=s['duration'],review='SAVED_COMPARATOR_ANALYSIS',pillar='P2: What the home asks of you' if 'short B-roll' in pair['pair'] else 'P1: Money you can live with',editorial_use='COMPARATOR_REVIEW',source_file=str(L/'BENCHMARKS.json'),outlier=None,baseline_kind=None,paid_status='UNKNOWN',conversion_status='NOT_SUPPLIED',freshness='DATED_POST',snapshot_context='Saved September 7 comparator snapshot'))
notes=json.loads((L/'broll-resonance-pass/evidence/full-caption-reading-notes.json').read_text())
for n in notes:
 sid='ig:'+n['url'].strip('/').split('/')[-1];s=n['snapshot'];v=s.get('plays_vidiq',s.get('search_views'))
 rows.append(dict(source_id=sid,creator=n['creator'],url=n['url'],platform='Instagram',concept=n['summary'],views=v,outlier=s.get('search_median_multiple'),posted_at='2024-11-28' if n['creator']=='terra.wrightknudsen' else '2026-09-01' if n['creator']=='karime215' else None,review='SAVED_FULL_CAPTION_READING_NOTE',pillar='P3: Someone on your side' if n['creator']=='karime215' else 'P1: Money you can live with' if n['creator']=='iamstacierihl' else 'P4: Life around the home',editorial_use='TOPIC_REVIEW' if n['creator']=='karime215' else 'CRAFT_ONLY',source_file=str(L/'broll-resonance-pass/evidence/full-caption-reading-notes.json'),caption_excerpt=n['excerpt'],decision=n['decision'],paid_status='UNKNOWN',conversion_status='NOT_SUPPLIED',snapshot_context='Mixed provider/browser snapshots retained separately',separate_snapshot_metrics=s,freshness='HISTORICAL' if n['creator']=='terra.wrightknudsen' else 'REVIEW'))
assert len({r['source_id'] for r in rows})==len(rows)
writej('source-ledger.json',rows)
with (OP/'source-ledger.csv').open('w',newline='') as f:
 keys=['source_id','creator','platform','url','pillar','editorial_use','review','views','outlier','baseline_kind','posted_at','paid_status','source_file'];w=csv.DictWriter(f,keys,extrasaction='ignore');w.writeheader();w.writerows(rows)
# Language categories are a transparent triage, never population estimates.
def ccat(c):
 t=c['text'].lower()
 if c['platform']=='Instagram' and len(t.split())<=4:return 'CTA response or short reaction'
 if any(x in t for x in ['catch','criminal','illegal','crash','under water']):return 'Distrust / hidden downside'
 if any(x in t for x in ['monthly','mortgage','payments','house poor','afford','insurance','taxes','maintenance']):return 'Ongoing cost / financial comfort'
 if any(x in t for x in ['down','closing','deposit','pmi']):return 'Cash upfront / financing comparison'
 if any(x in t for x in ['confused','explain','question','understand']):return 'Needs explanation'
 return 'Other / contextual / unclassified'
classified=[dict(c,triage_category=ccat(c),category_method='keyword-assisted triage; not a representative coded survey') for c in comments]
writej('audience-language.json',classified)
quote_ids=['2980bfdfba5df210','3ccc24720f832823','8ebb267311ffe9f8','9ff68ae70b3a91d3','688e5699027ec6bb','2f97fa507616e33d','c8419cc957ec0553','a9a471dbd5ed8cc1','e6653241504ccbd9','43d9e8e599b83bde','8b280378b21a6438','fd1f58707c21165c']
selected=[next(c for c in classified if c['comment_id']==i) for i in quote_ids];writej('selected-buyer-quotes.json',selected)
# Explicitly supplied creator medians only; no selected-pool or global fallback baselines.
radar=[]
for r in rows:
 if r.get('median') and r.get('views') and r.get('original_hook') and r['editorial_use']=='TOPIC_REVIEW':
  radar.append(dict(platform=r['platform'],creator=r['creator'],hook_text=r['original_hook'],views=r['views'],baseline_views=r['median'],baseline_kind='PROVIDER_CREATOR_MEDIAN_NOT_MEAN',topic=r['pillar'],url=r['url'],source_ref=r['source_id'],permission_status='manual_reference',evidence_lane='PUBLIC_PROXY',paid_status='unknown',paid_brand_deal='',reported_outlier=r.get('outlier')))
writej('radar-input.json',radar)
# Candidate library is for triage; reviewed references rank ahead of uninspected high numbers.
priority=['ig:DcwRrZ6NZJI','ig:DbEo59HMjuH','ig:Db33yOnS6ig','ig:DceVX_-qheI','tt:7663981949198929183','ig:DcyMJKJohSq','ig:DciwVxDIhne','ig:DckFie2A0KX','ig:DcmeWC-POkw','ig:DaTREfOhA3C','ig:DaF9sXJAY6p','ig:DbIuZQ_oeCb','ig:Dadpa0OhHAU','tt:7652137045111934239','ig:DC7A7aWv9Nl','ig:DZqhDCfhc75','tt:7668367393843858719','ig:Dax4JjkOdcN','ig:DZY0IBOxhNC','ig:DcCYTUeCYFI','ig:DbMUBmlhKKr']
byid={r['source_id']:r for r in rows}; shortlist=[byid[i] for i in priority if i in byid]
for r in sorted(rows,key=lambda x:x.get('outlier') or 0,reverse=True):
 if len(shortlist)>=50:break
 if r not in shortlist and r['editorial_use']=='TOPIC_REVIEW' and not r['pillar'].startswith('CRAFT'):shortlist.append(r)
writej('reference-top-50.json',shortlist)
for f in list((L/'evidence').glob('*.json')):files.append(f)
writej('input-hashes.json',[dict(path=str(f),sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in dict.fromkeys(files)])
writej('data-summary.json',dict(original_sources=len(raw),normalized_sources=len(rows),original_review_counts=dict(collections.Counter(x['review'] for x in raw)),language_records=len(comments),language_platforms=dict(collections.Counter(x['platform'] for x in comments)),language_triage=dict(collections.Counter(x['triage_category'] for x in classified)),radar_rows=len(radar),top50=len(shortlist),paid_credits_used=0,owned_snapshot_rows=sum(r['editorial_use']=='OWNED_VOICE' for r in rows),private_outcomes_supplied=0))
print((OP/'data-summary.json').read_text())
