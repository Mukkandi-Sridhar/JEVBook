# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
# ---

# %% [markdown]
# # Lab 3 · Data, loss and gradient descent
#
# *Decide, Don't Generate*, Chapter 3. You'll build logistic regression from scratch in NumPy,
# train it by gradient descent, and check it on alerts it never saw. Synthetic data throughout.

# %%
import importlib.util, subprocess, sys
if importlib.util.find_spec("jevkit") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "typesafe-sdk==0.7.2",
                    "git+https://github.com/Mukkandi-Sridhar/JEVBook"], check=True)

# %%
import numpy as np
from jevkit import soc

alerts = soc.load()
train, calib, test = soc.split(alerts)        # 60% / 20% / 20%
X = soc.feature_matrix(train).to_numpy()
Xt = soc.feature_matrix(test).to_numpy()
y, yt = train.malicious.to_numpy(), test.malicious.to_numpy()
print(X.shape, Xt.shape)

# %% [markdown]
# ## The model: add up evidence, squash with the S-curve

# %%
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def log_loss(p, y):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))

# put every feature on a similar scale so one step size suits them all
mu, sd = X.mean(0), X.std(0) + 1e-9
Xs, Xts = (X - mu) / sd, (Xt - mu) / sd

# %% [markdown]
# ## Gradient descent

# %%
w, b = np.zeros(X.shape[1]), 0.0
for step in range(401):
    p = sigmoid(Xs @ w + b)
    w -= 0.5 * Xs.T @ (p - y) / len(y)     # the slope, for every weight at once
    b -= 0.5 * np.mean(p - y)
    if step % 100 == 0:
        print(f"step {step:3d}  loss {log_loss(p, y):.4f}")

# %% [markdown]
# ## On alerts it never saw

# %%
pt = sigmoid(Xts @ w + b)
print(f"test log loss   {log_loss(pt, yt):.4f}")
print(f"truth log loss  {log_loss(test.p_true.to_numpy(), yt):.4f}   (the best possible)")

# %% [markdown]
# **Try:** change the step size from 0.5 to 5 and to 0.01. What happens to the printed loss?
#
# **Try:** add a feature that leaks the answer, e.g. `Xs = np.c_[Xs, y]`. What happens to the training
# loss? Why is that useless?

# %% [markdown]
# ## Overfitting: a model that memorises

# %%
from sklearn.tree import DecisionTreeClassifier
for depth in (2, 4, 8, 16):
    t = DecisionTreeClassifier(max_depth=depth, random_state=0).fit(X, y)
    tr = log_loss(np.clip(t.predict_proba(X)[:, 1], 1e-3, 1 - 1e-3), y)
    te = log_loss(np.clip(t.predict_proba(Xt)[:, 1], 1e-3, 1 - 1e-3), yt)
    print(f"depth {depth:2d}: train {tr:.3f}  test {te:.3f}")
