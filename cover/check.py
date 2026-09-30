"""Checks for the finished cover: python cover/check.py  -> cover/checks.json

Thumbnail (150 px wide) and greyscale versions of the front, WCAG contrast of every text colour against its
ground, a spell-check of every word on the cover, and the PDF page sizes against the calculated wrap.
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from PIL import Image  # noqa: E402
from spellchecker import SpellChecker  # noqa: E402

from coverlib import C, COVER, contrast  # noqa: E402
from wrap import BG, BODY  # noqa: E402

ALLOW = {"jev", "mukkandi", "sridhar", "jevbook", "llm", "llms", "soc", "api", "inr", "usd", "praise", "author", "bio",
         "photo", "price", "authorhub", "gmail", "github", "com", "ated", "er", "ate", "gen", "ai", "agentic", "tech"}


def main():
    out = {}
    front = Image.open(COVER / "src" / "front.png").convert("RGB")
    thumb = front.resize((150, round(150 * front.height / front.width)), Image.LANCZOS)
    thumb.save(COVER / "concepts" / "final-front-thumb150.png")
    thumb.convert("L").save(COVER / "concepts" / "final-front-thumb150-grey.png")
    Image.open(COVER / "print" / "cover-paperback-preview.png").convert("L").save(
        COVER / "print" / "cover-paperback-preview-grey.png")
    out["contrast_vs_ground"] = {k: round(contrast(v, BG), 2) for k, v in {
        "title green": C["jev_on_dark"], "white": C["text_on_dark"], "subtitle": C["sub_on_dark"], "blurb": BODY,
        "small captions": C["faint_on_dark"], "orange tokens": C["llm_on_dark"]}.items()}
    out["contrast_card_caption"] = round(contrast(C["faint_on_dark"], C["night2"]), 2)
    words = set()
    for f in ("cover-paperback.svg", "cover-hardcover.svg", "ebook-front.svg"):
        for s in re.findall(r"<text[^>]*>(.*?)</text>", (COVER / "src" / f).read_text(), re.S):
            words.update(re.findall(r"[A-Za-z][A-Za-z'’]+", html.unescape(re.sub(r"<[^>]+>", "", s))))
    sp = SpellChecker()
    norm = lambda w: w.lower().replace("’", "'")  # noqa: E731
    out["spelling"] = dict(words=len(words), unknown=sorted(w for w in words if norm(w) not in ALLOW
                                                            and sp.unknown([norm(w)])))
    dims = json.loads((COVER / "print" / "dimensions.json").read_text())
    for kind in ("paperback", "hardcover"):
        info = subprocess.run(["pdfinfo", str(COVER / "print" / f"cover-{kind}.pdf")], capture_output=True,
                              text=True).stdout
        w, h = map(float, re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info).groups())
        out[f"{kind}_pdf_in"] = [round(w / 72, 4), round(h / 72, 4)]
        out[f"{kind}_expected_in"] = [dims[kind]["width_in"], dims[kind]["height_in"]]
    (COVER / "checks.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
