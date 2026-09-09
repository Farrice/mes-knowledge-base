from pathlib import Path
import json,re
OUT=Path(__file__).resolve().parents[1]; ROOT=Path.cwd(); OP=OUT/'operator'; P=ROOT/'_active/clients/jen-listings/04-deliverables/social-content/2026-09-06-vidiq-production-run';L=P/'faithful-rebuild/reel-format-lab'
S={r['source_id']:r for r in json.loads((OP/'source-ledger.json').read_text())}
links={'VOICE':ROOT/'skills/jen-santulan-listing-content/references/jen-real-voice-profile.md','DIRECTION':ROOT/'_active/clients/jen-listings/brand_context/CREATIVE-DIRECTION.md','PRIOR':ROOT/'_active/clients/jen-listings/06-system/content-intelligence/Jen First-Time Buyer ICP Options.md','SOURCELEDGER':OP/'source-ledger.csv','LANGUAGE':OP/'audience-language.json','BENCHMARKS':L/'BENCHMARKS.json','VIDIQ':P/'faithful-rebuild/sources/vidiq-system-v3.md','CFPB':'https://www.consumerfinance.gov/owning-a-home/prepare/figure-out-how-much-you-want-to-spend/','SFV':'https://www.reddit.com/r/SFV/comments/1tq96p1/looking_for_home_buying_advice_and_a_realtor_in/'}
files=['01-positioning-dossier.md','02-audience-bullseye.md','03-positioning-opportunity-map.md','04-ai-topic-mining-report.md','05-hook-and-messaging-library.md','06-format-playbook.md','07-creative-brief-bank.md','08-content-blueprint.md']
def ref(m):
 key=m.group(1)
 if key in S:return f"[@{S[key]['creator']} reference]({S[key]['url']})"
 if key in links:return f'[{key.lower().replace("sourceledger","source ledger")}]({"<"+str(links[key])+">" if isinstance(links[key],Path) else links[key]})'
 if key.isdigit():return f'[Document {key}](<{OUT/files[int(key)-1]}>)'
 raise ValueError(key)
def doc(n,text):
 text=re.sub(r'\{\{([^}]+)\}\}',ref,text.strip())+'\n';p=OUT/files[n-1];p.write_text(text)
 (OUT/(p.stem+'.metadata.json')).write_text(json.dumps(dict(title=text.splitlines()[0].lstrip('# '),artifact_type='document',client='Jen Santulan',date='2026-09-07',status='research_complete_recommendations_untested',sequence=n),indent=2)+'\n')

doc(1,'''# Jen’s niche and positioning dossier

**Decision:** Keep first-time buyers in the San Fernando Valley as the umbrella. Speak most directly to the buyer choosing between homes that each require a different compromise.

September 7, 2026 · Research synthesis, not a new client interview. Existing direction preserved; recommendations below await performance evidence.

## The person across the table

They can see a route to buying, but the homes in reach are asking them to give something up. One has the kitchen they want and shared walls. Another has a yard and repairs they cannot price from photographs. A third gives them space but changes the trip to work. They have saved listings; adding more listings may make the decision harder.

The [local buyer discussion](https://www.reddit.com/r/SFV/comments/1tq96p1/looking_for_home_buying_advice_and_a_realtor_in/) supplies a concrete version: a person comparing “a pretty decent condo or an okay house that probably will need some work done.” That is a real question in Jen’s market. It does not establish the size of this segment.

**Working portrait, inferred from that discussion and the saved comment bank:** This buyer wants to feel responsible, not timid. They may be embarrassed to ask for another explanation. They want someone to help them see the compromise before it becomes their everyday life. An honest reason to wait can build more trust than another reason to stretch.

The older age, household-income and rent bands are planning assumptions, not verified boundaries for this audience. Relationship status, income type and life stage provide occasional context; they do not determine who deserves help. The main qualification is the decision being faced.

## What Jen can credibly stand for

**Recommended positioning:** Jen helps first-time buyers in the Valley understand the tradeoffs, ask every question, and choose a home they can feel comfortable living with.

Two alternate expressions for different surfaces:

- **Short:** Clear, personal guidance for your first home in the Valley.
- **Service-led:** From the saved listing to the questions that change your decision, Jen helps you work through the purchase one step at a time.

These are positioning statements, not mandatory hooks. Social openings should start inside a recognizable moment; the positioning should be felt in Jen’s response.

The strongest support is her recorded phrase, preserved in the voice profile: “i do this to protect you and your best interest.” The underlying voice-memo transcript was not recovered in this run, so this is a quotation from the saved profile, not newly checked audio. {{VOICE}}

## Beliefs, resistance and the cost of saying it aloud

| Situation | What is observed | Interpretation to test | Messaging consequence |
|---|---|---|---|
| A low-down-payment example looks attainable | Public comments ask what the monthly payment becomes | The buyer distrusts an entry price that hides the ongoing obligation | Show what happens after the exciting headline |
| Two down-payment options appear | A commenter asks which is best, 20% or 3% | They need a comparison that respects the cash they would keep or spend | Explain the choice; avoid a universal winner |
| The agent has already explained a term | The Karime reference names embarrassment about asking again | Silence may protect the buyer from feeling uninformed | Let Jen answer as an ally; never make the buyer the joke |
| A polished home needs a compromise | The local discussion weighs condition against shared walls | A buyer may feel ungrateful for rejecting a home they can afford | Make personal fit discussable without declaring one property type superior |
| They have not decided to buy | Current direction permits curiosity without pressure | Remaining undecided can protect financial comfort and autonomy | Offer a next step that makes the decision clearer, including waiting |

The interpretations are hypotheses. They are not interview findings from Jen’s clients. Buyer language is documented below; performance and conversion remain separate.

## Buyer language that changes the brief

The complete, categorized bank contains 158 public comments/replies: 131 from YouTube and 27 from Instagram. It is a relevance-selected sample, largely outside Jen’s own audience. Short CTA responses, replies and substantive questions are distinguished in the supporting data. {{LANGUAGE}}

<!-- QUOTES -->

Use the language to identify a concern, not to repeat commenters’ financial claims. A question about interest is evidence of confusion; a commenter’s calculation is not verified mortgage advice.

## Pain → useful content → service bridge

| Buyer concern | Content has to deliver | Natural next step | Commercial role |
|---|---|---|---|
| Which home’s compromise is livable? | A concrete comparison with a reasoned verdict | Bring the two real options to Jen | Buyer consultation |
| Is that payment comfortable for my life? | Questions and inputs for a complete budget conversation | Work through the property with Jen and a lender | Readiness and purchase planning |
| Am I missing something in the report? | What needs clarification, professional assessment and a decision | Discuss the actual report with the relevant professionals | Representation and coordination |
| Am I allowed to ask again? | Dignity plus an example of the help Jen provides | Ask the unresolved question | Lower-friction first conversation |
| Does this place fit my actual week? | An observation from the property or daily route | Arrange an informed second look | Search refinement |

Commission terms, consultation pricing, close rate and lead value were not supplied. The package does not estimate income from views. No new consultation, client or revenue event was generated by this research.

## Jen’s seven-attribute starting position

| Attribute | Assessment | Evidence / remaining limit |
|---|---|---|
| Topic selection | Strong direction | Valley tradeoff buyer already identified in September 3 research; not a proven conversion segment |
| Substance depth | Possible, with usable starting material | Existing buyer-education posts; each new technical claim still needs support |
| Unique stories | Possible | Source-linked buyer and inspection stories in prior dossier; confirm exact details before reuse |
| Audience specificity | Strong direction | A decision in a named market, rather than a broad demographic persona |
| Delivery style | Strong evidence of voice | Saved captions and filmed-analysis notes support calm warmth and gentle humor |
| Storytelling | Possible | User likes expert-video topics; full Reel packages are not approved |
| Visual format | Strong taste approval | Approved six-slide photographic carousel; no owned performance claim |

## What would change this recommendation

Keep the Valley tradeoff buyer as the starting point from {{PRIOR}}. Change the emphasis if Jen’s actual inquiries consistently concern a different decision, if she has little experience with these comparisons, or if repeated tests attract viewers who are not prospective local buyers. The next documents translate this audience into the bullseye, topic choices and production briefs. {{2}}
''')
quotes=json.loads((OP/'selected-buyer-quotes.json').read_text())
qtext='\n\n'.join(f'> {q["text"]}\n\n[{q["author"]}, {q["published_at"][:10]}]({q["source_url"]}) · comment `{q["comment_id"]}` · {q["triage_category"]}' for q in quotes)
p=OUT/files[0];p.write_text(p.read_text().replace('<!-- QUOTES -->',qtext))

