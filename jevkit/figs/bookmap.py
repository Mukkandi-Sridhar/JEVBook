"""The book's structure, in one place. Used by the 'you are here' map and the build tools."""

PARTS = [
    ("I", "Probability, calibration and decisions", [
        (1, "ch01", "What “learning” means"),
        (2, "ch02", "Probability is the language of decisions"),
        (3, "ch03", "Data, loss and gradient descent"),
        (4, "ch04", "Calibration: when 0.8 really means 80%"),
        (5, "ch05", "From probabilities to actions"),
    ]),
    ("II", "Deep learning in plain English", [
        (6, "ch06", "Neurons to networks"),
        (7, "ch07", "Embeddings: meaning as geometry"),
        (8, "ch08", "Attention and transformers, visually"),
        (9, "ch09", "Training at scale, and why big models are overconfident"),
    ]),
    ("III", "LLMs, GenAI and agents", [
        (10, "ch10", "How an LLM writes, one token at a time"),
        (11, "ch11", "Structured outputs and JSON mode"),
        (12, "ch12", "RAG and memory"),
        (13, "ch13", "Agents: Observe, Decide, Act"),
        (14, "ch14", "Where agents break"),
    ]),
    ("IV", "Jev in depth", [
        (15, "ch15", "System 1 and System 2"),
        (16, "ch16", "Inside Jev: what we know and what we don’t"),
        (17, "ch17", "The type system: choice, score, noul"),
        (18, "ch18", "Testing Jev’s calibration yourself"),
        (19, "ch19", "The Jevons paradox of decisions"),
    ]),
    ("V", "The decision layer", [
        (20, "ch20", "The bake-off: six ways to make a decision"),
        (21, "ch21", "Act, review, or escalate"),
        (22, "ch22", "A catalog of decision patterns"),
    ]),
    ("VI", "Building", [
        (23, "ch23", "First calls, and the mock that makes them free"),
        (24, "ch24", "A hybrid agent: Jev decides, the LLM reasons"),
        (25, "ch25", "Case study: SOC alert triage"),
        (26, "ch26", "An applications gallery"),
        (27, "ch27", "Build your own System One model"),
        (28, "ch28", "Capstone: a production decision service"),
    ]),
    ("VII", "The industry shift", [
        (29, "ch29", "What changes now"),
    ]),
]

CHAPTERS = {c[1]: (c[0], c[2], p[0], p[1]) for p in PARTS for c in p[2]}


def part_of(chapter: str) -> str:
    return CHAPTERS[chapter][2]
