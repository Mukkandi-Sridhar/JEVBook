import numpy as np
import figstyle as fs
from figstyle import C


def fig_history_cost():
    """Input tokens per turn when the whole history is resent (assumed sizes)."""
    f, ax = fs.subplots(height=2.0)
    turns = np.arange(1, 21)
    fixed = np.full_like(turns, 1300)
    history = 150 * (turns - 1)
    new = np.full_like(turns, 40)
    ax.bar(turns, fixed, color=C["indigo_t"], edgecolor=C["indigo"], lw=0.5, width=0.72, label="instructions + tools")
    ax.bar(turns, history, bottom=fixed, color=C["saffron"], width=0.72, label="earlier messages, sent again")
    ax.bar(turns, new, bottom=fixed + history, color=C["ink"], width=0.72, label="the new message")
    ax.set_xticks([1, 5, 10, 15, 20])
    ax.set_xlabel("turn of the conversation")
    ax.set_ylabel("input tokens for that turn")
    ax.set_yticks([0, 1000, 2000, 3000, 4000], ["0", "1,000", "2,000", "3,000", "4,000"])
    ax.set_ylim(0, 5000)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper left", ncol=1, fontsize=6.4)
    ax.text(20, 1300 + 2850 + 40 + 120, "turn 20:\n4,190 tokens", ha="center", fontsize=6.2)
    return f


def _chips(ax, y, kept, label, summary=False, n=20):
    ax.text(0.95, y + 0.1, label, ha="right", va="center", fontsize=6.6, fontweight="bold")
    x0, w = 1.05, 0.19
    for i in range(1, n + 1):
        x = x0 + (i - 1) * w
        on = i in kept
        order = i == 1
        fc = (C["saffron_t"] if order else C["indigo_t"]) if on else "white"
        ec = (C["saffron"] if order else C["indigo"]) if on else C["grid"]
        fs.box(ax, x, y, w - 0.04, 0.2, "", fc=fc, ec=ec, lw=0.7, radius=0.02)
        if order:
            ax.text(x + (w - 0.04) / 2, y + 0.1, "#", ha="center", va="center", fontsize=6,
                    color=C["saffron"] if on else C["muted"], fontweight="bold")
    if summary:
        fs.box(ax, x0 - 0.02, y - 0.26, 2.85, 0.19, "summary of messages 1–14, with order TK-5521", size=5.6,
               fc=C["paper"], ec=C["ink2"], lw=0.7, radius=0.02)


def fig_trim_summarise():
    f, ax = fs.canvas(5.2, 2.25)
    ax.text(1.05, 2.12, "20 earlier messages of about 75 tokens each; message 1 holds the order number (#)", fontsize=6.2, color=C["ink2"])
    _chips(ax, 1.75, set(range(1, 21)), "Everything")
    _chips(ax, 1.3, set(range(15, 21)), "Trim")
    ax.text(5.0, 1.4, "450 tokens\norder number lost", fontsize=6.0, color=C["crimson"], ha="left", va="center")
    _chips(ax, 0.6, set(range(15, 21)), "Summary +\nlast 6", summary=True)
    ax.text(5.0, 0.6, "650 tokens\norder number kept", fontsize=6.0, color=C["indigo"], ha="left",
            va="center")
    ax.text(5.0, 1.85, "1,500 tokens", fontsize=6.0, color=C["ink2"], ha="left", va="center")
    ax.text(1.05, 0.05, "Filled boxes are sent to the model. (Sizes assumed for illustration.)", fontsize=6.0,
            color=C["ink2"])
    return f


def fig_hooks():
    f, ax = fs.canvas(5.2, 1.7)
    fs.box(ax, 0.0, 0.6, 0.85, 0.5, "Customer's\nmessage", size=6.6)
    fs.box(ax, 1.1, 0.35, 1.3, 1.0, "", fc=C["indigo_t"], ec=C["indigo"])
    ax.text(1.75, 1.2, "BEFORE THE MODEL", ha="center", fontsize=6.4, fontweight="bold", color=C["indigo"])
    ax.text(1.18, 0.78, "• load the thread\n• add saved memories\n• summarise if too long", fontsize=6.0,
            va="center", linespacing=1.4)
    fs.box(ax, 2.65, 0.6, 0.8, 0.5, "Model", size=7, weight="bold", fc=C["saffron_t"], ec=C["saffron"])
    fs.box(ax, 3.7, 0.35, 1.3, 1.0, "", fc=C["indigo_t"], ec=C["indigo"])
    ax.text(4.35, 1.2, "AFTER THE MODEL", ha="center", fontsize=6.4, fontweight="bold", color=C["indigo"])
    ax.text(3.78, 0.78, "• save the thread\n• note new facts\n• log tokens and cost", fontsize=6.0,
            va="center", linespacing=1.4)
    for x1, x2 in [(0.85, 1.1), (2.4, 2.65), (3.45, 3.7)]:
        fs.arrow(ax, x1, 0.85, x2, 0.85, lw=1.0)
    ax.text(2.6, 0.08, "Middleware: your code, run around every model call", ha="center", fontsize=6.2,
            color=C["ink2"])
    return f


def fig_memory_store():
    f, ax = fs.canvas(5.2, 2.45)
    # short-term
    ax.text(0.0, 2.33, "SHORT-TERM: one conversation", fontsize=6.6, fontweight="bold", color=C["saffron"])
    for i, (tid, msgs) in enumerate([("cust-881:chat-17", "12 Oct · earbuds refund · 14 messages"),
                                     ("cust-881:chat-18", "today · \"same problem as last time\""),
                                     ("cust-312:chat-4", "today · size exchange · 6 messages")]):
        y = 1.83 - i * 0.42
        fs.box(ax, 0.0, y, 2.35, 0.34, "", fc="white", ec=C["saffron"], lw=0.8)
        ax.text(0.08, y + 0.23, tid, fontsize=6.0, fontweight="bold", family="monospace" if False else None)
        ax.text(0.08, y + 0.09, msgs, fontsize=5.7, color=C["ink2"])
    ax.text(0.0, 0.45, "key: thread_id\nkept by a checkpointer", fontsize=6.0, color=C["ink2"], va="top")
    # long-term
    ax.text(2.75, 2.33, "LONG-TERM: across conversations", fontsize=6.6, fontweight="bold", color=C["indigo"])
    fs.box(ax, 2.75, 0.62, 2.45, 1.58, "", fc=C["indigo_t"], ec=C["indigo"], lw=0.9)
    ax.text(2.85, 2.06, "customers / cust-881", fontsize=6.2, fontweight="bold")
    rows = [("fact", "Prefers replies in Hinglish"),
            ("event", "12 Oct: refund for earbuds approved"),
            ("event", "18 Oct: refund received"),
            ("how-to", "Send the tracking link with\nevery delivery answer")]
    y = 1.82
    for kind, text in rows:
        ax.text(2.85, y, kind, fontsize=5.8, color=C["indigo"], fontweight="bold", va="top")
        ax.text(3.4, y, text, fontsize=5.8, va="top", linespacing=1.2)
        y -= 0.27 if "\n" not in text else 0.4
    ax.text(2.75, 0.45, "key: customer id, from your login system\nkept in a store", fontsize=6.0,
            color=C["ink2"], va="top")
    fs.arrow(ax, 2.37, 1.6, 2.73, 1.6, lw=0.9, ls=(0, (3, 2)))
    return f
