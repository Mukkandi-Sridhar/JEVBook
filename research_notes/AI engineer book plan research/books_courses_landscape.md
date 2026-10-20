# Landscape of Books and Courses on Applied AI Engineering / LLM Apps / Agentic AI (as of October 2026)

Research date: 2026-10-20. Method: about 18 web searches and fetches. Several key review pages (computingforgeeks.com, buildingagenticai.com, dev.to, newsletter.victordibia.com) failed to load with a DNS error in this environment, so the details below come from search-result summaries, not full-page reads. Search summaries can lose context, so treat single-source claims with care.

Labelling convention used below:
- **[Verified this session]**: came from a search result or page retrieved during this research.
- **[Prior knowledge, not re-verified]**: well-known publication facts from the researcher's background knowledge (cutoff mid-2026). They were NOT re-checked in this session. The writer should confirm them, or soften them, before treating them as fact.

---

## Q0. What exists, and what is each resource's scope, date, strengths and criticisms?

### Takeaway
The market has three layers:
1. A small "canon" of 2024–2025 foundation and production books. Chip Huyen's *AI Engineering* is the consensus number-one pick.
2. A fast-growing 2025–2026 wave of agent-specific books, many built around MCP, A2A or a framework.
3. A mostly free course layer: DeepLearning.AI, Kaggle/Google, Hugging Face and Anthropic/Claude Academy. Above it sit expensive cohort courses, Maven at around $4,200, and Indian programmes that are university-branded or YouTuber-led.

No single resource joins the dots from beginner to designer of agentic systems, end to end.

### Cited Findings — Books

