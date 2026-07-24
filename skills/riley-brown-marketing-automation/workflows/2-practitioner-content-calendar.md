# Workflow: /riley-content-calendar-orchestrator

**Tier**: Practitioner  
**Complexity**: Medium-High  
**Time**: 10-30 minutes  
**Cost**: $5-15 (Claude, optional scheduling service)  
**APIs**: Notion, Gmail, Cal.com, Claude  
**Output**: Scheduled content calendar + draft emails to reviewers

---

## Pre-Flight Gate

**When to Use**:
- You have generated content from multiple creators/sources
- You want to schedule it across dates and notify reviewers
- You're coordinating multi-creator content distribution

**Prerequisites**:
- Notion database with drafted content (from `/riley-skill-extractor`, `/ghostwrite`, `/parallax`, etc.)
- Gmail API key + reviewer email addresses
- Cal.com API key (optional, for auto-calendar creation)
- Claude API key (optional, for draft refinement)

**Don't Use When**:
- You're publishing directly (no review needed)
- You're scheduling <3 pieces of content (manual calendar is faster)
- Reviewers require specialized feedback tools

---

## Skill Acquisition

**Read First**:
1. `genius.md` — Section: "Real-Time Orchestration"
2. `SKILL.md` — Quick Reference: `/riley-content-calendar-orchestrator`
3. `references/api-integration-guide.md` — Sections: "5. Gmail API", "6. Cal.com API"
4. `references/notion-schema-templates.md` — Section: "Template 4: Content Calendar"

**Key Concepts**:
- Notion as the source of truth (all content lives here)
- Gmail API sends draft reviews to stakeholders
- Cal.com API creates calendar blocks for publishing
- Claude can help refine drafts before sending to reviewers

---

## Execution

### Step 1: Create Content Calendar in Notion

```python
import notion_client
import datetime

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

# Create database
db = client.databases.create(
    parent={"page_id": "PARENT_PAGE_ID"},
    title="Content Calendar",
    properties={
        "Post Title": {"title": {}},
        "Creator/Source": {"select": {"options": [
            {"name": "Kallaway"}, {"name": "Farrice"}, {"name": "Riley"},
            {"name": "Lara Acosta"}, {"name": "Custom"}
        ]}},
        "Platform": {"select": {"options": [
            {"name": "LinkedIn"}, {"name": "Substack"}, 
            {"name": "Twitter"}, {"name": "YouTube"}
        ]}},
        "Content Type": {"select": {"options": [
            {"name": "Post"}, {"name": "Essay"}, {"name": "Video Script"}
        ]}},
        "Status": {"select": {"options": [
            {"name": "Draft"}, {"name": "In Review"}, 
            {"name": "Approved"}, {"name": "Scheduled"}, {"name": "Published"}
        ]}},
        "Content": {"rich_text": {}},
        "Scheduled Date": {"date": {}},
        "Reviewer": {"select": {"options": [
            {"name": "Farrice"}, {"name": "Subject Matter Expert"},
            {"name": "Copy Editor"}
        ]}},
        "Review Deadline": {"date": {}},
        "Feedback": {"rich_text": {}},
        "Next Steps": {"rich_text": {}}
    }
)

return db['id']
```

### Step 2: Populate Calendar from Generated Content

Export drafted content from source databases (e.g., `/riley-skill-extractor`, `/ghostwrite`) and add to calendar:

```python
# Query source databases
creator_db_results = client.databases.query(
    database_id="CREATOR_DB_ID",
    filter={"property": "Status", "select": {"equals": "Ready for Calendar"}}
)

# Add each piece to calendar
for page in creator_db_results['results']:
    props = page['properties']
    
    client.pages.create(
        parent={"database_id": calendar_db_id},
        properties={
            "Post Title": {"title": [{"text": {"content": props['Title']['title'][0]['text']['content']}}]},
            "Creator/Source": {"select": {"name": props.get('Creator', 'Custom')}},
            "Platform": {"select": {"name": props.get('Platform', 'LinkedIn')}},
            "Status": {"select": {"name": "Draft"}},
            "Content": {"rich_text": [{"text": {"content": props['Content']['rich_text'][0]['text']['content']}}]}
        }
    )

print(f"✓ Added {len(creator_db_results['results'])} pieces to calendar")
```

