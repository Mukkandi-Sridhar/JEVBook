"""Build the book's index: python tools/make_index.py

Writes two things:

- back/index-terms.json: the terms the print edition indexes by page. The Lua filter (filters/book.lua) reads it and
  adds a LaTeX \\index entry where each term is defined in bold, and, for specific terms, at its first mention in
  each chapter. makeindex then turns those into page numbers.
- back/index-terms.qmd: the index page. In print it's the page index; on the web, where pages don't exist, it lists
  the chapters that use each term.

Run after editing chapters or the glossary.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# display name -> (plain lowercase patterns, strict)
#   a pattern ending in "*" matches as a prefix ("overfit*" matches "overfitting");
#   a pattern with capitals matches case-sensitively ("ReAct" isn't "react");
#   strict terms are ordinary words ("label", "state"), so only their bold definitions are indexed.
TERMS = {
    "Act, review, escalate": (["act, review", "three doors", "three zones"], False),
    "Agent": (["agent", "agents"], True),
    "Attention": (["attention"], False),
    "Audit (random)": (["random audit*", "audit"], True),
    "AUC": (["auc"], False),
    "Base rate": (["base rate*", "base-rate"], False),
    "Brier score": (["brier"], False),
    "Calibration": (["calibrat*"], True),
    "Capacity": (["capacity"], True),
    "Cassette": (["cassette*"], False),
    "Choice (question type)": (["choice"], True),
    "Confidence": (["confidence"], True),
    "Context window": (["context window*"], False),
    "Cost line": (["cost line*", "cost-based line", "cost-based threshold"], False),
    "Decision layer": (["decision layer*"], False),
    "Decision record": (["decision record*"], False),
    "Drift": (["drift*"], True),
    "ECE (expected calibration error)": (["ece", "expected calibration error"], False),
    "Elasticity": (["elastic*"], False),
    "Embedding": (["embedding*"], False),
    "Escape option": (["escape option*", "\"other\"", "not enough information"], True),
    "Extract, then decide": (["extract, then decide", "extracts, jev decides"], False),
    "Fail-safe": (["fail-safe*"], False),
    "Fine-tuning": (["fine-tun*"], False),
    "Gradient descent": (["gradient descent"], False),
    "Guardrail gate": (["guardrail*"], False),
    "Hallucination": (["hallucinat*"], False),
    "Hybrid agent": (["hybrid agent*", "hybrid"], True),
    "Isotonic regression": (["isotonic"], False),
    "Jevons paradox": (["jevons paradox"], False),
    "JSON mode": (["json mode", "constrained decoding"], False),
    "Label": (["label", "labels"], True),
    "LLM (large language model)": (["large language model*"], True),
    "LLM-as-judge": (["llm-as-judge", "llm-as-a-judge"], False),
    "Log loss": (["log loss"], False),
    "Logistic regression": (["logistic regression"], False),
    "Loss": (["loss"], True),
    "Mock": (["mock"], True),
    "Noul": (["noul", "nouls"], False),
    "Observe, Decide, Act": (["observe, decide", "ooda"], False),
    "Ordinal": (["ordinal"], False),
    "Overconfidence": (["overconfiden*"], False),
    "Overfitting": (["overfit*"], False),
    "Platt scaling": (["platt scaling"], False),
    "Policy": (["policy"], True),
    "Prior shift": (["prior shift", "prior-shift"], False),
    "Prompt injection": (["prompt injection"], False),
    "Proper scoring rule": (["proper scoring rule*"], False),
    "RAG (retrieval-augmented generation)": (["rag", "retrieval-augmented"], False),
    "Reliability diagram": (["reliability diagram*"], False),
    "RLCD": (["rlcd"], False),
    "RLHF": (["rlhf"], False),
    "Router": (["router*", "routing"], True),
    "Score (question type)": (["score"], True),
    "Shadow mode": (["shadow"], False),
    "Softmax": (["softmax"], False),
    "State": (["state"], True),
    "Structured output": (["structured output*"], False),
    "System 1, System 2": (["system 1", "system 2"], False),
    "System One model": (["system one model*"], False),
    "Temperature (calibration)": (["temperature scaling", "fitted temperature"], False),
    "Temperature (sampling)": (["temperature 0", "temperature 0.7", "temperature of"], False),
    "Three-zone policy": (["three-zone"], False),
    "Token": (["token", "tokens"], True),
    "Trace": (["trace", "traces"], True),
    "Transformer": (["transformer*"], False),
    "Transport": (["transport"], True),
    "Typed question": (["typed question*"], False),
    "Vendor-reported": (["vendor-reported"], True),
    # names and things that aren't in the glossary
    "Bake-off": (["bake-off"], False),
    "Bayes' rule": (["bayes"], False),
    "Doom demo": (["doom"], False),
    "Harbor Pharma": (["harbor"], False),
    "Jev-Mem": (["jev-mem"], False),
    "Jevons, William Stanley": (["jevons"], False),
    "jevkit": (["jevkit"], False),
    "Kahneman, Daniel": (["kahneman"], False),
    "Molas, Alex": (["molas"], False),
    "Murphy, Allan": (["murphy"], False),
    "Phishing campaign": (["campaign"], False),
    "Reasoning models": (["reasoning model*"], False),
    "ReAct": (["ReAct"], False),
    "Threat intel": (["threat intel*"], False),
    "TinyJev": (["tinyjev"], False),
    "TypeSafe AI": (["typesafe"], False),
    "typesafe-sdk": (["typesafe-sdk", "typesafeclient"], False),
}
CODE = {"jevkit", "typesafe-sdk"}          # shown in code type; sorted as words


def chapters():
    out = []
    for q in sorted((ROOT / "chapters").glob("ch*.qmd")):
        text = re.sub(r"```.*?```", " ", q.read_text(), flags=re.S)      # prose only, not code
        out.append((int(q.stem[2:]), text))
    return out


def regex(patterns):
    parts = []
    for p in patterns:
        body = r"(?<!\w)" + (re.escape(p[:-1]) if p.endswith("*") else re.escape(p) + r"(?!\w)")
        parts.append(body if p != p.lower() else "(?i:" + body + ")")
    return re.compile("|".join(parts))


def fmt(chs):
    runs, start, prev = [], chs[0], chs[0]
    for c in chs[1:] + [None]:
        if c is not None and c == prev + 1:
            prev = c
            continue
        runs.append(f"{start}" if start == prev else (f"{start}, {prev}" if prev == start + 1 else f"{start}–{prev}"))
        if c is not None:
            start = prev = c
    return ", ".join(runs)


def main():
    spec = [dict(display=t, sort=t.lower().replace("'", ""), patterns=p, strict=s, code=t in CODE)
            for t, (p, s) in TERMS.items()]
    (ROOT / "back" / "index-terms.json").write_text(json.dumps(dict(terms=spec), indent=1) + "\n")

    chs = chapters()
    rows = []
    for t, (p, _) in TERMS.items():
        hits = [n for n, text in chs if regex(p).search(text)]
        if hits:
            rows.append((t.lower().replace("'", ""), t, fmt(hits)))
    rows.sort()
    out = ["# Index {.unnumbered}", "",
           "::: {.content-visible when-format=\"pdf\"}", "```{=latex}", "\\printindex", "```", ":::", "",
           "::: {.content-visible unless-format=\"pdf\"}",
           "Chapters where each term appears. The glossary gives a one-sentence definition of most of them.", "",
           "::: {.indexlist}"]
    letter = None
    for key, term, f in rows:
        if key[0].upper() != letter:
            letter = key[0].upper()
            out += ["", f"**{letter}**", ""]
        shown = f"`{term}`" if term in CODE else term
        out.append(f"{shown} · {f}\\")
    out += ["", ":::", ":::", ""]
    (ROOT / "back" / "index-terms.qmd").write_text("\n".join(out))
    print(f"{len(spec)} terms, {len(rows)} in the web index")


if __name__ == "__main__":
    main()
