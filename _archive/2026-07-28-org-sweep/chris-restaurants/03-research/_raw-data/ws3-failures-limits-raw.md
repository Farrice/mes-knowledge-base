# Report: Documented Failures and Operational Limits of Commercial AI Systems in Restaurants (2024–2026)

Executive summary
- Across 2024–2026, multiple high-profile pilots and commercial deployments of AI in restaurants revealed recurring operational limits: speech-recognition and conversational failures in drive-thru voice systems; overstated “autonomy” claims by vendors; cost/scale/maintenance problems for kitchen robotics; slower-than-marketed rollouts for automated kitchens; POS data‑quality burdens on independent operators; legacy POS integration frictions; discrete legal and reputation problems from AI hiring and AI‑generated marketing. Evidence is drawn from contemporaneous reporting, company statements, SEC proceedings, vendor materials, trade press, and documented social‑media incidents cited below.

## 1) McDonald’s — IBM Automated Order Taker (AOT) pilot ending (June 2024)

Annotated citations (source, date/period, direct extract or figure)
- NRN: “McDonald’s AI‑driven Automated Order Taker (AOT) test at the drive‑thru, in partnership with IBM, is ending after two and a half years … The AOT technology was installed at approximately 100 locations before being discontinued.” [1]  
- CNBC (17 Jun 2024): “The AOT test was conducted in more than 100 McDonald’s restaurants … The system’s accuracy remained in the low‑to‑mid 80% range, below the ~95% threshold needed for viability” and franchisees “complained that the AI struggled with different accents and dialects.” [2]  
- BBC: reporting that the experiment generated “viral videos in 2023 showing order errors such as bacon added to ice cream and hundreds of dollars worth of chicken nuggets.” [3]  
- Restaurant Online (UK): documented TikTok video showing a customer ordering vanilla ice cream and water but receiving multiple ice‑cream scoops, ketchup packets, and butter packets. [4]  
- Business Insider: McDonald’s CEO said in June 2021 that the voice‑recognition technology was “about 85% accurate, with humans assisting roughly one in five orders”; viral social postings captured extreme misorders (e.g., excessive nuggets). [6]  
- LinkedIn social clip: a circulated video reportedly showing the AI mistakenly adding “260 chicken nuggets” to an order (social evidence entry). [5]

Synthesis — what malfunctioned and how
- Scope and outcome: McDonald’s pilot (≈100 locations) with IBM’s AOT was terminated and technology removed from test sites by end of July 2024 after persistent operational shortcomings and social‑media backlash [1], [2], [3], [4].  
- Observable failure modes from the public record and social clips: gross misinterpretation of spoken input leading to massively incorrect item quantities (e.g., “260 chicken nuggets”), unexpected additions (bacon added to ice cream), and multi‑item noise/misrouting when cross‑talk occurred in adjacent drive‑thru lanes [3], [4], [5], [6].  
- Technical/UX failure categories supported by the evidence:
  - Speech‑recognition accuracy too low for unattended use: reported accuracy in the “low‑to‑mid 80%” range vs. an implied commercial viability threshold ≈95% [2], [6].  
  - Accent/dialect sensitivity: franchisee complaints that the system “struggled with different accents and dialects” reduced order accuracy [2].  
  - Background noise and cross‑talk vulnerability: cross‑talk from neighboring lanes triggered large, incorrect additions (e.g., nine sweet teas) in social videos and reporting [4], [6].  
  - Edge cases and special requests: social videos show failures handling unusual or brief utterances (e.g., “vanilla ice cream and water” being interpreted as multiple items) [4], [3].  
  - Human‑handoff and intervention model limits: historical comment that humans assisted “roughly one in five orders” aligns with capacity gaps when confidence thresholds fell [6].  
  - Operational and cost considerations: analysts and reporting referenced high operating costs and the pilot’s inability to scale given accuracy and crew concerns [2], [1].

Lessons generalized for drive‑thru voice AI (supported by citations)
- Commercial viability requires substantially higher end‑to‑end accuracy than many pilots achieved; public reporting cites low‑to‑mid 80% accuracy as insufficient [2].  
- Robustness to accents/dialects, ambient noise, and lane cross‑talk is essential; failure to handle these leads to both incorrect orders and viral reputational damage [2], [3], [4].  
- Edge cases / special requests remain hard to model reliably; social clips demonstrate surprising, high‑cost misinterpretations [3], [4], [5].  
- Pilot metrics that rely on human fallback can mask real customer experience and back‑of‑house burden; public figures describing human assistance rates (≈20%) indicate significant human‑in‑the‑loop support during pilots [6].

