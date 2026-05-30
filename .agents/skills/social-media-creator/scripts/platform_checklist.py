#!/usr/bin/env python3
"""Platform channel setup checklist.
Usage: python platform_checklist.py <platform>
Platforms: youtube, tiktok, instagram, twitter, facebook, linkedin, snapchat, pinterest
"""
import sys

CHECKLISTS = {
    "youtube": {
        "required": [
            "Channel name set (≤50 chars, keyword included naturally)",
            "Custom handle (@username) claimed",
            "Channel description written (keyword in first 100 chars)",
            "Channel art uploaded (2560×1440px)",
            "Profile photo uploaded (800×800px)",
            "Channel trailer created (45–90s, hook in first 5s)",
            "Channel tags added (Settings > Channel > Basic Info)",
            "Links section filled",
            "Channel category selected",
        ],
        "recommended": [
            "Featured sections configured",
            "Playlist structure created (1 playlist per topic)",
            "Monetization requirements reviewed",
            "End screen template saved",
        ],
    },
    "tiktok": {
        "required": [
            "Username consistent with other platforms",
            "Bio written (≤80 chars: keyword + emoji + CTA)",
            "Profile photo uploaded (200×200px min)",
            "Link in bio active",
            "Creator Account enabled (not Personal)",
            "Auto-captions turned ON",
        ],
        "recommended": [
            "TikTok Creative Center bookmarked for trends",
            "Duet/Stitch settings configured",
            "LIVE access plan noted (requires 1K followers)",
        ],
    },
    "instagram": {
        "required": [
            "Username set (keyword-searchable)",
            "Name field includes keyword (SEARCHABLE — not just handle)",
            "Bio written (≤150 chars, value line 1, CTA line 2)",
            "Profile photo uploaded (320×320px for best quality)",
            "Link in bio active",
            "Creator or Business account selected",
            "Content category set",
        ],
        "recommended": [
            "Highlights covers created (branded icons)",
            "Contact options configured (Business only)",
            "Shopping catalog linked (if applicable)",
        ],
    },
    "twitter": {
        "required": [
            "Display name set (≤50 chars)",
            "Handle (@username ≤15 chars)",
            "Bio written (≤160 chars with keyword)",
            "Header image uploaded (1500×500px)",
            "Profile photo uploaded (400×400px)",
            "Location field filled",
            "Website URL added",
        ],
        "recommended": [
            "Best tweet pinned to profile",
            "X Premium evaluated for verification",
            "Relevant Communities joined",
        ],
    },
    "facebook": {
        "required": [
            "Page name set",
            "Category selected (most specific)",
            "Username (@handle) claimed",
            "Short description written (≤255 chars with keywords)",
            "Cover photo uploaded (851×315px)",
            "Profile photo uploaded (170×170px)",
            "CTA button configured",
        ],
        "recommended": [
            "Long description written",
            "Meta Business Suite linked",
            "Facebook Group created or joined",
        ],
    },
    "linkedin": {
        "required": [
            "Headline written (≤220 chars, keyword-rich value statement)",
            "About section: hook in first 300 chars (visible before 'see more')",
            "Creator Mode enabled",
            "Profile photo (professional, high contrast)",
            "Banner image uploaded (1584×396px)",
        ],
        "recommended": [
            "Featured section configured with top posts",
            "Skills section: top 5 endorsed",
            "LinkedIn Newsletter started",
            "Company page specialties listed (≤20 keywords)",
        ],
    },
    "snapchat": {
        "required": [
            "Display name set (≤75 chars)",
            "Bio written (≤150 chars)",
            "Profile picture / Bitmoji configured",
            "Story visibility set to Public",
        ],
        "recommended": [
            "Spotlight submission format understood (9:16, 60s, no watermarks)",
            "Snapcode downloaded for cross-platform promotion",
        ],
    },
    "pinterest": {
        "required": [
            "Business account created (not personal)",
            "Business name set (keyword-friendly)",
            "About section written (≤160 chars)",
            "Website claimed and verified",
            "Profile photo uploaded (165×165px)",
            "Initial board structure created (≥5 boards)",
            "Board names are keyword-rich",
        ],
        "recommended": [
            "Rich Pins enabled",
            "Shopping catalog linked (if applicable)",
            "Idea Pins format reviewed",
        ],
    },
}

ALIASES = {
    "x": "twitter", "x/twitter": "twitter", "fb": "facebook",
    "ig": "instagram", "yt": "youtube", "tt": "tiktok",
    "snap": "snapchat", "pin": "pinterest",
}


def run_checklist(platform: str) -> None:
    key = ALIASES.get(platform.lower(), platform.lower())
    if key not in CHECKLISTS:
        print(f"Unknown platform '{platform}'.")
        print(f"Available: {', '.join(sorted(CHECKLISTS))}")
        sys.exit(1)

    items = CHECKLISTS[key]
    sep = "=" * 52
    print(f"\n{sep}")
    print(f"  {key.upper()} CHANNEL SETUP CHECKLIST")
    print(sep)

    print("\n[REQUIRED — complete before first post]")
    for i, label in enumerate(items["required"], 1):
        print(f"  {i:2}. [ ] {label}")

    print("\n[RECOMMENDED — complete within first week]")
    for i, label in enumerate(items["recommended"], 1):
        print(f"  {i:2}. [ ] {label}")

    req = len(items["required"])
    rec = len(items["recommended"])
    print(f"\n  Required: {req}  |  Recommended: {rec}  |  Total: {req + rec}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python platform_checklist.py <platform>")
        print(f"Platforms: {', '.join(sorted(CHECKLISTS))}")
        sys.exit(1)
    run_checklist(" ".join(sys.argv[1:]))