**Chip Huyen, *AI Engineering: Building Applications with Foundation Models* (O'Reilly)**
- Called the top single pick in most 2026 roundups: "the most-cited production AI engineering book of 2026", "not framework-specific". It covers prompting, RAG, evaluation, fine-tuning, agents, and "the engineering judgment around each" — [KDnuggets 2026 roundup / computingforgeeks via search summary](https://computingforgeeks.com/best-llm-engineering-books/); [KDnuggets](https://www.kdnuggets.com/5-best-books-for-building-agentic-ai-systems-in-2026)
- Praise: "best technical introduction I've encountered to date" — [Mark Ferree Substack](https://markferree.substack.com/p/ai-engineering-book-review). Another reviewer says it "focuses on concepts rather than technologies which will soon change" — [Scott Pearson Substack](https://scottjpearson.substack.com/p/ai-engineering-building-applications)
- Criticisms (opinion): some chapters are dry, and the math-heavy sections needed supplementary reading — [Skybridge/NeoDB review](https://bridge.neodb.net/users/ryancowl.es/posts/ai-engineering-by-chip-huyen). Because it came out in early 2025, it "cannot cover the most recent updates" — [DEV Community review](https://dev.to/uponthesky/book-reviewai-engineering-by-chip-huyen-4e26). The author's own repo says it "might not be for everyone" because of its level of detail — [chiphuyen/aie-book via ecosyste.ms](https://awesome.ecosyste.ms/projects/github.com%2Fchiphuyen%2Faie-book)
- [Prior knowledge, not re-verified] Published in December 2024 / January 2025, about 530 pages. It has a companion GitHub repo (chiphuyen/aie-book) with resources, not a runnable end-to-end project. Agents get one chapter. It predates the mainstream adoption of MCP and A2A.

**Paul Iusztin & Maxime Labonne, *LLM Engineer's Handbook* (Packt)**
- Often ranked second, and "leans toward operations (MLOps, deployment, monitoring)". One review notes it "ends on MLOps principles with no agent chapter at all" — [computingforgeeks/KDnuggets via search summary](https://computingforgeeks.com/best-llm-engineering-books/)
- [Prior knowledge, not re-verified] Packt, October 2024, about 520 pages. Builds one end-to-end "LLM Twin" project on AWS/SageMaker, ZenML, Qdrant and Comet/Opik. Readers praise the end-to-end project. Common complaints are that it is cloud- and tool-heavy (AWS costs) and that the code goes stale.

**Jay Alammar & Maarten Grootendorst, *Hands-On Large Language Models* (O'Reilly)**
- Recommended as a visual, approachable foundation, "less about agents specifically, more about what is under them" — [computingforgeeks/KDnuggets via search summary](https://computingforgeeks.com/best-llm-engineering-books/)
- [Prior knowledge, not re-verified] September 2024, about 400 pages, around 300 custom illustrations, Colab notebooks repo. Strong on embeddings, classification, clustering, RAG and fine-tuning. Weak on production, evals and agents.

**Sebastian Raschka, *Build a Large Language Model (From Scratch)* (Manning) and follow-up**
- The follow-up *Build a Reasoning Model (From Scratch)* (Manning, ISBN 978-1-63343-467-7, about 440 pages, 8 chapters plus 7 appendices) covers inference-time scaling, self-refinement, RL/GRPO, distillation and verifier-based evaluation. Release dates conflict: Apple Books says June 30, 2026, a Taiwanese retailer says July 28, 2026, and Schweitzer says November 2, 2026 — [i-programmer](https://www.i-programmer.info/book-watch-archive/19064-build-a-reasoning-model-from-scratch-manning.html); [Schweitzer](https://www.schweitzer-online.de/en/buch/Raschka/Build-Reasoning-Model-From-Scratch/9781633434677/A76092441/); [Apple Books](https://books.apple.com/ca/book/build-a-reasoning-model-from-scratch/id6756786110)
- [Prior knowledge, not re-verified] The first book came out in September 2024, about 370 pages, with a very popular GitHub repo (LLMs-from-scratch). It is model-internals focused (PyTorch GPT-2 style), not application or agent engineering. It is widely praised for clarity.

**John Berryman & Albert Ziegler, *Prompt Engineering for LLMs* (O'Reilly)**
- [Prior knowledge, not re-verified] November 2024, about 280 pages, by GitHub Copilot engineers. Readers praise its "LLM as document completion" mental model and its Copilot case material. It is criticised as light on code and agents, and partly outdated now that reasoning models and "context engineering" have arrived. No review evidence was retrieved this session.

**Louis-François Bouchard et al. (Towards AI), *Building LLMs for Production***
- [Prior knowledge, not re-verified] Self-published through Towards AI in 2024 (2nd edition late 2024). Covers prompting, RAG, LangChain/LlamaIndex and fine-tuning. Heavy dependence on frameworks makes it vulnerable to API churn. No review evidence was retrieved this session.

**Micheal Lanham, *AI Agents in Action* (Manning)**
- The second edition is subtitled "Intelligent workflows with LLMs, MCP, A2A, and more". Manning lists June 2026, ISBN 9781633434530, 392 pages, for intermediate Python programmers. Amazon gives a paperback date of July 14, 2026 — [Manning](https://www.manning.com/books/ai-agents-in-action-second-edition); [Amazon](https://www.amazon.com/Agents-Action-Second-Intelligent-workflows/dp/1633434532)
- It "rewrote the 2025 first edition around the OpenAI Agents SDK and MCP". In other words, the first edition was overtaken within roughly a year — [computingforgeeks agents list via search summary](https://computingforgeeks.com/best-ai-agents-books/)

**Antonio Gulli, *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems* (Springer)**
- 427 pages. eBook October 30, 2025, softcover October 31, 2025. 21 patterns, one per chapter, each with overview, use cases, code and takeaways. Companion notebooks on GitHub. Royalties go to Save the Children — [Springer](https://link.springer.com/doi/10.1007/978-3-032-01402-3); [system-design.space review](https://system-design.space/en/chapter/agentic-design-patterns-book/)
- Praised for its sequencing, from a single governed LLM call to multi-agent systems — [system-design.space](https://system-design.space/en/chapter/agentic-design-patterns-book/)

**Valliappa Lakshmanan & Hannes Hapke, *Generative AI Design Patterns* (O'Reilly)**
- 32 patterns for problems such as hallucinations, nondeterminism and knowledge cutoffs. Each pattern has a problem statement, coded solution and trade-off discussion, and there is a companion GitHub code catalogue. The O'Reilly listing shows October 2025 and 508 pages. A German retailer lists a 370-page paperback, so page counts differ — [O'Reilly](https://www.oreilly.com/library/view/-/9798341622654/); [sourcepulse repo](https://www.sourcepulse.org/projects/20641724)
- No reader reviews were found this session.

**Anjanava Biswas & Wrick Talukdar, *Building Agentic AI Systems* (Packt)**
- Appears on several 2026 roundups. One reviewer calls it a must-read for agent architectures, orchestration and memory — [KDnuggets/computingforgeeks via search summary](https://www.kdnuggets.com/5-best-books-for-building-agentic-ai-systems-in-2026)

**Kyle Stratis, *AI Agents with MCP: Model Context Protocol for Building Clients, Servers, and End-to-End Agents* (O'Reilly)**
- Listed publication date October 20, 2026, 347 pages. Covers MCP but not A2A. The preface notes that the 2026-07-28 protocol version changed the protocol and its transport, an example of print content chasing a moving spec — [Amazon](https://www.amazon.com/AI-Agents-MCP-End-End/dp/B0FYCBVGX7)

**Hur & Song, *Build an AI Agent (From Scratch)* (Manning)**
- Listed on O'Reilly as July 2026. A video edition has a chapter titled "MCP: Standardizing tools" — [O'Reilly video](https://www.oreilly.com/videos/build-an-ai/9781633434615VE/9781633434615VE-byfla_c34/)

**Other 2026 roundups**
- Several Javarevisited/Medium "I read 20+ books" lists (April, May and September 2026) exist. They are affiliate-style, so treat them as opinion — [Javarevisited Sept 2026](https://javarevisited.wordpress.com/2026/09/14/i-read-20-books-on-ai-engineering-and-llms-here-are-my-top-5-recommendations-for-2026/); [Javarevisited Apr 2026](https://javarevisited.wordpress.com/2026/04/13/the-ai-and-llm-engineers-reading-list-for-2026-10-books-that-matter/)
- A dev.to post compares "Gulli vs Lanham vs Huyen" for 2026 agentic AI books. It was not fetchable here — [dev.to](https://dev.to/shaam_ai/agentic-ai-books-2026-gulli-vs-lanham-vs-huyen-2idj)
- [Prior knowledge, not re-verified] Victor Dibia (Microsoft AutoGen) wrote *Designing Multi-Agent Systems* (2025, self-published/Manning-adjacent) and runs a yearly "top agent books" newsletter. Other titles: *Learning LangChain* (Oshin & Campos, O'Reilly 2025), *LLM Agents in Action*, and Packt titles on LangGraph, CrewAI and AutoGen.

### Cited Findings — Courses

**DeepLearning.AI, *Agentic AI* (Andrew Ng)**
- Self-paced and intermediate. About 10 hours, 31 video lessons, 7 code examples and 8 graded assignments per the DLAI page. Coursera lists it as 2 weeks × 10 hours with 5 assignments. Focus: reflection, tool use, planning, multi-agent workflows, and evals/error analysis — [DeepLearning.AI](https://deeplearning.ai/courses/agentic-ai/); [Coursera](https://www.coursera.org/learn/dlai-agentic-ai)
- Pricing: free to audit the videos. Labs and the certificate need DLAI Pro, which a third party reports at about $30/month or $25/month annually (not verified on the official site) — [hermes-agent review](https://hermes-agent.ai/blog/deeplearning-ai-agentic-ai-review)
- Criticisms (third party, opinion): "limited production-engineering depth", "heavily scaffolded assessments", and learner reports of shared API quota failures that blocked labs. The first module is slow — [hermes-agent review](https://hermes-agent.ai/blog/deeplearning-ai-agentic-ai-review); [learner GitHub](https://github.com/nhatnam2609/agentic_ai_andrew)
- [Prior knowledge, not re-verified] DLAI also hosts 80+ free 1-hour short courses, many co-branded with vendors (LangChain, CrewAI, Anthropic MCP, etc.). They are good for single topics but fragmented, and each tends to be vendor-tied.

**Kaggle + Google, *5-Day AI Agents Intensive***
- The live run was in November 2025 and was later turned into a self-paced Kaggle Learn Guide. A refreshed run themed on vibe coding ran in June 2026 with a capstone. Each day pairs a whitepaper with Gemini + Agent Development Kit (ADK) codelabs — [KDnuggets](https://www.kdnuggets.com/kaggle-googles-free-5-day-agentic-ai-course); [AIWeekly](https://aiweekly.co/learning-ai/generative-ai/learn-ai-agents)
- Days: agent introduction; tools and MCP; context engineering (sessions and memory); agent quality (evals/observability); prototype to production — [DEV learner write-up](https://dev.to/rutuja_yadav/5-day-ai-agents-intensive-course-google-x-kaggle-1fhj)
- [Prior knowledge, not re-verified] It was preceded by a 5-day GenAI Intensive (November 2024 and March/April 2025) covering foundation models, embeddings, agents, domain LLMs and MLOps. Very large enrolments were reported (hundreds of thousands).

**Hugging Face courses**
- Certificates are free and verifiable, and the early steps need no coding — [AIWeekly](https://aiweekly.co/learning-ai/generative-ai/learn-ai-agents)
- [Prior knowledge, not re-verified] The Agents Course launched in February 2025, covering smolagents, LlamaIndex, LangGraph, a GAIA-benchmark final unit and a certificate. A separate MCP course (with Anthropic) came in mid-2025. The LLM Course is a refresh of the older NLP course. All are free. Common learner complaints are buggy notebooks and space/runtime issues.

**Anthropic Academy, now Claude Academy**
- Hosted on Skilljar. No account or subscription is needed, and all courses and certificates are free. 17 courses as of April 2026. A rename to "Claude Academy" was announced in August 2026, reorganised around five products, with a reported 26 courses (secondary source). It has an MCP track (intro and advanced). English only — [pasqualepillitteri.it Apr 2026](https://pasqualepillitteri.it/en/news/371/anthropic-academy-free-courses-claude); [pasqualepillitteri.it Aug 2026](https://pasqualepillitteri.it/en/news/12081/claude-academy-live-free-courses-learn-claude); [fast.io guide](https://fast.io/resources/claude-ai-courses-guide/)

**Maven: Hamel Husain & Shreya Shankar, *AI Evals for Engineers & PMs***
- Live cohort from October 10 to November 21, 2026 at $4,200 list. A 25% promotion is sometimes offered, and another listing shows $5,000 → $3,750. The 4-week cohort runs at about 3–5 hours/week and includes lifetime recordings. It covers error analysis, synthetic data, LLM-as-judge, RAG debugging and CI/CD for AI — [techinterview.org directory](https://www.techinterview.org/bootcamp_directory/p/maven-ai-engineering-cohorts/); [Beri review](https://www.beri.net/learning/maven-ai-evals-for-engineers-and-pms); [Product Compass](https://www.productcompass.pm/p/best-ai-product-management-courses)
- An older price of $1,995 appears on a stale listing. The original Husain/Becker "Mastering LLMs" course is retired to a $20 recorded archive — [aiagentrank](https://aiagentrank.io/learn/course/maven-llm-evaluation-hamel)

**Other paid bootcamps**
- Data Science Dojo Agentic AI Bootcamp: $2,499, regularly $2,999 — [DSD help center](https://help.datasciencedojo.com/what-is-the-price-of-the-agentic-ai-bootcamp)

**Indian programmes**
- IIT Kharagpur online Executive PG Certificate in Generative and Agentic AI, marketed to freshers and to 2+ year professionals — [IIT KGP online](https://online.iitkgp.ac.in/blog/best-generative-agentic-ai-course-in-india)
- IITM Pravartak agentic AI certificate covers AI engineering, RAG, no-code and code workflows, and deployable agents. IIT Roorkee also has a GenAI + agentic programme. Intellipaat is noted for live training — [Futurense guide](https://futurense.com/blog/best-agentic-ai-courses-in-india)
- Caveat from an Indian guide: "course quality varies significantly — some focus on genuine agent development while others largely repackage prompt engineering" — [Futurense](https://futurense.com/blog/best-agentic-ai-courses-in-india)
- Krish Naik's site lists a "3.0 Agentic AI Specialisation with AgentOps" running 5 months. No fee was found — [krishnaik.in](https://www.krishnaik.in/)
- The Indian course market found in search is dominated by provider and marketing blogs, not community reviews — [Futurense](https://futurense.com/blog/best-agentic-ai-courses-in-india); [TechnoGeeks dev.to](https://dev.to/technogeekscspuneindia/best-generative-ai-and-agentic-ai-course-in-pune-developer-friendly-overview-2moh)

**Free canonical web resources**
- Anthropic's "Building Effective Agents" post is called "the single best short piece on patterns". Free resources are often more current than print — [computingforgeeks/KDnuggets via search summary](https://computingforgeeks.com/best-ai-agents-books/)

### Inferences
- Huyen is the conceptual anchor everyone recommends. Agents get a single chapter, and the book predates MCP, A2A and context engineering as named practices. A new book can position itself as "the practical sequel/companion for the agentic era", not as a competitor.
- The agent-book wave splits into pattern catalogues (Gulli, Lakshmanan & Hapke), protocol books (Stratis on MCP, Lanham 2e on MCP/A2A) and from-scratch builds (Hur & Song, Raschka). None of the evidence found shows a beginner-to-practitioner path with one end-to-end system and a decision or judgement layer.
- Courses are short and free for breadth (DLAI, Kaggle, Hugging Face, Claude Academy) or very expensive for depth (Maven at $4,200). There is a price gap between a ₹500–₹1,500 book and a $4,200 cohort.

### Gaps
- Amazon star ratings and review counts were not retrieved for any title, because Amazon pages were not fetched.
- No Reddit or Hacker News threads were surfaced by search for these specific books, despite targeted queries.
- Specific content of Full Stack Deep Learning's LLM Bootcamp: [Prior knowledge, not re-verified] it ran in spring 2023, with free videos still online, and is now dated (pre-agents, pre-MCP). It was not re-checked this session.
- OpenAI Cookbook and the roadmap.sh AI Engineer roadmap were not fetched this session.
- Fees for Indian platforms (Krish Naik, Analytics Vidhya, Scaler, upGrad, Great Learning) were not found.

---

## Q1. Which topics are well covered by existing resources, and which are poorly covered or missing?

### Takeaway
Basic patterns are heavily covered: prompting, RAG, fine-tuning, LLM internals, and the textbook agent patterns of reflection, tool use, planning and multi-agent. Coverage is thin or scattered for:
- context engineering, which appears in the Kaggle course and not in the canon books
- agent-specific evals, which sit behind a $4,200 Maven course
- MCP/A2A, which have just reached print and are already shifting
- security
- cost engineering
- the decision/calibration layer (when not to use an LLM or agent)
- end-to-end system design taken from beginner level up
- Indian context: none was found

### Cited Findings
- **Well covered — foundations and RAG/fine-tuning:** Huyen covers "prompting, RAG, evaluation, fine-tuning, agents" — [computingforgeeks](https://computingforgeeks.com/best-llm-engineering-books/). Alammar & Grootendorst cover "what is under" agents — [same](https://computingforgeeks.com/best-llm-engineering-books/). Raschka covers model internals and now reasoning/RL — [i-programmer](https://www.i-programmer.info/book-watch-archive/19064-build-a-reasoning-model-from-scratch-manning.html)
- **Well covered — agent patterns:** Ng's course covers reflection, tool use, planning and multi-agent — [DeepLearning.AI](https://deeplearning.ai/courses/agentic-ai/). Gulli has 21 patterns — [Springer](https://link.springer.com/doi/10.1007/978-3-032-01402-3). Lakshmanan & Hapke have 32 patterns — [O'Reilly](https://www.oreilly.com/library/view/-/9798341622654/)
- **MCP/A2A — now arriving but unstable:** Lanham 2e (June/July 2026) covers MCP and A2A — [Manning](https://www.manning.com/books/ai-agents-in-action-second-edition). Stratis (October 2026) covers MCP only, and notes that the 2026-07-28 spec changed transports — [Amazon](https://www.amazon.com/AI-Agents-MCP-End-End/dp/B0FYCBVGX7). The Kaggle course covers MCP on Day 2 — [KDnuggets](https://www.kdnuggets.com/kaggle-googles-free-5-day-agentic-ai-course). Claude Academy has an MCP track — [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/371/anthropic-academy-free-courses-claude)
- **Context engineering:** taught as a named topic in the Kaggle/Google intensive (sessions and memory) — [DEV write-up](https://dev.to/rutuja_yadav/5-day-ai-agents-intensive-course-google-x-kaggle-1fhj). None of the book descriptions retrieved this session lists it as a chapter (absence of evidence, not proof).
- **Evals:** the deepest offering is a paid cohort ($4,200) — [Beri](https://www.beri.net/learning/maven-ai-evals-for-engineers-and-pms). Ng's course includes evals and error analysis but is "limited production-engineering depth" — [hermes-agent](https://hermes-agent.ai/blog/deeplearning-ai-agentic-ai-review). The *LLM Engineer's Handbook* has "no agent chapter at all" — [computingforgeeks](https://computingforgeeks.com/best-llm-engineering-books/)
- **Production and ops:** covered by the *LLM Engineer's Handbook* (MLOps, deployment, monitoring) and by Kaggle Day 5 (prototype to production) — [computingforgeeks](https://computingforgeeks.com/best-llm-engineering-books/); [DEV](https://dev.to/rutuja_yadav/5-day-ai-agents-intensive-course-google-x-kaggle-1fhj)
- **Indian quality issue:** many Indian courses "largely repackage prompt engineering" — [Futurense](https://futurense.com/blog/best-agentic-ai-courses-in-india)

### Inferences
- The clearest openings for the new book:
  - **(a) A decision/calibration layer:** whether to use an LLM at all, agent vs. workflow vs. plain code, confidence and abstention. It barely appears in any table of contents found.
  - **(b) Agent evals at book price.**
  - **(c) Security for agents:** prompt injection, tool permissions, MCP server trust.
  - **(d) Cost and latency budgeting**, especially for Indian-scale, price-sensitive deployments in INR, with cheaper and open models.
  - **(e) One end-to-end system carried through the whole book**, starting from beginner level.
  - **(f) Indian context:** Indic languages, UPI/ONDC/IndiaStack-style integrations, the DPDP Act on data protection, and Indian hiring and interview expectations.
- Write protocol (MCP/A2A) chapters at the concept level with a versioned appendix, because specs change within months (Stratis preface).

### Gaps
- No source was found that explicitly audits security or cost coverage across books. The "missing" claims for those topics rest on the absence of evidence in the retrieved descriptions.
- No book or course was found that covers Indian context (Indic NLP, DPDP Act, Indian deployment economics) for LLM apps. This search did not specifically target, for example, AI4Bharat/Sarvam tutorials.

---

## Q2. What do readers complain about?

### Takeaway
The dominant complaints:
- **Code goes stale fast**, especially LangChain or framework-tied books and courses.
- **Too dense or academic** in places (Huyen).
- **Not current** with the latest protocols and models.
- **Too scaffolded or shallow** for production (DLAI).
- **Variable quality and marketing-driven** (Indian courses).

No direct evidence was found of a "US-centric" complaint. That remains an inference.

### Cited Findings
- *Learning LangChain* (Goodreads): "concepts solid but code outdated". The companion GitHub code was refreshed but "already out of date again". "Dynamic publishing was solved several years ago" — [Goodreads](https://www.goodreads.com/book/show/220306097-learning-langchain)
- Course reviews report deprecated calls (`predict()` → `invoke()`) and courses stuck on LangChain 0.2.x when 0.3.x was current — [Coursera/Packt LangChain course reviews](https://www.coursera.org/programs/computational-data-sciences-learning-program-qop5d/learn/packt-the-complete-langchain-llms-guide-ep8du/reviews)
- Victor Dibia excluded framework-specific books (LangChain, CrewAI) from his 2025 list because their APIs "change frequently enough that printed content dates quickly" — [Dibia newsletter, via search summary](https://newsletter.victordibia.com/p/top-books-on-ai-agents-in-2025)
- Writers of LangChain-tied content describe breaking changes that made their content obsolete almost immediately — [Medium](https://shashankguda.medium.com/challenges-criticisms-of-langchain-b26afcef94e7)
- Huyen: some chapters are dry, and the math-heavy sections needed outside reading — [Skybridge](https://bridge.neodb.net/users/ryancowl.es/posts/ai-engineering-by-chip-huyen). It can't cover recent updates — [DEV](https://dev.to/uponthesky/book-reviewai-engineering-by-chip-huyen-4e26)
- DLAI Agentic AI: scaffolded assessments, little production depth, and lab API quota failures — [hermes-agent](https://hermes-agent.ai/blog/deeplearning-ai-agentic-ai-review)
- Agent-specific books "age fastest". Free resources such as Anthropic's "Building Effective Agents" are often more current — [computingforgeeks via search summary](https://computingforgeeks.com/best-ai-agents-books/)
- Indian courses: quality varies, and some are prompt-engineering repackaged — [Futurense](https://futurense.com/blog/best-agentic-ai-courses-in-india)

### Inferences
- Readers reward books that teach durable concepts and judgement, with code kept separately in a maintained repo. Huyen is praised precisely for "concepts rather than technologies".
- "US-centric" is a plausible complaint for Indian readers: AWS-centred stacks, dollar costs, English-only examples. But no review text saying this was found.

### Gaps
- Amazon and Reddit review text was not retrieved. Complaint frequencies (for example, the share of 1–2 star reviews citing outdated code) are unknown.

---

## Q3. What formats and structures do successful books in this space use?

### Takeaway
The successful patterns:
- A companion GitHub repo, almost universal: notebooks per chapter or a code catalogue.
- Either a single running end-to-end project (*LLM Engineer's Handbook*, Raschka) or a pattern-per-chapter catalogue (Gulli: overview → use cases → code → takeaways; Lakshmanan & Hapke: problem → solution → trade-offs).
- Visual explanation (Alammar).

Courses add a capstone, certificates and whitepapers.

### Cited Findings
- Gulli: one pattern per chapter (overview, use cases, code, takeaways). GitHub notebooks per chapter. About 63 illustrations — [Springer](https://link.springer.com/doi/10.1007/978-3-032-01402-3); [system-design.space](https://system-design.space/en/chapter/agentic-design-patterns-book/)
- Lakshmanan & Hapke: problem statement, coded solution and trade-offs per pattern, plus a Python code catalogue repo — [O'Reilly](https://www.oreilly.com/library/view/-/9798341622654/)
- Raschka (reasoning book): chapters build step by step on one model, with 7 substantial appendices — [i-programmer](https://www.i-programmer.info/book-watch-archive/19064-build-a-reasoning-model-from-scratch-manning.html)
- Kaggle intensive: whitepaper + codelab per day, plus a capstone in the 2026 run — [KDnuggets](https://www.kdnuggets.com/kaggle-googles-free-5-day-agentic-ai-course)
- DLAI: video lessons + code examples + graded labs + certificate — [DeepLearning.AI](https://deeplearning.ai/courses/agentic-ai/)
- Maven: live cohort, recordings, lifetime access — [Beri](https://www.beri.net/learning/maven-ai-evals-for-engineers-and-pms)
- Huyen: a companion repo with resources, plus a framework-neutral, concept-first structure — [aie-book](https://awesome.ecosyste.ms/projects/github.com%2Fchiphuyen%2Faie-book)
- Audiobook editions are now produced even for code books (Raschka's reasoning book, narrated by Lisa Farina) — [Audible UK](https://www.audible.co.uk/pd/B0HKQ7319D)

### Inferences
- A hybrid structure fits the gaps found:
  - concept chapters, each with a "decision checklist"
  - one running project that grows across the book
  - a pattern catalogue in the appendix
  - a maintained repo pinned to versions, with a changelog
- Exercises and interview-style questions would suit the Indian audience, where courses are bought for job outcomes.

### Gaps
- No data was found on which format sells best, such as sales figures or bestseller ranks.

---

## Q4. What price points and lengths are typical, how fast do these go out of date, and how do authors handle updates?

### Takeaway
Lengths:
- Mainstream titles: 350–530 pages. Confirmed: 347 (Stratis), 392 (Lanham 2e), 427 (Gulli), 440 (Raschka reasoning), 508 (Lakshmanan & Hapke).
- Courses: free (DLAI audit, Kaggle, Hugging Face, Claude Academy) to around $2,500–$4,200 (DSD, Maven).

Shelf life:
- Agent and framework content goes stale in months. The first edition of Lanham's *AI Agents in Action* (2025) was rewritten as a second edition by mid-2026, and MCP books face spec changes within months.

How authors cope:
- New editions (Lanham), refreshed GitHub repos (which readers say still lag), and refreshed course runs (Kaggle June 2026).

### Cited Findings
- Page counts: Stratis 347 — [Amazon](https://www.amazon.com/AI-Agents-MCP-End-End/dp/B0FYCBVGX7). Lanham 2e 392 — [Manning](https://www.manning.com/books/ai-agents-in-action-second-edition). Gulli 427 — [Springer](https://link.springer.com/doi/10.1007/978-3-032-01402-3). Raschka reasoning 440 — [Schweitzer](https://www.schweitzer-online.de/en/buch/Raschka/Build-Reasoning-Model-From-Scratch/9781633434677/A76092441/). Lakshmanan & Hapke 508 (O'Reilly) vs. 370 (a retailer) — [O'Reilly](https://www.oreilly.com/library/view/-/9798341622654/)
- Update cycle: Lanham's first edition (2025) was rewritten around the OpenAI Agents SDK + MCP as a second edition in 2026 — [computingforgeeks via search summary](https://computingforgeeks.com/best-ai-agents-books/); [Manning](https://www.manning.com/books/ai-agents-in-action-second-edition)
- The MCP spec version of 2026-07-28 changed transports, as noted in an October 2026 book preface — [Amazon](https://www.amazon.com/AI-Agents-MCP-End-End/dp/B0FYCBVGX7)
- Repos are refreshed but still lag — [Goodreads Learning LangChain](https://www.goodreads.com/book/show/220306097-learning-langchain)
- Courses re-run with new themes: Kaggle November 2025 → June 2026 vibe-coding run — [KDnuggets](https://www.kdnuggets.com/kaggle-googles-free-5-day-agentic-ai-course). Claude Academy grew from 13 to 17 to a reported 26 courses within 2026 and was renamed — [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/12081/claude-academy-live-free-courses-learn-claude)
- Course prices: Maven evals $4,200 — [techinterview.org](https://www.techinterview.org/bootcamp_directory/p/maven-ai-engineering-cohorts/). DSD $2,499–$2,999 — [DSD](https://help.datasciencedojo.com/what-is-the-price-of-the-agentic-ai-bootcamp). DLAI Pro about $25–30/month (third party) — [hermes-agent](https://hermes-agent.ai/blog/deeplearning-ai-agentic-ai-review). Claude Academy free — [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/371/anthropic-academy-free-courses-claude)
- Free alternatives compete with print on currency — [computingforgeeks via search summary](https://computingforgeeks.com/best-ai-agents-books/)

### Inferences
- A practical shelf-life planning number: framework-specific code goes stale in 6–12 months, protocol details in 3–6 months, and concepts and judgement in 2–4 years. (This is an inference from the cases above, not a measured statistic.)
- Ways a new book can handle updates:
  - keep framework code out of the printed text, using plain SDK calls or pseudocode
  - pin versions in the repo and keep a CHANGELOG
  - publish an "errata and updates" page
  - plan a yearly ebook refresh, which is easy with print-on-demand and self-publishing
- An India-priced edition can undercut all paid courses.

### Gaps
- Book prices were not retrieved this session. [Prior knowledge, not re-verified] Typical US list prices are $50–80 for O'Reilly and Manning print, and Packt ebooks often sell for $30–50 with frequent discounts. Indian reprints (Shroff/O'Reilly India, Packt India, Manning via Dreamtech/Wiley India) often sell for roughly ₹1,000–₹2,500. Confirm these on Amazon.in before citing.
- Indian course fees (IIT executive programmes, Krish Naik, Analytics Vidhya, Scaler) were not found. They need direct checks.
- No sales or bestseller-rank data was found for any title.
