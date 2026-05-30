---
name: social-media-creator
description: >
  Builds and manages a complete social media presence across all major platforms
  with AI-powered content writing, video scripting, analytics, and audience growth.
  Use when the user wants to create channels, write posts, script videos, optimize
  titles and descriptions, analyze performance, or grow their audience on YouTube,
  TikTok, Instagram, X/Twitter, Facebook, LinkedIn, Snapchat, or Pinterest.
version: 1.0.0
---

# Social Media Creator

Full-stack social media assistant: channel setup, AI copywriting, video scripting,
SEO optimization, analytics, and growth across all major platforms.

## Phase 1 — Platform & Channel Setup

1. Ask: Which platforms? (YouTube / TikTok / Instagram / X / Facebook / LinkedIn / Snapchat / Pinterest)
2. Ask: Niche/topic, target audience, brand voice (professional / casual / educational / entertainment)
3. For each platform run: `python scripts/platform_checklist.py <platform>`
4. Follow `references/platform_setup_guide.md` for full per-platform optimization

**Channel essentials:** name, handle, keyword-rich bio, profile photo + banner (correct dimensions),
links, category, verification path, monetization requirements.

## Phase 2 — Content Creation

### Written Content (Posts, Captions, Threads, Articles)
1. Choose framework from `references/copywriting_frameworks.md`: AIDA / PAS / Hook-Story-CTA / BAB
2. Score draft: `python scripts/content_scorer.py "<text>" <platform>`
3. Platform-specific character limits and formats apply (see framework reference)

### Video Scripts
1. Structure: Hook (3s) → Value body → CTA — full templates in `references/video_production_guide.md`
2. Short-form (TikTok/Reels/Shorts): 15–90s vertical
3. Long-form (YouTube): 8–20min with chapters and timestamps

### Titles, Descriptions & Hashtags
1. SEO formulas, keyword placement, character budgets: `references/seo_and_optimization.md`
2. Hashtag strategy (niche/mid/broad mix): `python scripts/hashtag_strategy.py <platform> "<topic>"`
3. Thumbnail concept briefs: see video production guide

## Phase 3 — Analytics & Growth

1. Key metrics per platform: `references/analytics_and_growth.md`
2. Diagnose weak points: CTR, watch time %, engagement rate, follower velocity
3. Build 30-day posting calendar: `references/content_calendar.md`
4. Content repurposing: one video → 8+ pieces of content

## Platform Quick Reference

| Platform  | Best Format         | Peak Hours (local)   | Primary Metric    |
|-----------|---------------------|----------------------|-------------------|
| YouTube   | Long-form + Shorts  | Fri–Sun 14:00–16:00  | Watch time / CVR  |
| TikTok    | 15–90s vertical     | Daily 19:00–21:00    | FYP reach         |
| Instagram | Reels + Carousel    | Tue–Thu 11:00        | Saves + Shares    |
| X/Twitter | Threads + clips     | 08:00–09:00 / 17:00  | Impressions       |
| LinkedIn  | Articles + polls    | Tue–Thu 09:00        | Profile views     |
| Facebook  | Video + Lives       | Wed–Fri 13:00        | Organic reach     |
| Snapchat  | Stories + Spotlight | Daily 19:00–23:00    | Story views       |
| Pinterest | Pins + Idea Pins    | Sat–Sun 20:00–23:00  | Monthly viewers   |

## Trending & Virality Signals

- Trend sources: TikTok Creative Center, YouTube Trending, Google Trends, Exploding Topics
- Virality formula: emotional trigger + pattern interrupt + value promise + social proof
- Repurpose matrix: 1 video → clips (TikTok/Reels/Shorts) + thread (X) + carousel (IG/LinkedIn)
  + blog post (website) + pin (Pinterest) + story sequence (IG/Snap) + newsletter section