### Step 3: Schedule Content Dates

Batch schedule across dates (stagger 3-5 days apart):

```python
import datetime

# Get all Draft posts
draft_posts = client.databases.query(
    database_id=calendar_db_id,
    filter={"property": "Status", "select": {"equals": "Draft"}},
    page_size=50
)

# Schedule them 3 days apart, starting from tomorrow
start_date = datetime.datetime.now() + datetime.timedelta(days=1)
posts = draft_posts['results']

for i, page in enumerate(posts):
    scheduled_date = start_date + datetime.timedelta(days=i*3)
    
    client.pages.update(
        page_id=page['id'],
        properties={
            "Scheduled Date": {"date": {"start": scheduled_date.isoformat()}}
        }
    )

print(f"✓ Scheduled {len(posts)} posts (3 days apart)")
```

### Step 4: Generate Review Drafts via Gmail

For each post in "Draft" status, send a review email:

```python
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Build Gmail service
service = build('gmail', 'v1', credentials=creds)

# Get all Draft posts
draft_posts = client.databases.query(
    database_id=calendar_db_id,
    filter={"property": "Status", "select": {"equals": "Draft"}},
    page_size=50
)

# For each draft, compose and send review email
for page in draft_posts['results']:
    props = page['properties']
    
    title = props['Post Title']['title'][0]['text']['content']
    content = props['Content']['rich_text'][0]['text']['content']
    reviewer = props['Reviewer']['select']['name'] if props['Reviewer']['select'] else "Farrice"
    platform = props['Platform']['select']['name']
    scheduled_date = props['Scheduled Date']['date']['start'] if props['Scheduled Date']['date'] else "TBD"
    
    # Compose email
    subject = f"Review: {title} (scheduled {platform} {scheduled_date})"
    
    body = f"""
Hi {reviewer},

Please review this {platform} post scheduled for {scheduled_date}.

---

TITLE: {title}

PLATFORM: {platform}

CONTENT:
{content}

---

Feedback requested by: {(datetime.datetime.fromisoformat(scheduled_date) - datetime.timedelta(days=1)).isoformat()}

Approve, request changes, or reject.

Reply with feedback or react with 👍 to approve.

---

Farrice
"""
    
    # Create MIME message
    message = MIMEMultipart()
    message['to'] = get_reviewer_email(reviewer)
    message['subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    # Send
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
    
    # Update status to "In Review"
    client.pages.update(
        page_id=page['id'],
        properties={"Status": {"select": {"name": "In Review"}}}
    )

print(f"✓ Sent {len(draft_posts['results'])} review emails")

def get_reviewer_email(reviewer_name):
    """Map reviewer name to email."""
    emails = {
        "Farrice": "farrice.cain@gmail.com",
        "Subject Matter Expert": "expert@domain.com",
        "Copy Editor": "editor@domain.com"
    }
    return emails.get(reviewer_name, "farrice.cain@gmail.com")
```

### Step 5: Create Calendar Events (Optional Cal.com)

Schedule calendar blocks for each post:

```python
import requests

# Cal.com API
headers = {"Authorization": f"Bearer YOUR_CALCOM_KEY"}

# Get all scheduled posts
scheduled_posts = client.databases.query(
    database_id=calendar_db_id,
    filter={"property": "Status", "select": {"equals": "Scheduled"}},
    page_size=50
)

for page in scheduled_posts['results']:
    props = page['properties']
    
    title = props['Post Title']['title'][0]['text']['content']
    platform = props['Platform']['select']['name']
    scheduled_date = props['Scheduled Date']['date']['start']
    
    # Create calendar event
    event = {
        "title": f"Publish: {title} ({platform})",
        "startTime": f"{scheduled_date}T09:00:00Z",
        "endTime": f"{scheduled_date}T09:30:00Z",
        "description": f"Publish {platform} post: {title}"
    }
    
    response = requests.post(
        "https://api.cal.com/v1/events",
        json=event,
        headers=headers
    )

print(f"✓ Created {len(scheduled_posts['results'])} calendar events")
```

