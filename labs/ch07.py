# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
# ---

# %% [markdown]
# # Lab 7 · Embeddings: meaning as geometry
#
# *Decide, Don't Generate*, Chapter 7.
#
# 1. Learn word vectors from a synthetic corpus of analyst notes, by counting context.
# 2. Measure similarity with cosine.
# 3. Embed whole alerts and find "alerts like this one".
# 4. Turn neighbours into a probability, and check it.

# %%
import importlib.util, subprocess, sys
if importlib.util.find_spec("jevkit") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "typesafe-sdk==0.7.2",
                    "git+https://github.com/Mukkandi-Sridhar/JEVBook"], check=True)

# %%
import numpy as np
from jevkit import text

notes = text.notes_corpus()
print(len(notes), "notes, e.g.:")
for n in notes[:4]:
    print("  ", " ".join(n))

# %%
vocab, vectors, counts = text.note_vectors()
def cosine(a, b):
    va, vb = vectors[vocab.index(a)], vectors[vocab.index(b)]
    return float(va @ vb / (np.linalg.norm(va) * np.linalg.norm(vb)))

for a, b in [("invoice", "bill"), ("invoice", "trojan"), ("upload", "download"), ("phishing", "spoofed")]:
    print(f"{a:>9} vs {b:<9} {cosine(a, b):+.2f}")
print(text.note_nearest("ransomware"))

# %% [markdown]
# ## Alerts as vectors

# %%
from sklearn.neighbors import NearestNeighbors
from jevkit import soc, calibration as cal

alerts = soc.load()
train, calib, test = soc.split(alerts)
embed = text.alert_embedder(train.description.tolist())
Z_train = embed(train.description.tolist())
Z_test = embed(test.description.tolist())

nn = NearestNeighbors(n_neighbors=5, metric="cosine").fit(Z_train)
dist, idx = nn.kneighbors(Z_test[:1])
print("QUERY:", test.description.iloc[0][:110])
for d, i in zip(dist[0], idx[0]):
    print(f"  sim {1 - d:.2f}  {train.description.iloc[i][:100]}")

# %% [markdown]
# ## Among the 50 most similar past alerts, how many were attacks?

# %%
nn50 = NearestNeighbors(n_neighbors=50, metric="cosine").fit(Z_train)
_, idx = nn50.kneighbors(Z_test)
p_knn = np.clip(train.malicious.to_numpy()[idx].mean(1), 0.005, 0.995)
print(cal.summary(p_knn, test.malicious))
