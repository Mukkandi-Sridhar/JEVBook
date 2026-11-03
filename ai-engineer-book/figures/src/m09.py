import json
import numpy as np
import figstyle as fs
from figstyle import C

S = json.loads((fs.ROOT / "research" / "m09-stats.json").read_text())


def fig_score_spread():
    f, ax = fs.subplots(height=1.9)
    v = np.array(S["spread"]["values"]) * 100
    c = np.array(S["spread"]["counts"]) / sum(S["spread"]["counts"]) * 100
    inside = (v >= 70) & (v <= 88)
    ax.bar(v, c, width=1.5, color=[C["indigo"] if i else C["slate_t"] for i in inside],
           edgecolor=[C["indigo"] if i else C["slate"] for i in inside], lw=0.5)
    ax.axvline(80, color=C["saffron"], lw=1.2, ls=(0, (4, 2)))
    ax.text(80.6, max(c) * 1.02, "true accuracy: 80%", fontsize=6.2, color=C["saffron"])
    ax.annotate("", xy=(70, -2.2), xytext=(88, -2.2), arrowprops=dict(arrowstyle="<->", color=C["ink2"], lw=0.8),
                annotation_clip=False)
    ax.text(79, -3.6, "9 runs in 10 land between 70% and 88%", ha="center", fontsize=6.2, color=C["ink2"])
    ax.set_xlim(58, 98)
    ax.set_ylim(0, max(c) * 1.18)
    ax.set_xticks([60, 70, 80, 90], ["60%", "70%", "80%", "90%"])
    ax.set_ylabel("share of runs (%)")
    ax.set_xlabel("score on 50 questions", labelpad=16)
    ax.grid(axis="x", visible=False)
    return f


def fig_retrieval_metrics():
    f, ax = fs.canvas(5.2, 1.75)
    qs = [("Q1  opened earbuds?", {"s3"}, ["s3", "s1", "s4", "s2", "s5"], "first right at rank 1: 1/1 = 1.0"),
          ("Q2  opened but faulty?", {"s3", "s4"}, ["s1", "s4", "s2", "s3", "s5"], "first right at rank 2: 1/2 = 0.5"),
          ("Q3  when is my refund?", {"s5"}, ["s1", "s2", "s4", "s3", "s6"], "not found in top 5: 0")]
    for j in range(5):
        ax.text(1.5 + j * 0.37 + 0.155, 1.62, f"rank {j + 1}" if j == 0 else str(j + 1), ha="center", fontsize=6.0,
                color=C["ink2"])
    for i, (q, rel, ranked, rr) in enumerate(qs):
        y = 1.2 - i * 0.5
        ax.text(0.0, y + 0.13, q, fontsize=6.4, va="center")
        for j, d in enumerate(ranked):
            hit = d in rel
            fs.box(ax, 1.5 + j * 0.37, y, 0.31, 0.26, d, size=6.0, fc=C["saffron_t"] if hit else "white",
                   ec=C["saffron"] if hit else C["rule"])
        ax.text(3.45, y + 0.13, rr, fontsize=6.1, va="center", color=C["ink2"])
    return f


def fig_judge_check():
    f, ax = fs.canvas(5.2, 1.85)
    x0, y0, w, h = 1.35, 0.1, 0.95, 0.6
    ax.text(x0 + w, 1.72, "THE JUDGE SAID", ha="center", fontsize=6.4, fontweight="bold", color=C["ink2"])
    ax.text(x0 + w / 2, 1.47, "pass", ha="center", fontsize=6.4)
    ax.text(x0 + 1.5 * w, 1.47, "fail", ha="center", fontsize=6.4)
    ax.text(0.0, 0.75, "THE\nPERSON\nSAID", fontsize=6.4, fontweight="bold", color=C["ink2"], va="center")
    ax.text(x0 - 0.08, y0 + 1.5 * h, "pass (85)", ha="right", va="center", fontsize=6.4)
    ax.text(x0 - 0.08, y0 + 0.5 * h, "fail (15)", ha="right", va="center", fontsize=6.4)
    cells = [(0, 1, "82", "agree", "white"), (1, 1, "3", "too strict", C["paper"]),
             (0, 0, "6", "missed failures", C["crimson_t"]), (1, 0, "9", "caught", C["indigo_t"])]
    for cx, cy, n, lab, fc in cells:
        x, y = x0 + cx * w, y0 + cy * h
        fs.box(ax, x, y, w - 0.04, h - 0.04, "", fc=fc, ec=C["rule"], radius=0.02)
        ax.text(x + w / 2 - 0.02, y + h * 0.58, n, ha="center", fontsize=9, fontweight="bold")
        ax.text(x + w / 2 - 0.02, y + h * 0.25, lab, ha="center", fontsize=5.8, color=C["ink2"])
    ax.text(3.5, 1.15, "Agreement: 91 of 100", fontsize=6.6, fontweight="bold")
    ax.text(3.5, 0.92, "looks good, but…", fontsize=6.2, color=C["ink2"])
    ax.text(3.5, 0.6, "Failures caught: 9 of 15 (60%)", fontsize=6.6, fontweight="bold", color=C["crimson"])
    ax.text(3.5, 0.37, "the number that matters", fontsize=6.2, color=C["ink2"])
    return f


