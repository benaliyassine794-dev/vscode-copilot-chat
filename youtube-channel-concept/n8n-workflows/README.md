# Money Mind – n8n Automation Workflows

5 ready-to-import n8n workflows that automate your entire YouTube channel.

---

## Workflows Overview

| # | File | Trigger | What It Does |
|---|------|---------|-------------|
| 1 | `01-upload-reminder.json` | Tue/Wed/Fri/Sun at 10 AM | Reminds you to upload with full checklist |
| 2 | `02-weekly-analytics-report.json` | Every Wednesday 9 AM | Pulls YouTube stats + sends weekly report |
| 3 | `03-comment-monitor.json` | Every 2 hours | Alerts when popular comments need a reply |
| 4 | `04-production-checklist.json` | Every Monday 8 AM | Sends the full weekly production plan |
| 5 | `05-subscriber-milestone.json` | Every day at noon | Tracks subs + celebrates milestones |

---

## Setup Instructions

### Step 1 – Install n8n
```bash
# Option A: Docker (recommended)
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n

# Option B: npm
npm install n8n -g
n8n start
```
Then open: `http://localhost:5678`

---

### Step 2 – Connect YouTube API

1. Go to **Google Cloud Console** → Create a project
2. Enable **YouTube Data API v3**
3. Create **OAuth 2.0 credentials**
4. In n8n → Settings → Credentials → Add **YouTube OAuth2**
5. Paste your Client ID and Client Secret
6. Authorize with your YouTube channel account

---

### Step 3 – Set Up Discord Webhook (for notifications)

1. Open your Discord server
2. Go to a channel → **Edit Channel** → **Integrations** → **Webhooks**
3. Click **New Webhook** → Copy the webhook URL
4. In each workflow, replace:
   ```
   https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN
   ```
   with your actual webhook URL

> **Don't use Discord?** Replace the Discord HTTP Request node with:
> - **Gmail node** → sends email instead
> - **Telegram node** → sends Telegram message
> - **Slack node** → sends Slack message

---

### Step 4 – Import Each Workflow

1. Open n8n → Click **"+"** → **Import from file**
2. Select each `.json` file one by one
3. After import, click **"Activate"** toggle on each workflow

---

### Step 5 – Configure Workflow 03 (Comment Monitor)

In `03-comment-monitor.json`, replace `YOUR_LATEST_VIDEO_ID` with your actual video ID.

You can find the video ID in the YouTube URL:
```
https://www.youtube.com/watch?v=VIDEO_ID_HERE
```

Update this manually after each new upload, or upgrade to auto-fetch latest video ID.

---

## Automation Schedule Summary

```
MONDAY    08:00 AM → Weekly production plan sent
TUESDAY   10:00 AM → Upload reminder (Main Video)
WEDNESDAY 09:00 AM → Weekly analytics report
WEDNESDAY 10:00 AM → Upload reminder (Quick Tip)
FRIDAY    10:00 AM → Upload reminder (Comparison Video)
SUNDAY    10:00 AM → Upload reminder (Myth-Bust Video)
DAILY     12:00 PM → Subscriber count + milestone check
EVERY 2H            → Comment monitor (popular comments)
```

---

## Customization Tips

### Change Notification Platform
Replace the `HTTP Request (Discord)` node with any of these n8n nodes:
- `Gmail` – send to your email
- `Telegram` – send to Telegram bot
- `Slack` – send to Slack channel
- `WhatsApp Business` – send to WhatsApp

### Add Google Sheets Logging
Add a **Google Sheets** node after the analytics node to log weekly stats automatically into a spreadsheet for trend tracking.

### Auto-Post Community Tab Update
Use the **YouTube** node with operation `Insert` on resource `communityPost` to auto-post a Community Tab teaser when a new video is uploaded.
