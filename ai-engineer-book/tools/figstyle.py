"""The book's figure style for Matplotlib (kept in step with assets/latex/preamble.tex).

Black-and-white safe: colour is never the only cue. Lines differ by style and marker too, filled areas that touch
carry hatching, and important lines are labelled directly.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / "assets" / "fonts"

# Indigo and saffron, with crimson for failure and slate for neutral; matches assets/latex/preamble.tex
C = dict(
    indigo="#3B4BA8", saffron="#D97706", plum="#8E3B7A", crimson="#B42318", slate="#5B6476", navy="#1B2A4A",
    ink="#14161A", ink2="#4A5160", muted="#7A8191", grid="#E3E5EA", rule="#A3A9B5",
    indigo_t="#DCE0F3", saffron_t="#F8E3C6", plum_t="#EDD5E6", crimson_t="#F6D5D1", slate_t="#E2E4E9", paper="#EEEBE5",
)
LINESTYLES = ["-", (0, (5, 2)), (0, (1, 1.6)), (0, (5, 1.5, 1, 1.5))]
MARKERS = ["o", "s", "^", "D"]
SERIES = [dict(color=c, ls=ls, marker=m) for c, ls, m in
          zip([C["indigo"], C["saffron"], C["plum"], C["crimson"]], LINESTYLES, MARKERS)]
TEXT_W = 4.7
_ready = False


def setup():
    global _ready
    if _ready:
        return
    for f in FONT_DIR.glob("*.ttf"):
        font_manager.fontManager.addfont(str(f))
    mpl.rcParams.update({
        "font.family": "Work Sans", "font.size": 7.8, "axes.labelsize": 7.8, "axes.labelcolor": C["ink2"],
        "axes.edgecolor": C["rule"], "axes.linewidth": 0.6, "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "axes.axisbelow": True, "grid.color": C["grid"], "grid.linewidth": 0.5,
        "xtick.color": C["ink2"], "ytick.color": C["ink2"], "xtick.labelsize": 7, "ytick.labelsize": 7,
        "xtick.major.size": 0, "ytick.major.size": 0, "lines.linewidth": 1.5, "lines.markersize": 4.5,
        "legend.frameon": False, "legend.fontsize": 7, "text.color": C["ink"], "pdf.fonttype": 42,
        "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white", "hatch.linewidth": 0.6,
    })
    _ready = True


def subplots(nrows=1, ncols=1, width=TEXT_W, height=2.4, **kw):
    setup()
    return plt.subplots(nrows, ncols, figsize=(width, height), **kw)


def canvas(width=TEXT_W, height=2.4):
    """A blank drawing area in data units 0..width x 0..height, for diagrams."""
    setup()
    f = plt.figure(figsize=(width, height))
    ax = f.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis("off")
    return f, ax


def box(ax, x, y, w, h, text, fc="white", ec=None, size=7.2, weight="normal", color=None, hatch=None, lw=0.8,
        ha="center", radius=0.06):
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={radius}", fc=fc,
                                ec=ec or C["rule"], lw=lw, hatch=hatch))
    tx = x + w / 2 if ha == "center" else x + 0.08
    ax.text(tx, y + h / 2, text, ha=ha, va="center", fontsize=size, fontweight=weight, color=color or C["ink"],
            linespacing=1.25)


def arrow(ax, x1, y1, x2, y2, color=None, lw=0.9, style="-|>", ls="-"):
    from matplotlib.patches import FancyArrowPatch
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=8, color=color or C["ink2"],
                                 lw=lw, linestyle=ls, shrinkA=0, shrinkB=0))


def save(f, chapter: str, name: str):
    out = ROOT / "figures" / chapter
    out.mkdir(parents=True, exist_ok=True)
    for ax in f.axes:
        if not ax.axison:
            for a in ax.get_children():
                if a is not ax.patch:
                    a.set_clip_on(False)
    f.savefig(out / f"{name}.pdf", bbox_inches="tight", pad_inches=0.04,
              metadata={"CreationDate": None, "ModDate": None, "Producer": None, "Creator": None})
    plt.close(f)
