import figstyle as fs
from figstyle import C
from matplotlib.patches import Ellipse


def fig_map():
    f, ax = fs.subplots(height=2.8)
    groups = [
        (C["indigo"], "o", [("refund", .10, .84), ("money back", .27, .80), ("paisa wapas", .07, .68),
                          ("amount not credited", .20, .60)], (.24, .72, .48, .40), "refunds"),
        (C["saffron"], "s", [("delivery", .62, .84), ("courier", .82, .80), ("order nahi aaya", .58, .68),
                            ("tracking not working", .70, .59)], (.76, .72, .46, .40), "delivery"),
        (C["plum"], "^", [("battery life", .33, .30), ("screen size", .50, .21),
                          ("size chart", .35, .12)], (.47, .21, .44, .32), "product questions"),
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