doc(2,'''# Jen’s audience bullseye

**Center:** A first-time Valley buyer comparing a comfortable condo or townhome with an older, smaller or farther-away house, unsure which compromise they will regret.

Use this person to make the writing specific. Build repeatable content around Rings 2–4 so the account has room to grow.

## Five rings, with an explicit change at each step

```mermaid
flowchart TB
    R5[5 · General entertainment and money audiences]
    R4[4 · US first-time buyers facing a meaningful housing tradeoff]
    R3[3 · SFV and Los Angeles first-time buyers facing that tradeoff]
    R2[2 · SFV first-time buyers comparing homes and compromises]
    R1[1 · SFV buyer choosing condo or townhome versus an older house]
    R5 --> R4 --> R3 --> R2 --> R1
```

| Ring | Constraint relaxed from the ring inside | Relative size | Purchase-conversation proximity | Competitive evidence |
|---|---|---|---|---|
| 1 | None: the precise reference person | Smallest by definition; count unknown | Potentially close if actively comparing | A real SFV discussion demonstrates the situation; creator competition not measured |
| 2 | Remove the condo-versus-house restriction | Broader; count unknown | High when a real property decision is present | Jen’s own budget/wishlist post supplies a specimen, not a market-share measure |
| 3 | Widen geography from SFV to the rest of Los Angeles | Broader; count unknown | Relevant if Jen serves the location | LA/California sources exist; no exhaustive local competitor audit |
| 4 | Widen geography to the United States | Broader; count unknown | Mixed: many viewers cannot become Jen’s local clients | Nate, Rachael, Logan, Trips and Karime supply topical/craft examples |
| 5 | Remove the remaining first-purchase and housing-decision constraints | Broadest; count unknown | Usually low for Jen’s service | General home, finance and entertainment specimens are craft references only |

Size follows the nesting; it is not TAM research. Proximity is a strategic estimate, not a measured conversion rate. Geography widens in two deliberate steps so local service relevance remains visible. Ring 5 is deliberately outside the buyer definition; the jump relaxes all remaining constraints.

## The starting mix: three buckets, two pieces each, one experiment

A **seven-piece batch**, not a requirement to publish seven videos every week. It may run across two or more weeks to fit Jen’s capacity. Carousels and Reels have separate jobs.

| Bucket | Ring and job | Two first topics | Why this belongs |
|---|---|---|---|
| **The home you can live with** / alternate: Before the offer | 2–3 · Decision support | Condo versus older house; what changes after a second look | Preserves the existing Valley tradeoff focus |
| **The question you almost didn’t ask** / alternate: Ask Jen | 2–3 · Trust and expertise | Asking for another explanation; inspection-report panic | Connects Jen’s protective voice to the strongest user-endorsed reference |
| **The part of buying you recognize** / alternate: House-shopping moments | 4 · Reach, re-aimed at the local buyer | Listing codewords; first purchase after closing that surprised the buyer | A recognizable scene can travel without turning into generic motivation |

No bucket requires every topic to be a B-roll Reel. The approved negotiation carousel remains a comparison; the first asking-again treatment is B-roll; inspection triage belongs in an expert explanation.

## Bucket bench and service connection

Every row is a choice, not an obligation. “Working” thresholds below are proposed learning rules, not industry benchmarks. Lead value is unknown for every row because Jen’s economics and attribution were not supplied.

| Candidate / alternate name | Ring; role | Example topics | Service / useful response | Working signal across three batches; then decision |
|---|---|---|---|---|
| The home you can live with / Before the offer | 2–3; decision support | Condo vs older house; second-look priorities | Property comparison consultation | At least two relevant property-comparison inquiries: continue; otherwise review exposure and test Money after closing |
| The question you almost didn’t ask / Ask Jen | 2–3; trust | Ask again; inspection confusion | Buyer question conversation | At least two substantive local buyer questions: continue; otherwise test a more specific question |
| The part of buying you recognize / House-shopping moments | 4; reach | Codewords; furnishing surprise | Optional first conversation | One relevant inquiry or repeated identifiable target-buyer responses: retain provisionally; views alone do not earn more slots |
| Money after closing / The payment and the rest | 2–3; readiness | Cash kept back; quoted payment versus full expense picture | Jen + lender planning | Two readiness questions: trial as a core bucket |
| Life around the home / A normal Tuesday | 2–3; search refinement | Route observation; layout during a working day | Search refinement | Two local requests about fit: keep; no response prompts a better specimen before retirement |
| The offer and what happened next / After you find it | 2–3; expertise | Competing offer; report follow-up | Buyer representation | Two specific offer-stage questions: keep |
| Income that needs explaining / Before the lender call | 2–3; specialist test | Mixed-income preparation; documents that need clarification | Lender introduction | One relevant inquiry plus Jen’s evidence of service fit: develop; otherwise leave on bench |
| Buying with help / Before money changes hands | 2–3; specialist test | Family contribution expectations; who answers which question | Professional coordination | One qualified conversation and verified technical scope: develop; otherwise hold |
| A fresh start with support / Someone to work it through with | 2–3; trust | Decision load; asking someone to join a second look | Buyer planning | Two relevant responses about support: develop if Jen has a real story |

A zero after poor distribution is inconclusive. After adequate exposure across two or three batches, change the premise or its presentation before discarding the audience.

## Sourcing map: who to study and what to take

| Ring | Pillar and bucket served | Concrete topic examples | Source and permitted use | Search starting points | Trap |
|---|---|---|---|---|---|
| 1 | Property tradeoffs → The home you can live with | Shared walls versus repair capacity; paying for a renovated condo; a second visit focused on a dealbreaker | SFV buyer discussion: audience language and questions; no creator winner identified at this exact ring | SFV condo versus house; Valley older home repairs | Turning one person’s story into a population claim |
| 2 | Local decision confidence → both narrow buckets | Ask again during a tour; what to clarify after an inspection; price versus cash needed | Jen’s budget/wishlist and affordability posts: own voice/topic material | SFV first-time buyer questions; SFV inspection decisions | Assuming a published post proves lead generation |
| 3 | LA purchase choices → both narrow buckets | Buy/wait comparison; local home cost inputs; competing priorities | California-context sources in the ledger: topic candidates pending claims review | LA condo first purchase; Los Angeles home payment questions | Substituting a neighborhood name for real local substance |
| 4 | Familiar buying moments → broad bucket | Permission to ask; moving-day surprise; source-led comic translation | Karime, Rachael, Nate: question/scene construction; Logan: casual answer delivery | first home embarrassed question; just closed moving costs | Importing another state’s rules, numbers or client story |
| 5 | No topic pillar; craft reserve only | Reveal timing; ordinary gesture before an explanation; visual comparison | Moneyletter cups and Brickhomehaven reveal: craft only | visual reveal; object comparison demonstration | A popular unrelated subject becoming Jen’s content strategy |

Sources: {{SFV}} · {{ig:DbEo59HMjuH}} · {{ig:Db33yOnS6ig}} · {{ig:DcwRrZ6NZJI}} · {{ig:DaTREfOhA3C}} · {{tt:7663981949198929183}} · {{ig:DcTb9M9xLC0}} · {{ig:DcAJdUvBDXO}}.

## Four controlled experiments

1. **A real second-look disagreement:** Jen explains what changed her view of a home. Tests the opportunity in visible judgment. Requires her actual example.
2. **Buyer asks off-camera:** Someone asks Jen an actual buyer question during an ordinary action. Tests whether the natural answer survives filming better than a memorized script.
3. **A personal item from Jen’s first home:** Tests whether a truthful ownership memory strengthens the buyer relationship. Item and story are still needed.
4. **One property, two different lives:** A hypothetical comparison using the same verified property inputs. Tests whether life-fit comparisons outperform feature lists. The scenarios must be labeled hypothetical.

**Ring 5 traps:** a general marriage skit with a house word pasted in; a forecast of the next housing crash without evidence; a luxury mansion spectacle without a first-buyer connection. They may attract attention, but no evidence here shows they bring Jen relevant buyers.

Read {{7}} for the first seven briefs and {{8}} for measurement and ownership.
''')

