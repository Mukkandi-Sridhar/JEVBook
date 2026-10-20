# Prompt engineering, context engineering, structured outputs, tool calling, embeddings, vector databases and RAG (state as of October 2026)

Research date: 2026-10-20. Method: web search plus fetches of primary pages where reachable. Some primary domains (research.trychroma.com, developers.openai.com, jxnl.co) failed DNS resolution in this environment, so several claims rely on search-result summaries of those pages. These are flagged. Items marked "canonical paper, not re-fetched" are well-known arXiv papers cited by their stable arXiv URL from background knowledge. They were not re-read in this session.

---

## Q1. What is the current consensus on prompt and context engineering, and what changed with reasoning models in 2025-2026?

### Takeaway
By late 2026, "prompt engineering" has been absorbed into **context engineering**: choosing the smallest set of high-signal tokens (instructions, tools, examples, retrieved data, history, memory) for each model call. Context is treated as a finite "attention budget" that degrades as it fills ("context rot"). With reasoning models (OpenAI o-series to GPT-5.x, Claude 4.x with extended thinking, Gemini 2.5+), the advice moved away from hand-written chain-of-thought and step-by-step scripts. The newer advice is to state the outcome, the constraints and the success criteria, tune a reasoning-effort parameter, move output schemas into structured-output APIs, and keep prompts lean.

### Cited Findings