### Step 6: Monitor Review Status & Close Loop

Track which posts are approved, rejected, or need revision:

```python
# Get all "In Review" posts
in_review = client.databases.query(
    database_id=calendar_db_id,
    filter={"property": "Status", "select": {"equals": "In Review"}},
    page_size=50
)

print(f"Posts in review: {len(in_review['results'])}")
print("\nWaiting on approval for:")
for page in in_review['results']:
    title = page['properties']['Post Title']['title'][0]['text']['content']
    deadline = page['properties']['Review Deadline']['date']['start']
    print(f"  - {title} (due {deadline})")

# Manual step: Check Gmail for responses, update status to "Approved" or "Revise"
# (Can be automated with Gmail label detection if needed)
```

---

## Content Type Adaptations

### LinkedIn Posts
- Length: 150-500 words
- Scheduling: Tuesday-Thursday, 8-10am
- Review time: 24 hours

### Substack Essays
- Length: 800-2000 words
- Scheduling: Thursday-Sunday
- Review time: 48 hours

### Twitter/X Threads
- Length: 5-15 tweets, 100-280 chars each
- Scheduling: Weekday mornings
- Review time: 12 hours

### YouTube Scripts
- Length: 3000-8000 words (depending on video length)
- Scheduling: Upload Friday evening for Saturday morning publish
- Review time: 72 hours

---

## Output Requirements

**Content Calendar**:
- ✓ All drafted content populated (minimum 5 pieces)
- ✓ Scheduled dates staggered 3-5 days apart
- ✓ Review emails sent to stakeholders
- ✓ Status tracked (Draft → In Review → Approved → Scheduled → Published)
- ✓ Calendar events created (optional but recommended)

**Quality Gate**:
- ✓ All emails sent successfully (check Gmail Sent folder)
- ✓ Review deadlines are realistic (24-72 hours before publish)
- ✓ Calendar events show up on calendar
- ✓ No content is missing from Notion
- ✓ Status updates are accurate

**Next Workflows**:
- Monitor approvals and revisions
- Publish on scheduled dates
- Update status to "Published" after going live
- Use calendar for monthly content performance review

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Review emails failed to send (check Gmail API authentication)
- [ ] Scheduled dates are in the past (timezone issue)
- [ ] Review deadlines are unrealistic (< 12 hours)
- [ ] Calendar events don't appear on calendar
- [ ] Missing content fields (title, content, platform)

**Validation Checklist**:
1. Open Notion calendar; verify 5+ posts are visible
2. Check Gmail Sent folder; confirm review emails were sent
3. Open Cal.com or Google Calendar; verify events appear
4. Pick one scheduled post; verify date is realistic (not in past)
5. Check one reviewer email; verify content is readable and clear

**Anti-Patterns**:
- Do NOT schedule posts too close together (<24 hours)
- Do NOT send reviews without review deadlines
- Do NOT forget to update status after approval
- Do NOT mix review feedback in Notion (use email or linked comments)
- Do NOT publish without approval (respects review gate)

---

## Troubleshooting

**"Gmail API returns authentication error"**
→ Verify OAuth2 credentials are valid. Re-authenticate if needed: `gws auth login`.

**"Calendar events don't appear on Cal.com"**
→ Check Cal.com API key and timezone settings.

**"Scheduled dates are all wrong"**
→ Timezone mismatch. Ensure dates are in ISO format with correct timezone offset.

**"Review emails are going to spam"**
→ Add reviewers' email addresses to your contact list. Gmail will stop filtering them as spam.

---

## Next Steps After Completion

1. **Monitor** review status in Notion (check for approvals daily)
2. **Collect** feedback from reviewers
3. **Revise** any rejected posts (update content, move status back to Draft)
4. **Publish** approved posts on scheduled dates
5. **Track** post performance after publishing (engagement metrics, feedback)

**Downstreams**: Publishing platforms (LinkedIn, Substack, Twitter), performance tracking, next content cycle