Reliability assessment
- High reliability: company and trade disclosures on pilot scope and termination [1], [2], [6].  
- Corroborated social‑media incidents (TikTok/LinkedIn) are described in mainstream outlets (BBC, Restaurant Online), which increases confidence; however, social clips themselves are not full transcripts and can lack context [3], [4], [5].  
- Where specific accuracy percentages are reported (≈85% / low‑to‑mid 80%), these come from corporate comment and reporting rather than independently audited field studies and should be treated as operational indicators rather than definitive validated metrics [6], [2].

Primary evidence excerpts (verbatim as reported)
- “The AI test generated viral videos in 2023 showing order errors such as bacon added to ice cream and hundreds of dollars worth of chicken nuggets.” — BBC reporting [3].  
- “A TikTok video showed a customer ordering vanilla ice cream and water but receiving multiple ice‑cream scoops, ketchup packets, and butter packets.” — Restaurant Online [4].  
- “About 85% accurate, with humans assisting roughly one in five orders.” — Business Insider quoting McDonald’s CEO statement (June 2021) [6].

## 2) Wendy’s — FreshAI (drive‑thru voice AI)

Annotated citations
- Wendy’s corporate blog: FreshAI pilot began in two states in 2024, expanded nationwide, “processes tens of thousands of orders daily,” and added Spanish capabilities in 2024; Wendy’s describes customer reactions as “even better than interacting with a real person.” [7]  
- Forbes (15 Jan 2025): Wendy’s measured “percentage of orders handled by FreshAI without restaurant team member intervention averaged 86%” and “using a broader definition of accuracy (including orders where crew joins), FreshAI success rate reaches nearly 99%.” [8]  
- AIProuctCraft and QSR/NRN reporting: test site showed service times 22 seconds faster than market average; reports of 86% non‑intervention and cases of >90% accuracy cited across vendor and trade coverage [9], [10].  
- Customer/operator complaints: consumer reports and Reddit anecdotes describe misinterpretation and negative reactions (e.g., wrong items, inability to understand accents), and some franchisees/customers expressed dissatisfaction in public posts [11], [12].

Synthesis — claimed vs. observed performance
- Vendor/owner claims: Wendy’s and partners promote FreshAI as widely deployable, multilingual, and capable of high accuracy and speed gains (tens of thousands of orders processed daily; service time reductions of ~22 seconds in test markets) [7], [9], [10].  
- Measured/operational KPIs reported: Forbes and trade sources cite an 86% rate of orders handled without restaurant team intervention, with broader definitions of “success” (including crew intervention but completed correctly) reaching nearly 99% [8], [10].  
- Reported complaints and variance: trade and consumer anecdotes indicate instances of misinterpretation and customer frustration, including inability to understand accents and customization errors [11], [12]. These reports suggest variability across locations and customer populations despite headline metrics.

Reliability assessment
- High reliability for Wendy’s self‑reported metrics (corporate blog, test‑site performance claims) but these reflect company definitions of metrics; Forbes and trade reporting relay those figures [7], [8], [9].  
- Independent operator/consumer complaints are anecdotal in the cited items (Reddit, consumer articles) and demonstrate existence of failure cases but do not provide systematic error‑rate measurement [11], [12].  
- Overall, available evidence shows Wendy’s reported strong pilot metrics alongside documented real‑world complaints; methodological differences in “accuracy” and “success” definitions are explicitly noted in the sources [8], [10].

## 3) Presto Automation (PRST) — voice product and human‑intervention rates

Annotated citations
- Presto corporate marketing: Presto’s marketing claimed “up to 95% non‑intervention rates” and reported survey/test figures (e.g., Wall Street Journal test at Hardee’s with staff intervening in 3 of 30 orders). [15]  
- SEC enforcement material and administrative file (SEC administrative litigation exhibit PDF / proceeding summary): SEC charged Presto with making false and misleading statements about AI capabilities and disclosed that Presto’s “non‑intervention” rates referred to orders completed without restaurant staff (not without any human involvement), that a third‑party owned/operated speech recognition for a period, and that Presto’s in‑house voice AI required human agent intervention in all instances before June 2023; June–Dec 2023 pilot required human agents to enter orders approximately 70% of the time. [11], [12]  
- Legal commentary and law‑firm summary: summarizes SEC findings that over 70% of orders processed required human agent intervention and that Presto’s public claims were misleading. [13], [16]

