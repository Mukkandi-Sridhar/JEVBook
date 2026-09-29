# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
# ---

# %% [markdown]
# # Lab 12 · RAG and memory
#
# *Decide, Don't Generate*, Chapter 12. Kestrel's knowledge base is synthetic.
#
# 1. Chunk a small knowledge base and retrieve passages for a question.
# 2. Measure retrieval: does the answer land in the top k?
# 3. Decide when to say "I don't know".

# %%
import importlib.util, subprocess, sys
if importlib.util.find_spec("jevkit") is None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "typesafe-sdk==0.7.2", "autograd",
                    "git+https://github.com/Mukkandi-Sridhar/JEVBook"], check=True)

# %%
import numpy as np
from jevkit import kb

chunks = kb.corpus(size_words=30)          # policies + runbooks, plus 300 old alerts as distractors
texts = [t for _, t in chunks]
retriever = kb.Retriever(texts, mode="char")
for score, text in retriever.search("Is svc-backup supposed to upload data at night?", k=3):
    print(f"{score:.2f}  {text[:90]}")

# %% [markdown]
# ## Building the prompt

# %%
question = "A user clicked a phishing link. What are the first steps?"
hits = retriever.search(question, k=3)
prompt = "Answer using ONLY the passages below. If they don't contain the answer, say you don't know.\n\n"
prompt += "\n".join(f"[{i + 1}] {t}" for i, (_, t) in enumerate(hits))
prompt += f"\n\nQuestion: {question}"
print(prompt)

# %% [markdown]
# ## How good is retrieval?

# %%
def recall_at_k(mode, k):
    r = kb.Retriever(texts, mode)
    S = r.scores([q for _, q in kb.QUESTIONS])
    hits = [any(kb.ANSWER_KEY[q] in texts[j] for j in np.argsort(-S[i])[:k])
            for i, (_, q) in enumerate(kb.QUESTIONS)]
    return np.mean(hits)

for mode in ("word", "char", "hybrid"):
    print(mode, [round(recall_at_k(mode, k), 2) for k in (1, 3, 5)])

# %% [markdown]
# ## When to say "I don't know"

# %%
best_answerable = retriever.scores([q for _, q in kb.QUESTIONS]).max(1)
best_unanswerable = retriever.scores(kb.UNANSWERABLE).max(1)
for t in (0.2, 0.25, 0.3, 0.35):
    print(f"threshold {t}: answers {np.mean(best_answerable >= t):.0%} of answerable, "
          f"{np.mean(best_unanswerable >= t):.0%} of unanswerable")
