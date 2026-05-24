# Money Mind – Zapier Automation Setup Guide

Complete setup guide for automating your YouTube channel workflow using Zapier.

---

## What Gets Automated

| Automation | Trigger | Action |
|-----------|---------|--------|
| Upload Reminder | Tue/Wed/Fri/Sun at 10 AM | Email to benaliyassine794@gmail.com |
| Weekly Analytics Report | Every Wednesday 9 AM | Email with YouTube stats |
| Production Checklist | Every Monday 8 AM | Email with full weekly plan |
| Subscriber Milestone Alert | Every day 12 PM | Email when milestone hit |

---

## Step 1 – Connect Your Accounts in Zapier

### Connect Gmail
1. Go to zapier.com → **My Apps**
2. Click **+ Add Connection** → search **Gmail**
3. Sign in with your Google account (benaliyassine794@gmail.com)
4. Allow Zapier access

### Connect YouTube
1. Go to zapier.com → **My Apps**
2. Click **+ Add Connection** → search **YouTube**
3. Sign in with your YouTube channel's Google account
4. Allow Zapier access

---

## Step 2 – Create the 4 Automated Zaps

### ZAP 1 – Weekly Production Checklist (Monday 8 AM)

**Trigger:** Schedule by Zapier
- Frequency: Every week
- Day of week: Monday
- Time: 8:00 AM

**Action:** Gmail – Send Email
- To: benaliyassine794@gmail.com
- Subject: `🗓 Money Mind – Weekly Production Plan`
- Body (paste this):
```
🗓 MONEY MIND – Weekly Production Plan

━━━━━━━━━━━━━━━━━━━━
This Week's Upload Schedule:

🎓 Tuesday 10:00 AM – Main Educational Video (12–18 min)
💡 Wednesday 10:00 AM – Quick Money Tip (5–7 min)
⚖️ Friday 10:00 AM – Comparison Video A vs B (10–15 min)
🔥 Sunday 10:00 AM – Myth-Busting / Story (8–12 min)

━━━━━━━━━━━━━━━━━━━━
Production Checklist:

🎬 4 Videos to Produce:
- [ ] Tuesday script written + voiceover recorded
- [ ] Wednesday script written + voiceover recorded
- [ ] Friday script written + voiceover recorded
- [ ] Sunday script written + voiceover recorded

🖼 4 Thumbnails to Design:
- [ ] Tuesday thumbnail (1280×720)
- [ ] Wednesday thumbnail (1280×720)
- [ ] Friday thumbnail (1280×720)
- [ ] Sunday thumbnail (1280×720)

✏️ 4 Metadata Sets to Write:
- [ ] 4 video titles (under 60 characters each)
- [ ] 4 descriptions (300+ words each)
- [ ] 4 sets of tags (10–15 tags each)

⚡ BATCH TIP: Record all 4 voiceovers in ONE session today!
Save time by scripting all 4 before you record anything.
```

---

### ZAP 2 – Tuesday Upload Reminder (10 AM)

**Trigger:** Schedule by Zapier
- Frequency: Every week
- Day of week: Tuesday
- Time: 10:00 AM

**Action:** Gmail – Send Email
- To: benaliyassine794@gmail.com
- Subject: `🎬 UPLOAD NOW – Tuesday Main Video | Money Mind`
- Body:
```
🎬 IT'S UPLOAD DAY – Tuesday Main Educational Video

Upload Checklist:
- [ ] Video file exported (1080p minimum)
- [ ] Thumbnail uploaded (1280×720 JPG)
- [ ] Title written (under 60 chars, keyword-rich)
- [ ] Description written (300+ words, timestamps, links)
- [ ] Tags added (10–15 tags)
- [ ] End screen set (subscribe + next video)
- [ ] Cards added (at 20% and 70% of video)
- [ ] Premiere time: 10:00 AM TODAY

Best Title Formulas:
📌 "How to [Achieve Goal] Without [Common Pain]"
📌 "[Number] Things About [Topic] No One Tells You"
📌 "The Truth About [Topic] (That Changes Everything)"

✅ Schedule your upload for 10:00 AM EXACTLY — consistency trains the algorithm.
```

