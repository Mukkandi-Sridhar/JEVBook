# Foundations and LLM Internals for an Applied AI Engineer (state as of October 2026)

Research date: 2026-10-20. Method: web search across practitioner blogs, arXiv, engine blogs and release roundups, plus well-known primary papers cited by arXiv ID. Several primary sites (sebastianraschka.com, magazine.sebastianraschka.com, latent.space, hidekazu-konishi.com) failed DNS resolution from this environment. Facts attributed to them come from search snippets only and are marked as such.

Source-quality legend used below:
- **[primary]**: the lab's own report or paper, or the engine's own blog.
- **[secondary]**: a practitioner blog, aggregator or roundup. Dates and version numbers from these should be checked before printing.
- **[canonical, not re-fetched]**: a famous paper cited by its stable arXiv ID from prior knowledge and not re-opened in this session. These are low-risk citations, but the wording should still be checked against the paper.

---

## Q1. Which foundation topics are truly necessary for applied AI engineers, and which are nice-to-have?

### Takeaway
Practitioner curricula agree that applied AI engineers can start building on foundation models without a formal ML background. What they need is a working mental model of how a model learns (objective, loss, gradient descent, overfitting, train/validation/test splits), how a transformer LLM produces tokens, and enough statistics to run trustworthy evaluations. Deep math (measure-theoretic probability, convex optimisation proofs, most classical ML algorithms in detail) is optional for this audience. Evaluation and statistics literacy matter more than model-building math.