Synthesis — exact percentages and reconciliation
- Public claims: Presto’s marketing and web materials claimed non‑intervention (automated order completion) rates up to 95% [15].  
- SEC findings / measured field realities: the SEC found that Presto’s “non‑intervention” language mischaracterized the nature of human involvement; administrative exhibits state that a pilot version “required human agents to enter orders approximately 70% of the time from June 2023 through December 2023,” and that >70% of orders required human agent intervention in certain contexts [11], [12], [13], [16].  
- Reconciliation: Presto’s >95% marketing figure used a definition (orders ultimately completed without restaurant staff intervention) that did not capture off‑site human agents or staged handoffs; SEC disclosures and the administrative file present the countervailing operational reality that human agents (including off‑site agents) performed substantial order entry work during the cited periods [11], [12], [13].

Reliability assessment
- SEC administrative documents and filings are authoritative for disclosures and regulatory findings; summaries and the enforcement PDF provide specific percentages and factual findings and are high‑reliability sources [11], [12].  
- Presto marketing pages provide the contrasting claims and are primary vendor sources for claimed figures but are less reliable for representing operational realities in light of the SEC findings [15].  
- Legal commentary and firm memos corroborate SEC conclusions and provide context [13], [16].

## 4) Kitchen robotics and automated‑kitchen companies that retreated or failed

Annotated citations (selected firms)
- Zume: reporting documents large fundraising, expensive hardware model and pivot; Zume pivoted away from robot pizza trucks, laid off hundreds, and shut down operations entirely in June 2023 after failing to achieve sufficient sales and external funding. [17], [18]  
- Miso Robotics / Flippy (CaliBurger): Miso introduced Flippy in 2017 and planned rollouts; coverage documents the robot and unit pricing/rollout plans and later company updates on next‑generation Flippy. [19], [20]  
- Creator: company profile indicates fundraising and later cessation (dead‑pooled) in traces. [21]  
- Spyce: opened in 2018, acquired by Sweetgreen in 2021, and closed Boston locations by late 2021/2022; Sweetgreen later sold Spyce robotics business to Wonder in 2025 and used Infinite Kitchen in Sweetgreen rollouts. [22], [23], [24]  
- Karakuri: UK kitchen‑robotics startup that announced winding down operations and layoffs in June 2023 after failing to secure funding; Ocado had been an investor. [25], [26], [27]

Synthesis — deployment timelines, pivots/shutdowns, and documented operational failures
- Common trajectories: many robotics startups raised significant capital, executed limited pilots or restaurant integrations, then pivoted, shrank, or shut down after failing to scale commercial deployments or secure follow‑on funding (Zume, Karakuri, Creator, Spyce) [17], [18], [25], [26], [21], [22], [23].  
- Reported operational failures and challenges in the public record:
  - High capital intensity and hardware cost burdens (Zume raised hundreds of millions but hardware and operations were expensive) [17], [18].  
  - Slow scaling and limited commercial rollouts despite initial PR (e.g., Flippy piloted at CaliBurger but broader scaling proved challenging) [19], [20].  
  - Food‑quality, throughput, maintenance, and menu‑variability issues are cited as recurring practical hurdles across firms in trade narratives and company histories (e.g., Zume’s pivot from cooking trucks to packaging; Karakuri’s inability to secure scale partnerships) [18], [25], [26].  
  - Acquisitions and partial absorptions (Spyce → Sweetgreen → later sale of robotics business) illustrate selective value extraction (intellectual property/technology) rather than full commercial automation deployment at scale [24], [23].  

Recurring root causes (supported by the evidence)
- Technical limitations and complexity of food preparation tasks at scale, which increased costs and reduced ability to reach profitable unit economics [17], [18], [19].  
- High capital expenditure per installation and slow throughput scaling compared with labor or conventional equipment, constraining ROI and fundraising outlook [17], [18], [31].  
- Difficulty matching limited, deterministic robotic workflows to variable restaurant menus, special requests, and real operational environments; this produced maintenance and reliability burdens [18], [25].  
- Funding and partnership failures: inability to secure necessary manufacturing, equipment, or distribution partnerships (Karakuri’s failed negotiations; Zume’s funding collapse) precipitated wind‑downs [25], [27], [17].  
- Strategic pivots to other business lines (e.g., packaging) or sale of IP rather than continued hardware commercialization where food‑robot economics did not support scale [18], [24].

