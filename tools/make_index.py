"""Generate back/index-terms.qmd: every glossary term, plus names, with the chapters that use it.

A print index would give page numbers; this one gives chapters, which survive every re-render.
Run after editing chapters or the glossary: python tools/make_index.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXTRA = {
    "Jev": r"\bJev\b", "TypeSafe AI": r"\bTypeSafe\b", "typesafe-sdk": r"typesafe-sdk|TypeSafeClient",
    "Kestrel Logistics": r"\bKestrel\b", "jevkit": r"\bjevkit\b", "Kahneman, Daniel": r"\bKahneman\b",
    "Jevons, William Stanley": r"\bJevons\b", "Doom demo": r"\bDoom\b", "Jev-Mem": r"Jev-Mem",
    "Harbor Pharma": r"\bHarbor\b", "TinyJev": r"\bTinyJev\b", "phishing campaign": r"\bcampaign\b",
    "SOC (security operations centre)": r"\bSOC\b", "threat intel": r"threat intel", "ReAct": r"\bReAct\b",
    "reasoning models": r"reasoning model", "bake-off": r"bake-off", "Bayes' rule": r"\bBayes\b",
}
# glossary term -> regex, when the term's name alone won't match the text
ALIASES = {
    "Act, review, escalate": r"act, review,? (?:and|or) escalate|three zones?|three-zone",
    "ECE (expected calibration error)": r"\bECE\b|calibration error",
    "LLM (large language model)": r"\bLLMs?\b",
    "RAG (retrieval-augmented generation)": r"\bRAG\b",
    "System 1, System 2": r"System 1\b|System 2\b",
    "Temperature (calibration)": r"temperature scaling|fitted temperature|one temperature",
    "Temperature (sampling)": r"temperature 0|temperature of 0|temperature \d",
    "Audit (random)": r"random audit|audit (?:a|the) (?:random|sample)|audited",
    "Observe, Decide, Act": r"Observe, Decide|Observe → Decide|observe, decide",
    "Extract, then decide": r"extract, then decide|extracts, Jev decides|Extract, then decide",
    "Overfitting": r"overfit",
    "Overconfidence": r"overconfiden",
    "Fine-tuning": r"fine-tun",
    "Hallucination": r"hallucinat",
    "Label": r"\blabels?\b",
    "Mock": r"\bmock\b",
    "Loss": r"\bloss\b",
    "Embedding": r"embedding",
    "Agent": r"\bagents?\b",
    "Noul": r"\bnouls?\b",
    "Choice": r"`choice`|Choice\(|a choice (?:over|with|head|question)|choice head|choice question",
    "Score": r"`score`|\bScore\b|score question",
    "Router": r"\brout(er|ing|e)\b",
    "Trace": r"\btrace\b",
    "State": r"\bstate\b",
    "Policy": r"\bpolicy\b",
    "Drift": r"\bdrift",
    "Capacity": r"\bcapacity\b",
    "Token": r"\btokens?\b",
    "Transformer": r"transformer",
    "Structured output": r"structured output",
    "JSON mode": r"JSON mode",
    "Prompt injection": r"injection",
    "Prior shift": r"prior shift|prior-shift|base-rate correction",
    "Cost line": r"cost line|draw(?:ing|n)? (?:the )?lines?|where the line goes|the line at|\bthe line\b",
    "Typed question": r"typed question",
    "Decision record": r"decision record|DecisionRecord",
    "Shadow mode": r"\bshadow",
    "Cassette": r"cassette",
    "Transport": r"transport",
    "Vendor-reported": r"vendor-reported",
    "Elasticity": r"elastic",
    "Confidence": r"`confidence`|stated confidence|verbali[sz]ed confidence",
    "Attention": r"self-attention|attention (?:layer|head|weight|map|pattern)|Attention Is All",
    "Escape option": r"\"other\"|\"none\"|not enough information|escape",
}


def chapters():
    out = []
    for q in sorted((ROOT / "chapters").glob("ch*.qmd")):
        text = q.read_text()
        text = re.sub(r"```.*?```", " ", text, flags=re.S)          # prose only, not code
        out.append((int(q.stem[2:]), text))
    return out


def glossary_terms():
    lines = (ROOT / "back" / "glossary.qmd").read_text().splitlines()
    return [lines[i].strip() for i in range(len(lines) - 1)
            if lines[i + 1].startswith(": ") and lines[i].strip()]


def fmt(chs):
    if not chs:
        return None
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
    chs = chapters()
    entries = {}
    for t in glossary_terms():
        pat = ALIASES.get(t, re.escape(t.split(" (")[0]))
        entries[t] = pat
    entries.update(EXTRA)
    rows = []
    for term, pat in entries.items():
        rx = re.compile(pat, re.I if term not in EXTRA else 0)
        hits = [n for n, text in chs if rx.search(text)]
        f = fmt(hits)
        if f:
            rows.append((term.lower(), term, f))
    rows.sort()
    out = ["# Index of terms {.unnumbered}", "",
           "Chapters where each term appears. The glossary gives a one-sentence definition of most of them.", "",
           "::: {.indexlist}"]
    letter = None
    for key, term, f in rows:
        if key[0].upper() != letter:
            letter = key[0].upper()
            out += ["", f"**{letter}**", ""]
        out.append(f"{term} · {f}\\")
    out += ["", ":::", ""]
    (ROOT / "back" / "index-terms.qmd").write_text("\n".join(out))
    print(f"{len(rows)} entries")


if __name__ == "__main__":
    main()
