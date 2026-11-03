import json
import numpy as np
import figstyle as fs
from figstyle import C

E = json.loads((fs.ROOT / "research" / "m10-experiment.json").read_text())


def fig_decide_or_write():
    f, ax = fs.canvas(5.2, 1.55)
    steps = [("Which topic?", "pick one", True), ("Order number\ngiven?", "yes / no", True),
             ("Refund\nallowed?", "yes / no", True), ("How\nupset?", "scale", True),
             ("Needs a\nperson?", "yes / no", True), ("Write the\nreply", "text", False)]
    w, gap = 0.78, 0.104
    for i, (t, kind, dec) in enumerate(steps):
        x = i * (w + gap)
        fs.box(ax, x, 0.55, w, 0.6, t, size=6.2, fc=C["indigo_t"] if dec else C["saffron_t"],
               ec=C["indigo"] if dec else C["saffron"], weight="normal" if dec else "bold")
        ax.text(x + w / 2, 0.42, kind, ha="center", va="top", fontsize=5.8, color=C["ink2"])
        if i < len(steps) - 1:
            fs.arrow(ax, x + w, 0.85, x + w + gap, 0.85, lw=0.8)
    ax.text(2.2, 1.38, "DECIDING: five steps, each a fixed set of answers", ha="center", fontsize=6.4,
            fontweight="bold", color=C["indigo"])
    ax.text(4.85, 1.38, "WRITING: one", ha="center", fontsize=6.4, fontweight="bold", color=C["saffron"])
    return f


def fig_base_rate():
    f, ax = fs.canvas(5.2, 1.9)
    ax.text(0.0, 1.8, "10,000 refund requests, 3% abusive. The checker catches 95% of abuse, and wrongly flags 5% "
            "of honest ones.", fontsize=6.0, color=C["ink2"])
    rows = [("abusive: 300", 300, [(285, "flagged 285", C["crimson"]), (15, "", C["crimson_t"])]),
            ("honest: 9,700", 9700, [(485, "flagged 485", C["saffron"]), (9215, "not flagged 9,215", C["slate_t"])])]
    scale = 4.0 / 10000
    for i, (lab, n, parts) in enumerate(rows):
        y = 1.2 - i * 0.48
        ax.text(1.0, y + 0.15, lab, ha="right", va="center", fontsize=6.4)
        x = 1.08
        for m, t, col in parts:
            w = max(m * scale, 0.02)
            fs.box(ax, x, y, w, 0.3, "", fc=col, ec="none", radius=0.01)
            if t:
                ax.text(x + w + 0.04 if w < 0.6 else x + w / 2, y + 0.15, t, ha="left" if w < 0.6 else "center",
                        va="center", fontsize=6.0)
            x += w
    ax.text(0.0, 0.2, "Of the 770 flagged requests, only 285 are abusive: 37%. Most alarms are false, "
            "because honest requests are so many.", fontsize=6.4, fontweight="bold")
    return f


def fig_reliability():
    f, ax = fs.subplots(height=2.3)
    ax.plot([0, 0.3], [0, 0.3], color=C["rule"], ls=(0, (3, 2)), lw=0.9)
    ax.text(0.215, 0.255, "perfect", fontsize=6.0, color=C["ink2"], rotation=45, ha="center")
    r = E["rel_lr"]
    ax.plot([b["said"] for b in r], [b["happened"] for b in r], color=C["indigo"], marker="o")
    ax.text(0.15, 0.115, "logistic regression:\nsays 13%, happens 14%", fontsize=6.0, color=C["indigo"])
    ax.set_xlim(0, 0.3)
    ax.set_ylim(0, 0.3)
    ax.set_xticks([0, 0.1, 0.2, 0.3], ["0%", "10%", "20%", "30%"])
    ax.set_yticks([0, 0.1, 0.2, 0.3], ["0%", "10%", "20%", "30%"])
    ax.set_xlabel("what the model said (chance the team rejects)")
    ax.set_ylabel("how often the team rejected")
    ax.set_aspect("equal")
    return f


def fig_cost_threshold():
    f, ax = fs.subplots(height=1.9)
    cc = np.array(E["cost_curve"])
    ax.plot(cc[:, 0] * 100, cc[:, 1], color=C["indigo"])
    t = E["t_low"]
    best = E["cost_per_request"][f"{t:.3f}"]
    ax.plot([t * 100], [best], "o", color=C["saffron"])
    ax.annotate(f"line at {t:.1%}: ₹{best:.0f} per request", xy=(t * 100, best), xytext=(8, 27),
                fontsize=6.2, color=C["saffron"], arrowprops=dict(arrowstyle="-", color=C["saffron"], lw=0.7))
    ax.axhline(40, color=C["slate"], ls=(0, (3, 2)), lw=0.8)
    ax.text(5.5, 40.6, "review everything: ₹40", ha="left", fontsize=6.0, color=C["slate"])
    ax.set_xlabel("approve automatically below this chance of rejection (%)")
    ax.set_ylabel("average cost per request (₹)")
    ax.set_xlim(0, 30)
    ax.set_ylim(20, 46)
    return f


def fig_bands():
    f, ax = fs.canvas(5.2, 1.4)
    b = E["bands"]
    parts = [("ACT", "approve automatically", b["act"], C["indigo_t"], C["indigo"], "below 2.7%"),
             ("REVIEW", "a person checks", b["review"], C["saffron_t"], C["saffron"], "2.7% to 20%"),
             ("ESCALATE", "fraud team", b["escalate"], C["crimson_t"], C["crimson"], "20% and above")]
    x = 0.0
    widths = [2.55, 1.6, 1.05]
    for (name, what, d, fc, ec, rng), w in zip(parts, widths):
        fs.box(ax, x, 0.45, w - 0.04, 0.6, "", fc=fc, ec=ec)
        ax.text(x + 0.08, 0.92, name, fontsize=6.6, fontweight="bold", color=ec)
        ax.text(x + 0.08, 0.73, what, fontsize=6.0)
        ax.text(x + 0.08, 0.56, f"{d['share']:.1%} of requests", fontsize=6.0, color=C["ink2"])
        ax.text(x + 0.02, 0.33, rng, fontsize=5.8, color=C["ink2"], va="top")
        x += w
    ax.text(0.0, 1.22, "Chance the refund team would reject, from the model", fontsize=6.2, color=C["ink2"])
    ax.text(0.0, 0.05, "Bands drawn wider than their share so the labels fit.", fontsize=5.6, color=C["muted"])
    return f