Reliability assessment
- Business and trade reporting on fundraising, layoffs, pivots, and shutdowns (Business Insider, Physics World, TechCrunch, The Robot Report) are consistent and corroborated; company announcements and acquisition filings (e.g., Sweetgreen/Spyce sale) provide direct support [17], [18], [19], [24], [25].  
- Specific operational failure modes (food quality, throughput) are summarized across sources; individual device/op‑report detail varies by firm but the pattern of hardware cost, scale mismatch, and funding shortfall is consistently reported.

## 5) Sweetgreen — Infinite Kitchen rollout vs. marketing claims (status as of Q4 2025)

Annotated citations
- Restaurant Business Online (Spyce sale reporting, Nov 2025): “Spyce’s automated kitchen technology, called Infinite Kitchen, is now used in more than 20 Sweetgreen locations across the United States.” [24]  
- Q4 2025 earnings‑call transcript / Fool.com (26 Feb 2026): “Sweetgreen’s Infinite Kitchen technology is deployed in more than 20 of its 270 locations as of the end of 2025,” and the transcript also states Sweetgreen “ended 2025 with 30 Infinite Kitchen locations and opened two additional Infinite Kitchen stores in Q1 2026, bringing the total to 32.” [28]  
- Sweetgreen investor PDF (earnings release): guidance for fiscal 2026 calls for ~15 net new restaurant openings, with about half featuring Infinite Kitchen technology. [29]  
- NRN (analysis): CFO said Infinite Kitchen will be used in 50% of new stores but older smaller stores will not be retrofitted; first Infinite Kitchen store opened May 2023 with an early margin lift reported. [30]  
- Wesleyan business review (capacity/cost figure): “Infinite Kitchen can produce up to 500 bowls per hour, with an installation cost that can reach $550,000 per system.” [31]

Synthesis — rollout pace and discrepancies
- Deployment counts and discrepancies: multiple trade/company sources agree Infinite Kitchen was present in the low tens of locations by end‑2025, but exact counts vary among public materials. Restaurant Business Online (Nov 2025) reports “more than 20” locations using Infinite Kitchen [24]. The Q4‑2025 earnings transcript cited by Fool.com reports “ended 2025 with 30 Infinite Kitchen locations” and notes 32 by Q1 2026 [28]. These two statements create a quantifiable discrepancy in reported deployed‑store counts (≫20 vs. 30).  
- Rollout pace vs. marketing: Sweetgreen’s guidance envisaged roughly half of new openings featuring Infinite Kitchen, and the company framed Infinite Kitchen as a margin‑enhancement investment for new units rather than retrofitting older small stores [29], [30]. Cost and capacity numbers (up to 500 bowls per hour; up to ~$550K install) indicate significant capital commitment per system that constrains retrofit economics [31].

Reliability assessment
- High reliability for company disclosures (earnings transcript, investor PDF) and trade reporting on company statements; the discrepancy in deployed counts is present in the public record and must be treated as conflicting evidence rather than resolved fact [24], [28], [29].  
- The data gap between “more than 20” and “30” underscores either timing differences between sources or reporting rounding; available evidence does not resolve the conflict conclusively.

## 6) POS data quality problems for independent restaurants (Toast, Square, Aloha/NCR)

Annotated citations
- Toast support and community posts: documentation of missing menu items due to menu targeting/versioning errors and guidance on reconciliation reports; community posts describe duplicate/incorrect charges and pending CC charge issues. [33], [35], [15]  
- Square community forum: user report that recent sales and transaction data were not appearing correctly in the Square Dashboard. [34]  
- Aloha (NCR) developer docs: detailed integration settings (polling times, print intercept timeouts) and file‑size/debout limits that create configuration constraints for third‑party integrations. [32]  
- Reddit threads and community posts cite duplicate pending charges and test‑mode actions bleeding into live environments for Toast. [15], [36]

