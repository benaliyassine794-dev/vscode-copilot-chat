#!/usr/bin/env python3
"""Language formatter for multilingual social media content.
Usage:
  python language_formatter.py "<text>" <lang_code>
  python language_formatter.py --list

Examples:
  python language_formatter.py "Hello world" ar
  python language_formatter.py --list
"""
import sys

LANGUAGES = {
    # code: (name, direction, script, platform_notes)
    "ar": ("Arabic",     "RTL", "Arabic",   "Massive MENA audience. Use Arabic hashtags alongside English."),
    "he": ("Hebrew",     "RTL", "Hebrew",   "Israel market. RTL text on all platforms."),
    "fa": ("Farsi",      "RTL", "Arabic",   "Iran, Afghanistan. Use Persian-specific fonts."),
    "ur": ("Urdu",       "RTL", "Nastaliq", "Pakistan + India Urdu speakers."),
    "ps": ("Pashto",     "RTL", "Arabic",   "Afghanistan, Pakistan border regions."),
    "en": ("English",    "LTR", "Latin",    "Global reach. Use as base language."),
    "es": ("Spanish",    "LTR", "Latin",    "2nd largest YouTube audience. LATAM + Spain."),
    "fr": ("French",     "LTR", "Latin",    "France + 30 African countries. High LinkedIn engagement."),
    "pt": ("Portuguese", "LTR", "Latin",    "Brazil = #4 TikTok market. Use Brazilian Portuguese (pt-BR)."),
    "hi": ("Hindi",      "LTR", "Devanagari","India = YouTube's largest market. High growth."),
    "bn": ("Bengali",    "LTR", "Bengali",  "Bangladesh + West Bengal, India."),
    "zh": ("Mandarin",   "LTR", "Chinese",  "Douyin (TikTok China) separate platform. Use for diaspora."),
    "ja": ("Japanese",   "LTR", "Kanji/Kana","Top X/Twitter market. Anime/tech content thrives."),
    "ko": ("Korean",     "LTR", "Hangul",   "K-content global wave. Beauty, music, food niches."),
    "de": ("German",     "LTR", "Latin",    "Germany, Austria, Switzerland. High LinkedIn use."),
    "ru": ("Russian",    "LTR", "Cyrillic", "Russia + CIS. VK and Telegram dominant; YouTube strong."),
    "id": ("Indonesian", "LTR", "Latin",    "Indonesia = top 5 TikTok market. Fast growth."),
    "tr": ("Turkish",    "LTR", "Latin",    "Turkey + Central Asia diaspora."),
    "sw": ("Swahili",    "LTR", "Latin",    "East Africa: Kenya, Tanzania, Uganda. Fastest-growing."),
    "th": ("Thai",       "LTR", "Thai",     "Thailand. Facebook + TikTok heavy market."),
    "vi": ("Vietnamese", "LTR", "Latin",    "Vietnam. Explosive TikTok + YouTube growth."),
    "ha": ("Hausa",      "LTR", "Latin",    "West Africa: Nigeria, Niger, Ghana."),
    "yo": ("Yoruba",     "LTR", "Latin",    "Nigeria. Creator economy growing rapidly."),
    "am": ("Amharic",    "LTR", "Ge'ez",    "Ethiopia + Ethiopian diaspora."),
    "nl": ("Dutch",      "LTR", "Latin",    "Netherlands + Belgium."),
    "pl": ("Polish",     "LTR", "Latin",    "Poland + Polish diaspora."),
    "uk": ("Ukrainian",  "LTR", "Cyrillic", "Ukraine + diaspora. High growth post-2022."),
    "it": ("Italian",    "LTR", "Latin",    "Italy. Fashion, food, travel niches."),
    "ms": ("Malay",      "LTR", "Latin",    "Malaysia, Brunei, Singapore."),
    "ta": ("Tamil",      "LTR", "Tamil",    "Tamil Nadu India + Sri Lanka + diaspora."),
}

PLATFORM_CHAR_LIMITS = {
    "instagram": 2200, "tiktok": 2200, "twitter": 280,
    "linkedin": 3000, "facebook": 63206, "youtube": 5000,
    "pinterest": 500,
}

RTL_LANGUAGES = {code for code, (_, direction, _, _) in LANGUAGES.items() if direction == "RTL"}


def format_text(text: str, lang_code: str) -> None:
    code = lang_code.lower().strip()
    if code not in LANGUAGES:
        print(f"Unknown language code '{lang_code}'.")
        print("Run with --list to see all supported languages.")
        sys.exit(1)

    name, direction, script, notes = LANGUAGES[code]
    is_rtl = direction == "RTL"
    char_count = len(text)

    sep = "=" * 56
    print(f"\n{sep}")
    print(f"  LANGUAGE FORMATTER — {name.upper()} ({code.upper()})")
    print(sep)
    print(f"  Direction: {direction}  |  Script: {script}")
    print(f"  Market notes: {notes}")
    print(f"  Character count: {char_count}")

    if is_rtl:
        print("\n  RTL Formatting (apply in video editing + captions):")
        print("    • Text overlay: RIGHT-align all text")
        print("    • Subtitles: enable RTL mode in CapCut / Premiere / DaVinci")
        print("    • Caption opener: add RTL marker (‫) before text if platform needs it")
        print("    • Numbers stay LTR even inside RTL text")
        print("    • Punctuation: question mark placed on LEFT in Arabic (؟)")
        print(f"\n  Your text ({direction}):")
        print(f"    {chr(0x202B)}{text}")
    else:
        print(f"\n  Your text ({direction}):")
        print(f"    {text}")

    print("\n  Platform character limit check:")
    for platform, limit in PLATFORM_CHAR_LIMITS.items():
        status = "OK" if char_count <= limit else f"OVER by {char_count - limit}"
        bar = "▓" if char_count <= limit else "░"
        print(f"    {platform:<12} {char_count:>5}/{limit:<6} {bar} {status}")

    print("\n  Translation tools recommended:")
    if code in ("ar", "he", "fa", "ur"):
        print("    DeepL (good Arabic support) + native speaker review")
    elif code in ("zh", "ja", "ko"):
        print("    DeepL or ChatGPT + native speaker review for CJK languages")
    elif code in ("sw", "ha", "yo", "am"):
        print("    Google Translate + LOCAL native speaker review (AI quality lower for African languages)")
    else:
        print("    DeepL (highest quality for this language) + native speaker review")
    print()


def list_languages() -> None:
    sep = "=" * 70
    print(f"\n{sep}")
    print("  SUPPORTED LANGUAGES")
    print(sep)
    print(f"  {'Code':<6} {'Language':<14} {'Dir':<5} {'Script':<12} {'Key Market'}")
    print("  " + "-" * 64)
    for code, (name, direction, script, notes) in sorted(LANGUAGES.items(), key=lambda x: x[1][0]):
        market = notes.split(".")[0]
        print(f"  {code:<6} {name:<14} {direction:<5} {script:<12} {market}")
    print(f"\n  Total: {len(LANGUAGES)} languages | RTL: {len(RTL_LANGUAGES)} ({', '.join(sorted(RTL_LANGUAGES))})\n")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python language_formatter.py \"<text>\" <lang_code>")
        print("       python language_formatter.py --list")
        sys.exit(0)
    if sys.argv[1] == "--list":
        list_languages()
    elif len(sys.argv) >= 3:
        format_text(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python language_formatter.py \"<text>\" <lang_code>")
        sys.exit(1)
