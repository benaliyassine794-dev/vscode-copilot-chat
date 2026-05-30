#!/usr/bin/env python3
"""Music and audio feature checker per social media platform.
Usage: python music_platform_checker.py <platform>
"""
import sys

PLATFORM_AUDIO = {
    "tiktok": {
        "library": "500K+ licensed tracks via TikTok Sounds library",
        "trending_source": "TikTok Creative Center → Trending → Sounds",
        "features": [
            "Duet/Stitch with original audio (piggyback on viral sounds)",
            "Voiceover tool (built-in TTS in 10+ languages)",
            "Sound effects library",
            "Volume control: original vs added sound",
            "Auto-generated captions from audio",
        ],
        "restrictions": "Some tracks limited by region; commercial accounts have reduced library",
        "strategy": "Use trending sounds 1-3 days old for max FYP boost",
        "royalty_free_tip": "Use Epidemic Sound or Artlist tracks uploaded as original audio",
    },
    "instagram": {
        "library": "Large licensed library (personal/creator); limited for Business accounts",
        "trending_source": "Reels → Browse → Audio → Trending",
        "features": [
            "Music sticker for Stories",
            "Audio overlay for Reels",
            "Original audio naming (make your sound searchable)",
            "Collab audio to ride viral sounds",
            "Lyrics display for Stories music",
        ],
        "restrictions": "Business accounts: switch to Creator account for full music access",
        "strategy": "Name your original audio with a keyword — becomes discoverable if it goes viral",
        "royalty_free_tip": "Upload royalty-free tracks as original audio on your Creator account",
    },
    "youtube": {
        "library": "YouTube Audio Library — free royalty-free music + SFX",
        "trending_source": "YouTube Shorts → trending audio section",
        "features": [
            "Audio Library in YouTube Studio (free download)",
            "Shorts trending audio (same mechanic as TikTok)",
            "Content ID: automatic copyright detection",
            "Music Policies: check before using any commercial track",
            "Subscription music via YouTube Premium content",
        ],
        "restrictions": "Commercial music triggers Content ID → mute, claim, or revenue share",
        "strategy": "Use YouTube Audio Library for long-form; use trending Shorts audio for discovery",
        "royalty_free_tip": "Epidemic Sound, Artlist, and Musicbed are YouTube-safe with subscription",
    },
    "facebook": {
        "library": "Sound Collection in Meta Creator Studio",
        "trending_source": "Reels → Explore → Audio trending tab",
        "features": [
            "Sound Collection: royalty-free tracks for Pages",
            "Shared audio library with Instagram Reels",
            "Live audio (licensed through Facebook agreements)",
            "Lip sync / audio duet on Reels",
        ],
        "restrictions": "Facebook Live music licensing is limited; some tracks blocked for live streams",
        "strategy": "Use Reels audio shared from Instagram for cross-platform consistency",
        "royalty_free_tip": "Download from Sound Collection before recording — rights pre-cleared",
    },
    "linkedin": {
        "library": "No built-in music library",
        "trending_source": "N/A — not applicable",
        "features": [
            "Background audio in uploaded videos (royalty-free only)",
            "Clear voice-over is more important than music here",
        ],
        "restrictions": "Copyright applies; no safe harbor — use only licensed audio",
        "strategy": "Focus on clean voice-over; subtle instrumental BGM at -25 dB if any",
        "royalty_free_tip": "Pixabay Music or YouTube Audio Library tracks safe for LinkedIn use",
    },
    "snapchat": {
        "library": "Licensed music library in Snap Sounds",
        "trending_source": "Snap → Sounds → Trending",
        "features": [
            "Snap Sounds: add music to Stories and Spotlight",
            "Trending sounds for Spotlight discovery boost",
            "Music sticker: shareable music moment",
        ],
        "restrictions": "Spotlight: no other platform watermarks; audio from other apps may cause issues",
        "strategy": "Use trending Snap Sounds for Spotlight submissions to improve reach",
        "royalty_free_tip": "Use Snap's own library — pre-cleared for the platform",
    },
    "pinterest": {
        "library": "Licensed music for Idea Pins (built-in)",
        "trending_source": "N/A — music is secondary on Pinterest",
        "features": [
            "Background music for Idea Pins",
            "Voice-over recording in Idea Pin editor",
        ],
        "restrictions": "Limited music options; focus on visuals over audio",
        "strategy": "Use calm, aspirational instrumental music matching pin aesthetic",
        "royalty_free_tip": "Artlist or Musicbed tracks work well for Pinterest Idea Pins",
    },
    "twitter": {
        "library": "No built-in music library",
        "trending_source": "N/A",
        "features": [
            "Video uploads: royalty-free audio only",
            "Twitter Spaces: live audio rooms (no music — copyright risk)",
        ],
        "restrictions": "Twitter enforces copyright on videos; Twitter Spaces music violates ToS",
        "strategy": "Use voice-over or ambient SFX; avoid recognizable commercial music in tweets",
        "royalty_free_tip": "Pixabay Music CC0 tracks are safest for X/Twitter uploads",
    },
}

ALIASES = {
    "x": "twitter", "ig": "instagram", "yt": "youtube",
    "fb": "facebook", "tt": "tiktok", "snap": "snapchat", "pin": "pinterest",
}

ROYALTY_FREE_SOURCES = [
    ("YouTube Audio Library", "Free",     "studio.youtube.com/channel/music"),
    ("Epidemic Sound",       "$15/mo",    "epidemicsound.com"),
    ("Artlist",              "$199/yr",   "artlist.io"),
    ("Pixabay Music",        "Free",      "pixabay.com/music"),
    ("Uppbeat",              "Free+Pro",  "uppbeat.io"),
    ("Bensound",             "Free/Paid", "bensound.com"),
    ("Free Music Archive",   "Free",      "freemusicarchive.org"),
    ("Soundstripe",          "$16/mo",    "soundstripe.com"),
]


def run(platform: str) -> None:
    key = ALIASES.get(platform.lower(), platform.lower())
    if key not in PLATFORM_AUDIO:
        print(f"Unknown platform '{platform}'.")
        print(f"Available: {', '.join(sorted(PLATFORM_AUDIO))}")
        sys.exit(1)

    data = PLATFORM_AUDIO[key]
    sep = "=" * 56
    print(f"\n{sep}")
    print(f"  MUSIC & AUDIO GUIDE — {key.upper()}")
    print(sep)
    print(f"\n  Library:         {data['library']}")
    print(f"  Trending source: {data['trending_source']}")
    print(f"  Strategy:        {data['strategy']}")
    print(f"  Restrictions:    {data['restrictions']}")
    print(f"  Royalty-free tip: {data['royalty_free_tip']}")
    print("\n  Platform Audio Features:")
    for feat in data["features"]:
        print(f"    • {feat}")
    print("\n  Royalty-Free Music Sources:")
    print(f"  {'Source':<22} {'Cost':<12} {'URL'}")
    print("  " + "-" * 52)
    for name, cost, url in ROYALTY_FREE_SOURCES:
        print(f"  {name:<22} {cost:<12} {url}")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python music_platform_checker.py <platform>")
        print(f"Platforms: {', '.join(sorted(PLATFORM_AUDIO))}")
        sys.exit(1)
    run(" ".join(sys.argv[1:]))