Synthesis — specific data‑quality failure types and operational impacts
- Common data‑quality issues documented in vendor support and community posts include: missing menu items caused by version/targeting mismatches in multi‑location menu management (Toast) [33]; disappearing or delayed sales data in dashboards (Square community report) [34]; duplicate or pending credit‑card charges reported by operators (community/Reddit) [15]; and reconciliation/reporting complexity requiring manual CSV exports and manual reconciliation steps (Toast Reconciliation guidance) [35].  
- Integration‑level constraints in Aloha POS (NCR) — e.g., maximum file sizes, polling timeouts, and print‑intercept timeouts — impose limits on third‑party data exchanges and can contribute to synchronization mismatches or partial data transfers if not tuned properly [32].  
- Operational impacts: missing/duplicated transactions and mapping mismatches increase reconciliation workload, create cashflow/settlement confusion, and necessitate manual corrections by operators and accountants; vendor guidance and community reports document workflows for remediation that impose labor and time costs on operators [33], [35], [15].

Reliability assessment
- High reliability for vendor support articles (Toast, Aloha) describing system behaviors/configuration and reconciliation workflows [33], [35], [32].  
- Community and forum posts provide corroborating practitioner evidence of impact but are anecdotal and do not quantify prevalence [15], [34], [36].

## 7) Legacy POS integration frictions — Aloha (NCR) and Micros (Oracle)

Annotated citations
- Aloha integrator documentation shows configurable integration limits (print intercept timeout, polling times, debout file size limits) that can block or complicate third‑party integrations if not accommodated by integrators. [32]  
- ReformingRetail analysis: POS marketplaces and legacy partner programs may impose revenue‑share fees or certification/maintenance costs for third‑party integrations, increasing integration costs for vendors and merchants. [36]  
- NRN tech‑tracker: trade coverage noting an ongoing “technology integration boom” and that some POS vendors/players (PAR, others) claim extensive third‑party integrations, implying variance in integration openness across vendors. [37]

Synthesis — evidence of frictions and blockers
- Technical blockers: Aloha’s integration configuration parameters and limits (file sizes, polling timeouts) create concrete technical constraints that third‑party AI or cloud services must accommodate, increasing integration complexity and risk of partial data exchange [32].  
- Business model and contractual friction: industry analysis reports that legacy POS partner programs sometimes impose certification or revenue‑share fees for listing/marketplace access, forming a business hurdle to rapid, low‑cost third‑party integration [36].  
- Variability across vendors: trade tracking indicates a mixed landscape—some POS systems tout many integrations while others present more closed ecosystems, implying that AI/third‑party adoption faces uneven barriers depending on POS vendor and contract terms [37].

Reliability assessment
- High reliability for Aloha technical documentation [32] and for industry commentary on partner‑program frictions [36], [37]. The evidence supports technical and contractual friction rather than a single universal “hostility” across all legacy POS vendors.

## 8) AI hiring tools in restaurants — bias and complaints

Annotated citations
- Ogletree legal summary: Eightfold AI Inc. was sued (Jan 20, 2026) in California state court alleging FCRA and California ICRAA violations and alleging compilation of sensitive personal information; the filing relates to AI recruiting/report generation practices and is cited in coverage of legal challenges to AI hiring tools. [38]

Synthesis and reliability
- Evidence shows active litigation alleging problematic data practices and regulatory violations by a major AI hiring vendor (Eightfold) that could affect industries including restaurants where such vendors are used; the cited source is a law‑firm summary of the complaint and is reliable for documenting the existence of legal action and the complaint’s allegations [38].  
- Evidence gap: no explicit, documented EEOC decisions or restaurant‑sector‑specific judgments are present in the provided findings; the available litigation reference documents alleged unlawful practices but does not provide sector‑wide empirical measures of bias in restaurant hiring tools.

## 9) AI‑generated marketing copy failures for ethnic restaurant concepts

Annotated citations
- CreativeBloq: The Salty Otter Sports Grill (Santa Cruz) used an AI‑generated otter‑on‑a‑surfboard logo in May 2025, received harsh backlash and one‑star reviews, and replaced the logo; local reviewers criticized the AI origin and lack of a local artist. [39]  
- Entrepreneur: owner says AI logo controversy significantly harmed the business’s debut and led to replacement of the logo; reporting emphasizes reputational and community backlash. [40]

Synthesis, limits, and evidence gaps
- Documented failure: an AI‑generated logo and marketing asset provoked community backlash and reputational harm in a single‑business case (The Salty Otter), leading to replacement of the AI asset [39], [40].  
- Evidence gap for ethnic‑concept specific failures: the provided findings do not include direct documented examples of AI‑generated menus/marketing producing inaccurate or offensive copy specifically for ethnic cuisines. The Salty Otter case shows reputational risk from AI‑generated creative work but is not explicitly an ethnic‑food case. Recommended next steps to fill the gap are listed below.

