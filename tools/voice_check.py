"""Mechanical half of the voice self-edit. The other half is reading it aloud.

Flags:
  - banned words and phrases (the ones that give away machine-written prose)
  - em-dash density (more than ~4 per 1,000 words reads as a tic)
  - "not just X, but Y" constructions
  - walls of text (prose paragraphs over 120 words)
  - sections that open with a definition ("X is a/an/the ...")
  - reflexive triads: "A, B, and C" lists of single words, counted per 1,000 words
  - summary closers ("In summary", "In conclusion", "To sum up")

usage: python tools/voice_check.py chapters/ch01.qmd [...]
"""
import re
import sys
from pathlib import Path

BANNED = [
    r"\bdelve", r"\btapestry", r"\blandscape", r"\brealm", r"\bcrucial", r"\bpivotal", r"\bleverag", r"\brobust",
    r"\bseamless", r"fast-paced world", r"let'?s dive in", r"dive into", r"in this chapter,? we will explore",
    r"it'?s important to note", r"it is important to note", r"game[- ]changer", r"\bunleash", r"\bharness the power",
    r"\bnavigate the complexit", r"\bever-evolving", r"\bin today'?s", r"\bembark", r"\btestament to", r"\bunlock",
    r"\bmyriad", r"\bplethora", r"\bparadigm shift", r"\bsynerg", r"\bcutting-edge", r"\bstate-of-the-art",
    r"\bin summary\b", r"\bin conclusion\b", r"\bto sum up\b", r"\boverall,", r"\bfurthermore\b", r"\bmoreover\b",
    r"\bnuanced?\b", r"\bfoster", r"\bholistic", r"\bempower",
]
NOT_JUST = re.compile(r"\bnot (just|only|merely)\b[^.]{0,80}?\bbut\b", re.I)
DEF_OPEN = re.compile(r"^(An?|The)\s+[\w\s-]{1,40}\s+(is an?|are|refers to|is defined as|means)\b")
TRIAD = re.compile(r"\b(\w{3,}), (\w{3,}),? and (\w{3,})\b")


def prose_blocks(text: str):
    """Yield (kind, block) skipping code, YAML, divs markers and figures."""
    in_code = False
    buf = []
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            if buf:
                yield "\n".join(buf)
                buf = []
            continue
        if in_code:
            continue
        if not line.strip() or line.startswith(":::") or line.startswith("!["):
            if buf:
                yield "\n".join(buf)
                buf = []
            continue
        buf.append(line)
    if buf:
        yield "\n".join(buf)


def strip_quotes(text: str) -> str:
    """Quotations are other people's words: never flag them."""
    out, inq = [], False
    for line in text.splitlines():
        if line.startswith(("::: {.bookquote", "::: {.epigraph")):
            inq = True
            continue
        if inq and line.startswith(":::"):
            inq = False
            continue
        if not inq:
            out.append(line)
    return "\n".join(out)


def check(path: Path) -> int:
    text = strip_quotes(path.read_text())
    blocks = list(prose_blocks(text))
    prose = "\n".join(b for b in blocks if not b.lstrip().startswith(("#", "|", "- ", "1. ")))
    words = len(re.findall(r"\b\w+\b", prose))
    issues = []
    for pat in BANNED:
        for m in re.finditer(pat, text, re.I):
            line = text[: m.start()].count("\n") + 1
            issues.append(f"{path.name}:{line}: banned: '{m.group(0)}'")
    dashes = prose.count("—") + prose.count(" -- ")
    per_k = dashes / max(1, words) * 1000
    if per_k > 4:
        issues.append(f"{path.name}: em-dash density {per_k:.1f}/1000 words (max 4)")
    for m in NOT_JUST.finditer(prose):
        issues.append(f"{path.name}: 'not just ... but': \"{m.group(0)[:60]}\"")
    for b in blocks:
        if b.lstrip().startswith(("#", "|", "- ", "* ", "1. ", "<", "{")):
            continue
        n = len(b.split())
        if n > 120:
            issues.append(f"{path.name}: wall of text ({n} words): \"{b[:60]}...\"")
    lines = text.splitlines()
    for i, l in enumerate(lines):
        if l.startswith("## ") or l.startswith("### "):
            nxt = next((x for x in lines[i + 1:] if x.strip()), "")
            if DEF_OPEN.match(nxt):
                issues.append(f"{path.name}:{i + 2}: section opens with a definition: \"{nxt[:60]}\"")
    triads = len(TRIAD.findall(prose))
    if triads / max(1, words) * 1000 > 2.5:
        issues.append(f"{path.name}: {triads} 'A, B and C' triads ({triads / max(1, words) * 1000:.1f}/1000 words, max 2.5)")
    print(f"{path.name}: {words} words of prose, {len(issues)} issue(s)")
    for s in issues:
        print("   " + s)
    return len(issues)


if __name__ == "__main__":
    total = sum(check(Path(p)) for p in sys.argv[1:])
    sys.exit(1 if total else 0)