---

### ZAP 3 – Wednesday Analytics Report + Upload Reminder (9 AM)

**Trigger:** Schedule by Zapier
- Frequency: Every week
- Day of week: Wednesday
- Time: 9:00 AM

**Action:** Gmail – Send Email
- To: benaliyassine794@gmail.com
- Subject: `📊 Weekly Analytics + Upload Reminder | Money Mind`
- Body:
```
📊 MONEY MIND – Wednesday Report

━━━ UPLOAD REMINDER ━━━
🕙 Upload your Quick Tip video at 10:00 AM today!

Quick Tip Checklist:
- [ ] 5–7 min video exported
- [ ] Thumbnail ready
- [ ] Scheduled for 10:00 AM

━━━ THIS WEEK'S GOALS ━━━
Review these benchmarks in YouTube Studio:

📈 CTR Target: 6–10%
⏱ Watch Duration Target: 50%+
👥 Subscribers This Week: Check growth trend
💬 Comments to Reply: Reply within 24 hours

━━━ ANALYTICS CHECKLIST ━━━
- [ ] Open YouTube Studio → Analytics
- [ ] Check top-performing video this week
- [ ] Note which thumbnail performed best
- [ ] Note which title formula got highest CTR
- [ ] Plan next week's content based on what's working

📌 TIP: Double down on whatever performed best this week.
The algorithm rewards consistency with your best content types.
```

---

### ZAP 4 – Friday + Sunday Upload Reminders

Create **two separate Zaps** (or use Filter by Zapier to handle both days):

**Friday Zap:**
- Trigger: Schedule → Friday 10:00 AM
- Action: Gmail → Send Email
- Subject: `⚖️ UPLOAD NOW – Friday Comparison Video | Money Mind`
- Body: Same format as Tuesday but for "Comparison Video (A vs B)"

**Sunday Zap:**
- Trigger: Schedule → Sunday 10:00 AM
- Action: Gmail → Send Email
- Subject: `🔥 UPLOAD NOW – Sunday Myth-Bust Video | Money Mind`
- Body: Same format as Tuesday but for "Myth-Busting / Story Video"

---

## Step 3 – Add YouTube Analytics (Optional Upgrade)

To include real stats in your Wednesday report:

1. In the Wednesday Zap, add a second action step before Gmail
2. Action: YouTube → **Get Channel Statistics**
3. Use the dynamic data from YouTube in your email body:
   - `{{subscribers}}` — current subscriber count
   - `{{total_views}}` — total channel views
   - `{{video_count}}` — total videos published

---

## Step 4 – Test Each Zap

1. Click **"Test Zap"** on each one
2. Check benaliyassine794@gmail.com for the test emails
3. Turn on each Zap (toggle at top right)

---

## Automation Schedule Summary

```
MONDAY    08:00 AM → Full production plan emailed
TUESDAY   10:00 AM → Upload reminder (Main Educational Video)
WEDNESDAY 09:00 AM → Analytics report + Quick Tip upload reminder
FRIDAY    10:00 AM → Upload reminder (Comparison Video)
SUNDAY    10:00 AM → Upload reminder (Myth-Bust Video)
```

---

## Upgrade Path

Once your channel grows to 1,000+ subscribers:

- **Add Zapier + YouTube → Google Sheets** to log weekly stats automatically
- **Add Zapier + YouTube → Slack/Discord** for real-time comment alerts
- **Upgrade to n8n** (your 5 JSON workflows are ready in `/n8n-workflows/`) for more complex logic including subscriber milestone celebrations

---

## Zapier Plan Required

| Feature | Free Plan | Starter ($20/mo) |
|---------|-----------|-----------------|
| Zaps | 5 | 20 |
| Schedule trigger | ✅ | ✅ |
| Multi-step Zaps | ❌ | ✅ |
| YouTube integration | ✅ | ✅ |
| Gmail integration | ✅ | ✅ |

**Recommendation:** The Free plan supports all 5 Zaps above. Start free, upgrade only when you need multi-step Zaps.
