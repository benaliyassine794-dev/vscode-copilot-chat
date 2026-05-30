---
name: social-media-creator
description: >
  Builds and manages a complete social media presence across all major platforms
  with AI-powered content writing, video scripting, analytics, audience growth,
  music and audio strategy, multilingual content in all world languages, and
  professional video editing and montage. Use when the user wants to create
  channels, write posts, script videos, select music, produce multilingual
  content, edit or montage videos, or grow an audience on any platform.
version: 1.1.0
---

# Social Media Creator

Full-stack social media assistant: channel setup, AI copywriting, video scripting,
music strategy, multilingual content, montage and editing, SEO, analytics, and
growth across all major platforms.

## Phase 1 — Platform & Channel Setup

1. Ask: Which platforms? (YouTube / TikTok / Instagram / X / Facebook / LinkedIn / Snapchat / Pinterest)
2. Ask: Niche/topic, target audience, language(s), brand voice (professional / casual / educational / entertainment)
3. For each platform run: `python scripts/platform_checklist.py <platform>`
4. See `references/platform_setup_guide.md` for full per-platform optimization

## Phase 2 — Content Creation

### Written Content (Posts, Captions, Threads)
1. Framework: `references/copywriting_frameworks.md` → AIDA / PAS / Hook-Story-CTA / BAB
2. Score: `python scripts/content_scorer.py "<text>" <platform>`

### Video Scripts
1. Hook (3s) → Value body → CTA — templates in `references/video_production_guide.md`
2. Short-form (TikTok/Reels/Shorts 15–90s) or long-form (YouTube 8–20min)

### Video Editing & Montage
1. Cuts, pacing, transitions, color grading, B-roll: `references/video_editing_montage.md`
2. Tools: CapCut (mobile) · DaVinci Resolve · Premiere Pro · Final Cut Pro
3. Platform-specific pacing: 0.5–2s cuts (TikTok) vs 3–5s cuts (YouTube)

### Music & Audio
1. Trending sounds per platform, royalty-free sources, licensing: `references/music_and_audio_guide.md`
2. Check platform audio features: `python scripts/music_platform_checker.py <platform>`
3. Audio branding: intro jingle, consistent BGM, voice-over tips

### Multilingual Content (All World Languages)
1. Translate + localize for target culture: `references/multilingual_content.md`
2. Format RTL/LTR: `python scripts/language_formatter.py "<text>" <lang_code>`
3. Top languages by platform reach: Arabic · Spanish · Hindi · French · Portuguese · Mandarin · German · Swahili · Indonesian + more

### Titles, Descriptions & Hashtags
1. SEO formulas + character budgets: `references/seo_and_optimization.md`
2. Hashtag mix: `python scripts/hashtag_strategy.py <platform> "<topic>"`

## Phase 3 — Analytics & Growth

1. Key metrics per platform: `references/analytics_and_growth.md`
2. 30-day content calendar: `references/content_calendar.md`
3. Repurposing: 1 video → 8+ pieces across all platforms

## Platform Quick Reference

| Platform  | Best Format         | Peak Hours (local)   | Primary Metric   |
|-----------|---------------------|----------------------|------------------|
| YouTube   | Long-form + Shorts  | Fri–Sun 14:00–16:00  | Watch time / CVR |
| TikTok    | 15–90s vertical     | Daily 19:00–21:00    | FYP reach        |
| Instagram | Reels + Carousel    | Tue–Thu 11:00        | Saves + Shares   |
| X/Twitter | Threads + clips     | 08:00–09:00 / 17:00  | Impressions      |
| LinkedIn  | Articles + polls    | Tue–Thu 09:00        | Profile views    |
| Facebook  | Video + Lives       | Wed–Fri 13:00        | Organic reach    |
| Snapchat  | Stories + Spotlight | Daily 19:00–23:00    | Story views      |
| Pinterest | Pins + Idea Pins    | Sat–Sun 20:00–23:00  | Monthly viewers  |

## Virality Formula

Emotional trigger + pattern interrupt + value promise + trending audio + social proof
