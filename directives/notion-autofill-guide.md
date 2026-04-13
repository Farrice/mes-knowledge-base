# Notion Autofill & Custom Agents Configuration Guide

How to set up Notion's built-in Autofill properties and Custom Agents so your databases do work for you instead of sitting dormant.

---

## Part 1: Autofill Properties

Autofill uses Notion AI to automatically populate a property when a page is created or updated. You configure it per-property in each database's schema.

### How to Add an Autofill Property (General Steps)

1. Open the database in **full-page view** (not inline). Click the database title to expand it.
2. Click the **+** button in the rightmost column header to add a new property, or click an existing property name to edit it.
3. In the property configuration panel, set the **Type** to "AI autofill" (scroll down in the type dropdown -- it is near the bottom, under "Advanced").
4. Once you select "AI autofill", Notion shows a **prompt field**. This is where you write what the AI should generate.
5. You can reference other properties in the prompt using `@Property Name` syntax. This is how the AI reads existing fields to generate new ones.
6. Set the **Fill mode**:
   - "When empty" -- fills only when the field is blank (recommended for most cases)
   - "Always" -- overwrites every time the page is edited (use sparingly)
7. Click **Done**. The autofill will trigger next time a page is created or edited.

**Important**: Autofill properties count against your Notion AI usage. If you are on a free AI trial, monitor your usage at Settings > Plans > AI add-on.

---

### Database: Performance Log

**Database ID**: `31f49875-a897-81db-b599-dee5e7961b5c`

#### Autofill 1: Summary (from Notes)

Purpose: Auto-generate a one-line summary from the freeform Notes field so you can scan the database without opening each entry.

1. Open the **Performance Log** database.
2. Click the **+** column header to add a new property.
3. Name it **Summary**.
4. Set type to **AI autofill**.
5. In the prompt field, enter:

```
Summarize the following notes in one sentence (max 15 words). Focus on what was produced and the key quality signal. Notes: @Notes
```

6. Set fill mode to **When empty**.
7. Click Done.

#### Autofill 2: Domain (from Skill)

Purpose: Auto-tag the knowledge domain based on the Skill name, so you can filter/sort by domain without manually entering it every time.

1. In the Performance Log, click the **+** column header to add a new property.
2. Name it **Domain**.
3. Set type to **AI autofill**.
4. In the prompt field, enter:

```
Based on this skill path, output ONLY the knowledge domain as a single word or short phrase. Use these categories: LinkedIn, Copywriting, SEO, Brand Strategy, Content Strategy, Screenwriting, Sales Psychology, Ghostwriting, Consumer Psychology, Systems, Research. Skill: @Skill
```

5. Set fill mode to **When empty**.
6. Click Done.

---

### Database: Content Pipeline

**Database ID**: `ff77ee45-8ee8-4fce-996e-20c76fa65d9c`

#### Autofill 1: SEO Description (from Core Idea)

Purpose: Generate a search-optimized meta description (155 chars) from the Core Idea so every content piece has an SEO hook ready before publishing.

1. Open the **Content Pipeline** database.
2. Click **+** to add a new property.
3. Name it **SEO Description**.
4. Set type to **AI autofill**.
5. In the prompt field, enter:

```
Write a meta description (max 155 characters) for this content piece. It should be compelling, include the main keyword naturally, and end with an implied benefit or curiosity gap. Core idea: @Core Idea. Platform: @Platform.
```

6. Set fill mode to **When empty**.
7. Click Done.

#### Autofill 2: Content Type Tag (from Core Idea + Hook)

Purpose: Auto-classify content type so you can filter your pipeline by format without manual tagging.

1. In the Content Pipeline, click **+** to add a new property.
2. Name it **Auto Type**.
3. Set type to **AI autofill**.
4. In the prompt field, enter:

```
Classify this content into exactly ONE type based on the core idea and hook. Choose from: Thought Leadership, How-To, Story, Listicle, Case Study, Opinion, Curation, Announcement. Output only the type name, nothing else. Core idea: @Core Idea. Hook: @Hook.
```

5. Set fill mode to **When empty**.
6. Click Done.

---

### Database: Knowledge Vault

**Database ID**: `5c63b25c-e040-4c6f-8a7b-906643090694`

#### Autofill 1: Key Patterns (from page content)

Purpose: Auto-extract key patterns from the source content so the Knowledge Vault is searchable by pattern, not just by title.

1. Open the **Knowledge Vault** database.
2. Find the existing **Key Patterns** property (rich_text type). If you want to keep it manual AND have an auto version, create a new property called **Auto Patterns** instead.
3. To create the new property: click **+**, name it **Auto Patterns**, set type to **AI autofill**.
4. In the prompt field, enter:

```
Read the page content below and extract 3-5 key patterns, frameworks, or principles. Format as a comma-separated list. Each pattern should be 2-5 words. Focus on actionable, transferable insights -- not summaries. If the content is about an expert's methodology, name their specific techniques.
```

Note: This autofill reads the **page body content** (not just properties) because no `@Property` is referenced. Notion AI will scan the full page.

5. Set fill mode to **When empty**.
6. Click Done.

---

## Part 2: Custom Agents (Beta)

Notion Custom Agents are automated AI workflows that run on a trigger (schedule or event) and can read/write across your databases. As of April 2026, they are in beta and **free until May 2026**.

To access: Settings (gear icon, bottom-left) > Connections > Custom Agents (beta tab).

**Limitations to know**:
- Custom Agents run asynchronously -- they are not instant.
- They can read database entries and update properties, but cannot create new pages (yet).
- They operate within your workspace permissions.
- After the beta ends (May 2026), they will likely require the AI add-on subscription.

