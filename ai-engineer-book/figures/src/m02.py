import numpy as np
import figstyle as fs
from figstyle import C
from matplotlib.patches import Ellipse


def fig_next_token():
    """Softmax over made-up scores for the next token, at two temperatures."""
    tokens = ["7", "3", "5", "10", "24", "two"]
    scores = np.array([2.6, 2.0, 1.6, 1.0, 0.5, 0.1])
    f, axes = fs.subplots(1, 2, height=1.9, sharey=True)
    for ax, t, col, title in [(axes[0], 0.3, C["indigo"], "Temperature 0.3"),
                              (axes[1], 1.2, C["saffron"], "Temperature 1.2")]:
        p = np.exp(scores / t)
        p /= p.sum()
        bars = ax.bar(tokens, p, color=col, width=0.62)
        for b, v in zip(bars, p):
            ax.text(b.get_x() + b.get_width() / 2, v + 0.02, f"{v:.0%}", ha="center", fontsize=6.4)
        ax.set_title(title, fontsize=7.2, color=C["ink"], pad=4)
        ax.set_ylim(0, 1.0)
        ax.set_yticks([0, 0.5, 1.0], ["0%", "50%", "100%"])
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel("chance of being picked")
    f.text(0.5, -0.04, 'Next token after "Your refund will reach you within …"', ha="center", fontsize=6.8,
           color=C["ink2"])
    f.tight_layout()
    return f


def fig_attention():
    f, ax = fs.canvas(4.7, 1.55)
    words = ["I", "sat", "on", "the", "river", "bank"]
    xs = np.linspace(0.25, 4.4, len(words))
    for x, w in zip(xs, words):
        fs.box(ax, x - 0.3, 0.2, 0.6, 0.34, w, size=6.8, fc=C["saffron_t"] if w == "bank" else "white",
               ec=C["saffron"] if w == "bank" else None)
    weights = {"river": 0.6, "sat": 0.15, "on": 0.1, "I": 0.05, "the": 0.1}
    xb = xs[-1]
    for x, w in zip(xs[:-1], words[:-1]):
        a = weights[w]
        h = 0.62 + 0.55 * (xb - x) / (xb - xs[0])
        ax.annotate("", xy=(x, 0.56), xytext=(xb, 0.56),
                    arrowprops=dict(arrowstyle="-|>", color=C["indigo"], lw=0.5 + 5 * a,
                                    connectionstyle=f"arc3,rad=0.45", alpha=0.9))
        ax.text(x, 0.66 + 0.02, f"{a:.2f}", ha="center", fontsize=5.8, color=C["ink2"])
    ax.text(2.3, 1.48, "how much \"bank\" looks at each earlier word (made-up weights for illustration)", ha="center",
            fontsize=6.0, color=C["ink2"])
    return f


def fig_embedding_map():
    f, ax = fs.subplots(height=2.5)
    groups = [
        (C["indigo"], "o", [("refund", .10, .84), ("money back", .27, .80), ("paisa wapas", .07, .68),
                          ("amount not credited", .20, .60)], (.24, .72, .48, .40), "about refunds"),
        (C["saffron"], "s", [("delivery", .62, .84), ("courier", .82, .80), ("order nahi aaya", .58, .68),
                            ("tracking not working", .70, .59)], (.76, .72, .46, .40), "about delivery"),
        (C["plum"], "^", [("battery life", .33, .30), ("screen size", .50, .21),
                          ("size chart", .35, .12)], (.47, .21, .44, .32), "about products"),
    ]
    for col, m, pts, (cx, cy, w, h), name in groups:
        ax.add_patch(Ellipse((cx, cy), w, h, fc="none", ec=col, lw=0.8, ls=(0, (3, 2))))
        for t, x, y in pts:
            ax.plot(x, y, m, color=col, ms=5)
            ax.text(x + 0.018, y, t, fontsize=6.6, va="center")
        ax.text(cx, cy + h / 2 + 0.03, name, ha="center", fontsize=6.8, fontweight="bold", color=col)
    ax.set_xlim(0, 1.02)
    ax.set_ylim(0, 1.0)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)
    return f


