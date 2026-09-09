from pathlib import Path
import json,collections,re,datetime,hashlib
OUT=Path(__file__).resolve().parents[1];OP=OUT/'operator';ROOT=Path.cwd()
files=sorted(OUT.glob('0[1-8]-*.md'))
urls={'W01':'https://www.calhfa.ca.gov/dream/index.htm','W02':'https://www.car.org/aboutus/mediacenter/newsreleases/2026releases/July2026HomeSales','W03':'https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm','W04':'https://www.reddit.com/r/LosAngelesRealEstate/comments/1vxqmex/whats_the_biggest_mistake_you_made_buying_your/','W05':'https://www.reddit.com/r/LosAngelesRealEstate/comments/1vxa380/has_la_housing_inventory_increased_in_2026/','W06':'https://www.reddit.com/r/FirstTimeHomeBuyer/comments/1tisqil/ca_dream_for_all_updates_mega_thread/','W07':'https://singlefamily.fanniemae.com/media/document/pdf/lender-letter-ll-2026-03-updates-project-standards-property-insurance-requirements','W08':'https://selling-guide.fanniemae.com/sel/b4-2.1-01/general-information-project-standards','W09':'https://www.consumerfinance.gov/owning-a-home/prepare/figure-out-how-much-you-want-to-spend/','W10':'https://www.reddit.com/r/SFV/comments/1tq96p1/looking_for_home_buying_advice_and_a_realtor_in/','W11':'https://www.insurance.ca.gov/0400-news/0102-alerts/2026/Insurance-surge-expanding-options-for-Ca.cfm'}
entries=[('W01','CalHFA Dream For All','Live page; May 20, 2026 update; registration closed March 16','Current program status','Replace apply-now angle with status and alternatives; shared appreciation is not a grant'),('W02','C.A.R. July 2026 market report','Published August 17, 2026; observation month July','Official industry report','County/metro are not SFV; no individual listing prediction'),('W03','California DOI residential insurance guide','Revised January 2026; page read September 7','Official consumer guidance','Coverage and price are separate questions; no property quote implied'),('W04','LA first-home mistakes discussion','Search index: August 25, 2026; opened page says 1d ago; exact day unresolved','Agent-initiated discussion with self-reported buyer comments','Current-year qualitative signal; regret-seeking prompt biases sample; agent replies separate'),('W05','LA inventory discussion','Search index: August 24–25, 2026; relative page times differ','Commercial poster analysis + discussion','Local statistics unverified; useful lead to primary condo-policy documents only'),('W06','Dream For All discussion','2026 cycle; exact dates of selected replies unavailable','Public participant self-reports','Waitlist uncertainty is language evidence; forecasts not program facts'),('W07','Fannie Mae LL-2026-03','March 18, 2026; effective dates August 3, 2026 and January 4, 2027','Primary lender letter; page 3 text and screenshot requested','Keep current and future rules separate; no universal condo eligibility claim'),('W08','Fannie Mae project standards','Updated August 5, 2026','Primary current guide result','Qualifying waiver exceptions prevent blanket claims'),('W09','CFPB home budget guidance','Updated February 18, 2026; page read September 7','Official consumer guidance','Complete-cost framing; no personalized financial verdict'),('W10','SFV condo versus house discussion','Opened page says 3mo ago; precise day not recovered','Public local buyer question','Supports a concrete situation, not prevalence or demand'),('W11','California DOI coverage expansion alert','July 23, 2026 per official alert index; live page checked','Official current-event context','Some expansion starts January 2027; no claim all homes can now get coverage')]
(OP/'current-source-ledger.json').write_text(json.dumps([dict(id=i,title=t,url=urls[i],source_date=d,retrieved_at='2026-09-07',source_type=k,decision=c) for i,t,d,k,c in entries],indent=2)+'\n')
fresh_quotes=[('Q2026-01','No_Noise_1978','Letting my broker pick the home inspection people.','W04','Inspection trust'),('Q2026-02','Who_what_where_whyyy','Trusting the agent too much to share relevant info that wouldn’t be obvious to a buyer.','W04','Expectation of guidance'),('Q2026-03','lovingawareness1111','no money left for new floors, kitchen reno, bathroom reno, etc.','W04','Necessary work displaced wanted work'),('Q2026-04','shadowstripes','Trading off size for a nice view. Definitely not worth it, especially after the shift to WFH.','W04','Regret about space tradeoff'),('Q2026-05','overitallofittoo','Everyone my realtor recommended was great.','W04','Counterexample to blanket distrust'),('Q2026-06','Interesting-Film4379','Does anyone in the waitlist get moving?','W06','Waiting uncertainty')]
(OP/'current-audience-excerpts.json').write_text(json.dumps([dict(id=i,author=a,exact_excerpt=q,source_id=s,url=urls[s],category=c,publication_date_status='2026 discussion; individual exact day unavailable',retrieved_at='2026-09-07',truth_scope='self-reported experience or question, not independently verified') for i,a,q,s,c in fresh_quotes],ensure_ascii=False,indent=2)+'\n')
add='''## Current-source research addendum · checked September 7, 2026

**The fresh research changes the brief bank.** Move T03 inspection judgment and T12 repair/condition questions forward. Upgrade T14 from a general HOA topic to a current condo-project-review brief, B07. Narrow T16 to current program status rather than a program teaser. Add insurance coverage comparison as a timely research candidate.

### What is current, and what is not

| Evidence layer | Actual date coverage | Permitted conclusion |
|---|---|---|
| Saved social-content library | 75 records explicitly dated 2026; 3 dated 2025; 1 dated 2024; 2 dated 2022; 158 with no publication date | Source discovery and craft references; undated records do not prove 2026 trends |
| Original public comment bank | 20 dated 2026; 111 dated 2025; 27 undated | Buyer language; historical concerns require present corroboration |
| This run’s current-source layer | 11 cited primary/discussion sources; source dates and retrieval dates recorded separately | Current facts and recent qualitative questions, with scope limits |
| This run’s new listening excerpts | Six selected excerpts from two 2026-cycle discussions | Additional qualitative evidence; not added to the original sample count |
| Trend velocity / conversion | No comparable repeated snapshots or attributed buyer outcomes | Unmeasured; no trend-growth or conversion claim |

The 239 source-record total does **not** include the separate 11-source current-context ledger. Do not present 250 sources as 250 videos. Search-index dates and rendered Reddit relative times conflict on two discussions; the current-year classification is supported, the exact day is not settled.

### Four findings that change production

1. **Program status changes the invitation.** CalHFA’s live Dream For All page says new voucher applications are closed. The useful content is what a selected, waitlisted or not-selected buyer can clarify next, not a new-application pitch. Shared appreciation is part of the program’s structure. [CalHFA](W01)
2. **Condo review has a real 2026 change.** Fannie Mae retired Limited Review for applications dated August 3, 2026 onward; an applicable Full Review or waiver route matters. A separate reserve-allocation change applies January 4, 2027. Brief B07 gives this a buyer-facing question without suggesting all condos are ineligible. [Lender letter](W07), [current project standards](W08)
3. **Insurance needs a coverage conversation, not a generic crisis hook.** The January 2026 consumer guide explains that FAIR Plan basic coverage has limits and supplemental coverage may be relevant. The July expansion announcement includes future implementation, so it does not prove that a particular buyer can obtain coverage today. [DOI guide](W03), [DOI expansion alert](W11)
4. **A county headline is not a verdict on a Valley home.** C.A.R.’s July report gives Los Angeles County a $888,120 median for existing single-family homes, down 2.6% year over year. That does not tell us a particular condo is a bargain or that every seller will negotiate. Use the report as context, then obtain the property-specific comparison. [C.A.R., released August 17](W02)

### New listening: exact language, with the opposing evidence kept

'''
for i,a,q,s,c in fresh_quotes:add+=f'> {q}\n\n[{a}]({urls[s]}) · {i} · {c}. Exact comment day unresolved; retrieved September 7.\n\n'
add+='''The LA regrets thread was started by an agent asking about mistakes. It selects for negative experiences and contains professional responses and promotion. The contrasting positive recommendation is retained so we do not turn a few complaints into “agents cannot be trusted.” These reports guide questions; they do not verify the alleged transactions or professional conduct.

### Timely candidate briefs

| Candidate | Why now | Payoff | Format | What must still be checked |
|---|---|---|---|---|
| T21 · The condo and the lender’s building review | August 2026 Fannie Mae change; strengthens T14 | The question to ask before confusing personal preapproval with project eligibility | B07 carousel | Actual lender/project/application facts |
| T22 · Dream For All: what happens after the status you received? | Current page describes closed registration and status paths | A useful next clarification instead of an expired invitation | Expert answer | Current program page immediately before publishing; buyer’s actual status |
| T23 · Comparing two insurance quotes that cover different things | Current California coverage guidance | Understand why premium alone is not the comparison | Carousel or expert + licensed insurance professional | Actual coverage terms; no generic premium estimate |

These are **timely factual opportunities**, not proven viral topics. Their source support is stronger than their social-performance evidence. The current findings improve topic substance; the saved Reel references still guide form.

'''
for k,v in urls.items():add=add.replace(']('+k+')',']('+v+')')
p=files[3];s=p.read_text();s=s.replace('## Twenty ranked topic seeds',add+'## Twenty core topic seeds');s=s.replace('The ranking below is editorial:','The core ordering below is editorial and precedes the freshness addendum; that addendum promotes T03, T12 and T14. Selection uses');p.write_text(s)
# Link the freshness detail from all other documents without duplicating market claims.
for p in files:
 if p==files[3]:continue
 s=p.read_text();i=s.index('\n\n',s.index('\n')+1) if '\n\n' in s[s.index('\n')+1:] else len(s)
 note=f'\n\n**Freshness:** Current 2026 facts and new listening are separated from historical and undated references in the [research addendum](<{files[3]}>).'
 s=s[:i]+note+s[i:];p.write_text(s)
