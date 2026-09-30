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
from coverlib import PT, Wrap, html_page, interior_pages  # noqa: E402
from wrap import BG, BODY, HARDCOVER_PAPER, PAPERBACK_PAPER, barcode_local, case_study, wrap_svg  # noqa: E402
from coverlib import strapline  # noqa: E402

ALLOW = {"jev", "mukkandi", "sridhar", "jevbook", "llm", "llms", "soc", "api", "inr", "usd", "praise", "author", "bio",
         "price", "authorhub", "typesafe", "ne", "ra", "te", "gmail", "github", "com", "ated", "er", "ate", "gen", "ai", "agentic", "tech"}


def boxes(html_file, selector):
    res = subprocess.run(["node", str(COVER / "bbox.mjs"), str(html_file), selector], capture_output=True, text=True,
                         check=True)
    return json.loads(res.stdout)


def hit(a, b, pad=0.5):
    return not (a["x"] + a["w"] <= b["x"] + pad or b["x"] + b["w"] <= a["x"] + pad or
                a["y"] + a["h"] <= b["y"] + pad or b["y"] + b["h"] <= a["y"] + pad)


def layout(kind, paper, strap):
    """Every back-cover item inside the safe area, clear of the barcode area and of each other; the front's
    fragments clear of the title and inside the safe area."""
    wr = Wrap(kind, pages=interior_pages(), paper=paper)
    src = COVER / "src" / f"_layout-{kind}.html"
    src.write_text(html_page(wrap_svg(wr, strap), f"{wr.width}in", f"{wr.height}in"))
    e, s = wr.edge * PT, wr.safe * PT
    hinge = wr.hinge * PT if kind == "hardcover" else 0
    W, H = (wr.panel_w * PT - hinge), wr.panel_h * PT
    problems = []
    back = boxes(src, "#back text, #back .qrplate, #back rect[stroke-dasharray]")
    for b in back:
        b["x"] -= e
        b["y"] -= e
    bc = dict(zip("xywh", barcode_local(W, H)))
    for b in back:
        name = (b["text"] or b["cls"] or b["tag"])[:40]
        if b["x"] < s - 0.01 or b["y"] < s - 0.01 or b["x"] + b["w"] > W - s + 0.01 or b["y"] + b["h"] > H - s + 0.01:
            problems.append(f"back: '{name}' outside the safe area")
        if hit(b, bc, 0):
            problems.append(f"back: '{name}' in the barcode area")
    texts = [b for b in back if b["tag"] == "text"]
    others = [b for b in back if b["tag"] != "text"]
    for i, a in enumerate(texts):
        for b in texts[i + 1:] + others:
            inside = b["tag"] != "text" and b["x"] <= a["x"] and a["x"] + a["w"] <= b["x"] + b["w"] and \
                b["y"] <= a["y"] and a["y"] + a["h"] <= b["y"] + b["h"]   # a label inside its own box
            if hit(a, b) and not inside:
                problems.append(f"back: '{a['text'][:30]}' overlaps '{(b['text'] or b['cls'])[:30]}'")
    fx = wr.front_x * PT + hinge
    front = boxes(src, "#front text")
    for b in front:
        b["x"] -= fx
        b["y"] -= e
        if b["x"] < s - 0.01 or b["x"] + b["w"] > W - s + 0.01 or b["y"] + b["h"] > H - s + 0.01:
            problems.append(f"front: '{b['text'][:30]}' outside the safe area")
    title = [b for b in front if b["text"] in ("Decide,", "Don’t")]
    for f in (b for b in front if b["cls"] == "frag"):
        for t in title:
            if hit(f, t):
                problems.append(f"front: fragment '{f['text']}' overlaps '{t['text']}'")
    src.unlink()
    return dict(items_checked=len(back) + len(front), problems=problems)


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
    strap = strapline()
    out["layout"] = {"paperback": layout("paperback", PAPERBACK_PAPER, strap),
                     "hardcover": layout("hardcover", HARDCOVER_PAPER, strap)}
    # the stat card must match what Chapter 18 prints (its summary table: "real threats a person sees")
    book = subprocess.run(["pdftotext", str(next((COVER.parent / "_book").glob("*.pdf"))), "-"], capture_output=True,
                          text=True).stdout
    i = book.find("real threats a person sees")
    in_book = re.findall(r"(\d+)%", book[i:i + 200])[:2] if i >= 0 else []
    before, after, _ = case_study()
    on_cover = [f"{before * 100:.0f}", f"{after * 100:.0f}"]
    out["case_study"] = dict(cover=on_cover, chapter18=in_book, match=on_cover == in_book)
    (COVER / "checks.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