doc(3,'''# Jen’s positioning opportunity map

**Recommended edge:** Show the judgment and care that happen between finding an attractive listing and deciding to buy it.

This is a supported positioning hypothesis. The research does not prove that no other Valley agent occupies it.

## What the source pool actually contains

The original bank contains 228 unique records, including 12 Jen posts and three YouTube comment-source videos. Its inherited review labels are 136 search-only, 64 profile-only, 24 with video analysis, three with comments collected, and one unavailable video. This run adds 11 unique Reel-lab references for **239 records**. That total describes a mixed research library, not 239 fully watched competing posts. {{SOURCELEDGER}}

The detailed watchlist below deliberately mixes topic references, delivery references and Jen’s own voice. A creator’s place here is an analyst recommendation, not a claim that Jen endorsed the account. Size matching, paid distribution and local conversion are generally unknown.

## Twelve-account study list

| Account | What the available specimen supports | Use / boundary |
|---|---|---|
| @_jiing | Budget versus wishlist, gentle misconception correction, lived personality | Own voice and experience; keep luxury and everyday registers distinct |
| @karime215 | A buyer’s embarrassment answered with warmth and tangible stakes | Closest B-roll treatment reference; one selected post, not a proven formula family |
| @natesoetaert.realestate | Concrete moving-day warning versus a broader warning | Study the controlled comparison; full caption payoff not recovered |
| @rachaelnovak | Familiar milestone → specific unfinished task → caption | Caption-led structure; cannot judge the missing list’s quality |
| @logan_the_lender | A plain question answered during an ordinary action | Delivery model; do not copy oversimplified transaction sequencing |
| @tripsmortgagetips | Worked explanation with a visible object; higher/lower reach comparison | Useful when the numbers are the story; do not require a prop for every answer |
| @battlebornsteve | Comic listing-language translation | Approved carousel family; local adaptations still need responsible wording |
| @christianatherealtor | Answers a specific viewer concern with the environment itself | Observation as proof; rail noise does not establish conditions at Jen’s properties |
| @carligerber | Specific neighborhood-visit prompt | Shows a concrete action; does not rescue the rejected commute copy |
| @sandyceo | A named Valley place as the subject | Local familiarity; verify current access/details before production |
| @terra.wrightknudsen | Personal place attachment with an admitted inconvenience | Story craft only; 2024 specimen is historical, not a current trend |
| @moneyletter | Financial ideas made visible with ordinary objects | Cross-topic visual craft; reject its budgeting ratios as universal advice |

Specimens: {{ig:DbEo59HMjuH}} · {{ig:DcwRrZ6NZJI}} · {{ig:DckFie2A0KX}} · {{ig:DaTREfOhA3C}} · {{tt:7663981949198929183}} · {{ig:DcyMJKJohSq}} · {{ig:DceVX_-qheI}} · {{tt:7668367393843858719}} · {{ig:DZqhDCfhc75}} · {{ig:DZY0IBOxhNC}} · {{ig:DC7A7aWv9Nl}} · {{ig:DcTb9M9xLC0}}.

## Positioning wheel: eight attributes

These are specimen-level judgments. A full per-account score would imply coverage we do not have; account-wide superiority is unconfirmed on every attribute.

| Attribute | Seen in the references | Jen’s available strength | Decision |
|---|---|---|---|
| Topic | Finance tips and buying tasks recur in the bank | Valley property tradeoffs are already her chosen focus | Make a buyer’s decision the topic boundary |
| Substance | Some high-reach claims omit conditions | Jen can explain the specific choice and involve the right professional | Pair each claim with usable support |
| Perspective | Authority often appears as instruction | Her recorded service language is protective | Let her take the buyer’s side without attacking others |
| Audience | Many references address national buyers | Named Valley context plus an identifiable decision | Include local substance when it changes the choice |
| Story | Client reveals and milestone moments appear | Existing first-buyer stories are documented in prior research | Recover one actual turning point before drafting a story |
| Delivery | Casual answers coexist with formal demonstrations | Calm warmth, ordinary cadence and occasional dry humor | Test the question-led answer first |
| Structure | Lists, warnings, comparisons and permission appear | Approved comic/comparison carousels and a preferred permission reference | Select structure by topic; keep more than one available |
| Visual | Repeated B-roll, touring, props and direct camera | Jen supplies real imagery; photographic carousel already approved | Reuse her footage and the approved carousel system |

## Four opportunities and their competing explanations

| Opportunity | Supporting evidence | What could make it a weak bet | Action |
|---|---|---|---|
| Make the hidden compromise visible | Existing ICP research and local discussion; approved comparison carousel | Comparison content might be useful without generating inquiries | Lead the first carousel brief with a concrete choice; measure actual questions |
| Make asking feel welcome | Karime source, Jen’s protective words, user’s clear taste response | Warmth alone may create likes without demonstrating competence | Follow recognition with the kind of question Jen helps resolve |
| Show one judgment in real time | Logan’s natural delivery; user likes expert-video topics | Over-scripted speech could remove the very quality being borrowed | Give Jen an opening, reasoning beats and optional script rather than insist on recitation |
| Let a place answer a buyer’s question | Rail-noise specimen and local-place content | Lifestyle imagery may attract visitors rather than buyers | Tie observation to a purchase decision; leave broad place content occasional |

**Contested:** warmth is not unique to Jen; Karime demonstrates it well. **Supported as a fit:** Jen’s voice and the approved visual treatment can carry it. **Unconfirmed as an advantage:** whether her specific combination wins more relevant inquiries than competitors. **Redirected:** generic “programs nobody tells you about” is a source category, not Jen’s central identity.

## Why some VidIQ instructions need interpretation

The saved v3 strategy says a median multiple proves the format caused growth. It does not: subject, distribution, creator, post age and other factors remain mixed together. It also recommends bank-distrust and program-FOMO language that conflicts with Jen’s current direction. Keep the referenced post and its useful construction; reject unsupported causality and borrowed distrust. {{VIDIQ}}

The automated radar can retrieve candidate groups. It cannot decide that an empty cell is an uncontested market opportunity, that a short hook sounds like Jen, or that a missing caption fulfilled its promise. Those judgments remain explicit in these documents.

## Blind spots that matter

This is a selected, winner-heavy source pool, not a representative competitor census. Most publication dates and paid-status fields are missing. Saves, private shares, retention and attributable buyer outcomes are not available. The supplied 12-post Jen snapshot is too mixed and small to set an account-wide benchmark; the earlier dossier’s 2,779-post archive count was not re-audited here. We therefore use **proxy-led research with limited owned evidence**, not a false claim that Jen is a new account.

Next: {{4}} turns these opportunities into ranked topics; {{6}} assigns the right form.
''')

