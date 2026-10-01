# Language pass (v1.0.1)

The reader is a first-year student who knows basic Python and reads English as a second language. Rules:

- US grade level 8 or lower in every chapter; most prose sentences under 25 words, one idea per sentence.
- No idioms or slang whose meaning can't be worked out from the words; metaphors only when explained and universal.
- One name for one idea. **Calibrated** is the term and "honest probabilities" its plain explanation.
  **Threshold** is the term for a cut-off on the probability scale; "line" now means only a drawn or written line.
  The three zones are **act**, **review** and **escalate**.
- Every technical term defined in one plain sentence at first use; at most one new term per paragraph.
- Common words: "use", "show", "about".

Numbers, code, figure data, citations, quotations, chapter structure and the voice are unchanged. Grade levels are
Flesch-Kincaid grades computed by `tools/readability.py` on prose only (code, figures, tables and maths removed).
Every change is logged below as a before/after pair, applied by `tools/simplify_apply.py`.

## Chapter 5: Deep learning in one chapter

34 changes.

- `chapters/ch05.qmd`
  - Before: "Deep learning" might be the most intimidating phrase in the field. It sounds like something between neuroscience and magic.
  - After: "Deep learning" may be the scariest phrase in the field. It sounds like a mix of brain science and magic.
- `chapters/ch05.qmd`
  - Before: The logistic regression from Chapter 2 is a single artificial neuron. A deep network is many of them, stacked in layers and trained with the same downhill walk. Add two more ideas, a way to turn words into meaningful numbers and a way for words to look at each other, and you have the machinery inside every LLM.
  - After: The logistic regression from Chapter 2 is a single artificial neuron. A deep network is many of them, stacked in layers and trained with the same downhill walk. Add two more ideas and you have the machinery inside every LLM. One is a way to turn words into useful numbers. The other is a way for words to look at each other.
- `chapters/ch05.qmd`
  - Before: This chapter is a fast tour, not a course. You need four ideas from it, and each is smaller than it sounds.
  - After: This chapter is a fast tour, not a full course. You need four ideas from it, and each one is simpler than it sounds.
- `chapters/ch05.qmd`
  - Before: Look at what a neuron does to an alert: multiply each clue by a weight, add everything up, squash the total into a probability. The places where a weighted sum equals some value form a straight line. So all a single neuron can do is cut the space in two with a straight edge.
  - After: Look at what a neuron does to an alert. It multiplies each clue by a weight, adds everything up, and squashes the total into a probability. All the points where a weighted sum has the same value form a straight line. So a single neuron can only cut the space in two with a straight edge.
- `chapters/ch05.qmd`
  - Before: A real limit. Imagine behaviour that's suspicious when it's *unusual in any direction*: far too much activity, or far too little, far too early, or far too late. Normal sits in the middle, and no straight line separates the middle from the edges.
  - After: That's a real limit. Imagine behaviour that's suspicious when it's *unusual in any direction*: far too much activity or far too little, far too early or far too late. Normal behaviour sits in the middle. No straight line can separate the middle from the edges.
- `chapters/ch05.qmd`
  - Before: The fix is to send the clues to a few neurons first, each drawing its own line, and let an output neuron combine *their* answers. Three straight edges make a triangle. Twelve make something close to a circle (@fig-line-limit), and the log loss drops from
  - After: The fix is to send the clues to a few neurons first. Each one draws its own line, and an output neuron combines *their* answers. Three straight edges make a triangle. Twelve make something close to a circle (@fig-line-limit), and the log loss drops from
- `chapters/ch05.qmd`
  - Before: One detail makes it work. A weighted sum of weighted sums is still a weighted sum, so each hidden neuron applies a bend before passing its answer on. The popular bend is almost embarrassingly simple: if the sum is negative, output zero; otherwise pass it through. It's called **ReLU**, and it's a hinge. Enough hinges, added together, can trace almost any curve.
  - After: One detail makes it work. A weighted sum of weighted sums is still just a weighted sum. So each hidden neuron bends its answer before passing it on. The most common bend is very simple: if the sum is negative, output zero; otherwise pass it through unchanged. It's called **ReLU**, and it works like a hinge. Add enough hinges together and you can draw almost any curve.
- `chapters/ch05.qmd`
  - Before: Training works the same way as before, rolling downhill on log loss. The only new problem is finding the slope for a weight buried several layers deep, and the answer, **backpropagation**, is easiest to picture as blame [@rumelhart1986]. The error at the output is shared back through the network, each layer passing blame to the one before in proportion to how much each weight contributed.
  - After: Training works the same way as before: roll downhill on log loss. The only new problem is finding the slope for a weight that sits several layers deep. The answer is called **backpropagation**, and it's easiest to picture as sharing out blame [@rumelhart1986]. The error at the output is passed back through the network. Each layer passes blame to the layer before it, in proportion to how much each weight added to the error.
- `chapters/ch05.qmd`
  - Before: Depth matters in practice for a simple reason. On photos, the first layers of a trained network learn to detect edges, later ones textures and shapes, the last ones whole objects [@lecun2015]. Nobody wrote a rule for "edge". A deep network takes raw input, pixels or characters, and *learns its own clues*.
  - After: Depth matters in practice for a simple reason. On photos, the first layers of a trained network learn to find edges. Later layers find textures and shapes, and the last ones find whole objects [@lecun2015]. Nobody wrote a rule for "edge". A deep network takes raw input, such as pixels or characters, and *learns its own clues*.
- `chapters/ch05.qmd`
  - Before: On Kestrel's neat, hand-made features, though, it has nothing to find. A small network ties logistic regression,
  - After: On Kestrel's neat, hand-made features, though, there's nothing left for it to find. A small network does as well as logistic regression, but no better:
- `chapters/ch05.qmd`
  - Before: Deep networks earn their keep on raw, messy input. On neat features, start simple.
  - After: Deep networks are worth their cost on raw, messy input. On neat features, start with something simple.
- `chapters/ch05.qmd`
  - Before: A network does arithmetic, so every word has to become a number. Number the words, "invoice" is 101 and "bill" is 102, and the maths takes the numbers literally: "bill" becomes halfway between "invoice" and "lunch". Give every word its own slot instead, and every word is exactly as different from every other. Neither representation knows anything.
  - After: A network does arithmetic, so every word has to become a number. Suppose you just number the words: "invoice" is 101, "bill" is 102 and "lunch" is 103. The maths takes the numbers literally, so "bill" is halfway between "invoice" and "lunch". Suppose instead you give every word its own slot. Then every word is exactly as different from every other word. Neither way knows anything about meaning.
- `chapters/ch05.qmd`
  - Before: The fix came from linguistics, decades before deep learning.
  - After: The fix came from linguistics, the study of language, decades before deep learning.
- `chapters/ch05.qmd`
  - Before: "phishing" and "spoofed" rarely appear in the same sentence. But they appear in the same *kinds* of places, next to "email", before "asked", near "password". Count, for every word, which words turn up near it, and squash those counts into a short list of numbers. Words used in similar ways end up with similar lists. That list is an **embedding**.
  - After: "phishing" and "spoofed" rarely appear in the same sentence. But they appear in the same *kinds* of places: next to "email", before "asked", near "password". For every word, count which words turn up near it. Then squash those counts into a short list of numbers. Words used in similar ways end up with similar lists. That list is an **embedding**.
- `chapters/ch05.qmd`
  - Before: Nobody told the method that "trojan", "ransomware" and "backdoor" belong together. It found out (@fig-word-map). Closeness is measured by the angle between two word vectors, called **cosine similarity**: about 1 when they point the same way, about 0 when they're unrelated.
  - After: Nobody told the method that "trojan", "ransomware" and "backdoor" belong together. It found out by itself (@fig-word-map). We measure closeness by the angle between two word vectors. This measure is called **cosine similarity**. It's about 1 when two vectors point the same way and about 0 when the words are unrelated.
- `chapters/ch05.qmd`
  - Before: The same trick works for whole alerts: similar alerts land near each other, which lets an analyst ask "show me past alerts like this one". It's also the engine inside RAG (Chapter 7). But it has a blind spot worth remembering. Finding Kestrel's 50 most similar past alerts by text and counting the attacks gives a well-calibrated probability, with a calibration error of {{< num ch07 knn.ece f3 >}}, and a blunt one: AUC {{< num ch07 knn.auc f2 >}}, against {{< num ch07 lr.auc f2 >}} for logistic regression on the fields. Two "large upload" alerts look identical to an embedding whether the threat-intel score is 0.05 or 0.95.
  - After: The same trick works for whole alerts. Similar alerts land near each other, so an analyst can ask "show me past alerts like this one". It's also the engine inside RAG (Chapter 7). But it has a weakness worth remembering. Here's a test: for each alert, find Kestrel's 50 most similar past alerts by their text, and count how many were attacks. That gives a calibrated probability, with a calibration error of {{< num ch07 knn.ece f3 >}}. But it ranks alerts poorly: its AUC is {{< num ch07 knn.auc f2 >}}, against {{< num ch07 lr.auc f2 >}} for logistic regression on the fields. To an embedding, two "large upload" alerts look the same whether the threat-intel score is 0.05 or 0.95.
- `chapters/ch05.qmd`
  - Before: One vector per word still isn't enough. "invoice, not phishing" is an analyst clearing an alert; "phishing, not invoice" is an analyst raising one. Same three words. A model that only knows *which words appear* sees two identical notes.
  - After: One vector per word still isn't enough. "invoice, not phishing" is an analyst clearing an alert. "phishing, not invoice" is an analyst raising one. They use the same three words. A model that only knows *which words appear* sees two identical notes.
- `chapters/ch05.qmd`
  - Before: **Attention** fixes this, and the core idea fits in a sentence: every word asks which other words should change its meaning, and listens to them in proportion.
  - After: **Attention** fixes this. The core idea fits in one sentence: every word asks which other words should change its meaning, and listens to them in proportion.
- `chapters/ch05.qmd`
  - Before: Each word makes three vectors from its own: a **query** ("what am I looking for?"), a **key** ("what can I tell you about?") and a **value** (what it passes on). Compare every query with every key, turn the scores into weights that add up to 1 with a **softmax**, and take the weighted mix of values (@fig-qkv). That's the Q, K and V from the scary diagrams.
  - After: Each word makes three vectors from its own: a **query** ("what am I looking for?"), a **key** ("what can I tell you about?") and a **value** (what it passes on). Compare every query with every key. Turn the scores into weights that add up to 1; the function that does this is called a **softmax**. Then take the weighted mix of the values (@fig-qkv). Those are the Q, K and V you see in diagrams of attention.
- `chapters/ch05.qmd`
  - Before: Train one attention layer on 4,000 tiny notes where "not" flips the meaning, and a bag of words tops out at {{< num ch08 acc_bow pct >}} while attention reaches {{< num ch08 acc_att pct >}}. Look inside, and you find what it learned.
  - After: Train one attention layer on 4,000 tiny notes where "not" flips the meaning. A model that only counts words (a "bag of words") reaches {{< num ch08 acc_bow pct >}} accuracy at best. Attention reaches {{< num ch08 acc_att pct >}}. Look inside, and you can see what it learned.
- `chapters/ch05.qmd`
  - Before: A **transformer** is this idea repeated and polished: attention, then a small network on each word, stacked dozens of times [@vaswani2017]. It took over because attention looks at every pair of words *at once*, so it runs in parallel on graphics chips and can use enormous hardware. One more distinction matters for this book. A **reader** (encoder) lets every word see the whole input, which is what you want for understanding and deciding. A **writer** (decoder) lets each word see only the words before it, which is what you need for generating text, because when you're writing word five, word six doesn't exist yet. LLMs are writers.
  - After: A **transformer** is this idea repeated and improved: attention, then a small network on each word, stacked dozens of times [@vaswani2017]. Transformers took over because attention looks at every pair of words *at once*. So the work runs in parallel on graphics chips and can use very large computers. One more difference matters for this book. A **reader** (encoder) lets every word see the whole input. That's what you want for understanding and deciding. A **writer** (decoder) lets each word see only the words before it. That's what you need for writing text: when you're writing word five, word six doesn't exist yet. LLMs are writers.
- `chapters/ch05.qmd`
  - Before: How did attention stacked up turn into something that writes essays? Mostly, it got bigger, trained on a task that needs no labels: take any text, hide the next word, and guess it. Every sentence ever written becomes free training data. To get good at the guessing, a model has to learn grammar, facts and a surprising amount of reasoning. This is **pretraining**, and researchers found its loss falls smoothly and predictably as models, data and computing power grow [@kaplan2020].
  - After: How did stacked attention turn into something that writes essays? Mostly, it got bigger. It was trained on a task that needs no labels: take any text, hide the next word, and guess it. So every sentence ever written becomes free training data. To get good at guessing, a model has to learn grammar, facts and a surprising amount of reasoning. This stage is called **pretraining**. Researchers found that its loss falls smoothly and predictably as models, data and computing power grow [@kaplan2020].
- `chapters/ch05.qmd`
  - Before: Two more stages turn a text predictor into an assistant: **instruction tuning**, on examples of good answers, and **preference tuning**, where the model learns the answers people prefer [@ouyang2022]. People tend to prefer answers that sound sure. OpenAI's own report on GPT-4 showed the pretrained model's confidence was well calibrated and, after preference tuning, noticeably less so [@openai2023].
  - After: Two more stages turn a text predictor into an assistant. In **instruction tuning**, the model trains on examples of good answers. In **preference tuning**, it learns which answers people prefer [@ouyang2022]. People tend to prefer answers that sound sure. OpenAI's own report on GPT-4 showed that the pretrained model's confidence was well calibrated. After preference tuning, it was clearly less so [@openai2023].
- `chapters/ch05.qmd`
  - Before: There's a deeper version of this effect, and you can watch it happen on Kestrel's alerts. Train a network much bigger than the job needs, for a long time, and check it on test alerts.
  - After: There's a deeper version of this effect, and you can watch it happen on Kestrel's alerts. Train a network much bigger than the job needs, train it for a long time, and check it on test alerts.
- `chapters/ch05.qmd`
  - Before: Accuracy barely changed. Meanwhile the test log loss went from {{< num ch09 first.log_loss f2 >}} to {{< num ch09 last.log_loss f2 >}}, and the calibration error from {{< num ch09 first.ece f3 >}} to {{< num ch09 last.ece f3 >}} (@fig-overtraining). The model's *ranking* of alerts held up. Its *honesty* fell apart.
  - After: Accuracy barely changed. Meanwhile, the test log loss went from {{< num ch09 first.log_loss f2 >}} to {{< num ch09 last.log_loss f2 >}}, and the calibration error went from {{< num ch09 first.ece f3 >}} to {{< num ch09 last.ece f3 >}} (@fig-overtraining). The model still *ranked* alerts well. But it was no longer *calibrated*.
- `chapters/ch05.qmd`
  - Before: The mechanism follows from Chapter 2. Once a model gets most training examples right, the only way left to lower log loss is to push correct answers closer to certainty: 0.95, then 0.99, then 0.999. A flexible model trained long enough becomes certain of everything it saw, including the noise, and carries that certainty onto new cases where it hasn't earned it. Deeper, wider modern networks show the same thing [@guo2017].
  - After: The reason follows from Chapter 2. Once a model gets most training examples right, there's only one way left to lower log loss: push correct answers closer to certainty, 0.95, then 0.99, then 0.999. A flexible model trained long enough becomes certain of everything it saw, including the noise. Then it brings that certainty to new cases, where it isn't justified. Deeper, wider modern networks show the same thing [@guo2017].
- `chapters/ch05.qmd`
  - Before: Flexible models trained to squeeze out the last drop of training loss learn to be certain.
  - After: Flexible models trained to make their training loss as small as possible learn to be too certain.
- `chapters/ch05.qmd`
  - Before: The fixes are ones you've already met in Chapters 2 and 3, and they're simple. Stop training when the loss on held-out data stops improving;
  - After: You've already met the fixes in Chapters 2 and 3, and they're simple. First, stop training when the loss on held-out data stops improving;
- `chapters/ch05.qmd`
  - Before: And correct the probabilities afterwards on data the model never saw: a single "temperature" cut the calibration error from {{< num ch09 last.ece f3 >}} to {{< num ch09 ece_after_T f3 >}}. A correction can make the numbers trustworthy again. It can't give back what the model threw away by memorising.
  - After: Second, correct the probabilities afterwards, using data the model never saw. Here, a single "temperature" cut the calibration error from {{< num ch09 last.ece f3 >}} to {{< num ch09 ece_after_T f3 >}}. A correction can make the numbers calibrated again. It can't give back what the model lost by memorising.
- `chapters/ch05.qmd`
  - Before: Networks need lots of data, and with too little they memorise. They're hard to read: no tidy "×2.9 for a new country". Embeddings inherit the associations in their training text, including stereotypes [@bolukbasi2016], and they're bad at negation, since "malicious" and "not malicious" keep almost the same company. Attention maps are tempting to read as explanations; in large models they often aren't [@jain2019]. And you usually can't retrain someone else's big model, or even see its raw probabilities, which is one reason a decision model that returns probabilities as its main output, and gets tested, matters so much.
  - After: Networks need lots of data, and with too little they memorise. They're hard to read: there's no tidy "×2.9 for a new country". Embeddings copy the associations in their training text, including stereotypes [@bolukbasi2016]. They're also bad at negation, since "malicious" and "not malicious" appear next to almost the same words. It's tempting to read attention maps as explanations, but in large models they often aren't [@jain2019]. And you usually can't retrain someone else's big model, or even see its raw probabilities. That's one reason it matters so much to have a decision model that returns probabilities as its main output, and to test them.
- `chapters/ch05.qmd`
  - Before: Your team swaps Kestrel's logistic regression for a big network because its training loss is lower, and keeps the same line: alerts below P = 0.03 close automatically. Will more or fewer real threats be closed without a human?
  - After: Your team replaces Kestrel's logistic regression with a big network because its training loss is lower. They keep the same threshold: alerts below P = 0.03 close automatically. Will more or fewer real threats be closed without a person seeing them?
- `chapters/ch05.qmd`
  - Before: (More. The big network is overconfident: many alerts it pushes near zero aren't really that safe. The line assumed honest probabilities. Recalibrate first and re-check the line, or keep the simpler model.)
  - After: (More. The big network is overconfident: many alerts it pushes near zero aren't really that safe. The threshold assumed calibrated probabilities. Recalibrate first and check the threshold again, or keep the simpler model.)
- `chapters/ch05.qmd`
  - Before: A neuron could only draw straight lines, so we stacked neurons in layers and gave each a hinge. Words needed to become numbers with meaning, so we placed them by the company they keep. One vector per word couldn't tell "not phishing" from "phishing", so we let words look at each other, and attention learned negation on its own. Scaled up and trained to guess the next word, that machinery became the LLM, with a side effect: flexible models trained long enough become sure of themselves, and accuracy hides it.
  - After: A neuron could only draw straight lines, so we stacked neurons in layers and gave each one a hinge. Words needed to become numbers with meaning, so we placed them by the words they appear with. One vector per word couldn't tell "not phishing" from "phishing". So we let words look at each other, and attention learned negation on its own. Made bigger and trained to guess the next word, that machinery became the LLM. It came with a side effect: flexible models trained long enough become too sure of themselves, and accuracy hides it.
- `chapters/ch05.qmd`
  - Before: Next: what does an LLM actually do when it writes? One token at a time, with a probability for every possible next piece, and that detail matters a great deal for decisions.
  - After: Next: what does an LLM actually do when it writes? It writes one token at a time, with a probability for every possible next piece. That detail matters a great deal for decisions.

## Chapter 6: How an LLM writes

29 changes.

- `chapters/ch06.qmd`
  - Before: You've probably wondered whether that's just a nice animation, with the whole answer sitting there, finished, revealed slowly for effect.
  - After: You may have wondered if that's just a nice animation. Maybe the whole answer is already finished, and it's shown slowly for effect.
- `chapters/ch06.qmd`
  - Before: It isn't an animation. The model really works like that: it doesn't know the end of its sentence when it writes the beginning. It picks one small piece, then the next, each time looking back at everything so far.
  - After: It isn't an animation. The model really works like that. It doesn't know the end of its sentence when it writes the beginning. It picks one small piece, then the next. Each time, it looks back at everything written so far.
- `chapters/ch06.qmd`
  - Before: That one detail explains a surprising amount: why long answers are slow, why the same question can get different answers, why you pay per token, and why "just ask the LLM" is an awkward way to make a decision. It also explains why getting a clean, trustworthy *decision* out of a writing machine is harder than adding "reply in JSON" to a prompt.
  - After: That one detail explains a lot. It explains why long answers are slow, why the same question can get different answers, and why you pay per token. It also explains why "just ask the LLM" is an awkward way to make a decision. Getting a clean, calibrated *decision* out of a writing machine is harder than adding "reply in JSON" to a prompt.
- `chapters/ch06.qmd`
  - Before: A language model reads **tokens**: chunks of text, often parts of words, made by a separate program called a tokeniser. Common words become one chunk; rare ones, like hostnames, typos and base64 blobs, the stuff security logs are made of, break into many small pieces. You pay per token, and numbers such as 0.87 or an IP address may be split in ways that don't line up with their meaning, which is one reason LLMs can be clumsy with arithmetic.
  - After: A language model reads **tokens**: chunks of text, often parts of words. A separate program, called a tokeniser, cuts the text into tokens. Common words become one chunk. Rare ones break into many small pieces, and security logs are full of rare strings: hostnames, typos and encoded data. You pay per token. Numbers such as 0.87, or an IP address, may be split in ways that don't match their meaning. That's one reason LLMs can be clumsy with arithmetic.
- `chapters/ch06.qmd`
  - Before: Read everything so far. Produce a probability for every token in the vocabulary, often around a hundred thousand of them. Pick one. Append it, and go round again (@fig-loop-06). The probability step is the transformer from Chapter 5, a *writer* that can only look backwards. Everything else is a loop around it.
  - After: Read everything so far. Produce a probability for every token in the vocabulary, often about a hundred thousand of them. Pick one. Add it to the end, and go round again (@fig-loop-06). The probability step is the transformer from Chapter 5, a *writer* that can only look backwards. Everything else is a loop around it.
- `chapters/ch06.qmd`
  - Before: The picking hides a choice. Always taking the most likely token, **greedy** decoding, is predictable but dull. Rolling a die weighted by the probabilities, **sampling**, gives variety. A setting called **temperature** controls how adventurous the die is: divide every score by *T* before turning scores into probabilities, so below 1 the favourites win more, and above 1 long shots get a real chance. (It's the same temperature Chapter 3 used to soften overconfident models, pointed the other way.)
  - After: The picking step hides a choice. You can always take the most likely token. That's called **greedy** decoding, and it's predictable but dull. Or you can roll a die weighted by the probabilities. That's called **sampling**, and it gives variety. A setting called **temperature** controls how bold the die is. Every score is divided by *T* before the scores become probabilities. Below 1, the likely tokens win more often. Above 1, unlikely tokens get a real chance. (It's the same temperature Chapter 3 used to soften overconfident models, used the other way round.)
- `chapters/ch06.qmd`
  - Before: Because each token waits for the one before it, generation is *sequential*: token fifty can't exist before token forty-nine. So the length of the answer drives how long it takes.
  - After: Each token waits for the one before it, so generation is *sequential*: token fifty can't exist before token forty-nine. So the length of the answer sets how long it takes.
- `chapters/ch06.qmd`
  - Before: Assuming {{< num ch10 ttft f2 >}} seconds before the first token and {{< num ch10 tps int >}} tokens a second after (illustrative, not measured), a one-word answer takes about {{< num ch10 lat_1 f1 >}} seconds, an explanation of a few hundred tokens about {{< num ch10 lat_300 f1 >}}, and 1,500 tokens of step-by-step reasoning about {{< num ch10 lat_1500 int >}} (@fig-latency-06). The newest "reasoning" models write long chains of thought before answering, which makes them much better on hard problems and much slower, because every thinking token goes through the loop. That trade-off, careful and slow against quick and intuitive, is the heart of Part III.
  - After: Assume {{< num ch10 ttft f2 >}} seconds before the first token and {{< num ch10 tps int >}} tokens a second after that (illustrative numbers, not measured). Then a one-word answer takes about {{< num ch10 lat_1 f1 >}} seconds. An explanation of a few hundred tokens takes about {{< num ch10 lat_300 f1 >}}. And 1,500 tokens of step-by-step reasoning take about {{< num ch10 lat_1500 int >}} (@fig-latency-06). The newest "reasoning" models write long chains of thought before they answer. This makes them much better on hard problems, and much slower, because every thinking token goes through the loop. That trade-off, careful and slow against quick and intuitive, is the centre of Part III.
- `chapters/ch06.qmd`
  - Before: Sampling has another consequence, and for decisions it's a big one. Ask the same question twice at any temperature above zero, and you might get two different answers. For a poem, that's a feature. For deciding whether an alert is real, it's a problem.
  - After: Sampling has another effect, and for decisions it's a big one. Ask the same question twice at any temperature above zero, and you might get two different answers. For a poem, that's useful. For deciding whether an alert is real, it's a problem.
- `chapters/ch06.qmd`
  - Before: This is the book's stand-in LLM, `llm-mock-synthetic`, built to behave the way LLMs typically do; it isn't a model of any real product. Across forty borderline alerts, each asked twenty times, most got *both* answers.
  - After: This is the book's stand-in LLM, `llm-mock-synthetic`. It's built to behave the way LLMs usually do; it isn't a copy of any real product. We asked it about forty borderline alerts, twenty times each. Most alerts got *both* answers.
- `chapters/ch06.qmd`
  - Before: In @fig-variance-06, {{< num ch10 n_split int >}} of the {{< num ch10 n_alerts int >}} alerts flipped. Set the temperature to zero and answers become much more repeatable, but the *uncertainty* doesn't go away. It just stops showing.
  - After: In @fig-variance-06, {{< num ch10 n_split int >}} of the {{< num ch10 n_alerts int >}} alerts flipped between answers. Set the temperature to zero and the answers repeat much more often. But the *uncertainty* doesn't go away. You just stop seeing it.
- `chapters/ch06.qmd`
  - Before: And nothing in the loop checks whether the sentence is *true*. The model produces a plausible next token. It can write a fluent, confident, completely made-up hostname or citation, because that's the kind of thing that *would* come next. That's **hallucination**.
  - After: And nothing in the loop checks whether the sentence is *true*. The model produces a likely-sounding next token. It can write a fluent, confident, completely made-up hostname or citation, because that's the kind of thing that *would* come next. That's called **hallucination**.
- `chapters/ch06.qmd`
  - Before: Software can't read a paragraph. It needs `verdict = "malicious"`: a field, a value. So every team wiring an LLM into a pipeline adds a line to the prompt: *"Reply only with JSON."* And it works. Almost always.
  - After: Software can't read a paragraph. It needs `verdict = "malicious"`: a field and a value. So every team that connects an LLM to other software adds a line to the prompt: *"Reply only with JSON."* And it works. Almost always.
- `chapters/ch06.qmd`
  - Before: But "almost" adds up. Over 4,000 alerts, {{< num ch11 prompt_fail_share pct1 >}} of the answers came back broken, wrapped or padded with an extra field. At seven hundred alerts a day, that's about {{< num ch11 prompt_fail_per_day int >}} failures every day.
  - After: But "almost" adds up. Over 4,000 alerts, {{< num ch11 prompt_fail_share pct1 >}} of the answers came back broken, wrapped in extra text, or with an extra field. At seven hundred alerts a day, that's about {{< num ch11 prompt_fail_per_day int >}} failures every day.
- `chapters/ch06.qmd`
  - Before: The three classic failures are in @fig-json-failures: chatty text around the JSON ("Sure! Here is..."), a response cut off mid-object, and valid JSON with an invented field, here an `attacker_country` that isn't in the alert at all. That last one is the worst, because it parses fine and slips made-up data into your system.
  - After: The three common failures are in @fig-json-failures. The first is chatty text around the JSON ("Sure! Here is..."). The second is a response cut off in the middle. The third is valid JSON with an invented field: here, an `attacker_country` that isn't in the alert at all. That last one is the worst. It parses fine, so made-up data gets into your system without anyone noticing.
- `chapters/ch06.qmd`
  - Before: The generation loop gives us a lever. At each step, we can forbid every token that would break the required format. That's **constrained decoding**, sold as "JSON mode" or "structured outputs" [@willard2023]. It guarantees the *shape* of the answer.
  - After: The generation loop gives us a way to control this. At each step, we can forbid every token that would break the required format. That's called **constrained decoding**, and providers sell it as "JSON mode" or "structured outputs" [@willard2023]. It guarantees the *shape* of the answer.
- `chapters/ch06.qmd`
  - Before: A constrained model can still say "benign" for a real attack, in perfect syntax. So whatever the provider promises, treat model output like text typed into a web form by a stranger. Parse it into a strict type that rejects unknown fields and wrong values, and if it fails, send the case to a person, never to an automatic action.
  - After: A constrained model can still say "benign" for a real attack, in perfect syntax. So whatever the provider promises, treat model output like text a stranger typed into a web form. Parse it into a strict type that rejects unknown fields and wrong values. If parsing fails, send the case to a person, never to an automatic action.
- `chapters/ch06.qmd`
  - Before: There are three different numbers you might use. **The confidence the model wrote** is text: the characters "0", ".", "9", "5", picked like any other tokens. **The token probability** is the probability the model gave to "malicious" as the next token, which many APIs will return. And **a probability from a decision model** is one whose actual output is a probability for each option.
  - After: There are three different numbers you might use. **The confidence the model wrote** is text: the characters "0", ".", "9", "5", picked like any other tokens. **The token probability** is the probability the model gave to "malicious" as the next token; many APIs will return it. And **a probability from a decision model** comes from a model whose real output is a probability for each option.
- `chapters/ch06.qmd`
  - Before: The mock wrote only {{< num ch11 n_distinct_stated int >}} different confidence values, {{< num ch11 share_stated_ge_09 pct >}} of them 0.9 or higher, a pattern many people have noticed with real models. Stated confidence ranks poorly, with an AUC of {{< num ch11 verbal.auc f2 >}}. The token probability ranks much better ({{< num ch11 token.auc f2 >}}) but is overconfident (ECE {{< num ch11 token.ece f3 >}}). The decision model ranks slightly better again ({{< num ch11 jev_text.auc f2 >}}) and is also well calibrated, with an ECE of {{< num ch11 jev_text.ece f3 >}} (@fig-three-confidences).
  - After: The mock wrote only {{< num ch11 n_distinct_stated int >}} different confidence values, and {{< num ch11 share_stated_ge_09 pct >}} of them were 0.9 or higher. Many people have noticed the same pattern with real models. Stated confidence ranks alerts poorly, with an AUC of {{< num ch11 verbal.auc f2 >}}. The token probability ranks much better ({{< num ch11 token.auc f2 >}}) but is overconfident (ECE {{< num ch11 token.ece f3 >}}). The decision model ranks slightly better again ({{< num ch11 jev_text.auc f2 >}}). It's also well calibrated, with an ECE of {{< num ch11 jev_text.ece f3 >}} (@fig-three-confidences).
- `chapters/ch06.qmd`
  - Before: Look closely and the stated confidence has the lowest ECE of the three, {{< num ch11 verbal.ece f3 >}}. That isn't a win. When a model says nearly the same thing about every alert, it can be right *on average* and still tell you almost nothing about which alert is which. It's Chapter 3's lesson again: calibration and ranking are separate, and you need both.
  - After: Look closely: the stated confidence has the lowest ECE of the three, {{< num ch11 verbal.ece f3 >}}. That isn't a win. A model that says nearly the same thing about every alert can be right *on average*. But it tells you almost nothing about which alert is which. It's Chapter 3's lesson again: calibration and ranking are separate, and you need both.
- `chapters/ch06.qmd`
  - Before: Research on real models is mixed here; one study found stated confidence *better* calibrated than token probabilities for some tuned models [@tian2023], another found it badly overconfident [@xiong2024]. The only safe rule is to measure yours.
  - After: Research on real models gives mixed results here. One study found stated confidence *better* calibrated than token probabilities for some tuned models [@tian2023]. Another found it badly overconfident [@xiong2024]. The only safe rule is to measure your own model.
- `chapters/ch06.qmd`
  - Before: Why isn't a token probability the probability of the answer? Because the model is choosing between tens of thousands of tokens, not two answers. "malicious", "Malicious" and " malicious" with a space are all different tokens, and some probability goes to the model starting a sentence instead of answering. You can add up the right ones and renormalise, but by then you're building a decision model by hand on top of a writing model.
  - After: Why isn't a token probability the probability of the answer? Because the model is choosing between tens of thousands of tokens, not between two answers. "malicious", "Malicious" and " malicious" with a space are all different tokens. Some probability also goes to the model starting a sentence instead of answering. You can add up the right tokens and rescale so they sum to 1. But then you're building a decision model by hand, on top of a writing model.
- `chapters/ch06.qmd`
  - Before: Which brings us to a different way of asking. Instead of asking a writer to produce text in a decision-shaped format, ask a model whose native output *is* the decision. Declare the question and its possible answers as types, and get back data, with a probability for every option.
  - After: That leads to a different way of asking. Don't ask a writer to produce text shaped like a decision. Ask a model whose natural output *is* the decision. Declare the question and its possible answers as types. You get back data, with a probability for every option.
- `chapters/ch06.qmd`
  - Before: Jev's interface looks like this (@fig-typed-vs-text): nothing to parse, no format to break, labels that can only be the ones you listed, and a number designed to be a probability, which makes it a claim you can check. Part III takes it apart.
  - After: Jev's interface looks like this (@fig-typed-vs-text). There's nothing to parse and no format to break. The labels can only be the ones you listed. And the number is designed to be a probability, so it's a claim you can check. Part III looks at Jev in detail.
- `chapters/ch06.qmd`
  - Before: Token probabilities describe the next piece of text, not the truth of the answer. JSON mode doesn't stop a model choosing the wrong value or copying an attacker's text into a field, and strict validation doesn't catch a value that's valid but wrong: a threat-intel score misread as 0.18 instead of 0.81 passes every schema. Providers update models, so "temperature 0" behaviour can shift between versions; pin versions for anything you'll audit. And typed decision APIs have their own limits: probabilities without reasons, and calibration that still has to be tested on your data.
  - After: Token probabilities describe the next piece of text, not the truth of the answer. JSON mode doesn't stop a model from choosing the wrong value, or from copying an attacker's text into a field. Strict checking doesn't catch a value that's valid but wrong: a threat-intel score misread as 0.18 instead of 0.81 passes every schema. Providers update their models, so "temperature 0" behaviour can change between versions. Fix the model version for anything you'll audit. And typed decision APIs have their own limits: they give probabilities without reasons, and their calibration still has to be tested on your data.
- `chapters/ch06.qmd`
  - Before: Kestrel wants to auto-close alerts the LLM labels "benign" with stated confidence at least 0.95. Would you trust that line? What would you threshold instead?
  - After: Kestrel wants to auto-close alerts that the LLM labels "benign" with a stated confidence of at least 0.95. Would you trust that threshold? What would you put a threshold on instead?
- `chapters/ch06.qmd`
  - Before: (No. 0.95 and 0.99 are the mock's favourite values, so the line filters almost nothing. Put the line on the best-calibrated probability you have, checked on recent history, with its position set by what mistakes cost, as Chapter 4 shows.)
  - After: (No. 0.95 and 0.99 are the mock's favourite values, so the threshold filters almost nothing. Put the threshold on the best-calibrated probability you have, checked on recent history. Set its position by what mistakes cost, as Chapter 4 shows.)
- `chapters/ch06.qmd`
  - Before: ChatGPT's typing turned out to be the real mechanism: tokens come out one at a time, each chosen from a probability for every possible next piece. That loop explained why long answers are slow, why the same question can get different answers, and why fluent doesn't mean true. Then we asked the loop for decisions. The format broke a few times in every hundred, constrained decoding fixed the format but not the content, and of three candidates for "how sure", only one was designed to be thresholded.
  - After: ChatGPT's typing turned out to be how the model really works. Tokens come out one at a time, each chosen from a probability for every possible next piece. That loop explained why long answers are slow, why the same question can get different answers, and why fluent doesn't mean true. Then we asked the loop for decisions. The format broke a few times in every hundred. Constrained decoding fixed the format but not the content. And of three candidates for "how sure", only one was designed to have a threshold put on it.
- `chapters/ch06.qmd`
  - Before: Next: an LLM knows the internet, not your company. Retrieval hands it the right documents, agents let it act, and both open new ways to fail.
  - After: Next: an LLM knows the internet, not your company. Retrieval gives it the right documents, and agents let it act. Both bring new ways to fail.

## Chapter 19: An applications gallery

27 changes.

- `chapters/ch19.qmd`
  - Before: It isn't. Kestrel's SOC was a teaching example, chosen because it has everything: lots of decisions, a real cost to mistakes, a queue of people with limited time. But once you've learned to see a decision layer, you start seeing them everywhere. There's one behind the support inbox, the fraud check on your card, the moderation queue on every social network, and the triage desk at a hospital.
  - After: It isn't. Kestrel's SOC was a teaching example. We chose it because it has everything: lots of decisions, a real cost to mistakes, and a queue of people with limited time. But once you've learned to see a decision layer, you start seeing them everywhere. There's one behind a support inbox and one behind the fraud check on your card. There's one behind the queue of posts a social network reviews, and one at the triage desk in a hospital.
- `chapters/ch19.qmd`
  - Before: This chapter is a short tour. For each stop, the same few questions: what does the model read, what does it answer, where does the line go, and who makes the final call?
  - After: This chapter is a short tour. At each stop we ask the same four questions. What does the model read? What does it answer? Where does the threshold go? And who makes the final call?
- `chapters/ch19.qmd`
  - Before: - Use the Chapter 4 line to see why the same model gets very different thresholds in different jobs.
  - After: - Use the Chapter 4 formula to see why the same model gets very different thresholds in different jobs.
- `chapters/ch19.qmd`
  - Before: Look across @fig-cards and notice how little changes from card to card. Each has a state: a ticket, a post, a transaction, a claim, a nurse's note, a diff. Each asks two or three typed questions. And each choice has an escape hatch: "other", "none", "needs more info", "not enough information". Chapter 10 showed what happens without one. The model spreads all its belief across the options you gave it, and cases that fit none of them get confidently mislabelled.
  - After: Look across @fig-cards and notice how little changes from card to card. Each has a state: a ticket, a post, a transaction, a claim, a nurse's note, or a code change. Each asks two or three typed questions. And each choice has an escape option: "other", "none", "needs more info" or "not enough information". Chapter 10 showed what happens without one. The model spreads all its belief across the options you gave it. Cases that fit none of them get a wrong label with high confidence.
- `chapters/ch19.qmd`
  - Before: @fig-domains places each domain on two axes, and they tell a story. At the bottom right, content moderation and payment fraud involve millions of decisions a day, each of which costs little if it's wrong. No team of people could look at them all, so the model decides, and people audit a sample, the way Kestrel audited its auto-closed alerts.
  - After: @fig-domains places each domain on two axes, and together they tell a story. At the bottom right are content moderation and payment fraud. They involve millions of decisions a day, and each one costs little if it's wrong. No team of people could look at them all. So the model decides, and people audit a sample, the way Kestrel audited its auto-closed alerts.
- `chapters/ch19.qmd`
  - Before: At the top left, clinical intake involves a few hundred decisions a day, and a missed emergency is catastrophic. There, the model should never close a case. Its job is to put the right patient at the top of the list.
  - After: At the top left is clinical intake, where a hospital decides who needs care first. It involves a few hundred decisions a day, and a missed emergency is a disaster. There, the model should never close a case. Its job is to put the right patient at the top of the list.
- `chapters/ch19.qmd`
  - Before: Every number in that chart is an assumption, chosen to be plausible for a mid-sized organisation. The shape is what matters: the further up and to the left a decision sits, the more a person belongs in the loop.
  - After: Every number in that chart is an assumption, chosen to be realistic for a mid-sized organisation. The shape is what matters. The further up and to the left a decision sits, the more a person belongs in the loop.
- `chapters/ch19.qmd`
  - Before: ## The same formula, very different lines
  - After: ## The same formula, very different thresholds
- `chapters/ch19.qmd`
  - Before: This surprises people. The line where you should start treating a case as a problem is set by the same formula in every domain, the one from Chapter 4: the cost of a false alarm, divided by the false alarm plus the miss.
  - After: This surprises people. In every domain, the same formula sets the threshold where you should start treating a case as a problem. It's the formula from Chapter 4: the cost of a false alarm, divided by the cost of a false alarm plus the cost of a miss.
- `chapters/ch19.qmd`
  - Before: For support tickets, a missed urgent ticket costs a bit of goodwill, and a false "urgent" costs a few minutes. The line lands near 5%. For clinical intake, a missed emergency costs vastly more than an unnecessary fast-track, and the line drops to about 0.3% (@fig-lines).
  - After: For support tickets, a missed urgent ticket costs a little customer goodwill, and a false "urgent" costs a few minutes. The threshold lands near 5%. For clinical intake, a missed emergency costs far more than moving a patient forward who didn't need it. So the threshold drops to about 0.3% (@fig-lines).
- `chapters/ch19.qmd`
  - Before: A line that low means a lot of flagging, which is fine: flagging is cheap. What it demands is honest probabilities down in the fractions of a percent, which is where Chapter 5 said big models are least reliable, and where Chapter 11's calibration checks matter most.
  - After: A threshold that low means a lot of flagging, which is fine: flagging is cheap. But it needs probabilities that are calibrated even below one percent. That's where Chapter 5 said big models are least reliable, and where Chapter 11's calibration checks matter most.
- `chapters/ch19.qmd`
  - Before: The formula never changes. The costs do, and they move the line by more than an order of magnitude.
  - After: The formula never changes. The costs do, and they can move the threshold by a factor of ten or more.
- `chapters/ch19.qmd`
  - Before: Let's take one stop and actually run it: support tickets. I generated {{< num ch26 n_tickets int >}} synthetic tickets, each with a known team and a known answer to "does this need a reply today?", and asked the mock.
  - After: Let's take one stop and actually run it: support tickets. I made {{< num ch26 n_tickets int >}} synthetic tickets. Each has a known team and a known answer to "does this need a reply today?". Then I asked the mock.
- `chapters/ch19.qmd`
  - Before: The mock routed {{< num ch26 topic_acc pct >}} of tickets to the right team. Billing was perfect. Account problems went to the right place only {{< num ch26 per_topic.account pct >}} of the time; login trouble kept landing in "technical" (@fig-tickets). And its answers to "does this need a reply today?" barely ranked the urgent tickets above the rest, with an AUC of {{< num ch26 urgent_auc f2 >}}.
  - After: The mock sent {{< num ch26 topic_acc pct >}} of tickets to the right team. Billing was perfect. Account problems went to the right place only {{< num ch26 per_topic.account pct >}} of the time; login trouble kept landing in "technical" (@fig-tickets). Its answers to "does this need a reply today?" were weak too. They barely ranked the urgent tickets above the rest, with an AUC of {{< num ch26 urgent_auc f2 >}}.
- `chapters/ch19.qmd`
  - Before: The reason is a little embarrassing: outside the SOC, the book's mock is a simple word-matcher, and "I can't log in" shares words with "the app isn't working". Real Jev would do better or worse; I can't say which. What I can say is that you'd only know by measuring, and the test took twenty lines.
  - After: The reason is simple. Outside the SOC, the book's mock only matches words, and "I can't log in" shares words with "the app isn't working". Real Jev would do better or worse; I can't say which. What I can say is that you'd only know by measuring, and the test took twenty lines of code.
- `chapters/ch19.qmd`
  - Before: Two things rescue the situation, and neither needs a better model. First, route only when sure: routing tickets only when the top label's probability was at least 0.6 covered {{< num ch26 cov60 pct >}} of them and got {{< num ch26 acc60 pct >}} right, with the rest going to a person. Second, fix the options. "Technical" and "account" overlap, and Chapter 10 warned that overlapping options split belief. Sharper descriptions, or a separate noul for "is this about signing in?", are the first thing to try.
  - After: Two things fix most of the problem, and neither needs a better model. First, route a ticket only when the model is sure. We routed tickets only when the top label's probability was at least 0.6. That covered {{< num ch26 cov60 pct >}} of them and got {{< num ch26 acc60 pct >}} right; the rest went to a person. Second, fix the options. "Technical" and "account" overlap, and Chapter 10 warned that overlapping options split belief. Try clearer descriptions first, or a separate noul for "is this about signing in?".
- `chapters/ch19.qmd`
  - Before: In the red domains, the design flips. The model doesn't close anything. It reads every case, estimates the probabilities that matter, and orders the queue, so that a person sees the likeliest emergencies first (@fig-human-final). Chapter 18 showed that ordering alone can cut the wait for a real threat from hours to minutes. In a hospital, that's where the value lies.
  - After: In the red domains, the design is the other way round. The model doesn't close anything. It reads every case, estimates the probabilities that matter, and orders the queue. That way a person sees the likeliest emergencies first (@fig-human-final). Chapter 18 showed that ordering alone can cut the wait for a real threat from hours to minutes. In a hospital, that's where the value is.
- `chapters/ch19.qmd`
  - Before: Keep the log. When the model says 0.4 and the clinician says "routine", and the clinician is right, that's a label. When the model says 0.4 and the clinician says "routine" and is wrong, that's a lesson. Either way it's evidence for the next calibration check.
  - After: Keep the log. Say the model says 0.4, the clinician says "routine", and the clinician is right: that's a label. If the clinician is wrong, that's a lesson. Either way, it's evidence for the next calibration check.
- `chapters/ch19.qmd`
  - Before: Some decisions also carry legal weight. Lending, hiring, benefits and medical decisions face rules in many places about automated decision-making and the right to a human review. I'm not a lawyer, and this isn't legal advice. But the design above, a person deciding with the model as an assistant and every step logged, is the one most likely to survive a question from a regulator.
  - After: Some decisions also carry legal weight. In many places, lending, hiring, benefits and medical decisions face rules about automated decision-making and the right to a human review. I'm not a lawyer, and this isn't legal advice. But one design is the most likely to satisfy a regulator: a person decides, the model assists, and every step is logged.
- `chapters/ch19.qmd`
  - Before: Not everything is a decision layer. @fig-fit is a quick checklist for telling the two apart. If there are many similar cases a day, a fixed set of answers, outcomes you can eventually learn from, and a cost you can put on a mistake, it's a good fit. If the problem is a one-off, the answer has to be written, there are no labels, or the job needs a plan rather than a verdict, it's the wrong tool. That's the System 2 work from Chapter 8, and it still belongs to people and to slower models.
  - After: Not everything is a decision layer. @fig-fit is a quick checklist for telling the two apart. It's a good fit when there are many similar cases a day and a fixed set of answers. You should also be able to learn the outcomes in time, and put a cost on a mistake. It's the wrong tool when the problem happens only once, or when the answer has to be written. It's also wrong when there are no labels, or when the job needs a plan rather than a verdict. That's the System 2 work from Chapter 8, and it still belongs to people and to slower models.
- `chapters/ch19.qmd`
  - Before: Every volume and cost in this chapter is an illustrative assumption; your organisation's will differ, sometimes by orders of magnitude, and the lines move with them. The support-ticket demo uses the mock's general-purpose engine, which is a word-matcher, so its weak numbers say nothing about real Jev in either direction. And "a person decides" only protects anyone if the person has time to think. A clinician who must approve four hundred model suggestions an hour isn't deciding; they're clicking. Watch the load on the humans in the loop as carefully as the model.
  - After: Every volume and cost in this chapter is an illustrative assumption. Your organisation's numbers will be different, sometimes by a factor of a hundred, and the thresholds move with them. The support-ticket demo uses the mock's general engine, which only matches words. So its weak numbers say nothing about real Jev, good or bad. And "a person decides" only protects anyone if the person has time to think. A clinician who must approve four hundred model suggestions an hour isn't deciding; they're just clicking. Watch the workload of the people in the loop as carefully as you watch the model.
- `chapters/ch19.qmd`
  - Before: An online shop wants to auto-approve refunds under \$50. A wrongly approved fraudulent refund costs the refund; a wrongly refused honest one costs about \$30 in support time and some goodwill, which the team values at another \$40. For a \$40 refund, at what P(fraud) should the model refuse and send it to a person instead?
  - After: An online shop wants to approve refunds under \$50 automatically. Approving a fraudulent refund by mistake costs the refund. Refusing an honest one by mistake costs about \$30 in support time, plus lost goodwill, which the team values at another \$40. For a \$40 refund, at what P(fraud) should the model refuse and send it to a person instead?
- `chapters/ch19.qmd`
  - Before: (A wrong approval costs \$40; a wrong refusal costs about \$70. Send it to a person when P(fraud) is above 70 ÷ 110, about 64%. A high line, and rightly so: for small refunds, occasionally paying a fraudster is cheaper than annoying honest customers. For a \$500 refund the same arithmetic gives about 12%.)
  - After: (A wrong approval costs \$40; a wrong refusal costs about \$70. Send it to a person when P(fraud) is above 70 ÷ 110, about 64%. That's a high threshold, and rightly so: for small refunds, sometimes paying a fraudster is cheaper than annoying honest customers. For a \$500 refund, the same arithmetic gives about 12%.)
- `chapters/ch19.qmd`
  - Before: Maslow was talking about scientists and their methods [@maslow1966]. It's a fair warning for this chapter too. Once you've learned to see decision layers, it's tempting to see nothing else. The checklist in @fig-fit is there to stop you reaching for it by habit.
  - After: Maslow was talking about scientists and their methods [@maslow1966]. It's a fair warning for this chapter too. Once you've learned to see decision layers, it's tempting to see nothing else. The checklist in @fig-fit is there to stop you using one out of habit.
- `chapters/ch19.qmd`
  - Before: We toured six decision layers and found the same parts in every one: a state, a few typed questions, and an option for what fits nowhere. What changed from job to job was who decides. Where decisions are many and cheap, the model decides and people audit. Where they're few and costly, the model orders the queue and a person decides. The Chapter 4 formula put the line anywhere from 5% to 0.3%, depending only on costs. And running one stop for real, support tickets, showed why you measure first: the mock that did well at Kestrel stumbled on a new kind of text, and routing only when it was sure recovered most of the damage.
  - After: We toured six decision layers and found the same parts in every one: a state, a few typed questions, and an option for what fits nowhere. What changed from job to job was who decides. Where decisions are many and cheap, the model decides and people audit. Where they're few and costly, the model orders the queue and a person decides. The Chapter 4 formula put the threshold anywhere from 5% to 0.3%, depending only on costs. Then we ran one stop for real, support tickets, and saw why you measure first. The mock that did well at Kestrel did badly on a new kind of text. Routing only when it was sure fixed most of the damage.
- `chapters/ch19.qmd`
  - Before: 3. Using the threshold formula, find the refund amount at which the line in the box above crosses 50%.
  - After: 3. Using the threshold formula, find the refund amount at which the threshold in the box above reaches 50%.
- `chapters/ch19.qmd`
  - Before: 4. For clinical intake, list three things you'd log for every case so that, in a month, you could tell whether the model's probabilities were honest.
  - After: 4. For clinical intake, list three things you'd log for every case, so that in a month you could tell whether the model's probabilities were calibrated.

## Chapter 9: Inside Jev

31 changes.

- `chapters/ch09.qmd`
  - Before: A confession shapes this chapter: I've never called Jev.
  - After: I have to admit something that shapes this chapter: I've never called Jev.
- `chapters/ch09.qmd`
  - Before: When I wrote this book, Jev had been public for a couple of weeks, in early access, and I didn't have an API key. What I did have was TypeSafe's official Python library, which anyone can download and read, TypeSafe's public documentation, a stream of launch coverage and early commentary, and a growing pile of research papers from people who *had* used it.
  - After: When I wrote this book, Jev had been public for a couple of weeks, in early access, and I didn't have an API key. But I did have four things. I had TypeSafe's official Python library, which anyone can download and read, and TypeSafe's public documentation. I had the news coverage and early comments from the launch. And I had a growing number of research papers from people who *had* used it.
- `chapters/ch09.qmd`
  - Before: More than you'd think, and less than most articles imply. The trick is to sort every claim into one of three piles: what you can verify yourself, what the vendor says, and what nobody outside the company knows. That habit is worth more than any single fact in this chapter, because Jev won't be the last new model you have to evaluate from the outside.
  - After: More than you'd think, and less than most articles suggest. The trick is to sort every claim into one of three piles: what you can check yourself, what the vendor says, and what nobody outside the company knows. That habit is worth more than any single fact in this chapter. Jev won't be the last new model you have to judge from the outside.
- `chapters/ch09.qmd`
  - Before: **Vendor-reported** means TypeSafe, or coverage quoting TypeSafe, said it. It may well be true. It hasn't been independently checked here, and every such number carries that label.
  - After: **Vendor-reported** means TypeSafe said it, or an article quoting TypeSafe did. It may well be true. It hasn't been checked independently here, and every such number carries that label.
- `chapters/ch09.qmd`
  - Before: **Unknown** means it hasn't been published, so any statement about it is a guess, and I'll say so when I guess.
  - After: **Unknown** means it hasn't been published. Any statement about it is a guess, and I'll say so when I guess.
- `chapters/ch09.qmd`
  - Before: Treat every vendor number in this book as a claim to check, not a fact. A good habit: when a claim about a model appears without a pile attached, ask which pile it belongs in.
  - After: Treat every vendor number in this book as a claim to check, not a fact. Here's a good habit: when you see a claim about a model with no pile attached, ask which pile it belongs in.
- `chapters/ch09.qmd`
  - Before: Jev's interface is refreshingly small. You send one request to one endpoint, `POST /v1/systemone`, with three things:
  - After: Jev's interface is pleasantly small. You send one request to one address, `POST /v1/systemone`, with three things:
- `chapters/ch09.qmd`
  - Before: You don't have to take my word for the shape. This is the exchange as the SDK actually sends it. The mock records it on the way through.
  - After: You don't have to trust me about the shape. This is the exchange as the SDK actually sends it; the mock records it as it passes through.
- `chapters/ch09.qmd`
  - Before: A few details from the SDK and TypeSafe's documentation are worth knowing [@typesafedocs2026]. A `choice` answer includes the chosen label, a `confidence` and a probability for every label. A `score` answer includes an expected score, a `confidence`, the rubric as a legend and a probability for every level. A `noul` (yes or no) answer is a single number, the probability of "yes", with no `confidence` attached. The schema describes output tokens as "currently free of charge". And the library handles retries and rate limits for you, which Chapter 16 puts to use.
  - After: A few details from the SDK and TypeSafe's documentation are worth knowing [@typesafedocs2026]. A `choice` answer includes the chosen label, a `confidence` and a probability for every label. A `score` answer includes an expected score, a `confidence`, the scoring guide (the rubric) and a probability for every level. A `noul` (yes or no) answer is a single number: the probability of "yes", with no `confidence`. The schema describes output tokens as "currently free of charge". And the library handles retries and rate limits for you, which Chapter 16 uses.
- `chapters/ch09.qmd`
  - Before: What about `confidence`? TypeSafe's documentation describes it as a statistic computed from the *shape* of the answer's probabilities: high when they're piled on one option, low when they're spread across several. It doesn't publish the formula. Its quick-start example shows why that matters: a support ticket goes to "technical" with probability 0.85, and the answer's confidence is 0.78. So real confidence isn't simply the top probability. The book's mock uses that simplest stand-in anyway, the top option's probability, and the repository's `docs/mock-design.md` says so. With a real key, read the `probabilities` and test `confidence` on your own labels before you set a threshold on it.
  - After: What about `confidence`? TypeSafe's documentation describes it as a number computed from the *shape* of the answer's probabilities. It's high when the probability is mostly on one option, and low when it's spread across several. The formula isn't published. Its quick-start example shows why that matters: a support ticket goes to "technical" with probability 0.85, and the answer's confidence is 0.78. So real confidence isn't simply the top probability. The book's mock uses the simplest stand-in anyway, the top option's probability, and the repository's `docs/mock-design.md` says so. With a real key, read the `probabilities`, and test `confidence` on your own labels before you set a threshold on it.
- `chapters/ch09.qmd`
  - Before: Two claims sit at the centre of how TypeSafe describes Jev: a new architecture with a "parallel sampler", and a training method it calls RLCD [@typesafe2026; @typesafedocs2026].
  - After: Two claims are at the centre of how TypeSafe describes Jev. One is a new design with a "parallel sampler". The other is a training method it calls RLCD [@typesafe2026; @typesafedocs2026].
- `chapters/ch09.qmd`
  - Before: **A "parallel sampler".** An LLM, as Chapter 6 showed, writes one token at a time, each waiting for the last. TypeSafe says Jev instead produces all its outputs *in a single pass*. It doesn't write an answer; it computes one. TypeSafe presents this as the source of the speed. According to the documentation, each question in a call is answered separately but at the same time, all against the same state, which is why asking a few more questions hardly slows a call down [@typesafedocs2026].
  - After: **A "parallel sampler".** As Chapter 6 showed, an LLM writes one token at a time, and each token waits for the one before. TypeSafe says Jev instead produces all its outputs *in a single pass*. It doesn't write an answer; it computes one. TypeSafe says this is where the speed comes from. According to the documentation, each question in a call is answered separately but at the same time, all from the same state. That's why asking a few more questions hardly slows a call down [@typesafedocs2026].
- `chapters/ch09.qmd`
  - Before: **RLCD: reinforcement learning for calibrated decisions.** TypeSafe contrasts this with RLHF, which rewards answers people prefer (Chapter 5), and with reinforcement learning from verifiable rewards, which rewards answers a program can check. RLCD, they say, rewards *honest probabilities*.
  - After: **RLCD: reinforcement learning for calibrated decisions.** TypeSafe compares this with RLHF, which rewards answers people prefer (Chapter 5). It also compares it with reinforcement learning from verifiable rewards, which rewards answers a program can check. RLCD, they say, rewards *calibrated* probabilities: honest ones.
- `chapters/ch09.qmd`
  - Before: We don't know the details of either. But you already have the background to think about them clearly. Chapter 2 showed that a **proper scoring rule**, like log loss, makes honesty the best possible strategy: you can't improve your average score by exaggerating. If RLCD's reward is built on a rule like that, calibration is what it would be pushing towards. That's an inference, not something TypeSafe has published, and it still wouldn't guarantee calibration on *your* data, as Chapter 11 will show.
  - After: We don't know the details of either claim. But you already know enough to think about them clearly. Chapter 2 showed that with a **proper scoring rule**, like log loss, honesty is the best strategy: you can't improve your average score by exaggerating. If RLCD's reward is built on a rule like that, it would push the model towards calibration. That's my own reasoning, not something TypeSafe has published. And it still wouldn't guarantee calibration on *your* data, as Chapter 11 will show.
- `chapters/ch09.qmd`
  - Before: If you want a mental model, @fig-guess is mine, and I want to be very clear that it's a guess. It's built from what the interface demands and from what Chapter 5 said about readers and writers. You can also build it yourself, and Chapter 20 does.
  - After: If you want a picture in your head, @fig-guess is mine. I want to be very clear that it's a guess. It's built from what the interface needs and from what Chapter 5 said about readers and writers. You can also build it yourself, and Chapter 20 does.
- `chapters/ch09.qmd`
  - Before: TypeSafe and its launch coverage report end-to-end latency of roughly 70 to 500 milliseconds, and "two orders of magnitude" faster than LLMs on System One tasks. Both are vendor-reported.
  - After: TypeSafe and the launch articles report a total response time (latency) of about 70 to 500 milliseconds. They also say Jev is "two orders of magnitude", about a hundred times, faster than LLMs on System One tasks. Both claims are vendor-reported.
- `chapters/ch09.qmd`
  - Before: One critic pointed out that the most dramatic speed multipliers in the launch material compare Jev with slow *reasoning* models, which think for a long time before answering [@regolo2026]. Fair for some uses, unfair for others. Against a fast, non-reasoning LLM asked for a one-word label, the gap is much smaller. Always ask: faster than *what*, doing *what*?
  - After: One critic pointed out a problem with the biggest speed claims in the launch material. They compare Jev with slow *reasoning* models, which think for a long time before answering [@regolo2026]. That comparison is fair for some uses and unfair for others. Against a fast LLM that doesn't reason, asked for a one-word label, the gap is much smaller. Always ask: faster than *what*, doing *what*?
- `chapters/ch09.qmd`
  - Before: The price is where the story gets interesting. The listed price is \$0.042 per million input tokens, with output free. For a decision that reads about 500 tokens of state and questions, that's about \${{< num ch16 jev_cost_per_million int >}} per million decisions.
  - After: The price is the most interesting part. The listed price is \$0.042 per million input tokens, and output is free. Suppose a decision reads about 500 tokens of state and questions. Then a million decisions cost about \${{< num ch16 jev_cost_per_million int >}}.
- `chapters/ch09.qmd`
  - Before: Using this book's illustrative LLM prices (\${{< num ch16 llm_price_in f2 >}} per million input tokens, \${{< num ch16 llm_price_out f2 >}} per million output, and 40 output tokens for a small JSON answer), the same million decisions would cost about \${{< num ch16 llm_cost_per_million int >}}. Roughly {{< num ch16 ratio int >}} times more (@fig-cost). Real LLM prices range over two orders of magnitude, so treat the ratio as a shape. Chapter 12 is about why that shape might matter more than any benchmark.
  - After: Now use this book's illustrative LLM prices: \${{< num ch16 llm_price_in f2 >}} per million input tokens, \${{< num ch16 llm_price_out f2 >}} per million output tokens, and 40 output tokens for a small JSON answer. The same million decisions would cost about \${{< num ch16 llm_cost_per_million int >}}, roughly {{< num ch16 ratio int >}} times more (@fig-cost). Real LLM prices vary by a factor of a hundred, so treat the ratio as a rough size, not an exact number. Chapter 12 explains why that size might matter more than any benchmark.
- `chapters/ch09.qmd`
  - Before: Take one habit away from this chapter. When a vendor gives you several numbers, see whether they agree with *each other*.
  - After: If you remember one habit from this chapter, make it this one. When a vendor gives you several numbers, check whether they agree with *each other*.
- `chapters/ch09.qmd`
  - Before: TypeSafe's launch demo had Jev playing the video game Doom, making decisions from a text description of the game state about ten times a second, at a reported cost of about \$7 an hour. Do those numbers hang together with the listed price?
  - After: In TypeSafe's launch demo, Jev played the video game Doom. It made decisions from a text description of the game, about ten times a second, at a reported cost of about \$7 an hour. Do those numbers fit with the listed price?
- `chapters/ch09.qmd`
  - Before: Ten decisions a second is {{< num ch16 doom_decisions_per_hour int >}} an hour. At \$7 an hour, each decision costs about \${{< num ch16 doom_cost_per_decision f4 >}}. At \$0.042 per million input tokens, that implies about {{< num ch16 doom_implied_tokens int >}} tokens of game state per decision. Plausible, for a detailed text description of a game screen (@fig-doom-check). The numbers are consistent. That doesn't prove them, but if they'd implied three tokens per decision, or three million, you'd have learned something important.
  - After: Ten decisions a second is {{< num ch16 doom_decisions_per_hour int >}} an hour. At \$7 an hour, each decision costs about \${{< num ch16 doom_cost_per_decision f4 >}}. At \$0.042 per million input tokens, that means about {{< num ch16 doom_implied_tokens int >}} tokens of game description per decision. That's believable for a detailed text description of a game screen (@fig-doom-check). The numbers agree with each other. That doesn't prove them. But if they had meant three tokens per decision, or three million, you'd have learned something important.
- `chapters/ch09.qmd`
  - Before: Now the uncomfortable part: the unknowns are the very things a decision layer depends on.
  - After: Now the uncomfortable part: the unknowns are exactly what a decision layer depends on.
- `chapters/ch09.qmd`
  - Before: We don't know the model's size, its architecture or its training data. We don't know how well its probabilities are calibrated on data like yours. We don't know how it behaves on adversarial input, like the planted sentence from Chapter 7. We don't know how stable its behaviour is across versions: `jev-latest` is an alias, and aliases move. And by design, it gives no reasons, only probabilities. Some early critics called that a compliance problem for regulated uses [@datacamp2026]. Chapter 14 will answer it with decision logs that audit the policy rather than the model.
  - After: We don't know the model's size, its design or its training data. We don't know how well its probabilities are calibrated on data like yours. We don't know how it behaves on input written by an attacker, like the planted sentence from Chapter 7. We don't know how much its behaviour changes between versions: `jev-latest` is a nickname that can point to a new version at any time. And by design, it gives no reasons, only probabilities. Some early critics said that's a problem for regulated uses [@datacamp2026]. Chapter 14 answers it with decision logs that audit the policy rather than the model.
- `chapters/ch09.qmd`
  - Before: None of those unknowns are reasons to avoid a new model. They're reasons to *test* it, on your own data, with the tools you already have. The next two chapters do just that: first by understanding each question type properly, then by testing calibration the way Chapter 3 taught.
  - After: None of those unknowns are reasons to avoid a new model. They're reasons to *test* it, on your own data, with the tools you already have. The next two chapters do just that. First we look at each question type properly. Then we test calibration the way Chapter 3 taught.
- `chapters/ch09.qmd`
  - Before: Vendor numbers are measured on the vendor's tasks, in the vendor's setup, against comparisons the vendor chose. Early-access models change quickly, so behaviour you test this month may shift next month. Pin a model version where you can, rather than `jev-latest`, and re-run your checks when it changes. And be wary of third-party "benchmarks" that appeared within days of launch: some are careful, some aren't, and most can't tell you how the model behaves on your data.
  - After: Vendor numbers are measured on the vendor's tasks, in the vendor's setup, against comparisons the vendor chose. Early-access models change quickly, so behaviour you test this month may change next month. Use a fixed model version where you can, rather than `jev-latest`, and run your checks again when it changes. And be careful with "benchmarks" from other people that appeared within days of the launch. Some are careful and some aren't, and most can't tell you how the model behaves on your data.
- `chapters/ch09.qmd`
  - Before: Kestrel's agent makes about 3,700 small decisions a day (Chapter 7's count, scaled up). At the vendor-reported price and 500 tokens each, what would a year of those decisions cost? At the illustrative LLM price? At what daily volume would the difference be worth a week of an engineer's time to switch?
  - After: Kestrel's agent makes about 3,700 small decisions a day (Chapter 7's count, scaled up). At the vendor-reported price and 500 tokens each, what would a year of those decisions cost? What would they cost at the illustrative LLM price? At what daily volume would the saving pay for a week of an engineer's time to switch?
- `chapters/ch09.qmd`
  - Before: (About 1.35 million decisions a year: roughly \$28 at the Jev price and about \$900 at the illustrative LLM price. At Kestrel's volume, price alone doesn't justify a switch. Speed and calibration might. At a hundred times the volume, price becomes a real argument.)
  - After: (About 1.35 million decisions a year: roughly \$28 at the Jev price and about \$900 at the illustrative LLM price. At Kestrel's volume, price alone isn't a reason to switch. Speed and calibration might be. At a hundred times the volume, price becomes a real reason.)
- `chapters/ch09.qmd`
  - Before: I started without an API key, so we sorted what can be known into three piles. The interface was verifiable, and small: state and typed questions in, probabilities out. The speed and training method were the vendor's claims, and we could reason about them without accepting them. The prices let us do our own arithmetic, and the vendor's numbers turned out to agree with each other. What remained unknown was what a decision layer depends on most, which means the next job is testing.
  - After: I started without an API key, so we sorted what can be known into three piles. The interface could be checked, and it was small: state and typed questions in, probabilities out. The speed and the training method were the vendor's claims. We could reason about them without accepting them. The prices let us do our own arithmetic, and the vendor's numbers turned out to agree with each other. What stayed unknown was what a decision layer depends on most. So the next job is testing.
- `chapters/ch09.qmd`
  - Before: 2. In the lab, send a `score` question with five levels instead of three. Look at the raw response. What does `score` mean when it's 2.4?
  - After: 2. In the lab, send a `score` question with five levels instead of three. Look at the raw response. What does `score` mean when its value is 2.4?
- `chapters/ch09.qmd`
  - Before: Next: the three question types, `choice`, `score` and `noul`, one at a time, with the design choices that make each work well.
  - After: Next: the three question types, `choice`, `score` and `noul`, one at a time, and the design choices that make each one work well.

## Chapter 11: Testing Jev's calibration yourself

33 changes.

- `chapters/ch11.qmd`
  - Before: A week after Jev launched, two claims were circling.
  - After: A week after Jev launched, people were repeating two claims.
- `chapters/ch11.qmd`
  - Before: TypeSafe's: Jev returns *calibrated* probabilities. Its training method, RLCD, is named after that goal [@typesafe2026].
  - After: The first was TypeSafe's: Jev returns *calibrated* probabilities. Its training method, RLCD, is named after that goal [@typesafe2026].
- `chapters/ch11.qmd`
  - Before: And a blunt reply from the data scientist Alex Molas, in a post titled "Jev can't be calibrated": useful, yes, but treat its outputs as scores, not probabilities, because calibration depends on *your* data, which Jev never sees [@molas2026].
  - After: The second was a direct reply from the data scientist Alex Molas, in a post titled "Jev can't be calibrated". Jev is useful, he said, but treat its outputs as scores, not probabilities. Calibration depends on *your* data, and Jev never sees your data [@molas2026].
- `chapters/ch11.qmd`
  - Before: Both, and neither, and that's the point of this chapter. You already have everything you need to settle it for your own use: Chapter 3's reliability diagram, a few hundred labelled cases, and an afternoon. This chapter shows why the critic's argument is right in a precise sense, how to measure it, and how to fix it when it bites.
  - After: Both, and neither, and that's the point of this chapter. You already have everything you need to answer it for your own use: Chapter 3's reliability diagram, a few hundred labelled cases, and an afternoon. This chapter shows in what exact sense the critic is right. It shows how to measure the problem, and how to fix it when it happens.
- `chapters/ch11.qmd`
  - Before: Chapter 2 said a probability is a claim about *how often, among cases like this one*. Now imagine two companies send Jev the same alert text. Jev, reading the same input, returns the same probability to both. But suppose one company is a frequent target and the other rarely is. Among alerts that look exactly like this one, the true share of attacks can differ between them. A single number can't be right for both.
  - After: Chapter 2 said a probability is a claim about *how often, among cases like this one*. Now imagine two companies send Jev the same alert text. Jev reads the same input, so it returns the same probability to both. But suppose one company is attacked often and the other rarely. Among alerts that look exactly like this one, the true share of attacks can be different at the two companies. A single number can't be right for both.
- `chapters/ch11.qmd`
  - Before: That's the base-rate trap from Chapter 2, turned on the model. It's called *prior shift* or *label shift*: the mix of outcomes changes while the way each outcome looks stays the same. A model trained or tuned on one mix can be perfectly calibrated there, and systematically off everywhere the mix is different.
  - After: That's the base-rate trap from Chapter 2, now catching the model. It's called *prior shift* or *label shift*: the mix of outcomes changes, but the way each outcome looks stays the same. A model trained or tuned on one mix can be perfectly calibrated there. But it will be wrong in the same direction everywhere the mix is different.
- `chapters/ch11.qmd`
  - Before: Let's see it happen. Alongside Kestrel Logistics I've generated a second synthetic company, Harbor Pharma. Its alerts come from the same detectors and look the same, but real attacks are less common there: {{< num ch18 harbor_base pct1 >}} of alerts, against Kestrel's {{< num ch18 kestrel_base pct1 >}}.
  - After: Let's see it happen. Next to Kestrel Logistics, I've made a second synthetic company, Harbor Pharma. Its alerts come from the same detectors and look the same. But real attacks are less common there: {{< num ch18 harbor_base pct1 >}} of alerts, against Kestrel's {{< num ch18 kestrel_base pct1 >}}.
- `chapters/ch11.qmd`
  - Before: At Kestrel, the ECE is {{< num ch18 ece_kestrel f3 >}}. At Harbor, it's {{< num ch18 ece_harbor f3 >}}, and the direction is consistent: Harbor's average predicted risk is {{< num ch18 harbor_mean_p pct1 >}} when the real attack rate is {{< num ch18 harbor_base pct1 >}}. Put Chapter 14's act line on those numbers and Harbor sends roughly twice as many alerts to review as it needs to (@fig-two-companies).
  - After: At Kestrel, the ECE is {{< num ch18 ece_kestrel f3 >}}. At Harbor, it's {{< num ch18 ece_harbor f3 >}}, and the error always goes the same way. Harbor's average predicted risk is {{< num ch18 harbor_mean_p pct1 >}} when the real attack rate is {{< num ch18 harbor_base pct1 >}}. Use Chapter 14's act threshold on those numbers, and Harbor sends about twice as many alerts to review as it needs to (@fig-two-companies).
- `chapters/ch11.qmd`
  - Before: As always, the mock is synthetic and I built Harbor to make the point cleanly. I can't tell you how much real Jev's calibration varies between real companies. What I can tell you is that the mechanism is general, and it applies to every model that returns probabilities without seeing your base rate.
  - After: As always, the mock is synthetic, and I built Harbor to show the point clearly. I can't tell you how much real Jev's calibration varies between real companies. What I can tell you is that the cause is general. It applies to every model that returns probabilities without seeing your base rate.
- `chapters/ch11.qmd`
  - Before: The good news is very good. This kind of miscalibration is often easy to fix.
  - After: The good news is very good: this kind of miscalibration is often easy to fix.
- `chapters/ch11.qmd`
  - Before: **Adjust for the base rate.** If the model's probabilities were right for one base rate, and you know yours, you can correct them with one line of arithmetic. Multiply the odds by the ratio of the two base rates' odds. That's Bayes' rule from Chapter 2 again: the new evidence is the same, only the starting point moved [@saerens2002].
  - After: **Adjust for the base rate.** Suppose the model's probabilities were right for one base rate, and you know yours. Then you can correct them with one line of arithmetic: multiply the odds by the ratio of the two base rates' odds. That's Bayes' rule from Chapter 2 again. The evidence is the same; only the starting point moved [@saerens2002].
- `chapters/ch11.qmd`
  - Before: With the base rate known exactly, the odds adjustment brings Harbor's ECE down to {{< num ch18 ece_prior_known f3 >}}. With the base rate *estimated* from just 300 labelled alerts, it gets {{< num ch18 ece_prior_est f3 >}}. Platt scaling fitted on the same 300 labels does best of all, {{< num ch18 ece_platt300 f3 >}} (@fig-harbor-fixes), because it can correct a stretch as well as a shift.
  - After: With the base rate known exactly, the odds adjustment brings Harbor's ECE down to {{< num ch18 ece_prior_known f3 >}}. With the base rate *estimated* from just 300 labelled alerts, it gets {{< num ch18 ece_prior_est f3 >}}. Platt scaling fitted on the same 300 labels does best of all, {{< num ch18 ece_platt300 f3 >}} (@fig-harbor-fixes). That's because it can correct probabilities that are too spread out or too bunched together, not only ones that are all too high.
- `chapters/ch11.qmd`
  - Before: The adjustment rests on an assumption: that alerts of each kind look the same at both places, and only how common each kind is has changed. When that's not true, when your attackers use different techniques or your detectors fire differently, only fitting on your own labels will do. One more reason the labels matter.
  - After: The adjustment depends on one assumption: alerts of each kind look the same at both places, and only how common each kind is has changed. Sometimes that's not true. Your attackers may use different methods, or your detectors may fire differently. Then only fitting on your own labels will work. That's one more reason the labels matter.
- `chapters/ch11.qmd`
  - Before: "A few hundred labels" is the answer I've been giving. It's time to be precise, because small samples play a nasty trick on calibration measurements.
  - After: "A few hundred labels" is the answer I've been giving. It's time to be exact, because small samples can badly mislead calibration measurements.
- `chapters/ch11.qmd`
  - Before: Take the mock at Kestrel, whose ECE on all 20,000 alerts is {{< num ch18 ece_full f3 >}}. Now pretend you only had a random 100 labelled alerts, and measure ECE on those. Do it 200 times with different random samples.
  - After: Take the mock at Kestrel. Its ECE on all 20,000 alerts is {{< num ch18 ece_full f3 >}}. Now pretend you only had 100 labelled alerts, chosen at random, and measure ECE on those. Do it 200 times, with different random samples.
- `chapters/ch11.qmd`
  - Before: With 100 labels, the typical measured ECE is {{< num ch18 ece_n100 f3 >}}, over three times the real value, and one sample in twenty reads as high as {{< num ch18 ece_n100_hi f3 >}} (@fig-ece-noise). That isn't the model being worse; it's the measurement. With few cases per bin, every bin's observed rate wobbles, and ECE adds up the *size* of the wobbles regardless of direction, so noise always pushes it up. By 3,200 labels, the measurement is close to the truth.
  - After: With 100 labels, the typical measured ECE is {{< num ch18 ece_n100 f3 >}}, over three times the real value. One sample in twenty gives a value as high as {{< num ch18 ece_n100_hi f3 >}} (@fig-ece-noise). The model isn't worse; the measurement is. With few cases per bin, each bin's observed rate moves up and down by chance. ECE adds up the *size* of those random errors, whatever their direction, so noise always pushes it up. By 3,200 labels, the measurement is close to the truth.
- `chapters/ch11.qmd`
  - Before: The practical upshot is a trade-off. A few hundred labels are enough to *fix* a big, systematic problem like Harbor's base rate. Checking that a model is calibrated to within a percentage point or two takes a few thousand. Use `ece_interval()`, or plot the diagram with the counts showing, and let the range guide you.
  - After: In practice, this is a trade-off. A few hundred labels are enough to *fix* a big problem that always goes the same way, like Harbor's base rate. Checking that a model is calibrated to within a percentage point or two takes a few thousand. Use `ece_interval()`, or plot the diagram with the counts showing, and let the range guide you.
- `chapters/ch11.qmd`
  - Before: For a **choice**, start with the simplest version: is the top label's confidence calibrated? Among all the times the model's top label had confidence around 0.8, was it right about 80% of the time?
  - After: For a **choice**, start with the simplest version: is the top label's confidence calibrated? Take all the times the model's top label had confidence around 0.8. Was it right about 80% of the time?
- `chapters/ch11.qmd`
  - Before: For the mock's category answers, the top label's average confidence is {{< num ch18 top_conf_mean pct >}} and it's right {{< num ch18 top_acc pct >}} of the time, with an ECE of {{< num ch18 top_ece f3 >}} (@fig-top-label). Then go further: check each label's probability on its own (*is "phishing" at 0.3 right 30% of the time?*), especially the labels you act on.
  - After: For the mock's category answers, the top label's average confidence is {{< num ch18 top_conf_mean pct >}}. It's right {{< num ch18 top_acc pct >}} of the time, with an ECE of {{< num ch18 top_ece f3 >}} (@fig-top-label). Then go further. Check each label's probability on its own (*is "phishing" at 0.3 right 30% of the time?*), especially the labels you act on.
- `chapters/ch11.qmd`
  - Before: @fig-protocol is a routine for checking any model's probabilities before you trust them for a decision, and on a schedule afterwards.
  - After: @fig-protocol is a routine for checking any model's probabilities. Run it before you use them for a decision, and then again on a regular schedule.
- `chapters/ch11.qmd`
  - Before: 1. **Collect labels.** Recent cases with known outcomes, and a few thousand if you can get them. In a SOC, include random audits of auto-closed alerts, as Chapter 14 will insist, or your labels will only cover the cases people looked at.
  - After: 1. **Collect labels.** Use recent cases with known outcomes, a few thousand if you can get them. In a SOC, include random audits of auto-closed alerts, as Chapter 14 explains. Otherwise your labels will only cover the cases people looked at.
- `chapters/ch11.qmd`
  - Before: 2. **Plot, don't just score.** A reliability diagram with the counts showing, and ECE with a range. Look hardest near your thresholds.
  - After: 2. **Plot, don't just score.** Draw a reliability diagram with the counts showing, and report ECE with a range. Look most closely near your thresholds.
- `chapters/ch11.qmd`
  - Before: 3. **Slice.** Every group you'll act on differently: source, customer tier, language, region.
  - After: 3. **Slice.** Check every group you'll treat differently: source, customer tier, language, region.
- `chapters/ch11.qmd`
  - Before: 4. **Fix.** A base-rate adjustment if that's the problem and you know the rate; Platt or temperature scaling on your labels otherwise.
  - After: 4. **Fix.** Use a base-rate adjustment if that's the problem and you know the rate. Otherwise, use Platt or temperature scaling on your labels.
- `chapters/ch11.qmd`
  - Before: 5. **Re-test.** On a schedule, and whenever the model version or your data changes. Aliases like `jev-latest` can move under you.
  - After: 5. **Test again.** Do it on a schedule, and whenever the model version or your data changes. A name like `jev-latest` can point to a new version without warning.
- `chapters/ch11.qmd`
  - Before: So, back to the two claims. The vendor may well be right that Jev is calibrated on the data they tested it on. The critic is right that this doesn't make it calibrated on yours. The routine turns the argument into a measurement.
  - After: So, back to the two claims. The vendor may well be right that Jev is calibrated on the data they tested it on. The critic is right that this doesn't make it calibrated on yours. The routine turns the argument into something you can measure.
- `chapters/ch11.qmd`
  - Before: Labels are themselves imperfect. Analysts disagree, some attacks are never discovered, and labels arrive late: an alert closed today may turn out to be part of an intrusion found next month. Calibration measured on today's labels will look better than it is. Keep a "mature labels" set, cases old enough that their outcomes have settled, and measure on that. And be careful with labels that exist only because of the model's own decisions: if the model auto-closed a case, nobody labelled it, and your sample is biased towards the cases it sent to people.
  - After: Labels aren't perfect either. Analysts disagree, some attacks are never found, and labels arrive late. An alert closed today may turn out to be part of a break-in found next month. So calibration measured on today's labels will look better than it is. Keep a set of "mature labels": cases old enough that their outcomes are settled. Measure on that set. And be careful with labels that exist only because of the model's own decisions. If the model auto-closed a case, nobody labelled it. Your sample then leans towards the cases it sent to people.
- `chapters/ch11.qmd`
  - Before: Harbor adopts Kestrel's act line of 0.031 without checking calibration. Given that Harbor's probabilities run about twice too high, is Harbor's line effectively stricter or looser than Kestrel's? What happens to Harbor's review queue, and to its missed threats?
  - After: Harbor copies Kestrel's act threshold of 0.031 without checking calibration. Harbor's probabilities are about twice too high. So is Harbor's threshold, in effect, stricter or looser than Kestrel's? What happens to Harbor's review queue, and to its missed threats?
- `chapters/ch11.qmd`
  - Before: (Stricter. With inflated probabilities, fewer alerts fall below 0.031, so Harbor auto-closes less than it safely could. Its queue swells, and its missed threats go *down*, at the cost of analyst time it may not have. Fix the calibration, then recompute the line from Harbor's own costs.)
  - After: (Stricter. With probabilities that are too high, fewer alerts fall below 0.031, so Harbor auto-closes less than it safely could. Its queue grows, and its missed threats go *down*, but it costs analyst time Harbor may not have. Fix the calibration, then work out the threshold again from Harbor's own costs.)
- `chapters/ch11.qmd`
  - Before: De Finetti meant that probability isn't a physical property of the world, but a statement of belief given what you know. For a model, "what it knows" never includes your base rate, unless you tell it.
  - After: De Finetti meant that probability isn't a physical property of the world. It's a statement of belief, given what you know. For a model, "what it knows" never includes your base rate, unless you tell it.
- `chapters/ch11.qmd`
  - Before: Two claims collided, and we tested instead of taking sides. The same model was honest at one company and inflated at another, because a probability depends on its data as well as its model. A one-line odds adjustment or a few hundred labels fixed the gap. Then we found that a few hundred labels can't *prove* calibration, because small samples make good models look bad. What remains is a routine you can run on Jev or on anything else.
  - After: Two claims disagreed, and we tested instead of taking sides. The same model was calibrated at one company and too high at another, because a probability depends on its data as well as its model. A one-line odds adjustment, or a few hundred labels, fixed the gap. Then we found that a few hundred labels can't *prove* calibration, because small samples make good models look bad. What's left is a routine you can run on Jev or on any other model.
- `chapters/ch11.qmd`
  - Before: 4. Design the labelling plan for testing Jev's calibration at your organisation, or one you know: how many labels, from which cases, how you'd avoid only labelling what the model sent to people, and how often you'd repeat it.
  - After: 4. Plan how you'd collect labels to test Jev's calibration at your organisation, or one you know. How many labels, from which cases? How would you avoid labelling only what the model sent to people? How often would you repeat it?
- `chapters/ch11.qmd`
  - Before: Next: TypeSafe named the model after a Victorian economist who noticed something strange about coal. Chapter 12 is about why that might be the most important thing about it.
  - After: Next: TypeSafe named the model after a 19th-century economist who noticed something strange about coal. Chapter 12 explains why that might be the most important thing about it.

## Chapter 11 (continued)

1 changes.

- `chapters/ch11.qmd`
  - Before: For a **score**, check the probability of each tail you put a threshold on, such as P(severity is medium or high), just as you would a noul.
  - After: For a **score**, check the probability you put a threshold on, such as P(severity is medium or high). Test it just as you would test a noul.

## Chapter 21: Capstone

30 changes.

- `chapters/ch21.qmd`
  - Before: There's a moment in every project when the notebook works and someone asks, "Great. Can we run it on Monday?"
  - After: In every project, there's a moment when the notebook works and someone asks, "Great. Can we run it on Monday?"
- `chapters/ch21.qmd`
  - Before: That question is harder than anything in the notebook. A model that decides well on a laptop is not a service. A service has to answer at three in the morning when the API is slow, has to explain itself to an auditor a year later, and has to tell someone when the world has changed under it. And when you improve it, it has to change safely.
  - After: That question is harder than anything in the notebook. A model that decides well on a laptop is not a service. A service has to answer at three in the morning when the API is slow. It has to explain itself to an auditor a year later. It has to tell someone when the world has changed. And when you improve it, it has to change safely.
- `chapters/ch21.qmd`
  - Before: This chapter builds that service, in miniature, from pieces built across the book. It's under two hundred lines of Python, in `jevkit/service.py`. You could read it in one sitting, and I'd encourage you to.
  - After: This chapter builds a small version of that service from pieces built across the book. It's under two hundred lines of Python, in `jevkit/service.py`. You could read it all at once, and I'd encourage you to.
- `chapters/ch21.qmd`
  - Before: Read @fig-architecture-21 left to right, and you'll recognise every box. The state is built from trusted fields only, never the alert's free text, because Chapter 7 showed what a planted sentence can do. The three typed questions are Chapter 10's. The calibration is Chapter 11's. The policy, with its capacity, is Chapter 14's. The rest is what turns a pipeline into a service.
  - After: Read @fig-architecture-21 from left to right, and you'll recognise every box. The state is built from trusted fields only, never the alert's free text, because Chapter 7 showed what a planted sentence can do. The three typed questions are Chapter 10's. The calibration is Chapter 11's. The policy, with its capacity, is Chapter 14's. The rest is what turns a chain of steps into a service.
- `chapters/ch21.qmd`
  - Before: The first rule: *Everything that can change a decision lives in one place, with a version.*
  - After: The first rule is this: *everything that can change a decision lives in one place, with a version number.*
- `chapters/ch21.qmd`
  - Before: That means the model name, the calibration numbers, the two lines and every business rule, such as "never auto-close a critical asset". They all live in one small config object, and every decision the service makes is stamped with that config's version and a fingerprint of its contents.
  - After: That means the model name, the calibration numbers, the two thresholds and every business rule, such as "never auto-close a critical asset". They all live in one small config object. Every decision the service makes is stamped with that config's version and a fingerprint of its contents: a short code that changes if anything in it changes.
- `chapters/ch21.qmd`
  - Before: Why so strict? Because the question you'll be asked most often, months later, is "why did it do *that*?" If the answer depends on which calibration was live that week, you need to know which one was.
  - After: Why so strict? Because months later, the question you'll hear most is "why did it do *that*?" If the answer depends on which calibration was in use that week, you need to know which one it was.
- `chapters/ch21.qmd`
  - Before: Jev gives no reasons, only probabilities. Some early critics saw that as a problem for audits, and Chapter 14 answered it: audit the *policy*, not the model. The record in @fig-record is how. It holds the raw and calibrated probabilities, the lines they were compared with, the rule that fired and the version that decided. Together they make a complete, checkable explanation of every action, even though the model itself explains nothing.
  - After: Jev gives no reasons, only probabilities. Some early critics saw that as a problem for audits, and Chapter 14 answered it: audit the *policy*, not the model. The record in @fig-record is how. It holds the raw and calibrated probabilities, the thresholds they were compared with, the rule that fired, and the version that decided. Together they explain every action completely, in a way anyone can check, even though the model itself explains nothing.
- `chapters/ch21.qmd`
  - Before: Before the service touched anything, I ran it across the live week in a dry run, logging its decisions without acting on them. The monitor raised a flag on the first day: the review queue was over capacity.
  - After: Before the service touched anything, I ran it over the live week as a test, a "dry run". It logged its decisions without acting on them. The monitor raised a flag on the first day: the review queue was over capacity.
- `chapters/ch21.qmd`
  - Before: It shouldn't have been. The lines had been chosen, as in Chapter 14, to fit a queue of 240 a day. But after they were fitted, someone had added a sensible business rule: never auto-close an alert on a critical asset. Every alert that rule moved from "act" to "review" was extra work the lines hadn't budgeted for.
  - After: It shouldn't have been. As in Chapter 14, the thresholds had been chosen to fit a queue of 240 a day. But after they were fitted, someone added a sensible business rule: never auto-close an alert on a critical asset. Every alert that rule moved from "act" to "review" was extra work the thresholds hadn't allowed for.
- `chapters/ch21.qmd`
  - Before: ![Alerts sent to review each day of the live week, before and after the fix. Fitted without the critical-asset rule, the lines let the queue run over capacity every day. Fitted with it, the low line rises slightly and the queue fits.]
  - After: ![Alerts sent to review each day of the live week, before and after the fix. Fitted without the critical-asset rule, the thresholds let the queue run over capacity every day. Fitted with it, the act threshold rises slightly and the queue fits.]
- `chapters/ch21.qmd`
  - Before: The fix was to fit the lines *with* the rule in place, so the model's share of the queue shrinks to leave room for it. The low line moved from {{< num ch28 v1_low f3 >}} to {{< num ch28 v2_low f3 >}}, and the average queue went from about {{< num ch28 v1_mean_reviews int >}} to {{< num ch28 v2_mean_reviews int >}} a day (@fig-dry-run).
  - After: The fix was to fit the thresholds *with* the rule in place, so the model's share of the queue gets smaller and leaves room for the rule. The act threshold moved from {{< num ch28 v1_low f3 >}} to {{< num ch28 v2_low f3 >}}, and the average queue went from about {{< num ch28 v1_mean_reviews int >}} to {{< num ch28 v2_mean_reviews int >}} a day (@fig-dry-run).
- `chapters/ch21.qmd`
  - Before: It's a small bug, and it's the most common kind: two reasonable changes, each tested alone, that don't fit together. It's why the config holds the rules *and* the lines. They're one decision, and they have to be fitted together.
  - After: It's a small bug, and it's the most common kind: two reasonable changes, each tested alone, that don't work together. That's why the config holds the rules *and* the thresholds. They're one decision, and they have to be fitted together.
- `chapters/ch21.qmd`
  - Before: The API will fail sometimes. Chapter 16 said to decide in advance what a failure *means*, and the service makes that a config setting: `fallback="review"`.
  - After: The API will fail sometimes. Chapter 16 said to decide in advance what a failure *means*. The service makes that a config setting: `fallback="review"`.
- `chapters/ch21.qmd`
  - Before: To test it, I made 10% of calls fail. With the fallback set to review, the {{< num ch28 fallback_threats int >}} real threats among the failed calls went to a person. With it set to "act", the same {{< num ch28 fallback_act_closed int >}} would have been closed unseen, and every other number on the dashboard would have looked normal (@fig-failsafe). The monitor watches the fallback rate for that reason: a failure you don't count is a failure you don't see.
  - After: To test it, I made 10% of calls fail. With the fallback set to review, the {{< num ch28 fallback_threats int >}} real threats among the failed calls went to a person. With it set to "act", the same {{< num ch28 fallback_act_closed int >}} would have been closed without anyone seeing them. And every other number on the dashboard would have looked normal (@fig-failsafe). That's why the monitor watches the fallback rate: a failure you don't count is a failure you don't see.
- `chapters/ch21.qmd`
  - Before: The service writes every record to a log. Once a day, a small report reads the log and checks a handful of numbers against expected ranges: the share of alerts in each zone, the review queue against capacity, the fallback rate, and, for alerts a person has seen, the share predicted real against the share confirmed real.
  - After: The service writes every record to a log. Once a day, a small report reads the log and checks a few numbers against expected ranges. It checks the share of alerts in each zone, the review queue against capacity, and the fallback rate. And for alerts a person has seen, it compares the share predicted to be real with the share confirmed to be real.
- `chapters/ch21.qmd`
  - Before: The live week raised no flags at all. That matters as much as what comes next: a monitor that raises false alarms soon stops being read, which is why the queue check allows a tenth over capacity before it complains.
  - After: The live week raised no flags at all. That matters as much as what comes next. People soon stop reading a monitor that raises false alarms. That's why the queue check allows 10% over capacity before it raises a flag.
- `chapters/ch21.qmd`
  - Before: On the first day of the campaign week, two flags went up: the queue was well over capacity, and the alerts people saw were real far more often than predicted (@fig-monitor). That second flag is the one I'd most want in any decision service. It says, in plain numbers, "the probabilities have stopped matching reality", which is what Chapter 11 taught you to test for and Chapter 18 showed you how to fix.
  - After: On the first day of the campaign week, two flags went up. The queue was well over capacity, and the alerts people saw were real far more often than predicted (@fig-monitor). That second flag is the one I'd most want in any decision service. It says, in plain numbers, "the probabilities are no longer calibrated". Chapter 11 taught you to test for that, and Chapter 18 showed you how to fix it.
- `chapters/ch21.qmd`
  - Before: A flag is only useful if someone reads it. The last item on the checklist below is a named owner, with the authority to switch the service to "review everything" while they find out what happened.
  - After: A flag is only useful if someone reads it. The last item on the checklist below is a named owner. That person has the authority to switch the service to "review everything" while they find out what happened.
- `chapters/ch21.qmd`
  - Before: The service will improve. New calibration, new lines, a new model version. Each change is a new config, and a new config runs in **shadow** first: it decides every alert alongside the current version, logs what it would have done, and touches nothing.
  - After: The service will improve: new calibration, new thresholds, a new model version. Each change is a new config, and a new config runs in **shadow mode** first. It decides every alert next to the current version and logs what it would have done, but it doesn't act on anything.
- `chapters/ch21.qmd`
  - Before: The candidate here is the fixed config from the dry run. It agreed with the current version on {{< num ch28 shadow_agree pct >}} of alerts (@fig-shadow-21). The disagreements all go one way: about {{< num ch28 shadow_review_to_act_day f1 >}} alerts a day that the current version queues and the candidate would close. Among those, about {{< num ch28 shadow_moved_threats_day f1 >}} a day were real threats.
  - After: The candidate here is the fixed config from the dry run. It agreed with the current version on {{< num ch28 shadow_agree pct >}} of alerts (@fig-shadow-21). The disagreements all go the same way. There are about {{< num ch28 shadow_review_to_act_day f1 >}} alerts a day that the current version sends to review and the candidate would close. Among those, about {{< num ch28 shadow_moved_threats_day f1 >}} a day were real threats.
- `chapters/ch21.qmd`
  - Before: That's the price of fitting the queue, not a bug, and the shadow run puts a number on it before anyone pays it. Someone can now decide, with that number in front of them, whether to switch, hire, or accept a queue that runs over.
  - After: That's the price of fitting the queue, not a bug. The shadow run measures that price before anyone pays it. Someone can now decide, with that number in front of them, whether to switch, to hire, or to accept a queue that runs over.
- `chapters/ch21.qmd`
  - Before: @fig-checklist is the list I'd want ticked before switching on any decision service, whatever model sits inside it. None of it is specific to Jev. All of it is specific to *deciding*: once a model's output closes a case, pages a person or blocks a login, every item on that list stops being good practice and becomes the job.
  - After: @fig-checklist is the list I'd want completed before switching on any decision service, whatever model is inside it. None of it is specific to Jev. All of it is specific to *deciding*. Once a model's output closes a case, calls a person or blocks a login, every item on that list stops being optional. It becomes part of the job.
- `chapters/ch21.qmd`
  - Before: This is a teaching service. A real one needs things this chapter leaves out: authentication, rate limiting of its own callers, a durable log store rather than a file, access control on who can change the config, and data protection for the states it records, which may hold personal data. The monitor's bands were set by eye from one quiet week, so treat them as a starting point to tune. And shadow comparisons only show where versions *disagree*; if both are wrong in the same way, a shadow run can't tell you. Keep the random audit going.
  - After: This is a teaching service. A real one needs things this chapter leaves out. It needs sign-in for its callers and limits on how often they can call. It needs a proper log store rather than a file, and control over who can change the config. And it needs to protect the states it records, which may hold personal data. The monitor's expected ranges were set by eye from one quiet week, so treat them as a starting point to adjust. And shadow comparisons only show where versions *disagree*. If both versions are wrong in the same way, a shadow run can't tell you. Keep the random audit going.
- `chapters/ch21.qmd`
  - Before: The candidate config in shadow would auto-close about 29 more alerts a day, about one of them a real threat, to keep the queue at capacity. A missed threat costs about \$10,000; an extra analyst costs about \$600 a day and clears 40 reviews. Should Kestrel switch to the candidate, or keep the current version and add capacity?
  - After: To keep the queue at capacity, the candidate config in shadow would auto-close about 29 more alerts a day. About one of them is a real threat. A missed threat costs about \$10,000. An extra analyst costs about \$600 a day and clears 40 reviews. Should Kestrel switch to the candidate, or keep the current version and add capacity?
- `chapters/ch21.qmd`
  - Before: (Switching saves the queue about 29 reviews a day and costs about one missed threat, around \$10,000 a day in expected loss. Adding one analyst, about \$600 a day, would absorb those reviews instead. Unless hiring is impossible, keep the current lines and add capacity. The shadow run turned that from a hunch into arithmetic.)
  - After: (Switching saves about 29 reviews a day and costs about one missed threat, around \$10,000 a day in expected loss. Adding one analyst, at about \$600 a day, would handle those reviews instead. Unless hiring is impossible, keep the current thresholds and add capacity. The shadow run turned that from a guess into arithmetic.)
- `chapters/ch21.qmd`
  - Before: Vogels has said this in many talks. A decision service is built around it. Calls fail, models drift, and campaigns arrive on a Tuesday. The service doesn't prevent any of that. It makes sure each failure has a decided meaning, leaves a record, and reaches a person who can act.
  - After: Vogels has said this in many talks. A decision service is built around it. Calls fail, models drift, and attack campaigns arrive without warning. The service doesn't prevent any of that. It makes sure each failure has a decided meaning, leaves a record, and reaches a person who can act.
- `chapters/ch21.qmd`
  - Before: We built the service from the book's pieces. One versioned config held the model, calibration, lines and rules. Every decision left a record that explains it. A dry run caught a rule and a set of lines that didn't fit together, and fitting them together fixed it. A deliberate failure test showed why failures must fall back to review. A daily monitor stayed silent through a normal week and spoke up on the first day of a campaign. And a shadow run put a price on the next change before anyone paid it.
  - After: We built the service from the book's pieces. One versioned config held the model, calibration, thresholds and rules. Every decision left a record that explains it. A dry run caught a rule and a set of thresholds that didn't work together, and fitting them together fixed it. A planned failure test showed why failures must fall back to review. A daily monitor stayed quiet through a normal week and raised a flag on the first day of a campaign. And a shadow run measured the cost of the next change before anyone paid it.
- `chapters/ch21.qmd`
  - Before: 4. Write the one-paragraph runbook for the person who owns the flags: what they check first, and when they switch the service to review everything.
  - After: 4. Write one paragraph of instructions for the person who owns the flags: what they check first, and when they switch the service to review everything.
- `chapters/ch21.qmd`
  - Before: Next: the last chapter. What changes when deciding becomes cheap, fast and trustworthy, for the industry, and for you.
  - After: Next: the last chapter. What changes, for the industry and for you, when deciding becomes cheap, fast and calibrated?

## Chapter 1: What "learning" means

50 changes.

- `chapters/ch01.qmd`
  - Before: After a while, a nagging thought starts to form:
  - After: After a while, a worrying thought starts to form:
- `chapters/ch01.qmd`
  - Before: The short answer: you need less than you fear, but you need it in the right order. These words aren't a list of separate subjects. They're chapters of one story, and each one exists because the one before it ran into a wall.
  - After: The short answer: you need less than you fear, but you need it in the right order. These words aren't a list of separate subjects. They're chapters of one story. Each one exists because the one before it hit a problem it couldn't solve.
- `chapters/ch01.qmd`
  - Before: So let's walk the story. Slowly, with real examples, and without pretending you already know things you don't.
  - After: So let's go through the story. We'll go slowly, with real examples, and without pretending you already know things you don't.
- `chapters/ch01.qmd`
  - Before: A computer following a rule, nothing more. I told it what to do, step by step. It didn't figure anything out. It just checks a number and acts.
  - After: That's a computer following a rule, nothing more. I told it what to do, step by step. It didn't work anything out. It just checks a number and acts.
- `chapters/ch01.qmd`
  - Before: A surprising amount of software that gets called "AI" is no more than this. A bank that blocks card payments over a limit. A spam filter that bins any email containing "lottery". An office system that marks you absent if you haven't badged in by 10 a.m.
  - After: A lot of software that people call "AI" is no more than this. A bank blocks card payments over a limit. A spam filter deletes any email containing "lottery". An office system marks you absent if you haven't scanned your badge by 10 a.m.
- `chapters/ch01.qmd`
  - Before: And here's something people rarely say out loud: rules are *good*. They're fast, they're cheap, and when one goes wrong you can open it up and read why. When a rule does the job, use the rule. We'll come back to this in Chapter 13, where plain rules win more than one round of a contest against much fancier models.
  - After: And here's something people rarely say: rules are *good*. They're fast and cheap. When one goes wrong, you can open it up and read why. When a rule does the job, use the rule. We'll come back to this in Chapter 13, where plain rules win more than one round of a contest against much more complex models.
- `chapters/ch01.qmd`
  - Before: The trouble starts when the world won't sit still long enough for a rule.
  - After: The trouble starts when the world changes faster than you can write rules.
- `chapters/ch01.qmd`
  - Before: But what if the cat is hiding behind a sofa and you can only see its tail? What if it's black, on a black cushion, in a dark room? What if it's a kitten, all head and no legs?
  - After: But what if the cat is hiding behind a sofa and you can only see its tail? What if it's black, on a black cushion, in a dark room? What if it's a tiny kitten with a big head and short legs?
- `chapters/ch01.qmd`
  - Before: This isn't only a cat problem. Anyone who defends a company's computers faces it every day.
  - After: This isn't only a problem with cats. Anyone who protects a company's computers faces it every day.
- `chapters/ch01.qmd`
  - Before: Picture the security team at Kestrel Logistics, a freight company we'll follow to the last page. They want to catch phishing emails, the ones that trick staff into typing a password into a fake page. So someone writes the obvious rule: *if an email mentions "password", flag it.*
  - After: Picture the security team at Kestrel Logistics, a shipping company we'll follow to the last page. They want to catch phishing emails: emails that trick staff into typing a password into a fake page. So someone writes the obvious rule: *if an email mentions "password", flag it.*
- `chapters/ch01.qmd`
  - Before: Friday, the attacker stops writing the word at all and puts it inside an image. Then they drop the text entirely and send a link to a shared document that looks exactly like the real ones.
  - After: Friday, the attacker stops writing the word at all and puts it inside an image. Then they remove the text completely and send a link to a shared document that looks exactly like the real ones.
- `chapters/ch01.qmd`
  - Before: @fig-rules-vs-examples shows where this ends. The rulebook grows, and it's always one trick behind, because the attacker gets to read your rules by testing them and you don't get to read theirs.
  - After: @fig-rules-vs-examples shows where this ends. The list of rules grows, and it's always one trick behind. The attacker can learn your rules by testing them, but you can't read theirs.
- `chapters/ch01.qmd`
  - Before: So we flip the job around.
  - After: So we turn the job around.
- `chapters/ch01.qmd`
  - Before: Instead of telling the computer every rule, we give it a pile of emails where we already know the answer. This one was phishing. This one was fine. This one was phishing. Thousands of them.
  - After: Instead of telling the computer every rule, we give it a large set of emails where we already know the answer. This one was phishing. This one was fine. This one was phishing. Thousands of them.
- `chapters/ch01.qmd`
  - Before: You've been on the receiving end of this for years. When your bank texts *"Did you just spend \$640 at an electronics shop in another city?"*, no one at the bank wrote a rule about you, that shop and that amount. A system learned what your normal spending looks like from millions of past payments, and this one didn't fit. When Netflix puts a documentary at the top of your screen, it's the same move. Nobody wrote "people who watched these three shows want this one". The pattern came from examples.
  - After: Machine learning has been making decisions about you for years. Your bank may text you: *"Did you just spend \$640 at an electronics shop in another city?"* No one at the bank wrote a rule about you, that shop and that amount. A system learned what your normal spending looks like from millions of past payments, and this one didn't fit. When Netflix puts a documentary at the top of your screen, it's the same idea. Nobody wrote "people who watched these three shows want this one". The pattern came from examples.
- `chapters/ch01.qmd`
  - Before: You'll hear the word *model* constantly, so let's pin it down.
  - After: You'll hear the word *model* all the time, so let's define it clearly.
- `chapters/ch01.qmd`
  - Before: When the computer finishes studying the examples, what's left behind is a thing that takes an input and produces an answer. Give it a new email, it says "phishing" or "fine". Give it a payment, it says "normal" or "odd". That thing is the model.
  - After: When the computer finishes studying the examples, it leaves behind something that takes an input and produces an answer. Give it a new email, and it says "phishing" or "fine". Give it a payment, and it says "normal" or "odd". That thing is the model.
- `chapters/ch01.qmd`
  - Before: Think of it as a machine with a lot of knobs. Learning is the process of turning those knobs until the machine gets the examples right as often as possible. Once the knobs are set, you stop turning them and put the machine to work, on cases where nobody knows the answer yet. If you already knew the answer, you wouldn't need the model.
  - After: Think of it as a machine with a lot of knobs. Learning means turning those knobs until the machine gets the examples right as often as possible. Once the knobs are set, you stop turning them and put the machine to work on cases where nobody knows the answer yet. If you already knew the answer, you wouldn't need the model.
- `chapters/ch01.qmd`
  - Before: Before we go further, let's get our hands on something real enough to learn from.
  - After: Before we go further, let's look at some data that's realistic enough to learn from.
- `chapters/ch01.qmd`
  - Before: Kestrel Logistics has a small security operations centre, a SOC. Every system the company runs, from laptops and email to cloud storage and sign-ins, produces *alerts*: short, messy notes that say "this looked suspicious". Over four weeks the SOC receives {{< num ch01 n_alerts int >}} of them. About {{< num ch01 per_day int >}} a day, for a handful of analysts.
  - After: Kestrel Logistics has a small security operations centre, or SOC: the team that watches for attacks. Every system the company runs, from laptops and email to cloud storage and sign-ins, produces *alerts*. An alert is a short, messy note that says "this looked suspicious". Over four weeks the SOC receives {{< num ch01 n_alerts int >}} of them. That's about {{< num ch01 per_day int >}} a day, for a few analysts.
- `chapters/ch01.qmd`
  - Before: I'll be straight with you about one thing: Kestrel Logistics doesn't exist. Every alert in this book comes from a generator I wrote, and the reason is a good one. With real security data you never know the true answer for sure, and you're never allowed to publish it anyway. With synthetic data we know what happened in every single case, so we can check every model's work, all book long.
  - After: I'll be honest with you about one thing: Kestrel Logistics doesn't exist. Every alert in this book comes from a program I wrote, and there's a good reason. With real security data, you never know the true answer for sure, and you're never allowed to publish it anyway. With synthetic (made-up) data, we know what happened in every case. So we can check every model's work, all through the book.
- `chapters/ch01.qmd`
  - Before: Look at that alert for a second. Someone received a flood of sign-in approval requests on their phone in the middle of the night, and one was approved. Attackers do exactly this: they spam your phone until you tap "yes" just to make it stop.
  - After: Look at that alert for a moment. Someone received a large number of sign-in approval requests on their phone in the middle of the night, and one was approved. Attackers do exactly this. They send request after request until you tap "yes" just to make it stop.
- `chapters/ch01.qmd`
  - Before: Real attack, or not? Hold that question. We'll come back to this exact alert.
  - After: Real attack, or not? Keep that question in mind. We'll come back to this exact alert.
- `chapters/ch01.qmd`
  - Before: Every alert comes with a *threat-intel score* between 0 and 1. It's a rough measure of how bad the outside world thinks the website, address or sender involved is. A reasonable-sounding rule would be: flag the alert if the score is at least some number, call it *t*.
  - After: Every alert comes with a *threat-intel score* between 0 and 1. It's a rough measure of how dangerous outside security sources think the website, address or sender is. A sensible-sounding rule would be: flag the alert if the score is at least some number, *t*. A number like this, which splits cases into two groups, is called a **threshold**. Think of it as a line on the scale from 0 to 1.
- `chapters/ch01.qmd`
  - Before: The machine searched every threshold and found the one with the fewest mistakes. It picked {{< num ch01 best_t f2 >}}, which means it flags only the alerts with the very worst scores. Almost nothing gets flagged. And a "strategy" of never flagging anything at all makes only a few more mistakes.
  - After: The machine searched every threshold and found the one with the fewest mistakes. It picked {{< num ch01 best_t f2 >}}, so it flags only the alerts with the very worst scores. Almost nothing gets flagged. And a "strategy" of never flagging anything at all makes only a few more mistakes.
- `chapters/ch01.qmd`
  - Before: ![Every possible threshold, and the mistakes it makes. Low thresholds drown the team in false alarms; high ones miss attacks. The total bottoms out at the far right, barely below the dashed line for "flag nothing at all".]
  - After: ![Every possible threshold, and the mistakes it makes. Low thresholds give the team far too many false alarms; high ones miss attacks. The total is lowest at the far right, just below the dashed line for "flag nothing at all".]
- `chapters/ch01.qmd`
  - Before: @fig-threshold-search shows why. There are so many harmless alerts that every false alarm costs the rule more than a missed attack helps it. So the search slides the threshold up and up until it has almost stopped raising alarms. Of {{< num ch01 attacks int >}} real attacks, the "best" rule catches {{< num ch01 best_caught int >}}.
  - After: @fig-threshold-search shows why. There are so many harmless alerts that each false alarm hurts the rule's score more than catching an attack helps it. So the search moves the threshold higher and higher, until the rule has almost stopped raising alarms. Of {{< num ch01 attacks int >}} real attacks, the "best" rule catches {{< num ch01 best_caught int >}}.
- `chapters/ch01.qmd`
  - Before: The first: we treated every mistake as equal. But letting a real attacker walk in and bothering an analyst for five minutes aren't equal mistakes, not even close. Chapter 4 fixes this properly.
  - After: The first: we treated every mistake as equal. But letting a real attacker in and bothering an analyst for five minutes are very different mistakes. Chapter 4 fixes this properly.
- `chapters/ch01.qmd`
  - Before: The second is subtler, and it's the one this book is really about. We forced the answer to be *yes* or *no*.
  - After: The second is harder to see, and it's the one this book is really about. We forced the answer to be *yes* or *no*.
- `chapters/ch01.qmd`
  - Before: A learned model only knows the world its examples came from. If attackers invent a trick that isn't in the training data, the model has never seen it, and it won't tell you that it hasn't. Its answer will look just as confident as always. Labels can be wrong too: analysts disagree, and some attacks are never discovered, so they sit in the data marked "fine". A model will happily learn those mistakes as if they were truth.
  - After: A learned model only knows the world its examples came from. If attackers invent a trick that isn't in the training data, the model has never seen it, and it won't tell you so. Its answer will look just as confident as always. Labels can be wrong too. Analysts disagree, and some attacks are never found, so they stay in the data marked "fine". A model will learn those mistakes as if they were true.
- `chapters/ch01.qmd`
  - Before: Let's look at the same data from a different angle. Instead of asking "attack or not?", let's ask: *among alerts with a given score, how many turned out to be attacks?*
  - After: Let's look at the same data in a different way. Instead of asking "attack or not?", let's ask: *among alerts with a given score, how many turned out to be attacks?*
- `chapters/ch01.qmd`
  - Before: There's no clean line where alerts switch from harmless to dangerous. Among the lowest-scoring alerts, about {{< num ch01 bottom_bin_rate pct >}} were attacks. That sounds tiny, but that bucket holds {{< num ch01 bottom_bin_n int >}} alerts, so it's well over a hundred real attacks hiding among the most harmless-looking noise. Among the highest-scoring alerts, {{< num ch01 top_bin_rate pct >}} were attacks. Which means more than a third of the scariest-looking ones were nothing.
  - After: There's no clear point where alerts switch from harmless to dangerous. Among the lowest-scoring alerts, about {{< num ch01 bottom_bin_rate pct >}} were attacks. That sounds tiny. But that group holds {{< num ch01 bottom_bin_n int >}} alerts, so well over a hundred real attacks are hiding among the most harmless-looking alerts. Among the highest-scoring alerts, {{< num ch01 top_bin_rate pct >}} were attacks. So more than a third of the scariest-looking ones were nothing.
- `chapters/ch01.qmd`
  - Before: That number, a chance, carries far more than a yes or a no. It tells the analyst how worried to be. It lets you sort the queue so the likeliest attacks come first. And, as you'll see in Chapter 4, it lets you set your line in the right place once you've decided what each kind of mistake costs.
  - After: That number, a chance, tells you far more than a yes or a no. It tells the analyst how worried to be. It lets you sort the queue so the likeliest attacks come first. And, as you'll see in Chapter 4, it lets you put your threshold in the right place, once you've decided what each kind of mistake costs.
- `chapters/ch01.qmd`
  - Before: That last part, being *right about how sure it is*, has a name, and a whole part of this book to itself. For now, just notice that it's a very different goal from "make the fewest mistakes".
  - After: That last part, being *right about how sure it is*, has a name: **calibration**. A model that gets it right is *calibrated*: its probabilities are honest. Chapter 3 is about it. For now, just notice that it's a very different goal from "make the fewest mistakes".
- `chapters/ch01.qmd`
  - Before: (Down, a long way. When a miss hurts more, you accept more false alarms to avoid one. Chapter 4 turns that intuition into a formula.)
  - After: (Down, by a lot. When a miss hurts more, you accept more false alarms to avoid one. Chapter 4 turns that idea into a formula.)
- `chapters/ch01.qmd`
  - Before: Our threat-intel rule had it easy: someone handed it a single useful number. A photo is millions of pixels, and an email is a string of words. Nobody can hand-write the features for "this sounds like a scam". So the next step was models that learn their own features, in many stacked layers. The name for that is **deep learning** (Chapter 5).
  - After: Our threat-intel rule had an easy job: someone gave it a single useful number. But a photo is millions of pixels, and an email is a string of words. Nobody can write the clues for "this sounds like a scam" by hand. So the next step was models that learn their own clues, in many stacked layers. The name for that is **deep learning** (Chapter 5).
- `chapters/ch01.qmd`
  - Before: Train a very large deep-learning model on a huge amount of text, with one simple task, guess the next word, and it picks up grammar, facts and even some reasoning along the way. The result is a **large language model**, an LLM (Chapter 6).
  - After: Train a very large deep-learning model on a huge amount of text, with one simple task: guess the next word. Along the way, it learns grammar, facts and even some reasoning. The result is a **large language model**, or LLM (Chapter 6).
- `chapters/ch01.qmd`
  - Before: LLMs know a lot about the world and nothing about *your* world, so we let them look things up before answering. The technique is called **retrieval-augmented generation**, or RAG. And once a model can read, the next wish is for it to *do* things: check a log, block an account, look at what happened, decide what to do next. A model working in that loop is an **agent** (Chapter 7).
  - After: LLMs know a lot about the world and nothing about *your* world, so we let them look things up before answering. That method is called **retrieval-augmented generation**, or RAG. And once a model can read, we want it to *do* things: check a log, block an account, look at what happened, decide what to do next. A model working in that loop is an **agent** (Chapter 7).
- `chapters/ch01.qmd`
  - Before: Most of its steps aren't writing essays. They're small decisions. Is this alert real? Which queue does this ticket go in? Is this action safe to take? Did that tool call work? Hundreds of little judgements, each with a known set of possible answers.
  - After: Most of its steps aren't writing essays. They're small decisions. Is this alert real? Which queue does this ticket go in? Is this action safe to take? Did that tool call work? There are hundreds of these small judgements, each with a known set of possible answers.
- `chapters/ch01.qmd`
  - Before: For each of those, the usual approach today is to ask an LLM, get a paragraph back, and then write code to dig the answer out of the paragraph. It works. It's also a bit like hiring a novelist to tick a checkbox.
  - After: For each one, the usual approach today is to ask an LLM, get a paragraph back, and then write code to find the answer inside the paragraph. It works. But it's a bit like hiring a novelist to tick a checkbox.
- `chapters/ch01.qmd`
  - Before: In September 2026, a start-up called TypeSafe AI released a model built for those checkbox moments. It's called **Jev**. It doesn't write text at all. You give it the situation and a typed question, like "pick one of these labels" or "is this true, yes or no", and it gives back the answer as data, with a probability attached to every option (@fig-generate-vs-decide). TypeSafe calls it a *System One* model, after the fast, intuitive kind of thinking described by the psychologist Daniel Kahneman, as opposed to slow, deliberate *System Two* thinking [@kahneman2011]. Part III takes Jev apart properly.
  - After: In September 2026, a start-up called TypeSafe AI released a model built for those checkbox moments. It's called **Jev**. It doesn't write text at all. You give it the situation and a typed question, like "pick one of these labels" or "is this true, yes or no". It gives back the answer as data, with a probability for every option (@fig-generate-vs-decide). TypeSafe calls it a *System One* model. The name comes from the psychologist Daniel Kahneman, who described fast, intuitive thinking (System One) and slow, careful thinking (System Two) [@kahneman2011]. Part III looks at Jev in detail.
- `chapters/ch01.qmd`
  - Before: One thing you should know now, because it shapes every page that follows. I didn't have access to the Jev API while writing this book. So everywhere you see Jev answer a question, the answer comes from `jev-mock-synthetic`, a stand-in I built that speaks Jev's exact public interface through TypeSafe's official Python library. The code is real. The numbers are synthetic, and every one of them is labelled that way.
  - After: You should know one thing now, because it affects every page that follows. I didn't have access to the Jev API while writing this book. So everywhere you see Jev answer a question, the answer comes from `jev-mock-synthetic`. It's a stand-in I built, and it uses Jev's exact public interface through TypeSafe's official Python library. The code is real. The numbers are synthetic, and every one of them is labelled that way.
- `chapters/ch01.qmd`
  - Before: Time for your first question to it. Same alert as before, the flood of sign-in requests at night.
  - After: Time for your first question to it. It's the same alert as before: the many sign-in requests at night.
- `chapters/ch01.qmd`
  - Before: It thinks it's probably an attack. It wasn't. And that's not a bug in the story, it's the story.
  - After: It thinks it's probably an attack. It wasn't. And that's not a mistake in the story; it's the point of the story.
- `chapters/ch01.qmd`
  - Before: A probability of {{< num ch01 mock_p_99 f2 >}} is a claim, not a promise: among alerts like this one, roughly two out of three are attacks. This one happened to be in the other third. Whether a model's "0.68" really does mean two out of three is something we can *test*, and we will, in Chapter 3 for ordinary models and in Chapter 11 for Jev.
  - After: A probability of {{< num ch01 mock_p_99 f2 >}} is a claim, not a promise: among alerts like this one, about two out of three are attacks. This one happened to be in the other third. We can *test* whether a model's "0.68" really means two out of three. We will, in Chapter 3 for ordinary models and in Chapter 11 for Jev.
- `chapters/ch01.qmd`
  - Before: We wanted computers to do intelligent things. Rules weren't enough, so we taught machines from examples. As problems got harder, our models got bigger and started learning their own features. Some of them learned language. We gave them documents to read, then tools to use.
  - After: We wanted computers to do intelligent things. Rules weren't enough, so we taught machines from examples. As problems got harder, our models got bigger and started learning their own clues. Some of them learned language. We gave them documents to read, then tools to use.
- `chapters/ch01.qmd`
  - Before: And now, inside those tools and loops, we're finding that most of the work is *deciding*. Quickly, cheaply, and with an honest sense of how sure we are.
  - After: And now, inside those tools and loops, we're finding that most of the work is *deciding*: quickly, cheaply, and with calibrated probabilities that honestly say how sure we are.
- `chapters/ch01.qmd`
  - Before: ![The story so far. Each step exists because the one before it hit a wall. System One models like Jev branch off deep learning and slot into the "decide" step of an agent.]
  - After: ![The story so far. Each step exists because the one before it hit a problem it couldn't solve. System One models like Jev grow out of deep learning and fit into the "decide" step of an agent.]
- `chapters/ch01.qmd`
  - Before: You don't need to understand every box today. Just know where we're going. The next three chapters stay down at the bottom-left corner of this map on purpose, because everything above it, Jev included, is built on one idea we've only just met: a model's answer should be a probability, and the probability should mean what it says.
  - After: You don't need to understand every box today. Just know where we're going. The next three chapters stay in the bottom-left corner of this map on purpose. Everything above it, Jev included, is built on one idea we've only just met: a model's answer should be a probability, and the probability should mean what it says.
- `chapters/ch01.qmd`
  - Before: Next: that "how likely" idea. It sounds like a small change. It's the most important idea in the book, and it hides a trap that fools doctors, judges and security teams alike.
  - After: Next: that "how likely" idea. It sounds like a small change. It's the most important idea in the book, and it hides a trap that fools doctors, judges and security teams.

## Chapter 2: Probability

38 changes.

- `chapters/ch02.qmd`
  - Before: A reasonable thought, and the most expensive mistake people make in this field.
  - After: It's a reasonable thought. It's also the most costly mistake people make in this field.
- `chapters/ch02.qmd`
  - Before: In the last chapter, a machine learned what we asked and still ended up useless, because we asked for yes-or-no answers. The fix was to ask for a *chance* instead. This chapter does two things. First, it makes sure you can read a chance without being fooled, including the one trap that catches doctors, judges and security teams alike. Then it builds, in about twenty lines of code, a model that learns chances from examples.
  - After: In the last chapter, a machine learned what we asked and was still useless, because we asked for yes-or-no answers. The fix was to ask for a *chance* instead. This chapter does two things. First, it makes sure you can read a chance without being fooled. That includes the one trap that catches doctors, judges and security teams. Then it builds a model that learns chances from examples, in about twenty lines of code.
- `chapters/ch02.qmd`
  - Before: There's no heavy maths here. There are a few ideas that, once they click, you'll use for the rest of your career.
  - After: There's no difficult maths here. There are a few ideas that, once you understand them, you'll use for the rest of your career.
- `chapters/ch02.qmd`
  - Before: - Spot the base-rate trap before it costs you, and update a probability by multiplying odds.
  - After: - Notice the base-rate trap before it costs you, and update a probability by multiplying odds.
- `chapters/ch02.qmd`
  - Before: Not necessarily. One day can't tell you. What *can* tell you is the forecaster's track record. Collect every day they said "70%". If it rained on about 70 of every 100 of those days, the forecaster is doing their job, and a dry day is just one of the 30.
  - After: Not necessarily. One day can't tell you. What *can* tell you is the forecaster's record. Collect every day they said "70%". If it rained on about 70 of every 100 of those days, the forecaster is doing their job. A dry day is just one of the 30.
- `chapters/ch02.qmd`
  - Before: So here's the idea to hold on to: **a probability is a claim about how often something happens among cases like this one.**
  - After: So here's the idea to remember: **a probability is a claim about how often something happens among cases like this one.**
- `chapters/ch02.qmd`
  - Before: That definition is useful because it's *checkable*. When a model tells you an alert is 70% likely to be an attack, it's making the same kind of promise as the weather app, and we can hold it to the same standard.
  - After: That definition is useful because you can *check* it. When a model tells you an alert is 70% likely to be an attack, it's making the same kind of promise as the weather app. We can check it in the same way.
- `chapters/ch02.qmd`
  - Before: At Kestrel Logistics, about {{< num ch02 base pct1 >}} of all alerts turn out to be real attacks: the probability of an attack **among all alerts**. Among alerts with a threat-intel score of 0.7 or more, the share is much higher. Same question, a different answer depending on *which group* you're asking about.
  - After: At Kestrel Logistics, about {{< num ch02 base pct1 >}} of all alerts turn out to be real attacks. That's the probability of an attack **among all alerts**. Among alerts with a threat-intel score of 0.7 or more, the share is much higher. It's the same question, but the answer depends on *which group* you're asking about.
- `chapters/ch02.qmd`
  - Before: Statisticians write the second kind with a vertical bar, read as "given": P(attack | bad score) is the chance of an attack *given* a bad score. And here's where people get tangled. P(attack | bad score) and P(bad score | attack) look like mirror images. They're not.
  - After: Statisticians write the second kind with a vertical bar, read as "given": P(attack | bad score) is the chance of an attack *given* a bad score. And here's where people get confused. P(attack | bad score) and P(bad score | attack) look like the same thing reversed. They're not the same.
- `chapters/ch02.qmd`
  - Before: About {{< num ch02 ioc_attack_share pct >}} of attacks come with a bad score. That doesn't make a bad-score alert {{< num ch02 ioc_attack_share pct >}} likely to be an attack. "How often do attacks look like this?" and "how often is something that looks like this an attack?" are different questions. Mixing them up has a name in courtrooms, the *prosecutor's fallacy*, and it has put innocent people in prison. In a SOC it just ruins your week.
  - After: About {{< num ch02 ioc_attack_share pct >}} of attacks come with a bad score. That doesn't make a bad-score alert {{< num ch02 ioc_attack_share pct >}} likely to be an attack. "How often do attacks look like this?" and "how often is something that looks like this an attack?" are different questions. In courts, mixing them up has a name: the *prosecutor's fallacy*. It has put innocent people in prison. In a SOC, it causes a lot of wasted work.
- `chapters/ch02.qmd`
  - Before: If that feels wrong, you're in excellent company. In a well-known 1978 study, doctors and students at Harvard Medical School were given the same puzzle about a medical test, and the most common answer was 95% [@casscells1978]. The way out is counting, not a formula.
  - After: If that feels wrong, you're not alone. In a well-known 1978 study, doctors and students at Harvard Medical School got the same puzzle about a medical test. The most common answer was 95% [@casscells1978]. The way to solve it is to count, not to use a formula.
- `chapters/ch02.qmd`
  - Before: @fig-base-rate-tree holds the trick. The 5% false-alarm rate sounds small, but it's 5% of a *huge* number. The 99% hit rate sounds large, but it's 99% of a *tiny* one. The psychologist Gerd Gigerenzer showed that people who reason with counts like these get such puzzles right far more often [@gigerenzer1995]. If a probability ever surprises you, turn it into counts of events. The surprise usually vanishes.
  - After: @fig-base-rate-tree shows the answer. The 5% false-alarm rate sounds small, but it's 5% of a *huge* number. The 99% hit rate sounds large, but it's 99% of a *tiny* one. The psychologist Gerd Gigerenzer showed that people who think in counts like these get such puzzles right far more often [@gigerenzer1995]. If a probability ever surprises you, turn it into counts of events. The surprise usually goes away.
- `chapters/ch02.qmd`
  - Before: The chance of something before you see any evidence, the 1 in 1,000, is called the **base rate**. Ignoring it is the base-rate fallacy, and it's why a "95% accurate" fraud model can still bury a bank in false alarms.
  - After: The chance of something before you see any evidence, here 1 in 1,000, is called the **base rate**. Ignoring it is the base-rate fallacy. It's why a "95% accurate" fraud model can still give a bank far too many false alarms.
- `chapters/ch02.qmd`
  - Before: ## Bayes' rule, without the fear
  - After: ## Bayes' rule, made simple
- `chapters/ch02.qmd`
  - Before: The cleanest way uses **odds**: "for" compared with "against". A probability of 20% is odds of 20 to 80, or 0.25. Every clue has a strength: how much more common is it among attacks than among harmless alerts? That ratio is the **likelihood ratio**. At Kestrel, a threat-intel score of 0.7 or more shows up in {{< num ch02 ioc_attack_share pct >}} of attacks and {{< num ch02 ioc_benign_share pct1 >}} of harmless alerts, so its likelihood ratio is about {{< num ch02 lr_ioc f1 >}}.
  - After: The simplest way uses **odds**: "for" compared with "against". A probability of 20% is odds of 20 to 80, or 0.25. Every clue has a strength: how much more common is it among attacks than among harmless alerts? That ratio is the **likelihood ratio**. At Kestrel, a threat-intel score of 0.7 or more shows up in {{< num ch02 ioc_attack_share pct >}} of attacks and {{< num ch02 ioc_benign_share pct1 >}} of harmless alerts. So its likelihood ratio is about {{< num ch02 lr_ioc f1 >}}.
- `chapters/ch02.qmd`
  - Before: One caveat. Multiplying like this assumes each clue tells you something *new*. Real clues overlap: attackers who use bad infrastructure also tend to work at night. Among alerts with both clues, the real attack rate is {{< num ch02 real12 pct >}}, not the {{< num ch02 p2 pct >}} our multiplication predicted. That gap is why, in practice, we let a model learn how much each clue is worth. We'll build one in a moment.
  - After: One warning. Multiplying like this assumes each clue tells you something *new*. Real clues overlap: attackers who use known-bad servers also tend to work at night. Among alerts with both clues, the real attack rate is {{< num ch02 real12 pct >}}, not the {{< num ch02 p2 pct >}} our multiplication predicted. That gap is why, in practice, we let a model learn how much each clue is worth. We'll build one in a moment.
- `chapters/ch02.qmd`
  - Before: First, how do we score a yes-or-no rule? Take *raise an alert whenever the threat-intel score is 0.5 or more*, and sort every alert into four boxes.
  - After: First, how do we score a yes-or-no rule? Take the rule *raise an alert whenever the threat-intel score is 0.5 or more*. Sort every alert into four boxes.
- `chapters/ch02.qmd`
  - Before: **Precision** answers: *when the rule raises an alert, how often is it real?* Here it's {{< num ch02 precision pct >}}. **Recall** answers: *of all the real attacks, how many did the rule catch?* Here it's {{< num ch02 recall pct >}}. And **accuracy**, the share of all alerts put in the right box (@fig-confusion), comes out at {{< num ch02 accuracy pct >}}. That sounds decent, until you notice that a rule that *never raises any alert at all* scores {{< num ch02 always_benign_acc pct >}}. When one outcome is rare, accuracy mostly measures how common the other one is.
  - After: **Precision** answers: *when the rule raises an alert, how often is it real?* Here it's {{< num ch02 precision pct >}}. **Recall** answers: *of all the real attacks, how many did the rule catch?* Here it's {{< num ch02 recall pct >}}. And **accuracy** is the share of all alerts put in the right box (@fig-confusion). It comes out at {{< num ch02 accuracy pct >}}. That sounds good, until you notice that a rule that *never raises any alert at all* scores {{< num ch02 always_benign_acc pct >}}. When one outcome is rare, accuracy mostly measures how common the other one is.
- `chapters/ch02.qmd`
  - Before: Bayes' rule multiplied odds. Multiplying is awkward and adding is easy, so take the logarithm of the odds, the **log-odds**, and every multiplication becomes an addition. That gives a very simple machine. Start from a baseline number, add a **weight** for each clue, and turn the total back into a probability with an S-shaped curve.
  - After: Bayes' rule multiplied odds. Multiplying is awkward and adding is easy. So take the logarithm of the odds, called the **log-odds**, and every multiplication becomes an addition. That gives a very simple machine. Start from a starting number, add a **weight** for each clue, and turn the total back into a probability with an S-shaped curve.
- `chapters/ch02.qmd`
  - Before: And that's the model (@fig-sigmoid): **logistic regression**, used for credit scores and medical risk for decades. Underneath, it's Bayes' rule on the log-odds scale, with one upgrade: the model learns all the weights *together*, so it can discount clues that overlap.
  - After: And that's the model (@fig-sigmoid): **logistic regression**. It has been used for credit scores and medical risk for decades. Underneath, it's Bayes' rule on the log-odds scale, with one improvement. The model learns all the weights *together*, so it can give less weight to clues that overlap.
- `chapters/ch02.qmd`
  - Before: Think about how *you'd* want to be judged as a forecaster. Say 90% and be right, and you should lose almost nothing. Say 1% and be wrong, and you should be embarrassed, badly, because you were confidently wrong. That score exists. **Log loss** measures surprise: the penalty is minus the logarithm of the probability you gave to what actually happened.
  - After: Think about how *you'd* want to be judged as a forecaster. Say 90% and be right, and you should lose almost nothing. Say 1% and be wrong, and you should lose a lot, because you were confidently wrong. That score exists. **Log loss** measures surprise. The penalty is minus the logarithm of the probability you gave to what actually happened.
- `chapters/ch02.qmd`
  - Before: ![Log loss for a single alert. If it really was an attack (red), the penalty is small when the model gave "attack" a high probability and explodes as that probability heads towards zero. Harmless alerts (blue) work the same way from the other side.]
  - After: ![Log loss for a single alert. If it really was an attack (red), the penalty is small when the model gave "attack" a high probability. It grows very fast as that probability gets close to zero. Harmless alerts (blue) work the same way from the other side.]
- `chapters/ch02.qmd`
  - Before: Log loss has a deeper property, and it's the reason this book cares so much about it. It's a **proper scoring rule**: the only way to get the best score, on average, is to report the probabilities you actually believe. Say 99% when you believe 80%, and over many cases you lose more than you gain. So models trained this way tend to come out reasonably *honest*, a word the next chapter spends all its pages on.
  - After: Log loss has a deeper property, and it's why this book cares so much about it. It's a **proper scoring rule**: the only way to get the best score, on average, is to report the probabilities you actually believe. Say 99% when you believe 80%, and over many cases you lose more than you gain. So models trained this way tend to come out fairly well *calibrated*: their probabilities are close to honest. The next chapter is all about calibration.
- `chapters/ch02.qmd`
  - Before: Log loss rewards honest confidence and punishes confident mistakes.
  - After: Log loss rewards honest probabilities and punishes confident mistakes.
- `chapters/ch02.qmd`
  - Before: Picture the log loss as hilly ground: every combination of weights is a place, and the height is the loss. Learning means finding the lowest point. We can't search every place, but we don't have to. Stand on a hillside in thick fog, feel which way the ground slopes under your feet, take a step downhill, and repeat until the ground is flat.
  - After: Picture the log loss as hilly ground. Every combination of weights is a place, and the height is the loss. Learning means finding the lowest point. We can't search every place, but we don't have to. Stand on a hill in thick fog. Feel which way the ground slopes under your feet, take a step downhill, and repeat until the ground is flat.
- `chapters/ch02.qmd`
  - Before: The **gradient** is the slope in every direction at once. For logistic regression it has a lovely form: for each alert, take what the model said minus what happened, *p* − *y*, multiply by the alert's clues, and average. Step the other way. How big a step to take is the **learning rate**: too small and you barely move, too big and you overshoot the valley.
  - After: The **gradient** is the slope in every direction at once. For logistic regression it's simple to compute. For each alert, take what the model said minus what happened, *p* − *y*. Multiply by the alert's clues, and average. Then step the other way. The size of each step is the **learning rate**. Too small and you barely move; too big and you step right over the lowest point.
- `chapters/ch02.qmd`
  - Before: Here it is, on Kestrel's alerts. We keep 20% of them locked away for testing, because the only fair estimate of how a model will do on new alerts comes from alerts it never saw.
  - After: Here it is, on Kestrel's alerts. We keep 20% of them aside for testing. The only fair way to estimate how a model will do on new alerts is to test it on alerts it never saw.
- `chapters/ch02.qmd`
  - Before: That loop is the heart of machine learning. Everything else, including the training of LLMs, is this loop with a bigger model, more data and cleverer steps.
  - After: That loop is the centre of machine learning. Everything else, including the training of LLMs, is this loop with a bigger model, more data and smarter steps.
- `chapters/ch02.qmd`
  - Before: **Overfitting** is memorising instead of learning. A flexible enough model can shape itself around every quirk of the training data, including the noise, and its training loss keeps falling while it gets *worse* at anything new.
  - After: **Overfitting** is memorising instead of learning. A flexible enough model can fit every small detail of the training data, including the noise. Its training loss keeps falling while it gets *worse* at anything new.
- `chapters/ch02.qmd`
  - Before: A decision tree allowed {{< num ch03 tree_best_depth int >}} levels of questions does best on new alerts. Allowed twenty, it nearly memorises the training set, with a training loss of {{< num ch03 tree_deep_train f3 >}}, and does terribly on alerts it hasn't seen ({{< num ch03 tree_deep_test f2 >}}) (@fig-overfit). The only way to see this is to test on data the model never trained on.
  - After: A decision tree is a model that asks a series of yes-or-no questions about an alert. Allowed {{< num ch03 tree_best_depth int >}} levels of questions, it does best on new alerts. Allowed twenty, it nearly memorises the training set, with a training loss of {{< num ch03 tree_deep_train f3 >}}. And it does very badly on alerts it hasn't seen ({{< num ch03 tree_deep_test f2 >}}) (@fig-overfit). The only way to see this is to test on data the model never trained on.
- `chapters/ch02.qmd`
  - Before: **Leakage** is subtler and nastier. A feature carries the answer in disguise.
  - After: **Leakage** is harder to spot and more dangerous. It's when a clue secretly contains the answer.
- `chapters/ch02.qmd`
  - Before: Suppose Kestrel's alert database has a field called `analyst_notes`. Train with it and the results look astonishing, because notes like "confirmed phishing" are only written *after* someone has decided. At 2:14 a.m., when the model has to decide, that field is empty. Ask of every feature: *would I actually have this value at the moment of the decision?* And remember that probabilities are always "among cases like this": if attackers launch a campaign, the base rate jumps, and every probability computed from last month is suddenly too low.
  - After: Suppose Kestrel's alert database has a field called `analyst_notes`. Train with it and the results look amazing, because notes like "confirmed phishing" are only written *after* someone has decided. At 2:14 a.m., when the model has to decide, that field is empty. Ask this about every clue: *would I actually have this value at the moment of the decision?* And remember that probabilities are always "among cases like this". If attackers start a campaign, the base rate jumps. Then every probability computed from last month is suddenly too low.
- `chapters/ch02.qmd`
  - Before: Precision and recall pull against each other. Lower the rule's threshold from 0.5 to 0.3: which goes up, and which goes down? If Kestrel's analysts can only look at 300 alerts a day, which should they care about more?
  - After: Precision and recall pull in opposite directions. Lower the rule's threshold from 0.5 to 0.3. Which one goes up, and which goes down? If Kestrel's analysts can only look at 300 alerts a day, which should they care about more?
- `chapters/ch02.qmd`
  - Before: (Recall goes up, precision down: you catch more attacks and raise more false alarms. With a fixed daily budget, precision decides how many real attacks fit inside those 300 looks. Chapter 4 puts both into a single cost.)
  - After: (Recall goes up and precision goes down: you catch more attacks and raise more false alarms. With a fixed daily limit, precision decides how many real attacks are among those 300 alerts. Chapter 4 puts both into a single cost.)
- `chapters/ch02.qmd`
  - Before: A probability, we found, only means something as a track record, which is why "among what?" matters so much. Asking it carefully exposed the base-rate trap, and escaping the trap meant multiplying odds: Bayes' rule. Accuracy flattered a rule that caught almost nothing, so we needed precision and recall. Then we built a machine that learns probabilities: it adds evidence on the log-odds scale, is scored by log loss, and rolls downhill, and it came within a whisker of the truth on alerts it never saw.
  - After: A probability, we found, only means something as a record over many cases. That's why "among what?" matters so much. Asking it carefully showed us the base-rate trap, and getting out of the trap meant multiplying odds: Bayes' rule. Accuracy made a rule that caught almost nothing look good, so we needed precision and recall. Then we built a machine that learns probabilities. It adds up evidence on the log-odds scale, is scored by log loss, and rolls downhill. On alerts it never saw, it came very close to the truth.
- `chapters/ch02.qmd`
  - Before: Log loss *rewards* honesty. That isn't the same as *being* honest, and that's what we have to check next.
  - After: Log loss *rewards* calibrated probabilities. That isn't the same as *producing* them, and that's what we have to check next.
- `chapters/ch02.qmd`
  - Before: 1. A spam filter catches 98% of spam and wrongly flags 1% of real email. If 20% of incoming email is spam, what fraction of flagged emails are real? Redo it for a mailbox where only 1% is spam. Use natural frequencies.
  - After: 1. A spam filter catches 98% of spam and wrongly flags 1% of real email. If 20% of incoming email is spam, what fraction of flagged emails are real? Do it again for a mailbox where only 1% is spam. Use counts, as in @fig-base-rate-tree.
- `chapters/ch02.qmd`
  - Before: Next: our model says 0.8. Does 0.8 really mean 80%? We'll check, find out where it lies, and fix it.
  - After: Next: our model says 0.8. Does 0.8 really mean 80%? We'll check, find out where it's wrong, and fix it.

## Chapter 3: Calibration

49 changes.

- `chapters/ch03.qmd`
  - Before: A question that sounds silly until it costs you money:
  - After: Here's a question that sounds silly until it costs you money:
- `chapters/ch03.qmd`
  - Before: Your instinct is probably "obviously": it's a probability, and that's what the number is for.
  - After: Your first answer is probably "of course": it's a probability, and that's what the number is for.
- `chapters/ch03.qmd`
  - Before: But a number is just a number. A model can say 0.8 about alerts that turn out to be attacks half the time, or nineteen times out of twenty. Nothing in the maths of the model forces its 0.8 to line up with reality. It lines up only if we built it well, trained it on the right data and checked, and even then it can drift.
  - After: But a number is just a number. A model can say 0.8 about alerts that turn out to be attacks half the time, or nineteen times out of twenty. Nothing in the maths of the model forces its 0.8 to match reality. It matches only if we built it well, trained it on the right data and checked it. Even then, it can slowly go wrong over time.
- `chapters/ch03.qmd`
  - Before: This chapter is about checking, the single most important habit in the book. Every threshold in Chapter 4, every policy in Chapter 14 and every claim about Jev in Part III rests on it.
  - After: This chapter is about checking, the most important habit in the book. Every threshold in Chapter 4, every policy in Chapter 14 and every claim about Jev in Part III depends on it.
- `chapters/ch03.qmd`
  - Before: People love to complain about forecasters. But in the 1970s, when researchers checked American weather forecasters' chance-of-rain forecasts against what actually happened, they found something surprising. When the forecasters said "30% chance of rain", it rained on roughly 30% of those days. When they said 70%, it rained roughly 70% of the time. Across the whole range, what they said and what happened lined up almost perfectly [@murphy1977].
  - After: People love to complain about weather forecasters. But in the 1970s, researchers checked American forecasters' chance-of-rain forecasts against what actually happened. They found something surprising. When the forecasters said "30% chance of rain", it rained on about 30% of those days. When they said 70%, it rained about 70% of the time. Across the whole range, what they said and what happened matched almost perfectly [@murphy1977].
- `chapters/ch03.qmd`
  - Before: Compare that with how people usually do. Ask someone to give a range they're "90% sure" contains the answer to a trivia question, and the truth lands inside far less often than 90% of the time. We are, as a species, reliably too sure of ourselves.
  - After: Compare that with most people. Ask someone for a range they're "90% sure" contains the answer to a quiz question. The true answer falls inside it far less often than 90% of the time. As a rule, people are too sure of themselves.
- `chapters/ch03.qmd`
  - Before: What makes the weather forecasters good isn't that they're always right. They can't be. It's that their numbers mean what they say. That property has a name.
  - After: The weather forecasters aren't good because they're always right. They can't be. They're good because their numbers mean what they say. That property has a name: **calibration**.
- `chapters/ch03.qmd`
  - Before: And, importantly, calibration is something you can *check*, with nothing more than grouping and counting. You collect everything the model said "about 80%" to, and count how often it happened.
  - After: And, importantly, you can *check* calibration with nothing more than grouping and counting. Collect everything the model said "about 80%" to, and count how often it happened. A calibrated model's probabilities are honest: they mean what they say.
- `chapters/ch03.qmd`
  - Before: ## Good at ranking, bad at honesty
  - After: ## Good at ranking, badly calibrated
- `chapters/ch03.qmd`
  - Before: Before we check anything, one idea needs to land, because people confuse it constantly.
  - After: Before we check anything, you need one idea, because people confuse it all the time.
- `chapters/ch03.qmd`
  - Before: The first is **ranking**: does the model give attacks higher numbers than harmless alerts? If you sort alerts by the model's score, do the real attacks rise to the top? The AUC measures this, the number you've seen in a few tables already. An AUC of 1 means every attack scored above every harmless alert. An AUC of 0.5 means the scores are no better than a coin flip.
  - After: The first is **ranking**: does the model give attacks higher numbers than harmless alerts? If you sort alerts by the model's score, do the real attacks rise to the top? The **AUC** measures this. It's the chance that a real attack, picked at random, scores higher than a harmless alert picked at random. An AUC of 1 means every attack scored above every harmless alert. An AUC of 0.5 means the scores are no better than tossing a coin.
- `chapters/ch03.qmd`
  - Before: The second is **honesty**: when the model says 0.3, do three in ten of those alerts turn out to be attacks? That's calibration.
  - After: The second is **calibration**: when the model says 0.3, do three in ten of those alerts turn out to be attacks?
- `chapters/ch03.qmd`
  - Before: The two are independent. A model can rank perfectly and still lie about how sure it is.
  - After: The two are separate. A model can rank perfectly and still be wrong about how sure it is.
- `chapters/ch03.qmd`
  - Before: @fig-same-auc shows two models with the same AUC, {{< num ch04 lr.auc f3 >}}. Model B's numbers are a mess: it says 40% about alerts that are attacks only a few percent of the time. If you only ever sort alerts, Model B is as good as Model A. The moment you put a threshold on its numbers, or add them into a cost, or show them to an analyst, it'll mislead you.
  - After: @fig-same-auc shows two models with the same AUC, {{< num ch04 lr.auc f3 >}}. Model B's numbers are badly wrong: it says 40% about alerts that are attacks only a few percent of the time. If you only ever sort alerts, Model B is as good as Model A. But as soon as you put a threshold on its numbers, use them in a cost, or show them to an analyst, it'll mislead you.
- `chapters/ch03.qmd`
  - Before: Here lies the trap: most leaderboards and most model comparisons report ranking metrics like AUC, accuracy or F1.
  - After: This is the trap: most leaderboards and model comparisons report ranking measures like AUC, accuracy or F1.
- `chapters/ch03.qmd`
  - Before: Calibration is often not measured at all. For a decision system it's usually the thing that matters most.
  - After: Calibration is often not measured at all. But for a decision system, it's usually what matters most.
- `chapters/ch03.qmd`
  - Before: 1. Take a pile of predictions where you know what happened: our test alerts from Chapter 2.
  - After: 1. Take a set of predictions where you know what happened: our test alerts from Chapter 2.
- `chapters/ch03.qmd`
  - Before: ![The reliability diagram of our Chapter 2 model on alerts it never saw. Points on the dashed diagonal mean the model's numbers can be taken at face value. Underneath, a histogram (log scale) shows how many alerts fall in each part of the range: most sit near zero, and only a handful above 50%.]
  - After: ![The reliability diagram of our Chapter 2 model on alerts it never saw. Points on the dashed diagonal mean the model's numbers can be trusted as they are. Underneath, a histogram (log scale) shows how many alerts fall in each part of the range: most are near zero, and only a few are above 50%.]
- `chapters/ch03.qmd`
  - Before: Look at @fig-anatomy-03 carefully, top and bottom together, because the bottom panel is the one people forget. Our model's points sit near the diagonal where there's lots of data. Up at the right end, the dots jump around, and the histogram tells you why: only a few dozen alerts live up there. A wobbly dot with twelve alerts behind it is weak evidence, as Chapter 2 warned. Always look at the counts before you panic, or relax.
  - After: Look at @fig-anatomy-03 carefully, top and bottom together, because people forget the bottom panel. Our model's points are near the diagonal where there's lots of data. At the right end, the dots jump around, and the histogram tells you why: only a few dozen alerts are there. A dot based on twelve alerts is weak evidence, as Chapter 2 warned. Always look at the counts before you worry, or before you relax.
- `chapters/ch03.qmd`
  - Before: Pictures are the best way to *see* calibration, but sometimes you need a single number, to compare models or to raise an alarm when it drifts. The most common is the **expected calibration error**, ECE: the average gap between "said" and "happened" across the bins, weighted by how many predictions each bin holds [@naeini2015].
  - After: Pictures are the best way to *see* calibration. But sometimes you need a single number, to compare models or to raise an alarm when calibration gets worse. The most common is the **expected calibration error**, or ECE. It's the average gap between "said" and "happened" across the bins, weighted by how many predictions each bin holds [@naeini2015].
- `chapters/ch03.qmd`
  - Before: Our logistic regression's ECE is {{< num ch04 lr.ece f3 >}}, meaning that on average, its probabilities are off by less than one percentage point. Good. Model B's is {{< num ch04 squashed.ece f2 >}}.
  - After: Our logistic regression's ECE is {{< num ch04 lr.ece f3 >}}. That means its probabilities are off by less than one percentage point on average. Good. Model B's is {{< num ch04 squashed.ece f2 >}}.
- `chapters/ch03.qmd`
  - Before: ECE has weaknesses worth knowing. It depends on how you choose the bins. And because it's an average, a model can hide terrible calibration in a small region, such as the high end where the dangerous alerts live, behind excellent calibration where most of the data sits. Report it, but always look at the picture too.
  - After: ECE has weaknesses worth knowing. It depends on how you choose the bins. And because it's an average, it can hide very bad calibration in a small region. The high end, where the dangerous alerts are, can be badly calibrated while the rest of the data is fine. Report ECE, but always look at the picture too.
- `chapters/ch03.qmd`
  - Before: The Brier score from Chapter 2 splits neatly into three parts, a result due to Allan Murphy [@murphy1973]: Brier = *reliability* − *resolution* + *uncertainty*. **Uncertainty** is how hard the problem is to begin with (it depends only on the base rate).
  - After: The **Brier score** is the average squared gap between a predicted probability and what happened (1 or 0). Allan Murphy showed that it splits into three parts [@murphy1973]: Brier = *reliability* − *resolution* + *uncertainty*. **Uncertainty** is how hard the problem is to begin with (it depends only on the base rate).
- `chapters/ch03.qmd`
  - Before: **Resolution** is how much the model's predictions separate cases that turn out differently, which is roughly the ranking skill. **Reliability** is the calibration error: the squared gap between said and happened, bin by bin. For our model: reliability {{< num ch04 decomposition.reliability f4 >}}, resolution {{< num ch04 decomposition.resolution f4 >}}, uncertainty {{< num ch04 decomposition.uncertainty f4 >}}. A model can improve its Brier score by getting better at ranking, or by getting better calibrated, and the decomposition tells you which.
  - After: **Resolution** is how well the model's predictions separate cases that turn out differently; it's close to ranking skill. **Reliability** is the calibration error: the squared gap between said and happened, bin by bin. For our model: reliability {{< num ch04 decomposition.reliability f4 >}}, resolution {{< num ch04 decomposition.resolution f4 >}}, uncertainty {{< num ch04 decomposition.uncertainty f4 >}}. A model can improve its Brier score by ranking better or by being better calibrated. The three parts tell you which.
- `chapters/ch03.qmd`
  - Before: If log loss rewards honesty, as Chapter 2 said, why would a model ever come out miscalibrated? Because the training setup can mislead it. Here are the usual suspects.
  - After: If log loss rewards calibrated probabilities, as Chapter 2 said, why would a model ever come out miscalibrated? Because the way it's trained can mislead it. Here are the usual causes.
- `chapters/ch03.qmd`
  - Before: **Rebalancing the data.** This is one of the most common, and it's usually done with the best intentions. Attacks are rare, only {{< num ch04 base pct >}} of alerts, so someone decides the model needs to "see more attacks" and trains it on a 50/50 mix: every attack, plus an equal number of randomly chosen harmless alerts. The ranking survives. But the model has learned from a world where attacks are *common*, and it faithfully reports probabilities for that world.
  - After: **Rebalancing the data.** This is one of the most common causes, and people usually do it with good intentions. Attacks are rare, only {{< num ch04 base pct >}} of alerts. So someone decides the model needs to "see more attacks" and trains it on a 50/50 mix: every attack, plus the same number of harmless alerts chosen at random. The ranking is still fine. But the model has learned from a world where attacks are *common*, and it correctly reports probabilities for that world, not ours.
- `chapters/ch03.qmd`
  - Before: The rebalanced model's average prediction is {{< num ch04 bal_mean_pred pct >}}. The real attack rate is {{< num ch04 base pct >}}. Put a threshold on those numbers and you'll drown your analysts.
  - After: The rebalanced model's average prediction is {{< num ch04 bal_mean_pred pct >}}. The real attack rate is {{< num ch04 base pct >}}. Put a threshold on those numbers and you'll send your analysts far more alerts than they can handle.
- `chapters/ch03.qmd`
  - Before: **Scores that were never probabilities.** Some models output a "score" that happens to fall between 0 and 1 but was never trained with a proper scoring rule. Treat it as a ranking until you've checked it.
  - After: **Scores that were never probabilities.** Some models output a "score" that happens to be between 0 and 1 but was never trained with a proper scoring rule. Treat it as a ranking until you've checked it.
- `chapters/ch03.qmd`
  - Before: **Big modern networks.** Surprisingly, very large neural networks trained for classification tend to be *overconfident* [@guo2017]. Chapter 5 looks at why. And the "confidence" an LLM states in words is a different animal again. Chapter 6 measures it.
  - After: **Big modern networks.** Surprisingly, very large neural networks trained to sort things into classes tend to be *overconfident* [@guo2017]. Chapter 5 looks at why. The "confidence" an LLM states in words is a different thing again; Chapter 6 measures it.
- `chapters/ch03.qmd`
  - Before: **The world changing.** A model calibrated on last month's base rate is miscalibrated the day a campaign doubles the number of attacks. Chapter 14 will watch it happen.
  - After: **The world changing.** A model calibrated on last month's base rate is miscalibrated on the day an attack campaign doubles the number of attacks. Chapter 14 shows this happening.
- `chapters/ch03.qmd`
  - Before: The good news: a model with good ranking and bad calibration is usually easy to fix. You don't retrain it. You put a small correction on top.
  - After: The good news: a model that ranks well but is badly calibrated is usually easy to fix. You don't retrain it. You add a small correction on top.
- `chapters/ch03.qmd`
  - Before: The recipe is always the same. Hold back a **calibration set**, data the model never trained on. That's the 20% we set aside in Chapter 2. Run the model on it, and learn a simple function that maps the model's raw probabilities to calibrated ones. Then check the result on the *test* set, which neither the model nor the correction has seen.
  - After: The method is always the same. Keep back a **calibration set**: data the model never trained on. Run the model on it, and learn a simple function that turns the model's raw probabilities into calibrated ones. Then check the result on the *test* set, which neither the model nor the correction has seen.
- `chapters/ch03.qmd`
  - Before: **Platt scaling** fits a tiny logistic regression on top of the model's log-odds: two numbers, a stretch and a shift [@platt1999]. It's the usual first choice.
  - After: **Platt scaling** fits a tiny logistic regression on top of the model's log-odds. It learns two numbers: a stretch and a shift [@platt1999]. It's the usual first choice.
- `chapters/ch03.qmd`
  - Before: **Temperature scaling** fits just one number, *T*, and divides the log-odds by it [@guo2017]. *T* above 1 softens overconfident predictions; below 1 sharpens timid ones. It's the standard fix for overconfident neural networks, and it's what people usually mean when they talk about calibrating an LLM classifier.
  - After: **Temperature scaling** fits just one number, *T*, and divides the log-odds by it [@guo2017]. A *T* above 1 softens overconfident predictions; a *T* below 1 sharpens predictions that are too cautious. It's the standard fix for overconfident neural networks. It's also what people usually mean by calibrating an LLM classifier.
- `chapters/ch03.qmd`
  - Before: **Isotonic regression** fits a staircase that only ever goes up [@zadrozny2002]. It can fix almost any shape, but it needs more data and can overfit a small calibration set.
  - After: **Isotonic regression** fits a staircase that only ever goes up [@zadrozny2002]. It can fix almost any shape, but it needs more data, and it can overfit a small calibration set.
- `chapters/ch03.qmd`
  - Before: Platt and isotonic fix the rebalanced model almost completely. Temperature scaling doesn't help at all, and the reason teaches you something. Rebalancing didn't make the model overconfident. It *shifted* every prediction upwards, as if attacks were common. A temperature can only stretch or squeeze predictions around 0.5. It can't slide them all down. Platt can, because it has a shift as well as a stretch.
  - After: Platt and isotonic fix the rebalanced model almost completely. Temperature scaling doesn't help at all, and the reason teaches you something. Rebalancing didn't make the model overconfident. It *moved* every prediction up, as if attacks were common. A temperature can only stretch or squeeze predictions around 0.5. It can't move them all down. Platt can, because it has a shift as well as a stretch.
- `chapters/ch03.qmd`
  - Before: ## Honest on average, dishonest in the corner
  - After: ## Calibrated on average, wrong for one group
- `chapters/ch03.qmd`
  - Before: One more trap, and it's the one that bites in production.
  - After: There's one more trap, and it's the one that causes problems in real systems.
- `chapters/ch03.qmd`
  - Before: A model can be well calibrated *overall* and badly calibrated for a particular group. Take a version of our model trained without knowing which detection rule fired, so it can't tell an email alert from an endpoint one.
  - After: A model can be well calibrated *overall* and badly calibrated for one group. Take a version of our model trained without knowing which detection rule fired. It can't tell an email alert from an alert on a laptop or server (an "endpoint").
- `chapters/ch03.qmd`
  - Before: Its overall ECE is excellent, {{< num ch04 generic.ece f3 >}}. Yet for endpoint (EDR) alerts it says
  - After: Its overall ECE is excellent, {{< num ch04 generic.ece f3 >}}. Yet for endpoint alerts, which come from EDR (endpoint detection and response) tools, it says
- `chapters/ch03.qmd`
  - Before: The over- and under-estimates cancel out in the average.
  - After: The estimates that are too high and too low cancel out in the average.
- `chapters/ch03.qmd`
  - Before: If your policy treats every source the same way, you'll send too many harmless DLP alerts to the queue and close too many real EDR ones. The rule is simple: **check calibration inside every group you'll act on differently**, and inside every group where a mistake would be especially costly. Sources, customer tiers, languages, regions, and yes, demographic groups when a model touches people's lives.
  - After: If your policy treats every source the same way, you'll send too many harmless DLP alerts to the queue and close too many real EDR ones. The rule is simple: **check calibration inside every group you'll treat differently**, and inside every group where a mistake would be especially costly. That means sources, customer tiers, languages and regions. It also means groups of people, such as age or gender, when a model affects people's lives.
- `chapters/ch03.qmd`
  - Before: Kestrel auto-closes any alert under 3%. The model above says EDR alerts average {{< num ch04 by_source.EDR.pred pct1 >}} risk, but they're really {{< num ch04 by_source.EDR.actual pct1 >}}. Roughly how much more often than planned will a real EDR threat be auto-closed? What are two different ways to fix this: one that changes the model, and one that changes only the policy?
  - After: Kestrel auto-closes any alert under 3%. The model above says EDR alerts average {{< num ch04 by_source.EDR.pred pct1 >}} risk, but they're really {{< num ch04 by_source.EDR.actual pct1 >}}. About how much more often than planned will a real EDR threat be auto-closed? Name two ways to fix this: one that changes the model, and one that changes only the policy.
- `chapters/ch03.qmd`
  - Before: (About half as often again. You could add the source as a feature, or calibrate separately per source, so the model's numbers hold up for every source. Or you could keep the model and set a stricter act line for EDR alerts. The first is better; the second is quicker.)
  - After: (About 50% more often. You could add the source as a clue, or calibrate separately for each source, so the model is calibrated for every source. Or you could keep the model and set a stricter act threshold for EDR alerts. The first is better; the second is quicker.)
- `chapters/ch03.qmd`
  - Before: Calibration is always measured *on some data*, and it's only guaranteed for data like that. A model calibrated on last quarter's alerts can drift as tools, attackers and staff change. Isotonic regression fitted on a few hundred examples will overfit and produce jagged, overconfident corrections. And calibration says nothing about any *single* prediction: a perfectly calibrated 70% is still wrong three times in ten. Keep a fresh calibration set, refit on a schedule, and keep watching the diagram.
  - After: Calibration is always measured *on some data*, and it only holds for data like that. A model calibrated on last quarter's alerts can become less calibrated as tools, attackers and staff change. Isotonic regression fitted on a few hundred examples will overfit and produce rough, overconfident corrections. And calibration says nothing about any *single* prediction: a perfectly calibrated 70% is still wrong three times in ten. Keep a fresh calibration set, refit on a schedule, and keep watching the diagram.
- `chapters/ch03.qmd`
  - Before: The weather forecasters showed us that honesty is checkable. Then two models with the same ranking and very different calibration showed us why checking matters. Grouping and counting gave us the reliability diagram, and a well-meant rebalancing broke it. A small correction fitted on held-out data put it back. And just when the average looked fine, the EDR alerts reminded us to look inside every group we'll act on.
  - After: The weather forecasters showed us that calibration can be checked. Then two models with the same ranking and very different calibration showed us why checking matters. Grouping and counting gave us the reliability diagram, and a well-meant rebalancing broke calibration. A small correction fitted on held-out data fixed it. And just when the average looked fine, the EDR alerts reminded us to look inside every group we'll treat differently.
- `chapters/ch03.qmd`
  - Before: When Part III tests Jev's own calibration, it'll use these same tools, pointed at the mock, with everything in this chapter as the yardstick.
  - After: When Part III tests Jev's own calibration, it'll use these same tools on the mock, and measure it against everything in this chapter.
- `chapters/ch03.qmd`
  - Before: 1. Explain to a colleague, without jargon, the difference between a model that ranks well and a model that's calibrated. Use a weather example.
  - After: 1. Explain to a colleague, without technical words, the difference between a model that ranks well and a model that's calibrated. Use a weather example.
- `chapters/ch03.qmd`
  - Before: Next: we finally have probabilities we can trust. Chapter 4 turns them into actions: what each mistake costs, where the lines go, and how to see the whole trade-off on one page.
  - After: Next: we finally have calibrated probabilities. Chapter 4 turns them into actions: what each mistake costs, where the thresholds go, and how to see the whole trade-off on one page.

## Chapter 3 (continued)

3 changes.

- `chapters/ch03.qmd`
  - Before: Yet for endpoint alerts, which come from EDR (endpoint detection and response) tools, it says {{< num ch04 by_source.EDR.pred pct1 >}} when the truth is {{< num ch04 by_source.EDR.actual pct1 >}}, and for DLP alerts (data loss prevention: warnings that company data may be leaving the building) it says {{< num ch04 by_source.DLP.pred pct1 >}} when the truth is {{< num ch04 by_source.DLP.actual pct1 >}}.
  - After: Endpoint alerts come from EDR (endpoint detection and response) tools. For them, it says {{< num ch04 by_source.EDR.pred pct1 >}} when the truth is {{< num ch04 by_source.EDR.actual pct1 >}}. DLP (data loss prevention) alerts warn that company data may be leaving the building. For them, it says {{< num ch04 by_source.DLP.pred pct1 >}} when the truth is {{< num ch04 by_source.DLP.actual pct1 >}}.
- `chapters/ch03.qmd`
  - Before: Its overall ECE is excellent, {{< num ch04 generic.ece f3 >}}.
  - After: Its overall ECE is excellent: {{< num ch04 generic.ece f3 >}}.
- `chapters/ch03.qmd`
  - Before: **Overfitting.** Flexible models that memorise, like the deep decision tree from Chapter 2, push their probabilities towards 0 and 1, because on the training data they really were that sure.
  - After: **Overfitting.** Flexible models that memorise, like the deep decision tree from Chapter 2, push their probabilities towards 0 and 1. On the training data, they really were that sure.

## Chapter 4: From probabilities to actions

45 changes.

- `chapters/ch04.qmd`
  - Before: And now you hit the wall everyone hits:
  - After: And now you reach the problem everyone reaches:
- `chapters/ch04.qmd`
  - Before: *"Great. So where do I put the line?"*
  - After: *"Great. So where do I put the threshold?"*
- `chapters/ch04.qmd`
  - Before: Most people pick 0.5 without thinking about it. It's the default in almost every library. It *feels* neutral.
  - After: Most people pick 0.5 without thinking about it. It's the default in almost every library. It *feels* neutral.
- `chapters/ch04.qmd`
  - Before: It isn't neutral at all. It's a very specific opinion about your business, and it's usually the wrong one. This chapter shows you how to put the line where it belongs, with nothing fancier than the arithmetic you already have.
  - After: It isn't neutral at all. It's a very specific opinion about your business, and it's usually the wrong one. This chapter shows you how to put the threshold where it belongs, using only the arithmetic you already know.
- `chapters/ch04.qmd`
  - Before: - Check the formula against a brute-force search on real (synthetic) data.
  - After: - Check the formula against a search that tries every threshold, on realistic (synthetic) data.
- `chapters/ch04.qmd`
  - Before: Let's start somewhere dry. Well, somewhere that might not be.
  - After: Let's start with the weather again.
- `chapters/ch04.qmd`
  - Before: It depends on two things you already know without thinking about them. Carrying an umbrella you didn't need is mildly annoying; call it 1 unit of annoyance. Getting soaked on the way to a meeting is much worse; call it 4.
  - After: It depends on two things you already know without thinking about them. Carrying an umbrella you didn't need is a little annoying; call it 1 unit of annoyance. Getting very wet on the way to a meeting is much worse; call it 4.
- `chapters/ch04.qmd`
  - Before: If you carry it, you pay 1, rain or shine. If you leave it, you pay 4, but only if it rains, so on average you pay 4 × the chance of rain.
  - After: If you carry it, you pay 1, rain or not. If you leave it, you pay 4, but only if it rains. So on average you pay 4 × the chance of rain.
- `chapters/ch04.qmd`
  - Before: - a **false alarm**: you act, and you didn't need to (carried the umbrella; blocked a harmless login);
  - After: - a **false alarm**: you act, and you didn't need to (you carried the umbrella; you blocked a harmless login);
- `chapters/ch04.qmd`
  - Before: - a **miss**: you don't act, and you should have (got soaked; let an attacker in).
  - After: - a **miss**: you don't act, and you should have (you got wet; you let an attacker in).
- `chapters/ch04.qmd`
  - Before: Check it with the umbrella: 1 ÷ (1 + 4) = 0.2. Exactly where the lines crossed.
  - After: Check it with the umbrella: 1 ÷ (1 + 4) = 0.2. That's exactly where the two lines crossed.
- `chapters/ch04.qmd`
  - Before: Now look at what happens when the two costs are equal. The formula gives 1 ÷ 2 = 0.5. *That's* where 0.5 comes from. It's the right threshold only when a false alarm and a miss hurt the same amount, which is almost never true for anything worth building a model for.
  - After: Now look at what happens when the two costs are equal. The formula gives 1 ÷ 2 = 0.5. *That's* where 0.5 comes from. It's the right threshold only when a false alarm and a miss hurt the same amount. That's almost never true for anything worth building a model for.
- `chapters/ch04.qmd`
  - Before: ![The right threshold for any ratio between the cost of a miss and the cost of a false alarm (both axes on a log scale). Equal costs give 0.5. As misses get more expensive, the line drops fast.]
  - After: ![The right threshold for any ratio between the cost of a miss and the cost of a false alarm (both axes on a log scale). Equal costs give 0.5. As misses get more expensive, the threshold drops fast.]
- `chapters/ch04.qmd`
  - Before: @fig-threshold-ratio puts a few real decisions on one curve. Kestrel's decision in Chapter 14, whether an alert may close itself without any human looking at it, sits in the far bottom-right corner: a miss there is about 630 times worse than an analyst's twelve minutes, so the line drops to about {{< num ch05 soc_review_t f4 >}}. Different decision, different costs, different line.
  - After: @fig-threshold-ratio puts a few real decisions on one curve. In Chapter 14, Kestrel decides whether an alert may close itself without any person looking at it. That decision is in the far bottom-right corner. A miss there is about 630 times worse than twelve minutes of an analyst's time, so the threshold drops to about {{< num ch05 soc_review_t f4 >}}. A different decision has different costs, so it gets a different threshold.
- `chapters/ch04.qmd`
  - Before: Where the formula comes from. For a single case with probability *P*, acting costs (1 − *P*) × *C*~fa~ on average (you pay only if it was harmless), and not acting costs *P* × *C*~miss~ (you pay only if it was real). Act when the first is smaller: (1 − *P*) *C*~fa~ < *P* *C*~miss~, which rearranges to *P* > *C*~fa~ / (*C*~fa~ + *C*~miss~). If getting it *right* also has costs or benefits (say, blocking a real threat earns some credit), the same logic works with a 2×2 table of costs, one for each combination of action and truth. This is the foundation of cost-sensitive learning [@elkan2001].
  - After: Where the formula comes from. For a single case with probability *P*, acting costs (1 − *P*) × *C*~fa~ on average, because you pay only if it was harmless. Not acting costs *P* × *C*~miss~, because you pay only if it was real. Act when the first is smaller: (1 − *P*) *C*~fa~ < *P* *C*~miss~. Rearranged, that's *P* > *C*~fa~ / (*C*~fa~ + *C*~miss~). Getting it *right* can also have costs or benefits; for example, blocking a real threat might earn some credit. Then the same logic works with a 2×2 table of costs, one for each combination of action and truth. This is the basis of cost-sensitive learning [@elkan2001].
- `chapters/ch04.qmd`
  - Before: A formula is nice. Evidence is better. Let's test it.
  - After: A formula is nice, but evidence is better. Let's test it.
- `chapters/ch04.qmd`
  - Before: Kestrel makes one decision on every alert: **block it or allow it?** Block the sender, the connection or the sign-in, automatically. Wrongly blocking something harmless costs about \$200 in disrupted work: a stuck shipment, an angry customer, an engineer locked out. Letting a real threat through at this step costs about \$4,000, since other defences still have a chance to catch it later. Those are illustrative numbers, but plausible ones.
  - After: Kestrel makes one decision on every alert: **block it or allow it?** Blocking means automatically stopping the sender, the connection or the sign-in. Wrongly blocking something harmless costs about \$200 in lost work: a delayed shipment, an angry customer, an engineer who can't sign in. Letting a real threat through at this step costs about \$4,000, since other defences still have a chance to catch it later. Those numbers are illustrative, but realistic.
- `chapters/ch04.qmd`
  - Before: Compare the formula with a brute-force search over 300 thresholds, using the calibrated logistic regression from Chapter 2 on the test alerts.
  - After: Compare the formula with a search that tries 300 thresholds, using the calibrated logistic regression from Chapter 2 on the test alerts.
- `chapters/ch04.qmd`
  - Before: The formula lands close to the brute-force best, and the cost difference is small. The 0.5 line costs {{< num ch05 half_penalty f1 >}} times as much.
  - After: The formula lands close to the best threshold the search found, and the cost difference is small. A threshold of 0.5 costs {{< num ch05 half_penalty f1 >}} times as much.
- `chapters/ch04.qmd`
  - Before: ![Total cost on the test alerts at every threshold. For the calibrated model (green), the formula's line sits near the bottom of the valley. For the same model trained on rebalanced data (red), the same line lands halfway up the wall.]
  - After: ![Total cost on the test alerts at every threshold. For the calibrated model (green), the formula's threshold is near the lowest point of the curve. For the same model trained on rebalanced data (red), the same threshold lands far from its lowest point.]
- `chapters/ch04.qmd`
  - Before: And now the reason Chapter 3 came first. @fig-cost-curve also shows the rebalanced model from Chapter 3, which ranks alerts almost as well but whose probabilities are inflated. Put the formula's line on *its* numbers and the cost is {{< num ch05 bal_penalty pct >}} higher. Its own cheapest line is way out at about {{< num ch05 t_bal_best f2 >}}, and there's no formula that could have told you so. You'd have to find it by trial and error, and redo the search every time the costs change.
  - After: And now you can see why Chapter 3 came first. @fig-cost-curve also shows the rebalanced model from Chapter 3. It ranks alerts almost as well, but its probabilities are too high. Use the formula's threshold on *its* numbers and the cost is {{< num ch05 bal_penalty pct >}} higher. Its own cheapest threshold is far away, at about {{< num ch05 t_bal_best f2 >}}, and no formula could have told you so. You'd have to find it by trial and error, and search again every time the costs change.
- `chapters/ch04.qmd`
  - Before: With calibrated probabilities, costs set the line directly. Without them, you're guessing.
  - After: With calibrated probabilities, costs set the threshold directly. Without them, you're guessing.
- `chapters/ch04.qmd`
  - Before: That's the practical payoff of calibration, in one sentence. It turns threshold-setting from an endless tuning exercise into a line of arithmetic you can explain to your finance team.
  - After: That's the practical value of calibration, in one sentence. It turns setting a threshold from endless trial and error into one line of arithmetic you can explain to your finance team.
- `chapters/ch04.qmd`
  - Before: In Chapter 2, precision and recall looked like two scores. Now you can see them for what they are: two ends of the same rope.
  - After: In Chapter 2, precision and recall looked like two separate scores. Now you can see what they really are: two sides of one trade-off. When one goes up, the other goes down.
- `chapters/ch04.qmd`
  - Before: ![As the threshold moves up, precision (how many blocks were real) rises and recall (how many threats got blocked) falls. The grey line shows how much traffic you're blocking. The vertical line is the cost-based threshold.]
  - After: ![As the threshold moves up, precision (how many blocks were real) rises and recall (how many threats got blocked) falls. The grey curve shows how much traffic you're blocking. The vertical line is the cost-based threshold.]
- `chapters/ch04.qmd`
  - Before: At the cost-based line in @fig-pr-threshold, Kestrel blocks about {{< num ch05 blocked_frac pct >}} of alerts. That catches {{< num ch05 caught pct >}} of real threats, but only {{< num ch05 precision pct >}} of the blocks are real ones. That precision sounds poor. Is it?
  - After: At the cost-based threshold in @fig-pr-threshold, Kestrel blocks about {{< num ch05 blocked_frac pct >}} of alerts. That catches {{< num ch05 caught pct >}} of real threats, but only {{< num ch05 precision pct >}} of the blocks are real ones. That precision sounds poor. Is it?
- `chapters/ch04.qmd`
  - Before: Only the costs can say. Each wrong block costs \$200; each missed threat \$4,000. The line sits at 200 ÷ 4,200, about {{< num ch05 t_formula f3 >}}: block an alert when the chance it's real is better than about 1 in 21. The rule is about the *marginal* alert, the one sitting right on the line, where blocking and letting it through cost the same on average.
  - After: Only the costs can say. Each wrong block costs \$200; each missed threat costs \$4,000. The threshold is 200 ÷ 4,200, about {{< num ch05 t_formula f3 >}}: block an alert when the chance it's real is better than about 1 in 21. The rule is about the alert that sits *exactly* on the threshold. For that alert, blocking it and letting it through cost the same on average.
- `chapters/ch04.qmd`
  - Before: Precision is a different thing: an average over *every* alert above the line, and most of those are far likelier than 1 in 21 to be real, which is why it comes out nearer one in five. Nobody chose that number; it falls out of putting the line where the costs say, and a model with better ranking would push it up without moving the line at all. Arguing about precision or recall on its own, without the costs, is arguing about half a sentence.
  - After: Precision is a different thing. It's an average over *every* alert above the threshold, and most of those are far more likely than 1 in 21 to be real. That's why precision comes out nearer one in five. Nobody chose that number. It's simply what happens when you put the threshold where the costs say. A model that ranks better would raise precision without moving the threshold at all. So precision or recall alone, without the costs, tells you only part of the story.
- `chapters/ch04.qmd`
  - Before: Kestrel's sales team complains that blocked customer emails are costing deals, and argues a wrong block costs \$800, not \$200. Recompute the blocking line. Roughly what happens to the share of alerts blocked, and to recall?
  - After: Kestrel's sales team complains that blocked customer emails are losing them sales. They say a wrong block costs \$800, not \$200. Work out the blocking threshold again. About what happens to the share of alerts blocked, and to recall?
- `chapters/ch04.qmd`
  - Before: (800 ÷ 4,800 ≈ 0.17. The line moves up, fewer alerts get blocked and more threats get through. The model didn't change. The business's priorities did, and the threshold should follow them.)
  - After: (800 ÷ 4,800 ≈ 0.17. The threshold moves up, fewer alerts get blocked, and more threats get through. The model didn't change. The business's priorities did, and the threshold should follow them.)
- `chapters/ch04.qmd`
  - Before: The idea is old. In 1970 the engineer C. K. Chow showed that a recogniser allowed to reject its least certain cases could cut its error rate dramatically, and worked out the best trade-off [@chow1970]. Today it's called *selective prediction*, or classification with a reject option [@geifman2017].
  - After: The idea is old. In 1970, the engineer C. K. Chow showed something about systems that recognise characters. If they were allowed to refuse their least certain cases, their error rate fell sharply. He also worked out the best trade-off [@chow1970]. Today this is called *selective prediction*, or classification with a reject option [@geifman2017].
- `chapters/ch04.qmd`
  - Before: At Kestrel it works like this. Sort the alerts by how confident the model is, surest first. Let the machine decide only the top slice, and send the rest to people. How low does the error rate go?
  - After: At Kestrel it works like this. Sort the alerts by how confident the model is, surest first. Let the machine decide only the top part of the list, and send the rest to people. How low does the error rate go?
- `chapters/ch04.qmd`
  - Before: Deciding every alert, the model gets {{< num ch05 risk_100 pct1 >}} wrong. Deciding only the surest 80%, just {{< num ch05 risk_80 pct1 >}} of its decisions are wrong. Deciding the surest half, {{< num ch05 risk_50 pct1 >}}.
  - After: Deciding every alert, the model gets {{< num ch05 risk_100 pct1 >}} wrong. Deciding only the surest 80%, just {{< num ch05 risk_80 pct1 >}} of its decisions are wrong. Deciding the surest half, only {{< num ch05 risk_50 pct1 >}} are wrong.
- `chapters/ch04.qmd`
  - Before: That curve, from @fig-coverage-risk, is one of the most useful pictures you can show a manager. It turns "how good is the model?" into "how much of this work can we safely hand over, at what error rate?", which is the question they actually have.
  - After: That curve, in @fig-coverage-risk, is one of the most useful pictures you can show a manager. It changes the question from "how good is the model?" to "how much of this work can we safely hand over, at what error rate?". That's the question managers actually have.
- `chapters/ch04.qmd`
  - Before: Put the two ideas together, cost-based lines and "ask a person", and a shape appears that we'll use for the rest of the book.
  - After: Put the two ideas together, cost-based thresholds and "ask a person", and you get a design we'll use for the rest of the book.
- `chapters/ch04.qmd`
  - Before: ![The three doors. At one end the model is confident nothing's needed, so the machine handles it. At the other end it's confident something's badly wrong, so a person is pulled in immediately. In between, where it's unsure, a person looks when they can.]
  - After: ![The three doors. At one end the model is confident nothing's needed, so the machine handles it. At the other end it's confident something's badly wrong, so a person is called in immediately. In between, where it's unsure, a person looks when they can.]
- `chapters/ch04.qmd`
  - Before: **Act** when the model is confident the machine can handle it alone. **Review** when it's unsure, so a person checks in the normal flow of work. **Escalate** when it's confident something important is wrong, so a person is pulled in right now.
  - After: **Act** when the model is confident the machine can handle it alone. **Review** when it's unsure, so a person checks it as part of normal work. **Escalate** when it's confident something important is wrong, so a person is called in right now. These three choices are the book's three zones: act, review and escalate.
- `chapters/ch04.qmd`
  - Before: The two boundaries between the doors come from the same kind of cost arithmetic you've just done, with one extra line for each extra action. Chapter 14 does that for Kestrel's SOC, and then does the part this chapter skips: what happens when you don't have enough people to staff the middle door.
  - After: The two boundaries between the zones come from the same kind of cost arithmetic you've just done, with one extra threshold for each extra action. Chapter 14 does that for Kestrel's SOC. Then it does the part this chapter skips: what happens when you don't have enough people for the middle zone.
- `chapters/ch04.qmd`
  - Before: Costs are guesses, and guesses carry the same weight in the formula as facts. Two habits help. First, try your costs at half and double their value and see how much the line moves; if the answer barely changes, stop arguing about the exact number. Second, remember that costs often differ from case to case: a false alarm on the CEO's laptop isn't a false alarm on a test server. Per-case costs mean per-case thresholds, which is fine, as long as you write them down. And some costs aren't money at all: trust, fairness, safety and the law. Put those on the table explicitly, or someone else's defaults will decide them for you.
  - After: Costs are guesses, and the formula treats guesses exactly like facts. Two habits help. First, try your costs at half and at double their value, and see how much the threshold moves. If the answer barely changes, stop arguing about the exact number. Second, remember that costs often differ from case to case. A false alarm on the CEO's laptop costs more than a false alarm on a test server. Different costs for different cases mean different thresholds, and that's fine, as long as you write them down. And some costs aren't money at all: trust, fairness, safety and the law. Discuss those openly, or someone else's default settings will decide them for you.
- `chapters/ch04.qmd`
  - Before: The same goes for cost estimates. The numbers will be wrong. Writing them down, arguing about them and seeing what they imply is where the value is.
  - After: The same is true of cost estimates. The numbers will be wrong. The value comes from writing them down, discussing them and seeing what they lead to.
- `chapters/ch04.qmd`
  - Before: In Chapter 1 a machine learned what we asked and was useless, because we asked for yes or no. So we asked for a chance instead, and had to learn what a chance means. That took us to a model that outputs one, and then to the uncomfortable discovery that its number might not be honest. Once we could check and fix that, the last step was the one this chapter took: letting costs, not habit, decide where the lines go, and leaving a door open for the cases a machine shouldn't decide alone.
  - After: In Chapter 1, a machine learned what we asked and was useless, because we asked for yes or no. So we asked for a chance instead, and had to learn what a chance means. That led to a model that outputs one, and then to an uncomfortable discovery: its number might not be calibrated. Once we could check and fix that, this chapter took the last step. We let costs, not habit, decide where the thresholds go. And we left a door open for the cases a machine shouldn't decide alone.
- `chapters/ch04.qmd`
  - Before: Everything else stands on this. Every system in the rest of the book, from deep networks to LLMs to Jev, gets judged by it.
  - After: Everything else is built on this. Every system in the rest of the book, from deep networks to LLMs to Jev, is judged by it.
- `chapters/ch04.qmd`
  - Before: 4. Using the coverage–risk curve, how much of Kestrel's blocking decision could you automate if the business tolerates a 2% error rate among automated decisions? Where would the rest go?
  - After: 4. Using the coverage–risk curve, how much of Kestrel's blocking decision could you automate if the business accepts a 2% error rate among automated decisions? Where would the rest go?
- `chapters/ch04.qmd`
  - Before: 5. Pick a decision at your work or in your life with a natural third option ("ask someone", "wait a day", "get a second opinion"). Sketch its three doors and what would move each boundary.
  - After: 5. Pick a decision at your work or in your life with a natural third option ("ask someone", "wait a day", "get a second opinion"). Draw its three doors and say what would move each boundary.
- `chapters/ch04.qmd`
  - Before: Next, Part II: so far our models were handed neat features like a threat-intel score. What about raw pixels, raw words, raw logs? That's where deep learning comes in, and it starts with a single artificial neuron.
  - After: Next, Part II. So far, our models were given neat clues like a threat-intel score. What about raw pixels, raw words, raw logs? That's where deep learning comes in, and it starts with a single artificial neuron.

## Chapter 7: RAG, agents, and where they break

33 changes.

- `chapters/ch07.qmd`
  - Before: Ask a big LLM what `svc-backup` is allowed to do at Kestrel Logistics and you'll get an answer. A confident, well-written, entirely invented answer.
  - After: Ask a big LLM what `svc-backup` is allowed to do at Kestrel Logistics and you'll get an answer. It will be a confident, well-written, completely invented answer.
- `chapters/ch07.qmd`
  - Before: It isn't lying. It has simply never seen Kestrel's service-account inventory. Nobody outside Kestrel has.
  - After: It isn't lying. It has simply never seen Kestrel's list of service accounts. Nobody outside Kestrel has.
- `chapters/ch07.qmd`
  - Before: So people hand the model the right pages at the right moment. Then they give it tools and a loop, so it can look things up and act on what it finds. Most of today's excitement about AI lives in retrieval and agents. So do most of the silent failures, and this chapter walks through both. Watch closely, because one pattern keeps appearing: nearly every weak point is a small decision.
  - After: So people give the model the right pages at the right moment. Then they give it tools and a loop, so it can look things up and act on what it finds. Most of today's excitement about AI is about retrieval and agents. So are most of the failures nobody notices, and this chapter goes through both. Watch closely, because one pattern keeps appearing: nearly every weak point is a small decision.
- `chapters/ch07.qmd`
  - Before: - Explain why errors compound over a loop.
  - After: - Explain why errors add up over a loop.
- `chapters/ch07.qmd`
  - Before: ## Hand it the right page
  - After: ## Give it the right page
- `chapters/ch07.qmd`
  - Before: The idea fits in one breath. Before the model answers, **search** your documents for the passages most relevant to the question, **paste** them into the prompt, and **ask** the model to answer from them. It's called retrieval-augmented generation, RAG, and it works because the model conditions every token on everything in its context [@lewis2020].
  - After: The idea is short. Before the model answers, **search** your documents for the passages most relevant to the question. **Paste** them into the prompt, and **ask** the model to answer from them. It's called retrieval-augmented generation, or RAG. It works because every token the model writes depends on everything in its **context window**: the text it can read at once [@lewis2020].
- `chapters/ch07.qmd`
  - Before: For Kestrel I wrote a small synthetic knowledge base of {{< num ch12 n_docs int >}} policies and runbooks, and mixed in 300 old alert descriptions that use the same vocabulary and contain none of the answers. Real search indexes are like that: full of near-misses.
  - After: For Kestrel, I wrote a small synthetic collection of {{< num ch12 n_docs int >}} policies and how-to guides. I mixed in 300 old alert descriptions that use the same words but contain none of the answers. Real search indexes are like that: full of passages that look relevant but aren't.
- `chapters/ch07.qmd`
  - Before: The first hit has the answer: `svc-backup` copies snapshots offsite every night between 01:00 and 04:00. Searching by character pieces (so "passw0rd" still overlaps "password"), the right chunk came first {{< num ch12 recall.char.0 pct >}} of the time and was in the top three {{< num ch12 recall.char.2 pct >}} of the time.
  - After: The first result has the answer: `svc-backup` copies snapshots to another site every night between 01:00 and 04:00. We searched by small pieces of words, so "passw0rd" still matches "password". The right chunk came first {{< num ch12 recall.char.0 pct >}} of the time and was in the top three {{< num ch12 recall.char.2 pct >}} of the time.
- `chapters/ch07.qmd`
  - Before: One part decides whether a RAG system is any good, and it isn't the LLM. If the chunk with the answer isn't retrieved, no model can use it. The LLM will produce the most plausible answer from what it *can* see, assembled from the nearest-looking chunk. Fluent, cited, wrong.
  - After: One part decides whether a RAG system is any good, and it isn't the LLM. If the chunk with the answer isn't found, no model can use it. The LLM will build the most likely-sounding answer from what it *can* see, using the chunk that looks closest. The answer will be fluent, with a source, and wrong.
- `chapters/ch07.qmd`
  - Before: Some questions have no answer in the documents at all: "What's our cyber insurance deductible?" A good system says so. There's a simple signal: how well the *best* chunk matches.
  - After: Some questions have no answer in the documents at all: "How much must we pay ourselves before our cyber insurance pays?" A good system says it doesn't know. There's a simple signal: how well the *best* chunk matches.
- `chapters/ch07.qmd`
  - Before: They overlap, but not much. Below a line, the system should decline to answer.]
  - After: They overlap, but not much. Below a threshold, the system should decline to answer.]
- `chapters/ch07.qmd`
  - Before: With the line where I've drawn it, the system answers {{< num ch12 answered_share pct >}} of answerable questions and only {{< num ch12 unans_answered pct >}} of unanswerable ones (@fig-abstain). Where the line should go depends on what a wrong answer costs against an unnecessary "I don't know", which is Chapter 4's arithmetic.
  - After: With the threshold where I've put it, the system answers {{< num ch12 answered_share pct >}} of answerable questions and only {{< num ch12 unans_answered pct >}} of unanswerable ones (@fig-abstain). Where the threshold should go depends on what a wrong answer costs, compared with an unnecessary "I don't know". That's Chapter 4's arithmetic.
- `chapters/ch07.qmd`
  - Before: Notice what just happened. Inside a system built for *generating* answers, the step that decides whether to answer at all is a small yes-or-no decision with a score and a threshold. So is deciding what an agent should remember, which past cases are relevant and which retrieved fact is trustworthy enough to act on. Keep counting.
  - After: Notice what just happened. This system is built for *writing* answers. But the step that decides whether to answer at all is a small yes-or-no decision with a score and a threshold. So is deciding what an agent should remember, which past cases are relevant, and which retrieved fact is reliable enough to act on. Keep counting.
- `chapters/ch07.qmd`
  - Before: "Agent" might be the most overused word in AI right now. Strip away the marketing and it's a simple thing: a model in a **loop**, with **tools**. It looks at the situation, decides what to do, does it, looks at what happened, and goes round again.
  - After: "Agent" may be the most overused word in AI right now. Without the marketing, it's a simple thing: a model in a **loop**, with **tools**. It looks at the situation, decides what to do, does it, looks at what happened, and goes round again.
- `chapters/ch07.qmd`
  - Before: Military strategists had a name for this long before AI did. The US Air Force colonel John Boyd described the OODA loop, observe, orient, decide, act, to explain why fighter pilots who cycled through it faster tended to win [@boyd1987]. I'll use the simpler **Observe, Decide, Act**.
  - After: Military planners had a name for this long before AI did. The US Air Force colonel John Boyd described the OODA loop: observe, orient, decide, act. He used it to explain why fighter pilots who went through the loop faster tended to win [@boyd1987]. I'll use the simpler **Observe, Decide, Act**.
- `chapters/ch07.qmd`
  - Before: A "tool call" makes it sound as if the model reaches out and presses buttons. It doesn't. The model *writes down* which tool it wants and with what arguments, usually as the structured output of Chapter 6 [@yao2023; @schick2023]. Your code checks that request, runs the tool if it's allowed, and hands back the result. Look at what the request is: a choice from a fixed list of tools, plus some values. It's a typed decision wearing a costume. The model proposes; your code disposes.
  - After: A "tool call" makes it sound as if the model reaches out and presses buttons. It doesn't. The model *writes down* which tool it wants and with what arguments, usually as the structured output of Chapter 6 [@yao2023; @schick2023]. Your code checks that request, runs the tool if it's allowed, and gives back the result. Look at what the request really is: a choice from a fixed list of tools, plus some values. It's a typed decision that looks like text. The model suggests; your code decides.
- `chapters/ch07.qmd`
  - Before: The book's SOC agent is deliberately small. For each alert it reads the alert, **decides** which evidence to gather next (threat intel, host history, policies or none), **decides** whether it has enough, **decides** the verdict, and then acts: closing the alert, or writing a case note for an analyst, or writing a page for on-call. Decisions go to the mock Jev as typed questions; writing goes to the mock LLM.
  - After: The book's SOC agent is small on purpose. For each alert, it reads the alert and **decides** which evidence to collect next (threat intel, host history, policies or none). It **decides** whether it has enough, **decides** the verdict, and then acts. It closes the alert, or writes a case note for an analyst, or writes an urgent message to the analyst on call. Decisions go to the mock Jev as typed questions; writing goes to the mock LLM.
- `chapters/ch07.qmd`
  - Before: You could object that I built the agent, so I chose that mix. Fair. Run the same count on any agent you build or buy. I'd be surprised if you found a very different shape: pick a tool, check a result, decide whether to continue, route the case. Writing is the occasional output. Deciding is the everyday work.
  - After: You could say that I built the agent, so I chose that mix. That's fair. Run the same count on any agent you build or buy. I'd be surprised if you found a very different pattern: pick a tool, check a result, decide whether to continue, send the case somewhere. Writing happens now and then. Deciding is the everyday work.
- `chapters/ch07.qmd`
  - Before: ## Errors compound
  - After: ## Errors add up
- `chapters/ch07.qmd`
  - Before: Loops come with some uncomfortable arithmetic. If each step is right 95% of the time, and a task needs ten steps to go right, the whole task succeeds with probability 0.95 multiplied by itself ten times: about {{< num ch13 compound_95_10 pct >}}.
  - After: Loops come with some uncomfortable arithmetic. Suppose each step is right 95% of the time, and a task needs ten steps to go right. Then the whole task succeeds with probability 0.95 multiplied by itself ten times: about {{< num ch13 compound_95_10 pct >}}.
- `chapters/ch07.qmd`
  - Before: That's why agents that shine in a demo stumble in production (@fig-compound). A demo is a few steps on a friendly example. Production is twenty steps on a strange one: at 95% per step, a twenty-step task succeeds about {{< num ch13 compound_95_20 pct >}} of the time. And the direction points at the decisions. They're most of the steps, so they're most of the risk. A decision that comes with a trustworthy probability can be caught before it compounds, by routing it to review or gathering more evidence. A decision that comes back as a confident sentence can't.
  - After: That's why agents that look great in a demo fail in real use (@fig-compound). A demo is a few steps on an easy example. Real use is twenty steps on an unusual one. At 95% per step, a twenty-step task succeeds about {{< num ch13 compound_95_20 pct >}} of the time. And this points at the decisions. They're most of the steps, so they're most of the risk. A decision that comes with a calibrated probability can be caught early, by sending it to review or collecting more evidence. A decision that comes back as a confident sentence can't.
- `chapters/ch07.qmd`
  - Before: Now the most dangerous failure. In a RAG system or an agent, the model reads text that someone else wrote: emails, tickets, web pages, alert descriptions. If an attacker can get text in front of the model, they can write instructions or claims into it. It's called **prompt injection**, and it's usually described as an LLM problem [@greshake2023]. The problem is broader than that. Any model that reads attacker-controlled text can be steered by it, decision models included.
  - After: Now the most dangerous failure. In a RAG system or an agent, the model reads text that someone else wrote: emails, tickets, web pages, alert descriptions. If an attacker can get text in front of the model, they can write instructions or false claims into it. This is called **prompt injection**, and it's usually described as an LLM problem [@greshake2023]. The problem is wider than that. Any model that reads text an attacker controls can be steered by it, decision models included.
- `chapters/ch07.qmd`
  - Before: Take a concrete case. Kestrel's alert text sometimes includes "Matches approved IT tooling (change ticket on file)", one of the strongest signs an alert is harmless. Suppose an attacker adds that one sentence to the alert text, through a command line, an email subject or a file name.
  - After: Take a real example. Kestrel's alert text sometimes includes "Matches approved IT tooling (change ticket on file)". It's one of the strongest signs that an alert is harmless. Suppose an attacker adds that one sentence to the alert text, through a command line, an email subject or a file name.
- `chapters/ch07.qmd`
  - Before: The sentence drags many real threats below the auto-close line.
  - After: The sentence pulls many real threats below the auto-close threshold.
- `chapters/ch07.qmd`
  - Before: One sentence. The share of real threats that would close themselves without a human rose from {{< num ch14 inj_act_before pct >}} to {{< num ch14 inj_act_after pct >}} (@fig-injection). The exact numbers are the mock's, but the lesson isn't. The fix is structural: ask the change-management system whether a ticket exists, and pass the answer as a separate field the attacker can't write. With that, only {{< num ch14 inj_act_trusted pct >}} of threats would auto-close.
  - After: One sentence. The share of real threats that would close without a person seeing them rose from {{< num ch14 inj_act_before pct >}} to {{< num ch14 inj_act_after pct >}} (@fig-injection). The exact numbers are the mock's, but the lesson is general. The fix is in the design. Ask the system that records approved changes whether a ticket exists. Pass the answer as a separate field that the attacker can't write. With that, only {{< num ch14 inj_act_trusted pct >}} of threats would auto-close.
- `chapters/ch07.qmd`
  - Before: Other failures are quieter. Retrieval returns a weak match and nobody checks: {{< num ch14 weak_retrieval pct >}} of the agent's policy lookups fell below the "I don't know" line. Loops run on without a budget. And the worst failures come at the end, where the agent acts: isolating the CEO's laptop mid-meeting, or closing a real incident. When anything goes wrong, from a timeout to a parse failure, the agent should fail towards a person reviewing it, never towards acting.
  - After: Other failures are harder to notice. Retrieval returns a weak match and nobody checks: {{< num ch14 weak_retrieval pct >}} of the agent's policy lookups fell below the "I don't know" threshold. Loops keep running with no limit. And the worst failures come at the end, where the agent acts: cutting the CEO's laptop off the network during a meeting, or closing a real incident. When anything goes wrong, from a timeout to a parse failure, the agent should send the case to a person, never act on it.
- `chapters/ch07.qmd`
  - Before: Look back over this chapter and a pattern appears. Nearly every catch is the same kind of thing: a check, turned into a decision, with a threshold chosen from what mistakes cost.
  - After: Look back over this chapter and a pattern appears. Nearly every protection is the same kind of thing: a check, turned into a decision, with a threshold chosen from what mistakes cost.
- `chapters/ch07.qmd`
  - Before: The agent proposes. The decision layer disposes (@fig-defences). It checks the proposal against what's allowed, asks typed questions and gets calibrated probabilities, applies lines drawn from costs, enforces budgets, and takes risky facts from trusted systems. Then each case leaves through one of three doors: act, review or escalate.
  - After: The agent suggests; the decision layer decides (@fig-defences). It checks the suggestion against what's allowed. It asks typed questions and gets calibrated probabilities. It applies thresholds set from costs, enforces limits, and takes risky facts from trusted systems. Then each case leaves through one of three doors: act, review or escalate.
- `chapters/ch07.qmd`
  - Before: None of that needs a more intelligent model. It needs decisions fast enough to put everywhere, cheap enough to ask often, and honest enough to put a threshold on. A model like Jev is designed for that gap.
  - After: None of that needs a more intelligent model. It needs decisions that are fast enough to use everywhere, cheap enough to ask often, and calibrated enough to put a threshold on. A model like Jev is designed for that need.
- `chapters/ch07.qmd`
  - Before: Retrieved text is untrusted input: separate instructions from data, and never let retrieved text trigger actions directly. A decision layer isn't a shield against everything, either. If the attacker controls a "trusted" system, the trusted field lies too; if every check shares one blind spot, the layers fail together; and thresholds set once and never revisited drift out of date. Red-team your own layer: try to get a real threat through the act door, and see which check catches you.
  - After: Retrieved text is untrusted input. Keep instructions separate from data, and never let retrieved text start actions directly. A decision layer doesn't protect against everything, either. If the attacker controls a "trusted" system, the trusted field lies too. If every check has the same weakness, the layers all fail together. And thresholds set once and never checked again go out of date. Attack your own layer: try to get a real threat through the act door, and see which check stops you.
- `chapters/ch07.qmd`
  - Before: Kestrel's agent can take four actions without a human: close an alert, add a note, block a sender domain and isolate a laptop. Which should be allowed automatically when the model is confident, and which should always need a person?
  - After: Kestrel's agent can take four actions without a person: close an alert, add a note, block a sender domain, and cut a laptop off the network. Which should be allowed automatically when the model is confident, and which should always need a person?
- `chapters/ch07.qmd`
  - Before: (Closing and noting are cheap and reversible, so they're fine automatically with a calibrated line. Blocking a domain is reversible but can cost business, so give it a stricter line and a list of partners it may never block. Isolating a laptop disrupts someone's work and may destroy evidence, so it needs a person.)
  - After: (Closing and adding notes are cheap and can be undone, so they're fine automatically with a threshold on a calibrated probability. Blocking a domain can be undone but can cost business, so give it a stricter threshold and a list of partners it may never block. Cutting off a laptop stops someone's work and may destroy evidence, so it needs a person.)
- `chapters/ch07.qmd`
  - Before: The model didn't know Kestrel, so we handed it the right pages, and retrieval became the step everything depended on. Then we let the model act. An agent turned out to be a model in a loop, whose tool calls are really decisions your code carries out, and when we counted its steps, most were decisions. Errors compounded over the loop, one planted sentence steered a verdict, and nearly every catch was a decision with a threshold.
  - After: The model didn't know Kestrel, so we gave it the right pages, and retrieval became the step everything depended on. Then we let the model act. An agent turned out to be a model in a loop. Its tool calls are really decisions that your code carries out. When we counted its steps, most were decisions. Errors added up over the loop, and one planted sentence changed a verdict. Nearly every protection was a decision with a threshold.

## Chapter 8: System 1 and System 2

30 changes.

- `chapters/ch08.qmd`
  - Before: It's both, and the idea deserves unpacking properly before we open Jev up in the next chapter. The name comes from one of the best-known ideas in modern psychology, and that idea describes the software we've been building in this book surprisingly well. Most of the work is fast judgement. A little of it is slow thought. And the art is sending each case to the right one.
  - After: It's both. The idea deserves a proper explanation before we look inside Jev in the next chapter. The name comes from one of the best-known ideas in modern psychology. That idea describes the software in this book surprisingly well. Most of the work is fast judgement. A little of it is slow thought. And the skill is sending each case to the right one.
- `chapters/ch08.qmd`
  - Before: - Map them onto software: which tools behave like each.
  - After: - Match them to software: which tools behave like each.
- `chapters/ch08.qmd`
  - Before: - Route cases between a fast system and a slow one by doubt, and measure what that buys.
  - After: - Send cases to a fast system or a slow one depending on doubt, and measure what that gains.
- `chapters/ch08.qmd`
  - Before: - Say when fast judgement can be trusted, and why honest doubt is the key condition.
  - After: - Say when fast judgement can be trusted, and why calibrated doubt is the key condition.
- `chapters/ch08.qmd`
  - Before: That one felt different. You had to stop, hold numbers in your head, do steps in order. You could feel the effort. Your pupils probably widened.
  - After: That one felt different. You had to stop, keep numbers in your head, and do steps in order. You could feel the effort. The dark centres of your eyes probably got a little bigger.
- `chapters/ch08.qmd`
  - Before: The psychologist Daniel Kahneman used these very examples to introduce two modes of thinking, which he called **System 1** and **System 2** [@kahneman2011]. System 1 is fast, automatic and effortless: recognising a face, reading a word, sensing that a sentence is hostile, knowing that 2 + 2 is 4. System 2 is slow, deliberate and effortful: long multiplication, filling in a tax form, checking an argument.
  - After: The psychologist Daniel Kahneman used these same examples to describe two ways of thinking. He called them **System 1** and **System 2** [@kahneman2011]. System 1 is fast, automatic and effortless: recognising a face, reading a word, sensing that a sentence is unfriendly, knowing that 2 + 2 is 4. System 2 is slow, careful and effortful: long multiplication, filling in a tax form, checking an argument.
- `chapters/ch08.qmd`
  - Before: Neither is better. System 1 runs almost everything you do, and it's usually right. But it can be confidently wrong. Try a famous test of it [@frederick2005]:
  - After: Neither is better. System 1 runs almost everything you do, and it's usually right. But it can be confidently wrong. Try this famous test [@frederick2005]:
- `chapters/ch08.qmd`
  - Before: The answer that jumps out is 10 cents. It's wrong: the ball costs 5 cents. System 1 offered a quick, plausible answer, and unless System 2 stepped in to check, that's the answer you'd have given.
  - After: The answer that comes to mind first is 10 cents. It's wrong: the ball costs 5 cents. System 1 offered a quick answer that sounded right. Unless System 2 stepped in to check, that's the answer you'd have given.
- `chapters/ch08.qmd`
  - Before: Rules and classifiers are System 1–like: fast, automatic, good at familiar patterns, useless outside them. Logistic regression doesn't deliberate. It adds up the evidence and answers in microseconds.
  - After: Rules and classifiers are like System 1: fast, automatic, good at familiar patterns, and useless outside them. Logistic regression doesn't think things over. It adds up the evidence and answers in millionths of a second.
- `chapters/ch08.qmd`
  - Before: Large language models, especially the newer ones that write out their reasoning before answering, are the closest software has come to System 2: slow, effortful, general, able to tackle problems they've never seen. Chapter 6 showed what that costs. Every step of reasoning is tokens in the loop, and tokens are time and money.
  - After: Large language models are the closest software has come to System 2, especially the newer ones that write out their reasoning before answering. They're slow, effortful and general, and they can work on problems they've never seen. Chapter 6 showed what that costs. Every step of reasoning is tokens in the loop, and tokens cost time and money.
- `chapters/ch08.qmd`
  - Before: For the last few years, the industry's instinct has been to use that System 2 machinery for *everything*, including judgements that System 1 handles fine. Chapter 7 counted what that looks like inside an agent: mostly small, familiar decisions, each made by a slow, general reasoner.
  - After: For the last few years, the industry has tended to use that System 2 machinery for *everything*, including judgements that System 1 handles well. Chapter 7 counted what that looks like inside an agent: mostly small, familiar decisions, each made by a slow, general reasoner.
- `chapters/ch08.qmd`
  - Before: ![Tasks in and around a SOC, placed by how often they happen and how much thinking each needs (illustrative). The high-volume ones cluster at the bottom right: quick judgements made hundreds or thousands of times a day. The few that need real reasoning happen rarely.]
  - After: ![Tasks in and around a SOC, placed by how often they happen and how much thinking each needs (illustrative). The frequent ones are grouped at the bottom right: quick judgements made hundreds or thousands of times a day. The few that need real reasoning happen rarely.]
- `chapters/ch08.qmd`
  - Before: @fig-task-map is illustrative, but the shape is familiar to anyone who has worked in operations. A handful of tasks need real thought: reconstructing an attack, writing the incident report, explaining a breach to the board. The overwhelming volume is quick judgement: is this alert real, which queue, which tool next, is this chunk relevant, is this the same incident as that one.
  - After: @fig-task-map is illustrative, but anyone who has worked in operations knows the pattern. A few tasks need real thought: working out how an attack happened, writing the incident report, explaining a break-in to the company's leaders. Almost all the rest is quick judgement. Is this alert real? Which queue? Which tool next? Is this chunk relevant? Is this the same incident as that one?
- `chapters/ch08.qmd`
  - Before: That mismatch is the gap TypeSafe named Jev's model class after. A **System One model**, in their sense, is one built for the high-volume corner of @fig-task-map. It answers typed questions fast and returns probabilities, and it doesn't reason in text at all. Whether Jev fills that gap well is the subject of the rest of Part III, measured with the tools of Part I.
  - After: TypeSafe named Jev's type of model after that mismatch. A **System One model**, as they use the term, is built for the busy corner of @fig-task-map. It answers typed questions fast, returns probabilities, and doesn't reason in text at all. Whether Jev does this well is the subject of the rest of Part III, measured with the tools of Part I.
- `chapters/ch08.qmd`
  - Before: A good analyst already knows the answer. They triage most alerts in seconds, and they *notice* the ones that don't feel right. Those get the slow treatment. The skill isn't only fast judgement. It's fast judgement *plus an honest sense of when it's not enough*.
  - After: A good analyst already knows the answer. They sort most alerts in seconds, and they *notice* the ones that don't feel right. Those get the slow, careful treatment. The skill isn't only fast judgement. It's fast judgement *plus a true sense of when it's not enough*.
- `chapters/ch08.qmd`
  - Before: Let's measure what that design buys at Kestrel. System 1 is the mock decision model reading each alert's raw text, recalibrated on the history weeks. System 2 is a careful investigation, which in our synthetic world I can model perfectly: it learns each alert's *true* probability. That's the best any investigation could do, so it's the upper limit of what System 2 can add.
  - After: Let's measure what that design gains at Kestrel. System 1 is the mock decision model reading each alert's raw text, recalibrated on the history weeks. System 2 is a careful investigation. In our synthetic world I can model it perfectly: it learns each alert's *true* probability. That's the best any investigation could do, so it's the most that System 2 could add.
- `chapters/ch08.qmd`
  - Before: We decide whether each live alert is a threat using the cost line from Chapter 4, with a missed threat at \$10,000 and a false alarm at \$400. Then we send a share of alerts to System 2, either the ones System 1 is least sure about, or a random selection.
  - After: We decide whether each live alert is a threat using the cost-based threshold from Chapter 4, with a missed threat at \$10,000 and a false alarm at \$400. Then we send a share of alerts to System 2: either the ones System 1 is least sure about, or a random selection.
- `chapters/ch08.qmd`
  - Before: The result in @fig-routing-curve is the argument for a dual-process design, in one chart. Sending the 20% of alerts System 1 is least sure about captures {{< num ch15 share_gain_20 pct >}} of everything System 2 could possibly add. Sending a random 20% captures {{< num ch15 share_gain_20_random pct >}}.
  - After: @fig-routing-curve makes the case for a design with two systems, in one chart. Sending the 20% of alerts System 1 is least sure about gets {{< num ch15 share_gain_20 pct >}} of everything System 2 could possibly add. Sending a random 20% gets {{< num ch15 share_gain_20_random pct >}}.
- `chapters/ch08.qmd`
  - Before: And the cost of System 2 is paid only on that 20%. If a careful pass takes 25 seconds and a fast decision 0.15 (illustrative numbers again), then routing by doubt averages about {{< num ch15 time_20 f1 >}} seconds per alert, against 25 for sending everything to the slow system.
  - After: And you pay for System 2 only on that 20%. Say a careful pass takes 25 seconds and a fast decision takes 0.15 seconds (illustrative numbers again). Then routing by doubt takes about {{< num ch15 time_20 f1 >}} seconds per alert on average, against 25 for sending everything to the slow system.
- `chapters/ch08.qmd`
  - Before: A fast system earns its keep twice: by its speed, and by knowing which cases it shouldn't decide.
  - After: A fast system is valuable in two ways: its speed, and knowing which cases it shouldn't decide.
- `chapters/ch08.qmd`
  - Before: That's why calibration keeps coming back in this book. Routing by doubt only works if System 1's doubt is *honest*: if its 0.5 really means "this could go either way" and its 0.02 really means "almost certainly fine". An overconfident System 1 sends the wrong cases to System 2, and keeps the dangerous ones for itself.
  - After: That's why calibration keeps coming back in this book. Routing by doubt only works if System 1 is *calibrated*: its 0.5 must really mean "this could go either way", and its 0.02 must really mean "almost certainly fine". An overconfident System 1 sends the wrong cases to System 2, and keeps the dangerous ones for itself.
- `chapters/ch08.qmd`
  - Before: Psychologists spent years arguing about intuition. Some, like Gary Klein, studied experts such as firefighters and nurses, whose split-second judgements were very good. Others, like Kahneman, catalogued the ways snap judgements go wrong. In 2009 the two of them wrote a joint paper setting out when intuition can be trusted, and found they mostly agreed [@kahneman2009].
  - After: Psychologists argued about intuition for years. Some, like Gary Klein, studied experts such as firefighters and nurses, whose very fast judgements were very good. Others, like Kahneman, listed the ways quick judgements go wrong. In 2009 the two of them wrote a paper together about when intuition can be trusted. They found they mostly agreed [@kahneman2009].
- `chapters/ch08.qmd`
  - Before: Their answer, roughly: trust fast judgement in a **regular** environment, where the same cues keep meaning the same things, after **plenty of practice** with **quick, clear feedback** (@fig-conditions). Don't trust it in chaotic environments, or where feedback is slow and rare, however confident the expert feels.
  - After: Their answer, roughly: trust fast judgement in a **regular** environment, where the same signs keep meaning the same things. It also needs **plenty of practice** with **quick, clear feedback** (@fig-conditions). Don't trust it where things are unpredictable, or where feedback is slow and rare, however confident the expert feels.
- `chapters/ch08.qmd`
  - Before: I've added a fourth condition that I think matters just as much for machines: an honest sense of doubt. A good expert knows when a case is outside their experience. A good System One model should too, and for a model "knowing" means one thing: calibrated probabilities that drop towards uncertainty when the case is unfamiliar.
  - After: I've added a fourth condition that I think matters just as much for machines: a true sense of doubt. A good expert knows when a case is outside their experience. A good System One model should too. For a model, "knowing" means one thing: calibrated probabilities that move towards uncertainty when the case is unfamiliar.
- `chapters/ch08.qmd`
  - Before: SOC triage fits the first three conditions better than most jobs. Alerts come from a fixed set of detectors; there are thousands of examples; analysts find out, eventually, which alerts were real. Novel attack investigations fit badly. So do one-off strategic decisions. It makes a useful rule of thumb for where System One models belong, and where they don't.
  - After: SOC triage fits the first three conditions better than most jobs. Alerts come from a fixed set of detectors, there are thousands of examples, and analysts find out in the end which alerts were real. Investigating new kinds of attack fits badly. So do one-time business decisions. This gives a useful guide to where System One models belong, and where they don't.
- `chapters/ch08.qmd`
  - Before: The two-systems idea is a metaphor, and Kahneman himself was clear that the "systems" are shorthand, not two machines in the brain. Mapping it onto software is looser still: a System One model isn't intuitive in any human sense; it's a trained function. And routing by doubt has a weakness: if System 1 is confidently wrong about a whole class of cases, say a new attack technique it has never seen, it won't route them to System 2, because it doesn't feel unsure. Random audits (Chapter 14) and drift checks are there to catch what doubt misses.
  - After: The two-systems idea is a comparison, not a fact about the brain. Kahneman himself said the "systems" are a short way of speaking, not two machines in the head. Applying it to software is even less exact: a System One model isn't intuitive in any human sense; it's a trained function. And routing by doubt has a weakness. System 1 may be confidently wrong about a whole type of case, such as a new attack method it has never seen. Then it won't send those cases to System 2, because it doesn't feel unsure. Random audits (Chapter 14) and checks for drift are there to catch what doubt misses.
- `chapters/ch08.qmd`
  - Before: Kestrel's System 2 is expensive: a senior analyst's time. The team can afford to send 10% of alerts, not 20%. Using @fig-routing-curve, roughly how much of the benefit do they keep? And if they could make System 1 better calibrated, would the curve move up, down, or change shape?
  - After: Kestrel's System 2 is expensive: it's a senior analyst's time. The team can afford to send 10% of alerts, not 20%. Using @fig-routing-curve, about how much of the benefit do they keep? And if they could make System 1 better calibrated, would the curve move up, move down, or change shape?
- `chapters/ch08.qmd`
  - Before: (They'd keep somewhat over half. Better calibration makes the green curve drop *faster*, because the cases System 1 marks as uncertain would really be the uncertain ones, so each escalation buys more.)
  - After: (They'd keep a little over half. Better calibration makes the green curve drop *faster*. The cases System 1 marks as uncertain would really be the uncertain ones, so each case sent to System 2 gains more.)
- `chapters/ch08.qmd`
  - Before: We started with 2 + 2 and 17 × 24, and found two modes of thinking in each of us. Software, we saw, has mostly used its slow, general mode for every job, even though most jobs are quick judgements. So we put a fast system in front of a slow one and sent across only the cases it doubted, and a fifth of the traffic bought most of the benefit. That only worked because the fast system's doubt was sound, the very condition under which psychologists say intuition can be trusted.
  - After: We started with 2 + 2 and 17 × 24, and found two ways of thinking in each of us. Software, we saw, has mostly used its slow, general way for every job, even though most jobs are quick judgements. So we put a fast system in front of a slow one, and sent across only the cases it doubted. A fifth of the cases got most of the benefit. That only worked because the fast system was calibrated. That's the same condition under which psychologists say intuition can be trusted.
- `chapters/ch08.qmd`
  - Before: 2. In the lab, route the alerts randomly instead of by doubt, and plot both curves. At what share does random routing catch up?
  - After: 2. In the lab, route the alerts randomly instead of by doubt, and plot both curves. At what share does random routing do as well?

## Chapter 10: The type system

35 changes.

- `chapters/ch10.qmd`
  - Before: Jev asks you to put every question into one of three shapes. Yes or no. Pick one. Rate it on a scale.
  - After: Jev asks you to put every question into one of three shapes: yes or no, pick one, or rate it on a scale.
- `chapters/ch10.qmd`
  - Before: That's the first thing people push back on:
  - After: That's the first thing people object to:
- `chapters/ch10.qmd`
  - Before: They are. But look back at Chapter 7's agent, or at your own working day, and notice how many of those messy decisions break down into a handful of these three shapes. Is this a real attack? Which team should handle it? How urgent is it? The mess usually lives in how the question is *asked*, not in the shape of the answer.
  - After: They are. But look back at Chapter 7's agent, or at your own working day. Notice how many of those messy decisions break down into a few questions of these three shapes. Is this a real attack? Which team should handle it? How urgent is it? The mess is usually in how the question is *asked*, not in the shape of the answer.
- `chapters/ch10.qmd`
  - Before: This chapter takes each type in turn, with the design choices that make it work and the traps that make it fail. The traps are the more useful part.
  - After: This chapter takes each type in turn. It covers the design choices that make each one work, and the traps that make it fail. The traps are the more useful part.
- `chapters/ch10.qmd`
  - Before: - Read a score's whole distribution, and act on its tails rather than its average.
  - After: - Read all of a score's probabilities, and act on the levels you care about rather than on its average.
- `chapters/ch10.qmd`
  - Before: If they look familiar, they should. Each is something you've already built.
  - After: If they look familiar, that's because you've already built each of them.
- `chapters/ch10.qmd`
  - Before: ![Each type is an old friend. A noul is the S-curve from Chapter 2, turning evidence into one probability.
  - After: ![You've met each type before. A noul is the S-curve from Chapter 2, turning evidence into one probability.
- `chapters/ch10.qmd`
  - Before: The odd name is TypeSafe's, for a yes-or-no question. You give it instructions, a question or a statement, and optionally a description of what counts as yes and what counts as no. You get back one number: the probability of yes.
  - After: "Noul" is TypeSafe's unusual name for a yes-or-no question. You give it instructions: a question or a statement. You can also describe what counts as yes and what counts as no. You get back one number: the probability of yes.
- `chapters/ch10.qmd`
  - Before: A `noul` is the most useful type and the easiest to ask badly. Three habits help.
  - After: A `noul` is the most useful type, and the easiest to ask badly. Three habits help.
- `chapters/ch10.qmd`
  - Before: **One fact per question.** "Is this a real attack on a critical server?" bundles two facts, and the answer can't tell you which one failed. Ask two nouls and combine them in your code, where the logic is visible.
  - After: **One fact per question.** "Is this a real attack on a critical server?" joins two facts, and a "no" can't tell you which one was false. Ask two nouls and combine them in your code, where the logic is visible.
- `chapters/ch10.qmd`
  - Before: **Spell out yes and no.** "Is this malicious?" leaves the edges vague. Is an employee breaking policy malicious? Is a penetration test? Say what counts. The API lets you describe both outcomes:
  - After: **Say exactly what yes and no mean.** "Is this malicious?" leaves the unclear cases open. Is an employee breaking a company rule malicious? Is a test attack that the company paid for? Say what counts. The API lets you describe both outcomes:
- `chapters/ch10.qmd`
  - Before: **No double negatives.** "Is this not unlikely to be benign?" is hard for people and models alike. Ask the question the right way up.
  - After: **No double negatives.** "Is this not unlikely to be benign?" is hard for people and models. Ask the question in the simple, positive way.
- `chapters/ch10.qmd`
  - Before: ![Category probabilities for four alerts. Some are sharply decided; others spread their probability over two or three labels. The spread is information: it tells you how sure the model is, and between what.]
  - After: ![Category probabilities for four alerts. Some are clearly decided; others spread their probability over two or three labels. The spread is useful: it tells you how sure the model is, and which labels it's choosing between.]
- `chapters/ch10.qmd`
  - Before: That "add up to 1" is the property to respect, because it cuts both ways. The model *must* distribute all of its belief across the labels you gave it. If the right answer isn't among them, the probability doesn't vanish. It lands on the wrong labels.
  - After: That "add up to 1" is important, and it has a downside. The model *must* spread all of its belief across the labels you gave it. If the right answer isn't among them, the probability doesn't disappear. It lands on the wrong labels.
- `chapters/ch10.qmd`
  - Before: It looks like this. I asked the mock to classify {{< num ch17 n_harmless int >}} harmless alerts twice: once with the full list of categories, including "benign", and once with only the threat categories.
  - After: Here's what that looks like. I asked the mock to label {{< num ch17 n_harmless int >}} harmless alerts twice. The first time it had the full list of categories, including "benign". The second time it had only the threat categories.
- `chapters/ch10.qmd`
  - Before: With "benign" available, {{< num ch17 full_benign_share pct >}} of the harmless alerts were labelled benign. Without it, every one of them got a threat label, with a median confidence of {{< num ch17 forced_conf_median f2 >}} (@fig-forced). The model wasn't wrong, exactly. You asked it which *threat* each alert was, and it answered. But anyone reading "malware, 0.95" would draw the wrong conclusion.
  - After: With "benign" available, {{< num ch17 full_benign_share pct >}} of the harmless alerts were labelled benign. Without it, every one of them got a threat label, with a median confidence of {{< num ch17 forced_conf_median f2 >}} (@fig-forced). The model wasn't exactly wrong. You asked it which *threat* each alert was, and it answered. But anyone reading "malware, 0.95" would reach the wrong conclusion.
- `chapters/ch10.qmd`
  - Before: So include "benign", "none", "other" or "not enough information" whenever those can happen. Make the options mutually exclusive, too: if two labels can both be true at once ("phishing" and "credential theft"), a choice will split its probability between them and neither will look confident. When things really can overlap, use several nouls instead of one choice.
  - After: So include "benign", "none", "other" or "not enough information" whenever those can happen. Also make sure only one option can be true at a time. Suppose two labels can both be true at once, like "phishing" and "credential theft". Then a choice will split its probability between them, and neither will look confident. When things really can overlap, use several nouls instead of one choice.
- `chapters/ch10.qmd`
  - Before: ## Score: levels in order, and the tails
  - After: ## Score: levels in order
- `chapters/ch10.qmd`
  - Before: A `score` gives the model an ordered list of levels, and returns a probability for each, plus the **expected score**: the probability-weighted average level.
  - After: A `score` gives the model a list of levels in order. It returns a probability for each level, plus the **expected score**: the average level, weighted by the probabilities.
- `chapters/ch10.qmd`
  - Before: That average is convenient, and it can mislead you badly.
  - After: That average is convenient, but it can badly mislead you.
- `chapters/ch10.qmd`
  - Before: Look at the first panel of @fig-severity. The alert's average severity is {{< num ch17 sev_example.expected f2 >}}, which reads as "low: review within a week". But there's hardly any probability *at* low. The model is really saying: *this is either nothing, or it's serious.* There's a {{< num ch17 sev_example.p_high pct >}} chance it's medium or high. An average of two very different possibilities describes neither of them.
  - After: Look at the first panel of @fig-severity. The alert's average severity is {{< num ch17 sev_example.expected f2 >}}, which reads as "low: review within a week". But there's hardly any probability *at* low. The model is really saying: *this is either nothing, or it's serious.* There's a {{< num ch17 sev_example.p_high pct >}} chance it's medium or high. The average of two very different possibilities describes neither of them.
- `chapters/ch10.qmd`
  - Before: That happens whenever the model is unsure about *whether* something is real. A harmless alert would be informational, and a real one would be serious, so the distribution splits into two humps. So act on the tail:
  - After: That happens whenever the model is unsure *whether* something is real. A harmless alert would be informational, and a real one would be serious. So the probabilities form two peaks, one at each end. Act on the probability of the levels you care about, here the high end:
- `chapters/ch10.qmd`
  - Before: "Page someone if P(medium or high) is above 0.3" is a rule you can reason about and set with costs. "Page someone if the average is above 1.5" isn't.
  - After: "Call someone if P(medium or high) is above 0.3" is a rule you can reason about and set with costs. "Call someone if the average is above 1.5" isn't.
- `chapters/ch10.qmd`
  - Before: Averages hide tails. Put thresholds on the probability of the levels you care about.
  - After: Averages hide the extremes. Put thresholds on the probability of the levels you care about.
- `chapters/ch10.qmd`
  - Before: In @fig-expected-cost, "benign" is the top label at 0.40, but 0.60 of the probability says *some kind of threat*. Closing the alert risks all of those. The cheapest action is to route it to the identity team, the most likely *threat*. That's the Chapter 4 formula generalised: for each action, add up what it costs under each possible truth, weighted by that truth's probability, and take the cheapest.
  - After: In @fig-expected-cost, "benign" is the top label at 0.40, but 0.60 of the probability says *some kind of threat*. Closing the alert risks all of those. The cheapest action is to send it to the identity team, which handles the most likely *threat*. That's the Chapter 4 formula made more general. For each action, add up what it costs under each possible truth, weighted by that truth's probability. Then take the cheapest action.
- `chapters/ch10.qmd`
  - Before: It's also why you want probabilities for every option, not just the winning label. A text answer that says "benign" throws away the very information you need here.
  - After: It's also why you want probabilities for every option, not just the top label. A text answer that says "benign" throws away exactly the information you need here.
- `chapters/ch10.qmd`
  - Before: Real decisions usually need a few answers about the same situation. You can ask them together. The state is sent once, and each question gets its own typed answer. The SDK even lets you declare the response as your own class, so your code works with typed fields instead of dictionaries:
  - After: Real decisions usually need a few answers about the same situation. You can ask the questions together. The state is sent once, and each question gets its own typed answer. The SDK even lets you describe the response as your own class. Then your code works with typed fields instead of dictionaries:
- `chapters/ch10.qmd`
  - Before: Three types can't express everything. Numbers on a continuous range ("how many megabytes?"), free-text fields ("which username?") and structured extraction still need something else, often an LLM, as Chapter 15's "extract, then decide" pattern shows. The answers of separate questions in one call aren't guaranteed to be consistent with each other: a low P(attack) alongside a high P(severity high) is possible, and your combining code should expect it. And question wording matters: a clearer description can move the probabilities, so test wording changes like any other change.
  - After: Three types can't express everything. Some answers still need something else, often an LLM: a number on a continuous range ("how many megabytes?"), free text ("which username?"), or several fields pulled out of a document. Chapter 15's "extract, then decide" pattern shows how. The answers to separate questions in one call may not agree with each other. A low P(attack) next to a high P(severity high) is possible, and the code that combines them should expect it. And wording matters: a clearer description can change the probabilities, so test wording changes like any other change.
- `chapters/ch10.qmd`
  - Before: Kestrel pages on-call when P(severity medium or high) is at least some line. A false page costs \$400; a missed serious incident costs about \$10,000 more than handling it in the morning. Using the Chapter 4 formula, where does the line go? Would you use the same line for alerts on critical assets?
  - After: Kestrel calls the analyst on call when P(severity medium or high) is at least some threshold. A false call costs \$400. A missed serious incident costs about \$10,000 more than handling it in the morning. Using the Chapter 4 formula, where does the threshold go? Would you use the same threshold for alerts on critical assets?
- `chapters/ch10.qmd`
  - Before: (400 ÷ 10,400 ≈ 0.04, so page at about 4%. Low, and it would page a lot, which is why Chapter 14 will cap pages by what on-call can absorb. For critical assets a miss costs more, so the line should be even lower.)
  - After: (400 ÷ 10,400 ≈ 0.04, so call at about 4%. That's low, and it would mean many calls. That's why Chapter 14 limits calls to what the on-call analyst can handle. For critical assets a miss costs more, so the threshold should be even lower.)
- `chapters/ch10.qmd`
  - Before: Brooks meant data structures in software. The same holds for decisions: get the *shape* of the question and its answers right, and most of the logic around it becomes obvious.
  - After: Brooks meant data structures in software. The same is true for decisions: get the *shape* of the question and its answers right, and most of the logic around it becomes obvious.
- `chapters/ch10.qmd`
  - Before: Three shapes, we found, cover most small decisions, as long as the questions are asked carefully. A noul wants one fact and a clear idea of what yes means. A choice spreads all its belief over the options you give it, so every real case needs one. A score's average can describe a case that doesn't exist, so thresholds belong on the tails. And for all three, the whole distribution beats the top answer, because decisions are made with costs.
  - After: Three shapes, we found, cover most small decisions, as long as the questions are asked carefully. A noul needs one fact and a clear idea of what yes means. A choice spreads all its belief over the options you give it, so every real case needs an option. A score's average can describe a case that doesn't exist, so thresholds belong on the probability of the levels you care about. And for all three, the full set of probabilities is better than the top answer, because decisions are made with costs.
- `chapters/ch10.qmd`
  - Before: Everything here has assumed the probabilities are honest. Time to check.
  - After: Everything here has assumed the probabilities are calibrated. Time to check.
- `chapters/ch10.qmd`
  - Before: 1. Rewrite each bundled question as separate nouls, and say how you'd combine them: "Is this a phishing email that someone clicked on?"; "Is this login suspicious and from an admin account?"
  - After: 1. Rewrite each of these two-part questions as separate nouls, and say how you'd combine them: "Is this a phishing email that someone clicked on?"; "Is this login suspicious and from an admin account?"
- `chapters/ch10.qmd`
  - Before: 3. Find an alert in the lab whose severity distribution has two humps. What does its P(attack) look like? Why do the two go together?
  - After: 3. Find an alert in the lab whose severity probabilities have two peaks. What does its P(attack) look like? Why do the two go together?

## Chapter 12: The Jevons paradox of decisions

40 changes.

- `chapters/ch12.qmd`
  - Before: In 1865 a 29-year-old economist named William Stanley Jevons published a book about coal, and it made him famous almost overnight [@jevons1865].
  - After: In 1865, a 29-year-old economist named William Stanley Jevons published a book about coal. It made him famous almost immediately [@jevons1865].
- `chapters/ch12.qmd`
  - Before: Britain ran on coal. Its factories, mines, ships and railways all burned it, and people had started to worry about how long it would last. The comforting answer was engineering. James Watt's steam engine got far more work out of each ton than the engines before it, and engineers kept improving it. Surely, as engines got more efficient, Britain would need less coal.
  - After: Britain ran on coal. Its factories, mines, ships and railways all burned it, and people had started to worry about how long it would last. The comforting answer was engineering. James Watt's steam engine got far more work out of each ton of coal than the engines before it, and engineers kept improving it. Surely, as engines used coal better, Britain would need less of it.
- `chapters/ch12.qmd`
  - Before: Jevons said no. More efficient engines had made coal-powered work *cheaper*, and cheaper work got used for more things. Engines that had been too costly to run became worth running, in more mills and more mines. Each engine used less coal. Britain used far more.
  - After: Jevons said no. Better engines had made coal-powered work *cheaper*, and cheaper work got used for more things. Engines that had cost too much to run became worth running, in more factories and more mines. Each engine used less coal. Britain used far more.
- `chapters/ch12.qmd`
  - Before: A model whose name is short for Jevons invites the question: what's the coal, this time?
  - After: Jev's name is short for Jevons. So we should ask: what's the coal this time?
- `chapters/ch12.qmd`
  - Before: - See where the paradox really bites: in new uses, not old ones.
  - After: - See where the paradox really shows up: in new uses, not old ones.
- `chapters/ch12.qmd`
  - Before: - Spot the catch: cheap decisions move the load onto the people who review them.
  - After: - Notice the hidden cost: cheap decisions move work onto the people who review them.
- `chapters/ch12.qmd`
  - Before: Think about photographs. When a photo meant film, developing and a trip to the chemist, you took a few dozen on a holiday and chose each one with care. Then each photo cost next to nothing. Nobody takes the same few dozen photos for less money. You take thousands, of receipts and parking spots and whiteboards, because each one is now worth taking.
  - After: Think about photographs. When a photo meant buying film and paying a shop to print it, you took a few dozen on a holiday and chose each one with care. Then each photo started to cost almost nothing. Nobody takes the same few dozen photos for less money. You take thousands, of receipts and parking spots and whiteboards, because each one is now worth taking.
- `chapters/ch12.qmd`
  - Before: Or light. Over the last two centuries, the price of an hour of light fell enormously, from candles to gas to electric bulbs to LEDs. Economic historians who traced it for the UK found that people didn't pocket the savings and keep a candle's worth of light. They lit streets and buildings and kept them lit all night, and use grew far faster than the price fell [@fouquet2006].
  - After: Or light. Over the last two hundred years, the price of an hour of light fell enormously, from candles to gas to electric bulbs to LEDs. Historians who studied this for the UK found that people didn't keep the savings and use the same small amount of light. They lit streets and buildings and kept them lit all night. Use grew far faster than the price fell [@fouquet2006].
- `chapters/ch12.qmd`
  - Before: That pattern has a name. The **Jevons paradox** is what happens when something becomes more efficient to use, each unit of use gets cheaper, and total use rises instead of falling.
  - After: That pattern has a name. The **Jevons paradox** is when something becomes more efficient to use, each unit gets cheaper, and total use rises instead of falling.
- `chapters/ch12.qmd`
  - Before: The paradox isn't a law. Plenty of things got cheaper without anyone using much more of them. Salt is cheap, and you don't eat ten times as much as your great-grandparents did.
  - After: The paradox isn't a law. Many things got cheaper without anyone using much more of them. Salt is cheap, but you don't eat ten times as much as your great-grandparents did.
- `chapters/ch12.qmd`
  - Before: What decides it is how hungry people are for more, which economists measure as **elasticity**: how much the amount people use changes when the price changes. Total spend is price times quantity, so there are three cases.
  - After: What decides it is how much more people want when the price falls. Economists measure this as **elasticity**: how much the amount people use changes when the price changes. Total spending is price times quantity, so there are three cases.
- `chapters/ch12.qmd`
  - Before: If demand is **inelastic**, like salt, a price cut mostly saves money. If demand is **elastic**, like photos or light, a price cut opens up so many new uses that the total bill goes *up* (@fig-elasticity). Economists call the general effect a rebound, and they reserve "backfire" for the case where it more than cancels the saving. How often full backfire happens with energy is still argued over [@sorrell2009].
  - After: If demand is **inelastic**, like salt, a price cut mostly saves money. If demand is **elastic**, like photos or light, a price cut opens up so many new uses that the total bill goes *up* (@fig-elasticity). Economists call the general effect a "rebound". They use "backfire" only when it more than cancels the saving. Experts still disagree about how often full backfire happens with energy [@sorrell2009].
- `chapters/ch12.qmd`
  - Before: So the question for decisions isn't "is the paradox true?" It's: *how elastic is the demand for decisions?* Are there lots of decisions that aren't being made today, only because they cost too much?
  - After: So the question for decisions isn't "is the paradox true?" It's: *how elastic is the demand for decisions?* Are there many decisions that aren't being made today, only because they cost too much?
- `chapters/ch12.qmd`
  - Before: TypeSafe has said the name nods to Jevons: that cheaper intelligence leads to wider use, not less of it. It's a good choice, and a pointed one, because the same idea did the rounds in early 2025, when cheaper AI models briefly rattled investors and several technology leaders reached for Jevons to argue that cheaper AI would mean more AI, not less.
  - After: TypeSafe has said the name refers to Jevons: cheaper intelligence leads to wider use, not less. It's a good choice, and a deliberate one. The same idea was popular in early 2025. Cheaper AI models briefly worried investors, and several technology leaders used Jevons to argue that cheaper AI would mean more AI, not less.
- `chapters/ch12.qmd`
  - Before: We don't need to settle that argument for an entire industry. We can look at one company and count.
  - After: We don't need to settle that argument for a whole industry. We can look at one company and count.
- `chapters/ch12.qmd`
  - Before: Every decision has a **value**: the expected loss it avoids. Chapter 4 gave you the tools to put a number on it. Checking an alert that has a 3% chance of being a \$10,000 breach, when a good decision would stop it, is worth about \$300. A decision is worth making when its value is above its price.
  - After: Every decision has a **value**: the expected loss it avoids. Chapter 4 gave you the tools to put a number on it. Suppose an alert has a 3% chance of being a \$10,000 break-in, and a good decision would stop it. Then checking it is worth about \$300. A decision is worth making when its value is above its price.
- `chapters/ch12.qmd`
  - Before: Look at Kestrel. Its SOC makes a few thousand careful decisions a day. But the company generates millions of *possible* decisions: every inbound email, every login, every line in the logs. Each is almost certainly fine. Each is worth checking for a sliver of a cent.
  - After: Look at Kestrel. Its SOC makes a few thousand careful decisions a day. But the company produces millions of *possible* decisions: every incoming email, every login, every line in the logs. Each is almost certainly fine. Each is worth checking only if the check costs a tiny fraction of a cent.
- `chapters/ch12.qmd`
  - Before: I've built a small, deliberately simple model of this, and I want to be clear about what it is. Every number in it is an assumption, chosen to be plausible and written down in `jevkit/econ.py` where you can change it. It isn't a measurement of Kestrel or anyone else.
  - After: I've built a small, simple model of this on purpose, and I want to be clear about what it is. Every number in it is an assumption, chosen to be realistic. They're all written down in `jevkit/econ.py`, where you can change them. It isn't a measurement of Kestrel or anyone else.
- `chapters/ch12.qmd`
  - Before: Look at the long bottom rows of @fig-pools. There are about {{< num ch19 pool_raw approx >}} log events a day. A typical one is worth about two thousandths of a cent to check. At the book's illustrative LLM price of \${{< num ch19 llm_price f5 >}} a decision, only a sliver of them clear the bar. At Jev's vendor-reported price of \${{< num ch19 jev_price f6 >}}, about half of them do.
  - After: Look at the long bottom rows of @fig-pools. There are about {{< num ch19 pool_raw approx >}} log events a day. A typical one is worth about two thousandths of a cent to check. At the book's illustrative LLM price of \${{< num ch19 llm_price f5 >}} a decision, only a very small share of them are worth checking. At Jev's vendor-reported price of \${{< num ch19 jev_price f6 >}}, about half of them are.
- `chapters/ch12.qmd`
  - Before: Price isn't the only thing that stops a decision being made. Time does too.
  - After: Price isn't the only thing that stops a decision from being made. Time does too.
- `chapters/ch12.qmd`
  - Before: When someone logs in, they're sitting there waiting. You might have a few hundred milliseconds to decide whether the login looks risky before the delay becomes the problem. An email can wait a few seconds before it's delivered. An alert can wait a minute.
  - After: When someone logs in, they're sitting there waiting. You might have a few hundred milliseconds to decide whether the login looks risky before the delay itself becomes the problem. An email can wait a few seconds before it's delivered. An alert can wait a minute.
- `chapters/ch12.qmd`
  - Before: @fig-gates puts both gates on one chart. The LLM's region starts at over a second and at a price that rules out the cheap pools. Jev's region reaches much further left, and further down. Logins are the interesting case: they fall inside Jev's region only if its calls land at the fast end of the vendor's range. You'd measure that before promising anyone real-time login checks.
  - After: @fig-gates puts both gates on one chart. The LLM's region starts at over a second, and at a price too high for the cheap pools. Jev's region reaches much further left, and further down. Logins are the interesting case. They fall inside Jev's region only if its calls are at the fast end of the vendor's range. You'd measure that before promising anyone instant login checks.
- `chapters/ch12.qmd`
  - Before: With both gates applied, the illustrative LLM makes about {{< num ch19 llm_decisions approx >}} decisions a day and spends about \${{< num ch19 llm_spend int >}}. Jev, at the fast end of its range, makes about {{< num ch19 jev_decisions approx >}} and spends about \${{< num ch19 jev_spend int >}}. About {{< num ch19 decisions_ratio int >}} times as many decisions for a quarter of the bill.
  - After: With both gates applied, the illustrative LLM makes about {{< num ch19 llm_decisions approx >}} decisions a day and spends about \${{< num ch19 llm_spend int >}}. Jev, at the fast end of its range, makes about {{< num ch19 jev_decisions approx >}} and spends about \${{< num ch19 jev_spend int >}}. That's about {{< num ch19 decisions_ratio int >}} times as many decisions for a quarter of the cost.
- `chapters/ch12.qmd`
  - Before: Notice what didn't happen. The bill went *down*. Inside Kestrel's existing jobs, demand for decisions is elastic enough to multiply the count, but not elastic enough to raise the spend. The newly affordable decisions are worth so little each that they add only about \${{< num ch19 value_gain int >}} a day of avoided loss.
  - After: Notice what didn't happen. The bill went *down*. Inside Kestrel's existing jobs, demand for decisions is elastic enough to multiply the number of decisions, but not enough to raise the spending. The newly affordable decisions are each worth so little that together they avoid only about \${{< num ch19 value_gain int >}} a day of loss.
- `chapters/ch12.qmd`
  - Before: Suppose cheap decisions let Kestrel build something new: checking every file that's shared outside the company, {{< num ch19 new_job approx >}} a day, each worth about three thousandths of a cent. At LLM prices almost nobody would build that. At Jev's price, the model takes about {{< num ch19 jev_new_taken approx >}} of those checks a day, and Kestrel's decision bill jumps from \${{< num ch19 jev_spend int >}} to about \${{< num ch19 jev_new_spend int >}}.
  - After: Suppose cheap decisions let Kestrel build something new: checking every file shared outside the company. That's {{< num ch19 new_job approx >}} files a day, each check worth about three thousandths of a cent. At LLM prices, almost nobody would build that. At Jev's price, the model makes about {{< num ch19 jev_new_taken approx >}} of those checks a day. Kestrel's decision bill jumps from \${{< num ch19 jev_spend int >}} to about \${{< num ch19 jev_new_spend int >}}.
- `chapters/ch12.qmd`
  - Before: Add two or three more jobs like that and Kestrel spends more on decisions than it ever did with an LLM, while making dozens of times as many. That's Jevons' coal, in miniature, and it's what TypeSafe's Doom demo from Chapter 9 was really showing: an agent making ten decisions a second is a use that simply didn't exist when each decision took a second and cost a tenth of a cent.
  - After: Add two or three more jobs like that, and Kestrel spends more on decisions than it ever did with an LLM, while making dozens of times as many. That's Jevons' coal again, on a small scale. It's also what TypeSafe's Doom demo from Chapter 9 was really showing. An agent making ten decisions a second is a use that didn't exist when each decision took a second and cost a tenth of a cent.
- `chapters/ch12.qmd`
  - Before: ## The catch: where the load goes
  - After: ## The hidden cost: where the work goes
- `chapters/ch12.qmd`
  - Before: There's a second, less comfortable consequence, and it's the one I'd want you to remember on a Monday morning.
  - After: There's a second, less comfortable result, and it's the one I'd most want you to remember at work.
- `chapters/ch12.qmd`
  - Before: ![Alerts sent to a person per day, under two rules (illustrative). A rule that flags a fixed share of what the model looks at scales with the number of decisions, and swamps the team's capacity at Jev volumes. A cost line, which flags only when the expected loss is larger than the cost of a review, barely moves.]
  - After: ![Alerts sent to a person per day, under two rules (illustrative). A rule that flags a fixed share of what the model looks at grows with the number of decisions, and at Jev volumes it sends far more than the team can handle. A cost-based threshold, which flags only when the expected loss is larger than the cost of a review, barely moves.]
- `chapters/ch12.qmd`
  - Before: Only some of those decisions can end with a person, though. Agent steps and checks on LLM outputs never go to a queue, so of the LLM's roughly {{< num ch19 llm_decisions approx >}} decisions a day, about {{< num ch19 reviewable_llm approx >}} are the reviewable kind; at Jev's volume it's about {{< num ch19 reviewable_jev approx >}}. Those are the counts @fig-flags labels.
  - After: Only some of those decisions can end with a person, though. Agent steps and checks on LLM outputs never go to a queue. So of the LLM's roughly {{< num ch19 llm_decisions approx >}} decisions a day, about {{< num ch19 reviewable_llm approx >}} are the kind a person could review. At Jev's volume it's about {{< num ch19 reviewable_jev approx >}}. Those are the counts shown in @fig-flags.
- `chapters/ch12.qmd`
  - Before: Now suppose you carried over a rule that seemed sensible at LLM volumes: send the top 0.1% of the reviewable decisions to a person. That sends {{< num ch19 flags_top_llm int >}} a day, comfortably under the team's capacity of {{< num ch19 capacity int >}}. At Jev volumes, the same rule sends {{< num ch19 flags_top_jev int >}} (@fig-flags). Nobody changed the policy. The queue just grew eightfold.
  - After: Now suppose you kept a rule that seemed sensible at LLM volumes: send the top 0.1% of the reviewable decisions to a person. That sends {{< num ch19 flags_top_llm int >}} a day, well under the team's capacity of {{< num ch19 capacity int >}}. At Jev volumes, the same rule sends {{< num ch19 flags_top_jev int >}} (@fig-flags). Nobody changed the policy. The queue just grew eight times bigger.
- `chapters/ch12.qmd`
  - Before: The cost line from Chapter 4 doesn't have this problem. It flags a case when its expected loss is bigger than the \$15 a review costs, and a log line worth two thousandths of a cent is never going to clear that. It sends {{< num ch19 flags_cost_jev int >}} a day either way.
  - After: The cost-based threshold from Chapter 4 doesn't have this problem. It flags a case only when its expected loss is bigger than the \$15 a review costs. A log line worth two thousandths of a cent will never reach that. It sends {{< num ch19 flags_cost_jev int >}} a day either way.
- `chapters/ch12.qmd`
  - Before: When decisions get cheap, thresholds must be set by cost, not by share. Otherwise the saving on machines turns into a bill for people.
  - After: When decisions get cheap, thresholds must be set by cost, not by share. Otherwise the money saved on machines is spent on people's time.
- `chapters/ch12.qmd`
  - Before: Calibration matters more, not less, as decisions multiply. A cost line only works if the probabilities can be trusted. An overconfident model making a million decisions a day doesn't make a few extra mistakes. It fills the queue.
  - After: Calibration matters more, not less, as decisions multiply. A cost-based threshold only works if the probabilities are calibrated. An overconfident model making a million decisions a day doesn't make a few extra mistakes. It fills the queue.
- `chapters/ch12.qmd`
  - Before: Everything in this chapter's Kestrel model is an assumption: the pools, their sizes, the value of each decision, the time budgets. Change them and the numbers move a lot, which is why the lab lets you. Jev's price and latency are vendor-reported, and early-access prices can change. The "value of a decision" is itself an estimate that depends on calibrated probabilities, which Chapter 11 showed you can't assume. And historical analogies are suggestive, not proof: whether demand for decisions turns out more like light or more like salt is something only the next few years will show.
  - After: Everything in this chapter's Kestrel model is an assumption: the pools, their sizes, the value of each decision, the time limits. Change them and the numbers move a lot, which is why the lab lets you. Jev's price and latency are vendor-reported, and early-access prices can change. The "value of a decision" is itself an estimate that depends on calibrated probabilities, which Chapter 11 showed you can't assume. And comparisons with history are hints, not proof. Only the next few years will show whether demand for decisions is more like light or more like salt.
- `chapters/ch12.qmd`
  - Before: Kestrel wants to check every login in real time. There are 150,000 a day; a typical check is worth about \$0.0005; the budget is 300 milliseconds. At Jev's vendor-reported price, is the check worth making? What would you need to measure before switching it on? And what should the rule be for sending a login to a person?
  - After: Kestrel wants to check every login as it happens. There are 150,000 a day. A typical check is worth about \$0.0005, and the time limit is 300 milliseconds. At Jev's vendor-reported price, is the check worth making? What would you need to measure before switching it on? And what should the rule be for sending a login to a person?
- `chapters/ch12.qmd`
  - Before: (At \$0.000021 a check, yes: a typical login is worth about twenty times the price of checking it. The open question is time, so measure Jev's latency from your own network at your own volumes, including the slow tail. Send a login to a person only when its expected loss exceeds the cost of a review, never as a fixed share.)
  - After: (At \$0.000021 a check, yes: a typical login is worth about twenty times the price of checking it. The open question is time. Measure Jev's latency from your own network at your own volumes, including the slowest calls. Send a login to a person only when its expected loss is more than the cost of a review, never as a fixed share.)
- `chapters/ch12.qmd`
  - Before: Jevons noticed that better engines made coal-powered work cheaper, and cheaper work spread until Britain burned more coal than ever. Decisions, we found, work the same way, with a twist. Inside the jobs a company already does, cheaper decisions multiply the count and shrink the bill. The paradox arrives through new jobs, ones that were never worth doing at a tenth of a cent. And every extra decision can turn into work for a person, unless the lines are drawn by cost.
  - After: Jevons noticed that better engines made coal-powered work cheaper, and cheaper work spread until Britain burned more coal than ever. Decisions, we found, work the same way, with one difference. Inside the jobs a company already does, cheaper decisions multiply the number of decisions and shrink the bill. The paradox comes through new jobs: ones that were never worth doing at a tenth of a cent. And every extra decision can turn into work for a person, unless the thresholds are set by cost.
- `chapters/ch12.qmd`
  - Before: Part III has been about Jev on its own: what it is, what it answers, whether its probabilities can be trusted and what it might do to demand. Part IV puts it in context, against every other way of making the same decision.
  - After: Part III has been about Jev on its own: what it is, what it answers, whether its probabilities are calibrated, and what it might do to demand. Part IV compares it with every other way of making the same decision.
- `chapters/ch12.qmd`
  - Before: 4. The "top 0.1%" rule sounded sensible. Write down a rule from your own work that is set as a share, not a cost. What would happen to it if volume went up tenfold?
  - After: 4. The "top 0.1%" rule sounded sensible. Write down a rule from your own work that is set as a share, not a cost. What would happen to it if the volume grew ten times?

## Chapter 13: The bake-off

43 changes.

- `chapters/ch13.qmd`
  - Before: Every SOC has the same argument, and it never quite ends.
  - After: Every SOC has the same argument, and it never really ends.
- `chapters/ch13.qmd`
  - Before: The senior analyst says the rules are fine; they're written by people who know the attacks, and you can read every one. The data scientist says a trained model would beat the rules, if only someone would label enough alerts. The new engineer has wired an LLM into the ticketing system and says it reads alerts better than either of them. And now someone has read about Jev.
  - After: The senior analyst says the rules are fine. People who know the attacks wrote them, and you can read every one. The data scientist says a trained model would beat the rules, if only someone would label enough alerts. The new engineer has connected an LLM to the ticket system and says it reads alerts better than either of them. And now someone has read about Jev.
- `chapters/ch13.qmd`
  - Before: Each of them is right about something. The argument never ends because they're scoring on different things: one on explainability, one on accuracy, one on flexibility, and one on price. Nobody puts all the numbers on one sheet.
  - After: Each of them is right about something. The argument never ends because they're judging different things. One cares about explaining decisions, one about accuracy, one about flexibility, and one about price. Nobody puts all the numbers on one page.
- `chapters/ch13.qmd`
  - Before: So let's do that. Six methods, one dataset, one fair contest, and a scorecard with every column that matters. I'll tell you now that Jev doesn't win every round.
  - After: So let's do that: six methods, one dataset, one fair contest, and a scorecard with every column that matters. We'll call it a "bake-off", the name for a contest where everyone makes the same thing. I'll tell you now that Jev doesn't win every round.
- `chapters/ch13.qmd`
  - Before: - Tell which results come from how the synthetic contestants were built, and which would carry over to your own test.
  - After: - Tell which results come from how the synthetic contestants were built, and which would also appear in your own test.
- `chapters/ch13.qmd`
  - Before: The decision is Kestrel's: is this alert a real threat? Every method gets the three history weeks, {{< num ch20 n_hist int >}} alerts with analysts' verdicts, to train or tune on. Every method is then scored on the fourth week, {{< num ch20 n_live int >}} alerts it has never seen, of which {{< num ch20 live_threats int >}} are real.
  - After: The decision is Kestrel's: is this alert a real threat? Every method gets the three history weeks to train or tune on: {{< num ch20 n_hist int >}} alerts with analysts' verdicts. Then every method is scored on the fourth week, the "live week": {{< num ch20 n_live int >}} alerts it has never seen, of which {{< num ch20 live_threats int >}} are real.
- `chapters/ch13.qmd`
  - Before: Each reads what it would naturally read in practice (@fig-contenders).
  - After: Each one reads what it would normally read in practice (@fig-contenders).
- `chapters/ch13.qmd`
  - Before: The **text classifier** needs a word of explanation. It stands in for a fine-tuned model: a classic word-counting classifier (word weights plus logistic regression) trained on the history labels, which re-trains in seconds on any laptop. A fine-tuned transformer, even a small one of the MiniLM kind, would usually read the text better, so treat this row as a floor for what a trained text model can do.
  - After: The **text classifier** needs a short explanation. It stands in for a fine-tuned model. It's a classic classifier that counts words (word weights plus logistic regression), trained on the history labels. It re-trains in seconds on any laptop. A fine-tuned transformer, even a small one, would usually read the text better. So treat this row as the lowest result a trained text model should get.
- `chapters/ch13.qmd`
  - Before: One warning before any results, and it's the most important paragraph in this chapter. Both LLM contestants are the book's mock, and I built it as a *noisier reader* than mock Jev (the repository's `docs/mock-design.md` explains how). So when the LLM ranks alerts worse than Jev below, that's a consequence of how the mocks were made. It isn't evidence about real LLMs or real Jev. What *does* carry over is the shape of the other results: how stated confidences behave, how often free-text JSON breaks, what happens when you ask twice, what labels cost. Those come from how each kind of method works, not from my choice of noise.
  - After: One warning before any results, and it's the most important paragraph in this chapter. Both LLM contestants are the book's mock, and I built it to read alerts *less accurately* than mock Jev (the repository's `docs/mock-design.md` explains how). So when the LLM ranks alerts worse than Jev below, that's because of how the mocks were made. It isn't evidence about real LLMs or real Jev. What you *can* rely on is the pattern of the other results. That means how stated confidences behave, how often free-text JSON breaks, what happens when you ask twice, and what labels cost. Those come from how each kind of method works, not from choices I made in the mocks.
- `chapters/ch13.qmd`
  - Before: Logistic regression wins round one, narrowly: an AUC of {{< num ch20 logistic_auc f3 >}} against Jev's {{< num ch20 jev_auc f3 >}} (@fig-scores). With Kestrel's review capacity of 240 alerts a day, it catches {{< num ch20 logistic_caught pct >}} of real threats; Jev catches {{< num ch20 jev_caught pct >}}.
  - After: Logistic regression wins round one, by a small margin: an AUC of {{< num ch20 logistic_auc f3 >}} against Jev's {{< num ch20 jev_auc f3 >}} (@fig-scores). With Kestrel's review capacity of 240 alerts a day, it catches {{< num ch20 logistic_caught pct >}} of real threats; Jev catches {{< num ch20 jev_caught pct >}}.
- `chapters/ch13.qmd`
  - Before: That isn't a fluke. The logistic regression was trained on fifteen thousand of Kestrel's own labelled alerts, on clean structured fields, for a decision that's nearly linear in those fields. Classic machine learning is at home here. A general model reading the same fields with no training on Kestrel at all shouldn't be expected to beat it there, and it doesn't.
  - After: That isn't luck. The logistic regression was trained on fifteen thousand of Kestrel's own labelled alerts, on clean structured fields. And the decision depends on those fields in a nearly straight-line way. This is exactly the kind of problem classic machine learning is good at. A general model reading the same fields, with no training on Kestrel at all, shouldn't be expected to beat it here, and it doesn't.
- `chapters/ch13.qmd`
  - Before: The rules come last on ranking, with an AUC of {{< num ch20 rules_auc f2 >}}, for a structural reason: a rule says yes or no. Among the hundreds of alerts it says yes to, it has no way to say which to look at first.
  - After: The rules come last on ranking, with an AUC of {{< num ch20 rules_auc f2 >}}. The reason is simple: a rule only says yes or no. Among the hundreds of alerts it says yes to, it has no way to say which to look at first.
- `chapters/ch13.qmd`
  - Before: Give Jev the raw text instead of the fields, and its AUC drops to {{< num ch20 jev_text_auc f3 >}}. Still well ahead of the trained text classifier's {{< num ch20 text_clf_auc f3 >}}, because reading "threat intel score: 0.82" as a number is what a word-counting classifier is worst at.
  - After: Give Jev the raw text instead of the fields, and its AUC drops to {{< num ch20 jev_text_auc f3 >}}. That's still well ahead of the trained text classifier's {{< num ch20 text_clf_auc f3 >}}. A classifier that counts words is worst at reading "threat intel score: 0.82" as a number.
- `chapters/ch13.qmd`
  - Before: ## Round two: honesty
  - After: ## Round two: calibration
- `chapters/ch13.qmd`
  - Before: Ranking is only half the job. Chapter 14 will draw lines at probabilities, and lines only work if the probabilities mean what they say.
  - After: Ranking is only half the job. Chapter 14 will put thresholds on probabilities, and thresholds only work if the probabilities mean what they say.
- `chapters/ch13.qmd`
  - Before: The LLM's stated confidences cluster on a few values; the judge's ratings, read as probabilities, are far too high in the middle.]
  - After: The LLM's stated confidences are grouped on a few values; the judge's ratings, read as probabilities, are far too high in the middle.]
- `chapters/ch13.qmd`
  - Before: Most of the contestants are close to the line (@fig-reliability). The logistic regression was fitted with log loss on this company's data, the recipe Chapter 2 said produces honest probabilities. Mock Jev was designed to be well calibrated at Kestrel, and Chapter 11 showed that's worth checking at your own company, not assuming.
  - After: Most of the contestants are close to the diagonal (@fig-reliability). The logistic regression was fitted with log loss on this company's data. Chapter 2 said that method produces calibrated probabilities. Mock Jev was designed to be well calibrated at Kestrel. Chapter 11 showed that you should check this at your own company, not assume it.
- `chapters/ch13.qmd`
  - Before: The LLM's stated confidence came from the JSON it wrote: `"confidence": 0.95`. Across five thousand alerts, it used only {{< num ch20 conf_levels int >}} distinct values, mostly 0.9, 0.95 and 0.99. Chapter 6 predicted as much. A number that a model *writes* is text, and text tends to be round. It can't rank finely, which is why the LLM's AUC is the lowest of the probability methods.
  - After: The LLM's stated confidence came from the JSON it wrote: `"confidence": 0.95`. Across five thousand alerts, it used only {{< num ch20 conf_levels int >}} different values, mostly 0.9, 0.95 and 0.99. Chapter 6 predicted this. A number that a model *writes* is text, and text tends to use round numbers. So it can't rank alerts finely. That's why the LLM's AUC is the lowest of the methods that give probabilities.
- `chapters/ch13.qmd`
  - Before: The judge's 1-to-10 rating was never meant to be a probability, and reading it as one gives the worst calibration in the contest: {{< num ch20 llm_judge_ece f3 >}}. You could fix that with Platt scaling on a few hundred labels, as Chapter 3 showed. But then you're no longer comparing a zero-label method.
  - After: In the LLM-as-judge method, the LLM rates each alert from 1 to 10. That rating was never meant to be a probability. Reading it as one gives the worst calibration in the contest: {{< num ch20 llm_judge_ece f3 >}}. You could fix that with Platt scaling on a few hundred labels, as Chapter 3 showed. But then it's no longer a method that needs zero labels.
- `chapters/ch13.qmd`
  - Before: "Logistic regression wins" comes with a price tag: fifteen thousand labels. What if you have fewer?
  - After: "Logistic regression wins" comes at a cost: fifteen thousand labels. What if you have fewer?
- `chapters/ch13.qmd`
  - Before: Jev and the LLMs need no labels to start, so they're flat lines. Logistic regression draws level with Jev at about 3,000 labels.]
  - After: Jev and the LLMs need no labels to start, so they're flat lines. Logistic regression catches up with Jev at about 3,000 labels.]
- `chapters/ch13.qmd`
  - Before: @fig-labels is the chart I'd show the data scientist in that argument. Logistic regression needs about 3,000 labelled alerts to draw level with Jev, and at a few hundred it's clearly behind.
  - After: @fig-labels is the chart I'd show the data scientist in that argument. Logistic regression needs about 3,000 labelled alerts to catch up with Jev. With a few hundred, it's clearly behind.
- `chapters/ch13.qmd`
  - Before: Where would 3,000 labels come from? Not from analysts' reviews alone: at 240 a day, that's nearly two weeks of verdicts. Kestrel's labels are *eventual outcomes*: the incident that was confirmed or ruled out, the user who said "that was me", the alert nobody followed up and nothing came of. Every alert gets one sooner or later, so at about 700 alerts a day, 3,000 labels is around four days of history, which Kestrel happens to have. A team that's just starting, or a new decision nobody has labelled yet, doesn't.
  - After: Where would 3,000 labels come from? Not from analysts' reviews alone: at 240 a day, that's nearly two weeks of verdicts. Kestrel's labels are *what finally happened*: the incident that was confirmed or ruled out, the user who said "that was me", the alert nobody followed up that turned out to be nothing. Every alert gets a label sooner or later. So at about 700 alerts a day, 3,000 labels is about four days of history, and Kestrel has that. A team that's just starting doesn't, and neither does a new decision nobody has labelled yet.
- `chapters/ch13.qmd`
  - Before: The text classifier never catches up, even with every label we have. Words alone, counted, don't carry the numbers.
  - After: The text classifier never catches up, even with every label we have. Counting words doesn't capture the numbers in the text.
- `chapters/ch13.qmd`
  - Before: Labels are the hidden cost of trained models. A method that needs none can start today; a method that needs thousands has to wait for them, and needs them again when things change.
  - After: Labels are the hidden cost of trained models. A method that needs none can start today. A method that needs thousands has to wait for them, and needs them again when things change.
- `chapters/ch13.qmd`
  - Before: ![Time and cost per decision for each method, on log scales. Classic models run in microseconds for fractions of a cent per million (an assumption: compute only).
  - After: ![Time and cost per decision for each method, on log scales. Classic models run in millionths of a second, for fractions of a cent per million decisions (an assumption: computing cost only).
- `chapters/ch13.qmd`
  - Before: Nothing beats a rule on speed or price, and the classic models are close behind (@fig-cost-latency). They run in microseconds, on hardware you already own. Jev's vendor-reported figures put it in between: about \${{< num ch20 jev_cost_m int >}} per million decisions, in tens to hundreds of milliseconds. The illustrative LLM costs about \${{< num ch20 llm_json_cost_m int >}} per million and takes about {{< num ch20 llm_json_latency f1 >}} seconds. A little more than Chapter 9's figures, because the bake-off's JSON answer carries four fields (verdict, confidence, rule and threat-intel score), about 60 output tokens rather than 40.
  - After: Nothing beats a rule on speed or price, and the classic models are close behind (@fig-cost-latency). They run in millionths of a second, on computers you already own. Jev's vendor-reported figures put it in between: about \${{< num ch20 jev_cost_m int >}} per million decisions, in tens to hundreds of milliseconds. The illustrative LLM costs about \${{< num ch20 llm_json_cost_m int >}} per million and takes about {{< num ch20 llm_json_latency f1 >}} seconds. That's a little more than Chapter 9's figures. The bake-off's JSON answer has four fields (verdict, confidence, rule and threat-intel score), so it's about 60 output tokens rather than 40.
- `chapters/ch13.qmd`
  - Before: If a decision can be made well by a rule or a logistic regression, one of those is the cheapest, fastest option, by orders of magnitude. Jev's price advantage is against *LLMs*, not against everything.
  - After: If a rule or a logistic regression can make a decision well, use one of them. It's the cheapest and fastest option by a factor of a thousand or more. Jev's price advantage is against *LLMs*, not against everything.
- `chapters/ch13.qmd`
  - Before: Ask the LLM the same question five times at a temperature of 0.7, and {{< num ch20 flip_rate pct1 >}} of verdicts change at least once (@fig-variance-13). At temperature 0 the mock is repeatable, and real APIs mostly are too, though not always perfectly. And {{< num ch20 parse_fail pct1 >}} of its JSON answers were broken badly enough to fail parsing. We fell back to the base rate for those, but in a real system each one is an exception to handle.
  - After: Ask the LLM the same question five times at a temperature of 0.7, and {{< num ch20 flip_rate pct1 >}} of verdicts change at least once (@fig-variance-13). At temperature 0, the mock always gives the same answer. Real APIs mostly do too, though not always. And {{< num ch20 parse_fail pct1 >}} of its JSON answers were so broken that they couldn't be parsed. We used the base rate for those, but in a real system each one is an error your code has to handle.
- `chapters/ch13.qmd`
  - Before: Jev's typed answers can't fail to parse: the probabilities arrive as numbers in a fixed shape. The mock always gives the same answer to the same question. Whether real Jev does is something to check.
  - After: Jev's typed answers can't fail to parse: the probabilities arrive as numbers in a fixed shape. The mock always gives the same answer to the same question. You should check whether real Jev does.
- `chapters/ch13.qmd`
  - Before: Now put everything on one sheet.
  - After: Now put everything on one page.
- `chapters/ch13.qmd`
  - Before: ![The whole contest on one sheet. Bold marks the best in each numeric column.
  - After: ![The whole contest on one page. Bold marks the best in each numeric column.
- `chapters/ch13.qmd`
  - Before: If you have thousands of labels, clean fields and a decision that doesn't change much, logistic regression is hard to beat: it ranks best, it's calibrated, it's nearly free, and you can read its weights. Jev loses there, and plainly.
  - After: If you have thousands of labels, clean fields and a decision that doesn't change much, logistic regression is hard to beat. It ranks best, it's calibrated, it's nearly free, and you can read its weights. Jev clearly loses there.
- `chapters/ch13.qmd`
  - Before: If you need to explain every decision to an auditor, rules win the last column outright, and nothing else comes close.
  - After: If you need to explain every decision to an auditor, rules clearly win the last column, and nothing else comes close.
- `chapters/ch13.qmd`
  - Before: If you have no labels, raw text, or many different decisions to make, Jev's row is the strongest. It starts with zero labels, ranks nearly as well as the trained model, gives probabilities you can draw lines on after a check, answers in a shape that can't break, and costs a small fraction of an LLM call.
  - After: If you have no labels, raw text, or many different decisions to make, Jev's row is the strongest. It starts with zero labels and ranks nearly as well as the trained model. After a calibration check, you can put thresholds on its probabilities. Its answers come in a shape that can't break, and it costs a small fraction of an LLM call.
- `chapters/ch13.qmd`
  - Before: And the LLM? In this contest it's the weakest decider, partly by construction. But notice what it's good at that no other row even attempts: it reads anything, and it *writes*. That's why Chapter 15's first pattern gives it the job of extracting and explaining, and gives the decision to something else.
  - After: And the LLM? In this contest it's the weakest at deciding, partly because of how the mock was built. But notice what it does that no other row even tries: it reads anything, and it *writes*. That's why Chapter 15's first pattern gives it the job of extracting and explaining, and gives the decision to something else.
- `chapters/ch13.qmd`
  - Before: This is one decision, on one synthetic company, with mocks standing in for the LLM and for Jev. The LLM-versus-Jev accuracy gap was built into the mocks and tells you nothing about the real models. The text classifier is a weak stand-in for a fine-tuned model. And a single live week has only about four hundred real threats, so differences in the second decimal place of AUC are within noise. The value of a bake-off is the *method*: run the same contest on your own data, with the real models, and fill in your own scorecard.
  - After: This is one decision, at one synthetic company, with mocks standing in for the LLM and for Jev. The accuracy gap between the LLM and Jev was built into the mocks. It says nothing about the real models. The text classifier is a weak stand-in for a fine-tuned model. And a single live week has only about four hundred real threats, so differences in the second decimal place of AUC could be chance. The value of a bake-off is the *method*. Run the same contest on your own data, with the real models, and fill in your own scorecard.
- `chapters/ch13.qmd`
  - Before: A new team at Kestrel is taking over cloud-storage alerts, a decision nobody has labelled. They'll get about 300 labels a week from their own reviews. Which method would you start with, and when would you consider switching? What would you use the first 300 labels for?
  - After: A new team at Kestrel is taking over cloud-storage alerts, a decision nobody has labelled. They'll get about 300 labels a week from their own reviews. Which method would you start with, and when would you think about switching? What would you use the first 300 labels for?
- `chapters/ch13.qmd`
  - Before: (Start with a zero-label method, Jev in this contest, and use the first 300 labels to check and fix its calibration, as in Chapter 11. After three or four weeks of labels, train a logistic regression alongside it and compare on the next week. If the two agree closely, keep the cheaper one. If they disagree, look at the alerts where they do.)
  - After: (Start with a method that needs no labels, Jev in this contest. Use the first 300 labels to check and fix its calibration, as in Chapter 11. After three or four weeks of labels, train a logistic regression next to it and compare them on the next week. If the two agree closely, keep the cheaper one. If they disagree, look at the alerts where they disagree.)
- `chapters/ch13.qmd`
  - Before: Wolpert and Macready proved that about search and optimisation [@wolpert1997], but it's the right spirit for any bake-off. There is no best method, only a best method for a decision.
  - After: Wolpert and Macready proved this about search and optimisation [@wolpert1997], but the idea fits any bake-off. There is no best method, only a best method for a particular decision.
- `chapters/ch13.qmd`
  - Before: Six methods sat the same exam. The trained logistic regression won on ranking and calibration, because it had fifteen thousand labels on clean fields. It needed about three thousand of them just to draw level with a method that needed none. The rules won on explanation and price. The LLM's stated confidences turned out to be round numbers, and its free-text JSON broke often enough to matter. Jev's row was the strongest wherever labels were scarce or the input was raw text. None of that tells you what real models will do on your data. It tells you which columns to measure when you try.
  - After: Six methods took the same test. The trained logistic regression won on ranking and calibration, because it had fifteen thousand labels on clean fields. It needed about three thousand of them just to catch up with a method that needed none. The rules won on explanation and price. The LLM's stated confidences turned out to be round numbers, and its free-text JSON broke often enough to matter. Jev's row was the strongest wherever labels were few or the input was raw text. None of that tells you what real models will do on your data. It tells you which columns to measure when you try.
- `chapters/ch13.qmd`
  - Before: 3. Rerun the labels curve with the text classifier using bigrams only. Does it help? Why might a fine-tuned transformer do better?
  - After: 3. Run the labels curve again with the text classifier using bigrams (pairs of words) only. Does it help? Why might a fine-tuned transformer do better?
- `chapters/ch13.qmd`
  - Before: Next: a probability isn't an action. Chapter 14 turns these numbers into three doors, act, review and escalate, and puts the lines where the costs say they belong.
  - After: Next: a probability isn't an action. Chapter 14 turns these numbers into three doors, act, review and escalate, and puts the thresholds where the costs say they belong.

## Chapter 14: Act, review, or escalate

74 changes.

- `chapters/ch14.qmd`
  - Before: You've spent a good part of this book earning that number. You know it's a probability, you know how to check it against reality, and you know how it compares with what an LLM or a logistic regression would have said.
  - After: You've spent a good part of this book learning about that number. You know it's a probability, you know how to check it against reality, and you know how it compares with what an LLM or a logistic regression would have said.
- `chapters/ch14.qmd`
  - Before: And now someone in the SOC is standing behind you asking the only question that matters at 2:14 a.m.:
  - After: And now someone in the SOC is standing behind you, asking the only question that matters at 2:14 a.m.:
- `chapters/ch14.qmd`
  - Before: This chapter is about that moment: the step from a number to an action. It's the least glamorous part of any AI system, and it's where most of the money is won or lost.
  - After: This chapter is about that moment: the step from a number to an action. It's the least exciting part of any AI system, and it's where most of the money is saved or lost.
- `chapters/ch14.qmd`
  - Before: - Explain why a single cut-off at 0.5 is almost always the wrong policy.
  - After: - Explain why a single threshold at 0.5 is almost always the wrong policy.
- `chapters/ch14.qmd`
  - Before: - Derive the zone boundaries from what mistakes cost, then adjust them for how many people you actually have.
  - After: - Work out the zone thresholds from what mistakes cost, then adjust them for how many people you actually have.
- `chapters/ch14.qmd`
  - Before: - Run the policy in production: decision logs, fail-safes, audits, and drift.
  - After: - Run the policy in real use: decision logs, fail-safes, audits, and drift.
- `chapters/ch14.qmd`
  - Before: Let's try it on a real week. We'll use the first three weeks of Kestrel's alerts as history and treat the fourth week as "live", the way you would if you were switching this on for real.
  - After: Let's try it on a realistic week. We'll use the first three weeks of Kestrel's alerts as history. We'll treat the fourth week as "live", the way you would if you were switching this on for real.
- `chapters/ch14.qmd`
  - Before: About {{< num ch21 naive.act int >}} alerts a day close themselves, which sounds wonderful until you read the next line. Every day, roughly {{< num ch21 naive.missed_by_automation int >}} of them were real threats: genuine phishing, genuine malware, a genuine stranger with someone's password. The machine closed them on its own and nobody ever looked.
  - After: About {{< num ch21 naive.act int >}} alerts a day close themselves. That sounds wonderful until you read the next line. Every day, about {{< num ch21 naive.missed_by_automation int >}} of them were real threats: real phishing, real malware, a real stranger with someone's password. The machine closed them on its own, and nobody ever looked.
- `chapters/ch14.qmd`
  - Before: Because 0.5 silently assumes two things that aren't true here. It assumes a missed threat and a false alarm cost the same, which you already know from Chapter 4 is absurd for a SOC. And it assumes there are only two things you can do with an alert.
  - After: Because 0.5 quietly assumes two things that aren't true here. It assumes a missed threat and a false alarm cost the same. You know from Chapter 4 that this is far from true for a SOC. And it assumes there are only two things you can do with an alert.
- `chapters/ch14.qmd`
  - Before: The first door is the one nobody sees. The alert is closed, or handled by an automated playbook, and no human ever reads it. Most alerts should leave this way, because most alerts are noise.
  - After: The first door is the one nobody sees. The alert is closed, or handled by an automatic procedure, and no person ever reads it. Most alerts should leave this way, because most alerts are harmless.
- `chapters/ch14.qmd`
  - Before: The second door leads to the queue. An analyst picks the alert up, pulls the logs, maybe messages the user, and makes the call. It costs about twelve minutes of a skilled person's time.
  - After: The second door leads to the queue. An analyst picks up the alert, reads the logs, maybe messages the user, and decides. It costs about twelve minutes of a skilled person's time.
- `chapters/ch14.qmd`
  - Before: The third door is the loud one. Someone's phone rings. An on-call responder drops what they're doing, at 2:14 a.m. if necessary, because this one can't wait.
  - After: The third door is the loud one. Someone's phone rings. The analyst on call stops what they're doing, at 2:14 a.m. if necessary, because this one can't wait.
- `chapters/ch14.qmd`
  - Before: Act, review, escalate. Machines take the easy ends; people take the middle.
  - After: Act, review, escalate. Machines handle the clear cases at each end; people handle the middle.
- `chapters/ch14.qmd`
  - Before: In this book, **act** means the system handles the case by itself, **review** means a person checks it in the normal course of work, and **escalate** means a person is pulled in right now. The names are general on purpose. In customer support, act might be an automatic reply, review a human agent, escalate a supervisor. In content moderation, it might be auto-approve, human review, and legal.
  - After: In this book, **act** means the system handles the case by itself. **Review** means a person checks it as part of normal work. **Escalate** means a person is called in right now. The names are general on purpose. In customer support, act might be an automatic reply, review a human agent, and escalate a supervisor. In checking social media posts, it might be automatic approval, human review, and the legal team.
- `chapters/ch14.qmd`
  - Before: Note the log scale: most alerts are crowded at the far left, where the model is confident they're harmless. The red dots, real threats, gather to the right, but not all of them.]
  - After: Note the log scale: most alerts are crowded at the far left, where the model is confident they're harmless. The red dots, real threats, are mostly to the right, but not all of them.]
- `chapters/ch14.qmd`
  - Before: Look at @fig-zones-strip for a moment, because the entire problem is in it. The grey dots pile up on the left: the easy harmless alerts. The red dots lean right. But there are red dots scattered through the middle and even a few in the far-left crowd, and grey dots sitting in the escalate zone. No placement of two lines makes every dot land in the right zone. Our job is to place the lines so the *mistakes we can't avoid* are the cheap ones.
  - After: Look at @fig-zones-strip for a moment, because the whole problem is in it. The grey dots are crowded on the left: the easy, harmless alerts. The red dots are mostly to the right. But some red dots are spread through the middle, and a few are even in the crowd on the far left. And some grey dots sit in the escalate zone. No two thresholds can put every dot in the right zone. Our job is to place the thresholds so that the *mistakes we can't avoid* are the cheap ones.
- `chapters/ch14.qmd`
  - Before: ## Let the costs draw the lines
  - After: ## Let the costs set the thresholds
- `chapters/ch14.qmd`
  - Before: So where do the lines go? Not where they look nice. Where the money says.
  - After: So where do the thresholds go? Not where they look nice, but where the costs say.
- `chapters/ch14.qmd`
  - Before: For every action, we can write down what it costs *on average*, given the probability *P* that the alert is real. Here are Kestrel's numbers. They're my estimates for a company this size, not industry figures, and the method matters far more than the exact values.
  - After: For every action, we can write down what it costs *on average*, given the probability *P* that the alert is real. Here are Kestrel's numbers. They're my estimates for a company this size, not industry figures. The method matters far more than the exact values.
- `chapters/ch14.qmd`
  - Before: - **Act** (auto-close). If the alert was real, we've let a threat through. Other defences catch much of what slips past, so the *expected* loss per missed threat is about \$10,000. Expected cost: *P* × \$10,000.
  - After: - **Act** (auto-close). If the alert was real, we've let a threat through. Other defences catch much of what gets past, so the *expected* loss per missed threat is about \$10,000. Expected cost: *P* × \$10,000.
- `chapters/ch14.qmd`
  - Before: - **Review.** Twelve minutes of an analyst at \$75 an hour is \$15. Analysts are human and miss about one threat in twenty. Expected cost: \$15 + *P* × 5% × \$10,000.
  - After: - **Review.** Twelve minutes of an analyst's time at \$75 an hour is \$15. Analysts are human and miss about one threat in twenty. Expected cost: \$15 + *P* × 5% × \$10,000.
- `chapters/ch14.qmd`
  - Before: - **Escalate** (page on-call). If the alert was harmless, we've woken someone up for nothing. Call it \$400. Expected cost: (1 − *P*) × \$400.
  - After: - **Escalate** (call the analyst on call). If the alert was harmless, we've woken someone up for nothing. Call that \$400. Expected cost: (1 − *P*) × \$400.
- `chapters/ch14.qmd`
  - Before: Now draw all three as lines against *P* and, at every value of *P*, pick the cheapest one.
  - After: Now draw all three as lines against *P*. At every value of *P*, pick the cheapest one.
- `chapters/ch14.qmd`
  - Before: The lines in @fig-cost-lines cross in just two places, and those two crossings are your thresholds. You can find them with a pencil. Acting beats reviewing when *P* × 10,000 < 15 + *P* × 500, which works out to *P* below about 0.0016. Escalating beats reviewing when *P* rises above about 0.43.
  - After: The lines in @fig-cost-lines cross in just two places, and those two crossings are your thresholds. You can find them with a pencil. Acting is cheaper than reviewing when *P* × 10,000 < 15 + *P* × 500. That works out to *P* below about 0.0016. Escalating is cheaper than reviewing when *P* rises above about 0.43.
- `chapters/ch14.qmd`
  - Before: That first number deserves a second look. It says: only let the machine close an alert on its own if it's more than 99.8% sure the alert is harmless. When closing a real threat unseen costs about 630 times more than a review (\$9,500 extra, once you allow for the 5% a reviewer would miss anyway, against \$15), that's what "cheap mistakes only" means.
  - After: That first number deserves a second look. It says: only let the machine close an alert on its own if it's more than 99.8% sure the alert is harmless. Closing a real threat without anyone seeing it costs about 630 times more than a review. That's \$9,500 extra, once you allow for the 5% a reviewer would miss anyway, against \$15. At those costs, "only make cheap mistakes" means exactly this.
- `chapters/ch14.qmd`
  - Before: Suppose Kestrel invests in better endpoint protection, and the expected loss from a missed threat falls from \$10,000 to \$2,000. Recompute the *act* line using the same formula: 15 ÷ (2,000 × 0.95). Does it move up or down? By roughly how much? What happens to the number of alerts the machine can close alone?
  - After: Suppose Kestrel buys better protection for its laptops and servers, and the expected loss from a missed threat falls from \$10,000 to \$2,000. Work out the *act* threshold again with the same formula: 15 ÷ (2,000 × 0.95). Does it move up or down? By about how much? What happens to the number of alerts the machine can close alone?
- `chapters/ch14.qmd`
  - Before: (It moves up, to about 0.008, five times higher, so far more alerts can safely close themselves. Cheaper misses buy you more automation.)
  - After: (It moves up, to about 0.008, five times higher, so far more alerts can safely close themselves. When misses cost less, you can automate more.)
- `chapters/ch14.qmd`
  - Before: ## Before you trust a line, check the number under it
  - After: ## Before you trust a threshold, check the probability
- `chapters/ch14.qmd`
  - Before: There's a catch hiding in @fig-cost-lines, and it's the catch this whole book has been building towards.
  - After: There's a hidden problem in @fig-cost-lines, and it's the problem this whole book has been leading to.
- `chapters/ch14.qmd`
  - Before: The cost lines are drawn as if *P* means what it says. As if, among all the alerts the model scores at 0.001, one in a thousand really is a threat. If the model is overconfident, and says 0.001 when the truth is 0.003, then your "cheapest action" isn't the cheapest at all, and the machine is closing threats you never agreed to close.
  - After: The cost lines are drawn as if *P* means what it says: as if, among all the alerts the model scores at 0.001, one in a thousand really is a threat. Suppose the model is overconfident, and says 0.001 when the truth is 0.003. Then your "cheapest action" isn't the cheapest at all. The machine is closing threats you never agreed to close.
- `chapters/ch14.qmd`
  - Before: So before we move a single line, we check. We take the history weeks, where we know how every alert turned out, and ask the question from Chapter 3: when the model says *x*, does *x* happen?
  - After: So before we set any threshold, we check. We take the history weeks, where we know how every alert turned out. And we ask the question from Chapter 3: when the model says *x*, does *x* happen?
- `chapters/ch14.qmd`
  - Before: The result is uncomfortable. Among live alerts the raw model called "under 2% likely", it claimed an average of about {{< num ch21 raw_believed pct1 >}}. The real rate was {{< num ch21 raw_actual pct1 >}}. Its "almost certainly harmless" alerts were about {{< num ch21 raw_ratio f1 >}} times riskier than it said.
  - After: The result is uncomfortable. Take the live alerts the raw model called "under 2% likely". For those, it said the chance was about {{< num ch21 raw_believed pct1 >}} on average. The real rate was {{< num ch21 raw_actual pct1 >}}. Its "almost certainly harmless" alerts were about {{< num ch21 raw_ratio f1 >}} times riskier than it said.
- `chapters/ch14.qmd`
  - Before: That's not a bug I planted for drama. The mock is built to be slightly overconfident at the extremes (the repository's `docs/mock-design.md` gives the settings), because that's how most real models behave, as Chapter 5 explained. Whether *real* Jev behaves this way on *your* data is the kind of thing you should never assume and always measure. Chapter 11 shows how.
  - After: That's not a bug I added for effect. The mock is built to be slightly overconfident at the extremes (the repository's `docs/mock-design.md` gives the settings). That's how most real models behave, as Chapter 5 explained. You should never assume whether *real* Jev behaves this way on *your* data. Always measure it. Chapter 11 shows how.
- `chapters/ch14.qmd`
  - Before: ![Zoomed in on the low end, where the ACT zone lives. Raw scores (red) sit above the diagonal: the model was more confident than reality justified. After Platt scaling fitted on other days (green), the curve hugs the diagonal much more closely.]
  - After: ![A close-up of the low end, where the act zone is. Raw scores (red) sit above the diagonal: the model was more confident than it should have been. After Platt scaling fitted on other days (green), the curve stays much closer to the diagonal.]
- `chapters/ch14.qmd`
  - Before: After Platt scaling, fitted only on the three history weeks, the picture improves (@fig-calibration-zones). Not perfect, but much closer. So here is the rule, stated properly:
  - After: After Platt scaling, fitted only on the three history weeks, the picture improves (@fig-calibration-zones). It's not perfect, but it's much closer. So here is the rule, stated properly:
- `chapters/ch14.qmd`
  - Before: From here on, every line we draw is on the *calibrated* scale.
  - After: From here on, every threshold we set is on the *calibrated* probabilities.
- `chapters/ch14.qmd`
  - Before: ## Then reality walks in: the queue
  - After: ## Then the real limit appears: the queue
- `chapters/ch14.qmd`
  - Before: We have cost-optimal thresholds and calibrated probabilities. Let's switch it on.
  - After: We have the cheapest thresholds for our costs and calibrated probabilities. Let's switch it on.
- `chapters/ch14.qmd`
  - Before: Under the pure-cost policy, the live week sends about {{< num ch21 ideal.review int >}} alerts a day to review. At twelve minutes each, that's the full working day of about {{< num ch21 ideal_reviews_analysts int >}} analysts.
  - After: Under the policy based only on costs, the live week sends about {{< num ch21 ideal.review int >}} alerts a day to review. At twelve minutes each, that's a full working day for about {{< num ch21 ideal_reviews_analysts int >}} analysts.
- `chapters/ch14.qmd`
  - Before: Kestrel has {{< num ch21 analysts int >}}. Each can clear about 40 alerts in a shift, so the queue can take {{< num ch21 capacity int >}} a day. The on-call responders can absorb about {{< num ch21 pages_cap int >}} pages a day before the pages themselves become the problem.
  - After: Kestrel has {{< num ch21 analysts int >}}. Each can clear about 40 alerts in a shift, so the queue can take {{< num ch21 capacity int >}} a day. The analysts on call can handle about {{< num ch21 pages_cap int >}} urgent calls a day before the calls themselves become the problem.
- `chapters/ch14.qmd`
  - Before: A policy that ignores capacity isn't a policy. It's a wish. Anything beyond {{< num ch21 capacity int >}} simply doesn't get looked at, in some order nobody chose.
  - After: A policy that ignores capacity isn't a policy. It's a wish. Anything beyond {{< num ch21 capacity int >}} simply doesn't get looked at, and nobody chooses which ones are skipped.
- `chapters/ch14.qmd`
  - Before: So we ask a better question: *among all the policies that fit the team we actually have, which is cheapest?* That search is quick, because for any escalation line the best review line is the one that fills the queue and no more.
  - After: So we ask a better question: *among all the policies that fit the team we actually have, which is cheapest?* That search is quick. For any escalate threshold, the best act threshold is the one that fills the queue and no more.
- `chapters/ch14.qmd`
  - Before: Fitted on history, checked on the live week. The machine now closes about {{< num ch21 chosen.act int >}} alerts a day by itself, the analysts get {{< num ch21 chosen.review int >}}, on-call gets {{< num ch21 chosen.escalate int >}} pages, and the number of real threats closed without a human falls from {{< num ch21 naive.missed_by_automation int >}} a day to about {{< num ch21 chosen.missed_by_automation f1 >}}.
  - After: We fitted the policy on history and checked it on the live week. The machine now closes about {{< num ch21 chosen.act int >}} alerts a day by itself. The analysts get {{< num ch21 chosen.review int >}}, and the analyst on call gets {{< num ch21 chosen.escalate int >}} urgent calls. The number of real threats closed without a person falls from {{< num ch21 naive.missed_by_automation int >}} a day to about {{< num ch21 chosen.missed_by_automation f1 >}}.
- `chapters/ch14.qmd`
  - Before: Look closely and the live week slightly overshoots the team: about {{< num ch21 chosen.review int >}} reviews against a capacity of {{< num ch21 capacity int >}}, and {{< num ch21 chosen.escalate int >}} pages against {{< num ch21 pages_cap int >}}. The lines were fitted to fill capacity on the history weeks, and the live week happens to be a little busier. Expect that. Lines fitted on the past are a forecast, not a guarantee, which is why Chapter 21's service watches the queue every day and flags when it runs over.
  - After: Look closely, and the live week is slightly more than the team can handle: about {{< num ch21 chosen.review int >}} reviews against a capacity of {{< num ch21 capacity int >}}, and {{< num ch21 chosen.escalate int >}} urgent calls against {{< num ch21 pages_cap int >}}. The thresholds were fitted to fill capacity on the history weeks, and the live week happens to be a little busier. Expect that. Thresholds fitted on the past are a forecast, not a promise. That's why Chapter 21's service watches the queue every day and raises a flag when it runs over.
- `chapters/ch14.qmd`
  - Before: ![Where the live week's real threats (left) and harmless alerts (right) end up each day, under one line at 0.5 and under the capacity-aware three-zone policy. The light segment on the left is the number that matters: threats closed with no human involved.]
  - After: ![Where the live week's real threats (left) and harmless alerts (right) end up each day, under one threshold at 0.5 and under the three-zone policy that respects capacity. The light segment on the left is the number that matters: threats closed with no person involved.]
- `chapters/ch14.qmd`
  - Before: @fig-one-vs-three puts the two policies side by side. Notice what didn't change much: the number of harmless alerts the machine closes. Notice what did: the "act" segment on the threat side (the lightest purple) shrank from the biggest to the smallest.
  - After: @fig-one-vs-three puts the two policies side by side. Notice what didn't change much: the number of harmless alerts the machine closes. Notice what did: the "act" segment on the threat side (the lightest purple) went from the biggest to the smallest.
- `chapters/ch14.qmd`
  - Before: But about six a day is still not zero, and here's where I want you to stop thinking like a modeller and start thinking like the person who signs the budget.
  - After: But about six a day is still not zero. Here I want you to stop thinking like someone who builds models, and start thinking like the person who approves the budget.
- `chapters/ch14.qmd`
  - Before: ![Threats auto-closed per day, for every team size from 3 to 14 analysts, with thresholds re-fitted for each. The gap between the two curves is what better input is worth: the same model reading structured alert fields instead of raw alert text.]
  - After: ![Threats auto-closed per day, for every team size from 3 to 14 analysts, with thresholds fitted again for each. The gap between the two curves is what better input is worth: the same model reading structured alert fields instead of raw alert text.]
- `chapters/ch14.qmd`
  - Before: @fig-capacity is the most useful chart in this chapter. Every point on the green curve is a fully optimised policy; the only thing that changes is how many people are on the queue. Going from six analysts to eight cuts the threats closed without review from {{< num ch21 chosen.missed_by_automation f1 >}} a day to {{< num ch21 eight.missed_by_automation f1 >}}. With Kestrel's cost estimates, two extra salaries buy back roughly {{< num ch21 saved_money_per_day money >}} of expected loss a day. The model doesn't get to make that call, and neither do you on your own. But now it's a decision with a visible price instead of a hunch.
  - After: @fig-capacity is the most useful chart in this chapter. Every point on the green curve is the best policy for that team; the only thing that changes is how many people work on the queue. Going from six analysts to eight cuts the threats closed without review from {{< num ch21 chosen.missed_by_automation f1 >}} a day to {{< num ch21 eight.missed_by_automation f1 >}}. With Kestrel's cost estimates, two extra salaries avoid about {{< num ch21 saved_money_per_day money >}} of expected loss a day. The model doesn't get to make that decision, and neither do you on your own. But now it's a decision with a clear price, not a guess.
- `chapters/ch14.qmd`
  - Before: The grey curve is worth a look too. It's the same mock, scoring the same alerts, but reading only the raw alert text instead of clean structured fields. At every team size it does worse. Better input buys you the same thing as more analysts. The same idea drives the "LLM extracts, Jev decides" pattern in the next chapter.
  - After: The grey curve is worth a look too. It's the same mock, scoring the same alerts, but reading only the raw alert text instead of clean structured fields. At every team size it does worse. Better input gives you the same benefit as more analysts. The same idea is behind the "LLM extracts, Jev decides" pattern in the next chapter.
- `chapters/ch14.qmd`
  - Before: Because accuracy counts every mistake as one mistake. With 8% of alerts being real, a policy that closes everything is 92% accurate and catastrophic. Chapter 1 made the same mistake on purpose. Costs and capacity are what turn "a good model" into "a good decision".
  - After: Because accuracy counts every mistake as one mistake. When 8% of alerts are real, a policy that closes everything is 92% accurate, and a disaster. Chapter 1 made the same mistake on purpose. Costs and capacity are what turn "a good model" into "a good decision".
- `chapters/ch14.qmd`
  - Before: So far the model has answered one yes-or-no question. Real triage asks several at once, and Jev's typed questions make that cheap: in one call you can ask whether it's real (a `Noul`), what kind of threat it is (a `Choice`), and how severe (a `Score`).
  - After: So far the model has answered one yes-or-no question. Real triage asks several at once, and Jev's typed questions make that cheap. In one call you can ask whether it's real (a `Noul`), what kind of threat it is (a `Choice`), and how severe it is (a `Score`).
- `chapters/ch14.qmd`
  - Before: A model can be 99% sure an alert on the payroll database server is harmless. The 1% still lives on the payroll database server. So the policy looks at *what's at risk* as well as *how likely*:
  - After: A model can be 99% sure that an alert on the payroll database server is harmless. But the other 1% is still on the payroll database server. So the policy looks at *what's at risk* as well as *how likely*:
- `chapters/ch14.qmd`
  - Before: Two details in `route()` are worth copying. The *act* door has an extra lock: nothing on a critical asset closes itself, however confident the model is. And the final line sends everything that doesn't clearly qualify for the other doors to a human. When in doubt, review.
  - After: Two details in `route()` are worth copying. The *act* door has an extra rule: nothing on a critical asset closes itself, however confident the model is. And the final line of code sends everything that doesn't clearly belong behind the other doors to a person. When in doubt, review.
- `chapters/ch14.qmd`
  - Before: The same shape works for any typed decision. For a `Choice` such as "which queue?", act on the top label only when its probability clears your line, and send the rest to review. It's Chapter 4's coverage-and-risk trade-off, one label at a time.
  - After: The same design works for any typed decision. For a `Choice` such as "which queue?", act on the top label only when its probability is above your threshold. Send the rest to review. It's Chapter 4's coverage-and-risk trade-off, one label at a time.
- `chapters/ch14.qmd`
  - Before: A policy that works in a notebook is maybe a third of the job. The rest is what happens on the day the model is down, the week the attackers change tactics, and the month an auditor asks why an alert was closed.
  - After: A policy that works in a notebook is maybe a third of the job. The rest is what happens on the day the model stops working, the week the attackers change methods, and the month an auditor asks why an alert was closed.
- `chapters/ch14.qmd`
  - Before: ![The decision loop in production. Every alert flows through the model, calibration and a versioned policy into one of three doors.
  - After: ![The decision loop in real use. Every alert flows through the model, calibration and a versioned policy into one of three doors.
- `chapters/ch14.qmd`
  - Before: @fig-production-loop shows the loop. Four habits make it trustworthy.
  - After: @fig-production-loop shows the loop. Four habits make it reliable.
- `chapters/ch14.qmd`
  - Before: **Write the policy down as code, and version it.** Thresholds that live in someone's head change without anyone noticing. `policy v3: act below 0.031, escalate at 0.34, fitted on 1–21 September, six analysts` is something you can review, test and roll back.
  - After: **Write the policy down as code, and give it a version number.** Thresholds that exist only in someone's head change without anyone noticing. `policy v3: act below 0.031, escalate at 0.34, fitted on 1–21 September, six analysts` is something you can review, test and go back to.
- `chapters/ch14.qmd`
  - Before: **Log every decision.** Jev returns probabilities, not reasons, and critics are right that this makes a single answer hard to explain. But you can make the *system* explainable. Record what the model saw, what it said, which policy version turned that into an action, and when. Then any decision can be replayed and questioned later.
  - After: **Log every decision.** Jev returns probabilities, not reasons, and critics are right that this makes a single answer hard to explain. But you can make the *system* explainable. Record what the model saw, what it said, which policy version turned that into an action, and when. Then anyone can repeat and question any decision later.
- `chapters/ch14.qmd`
  - Before: **Fail safe towards review, never towards act.** If the model times out, returns an error or is simply unavailable, the alert goes to a human. A decision system should never close alerts unseen because a dependency went down.
  - After: **When something fails, send the case to review, never to act.** If the model times out, returns an error or is simply unavailable, the alert goes to a person. A decision system should never close alerts unseen because another system it depends on stopped working.
- `chapters/ch14.qmd`
  - Before: Every alert that goes to review or escalation comes back with an answer: an analyst decided. Alerts the machine closed come back with *nothing*. If you only learn from the alerts people looked at, you will never see the machine's own mistakes, and your calibration checks will slowly go blind in the one zone where they matter.
  - After: Every alert that goes to review or escalation comes back with an answer: an analyst decided. Alerts the machine closed come back with *nothing*. If you only learn from the alerts people looked at, you will never see the machine's own mistakes. Your calibration checks will slowly stop seeing the one zone where they matter most.
- `chapters/ch14.qmd`
  - Before: So send a small random slice of auto-closed alerts, say 3%, to an analyst anyway. At Kestrel's volume that's about a dozen a day. It isn't free, and at a true miss rate around 1% you'll need a few weeks of audits before the estimate is tight. It's still the only clear window into the act zone.
  - After: So send a small random share of auto-closed alerts, say 3%, to an analyst anyway. At Kestrel's volume that's about a dozen a day. It isn't free. And if the true miss rate is about 1%, you'll need a few weeks of audits before the estimate is precise. It's still the only clear view of the act zone.
- `chapters/ch14.qmd`
  - Before: Thresholds are fitted to the past, and attackers live in the future. If an attacker learns what makes your model relax, for example alerts that look like approved IT tooling, they will shape their activity to land in the act zone. Random audits, never exposing scores outside the SOC, and rules that keep critical assets out of the act zone all make this harder. None make it impossible. The cost figures are guesses too. Revisit them when the business changes, not just when the model does.
  - After: Thresholds are fitted to the past, but attackers act in the future. If an attacker learns what makes your model relax, such as alerts that look like approved IT tools, they will shape their activity to land in the act zone. Three things make this harder: random audits, never showing scores outside the SOC, and rules that keep critical assets out of the act zone. None make it impossible. The cost figures are guesses too. Check them again when the business changes, not just when the model does.
- `chapters/ch14.qmd`
  - Before: In week five, Kestrel is hit by a phishing campaign. Link alerts fire three times as often as usual, and far more of them are real. Nothing about any individual alert looks unusual. The model scores them just as it scored last month's.
  - After: In week five, Kestrel is hit by a phishing campaign. Alerts about links fire three times as often as usual, and far more of them are real. Nothing about any single alert looks unusual. The model scores them just as it scored last month's.
- `chapters/ch14.qmd`
  - Before: In week five (shaded), reality pulls away from the model, and the queue overflows.]
  - After: In week five (shaded), reality moves away from the model, and the queue overflows.]
- `chapters/ch14.qmd`
  - Before: @fig-drift-watch shows two things going wrong at once. The model expected about {{< num ch21 campaign_pred pct >}} of alerts to be threats; the real figure was {{< num ch21 campaign_actual pct >}}. And the review queue climbed to an average of about {{< num ch21 campaign_reviews_per_day int >}} a day over the campaign week against a capacity of {{< num ch21 capacity int >}}, so work that nobody chose to skip started getting skipped.
  - After: @fig-drift-watch shows two things going wrong at once. The model expected about {{< num ch21 campaign_pred pct >}} of alerts to be threats; the real figure was {{< num ch21 campaign_actual pct >}}. And the review queue rose to an average of about {{< num ch21 campaign_reviews_per_day int >}} a day over the campaign week, against a capacity of {{< num ch21 capacity int >}}. So work that nobody chose to skip started getting skipped.
- `chapters/ch14.qmd`
  - Before: Neither problem is visible from a single alert. Both are obvious on a daily chart. That's why the weekly check in @fig-production-loop tracks three numbers: the share of alerts in each zone, the queue against capacity, and predicted threats against confirmed ones. When they diverge, three responses are available, and a human should pick among them: refit calibration on the most recent week, temporarily move the act line down for the affected alert type, or add review capacity until the campaign passes.
  - After: You can't see either problem from a single alert. Both are obvious on a daily chart. That's why the weekly check in @fig-production-loop tracks three numbers: the share of alerts in each zone, the queue against capacity, and predicted threats against confirmed ones. When they move apart, there are three possible responses, and a person should choose. Refit calibration on the most recent week. Or move the act threshold down for the affected type of alert, for a while. Or add review capacity until the campaign ends.
- `chapters/ch14.qmd`
  - Before: For a decision layer, I'd put it slightly differently: the purpose of a probability is an action. Everything in this chapter is the machinery for getting from one to the other without fooling yourself along the way.
  - After: For a decision layer, I'd say it slightly differently: the purpose of a probability is an action. Everything in this chapter is the machinery for getting from one to the other without fooling yourself.
- `chapters/ch14.qmd`
  - Before: We started with one probability and ended with a policy. Costs gave us two lines, and the lines sent every alert through one of three doors: act, review or escalate. Checking calibration against recent outcomes made those lines mean what they say. Capacity turned the cheapest policy on paper into the cheapest one the team can actually run, and put a price on two more analysts. With several answers per alert, stakes overrode confidence. Then the policy went into production with a log, an audit and a daily watch, and that watch caught the week the world changed.
  - After: We started with one probability and ended with a policy. Costs gave us two thresholds, and the thresholds sent every alert through one of three doors: act, review or escalate. Checking calibration against recent outcomes made those thresholds mean what they say. Capacity turned the cheapest policy in theory into the cheapest one the team can actually run, and put a price on two more analysts. With several answers per alert, what's at stake mattered more than confidence. Then the policy went into use with a log, an audit and a daily check. That check caught the week the world changed.
- `chapters/ch14.qmd`
  - Before: 1. In the lab, rerun the capacity search for 4, 8 and 10 analysts. Plot threats auto-closed per day against team size. Where does the curve flatten out, and what does that suggest about where extra money is best spent?
  - After: 1. In the lab, run the capacity search again for 4, 8 and 10 analysts. Plot threats auto-closed per day against team size. Where does the curve become flat, and what does that suggest about where extra money is best spent?
- `chapters/ch14.qmd`
  - Before: 2. Change the false-page cost from \$400 to \$2,000. Recompute both cost-optimal thresholds by hand, then check your answer with `cost_optimal_thresholds`. Which line moved, and why only that one?
  - After: 2. Change the cost of a false urgent call from \$400 to \$2,000. Work out both cost-based thresholds by hand, then check your answer with `cost_optimal_thresholds`. Which threshold moved, and why only that one?
- `chapters/ch14.qmd`
  - Before: 4. Your audit samples 3% of the act zone. After four weeks, analysts have found 11 real threats among 1,200 audited alerts. Estimate the true miss rate in the act zone, and say roughly how uncertain that estimate is. (Hint: this is a proportion, and Chapter 2's tools are enough.)
  - After: 4. Your audit checks 3% of the act zone. After four weeks, analysts have found 11 real threats among 1,200 audited alerts. Estimate the true miss rate in the act zone, and say about how uncertain that estimate is. (Hint: this is a proportion, and Chapter 2's tools are enough.)
- `chapters/ch14.qmd`
  - Before: Next: you now know how to turn one decision into an action. Chapter 15 shows the recurring shapes that decision layers take inside real systems, from "LLM extracts, Jev decides" to guardrails, judges and routers.
  - After: Next: you now know how to turn one decision into an action. Chapter 15 shows the common designs that decision layers use inside real systems, from "LLM extracts, Jev decides" to guardrails, judges and routers.

## Chapter 15: A catalogue of decision patterns

45 changes.

- `chapters/ch15.qmd`
  - Before: When you learn to cook, you start with recipes. After a while you notice that most recipes are the same few moves in different clothes: brown something, add liquid, reduce. Once you can see the moves, you stop needing the recipe.
  - After: When you learn to cook, you start with recipes. After a while, you notice that most recipes use the same few steps with different ingredients: fry something until brown, add liquid, cook until it thickens. Once you can see the steps, you stop needing the recipe.
- `chapters/ch15.qmd`
  - Before: Software has moves like that too, and people call them **patterns**. A pattern is a shape of solution that keeps turning up, with a name, so that a team can say "put a gate in front of that" and everyone knows what they mean.
  - After: Software has steps like that too, and people call them **patterns**. A pattern is a common kind of solution with a name. Then a team can say "put a gate in front of that" and everyone knows what they mean.
- `chapters/ch15.qmd`
  - Before: We've already met most of the decision patterns in this book, one at a time, inside Kestrel's story. This chapter lines them up. There are six. For each one: what it's for, what it looks like, what we measured where we could, and how it goes wrong.
  - After: We've already met most of the decision patterns in this book, one at a time, inside Kestrel's story. This chapter puts them side by side. There are six. For each one, we look at what it's for, what it looks like, what we measured where we could, and how it goes wrong.
- `chapters/ch15.qmd`
  - Before: - Recognise six recurring ways to put a decision model inside a larger system.
  - After: - Recognise six common ways to put a decision model inside a larger system.
- `chapters/ch15.qmd`
  - Before: Look at @fig-catalog before reading on and notice the common thread. In every pattern, the decision model never writes anything and never acts on its own. It answers a typed question, and ordinary code turns the answer into an action. That separation is what a decision layer is.
  - After: Look at @fig-catalog before reading on, and notice what the patterns share. In every pattern, the decision model never writes anything and never acts on its own. It answers a typed question, and ordinary code turns the answer into an action. That separation is what a decision layer is.
- `chapters/ch15.qmd`
  - Before: **The problem.** Your input is messy: an email, a chat message, a PDF, an alert written for humans. The decision you need is small and sharp. LLMs read messy input brilliantly. Chapter 13 showed they're weaker at the decision itself.
  - After: **The problem.** Your input is messy: an email, a chat message, a PDF, an alert written for people. The decision you need is small and clear. LLMs read messy input very well. Chapter 13 showed they're weaker at the decision itself.
- `chapters/ch15.qmd`
  - Before: **The pattern.** Let the LLM turn the mess into fields. Let the decision model decide on the fields.
  - After: **The pattern.** Let the LLM turn the messy input into fields. Let the decision model decide based on the fields.
- `chapters/ch15.qmd`
  - Before: ![Extract, then decide. The LLM reads the raw text and writes structured fields; a decision model answers a typed question about them; policy lines turn the answer into an action.
  - After: ![Extract, then decide. The LLM reads the raw text and writes structured fields; a decision model answers a typed question about them; policy thresholds turn the answer into an action.
- `chapters/ch15.qmd`
  - Before: We ran this on Kestrel's live week, alongside three other ways of making the same decision.
  - After: We ran this on Kestrel's live week, next to three other ways of making the same decision.
- `chapters/ch15.qmd`
  - Before: Extracting fields first beats letting the LLM decide, and edges out Jev reading the raw text.
  - After: Extracting fields first beats letting the LLM decide, and is slightly better than Jev reading the raw text.
- `chapters/ch15.qmd`
  - Before: Extracting first lifted the AUC from {{< num ch22 llm_decides_auc f3 >}}, when the LLM decided on its own, to {{< num ch22 extract_then_jev_auc f3 >}} (@fig-extract-results). It also edged out Jev reading the raw text directly, at {{< num ch22 jev_text_auc f3 >}}. The LLM's misreads, about {{< num ch22 misread pct >}} of alerts with a wrong number, were a small cost.
  - After: Extracting first raised the AUC from {{< num ch22 llm_decides_auc f3 >}}, when the LLM decided on its own, to {{< num ch22 extract_then_jev_auc f3 >}} (@fig-extract-results). It was also slightly better than Jev reading the raw text directly, at {{< num ch22 jev_text_auc f3 >}}. The LLM misread about {{< num ch22 misread pct >}} of alerts, writing a wrong number, but that cost little.
- `chapters/ch15.qmd`
  - Before: But look at the bottom row. The SIEM's own fields scored {{< num ch22 jev_fields_auc f3 >}}, better than any extraction. The extractor isn't to blame. The alert text simply never mentions some of what the SIEM knows, like how critical the machine is or the user's role, and no extractor can recover a fact that isn't written down.
  - After: But look at the bottom row. The SIEM's own fields scored {{< num ch22 jev_fields_auc f3 >}}, better than any extraction. The extractor isn't to blame. The alert text simply never mentions some of what the SIEM knows, like how critical the machine is or the user's job. No extractor can find a fact that isn't written down.
- `chapters/ch15.qmd`
  - Before: **How it breaks.** The extracted fields are LLM output, so everything Chapter 7 said applies: a planted sentence in the text can become a planted value in a field. Validate fields against types and ranges, and prefer trusted sources for anything that matters. One more thing: one extraction can feed many typed questions, so the LLM's cost is paid once per case, not once per decision.
  - After: **How it breaks.** The extracted fields are LLM output, so everything Chapter 7 said applies: a planted sentence in the text can become a planted value in a field. Check fields against types and allowed ranges, and use trusted sources for anything that matters. One more thing: one extraction can feed many typed questions. So you pay for the LLM once per case, not once per decision.
- `chapters/ch15.qmd`
  - Before: **The problem.** An agent runs a loop: observe, decide, act, repeat. Chapter 7 counted Kestrel's agent making about {{< num ch22 decide_per_alert f1 >}} small decisions per alert, and writing something only about {{< num ch22 generate_per_alert f2 >}} times. Yet most agent frameworks send every one of those decisions to the LLM, as text.
  - After: **The problem.** An agent runs a loop: observe, decide, act, repeat. Chapter 7 counted Kestrel's agent making about {{< num ch22 decide_per_alert f1 >}} small decisions per alert, and writing something only about {{< num ch22 generate_per_alert f2 >}} times. Yet most agent frameworks (the libraries people use to build agents) send every one of those decisions to the LLM, as text.
- `chapters/ch15.qmd`
  - Before: Because each decision comes back with probabilities, the loop can do something an LLM-driven loop can't do cleanly: notice when it's unsure. If no option is clearly ahead, stop and escalate, rather than picking one and carrying on confidently. Chapter 7's compounding arithmetic is the reason that matters: a small error rate per step becomes a large one over ten steps.
  - After: Each decision comes back with probabilities. So the loop can do something an LLM-driven loop can't easily do: notice when it's unsure. If no option is clearly ahead, stop and escalate, instead of picking one and continuing confidently. Chapter 7's arithmetic shows why that matters: a small error rate per step becomes a large one over ten steps.
- `chapters/ch15.qmd`
  - Before: **How it breaks.** Some steps aren't small decisions. Planning a novel investigation is real reasoning, and belongs with the LLM or a person. The skill is sorting the steps truthfully, the way Chapter 8 sorted System 1 work from System 2.
  - After: **How it breaks.** Some steps aren't small decisions. Planning the investigation of a new kind of attack is real reasoning, and belongs with the LLM or a person. The skill is sorting the steps honestly, the way Chapter 8 separated System 1 work from System 2.
- `chapters/ch15.qmd`
  - Before: **The problem.** Agents take actions: closing alerts, disabling accounts, sending emails. Chapter 7 showed how one planted sentence in an alert's text could talk the model into closing real threats. Auto-close among real threats went from {{< num ch22 inj_before pct >}} to {{< num ch22 inj_after pct >}}.
  - After: **The problem.** Agents take actions: closing alerts, disabling accounts, sending emails. Chapter 7 showed how one planted sentence in an alert's text could make the model close real threats. The share of real threats that were auto-closed went from {{< num ch22 inj_before pct >}} to {{< num ch22 inj_after pct >}}.
- `chapters/ch15.qmd`
  - Before: **The pattern.** Before any risky action runs, ask a typed question about it, using only trusted facts, and gate on the answer.
  - After: **The pattern.** Before any risky action runs, ask a typed question about it, using only trusted facts. Let the answer decide whether the action may go ahead.
- `chapters/ch15.qmd`
  - Before: In Chapter 7, reading only the trusted fields held auto-close at {{< num ch22 inj_trusted pct >}} under the same attack. The gate didn't need to be clever. It needed to look at the right things.
  - After: In Chapter 7, reading only the trusted fields kept auto-close at {{< num ch22 inj_trusted pct >}} under the same attack. The gate didn't need to be clever. It needed to look at the right things.
- `chapters/ch15.qmd`
  - Before: The three outcomes are the three zones of Chapter 14, pointed at actions instead of alerts. The lines come from the same arithmetic: what a wrongly allowed action costs, against what it costs to ask a person.
  - After: The three outcomes are the three zones of Chapter 14, used for actions instead of alerts. The thresholds come from the same arithmetic: what a wrongly allowed action costs, against what it costs to ask a person.
- `chapters/ch15.qmd`
  - Before: **How it breaks.** A gate is only as good as its idea of "trusted". If the attacker can write to a field you trust, the gate trusts the attacker. And a gate that asks a person too often gets clicked through; watch its ask rate the way Chapter 14 watched the review queue.
  - After: **How it breaks.** A gate is only as good as its idea of "trusted". If the attacker can write to a field you trust, the gate trusts the attacker. And people start approving everything from a gate that asks them too often without reading. Watch how often it asks, the way Chapter 14 watched the review queue.
- `chapters/ch15.qmd`
  - Before: **The problem.** Some outputs have to be written: an incident note, a customer reply, a summary for the board. LLMs write them well. They also sometimes state things the evidence doesn't support.
  - After: **The problem.** Some outputs have to be written: an incident note, a customer reply, a summary for the company's leaders. LLMs write them well. They also sometimes state things the evidence doesn't support.
- `chapters/ch15.qmd`
  - Before: **The pattern.** After the LLM writes, ask typed questions *about* the draft. Is every claim supported by the evidence? Does it name the affected host? Is the tone appropriate for a customer? Ship it, send it back once with the gaps named, or hand it to a person.
  - After: **The pattern.** After the LLM writes, ask typed questions *about* the draft. Is every claim supported by the evidence? Does it name the affected host? Is the tone right for a customer? Then send it, return it once with the problems listed, or give it to a person.
- `chapters/ch15.qmd`
  - Before: the answer decides whether the draft ships, goes back once for a redraft, or goes to a person.]
  - After: the answer decides whether the draft is sent, goes back once to be rewritten, or goes to a person.]
- `chapters/ch15.qmd`
  - Before: The listing stops short of printing the answer on purpose. The book's mock can't really check claims against evidence, so any number it gave here would be noise dressed up as a result. The shape is what matters, and it's the same shape as the LLM-as-judge from Chapter 13, with two differences. The answer is a probability you can calibrate and put lines on, not a 1-to-10 rating. And the check is cheap enough to run on every draft, not a sample.
  - After: The listing doesn't print the answer, on purpose. The book's mock can't really check claims against evidence, so any number it gave here would be meaningless, even though it would look like a result. The design is what matters. It's the same design as the LLM-as-judge from Chapter 13, with two differences. The answer is a probability you can calibrate and put thresholds on, not a 1-to-10 rating. And the check is cheap enough to run on every draft, not just a sample.
- `chapters/ch15.qmd`
  - Before: **How it breaks.** A checker that shares the writer's blind spots will wave its mistakes through. Test the checker on drafts you know are wrong. And cap the redrafts: a loop of "write, reject, rewrite" can run forever, so after one retry a person takes over.
  - After: **How it breaks.** A checker with the same weaknesses as the writer will let its mistakes through. Test the checker on drafts you know are wrong. And limit the rewrites: a loop of "write, reject, rewrite" can run forever. After one retry, a person takes over.
- `chapters/ch15.qmd`
  - Before: **The problem.** Cases need to go somewhere: the identity team, the malware team, the data-loss team. A wrong route costs a handoff and a delay.
  - After: **The problem.** Cases need to go somewhere: the identity team, the malware team, the data-loss team. Sending a case to the wrong team costs a transfer and a delay.
- `chapters/ch15.qmd`
  - Before: **The pattern.** Ask a `choice` with one option per destination. Route automatically only when the top option is clearly ahead; send the rest to a general queue, where a person routes them.
  - After: **The pattern.** Ask a `choice` with one option per team. Send the case automatically only when the top option is clearly ahead. Send the rest to a general queue, where a person decides where they go.
- `chapters/ch15.qmd`
  - Before: On a sample of the live week, routing every alert by the top label sent {{< num ch22 route_all_acc pct >}} to the right team. Routing only when the top probability was at least {{< num ch22 route_line f1 >}} covered {{< num ch22 route_cov pct >}} of alerts, and {{< num ch22 route_acc pct >}} of those went to the right place (@fig-router-15). Chapter 4's coverage trade-off again, and the curve lets you choose where to stand on it.
  - After: On a sample of the live week, routing every alert by the top label sent {{< num ch22 route_all_acc pct >}} to the right team. Routing only when the top probability was at least {{< num ch22 route_line f1 >}} covered {{< num ch22 route_cov pct >}} of alerts, and {{< num ch22 route_acc pct >}} of those went to the right place (@fig-router-15). It's Chapter 4's coverage trade-off again, and the curve lets you choose your point on it.
- `chapters/ch15.qmd`
  - Before: The same pattern routes between *models*: a cheap one for the confident cases, a slow one for the rest. That's Chapter 8's route by doubt, and it's probably the most valuable single use of calibrated probabilities.
  - After: The same pattern can choose between *models*: a cheap one for the confident cases, a slow one for the rest. That's Chapter 8's routing by doubt, and it's probably the most valuable single use of calibrated probabilities.
- `chapters/ch15.qmd`
  - Before: **How it breaks.** Remember Chapter 10: a choice must give every real case somewhere to go. A router without an "other" or "not sure" option will confidently misroute the cases that fit nowhere.
  - After: **How it breaks.** Remember Chapter 10: a choice must give every real case somewhere to go. A router without an "other" or "not sure" option will confidently send the cases that fit nowhere to the wrong team.
- `chapters/ch15.qmd`
  - Before: **The problem.** Agents need memory: past cases, what a host usually does, which policies apply. Every step raises small questions about it. Is this worth remembering? Which store should I look in? Is this old note still true? Chapter 7 showed that retrieving the wrong thing is one of the commonest ways a RAG system fails.
  - After: **The problem.** Agents need memory: past cases, what a host usually does, which policies apply. Every step raises small questions about it. Is this worth remembering? Where should I look? Is this old note still true? Chapter 7 showed that retrieving the wrong thing is one of the most common ways a RAG system fails.
- `chapters/ch15.qmd`
  - Before: **The pattern.** Treat each read and write as a typed decision. A noul decides whether a new fact is worth keeping. A choice decides which store to search, including "none". Only after the memory work is done does the LLM reason over what was fetched.
  - After: **The pattern.** Treat each read and write as a typed decision. A noul decides whether a new fact is worth keeping. A choice decides which store to search, including "none". Only after the memory work is done does the LLM reason about what was found.
- `chapters/ch15.qmd`
  - Before: Jev-Mem works much like this. In the design by Jiang, Li and Li at the University of Texas at Dallas, a System One controller decides how each memory is typed and linked, and at query time chooses the route, the retrieval budget and when to stop, calling a slower reasoning model only to compose the final answer [@jevmem2026]. On the LoCoMo long-conversation benchmark the authors report an LLM-as-judge score of 0.777, 11% above their strongest baseline, with memory built 6.6 times faster and queries answered in 0.93 seconds on average, 37% faster; those are the authors' numbers, not a replication.
  - After: Jev-Mem works much like this. It was designed by Jiang, Li and Li at the University of Texas at Dallas [@jevmem2026]. A System One controller decides how each memory is typed and linked. When a question comes in, it chooses where to look, how much to retrieve and when to stop. It calls a slower reasoning model only to write the final answer. The authors tested it on LoCoMo, a benchmark of long conversations. They report an LLM-as-judge score of 0.777, 11% above the best system they compared it with. Memory was built 6.6 times faster, and questions were answered in 0.93 seconds on average, 37% faster. Those are the authors' numbers; nobody has repeated the test here.
- `chapters/ch15.qmd`
  - Before: The idea underneath is the one this book keeps returning to: memory operations are frequent, small and typed, which makes them the kind of decision a decision model is for.
  - After: The idea underneath is the one this book keeps coming back to. Memory operations are frequent, small and typed. That makes them exactly the kind of decision a decision model is for.
- `chapters/ch15.qmd`
  - Before: **How it breaks.** Memory decisions fail without a sound. A fact wrongly discarded never shows up as an error; it just isn't there when it's needed. Log what the controller discards, and audit a sample, as Chapter 14 did with auto-closed alerts.
  - After: **How it breaks.** Memory decisions fail silently. A fact thrown away by mistake never shows up as an error; it just isn't there when it's needed. Log what the controller throws away, and audit a sample, as Chapter 14 did with auto-closed alerts.
- `chapters/ch15.qmd`
  - Before: Only patterns 1, 3 and 5 have measurements in this chapter, and all of them are synthetic. The others are shapes, drawn from how the pieces work, and each needs testing on real data before you trust it. Combining patterns multiplies failure points: an extractor feeding a gate feeding a router has three places to be wrong, and the errors can compound as Chapter 7 showed. And every pattern here assumes the decision model's probabilities hold on your data, which Chapter 11 said you must check, not assume.
  - After: Only patterns 1, 3 and 5 have measurements in this chapter, and all of them are synthetic. The others are designs based on how the pieces work, and each needs testing on real data before you trust it. Combining patterns adds more places to fail. An extractor feeding a gate feeding a router has three places to be wrong, and the errors can add up, as Chapter 7 showed. And every pattern here assumes the decision model is calibrated on your data. Chapter 11 said you must check that, not assume it.
- `chapters/ch15.qmd`
  - Before: Kestrel's agent wants to disable a user account when it suspects stolen credentials. Disabling a real attacker's account early saves about \$10,000. Disabling an innocent user's account costs about \$300 in lost work and a help-desk call. Asking the on-call analyst costs about \$15 and a few minutes. Where would you put the gate's two lines on P(attack)?
  - After: Kestrel's agent wants to disable a user account when it suspects a stolen password. Disabling a real attacker's account early saves about \$10,000. Disabling an innocent user's account costs about \$300 in lost work and a help-desk call. Asking the analyst on call costs about \$15 and a few minutes. Where would you put the gate's two thresholds on P(attack)?
- `chapters/ch15.qmd`
  - Before: (Allow when disabling is clearly worth it and asking adds nothing, block when it clearly isn't. Using Chapter 14's arithmetic: asking beats blocking once P × \$10,000 exceeds about \$15, so above roughly 0.2%; allowing beats asking once the expected cost of a wrong disable, (1 − P) × \$300, drops below \$15, so above about 0.95. Most cases land in the middle and go to a person, which is fine at Kestrel's volume. At a hundred times the volume, it wouldn't be.)
  - After: (Allow when disabling is clearly worth it and asking adds nothing. Block when it clearly isn't worth it. Using Chapter 14's arithmetic: asking is better than blocking once P × \$10,000 is more than about \$15, so above about 0.2%. Allowing is better than asking once the expected cost of a wrong disable, (1 − P) × \$300, drops below \$15, so above about 0.95. Most cases land in the middle and go to a person. That's fine at Kestrel's volume. At a hundred times the volume, it wouldn't be.)
- `chapters/ch15.qmd`
  - Before: Alexander was an architect writing about towns and buildings [@alexander1977]. Software engineers borrowed his idea, and it fits decision layers well: the same few shapes, never quite the same twice.
  - After: Alexander was an architect writing about towns and buildings [@alexander1977]. Software engineers borrowed his idea, and it fits decision layers well: the same few designs, never used in exactly the same way twice.
- `chapters/ch15.qmd`
  - Before: We lined up six patterns, and all of them had the same spine. Something else writes, reads or acts, and a typed question decides. Letting the LLM extract fields and Jev decide beat letting the LLM decide, though nothing beat the facts the SIEM already had. Gates kept a planted sentence from closing real threats because they looked only at trusted facts. A router that stepped aside when unsure was right far more often than one that always answered. Checking drafts and managing memory are decisions too, and so are the small steps inside every agent loop.
  - After: We put six patterns side by side, and all of them had the same structure. Something else writes, reads or acts, and a typed question decides. Letting the LLM extract fields and Jev decide beat letting the LLM decide, though nothing beat the facts the SIEM already had. Gates stopped a planted sentence from closing real threats, because they looked only at trusted facts. A router that passed cases on when unsure was right far more often than one that always answered. Checking drafts and managing memory are decisions too, and so are the small steps inside every agent loop.
- `chapters/ch15.qmd`
  - Before: That closes Part IV. We've compared the methods, drawn the lines and named the patterns. Part V builds them.
  - After: That ends Part IV. We've compared the methods, set the thresholds and named the patterns. Part V builds them.
- `chapters/ch15.qmd`
  - Before: 1. In the lab, change the router's line from 0.8 to 0.6 and to 0.9. Which would you choose if a misroute costs an hour and the general queue costs twenty minutes per alert?
  - After: 1. In the lab, change the router's threshold from 0.8 to 0.6 and to 0.9. Which would you choose if sending an alert to the wrong team costs an hour and the general queue costs twenty minutes per alert?
- `chapters/ch15.qmd`
  - Before: 2. Design a guardrail gate for an email agent that can send messages to customers. What's the typed question? Which facts are trusted? Where do the lines go?
  - After: 2. Design a guardrail gate for an email agent that can send messages to customers. What's the typed question? Which facts are trusted? Where do the thresholds go?
- `chapters/ch15.qmd`
  - Before: 4. The "check the writer" pattern can share the writer's blind spots. Describe a test that would reveal that.
  - After: 4. The checker in the "check the writer" pattern can have the same weaknesses as the writer. Describe a test that would show that.

## Chapter 16: First calls

35 changes.

- `chapters/ch16.qmd`
  - Before: Fifteen chapters in, you know what a System One model is for, how to test it and where to put it. You haven't yet written the ten lines of code that actually call one.
  - After: After fifteen chapters, you know what a System One model is for, how to test it and where to put it. But you haven't yet written the ten lines of code that actually call one.
- `chapters/ch16.qmd`
  - Before: That moment has a particular feeling with any new API. Where does the key go? What does an error look like? Will a bug in a loop cost me money? Will my tests break when the network's down?
  - After: Starting with any new API raises the same questions. Where does the key go? What does an error look like? Will a bug in a loop cost me money? Will my tests break when the network is down?
- `chapters/ch16.qmd`
  - Before: This chapter answers those questions with the official TypeSafe library, `typesafe-sdk`, and the book's mock. By the end you'll have made every kind of call, provoked every kind of error, and written tests that never touch the network. None of it will have cost anything.
  - After: This chapter answers those questions with the official TypeSafe library, `typesafe-sdk`, and the book's mock. By the end, you'll have made every kind of call, caused every kind of error, and written tests that never use the network. None of it will have cost anything.
- `chapters/ch16.qmd`
  - Before: - Tell errors you should retry from errors you should fix, and set retries for your latency budget.
  - After: - Tell errors you should retry from errors you should fix, and set retries to fit your time limit.
- `chapters/ch16.qmd`
  - Before: - Record real answers once and replay them in tests forever.
  - After: - Record real answers once and replay them in tests as often as you like.
- `chapters/ch16.qmd`
  - Before: The response carries more than the answer. `r.nouls`, `r.choices` and `r.scores` hold the typed answers, keyed by the names you gave your questions. `r.usage` counts tokens, which is what you're billed on. `r.request_id` identifies the call, and it's worth logging next to every decision so that you can trace a surprising answer later. And `r.raw_http_response` is there when you need the headers.
  - After: The response contains more than the answer. `r.nouls`, `r.choices` and `r.scores` hold the typed answers, under the names you gave your questions. `r.usage` counts tokens, which is what you pay for. `r.request_id` identifies the call. Log it next to every decision, so that you can trace a surprising answer later. And `r.raw_http_response` is there when you need the headers.
- `chapters/ch16.qmd`
  - Before: ## One argument decides what's on the other end
  - After: ## One argument decides where the request goes
- `chapters/ch16.qmd`
  - Before: A **transport** is the lowest layer of an HTTP client: the part that takes a finished request and returns a response. The SDK lets you supply your own, and that's the seam the book's mock plugs into (@fig-layers). Your code, the SDK's request building, its retries and its parsing all run as they would against the real service. Only the last step is different.
  - After: A **transport** is the lowest layer of an HTTP client: the part that takes a finished request and returns a response. The SDK lets you supply your own, and that's where the book's mock connects (@fig-layers). Your code, the SDK's request building, its retries and its parsing all run just as they would against the real service. Only the last step is different.
- `chapters/ch16.qmd`
  - Before: For the same reason, the mock can be trusted as a stand-in for the *interface*. It accepts the same request shape as the API, returns the same answer shape, and rejects bad requests with the same error codes, which I checked against the SDK's own data models. What it can't stand in for is the *answers*. They come from a small synthetic engine, every response says so in an `x-jevkit-synthetic` header, and the model name it reports is `jev-mock-synthetic`.
  - After: For the same reason, you can trust the mock as a stand-in for the *interface*. It accepts the same request shape as the API and returns the same answer shape. It rejects bad requests with the same error codes; I checked them against the SDK's own data models. What it can't stand in for is the *answers*. They come from a small synthetic engine. Every response says so in an `x-jevkit-synthetic` header, and the model name it reports is `jev-mock-synthetic`.
- `chapters/ch16.qmd`
  - Before: To call the real thing, drop the transport and give it a key:
  - After: To call the real service, remove the transport and give it a key:
- `chapters/ch16.qmd`
  - Before: Or use `jevkit.client()`, which returns the mock unless you set `JEVKIT_LIVE=1` and a key. Every lab in the book runs through it, so each one can be pointed at real Jev with two environment variables.
  - After: Or use `jevkit.client()`, which returns the mock unless you set `JEVKIT_LIVE=1` and a key. Every lab in the book uses it, so you can point each one at real Jev by setting two environment variables.
- `chapters/ch16.qmd`
  - Before: Pin the model if you can. `jev-latest` is an alias, and aliases move. Chapter 9 said the unknowns in a new model include how its behaviour changes between versions; pinning is how you make that a decision rather than a surprise.
  - After: Use a fixed model version if you can. `jev-latest` is a nickname that can point to a new version at any time. Chapter 9 said one unknown in a new model is how its behaviour changes between versions. Fixing the version turns that into your decision, not a surprise.
- `chapters/ch16.qmd`
  - Before: ## What happens on the wire
  - After: ## What happens during a call
- `chapters/ch16.qmd`
  - Before: ![One call's life. The SDK validates and sends the request.
  - After: ![The steps of one call. The SDK checks and sends the request.
- `chapters/ch16.qmd`
  - Before: Most of the time a call goes straight along the top of @fig-lifecycle. The interesting parts are the two ways off it.
  - After: Most of the time, a call goes straight along the top of @fig-lifecycle. The interesting parts are the two other paths.
- `chapters/ch16.qmd`
  - Before: I provoked every error I could think of against the mock and recorded what the SDK did.
  - After: I caused every error I could think of against the mock, and recorded what the SDK did.
- `chapters/ch16.qmd`
  - Before: **Your mistakes** fail fast: no key, a model name that doesn't exist, a question with no options. Some are caught before anything is sent; the rest come back as a 4xx error. Retrying them is pointless, because the same request will fail the same way. Fix the code.
  - After: **Your mistakes** fail at once: no key, a model name that doesn't exist, a question with no options. Some are caught before anything is sent; the rest come back as a 4xx error. Retrying them is pointless, because the same request will fail the same way. Fix the code.
- `chapters/ch16.qmd`
  - Before: **The world's mistakes** are worth retrying: rate limits (429), server errors (5xx) and a network that drops. The SDK retries these by default, twice, waiting a little longer each time.
  - After: **Problems outside your code** are worth retrying: rate limits (429), server errors (5xx) and a lost network connection. The SDK retries these by default, twice, waiting a little longer each time.
- `chapters/ch16.qmd`
  - Before: To see what retries buy, I made the mock fail at random, then counted how many calls succeeded.
  - After: To see what retries gain, I made the mock fail at random, then counted how many calls succeeded.
- `chapters/ch16.qmd`
  - Before: With one request in five failing, only {{< num ch23 ok_20_0 pct >}} of calls succeed with no retries. With the SDK's default two retries, {{< num ch23 ok_20_2 pct1 >}} do (@fig-retries). The arithmetic is simple: if each attempt fails independently with probability *q*, a call with *r* retries fails only with probability *q*^*r*+1^.
  - After: With one request in five failing, only {{< num ch23 ok_20_0 pct >}} of calls succeed with no retries. With the SDK's default two retries, {{< num ch23 ok_20_2 pct1 >}} do (@fig-retries). The arithmetic is simple. Suppose each attempt fails with probability *q*, independently of the others. Then a call with *r* retries fails only with probability *q*^*r*+1^.
- `chapters/ch16.qmd`
  - Before: Retries cost time, though. The default policy waits about half a second, then a second, before retrying. Fine for a batch job; not for Chapter 12's login check, which had three hundred milliseconds in total.
  - After: Retries cost time, though. The default policy waits about half a second, then a second, before retrying. That's fine for a job that runs in the background. It's not fine for Chapter 12's login check, which had three hundred milliseconds in total.
- `chapters/ch16.qmd`
  - Before: So here's the decision-layer way to think about it. A call that fails is just another case your policy must handle. For a tight budget, allow no retries and decide what a failure *means*: for a login, maybe "allow, but flag for review"; for closing an alert, "don't close; send to the queue". Chapter 14 called this a fail-safe. It belongs in the policy, where it's visible, not buried in a retry setting.
  - After: So here's how to think about it as a decision layer. A call that fails is just another case your policy must handle. With a tight time limit, allow no retries, and decide what a failure *means*. For a login, maybe it means "allow, but flag for review". For closing an alert, "don't close; send to the queue". Chapter 14 called this a fail-safe. It belongs in the policy, where people can see it, not hidden in a retry setting.
- `chapters/ch16.qmd`
  - Before: Retry the world's errors, never your own. And when the clock matters, decide in advance what a failed call means.
  - After: Retry errors from outside your code, never your own. And when time matters, decide in advance what a failed call means.
- `chapters/ch16.qmd`
  - Before: Asking Kestrel's four triage questions in one call used about {{< num ch23 tokens_four_one int >}} input tokens. Asking them in four separate calls used {{< num ch23 tokens_four_sep int >}}, because the alert went over the wire four times (@fig-tokens). One call is also one round trip instead of four.
  - After: Asking Kestrel's four triage questions in one call used about {{< num ch23 tokens_four_one int >}} input tokens. Asking them in four separate calls used {{< num ch23 tokens_four_sep int >}}, because the alert was sent four times (@fig-tokens). One call also means one trip to the server and back instead of four.
- `chapters/ch16.qmd`
  - Before: These are the mock's token counts, not the real tokeniser's. But they suggest something worth noticing: a Kestrel alert is short, about {{< num ch23 tokens_text int >}} tokens as text. Chapters 9 and 12 assumed 500 tokens per decision, which was generous. At short states like these, the vendor-reported price works out to a few dollars per million decisions.
  - After: These are the mock's token counts, not the real tokeniser's. But they show something worth noticing: a Kestrel alert is short, about {{< num ch23 tokens_text int >}} tokens as text. Chapters 9 and 12 assumed 500 tokens per decision, which was more than needed. For short states like these, the vendor-reported price comes to a few dollars per million decisions.
- `chapters/ch16.qmd`
  - Before: ## Tests that never touch the network
  - After: ## Tests that never use the network
- `chapters/ch16.qmd`
  - Before: Everything so far runs against the mock, so tests using it are already free, fast and repeatable. But at some point you'll want tests built on *real* answers, and you won't want them to call the API on every run.
  - After: Everything so far runs against the mock, so tests using it are already free, fast and repeatable. But at some point you'll want tests built on *real* answers. And you won't want them to call the API every time they run.
- `chapters/ch16.qmd`
  - Before: ![Record once, replay forever. With a key, a recording transport saves each real request and response to a file.
  - After: ![Record once, replay many times. With a key, a recording transport saves each real request and response to a file.
- `chapters/ch16.qmd`
  - Before: The toolkit includes both halves (@fig-record-replay). `RecordingTransport` wraps any transport and writes each exchange to a JSON-lines file, which testers call a **cassette**. `ReplayTransport` answers from that file, and raises if a test asks something that wasn't recorded, so a changed question can't silently pass.
  - After: The toolkit includes both parts (@fig-record-replay). `RecordingTransport` wraps any transport and writes each request and response to a JSON-lines file. Testers call this file a **cassette**. `ReplayTransport` answers from that file. It raises an error if a test asks something that wasn't recorded, so a changed question can't pass without anyone noticing.
- `chapters/ch16.qmd`
  - Before: The book's own repository works this way. Every lab and every listing runs in CI against the mock on each change. A separate weekly job calls the real API, if a key is configured, and checks that it still has the shape the book teaches, so a change in the interface shows up as a failing check rather than a surprise. Comparing the real *answers* against a recorded baseline is the natural next step, and exercise 3 builds the pieces.
  - After: The book's own repository works this way. Every lab and every listing runs against the mock on each change, in an automatic test system (CI, continuous integration). A separate weekly job calls the real API, if a key is set up. It checks that the API still has the shape the book teaches. So a change in the interface shows up as a failing check, not a surprise. The natural next step is to compare the real *answers* with recorded ones, and exercise 3 builds the pieces.
- `chapters/ch16.qmd`
  - Before: The mock copies the interface, not the model: every answer it gives is synthetic, and its token counts are its own. Behaviour the SDK leaves to the server, such as exact rate limits, timeouts under load and the precise meaning of `confidence`, can only be learned against the real API. Replayed cassettes go stale: they record what the model said on the day you recorded them, so re-record on a schedule and when you change model versions. And retries hide trouble as well as fixing it; count them, because a rising retry rate is often the first sign that something upstream is wrong.
  - After: The mock copies the interface, not the model. Every answer it gives is synthetic, and its token counts are its own. Some behaviour is decided by the server, not the SDK: exact rate limits, timeouts when the server is busy, and the exact meaning of `confidence`. You can only learn those from the real API. Replayed cassettes go out of date. They record what the model said on the day you recorded them, so record again on a schedule and when you change model versions. And retries hide problems as well as fixing them. Count them, because a rising retry rate is often the first sign that something is wrong at the server.
- `chapters/ch16.qmd`
  - Before: Kestrel's login check has a 300 ms budget. If the call to Jev fails or times out, the login must still be decided. Letting a risky login through costs about \$10,000 times its P(attack); blocking an innocent login costs about \$20 of lost work and a help-desk call. The typical login has P(attack) around 0.0001. What should a failed call do?
  - After: Kestrel's login check has a time limit of 300 ms. If the call to Jev fails or times out, the login must still be decided. Letting a risky login through costs about \$10,000 times its P(attack). Blocking an innocent login costs about \$20 of lost work and a help-desk call. The typical login has P(attack) around 0.0001. What should a failed call do?
- `chapters/ch16.qmd`
  - Before: (With no answer, the best estimate is the base rate. Letting it through costs about 0.0001 × \$10,000 = \$1 on average; blocking costs about \$20. So fail open: allow the login, and log it for a later check. For a class of logins with a much higher base rate, such as admin accounts from new countries, the same arithmetic may say fail closed.)
  - After: (With no answer, the best estimate is the base rate. Letting it through costs about 0.0001 × \$10,000 = \$1 on average; blocking costs about \$20. So when the call fails, allow the login, and log it for a later check. For a group of logins with a much higher base rate, such as admin accounts signing in from new countries, the same arithmetic may say: block when the call fails.)
- `chapters/ch16.qmd`
  - Before: Dijkstra's point [@dijkstra1970] is doubly true for a model behind an API: tests against a mock show your code handles the answers. They can't show the answers will be good. That's what Chapter 11's calibration checks are for.
  - After: Dijkstra's point [@dijkstra1970] is even more true for a model behind an API. Tests against a mock show that your code handles the answers. They can't show that the answers will be good. That's what Chapter 11's calibration checks are for.
- `chapters/ch16.qmd`
  - Before: The first call was ten lines, and the only thing that made it a mock was the transport. Errors split into two kinds: our own, which fail fast and should be fixed, and the world's, which the SDK retries. When the clock is tight, a failed call becomes a case for the policy to decide, not a retry setting. Asking four questions in one call sent the alert once instead of four times. And a recording made once with a key can drive every test afterwards, with no key at all.
  - After: The first call was ten lines, and the only thing that made it a mock was the transport. Errors come in two kinds. Our own fail at once and should be fixed. Errors from outside our code are retried by the SDK. When time is tight, a failed call becomes a case for the policy to decide, not a retry setting. Asking four questions in one call sent the alert once instead of four times. And a recording made once with a key can run every test afterwards, with no key at all.

## Chapter 17: A hybrid agent

30 changes.

- `chapters/ch17.qmd`
  - Before: Chapter 7 built Kestrel an agent. It read an alert, chose which evidence to gather, decided whether it had enough, reached a verdict and acted. We counted its steps, and more than half were small decisions.
  - After: Chapter 7 built an agent for Kestrel. It read an alert, chose which evidence to collect, decided whether it had enough, reached a verdict and acted. We counted its steps, and more than half were small decisions.
- `chapters/ch17.qmd`
  - Before: This chapter rebuilds that agent properly, as a **hybrid**: Jev makes every decision, and the LLM writes only what a person will read. Then we race it against an all-LLM version of itself.
  - After: This chapter builds that agent again, properly, as a **hybrid**: Jev makes every decision, and the LLM writes only what a person will read. Then we compare it with a version where the LLM does everything.
- `chapters/ch17.qmd`
  - Before: But first I have to tell you about a bug. It was in Chapter 7's agent all along, it never crashed, and I only found it because of a habit this chapter will try to give you.
  - After: But first I have to tell you about a bug. It was in Chapter 7's agent from the start. It never caused a crash, and I only found it because of a habit this chapter will try to teach you.
- `chapters/ch17.qmd`
  - Before: - Catch a decision step that's silently wrong by watching the distribution of its answers.
  - After: - Find a decision step that's wrong without any error, by counting how often it gives each answer.
- `chapters/ch17.qmd`
  - Before: - Know which work to leave as a decision, and which to simply do.
  - After: - Know which work to leave as a decision, and which to just do.
- `chapters/ch17.qmd`
  - Before: Jev decides which other evidence to gather, then answers the three verdict questions together. Chapter 14's policy turns the verdict into an action, and the LLM writes a case note or page message only when a person will read it.]
  - After: Jev decides which other evidence to collect, then answers the three verdict questions together. Chapter 14's policy turns the verdict into an action, and the LLM writes a case note or urgent message only when a person will read it.]
- `chapters/ch17.qmd`
  - Before: @fig-architecture-17 shows the design. Everything in green is a typed question to Jev, answered in one pass. Everything in blue is a tool that reads something. The policy is ordinary code. The LLM, in orange, appears once, at the end, and only on the paths where a person is waiting to read something.
  - After: @fig-architecture-17 shows the design. Everything in green is a typed question to Jev, answered in one pass. Everything in blue is a tool that reads something. The policy is ordinary code. The LLM, in orange, appears once, at the end. And it appears only on the paths where a person is waiting to read something.
- `chapters/ch17.qmd`
  - Before: That printout is the agent's **trace**, and it's more useful than it looks. It's the debugging tool, the audit log and the explanation all at once. When someone asks next month why alert 118 was closed, you read the trace: which evidence was gathered, what each decision said, with what probability, and which policy line it crossed.
  - After: That printout is the agent's **trace**: the step-by-step record of what it did. It's more useful than it looks. It's a debugging tool, an audit log and an explanation all at once. When someone asks next month why alert 118 was closed, you read the trace. It shows which evidence was collected, what each decision said, with what probability, and which policy threshold it crossed.
- `chapters/ch17.qmd`
  - Before: When I first ran the agent across the live week, the results looked plausible. Actions were spread across the three zones, every answer parsed, and nothing raised an error. Then came a check that's worth running on every decision step of every agent: count its answers.
  - After: When I first ran the agent over the live week, the results looked reasonable. Actions were spread across the three zones, every answer parsed, and nothing raised an error. Then I ran a check that's worth running on every decision step of every agent: count its answers.
- `chapters/ch17.qmd`
  - Before: Across {{< num ch24 n int >}} alerts, the "which evidence next?" decision chose host history, the policy lookup and "none" in roughly equal measure. It never chose threat intel. Not once (@fig-never-picked).
  - After: Across {{< num ch24 n int >}} alerts, the "which evidence next?" decision chose host history, the policy lookup and "none" about equally often. It never chose threat intel. Not once (@fig-never-picked).
- `chapters/ch17.qmd`
  - Before: So the verdict was always reached without the single most informative fact about an alert, and the model filled the gap with a default. The ranking suffered: AUC {{< num ch24 v1_auc f3 >}}, against the {{< num ch24 v2_auc f3 >}} it reaches with threat intel. And about {{< num ch24 v1_closed_threats_day f1 >}} real threats a day were auto-closed.
  - After: So the verdict was always reached without the most useful fact about an alert, and the model used a default value instead. The ranking got worse: AUC {{< num ch24 v1_auc f3 >}}, against the {{< num ch24 v2_auc f3 >}} it reaches with threat intel. And about {{< num ch24 v1_closed_threats_day f1 >}} real threats a day were auto-closed.
- `chapters/ch17.qmd`
  - Before: I want to be careful about what this says. The mock's evidence choices come from a simple word-matching engine, so I can't tell you real Jev would make the same mistake. What I can tell you is that *any* decision step can fail this way, whichever model answers it, and that nothing downstream will complain. Typed answers are always well-formed. Well-formed and right aren't the same thing.
  - After: I want to be careful about what this shows. The mock's evidence choices come from a simple word-matching engine, so I can't tell you real Jev would make the same mistake. What I can tell you is that *any* decision step can fail this way, whichever model answers it. And nothing later in the chain will report a problem. Typed answers always have the right format. The right format and the right answer aren't the same thing.
- `chapters/ch17.qmd`
  - Before: Chart the answers of every decision step. An option that's never chosen, or always chosen, is a warning, even when nothing has crashed.
  - After: Count the answers of every decision step. An option that's never chosen, or always chosen, is a warning, even when nothing has crashed.
- `chapters/ch17.qmd`
  - Before: The fix wasn't a better prompt or a better model. It was a design change. A threat-intel lookup takes a fraction of a second and costs nothing. Deciding *whether* to look it up costs about as much as just looking. When an observation is cheaper than the decision about it, don't decide. Do it.
  - After: The fix wasn't a better prompt or a better model. It was a design change. A threat-intel lookup takes a fraction of a second and costs nothing. Deciding *whether* to look it up costs about as much as just looking. When looking is cheaper than deciding whether to look, don't decide. Just look.
- `chapters/ch17.qmd`
  - Before: ## Racing the all-LLM agent
  - After: ## Comparing with the all-LLM agent
- `chapters/ch17.qmd`
  - Before: Now the comparison. The all-LLM agent runs the same loop, with the same tools and the same policy lines. The only difference is who decides: every decision is an LLM call returning JSON, and the verdict is the LLM's own answer with its stated confidence. A broken answer goes to review, the fail-safe from Chapter 14.
  - After: Now the comparison. The all-LLM agent runs the same loop, with the same tools and the same policy thresholds. The only difference is who decides. Every decision is an LLM call returning JSON, and the verdict is the LLM's own answer with its stated confidence. A broken answer goes to review, the fail-safe from Chapter 14.
- `chapters/ch17.qmd`
  - Before: The hybrid's decisions are thin slivers; the all-LLM agent's decisions are most of its time.]
  - After: The hybrid's decisions are very thin bars; the all-LLM agent's decisions take most of its time.]
- `chapters/ch17.qmd`
  - Before: @fig-trace shows the difference on a single alert, and it's mostly the width of the green bars. Across the sample, the hybrid took {{< num ch24 v2_seconds f1 >}} seconds per alert and the all-LLM agent {{< num ch24 llm_seconds f1 >}}, about {{< num ch24 speedup int >}} times as long.
  - After: @fig-trace shows the difference on a single alert, and it's mostly the width of the green bars. Across the sample, the hybrid took {{< num ch24 v2_seconds f1 >}} seconds per alert. The all-LLM agent took {{< num ch24 llm_seconds f1 >}}, about {{< num ch24 speedup int >}} times as long.
- `chapters/ch17.qmd`
  - Before: The bigger difference is the review queue (@fig-compare-17). The all-LLM agent sent about {{< num ch24 llm_reviews_day int >}} alerts a day to review, against a capacity of 240. You've seen why in Chapter 13: its stated confidences cluster at a few round values, so a line at 0.03 has almost nothing to separate. Most alerts land between the lines. The hybrid sent {{< num ch24 v2_reviews_day int >}}.
  - After: The bigger difference is the review queue (@fig-compare-17). The all-LLM agent sent about {{< num ch24 llm_reviews_day int >}} alerts a day to review, against a capacity of 240. You saw why in Chapter 13. Its stated confidences are grouped at a few round values, so a threshold at 0.03 has almost nothing to separate. Most alerts land between the thresholds. The hybrid sent {{< num ch24 v2_reviews_day int >}}.
- `chapters/ch17.qmd`
  - Before: A queue more than twice its capacity doesn't get worked twice as hard. The overflow simply isn't looked at, as Chapter 14 put it, in some order nobody chose. Counting both routes to a missed threat, auto-closed or never reached in the queue, the hybrid let about {{< num ch24 v2_missed_day int >}} real threats a day go unseen by a person. The all-LLM agent let about {{< num ch24 llm_missed_day int >}} through.
  - After: A queue with more than twice its capacity doesn't get worked twice as hard. As Chapter 14 said, the extra alerts simply aren't looked at, and nobody chooses which ones. A threat can be missed in two ways: auto-closed, or never reached in the queue. Counting both, the hybrid let about {{< num ch24 v2_missed_day int >}} real threats a day go unseen by a person. The all-LLM agent let about {{< num ch24 llm_missed_day int >}} through.
- `chapters/ch17.qmd`
  - Before: The simulated bill points the same way: about \${{< num ch24 hybrid_cost_1000 f2 >}} per thousand alerts for the hybrid, most of it the LLM writing case notes, against \${{< num ch24 llm_cost_1000 f2 >}} for the all-LLM agent.
  - After: The simulated cost shows the same thing. It's about \${{< num ch24 hybrid_cost_1000 f2 >}} per thousand alerts for the hybrid, mostly for the LLM writing case notes. For the all-LLM agent it's \${{< num ch24 llm_cost_1000 f2 >}}.
- `chapters/ch17.qmd`
  - Before: @fig-labour is the chart I find most telling. In the all-LLM agent, most of the time goes on deciding. In the hybrid, the largest share is *writing*: case notes for analysts and messages for on-call. The LLM's time belongs there. A person will read those words, and fluent, specific writing is what LLMs do best.
  - After: @fig-labour is the chart I find most revealing. In the all-LLM agent, most of the time goes on deciding. In the hybrid, the largest share is *writing*: case notes for analysts and messages for the analyst on call. That's where the LLM's time should go. A person will read those words, and fluent, specific writing is what LLMs do best.
- `chapters/ch17.qmd`
  - Before: Everything here is synthetic: the mock decides, the mock LLM writes, and the timings are simulated. The accuracy gap between the two agents is partly built into the mocks (Chapter 13 explained how), so treat the speed, the queue and the design lessons as the findings, not the verdict quality. The all-LLM agent used the hybrid's policy lines; you could retune them for its clumped confidences, but there are only a few values to put a line between. And the bug in this chapter shows that a hybrid agent has its own failure mode: a decision step that's wrong without any error. Monitoring each step's answers isn't optional.
  - After: Everything here is synthetic: the mock decides, the mock LLM writes, and the timings are simulated. The accuracy gap between the two agents is partly built into the mocks (Chapter 13 explained how). So treat the speed, the queue and the design lessons as the findings, not the quality of the verdicts. The all-LLM agent used the hybrid's policy thresholds. You could adjust them for its grouped confidences, but there are only a few values to put a threshold between. And the bug in this chapter shows that a hybrid agent has its own way to fail: a decision step that's wrong without any error. Watching each step's answers isn't optional.
- `chapters/ch17.qmd`
  - Before: The hybrid agent's "which evidence next?" step can choose "none" to stop gathering. Each extra lookup costs about 0.4 seconds and nothing else. Stopping too early, as the first version showed, can cost a missed threat. If you had to set a rule for when the agent may stop, what would it be, and would you let a probability decide it?
  - After: The hybrid agent's "which evidence next?" step can choose "none" to stop collecting evidence. Each extra lookup costs about 0.4 seconds and nothing else. Stopping too early, as the first version showed, can cost a missed threat. If you had to set a rule for when the agent may stop, what would it be? Would you let a probability decide it?
- `chapters/ch17.qmd`
  - Before: (One reasonable rule: never stop before the lookups that are cheap and always informative, like threat intel, and let the model decide only among the costly ones. Then check the rule the same way as any other decision: count how often "none" is chosen, and look at what it cost on the alerts where it was.)
  - After: (One reasonable rule: never stop before the lookups that are cheap and always useful, like threat intel. Let the model decide only among the costly ones. Then check the rule like any other decision. Count how often "none" is chosen, and look at what it cost on the alerts where it was chosen.)
- `chapters/ch17.qmd`
  - Before: Knuth was warning programmers against tuning code before measuring it [@knuth1974]. The first version of this agent optimised the wrong thing: it made "should we look this up?" a clever decision, when simply looking was cheaper. Measure first, then decide what's worth deciding.
  - After: Knuth was warning programmers not to tune code before measuring it [@knuth1974]. The first version of this agent optimised the wrong thing. It made "should we look this up?" a clever decision, when simply looking was cheaper. Measure first, then decide what's worth deciding.
- `chapters/ch17.qmd`
  - Before: We rebuilt Chapter 7's agent as a hybrid. Jev answered every decision and the LLM wrote only for people. Counting one step's answers exposed a bug that had never crashed: the agent never looked up threat intel. The fix was to stop deciding something that was cheaper to just do. Against an all-LLM twin, the hybrid was several times faster. It kept its review queue inside capacity and let fewer real threats go unseen. Most of its LLM time went on the one job that needed an LLM: writing words a person would read.
  - After: We rebuilt Chapter 7's agent as a hybrid. Jev answered every decision and the LLM wrote only for people. Counting one step's answers showed a bug that had never caused a crash: the agent never looked up threat intel. The fix was to stop deciding something that was cheaper to just do. Against the same agent with the LLM doing everything, the hybrid was several times faster. It kept its review queue within capacity and let fewer real threats go unseen. Most of its LLM time went on the one job that needed an LLM: writing words a person would read.
- `chapters/ch17.qmd`
  - Before: 1. In the lab, count the answers of the "enough evidence?" step. Is its distribution healthy? What would you expect it to look like?
  - After: 1. In the lab, count the answers of the "enough evidence?" step. Does the mix of answers look healthy? What would you expect it to look like?
- `chapters/ch17.qmd`
  - Before: 2. Add a fourth evidence tool to the agent (say, "check the user's recent password resets"). Which of the rules in this chapter decide whether it should be a decision or an unconditional step?
  - After: 2. Add a fourth evidence tool to the agent (say, "check the user's recent password resets"). Which of the rules in this chapter decide whether it should be a decision or a step that always runs?
- `chapters/ch17.qmd`
  - Before: 3. Retune the all-LLM agent's lines so its review queue fits in 240 a day. What happens to the threats it auto-closes?
  - After: 3. Adjust the all-LLM agent's thresholds so its review queue fits in 240 a day. What happens to the threats it auto-closes?

## Chapter 18: Case study

32 changes.

- `chapters/ch18.qmd`
  - Before: Every chapter so far has taken one piece of Kestrel's problem and looked at it closely. Calibration here, a threshold there, an agent, a pattern.
  - After: Every chapter so far has taken one piece of Kestrel's problem and looked at it closely: calibration here, a threshold there, an agent, a pattern.
- `chapters/ch18.qmd`
  - Before: This chapter puts the pieces back together and runs it end to end, the way a real team would. We'll meet the SOC as it was before any of this. We'll design the new system and run it in silence for a week before trusting it. Then we'll switch it on, and in the week after, a phishing campaign arrives.
  - After: This chapter puts the pieces back together and runs the whole thing from start to finish, the way a real team would. We'll see the SOC as it was before any of this. We'll design the new system and run it quietly for a week, without letting it act, before trusting it. Then we'll switch it on, and in the week after, a phishing campaign arrives.
- `chapters/ch18.qmd`
  - Before: - Assemble the system from the book's pieces, and name which chapter each piece comes from.
  - After: - Build the system from the book's pieces, and name which chapter each piece comes from.
- `chapters/ch18.qmd`
  - Before: - Handle a campaign that breaks the base rate, with monitoring, recalibration and overtime.
  - After: - Handle a campaign that changes the base rate, with monitoring, recalibration and overtime.
- `chapters/ch18.qmd`
  - Before: Before this project, every alert joined one queue. The alerts that the senior analyst's rules flagged went to the front; everything else was first come, first served. Whatever nobody reached within a day aged out and was closed without anyone looking.
  - After: Before this project, every alert joined one queue. The alerts that the senior analyst's rules flagged went to the front. Everything else was handled in the order it arrived. Any alert nobody reached within a day "aged out": it was closed without anyone looking.
- `chapters/ch18.qmd`
  - Before: That's a very ordinary way to run a SOC, and it hides its failures in a particular way: nobody ever sees the alerts that age out, so nobody knows how many of them were real.
  - After: That's a very ordinary way to run a SOC, and it hides its failures. Nobody ever sees the alerts that age out, so nobody knows how many of them were real.
- `chapters/ch18.qmd`
  - Before: The left half of @fig-routes looks similar before and after: most alerts get closed without a person either way. The right half is the difference. Before, alerts were closed by *running out of time*, with no regard for which ones mattered. After, they're closed by a *decision*, and the real threats mostly end up in front of a person.
  - After: The left half of @fig-routes looks similar before and after: most alerts get closed without a person either way. The right half shows the difference. Before, alerts were closed because time *ran out*, whether or not they mattered. After, they're closed by a *decision*, and the real threats mostly reach a person.
- `chapters/ch18.qmd`
  - Before: There's nothing in @fig-system you haven't built. The alert's fields go to Jev as three typed questions (Chapter 10). Platt scaling, fitted on three weeks of history, makes the probabilities trustworthy at Kestrel (Chapters 3 and 11). The three-zone policy, with its lines set by cost and capacity, routes each alert (Chapter 14). The LLM writes the case note for the queue and the message for the page, and nothing else (Chapters 15 and 17). And every decision is logged with its inputs, answers and policy version.
  - After: There's nothing in @fig-system you haven't built. The alert's fields go to Jev as three typed questions (Chapter 10). Platt scaling, fitted on three weeks of history, makes the probabilities calibrated at Kestrel (Chapters 3 and 11). The three-zone policy, with its thresholds set by cost and capacity, routes each alert (Chapter 14). The LLM writes the case note for the queue and the urgent message for the analyst on call, and nothing else (Chapters 15 and 17). And every decision is logged with its inputs, answers and policy version.
- `chapters/ch18.qmd`
  - Before: ## A week in the shadows
  - After: ## A week in shadow mode
- `chapters/ch18.qmd`
  - Before: You don't switch a system like this on and hope. You run it in **shadow mode**: it sees every alert and records what it *would* have done, while the analysts carry on as before. Nothing it decides touches anything.
  - After: You don't just switch a system like this on and hope. You run it in **shadow mode**. It sees every alert and records what it *would* have done, while the analysts work as before. Nothing it decides has any effect.
- `chapters/ch18.qmd`
  - Before: The meeting after a shadow week is mostly about one cell, the red one in @fig-shadow-18: about {{< num ch25 new_threats_closed_per_day f1 >}} real threats a day that the system would have auto-closed. That sounds bad until you compare it with the old queue, which let {{< num ch25 old.threats_unseen_per_day f1 >}} a day age out.
  - After: The meeting after a shadow week is mostly about one cell, the red one in @fig-shadow-18. It shows about {{< num ch25 new_threats_closed_per_day f1 >}} real threats a day that the system would have auto-closed. That sounds bad, until you compare it with the old queue, which let {{< num ch25 old.threats_unseen_per_day f1 >}} a day age out.
- `chapters/ch18.qmd`
  - Before: It's also more than forecast. Before the week began, the same policy on the three history weeks auto-closed about {{< num ch25 forecast_closed_hist f1 >}} real threats a day, and the calibrated probabilities themselves added up to about {{< num ch25 forecast_closed_expected f1 >}}. The live week came in higher, in line with it being a busier week than the ones the lines were fitted on. Say it out loud in the meeting: the forecast was in the right range but optimistic, and the daily monitor is what tells you whether the gap is noise or a trend.
  - After: It's also more than the forecast. Before the week began, the same policy on the three history weeks auto-closed about {{< num ch25 forecast_closed_hist f1 >}} real threats a day. And the calibrated probabilities themselves added up to about {{< num ch25 forecast_closed_expected f1 >}}. The live week was higher, which fits with it being busier than the weeks the thresholds were fitted on. Say this clearly in the meeting: the forecast was in the right range but too hopeful. The daily monitor will tell you whether the gap is chance or a trend.
- `chapters/ch18.qmd`
  - Before: The team's decision was to switch it on, with two conditions from Chapter 14: a random audit of 3% of auto-closed alerts, and a fail-safe that sends an alert to review whenever a call fails.
  - After: The team decided to switch it on, with two conditions from Chapter 14: a random audit of 3% of auto-closed alerts, and a fail-safe that sends an alert to review whenever a call fails.
- `chapters/ch18.qmd`
  - Before: The new review queue is sorted by probability: the alerts most likely to be real are looked at first. What if we'd kept the old habit of first come, first served, with the same alerts in the same queue?
  - After: The new review queue is sorted by probability: the alerts most likely to be real are looked at first. What if we had kept the old habit of handling alerts in the order they arrived, with the same alerts in the same queue?
- `chapters/ch18.qmd`
  - Before: The median real threat in the review queue would wait about {{< num ch25 fifo_wait int >}} minutes. Sorted by probability, it waits about {{< num ch25 prio_wait int >}}.
  - After: The typical (median) real threat in the review queue would wait about {{< num ch25 fifo_wait int >}} minutes. Sorted by probability, it waits about {{< num ch25 prio_wait int >}}.
- `chapters/ch18.qmd`
  - Before: ![How long it takes for a real threat to reach a person. Before, rule-flagged threats were seen quickly and the rest waited up to a day or were never seen. After, pages reach someone in about fifteen minutes and the queue takes the likeliest threats first.]
  - After: ![How long it takes for a real threat to reach a person. Before, rule-flagged threats were seen quickly and the rest waited up to a day or were never seen. After, urgent calls reach someone in about fifteen minutes and the queue takes the likeliest threats first.]
- `chapters/ch18.qmd`
  - Before: @fig-time-to-human shows the full distribution. The old way wasn't slow for everything. Rule-flagged threats jumped the queue and were seen within minutes. Its problem was the long flat stretch: threats the rules didn't flag waited behind everything else, and many never got a turn. After the change, {{< num ch25 new.threats_within_hour_share pct >}} of real threats reach a person within an hour, against {{< num ch25 old.threats_within_hour_share pct >}} before.
  - After: @fig-time-to-human shows all the waiting times. The old way wasn't slow for everything. Rule-flagged threats went to the front of the queue and were seen within minutes. Its problem was the long flat part of the curve. Threats the rules didn't flag waited behind everything else, and many were never reached. After the change, {{< num ch25 new.threats_within_hour_share pct >}} of real threats reach a person within an hour, against {{< num ch25 old.threats_within_hour_share pct >}} before.
- `chapters/ch18.qmd`
  - Before: Link alerts fired three times as often as usual, and far more of them were real. Chapter 14 used this same week to show how drift looks on a monitoring dashboard. @fig-campaign shows what it did to the operation.
  - After: Alerts about links fired three times as often as usual, and far more of them were real. Chapter 14 used this same week to show how drift looks on a monitoring chart. @fig-campaign shows what it did to the team's work.
- `chapters/ch18.qmd`
  - Before: On day 1 the review queue was already over capacity. Its worst day reached {{< num ch25 camp_peak_reviews int >}} alerts against {{< num ch25 capacity int >}}, above the week's average of about {{< num ch21 campaign_reviews_per_day int >}} that Chapter 14 reported. And the probabilities were now too low for link alerts, because they'd been calibrated on weeks when those alerts were mostly harmless. The monitoring from Chapter 14 caught both on day 2: the queue was over its line, and the reviewers were confirming far more link alerts than predicted.
  - After: On day 1, the review queue was already over capacity. Its worst day reached {{< num ch25 camp_peak_reviews int >}} alerts against {{< num ch25 capacity int >}}, above the week's average of about {{< num ch21 campaign_reviews_per_day int >}} that Chapter 14 reported. And the probabilities were now too low for link alerts. They'd been calibrated on weeks when those alerts were mostly harmless. The monitoring from Chapter 14 caught both problems on day 2. The queue was over its limit, and the reviewers were confirming far more link alerts than predicted.
- `chapters/ch18.qmd`
  - Before: On day 3 the team responded in two ways. They re-estimated the base rate for link alerts from what reviewers had confirmed so far, and adjusted those probabilities with the prior-shift correction from Chapter 11. And they approved overtime: two extra analysts' worth of reviews a day.
  - After: On day 3, the team responded in two ways. They estimated the base rate for link alerts again, from what reviewers had confirmed so far. Then they adjusted those probabilities with the base-rate correction from Chapter 11. And they approved overtime: two extra analysts' worth of reviews a day.
- `chapters/ch18.qmd`
  - Before: It helped. Over the week, the real threats never seen by a person fell from about {{< num ch25 camp_missed_base int >}} to about {{< num ch25 camp_missed_resp int >}} (@fig-campaign). But look at the left panel: with recalibrated probabilities, the queue grew *past* the overtime capacity. Once the link alerts' probabilities were corrected, far more of them deserved a look than even the enlarged team could give.
  - After: It helped. Over the week, the number of real threats never seen by a person fell from about {{< num ch25 camp_missed_base int >}} to about {{< num ch25 camp_missed_resp int >}} (@fig-campaign). But look at the left panel: with recalibrated probabilities, the queue grew *past* the overtime capacity. Once the link alerts' probabilities were corrected, far more of them deserved a look than even the bigger team could manage.
- `chapters/ch18.qmd`
  - Before: The campaign week's uncomfortable truth: calibration tells you truthfully how much work there is. It can't make the work smaller. When the world gets more dangerous, the decision layer's job is to make that visible early and to spend scarce attention on the likeliest threats. The rest is staffing.
  - After: Here is the uncomfortable truth of the campaign week. Calibration tells you truthfully how much work there is. It can't make the work smaller. When the world gets more dangerous, the decision layer's job is to show that early, and to spend the team's limited time on the likeliest threats. The rest is a question of how many people you have.
- `chapters/ch18.qmd`
  - Before: @fig-scorecard-18 is the summary I'd put in front of Kestrel's leadership. The analysts looked at about the same number of alerts a day. They weren't working harder. They were looking at different alerts, in a different order, and more real threats reached them, sooner.
  - After: @fig-scorecard-18 is the summary I'd show Kestrel's leaders. The analysts looked at about the same number of alerts a day. They weren't working harder. They were looking at different alerts, in a different order, and more real threats reached them, sooner.
- `chapters/ch18.qmd`
  - Before: One line needs a caveat. The *median* wait for a seen threat went up, from about five minutes to fifteen. That's because the old way's seen threats were mostly the rule-flagged ones that jumped the queue, and because I assumed on-call takes fifteen minutes to respond to a page. The fair comparison is the one above it: the share of all real threats seen within an hour more than doubled.
  - After: One row needs a warning. The typical (median) wait for a threat that was seen went up, from about five minutes to fifteen. There are two reasons. Under the old way, the threats that were seen were mostly the rule-flagged ones at the front of the queue. And I assumed the analyst on call takes fifteen minutes to respond to an urgent call. The fair comparison is the row above it: the share of all real threats seen within an hour more than doubled.
- `chapters/ch18.qmd`
  - Before: This whole case study is a simulation on synthetic alerts, with mock Jev and made-up costs, capacities and response times, so treat every number as an illustration of the method. Real SOCs differ in ways it leaves out: analysts aren't interchangeable, alerts arrive in bursts, and some real threats are caught later by other defences. Shadow mode is only as good as the labels you compare against, and labels for alerts nobody reviewed are precisely the ones you don't have; that's why the random audit matters. And the campaign response used labels from the first two days, which means the system was wrong for two days before anyone could fix it.
  - After: This whole case study is a simulation on synthetic alerts, with mock Jev and made-up costs, capacities and response times. So treat every number as an example of the method. Real SOCs differ in ways it leaves out. Analysts aren't all the same, alerts arrive in bursts, and some real threats are caught later by other defences. Shadow mode is only as good as the labels you compare against. And the labels you don't have are exactly those for alerts nobody reviewed. That's why the random audit matters. And the campaign response used labels from the first two days. So the system was wrong for two days before anyone could fix it.
- `chapters/ch18.qmd`
  - Before: During the campaign, Kestrel can afford overtime for two more analysts, or it can tell the policy to auto-close more link alerts to keep the queue at capacity. A missed threat costs about \$10,000; an analyst-day of overtime costs about \$600. The corrected probabilities say the extra reviews would find roughly one real threat for every six alerts. Which would you choose?
  - After: During the campaign, Kestrel can pay overtime for two more analysts. Or it can tell the policy to auto-close more link alerts, to keep the queue at capacity. A missed threat costs about \$10,000; one analyst's day of overtime costs about \$600. The corrected probabilities say the extra reviews would find about one real threat for every six alerts. Which would you choose?
- `chapters/ch18.qmd`
  - Before: (Each extra analyst clears about 40 alerts a day, which at one threat in six finds about 6 or 7 real threats worth around \$65,000. Roughly a hundred times the cost of the overtime. Staff up, and keep the lines honest: shrinking the queue by closing likely threats just moves the cost to where nobody sees it.)
  - After: (Each extra analyst clears about 40 alerts a day. At one threat in six, that finds about 6 or 7 real threats, worth around \$65,000. That's about a hundred times the cost of the overtime. Add the people, and keep the thresholds where the costs put them. Making the queue shorter by closing likely threats just moves the cost to where nobody sees it.)
- `chapters/ch18.qmd`
  - Before: Deming said something like this often, in talks and seminars. Kestrel's analysts were never the problem. The old queue decided what they saw by accident. The new one decides on purpose.
  - After: Deming often said something like this in talks and seminars. Kestrel's analysts were never the problem. The old queue decided what they saw by accident. The new one decides on purpose.
- `chapters/ch18.qmd`
  - Before: Kestrel's SOC used to decide by running out of time: whatever nobody reached aged out, and a large share of real threats went with it. We assembled the new system from pieces built across the book and ran it in shadow mode. Its mistakes matched its own forecast, so the team switched it on. With the same six analysts, more real threats reached a person, and they got there faster. The cheapest part of that gain came from putting the likeliest threats first. Then a phishing campaign arrived. Recalibration and overtime reduced the damage, and they also showed plainly how much more work the world had created.
  - After: Kestrel's SOC used to decide by running out of time. Whatever nobody reached aged out, and a large share of real threats went with it. We built the new system from pieces made across the book and ran it in shadow mode. Its mistakes were close to its own forecast, though a little higher, so the team switched it on. With the same six analysts, more real threats reached a person, and they got there faster. The cheapest part of that gain came from putting the likeliest threats first. Then a phishing campaign arrived. Recalibration and overtime reduced the damage. They also showed clearly how much more work the campaign had created.
- `chapters/ch18.qmd`
  - Before: 2. Rerun the campaign with a response on day 2 instead of day 3. How many more threats reach a person? What would you need in place to respond a day earlier?
  - After: 2. Run the campaign again with a response on day 2 instead of day 3. How many more threats reach a person? What would you need to have ready to respond a day earlier?
- `chapters/ch18.qmd`
  - Before: 3. The old way sorted rule-flagged alerts first. What if it had sorted by the SIEM's own severity field instead? Sketch how you'd test whether that alone closes most of the gap.
  - After: 3. The old way put rule-flagged alerts first. What if it had sorted by the SIEM's own severity field instead? Describe how you'd test whether that alone closes most of the gap.
- `chapters/ch18.qmd`
  - Before: Next: the same decision layer, a long way from a SOC. An applications gallery, from support tickets to clinical triage, with the questions each one would ask.
  - After: Next: the same decision layer, far away from a SOC. A tour of other uses, from support tickets to hospital triage, with the questions each one would ask.

## Chapter 20: Build your own System One model

32 changes.

- `chapters/ch20.qmd`
  - Before: For nineteen chapters you've been calling a System One model from the outside. You've sent it states and typed questions, read its probabilities, tested them and drawn lines on them.
  - After: For nineteen chapters, you've been calling a System One model from the outside. You've sent it states and typed questions, read its probabilities, tested them and put thresholds on them.
- `chapters/ch20.qmd`
  - Before: Their model, yes. Ours will be tiny, about two thousand numbers, and it will only know about Kestrel's alerts. But it will have the same *shape*: one pass, three kinds of typed answer, and probabilities trained to be honest. Building it is the best way I know to understand why each part of that shape is there. And at the end, you'll plug it into the official SDK and run the book's own code against it.
  - After: Their model, yes. Ours will be tiny, about two thousand numbers, and it will only know about Kestrel's alerts. But it will have the same *shape*: one pass, three kinds of typed answer, and probabilities trained to be calibrated. Building it is the best way I know to understand why each part of that shape is there. And at the end, you'll connect it to the official SDK and run the book's own code against it.
- `chapters/ch20.qmd`
  - Before: You already have every piece. Chapter 5 built networks and embeddings, Chapter 2 log loss and Chapter 3 temperature scaling. This chapter snaps them together.
  - After: You already have every piece. Chapter 5 built networks and embeddings, Chapter 2 built log loss, and Chapter 3 built temperature scaling. This chapter puts them together.
- `chapters/ch20.qmd`
  - Before: - Build a shared encoder that reads an alert's fields in one pass.
  - After: - Build a shared **encoder**: the part of the network that reads an alert's fields in one pass.
- `chapters/ch20.qmd`
  - Before: - Train all three at once with log loss, and see why that rewards honest probabilities.
  - After: - Train all three at once with log loss, and see why that rewards calibrated probabilities.
- `chapters/ch20.qmd`
  - Before: - Catch the overconfidence training still leaves, and fix it with one temperature per head.
  - After: - Find the overconfidence that training still leaves, and fix it with one temperature per head.
- `chapters/ch20.qmd`
  - Before: - Plug your model into the official SDK so the book's code runs against it unchanged.
  - After: - Connect your model to the official SDK so the book's code runs against it unchanged.
- `chapters/ch20.qmd`
  - Before: Start from the interface. A request carries a state and some typed questions. The response carries a probability for every option. Chapter 9 guessed at a design that fits that shape, and here it is, small enough to hold in your head.
  - After: Start from the interface. A request contains a state and some typed questions. The response contains a probability for every option. Chapter 9 guessed at a design that fits that shape. Here it is, small enough to keep in your head.
- `chapters/ch20.qmd`
  - Before: The **encoder** reads the alert once and produces a summary of 32 numbers (@fig-architecture-20). The rule name, like `impossible_travel`, isn't a number, so it gets an embedding, just as words did in Chapter 5. The **heads** each read the same summary and answer one kind of question.
  - After: The encoder reads the alert once and produces a summary of 32 numbers (@fig-architecture-20). The rule name, like `impossible_travel`, isn't a number, so it gets an embedding, just as words did in Chapter 5. The **heads** are small parts at the end of the network. Each one reads the same summary and answers one kind of question.
- `chapters/ch20.qmd`
  - Before: That sharing is the point. The encoder learns what matters about an alert *in general*, and every head benefits. Learning which category a threat belongs to teaches the encoder things that help decide whether it's a threat at all.
  - After: That sharing is the point. The encoder learns what matters about an alert *in general*, and every head benefits. Learning which category a threat belongs to teaches the encoder things that also help decide whether it's a threat at all.
- `chapters/ch20.qmd`
  - Before: ![The three heads. A noul turns one number into P(yes) with the S-curve. A choice turns one number per label into probabilities that add up to 1. A score turns one number into probabilities for ordered levels by cutting it at points that must stay in order.]
  - After: ![The three heads. A noul turns one number into P(yes) with the S-curve. A choice turns one number per label into probabilities that add up to 1. A score turns one number into probabilities for levels in order, by cutting it at points that must stay in order.]
- `chapters/ch20.qmd`
  - Before: The **noul head** is logistic regression sitting on top of the encoder: one number, through the S-curve from Chapter 2, gives P(attack).
  - After: The **noul head** is logistic regression on top of the encoder: one number, through the S-curve from Chapter 2, gives P(attack).
- `chapters/ch20.qmd`
  - Before: The **score head** is the interesting one. Severity levels have an order: "high" is more than "medium", which is more than "low". A softmax would throw that order away and treat the levels like unrelated labels. So the score head makes *one* number, a sort of severity dial, and cuts it at three points that are forced to stay in order (@fig-heads, right). The probability of each level is the share of the dial between its cut points. Statisticians call this an **ordinal** model.
  - After: The **score head** is the interesting one. Severity levels have an order: "high" is more than "medium", which is more than "low". A softmax would ignore that order and treat the levels like unrelated labels. So the score head makes *one* number, like a severity dial. It cuts the dial at three points that must stay in order (@fig-heads, right). The probability of each level is the share of the dial between its cut points. Statisticians call this an **ordinal** model: a model for values that come in order.
- `chapters/ch20.qmd`
  - Before: That design has a limitation worth knowing. One dial can move a single hump up and down the scale and make it wider or narrower, but it can't split an alert between two distant levels while skipping the one in between. Chapter 10's mock Jev gave uncertain alerts that very shape, two humps: "informational if it's harmless, serious if it's real". TinyJev's score head can't express it, and would smear such an alert across the middle levels instead. One more reason to ask "is it real?" as its own noul rather than reading it off the severity.
  - After: That design has a limit worth knowing. One dial can move a single peak up and down the scale, and make it wider or narrower. But it can't split an alert between two distant levels while skipping the one in between. Chapter 10's mock Jev gave uncertain alerts exactly that shape, with two peaks: "informational if it's harmless, serious if it's real". TinyJev's score head can't express that. It would spread such an alert across the middle levels instead. That's one more reason to ask "is it real?" as its own noul, rather than reading it from the severity.
- `chapters/ch20.qmd`
  - Before: Untrained, those numbers are noise. Training is what gives them meaning.
  - After: Before training, those numbers are random. Training is what gives them meaning.
- `chapters/ch20.qmd`
  - Before: We train all three heads at once, on two weeks of Kestrel's labelled alerts, by adding their log losses together and running gradient descent, as in Chapter 2.
  - After: We train all three heads at once, on two weeks of Kestrel's labelled alerts. We add their log losses together and run gradient descent, as in Chapter 2.
- `chapters/ch20.qmd`
  - Before: Log loss matters here for a reason Chapter 2 made precise. It's a **proper scoring rule**: the way to get the best average score is to report your honest probability, not to exaggerate. Training with log loss rewards calibration directly, and it does so for every head. A rule like this is the most likely way a model like Jev is trained to be calibrated, and in Chapter 9 I guessed that TypeSafe's RLCD might build on a rule like it.
  - After: Log loss matters here for a reason Chapter 2 explained. It's a **proper scoring rule**: the way to get the best average score is to report your honest probability, not to exaggerate. So training with log loss rewards calibration directly, for every head. A rule like this is the most likely way a model like Jev is trained to be calibrated. In Chapter 9, I guessed that TypeSafe's RLCD might build on a rule like it.
- `chapters/ch20.qmd`
  - Before: Right: a bigger network trained four times as long with no penalty on large weights. It keeps improving on the weeks it has seen and gets steadily worse on the week it hasn't.]
  - After: Right: a bigger network trained four times as long, with no penalty on large weights. It keeps improving on the weeks it has seen, and keeps getting worse on the week it hasn't.]
- `chapters/ch20.qmd`
  - Before: The left panel of @fig-curves is what healthy training looks like: both curves fall, then flatten, with a small gap between them. The right panel is what happens if you make the network bigger, take away the small penalty on large weights and let it run. It memorises the training weeks. Its loss there falls to {{< num ch27 over_train_noul f3 >}}, while on the week it hasn't seen, loss climbs to {{< num ch27 over_val_noul f3 >}}. That's Chapter 2's overfitting, and Chapter 5's overconfidence, happening in front of you.
  - After: The left panel of @fig-curves shows healthy training: both curves fall, then become flat, with a small gap between them. The right panel shows what happens if you make the network bigger, remove the small penalty on large weights, and let it run longer. It memorises the training weeks. Its loss there falls to {{< num ch27 over_train_noul f3 >}}, while on the week it hasn't seen, loss rises to {{< num ch27 over_val_noul f3 >}}. That's Chapter 2's overfitting and Chapter 5's overconfidence, happening in front of you.
- `chapters/ch20.qmd`
  - Before: ## Honest, but not quite
  - After: ## Calibrated, but not quite
- `chapters/ch20.qmd`
  - Before: The fix is Chapter 3's: hold back a week, and fit one number per head, a **temperature**, that softens its answers until they match what happened. The temperatures came out at about {{< num ch27 T_noul f2 >}} for the noul, {{< num ch27 T_choice f2 >}} for the choice and {{< num ch27 T_score f2 >}} for the score. All three above 1: all three a bit overconfident.
  - After: The fix is Chapter 3's. Keep back a week, and fit one number per head, a **temperature**, that softens its answers until they match what happened. The temperatures came out at about {{< num ch27 T_noul f2 >}} for the noul, {{< num ch27 T_choice f2 >}} for the choice and {{< num ch27 T_score f2 >}} for the score. All three are above 1, so all three heads were a bit overconfident.
- `chapters/ch20.qmd`
  - Before: The overtrained network is the cautionary tale. As trained, its calibration error on the live week was {{< num ch27 over_ece f3 >}} (the right-hand panel). Its fitted temperature was {{< num ch27 T_over f1 >}}, a huge correction, and afterwards the error was {{< num ch27 over_ece_temp f3 >}}: no better at all. A temperature can soften an answer. It can't put back what the model forgot about the world while it was memorising.
  - After: The overtrained network is the warning. As trained, its calibration error on the live week was {{< num ch27 over_ece f3 >}} (the right-hand panel). Its fitted temperature was {{< num ch27 T_over f1 >}}, a huge correction. Afterwards, the error was {{< num ch27 over_ece_temp f3 >}}: no better at all. A temperature can soften an answer. It can't put back what the model lost about the world while it was memorising.
- `chapters/ch20.qmd`
  - Before: ![TinyJev against the book's other models on the live week. It ranks a little worse than logistic regression trained on three weeks of labels and a little worse than mock Jev, and it's as well calibrated as either. The overtrained network is worse at both.]
  - After: ![TinyJev against the book's other models on the live week. It ranks a little worse than logistic regression trained on three weeks of labels, and a little worse than mock Jev. It's as well calibrated as either. The overtrained network is worse at both.]
- `chapters/ch20.qmd`
  - Before: Respectable, not magic. It trained on two weeks rather than three, and a two-layer network has no advantage over logistic regression on a problem that's nearly linear in its inputs, which Chapter 13 found this one is. Where a model like this earns its keep is when there are many questions to answer about the same state, so that one encoder is shared across all of them.
  - After: That's good, but not magic. It trained on two weeks rather than three. And a two-layer network has no advantage over logistic regression on a problem that depends on its inputs in a nearly straight-line way, as Chapter 13 found this one does. A model like this is most worth building when there are many questions to answer about the same state, so that one encoder is shared across all of them.
- `chapters/ch20.qmd`
  - Before: ## Plug it in
  - After: ## Connect it to the SDK
- `chapters/ch20.qmd`
  - Before: The response comes back in just the shape the SDK expects, with the model name `tinyjev-your-own` (@fig-plugin). Point any lab in the book at this transport and it runs against the model you just trained: the bake-off, the three zones, the hybrid agent. Now you have two decision models behind the same interface, and you can test one against the other with everything Part IV taught you.
  - After: The response comes back in exactly the shape the SDK expects, with the model name `tinyjev-your-own` (@fig-plugin). Point any lab in the book at this transport, and it runs against the model you just trained: the bake-off, the three zones, the hybrid agent. Now you have two decision models behind the same interface. You can test one against the other with everything Part IV taught you.
- `chapters/ch20.qmd`
  - Before: TinyJev reads structured fields, not free text; a real System One model reads text and JSON of any shape, which needs an attention-based reader like Chapter 5's, and far more data. It knows one company's alerts from two weeks, so it will drift the moment the world does, as Chapter 18's campaign showed. Its temperatures were fitted on one week, which is a small sample, and Chapter 11 showed how noisy calibration measurements are with few labels. And nothing here tells you how Jev is actually built; this is a design the interface suggests, built to understand the interface, not a copy of anything.
  - After: TinyJev reads structured fields, not free text. A real System One model reads text and JSON of any shape. That needs a reader built on attention, like Chapter 5's, and far more data. TinyJev knows one company's alerts from two weeks, so it will drift as soon as the world changes, as Chapter 18's campaign showed. Its temperatures were fitted on one week, which is a small sample. Chapter 11 showed how unreliable calibration measurements are with few labels. And nothing here tells you how Jev is actually built. This is a design that the interface suggests, built to understand the interface, not a copy of anything.
- `chapters/ch20.qmd`
  - Before: Your TinyJev feeds Kestrel's three-zone policy. After two weeks in production, the weekly calibration check shows the noul head's temperature has drifted from 1.2 to 1.6. What does that tell you, and what would you do before touching the policy's lines?
  - After: Your TinyJev feeds Kestrel's three-zone policy. After two weeks of real use, the weekly calibration check shows the noul head's temperature has moved from 1.2 to 1.6. What does that tell you? What would you do before changing the policy's thresholds?
- `chapters/ch20.qmd`
  - Before: (A higher temperature means the model has become more overconfident on current data: the world has moved away from its training weeks. Before moving any line, refit the temperature on recent labelled alerts and check calibration again. If the temperature keeps climbing week after week, retrain the model on recent data; the lines were set for calibrated probabilities, and that's what needs restoring.)
  - After: (A higher temperature means the model has become more overconfident on current data: the world has moved away from its training weeks. Before moving any threshold, refit the temperature on recent labelled alerts and check calibration again. If the temperature keeps rising week after week, retrain the model on recent data. The thresholds were set for calibrated probabilities, and that's what needs fixing.)
- `chapters/ch20.qmd`
  - Before: Feynman's blackboard is the best argument for this chapter. You don't need to build a System One model to use one. But having built a small one, you know what its probabilities are made of, why they drift and how to fix them.
  - After: Feynman's words are the best argument for this chapter. You don't need to build a System One model to use one. But having built a small one, you know what its probabilities are made of, why they drift and how to fix them.
- `chapters/ch20.qmd`
  - Before: We built a System One model in miniature. A shared encoder read each alert once, and three heads answered three typed questions: a sigmoid for the noul, a softmax for the choice, and an ordinal dial for the score. Log loss trained every head towards honest probabilities. Calibrated on the training weeks still meant overconfident on new ones, and one temperature per head fixed that. Training too long broke it in a way no temperature could repair. The model ranked alerts respectably, and once plugged into the official SDK, it ran the book's code unchanged.
  - After: We built a small System One model. A shared encoder read each alert once, and three heads answered three typed questions: a sigmoid for the noul, a softmax for the choice, and an ordinal dial for the score. Log loss trained every head towards calibrated probabilities. But calibrated on the training weeks still meant overconfident on new ones, and one temperature per head fixed that. Training too long broke it in a way no temperature could repair. The model ranked alerts well, and once connected to the official SDK, it ran the book's code unchanged.
- `chapters/ch20.qmd`
  - Before: 4. Point Chapter 14's lab at `TinyJevTransport`. Do the policy's lines need to move? Why?
  - After: 4. Point Chapter 14's lab at `TinyJevTransport`. Do the policy's thresholds need to move? Why?

## Chapter 22: What changes now

21 changes.

- `chapters/ch22.qmd`
  - Before: You've learned quite a lot of it since. Probability and calibration, neural networks, embeddings, attention, LLMs, agents. Then a new kind of model, and everything it takes to use one well. This last chapter is shorter. It steps back and asks what all of that adds up to, for the industry and for you.
  - After: You've learned quite a lot of it since: probability and calibration, neural networks, embeddings, attention, LLMs and agents. Then a new kind of model, and everything it takes to use one well. This last chapter is shorter. It steps back and asks what all of that means, for the industry and for you.
- `chapters/ch22.qmd`
  - Before: I'll try to be careful here. It's easy to end a book like this with predictions, and most predictions about AI age badly. So I'll stick to three things: what the book showed, what it suggests, and what nobody knows yet.
  - After: I'll try to be careful here. It's easy to end a book like this with predictions, and most predictions about AI soon turn out wrong. So I'll keep to three things: what the book showed, what it suggests, and what nobody knows yet.
- `chapters/ch22.qmd`
  - Before: - Keep an honest list of what isn't known yet.
  - After: - Keep a clear list of what isn't known yet.
- `chapters/ch22.qmd`
  - Before: The right-hand side of @fig-stack is the shape this book kept arriving at, chapter after chapter. The LLM does what only an LLM can do: read anything, and write for people. The decision layer answers small typed questions in one pass, with probabilities you can test. The policy draws the lines, from costs and capacity. And underneath, tools act and people review.
  - After: The right-hand side of @fig-stack is the design this book kept reaching, chapter after chapter. The LLM does what only an LLM can do: read anything, and write for people. The decision layer answers small typed questions in one pass, with probabilities you can test. The policy sets the thresholds, from costs and capacity. And underneath, tools act and people review.
- `chapters/ch22.qmd`
  - Before: Each layer is smaller than the system it serves. Each can be tested on its own, with the tools from Part I. And each can be replaced without rebuilding the others: a better LLM, a different decision model, new lines. That, more than any benchmark, is why I think the split will last.
  - After: Each layer is smaller than the system it serves. Each can be tested on its own, with the tools from Part I. And each can be replaced without rebuilding the others: a better LLM, a different decision model, new thresholds. That, more than any benchmark, is why I think this split will last.
- `chapters/ch22.qmd`
  - Before: Take one task, sketched the way Chapter 7 counted Kestrel's agent: a ticket comes in, an agent picks tools, checks whether it has enough, checks whether an action is safe, does it and writes a reply.
  - After: Take one task, described the way Chapter 7 counted Kestrel's agent. A ticket comes in. An agent picks tools, checks whether it has enough, checks whether an action is safe, does it, and writes a reply.
- `chapters/ch22.qmd`
  - Before: With the book's illustrative LLM figures and Jev's vendor-reported ones, the task drops from about {{< num ch29 task_llm_s int >}} seconds to {{< num ch29 task_jev_s int >}}, and the bill falls by about three quarters (@fig-task). What's left is mostly the one step where an LLM writes something a person will read. Chapter 17 measured the same shape on Kestrel's agent, which ran about {{< num ch29 ch24_speedup int >}} times faster as a hybrid.
  - After: With the book's illustrative LLM figures and Jev's vendor-reported ones, the task drops from about {{< num ch29 task_llm_s int >}} seconds to {{< num ch29 task_jev_s int >}}. The cost falls by about three quarters (@fig-task). What's left is mostly the one step where an LLM writes something a person will read. Chapter 17 measured the same pattern on Kestrel's agent, which ran about {{< num ch29 ch24_speedup int >}} times faster as a hybrid.
- `chapters/ch22.qmd`
  - Before: Then Chapter 12's warning applies. When decisions get this cheap, we won't make the same decisions for less. We'll make many more of them: every login checked, every retrieved passage judged, every agent step gated. Most of the change will happen there. It won't come from doing today's work more cheaply. It'll come from the work that becomes worth doing.
  - After: Then Chapter 12's warning applies. When decisions get this cheap, we won't make the same decisions for less. We'll make many more of them: every login checked, every retrieved passage judged, every agent step passed through a gate. Most of the change will happen there. It won't come from doing today's work more cheaply. It'll come from the work that becomes worth doing.
- `chapters/ch22.qmd`
  - Before: Judgement about the decision itself. Someone still has to decide what a mistake costs, where the lines go, how much the review queue can take, and whether the probabilities are still honest this week. The model can't do any of that for you.
  - After: Judgement about the decision itself. Someone still has to decide what a mistake costs, where the thresholds go, how much the review queue can take, and whether the probabilities are still calibrated this week. The model can't do any of that for you.
- `chapters/ch22.qmd`
  - Before: Which is why the book's first part, which may have felt like a long detour, was worth the time. Thinking in probabilities and testing calibration were the foundations, not the preamble (@fig-skills). They're what separates a system that makes a million cheap decisions well from one that makes a million cheap mistakes.
  - After: That's why the book's first part was worth the time, even if it felt like a long way round. Thinking in probabilities and testing calibration were the foundations, not just an introduction (@fig-skills). They're the difference between a system that makes a million cheap decisions well and one that makes a million cheap mistakes.
- `chapters/ch22.qmd`
  - Before: What matters less *on its own* is prompting for everything, and reaching for the biggest model by default. Both still have their place. They're just no longer all of it.
  - After: What matters less *on its own* is writing prompts for everything, and choosing the biggest model by default. Both are still useful. They're just no longer the whole job.
- `chapters/ch22.qmd`
  - Before: I've tried throughout to keep three piles: what's verified, what's vendor-reported and what's unknown. @fig-unknowns is the unknown pile, as it stands.
  - After: Throughout the book, I've tried to keep three piles: what's verified, what's vendor-reported and what's unknown. @fig-unknowns is the unknown pile, as it is today.
- `chapters/ch22.qmd`
  - Before: Every item in @fig-unknowns is open. None of them is a reason to wait. Calibration on your data is a test you can run this week. Drift between versions is a pin and a monitor. Prices are a spreadsheet with a sensitivity column. And the question of who else builds decision models matters less than it seems, because the pattern outlives any vendor. A typed question in, a probability out, and a policy in your own code: you can move that to a different model on a Tuesday afternoon.
  - After: Every item in @fig-unknowns is still open. None of them is a reason to wait. Calibration on your data is a test you can run this week. Changes between versions are handled by a fixed version number and a monitor. Prices are a spreadsheet where you try different values. And it matters less than it seems who else builds decision models, because the pattern will last longer than any one vendor. A typed question in, a probability out, and a policy in your own code: you can move that to a different model in an afternoon.
- `chapters/ch22.qmd`
  - Before: You don't need to predict how this plays out. You need decisions you can measure, lines you can move and a model you can swap.
  - After: You don't need to predict how this turns out. You need decisions you can measure, thresholds you can move and a model you can replace.
- `chapters/ch22.qmd`
  - Before: Then pick *one*. Get a few hundred labels. Test it the way Chapter 11 did. Put prices on its mistakes, draw its lines and run it in shadow. Switch it on with a fail-safe and a monitor. Then do the next one.
  - After: Then pick *one*. Get a few hundred labels. Test it the way Chapter 11 did. Put prices on its mistakes, set its thresholds and run it in shadow mode. Switch it on with a fail-safe and a monitor. Then do the next one.
- `chapters/ch22.qmd`
  - Before: It isn't glamorous. It's how every system in this book got better.
  - After: It isn't exciting. It's how every system in this book got better.
- `chapters/ch22.qmd`
  - Before: This chapter is the most speculative in the book. The cost and speed figures are illustrative, and Jev's are vendor-reported from its early access. The claim that a decision layer will become a standard part of AI systems is my reading of the evidence here, not a finding. It could be wrong if general-purpose models become fast and well calibrated enough that splitting stops paying off. If that happens, the skills in @fig-skills still apply; only the box they live in changes.
  - After: This chapter is the least certain in the book. The cost and speed figures are illustrative, and Jev's are vendor-reported from its early access. The claim that a decision layer will become a standard part of AI systems is my reading of the evidence here, not a finding. It could be wrong if general models become fast enough and well calibrated enough that splitting stops being worth it. If that happens, the skills in @fig-skills still apply; only the box they sit in changes.
- `chapters/ch22.qmd`
  - Before: Your own system: pick the decision in it that happens most often. What does a wrong "yes" cost? A wrong "no"? Where does the line go? And how would you know, a month from now, whether the probabilities behind it are still honest?
  - After: Your own system: pick the decision in it that happens most often. What does a wrong "yes" cost? A wrong "no"? Where does the threshold go? And how would you know, a month from now, whether the probabilities behind it are still calibrated?
- `chapters/ch22.qmd`
  - Before: Read @fig-journey from the top and you have the book in six lines. That's the map, and you know where everything on it is now. What's left is choosing the first decision in your own work that deserves the care.
  - After: Read @fig-journey from the top and you have the book in six lines. That's the map, and you now know where everything on it is. What's left is choosing the first decision in your own work that deserves this care.
- `chapters/ch22.qmd`
  - Before: 4. Write a one-page memo to your team proposing the first decision to move, using the vocabulary of this book: costs, lines, calibration, shadow, fail-safe.
  - After: 4. Write a one-page note to your team suggesting the first decision to move. Use the words of this book: costs, thresholds, calibration, shadow mode, fail-safe.
- `chapters/ch22.qmd`
  - Before: Thank you for reading. The labs, the mock and every figure's code are in the companion repository, waiting for your own data.
  - After: Thank you for reading. The labs, the mock and every figure's code are in the companion repository, ready for your own data.

## Front matter and part openers

37 changes.

- `index.qmd`
  - Before: Not about artificial intelligence in general, though you'll learn a good deal of that along the way. The subject is one narrow, very common job: looking at a situation and choosing what to do about it. Is this email phishing? Which team should get this ticket? Is this login safe? Should this agent call that tool?
  - After: It isn't about artificial intelligence in general, though you'll learn a lot of that along the way. The subject is one narrow, very common job: looking at a situation and choosing what to do about it. Is this email phishing? Which team should get this ticket? Is this login safe? Should this agent call that tool?
- `index.qmd`
  - Before: Software makes millions of those decisions every day, and for the last few years we've been handing more and more of them to large language models. LLMs are extraordinary at reading and writing. But a decision is a different thing from a paragraph: a choice between a few options, made under uncertainty, with a cost for getting it wrong. To make it well you need a probability you can trust and a line drawn from what mistakes cost. And you need to know when to hand the case to a person.
  - After: Software makes millions of those decisions every day. For the last few years, we've been giving more and more of them to large language models. LLMs are extremely good at reading and writing. But a decision is different from a paragraph. It's a choice between a few options, made without being sure, with a cost for getting it wrong. To make it well, you need a calibrated probability, one that means what it says, and a threshold set by what mistakes cost. And you need to know when to give the case to a person.
- `index.qmd`
  - Before: In 2026 a company called TypeSafe AI released Jev, which it describes as the first of a new class of **System One models**: models that don't write at all, only answer typed questions with probabilities, in a single fast pass [@typesafe2026]. Whether Jev lives up to its claims is something you'll learn to test for yourself. But the idea behind it is worth understanding whatever happens to any one product. Some decisions belong in a separate, fast, measurable layer of an AI system, and that layer needs different skills from the rest.
  - After: In 2026, a company called TypeSafe AI released Jev. It describes Jev as the first of a new kind of model, a **System One model**. These models don't write at all. They only answer typed questions with probabilities, in a single fast pass [@typesafe2026]. You'll learn to test for yourself whether Jev does what its makers claim. But the idea behind it is worth understanding whatever happens to any one product. Some decisions belong in a separate, fast, measurable layer of an AI system, and that layer needs different skills from the rest.
- `index.qmd`
  - Before: It's for anyone who builds, buys or runs systems that make decisions. If you're new to machine learning, Part I starts from the beginning and assumes only that you're comfortable with a little arithmetic and a little Python. If you already build with LLMs, you'll move quickly through Part II and find the substance in Parts III to V. If you lead a team, "How to read this book" suggests a shorter route.
  - After: It's for anyone who builds, buys or runs systems that make decisions. If you're new to machine learning, Part I starts from the beginning. It assumes only that you're comfortable with a little arithmetic and a little Python. If you already build with LLMs, you'll move quickly through Part II and find the main content in Parts III to V. If you lead a team, "How to read this book" suggests a shorter route.
- `index.qmd`
  - Before: Every chapter follows one fictional company, Kestrel Logistics, and its security operations centre, where a small team triages hundreds of alerts a day. SOC triage turned out to be a near-perfect teaching example: lots of decisions, a real price on mistakes, and a queue of people with limited time.
  - After: Every chapter follows one made-up company, Kestrel Logistics, and its security operations centre (SOC). There, a small team triages hundreds of alerts a day: it sorts them by how likely they are to be real and how urgent they are. SOC triage turned out to be an almost perfect teaching example. It has lots of decisions, a real cost for mistakes, and a queue of people with limited time.
- `index.qmd`
  - Before: Every figure is drawn by code, and almost every number in the book is computed by it. Each chapter has a lab, a notebook in the book's repository, that reproduces its numbers and lets you change them.
  - After: Every figure is drawn by code, and almost every number in the book is computed by it. Each chapter has a lab: a notebook in the book's repository that recreates its numbers and lets you change them.
- `index.qmd`
  - Before: **No invented measurements.** I didn't have access to Jev's API while writing, so every Jev number in this book comes from a mock model called `jev-mock-synthetic`, built to copy the real API's shape through TypeSafe's official Python library. Those numbers are marked *synthetic*, every time. They show you how to reason and test; they are not claims about the real model.
  - After: **No invented measurements.** I didn't have access to Jev's API while writing. So every Jev number in this book comes from a mock model called `jev-mock-synthetic`. It's built to copy the real API's shape, through TypeSafe's official Python library. Those numbers are marked *synthetic*, every time. They show you how to reason and test; they are not claims about the real model.
- `index.qmd`
  - Before: **Claims have piles.** Everything said about Jev is sorted into what I could verify, what the vendor reports and what nobody outside the company knows yet. Chapter 9 explains how, and I'd encourage you to keep the same three piles for anything you read about new models, including this book.
  - After: **Claims go in piles.** Everything said about Jev is sorted into three piles: what I could check, what the vendor reports, and what nobody outside the company knows yet. Chapter 9 explains how. I'd encourage you to keep the same three piles for anything you read about new models, including this book.
- `front/how-to-read.qmd`
  - Before: **If you're new to machine learning**, read it in order. Part I builds the foundation everything else rests on: probabilities, and how to turn them into actions you can defend. Part II is a short tour of neural networks, LLMs and agents that assumes you haven't met any of them before.
  - After: **If you're new to machine learning**, read it in order. Part I builds the foundation for everything else: probabilities, and how to turn them into actions you can explain and defend. Part II is a short tour of neural networks, LLMs and agents. It assumes you haven't met any of them before.
- `front/how-to-read.qmd`
  - Before: **If you already build with LLMs**, read Part I anyway, and don't skip Chapter 3 on calibration or Chapter 4 on costs. Then jump to Part III. The rest of the book leans on those two chapters more than on anything else.
  - After: **If you already build with LLMs**, read Part I anyway, and don't skip Chapter 3 on calibration or Chapter 4 on costs. Then go to Part III. The rest of the book depends on those two chapters more than on anything else.
- `front/how-to-read.qmd`
  - Before: **If you lead a team or a product**, read Part I, then Chapters 8 to 14, then Chapters 18 and 22. You'll skip the code-heavy chapters and still be able to ask your team the right questions: what does a mistake cost, where's the line, how do we know the probabilities are honest, and who reads the flags?
  - After: **If you lead a team or a product**, read Part I, then Chapters 8 to 14, then Chapters 18 and 22. You'll skip the chapters with the most code and still be able to ask your team the right questions. What does a mistake cost? Where's the threshold? How do we know the probabilities are calibrated? Who reads the warnings?
- `front/how-to-read.qmd`
  - Before: Each chapter opens with a short list of what you'll be able to do by the end, and closes with a short recap, exercises and a hook to the next chapter. In between, a few kinds of box recur (@fig-boxes).
  - After: Each chapter opens with a short list of what you'll be able to do by the end. It closes with a short summary, exercises and a link to the next chapter. In between, a few kinds of box appear again and again (@fig-boxes).
- `front/how-to-read.qmd`
  - Before: The *Try it* boxes contain code you can run; the *Set the threshold* boxes ask you to make a small decision with real costs; the *Where this breaks* boxes mark the limits of what the chapter just showed. *Going deeper* boxes hold optional maths, and a side box headed with a question, like *Why not just maximise accuracy?*, deals with the objection you're probably already forming. Read the *Where this breaks* boxes above all. They're the difference between knowing a technique and knowing when to trust it.
  - After: The *Try it* boxes contain code you can run. The *Set the threshold* boxes ask you to make a small decision with real costs. The *Where this breaks* boxes show the limits of what the chapter just taught. *Going deeper* boxes hold optional maths. A side box with a question as its title, like *Why not just maximise accuracy?*, answers the objection you're probably already thinking of. Read the *Where this breaks* boxes most of all. They're the difference between knowing a method and knowing when to trust it.
- `front/how-to-read.qmd`
  - Before: Every listing in the book runs, and a test in the book's repository checks that it still does. The labs are Jupyter notebooks. Chapter 1's lab is `labs/ch01.ipynb`, Chapter 2's is `labs/ch02.ipynb`, and so on; each one installs everything it needs the first time you run it.
  - After: Every code listing in the book runs, and a test in the book's repository checks that it still does. The labs are Jupyter notebooks. Chapter 1's lab is `labs/ch01.ipynb`, Chapter 2's is `labs/ch02.ipynb`, and so on. Each one installs everything it needs the first time you run it.
- `front/how-to-read.qmd`
  - Before: The second line installs `jevkit`, the book's toolkit. Among other things, it includes the mock that answers the official SDK's calls without a network connection or an API key. If you have a real TypeSafe API key, set `JEVKIT_LIVE=1` and `TYPESAFE_API_KEY`, and the labs call the real service instead; Chapter 16 explains how.
  - After: The second line installs `jevkit`, the book's toolkit. It includes the mock that answers the official SDK's calls without a network connection or an API key. If you have a real TypeSafe API key, set `JEVKIT_LIVE=1` and `TYPESAFE_API_KEY`, and the labs call the real service instead. Chapter 16 explains how.
- `front/how-to-read.qmd`
  - Before: The listings use short names for `jevkit`'s modules, imported at the top of each chapter's lab:
  - After: The listings use short names for `jevkit`'s modules. Each chapter's lab imports them at the top:
- `front/how-to-read.qmd`
  - Before: | `pol` | `jevkit.policy` | costs, lines and the three zones |
  - After: | `pol` | `jevkit.policy` | costs, thresholds and the three zones |
- `front/how-to-read.qmd`
  - Before: Four small browser tools let you move the book's numbers yourself: a threshold simulator (Chapter 14), a calibration playground (Chapters 3 and 11), a bake-off explorer (Chapter 13) and a decision cost calculator (Chapters 9, 12 and 16). They're in the `site/` folder of the repository and on the book's website, [mukkandi-sridhar.github.io/JEVBook](https://mukkandi-sridhar.github.io/JEVBook/), and they run entirely in your browser.
  - After: Four small browser tools let you change the book's numbers yourself: a threshold simulator (Chapter 14), a calibration tool (Chapters 3 and 11), a bake-off explorer (Chapter 13) and a decision cost calculator (Chapters 9, 12 and 16). They're in the `site/` folder of the repository and on the book's website, [mukkandi-sridhar.github.io/JEVBook](https://mukkandi-sridhar.github.io/JEVBook/). They run entirely in your browser.
- `front/how-to-read.qmd`
  - Before: Kestrel Logistics is fictional, and so are its alerts, which come from a generator with a known truth behind every one. Knowing the truth is what makes it possible to measure things exactly, like how many real threats a policy misses. It also means every number is an illustration of a method, not a fact about the world. When a figure is labelled *synthetic*, believe the shape and test the numbers on your own data.
  - After: Kestrel Logistics is made up, and so are its alerts. They come from a program that knows the true answer for every one. Knowing the truth lets us measure things exactly, like how many real threats a policy misses. It also means every number is an example of a method, not a fact about the world. When a figure is labelled *synthetic*, trust the pattern, and test the numbers on your own data.
- `front/prologue.qmd`
  - Before: The building is quiet. The coffee isn't. On your left screen, the alert queue is scrolling the way it always does at this hour: a sign-in from an unusual country, a script that ran from a temp folder, an email with a link to a domain registered last week, a laptop talking to a server nobody recognises.
  - After: The building is quiet. On your left screen, the alert queue is moving the way it always does at this hour: a sign-in from an unusual country, a program that ran from a temporary folder, an email with a link to a website created last week, a laptop talking to a server nobody recognises.
- `front/prologue.qmd`
  - Before: Most of them are nothing. You know that. A salesperson on a trip, an IT tool doing its job, a newsletter with a tracking link. After a few months on nights, you can feel which ones are nothing before you finish reading them.
  - After: Most of them are nothing. You know that. A salesperson on a trip, an IT tool doing its job, a newsletter with a tracking link. After a few months of night shifts, you can feel which ones are nothing before you finish reading them.
- `front/prologue.qmd`
  - Before: You open the next alert. Twelve minutes later, you've pulled the logs, checked the user's history, looked up the domain and decided: fine. Close it. Next.
  - After: You open the next alert. Twelve minutes later, you've read the logs, checked the user's history, looked up the website and decided: fine. Close it. Next.
- `front/prologue.qmd`
  - Before: ![One night at Kestrel, midnight to 7 a.m. Each line is an alert; red lines are the real ones. Working first come, first served, you open the ones on the left and the rest wait for the morning.]
  - After: ![One night at Kestrel, midnight to 7 a.m. Each line is an alert; red lines are the real ones. Working in the order they arrive, you open the ones on the left and the rest wait for the morning.]
- `front/prologue.qmd`
  - Before: @fig-night shows the night from above, a view you never get from your desk.
  - After: @fig-night shows the whole night at once, a view you never get from your desk.
- `front/prologue.qmd`
  - Before: You didn't do anything wrong. You were careful and quick, and you got every one you opened right. The problem is that the queue decided what you'd look at, and the queue doesn't know anything. It just knows what arrived first.
  - After: You didn't do anything wrong. You were careful and quick, and you got every one you opened right. The problem is that the queue decided what you'd look at, and the queue doesn't know anything. It only knows what arrived first.
- `front/prologue.qmd`
  - Before: Every alert that arrives is read in a fraction of a second by a model that doesn't write a report or explain itself. It answers three small questions: how likely is this to be real, what kind of threat would it be, and how bad? Its answers are probabilities, and someone checked last week that they hold up: of the alerts it calls one in ten, about one in ten turn out to be real.
  - After: A model reads every alert that arrives in a fraction of a second. It doesn't write a report or explain itself. It answers three small questions: how likely is this to be real, what kind of threat would it be, and how bad? Its answers are probabilities. Someone checked last week that they're calibrated: of the alerts it calls one in ten, about one in ten turn out to be real.
- `front/prologue.qmd`
  - Before: The alerts it's nearly certain are nothing get closed, and a random few of those go into a pile for you to spot-check. The ones it's fairly sure are serious wake up the on-call responder straight away. Everything in between comes to you, likeliest first.
  - After: The alerts it's nearly certain are nothing get closed, and a random few of those go into a pile for you to check. For the ones it's fairly sure are serious, the analyst on call is woken up straight away. Everything in between comes to you, likeliest first.
- `front/prologue.qmd`
  - Before: You still make the calls that matter. You just make them on the right alerts.
  - After: You still make the decisions that matter. You just make them on the right alerts.
- `front/prologue.qmd`
  - Before: That second night is what this book builds, piece by piece. That takes surprisingly little new technology and quite a lot of careful thinking. You need to know what a probability is and how to tell whether one can be trusted. You need to know how much a mistake costs, and where to draw a line so that the cheapest mistakes are the ones you make. And you need to know what to do when the world changes, as it will on some ordinary Tuesday.
  - After: That second night is what this book builds, piece by piece. It takes surprisingly little new technology and quite a lot of careful thinking. You need to know what a probability is and how to tell whether one can be trusted. You need to know how much a mistake costs, and where to set a threshold so that the mistakes you make are the cheap ones. And you need to know what to do when the world changes, as it will, on some ordinary day.
- `parts/p1.qmd`
  - Before: These four chapters build the answer from the ground up. What learning is. What a probability means, and how a machine learns one. How to check whether it's honest. And how to turn it into an action, once you know what each mistake costs.
  - After: These four chapters build the answer from the beginning. What learning is. What a probability means, and how a machine learns one. How to check whether it's calibrated. And how to turn it into an action, once you know what each mistake costs.
- `parts/p1.qmd`
  - Before: Everything later in the book stands on these pages. If you only read one part slowly, make it this one.
  - After: Everything later in the book is built on these pages. If you read only one part slowly, make it this one.
- `parts/p2.qmd`
  - Before: The models in Part I were handed neat clues. The real world hands you pixels and messy logs. Today's AI systems are built from models that find their own clues, and from models that write text and act in loops.
  - After: The models in Part I were given neat clues. The real world gives you pixels and messy logs. Today's AI systems are built from models that find their own clues, and from models that write text and act in loops.
- `parts/p2.qmd`
  - Before: You don't need every detail. You need to see where the decisions hide.
  - After: You don't need every detail. You need to see where the decisions are hidden.
- `parts/p3.qmd`
  - Before: This part separates what's published from what's claimed, walks through its three question types, shows you how to test its calibration yourself, and asks what happens to an industry when a decision becomes almost free.
  - After: This part separates what's published from what's claimed. It explains Jev's three question types and shows you how to test its calibration yourself. Then it asks what happens to an industry when a decision becomes almost free.
- `parts/p4.qmd`
  - Before: A model is not a system. Between a probability and an action sits a decision layer, and most of what goes wrong lives there.
  - After: A model is not a system. Between a probability and an action there is a decision layer, and most of what goes wrong happens there.
- `parts/p4.qmd`
  - Before: This part puts six ways of deciding into one fair contest, turns probabilities into act, review and escalate, and collects the patterns that keep turning up when decision models meet real software.
  - After: This part compares six ways of deciding in one fair contest. It turns probabilities into act, review and escalate. And it collects the patterns that keep appearing when decision models are used in real software.
- `parts/p5.qmd`
  - Before: Time to build. First calls through the official SDK, a hybrid agent where Jev decides and an LLM writes, a full SOC triage case study and a gallery of other applications.
  - After: Time to build: first calls through the official SDK, a hybrid agent where Jev decides and an LLM writes, a full SOC triage case study, and a tour of other uses.

## Part openers (continued)

2 changes.

- `parts/p5.qmd`
  - Before: Time to build: first calls through the official SDK, a hybrid agent where Jev decides and an LLM writes, a full SOC triage case study, and a tour of other uses.
  - After: Time to build. You'll make your first calls through the official SDK. You'll build a hybrid agent, where Jev decides and an LLM writes. Then come a full SOC triage case study and a tour of other uses.
- `parts/p2.qmd`
  - Before: These three chapters are a fast tour: deep learning in one chapter, how an LLM writes and why asking it for a decision is awkward, and what retrieval and agents do, including where they break.
  - After: These three chapters are a fast tour. The first covers deep learning. The second shows how an LLM writes, and why asking it for a decision is awkward. The third shows what retrieval and agents do, and where they break.

## Cheat sheets

11 changes.

- `back/cheatsheets.qmd`
  - Before: Everything on these pages is explained properly in the chapter given in brackets. They're here for the day you need the formula and not the story.
  - After: Everything on these pages is explained fully in the chapter given in brackets. They're here for the day you need the formula and not the explanation.
- `back/cheatsheets.qmd`
  - Before: ## Drawing the line (Chapter 4)
  - After: ## Setting the threshold (Chapter 4)
- `back/cheatsheets.qmd`
  - Before: With a review that costs $C_r$ and catches all but a share $m$ of real problems, a miss $C_{\text{miss}}$ and a false page $C_{\text{page}}$, the cost-optimal lines for calibrated probabilities are
  - After: Say a review costs $C_r$ and misses a share $m$ of real problems. A miss costs $C_{\text{miss}}$ and a false urgent call costs $C_{\text{page}}$. Then the cheapest thresholds for calibrated probabilities are
- `back/cheatsheets.qmd`
  - Before: Then check the queue. If the review zone holds more cases than people can clear, raise the low line until it fits, and write down what that costs.
  - After: Then check the queue. If the review zone holds more cases than people can clear, raise the low (act) threshold until it fits, and write down what that costs.
- `back/cheatsheets.qmd`
  - Before: | Temperature | $p' = \sigma(z / T)$, one number | the model is uniformly over- or underconfident |
  - After: | Temperature | $p' = \sigma(z / T)$, one number | the model is too confident (or not confident enough) everywhere |
- `back/cheatsheets.qmd`
  - Before: 3. Compare the average predicted probability with the observed base rate. A big gap usually means prior shift.
  - After: 3. Compare the average predicted probability with the observed base rate. A big gap usually means the base rate has changed (prior shift).
- `back/cheatsheets.qmd`
  - Before: 4. Fix the base rate first; then Platt scaling on a few hundred labels if needed.
  - After: 4. Fix the base rate first; then use Platt scaling on a few hundred labels if needed.
- `back/cheatsheets.qmd`
  - Before: 5. Re-test on labels you didn't fit on. Repeat on a schedule and whenever the model version changes.
  - After: 5. Test again on labels you didn't fit on. Repeat on a schedule and whenever the model version changes.
- `back/cheatsheets.qmd`
  - Before: - Decide with the whole distribution and the costs of each action, not the top label.
  - After: - Decide with all the probabilities and the costs of each action, not just the top label.
- `back/cheatsheets.qmd`
  - Before: | messy input and a sharp decision | an LLM to extract, a decision model to decide |
  - After: | messy input and a clear decision | an LLM to extract, a decision model to decide |
- `back/cheatsheets.qmd`
  - Before: Pinned model · a versioned, fingerprinted config · a meaning for every failure · a record for every decision · random audits of automatic actions · a daily monitor · shadow runs for new versions · an owner who can switch it all to review.
  - After: A fixed model version · a config with a version number and a fingerprint · a meaning for every failure · a record for every decision · random audits of automatic actions · a daily monitor · shadow runs for new versions · an owner who can switch everything to review.

## Glossary

7 changes.

- `back/glossary.qmd`
  - Before: One plain sentence for each term, and the chapter where it's explained properly.
  - After: One plain sentence for each term, and the chapter where it's explained fully.
- `back/glossary.qmd`
  - Before: : A model is calibrated when the things it calls 70% likely happen about 70% of the time (Chapter 3).
  - After: : A model is calibrated when the things it calls 70% likely happen about 70% of the time: its probabilities are honest (Chapter 3).
- `back/glossary.qmd`
  - Before: Cost line
: The probability above which acting is cheaper than not acting, set by what each kind of mistake costs (Chapter 4).
  - After: Cost-based threshold
: The probability above which acting is cheaper than not acting, set by what each kind of mistake costs (Chapter 4).
- `back/glossary.qmd`
  - Before: : The part of a system that turns probabilities into actions: typed questions, calibration, lines, rules and fail-safes (Part IV).
  - After: : The part of a system that turns probabilities into actions: typed questions, calibration, thresholds, rules and fail-safes (Part IV).
- `back/glossary.qmd`
  - Before: : The rules that turn a probability into an action, usually as lines between zones (Chapter 14).
  - After: : The rules that turn a probability into an action, usually as thresholds between zones (Chapter 14).
- `back/glossary.qmd`
  - Before: Three-zone policy
: A policy with two lines, splitting cases into act, review and escalate (Chapter 14).
  - After: Three-zone policy
: A policy with two thresholds, splitting cases into act, review and escalate (Chapter 14).

Threshold
: A number that splits cases into two groups, like a line on the probability scale: above it you do one thing, below it another (Chapters 1 and 4).
- `back/glossary.qmd`
  - Before: Transport
: The lowest layer of an HTTP client, which sends a finished request and returns a response; the book's mock is one (Chapter 16).
  - After: Transport
: The lowest layer of an HTTP client, which sends a finished request and returns a response; the book's mock is one (Chapter 16).

Triage
: Sorting cases by how likely they are to be real and how urgent they are, so the most important ones are handled first (Preface, Chapter 18).

## Back cover

3 changes.

- `cover/wrap.py`
  - Before: "Is this alert real? Which team gets this ticket? Is this action safe? Most agents hand every one of those "
    "small decisions to a large language model, then dig the answer out of a paragraph. It works, slowly and "
    "expensively, and the model sounds just as sure when it’s wrong.",
  - After: "Is this alert real? Which team gets this ticket? Is this action safe? Most agents give every one of those "
    "small decisions to a large language model. Then code has to find the answer inside a paragraph. It works, "
    "but it’s slow and expensive, and the model sounds just as sure when it’s wrong.",
- `cover/wrap.py`
  - Before: "This book shows you a better way to build the decision layer. You’ll get probabilities you can trust, "
    "lines drawn from what each mistake costs, and a clear rule for when to hand a case to a person. Every step is "
  - After: "This book shows you a better way to build the decision layer. You’ll get calibrated probabilities that "
    "mean what they say, thresholds set by what each mistake costs, and a clear rule for when to give a case to "
    "a person. Every step is "
- `cover/wrap.py`
  - Before: "Turn a probability into act, review or escalate, with lines drawn from real costs and real capacity",
  - After: "Turn a probability into act, review or escalate, with thresholds set by real costs and real capacity",

## Whole-book sweep

4 changes.

- `chapters/ch11.qmd`
  - Before: With a hundred labels the measurement is both noisy and biased upwards: an honest model looks dishonest. The bias shrinks as samples grow.]
  - After: With a hundred labels the measurement is both noisy and too high on average: a calibrated model looks miscalibrated. The error shrinks as samples grow.]
- `chapters/ch15.qmd`
  - Before: The skill is sorting the steps honestly, the way Chapter 8 separated System 1 work from System 2.
  - After: The skill is sorting the steps correctly, the way Chapter 8 separated System 1 work from System 2.
- `chapters/ch19.qmd`
  - Before: ![Where the line falls in each domain, from its (illustrative) costs of a miss and a false alarm.
  - After: ![Where the threshold falls in each domain, from its (illustrative) costs of a miss and a false alarm.
- `back/python.qmd`
  - Before: The two lines, 0.031 and 0.34, are the ones Chapter 14 settles on.
  - After: The two thresholds, 0.031 and 0.34, are the ones Chapter 14 settles on.

## Glossary (shorter sentences)

18 changes.

- `back/glossary.qmd`
  - Before: : The chance that a model gives a randomly chosen real case a higher score than a randomly chosen harmless one; it measures ranking, not calibration (Chapter 3).
  - After: : The chance that a model gives a randomly chosen real case a higher score than a randomly chosen harmless one. It measures ranking, not calibration (Chapter 3).
- `back/glossary.qmd`
  - Before: : The average squared gap between a predicted probability and what happened; lower is better (Chapters 2 and 3).
  - After: : The average squared gap between a predicted probability and what happened. Lower is better (Chapters 2 and 3).
- `back/glossary.qmd`
  - Before: : How many cases the people in the loop can handle in a day; a policy that ignores it isn't a policy (Chapter 14).
  - After: : How many cases the people in the loop can handle in a day. A policy that ignores it isn't a policy (Chapter 14).
- `back/glossary.qmd`
  - Before: : A typed question with a set of named options; the answer is a probability for each option, adding up to 1 (Chapter 10).
  - After: : A typed question with a set of named options. The answer is a probability for each option, adding up to 1 (Chapter 10).
- `back/glossary.qmd`
  - Before: : One score that balances how many flagged cases are real and how many real cases get flagged; it measures ranking and labelling, not calibration (Chapter 3).
  - After: : One score that balances how many flagged cases are real and how many real cases get flagged. It measures ranking and labelling, not calibration (Chapter 3).
- `back/glossary.qmd`
  - Before: : A calibration method that learns any increasing mapping from scores to probabilities; flexible, but needs more data than Platt scaling (Chapter 3).
  - After: : A calibration method that learns any increasing mapping from scores to probabilities. It's flexible, but needs more data than Platt scaling (Chapter 3).
- `back/glossary.qmd`
  - Before: : A score that punishes confident wrong answers heavily; a proper scoring rule (Chapter 2).
  - After: : A score that punishes confident wrong answers heavily. A proper scoring rule (Chapter 2).
- `back/glossary.qmd`
  - Before: : A number that measures how wrong a model is on some examples; training tries to make it smaller (Chapter 2).
  - After: : A number that measures how wrong a model is on some examples. Training tries to make it smaller (Chapter 2).
- `back/glossary.qmd`
  - Before: : A stand-in for a real service that answers in the same shape; this book's is `jev-mock-synthetic` (Chapter 16).
  - After: : A stand-in for a real service that answers in the same shape. This book's is `jev-mock-synthetic` (Chapter 16).
- `back/glossary.qmd`
  - Before: : TypeSafe's name for a yes-or-no question; the answer is the probability of yes (Chapter 10).
  - After: : TypeSafe's name for a yes-or-no question. The answer is the probability of yes (Chapter 10).
- `back/glossary.qmd`
  - Before: : Having a meaningful order, like severity levels; an ordinal model keeps that order in its probabilities (Chapter 20).
  - After: : Having a meaningful order, like severity levels. An ordinal model keeps that order in its probabilities (Chapter 20).
- `back/glossary.qmd`
  - Before: : Probabilities that are more extreme than the evidence justifies; common in large models and in overtrained small ones (Chapter 5).
  - After: : Probabilities that are more extreme than the evidence justifies. It's common in large models and in overtrained small ones (Chapter 5).
- `back/glossary.qmd`
  - Before: : A change in the base rate between where a model was calibrated and where it's used; correctable if the new base rate is known (Chapter 11).
  - After: : A change in the base rate between where a model was calibrated and where it's used. You can correct it if you know the new base rate (Chapter 11).
- `back/glossary.qmd`
  - Before: : A chart of what a model said against what happened; a calibrated model sits on the diagonal (Chapter 3).
  - After: : A chart of what a model said against what happened. A calibrated model sits on the diagonal (Chapter 3).
- `back/glossary.qmd`
  - Before: : TypeSafe's name for reinforcement learning for calibrated decisions, which it says trains Jev; details unpublished (Chapter 9).
  - After: : TypeSafe's name for reinforcement learning for calibrated decisions, which it says trains Jev. Details unpublished (Chapter 9).
- `back/glossary.qmd`
  - Before: : A typed question with ordered levels; the answer is a probability for each level and an expected level (Chapter 10).
  - After: : A typed question with ordered levels. The answer is a probability for each level and an expected level (Chapter 10).
- `back/glossary.qmd`
  - Before: : The tool that collects a company's logs and raises security alerts; Kestrel's alerts come from one (Chapter 13).
  - After: : The tool that collects a company's logs and raises security alerts. Kestrel's alerts come from one (Chapter 13).
- `back/glossary.qmd`
  - Before: : The lowest layer of an HTTP client, which sends a finished request and returns a response; the book's mock is one (Chapter 16).
  - After: : The lowest layer of an HTTP client, which sends a finished request and returns a response. The book's mock is one (Chapter 16).

## Glossary (continued)

3 changes.

- `back/glossary.qmd`
  - Before: : A score that punishes confident wrong answers heavily. A proper scoring rule (Chapter 2).
  - After: : A score that punishes confident wrong answers heavily. It's a proper scoring rule (Chapter 2).
- `back/glossary.qmd`
  - Before: : TypeSafe's name for reinforcement learning for calibrated decisions, which it says trains Jev. Details unpublished (Chapter 9).
  - After: : TypeSafe's name for reinforcement learning for calibrated decisions, which it says trains Jev. The details aren't published (Chapter 9).
- `back/glossary.qmd`
  - Before: : In a Jev `choice` or `score` answer, a number from 0 to 1 computed from the shape of the probabilities: high when they're concentrated on one option, low when they're spread out. It isn't simply the top probability (TypeSafe's quick-start shows 0.78 beside 0.85). The book's mock uses the top probability as a stand-in (Chapter 9).
  - After: : In a Jev `choice` or `score` answer, a number from 0 to 1 computed from the shape of the probabilities. It's high when most of the probability is on one option, and low when it's spread out. It isn't simply the top probability (TypeSafe's quick-start shows 0.78 beside 0.85). The book's mock uses the top probability as a stand-in (Chapter 9).

## Chapter 5 (paragraph split)

1 changes.

- `chapters/ch05.qmd`
  - Before: It's also the engine inside RAG (Chapter 7). But it has a weakness worth remembering. Here's a test:
  - After: It's also the engine inside RAG (Chapter 7).

But it has a weakness worth remembering. Here's a test:

## v1.0.2 touch-up

2 changes.

- `back/python.qmd`
  - Before: `groupby` splits the table into groups and sums up each group.
  - After: `groupby` splits the table into groups and summarises each one.
- `chapters/ch05.qmd`
  - Before: print(f"{a:>9} vs {b:<8} {cos(a, b):+.2f}")
```
:::
  - After: print(f"{a:>9} vs {b:<8} {cos(a, b):+.2f}")
```
:::

Real text would give something like 0.7 to 0.9. Our synthetic notes use these words almost interchangeably, so they come out identical.

## Key ideas (v1.0.3)

43 changes.

- `chapters/ch01.qmd`
  - Before: And we ask the computer to find the pattern that separates them.

::: {.keyidea}
That's machine learning.
:::

In one sentence: **machine learning is getting a computer to work out the rules itself, from examples where the answer is already known.**
  - After: And we ask the computer to find the pattern that separates them. That's machine learning. In one sentence:

::: {.keyidea}
**Machine learning** is getting a computer to work out the rules itself, from examples where the answer is already known.
:::
- `chapters/ch01.qmd`
  - Before: ::: {.keyidea}
The machine learned exactly what we asked. We asked the wrong question.
:::
  - After: ::: {.keyidea}
A model learns exactly what you ask for: ask the wrong question, and it learns the wrong thing.
:::
- `chapters/ch01.qmd`
  - Before: ::: {.keyidea}
A good model doesn't just answer. It says how sure it is, and it's right about how sure it is.
:::
  - After: ::: {.keyidea}
A good model doesn't just answer: it says how sure it is, and it's right about how sure it is.
:::
- `chapters/ch02.qmd`
  - Before: So here's the idea to remember: **a probability is a claim about how often something happens among cases like this one.**
  - After: So here's the idea to remember:

::: {.keyidea}
A **probability** is a claim about how often something happens among cases like this one.
:::
- `chapters/ch02.qmd`
  - Before: ::: {.keyidea}
Log loss rewards honest probabilities and punishes confident mistakes.
:::
  - After: ::: {.keyidea}
Log loss rewards calibrated probabilities and punishes confident mistakes.
:::
- `chapters/ch02.qmd`
  - Before: until the ground is flat.

::: {.keyidea}
That's gradient descent.
:::
  - After: until the ground is flat. That's gradient descent.
- `chapters/ch03.qmd`
  - Before: The rule is simple: **check calibration inside every group you'll treat differently**, and inside every group where a mistake would be especially costly. That means sources,
  - After: The rule is simple:

::: {.keyidea}
Check calibration inside every group you'll treat differently, not just on average.
:::

Do the same inside every group where a mistake would be especially costly. That means sources,
- `chapters/ch04.qmd`
  - Before: the cheapest thing to do, on average, is to act whenever

::: {.keyidea}
P > C~fa~ ÷ (C~fa~ + C~miss~)
:::
  - After: the cheapest thing to do, on average, is this:

::: {.keyidea}
Act when P > C~fa~ ÷ (C~fa~ + C~miss~): the false-alarm cost over the sum of both costs.
:::
- `chapters/ch04.qmd`
  - Before: That curve, in @fig-coverage-risk, is one of the most useful pictures
  - After: ::: {.keyidea}
Let a model decide only the cases it's surest about, and its error rate falls steeply.
:::

That curve, in @fig-coverage-risk, is one of the most useful pictures
- `chapters/ch05.qmd`
  - Before: ::: {.keyidea}
Weighted sums draw lines. Hinges bend them. Layers combine the bends.
:::
  - After: Weighted sums draw lines. Hinges bend them. Layers combine the bends.
- `chapters/ch07.qmd`
  - Before: ::: {.keyidea}
Take the facts that lower suspicion from systems attackers can't write to, never from the text they can.
:::
  - After: ::: {.keyidea}
Take the facts that lower suspicion from systems attackers can't write to.
:::
- `chapters/ch08.qmd`
  - Before: ::: {.keyidea}
Most of the work is System 1 work. Most of the machinery we've been using is System 2.
:::
  - After: ::: {.keyidea}
Most of the work is System 1 work, but most of the machinery we use is System 2.
:::
- `chapters/ch09.qmd`
  - Before: what nobody outside the company knows. That habit is worth more than any single fact in this chapter.
  - After: what nobody outside the company knows.

::: {.keyidea}
Sort every claim about a new model into three piles: verified, vendor-reported and unknown.
:::

That habit is worth more than any single fact in this chapter.
- `chapters/ch09.qmd`
  - Before: If you remember one habit from this chapter, make it this one. When a vendor gives you several numbers, check whether they agree with *each other*.
  - After: If you remember one habit from this chapter, make it this one.

::: {.keyidea}
When a vendor gives you several numbers, check whether they agree with *each other*.
:::
- `chapters/ch09.qmd`
  - Before: None of those unknowns are reasons to avoid a new model. They're reasons to *test* it, on your own data, with the tools you already have. The next two chapters do just that.
  - After: ::: {.keyidea}
Unknowns about a new model aren't reasons to avoid it; they're reasons to *test* it on your own data.
:::

You can test it with the tools you already have, and the next two chapters do just that.
- `chapters/ch10.qmd`
  - Before: ::: {.keyidea}
A choice's probabilities add up to 1 over the options you gave. Make sure every real case has somewhere to go.
:::
  - After: ::: {.keyidea}
A choice's probabilities add up to 1 over your options, so give every real case somewhere to go.
:::
- `chapters/ch11.qmd`
  - Before: ::: {.keyidea}
Treat a new model's outputs as scores until you've tested them on your data. After that, treat them as probabilities.
:::
  - After: ::: {.keyidea}
Treat a new model's outputs as scores until you've tested them on your own data.
:::

After that, you can treat them as probabilities.
- `chapters/ch12.qmd`
  - Before: ::: {.keyidea}
When decisions get cheap, thresholds must be set by cost, not by share. Otherwise the money saved on machines is spent on people's time.
:::
  - After: ::: {.keyidea}
When decisions get cheap, set thresholds by cost, not by share.
:::

Otherwise the money saved on machines is spent on people's time.
- `chapters/ch13.qmd`
  - Before: ::: {.keyidea}
Labels are the hidden cost of trained models. A method that needs none can start today. A method that needs thousands has to wait for them, and needs them again when things change.
:::
  - After: ::: {.keyidea}
Labels are the hidden cost of trained models: a method that needs none can start today.
:::

A method that needs thousands has to wait for them, and needs them again when things change.
- `chapters/ch13.qmd`
  - Before: If a rule or a logistic regression can make a decision well, use one of them. It's the cheapest
  - After: ::: {.keyidea}
If a rule or a logistic regression can make a decision well, use one of them.
:::

It's the cheapest
- `chapters/ch13.qmd`
  - Before: but the idea fits any bake-off. There is no best method, only a best method for a particular decision.
  - After: but the idea fits any bake-off.

::: {.keyidea}
There is no best method, only a best method for a particular decision.
:::
- `chapters/ch14.qmd`
  - Before: ::: {.keyidea}
Act, review, escalate. Machines handle the clear cases at each end; people handle the middle.
:::
  - After: ::: {.keyidea}
Act, review, escalate: machines handle the clear cases at each end, and people handle the middle.
:::
- `chapters/ch14.qmd`
  - Before: A policy that ignores capacity isn't a policy. It's a wish. Anything beyond
  - After: ::: {.keyidea}
A policy that ignores capacity isn't a policy. It's a wish.
:::

Anything beyond
- `chapters/ch15.qmd`
  - Before: notice what the patterns share. In every pattern, the decision model never writes anything and never acts on its own. It answers a typed question, and ordinary code turns the answer into an action. That separation
  - After: notice what the patterns share.

::: {.keyidea}
A decision model never writes and never acts on its own: it answers a typed question, and code acts.
:::

That's true in every pattern, and that separation
- `chapters/ch15.qmd`
  - Before: ::: {.keyidea}
Extract when the only input you have is text. When structured data exists, use it: extraction can't add facts the text doesn't contain.
:::
  - After: ::: {.keyidea}
Extract when the only input you have is text: extraction can't add facts the text doesn't contain.
:::

When structured data exists, use it.
- `chapters/ch16.qmd`
  - Before: Chapter 9 said one unknown in a new model is how its behaviour changes between versions. Fixing the version turns that into your decision, not a surprise.
  - After: Chapter 9 said one unknown in a new model is how its behaviour changes between versions.

::: {.keyidea}
Fix the model version, so a change in behaviour is your decision, not a surprise.
:::
- `chapters/ch16.qmd`
  - Before: ::: {.keyidea}
Retry errors from outside your code, never your own. And when time matters, decide in advance what a failed call means.
:::
  - After: ::: {.keyidea}
When time matters, decide in advance what a failed call means.
:::
- `chapters/ch17.qmd`
  - Before: ::: {.keyidea}
Count the answers of every decision step. An option that's never chosen, or always chosen, is a warning, even when nothing has crashed.
:::
  - After: ::: {.keyidea}
Count every decision step's answers: an option never or always chosen is a warning, even without a crash.
:::
- `chapters/ch17.qmd`
  - Before: costs about as much as just looking. When looking is cheaper than deciding whether to look, don't decide. Just look.
  - After: costs about as much as just looking.

::: {.keyidea}
When looking is cheaper than deciding whether to look, don't decide. Just look.
:::
- `chapters/ch17.qmd`
  - Before: The hybrid doesn't use less LLM because LLMs are bad. It uses the LLM for the work only an LLM can do.
  - After: The hybrid doesn't use less LLM because LLMs are bad.

::: {.keyidea}
Use the LLM for the work only an LLM can do.
:::
- `chapters/ch18.qmd`
  - Before: ::: {.keyidea}
A probability doesn't only decide *whether* a person looks. It decides *what they look at first*. Ordering the queue is often the cheapest improvement available.
:::
  - After: ::: {.keyidea}
A probability decides *what* a person looks at first, not only *whether* they look.
:::

Ordering the queue is often the cheapest improvement available.
- `chapters/ch18.qmd`
  - Before: Here is the uncomfortable truth of the campaign week. Calibration tells you truthfully how much work there is. It can't make the work smaller. When the world
  - After: Here is the uncomfortable truth of the campaign week.

::: {.keyidea}
Calibration tells you truthfully how much work there is. It can't make the work smaller.
:::

When the world
- `chapters/ch18.qmd`
  - Before: while the analysts work as before. Nothing it decides has any effect.
  - After: while the analysts work as before. Nothing it decides has any effect.

::: {.keyidea}
Run a new decision system in shadow mode before you let it act.
:::
- `chapters/ch19.qmd`
  - Before: ::: {.keyidea}
The formula never changes. The costs do, and they can move the threshold by a factor of ten or more.
:::
  - After: ::: {.keyidea}
The threshold formula never changes; the costs do, and they can move the threshold tenfold or more.
:::
- `chapters/ch19.qmd`
  - Before: The further up and to the left a decision sits, the more a person belongs in the loop.
  - After: The further up and to the left a decision sits, the more a person belongs in the loop.

::: {.keyidea}
Where decisions are many and cheap, the model decides; where they're few and costly, a person does.
:::
- `chapters/ch19.qmd`
  - Before: What I can say is that you'd only know by measuring, and the test took twenty lines of code.
  - After: What I can say is that you'd only know by measuring, and the test took twenty lines of code.

::: {.keyidea}
Measure a model on each new domain before you trust it, even if it works well elsewhere.
:::
- `chapters/ch20.qmd`
  - Before: ::: {.keyidea}
Train with a proper scoring rule, stop before the model memorises, then calibrate on data it has never seen. You need all three.
:::
  - After: ::: {.keyidea}
Train with a proper scoring rule, stop before the model memorises, then calibrate on data it has never seen.
:::

You need all three.
- `chapters/ch20.qmd`
  - Before: The ranking didn't change at all, because dividing every score by the same number doesn't change their order.
  - After: The ranking didn't change at all.

::: {.keyidea}
Temperature scaling never changes the ranking: dividing every score by one number keeps their order.
:::
- `chapters/ch21.qmd`
  - Before: ::: {.keyidea}
Every failure needs a decided meaning, and the safe meaning is the one that puts a person in front of the case.
:::
  - After: ::: {.keyidea}
Every failure needs a decided meaning, and the safe one puts a person in front of the case.
:::
- `chapters/ch21.qmd`
  - Before: The first rule is this: *everything that can change a decision lives in one place, with a version number.*
  - After: The first rule is this:

::: {.keyidea}
Everything that can change a decision lives in one place, with a version number.
:::
- `chapters/ch21.qmd`
  - Before: That's why the config holds the rules *and* the thresholds. They're one decision, and they have to be fitted together.
  - After: That's why the config holds the rules *and* the thresholds.

::: {.keyidea}
Thresholds and business rules are one decision, and they have to be fitted together.
:::
- `chapters/ch22.qmd`
  - Before: ::: {.keyidea}
You don't need to predict how this turns out. You need decisions you can measure, thresholds you can move and a model you can replace.
:::
  - After: You don't need to predict how this turns out.

::: {.keyidea}
You need decisions you can measure, thresholds you can move and a model you can replace.
:::
- `chapters/ch22.qmd`
  - Before: and whether the probabilities are still calibrated this week. The model can't do any of that for you.
  - After: and whether the probabilities are still calibrated this week. The model can't do any of that for you.

::: {.keyidea}
When deciding gets cheap, judgement about the decision itself becomes scarce.
:::

## Key ideas (v1.0.3), Chapter 16

1 changes.

- `chapters/ch16.qmd`
  - Before: The SDK retries these by default, twice, waiting a little longer each time.
  - After: The SDK retries these by default, twice, waiting a little longer each time.

::: {.keyidea}
Retry errors from outside your code, never your own.
:::

## Key ideas (v1.0.3), Chapter 12

1 changes.

- `chapters/ch12.qmd`
  - Before: Cheaper decisions rarely raise the bill for the jobs you already do. They raise it by making new jobs worth doing.
  - After: Cheaper decisions rarely raise the bill for jobs you already do; they raise it by making new jobs worth doing.

## Key ideas (v1.0.3), How to read

2 changes.

- `front/how-to-read.qmd`
  - Before: It closes with a short summary, exercises and a link to the next chapter.
  - After: It closes with a short summary, a *Keep these* box that lists the chapter's key ideas, exercises and a link to the next chapter.
- `front/how-to-read.qmd`
  - Before: The *Try it* boxes contain code you can run.
  - After: A *Key idea* box, with a thick bar down its left side, holds one sentence worth remembering a year from now. The *Key ideas* appendix lists all of them, with their pages, for revision. The *Try it* boxes contain code you can run.

## Black and white: second cues for colour words (v1.0.3)

39 changes.

- `front/prologue.qmd`
  - Before: Each line is an alert; red lines are the real ones.
  - After: Each line is an alert; the real ones are red, taller and marked on top.
- `chapters/ch01.qmd`
  - Before: just below the dashed line for "flag nothing at all".
  - After: just below the thin dotted line for "flag nothing at all".
- `chapters/ch02.qmd`
  - Before: If it really was an attack (red), the penalty
  - After: If it really was an attack (red, solid curve), the penalty
- `chapters/ch02.qmd`
  - Before: Harmless alerts (blue) work the same way
  - After: Harmless alerts (blue, dashed curve) work the same way
- `chapters/ch03.qmd`
  - Before: A model trained on 50/50 rebalanced data (red) thinks
  - After: A model trained on 50/50 rebalanced data (red, solid line with squares) thinks
- `chapters/ch03.qmd`
  - Before: fitted on a separate calibration set (green), the same model
  - After: fitted on a separate calibration set (green, dashed line with circles), the same model
- `chapters/ch04.qmd`
  - Before: For the calibrated model (green), the formula's threshold
  - After: For the calibrated model (green, solid line), the formula's threshold
- `chapters/ch04.qmd`
  - Before: trained on rebalanced data (red), the same threshold lands
  - After: trained on rebalanced data (red, dashed line), the same threshold lands
- `chapters/ch04.qmd`
  - Before: The grey curve shows how much traffic you're blocking.
  - After: The grey dotted curve shows how much traffic you're blocking.
- `chapters/ch04.qmd`
  - Before: A better model (green) gives you more coverage at the same risk.
  - After: A better model (green, solid line) gives you more coverage at the same risk.
- `chapters/ch05.qmd`
  - Before: Blue dots are normal activity; red dots surround them on every side.
  - After: Blue dots are normal activity; red crosses surround them on every side.
- `chapters/ch07.qmd`
  - Before: for questions the knowledge base can answer (green) and questions it can't (red).
  - After: for questions the knowledge base can answer (green, solid bars) and questions it can't (red, striped outline).
- `chapters/ch07.qmd`
  - Before: reading the alert text as written (black) and with one planted sentence (red).
  - After: reading the alert text as written (black, solid line) and with one planted sentence (red, dashed line).
- `chapters/ch07.qmd`
  - Before: When the same fact comes from a trusted system instead (green), the planted sentence does nothing.
  - After: When the same fact comes from a trusted system instead (green, dotted fill), the planted sentence does nothing.
- `chapters/ch08.qmd`
  - Before: Sending the alerts System 1 is least sure about (green) gets
  - After: Sending the alerts System 1 is least sure about (green, solid line) gets
- `chapters/ch08.qmd`
  - Before: Sending a random share (grey) gets almost nothing
  - After: Sending a random share (grey, dashed line) gets almost nothing
- `chapters/ch08.qmd`
  - Before: Better calibration makes the green curve drop *faster*.
  - After: Better calibration makes the solid green curve drop *faster*.
- `chapters/ch10.qmd`
  - Before: With "benign" among the options (green), almost all
  - After: With "benign" among the options (green, striped), almost all
- `chapters/ch10.qmd`
  - Before: Without it (red), every harmless alert
  - After: Without it (red, solid), every harmless alert
- `chapters/ch11.qmd`
  - Before: as returned (red), after adjusting the odds for Harbor's base rate (blue), and after Platt scaling on 300 labelled alerts (green).
  - After: as returned (red, solid line), after adjusting the odds for Harbor's base rate (blue, dashed line), and after Platt scaling on 300 labelled alerts (green, dotted line).
- `chapters/ch12.qmd`
  - Before: The shaded regions show which decisions each option can make,
  - After: The shaded regions, each labelled and outlined, show which decisions each option can make,
- `chapters/ch14.qmd`
  - Before: The red dots, real threats, are mostly to the right, but not all of them.
  - After: The red crosses, real threats, are mostly to the right, but not all of them.
- `chapters/ch14.qmd`
  - Before: The grey dots are crowded on the left: the easy, harmless alerts. The red dots are mostly to the right. But some red dots are spread through the middle, and a few are even in the crowd on the far left. And some grey dots sit in the escalate zone.
  - After: The grey circles are crowded on the left: the easy, harmless alerts. The red crosses are the real threats, and they're mostly to the right. But some red crosses are spread through the middle, and a few are even in the crowd on the far left. And some grey circles sit in the escalate zone.
- `chapters/ch14.qmd`
  - Before: Raw scores (red) sit above the diagonal:
  - After: Raw scores (red, solid line) sit above the diagonal:
- `chapters/ch14.qmd`
  - Before: After Platt scaling fitted on other days (green), the curve
  - After: After Platt scaling fitted on other days (green, dashed line), the curve
- `chapters/ch14.qmd`
  - Before: The light segment on the left is the number that matters:
  - After: The light, plain segment on the left (act) is the number that matters:
- `chapters/ch14.qmd`
  - Before: the "act" segment on the threat side (the lightest purple) went
  - After: the "act" segment on the threat side (the lightest purple, with no pattern) went
- `chapters/ch14.qmd`
  - Before: Every point on the green curve is the best policy for that team;
  - After: Every point on the green dashed curve is the best policy for that team;
- `chapters/ch14.qmd`
  - Before: The grey curve is worth a look too.
  - After: The grey solid curve is worth a look too.
- `chapters/ch14.qmd`
  - Before: real threats each day (black) against what the calibrated model expected (green).
  - After: real threats each day (black, solid line) against what the calibrated model expected (green, dashed line).
- `chapters/ch14.qmd`
  - Before: In week five (shaded), reality moves away
  - After: In week five (shaded, between dotted lines), reality moves away
- `chapters/ch17.qmd`
  - Before: Everything in green is a typed question to Jev, answered in one pass. Everything in blue is a tool that reads something. The policy is ordinary code. The LLM, in orange, appears once, at the end.
  - After: Everything in green, with "Jev" in its label, is a typed question to Jev, answered in one pass. Everything in blue, labelled "tools", is a tool that reads something. The policy is ordinary code. The LLM, in orange and labelled "LLM", appears once, at the end.
- `chapters/ch17.qmd`
  - Before: Blue steps observe, green steps decide, orange steps write, grey steps act.
  - After: Plain blue steps observe, striped green steps decide, dotted orange steps write, cross-hatched grey steps act.
- `chapters/ch17.qmd`
  - Before: it's mostly the width of the green bars.
  - After: it's mostly the width of the green, striped decide bars.
- `chapters/ch18.qmd`
  - Before: The red cell is the one to argue about:
  - After: The red cell, outlined in black and striped, is the one to argue about:
- `chapters/ch18.qmd`
  - Before: mostly about one cell, the red one in @fig-shadow-18.
  - After: mostly about one cell, the red one outlined in black in @fig-shadow-18.
- `chapters/ch19.qmd`
  - Before: Green cards let the model decide and people audit; red cards keep a person as the decider.
  - After: Green cards, which end "the model decides; people audit", let the model decide. Red cards, which end "a person decides", keep a person as the decider.
- `chapters/ch19.qmd`
  - Before: In the red domains, the design is the other way round.
  - After: In the red domains, shown as squares in @fig-domains, the design is the other way round.
- `chapters/ch21.qmd`
  - Before: Top: the review queue, red on days a flag was raised.
  - After: Top: the review queue, red and striped on days a flag was raised.

## Black and white: Chapter 17 fix (v1.0.3)

1 changes.

- `chapters/ch17.qmd`
  - Before: Everything in blue, labelled "tools", is a tool that reads something.
  - After: Everything in blue is a tool that reads something: the threat-intel lookup and the box labelled "tools".

## Black and white: Chapter 11 caption (v1.0.3)

1 changes.

- `chapters/ch11.qmd`
  - Before: is shown by the black line
  - After: is shown by the labelled black horizontal line

## Key ideas (v1.0.3), How to read paragraph split

1 changes.

- `front/how-to-read.qmd`
  - Before: The *Key ideas* appendix lists all of them, with their pages, for revision. The *Try it* boxes
  - After: The *Key ideas* appendix lists all of them, with their pages, for revision.

The *Try it* boxes
