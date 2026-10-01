"""Finish the EPUB after Quarto: python3 tools/epub_post.py in.epub out.epub

Quarto leaves figure images with alt="" when no fig-alt is given. Every figure here has a caption that describes it,
so the caption (without its "Figure N:" label) becomes the image's alt text. The archive is rewritten with the
mimetype entry first and uncompressed, as the EPUB spec requires.

Kindle's converter rejects the book with MathML in it ("We couldn't convert your HTML file"), so every formula is
replaced: the simple inline ones by plain HTML (italic letters, <sub>, <sup>), and the fractions and sums by PNG
images drawn with matplotlib's mathtext, each with a spoken-style alt text.
"""
import html
import io
import re
import sys
import zipfile

FIG = re.compile(r'(<figure\b.*?</figure>)', re.S)
IMG = re.compile(r'<img\b([^>]*?)alt=""([^>]*?)\s*/?>')
CAP = re.compile(r'<figcaption\b[^>]*>(.*?)</figcaption>', re.S)


def fix(xhtml: str) -> tuple[str, int]:
    count = 0

    def one(m):
        nonlocal count
        fig = m.group(1)
        cap = CAP.search(fig)
        if not cap:
            return fig
        text = re.sub(r"<[^>]+>", "", cap.group(1))
        text = re.sub(r"\s+", " ", html.unescape(text)).strip()
        text = re.sub(r"^(Figure|Table)\s+[\d.]+:\s*", "", text)
        alt = html.escape(text, quote=True)
        new, n = IMG.subn(lambda im: f"<img{im.group(1)}alt=\"{alt}\"{im.group(2)} />", fig)
        count += n
        return new

    return FIG.sub(one, xhtml), count


# ---------------------------------------------------------------- formulas
MATH = re.compile(r'<math\b[^>]*display="(\w+)"[^>]*>.*?<annotation encoding="application/x-tex">(.*?)</annotation>'
                  r'.*?</math>', re.S)
I = lambda v: f"<i>{v}</i>"  # noqa: E731
# the simple inline formulas, as plain HTML
INLINE = {
    r"p^{*} = 400 / 10{,}400 \approx 0.04": f"{I('p')}<sup>*</sup> = 400 / 10,400 ≈ 0.04",
    r"C_r": f"{I('C')}<sub>{I('r')}</sub>",
    r"m": I("m"),
    r"C_{\text{miss}}": f"{I('C')}<sub>miss</sub>",
    r"C_{\text{page}}": f"{I('C')}<sub>page</sub>",
    r"p_i": f"{I('p')}<sub>{I('i')}</sub>",
    r"y_i \in \{0, 1\}": f"{I('y')}<sub>{I('i')}</sub> ∈ {{0, 1}}",
    r"b": I("b"),
    r"n_b": f"{I('n')}<sub>{I('b')}</sub>",
    r"\bar p_b": f"{I('p̄')}<sub>{I('b')}</sub>",
    r"\bar y_b": f"{I('ȳ')}<sub>{I('b')}</sub>",
    r"p' = \sigma(z / T)": f"{I('p')}′ = {I('σ')}({I('z')} / {I('T')})",
    r"p' = \sigma(a z + b)": f"{I('p')}′ = {I('σ')}({I('a')}{I('z')} + {I('b')})",
    r"b'": f"{I('b')}′",
    r"\sigma": I("σ"),
}
# the formulas drawn as images: alt text read the way you'd say them
SPOKEN = {
    "p^{*} = \\frac": "p star equals C false alarm, divided by C false alarm plus C miss",
    "\\text{low} =": "low equals C r divided by C miss times one minus m; high equals C page minus C r, divided by "
                     "C page plus m times C miss",
    "\\text{Brier} =": "Brier equals the average over i of p i minus y i, squared; log loss equals minus the average "
                       "over i of y i log p i plus one minus y i, times log of one minus p i",
    "\\text{ECE} =": "ECE equals the sum over bins b of n b over n, times the absolute difference between the mean "
                     "p and the mean y in bin b",
    "\\dfrac{b'": "b prime over one minus b prime, divided by b over one minus b",
    "z = \\log": "z equals log of p over one minus p",
}


