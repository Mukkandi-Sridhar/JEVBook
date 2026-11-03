import figstyle as fs
from figstyle import C


def fig_tool_sequence():
    """Who does what in one tool call: your program, the model, the function."""
    f, ax = fs.canvas(5.2, 3.0)
    lanes = [(0.7, "YOUR PROGRAM", C["slate"]), (2.6, "THE MODEL", C["saffron"]), (4.5, "THE FUNCTION", C["indigo"])]
    for x, name, col in lanes:
        ax.text(x, 2.9, name, ha="center", fontsize=6.8, fontweight="bold", color=col)
        ax.plot([x, x], [0.05, 2.78], color=C["grid"], lw=1.2, zorder=0)

    def msg(y, x1, x2, n, text, col=C["ink2"]):
        fs.arrow(ax, x1, y, x2, y, lw=1.0, color=col)
        xm = (x1 + x2) / 2
        ax.text(xm, y + 0.05, f"{n}  {text}", ha="center", va="bottom", fontsize=6.0, linespacing=1.25)

    msg(2.45, 0.7, 2.6, 1, "messages + tool list\n\"Where is TK-5521?\"")
    msg(1.85, 2.6, 0.7, 2, "AI message with a tool call\ncheck_order_status(order_id=\"TK-5521\")",
        C["saffron"])
    msg(1.25, 0.7, 4.5, 3, "your code runs the function", C["indigo"])
    msg(0.95, 4.5, 0.7, 4, "\"Out for delivery, by 7 pm\"", C["indigo"])
    msg(0.55, 0.7, 2.6, 5, "everything so far + a tool message\nwith the result")
    fs.box(ax, 3.0, 0.05, 2.2, 0.36, "6  The model writes the reply:\n\"Your parcel arrives today by 7 pm.\"",
           size=5.9, fc=C["saffron_t"], ec=C["saffron"], ha="left")
    ax.text(2.75, 1.6, "the model only asks; your code decides and runs", fontsize=5.9, color=C["crimson"],
            va="center", ha="left")
    return f


def fig_structured():
    f, ax = fs.canvas(5.2, 1.55)
    fs.box(ax, 0.0, 0.3, 1.85, 0.95,
           "\"bhai mera refund abhi tak\nnahi aaya, order TK-5521,\n10 din ho gaye!!\"", size=6.4, fc="white")
    ax.text(0.92, 1.36, "CUSTOMER MESSAGE", ha="center", fontsize=6.2, fontweight="bold", color=C["ink2"])
    fs.arrow(ax, 1.9, 0.78, 2.35, 0.78, lw=1.2)
    ax.text(2.12, 0.88, "model", ha="center", fontsize=5.8, color=C["ink2"])
    fs.box(ax, 2.4, 0.3, 1.55, 0.95, "", fc=C["indigo_t"], ec=C["indigo"])
    for i, (k, v) in enumerate([("category", "\"refund\""), ("order_id", "\"TK-5521\""), ("urgent", "true")]):
        y = 1.05 - i * 0.27
        ax.text(2.5, y, k, fontsize=6.4, fontweight="bold", va="center")
        ax.text(3.2, y, v, fontsize=6.4, va="center")
    ax.text(3.17, 1.36, "TICKET (FIXED SHAPE)", ha="center", fontsize=6.2, fontweight="bold", color=C["indigo"])
    fs.arrow(ax, 4.0, 0.78, 4.3, 0.78, lw=1.2)
    ax.text(4.35, 0.78, "your code\nroutes it", fontsize=6.2, va="center")
    return f


def fig_risk_grid():
    f, ax = fs.canvas(5.2, 2.35)
    x0, y0, w, h = 1.15, 0.1, 1.95, 0.9
    ax.text(x0 + w / 2, 2.17, "small or easy to undo", ha="center", fontsize=6.6, fontweight="bold")
    ax.text(x0 + w * 1.5 + 0.05, 2.17, "large or hard to undo", ha="center", fontsize=6.6, fontweight="bold")
    ax.text(x0 - 0.1, y0 + h * 1.5 + 0.05, "READS\n(looks things up)", ha="right", va="center", fontsize=6.4,
            fontweight="bold")
    ax.text(x0 - 0.1, y0 + h / 2, "WRITES\n(changes things)", ha="right", va="center", fontsize=6.4,
            fontweight="bold")
    cells = [
        (0, 1, "Model calls it freely", "order status, policy search", "white", C["rule"]),
        (1, 1, "Freely, but check whose data", "a customer's full order history", "white", C["rule"]),
        (0, 0, "Model calls it, code sets limits", "resend invoice, refund up to ₹2,000", C["saffron_t"],
         C["saffron"]),
        (1, 0, "A person approves first", "refund above ₹2,000, cancel account", C["crimson_t"], C["crimson"]),
    ]
    for cx, cy, title, ex, fc, ec in cells:
        x, y = x0 + cx * (w + 0.1), y0 + cy * (h + 0.1)
        fs.box(ax, x, y, w, h, "", fc=fc, ec=ec, lw=1.0)
        ax.text(x + w / 2, y + h * 0.62, title, ha="center", va="center", fontsize=6.6, fontweight="bold")
        ax.text(x + w / 2, y + h * 0.3, ex, ha="center", va="center", fontsize=6.0, color=C["ink2"])
    return f


def fig_trifecta():
    f, ax = fs.canvas(5.2, 2.4)
    fs.box(ax, 2.05, 0.85, 1.1, 0.5, "Agent", size=7.4, weight="bold", fc=C["saffron_t"], ec=C["saffron"])
    legs = [(0.0, 1.55, "Reads untrusted text", "customer emails, reviews,\nweb pages, documents"),
            (3.55, 1.55, "Sees private data", "orders, addresses,\nother customers' details"),
            (1.78, 0.0, "Can act or send out", "refunds, emails, web requests")]
    for x, y, t, sub in legs:
        fs.box(ax, x, y, 1.65, 0.6, "", fc=C["crimson_t"], ec=C["crimson"], lw=1.0)
        ax.text(x + 0.825, y + 0.43, t, ha="center", va="center", fontsize=6.6, fontweight="bold")
        ax.text(x + 0.825, y + 0.19, sub, ha="center", va="center", fontsize=5.8, color=C["ink2"])
    fs.arrow(ax, 1.65, 1.75, 2.1, 1.35, lw=1.0, color=C["crimson"])
    fs.arrow(ax, 3.55, 1.75, 3.1, 1.35, lw=1.0, color=C["crimson"])
    fs.arrow(ax, 2.6, 0.85, 2.6, 0.6, lw=1.0, color=C["crimson"])
    ax.text(2.6, 2.32, "All three together: hidden instructions can steal data or act", ha="center",
            fontsize=6.2, color=C["crimson"])
    return f
