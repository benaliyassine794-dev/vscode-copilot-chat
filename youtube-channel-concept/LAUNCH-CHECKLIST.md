# Money Mind – Master Launch Checklist

**Channel:** Money Mind (@MoneyMindYT)
**Target launch date:** Week 1 scripts ready ✅

---

## ✅ COMPLETED

### Content — Video Scripts
- [x] Script 01: The Psychology of Money (Tue Week 1)
- [x] Script 02: Invest $100/Month (Wed Week 1)
- [x] Script 03: Renting vs Buying (Fri Week 1)
- [x] Script 04: Biggest Lie About Debt (Sun Week 1)
- [x] Script 05: Save $1,000 Emergency Fund in 30 Days (Wed Week 2)
- [x] Script 06: 800 vs 600 Credit Score (Fri Week 2)
- [x] Script 07: Biggest Myths About Index Funds (Sun Week 2)
- [x] Script 08: How to Negotiate Your Salary (Tue Week 3)
- [x] Script 09: Freelancing vs 9-to-5 (Fri Week 3)
- [x] Script 10: $1 Million by Age 40 (Tue Week 4)
- [x] Script 11: 50/30/20 Budget System (Wed Week 4)
- [x] Script 12: Buying vs Leasing a Car (Fri Week 4)
- [x] Script 13: Six-Figure Salary Myth (Sun Week 4)

### Strategy Documents
- [x] Channel strategy & content calendar
- [x] SEO keyword research & topic pipeline
- [x] Thumbnail design templates & brand guidelines
- [x] Zapier automation guide (manual setup instructions)

### n8n Automation Workflows
- [x] Workflow 01: Upload Reminder Scheduler (4x/week emails) — ID: v6TB1JsAFNEREu2E
- [x] Workflow 02: Production Checklist Generator — ID: (created)
- [x] Workflow 03: Analytics Report (weekly email) — ID: (created)
- [x] Workflow 06: Social Blaster (RSS → Facebook → Twitter → Gmail) — ID: IGzmTojZXKhSQACq
- [x] Workflow 07: AI Script Generator (NotebookLM alternative) — ID: VzWvHyltie984f2a

### Zapier Automation
- [x] Zapier skill created for YouTube + Gmail automation
- [x] Facebook posting action enabled
- [x] Gmail notification action enabled

---

## 🔲 PENDING — User Action Required

### CRITICAL: Connect Gmail in n8n (MUST DO FIRST)
**URL:** https://er12f6.app.n8n.cloud/credentials

Steps:
1. Go to Credentials → Add Credential
2. Search "Gmail OAuth2"
3. Follow Google OAuth2 flow to authorize benaliyassine794@gmail.com
4. Name it exactly: `Gmail OAuth2`
5. All 3 scheduling workflows will auto-activate after this

**Workflows waiting:** Upload Reminder, Production Checklist, Analytics Report

---

### Connect Social Blaster (After Gmail)
**Workflow:** Social Blaster — ID: IGzmTojZXKhSQACq
**URL:** https://er12f6.app.n8n.cloud/workflow/IGzmTojZXKhSQACq

Required credentials to add:
1. **YouTube Channel ID** — Find at: youtube.com → Your Channel → URL bar: `?channel_id=XXXXX`
   - Edit workflow file `06-social-blaster.json`: replace `YOUR_CHANNEL_ID`

2. **Facebook Graph API credential** — n8n Credentials → Facebook Graph API
   - Get token from: developers.facebook.com → Your App → Access Token
   - Edit workflow: replace `YOUR_FACEBOOK_PAGE_ID`

3. **Twitter OAuth2 credential** — n8n Credentials → Twitter OAuth2
   - Requires Twitter Developer Account: developer.twitter.com
   - Create App → OAuth 2.0 → copy Client ID + Client Secret into n8n

4. **Gmail OAuth2** (same credential as above, already connected after step 1)

---

### Reconnect Gmail on Zapier
**URL:** https://mcp.zapier.com/mcp/servers/4a31047f-4521-4913-ab5c-ce17551c13fd/config
- Gmail action was halted during testing
- Reconnect Gmail account in Zapier dashboard
- Re-test with a YouTube upload event

