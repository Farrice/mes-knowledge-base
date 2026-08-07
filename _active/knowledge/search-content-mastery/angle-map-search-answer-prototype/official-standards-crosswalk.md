# Official Search And Answer Standards Crosswalk

**Checked:** 2026-08-05  
**Use:** Internal prototype design  
**Evidence rule:** Platform behavior below is `VERIFIED` only where the linked owner documentation says it. Service-design consequences are `INFERRED`. None is a market-effect promise.

## What The Platforms Actually Support

| `VERIFIED` owner guidance | Prototype consequence (`INFERRED`) |
|---|---|
| Google says its AI search features rely on normal search foundations. There is no special AI markup, and a page must be indexed and eligible for a snippet. AI-feature activity is included in Search Console's Web reporting. [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) | Sell technical eligibility and answer usefulness. Do not sell secret AEO markup or clean Google-AI citation reporting. |
| Google asks for people-first content, original information, clear sourcing, authorship, demonstrated expertise, and an explicit who/how/why. Trust matters most, especially for health-related YMYL topics. [Google: helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Every real health asset needs a named author or qualified reviewer, source receipts, a review date, and information gain. |
| Scaled pages can violate spam policy when their main purpose is ranking manipulation and they add little value, regardless of whether humans or AI produced them. [Google: generative AI guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) and [Google: spam policies](https://developers.google.com/search/docs/essentials/spam-policies) | V1 produces one reviewed answer asset. Bulk article volume is outside scope. |
| Structured data must describe visible, current, non-misleading page content. Valid markup creates eligibility, not guaranteed appearance. [Google: structured-data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | Schema is an implementation specification with a validation receipt, never a ranking or citation lever by itself. |
| FAQ rich results are generally restricted to well-known authoritative government and health sites. [Google: FAQ rich-result change](https://developers.google.com/search/blog/2023/08/howto-faq-changes) | FAQs can improve human clarity and answer structure, but a supplement brand should not be promised a FAQ rich result. |
| Product visibility depends on accurate Product and Offer facts, purchasable single-product pages, and consistent price, availability, variants, shipping, returns, and identifiers. [Google: merchant listing markup](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) and [product variants](https://developers.google.com/search/docs/appearance/structured-data/product-variants) | Product-page work needs a separate lane. Product facts come from client truth, not the writer. |
| Bing says ordinary SEO foundations support grounding and citation eligibility. It favors focused, original, understandable content, evidence-supported claims, accurate freshness, clear structure, and consistent entities. [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/bing-webmaster-guidelines-30fba23a) | Use concise answers, tables, sources, and entity consistency as quality practices, not a guaranteed citation recipe. |
| Bing AI Performance separates citations, cited pages, and grounding-query groups, and warns that these do not measure rank, authority, clicks, importance, or causal effect. [Bing: AI Performance](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c) | Keep `CITED`, `RANKED`, `TRAFFIC`, `CONVERTED`, and `COLLECTED` as independent events. |
| IndexNow reports changed URLs to participating engines; acceptance does not guarantee indexing. [IndexNow documentation](https://www.indexnow.org/documentation) and [FAQ](https://www.indexnow.org/faq) | Include an implementation-ready change receipt where supported. Do not count submission as indexation. |
| OpenAI says publishers should allow `OAI-SearchBot` for ChatGPT search summaries and snippets. `GPTBot` is a separate training control. ChatGPT referrals include `utm_source=chatgpt.com`. [OpenAI publisher FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) | Add a crawler-access check and a ChatGPT-referral segment to implementation and measurement plans. Crawler access does not guarantee citation. |
| Schema.org defines `DietarySupplement` and health-oriented types such as `MedicalWebPage`, including safety, intake, reviewer, and review-date properties. [Schema.org: DietarySupplement](https://schema.org/DietarySupplement) and [MedicalWebPage](https://schema.org/MedicalWebPage) | Use specific health semantics only when the facts and page purpose make them truthful. Favor documented Google feature types for claimed search eligibility. |
| FDA says website and label claims can affect whether a supplement is treated as a drug. Structure/function claims require substantiation and specific notification/disclaimer handling. [FDA: supplement claims](https://www.fda.gov/food/dietary-supplements-guidance-documents-regulatory-information/dietary-supplement-labeling-guide-chapter-vi-claims) and [structure/function notification](https://www.fda.gov/food/information-industry-dietary-supplements/notifications-structurefunction-and-related-claims-dietary-supplement-labeling) | Every real project needs claim classification and a qualified reviewer. Marketing review does not become regulatory clearance. |
| FTC requires adequate substantiation for express and implied objective claims. The evidence must fit the formulation, dose, population, and claimed outcome. Testimonials are not substantiation, and a disclaimer cannot cure a contradictory message. [FTC: Health Products Compliance Guidance](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance) | Build a claim-to-evidence matrix. Ingredient research cannot silently become finished-product proof. |
| LinkedIn prohibits false health information and undisclosed paid endorsements. Its paid advertising rules apply additional restrictions to dietary supplements. [LinkedIn Community Policies](https://www.linkedin.com/legal/professional-community-policies) and [healthcare advertising policy](https://www.linkedin.com/help/lms/answer/a1320991) | An organic derivative is possible after review. Paid distribution is a separately gated service and is outside this prototype. |

## Durable Design Decisions

1. The working chain is: approved angle → approved claim territory → SearchBrief → claim/evidence review → owned answer asset → technical specification → LinkedIn derivative → dated observation receipt.
2. The prototype produces one high-confidence asset, not a generated cluster.
3. Claim classification, evidence quality, product match, qualified review, disclosure placement, and platform eligibility remain visible in scoring.
4. Technical readiness and schema eligibility are separate from observed indexing, ranking, citation, traffic, and conversion.
5. The commercial promise covers the work and its receipts. It does not cover market response.

## Unknowns That Stay Unknown

- No platform publishes a deterministic formula for earning AI citations.
- It is `UNCONFIRMED` whether health-specific Schema.org types improve ranking or citation likelihood.
- Google Search Console does not provide a clean Google-AI citation report.
- A technically eligible asset may never be crawled, indexed, ranked, cited, or visited.
- Regulatory acceptability depends on the real product, formula, evidence, wording, audience, jurisdiction, and complete page impression.
- No market effect exists until a dated external observation records it.
