"""Syllable counting for Headlines box timing (Headlines_Master_Rules_Structure.txt, Section B item 1a).

seconds = syllables / 4.4, written to two decimals, no rounding up, no hold allowance.
The override table merges syl.py (Headlines scripts folder, 25 Sep 2026) and the 26 Sep fill script.
Add a word to OVR when a pronunciation check shows the heuristic is wrong; never guess boxes from words per second.
"""
import re

OVR = {
    "ai": 2, "a.i.": 2, "ai's": 2, "xi": 1, "jinping": 2, "akamai": 3, "anthropic": 3, "salesforce's": 3,
    "salesforce": 2, "oracle": 3, "waymo's": 2, "waymo": 2, "alphafold": 3, "deepmind's": 2, "netflix's": 3,
    "wonka": 2, "gene": 1, "wilder's": 2, "ghoulish": 2, "deepseek's": 2, "deepseek": 2, "mexico": 3,
    "pipeline": 2, "twenty-seven": 3, "seventy": 3, "eighty-two": 3, "hijack": 2, "customer": 3, "database": 3,
    "prepare": 2, "pandemic": 3, "attorneys": 3, "general": 3, "overriding": 4, "states'": 1, "reviewer": 3,
    "ghoulishly": 3, "structures": 2, "flaws": 1, "fixed": 1, "leader": 2, "control": 2, "specific": 3,
    "offered": 2, "president": 3, "nations": 2, "billion": 2, "dollar": 2, "computing": 3, "company": 3,
    "shares": 1, "jumped": 1, "percent": 2, "researchers": 3, "showed": 1, "hidden": 2, "agents": 2, "steal": 1,
    "warned": 1, "delay": 2, "payments": 2, "center": 2, "because": 2, "slipped": 1, "driverless": 3, "driven": 2,
    "hundred": 2, "million": 2, "miles": 1, "injury": 3, "crashes": 2, "drivers": 2, "protein": 2, "virus": 2,
    "thousand": 2, "predicted": 3, "pairs": 1, "scientists": 3, "twenty-six": 3, "asked": 1, "congress": 2,
    "regulate": 3, "without": 2, "own": 1, "laws": 1, "critics": 2, "panned": 1, "uses": 2, "copy": 2, "voice": 1,
    "called": 1, "also": 2, "full": 1, "report": 2, "revenue": 3, "tops": 1, "factory": 3, "robots": 2, "record": 2,
    "five": 1, "bigger": 2, "picture": 2, "money": 2, "keeps": 1, "flowing": 2, "power": 2, "delays": 2,
    "costlier": 3, "debt": 1, "testing": 2, "eleven": 3, "point": 1, "six": 1, "seven-year": 3, "deal": 1, "rent": 1,
    "cloud": 1, "whose": 1, "about": 2, "twenty": 2, "white": 1, "house": 1, "models": 2, "british": 2, "testers": 2,
    "holds": 1, "new": 1, "hit": 1, "us": 2, "openai": 4, "ftc": 3, "qwen": 1, "skydio": 3, "skydios": 3, "nethack": 2,
    "microsoft": 3, "copilot": 3, "autopilot": 4, "gigawatts": 3, "capacity": 4, "operating": 4, "companies": 3,
    "politics": 3, "appeals": 2, "pentagons": 3, "defense": 2, "systems": 2, "reportedly": 4, "earlier": 3,
    "dozens": 2, "outside": 2, "computer": 3, "months": 1, "analysts": 3, "expansion": 3, "centres": 2, "launches": 2,
    "patrol": 2, "catches": 2, "returns": 2, "rebuilt": 2, "around": 2, "working": 2, "youre": 1, "science": 2,
    "particle": 3, "physics": 2, "calculation": 4, "human": 2, "reaching": 2, "physicists": 3, "federal": 3,
    "commission": 3, "independent": 4, "actors": 2, "cannot": 2, "lighter": 2, "gamings": 2, "games": 1,
    "hardest": 2, "attempt": 2, "alibabas": 4, "ninety": 2, "states": 1, "prices": 2, "risen": 2, "blacklist": 2,
    "broke": 1, "groups": 1, "those": 1, "research": 2, "nvidia": 3, "google": 2, "meta": 2, "apple": 2,
    "amazon": 3, "tesla": 2, "huawei": 3, "alibaba": 4, "tiktok": 2, "chatgpt": 4, "gemini": 3, "claude": 1,
    "headlines": 2, "ninety": 2, "seconds": 2, "coverage": 3, "tomorrow": 3, "tuning": 2,
}


def word_syllables(token: str) -> int:
    x = token.lower().strip(".,:;!?\"'()[]")
    if not x:
        return 0
    if x in OVR:
        return OVR[x]
    if x.endswith("s") and x[:-1] in OVR:  # possessive or plural of a listed word: Salesforce's -> 3, Waymo's -> 2
        return OVR[x[:-1]] + (1 if x[:-1].endswith(("s", "x", "z", "ch", "sh", "ce", "ge")) else 0)
    if "-" in x:
        return sum(word_syllables(p) for p in x.split("-"))
    if x.isupper() and len(x) <= 4 and token.isupper():
        return len(x)
    if len(x) > 3 and x.endswith("s") and not x.endswith(("ss", "us", "is", "ies", "oes")):
        stem = x[:-1]
        if not (x.endswith("es") and stem[:-1].endswith(("s", "x", "z", "ch", "sh", "g", "c"))):
            x = stem  # plural or third person: rules -> rule, makes -> make; changes and places keep the spoken -es
    v = re.findall(r"[aeiouy]+", x)
    n = len(v)
    syllabic_le = x.endswith("le") and len(x) > 2 and x[-3] not in "aeiou"  # table, little: yes; rule, mile: no
    if x.endswith("e") and n > 1 and not (x.endswith(("ee", "ye")) or syllabic_le):
        n -= 1
    if x.endswith("ed") and not x.endswith(("ted", "ded")) and n > 1:
        n -= 1
    return max(1, n)


def count(text: str, cues: dict | None = None) -> int:
    """Count syllables of a complete spoken line. cues maps a written token to its spoken form."""
    t = text
    for cue, real in (cues or {}).items():
        t = t.replace(cue, real)
    t = t.replace("'", "").replace("’", "")
    total = 0
    for token in re.findall(r"[A-Za-z][A-Za-z'\-]*|\d+", t):
        if token.isdigit():
            total += number_syllables(int(token))
        else:
            total += word_syllables(token)
    return total


def number_syllables(n: int) -> int:
    """Rough spoken length of a digit string; scripts should spell numbers as words (Section B item 3)."""
    if n < 20:
        return 1 if n in (0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12) else 2
    if n < 100:
        return 2 if n % 10 == 0 else 3
    return 3 + number_syllables(n % 100)


def box_seconds(syllables: int, rate: float = 4.4) -> float:
    """Clip duration = syllables / 4.4, two decimals, no rounding up (35 syllables = 7.95 s)."""
    return round(syllables / rate, 2)


def audit(text: str, cues: dict | None = None) -> list[tuple[str, int]]:
    """Word by word audit, for the pack's syllable_audit field."""
    t = text
    for cue, real in (cues or {}).items():
        t = t.replace(cue, real)
    t = t.replace("'", "").replace("’", "")
    return [(tok, number_syllables(int(tok)) if tok.isdigit() else word_syllables(tok))
            for tok in re.findall(r"[A-Za-z][A-Za-z'\-]*|\d+", t)]
