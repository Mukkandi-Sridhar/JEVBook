"""Finish the EPUB after Quarto: python3 tools/epub_post.py in.epub out.epub

Quarto leaves figure images with alt="" when no fig-alt is given. Every figure here has a caption that describes it,
so the caption (without its "Figure N:" label) becomes the image's alt text. The archive is rewritten with the
mimetype entry first and uncompressed, as the EPUB spec requires.
"""
import html
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


def main(src, dst):
    total = 0
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w") as zout:
        names = zin.namelist()
        zout.writestr(zipfile.ZipInfo("mimetype"), zin.read("mimetype"), compress_type=zipfile.ZIP_STORED)
        for name in names:
            if name == "mimetype":
                continue
            data = zin.read(name)
            if name.endswith(".xhtml"):
                s, n = fix(data.decode("utf-8"))
                total += n
                data = s.encode("utf-8")
            zout.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)
    print(f"alt text set on {total} figure images")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