topics=[
('T01','Asking the question again','P3','2','B-roll + caption','Buyer feels they have used up their allowance to ask','ig:DcwRrZ6NZJI','User-endorsed treatment; source has public reach, no conversion proof','Make the buyer feel welcome; caption shows what asking again can clarify','A useful way to ask for an explanation without pretending to understand','Question conversation','Which repeated question does Jen actually welcome most?','Ready for Jen’s small input'),
('T02','Condo you like versus house that needs work','P2','2','Six-slide comparison carousel','Two affordable options ask for different compromises','SFV','Local buyer discussion + established ICP direction','Compare the same decision dimensions for both homes; no universal winner','A comparison the buyer can use with a partner','Property comparison','What compromise most often changes the decision in Jen’s experience?','Research-ready; real property inputs needed'),
('T03','The inspection report looks worse than the tour felt','P2','2','Expert answer','Buyer cannot tell which finding deserves immediate attention','ig:DcyMJKJohSq','Expert demonstration is craft evidence; user likes inspection topic','Explain how questions are sorted and who resolves them; no unseen defect diagnosis','A calmer, more informed follow-up conversation','Representation','Which real finding looked alarming until it was explained, or vice versa?','Jen example and technical check needed'),
('T04','The payment looks possible; the rest of life looks tight','P1','2','Expert answer or comparison carousel','Qualification and personal comfort are being treated as the same question','ig:Dadpa0OhHAU','Buyer comments corroborate cost concern; source’s advice contains oversimplifications','Use a full budget conversation, not a universal income percentage','Something a buyer can discuss without sounding negative','Readiness planning','What do buyers tend to leave out when telling Jen their comfortable payment?','Fact-supported brief; fresh inputs needed'),
('T05','Realtor codewords before your next tour','P5','4','Approved carousel family','Listing language creates an expectation the photo cannot settle','ig:DceVX_-qheI','Strong source reach + user approval of current carousel package','Retain the comic translation and a useful question; avoid categorical defect claims','A knowing laugh that makes a friend a better shopper','Optional tour question','Which phrase does Jen hear that has a recognizable, fair translation?','Existing approved family; do not rewrite it here'),
('T06','A competing offer arrives after you finally like a home','P3','2','Expert answer','Urgency starts deciding the buyer’s limits for them','ig:DbEo59HMjuH','Owned budget/wishlist voice fit; user likes competing-offer topic','Explain the decision Jen helps revisit; outcome depends on actual terms','A grounded conversation with a co-buyer','Offer planning','What does Jen ask before a buyer changes their offer?','Jen reasoning needed'),
('T07','What you wanted to notice on the second visit','P2','2','Expert answer with optional footage','The first visit was about attraction; a specific uncertainty remains','ig:DcwRrZ6NZJI','Permission mechanism only; topic is an adaptation hypothesis','One unresolved observation and what a second look can reveal','Permission to take the next look seriously','Search refinement','What specific concern has made a second visit worthwhile?','Do not recycle rejected Zillow checklist'),
('T08','The first expense after you thought the buying was finished','P1','4','B-roll + substantial caption','Closing feels like the finish line; living there brings another cost','ig:Dax4JjkOdcN','Provider-reviewed blinds surprise; amount belongs to source only','Use Jen’s actual expense or clearly labeled example; explain why it was missed','A warning a friend would appreciate before moving','Readiness planning','What small-looking item surprised Jen or a documented buyer?','True example needed'),
('T09','What the two down-payment choices actually change','P1','3','Comparison carousel','A commenter wants one best answer to 20% versus 3%','tt:7672843729018899743','Buyer question supports topic; salary example supplies numerical structure only','Compare cash retained and payment implications using checked inputs','A decision aid to save and revisit with a lender','Lender planning','What decision belongs to the buyer after lender options are clear?','Fresh lender-supported example needed'),
('T10','The attractive listing that doesn’t fit a normal day','P4','2','Observation-led Reel','A property’s appeal and the buyer’s routine conflict','tt:7668367393843858719','Source demonstrates audible evidence; local fit remains untested','Show the actual condition at the actual property and its limited meaning','A relevant property discussion','Search refinement','What has Jen observed that photographs could not explain?','New observation required; rejected commute drafts excluded'),
('T11','Price reduction versus help with cash needed to close','P1','2','Approved negotiation carousel','Two concessions solve different constraints','CFPB','Approved existing treatment; technical numbers need their own original receipt','Preserve the approved comparison and its calculation support','A negotiation question worth bringing to the team','Offer planning','Which constraint matters in this actual transaction?','Existing approved carousel; no forced Reel conversion'),
('T12','A renovated home and the work still worth asking about','P2','2','Expert answer / carousel','Cosmetic appeal is being mistaken for information about condition','ig:DbbyqA1hxJh','Owned listing context; claim is a proposed investigation, not observed defect','Ask about a specific feature or document; avoid diagnosing from aesthetics','Sharper questions during the next tour','Representation','What does Jen mean by a lipstick remodel in a verifiable example?','Verified example needed'),
('T13','Your good rent changes the buy-now conversation','P1','2','Expert answer','Ownership feels expected even when the existing rental works','SFV','Local discussion provides the situation; no buy/wait financial verdict inferred','Show which circumstances would change the decision, including waiting','A way to discuss timing without shame','Readiness planning','When has Jen helped someone prepare rather than rush?','Jen example needed'),
('T14','The HOA fee and the questions behind it','P2','2','Carousel','A visible monthly fee is being used as a complete comparison','SFV','Local concern; documents and current costs still needed','Compare what is known, what is covered and what remains unresolved','A document-focused checklist with purpose','Property comparison','Which questions does Jen route to HOA documents or a specialist?','Document review needed'),
('T15','After losing an offer, what changed in the search','P3','2','True client story','Buyer hears failure where there may be a next decision','ig:DbEo59HMjuH','Own voice; prior dossier links a North Hills buyer story','Use the documented turning point; no inevitable happy ending promise','Hope with a credible next step','Buyer planning','Can Jen confirm a specific choice that changed after the lost offer?','Story confirmation and permission needed'),
('T16','The program sounds helpful; what is the catch?','P1','3','Expert answer','Viewer distrusts an attractive assistance headline','ig:Dbwh7a1TsA2','Public comment language + search-only program specimen','Explain one verified program’s conditions and tradeoff on a stated date','An informed question instead of borrowed FOMO','Readiness planning','Which program can a lender verify for this actual buyer?','Hold until current program check'),
('T17','A home’s layout during a workday','P4','2','Observation-led carousel','Square footage does not explain how a buyer uses the space','ig:Dak7zeYBTUK','Search-only space-feel specimen; local discussion mentions functional layout','Demonstrate the relevant layout with actual imagery, not an invented client routine','Something a partner can picture','Search refinement','Which ordinary use exposed a layout mismatch on a real tour?','Property and scenario needed'),
('T18','When your income does not fit one neat answer','P1','3','Expert Q&A with lender support','Buyer confuses documentation complexity with impossibility','PRIOR','Existing creative-income hypothesis; not validated by this Reel pool','Prepare the right questions and documents; lender decides eligibility','A lower-friction first professional conversation','Lender introduction','Does Jen repeatedly serve this situation?','Bench; service-fit and technical evidence needed'),
('T19','Before accepting help with the down payment','P3','3','Carousel / expert Q&A','Money help may come with unspoken expectations','PRIOR','Existing family-capital hypothesis, not proven content demand','Separate lender, ownership and family-expectation questions','A practical family conversation','Professional coordination','What experience can Jen share without disclosing private details?','Bench; professional review needed'),
('T20','One place that makes a neighborhood feel like yours','P4','3','Personal/local Reel','Buyer imagines life beyond the property listing','ig:DZY0IBOxhNC','Valley place reference has reach; buyer conversion unknown','One real place, one personal reason, accurate current details','Recognition or a recommendation to someone local','Audience relationship','Which place is actually Jen’s recommendation, and why?','Optional reach experiment'),
]
(OP/'topic-bank.json').write_text(json.dumps([dict(zip(['id','topic','pillar','ring','format','tension','source_key','evidence','payoff','share_save_reason','service','jen_input','status'],t)) for t in topics],ensure_ascii=False,indent=2)+'\n')
text='''# AI topic mining report for Jen

**Prioritize decisions the buyer is already trying to make.** Start with asking again, choosing between imperfect homes, and interpreting the inspection report. Preserve the approved carousels. Keep assistance programs and specialized finance on the bench until their claims and service fit are verified.

## Evidence and ranking method

The 239-record library combines the original 228 records with 11 additional references from the Reel lab. The 158-comment bank supplies audience language, not verified prospect demand. Search-only findings remain candidates. A source’s geographic relevance, review depth, paid status, age and available metrics affect what we can conclude. {{SOURCELEDGER}}

The ranking below is editorial: buyer decision fit first, usable evidence second, Jen’s voice/taste fit third, production feasibility fourth. It is not a statistical score. The top 50 in the appendix is a **curated inspection queue**, not the 50 highest-performing posts on social media.

## Five research tags, three publishing buckets

Tags organize research; the three bullseye buckets organize the publishing mix. They do not compete as separate strategies.

| Research pillar | Buyer’s concern | Evidence strength | Publishing bucket |
|---|---|---|---|
| P1 · Money you can live with | What will this choice leave me carrying? | Multiple public questions; missing Jen conversion data | Home you can live with; occasional recognizable moment |
| P2 · What the home asks of you | What am I taking on besides the purchase? | Local discussion, moving-cost references, existing ICP direction | Home you can live with |
| P3 · Someone on your side | Can I ask, slow down or disagree? | Strong voice/taste match; selected permission and expert references | Question you almost didn’t ask |
| P4 · Life around the home | Does this location and layout fit my life? | Local and observation specimens; no measured local-buyer conversion | Home you can live with; occasional reach |
| P5 · Seeing through the listing | What does that appealing description leave unclear? | Reviewed codewords source + approved carousel treatment | Part of buying you recognize |

The sample is deliberately selected, so raw tag counts do not establish which problem is most common in the market. The full comment triage retains unclassified and low-information rows instead of forcing everything into a buyer pain.

## Twenty ranked topic seeds

The titles below are research labels, not proposed on-screen hooks. Each seed identifies the remaining creative or factual work.

'''
for t in topics:
 id,title,pillar,ring,fmt,tension,source,evidence,payoff,motive,service,question,status=t
 text+=f'### {id} · {title}\n\n**{pillar} · Ring {ring} · {fmt}**\n\n{tension}.\n\n**Source and strength:** {{{{{source}}}}}. {evidence}.\n\n**Payoff:** {payoff}. **Reason to share/save, to test:** {motive}.\n\n**Service connection:** {service}. **Jen’s input:** {question}\n\n**Disposition:** {status}.\n\n'