---

### YouTube Channel Setup
- [ ] Create YouTube channel: @MoneyMindYT
- [ ] Upload channel banner (1280×720 thumbnail style, navy+gold branding)
- [ ] Write channel description (use Money Mind tagline: "Learn to Think Like Money")
- [ ] Add channel links (future: website, social media)
- [ ] Enable channel monetization eligibility tracking
- [ ] Set default upload settings (category: Education, language: English)

---

### Animation Production
- [ ] Commission or create 2D character design (see thumbnail-design-templates.md for specs)
- [ ] Create expression library (7 core expressions listed in thumbnail doc)
- [ ] Build prop library (money, charts, house, car, etc.)
- [ ] Produce intro animation (Money Mind logo reveal, 3–5 seconds)
- [ ] Produce outro animation (subscribe CTA, 5 seconds)
- [ ] Produce lower-third template (for name/stats on-screen)

**Tools to use:**
- Adobe After Effects + Character Animator (professional)
- Vyond (subscription, easiest for 2D business animation)
- Doodly (simpler whiteboard style)
- Canva Presentations (basic, lowest cost)

---

### Recording & Production Setup
- [ ] Record voiceovers for Script 01 (The Psychology of Money)
- [ ] Sync voiceover with animation for Script 01
- [ ] Add music bed (royalty-free, neutral/motivational — search Epidemic Sound or Artlist)
- [ ] Export final video: 1080p, 60fps, .mp4
- [ ] Produce custom thumbnail for Script 01 (use Template 2: Main Educational)

---

## 📋 WEEKLY PRODUCTION WORKFLOW (Ongoing)

### Thursday (1 week before upload)
- [ ] Finalize 4 scripts for next week
- [ ] Produce 4 thumbnails (batch)
- [ ] Record 4 voiceovers (batch)

### Friday–Sunday
- [ ] Animate 4 videos (or send to animator)
- [ ] Add music + sound effects
- [ ] Export + quality check

### Monday
- [ ] Upload all 4 videos as "Scheduled" in YouTube Studio
- [ ] Set publish times: Tue/Wed/Fri/Sun at 10:00 AM
- [ ] Add all metadata: title, description, tags, thumbnail, chapters, end screens

### Tuesday–Sunday
- [ ] n8n reminder emails auto-send ✅
- [ ] Social Blaster auto-posts to Facebook + Twitter on upload ✅ (after credentials connected)
- [ ] Weekly analytics report emails every Monday ✅

---

## 💰 BUDGET OVERVIEW

| Item | Monthly Cost | Notes |
|------|-------------|-------|
| n8n cloud | $20/month | Already set up |
| Zapier | $29/month | Free tier limited |
| Animation software | $49–$99/month | Vyond or After Effects |
| Music license | $15–$20/month | Epidemic Sound |
| Canva Pro | $13/month | Thumbnail design |
| Stock footage | $0 | All animated, no stock |
| **Total** | **~$126–$181/month** | |

**Revenue projection:**
- 0–1,000 subscribers: $0 (not monetized)
- 1,000 subs + 4,000 watch hours: YouTube Partner eligible ($2–$5 CPM)
- At 10,000 subscribers: ~$500–$1,000/month from AdSense
- At 100,000 subscribers: ~$3,000–$8,000/month from AdSense + sponsors

---

## 📞 IMMEDIATE ACTION SUMMARY

**Do these 3 things today:**

1. **Connect Gmail in n8n** → https://er12f6.app.n8n.cloud/credentials
   (Unlocks all 3 scheduling workflows)

2. **Create YouTube channel** → youtube.com → Create Channel → @MoneyMindYT
   (Needed to get Channel ID for Social Blaster)

3. **Open the AI Script Generator** → n8n workflow VzWvHyltie984f2a → copy the chat URL
   (Paste any book excerpt → get a full Money Mind script in seconds)

**Everything else is ready and waiting for these 3 steps.**