def math_png(tex: str, size: float = 15.0, dpi: int = 300) -> tuple[bytes, float, float]:
    """Draw a formula with matplotlib's mathtext; returns the PNG and its width and height in em of `size`."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    t = " ".join(tex.split())
    t = re.sub(r"\\text\{([^}]*)\}", lambda m: r"\mathrm{" + m.group(1).replace(" ", r"\ ") + "}", t)
    t = t.replace(r"\dfrac", r"\frac").replace(r"\big", "").replace("{,}", ",")
    fig = plt.figure()
    fig.text(0, 0, f"${t}$", fontsize=size, color="#1F2430", math_fontfamily="dejavuserif")
    buf = io.BytesIO()
    fig.savefig(buf, dpi=dpi, bbox_inches="tight", pad_inches=0.04, facecolor="white")
    plt.close(fig)
    from PIL import Image
    w, h = Image.open(io.BytesIO(buf.getvalue())).size
    em = size * dpi / 72
    return buf.getvalue(), w / em, h / em


NO_HYPHENS = ("\n/* code is never hyphenated (tools/epub_post.py) */\n"
              "pre, pre *, code, code * { hyphens: none; -webkit-hyphens: none; -epub-hyphens: none; "
              "adobe-hyphenate: none; text-align: left; }\n")
DATA_URI = re.compile(r"background-image:\s*url\(['\"]?data:[^)]*\);?")


def unmath(xhtml: str, images: list) -> str:
    def one(m):
        display, tex = m.group(1), html.unescape(m.group(2)).strip()
        if display == "inline" and tex in INLINE:
            return f'<span class="math-text">{INLINE[tex]}</span>'
        alt = next((v for k, v in SPOKEN.items() if tex.startswith(k)), tex)
        # two formulas set side by side with \qquad go on two lines, so neither has to shrink on a phone
        parts = tex.split(r"\qquad") if display == "block" else [tex]
        alts = alt.split("; ") if len(alt.split("; ")) == len(parts) else [alt] * len(parts)
        out = []
        for part, a in zip(parts, alts):
            png, w_em, h_em = math_png(part)
            name = f"math-{len(images) + 1:02d}.png"
            images.append((name, png))
            # mathtext draws fractions smaller than the body text, so the images are shown 1.5 times their drawn
            # size; a display formula gets a width (it shrinks to fit a phone), an inline one a height
            size = (f"width:{w_em * 1.5:.2f}em;max-width:100%;height:auto;" if display == "block"
                    else f"height:{h_em * 1.5:.2f}em;vertical-align:middle;")
            img = f'<img src="../media/{name}" alt="{html.escape(a, quote=True)}" style="{size}" />'
            out.append(f'<span class="math-block" style="display:block;text-align:center;margin:0.6em 0">{img}</span>'
                       if display == "block" else img)
        return "".join(out)
    return MATH.sub(one, xhtml)


def main(src, dst):
    total = 0
    images: list = []
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w") as zout:
        names = zin.namelist()
        zout.writestr(zipfile.ZipInfo("mimetype"), zin.read("mimetype"), compress_type=zipfile.ZIP_STORED)
        opf = None
        for name in names:
            if name == "mimetype":
                continue
            data = zin.read(name)
            if name.endswith(".css"):
                data += NO_HYPHENS.encode("utf-8")
            if name.endswith(".opf"):
                opf = (name, data.decode("utf-8"))
                continue
            if name.endswith(".xhtml"):
                s, n = fix(data.decode("utf-8"))
                total += n
                s2 = DATA_URI.sub("", unmath(s, images))
                if s2 != s and "<math" not in s2:
                    s2 = s2.replace(' properties="mathml"', "")
                data = s2.encode("utf-8")
            zout.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)
        name, s = opf
        base = name.rsplit("/", 1)[0] + "/"
        for img, png in images:
            zout.writestr(base + "media/" + img, png, compress_type=zipfile.ZIP_DEFLATED)
        items = "".join(f'<item id="{img[:-4]}" href="media/{img}" media-type="image/png" />\n' for img, _ in images)
        s = s.replace("</manifest>", items + "</manifest>")
        s = re.sub(r'(<item\b[^>]*?)\s*properties="mathml"', r"\1", s)
        s = re.sub(r'properties="mathml ([^"]*)"|properties="([^"]*) mathml"', lambda m: f'properties="{m.group(1) or m.group(2)}"', s)
        zout.writestr(name, s.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
    print(f"alt text set on {total} figure images; {len(images)} formulas drawn as images")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
