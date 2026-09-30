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
