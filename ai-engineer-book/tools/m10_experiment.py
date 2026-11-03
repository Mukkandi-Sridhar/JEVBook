"""Synthetic refund-review experiment for Module 10 (all data generated here; nothing real).

Task: predict whether Tarkika's refund team would REJECT a refund request.
"""
import json
from pathlib import Path
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, brier_score_loss

rng = np.random.default_rng(42)
N = 20000
value = rng.lognormal(7.2, 0.8, N)                     # order value in rupees
days = rng.integers(0, 30, N)                          # days since delivery
cat = rng.choice(4, N, p=[0.35, 0.35, 0.2, 0.1])       # electronics, fashion, home, hygiene
past = rng.poisson(0.6, N)                             # returns in the last 90 days
photo = rng.random(N) < 0.55                           # photo attached
age = rng.exponential(400, N)                          # account age in days
z = (-4.0 + 0.9 * (days > 10) + 0.6 * np.log(value / 1500) + 0.55 * past - 0.9 * photo
     - 0.002 * np.minimum(age, 1000) + np.array([0.3, -0.2, 0.0, 1.6])[cat])
p_true = 1 / (1 + np.exp(-z))
y = (rng.random(N) < p_true).astype(int)

def onehot(c):
    return np.eye(4)[c][:, 1:]
X = np.column_stack([days > 10, np.log(value / 1500), past, photo, np.minimum(age, 1000) / 1000, onehot(cat)])
leak = np.column_stack([X, y * rng.uniform(0.6, 1, N) + (1 - y) * rng.uniform(0, 0.3, N)])  # "team note length"

idx_tr, idx_te = train_test_split(np.arange(N), test_size=0.3, random_state=0, stratify=y)
res = {"n": N, "reject_rate": float(y.mean())}
res["baseline_acc"] = float(accuracy_score(y[idx_te], np.zeros(len(idx_te))))

lr = LogisticRegression(max_iter=2000).fit(X[idx_tr], y[idx_tr])
p_lr = lr.predict_proba(X[idx_te])[:, 1]
res["lr_acc"] = float(accuracy_score(y[idx_te], p_lr > 0.5))
res["lr_brier"] = float(brier_score_loss(y[idx_te], p_lr))

tree = DecisionTreeClassifier(random_state=0).fit(X[idx_tr], y[idx_tr])
res["tree_train_acc"] = float(tree.score(X[idx_tr], y[idx_tr]))
res["tree_test_acc"] = float(tree.score(X[idx_te], y[idx_te]))
p_tree = tree.predict_proba(X[idx_te])[:, 1]
sure_reject = p_tree >= 0.99
res["tree_says_100_share"] = float(sure_reject.mean())
res["tree_says_100_right"] = float(y[idx_te][sure_reject].mean())

lr_leak = LogisticRegression(max_iter=2000).fit(leak[idx_tr], y[idx_tr])
res["leak_acc"] = float(lr_leak.score(leak[idx_te], y[idx_te]))

def reliability(p, yy, bins=(0, .02, .05, .1, .2, .35, .5, .7, 1.0001)):
    out = []
    for a, b in zip(bins[:-1], bins[1:]):
        m = (p >= a) & (p < b)
        if m.sum() >= 20:
            out.append({"said": float(p[m].mean()), "happened": float(yy[m].mean()), "n": int(m.sum())})
    return out
res["rel_lr"] = reliability(p_lr, y[idx_te])
res["rel_tree"] = reliability(p_tree, y[idx_te], bins=(0, 0.5, 1.0001))

# Thresholds by cost: wrongly approving a refund the team would reject loses about Rs 1,500;
# a review costs about Rs 40 of staff time and delay.
cost_bad, cost_review = 1500, 40
t_low = cost_review / cost_bad
t_high = 0.2
yy = y[idx_te]
bands = {"act": p_lr < t_low, "review": (p_lr >= t_low) & (p_lr < t_high), "escalate": p_lr >= t_high}
res["t_low"] = t_low
res["bands"] = {k: {"share": float(m.mean()), "reject_rate": float(yy[m].mean()) if m.any() else 0}
                for k, m in bands.items()}
def total_cost(t):
    auto = p_lr < t
    return float((yy[auto] * cost_bad).sum() + (~auto).sum() * cost_review) / len(yy)
res["cost_per_request"] = {f"{t:.3f}": round(total_cost(t), 1) for t in [0.0, 0.01, t_low, 0.05, 0.1, 0.2, 1.0001]}
ts = np.linspace(0, 0.3, 61)
res["cost_curve"] = [[float(t), total_cost(t)] for t in ts]
Path(__file__).resolve().parents[1].joinpath("research/m10-experiment.json").write_text(json.dumps(res, indent=1))
print(json.dumps({k: v for k, v in res.items() if k != "cost_curve"}, indent=1))