text+='''## What the radar contributes, and what it cannot settle

The existing Kallaway radar ran on **68 rows with a supplied creator median, a source hook and a topic-candidate label**. It returned 11 automatic pattern groups. No paid tools were invoked. See the [raw run receipt](OP_RADAR).

The adapter passes the reported median through the tool’s generic baseline input; it does not pretend it is an arithmetic mean. Rounded provider displays can produce a recomputed multiple that differs from VidIQ’s stated multiple. The source ledger preserves the reported multiple separately. Most of these rows have no reliable publication date or engagement breakdown, and paid distribution is unknown.

**Editorial interpretation:** these are retrieval candidates, not validated winners. The tool’s “high” confidence means enough fields exist for its calculation; it does not mean the buyer, causal explanation or current trend is validated. No metric from a mixed global fallback was needed because every input had its own supplied baseline. Unknown sponsorship is not evidence of organic reach.

## The trend readout

**Current candidate signal:** a September 1 permission specimen fits the user’s stated taste. **Historical craft reference:** Terra’s November 2024 place story. **Unknown direction:** rising/falling topic demand and view velocity; there are no repeated comparable snapshots here.

Do not manufacture a trend arrow from a large lifetime view count. Refresh a source when its exact claim or recency changes a production decision, not merely to make the bank bigger.

## Top 50 reference inspection queue

Numbers retain the source snapshot’s precision. A high multiple nominates a post for inspection; it does not authorize the hook’s claims or prove a transferable format. Blank dates and multiples remain unavailable. See the linked source and full evidence record before production.

| Queue | Source | Snapshot views | Provider median multiple | Evidence available | Role |
|---:|---|---:|---:|---|---|
'''
for i,s in enumerate(json.loads((OP/'reference-top-50.json').read_text()),1):
 text+=f'| {i} | [{s["creator"]} · {s["source_id"]}]({s["url"]}) | {s.get("views","Unavailable"):,} | {str(s.get("outlier")) + "×" if s.get("outlier") else "Unavailable"} | {s["review"]} | {s["editorial_use"]} |\n'
text+='\n**Reject as claims:** universal affordability from salary alone; “free” assistance without conditions; inevitable refinancing; a low-down-payment teaser standing in for the ongoing budget. **Hold as craft only:** compelling examples from unrelated niches. **Preserve:** the useful question or presentation where it can survive factual correction.\n\nContinue with {{5}} and {{6}}, then use {{7}} as the production handoff.\n'
text=text.replace('OP_RADAR','<'+str(OP/'radar-raw/run-receipt.md')+'>');doc(4,text)

doc(5,'''# Hook and messaging library

**The source-to-draft gap is a change in the human situation.** The preferred reference lets a buyer reveal a small embarrassment and gives the agent enough room to answer warmly. Earlier drafts compressed that exchange into advice. The information survived; the relationship disappeared.

That is a diagnosis of this conversation’s revisions, not proof of a universal engagement mechanism.

## The calibration we should preserve

The source puts a buyer’s hesitant question beside the amount they are about to spend. The user’s preferred treatment is:

> “Sorry, one more question.”
>
> “You’re buying an $800K house? You can ask me whatever you need.”

**Status:** user-chosen cadence reference. It is not a claim that every Jen buyer has that budget or that the adaptation has performed on Instagram.

The first line is something a person could hear themselves saying. The second sounds like a response to that person. The amount gives the reassurance a reason. The sentence lasts long enough for the warmth to land. A caption can then show the help the buyer is allowed to ask for. Source: {{ig:DcwRrZ6NZJI}}. Jen’s own protective phrasing supports the stance. {{VOICE}}

Do not reduce this to “embarrassment + number + reassurance” for every post. A comic translation, a revealing comparison and an expert answer work differently.

## Ten source hooks to study

Source text is retained as research evidence, not recommended copy or verified financial advice. Transcriptions come from saved provider analyses/search results unless otherwise noted. Ellipses mark excerpts.

| Source opening / excerpt | Source and evidence | Useful construction | Restriction |
|---|---|---|---|
| “I know this is probably a stupid question…” | Karime, saved video/caption analysis | An admission the buyer recognizes | Preserve dignity; pet-name delivery is not required |
| “Before you unpack a single box, do these 10 things.” | Rachael, saved video analysis | A familiar milestone followed by unfinished practical value | Full list unavailable; cannot say its caption was good |
| “Don’t cook your first meal after moving in…” | Nate, saved video analysis; excerpt | Specific next action instead of a general warning | Full caption unavailable; do not inherit an unverified consequence |
| “What are the steps to buying a house?” | Logan, provider-transcribed spoken question | An ordinary question invites an ordinary answer | Transfer delivery, verify local transaction details |
| “Before you make an offer: drive the neighborhood at 7 AM, 3 PM, and 9 PM.” | Carli, reviewed-source bank | Action and timing make the task imaginable | Not proof that these exact times are right for everyone |
| “POV you finally bought your first home and just realized whole house blinds are $4,275” | Thatmortgageguy, reviewed-source bank | Celebration meets one surprisingly concrete expense | The price belongs to that source, not Jen’s example |
| “Realtor code words Pt. 2” | Battlebornsteve, reviewed-source bank | A recognizable recurring series promises translation | The actual translations must be accurate and fair |
| “What is the worst thing someone can do before buying a house?” | Khrissellstampa, search-only | A clear question gives an expert something to answer | Search result is not a fully studied script |
| “HOW MUCH DO YOU NEED TO MAKE TO AFFORD A $465,000 HOME?” | Realmortgagementor, search-only | Specific input makes the promised output obvious | Salary alone cannot settle affordability |
| “Why do some homes feel CROWDED no matter how big they are?” | Tinasellsoc, search-only | Recognizable mismatch invites a visible explanation | Needs full source inspection before close translation |

References: {{ig:DcwRrZ6NZJI}} · {{ig:DaTREfOhA3C}} · {{ig:DaF9sXJAY6p}} · {{tt:7663981949198929183}} · {{ig:DZqhDCfhc75}} · {{ig:Dax4JjkOdcN}} · {{ig:DceVX_-qheI}} · {{ig:Db6xbxqgpfn}} · {{tt:7672843729018899743}} · {{ig:Dak7zeYBTUK}}.

## Pattern families and the strength of the evidence

| Family | Specimens in this interpreted group | Pattern worth testing | Evidence limit |
|---|---|---|---|
| Permission after a hesitant question | Karime: 1 | Recognition → a complete protective reply → practical continuation | Strongest taste match; insufficient examples to claim a validated cluster |
| Milestone before a missed task or expense | Rachael, Nate, Thatmortgageguy: 3 | Familiar moment → specific unresolved detail | Three descriptive specimens; caption access incomplete; no causal validation |
| Plain question, spoken answer | Logan, Khrissellstampa: 2 | Someone asks what the viewer wants to know → expert answers | Second specimen is search-only; not a matched experiment |
| Concrete comparison or worked amount | Two Trips comparators plus Realmortgagementor: 3 | Present the actual choice → show reasoning → reach an answer | Different subjects and presentation; one comparison has lower reach but higher like rate |
| Visible condition resolves a concern | Christianatherealtor, Carli: 2 | Name the concern → let observation supply evidence | Different actions; no basis for a universal neighborhood rule |
| Comic listing translation | Battlebornsteve: 1 studied specimen here | Attractive phrase → recognizable interpretation → earned laugh | User approved the carousel adaptation; source count is thin for format generalization |

These hand-reviewed families are more useful than treating the radar’s 11 keyword groups as an editorial verdict. Family names describe construction, not a psychological guarantee.

## Higher reach does not automatically mean better content

**Nate comparison:** the same-date first-meal post had 85,143 plays; the broader house-poor warning had 2,169. The roughly 39.3× difference is worth examining. Different topics, visuals, audio and unknown distribution prevent a causal conclusion. Missing captions prevent a full payoff comparison. {{BENCHMARKS}}

**Trips comparison:** the worked example had 12,186 plays, 229 likes and 23 comments. The broader reassurance piece had 3,594 plays, 96 likes and three comments. The latter had about 26.7 likes per 1,000 plays versus 18.8. Lower reach therefore did not mean lower response on every visible measure. Neither ratio establishes buyer quality. {{BENCHMARKS}}

**Decision for Jen:** use specificity to make a concern visible; use observed responses to decide whether it resonates. Do not turn “specificity” into stuffing every opening with numbers.

## Message map for the three core buckets

| Bucket | What the reader should feel | What the caption or script must add | Avoid |
|---|---|---|---|
| Home you can live with | My hesitation is about a real tradeoff | A comparison, observation or question that improves the decision | Generic caution with no example |
| Question you almost didn’t ask | I can ask this without being talked down to | The kind of help Jen will give, illustrated concretely | Orders, credential claims or a pasted reassurance slogan |
| Part of buying you recognize | Someone understands the little absurdities of this process | A comic reveal, useful detail or recognizable continuation | Random relationship humor and a bolted-on real-estate CTA |

## Working prompt for the next writer

> Read the selected brief, the linked source’s opening and payoff evidence, Jen’s voice profile, and the current taste decisions. First identify the recognizable situation and the specific remaining benefit. Write three materially different treatments for the chosen format. Preserve the full human reply when it matters. Use a source’s construction without copying its story, financial claims or mannerisms. Keep any missing Jen experience explicit. For each treatment, show what the viewer gets on screen and what they still gain from the caption. Compare against the chosen reference for clarity, recognition, warmth and payoff. Reject generic advice, fake conversations and invented client facts. Deliver the strongest treatment and the reason for choosing it; do not label self-review as audience proof.

This is a local handoff prompt, not a newly installed skill or mandatory formula. For the first attempt, use brief B01 or B03 in {{7}}.
''')

