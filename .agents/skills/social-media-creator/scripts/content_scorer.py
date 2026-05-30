#!/usr/bin/env python3
"""Content quality scorer for social media captions and posts.
Usage: python content_scorer.py "<content_text>" <platform>
Returns 0-100 score with improvement suggestions.
"""
import sys
import re

PLATFORM_LIMITS = {
    "instagram": 2200, "tiktok": 2200, "twitter": 280, "x": 280,
    "facebook": 63206, "linkedin": 3000, "youtube": 5000,
    "pinterest": 500, "snapchat": 250,
}

OPTIMAL_RANGES = {
    "instagram": (138, 500), "tiktok": (100, 300), "twitter": (71, 140),
    "x": (71, 140), "linkedin": (500, 1000), "facebook": (100, 500),
    "youtube": (300, 1000), "pinterest": (100, 300), "snapchat": (50, 150),
}

HOOK_PATTERNS = [
    r"\bhow\s+to\b", r"\b\d+\s+(ways?|tips?|steps?|secrets?|mistakes?|things?|hacks?)\b",
    r"\bwhy\b.*\?", r"\bstop\b", r"\bpov\s*:", r"\bwait\b",
    r"\bmost\s+people\b", r"\bthe\s+truth\b", r"\bunpopular\s+opinion\b",
    r"\bi\s+(tried|tested|spent|made|earned|lost)\b", r"\bthis\s+(changed|ruined|saved)\b",
    r"\bwhat\s+nobody\b", r"\bsecret\b", r"\bmistake\b", r"\bwarning\b",
]

CTA_PATTERNS = [
    r"\b(follow|subscribe)\b", r"\b(comment|drop|reply)\b", r"\b(save|bookmark)\b",
    r"\b(share|send\s+this)\b", r"\b(like|double\s+tap)\b",
    r"\blink\s+in\s+(bio|description)\b", r"\bswipe\b", r"\bclick\b",
    r"\btag\s+(someone|a\s+friend)\b",
]

ENGAGEMENT_PATTERNS = [
    r"\bcomment\s+(below|your|a)\b", r"\b(agree|disagree)\?",
    r"\bwhat\s+do\s+you\b", r"\bhave\s+you\s+ever\b",
    r"\bam\s+i\s+the\s+only\b", r"\bwho\s+else\b", r"\btag\b",
]

HASHTAG_TARGETS = {
    "instagram": (3, 10), "tiktok": (3, 5), "twitter": (1, 2), "x": (1, 2),
    "linkedin": (3, 5), "facebook": (1, 3), "youtube": (0, 3),
    "pinterest": (2, 5), "snapchat": (0, 2),
}


def score(text: str, platform: str) -> dict:
    p = platform.lower().strip()
    scores, tips = {}, []
    char_limit = PLATFORM_LIMITS.get(p, 2200)
    length = len(text)
    opt_min, opt_max = OPTIMAL_RANGES.get(p, (50, 500))

    # Length (15pts)
    if length > char_limit:
        scores["length"] = 0
        tips.append(f"CRITICAL: exceeds {p} limit ({length}/{char_limit}). Trim {length - char_limit} chars.")
    elif opt_min <= length <= opt_max:
        scores["length"] = 15
    elif length < opt_min:
        scores["length"] = 8
        tips.append(f"Too short ({length} chars). Aim for {opt_min}–{opt_max} on {p}.")
    else:
        scores["length"] = 10
        tips.append(f"Slightly long ({length} chars). Optimal for {p}: {opt_min}–{opt_max}.")

    # Hook (25pts)
    first = text.strip().split("\n")[0][:150]
    hits = sum(1 for pat in HOOK_PATTERNS if re.search(pat, first, re.I))
    if hits >= 2:
        scores["hook"] = 25
    elif hits == 1:
        scores["hook"] = 15
        tips.append("Hook has pull but add a second signal (number, curiosity gap, or contradiction).")
    else:
        scores["hook"] = 5
        tips.append("Weak hook. Start with a number, bold claim, question, or pattern interrupt.")

    # CTA (20pts)
    cta_hits = sum(1 for pat in CTA_PATTERNS if re.search(pat, text, re.I))
    if cta_hits >= 2:
        scores["cta"] = 20
    elif cta_hits == 1:
        scores["cta"] = 12
        tips.append("Add a secondary CTA (e.g., 'Save this + Follow for more').")
    else:
        scores["cta"] = 0
        tips.append("No CTA. Add: 'Follow', 'Save this', 'Comment below', or 'Link in bio'.")

    # Engagement triggers (20pts)
    eng_hits = sum(1 for pat in ENGAGEMENT_PATTERNS if re.search(pat, text, re.I))
    if eng_hits >= 2:
        scores["engagement"] = 20
    elif eng_hits == 1:
        scores["engagement"] = 12
        tips.append("Add a direct question or debate prompt to invite more comments.")
    else:
        scores["engagement"] = 5
        tips.append("No engagement triggers. End with: 'Agree or disagree?' / 'What's your take?'")

    # Readability (10pts)
    lines = text.split("\n")
    avg_len = sum(len(l) for l in lines) / max(len(lines), 1)
    if len(lines) > 3 and avg_len < 80:
        scores["readability"] = 10
    elif len(lines) > 3:
        scores["readability"] = 7
    else:
        scores["readability"] = 4
        tips.append("Add line breaks every 1–2 sentences. Dense blocks reduce mobile readability.")

    # Hashtags (10pts)
    tags = re.findall(r"#\w+", text)
    ht_min, ht_max = HASHTAG_TARGETS.get(p, (2, 10))
    if ht_min <= len(tags) <= ht_max:
        scores["hashtags"] = 10
    elif len(tags) < ht_min:
        scores["hashtags"] = 5
        tips.append(f"Add hashtags. {p.title()} works best with {ht_min}–{ht_max} (found: {len(tags)}).")
    else:
        scores["hashtags"] = 5
        tips.append(f"Too many hashtags ({len(tags)}). {p.title()} optimal: {ht_min}–{ht_max}.")

    return {"total": sum(scores.values()), "breakdown": scores, "tips": tips, "platform": p, "chars": length}


def report(r: dict) -> None:
    t = r["total"]
    grade = "A — Excellent" if t >= 80 else "B — Good" if t >= 65 else "C — Average" if t >= 50 else "D — Needs Work" if t >= 35 else "F — Rewrite"
    stars = "★" * (t // 20) + "☆" * (5 - t // 20)
    sep = "=" * 50
    print(f"\n{sep}")
    print(f"  CONTENT SCORE — {r['platform'].upper()}")
    print(sep)
    print(f"  Overall: {t}/100  {stars}  ({grade})")
    print(f"  Characters: {r['chars']}\n")
    labels = [("length", "Length & Format", 15), ("hook", "Hook Strength", 25),
              ("cta", "Call to Action", 20), ("engagement", "Engagement Triggers", 20),
              ("readability", "Readability", 10), ("hashtags", "Hashtag Strategy", 10)]
    for key, label, max_s in labels:
        s = r["breakdown"].get(key, 0)
        bar = "█" * s + "░" * (max_s - s)
        print(f"  {label:<24} {s:3}/{max_s}  {bar}")
    if r["tips"]:
        print("\n  Improvements:")
        for i, tip in enumerate(r["tips"], 1):
            print(f"  {i}. {tip}")
    else:
        print("\n  No major issues. Content is well-optimized!")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python content_scorer.py \"<text>\" <platform>")
        sys.exit(1)
    report(score(sys.argv[1], sys.argv[2]))
