import figstyle as fs
from figstyle import C


def fig_network():
    f, ax = fs.canvas(4.7, 2.4)
    layers = [3, 5, 4, 2]
    xs = [0.6, 1.75, 2.9, 4.05]
    names = ["Inputs\n(pixels, words)", "Simple checks", "Combined checks", "Output\nprobabilities"]
    pos = []
    for n, x in zip(layers, xs):
        ys = [0.55 + (1.5 / (n - 1)) * i if n > 1 else 1.3 for i in range(n)]
        pos.append([(x, y) for y in ys])
    for a, b in zip(pos, pos[1:]):
        for (x1, y1) in a:
            for (x2, y2) in b:
                ax.plot([x1, x2], [y1, y2], color=C["rule"], lw=0.5)
    cols = [C["indigo"], C["plum"], C["plum"], C["saffron"]]
    for layer, col in zip(pos, cols):
        for (x, y) in layer:
            ax.scatter([x], [y], s=110, color="white", edgecolor=col, lw=1.4, zorder=3)
    for x, t in zip(xs, names):
        ax.text(x, 0.18, t, ha="center", va="center", fontsize=6.6)
    return f


def fig_memory():
    f, ax = fs.subplots(height=2.0)
    labels = ["Run in FP32", "Run in BF16", "Run in INT8", "Run in 4-bit", "Train fully\n(about 16 bytes each)"]
    vals = [28, 14, 7, 3.5, 112]
    cols = [C["indigo"]] * 4 + [C["crimson"]]
    y = range(len(labels))[::-1]
    for yi, v, c, i in zip(y, vals, cols, range(5)):
        ax.barh(yi, v, color=c, height=0.6, hatch="////" if i == 4 else None, edgecolor="white", lw=0.6)
        ax.text(v + 1.5, yi, f"{v:g} GB", va="center", fontsize=6.8)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels)
    ax.set_xlabel("GPU memory for a 7B model (GB)")
    ax.set_xlim(0, 128)
    ax.grid(axis="y", visible=False)
    return f