doc(6,'''# Jen’s format playbook

**Keep the approved carousel. Test two Reel forms: an ordinary question answered by Jen, and a recognizable on-screen moment carried by her own B-roll and a useful caption.**

A topic becomes a Reel only when the Reel adds something. The negotiation comparison does not need a video counterpart to be a good content asset.

## Structures: how the idea unfolds

| Structure | What it does | Opening example, described rather than scripted | Evidence |
|---|---|---|---|
| Comparison that leads to a decision | Uses the same criteria to weigh two choices | Two home photos establish the choice; the next slide shows the first consequential difference | User-approved negotiation carousel; Trips demonstrates visible reasoning |
| A hesitant question gets a real reply | Turns an awkward admission into welcome and useful help | Buyer’s question appears over Jen’s footage; her full answer follows, with room to read both | Karime and user-selected cadence |
| An ordinary question becomes an expert explanation | Lets competence show in the answer | Off-camera question while Jen finishes an ordinary action; she turns and answers | Logan’s refrigerator opening |
| A milestone reveals unfinished work | Makes a specific next step worth reading about | Moving-in footage establishes the moment; one unresolved expense or task appears | Rachael, Nate and the blinds-cost source |
| Comic translation | Reveals the gap between polished listing language and a recognizable interpretation | A listing phrase establishes expectation; a photo and a fair comic translation supply the reveal | Battlebornsteve and the approved carousel |
| Observation answers the question | Shows what an explanation alone cannot establish | A question about noise appears; a recording of the actual condition follows | Christianatherealtor’s viewer-question response |

References: {{ig:DcyMJKJohSq}} · {{ig:DcwRrZ6NZJI}} · {{tt:7663981949198929183}} · {{ig:DaTREfOhA3C}} · {{ig:DaF9sXJAY6p}} · {{ig:Dax4JjkOdcN}} · {{ig:DceVX_-qheI}} · {{tt:7668367393843858719}}.

## Layouts: what Jen has to make

| Layout | What the viewer sees | Production requirement | Estimated Jen effort, untested |
|---|---|---|---|
| Approved six-slide photo carousel | Existing real-photo hierarchy, legible serif and restrained color treatment | Team prepares copy and assembles approved design; Jen checks property truth | Aim for 5–10 minutes of review when all inputs exist |
| Reused B-roll + readable text | One ordinary clip or short sequence of Jen; text carries the opening | Jen chooses existing footage and cover; team supplies overlays and full caption | Aim for 5–10 minutes of selection/editing; editing skill affects time |
| Casual expert answer | Jen speaking naturally, optionally to an off-camera questioner | One quiet location, phone and usable audio; team supplies prompt, talking points and optional script | A short filming session; 5–10 minutes is a target, not a guarantee |
| Prop or paper demonstration | One object makes a numerical choice visible | Verified worked example plus simple prop; more preparation than ordinary talking | Longer if numbers or staging are not ready; optional only |
| Actual-condition footage | The property or route provides evidence | Access, accurate context, safe recording and privacy-conscious framing | Access-dependent; do not budget as effortless B-roll |

## Structure × layout selection

**Preferred** = recommended for this job. **Possible** = choose only if it helps. **Poor fit** = likely to lose the idea’s value, not a permanent prohibition.

| Structure | Six-slide photos | B-roll + caption | Casual answer | Prop demonstration | Actual-condition footage |
|---|---|---|---|---|---|
| Comparison | Preferred | Poor fit for detailed math | Possible | Possible | Possible for spatial differences |
| Hesitant question / reply | Possible | Preferred | Possible | Poor fit | Possible |
| Expert explanation | Possible | Poor fit when reasoning is the value | Preferred | Possible | Possible |
| Milestone / missed detail | Possible | Preferred | Possible | Possible | Possible |
| Comic translation | Preferred | Possible | Possible | Poor fit | Possible |
| Observation as answer | Possible | Possible | Possible | Poor fit | Preferred |

An empty or weak cell is not proof that nobody else uses that pairing. This is a production-fit judgment drawn from the inspected specimens and Jen’s constraints.

## Three production recipes

### F01 · Approved photographic carousel

**Best for:** T02, T05, T09, T11 and T14. **Structure:** recognizable choice or phrase → distinct reveals/comparison dimensions → useful final implication. Use all six slides only when each advances the idea. The approved visual reference and current codewords/negotiation packages are the anchors. {{DIRECTION}}

**Team supplies:** final slide copy, caption, source notes and the assembled approved layout. **Jen supplies:** property confirmation, personal corrections and imagery where needed. **Failure mode:** turning a comic reveal into a compliance checklist, or filling slides with general instructions. **Review:** can a reader state the useful comparison or joke without the caption explaining the entire carousel?

### F02 · Question-led expert answer

**Best for:** T03, T06, T13 and conditionally T16. **Structure:** actual question → Jen’s first useful answer → two or three reasoning beats → clear implication. The opening must earn the explanation; no fixed 30- or 60-second requirement.

**Team supplies:** the question, optional first line, key reasoning points, checked example and a separate caption that complements the spoken answer. **Jen supplies:** her actual judgment and delivery. A phone and clear audio are sufficient for the intended test. **Model:** {{tt:7663981949198929183}}; use Trips when a worked comparison benefits from a visible object. **Failure mode:** a textbook answer narrated over an incidental task. **Review:** if the footage disappeared, would the answer still help the buyer with one specific concern?

### F03 · Recognition-led B-roll with caption continuation

**Best for:** T01 and a truthful version of T08. **Structure:** familiar buyer moment → a complete response or pointed unresolved detail → caption delivers the practical continuation. The caption does not have to be long; it has to justify opening it.

**Team supplies:** the on-screen sequence, suggested reading holds, complete caption and optional invitation. **Jen supplies:** her own footage and cover. Read the overlay aloud at her natural pace, then allow a viewer to read without rushing; do not set a universal duration from one reference. **Model:** {{ig:DcwRrZ6NZJI}}; Rachael is a second model for caption dependence, with the explicit limit that her full caption was unavailable. **Failure mode:** giving orders, compressing a human reply into a slogan, or withholding everything behind a vague “read below.” **Review:** identify both the emotional value already delivered and the specific additional value waiting in the caption.

## What stays out of the production defaults

No generated Reel covers, generic luxury stock aesthetic, envelope props, stamped diagrams, obligatory keyword CTA or identical cross-format versions. These are current user constraints, not a claim that those devices never work elsewhere.

Choose two Reel experiments beside the approved carousel work. After two or three comparable batches, examine retention where available, responses from relevant buyers, consultations and Jen’s production burden. The current evidence does not crown a winning Reel format for her. {{8}}
''')

links.update({'DFA':'https://www.calhfa.ca.gov/dream/index.htm','REGRET':'https://www.reddit.com/r/LosAngelesRealEstate/comments/1vxqmex/whats_the_biggest_mistake_you_made_buying_your/','FANNIE':'https://singlefamily.fanniemae.com/media/document/pdf/lender-letter-ll-2026-03-updates-project-standards-property-insurance-requirements','FANNIEGUIDE':'https://selling-guide.fanniemae.com/sel/b4-2.1-01/general-information-project-standards','INSURANCE':'https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm','CAR':'https://www.car.org/aboutus/mediacenter/newsreleases/2026releases/July2026HomeSales'})

