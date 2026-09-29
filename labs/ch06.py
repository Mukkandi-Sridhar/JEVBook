# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
# ---

# %% [markdown]
# # Lab 6 · Neurons to networks
#
# *Decide, Don't Generate*, Chapter 6.
#
# 1. A toy problem one neuron can't solve: "unusual in any direction".
# 2. A one-hidden-layer network in NumPy, trained with backpropagation.
# 3. Networks on Kestrel's alerts: bigger is not automatically better.

# %%
import importlib.util, subprocess, sys
if importlib.util.find_spec("jevkit") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "typesafe-sdk==0.7.2",
                    "git+https://github.com/Mukkandi-Sridhar/JEVBook"], check=True)

# %%
import numpy as np
from jevkit.learn import sigmoid, log_loss, fit_logistic

rng = np.random.default_rng(3)
X = rng.uniform(-1, 1, (700, 2))
far = np.sqrt(((X - [0.1, 0.05]) ** 2).sum(1))
y = (rng.random(700) < sigmoid(12 * (far - 0.92))).astype(float)   # suspicious when far from normal

w, b, _ = fit_logistic(X, y, lr=1, steps=3000)
print(f"one neuron: log loss {log_loss(sigmoid(X @ w + b), y):.3f}")

# %% [markdown]
# ## A hidden layer, from scratch

# %%
H = 12
W1 = rng.normal(0, 1, (2, H)); b1 = np.zeros(H)
W2 = rng.normal(0, 0.3, H);    b2 = 0.0
lr = 0.3
for step in range(3001):
    h_in = X @ W1 + b1
    h = np.maximum(0, h_in)                      # ReLU hinges
    p = sigmoid(h @ W2 + b2)                     # forward pass
    d_out = (p - y) / len(y)                     # blame at the output
    d_h = np.outer(d_out, W2) * (h_in > 0)       # blame flows back through the hinges
    W2 -= lr * h.T @ d_out; b2 -= lr * d_out.sum()
    W1 -= lr * X.T @ d_h;   b1 -= lr * d_h.sum(0)
    if step % 1000 == 0:
        print(f"step {step:4d}  loss {log_loss(p, y):.3f}")

# %% [markdown]
# **Try:** delete the ReLU (use `h = h_in`). What happens to the loss, and why?

# %% [markdown]
# ## On Kestrel's alerts

# %%
import warnings
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from jevkit import soc, calibration as cal
from jevkit.learn import Standardizer

alerts = soc.load()
train, calib, test = soc.split(alerts)
F = lambda d: soc.feature_matrix(d).to_numpy()
st = Standardizer().fit(F(train))
models = {
    "logistic regression": LogisticRegression(C=1e4, max_iter=5000),
    "network, 16 units": MLPClassifier(hidden_layer_sizes=(16,), max_iter=400, random_state=0),
    "network, 64+64 units": MLPClassifier(hidden_layer_sizes=(64, 64), max_iter=400, random_state=0),
}
for name, m in models.items():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        m.fit(st(F(train)), train.malicious)
    s = cal.summary(m.predict_proba(st(F(test)))[:, 1], test.malicious)
    print(f"{name:>22}: AUC {s['auc']:.3f}  log loss {s['log_loss']:.3f}  ECE {s['ece']:.3f}")
