# Running notes: 15-day Agentic AI course transcript

Notes written while reading every line, in order. Line numbers refer to the transcript file.

## Day 1 (lines 1–2650)

### Lines 1–1300
- Opening: sets purpose, asks learners *why* they joined, promises "after this there is nothing to know".
- Core frame repeated: **problem statement first** ("without this concept, what is the problem?"), then how it works, why it works, then code. "There is never one correct solution": everything is **trade-offs**, like HLD.
- Separates three AI roles: model creation, inference engineering, agentic applications. States what the course is NOT (no internals), which sets scope.
- Builds definitions by contradiction with misconceptions: "OpenAI is not an LLM, it is a model provider; ChatGPT is an application."
- LLM limitations listed one at a time, each with an everyday probe question: knowledge cutoff ("who won IPL 2026?"), stateless (follow-up "when was she born?"), fixed context window, **probabilistic / non-deterministic** (contrast with HTTP API that always returns the same shape), cannot act.
- Agent definition built from two complementary weaknesses: "LLM understands language but cannot act; a tool can act but cannot understand language; together they form an agent." Very strong pairing device.
- Then the evolution of definitions: agent = LLM + tool → LLM + context → model + harness.
- RAG = when the tool fetches information. Unpacks the acronym word by word ("augment is a fancy term for adding").
- Tool-calling flow drawn as numbered steps 1–6 (query → query+tool list → LLM says which tool → app calls tool → tool response → back to LLM → final answer). Redraws when the diagram gets messy ("let me do this once more").
- Answers learner doubts with a counter-question (Jignesh: "Do you want JSON with a 4xx in your chat reply?").
- Semantic meaning example: "why are payment failures happening?" vs code named `CheckoutException`.
- Chunking problem framed with failure scenarios: split mid-class, mid-function, same function name in different classes; then the **user-experience test**: "would you use Claude Code again if it can't answer that?"
- Frequent check-ins ("Is everyone with me?"), names learners, invites doubts, promises to answer later instead of derailing.
- Frameworks: "only the APIs change; the concepts are the same". Decides for the learner what to worry about.
- Capstone: build a Claude-Code-like coding agent; second group project (stock trading app, deep-research agent).

### Lines 1301–2650
- Explains a mechanism twice when asked, the second time more slowly and with a drawn example (recursive splitter: by class, then by function, until every chunk ≤ 256).
- **Run it, see it fail, then fix it.** Demo answers "what does AuthService do?" well, then fails "what functions are in AuthService?". Opens the trace (LangSmith) to show exactly what went to the model, which chunk came back, and why `__init__` was the last thing seen.
- Turns one knob at a time and narrates the trade-off: chunk 256 → 1500 → 2500 (fewer chunks, more tokens, more complete answer). Shows token and cost counts in the trace.
- Surprises become lessons: the 6-times tool loop → retry middleware → "who decides to retry? The LLM, because only it can judge whether the answer is good enough."
- Short definitions while answering questions: tokens vs chunks; embedding dimension trade-off (more meaning, more space); chunk size is a setting, not a standard.
- "Do not memorise code; memorise the concept and the pros and cons." Code and frameworks change.
- Plants hooks for later: "tomorrow I'll show how adding the class name to each function chunk fixes this."
- Q&A section: interview story (a fintech asking "how can I trust you with our data?") answered as 1) redact PII before the LLM, 2) self-hosted open models, 3) compare with trusting any cloud vendor.
- Career advice: interviews care less about Python, more about concepts and trade-offs; "AI cannot replace you yet on judging trade-offs".
- "Same model, different application, different results": the application's chunking, context, prompt and harness make the difference.

### Who is teaching
- Learners address the instructor as "Kirti"/"Keerti" (Keerti Purswani), with teaching assistant Amit. The instructor's own example: "Who is Keerti Purswani... what is her company's name?". Course states the material is for paid students only and asks that it not be shared outside.
