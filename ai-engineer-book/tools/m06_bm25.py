"""Real BM25 scores for Module 6's worked example (rank_bm25 BM25Okapi, Porter stemming)."""
import json, re
from pathlib import Path
from nltk.stem import PorterStemmer
from rank_bm25 import BM25Okapi

DOCS = {
 "P1": "Returns: Most products can be returned within 10 days of delivery if unused and in original packaging.",
 "P2": "Hygiene policy: In-ear audio devices, innerwear and cosmetics cannot be returned once the seal is opened, unless they arrive faulty.",
 "P3": "Earbuds buying guide: Our earbuds come with three sizes of ear tips and a charging case. Battery lasts up to 30 hours.",
 "P4": "FAQ: Can I return unopened earbuds? Yes. Unopened earbuds can be returned within 10 days.",
 "P5": "Faulty items: If a product arrives damaged or faulty, report it within 48 hours for a free replacement or refund.",
 "P6": "Refunds reach the original payment method within 5 to 7 working days after the returned item is checked.",
 "P7": "Phones can be returned within 7 days only for manufacturing defects confirmed by our service partner.",
 "P8": "Product AX-7781 (wireless earbuds, black): return window extended to 30 days during the festival sale.",
}
ps = PorterStemmer()
STOP = {"can", "i", "the", "a", "of", "and", "or", "to", "is", "it", "if", "in", "for", "our", "by", "with", "be", "up", "are", "on", "once"}

def toks(t):
    return [ps.stem(w) for w in re.findall(r"[a-z0-9\-]+", t.lower()) if w not in STOP]

ids = list(DOCS)
corpus = [toks(DOCS[i]) for i in ids]
bm = BM25Okapi(corpus)
out = {}
for q in ["can I return opened earbuds", "can I send back earphones I already used", "return policy for AX-7781"]:
    qs = toks(q)
    sc = bm.get_scores(qs)
    out[q] = {"query_tokens": qs, "scores": {i: round(float(s), 2) for i, s in sorted(zip(ids, sc), key=lambda x: -x[1])}}
index = {}
for i, c in zip(ids, corpus):
    for w in set(c):
        index.setdefault(w, []).append(i)
out["index_sample"] = {w: index.get(w, []) for w in ["return", "earbud", "open", "unopen", "ax-7781", "faulti"]}
out["idf"] = {w: round(float(bm.idf.get(w, 0)), 2) for w in ["return", "earbud", "open", "ax-7781"]}
out["doc_len"] = {i: len(c) for i, c in zip(ids, corpus)}
Path(__file__).resolve().parents[1].joinpath("research/m06-bm25.json").write_text(json.dumps({"docs": DOCS, **out}, indent=1))
print(json.dumps(out, indent=1))