Reliability assessment
- Reliable for the specific local incident described; sources are mainstream trade/press reporting and operator quotes [39], [40]. However, no source in the provided evidence directly documents AI‑generated offensive menu copy for ethnic concepts.

## Evidence gaps and recommended next steps

Evidence gaps (items requested in the brief lacking accessible public documentation in the provided findings)
- Full verbatim transcripts or system logs for McDonald’s AOT failing interactions are not included in the provided evidence (only social‑media descriptions and mainstream reporting of clips). The public record in the findings contains descriptions and paraphrases of viral videos but not complete system transcripts.  
- Systematic, independent field data measuring Wendy’s FreshAI accuracy across a representative set of locations is not present; existing figures are company‑reported and trade‑reported summaries.  
- For Sweetgreen Infinite Kitchen, a definitive reconciled count for number of deployments as of Q4 2025 is ambiguous/conflicting across sources (see Section 5).  
- Restaurant‑sector EEOC complaints, enforcement actions, or adjudicated judgments specifically tying AI hiring tool bias to restaurant hiring outcomes are not present in the provided findings beyond the general Eightfold lawsuit (which is not sector‑specific).  
- Documented, sourced examples of AI‑generated marketing copy producing inaccurate or offensive copy specifically for ethnic restaurant concepts are not present.

Recommended next steps to obtain primary evidence
- Obtain primary transcripts/logs: contact McDonald’s corporate communications or IBM (or subpoena/FOIA equivalent for public‑interest review where applicable) for de‑identified pilot transcripts or internal postmortem summaries; interview franchisees who participated in pilot sites for direct copies of transcripts or video links.  
- Field measurements for FreshAI: request or commission an independent mystery‑shop study or audit of FreshAI in a representative sample of Wendy’s drive‑thrus and secure measured accuracy and human‑intervention metrics.  
- Reconcile Sweetgreen deployment counts: obtain Sweetgreen SEC exhibits and investor presentation slide decks (Q4 2025 investor day materials and subsequent slides) or request the company’s investor relations for a dated deployment list.  
- EEOC / legal records: search EEOC public dockets and federal/state court filings for restaurant‑sector complaints naming specific AI hiring vendors; request plaintiff counsel for case exhibits if permitted.  
- Ethnic‑cuisine marketing failures: solicit documented case submissions from trade groups, community organizations, and ethnic‑food business associations; archive and verify social‑media posts and vendor reply threads.

## Conclusion — cross‑cutting themes and implications
- Common, cross‑case operational limits documented in the evidence include: insufficient end‑to‑end accuracy for unsupervised customer‑facing voice systems; sensitivity to accents, noise, and cross‑talk; vendor claims that conflate different definitions of “non‑intervention” or “accuracy” with operational autonomy; hardware cost, maintenance and scale economics undermining kitchen robotics; integration complexity and data quality burdens created by legacy POS systems; and reputational/legal risks where AI output or data practices collide with community expectations or regulatory frameworks [1], [2], [3], [11], [17], [18], [32], [36], [38], [39].  
- Firms and operators should treat vendor metrics as conditioned on vendor definitions (e.g., presence/absence of off‑site human agents) and seek independent verification and clear metric definitions (e.g., orders completed without any human involvement vs. orders completed without in‑restaurant staff intervention) before deploying at scale [11], [12], [15].  
- For drive‑thru voice AI pilots, explicit testing across accented speech cohorts, multi‑lane cross‑talk scenarios, and edge‑case orders is essential to avoid both operational losses and viral reputational incidents [2], [3], [4], [5].  
- For kitchen robotics, careful total‑cost‑of‑ownership, retrofit economics, and realistic throughput modeling are necessary given recurring capital intensity and scale limitations reported across firms [17], [18], [25].  
- Legacy POS and data‑quality issues remain practical bottlenecks to AI integrations and to clean analytics for independent restaurants; vendors’ documentation and partner‑program terms should be reviewed closely to anticipate reconciliation labor and integration costs [32], [33], [35], [36].

## References