# Upgrade the machine handoff without changing legacy source facts.
topics=json.loads((OP/'topic-bank.json').read_text())
for t in topics:
 t['priority_after_current_check']='PROMOTE' if t['id'] in ['T03','T12','T14'] else 'MAINTAIN'
 if t['id']=='T16':t['status']='Use current status paths; new Dream For All applications closed per W01'
for id,title,source in [('T21','The condo and the lender’s building review','W07'),('T22','Dream For All: what happens after your status?','W01'),('T23','Two insurance quotes with different coverage','W03')]:topics.append(dict(id=id,topic=title,source_key=source,source_url=urls[source],status='Current factual candidate; social response untested',priority_after_current_check='TIMELY_TEST'))
(OP/'topic-bank.json').write_text(json.dumps(topics,ensure_ascii=False,indent=2)+'\n')
# User-facing index is navigation, not a ninth research deliverable.
index='''# Jen’s research foundation

Eight finished strategy artifacts · September 7, 2026

**Start with the bullseye and the blueprint.** The package keeps Jen’s approved carousel direction and builds a stronger audience, research and ideation foundation around it.

**The main call:** focus on the Valley buyer comparing homes and compromises. Use carousels for comparisons, expert videos for judgment, and B-roll when a recognizable moment earns a useful caption.

| Artifact | What is inside |
|---|---|
'''
descriptions=['Niche, audience portrait, beliefs/resistance, 12 sourced buyer quotes, positioning and service links','Five nested audience rings, sourcing map, three-bucket mix, nine choices and experimental reserve','12-account watchlist, eight-attribute positioning comparison, opportunities and contrary evidence','20 core seeds + 3 timely candidates, current-source addendum, 50-reference queue and radar interpretation','10 source openings, six interpreted pattern families, messaging and higher/lower comparisons','Structure × visual matrix, three production recipes, approved visual constraints','Seven complete research/production briefs; exact remaining Jen inputs','First batch, ownership, handoff prompt, measurement, resource opportunities and 90-day sequence']
for p,d in zip(files,descriptions):index+=f'| [{p.read_text().splitlines()[0][2:]}](<{p}>) | {d} |\n'
index+='''
## What the research can honestly claim

The work combines analysis of saved September VidIQ material with fresh September 7 web research and social listening. It is **not an all-2026 video database**: of 239 social records, 75 have a 2026 publication date and 158 are undated. The original 158-comment bank is mostly from 2025. These age limits are visible in the mining report.

The fresh check contributes 11 current-context sources, six selected discussion excerpts and consequential corrections: program registration status, condo-review changes and insurance coverage distinctions. Historical examples are used for craft, never labeled current trends. No new VidIQ credits were spent.

## Ready, retained and still to learn

**Ready:** all eight documents, categorized evidence, topic/format decisions and production handoffs. **Retained:** approved carousel work and Jen’s voice. **Still to learn:** her personal reaction where missing, which new Reel treatment she approves and which content brings relevant buyer conversations.

The standard readable-file view is used here; no dedicated native document-artifact API was available. The Markdown files are the portable source, with sidecar metadata and an index opened in Codex. No HTML/PDF export, publishing or main-thread review edits were made.
'''
(OUT/'START-HERE.md').write_text(index)
(OUT/'START-HERE.metadata.json').write_text(json.dumps(dict(title='Jen’s research foundation',artifact_type='document-index',date='2026-09-07'),indent=2)+'\n')
# Ring image: a static diagram embedded in the bullseye, not a new social aesthetic.
colors=['#f1f3f5','#e6edf1','#cedde5','#a7bfcc','#233e4d'];labels=['5 · General audience','4 · US first-time buyers','3 · LA first-time buyers','2 · Valley tradeoff buyers','1 · Condo or older house']
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="740" viewBox="0 0 1000 740"><rect width="1000" height="740" fill="#faf9f6"/><text x="40" y="52" font-family="Arial" font-size="29" fill="#233e4d">Jen’s audience bullseye</text>']
for i,(r,c) in enumerate(zip([300,244,188,132,76],colors)):
 svg.append(f'<circle cx="340" cy="390" r="{r}" fill="{c}" stroke="#faf9f6" stroke-width="3"/>')
 y=390-r+30 if i<4 else 394
 svg.append(f'<text x="340" y="{y}" text-anchor="middle" font-family="Arial" font-size="16" fill="'+('#ffffff' if i==4 else '#233e4d')+'">'+('1 · The exact buyer' if i==4 else labels[i])+'</text>')