def fig_error_pareto():
    f, ax = fs.subplots(height=1.95)
    cats = [("retrieved the wrong section", 17), ("missed an exception\n(\"unless faulty\")", 11),
            ("answered instead of\n\"a person will reply\"", 8), ("replied in the wrong language", 6),
            ("too long", 4), ("tone", 4)]
    ys = np.arange(len(cats))[::-1]
    ax.barh(ys, [c for _, c in cats], color=[C["saffron"]] * 2 + [C["indigo"]] * 4, height=0.6)
    for y, (_, c) in zip(ys, cats):
        ax.text(c + 0.3, y, str(c), va="center", fontsize=6.4)
    ax.set_yticks(ys, [t for t, _ in cats], fontsize=6.2)
    ax.set_xlabel("failures, out of 50 read (illustrative)")
    ax.set_xlim(0, 20)
    ax.grid(axis="y", visible=False)
    ax.text(19.8, 2.0, "two causes,\n28 of 50", ha="right", va="center", fontsize=6.4, color=C["saffron"])
    return f


def fig_pass_k():
    f, ax = fs.subplots(height=1.95)
    ks = np.arange(1, 11)
    for i, p in enumerate(["0.95", "0.9", "0.8"]):
        st = fs.SERIES[i]
        ax.plot(ks, np.array(S["pass_k"][p]) * 100, color=st["color"], ls=st["ls"], marker=st["marker"], ms=3.5)
        ax.text(10.2, S["pass_k"][p][-1] * 100, f"{float(p):.0%} per run", fontsize=6.2, color=st["color"],
                va="center")
    ax.set_xticks(ks)
    ax.set_xlim(0.7, 12.3)
    ax.set_ylim(0, 105)
    ax.set_yticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
    ax.set_xlabel("number of runs of the same task (k)")
    ax.set_ylabel("chance all k succeed")
    return f


def fig_eval_loop():
    f, ax = fs.canvas(5.2, 2.1)
    steps = [(0.0, 1.35, "Production\nreal chats"), (1.4, 1.35, "Sample and\nread failures"),
             (2.8, 1.35, "Add them to the\ngolden set"), (2.8, 0.15, "Change prompt,\nmodel or pipeline"),
             (1.4, 0.15, "Run the evals\non every change"), (0.0, 0.15, "Release if it\nbeats the old one")]
    for x, y, t in steps:
        fs.box(ax, x, y, 1.15, 0.55, t, size=6.2, fc=C["indigo_t"] if "evals" in t or "golden" in t else "white",
               ec=C["indigo"] if "evals" in t or "golden" in t else None)
    fs.arrow(ax, 1.15, 1.62, 1.4, 1.62)
    fs.arrow(ax, 2.55, 1.62, 2.8, 1.62)
    fs.arrow(ax, 3.37, 1.35, 3.37, 0.7)
    fs.arrow(ax, 2.8, 0.42, 2.55, 0.42)
    fs.arrow(ax, 1.4, 0.42, 1.15, 0.42)
    fs.arrow(ax, 0.57, 0.7, 0.57, 1.35)
    ax.text(4.15, 1.0, "The golden set\ngrows from real\nfailures, so the\nsame mistake\ncannot come back\nunnoticed.",
            fontsize=6.2, color=C["ink2"], va="center")
    return f