Sources
[1] https://nrn.com/quick-service/mcdonald-s-is-ending-its-ai-drive-thru-test-with-ibm  
[2] https://cnbc.com/2024/06/17/mcdonalds-to-end-ibm-ai-drive-thru-test.html  
[3] https://bbc.com/news/articles/c722gne7qngo  
[4] https://restaurantonline.co.uk/Article/2024/06/19/McDonald-s-ends-AI-drive-thru-trial-in-US-after-order-mistakes/  
[5] https://linkedin.com/posts/adam-elshimi_ai-agenticai-multiagentsystems-activity-7333788030027100160-fSnI  
[6] https://businessinsider.com/mcdonalds-ai-voice-order-technology-drive-thrus-2024-6  
[7] https://wendys.com/blog/wendysr-square-deal-blog/transforming-ordering-experience-wendys-freshai-update  
[8] https://forbes.com/sites/maribellopez/2025/01/15/wendys-serves-up-generative-ai-to-boost-its-customer-experience/  
[9] https://aiproductcraft.com/p/wendys-freshai-ai-drive-thru-order-system  
[10] https://cdotimes.com/2026/01/09/wendys-vs-mcdonalds-the-ai-drive-thru-reckoning/  
[11] https://sec.gov/files/litigation/admin/2025/33-11352.pdf  
[12] https://sec.gov/enforcement-litigation/administrative-proceedings/33-11352-s  
[13] https://jdsupra.com/legalnews/sec-charges-ai-washing-at-presto-3215624/  
[14] https://presto.com/  
[15] https://presto.com/the-improvement-and-impact-of-voice-ai-in-the-drive-thru/  
[16] https://lowenstein.com/media/0dbffgrh/20250203-cms-sec-charges-public-company-with-ai-washing.pdf  
[17] https://businessinsider.com/robot-pizza-startup-zume-shutting-down-raised-500-million-softban-2023-6  
[18] https://physicsworld.com/a/robot-cooked-pizza-delivered-to-your-door-heres-what-zumes-failure-tells-us/  
[19] https://techcrunch.com/2017/09/19/flippy-the-hamburger-cooking-robot-gets-its-first-restaurant-gig/  
[20] https://misorobotics.com/newsroom/miso-robotics-unveils-flippy-in-caliburger-kitchen-plans-worldwide-rollout/  
[21] https://tracxn.com/d/companies/creator/__4oU4vSBPXAQNby68tQa2U9t7Kwn4gXz2Q39BcDWeFiA  
[22] https://en.wikipedia.org/wiki/Spyce_Kitchen  
[23] https://bostonmagazine.com/restaurants/2018/04/24/spyce-robotic-restaurant-boston/  
[24] https://restaurantbusinessonline.com/technology/sweetgreen-completes-sale-spyce-robotics-business-wonder  
[25] https://therobotreport.com/food-robotics-startup-karakuri-shutting-down/  
[26] https://businesscloud.co.uk/news/kitchen-robotics-startup-karakuri-to-close/  
[27] https://news.sky.com/story/ocado-backed-robotics-start-up-karakuri-on-brink-of-collapse-12904836  
[28] https://fool.com/earnings/call-transcripts/2026/02/26/sweetgreen-sg-q4-2025-earnings-call-transcript/  
[29] https://s28.q4cdn.com/367108596/files/doc_news/Sweetgreen-Inc--Announces-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results-2026.pdf  
[30] https://nrn.com/restaurant-technology/here-s-why-sweetgreen-no-longer-wants-to-be-fully-automated  
[31] https://wesleyanbusinessreview.com/issueixtechnology/blog-post-title-two-79x5p  
[32] https://docs.ncrvoyix.com/restaurant/aloha-pos/implementing/field_definitions/integrations  
[33] https://support.toasttab.com/en/article/Why-have-my-menu-items-diasppeared  
[34] https://community.squareup.com/t5/Customer-Engagement/Square-Dashboard-Not-Showing-Recent-Sales-Data-Need-Help/td-p/829283  
[35] https://support.toasttab.com/article/Reconciliation-Report-and-Payout-Details-Overview  
[36] https://reformingretail.com/index.php/2018/11/27/ncrs-perfect-example-for-how-not-to-run-a-pos-partner-program/  
[37] https://nrn.com/restaurant-technology/tech-tracker-the-great-technology-integration-boom-continues  
[38] https://ogletree.com/insights-resources/blog-posts/groundbreaking-lawsuit-tests-whether-ai-hiring-tools-trigger-fcra-compliance/  
[39] https://creativebloq.com/design/logos-icons/restaurant-forced-to-change-its-logo-after-scathing-ai-backlash  
[40] https://entrepreneur.com/business-news/the-salty-otter-owner-says-ai-logo-controversy-crushed-her-dream
