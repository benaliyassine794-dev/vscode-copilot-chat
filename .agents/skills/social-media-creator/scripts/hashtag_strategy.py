#!/usr/bin/env python3
"""Hashtag strategy generator.
Usage: python hashtag_strategy.py <platform> "<topic>"
Example: python hashtag_strategy.py instagram "fitness"
"""
import sys
import re

PLATFORM_RULES = {
    "instagram": {"range": (3, 10), "optimal": 7, "placement": "End of caption or first comment",
                  "note": "Use topic-specific tags; avoid mega-tags (>50M posts)"},
    "tiktok":    {"range": (3, 5),  "optimal": 4, "placement": "In caption",
                  "note": "Include #fyp only for genuinely watch-through content"},
    "twitter":   {"range": (1, 2),  "optimal": 1, "placement": "End of tweet",
                  "note": "More than 2 hashtags consistently hurts engagement"},
    "linkedin":  {"range": (3, 5),  "optimal": 4, "placement": "End of post, separate line",
                  "note": "Use hashtags with active followers, not just post volume"},
    "youtube":   {"range": (1, 3),  "optimal": 2, "placement": "Top of description; use tags field for 15 keywords",
                  "note": "First tag in the tags field = primary keyword (most important)"},
    "facebook":  {"range": (1, 3),  "optimal": 2, "placement": "End of post",
                  "note": "Less hashtag impact than other platforms"},
    "pinterest": {"range": (2, 5),  "optimal": 4, "placement": "End of pin description",
                  "note": "Descriptive keyword tags — not trend-chasing"},
    "snapchat":  {"range": (0, 2),  "optimal": 1, "placement": "Caption",
                  "note": "Minimal hashtag impact on Snapchat"},
}

TOPIC_SEEDS = {
    "fitness":    {"n": ["#homeworkout","#functionalfitness","#hiitworkout"], "m": ["#workout","#gym","#fitness"], "b": ["#health","#fit"]},
    "food":       {"n": ["#mealprep","#healthyeating","#homecooking"],       "m": ["#foodie","#recipe","#instafood"], "b": ["#food","#eat"]},
    "travel":     {"n": ["#solotravel","#budgettravel","#digitalnomad"],      "m": ["#travel","#travelblogger","#adventure"], "b": ["#explore","#vacation"]},
    "business":   {"n": ["#smallbusiness","#sidehustle","#startuplife"],      "m": ["#entrepreneur","#business","#success"], "b": ["#marketing","#money"]},
    "technology": {"n": ["#techstartup","#artificialintelligence","#webdev"],   "m": ["#tech","#programming","#software"], "b": ["#AI","#innovation"]},
    "fashion":    {"n": ["#slowfashion","#capsulewardrobe","#outfitinspo"],     "m": ["#ootd","#streetstyle","#fashionista"], "b": ["#fashion","#style"]},
    "beauty":     {"n": ["#skincareroutine","#naturalmakeup","#cleanbeauty"],   "m": ["#makeup","#skincare","#beauty"], "b": ["#selfcare","#glam"]},
    "marketing":  {"n": ["#contentmarketing","#socialmediatips","#seo"],        "m": ["#marketing","#socialmedia","#branding"], "b": ["#digitalmarketing"]},
    "education":  {"n": ["#elearning","#studytips","#onlinelearning"],          "m": ["#education","#learning","#teaching"], "b": ["#knowledge","#study"]},
    "gaming":     {"n": ["#indiegame","#gamingsetup","#pcgaming"],              "m": ["#gaming","#gamer","#gameplay"], "b": ["#video games","#twitch"]},
}

ALIASES = {"x": "twitter", "ig": "instagram", "yt": "youtube", "fb": "facebook", "tt": "tiktok"}


def find_seeds(topic: str) -> tuple:
    t = topic.lower()
    for key, seeds in TOPIC_SEEDS.items():
        if key in t or t in key:
            return seeds, key
    words = [w for w in re.findall(r"\w+", t) if len(w) > 3]
    return {
        "n": [f"#{words[0]}tips", f"#{t.replace(' ', '')}"] if words else ["#niche"],
        "m": [f"#{words[0]}" if words else "#topic", "#content", "#creator"],
        "b": ["#trending", "#viral"],
    }, "custom"


def run(platform: str, topic: str) -> None:
    p = ALIASES.get(platform.lower(), platform.lower())
    if p not in PLATFORM_RULES:
        print(f"Unknown platform '{platform}'. Available: {', '.join(sorted(PLATFORM_RULES))}")
        sys.exit(1)

    rules = PLATFORM_RULES[p]
    seeds, cat = find_seeds(topic)
    lo, hi = rules["range"]

    sep = "=" * 56
    print(f"\n{sep}")
    print(f"  HASHTAG STRATEGY — {p.upper()} × {topic.upper()}")
    print(sep)
    print(f"  Count: {lo}–{hi} (optimal: {rules['optimal']})")
    print(f"  Placement: {rules['placement']}")
    print(f"  Note: {rules['note']}")
    print(f"  Topic category matched: {cat}\n")

    if p == "instagram":
        print("  [NICHE — 100K–500K posts — highest ranking chance]")
        for t in seeds["n"][:3]: print(f"    {t}")
        print("  [MID — 500K–5M posts — reach + discovery balance]")
        for t in seeds["m"][:3]: print(f"    {t}")
        print("  [BROAD — use 1 max]")
        for t in seeds["b"][:1]: print(f"    {t}")
    elif p == "tiktok":
        combo = seeds["n"][:1] + seeds["m"][:2] + ["#fyp"]
        print("  Recommended mix:")
        for t in combo[:4]: print(f"    {t}")
    elif p in ("twitter", "x"):
        print(f"  Recommended (use only 1): {seeds['m'][0]}")
    else:
        combo = seeds["b"][:1] + seeds["m"][:2] + seeds["n"][:1]
        print("  Recommended:")
        for t in combo[:rules["optimal"]]: print(f"    {t}")

    print("\n  Research steps before using:")
    print("    1. Search each hashtag on the platform")
    print("    2. Check post volume (active but not oversaturated)")
    print("    3. Confirm top posts match your content quality/niche")
    print("    4. Swap off-niche tags for better alternatives")
    print("\n  Research tools: TikTok Creative Center | Flick.tech (IG) | RiteTag | All Hashtag\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python hashtag_strategy.py <platform> \"<topic>\"")
        sys.exit(1)
    run(sys.argv[1], " ".join(sys.argv[2:]))