doc(7,'''# Creative brief bank: seven pieces with a reason to exist

**First production choice:** B03, the inspection explanation, or B02, the condo-versus-house carousel. B01 preserves the preferred B-roll treatment. B07 adds a timely condo-financing question discovered during the current-source research.

These are finished research and production briefs, not seven approved posts. Jen’s unrecorded experiences, enthusiasm scores and personal reactions remain hers to supply. The team can prepare everything around those inputs; it cannot invent them.

## B01 · The question you almost didn’t ask

**Audience / job:** Ring 2 buyer who wants another explanation; make the first conversation feel welcome. **Format:** F03, Jen’s B-roll plus complete caption. **Source:** Karime’s question/permission post and the user’s chosen cadence. {{ig:DcwRrZ6NZJI}}

**Opening anchor:** “Sorry, one more question.” / “You’re buying an $800K house? You can ask me whatever you need.” Preserve this as the comparison standard, not a line to sharpen into a slogan.

**Caption’s remaining job:** demonstrate what the buyer may ask Jen to clarify. Work through one real repeat question: what was confusing, how Jen explained it, and what became easier to decide. End when the question is genuinely resolved; a short invitation is optional.

**Reason someone might send it:** reassurance for the partner who keeps apologizing. This is a sharing hypothesis, not measured share behavior.

**Jen’s small input:** choose an actual question she repeats willingly and give her ordinary explanation. If unavailable, write an explicitly hypothetical example without claiming a client conversation.

**Team handoff:** two readable overlay beats, full caption, optional invitation, no cover design. **Review:** the reply must sound addressed to the hesitant person; the caption must add more than “ask questions.”

## B02 · The nice condo and the house with a to-do list

**Audience / job:** Ring 1 reference buyer, delivered to Ring 2; make a difficult comparison discussable. **Format:** F01 six-slide carousel. **Evidence:** current local tradeoff discussion; existing ICP research. {{SFV}}

**Creative premise:** Both options may be reasonable. The useful question is what each asks of the buyer after they move in. This is not a carousel declaring condos or houses the winner.

**Slide plan:** (1) two concrete options; (2) what the condo gives and asks; (3) what the house gives and asks; (4) one easy-to-miss difference established by evidence; (5) what changes the decision for this buyer; (6) the question to bring to a comparison conversation. Use matched criteria and the approved photographic hierarchy.

**Substance needed:** two real, permitted examples or clearly hypothetical cases; current property inputs; a verified observation about condition, ongoing obligations or practical use. No invented repair estimate.

**Reason to save/send:** a co-buyer can point to the compromise they are actually worried about. **Jen’s small input:** the difference she would discuss first and why. **Team handoff:** final slide copy, caption and a one-page source note. **Review:** every middle slide must make the choice clearer, not simply add another caution.

## B03 · The report arrived and now the house feels different

**Audience / job:** Ring 2 buyer in the inspection period; display Jen’s judgment through a real explanation. **Format:** F02 question-led expert answer. **Evidence:** the user likes this topic; new LA social listening includes inspection distrust and unexpected repair work. The thread was opened during this run; its indexed August 2026 date conflicts with relative page timestamps, so its exact publication day remains unconfirmed. {{REGRET}}

**Creative premise:** The tour and the report create different pictures of the same house. Jen helps the buyer understand the question that needs answering next.

**Reasoning beats:** acknowledge the change in feeling; distinguish a finding from its interpretation; show one example of the next question and the professional who can answer it; explain how the answer affects the decision. Do not classify an unseen issue as minor or promise the report is nothing to worry about.

**Opening preparation:** ask Jen the exact question a worried buyer would ask after receiving a report. Let her first spoken answer set the script’s cadence. The casual delivery reference is Logan, not a demand for his wording or transaction sequence. {{tt:7663981949198929183}}

**Caption’s job:** give the viewer a compact recap of what to discuss with their own team; do not duplicate a long script verbatim unless accessibility or deployment needs justify it.

**Jen’s small input:** one anonymized, confirmed example and what she said. **Team handoff:** opening question, three talking points, optional script after that input, caption and factual source note. **Review:** a buyer should understand one next distinction, and Jen should sound capable without sounding dismissive.

## B04 · The offer pressure and the number you already chose

**Audience / job:** Ring 2 buyer facing a competing offer; preserve decision ownership while explaining negotiation judgment. **Format:** F02 expert answer. **Evidence:** user-approved topic direction, Jen’s budget/wishlist voice, and the current LA discussion’s demand for an advocate. {{ig:DbEo59HMjuH}} · {{REGRET}}

**Creative premise:** A competing offer is new information. It does not tell the buyer which compromise is acceptable to them.

**Reasoning beats:** what changed; which previously agreed limits deserve revisiting; what Jen can clarify about the available options; how the buyer makes the decision with those facts. Avoid pretending the team knows another buyer’s confidential terms.

**Payoff:** a way to think during pressure, not a slogan about never overpaying. **Reason to send:** two buyers can use the video to restart their own conversation.

**Jen’s input:** what she actually asks before a buyer changes an offer. **Team handoff:** question-led script/talking points, caption and one explicit example. **Review:** the answer should reveal judgment; simply repeating “stick to your budget” fails.

## B05 · The listing translator

**Audience / job:** Ring 4 reach with local relevance; make the buyer laugh and notice more. **Format:** the already approved codewords carousel. **Evidence:** user’s 8/10 approval and the reviewed source. {{DIRECTION}} · {{ig:DceVX_-qheI}}

**Action:** reuse the approved package as the benchmark in the first comparison set. This brief does not authorize rewriting it.

**Expansion condition:** a new edition needs genuinely different, fair translations. Keep the comic reveal intact. Do not turn a subjective phrase into an accusation that a property has a defect, that a seller is hiding something or that a neighborhood is unsuitable for a protected group.

**Reason to send:** the recipient recognizes the phrase from their own saved listings. **Team handoff:** the preserved approved asset, its existing caption, and a clear version label. **Review:** compare any extension to that asset, not to the rejected drafts.

## B06 · The repair money that never reached the kitchen

**Audience / job:** Ring 2 tradeoff buyer; make the gap between buying a fixer and renovating it visible. **Format:** expert answer or comparison carousel. Use B-roll only if a truthful example supplies a complete caption payoff.

**Evidence:** a newly inspected LA discussion contains the phrase “no money left for new floors, kitchen reno, bathroom reno, etc.” The commenter reports spending on other work first. This is a person’s account, not a verified cost estimate or a representative result. {{REGRET}}

**Creative premise:** The intended renovation and the work the home needs may compete for the same money. Let the buyer picture the result they wanted, then show the verified question that comes before pricing that result.

**Payoff:** identify the next estimate or assessment required before treating the home as a manageable project. **Reason to save:** the buyer is actively deciding how much work they can take on.

**Jen’s small input:** a real instance where priorities changed, or an explicitly hypothetical case she considers realistic. **Team handoff:** source excerpt, chosen example, progression, caption and factual review notes. **Review:** no invented roof/HVAC prices; no suggestion that every older home is a financial trap.

## B07 · You like the condo; has the lender reviewed the building?

**Audience / job:** Ring 2 condo buyer; connect an appealing unit to the separate project-review question. **Format:** six-slide carousel first, or an expert answer with a lender-confirmed example. **Current evidence:** Fannie Mae’s March 18, 2026 letter and August 5 guide update. {{FANNIE}} · {{FANNIEGUIDE}}

**Research finding:** the Limited Review process was retired for applications dated August 3, 2026 onward. Full Review or an applicable waiver must be considered. The 15% reserve-allocation requirement is a separate change effective January 4, 2027 for Full Review applications; do not present that future requirement as already universal. Waiver conditions and lender requirements matter.

**Creative premise:** The buyer and the building present different questions. An attractive unit and a personal preapproval do not, by themselves, settle the project’s eligibility.

**Sequence:** establish the buyer’s recognizable assumption; separate buyer approval from building review; explain what Jen asks the lender to confirm; name the current/future timing only where it helps; conclude with the useful question to ask about the actual property.

**Jen’s small input:** how she introduces this issue without overwhelming a buyer. **Team handoff:** source-linked carousel brief, verified dates, lender-review question and caption. **Review:** no claim that all condos became unfinanceable, that every HOA must raise dues, or that this requirement is a blanket California law. This is a timely research-backed candidate, not a demonstrated viral topic.

## Production order and remaining human reaction

| Order | Brief | What is ready | What only Jen can supply |
|---:|---|---|---|
| 1 | B02 or B03 | Audience, evidence, structure, payoff and handoff | The actual comparison or inspection explanation |
| 2 | B01 | Preferred cadence and caption assignment | One natural example of the help she provides |
| 3 | B05 | Existing approved package | Optional final deployment review |
| 4 | B04 | Expert-answer brief | Actual negotiation judgment |
| 5 | B06 | Newly sourced buyer concern and creative premise | A truthful example |
| 6 | B07 | Current source and scoped explanation | Lender confirmation for a property-specific example |

This order is based on readiness and fit, not an invented enthusiasm score. Jen’s creative reaction remains pending. The research sprint is complete; a fabricated “only Jen could say this” story would weaken the package.

**Series connections:** B01 introduces permission; B03 demonstrates it. B02 establishes the choice; B06 makes one tradeoff tangible. B07 adds a current condo-specific consideration. B04 carries the same decision ownership into an offer. B05 keeps the account capable of being funny and useful.
''')

