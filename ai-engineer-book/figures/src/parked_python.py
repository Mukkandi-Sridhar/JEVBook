import figstyle as fs
from figstyle import C


def fig_retry():
    f, ax = fs.canvas(4.7, 2.2)
    fs.box(ax, 0.0, 0.85, 0.75, 0.5, "Call the\nmodel", size=6.6, weight="bold")
    fs.box(ax, 1.0, 0.85, 0.85, 0.5, "Did it\nsucceed?", fc=C["slate_t"], ec=C["slate"], size=6.6)
    fs.arrow(ax, 0.75, 1.1, 1.0, 1.1)
    fs.box(ax, 2.2, 1.55, 0.9, 0.42, "Use the reply", fc=C["indigo_t"], ec=C["indigo"], size=6.4)
    fs.arrow(ax, 1.85, 1.25, 2.2, 1.7)
    ax.text(1.98, 1.55, "yes", fontsize=5.8, color=C["ink2"])
    fs.box(ax, 2.2, 0.85, 0.9, 0.5, "Can waiting\nfix it?", fc=C["slate_t"], ec=C["slate"], size=6.4)
    fs.arrow(ax, 1.85, 1.1, 2.2, 1.1)
    ax.text(1.95, 1.15, "no", fontsize=5.8, color=C["ink2"])
    ax.text(2.65, 0.6, "429 busy, 500, 529,\ntimeout", ha="center", fontsize=5.6, color=C["ink2"], va="top")
    fs.box(ax, 3.45, 1.55, 1.2, 0.42, "Stop and fix the request\n(400 bad input, 401 key)", fc=C["crimson_t"],
           ec=C["crimson"], size=5.8, lw=1.4)
    fs.arrow(ax, 3.1, 1.2, 3.45, 1.7)
    ax.text(3.18, 1.5, "no", fontsize=5.8, color=C["ink2"])
    fs.box(ax, 3.45, 0.75, 1.2, 0.6, "Wait a random time\nup to 1, 2, 4, 8 s…\n(longer each try)", fc="white",
           size=5.8)
    fs.arrow(ax, 3.1, 1.05, 3.45, 1.05)
    ax.text(3.2, 1.1, "yes", fontsize=5.8, color=C["ink2"])
    fs.arrow(ax, 4.05, 0.75, 4.05, 0.35, style="-")
    fs.arrow(ax, 4.05, 0.35, 0.37, 0.35, style="-")
    fs.arrow(ax, 0.37, 0.35, 0.37, 0.85)
    ax.text(2.2, 0.2, "try again, up to a fixed number of times, then give up and log it", ha="center",
            fontsize=5.8, color=C["ink2"], style="italic")
    return f


def fig_timeline():
    f, ax = fs.subplots(height=1.9)
    # One at a time: 6 calls of 3 s
    for i in range(6):
        ax.barh(1, 0.15, left=i * 3, color=C["saffron"], height=0.42)
        ax.barh(1, 2.85, left=i * 3 + 0.15, color=C["saffron_t"], height=0.42, edgecolor=C["saffron"], lw=0.4,
                hatch="....")
    # Six at once: six calls start together and wait together
    for i in range(6):
        y = -0.3 + i * 0.1
        ax.barh(y, 0.15, left=i * 0.03, color=C["indigo"], height=0.08)
        ax.barh(y, 2.85, left=i * 0.03 + 0.15, color=C["indigo_t"], height=0.08, edgecolor=C["indigo"], lw=0.3,
                hatch="....")
    ax.set_yticks([1, -0.05], ["One at a time", "Six at once"])
    ax.set_xlim(0, 20.5)
    ax.set_xlabel("seconds")
    ax.grid(axis="y", visible=False)
    ax.text(18.3, 1, "18 s", va="center", ha="left", fontsize=7, color=C["ink"], fontweight="bold")
    ax.text(3.3, -0.05, "about 3 s", va="center", ha="left", fontsize=7, color=C["ink"], fontweight="bold")
    ax.text(9, 1.55, "solid: your code working     dotted: waiting for the model's reply", ha="center",
            fontsize=6.2, color=C["ink2"])
    ax.set_ylim(-0.5, 1.75)
    return f


def fig_pipeline():
    f, ax = fs.canvas(4.7, 1.55)
    steps = [("1", "4,000\nmessages\n(file)"), ("2", "Up to 20\ncalls at\nonce"), ("3", "Call with\nretry and\nback-off"),
             ("4", "Check the\nreply's shape\n(Ticket)"), ("5", "Save each\nresult\nat once")]
    w, gap = 0.78, 0.2
    for i, (n, t) in enumerate(steps):
        x = i * (w + gap)
        fs.box(ax, x, 0.45, w, 0.75, t, fc=C["indigo_t"] if i in (1, 2, 3) else "white",
               ec=C["indigo"] if i in (1, 2, 3) else None, size=6.2)
        ax.text(x + 0.1, 1.1, n, fontsize=6.4, fontweight="bold", color=C["saffron"], va="center")
        if i < len(steps) - 1:
            fs.arrow(ax, x + w, 0.82, x + w + gap, 0.82)
    ax.text(3 * (w + gap) + w / 2, 0.28, "bad reply:\nlog it, move on", ha="center", va="top", fontsize=5.6,
            color=C["crimson"], style="italic")
    ax.text(4 * (w + gap) + w / 2, 0.28, "a restart skips\nsaved messages", ha="center", va="top", fontsize=5.6,
            color=C["ink2"], style="italic")
    return f