def fig_prefill_decode():
    f, ax = fs.canvas(4.7, 1.75)
    ax.text(0.0, 1.62, "READING THE INPUT: all tokens in one pass", fontsize=6.4, fontweight="bold",
            color=C["indigo"])
    for i in range(12):
        fs.box(ax, 0.0 + i * 0.13, 1.12, 0.11, 0.3, "", fc=C["indigo_t"], ec=C["indigo"], lw=0.5, radius=0.02)
    ax.annotate("", xy=(1.62, 0.98), xytext=(0.0, 0.98),
                arrowprops=dict(arrowstyle="-", color=C["indigo"], lw=1.4))
    ax.text(0.8, 0.84, "one pass", ha="center", fontsize=6.0, color=C["indigo"])
    ax.text(2.0, 1.62, "WRITING THE OUTPUT: one token per pass", fontsize=6.4, fontweight="bold",
            color=C["saffron"])
    for i in range(6):
        x = 2.0 + i * 0.44
        fs.box(ax, x, 1.12, 0.11, 0.3, "", fc=C["saffron_t"], ec=C["saffron"], lw=0.5, radius=0.02)
        if i < 5:
            fs.arrow(ax, x + 0.13, 1.27, x + 0.42, 1.27, lw=0.6, color=C["rule"])
    ax.text(3.2, 0.84, "pass, pass, pass … each waits for the one before", ha="center", fontsize=6.0,
            color=C["saffron"])
    ax.plot([0, 4.6], [0.6, 0.6], color=C["rule"], lw=0.5)
    ax.text(0.0, 0.42, "Time to first token grows with the length of the input.", fontsize=6.3, color=C["ink"])
    ax.text(0.0, 0.2, "Total time grows with the length of the output, one step per token.", fontsize=6.3,
            color=C["ink"])
    return f


def fig_training():
    f, ax = fs.canvas(4.7, 1.3)
    steps = [("Pretraining", "predict the next token\non trillions of tokens", "a base model:\ncontinues any text"),
             ("Fine-tuning", "copy thousands of\ngood question–answer\nexamples", "follows\ninstructions"),
             ("Preference tuning", "people pick the better\nof two answers", "gives answers\npeople prefer"),
             ("Checkable rewards", "practise on problems\nwhose answers can be\nchecked", "better at maths\nand code")]
    w, gap = 1.04, 0.15
    for i, (name, how, result) in enumerate(steps):
        x = i * (w + gap)
        fs.box(ax, x, 0.55, w, 0.62, how, size=5.6, fc=C["indigo_t"] if i else C["saffron_t"],
               ec=C["indigo"] if i else C["saffron"])
        ax.text(x + w / 2, 1.24, name, ha="center", fontsize=6.4, fontweight="bold")
        ax.text(x + w / 2, 0.3, result, ha="center", va="center", fontsize=5.6, color=C["ink2"], style="italic")
        if i < 3:
            fs.arrow(ax, x + w, 0.86, x + w + gap, 0.86)
    return f


def fig_moe():
    f, ax = fs.canvas(4.7, 1.6)
    fs.box(ax, 0.0, 0.62, 0.62, 0.42, "a token", size=6.4)
    fs.box(ax, 0.85, 0.57, 0.7, 0.52, "router\npicks 2 of 8", fc=C["slate_t"], ec=C["slate"], size=6.2)
    fs.arrow(ax, 0.62, 0.83, 0.85, 0.83)
    chosen = {1, 5}
    for i in range(8):
        y = 0.05 + i * 0.19
        on = i in chosen
        fs.box(ax, 2.0, y, 0.9, 0.15, f"expert {i + 1}", size=5.6, fc=C["saffron_t"] if on else "white",
               ec=C["saffron"] if on else C["rule"], lw=1.1 if on else 0.6, radius=0.02)
        fs.arrow(ax, 1.55, 0.83, 2.0, y + 0.075, lw=0.9 if on else 0.4, color=C["ink2"] if on else C["grid"])
    fs.box(ax, 3.3, 0.57, 1.3, 0.52, "all 8 experts sit in memory;\nonly 2 do work for this token",
           fc=C["paper"], ec=C["ink2"], size=5.8)
    return f
