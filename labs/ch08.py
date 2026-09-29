# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
# ---

# %% [markdown]
# # Lab 8 · Attention and transformers, visually
#
# *Decide, Don't Generate*, Chapter 8.
#
# 1. Self-attention in 10 lines of NumPy.
# 2. A task a bag of words can't solve: "invoice not phishing" vs "phishing not invoice".
# 3. Train a one-layer attention model (NumPy + autograd) and look at what it attends to.

# %%
import importlib.util, subprocess, sys
if importlib.util.find_spec("jevkit") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "typesafe-sdk==0.7.2", "autograd",
                    "git+https://github.com/Mukkandi-Sridhar/JEVBook"], check=True)

# %%
import numpy as np

def softmax(s):
    s = s - s.max(-1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(-1, keepdims=True)

def self_attention(H, Wq, Wk, Wv):
    Q, K, V = H @ Wq, H @ Wk, H @ Wv            # questions, labels, contents
    weights = softmax(Q @ K.T / np.sqrt(K.shape[1]))
    return weights @ V, weights                  # each word: a weighted mix of the values

rng = np.random.default_rng(0)
H = rng.normal(size=(3, 8))                      # three words, 8 numbers each
out, w = self_attention(H, *(rng.normal(size=(8, 8)) for _ in range(3)))
print(np.round(w, 2))                            # every row sums to 1

# %% [markdown]
# ## The toy task

# %%
from jevkit import attention as at
X, y, notes = at.make_data(4000, 0)
X_test, y_test, _ = at.make_data(1000, 1)
for n, label in list(zip(notes, y))[:5]:
    print(f"{' '.join(n):<40} threat={int(label)}")

# %%
from sklearn.linear_model import LogisticRegression
def bag(M):
    B = np.zeros((len(M), len(at.VOCAB)))
    for i, row in enumerate(M):
        for t in row:
            B[i, t] += 1
    return B[:, 1:]
bow = LogisticRegression(max_iter=2000).fit(bag(X), y)
print(f"bag of words accuracy: {bow.score(bag(X_test), y_test):.1%}")

# %% [markdown]
# ## Train one attention layer (about 20 seconds)

# %%
params = at.train(X, y, steps=4000, lr=0.01, seed=1)
acc = ((at.forward(params, X_test) > 0.5) == y_test).mean()
print(f"attention accuracy: {acc:.1%}")

for words in (["invoice", "not", "phishing"], ["phishing", "not", "invoice"]):
    p, A = at.forward(params, at.encode(words), return_attn=True)
    print(words, "P(threat) =", round(float(p[0]), 3))
    print(np.round(A[0, :3, :3], 2))
