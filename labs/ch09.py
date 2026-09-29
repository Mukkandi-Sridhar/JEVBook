# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
# ---

# %% [markdown]
# # Lab 9 · Training at scale, and why big models are overconfident
#
# *Decide, Don't Generate*, Chapter 9.
#
# 1. A miniature "scaling" curve: next-word prediction gets better with more text.
# 2. Overtrain a network on Kestrel's alerts and watch accuracy stay flat while calibration collapses.
# 3. Fix it with temperature and Platt scaling, and compare with simply stopping early.

# %%
import importlib.util, subprocess, sys
if importlib.util.find_spec("jevkit") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "typesafe-sdk==0.7.2", "autograd",
                    "git+https://github.com/Mukkandi-Sridhar/JEVBook"], check=True)

# %%
from collections import Counter, defaultdict
import numpy as np
from jevkit import text

notes = text.notes_corpus(40000)
train_notes, test_notes = notes[:30000], notes[30000:33000]
V = len({w for n in notes for w in n}) + 2

def trigram_loss(n_train):
    counts = defaultdict(Counter)
    for s in train_notes[:n_train]:
        t = ["<s>", "<s>"] + s + ["</s>"]
        for a, b, c in zip(t, t[1:], t[2:]):
            counts[(a, b)][c] += 1
    total, n = 0.0, 0
    for s in test_notes:
        t = ["<s>", "<s>"] + s + ["</s>"]
        for a, b, c in zip(t, t[1:], t[2:]):
            ctx = counts[(a, b)]
            total -= np.log((ctx[c] + 0.05) / (sum(ctx.values()) + 0.05 * V))
            n += 1
    return total / n

for n in (30, 300, 3000, 30000):
    print(f"{n:>6} notes: next-word log loss {trigram_loss(n):.3f}")

# %% [markdown]
# ## Overtraining

# %%
import warnings
from sklearn.neural_network import MLPClassifier
from jevkit import soc, calibration as cal
from jevkit.learn import Standardizer

alerts = soc.load()
train, calib, test = soc.split(alerts)
F = lambda d: soc.feature_matrix(d).to_numpy()
st = Standardizer().fit(F(train))
net = MLPClassifier(hidden_layer_sizes=(128, 128), learning_rate_init=0.002, random_state=0, batch_size=256)
for epoch in range(1, 201):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        net.partial_fit(st(F(train)), train.malicious, classes=[0, 1])
    if epoch in (3, 20, 60, 200):
        p = net.predict_proba(st(F(test)))[:, 1]
        acc = ((p > 0.5) == test.malicious).mean()
        s = cal.summary(p, test.malicious)
        print(f"epoch {epoch:3d}: accuracy {acc:.3f}  log loss {s['log_loss']:.3f}  ECE {s['ece']:.3f}")

# %% [markdown]
# ## Fixing it after the fact

# %%
p_cal = net.predict_proba(st(F(calib)))[:, 1]
for name, fix in (("temperature", cal.Temperature()), ("Platt", cal.Platt())):
    fix.fit(p_cal, calib.malicious)
    print(f"{name:>11}: ECE {cal.ece(fix(p), test.malicious):.3f}  log loss {cal.log_loss(fix(p), test.malicious):.3f}")
