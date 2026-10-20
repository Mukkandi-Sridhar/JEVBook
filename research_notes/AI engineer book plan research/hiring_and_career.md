# Hiring and Careers for AI Engineers (applied AI / LLM / agentic), state as of October 2026

Research method note: these notes are from web searches run on 2026-10-20. Direct page fetches failed in this environment (the egress proxy blocked latent.space, levels.fyi, axialsearch.com, 365datascience.com, prachub.com). So most findings below come from search-engine summaries of the linked pages, not full reads. Figures should be re-checked against the primary page before printing. Where a source is a vendor, training company or SEO blog, it is marked as such.

## Q0. What is an "AI engineer"? (role definition vs ML engineer, data scientist, software engineer)

### Takeaway
An AI engineer is a software engineer who builds products on top of pre-trained foundation models (APIs or open weights). The work covers prompting, RAG, tool use and agents, evals, and production concerns such as cost, latency and safety. An ML engineer mostly trains and serves the model; a data scientist mostly analyses and models data. swyx's framing is that the ML engineer's job ends where inference is served and the AI engineer's job begins there. The line is "dotted", not hard.

### Cited Findings
- swyx (Shawn Wang) wrote the essay "The Rise of the AI Engineer" (Latent Space, June 2023). It "quickly went viral" and is widely credited with naming the role — [Scrimba podcast #146](https://podcast.scrimba.com/146); original essay at [latent.space/p/ai-engineer](https://www.latent.space/p/ai-engineer) (could not be fetched; not quoted directly here).
- Summary of swyx's talk: the ML engineer's job stops when they serve inference, and the AI engineer's job begins with inference. The boundary is a dotted line, so the roles overlap — [GitNation, "The Rise of the AI Engineer"](https://gitnation.com/contents/the-rise-of-the-ai-engineer).
- AI engineers integrate models into apps and systems through APIs and handle practical implementation and user-facing aspects. ML engineers focus on building and training models — [GitNation](https://gitnation.com/contents/the-rise-of-the-ai-engineer).
- Humanloop interview with swyx: the AI engineer sits between traditional ML engineering and product development. They work with pre-trained models and APIs and value fast iteration and product integration over deep mathematical optimisation. swyx proposes about 4 AI engineers per 1 ML engineer — [Humanloop, "What is an AI Engineer"](https://humanloop.com/blog/what-is-an-AI-Engineer).
- swyx's own updated definition of the role (2025 interview) — [RedMonk, July 23, 2025](https://redmonk.com/blog/2025/07/23/shawn-swyx-wang-ai-engineer/).
- LinkedIn named "AI Engineer" the fastest-growing job title (US, and for young workers two years running). The reported underlying figure is about 75,000 US AI engineer postings in 2023–2025, out of 639,000 AI-related postings — [Collab365 summary of LinkedIn](https://spaces.collab365.com/posts/ai-engineer-becomes-fastest-growing-job-title-for--stl1Bj); [Let's Data Science](https://letsdatascience.com/news/linkedin-identifies-ai-engineer-as-fastest-growing-role-e82f85f1). (These are secondary summaries.)

### Inferences
- For the book, a working role split:
  - **Software engineer**: builds deterministic systems.
  - **Data scientist**: analysis, experiments, classical models.
  - **ML engineer**: training, fine-tuning, model serving and MLOps.
  - **AI engineer**: product systems around foundation models (prompts, RAG, tools, agents, evals, guardrails, cost and latency).
- In practice, job titles blur. Indian IT services firms often use "GenAI Engineer", "AI/ML GenAI Engineer" or "Python GenAI Engineer" for the same role — see the Infosys titles on [NodeFlair](https://nodeflair.com/jobs/infosys-python-genai-engineer-503324).

### Gaps
- Could not fetch swyx's original essay to quote exact wording or his "1 to 2 orders of magnitude more AI engineers than ML engineers" prediction. Verify the wording at the original URL before quoting.

## Q1. What skills and tools appear most often in AI engineer job postings (2025–2026), globally and in India?

### Takeaway
Globally (mostly US data), Python is near-universal (62–71% of AI engineer postings). Cloud (AWS/Azure/GCP) and foundation-model or LLM experience come next, followed by RAG, vector databases, agents and evaluation. In India, postings stress the same stack: Python, LLM apps, RAG, vector DBs, MLOps and cloud. They also lean on backend skills (FastAPI, databases) and, at IT services firms, Azure OpenAI. Employers want breadth across the stack and production experience over research-only profiles.

### Cited Findings
**Global / US**
- Axial Search analysed 43,480 US postings. Python appears in 62% of AI engineering postings, cloud platforms in 55% and foundation models in 51%. Employers favour engineers who span the stack over single-tool specialists — [Axial Search, "AI Engineering Jobs in 2026: A Data-Backed Market Map"](https://axialsearch.com/insights/ai-engineering-jobs) (search summary; the page could not be fetched). Two Axial pages give slightly different sector shares (28% vs 29% professional services).
- 365 Data Science studied about 900 (903) US Glassdoor AI engineer postings:
  - Python 71%, Java 22%, AWS 32.9%, Azure 26%.
  - Only 2.5% of roles target 0–2 years of experience.
  - 48.6% accept a Master's or Bachelor's degree.
  - Source: [365 Data Science, "AI Engineer Job Outlook 2026"](https://365datascience.com/career-advice/career-guides/ai-engineer-job-outlook-2025/).
- Dice analysis of about 7M US tech listings: AI skills appear in 73% of tech job postings in 2026, up from 15% in January 2024 — [Metaintro summary](https://www.metaintro.com/blog/ai-skills-73-percent-tech-job-postings-2026). (Secondary summary; the 73% likely counts any AI mention, not AI engineer roles only.)
- Stanford AI Index 2026 (Lightcast data): AI skills appear in about 2.5% of all US job postings in 2025, up about 55% year on year. California has about 17% of US AI postings — [Lightcast, "Four Takeaways from the 2026 Stanford AI Index"](https://lightcast.io/resources/blog/stanford-ai-2026). Note that this conflicts in scale with the Dice 73% figure, because Dice measures tech postings only and uses a broader definition.
- LinkedIn: "AI engineering" and "prompting / model tuning" are among the fastest-growing skills in 2026 — [Interview Query summary of LinkedIn](https://interviewquery.com/p/linkedin-ai-engineering-fastest-growing-skills-2026).
- Skills hiring guides commonly list LLM API integration, RAG and vector databases — [Lucent Innovation (vendor)](https://www.lucentinnovation.com/resources/technology-posts/how-to-hire-ai-developers).

**India**
- Coverage of Naukri JobSpeak (mid-2026) lists Python, LLM apps, RAG, vector databases and MLOps as in-demand. Production-ready profiles are preferred over research-only ones — [CareerIndia, "GenAI Hiring Surge… 2026"](https://www.careerindia.com/news/genai-hiring-surge-india-2026-top-skills-salary-packages-cities-011-65139.html) (secondary, SEO-style).
- Infosys AI engineer interviews probe RAG vs fine-tuning, reranking, FastAPI concurrency and database indexing. This shows that backend engineering is expected alongside LLM skills — [Interview Query, Infosys AI Engineer guide](https://www.interviewquery.com/guides/infosys-ai-engineer).
- Infosys posts roles titled "AI, ML GEN AI Engineer" and "Python GenAI Engineer" — [NodeFlair listing 1](https://nodeflair.com/jobs/infosys-ai-ml-gen-ai-engineer-503144), [listing 2](https://nodeflair.com/jobs/infosys-python-genai-engineer-503324).
- CIEL HR (2026): demand for agentic AI engineers in India grew 260% year on year, LLM engineers 86.5% and MLOps engineers 82.2% — [Outlook Business](https://www.outlookbusiness.com/news/demand-for-agentic-ai-talent-rises-260-as-enterprises-embrace-ai-report); [People Matters](https://www.peoplematters.in/amp/news/ai-and-emerging-tech/demand-for-agentic-ai-talent-rises-260-pc-as-enterprises-embrace-ai-report-51991).
- City spread: Bengaluru is the volume leader. Hyderabad (and Vijayawada) show faster percentage growth — [Let's Data Science, "Bengaluru Anchors India AI Hiring"](https://letsdatascience.com/news/bengaluru-anchors-india-ai-hiring-as-cities-expand-opportuni-37af2ef1). July 2026 figures quoted in secondary coverage:
  - Bengaluru: about 27,840 tech openings.
  - Pune: about 11,050.
  - Hyderabad: +16% YoY white-collar hiring.
  - Source: [CareerIndia](https://www.careerindia.com/news/ai-jobs-india-2026-top-paying-roles-salary-trends-011-64983.html). The figures conflict across CareerIndia pages, so treat them as indicative.

### Inferences
- A skills list for the book that is consistent across sources:
  - Python (plus one backend framework such as FastAPI).
  - LLM APIs (OpenAI, Anthropic, Gemini, Azure OpenAI, Bedrock).
  - Prompt and context design.
  - RAG: chunking, embeddings, hybrid search, reranking, vector DBs.
  - Agents and tool calling.
  - Evals.
  - Cloud (Azure dominates Indian IT services because of Azure OpenAI; AWS/GCP at product firms).
  - Docker and CI/CD.
  - Observability and tracing; cost and latency management.
  - Guardrails and safety.
- Fine-tuning (LoRA etc.) appears as a "nice to have" more often than a core requirement for applied roles. The evidence is indirect: RAG-vs-fine-tune tradeoff questions are common, but the postings summarised do not list fine-tuning near the top.
- Experienced roles dominate. The 2.5% entry-level share (365 Data Science) suggests freshers usually enter through SWE or data roles, or through services-firm GenAI tracks.

### Gaps
- No primary frequency data was found for specific frameworks (LangChain, LangGraph, LlamaIndex, DSPy, MCP) in 2026 postings. No India-specific posting-level skill percentages from Naukri or LinkedIn were found either; only secondary prose summaries.

## Q2. What do interview loops look like (product companies, startups, Indian IT services), and what are the common questions?

### Takeaway
Product companies and startups typically run: recruiter screen, coding (DSA or practical), an LLM/ML concepts round, an AI system design round (RAG, agent or chatbot), often a take-home or practical project judged on accuracy and robustness, and a behavioural round. Indian IT services firms (Infosys, Wipro) run about 4 rounds: aptitude or technical test, technical interview(s) centred on your own project, HR, and sometimes a client round. The questions concentrate on RAG mechanics, hallucination handling, vector DBs, chunking, RAG vs fine-tuning, and transformer basics. Classic ML (CNNs, gradient descent) is now a minority, roughly a quarter, of technical content.

### Cited Findings
**General loop structure**
- Typical applied AI engineer stages are: recruiter screen, coding interview, AI/ML round, system design, practical project, and behavioural. Take-homes commonly cover retrieval, agents and tool use — [Nora, Applied AI Engineer Interview Guide 2026](https://interview.norahq.com/interview-guides/applied-ai-engineer-interview-questions-guide-2026).
- Classic ML questions (CNNs, gradient descent) now make up "maybe 25%" of technical rounds. The rest covers RAG, evaluation, prompt engineering and multi-agent design — [search summary of 2026 interview guides (Careery / Pensero / DataCamp)](https://careery.pro/blog/ai-careers/ai-engineer-interview-questions). This is a guide-writer's estimate, not measured data.
- Interviews test whether you can build and serve an LLM product: inference batching, RAG, agent design, cost and token budgets, and evaluation — [PracHub, "AI Engineer Interview Questions 2026"](https://prachub.com/resources/ai-engineer-interview-questions-2026-rag-agents-evals-and-production-systems). PracHub says its records are practice material, not leaked questions.
- Exponent says its AI engineer questions are drawn from real interviews reported by candidates at major labs — [Exponent](https://www.tryexponent.com/blog/ai-engineer-interview-questions).
- Strong answers define success, isolate failure modes, propose evidence, and say what should happen when the AI system is wrong — [Pensero, 2026 guide](https://pensero.ai/blog/ai-engineer-interview-questions).

**System design prompts seen across guides**
- Design a chatbot. Expected components: conversation memory, prompt orchestration, output validation, logging, rate limiting and cost tracking — [DataCamp](https://www.datacamp.com/blog/ai-engineer-interview-questions); [Exponent](https://www.tryexponent.com/blog/ai-engineer-interview-questions).
- Design a document search system using embeddings, or a RAG pipeline — same sources.
- Explain tool calling and multi-step agents. Debug retrieval or tool traces — [KodeKloud](https://kodekloud.com/blog/ai-interview-questions/); [PracHub](https://prachub.com/resources/ai-engineer-interview-questions-2026-rag-agents-evals-and-production-systems).
- Company-specific (Dataford guides): fine-tuning vs RAG tradeoffs, and how to minimise hallucinations in an LLM app — [Dataford, Techolution AI Engineer](https://dataford.io/interview-guides/techolution/ai-engineer); [Dataford, Aivar](https://dataford.io/interview-guides/aivar/ai-engineer).

**Take-homes (startups)**
- Startup hiring guide (2026): give the candidate a dataset of model outputs and ask them to write an evaluation harness. It warns against hiring someone who has "only called the API" — [Recruiting From Scratch, "How to hire an LLM AI engineer at a startup (2026)"](https://www.recruitingfromscratch.com/blog/how-to-hire-an-llm-ai-engineer-at-a-startup-2026).
- Tomoro AI (UK consultancy, Glassdoor reports):
  - Take-home: build a chatbot answering questions over financial documents, judged on LLM accuracy.
  - Also an LLM theory round and a live "LLM orchestration" coding challenge.
  - One candidate said brittle implementations are heavily penalised, so submit safe, reliable work over ambitious work.
  - Sources: [Glassdoor review 1](https://www.glassdoor.com.mx/Entrevista/Tomoro-AI-Entrevista-E9743971-RVW98089904.htm), [review 2](https://www.glassdoor.com.mx/Entrevista/Tomoro-AI-Entrevista-E9743971-RVW104722468.htm). These are anecdotal.
- Some employers use a proctored 1-hour live challenge with Google allowed and no AI assistants — [Djinni AI Engineer posting](https://djinni.co/jobs/767669-ai-engineer).

**Indian IT services**
- Infosys AI engineer: about 4 rounds (aptitude test, technical test, technical interview, HR). Interviewers keep returning to "explain the project architecture, then justify the model / retrieval setup / deployment path". Topics include RAG vs fine-tuning, reranking, FastAPI concurrency and DB indexing — [Interview Query, Infosys AI Engineer](https://www.interviewquery.com/guides/infosys-ai-engineer). A 2026 Glassdoor review mentions RAG, hallucination and project questions plus coding — [Glassdoor India, Infosys review](https://www.glassdoor.co.in/Interview/Infosys-Interview-E7927-RVW92710225.htm).
- Wipro GenAI / AI engineer: about 4 rounds over about 3–5 weeks. Sample questions:
  - Explain RAG architecture; handle hallucinations — [Dataford, Wipro GenAI Engineer](https://dataford.io/interview-guides/wipro/genai-engineer); [Dataford, Wipro AI Engineer](https://dataford.io/interview-guides/wipro/ai-engineer).
  - From Glassdoor reviews: "how RAG works", "why do we need a vector database", "what chunk size did you use in your project", "explain how a transformer works and what changes if we modify encoder/decoder blocks".
  - A later client round was "much more difficult than Wipro internal rounds".
  - Sources: [Glassdoor review A](https://static.glassdoor.com.br/Interview/Wipro-Interview-E9936-RVW103220419.htm), [Glassdoor review B](https://www.glassdoor.com.au/Interview/Wipro-Interview-E9936-RVW98086313.htm).
- Freshers at services firms usually face aptitude plus basic technical rounds. Experienced hires get deeper project and architecture questions — [search synthesis of Infosys/Wipro reports, as above](https://www.interviewquery.com/guides/infosys-ai-engineer).

### Inferences
- A consolidated question bank for the book (all appear in the sources above):
  - **LLM fundamentals**: how a transformer works; tokens and context windows; temperature/sampling; why hallucinations happen.
  - **RAG**: chunk size choice, why a vector DB, embeddings, hybrid search, reranking, RAG vs fine-tuning, reducing hallucinations, citing sources.
  - **Agents**: tool calling, multi-step loops, guardrails, debugging tool traces, multi-agent tradeoffs.
  - **Evals**: defining success metrics, building a test set, LLM-as-judge, writing an eval harness.
  - **Production**: batching, latency, token and cost budgets, rate limiting, logging/tracing, output validation.
  - **Backend**: FastAPI concurrency, DB indexing.
- The "client round" at services firms means candidates must explain their project to a non-specialist and defend choices. Communication is tested as well as technique.

### Gaps
- No TCS-specific AI/GenAI engineer interview details were found. No primary data on how many companies use take-homes vs live rounds.
- No official interview-process documentation from frontier labs or big Indian product firms (Flipkart, Swiggy, Razorpay, etc.) was retrieved.

## Q3. What portfolio projects impress hiring managers? (and certifications)

### Takeaway
Plain "chatbot wrapper" projects do not stand out. What impresses is one or two end-to-end projects on a real problem that show retrieval choices (chunking, hybrid search, reranking, citations), a measured eval with an honest test set, deployment, documented failure cases and guardrails, and a public write-up. Certifications are weak signals. One cloud cert (e.g., Azure AI-102) can help with employers on that cloud, especially Microsoft-partner IT services firms, but startups mostly ignore certs.

### Cited Findings
- "Building another basic chatbot probably won't differentiate your portfolio". Focus instead on RAG, LLM infrastructure, evaluation, fine-tuning and agent orchestration. Example ideas: hybrid-search RAG, text-to-SQL with guardrails, an automated eval-dataset generator — [LinkedIn post "07 AI Projects to Get Hired in 2026"](https://co.linkedin.com/in/strivino14) (social post; the repo names are examples, not verified projects).
- A multi-document RAG system with citation tracking, hybrid search and evaluation metrics signals more than an API wrapper — [Elite AI Advantage blog](https://eliteaiadvantage.com/blog/ai-portfolio-projects-get-hired-ai-engineer).
- A good project shows a user problem, app code, data or document context, and evaluation, plus deployment notes and a public write-up — [DataTalks.Club podwiki, AI engineering portfolio projects](https://datatalks.club/podwiki/wiki/ai-engineering-portfolio-projects/).
- For RAG, "show your chunking and retrieval choices, not just the vector store" — [DataTalks.Club, RAG portfolio projects](https://datatalks.club/podwiki/wiki/rag-portfolio-projects/).
- For agents, pick a workflow you actually run so you know its failure cases, and be ready to explain the guardrails — [myengineeringpath.dev GenAI portfolio guide (2026)](https://myengineeringpath.dev/genai-engineer/portfolio-guide/).
- Hiring managers use projects to judge AI fluency, design taste, evaluation rigour and shipping ability — [techinterview.org, "The AI Portfolio: What 'Built With AI' Means in 2026 Interviews"](https://www.techinterview.org/post/3233475399/ai-portfolio-built-with-ai-2026-interviews/).
- A portfolio should show proof of engineering judgement, validation standards and architectural control, not just prompt-driven output — [Fueler blog](https://fueler.io/blog/resumes-are-dead-for-ai-engineers-how-to-show-true-proof-of-work-in-the-age-of-vibe-coding).
- **Certifications**:
  - Azure AI Engineer Associate (AI-102, about US$165) is most often recommended for GenAI work because it covers Azure OpenAI. Its recognition is strong in the Microsoft partner ecosystem and mixed elsewhere — [Careery](https://careery.pro/blog/ai-careers/best-ai-certifications); [CloudThat](https://www.cloudthat.com/resources/blog/best-ai-certifications-to-pursue-in-2026-what-really-adds-career-value).
  - Other options: AWS ML Engineer Associate (about $150), AWS ML Specialty (about $300), Google Professional ML Engineer (advanced) — [Millersville](https://techprogram.millersville.edu/blog/best-ai-certifications-2026/); [Upwork](https://www.upwork.com/resources/ai-certifications).
  - An AWS "Generative AI Developer" certification is mentioned, but its details were not independently confirmed — [uCertify](https://www.ucertify.com/blog/ai-certifications-2026/).
  - "AI startups don't care about certifications at all — they want GitHub projects" — [aiagentrank.io](https://aiagentrank.io/blog/are-ai-certifications-worth-it-2026).

### Inferences
- Suggested portfolio for the book:
  - (1) A RAG system over a messy real corpus (e.g., Indian government PDFs or company policies), with hybrid search, reranking, citations, a 50–200 question eval set, and a before/after table.
  - (2) A tool-using agent on a workflow you really use, with guardrails, traces and failure write-ups.
  - (3) An eval harness or LLM-as-judge tool.
  - Each with a README covering the problem, architecture, eval results, cost/latency numbers, what broke and what you would do next.
- Readers aiming at Indian IT services may get some resume-screening value from AI-102, because Azure OpenAI is common in client work. This is an inference from Infosys/Wipro Azure-heavy delivery, not from a cited survey.

### Gaps
- No survey data quantifies how much portfolios vs certs vs degrees affect hiring outcomes. The "portfolio is the #1 signal" claim is opinion from career blogs.

## Q4. What do hiring managers say candidates commonly lack?

### Takeaway
The most-cited gaps are: never having run an eval (cannot show how they know the system works), not shipping beyond a Jupyter notebook, having "only called the API" without understanding retrieval or failure modes, and being unable to explain what broke and why. Indian surveys add a broad confidence and skills gap: most early-career engineers use AI tools, but few are "AI-native engineers".

### Cited Findings
- "No evals is the highest-signal red flag": a candidate who cannot explain how they knew their system worked — [Alpesh Nakrani, AI engineer red flags](https://alpeshnakrani.com/blog/ai-engineer-red-flags/) (practitioner blog).
- Many candidates "can't ship anything past a Jupyter notebook to production". Inability to reproduce results without a notebook is a screen-out — [Alian Software, "Hiring for production AI"](https://aliansoftware.com/blog/hiring-for-production-ai) (vendor blog).
- For mid-level roles, hiring managers screen for whether you know what broke and why, not just that it shipped — [MentorCruise](https://mentorcruise.com/blog/career-roadmap-how-to-build-an-ai-portfolio-that-gets-you-hired/).
- Warning against hiring someone who has only called the API — [Recruiting From Scratch (2026)](https://www.recruitingfromscratch.com/blog/how-to-hire-an-llm-ai-engineer-at-a-startup-2026).
- Gauntlet AI argues that company hiring pipelines were built for a different role (SWE/ML) and test the wrong things for AI engineers — [Gauntlet AI, "How does my company hire AI engineers?"](https://www.gauntletai.com/blog/how-to-hire-ai-engineers-when-your-pipeline-was-built-for-a-different-role); [Gauntlet AI, "What hiring managers actually look for in AI engineers"](https://gauntletai.com/night-school/what-hiring-managers-actually-look-for-in-ai-engineers).
- Survey claims from a recruiting firm: 95% of 2,000 senior hiring leaders list AI fluency as a hiring factor, and 59% admit to a bad AI hire — [Qureos (marketing page)](https://www.qureos.com/hiring-guide/why-companies-make-bad-ai-hires-and-how-to-fix-it). Survey origin unverified; use with caution.
- **India**:
  - NASSCOM finding: over 90% of early-career tech professionals use AI tools, but only 23% qualify as "AI-native engineers" — [secondary coverage, Morung Express](https://mail.morungexpress.com/ai-skills-overtake-traditional-engineering-and-it-capabilities-in-india-report).
  - LinkedIn survey (early 2026): 72% of Indian professionals are looking for a new job, but 84% lack confidence in their skills for AI-led hiring — [Storyboard18](https://www.storyboard18.com/trending/majority-of-indian-professionals-plan-job-switch-in-2026-but-feel-unprepared-for-ai-led-hiring-87252.htm); [Careers360](https://news.careers360.com/ai-reshapes-hiring-84-indian-professionals-feel-unprepared-in-2026-top-hiring-job-roles-linkedin-survey).
  - ManpowerGroup 2026: 82% of Indian employers report difficulty finding skilled talent, and AI skills are the hardest to find — [Storyboard18 / search summary](https://www.storyboard18.com/amp/digital/india-ai-talent-gap-demand-for-skilled-professionals-outpaces-supply-says-parliamentary-report-ws-e-93801.htm).
  - Wipro interview reports show interviewers asking for specifics ("what chunk size did you use"), which catches candidates who copied a tutorial — [Glassdoor Wipro review](https://www.glassdoor.com.au/Interview/Wipro-Interview-E9936-RVW98086313.htm).

### Inferences
- The book's career chapter should drill four habits: (1) always build an eval set first; (2) deploy something real (API + UI + logs); (3) keep a failure log; (4) be able to justify every number in your project (chunk size, top-k, model choice, cost per query).

### Gaps
- No rigorous, primary survey of hiring managers about AI engineer gaps was found. Most evidence is practitioner and vendor blogs plus Glassdoor anecdotes.

## Q5. Salary ranges and demand trends: India vs US (with sources and dates)

### Takeaway
**India**: the average "AI engineer" base is about ₹10 LPA (Glassdoor, Aug 2026; Indeed ₹10.48 LPA, Apr 2026), but this mixes many junior and services roles. GenAI/LLM engineers at product companies, GCCs and AI startups earn much more: roughly ₹20–35 LPA mid-career and ₹50–80+ LPA senior. Product companies and GCCs pay about 40–70% more than IT services firms. **US**: AI engineer total comp averages around $210–245K (Levels.fyi-derived, via secondary sources), and frontier labs pay far more. The AI premium is large at senior levels (about 19% at staff) and small at entry level (about 6%). **Demand**: India AI engineering postings grew about 51–60% YoY in 2026 (LinkedIn), and agentic AI demand grew about 260% (CIEL HR). US AI postings grew about 55% YoY in 2025 (AI Index/Lightcast). Entry-level tech hiring is shrinking and senior hiring dominates.

### Cited Findings
**India salaries** (all secondary or aggregator unless noted; ranges conflict)
- Glassdoor (Aug 2026): AI engineer average base about ₹10 LPA, typical range ₹6–15 LPA, plus about ₹1 lakh/yr extra. Indeed India: ₹10.48 LPA (79 submissions, Apr 2026) — [ITM blog citing Glassdoor/Indeed](https://www.itm.edu/blog/ai-engineer-salary-in-india/); [Futurense](https://futurense.com/blog/ai-developer-salary-in-india).
- AIM Research "AI Engineer Salary Study – India – 2025": median AI engineer salary about ₹12–15 LPA; Bengaluru is the most lucrative city — [AIM Research](https://aimresearch.co/?p=15406).
- GenAI engineers ₹20–70 LPA vs traditional ML engineers ₹10–40 LPA. Senior LLM specialists ₹25–50 LPA. Bengaluru GenAI engineers (mid to senior) ₹15–45 LPA — [Futurense](https://futurense.com/blog/ai-developer-salary-in-india); [buildfastwithai](https://www.buildfastwithai.com/blogs/ai-jobs-india-salary-2026) (blogs).
- GCCs and AI-native startups pay 40–70% more than IT services for equal experience. Services firms cap AI engineers around ₹20–30 LPA vs ₹35–50 LPA at product companies — [Taggd (staffing firm)](https://taggd.in/blogs/ai-engineer-salary/); [Futurense](https://futurense.com/blog/ai-developer-salary-in-india).
- Lead/Principal (10+ yrs): ₹60–110 LPA — [Taggd](https://taggd.in/blogs/ai-engineer-salary/) (vendor, less reliable).
- Mid-career GenAI offers ₹20–35 LPA; senior bands ₹50–80 LPA. EY Future of Pay 2026: GenAI/ML roles can command up to a 40% base-pay premium — [CareerIndia](https://www.careerindia.com/news/genai-hiring-surge-india-2026-top-skills-salary-packages-cities-011-65139.html) (secondary).
- Bengaluru mid-level (5–8 yrs) estimates conflict:
  - ₹38–68 LPA total CTC at AI-first startups, product firms and GCCs — [Omnivoo](https://omnivoo.com/blog/machine-learning-engineer-salary-india-2026).
  - ₹28–55 LPA — [Kaam.work](https://www.kaam.work/blog/ai-engineer-salaries-in-india-2026-machine-learning-data-science-and-llm-roles).
  - ₹26–36 LPA average — [Weekday](https://www.weekday.works/post/ai-engineer-salary-in-india-2026).
- Secondtalent rate card (Sep 2026): AI engineer India ₹50K–₹9.2L per month — [Secondtalent](https://www.secondtalent.com/developer-rate-card/ai-engineer-india/) (wide range, contractor-oriented).

**US salaries**
- Levels.fyi-derived figures:
  - AI-focused engineers averaged $245,000 in 2025 — [ThirstySprout](https://www.thirstysprout.com/post/ai-engineering-salary).
  - 2026 US average total comp $242,507 — [futureproofing.dev](https://www.futureproofing.dev/resources/ai-talent-gap/ai-engineer-salary-trends).
  - Median total comp $211,000 — [Uvik](https://uvik.net/blog/ai-engineer-salary/).
  - All secondary; definitions differ.
- Levels.fyi Q3 2025: the AI premium is about 6% at entry level (down from 11% in 2024) and about 19% at staff level (up from about 16%) — [AlgeriaTech News](https://algeriatech.news/tech-salary-report-ai-compensation-2026/); [Rockstar Developer University](https://rockstardeveloperuniversity.com/ai-engineer-statistics/).
- Frontier-lab software engineers: $600K–$795K median total comp (Levels.fyi, May 2026) — [Pin.com](https://pin.com/blog/ai-compensation-salary-guide).
- PwC 2025 AI Jobs Barometer: 56% wage premium for AI skills (vs 25% the prior year) — [Pin.com](https://pin.com/blog/ai-compensation-salary-guide).

**Demand trends: India**
- LinkedIn AI Labour Market Report 2026 (Apr 2026): AI engineering postings in India up 59.5% YoY, the fastest among major markets — [Let's Data Science](https://letsdatascience.com/news/bengaluru-anchors-india-ai-hiring-as-cities-expand-opportuni-37af2ef1). LinkedIn CEO Dan Shapero (Aug 2026): AI engineering jobs in India growing 51% YoY — [NewsBytes](https://www.newsbytesapp.com/news/business/india-sees-51-growth-in-ai-engineering-jobs-linkedin-ceo/story). The figures differ; the method and period are unclear.
- LinkedIn India Jobs on the Rise 2026: Prompt Engineer, AI Engineer and Software Engineer are the top three fastest-growing roles — [Careers360](https://news.careers360.com/ai-reshapes-hiring-84-indian-professionals-feel-unprepared-in-2026-top-hiring-job-roles-linkedin-survey); [Storyboard18](https://www.storyboard18.com/amp/trending/majority-of-indian-professionals-plan-job-switch-in-2026-but-feel-unprepared-for-ai-led-hiring-87252.htm).
- CIEL HR 2026: agentic AI engineer demand +260% YoY; LLM engineers +86.5%; MLOps +82.2% — [Outlook Business](https://www.outlookbusiness.com/news/demand-for-agentic-ai-talent-rises-260-as-enterprises-embrace-ai-report).
- TeamLease Digital (Sep 2026): a 53–60% talent gap in GenAI and cloud skills. GenAI talent demand is expected to cross 10 lakh roles by 2026 — [YourStory, Sep 2026](https://yourstory.com/2026/09/talent-gap-genai-cloud-india-stands-53-60-teamlease-digital-report).
- Quess Corp study of 350,000 AI postings: an 82.9% GenAI skills shortage against an AI workforce of about 920,000 — [SocialTalent summary](https://www.socialtalent.com/?p=95007).
- Deloitte–NASSCOM (Aug 2024): AI talent demand rising from 600–650K to over 1.25M between 2022 and 2027. Often misquoted as supply. Also a reported NASSCOM estimate of a 600K+ AI professional shortage by 2027 — [People Matters](https://www.peoplematters.in/article/talent-acquisition/indias-ai-workforce-crisis-how-to-meet-the-demand-for-over-1-mn-professionals-44783).
- Parliamentary Standing Committee (Mar 2026): AI talent demand is growing faster than supply — [Storyboard18](https://www.storyboard18.com/amp/digital/india-ai-talent-gap-demand-for-skilled-professionals-outpaces-supply-says-parliamentary-report-ws-e-93801.htm).
- Naukri JobSpeak (July 2026) coverage: IT is back in growth and AI-tagged roles are surging. Hyderabad +16% YoY — [CareerIndia](https://www.careerindia.com/news/indian-it-hiring-surge-2026-top-ai-roles-salary-premiums-cities-011-65037.html) (secondary).
- Stanford AI Index 2026: India has one of the largest AI workforces but ranks low on AI talent density — [HR Executive coverage](https://hrexecutive.com/?p=165500).

**Demand trends: US/global**
- AI Index 2026 / Lightcast: AI skills appear in about 2.5% of US postings in 2025 (+about 55% YoY). The US still leads in AI talent but is attracting new talent at the lowest rate in over a decade — [Lightcast](https://lightcast.io/resources/blog/stanford-ai-2026); [HR Executive](https://hrexecutive.com/?p=165500).
- ML engineer openings are about 59% above Feb 2020 levels, while general software engineering is about 49% below — [AI Weekly](https://aiweekly.co/alerts/ml-roles-surge-59-as-tech-cuts-hit-148092-in-2026) (job-market tracker).
- Entry-level squeeze:
  - Employment for 22–25-year-olds in the most AI-exposed occupations is down about 11% (Nov 2022–Jun 2026, Stanford payroll study, as cited) — [Uvik](https://uvik.net/blog/ai-job-displacement-statistics/).
  - 71% of the 2025–26 rebound in software postings came from senior roles (Indeed Hiring Lab, as cited) — [Uvik](https://uvik.net/blog/ai-job-displacement-statistics/).
  - Entry-level tech postings are down more than 35% since Jan 2023 — [Catalitium (Dec 2025)](https://catalitium.com/market-research/ai-productivity-paradox-junior-roles-2026).
  - Figures vary widely by source.

### Inferences
- For the book's India chapter, use tiers rather than one number. All figures are 2026, indicative, and conflicting across sources:
  - (a) IT services GenAI engineer: about ₹6–20 LPA, capped around ₹20–30 LPA.
  - (b) Product company or GCC mid-level: about ₹25–55 LPA.
  - (c) Senior or staff at top product firms, GCCs and AI startups: about ₹50–100+ LPA.
- For the US: about $150–250K typical total comp, and much higher at frontier labs.
- The senior-heavy premium (6% entry vs 19% staff) plus the 2.5% entry-level share of postings suggests the role rewards demonstrated production experience. Freshers should target SWE or services GenAI tracks and build an eval-backed portfolio.
- For seniority levels, the evidence is mostly indirect. Levels follow standard SWE ladders (junior/L3, mid/L4, senior/L5, staff/L6, principal). The key differentiators at senior and above are system design for LLM products, eval strategy ownership, and cost/latency/reliability tradeoffs. Inferred from the interview-loop and premium data above; no dedicated leveling guide was found.

### Gaps
- Could not access Levels.fyi, AmbitionBox or Glassdoor directly, so there are no first-hand, dated medians by level for India or the US. All salary numbers are second-hand and often from vendors or blogs.
- No primary NASSCOM 2026 report found. Could not obtain the Stanford AI Index 2026 India job-posting share.
- No Reddit (r/developersIndia, r/cscareerquestions) threads were retrieved, because of time and tool limits. Anecdotal community sentiment is not covered.
- No AI-engineer-specific seniority ladder (e.g., a published company leveling rubric for AI engineers) was found.