---

### Agent 1: Captures Auto-Triage

**Purpose**: When a new entry lands in the Captures database, classify its type and suggest where it should be routed (Content Pipeline, Knowledge Vault, Projects, or Personal Context).

#### Trigger Configuration

1. Go to Settings > Connections > Custom Agents.
2. Click **New Agent**.
3. Name it **Captures Triage Bot**.
4. Set the **Trigger** to: **When a page is added** in the **Captures** database (`f55d202d-233c-4284-a8f1-7ab1c145ffe1`).
5. Set the **Action** to: **Update page properties**.

#### Prompt Template

In the agent's instruction field, enter:

```
You are a triage agent for a knowledge management system. A new capture has arrived.

Read the capture:
- Title: {Name}
- Raw Content: {Raw Content}
- Source: {Source}

Do two things:

1. CLASSIFY: Set the "Type" property to the best fit from: Idea, Task, Note, Observation, Question, Voice Memo, Reference.

2. ROUTE: Set a new property called "Suggested Route" to exactly ONE of these destinations:
   - "Content Pipeline" -- if this is a content idea, hook, topic, or draft
   - "Knowledge Vault" -- if this is an extraction, framework, pattern, or research finding
   - "Projects" -- if this is an actionable task or project update
   - "Personal Context" -- if this is a journal entry, reflection, or identity insight
   - "Keep in Captures" -- if it does not clearly fit elsewhere

Be decisive. Pick the single best route. Do not hedge.
```

6. Under **Properties to update**, check: **Type**, **Suggested Route** (you will need to create a "Suggested Route" select property in the Captures database first -- options: Content Pipeline, Knowledge Vault, Projects, Personal Context, Keep in Captures).
7. Click **Save**.

#### Setup: Add the Suggested Route Property

Before enabling the agent, add the routing property:

1. Open the **Captures** database.
2. Click **+** to add a new property.
3. Name it **Suggested Route**.
4. Type: **Select**.
5. Add options: Content Pipeline, Knowledge Vault, Projects, Personal Context, Keep in Captures.
6. Click Done.

Now the agent will populate both Type and Suggested Route on every new capture.

---

### Agent 2: Weekly Content Pipeline Sweep

**Purpose**: Run every Monday at 9am. Scan the Content Pipeline for stale drafts (entries stuck in "Draft" or "Raw Idea" stage for 14+ days) and flag them so they do not rot in the pipeline.

#### Trigger Configuration

1. Go to Settings > Connections > Custom Agents.
2. Click **New Agent**.
3. Name it **Stale Draft Sweeper**.
4. Set the **Trigger** to: **Recurring schedule** -- every **Monday at 9:00 AM** (your local time).
5. Set the **Scope** to: **Content Pipeline** database (`ff77ee45-8ee8-4fce-996e-20c76fa65d9c`).
6. Set a **Filter** (if the UI supports it): Stage is "Raw Idea" or "Draft".

#### Prompt Template

```
You are a content pipeline manager. Review each entry in this database that has a Stage of "Raw Idea" or "Draft".

For each entry, check the "Created time" or last edited time.

If the entry has been in "Raw Idea" or "Draft" for more than 14 days:

1. Add the tag "Stale" to the Tags property.
2. Set a new property called "Sweep Note" to a brief suggestion (max 20 words):
   - If the Core Idea is strong: "Strong idea -- schedule a content sprint to finish"
   - If the Core Idea is vague: "Vague concept -- either sharpen or archive"
   - If it duplicates another entry: "Possible duplicate -- check [similar title]"

If the entry is less than 14 days old, skip it entirely.
```

7. Under **Properties to update**, check: **Tags**, **Sweep Note** (create "Sweep Note" as a rich_text property in the Content Pipeline first).
8. Click **Save**.

#### Setup: Add the Sweep Note Property

1. Open the **Content Pipeline** database.
2. Click **+** to add a new property.
3. Name it **Sweep Note**.
4. Type: **Text** (rich_text).
5. Click Done.

---

## Testing Before Relying On

Custom Agents are beta. Before trusting them with real workflows:

1. **Test with a dummy entry first.** Create a test capture like "Test triage -- delete me" and verify the agent classifies it correctly within a few minutes.
2. **Check for false positives.** After the first weekly sweep runs, review every entry it tagged "Stale" to confirm the logic is correct. Notion AI may misread dates or misclassify.
3. **Monitor for 2 weeks before automating downstream actions.** Do not build any automation that depends on agent output (like auto-archiving stale drafts) until you have confirmed accuracy over multiple runs.
4. **Watch for beta pricing changes.** Notion has announced Custom Agents are free until May 2026. Check Settings > Plans before that date to understand costs.

---

## Quick Reference: All New Properties to Create

| Database | Property Name | Type | Purpose |
|----------|--------------|------|---------|
| Performance Log | Summary | AI autofill | One-line summary from Notes |
| Performance Log | Domain | AI autofill | Auto-tagged from Skill name |
| Content Pipeline | SEO Description | AI autofill | Meta description from Core Idea |
| Content Pipeline | Auto Type | AI autofill | Content format classification |
| Content Pipeline | Sweep Note | Text | Weekly sweep suggestions |
| Knowledge Vault | Auto Patterns | AI autofill | Key patterns from page content |
| Captures | Suggested Route | Select | Triage routing destination |

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Created** | 2026-04-13 |
| **Last Updated** | 2026-04-13 |
| **Status** | Ready to configure -- no Notion changes made yet |