### Cited Findings
- Chip Huyen's *AI Engineering* (O'Reilly, 2025) companion repo says an ML background isn't required to start building with foundation models, but that "a rough understanding of how AI works under the hood is useful to prevent misuse." It lists no specific math prerequisites and points to "Aman's Math Primers" (basic differential calculus and probability). [primary] — [chiphuyen/aie-book resources.md](https://github.com/chiphuyen/aie-book/blob/main/resources.md)
- The same repo's recommended "ML Theory Fundamentals" are: Stanford CS231n notes (lectures 1–7 of the 2017 recordings), Karpathy's "Neural Networks: Zero to Hero" (implementing models from scratch), Murphy's *Machine Learning: A Probabilistic Perspective* (2012), described as "comprehensive but intense", and a short note on objective functions and learning procedures. [primary] — [chiphuyen/aie-book resources.md](https://github.com/chiphuyen/aie-book/blob/main/resources.md)
- The book's own chapter structure shows what an applied AI engineer covers: planning applications, understanding foundation models (training, scaling laws, sampling, context length/RoPE), evaluation (two chapters), prompt engineering, RAG and agents, finetuning (LoRA, QLoRA, PEFT), dataset engineering, inference optimisation (KV cache, speculative sampling), and architecture plus user feedback. Theory topics appear only inside chapters: transformer architecture in Ch. 2, embeddings in Ch. 3, backprop and trainable parameters in Ch. 7. [primary] — [chiphuyen/aie-book resources.md](https://github.com/chiphuyen/aie-book/blob/main/resources.md)
- Reviewers describe the book as having "no code or mathematical formulas" while still assuming a technical reader. Its explanations of attention and RLHF are said to be clear for readers without deep ML math. [secondary] — [Javarevisited review](https://medium.com/javarevisited/review-is-ai-engineering-book-by-chip-huyen-worth-it-61e5f435e8ac); [Adnan Masood review](https://medium.com/@adnanmasood/codifying-the-craft-review-of-ai-engineering-building-applications-with-foundation-models-by-chi-50f181791362)
- Huyen's broader MLOps guide points to math-heavy texts (Murphy; MacKay's *Information Theory, Inference, and Learning Algorithms*) for ML fundamentals. That reading is for ML engineers, not a stated AI-engineer prerequisite. [primary] — [huyenchip.com/mlops](https://huyenchip.com/mlops/)
- Her suggested reading on training is a short list: GPT-3, Gopher, InstructGPT and the Llama 3 paper ("if you read only three"), Chinchilla for scaling laws, the RoPE paper for context length, and constrained decoding for sampling. [primary] — [chiphuyen/aie-book resources.md](https://github.com/chiphuyen/aie-book/blob/main/resources.md)
- Evaluation is treated as core. The recommended reading includes "Judging LLM-as-a-Judge", HELM, Eugene Yan's task-specific evals post, and Hamel Husain's "Your AI Product Needs Evals". [primary] — [chiphuyen/aie-book resources.md](https://github.com/chiphuyen/aie-book/blob/main/resources.md)

### Inferences
Proposed "must / nice / skip" split for the book. This is a synthesis of the curricula above, not a quoted list.
- **Must-have (probability and statistics):** distributions and sampling, which explain temperature, top-p and why outputs vary. Expectation and variance. Conditional probability, which frames a model as computing P(next token | context). Log-probabilities and softmax. Cross-entropy and perplexity at an intuitive level. Confidence intervals and bootstrap for eval scores. Comparing two systems on the same eval set (paired tests, why n=50 is noisy). Precision, recall, F1 and calibration. Base rates in classifier and guardrail metrics.
- **Must-have (classical ML):** supervised vs unsupervised learning. Train/validation/test splits and leakage. Overfitting and regularisation intuition. Baselines (logistic regression, gradient-boosted trees) as cheap, strong alternatives for tabular and classification tasks. Embeddings and cosine similarity. k-NN and approximate nearest-neighbour search, which underpins vector search.
- **Must-have (deep learning):** neurons and layers as matrix multiplications. Loss, gradient descent and backprop at the conceptual level. Parameters vs activations vs optimiser state, which is needed for memory maths. Mixed precision (FP32/BF16/FP8). What finetuning changes and what LoRA does.
- **Must-have (NLP):** tokenisation (BPE), embeddings, the transformer decoder (attention, MLP, residual stream, normalisation), autoregressive generation, the context window, the KV cache, and sampling.
- **Nice-to-have:** implementing a small GPT from scratch (Karpathy-style), CNNs/RNNs for history, information theory beyond cross-entropy, RL basics (policy gradient) to understand RLHF and GRPO.
- **Usually skippable for applied engineers:** SVM and kernel theory, VC dimension and PAC learning, detailed probabilistic graphical models, hand-deriving backprop for every layer type, measure theory, and classical NLP pipelines (HMM/CRF taggers, parse trees) except as history.

### Gaps
- No formal survey quantifying which foundation topics working AI engineers actually use was found. The split above is inferred from curricula and book structure.
- The full text of Huyen's "minimum viable curriculum" (mentioned on her MLOps page) was not located.

---

## Q2. Which LLM architecture and training developments of 2025–2026 must an AI engineer understand?

### Takeaway
The core decoder-only transformer has barely changed. Most 2025–2026 change is in efficiency and in how models are trained. The shifts that matter:
- Mixture-of-experts (MoE) is now the default for large open models.
- Attention variants have moved toward KV-cache compression and sparsity: GQA, then MLA, then DeepSeek Sparse Attention and compressed attention, plus hybrids with linear-attention or state-space layers, aimed at 1M-token contexts.
- RoPE with context-extension tricks remains standard.
- Post-training has moved from RLHF/PPO and DPO toward large-scale RL from verifiable rewards (RLVR) using GRPO-family algorithms. That shift produced "thinking" models whose quality scales with test-time compute.

### Cited Findings

**Architecture landscape and convergence**
- Sebastian Raschka's 2026 "LLM Architecture Gallery" collects architecture figures and fact sheets per model (parameters, release date, dense vs MoE, attention mechanism). Snippets disagree on its size: one says about 98 architectures through mid-2026, a Korean write-up says 50 major LLMs from 2024–2026. [primary, snippet only; site unreachable] — [Raschka gallery](https://sebastianraschka.com/blog/2026/llm-architecture-gallery.html); [wikidocs summary](https://wikidocs.net/blog/@jaehong/9574/)
- A Korean commentary on the gallery is titled (translated) "LLM architectures are converging; the real war is elsewhere." [secondary] — [wikidocs](https://wikidocs.net/blog/@jaehong/9574/)
- Raschka also published "A Dream of Spring for Open-Weight LLMs: 10 Architectures from Jan–Feb 2026". [primary, snippet only] — [Raschka blog index](https://www.sebastianraschka.com/blog/)

**Attention variants (MHA → GQA → MLA → sparse and hybrid)**
- Raschka's "A Visual Guide to Attention Variants in Modern LLMs" (22 March 2026) covers MHA, GQA, MLA, sliding-window, sparse, gated and hybrid linear attention. [primary, snippet only] — [Ahead of AI](https://magazine.sebastianraschka.com/p/visual-attention-variants)
  - It presents MLA as *compression* rather than *sharing*, includes ablations, and traces MLA's spread from DeepSeek V3 to Kimi K2, GLM-5 and Mistral Large 3.
  - It contrasts DeepSeek Sparse Attention (DSA) with sliding windows and notes that DSA is paired with MLA.
  - Its hybrid examples are Gated DeltaNet, Kimi Delta Attention, Ling 2.5's Lightning Attention and Nemotron's Mamba-2 layers.
  - A third-party explainer of the gallery calls GQA "now the standard". [secondary] — [themenonlab](https://themenonlab.blog/blog/llm-architecture-gallery-raschka-explained)
- The gallery's attention-distribution page counts one model under several mechanisms (for example MLA plus DSA). [primary, snippet only] — [attention distribution](https://www.sebastianraschka.com/llm-architecture-gallery/attention-mechanism-distribution/)
- Background papers [canonical, not re-fetched]:
  - Multi-head attention: [Vaswani et al. 2017, arXiv 1706.03762](https://arxiv.org/abs/1706.03762).
  - Grouped-query attention, where several query heads share K/V heads to shrink the KV cache: [Ainslie et al. 2023, arXiv 2305.13245](https://arxiv.org/abs/2305.13245).
  - Multi-head latent attention, which caches a low-rank latent instead of full K/V, introduced in [DeepSeek-V2, arXiv 2405.04434](https://arxiv.org/abs/2405.04434) and used in [DeepSeek-V3, arXiv 2412.19437](https://arxiv.org/abs/2412.19437).
  - Linear-time state-space models: [Mamba, arXiv 2312.00752](https://arxiv.org/abs/2312.00752).
  - [Gated DeltaNet, arXiv 2412.06464](https://arxiv.org/abs/2412.06464).
- Active 2026 research on hybrid attention:
  - ConSA, on learnable allocation of sliding-window vs full-attention layers. — [arXiv 2606.18056](https://arxiv.org/pdf/2606.18056)
  - Work on massive activations in hybrid linear-attention LLMs. — [arXiv 2608.12149](https://arxiv.org/pdf/2608.12149)

**FlashAttention**
- FlashAttention computes exact attention with IO-aware tiling, so the full N×N attention matrix is never written to slow GPU memory. FlashAttention-2 improved parallelism, and FlashAttention-3 targets Hopper (asynchrony, FP8). [canonical, not re-fetched] — [FA1 arXiv 2205.14135](https://arxiv.org/abs/2205.14135); [FA2 arXiv 2307.08691](https://arxiv.org/abs/2307.08691); [FA3 arXiv 2407.08608](https://arxiv.org/abs/2407.08608)
- Key teaching point: FlashAttention is a *kernel* optimisation. It gives the same mathematical result and does not approximate attention. Sparse, sliding-window and linear attention *do* change the computation.

**Positional encodings and long context**
- RoPE (rotary position embeddings) encodes position by rotating query/key vectors. [canonical, not re-fetched] — [Su et al., arXiv 2104.09864](https://arxiv.org/abs/2104.09864)
- YaRN and similar RoPE-scaling methods extend context after pretraining. [canonical, not re-fetched] — [YaRN, arXiv 2309.00071](https://arxiv.org/abs/2309.00071)
- RoPE is the reference Huyen gives for context length. [primary] — [aie-book resources](https://github.com/chiphuyen/aie-book/blob/main/resources.md)

**DeepSeek V4 (24 April 2026): flagship example of 2026 efficiency architecture**
- Released as an open-weights preview on 24 April 2026 in two sizes. [secondary; tech report not reached] — [datanorth.ai](https://datanorth.ai/news/deepseek-releases-v4-open-source-1m-context); [smol.ai AINews 26-04-24](https://news.smol.ai/issues/26-04-24-deepseek-v4); [mer.vin explainer](https://mer.vin/2026/04/deepseek-v4-preview-explained)
  - V4-Pro: MoE, 1.6T total and about 49B active parameters.
  - V4-Flash: 284B total and about 13B active.
  - Both have a 1M-token context.
- Its long-context design is a hybrid attention called CSA + HCA (compressed sparse attention plus heavily compressed attention). At 1M context it reportedly needs about 27% of single-token FLOPs and about 10% of the KV cache of DeepSeek-V3.2. [secondary] — [same sources](https://news.smol.ai/issues/26-04-24-deepseek-v4)
- Other reported components: mHC (manifold-constrained hyper-connections), the Muon optimiser, FP4/FP8 mixed precision, and pretraining on about 33T tokens (Pro) and 32T (Flash). [secondary] — [same sources](https://datanorth.ai/news/deepseek-releases-v4-open-source-1m-context)
- A community summary describes a 128-token sliding window plus top-k sparse attention over compressed tokens. This is unverified. [secondary] — [mer.vin](https://mer.vin/2026/04/deepseek-v4-preview-explained-1m-context-architecture-benchmarks-pricing-and-enterprise-adoption-guide/?amp=1)
- License conflict: one source says Apache 2.0, others say MIT. Another roundup lists both V4 variants as MIT. [secondary, conflicting] — [Konishi timeline (snippet)](https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html)

**Mixture-of-experts**
- 2026's leading open models are mostly MoE, written as total-A-active. [secondary] — [Taskade, Aug 2026](https://www.taskade.com/blog/open-source-llms); [Codersera Oct 2026](https://codersera.com/blog/open-source-llms-landscape-2026/)
  - Qwen 3.6 35B-A3B.
  - DeepSeek V4 1.6T-A49B.
  - Qwen3.8-2.4T-A95B flagship.
  - Mistral Small 4 is also MoE.
- Dense models persist at the small and medium end: Qwen 3.6 27B dense, Gemma 4 up to 31B dense, Mistral Medium 3.5 128B dense. [secondary] — [Computing for Geeks](https://computingforgeeks.com/open-source-llm-comparison/); [Codersera](https://codersera.com/blog/open-source-llms-landscape-2026/)

**Pretraining data and scaling**
- Chinchilla (2022) established compute-optimal scaling of about 20 tokens per parameter. [canonical, not re-fetched] — [Hoffmann et al., arXiv 2203.15556](https://arxiv.org/abs/2203.15556)
- Modern models train far beyond Chinchilla-optimal ("overtraining") because inference cost dominates. DeepSeek V4's reported 32–33T tokens is one data point. [secondary] — [datanorth.ai](https://datanorth.ai/news/deepseek-releases-v4-open-source-1m-context)
- Huyen recommends the Llama 3 paper's synthetic-data section for dataset engineering. [primary] — [aie-book](https://github.com/chiphuyen/aie-book/blob/main/resources.md)

**Post-training: SFT → RLHF → DPO → RLVR/GRPO**
- InstructGPT (2022) set up the SFT + reward model + PPO (RLHF) pipeline. [canonical, not re-fetched] — [arXiv 2203.02155](https://arxiv.org/abs/2203.02155)
- DPO (2023) replaces the reward model and RL loop with a classification-style loss on preference pairs. [canonical, not re-fetched] — [arXiv 2305.18290](https://arxiv.org/abs/2305.18290)
- GRPO was introduced in DeepSeekMath (2024). DeepSeek-R1 (January 2025) showed that RL with rule-based, verifiable rewards produces long chain-of-thought reasoning. [canonical, not re-fetched] — [DeepSeekMath arXiv 2402.03300](https://arxiv.org/abs/2402.03300); [DeepSeek-R1 arXiv 2501.12948](https://arxiv.org/abs/2501.12948)
- As of 2026, RLVR is described as the dominant post-training approach for reasoning. It automatically checks answers in math and code. [primary preprints] — [PaperGym arXiv 2608.31119](https://arxiv.org/pdf/2608.31119); [MInTRL arXiv 2609.12419](https://arxiv.org/pdf/2609.12419)
- GRPO's core idea is to drop the learned critic or value model and use the group-average reward of sampled responses as the baseline. [primary] — [Demystifying GRPO, arXiv 2603.01162](https://arxiv.org/pdf/2603.01162)
- Refinements fix GRPO's length bias, instability and sample inefficiency: Dr. GRPO, DAPO, CISPO, VAPO, A*PO, and GSPO (sequence-level importance ratios). The field is moving away from PPO-style pipelines. [primary/secondary] — [MInTRL](https://arxiv.org/pdf/2609.12419); [Turing Post "Reasoning RL in 2026"](https://www.turingpost.com/p/reasoning-rl-in-2026)
- Open problems in 2026:
  - Rollout cost and sample efficiency. — [arXiv 2605.30789](https://arxiv.org/pdf/2605.30789); [rollout efficiency taxonomy arXiv 2609.25463](https://arxiv.org/pdf/2609.25463)
  - Poor understanding of what RL actually changes. — [Predictable GRPO arXiv 2606.30789](https://arxiv.org/pdf/2606.30789)
  - Mixing on-policy self-distillation with GRPO for denser per-token signal. — [PaperGym](https://arxiv.org/pdf/2608.31119)
  - Rubric-based rewards for non-verifiable tasks. — [PaperGym](https://arxiv.org/pdf/2608.31119)
- A unified policy-gradient survey of PPO and GRPO methods, revised May 2026. — [arXiv 2407.16216](https://arxiv.org/abs/2407.16216)

**Reasoning models and test-time compute**
- Snell et al. (2024) showed that spending more inference compute can beat scaling parameters on some tasks. DeepSeek-R1 (January 2025) made "thinking" models open. [canonical, not re-fetched] — [arXiv 2408.03314](https://arxiv.org/abs/2408.03314); [arXiv 2501.12948](https://arxiv.org/abs/2501.12948)
- By 2026, frontier releases are framed around cost per task and reasoning effort. One roundup says GPT-6.1 Sol performs near GPT-6 Astra "at about one-fifth the cost per task". [secondary, unverified] — [Medium "AI Landscape Sept 2026"](https://medium.com/@ConcernedhumanonAI/the-ai-landscape-september-2026-fd9a3140b1ce)

### Inferences
- For the book: teach the "standard 2026 block", meaning a decoder-only transformer with pre-norm (RMSNorm), SwiGLU MLP or MoE, RoPE, and GQA or MLA. Present everything else as deltas from that block. Raschka's gallery confirms this convergence.
- KV-cache size is the unifying idea behind nearly every 2025–2026 attention innovation (GQA, MLA, DSA, CSA/HCA, hybrids). Engineers should learn to estimate KV-cache memory as layers × KV heads × head dim × 2 (K and V) × bytes × tokens.
- Practitioners need RLVR/GRPO at the conceptual level: it explains why models are strongest at math and code (where rewards are verifiable), why reasoning traces are long and costly, and why "reasoning effort" knobs exist. They rarely need to implement it.

### Gaps
- The DeepSeek V4 technical report itself was not read (the source was unreachable). The CSA/HCA details, 27%/10% efficiency figures and license need verification against the report or Hugging Face card.
- Raschka's articles could not be opened. Model-to-mechanism mappings come from search snippets.
- No verified information was found on pretraining data composition trends for 2026 (data mixes, synthetic share, filtering) beyond token counts.
- Tokeniser developments in 2025–2026 (vocabulary sizes, byte-level or tokeniser-free models) were not researched in this session.

---

## Q3. What is current best practice for serving and inference, and for choosing between API models and open-weight or local models?

### Takeaway
Self-hosting in 2026 means running vLLM, SGLang or TensorRT-LLM. These engines combine paged KV-cache management, continuous batching, prefix caching and EAGLE-3-family speculative decoding with FP8 or 4-bit (AWQ/GPTQ, NVFP4/MXFP4 on Blackwell) quantisation. Local and desktop inference uses llama.cpp/GGUF at Q4_K_M–Q6_K. API models remain the default for frontier quality and low operational burden. Open-weight models win on data control, fine-tuning, predictable cost at high steady volume, and offline or edge use.

### Cited Findings

**Serving engines and core techniques**
- PagedAttention / vLLM manages the KV cache in fixed-size pages, like OS virtual memory, which enables continuous batching with little fragmentation. [canonical, not re-fetched] — [Kwon et al., arXiv 2309.06180](https://arxiv.org/abs/2309.06180)
- SGLang introduced RadixAttention for automatic prefix (KV) reuse across requests. [canonical, not re-fetched] — [Zheng et al., arXiv 2312.07104](https://arxiv.org/abs/2312.07104)
- Speculative decoding: a cheap draft proposes tokens and the target verifies them in parallel. The output distribution is unchanged. [canonical, not re-fetched] — [Leviathan et al., arXiv 2211.17192](https://arxiv.org/abs/2211.17192)
- EAGLE-3 (March 2025) is described as "the de facto industry standard for speculative decoding". SGLang, vLLM and TensorRT-LLM all support it. [primary] — [EAGLE-3 arXiv 2503.01840](https://arxiv.org/pdf/2503.01840); [SpecForge arXiv 2603.18567](https://arxiv.org/html/2603.18567v1)
- vLLM's blog (26 May 2026) announced EAGLE 3.1, built with the EAGLE team and TorchSpec. It is configured via `--speculative-config` with `"method":"eagle3"`. [primary] — [vLLM blog](https://vllm.ai/blog/2026-05-26-eagle-3-1)
- SGLang uses `--speculative-algorithm EAGLE3`. TensorRT-LLM provides EAGLE-3 heads, with modules on Hugging Face. [secondary] — [Spheron EAGLE-3 guide](https://www.spheron.network/blog/eagle-3-speculative-decoding-gpu-cloud/)
- vLLM published speculative decoding on AMD GPUs (23 August 2026), showing the engines are no longer NVIDIA-only. [primary] — [vLLM blog](https://vllm.ai/blog/2026-08-23-speculative-decoding-amd-gpus)
- Typical speculative-decoding speedups are put at 20–50%, with up to 2–5x claimed. These are vendor or blog numbers and workload-dependent. [secondary] — [Glukhov](https://www.glukhov.org/llm-performance/optimization/speculative-decoding/); [Spheron production guide](https://www.spheron.network/blog/speculative-decoding-production-guide/)
- Caveats on speculative decoding:
  - Adversarial prompts can collapse the acceptance rate and remove the speedup (2026). — [arXiv 2607.21804](https://arxiv.org/pdf/2607.21804)
  - Batched speculative decoding has known correctness pitfalls (the "ragged tensor" problem). — [arXiv 2510.22876](https://arxiv.org/pdf/2510.22876)
- NVIDIA ships NVFP4 checkpoints, for example Kimi-K2.6-NVFP4, served in vLLM with an EAGLE-3.1 draft. [secondary snippet] — [vLLM EAGLE 3.1 blog](https://vllm.ai/blog/2026-05-26-eagle-3-1)
- SemiAnalysis's InferenceX dashboard tracks DeepSeek V4 serving performance. It is a useful source for the book's cost and throughput figures. [secondary] — [InferenceX](https://inferencex.semianalysis.com/model/deepseek-v4)

**Quantisation**
- GGUF is a file format used by llama.cpp, not an algorithm. Its k-quants run on CPU, which makes it the default for local inference. [secondary] — [fungies.io guide](https://fungies.io/llm-quantization-gguf-awq-gptq-guide-2026/); [wz-it](https://wz-it.com/en/knowledge/ki/llm-quantization/)
  - Q5_K_M and Q6_K are near-BF16 quality.
  - Q4_K_M is the common default balance.
  - Q2_K degrades noticeably.
- AWQ usually gives the best 4-bit quality, especially for instruction-tuned models. GPTQ quality is comparable, and GPTQ-Int4 supports LoRA adapters in vLLM. [secondary] — [same guides](https://vrlatech.com/llm-quantization-explained-int4-int8-fp8-awq-and-gptq-in-2026/)
- Original papers [canonical, not re-fetched] — [GPTQ arXiv 2210.17323](https://arxiv.org/abs/2210.17323); [AWQ arXiv 2306.00978](https://arxiv.org/abs/2306.00978)
- FP8 is the "near-lossless" middle ground on Hopper, Ada and Blackwell GPUs. [secondary] — [traeai production quantization](https://learn.traeai.com/t/ai-engineering/phases/17-infrastructure-and-production/09-production-quantization)
- NVFP4 and MXFP4 are Blackwell-era 4-bit floating-point formats. NVFP4 uses an FP8 (E4M3) scale per 16 values plus an FP32 per-tensor scale, about 4.5 bits per value. They are aggressive and need per-block validation. [secondary] — [traeai](https://learn.traeai.com/t/ai-engineering/phases/17-infrastructure-and-production/09-production-quantization); [wz-it](https://wz-it.com/en/knowledge/ki/llm-quantization/)
- Quantisation pitfalls:
  - The calibration dataset must match the deployment domain.
  - KV-cache quantisation is separate from weight quantisation.
  - Quality loss is "typically 1–5%" depending on method and bit depth. [secondary] — [fungies.io](https://fungies.io/llm-quantization-gguf-awq-gptq-guide-2026/)
- DeepSeek V4 reportedly trained with FP4/FP8 mixed precision. Low precision is moving into training, not only inference. [secondary] — [datanorth.ai](https://datanorth.ai/news/deepseek-releases-v4-open-source-1m-context)
- QLoRA (4-bit base model + LoRA) is still the reference method for cheap fine-tuning. [canonical, not re-fetched] — [LoRA arXiv 2106.09685](https://arxiv.org/abs/2106.09685); [QLoRA arXiv 2305.14314](https://arxiv.org/abs/2305.14314)

**API vs open-weight trade-offs**
- Open-weight licensing is uneven, and "open" is not always permissive. [secondary] — [Codersera Oct 2026](https://codersera.com/blog/open-source-llms-landscape-2026/); [xigh/open-weight-models](https://github.com/xigh/open-weight-models)
  - Apache 2.0: Qwen 3.6, Gemma 4, Mistral Small 4.
  - MIT: DeepSeek V4, though reports conflict.
  - Custom or non-OSI: Qwen3.8 flagship (revenue-gated), Mistral Medium 3.5, and the Llama 4 Community License. One source reports EU restrictions on Llama multimodal use.
- 2026 frontier releases compete on "lower costs per unit of work" and on specific domains (coding, cybersecurity). [secondary, unverified] — [Medium Sept 2026](https://medium.com/@ConcernedhumanonAI/the-ai-landscape-september-2026-fd9a3140b1ce); [dutchstartup.ai](https://www.dutchstartup.ai/en/news/google-openai-anthropic-and-mistral-release-new-frontier-models-in-late)

### Inferences
- A decision framework for the book:
  1. Start with an API frontier model to establish a quality ceiling and build evals.
  2. Try a cheaper API tier (mini/flash/haiku class).
  3. Consider open-weight models only when one of these applies: data residency or privacy, a fine-tuning need, steady high volume where GPU utilisation can stay high, latency or edge constraints, or vendor-risk concerns.
  4. Self-hosting cost is dominated by GPU utilisation. Low or bursty traffic almost always favours APIs.
- Metrics to teach: time-to-first-token (prefill-bound), inter-token latency or tokens/s (decode-bound, memory-bandwidth-bound), throughput vs latency under batching, and cost per million tokens vs cost per *task*. Cost per task matters because reasoning models emit many hidden tokens.
- Prompt and prefix caching (provider-side, or RadixAttention/prefix caching in engines) is one of the cheapest wins. It depends on putting stable content at the start of the prompt.

### Gaps
- No primary 2026 source on disaggregated prefill/decode serving (for example NVIDIA Dynamo, llm-d, Mooncake-style designs) was found within the tool budget. It needs a separate lookup.
- No independent benchmark of NVFP4/MXFP4 quality versus AWQ/FP8 was found. Only vendor and blog claims.
- No authoritative 2026 cost comparison (API price per million tokens vs self-hosted $/M tokens) was collected. Current API prices should be taken from provider pricing pages at writing time.
- MLX (Apple), Ollama and LM Studio were not researched in this session.

---

## Q4. What are the current leading frontier and open-weight model families, and their notable capabilities (late 2026)?

### Takeaway
Closed frontier models: OpenAI's GPT-5.x line led into a reported GPT-6 generation (September 2026), Anthropic's Claude 4.x moved to 5.x (Opus/Sonnet 5.5 reported September 2026), and Google's Gemini 3.x (with a reported Gemini 4 variant in late September 2026). Early-2026 releases are well corroborated. September–October 2026 names and dates come only from aggregators and must be verified. Leading open-weight families: Qwen (3.5/3.6/3.8), DeepSeek (V4, April 2026), Gemma 4, Mistral (Small 4, Medium 3.5), Llama 4, Kimi K2.x/K3 and GLM-5.x. Most large open models are MoE.

### Cited Findings

**Closed or frontier models: well-corroborated timeline (late 2025 to mid 2026)**
- Gemini 3 Pro: late 2025 (about 3 weeks before GPT-5.2). [secondary/Wikipedia] — [GPT-5.2 Wikipedia](https://en.wikipedia.org/wiki/GPT-5.2)
- GPT-5.2: 11 December 2025. — [GPT-5.2 Wikipedia](https://en.wikipedia.org/wiki/GPT-5.2)
- GPT-5.3-Codex: 5 February 2026. — [GPT-5.3-Codex Wikipedia](https://en.wikipedia.org/wiki/GPT-5.3-Codex)
- GPT-5.4: 5 March 2026. — [TeamDay](https://www.teamday.ai/blog/frontier-ai-models-february-2026); [Plative March 2026](https://plative.com/insights/blog/frontier-model-stack-march-2026/)
- Claude Sonnet 4.6: 17 February 2026, "near-Opus performance at 1/5th the price". [secondary] — [TeamDay](https://www.teamday.ai/blog/frontier-ai-models-february-2026)
- Gemini 3.1 Pro: 19 February 2026, reported ARC-AGI-2 score of 77.1%. [secondary] — [TeamDay](https://www.teamday.ai/blog/frontier-ai-models-february-2026)
- A May 2026 roundup names the closed frontier as Gemini 3.1 Pro, Claude Sonnet 4.6, Claude Opus 4.7 and GPT-5.5. [secondary] — [localaimaster](https://localaimaster.com/blog/best-ai-models-2026)

**Closed or frontier models: September–October 2026 (only aggregator sources, which conflict)**
- OpenAI [secondary, conflicting] — [Medium](https://medium.com/@ConcernedhumanonAI/the-ai-landscape-september-2026-fd9a3140b1ce); [Microcenter](https://www.microcenter.com/site/mc-news/article/this-week-in-ai-oct-2-2026.aspx); [LLM Gateway timeline](https://llmgateway.io/timeline)
  - GPT-6 Astra reported 3 September 2026.
  - GPT-6 Sol and Luna reported 22 September.
  - GPT-6.1 Sol reported at DevDay on 29 September.
  - Reports that an October GPT-6.1 Astra release was scrapped after safety testing.
- Anthropic [secondary] — [Medium](https://medium.com/@ConcernedhumanonAI/the-ai-landscape-september-2026-fd9a3140b1ce); [LLM Gateway](https://llmgateway.io/timeline)
  - "Fable 5.1" and "Mythos 5.1" reported 1 September.
  - Claude Opus 5.5 reported 22 September.
  - Sonnet 5.5 reported 28 September.
  - Haiku 5.5 reported 7 October.
  - Corroboration: the environment running this research identifies itself as "Claude Opus 5.5" and its tooling references "Fable", which fits the existence of those names. Dates remain unverified.
- Google [secondary] — [Microcenter](https://www.microcenter.com/site/mc-news/article/this-week-in-ai-oct-2-2026.aspx); [LLM Gateway](https://llmgateway.io/timeline)
  - "Gemini 4 Argon" (cybersecurity-focused) reported 30 September 2026.
  - "Gemini 3.8 Flash" API reported 2 September 2026.
  - "Nano Banana 2.1" image model reported 6 October 2026.
- A Dutch outlet reports Google, OpenAI, Anthropic and Mistral all releasing new frontier models in late September 2026. [secondary] — [dutchstartup.ai](https://www.dutchstartup.ai/en/news/google-openai-anthropic-and-mistral-release-new-frontier-models-in-late)

**Open-weight families (2025–2026)**
- Older dated anchors [canonical, not re-fetched] — [Meta Llama 4 blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/); [OpenAI gpt-oss](https://openai.com/index/introducing-gpt-oss/); [Qwen3 tech report arXiv 2505.09388](https://arxiv.org/abs/2505.09388); [DeepSeek-R1 arXiv 2501.12948](https://arxiv.org/abs/2501.12948)
  - Llama 4 (Scout/Maverick, MoE, natively multimodal): 5 April 2025.
  - OpenAI gpt-oss-120b and gpt-oss-20b (MoE, Apache 2.0, MXFP4 weights): 5 August 2025.
  - Qwen3 family (dense and MoE, hybrid thinking/non-thinking): late April 2025.
  - DeepSeek-R1: 20 January 2025.
- **Qwen** [secondary] — [Taskade](https://www.taskade.com/blog/open-source-llms); [Codersera Oct](https://codersera.com/blog/open-source-llms-landscape-2026/); [Codersera May](https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/)
  - Qwen 3.5 (early 2026).
  - Qwen 3.6 (April 2026): 35B-A3B MoE and 27B dense, Apache 2.0.
  - Qwen3.8 27B dense (Apache 2.0), released 5 August or 14 August 2026 depending on the source. Described as the "most-downloaded new open model of 2026".
  - Qwen3.8-2.4T-A95B flagship under a revenue-gated custom license.
- **DeepSeek** [secondary] — [AceCloud](https://acecloud.ai/blog/best-open-source-llms/)
  - V4-Pro and V4-Flash (24 April 2026), MIT, 1M context.
  - V4.1-Flash appears in October 2026 roundups as a leading coding and agentic open model.
- **Gemma 4** (Google): Apache 2.0, small sizes up to 31B dense, with a 12B variant in June 2026. [secondary] — [Computing for Geeks](https://computingforgeeks.com/open-source-llm-comparison/)
- **Mistral** [secondary] — [Konishi timeline (snippet)](https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html); [Codersera](https://codersera.com/blog/open-source-llms-landscape-2026/); [Computing for Geeks](https://computingforgeeks.com/open-source-llm-comparison/)
  - Mistral Small 4 (March 2026): Apache 2.0 MoE combining reasoning, multimodal and coding.
  - Mistral Medium 3.5: 128B dense, custom license.
  - Mistral Large 3 uses MLA.
  - A larger open-weight family is in partner early access.
- **Llama 4**: still widely used, under the Llama 4 Community License (not permissive). [secondary] — [xigh/open-weight-models](https://github.com/xigh/open-weight-models)
- **Kimi (Moonshot)**: K2 uses MLA. K2.6 is available as an NVIDIA NVFP4 checkpoint. "Kimi K3" is named among the strongest open models in October 2026. [secondary] — [Raschka attention guide (snippet)](https://magazine.sebastianraschka.com/p/visual-attention-variants); [vLLM EAGLE 3.1 blog](https://vllm.ai/blog/2026-05-26-eagle-3-1); [AceCloud](https://acecloud.ai/blog/best-open-source-llms/)
- **GLM-5.x (Z.ai)**: uses MLA and is among the top open models in October 2026. [secondary] — [AceCloud](https://acecloud.ai/blog/best-open-source-llms/)
- **Hybrid-architecture open models**: Ling 2.5 (Lightning Attention) and NVIDIA Nemotron (Mamba-2 hybrid). [primary snippet] — [Raschka attention guide](https://magazine.sebastianraschka.com/p/visual-attention-variants)

**Multimodal**
- Mistral Small 4 is multimodal. Llama 4 is natively multimodal. Google ships image models (Nano Banana line). [secondary] — [Konishi timeline (snippet)](https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html); [LLM Gateway](https://llmgateway.io/timeline)

### Inferences
- For the book, describe model *tiers* and *selection criteria*, not specific version numbers. Version numbers changed roughly monthly in 2026, and print will date quickly. Suggested tiers:
  - Frontier reasoning (Opus/GPT-6/Gemini Pro class).
  - Fast, cheap workhorse (Sonnet/Flash/mini class).
  - Small, on-device (Gemma 4, small Qwen, Phi-class).
  - Large open MoE (DeepSeek V4, Qwen3.8, Kimi, GLM).
- Practical local sweet spots in 2026: around 27–35B models (Qwen 3.6/3.8 27B dense, Qwen 3.6 35B-A3B MoE, Gemma 4 31B), which run on one consumer or workstation GPU at 4-bit.

### Gaps
- No official release posts for the September–October 2026 frontier models (GPT-6 family, Claude 5.5 family, Gemini 4 Argon) were retrieved. Names, dates and capabilities need verification on openai.com, anthropic.com and blog.google before publication.
- Microsoft Phi (Phi-4 and successors) 2026 status was not found in this session.
- Multimodal details (vision encoders, native audio, realtime voice APIs such as OpenAI Realtime or Gemini Live, speech-to-speech latency) were not researched within budget. This is a notable gap for the multimodal chapter.
- Benchmark numbers for open vs closed models in late 2026 were not collected from a primary leaderboard (LMArena, Artificial Analysis, SWE-bench).

---

## Q5. What do engineers commonly misunderstand about LLM internals that causes production mistakes?

### Takeaway
The most costly misconceptions:
- Setting temperature to 0 makes output deterministic.
- A larger context window means the model reliably uses all of it.
- Tokens are words.
- Quantisation and speculative decoding are free.
- Price per token equals cost per task.
- Fine-tuning is the right way to add knowledge.
- The model "knows" or "remembers" across calls.

Most of these trace back to a missing understanding of sampling, batching, the KV cache and attention behaviour over long inputs.

### Cited Findings
- **Temperature 0 is not deterministic in serving.** Thinking Machines Lab (Horace He et al., September 2025) argues that the usual explanation, "floating-point non-associativity plus GPU concurrency", is incomplete. The main cause is *batch variance*: the same prompt in a batch of 1 vs 32 gives different logits because reduction kernels split work differently by batch size. [secondary summaries; original blog: thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference, not fetched] — [OpenAI community thread](https://community.openai.com/t/defeating-nondeterminism-in-llm-inference/1358623); [batch-invariant kernels explainer](https://mohakchugh.is-a.dev/blog/batch-invariant-kernels-deterministic-llm-inference)
  - The fix is batch-invariant kernels for RMSNorm, matmul and attention.
  - Reported results: 1000 runs of one prompt gave 80 unique completions on default vLLM vs 1 with deterministic kernels, at a cost of about 26s vs 42s on one task. Numbers are from secondary summaries.
- A 2026 paper (LLM-42) proposes determinism through verified speculation instead of universal batch-invariant kernels. — [arXiv 2601.17768](https://arxiv.org/pdf/2601.17768)
- **Long context degrades ("context rot").** Chroma's study (Hong, Troynikov, Huber, July 2025) tested 18 models, including GPT-4.1, Claude 4, Gemini 2.5 and Qwen3. [secondary summaries; original research.trychroma.com/context-rot not fetched] — [dair.ai](https://academy.dair.ai/papers/context-rot); [morphllm](https://www.morphllm.com/context-rot); [Cobus Greyling](https://cobusgreyling.substack.com/p/llm-context-rot)
  - Performance declined as input grew, even on trivial tasks such as repeating a string.
  - Lower question–evidence semantic similarity and plausible distractors made it worse.
  - GPT models tended to hallucinate when confused, and Claude models tended to abstain.
  - Coherent haystacks reportedly hurt *more* than shuffled ones.
- **"Lost in the middle":** information in the middle of long inputs is recalled worse than at the start or end. [canonical, not re-fetched] — [Liu et al., arXiv 2307.03172](https://arxiv.org/abs/2307.03172); also reported in context-rot summaries — [memx](https://memx.app/blog/context-rot-long-input-degradation/)
- **Speculative decoding is not always a speedup.** Acceptance rate depends on the workload, and adversarial or out-of-distribution prompts can collapse it. Batched implementations have correctness pitfalls. — [arXiv 2607.21804](https://arxiv.org/pdf/2607.21804); [arXiv 2510.22876](https://arxiv.org/pdf/2510.22876)
- **Quantisation is not free or uniform.** Calibration data must match the domain. KV-cache quantisation is separate from weights. Q2-level GGUF degrades noticeably. 4-bit FP formats need validation. — [fungies.io](https://fungies.io/llm-quantization-gguf-awq-gptq-guide-2026/); [traeai](https://learn.traeai.com/t/ai-engineering/phases/17-infrastructure-and-production/09-production-quantization)
- **Open weights does not mean open source or a permissive license.** Several 2026 "open" flagships use revenue-gated or custom licenses, and Llama's license has geographic and use limits. — [Codersera](https://codersera.com/blog/open-source-llms-landscape-2026/); [xigh/open-weight-models](https://github.com/xigh/open-weight-models)
- **Huyen's warning:** a rough understanding of internals is useful "to prevent misuse". [primary] — [aie-book resources](https://github.com/chiphuyen/aie-book/blob/main/resources.md)

### Inferences
Each misconception below is paired with the internal concept the book should teach to fix it.
- *"Temperature 0 = reproducible"* → teach sampling plus batch variance. Log model version and parameters, and design evals to tolerate variance (multiple runs, confidence intervals).
- *"1M context, so stuff everything in"* → teach attention dilution, context rot and lost-in-the-middle. Prefer retrieval and context curation, put key instructions at the start and end, and measure accuracy at the context lengths you will actually use. Also teach the cost and latency of long prefill.
- *"Tokens ≈ words"* → teach BPE. Token counts differ by language (Indic and other non-Latin scripts often cost more tokens per word), by numbers and by code. This affects cost, limits and arithmetic or character-level failures such as spelling and counting letters. (Tokeniser-specific statistics were not collected this session; see Gaps.)
- *"The model remembers previous calls"* → teach statelessness. Memory is whatever you put back in the context, and provider prompt caching is a cost and latency feature, not memory.
- *"Price per token is the cost"* → teach hidden reasoning tokens and test-time compute. Measure cost per completed task.
- *"Fine-tuning adds knowledge"* → teach what SFT/LoRA change (behaviour, format, style) vs retrieval (facts). Huyen's resources cite "Fine-Tuning or Retrieval?" ([aie-book](https://github.com/chiphuyen/aie-book/blob/main/resources.md)).
- *"Bigger total parameters = slower or needs more GPU compute"* (MoE) → teach total vs active parameters. Memory scales with *total* parameters and per-token compute with *active* ones. For example, DeepSeek V4-Flash has 284B total but 13B active: it is cheap to compute but still needs memory for all 284B.
- *"The KV cache is small"* → teach the KV-cache memory formula. Concurrency × context length, not weights, often limits GPU capacity, which is why GQA, MLA and sparse attention exist.
- *"Reasoning traces are faithful explanations"* → treat chain-of-thought as a generation, not a verified explanation. No primary source was fetched this session; see Gaps.

### Gaps
- The original Thinking Machines and Chroma posts were not fetched. Exact figures (80 vs 1 unique completions, 18 models) come from secondary summaries.
- No source was collected on tokenisation-induced production bugs (multilingual token inflation, number tokenisation) or on CoT faithfulness research. Both deserve primary citations (for example Anthropic's work on reasoning faithfulness) before the book makes these claims.
- No survey of real production incidents attributable to LLM-internals misunderstandings was found. The list above is a practitioner synthesis.