**Context engineering as the framing (Anthropic, 29 Sep 2025)**
- Anthropic's Applied AI team published "Effective context engineering for AI agents" on **29 September 2025**, around the Claude Sonnet 4.5 launch. It defines context engineering as "curating and maintaining the optimal set of tokens during inference", including messages, tools, external data and history. It presents this as the natural next step after prompt engineering, organised around the question "what configuration of context is most likely to generate our model's desired behavior?" — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Core principle: "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome". Context is an "attention budget" with diminishing returns. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- System prompts should be at the "right altitude": "the Goldilocks zone" between brittle hard-coded if-else logic and vague high-level guidance. Organise sections with XML tags or Markdown headers. Start with a minimal prompt on the best model, then add instructions and examples only to fix observed failures. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Few-shot: keep using examples, but curate a small set of "diverse, canonical" examples rather than stuffing in every edge case ("examples are the 'pictures' worth a thousand words"). — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Tools: tools should be self-contained, robust to errors, clearly scoped and token-efficient in what they return. A bloated tool set with overlapping functions is a common failure: "If a human engineer can't definitively say which tool should be used… an AI agent can't be expected to do better." — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **Just-in-time retrieval.** Agents hold lightweight identifiers (file paths, stored queries, links) and load data through tools at runtime, using metadata such as folder names and timestamps for progressive disclosure. Claude Code is the hybrid example: CLAUDE.md is loaded up front, and glob and grep fetch files just in time. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **Long-horizon techniques:**
  - *Compaction.* Summarise the conversation near the limit and restart with the summary. Claude Code keeps architectural decisions, unresolved bugs and the 5 most recently accessed files. Tune the summary for recall first, then for precision.
  - *Tool-result clearing.* The "lightest touch" form of compaction, shipped as a Claude Developer Platform feature.
  - *Structured note-taking / agentic memory.* Examples are NOTES.md and to-do lists. The memory tool entered public beta with Sonnet 4.5.
  - *Sub-agents.* These work in clean context windows and return condensed summaries of about 1,000-2,000 tokens.

  Use compaction for long back-and-forth, notes for milestone-based work, and multi-agent setups for parallel research. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Trade press read the post as "prompting isn't the main game anymore". — [The Neuron](https://www.theneuron.ai/explainer-articles/anthropic-just-changed-the-rules-for-working-with-ai-and-prompting-isnt-the-main-game-anymore); [eWeek](https://www.eweek.com/news/anthropic-context-engineering-building-ai-workflows/)

**Context rot (Chroma, July 2025)**
- Chroma's "Context Rot" technical report (July 2025) tested **18 frontier models**, including GPT-4.1, Claude 4, Gemini 2.5 and Qwen3. Every model got worse as input length grew, even on trivial retrieve-and-repeat tasks. Degradation starts well before the window is full (for example, noticeable at about 50K on a 200K-window model). — summarised by [Morph](https://www.morphllm.com/context-rot), [Cobus Greyling](https://cobusgreyling.substack.com/p/llm-context-rot), [DAIR.AI](https://academy.dair.ai/papers/context-rot). The primary report at research.trychroma.com/context-rot was unreachable from this environment.
- Reported findings from those summaries:
  - Lower question-to-needle similarity makes degradation worse.
  - Even a single similar-but-wrong distractor hurts.
  - Counter-intuitively, models did *worse* when the haystack was coherent text than when it was shuffled.
  - Position effects echo "lost in the middle".

  — [Morph](https://www.morphllm.com/context-rot); [PromptLayer](https://blog.promptlayer.com/why-llms-get-distracted-and-how-to-write-shorter-prompts/)
- Secondary sources disagree on refusals. One says Claude models tend to abstain when confused. Another quotes only 69 refusals in 194,480 calls (0.035%). Neither could be verified against the primary report. — [Morph](https://www.morphllm.com/context-rot); [Lyzr](https://lyzr.ai/blog/context-rot/)
- Background (older): "Lost in the Middle" (Liu et al., July 2023) showed U-shaped accuracy against the position of relevant information. — [arXiv 2307.03172](https://arxiv.org/abs/2307.03172) (canonical paper, not re-fetched)

**Reasoning models: what changed**
- OpenAI's current guidance (the GPT-5.5 model guide, which supersedes the original GPT-5 guide) says to describe the desired outcome and success criteria rather than prescribe step-by-step process, unless the exact path matters. It also says to move output schemas out of the prompt into Structured Outputs to keep prompts lean. — [OpenAI: Using GPT-5.5](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.5.md) (summarised via search; direct fetch failed)
- OpenAI recommends the **Responses API** for multi-turn and tool-calling work with reasoning models, because it carries reasoning items between calls. Start at `medium` reasoning effort and test other levels against representative tasks. — [OpenAI: Using GPT-5](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.md); [OpenAI: Using GPT-5.5](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.5.md)
- GPT-5 (August 2025) added "custom tools" that take freeform text input, optionally constrained by a **context-free grammar** (for example SQL or shell DSLs). — [OpenAI: Using GPT-5](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.md); secondary examples at [Viblo](https://viblo.asia/p/how-to-use-gpt-5s-new-parameters-and-tools-a-practical-guide-kNLr3dYEVgA)
- Classic techniques, dated for context:
  - Chain-of-thought prompting (Wei et al., Jan 2022). — [arXiv 2201.11903](https://arxiv.org/abs/2201.11903)
  - Self-consistency, which samples several reasoning paths and takes a majority vote (Wang et al., Mar 2022). — [arXiv 2203.11171](https://arxiv.org/abs/2203.11171)

  Both are canonical papers, not re-fetched. With reasoning models the CoT happens inside the model's thinking tokens, so explicit "think step by step" is mostly redundant. Self-consistency survives as "best-of-n plus a verifier or judge" at the application layer. (See Inferences.)

**Prompt caching (now a core design constraint)**
- Anthropic (explicit `cache_control` breakpoints): cache writes cost about 1.25x base input for the 5-minute TTL and 2x for the 1-hour TTL. Reads cost 0.1x. The TTL refreshes on each hit. — [IntuitionLabs PDF](https://intuitionlabs.ai/pdfs/llm-prompt-caching-cost-savings.pdf); [Portkey docs](https://portkey.ai/docs/aigw/integrations/llms/anthropic/prompt-caching); [Memx](https://memx.app/blog/prompt-caching-explained-three-providers/)
- OpenAI: caching is automatic for prompts of 1,024 tokens or more. Sources disagree on the discount: 50% on older models, up to 90% on newer ones. One source claims the GPT-5.6 generation moved to an Anthropic-style 1.25x-write / 0.1x-read structure. — [IntuitionLabs PDF](https://intuitionlabs.ai/pdfs/llm-prompt-caching-cost-savings.pdf). This is unverified against OpenAI's pricing page; it conflicts with older docs-mirror figures.
- Gemini: implicit caching is on by default, with explicit caching (plus per-token-hour storage fees) for guaranteed hits. Discounts are reported as 75% (2.0) and 90% (2.5+), but sources conflict. — [IntuitionLabs PDF](https://intuitionlabs.ai/pdfs/llm-prompt-caching-cost-savings.pdf); [DataLLMLab](https://www.datallmlab.com/blog/prompt-caching.html)
- Universal rule: caches match on byte-identical *prefixes*, so put static content (system prompt, tools, documents) first and variable content last. One 2026 practitioner reports real hit rates well below the rates they had modelled. — [Memx](https://memx.app/blog/prompt-caching-explained-three-providers/); [TKMX blog](https://www.tkmxai.it.com/why-prompt-caching-pricing-forced-us-to-rewrite-our-llm-cost-model-in-2026)

**Structured outputs and tool calling**
- Anthropic offers two complementary features:
  - **JSON outputs** via `output_config.format`, which shape the final response.
  - **Strict tool use** via `strict: true` on a tool, which guarantees tool names and inputs match the schema.

  Both use **constrained decoding**. They are GA on the Claude API for Opus 4.8, Mythos Preview, Opus 4.7/4.6/4.5, Sonnet 4.6/4.5 and Haiku 4.5. — [Claude docs: Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- Anthropic's feature started as a public beta behind the header `structured-outputs-2025-11-13`, so it dates from **November 2025**, on Sonnet 4.5 and Opus 4.1. — [Claude docs (older version)](https://docs.claude.com/en/docs/build-with-claude/structured-outputs). On Vertex AI it is off by default under an org policy. — [Google Cloud Vertex docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude/structured_outputs)
- Strict mode compiles the JSON schema into a grammar that constrains sampling. It supports a *subset* of JSON Schema: objects, required fields, enum/const and basic types. — [Level Up Coding](https://levelup.gitconnected.com/claude-api-structured-outputs-schemas-not-hope-952284782089); [Classmethod](https://dev.classmethod.jp/en/articles/claude-api-structured-outputs/)
- OpenAI's guidance: put schemas in Structured Outputs rather than in prose instructions. — [OpenAI: Using GPT-5.5](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.5.md)
- Open-source serving (vLLM) supports structured outputs combined with reasoning, meaning reasoning tokens are free-form and the final answer is constrained. — [vLLM docs](https://docs.vllm.ai/en/v0.9.1/examples/online_serving/openai_chat_completion_structured_outputs_with_reasoning.html)

### Inferences
- The book should present a layered model. Prompt (instructions at the right altitude) sits inside context (tools, examples, retrieved data, history, memory), and that context is managed over time through compaction, tool-result clearing, notes and sub-agents.
- For reasoning models, practical changes from 2023-24 habits:
  - Drop "think step by step".
  - Specify goals, constraints and acceptance criteria.
  - Use the effort knob instead of prompt tricks.
  - Keep the reasoning state across turns (Responses API reasoning items, Anthropic thinking blocks).
  - Use structured outputs instead of "respond only in JSON" prose.
- Prompt caching changes prompt design. Stable prefix ordering, avoiding timestamps or user IDs early in the prompt, and keeping tool definitions stable all have direct cost and latency consequences. Teams should monitor cache hit rate as a KPI.
- Self-consistency in 2026 is best taught as "sample N, verify or vote" for high-stakes outputs, not as a default.

### Gaps
- Could not fetch Google's Gemini prompting or context-engineering guide, or Google's "thinking budget" guidance, in this session.
- Could not verify OpenAI's exact current caching discount for the GPT-5.5/5.6 generation from a primary source.
- Could not read Chroma's primary report directly (DNS failure). Figures come from secondaries.
- No primary-source date found for OpenAI's GPT-5.5 release in this session.
- Cross-provider tool-calling conventions (OpenAI `tools`/`function_call` items in Responses, Anthropic `tool_use`/`tool_result` blocks, Gemini `functionDeclarations`, MCP as the cross-vendor tool protocol) were not re-verified here. They are presumably covered by an adjacent researcher on agents/MCP.

---

## Q2. Which RAG patterns actually work in production, and which hyped ones disappoint?

### Takeaway
The reliable 2026 production stack is unexciting:
- good parsing and chunking;
- **hybrid retrieval** (BM25 plus dense vectors, fused with Reciprocal Rank Fusion);
- metadata filtering;
- a **cross-encoder or LLM reranker** over the top 20-50 candidates;
- optional query rewriting;
- **contextual chunk enrichment** (Anthropic's Contextual Retrieval);
- evaluation-driven iteration.

For agents, especially coding agents, **agentic search** (the model calling grep/glob/search tools in a loop) has displaced one-shot vector RAG as the default, with embeddings demoted to one tool among several. Full GraphRAG is expensive and wins mainly on global or multi-hop "sensemaking" queries. Cheaper variants (LazyGraphRAG) reduce its cost. Long context replaces RAG only for small corpora.

### Cited Findings

**Hybrid search and reranking**
- Hybrid BM25 plus dense retrieval, merged with RRF, is the common default. Dense search handles paraphrase, and sparse search catches exact terms, product codes and rare names. — [Atlan 2026](https://atlan.com/know/advanced-rag-techniques/); [BuildMVPFast 2026](https://www.buildmvpfast.com/blog/hybrid-search-rag-vector-keyword-reranking-2026)
- RRF is preferred because it needs no score calibration across retrievers (BM25 and cosine scores have different ranges). A suggested starting point is RRF with k=60, adding a cross-encoder where latency allows. — [SemEval-2026 Task 8 paper, arXiv 2606.28352](https://arxiv.org/pdf/2606.28352); [Digital Applied 2026](https://www.digitalapplied.com/blog/hybrid-search-bm25-vector-reranking-reference-2026)
- Typical settings: retrieve the top 20-50 and rerank to the top 5-10 for the LLM. Static fusion weights are a weak default. Shift weight toward keyword matching when a query contains identifiers or code. — [BuildMVPFast](https://www.buildmvpfast.com/blog/hybrid-search-rag-vector-keyword-reranking-2026)
- Reranking is not a guaranteed win. The ARAGOG benchmark reportedly found Cohere Rerank gave no notable advantage over naive RAG on its dataset, so benchmark on your own corpus. — reported via [arXiv 2407.13193 survey](https://arxiv.org/pdf/2407.13193) and search summary
- Databricks-style advice cited in a survey: build the evaluation framework first, then add hybrid search, metadata filtering and reranking as progressively more expensive steps. — [arXiv 2407.13193](https://arxiv.org/pdf/2407.13193)
- An older empirical study (July 2024): the best configuration combined query classification, hybrid retrieval with HyDE and monoT5 reranking, but it was computationally expensive. — [Wang et al., "Searching for Best Practices in RAG", arXiv 2407.01219](https://arxiv.org/pdf/2407.01219)
- Query rewriting plus hybrid retrieval for multi-turn conversational RAG was the approach of a 2026 shared-task system. — [arXiv 2606.28352](https://arxiv.org/pdf/2606.28352)

**Contextual Retrieval (Anthropic, Sept 2024)**
- Anthropic prepends a 50-100-token, chunk-specific explanatory context (generated by an LLM from the whole document) to each chunk before embedding *and* before BM25 indexing. Results:
  - contextual embeddings plus contextual BM25 cut failed retrievals (top-20) by **49%**;
  - adding reranking brought the cut to **67%**.

  Prompt caching makes the per-chunk generation cheap. — [Anthropic: Contextual Retrieval](https://anthropic.com/news/contextual-retrieval); [Maginative](https://www.maginative.com/article/anthropics-contextual-retrieval-technique-enhances-rag-accuracy-by-67)
- Third-party breakdown of failure rates: 5.7% baseline, 3.7% with contextual embeddings (-35%), 2.9% adding BM25, 1.9% adding reranking. — [Gradient Flow](https://gradientflow.com/contextual-retrieval-rag/), via search summary; verify against the primary source
- Same post: if the knowledge base is under about 200K tokens, skip RAG and put the whole thing in the prompt, using caching. — [Anthropic: Contextual Retrieval](https://anthropic.com/news/contextual-retrieval)

**GraphRAG and knowledge graphs**
- Microsoft's **LazyGraphRAG** (Nov 2024) defers LLM summarisation to query time. Its indexing cost is identical to vector RAG and 0.1% of full GraphRAG. Its quality on global queries is comparable to GraphRAG Global Search at more than 700x lower query cost, and it beats vector RAG on local queries at comparable cost. — [Microsoft Research blog](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)
- Practitioner cost estimates for full GraphRAG: LLM entity extraction is about 58% of indexing tokens, at roughly $50-200 for a 500-page corpus versus under $5 for vector RAG. LazyGraphRAG adds 2-8 s of query latency. Lazy suits fast-changing corpora, and precomputed summaries suit stable, read-heavy corpora. The source states that GraphRAG does *not* win everywhere. — [Tian Pan, Apr 2026](https://tianpan.co/blog/2026-04-09-graphrag-production-when-vector-search-hits-ceiling)
- A vendor claim of "91% vs 67% multi-hop accuracy" for GraphRAG versus vector search has no traceable primary source. Treat it as unreliable. — [Delos blog](https://delos.so/blog/graphrag-vs-vector-search-enterprise-knowledge-retrieval)

**Agentic RAG and agentic search (2025-2026 shift)**
- Jason Liu (Sep 2025), drawing on Augment's SWE-bench agent: grep plus an agent loop beat embeddings for code retrieval quality and reliability, but struggles with speed, cost and scale. Embeddings still matter for large codebases and non-code content. — [jxnl.co, 11 Sep 2025](https://jxnl.co/writing/2025/09/11/why-grep-beat-embeddings-in-our-swe-bench-agent-lessons-from-augment/) (via search summary; fetch failed)
- Claude Code's retrieval is essentially glob and grep in an agent loop. Boris Cherny reportedly said it outperformed RAG. This is a secondhand quote. — [Morph: Agentic Search](https://www.morphllm.com/agentic-search); [yage.ai, Mar 2026](https://yage.ai/share/why-coding-agents-still-use-grep-en-20260327.html). It is consistent with Anthropic's own description of Claude Code's just-in-time retrieval. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Cursor (as described in Feb 2026) uses a hybrid: a custom embedding model trained on agent search traces gives initial candidates, and grep and file reads follow code paths. — [Morph](https://www.morphllm.com/agentic-search)
- Doug Turnbull, "Is grep all you need for RAG?" (6 Apr 2026): agentic search is "having a grep moment". — [softwaredoug.com](https://softwaredoug.com/blog/2026/04/06/agentic-search-is-having-a-grep-moment)
- 2026 research reframes the bottleneck as the *retrieval interface* exposed to agents ("direct corpus interaction", "LLM-driven logical retrieval beyond embeddings"). — [arXiv 2605.05242](https://arxiv.org/pdf/2605.05242); [arXiv 2605.27123](https://arxiv.org/pdf/2605.27123); [arXiv 2606.06880](https://arxiv.org/pdf/2606.06880). Survey: [arXiv 2510.04905](https://arxiv.org/pdf/2510.04905)
- One Medium piece claims Claude Code, Cursor, Windsurf, Cline and Amp "no longer index into a vector DB". This conflicts with the Cursor description above, so treat it as overstated. — [Medium (buzzgrewal)](https://buzzgrewal.medium.com/ai-agents-dont-need-vector-search-anymore-inside-the-agentic-search-stack-replacing-rag-in-2026-58efcabe4f6f)

**Multimodal RAG (vision-first document retrieval)**
- Late-interaction vision retrievers have moved from ColPali through ColQwen2.5 to **ColQwen3** and **ColQwen3.5**. These use a Qwen3-VL or Qwen3.5 backbone with a ColBERT-style head that produces per-token or per-patch embeddings, scored with MaxSim. They are supported in vLLM. — [vLLM ColQwen3 docs](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colqwen3/); [vLLM ColQwen3.5](https://docs.vllm.ai/en/v0.23.0/api/vllm/model_executor/models/colqwen3_5/)
- The vision-first pattern embeds each PDF page as an image. It reportedly beats OCR-then-text on ViDoRe v3, with the biggest gains on charts and tables. Its main cost is storage: about 2,048 patch vectors per page. Pruning (for example "DocPruner", reported at 50% pruning without loss) is unverified. — [Trae AI tutorial](https://learn.traeai.com/t/ai-engineering/phases/19-capstone-projects/04-multimodal-document-qa); [BigData Boutique](https://bigdataboutique.com/blog/multimodal-rag-retrieval-over-images-pdfs-and-text); [Spheron](https://www.spheron.network/blog/colpali-multimodal-document-rag-gpu-cloud/)
- Open multi-vector option: Nomic colnomic-embed-multimodal-7b. Single-vector multimodal options: Voyage voyage-multimodal-3.5 (Jan 2026; adds video frames and Matryoshka dimensions) and Gemini Embedding 2 (natively multimodal, preview). — [BigData Boutique](https://bigdataboutique.com/blog/multimodal-rag-retrieval-over-images-pdfs-and-text); [Ailog 2026](https://app.ailog.fr/en/blog/news/embedding-models-2026)

### Inferences
- Production priority order, roughly by return on investment:
  1. Evals and a labelled query set.
  2. Parsing quality, including tables and PDFs.
  3. Hybrid retrieval with metadata filters.
  4. Reranking.
  5. Contextual chunk enrichment.
  6. Query rewriting and decomposition for conversational or multi-hop queries.
  7. Agentic retrieval loops.
  8. Graphs, only if evals show multi-hop or global-summary failures.
- "Agentic RAG" is now the mainstream form of RAG inside agents. Retrieval becomes tools (search, grep, read file, SQL) that the model calls iteratively. Classic single-shot RAG remains right for latency-sensitive Q&A bots.
- Long context versus RAG: for corpora under about 200K tokens, stuffing plus caching is simplest. Context rot means bigger windows do not remove the need for selection, so retrieval and reranking still pay off for precision even when everything would fit.
- Hyped patterns that commonly disappoint (inferred from the sources above):
  - full GraphRAG on general corpora, because of cost;
  - rerankers without evals, given the ARAGOG result;
  - pure vector search for codes, IDs and jargon;
  - complex chunkers in place of good parsing;
  - "1M-token context replaces RAG".

### Gaps
- No rigorous 2025-26 head-to-head benchmark comparing chunking strategies (fixed, recursive, semantic, late chunking) was retrieved in this session. Chunking guidance here is thin.
- HyDE, RAPTOR, Self-RAG and CRAG were not re-verified for 2026 relevance.
- No independent production post-mortems on GraphRAG abandonment were found.
- Late chunking (Jina, 2024) and its 2025-26 uptake were not researched.

---

## Q3. How do teams choose embedding models and vector stores today?

### Takeaway
Embedding choice in 2026 is driven by your own retrieval evals, not MTEB rank alone. Leaderboard numbers from blogs conflict and MTEB v2 changed the scoring. Leading families:
- Qwen3-Embedding (open weights, 0.6B-8B);
- Gemini Embedding (001, and a multimodal Embedding 2 preview);
- Voyage (3.x / 4);
- OpenAI text-embedding-3;
- Cohere;
- large open models from Microsoft and others.

Matryoshka (truncatable) dimensions are now standard, letting teams trade dimension for cost. For vector stores the consensus heuristic is:
- **pgvector** (plus pgvectorscale) if you are already on Postgres and below a few million to tens of millions of vectors;
- **Pinecone** for zero-ops managed service;
- **Qdrant** (or Weaviate or Milvus) for filter-heavy, self-hosted or large workloads;
- **turbopuffer**-style object-storage engines for cheap, huge, multi-tenant corpora;
- **LanceDB** for embedded and multimodal use.

Several guides stress that embedding model, chunking and reranking matter more than the database.

### Cited Findings

**Embedding models**
- MTEB snapshots from 2026 blogs conflict. Qwen3-Embedding-8B is reported at about 75.1 (MTEB v2, open-weight leader) in one source and 70.6 in a January 2026 ranking in another. Gemini Embedding 001 is reported at 68.32 or ranked 2nd. QZhou-Embedding is listed at 75.97 but marked "unverified". — [Codesota MTEB](https://www.codesota.com/benchmark/mteb); [Ailog leaderboard 2026](https://app.ailog.fr/en/blog/news/embedding-models-leaderboard-2026); [Ailog MTEB 2026](https://app.ailog.fr/en/blog/news/rag-benchmark-mteb-2026); [Presenc](https://presenc.ai/research/best-open-weight-embedding-models-2026)
- Other reported strong models: Microsoft Harrier-OSS-v1-27B (top MTEB Multilingual v2, 0.7427), KaLM-Embedding-Gemma3-12B (72.32), Voyage 4 Large (about 66.8). One table gives voyage-3 at about 74.0, which looks like an outlier against another figure of 63.8. — [Ailog](https://app.ailog.fr/en/blog/news/embedding-models-2026); [AI Prompts Hub](https://aipromptshub.co/blog/embedding-model-leaderboard-2026)
- Technical reports: QZhou-Embedding (Aug 2025) — [arXiv 2508.21632](https://arxiv.org/pdf/2508.21632); LGAI-Embedding (Jun 2025) — [arXiv 2506.07438](https://arxiv.org/pdf/2506.07438)
- Guides recommend judging models on RAG-specific recall on your own data rather than the overall MTEB average, and weighing open (self-host, fine-tune) against API (convenience). — [AI Prompts Hub](https://aipromptshub.co/blog/embedding-model-leaderboard-2026); [Maximem 2026](https://www.maximem.ai/blog/best-embedding-models-2026)
- Matryoshka Representation Learning (Kusupati et al., 2022) lets one embedding be truncated to smaller dimensions with graceful quality loss. — [arXiv 2205.13147](https://arxiv.org/abs/2205.13147) (canonical paper, not re-fetched). 2026 commercial models ship with Matryoshka dimensions, for example voyage-multimodal-3.5. — [BigData Boutique](https://bigdataboutique.com/blog/multimodal-rag-retrieval-over-images-pdfs-and-text)
- Late interaction (ColBERT; Khattab & Zaharia, 2020) stores per-token vectors and scores with MaxSim. It gives higher quality at higher storage cost and now underpins ColPali/ColQwen multimodal retrieval. — [arXiv 2004.12832](https://arxiv.org/abs/2004.12832) (canonical paper, not re-fetched); [vLLM ColQwen3 docs](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colqwen3/)
- Domain-tuned embeddings: Cursor trains a custom embedding model on agent search traces. — [Morph](https://www.morphllm.com/agentic-search)

**Vector databases**
- pgvector: fits most RAG workloads under a few million vectors. It gives SQL filtering, joins and transactional consistency between documents and embeddings. pgvectorscale (Timescale) closed much of the performance gap. One benchmark claims 471 QPS at 99% recall on 50M vectors, "11.4x Qdrant". That is a contested vendor-adjacent figure. — [Encore](https://encore.dev/articles/best-vector-databases); [NisAI](https://nisai.dev/guides/vector-databases-compared-2026/); [Firecrawl](https://www.firecrawl.dev/blog/best-vector-databases)
- Pinecone: the pick when operations is the bottleneck. Serverless p50 is about 40-90 ms for a 1M-vector namespace with filters, slower than a well-provisioned self-hosted Qdrant. — [NisAI](https://nisai.dev/guides/vector-databases-compared-2026/); [Anthraai](https://anthraai.com/insights/vector-database-comparison-2026)
- Qdrant: often called the best open-source option in 2026, strong on filtering. Self-hosting at scale "requires real Kubernetes knowledge". — [Omid Saffari](https://omidsaffari.com/blog/best-vector-database); [Edgewisely](https://www.edgewisely.com/7-best-vector-databases-in-2026-pinecone-qdrant-weaviate-milvus-chroma-turbopuffer-and-pgvector-compared/)
- turbopuffer: vectors live in S3-compatible object storage behind a stateless query layer. Cold queries take about 200-500 ms and warm ones about 20 ms. Minimum pricing is reported as $64 or $16 a month, depending on the source. — [Edgewisely](https://www.edgewisely.com/7-best-vector-databases-in-2026-pinecone-qdrant-weaviate-milvus-chroma-turbopuffer-and-pgvector-compared/); [The AI Rankings](https://theairankings.com/best-vector-databases/)
- Multiple guides: the embedding model, chunking and reranking usually matter more than the database. Benchmark on your own data, filters and latency budget. — [Cognee](https://www.cognee.ai/best-vector-database); [MetaCTO](https://www.metacto.com/blogs/pinecone-alternatives-a-deep-dive-into-the-top-vector-databases-for-ai-apps)

### Inferences
- Default recommendation for a book reader: start with pgvector (or the search features of the database you already run, such as Elasticsearch/OpenSearch hybrid). Move to a dedicated engine only when scale, filter complexity, multi-tenancy or latency demands it.
- Pick the embedding model with a 100-500-query labelled eval on your own corpus, comparing recall@k. Consider Matryoshka truncation (for example 3072 down to 1024 or 512 dimensions) plus int8 or binary quantisation to cut cost, and re-check recall afterwards.
- Native hybrid (BM25 plus dense) support in the store is now a key selection criterion, given that hybrid search is the default.

### Gaps
- Could not access the official Hugging Face MTEB leaderboard. All scores above come from secondary blogs and conflict.
- No verified 2026 pricing for OpenAI, Cohere or Voyage embeddings.
- Weaviate, Milvus/Zilliz and LanceDB specifics (features, 2026 releases) were not individually researched.
- Binary and scalar quantisation recall trade-offs were not sourced.

---

## Q4. How is RAG quality evaluated in practice?

### Takeaway
Practitioners evaluate **retrieval and generation separately**:
- retrieval: recall@k, precision@k, MRR or nDCG against a labelled or synthetic query set;
- generation: faithfulness or groundedness, answer relevance and correctness, using LLM-as-judge frameworks such as RAGAS, calibrated with human spot checks.

The common lesson is that retrieval recall is usually the bottleneck, and a high faithfulness score can hide incomplete or stale retrieval.

### Cited Findings
- RAGAS faithfulness extracts claims from the answer and checks each against the retrieved context. The score is the share of claims that are grounded. — [Sapota](https://www.sapotacorp.vn/blog/rag-evaluation-ragas-faithfulness-relevance); [QA Skills](https://qaskills.sh/blog/ragas-rag-evaluation-guide). Original paper: RAGAS (Es et al., Sep 2023). — [arXiv 2309.15217](https://arxiv.org/abs/2309.15217) (canonical paper, not re-fetched)
- Context recall needs ground-truth or synthesised gold answers. Most other RAGAS metrics are reference-free LLM judgements. — [Medium (Patel)](https://medium.com/@aayushipatel135/evaluating-rag-systems-ragas-faithfulness-relevance-and-recall-metrics-2dc02ae4be36)
- Evaluate retrieval and generation as separate problems. — [Kili Technology](https://kili-technology.com/blog/rag-evaluation-guide-measuring-retrieval-and-generation-as-separate-problems); [Braintrust](https://www.braintrust.dev/articles/rag-evaluation-metrics)
- LLM judges work well on simple factual queries but degrade on multi-hop, numerical and domain logic. Periodic human spot checks are recommended. — [Atlan 2026](https://atlan.com/know/how-to-evaluate-rag-systems-explained/); [Braintrust](https://www.braintrust.dev/articles/rag-evaluation-metrics)
- Metrics can mislead. Faithfulness of 0.95 can still be wrong if the source is stale. Faithfulness of 1.0 with low context recall means the system accurately summarises incomplete information. — [Atlan 2026](https://atlan.com/know/how-to-evaluate-rag-systems-explained/)
- Example of retrieval as the bottleneck: a 2026 local pipeline had context recall of 0.23 (SciFact) and 0.04 (FiQA) against faithfulness of about 0.68-0.71. — [CUBO, arXiv 2602.03731](https://arxiv.org/pdf/2602.03731)
- Framework-level evaluation systems exist for comparing RAG frameworks. — [arXiv 2504.07803](https://arxiv.org/pdf/2504.07803)
- Anthropic's Contextual Retrieval work used "failed retrievals at top-20" (1 − recall@20) as its headline metric. This is a model of a simple, decision-useful retrieval metric. — [Anthropic](https://anthropic.com/news/contextual-retrieval)

### Inferences
- Recommended practice for the book:
  1. Build a golden set of real user queries with labelled relevant chunks. Synthetic generation is fine for bootstrapping.
  2. Track recall@k and MRR or nDCG for retrieval changes, which are cheap and deterministic.
  3. Use LLM-judge faithfulness and correctness for generation, with judges validated against human labels.
  4. Do error analysis on traces, reading failures and categorising them, before adding metrics. This is the Hamel Husain / Eugene Yan school, but it was not directly sourced this session.
- Every pipeline change (chunker, embedder, reranker, k) should be gated by the retrieval eval, given evidence that "improvements" such as rerankers do not always help.

### Gaps
- Searches did not surface primary posts from Hamel Husain, Eugene Yan or Simon Willison on RAG evals. Their positions (error analysis first, binary pass/fail judges, avoiding generic off-the-shelf metrics) are not cited here and need sourcing.
- No 2026 data on RAGAS version changes or on competitors (DeepEval, TruLens, Phoenix, Braintrust autoevals) beyond the mentions above.
- Online and production evaluation (user feedback, A/B tests) for RAG was not researched.

---

## Q5. What new techniques and tools appeared in 2025-2026 (with dates)?

### Takeaway
2025-26 brought:
- the context-engineering framing and the context-rot evidence (mid to late 2025);
- platform features for context management: compaction, tool-result clearing and the memory tool (late 2025);
- constrained-decoding structured outputs from Anthropic, joining OpenAI (Nov 2025 beta, now GA);
- CFG-constrained custom tools (OpenAI GPT-5, Aug 2025);
- the agentic-search / "grep moment" shift in retrieval (Sep 2025 to Apr 2026);
- LazyGraphRAG (Nov 2024, adopted 2025);
- new embedding families (Qwen3-Embedding, Gemini Embedding 2, Voyage 4, voyage-multimodal-3.5 in Jan 2026);
- late-interaction multimodal retrievers (ColQwen3 and ColQwen3.5).

### Cited Findings (chronological)
- **Sep 2024**: Anthropic Contextual Retrieval (49% / 67% fewer failed retrievals). — [Anthropic](https://anthropic.com/news/contextual-retrieval)
- **Nov 2024**: Microsoft LazyGraphRAG. — [Microsoft Research](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)
- **Jun-Aug 2025**: LGAI-Embedding and QZhou-Embedding technical reports. — [arXiv 2506.07438](https://arxiv.org/pdf/2506.07438); [arXiv 2508.21632](https://arxiv.org/pdf/2508.21632)
- **Jul 2025**: Chroma "Context Rot" report (18 models). — [Morph summary](https://www.morphllm.com/context-rot)
- **Aug 2025**: OpenAI GPT-5 with reasoning-effort and verbosity controls and CFG-constrained custom tools. Responses API recommended. — [OpenAI GPT-5 guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.md)
- **Sep 2025**: Jason Liu, "Why grep beat embeddings in our SWE-bench agent". — [jxnl.co](https://jxnl.co/writing/2025/09/11/why-grep-beat-embeddings-in-our-swe-bench-agent-lessons-from-augment/)
- **29 Sep 2025**: Anthropic "Effective context engineering for AI agents". Memory tool (beta) and tool-result clearing / context editing on the Claude Developer Platform, released with Sonnet 4.5. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **Nov 2025**: Anthropic structured outputs public beta (`structured-outputs-2025-11-13`), now GA across Claude 4.5+ models including Opus 4.8 and Mythos Preview. — [Claude docs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- **Jan 2026**: Voyage voyage-multimodal-3.5 (video frames, Matryoshka). — [BigData Boutique](https://bigdataboutique.com/blog/multimodal-rag-retrieval-over-images-pdfs-and-text)
- **Early 2026**: Qwen3-Embedding listed at the top of MTEB v2 open-weight models. Note that some sources date Qwen3-Embedding to mid-2025, which is a conflict. Gemini Embedding 2 (multimodal, preview). — [Ailog](https://app.ailog.fr/en/blog/news/embedding-models-2026); [Presenc](https://presenc.ai/research/best-open-weight-embedding-models-2026)
- **2026**: ColQwen3 and ColQwen3.5 late-interaction multimodal retrievers supported in vLLM. ViDoRe v3 benchmark. — [vLLM docs](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colqwen3/); [Trae AI](https://learn.traeai.com/t/ai-engineering/phases/19-capstone-projects/04-multimodal-document-qa)
- **Feb 2026**: Cursor's hybrid of custom-trained embeddings and grep for code search is described. — [Morph](https://www.morphllm.com/agentic-search)
- **Apr 2026**: Doug Turnbull, "agentic search is having a grep moment". Tian Pan, GraphRAG in production. — [softwaredoug.com](https://softwaredoug.com/blog/2026/04/06/agentic-search-is-having-a-grep-moment); [tianpan.co](https://tianpan.co/blog/2026-04-09-graphrag-production-when-vector-search-hits-ceiling)
- **May-Jun 2026**: arXiv work on agentic retrieval interfaces ("direct corpus interaction", "retrieving interaction spaces"). SemEval-2026 Task 8 on multi-turn RAG. — [arXiv 2605.05242](https://arxiv.org/pdf/2605.05242); [arXiv 2606.06880](https://arxiv.org/pdf/2606.06880); [arXiv 2606.28352](https://arxiv.org/pdf/2606.28352)
- **2026**: OpenAI GPT-5.5 guide supersedes GPT-5 guidance (outcome-first prompting, schemas via Structured Outputs). The GPT-5.6 generation is reported to have changed caching pricing (unverified). — [OpenAI GPT-5.5 guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.5.md); [IntuitionLabs](https://intuitionlabs.ai/pdfs/llm-prompt-caching-cost-savings.pdf)

### Inferences
- The centre of gravity moved from "build a better retriever pipeline" (2023-24) to "give an agent good retrieval tools and manage its context over long horizons" (2025-26).
- The book should date every specific number (MTEB scores, cache prices, model names) and steer readers to re-check them, because they changed several times within 2025-26.

### Gaps
- Exact release dates were not verified this session for Qwen3-Embedding, Gemini Embedding 2, Voyage 4, GPT-5.5/5.6 and Claude Opus 4.6-4.8.
- Google's 2025-26 context-caching and long-context guidance and its Gemini prompting docs were not fetched.
- LlamaIndex and LangChain 2025-26 positioning (LlamaIndex's "agentic document workflows", LangChain/LangGraph context-engineering posts) was not researched in this session.
- MCP as the cross-provider tool-calling standard was not researched here (likely covered by an agents researcher).