notes=[('1','The person we picture'),('2','The local decision we serve'),('3','Geography widens within LA'),('4','Broad buying moments'),('5','Craft inspiration only')]
for i,(n,t) in enumerate(notes):
 y=210+i*78;svg.append(f'<text x="675" y="{y}" font-family="Arial" font-size="21" fill="#233e4d">{n} · {t}</text>')
svg.append('<text x="40" y="718" font-family="Arial" font-size="15" fill="#536774">Conceptual rings, not population estimates. Full definitions and sourcing rules below.</text></svg>')
(OP/'bullseye.svg').write_text(''.join(svg))
p=files[1];s=p.read_text();s=s.replace('## Five rings, with an explicit change at each step',f'![Jen’s five audience rings](<{OP/"bullseye.svg"}>)\n\n## Five rings, with an explicit change at each step');p.write_text(s)
# Document actual execution and adaptations rather than claiming missing human input occurred.
manifest=dict(date='2026-09-07',scope='New, isolated Jen research documents in side conversation',artifacts=[str(p) for p in files],workflows={'gb-interview':'Synthesized existing voice, context and buyer evidence; no new interview claimed','gb-whitespace':'Specimen-based opportunity map; account-wide scoring unconfirmed','gb-bullseye':'Five rings, three-bucket mix, bench, service links and learning criteria','ai-topic-mining-engine':'20 core seeds plus 3 current-context candidates; 50-reference triage library','ai-hook-pattern-extractor':'10 openings and 6 interpreted families with limits','gb-format-find':'Structure/layout matrix and 3 production recipes','ai-creative-reaction-sprint':'7 prepared research briefs; Jen reaction and energy input pending, not fabricated','ai-content-operations':'Roles, handoff and learning cycle in blueprint','trend-hook-radar':'Executed existing script on 68 baselined rows; raw confidence demoted to field-completeness','gb-blueprint':'Assembled written blueprint with 90-day sequence'},adaptations=['Five AI engine workflows plus growth strategy workflows organized into eight requested reader artifacts; no claim of eight native mining commands','No HTML/PDF skill exports: native-readable written artifact preference honored','No fake TAM, lead value, trend velocity, paid-status check or causal proof','No bulk generated hook quota: research and production briefs requested','No shared chain finalizer or learning-log writes: isolated side-conversation artifact scope','Raw radar generated writing is machine output for inspection only; user-facing library supplies editorial judgment'],cost=dict(vidiq_credits=0,new_paid_calls=0),source_counts=dict(social_records=239,original_language_records=158,current_context_sources=11,current_excerpt_records=6,topic_seeds=23,reference_queue=50),verification='Pending final local checks')
(OP/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Created eight documents, index, current-source records and bullseye diagram.')
