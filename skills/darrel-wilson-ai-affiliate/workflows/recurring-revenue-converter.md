---
description: Convert one-time sales into subscription revenue — the recurring revenue conversion playbook
---

# Recurring Revenue Converter

Transform any one-time sale or project into a recurring revenue stream. Based on Darrel Wilson's model of converting $200 website builds into $97/month hosting+maintenance packages — where the real money is made over 12-24 months.

## Input Required

- **Current Offering**: What are you selling as a one-time payment?
- **Client Base**: How many past clients do you have?
- **Technical Ability**: Can you host/maintain/update what you deliver?
- **Price Sensitivity**: What can your market bear monthly?

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution

### Step 1: Recurring Opportunity Audit

For every one-time product/service, identify the recurring wrapper:

| One-Time Sale | Recurring Wrapper | Monthly Price | Justification |
|---------------|------------------|---------------|---------------|
| Website build ($200-$5K) | Hosting + maintenance + updates | $47-$197/month | "Your site stays fast, secure, and updated" |
| n8n workflow ($500-$5K) | Monitoring + optimization + support | $97-$497/month | "We keep it running and improve it monthly" |
| AI micro-app (one-time license) | SaaS subscription (hosted version) | $9.99-$29.99/month | "Always updated, cloud-hosted, no maintenance" |
| Content package ($500-$2K) | Content retainer | $500-$2,000/month | "Ongoing content creation and optimization" |
| Consulting session ($150-$300) | Advisory retainer | $500-$1,500/month | "Ongoing strategic guidance" |

### Step 2: The "Maintenance + Access" Formula

Every recurring offer needs two components:

1. **Maintenance Value** (they NEED this):
   - Security updates, hosting, backups
   - API monitoring, error resolution
   - Performance optimization
   - Bug fixes and compatibility updates

2. **Access Value** (they WANT this):
   - Priority support (email/Slack)
   - Monthly strategy call (15-30 minutes)
   - Quarterly optimization report
   - Early access to new features/tools

**Pricing Formula**: Take the annual value of maintenance + access, divide by 12, then price at 50-70% of that to create obvious ROI.

### Step 3: Conversion Playbook

**For New Clients (convert at point of sale):**
```
"The website build is $[price]. That includes everything to get you live.

For hosting and ongoing maintenance, I have two options:
• Self-hosted: You manage hosting, updates, and security yourself ($0/month, but you'll need technical ability).
• Managed: I handle everything — hosting, updates, security, monthly optimizations, priority support. It's $97/month.

93% of my clients choose managed because they'd rather focus on their business."
```

**For Past Clients (upsell):**
```
"Hey [Name], I noticed your website [specific observation — slow load time, outdated plugin, security warning]. 

I'm launching a managed maintenance program for past clients:
• Hosting, security, and speed optimization
• Monthly updates and improvements  
• Priority support if anything breaks

First 10 clients: $67/month (locked-in price). You'd be client #[X].

Want me to run a free site audit so you can see what needs attention?"
```

### Step 4: Pricing Tiers

Build 3 tiers to capture different buyer segments:

| Tier | Monthly Price | Includes | Target |
|------|--------------|----------|--------|
| **Essential** | $47/month | Hosting + security + weekly backups | Budget-conscious clients |
| **Growth** | $97/month | Essential + monthly optimization + email support | Most clients (anchor) |
| **Premium** | $197/month | Growth + monthly strategy call + priority support | High-value clients |

**Anchor Effect**: Most clients choose the middle tier when presented with 3 options. Design the middle tier as your target.

### Step 5: Retention Architecture

Churn is the enemy of recurring revenue. Prevent it:

| Retention Lever | Implementation | Impact |
|----------------|---------------|--------|
| **Monthly Reports** | Automated report showing value delivered (uptime, updates, security blocks) | Makes invisible value visible |
| **Quarterly Reviews** | 15-min call reviewing performance + suggesting improvements | Human connection = stickiness |
| **Annual Lock-In Discount** | 2 months free on annual billing | Reduces churn by 40-60% |
| **Switching Cost** | Migration away is painful (they'd need new hosting, DNS changes) | Natural barrier |
| **Ongoing Value Adds** | Add new features quarterly without raising prices | Increasing value = declining churn |

### Step 6: Revenue Projections

Model your recurring revenue growth:

| Month | New Clients | Total Clients | MRR @ $97 | Cumulative Revenue |
|-------|------------|--------------|-----------|-------------------|
| 1 | 3 | 3 | $291 | $291 |
| 3 | 3 | 9 | $873 | $2,037 |
| 6 | 3 | 18 | $1,746 | $6,111 |
| 12 | 3 | 33 (5% churn) | $3,201 | $18,297 |
| 24 | 3 | 58 (5% churn) | $5,626 | $56,025 |

**At $97/month, 3 new clients/month, 5% monthly churn → $5,600/month recurring by Month 24.**

## Output Schema

A complete recurring revenue conversion package, delivered as these fields:
- **Opportunity Audit** (table): one-time sale → recurring wrapper → monthly price → justification line, for every offering named in Input Required
- **3-Tier Pricing Structure** (table): Essential / Growth / Premium, price, includes, anchor-tier flag
- **Sales Scripts** (text blocks): new-client point-of-sale script, past-client upsell script — both with a fillable price/observation slot
- **Retention System** (table): retention lever → implementation → churn-reduction impact
- **Revenue Projection Model** (table): month → new clients → total clients (with churn %) → MRR → cumulative revenue
- **Monthly Report Template** (field list): uptime, updates applied, security blocks, next-step recommendation

---

## Quality Gate

> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
