import numpy as np
import figstyle as fs
from figstyle import C


def fig_interval():
    f, ax = fs.subplots(height=2.3)
    n = np.linspace(15, 1000, 400)
    w = 196 * np.sqrt(0.16 / n)
    ax.plot(n, w, color=C["indigo"], lw=1.8)
    for k in [20, 50, 200, 1000]:
        v = 196 * np.sqrt(0.16 / k)
        ax.plot(k, v, "o", color=C["indigo"], ms=4.5)
        ax.annotate(f"{k:,} cases: ±{v:.1f} points", (k, v), xytext=(8, 4) if k < 1000 else (-4, 9), ha="left" if k < 1000 else "right", textcoords="offset points", fontsize=6.6)
    ax.set_xscale("log")
    ax.set_xticks([20, 50, 100, 200, 500, 1000])
    ax.set_xticklabels(["20", "50", "100", "200", "500", "1,000"])
    ax.set_xlabel("Number of test cases")
    ax.set_ylabel("Range around the score\n(± percentage points)")
    ax.set_ylim(0, 20)
    return f


def fig_temperature():
    words = ["shipped", "delivered", "cancelled", "packed", "delayed", "refunded"]
    p = np.array([.42, .25, .12, .09, .07, .05])
    f, ax = fs.subplots(height=2.3)
    x = np.arange(len(words))
    styles = [(0.5, C["indigo"], ""), (1.0, C["plum"], "////"), (1.5, C["saffron"], "....")]
    for i, (t, col, h) in enumerate(styles):
        q = p ** (1 / t)
        q = q / q.sum()
        ax.bar(x + (i - 1) * 0.27, q * 100, 0.25, color=col, hatch=h or None, edgecolor="white", lw=0.6,
               label=f"temperature {t:g}")
    ax.set_xticks(x)
    ax.set_xticklabels(words)
    ax.set_ylabel("Chance of being picked (%)")
    ax.legend(loc="upper right")
    ax.grid(axis="x", visible=False)
    return f


def fig_calibration():
    f, ax = fs.subplots(width=3.2, height=3.0)
    said = np.array([.05, .15, .25, .35, .45, .55, .65, .75, .85, .95])
    good = said + np.array([.01, -.02, .02, -.01, .02, -.02, .01, -.02, .01, -.01])
    over = 0.5 + (said - 0.5) * 0.45
    ax.plot([0, 1], [0, 1], color=C["rule"], lw=0.8, ls=(0, (3, 2)))
    ax.plot(said, good, color=C["plum"], marker="o", lw=1.4)
    ax.plot(said, over, color=C["crimson"], marker="s", lw=1.4, ls=(0, (5, 2)))
    ax.text(0.5, 0.62, "calibrated", color=C["plum"], fontsize=7, rotation=38, ha="center")
    ax.text(0.80, 0.50, "overconfident", color=C["crimson"], fontsize=7, ha="center")
    ax.set_xlabel("Chance the model gave")
    ax.set_ylabel("How often it really happened")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.xaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.set_aspect("equal")
    return f
