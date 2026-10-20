import numpy as np
import figstyle as fs
from figstyle import C


def fig_split():
    f, ax = fs.canvas(4.7, 1.25)
    parts = [(0.0, 3.29, "Training set (70%)\nthe model learns from these\nlike practice papers", C["indigo_t"], C["indigo"], None),
             (3.29, 0.705, "Validation\n(15%)\nmock tests", C["saffron_t"], C["saffron"], "////"),
             (3.995, 0.705, "Test\n(15%)\nfinal exam,\nused once", C["paper"], C["ink2"], "xxxx")]
    for x, w, t, fc, ec, h in parts:
        fs.box(ax, x, 0.25, w, 0.85, "", fc=fc, ec=ec, hatch=h, radius=0.02)
        ax.text(x + w / 2, 0.675, t, ha="center", va="center", fontsize=6.4,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9) if h else None)
    return f


def fig_route():
    f, ax = fs.subplots(height=2.4)
    p = np.linspace(0.5, 1.0, 200)
    act = (1 - p) * 100 * 30
    ax.plot(p, act, color=C["indigo"], lw=1.8)
    ax.plot(p, np.full_like(p, 600), color=C["saffron"], lw=1.8, ls=(0, (5, 2)))
    ax.axvline(0.8, color=C["ink2"], lw=0.8, ls=(0, (2, 2)))
    ax.text(0.525, 690, "act alone:\n(1 − p) × 100 × ₹30", color=C["indigo"], fontsize=6.8)
    ax.text(0.86, 650, "ask a person: 100 × ₹6", color=C["saffron"], fontsize=6.8)
    ax.text(0.805, 1350, "threshold 80%", fontsize=6.8, color=C["ink"])
    ax.text(0.65, 80, "ask a person", ha="center", fontsize=7, color=C["ink2"])
    ax.text(0.9, 80, "act alone", ha="center", fontsize=7, color=C["ink2"])
    ax.set_xlabel("Probability the model is right")
    ax.set_ylabel("Cost of 100 messages (₹)")
    ax.xaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.set_ylim(0, 1550)
    return f