doc(8,'''# Jen’s content blueprint

**Build the library around a buyer’s real decision.** Jen’s advantage to test is her ability to make the tradeoff understandable and the question welcome. The approved carousel handles comparisons and comic reveals. Expert Reels show her judgment. B-roll carries recognition when the caption has something worth opening.

This package completes the research and strategy handoff. It does not claim that Jen’s new Reels are proven, that all sources were published in 2026, or that competitor views predict leads.

## The eight documents and the decisions they settle

| Document | Decision it supports |
|---|---|
| {{1}} · Niche and positioning | Who Jen speaks to and what she can credibly promise |
| {{2}} · Audience bullseye | How to widen reach without losing the buyer; starting trio and bench |
| {{3}} · Positioning opportunity map | Who to study, what to borrow and what advantage still needs proof |
| {{4}} · AI topic mining | Twenty core seeds, current-source additions and a 50-reference inspection queue |
| {{5}} · Hook and messaging library | Why the preferred treatment works as writing; source families and reusable brief prompt |
| {{6}} · Format playbook | Which topics belong in carousels, expert answers or caption-led B-roll |
| {{7}} · Creative brief bank | Seven source-linked briefs that production can actually use |
| This blueprint | Ownership, first batch, measurement and repeatable handoff |

## The decision from the fresh 2026 check

The current-source addendum in Document 4 changes the priorities: bring inspection/repair judgment forward; give condo project review its own brief; replace program-application hype with accurate current-status guidance. Source freshness is recorded separately from the date we retrieved it.

The current research supports useful questions and topical accuracy. It does not establish current social-format winners. The selected Reel comparisons remain dated snapshots with incomplete distribution, engagement and publication information.

## First seven-piece batch

This is a proposed order across roughly two weeks, subject to Jen’s capacity. No posts are scheduled or published by this package.

| Slot | Bucket | Piece | Format | What we want to learn |
|---:|---|---|---|---|
| 1 | Home you can live with | B02 condo versus older house | Approved carousel form | Does a real comparison produce relevant buyer questions? |
| 2 | Question you almost didn’t ask | B01 asking again | B-roll + caption | Does the preferred cadence survive adaptation and invite a question? |
| 3 | Part of buying you recognize | B05 approved listing translator | Carousel | Preserve an approved creative benchmark |
| 4 | Question you almost didn’t ask | B03 inspection concern | Expert answer | Does Jen’s explanation feel natural and demonstrate judgment? |
| 5 | Home you can live with | B06 repair priorities | Expert answer or carousel | Does the concrete consequence strengthen recognition? |
| 6 | Part of buying you recognize | T08 truthful moving-in surprise | B-roll only if the story fits | Can another premise work without repeating B01’s construction? |
| 7 | Experiment | B07 condo project review | Carousel | Can a current, consequential change become clear buyer-facing content? |

The existing negotiation carousel remains available; no forced Reel counterpart. B04 competing-offer explanation is the first expert-video reserve. If a real example is unavailable for a slot, use the reserve rather than inventing a client story.

## Roles without adding unnecessary agents

| Phase | Codex / production work | Farrice / Jen contribution | Finished output |
|---|---|---|---|
| Research | Retrieve, date, classify, compare and source claims | Direction and source taste when it changes selection | Evidence bank and decision brief |
| Ideation | Present the real tension, format choice and proposed payoff | Jen’s actual take; Farrice’s taste judgment | A selected creative brief |
| Drafting | Prepare alternatives, caption and optional script | Small corrections to voice and substance | Near-finished copy package |
| Review | Check factual scope, recognition, payoff and source transfer | Decide whether it sounds like Jen and lands | Approved version, clearly labeled |
| Production | Assemble approved carousels; supply minimal filming instructions | Jen supplies footage, covers and performance | Ready-to-post asset |
| Learning | Compare actual analytics and attributable responses | Identify relevant conversations and production burden | Keep/refine/replace decision |

No new agents, paid calls, external writes or publishing occurred. The user’s 95%-done goal is the target of the handoff, not a measured completion percentage for an unfilmed Reel.

## The repeatable handoff

Every production packet needs only the material that can change the draft:

1. **Audience moment:** one sentence, with the buyer’s source language when available.
2. **Chosen source:** opening plus actual payoff evidence; identify missing caption/transcript access.
3. **Jen’s take:** her words or a clearly marked missing input. Never an invented experience.
4. **Format and progression:** what happens on screen, what gets explained and what the caption adds.
5. **Claim support:** source, date, scope and any example inputs requiring confirmation.
6. **Delivery:** overlay text, caption, optional talking points/script and minimal filming note. Jen’s imagery remains hers.
7. **Decision record:** approved reference, rejected treatment boundaries and why the selected draft is stronger.

**Copy-ready production prompt:**

> Use brief [B-number] from this package. Read its named source, the current Jen voice profile and the user’s approved/rejected examples. Identify what makes the reference recognizable and what the viewer still wants after its opening. Draft for the selected format only. Give the strongest treatment enough room to sound like a person. Preserve factual conditions and label missing lived experience. Review and refine once against recognition, warmth, clarity, useful payoff and production ease. Deliver the caption, overlays and optional script/talking points as applicable, with source notes kept out of the social copy. Do not redesign the approved carousel, generate Reel covers or call the draft proven.

## Measurement that can change the next batch

Record each post’s format, topic, source family, publication date, paid/organic status and comparable age at review. Keep platform measures separate: plays, reach, retention, saves, public reposts, private shares and comments are not interchangeable.

For buyer response, record only what the person actually provides: their question, relevant location if known, purchase situation if volunteered, and whether a consultation or next step occurred. No inferred income or invented buyer qualification. A keyword comment alone is a resource request, not a qualified lead.

| Result after comparable exposure | Meaning | Next move |
|---|---|---|
| Views plus unrelated reactions | Reach without established buyer fit | Re-aim the situation before scaling |
| Saves or shares, no identifiable buyer conversations | Possible utility or resonance | Keep provisional; inspect whether the invitation and service connection fit |
| Specific local buyer questions | Stronger evidence of audience fit | Develop the same problem through a different useful angle |
| Consultation or representation linked to the post | Commercial evidence | Record the event and how attribution was established |
| Jen cannot finish it with small edits | Handoff or voice problem | Fix the brief/source transfer before adding topics |

Do not retire a topic on a 24-hour result. Review two or three batches at comparable post ages, with enough distribution to interpret. The bullseye’s inquiry thresholds are proposed learning criteria; low exposure or missing tracking makes the result inconclusive. Dollar value remains unknown until actual economics and attribution are supplied.

**Current tracker:** research batch complete; publication not performed; attributable inquiries not measured; consultations/revenue not measured. These are not zero-performance results.

## A practical 90-day sequence

| Period | Work | Decision at the end |
|---|---|---|
| Days 1–14 | Produce a small selected set from the first batch; retain approved carousel reference | Can Jen finish the packets easily, and which Reel delivery feels natural? |
| Days 15–42 | Repeat the strongest buyer problems through two or three comparable batches | Keep/refine/replace formats using buyer response and production burden |
| Days 43–70 | Increase useful repetitions; refresh claims and recent source examples where they affect a decision | Which two or three problems repeatedly attract the right conversations? |
| Days 71–90 | Consolidate the strongest series and prepare the matched resource most often requested | Which content-to-service path deserves expansion? |

Do not prewrite 90 days before learning from the first usable Reel set.

## Resource opportunities, ranked

**First: a two-home comparison sheet.** It directly supports the chosen audience and B02; useful only if it helps compare actual choices. **Second: an inspection follow-up question sheet.** Develop after B03 reveals the questions buyers ask; avoid pretending it replaces a professional review. **Third: a dated condo-purchase document guide.** Connect B07 to current lender questions and official links. These are resource briefs, not claims that new lead magnets or automated replies were built in this run.

## Maintain the evidence without turning research into busywork

Before any financial/program post, check the exact official source and date. For a claimed current format trend, require recent publication dates and comparable repeated observations; otherwise call it a reference. Revisit the creator list monthly when active production justifies it. Revisit the ICP when the actual questions change, not on an arbitrary date.

Use saved VidIQ material first. Any new paid mining requires a separately authorized cap in the active conversation. A 50-reference bank is already sufficient to start; deeper study of a few complete examples is more valuable than another 200 search snippets.

**Locked:** approved carousel direction and Jen’s ownership of Reel imagery. **Recommended:** Valley tradeoff buyer, the three-bucket mix and the two Reel forms. **Still to prove:** Jen’s distinctive take, current-format performance and attributable buyer response. **Next action:** take B02 or B03 into a small production comparison using this package.
''')
