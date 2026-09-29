"""The book's visual system for Matplotlib.

One colour code for the whole book (validated for colour-vision deficiency
with the dataviz palette checker; see DECISIONS.md):

    data     blue    anything that is input, evidence, features
    llm      orange  large language models, System 2, generation
    jev      green   Jev / System One decisions
    fail     red     failure modes, errors, missed attacks
    zones    purple  act / review / escalate (a single-hue ordinal ramp)
"""

from __future__ import annotations

import os
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[2]
FONT_DIR = ROOT / "assets" / "fonts"

C = dict(
    data="#2F6DB5", llm="#E07A1F", jev="#3B9C6E", fail="#B8323A",
    ink="#1F2430", ink2="#4B5563", muted="#8A919C", grid="#E4E7EB", rule="#C9CED6",
    surface="#FFFFFF", paper="#FBFAF7",
    # tints for filled boxes (text sits on these in ink)
    data_t="#E4EDF8", llm_t="#FCEBDC", jev_t="#E2F2E9", fail_t="#F7E0E1", neutral_t="#F1F2F4",
    # extra categorical slots for the rare chart that needs them (fixed order)
    slate="#5B6B82", gold="#C9971C",
)
ZONE = dict(act="#B7A6E0", review="#8468C9", escalate="#4B2C8F")
ZONE_T = dict(act="#EFEAF9", review="#E4DCF4", escalate="#DAD2EC")
ZONE_TEXT = dict(act=C["ink"], review="#FFFFFF", escalate="#FFFFFF")
KIND = dict(data=(C["data"], C["data_t"]), llm=(C["llm"], C["llm_t"]), jev=(C["jev"], C["jev_t"]),
            fail=(C["fail"], C["fail_t"]), neutral=(C["ink2"], C["neutral_t"]),
            act=(ZONE["act"], ZONE_T["act"]), review=(ZONE["review"], ZONE_T["review"]),
            escalate=(ZONE["escalate"], ZONE_T["escalate"]), plain=(C["rule"], "#FFFFFF"))

# Page geometry (inches) - must match assets/latex/geometry in _quarto.yml
TEXT_W = 4.7
WIDE_W = 5.95
MARGIN_W = 1.08

SANS = "Inter"
SERIF = "Source Serif 4"
MONO = "JetBrains Mono"

_ready = False


def setup():
    global _ready
    if _ready:
        return
    for f in FONT_DIR.glob("*.ttf"):
        font_manager.fontManager.addfont(str(f))
    mpl.rcParams.update({
        "font.family": SANS,
        "font.size": 7.8,
        "axes.titlesize": 8.5,
        "axes.titleweight": "semibold",
        "axes.titlelocation": "left",
        "axes.titlepad": 8,
        "axes.labelsize": 7.8,
        "axes.labelcolor": C["ink2"],
        "axes.edgecolor": C["rule"],
        "axes.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": C["grid"],
        "grid.linewidth": 0.5,
        "grid.linestyle": "-",
        "xtick.color": C["ink2"],
        "ytick.color": C["ink2"],
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "xtick.major.pad": 4,
        "ytick.major.pad": 4,
        "lines.linewidth": 1.5,
        "lines.solid_capstyle": "round",
        "lines.solid_joinstyle": "round",
        "lines.markersize": 5,
        "legend.frameon": False,
        "legend.fontsize": 7,
        "legend.handlelength": 1.4,
        "text.color": C["ink"],
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "pdf.fonttype": 42,
        "svg.fonttype": "none",
        "figure.dpi": 150,
        "axes.prop_cycle": mpl.cycler(color=[C["data"], C["llm"], C["jev"], C["fail"], C["slate"], C["gold"]]),
    })
    _ready = True


def fig(width: str | float = "text", height: float = 2.4, **kw):
    """New figure at print size. width: 'text' (4.7in), 'wide' (5.95in), 'margin' or inches."""
    setup()
    w = {"text": TEXT_W, "wide": WIDE_W, "margin": MARGIN_W}.get(width, width)
    return plt.figure(figsize=(w, height), **kw)


def subplots(nrows=1, ncols=1, width: str | float = "text", height: float = 2.4, **kw):
    setup()
    w = {"text": TEXT_W, "wide": WIDE_W, "margin": MARGIN_W}.get(width, width)
    return plt.subplots(nrows, ncols, figsize=(w, height), **kw)


def save(f, chapter: str, name: str, outdir: str | os.PathLike | None = None, tight=True):
    """Write <name>.pdf (print) and <name>.svg (web) under figures/<chapter>/."""
    out = Path(outdir) if outdir else ROOT / "figures" / chapter
    out.mkdir(parents=True, exist_ok=True)
    kw = dict(bbox_inches="tight", pad_inches=0.04) if tight else {}
    f.savefig(out / f"{name}.pdf", metadata={"CreationDate": None, "ModDate": None, "Producer": None, "Creator": None}, **kw)
    f.savefig(out / f"{name}.svg", metadata={"Date": None, "Creator": None}, **kw)
    plt.close(f)
    return out / f"{name}.pdf"


def synthetic_tag(f_or_ax, text="SYNTHETIC · not measured on real Jev", loc="br"):
    """The small label every Jev number carries."""
    f = f_or_ax.figure if hasattr(f_or_ax, "figure") and not isinstance(f_or_ax, plt.Figure) else f_or_ax
    x, ha = (0.995, "right") if loc.endswith("r") else (0.005, "left")
    y, va = (0.0, "bottom") if loc.startswith("b") else (1.0, "top")
    f.text(x, y, text, ha=ha, va=va, fontsize=5.6, color=C["muted"], fontweight="medium",
           bbox=dict(boxstyle="round,pad=0.25,rounding_size=0.15", fc="white", ec=C["grid"], lw=0.5))


def clean(ax, grid="y"):
    """Recessive axes: hairline grid on one axis only."""
    ax.grid(False)
    if grid in ("y", "both"):
        ax.yaxis.grid(True)
    if grid in ("x", "both"):
        ax.xaxis.grid(True)
    ax.spines["left"].set_visible(grid != "y")
    return ax


def pct(x, pos=None):
    return f"{x:.0%}"
