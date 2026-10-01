# Publishing guide: *Decide, Don't Generate*, from start to launch

The plan in order, with every piece of text ready to paste. `KDP-UPLOAD.md` has the full field-by-field sheet.

**The plan in one line:** a Kindle ebook at $12.99 (₹499 on amazon.in) and a colour paperback on standard colour ink at $34.99, launched
together. Add the black-and-white paperback and the hardcover later if people ask for them.

---

## Step 0. Before you start (one-time)

- [x] The companion repository and website are set up, and the book points to them (v1.0.4).
- [ ] Download the files you'll upload. On GitHub, switch to the branch `claude/compassionate-planck-ao0jvq`, open
      `release/v1.0/`, click each file, then the download button:
  - `print-color/interior-color.pdf` (the inside of the book)
  - `print-color/cover-paperback-standard-color.pdf` (the cover for a standard-colour paperback)
  - `ebook/book.epub` and `ebook/ebook-cover.jpg` (the Kindle edition)

## Step 1. Your KDP account

At **kdp.amazon.com → Your Account**:

- [ ] **Two-Step Verification**: an authenticator app or SMS. Save the backup codes.
- [ ] **Author/Publisher information**: your real name (as on your PAN) and your address.
- [ ] **Getting paid**: your Indian bank account (holder name, account number, IFSC).
- [ ] **Tax information**: individual, not a US person, India, your PAN, and **Yes** to treaty benefits.

You can create the book while these are pending; you can't publish until they're done.

## Step 2. The paperback

**Bookshelf → + Create new title or series → Paperback.**

### Page 1: Details

| Field | Enter |
|---|---|
| Language | English |
| Book title | Decide, Don't Generate |
| Subtitle | Jev, System One Models, and the Decision Layer of Agentic AI |
| Edition | 1 |
| Author | Sridhar Mukkandi |
| Description | the text below |
| Publishing rights | I own the copyright and hold the necessary publishing rights |
| Sexually explicit | No |
| Reading age | leave blank |
| Primary marketplace | Amazon.com |
| Categories | the three below |
| Keywords | the seven below |
| Low-content / Large print | No / No |
| AI-generated content | Text: Yes. Images: Yes (the figures were drawn by code an AI wrote). Translations: No. If asked, "extensively edited". |

**Description** (paste exactly; the tags become bold text and bullet points on Amazon):

```html
<b>Your AI agent makes hundreds of small decisions a day. How many of them would you trust?</b><br><br>
Is this alert real? Which team should get this ticket? Is it safe to run this command? Most agents send every one of these questions to a large language model and hope the paragraph that comes back has a usable answer in it. It works, sort of. It's slow, it costs more than it should, and the model sounds just as confident when it's wrong as when it's right.<br><br>
This book is about doing it properly. It starts from the ground up: what a probability really means, how to tell whether a model's 80% actually happens 80% of the time, and how to turn that number into a decision you can defend. Act on it, send it to a person, or wake someone up.<br><br>
You'll follow one fictional security team as their alerts pile up and their analysts run out of time. Every chapter has a lab you can run on your own laptop. You'll compare six ways to make the same decision, build an agent where a fast decision model decides and the LLM only writes, and finish with a small decision service you could really put into production.<br><br>
<b>You'll learn how to:</b>
<ul>
<li>check whether a model's probabilities can be trusted, and fix them when they can't</li>
<li>set thresholds from what each mistake costs, and from how many people you have to review cases</li>
<li>choose between rules, classic machine learning, LLMs and decision models for a given job</li>
<li>build agents that know when they're unsure, and hand those cases to a person</li>
<li>test, monitor and safely change a decision system once it's live</li>
</ul>
<b>Inside:</b> 22 chapters and 22 Python labs, a free mock of the API so nothing costs money and you don't need a key, 138 figures, and a list of the 62 key ideas for quick revision.<br><br>
<b>Who it's for:</b> computer science students, engineers building AI agents, and tech leads deciding what to build. If you can read basic Python, you can follow every chapter.<br><br>
<i>An independent guide, not affiliated with TypeSafe AI. The security team and all its data are synthetic.</i>
```

**Keywords** (one per box):

```
agentic AI agents for engineers
LLM agent architecture design patterns
probability calibration machine learning
AI decision making systems in production
human in the loop review thresholds
hands on AI engineering Python projects
cybersecurity SOC alert triage machine learning
```

**Categories** (the closest names in KDP's picker):

1. Books › Computers & Technology › Computer Science › AI & Machine Learning › General
2. Books › Computers & Technology › Computer Science › AI & Machine Learning › Expert Systems
3. Books › Computers & Technology › Computer Science › AI & Machine Learning › Generative AI

### Page 2: Content

| Field | Choose |
|---|---|
| Print ISBN | **Get a free KDP ISBN → Assign ISBN** |
| Publication date | leave blank (today) |
| Ink and paper | **Standard colour, white paper** |
| Trim size | **7 × 10 in** |
| Bleed | **No bleed** |
| Cover finish | **Matte** |
| Manuscript | upload `interior-color.pdf` |
| Book cover | **Upload a cover you already have** → `cover-paperback-standard-color.pdf` |
| Barcode | leave KDP's option on |

Then click **Launch Previewer** and check: 270 pages, nothing cut off, the cover's spine fits. Approve.

### Page 3: Pricing

| Setting | Choose |
|---|---|
| Territories | All territories |
| Primary marketplace | Amazon.com |
| Price (USD) | **$34.99** (printing costs $11.85, so you earn about $9.14 a copy) |
| Amazon.in | not offered for standard colour paperbacks; Indian readers get the Kindle edition |
| Other marketplaces | let KDP convert from the US price |
| Expanded Distribution | **Off** for now (it pays less and needs a higher price) |

**Before you click Publish**, order an author proof copy (**Request printed proofs**, on the Content page or from
the book's **…** menu on your Bookshelf). It costs only the
printing and arrives in about a week. Check the colours, the figures and the code in print, then publish.

## Step 3. The Kindle ebook

**Bookshelf → + Create → Kindle eBook.** Same title, subtitle, author, description, keywords and categories.

| Field | Choose |
|---|---|
| ISBN | not needed |
| Manuscript | `book.epub` |
| Kindle eBook cover | `ebook-cover.jpg` |
| AI-generated content | same answers as the paperback |
| KDP Select | **Yes** (Kindle Unlimited readers; it runs in 90-day terms you can choose not to renew) |
| Royalty | **70%** |
| Price | **$12.99** (the top of the 70% band, which KDP raised from $9.99; about $7.43 a copy after the $1.66 delivery fee for the 11.07 MB converted file). Amazon.in: **₹499** |

Check it in the Kindle Previewer on the phone view, especially a chapter with code (Chapter 16).

KDP links the ebook and the paperback on one Amazon page automatically, usually within a few days.

## Step 4. The day it goes live

- [ ] **Amazon Author Central** (author.amazon.com): claim the book, add your photo and this bio:
  *Sridhar Mukkandi is an applied AI engineer who builds agents and the decision systems behind them. He writes for
  engineers who want AI systems they can trust.*
- [ ] **A+ Content** (KDP → Marketing → A+ Content, free): image panels under the description. Good ones for this
  book: the three-zone act / review / escalate figure, a page of a lab, and the key-ideas list.
- [ ] Add the Amazon link to the GitHub README, your LinkedIn profile and your email signature.

## Step 5. Getting the first readers and reviews

The first 10 honest reviews matter more than anything else.

- [ ] **Advance readers**: give the free PDF (`preview/Decide-Dont-Generate-COMPLETE.pdf`) to 15–20 people who
      will actually read it: classmates, seniors working in AI, professors, people from AI communities. Ask them to
      leave an honest review on Amazon once it's live. Never pay for reviews or swap them; Amazon removes them and
      can close accounts.
- [ ] **LinkedIn launch post** (the draft below), with a photo of the printed book or `marketing/mockup-3d.png`.
- [ ] **Show the work**: one short post a week for a month, each about one idea from the book (one figure + three
      lines). The 62 key ideas are ready-made topics.
- [ ] **GitHub**: the labs are free; a clear README with the book link brings readers from people who find the code.
- [ ] **Amazon Ads**: only after 3–5 reviews. Start at about $5 a day with automatic targeting, check weekly, stop
      keywords that cost more than they earn.
- [ ] **Kindle Countdown Deal** (KDP Select): after 30 days, the ebook at $2.99 for a week, announced on LinkedIn.

### LinkedIn launch post (edit it so it sounds like you)

> I wrote a book.
>
> It started with a question I kept running into while building AI agents: why do we ask a large language model to
> write a paragraph every time we just need a yes or no?
>
> Most of what an agent does is small decisions. Is this alert real? Which team gets this ticket? Is this action
> safe? *Decide, Don't Generate* is about doing those decisions properly: probabilities you can check, thresholds
> set by what mistakes cost, and agents that know when to ask a person.
>
> It has 22 chapters and 22 Python labs, and every example runs for free on a laptop. No API key needed.
>
> It's out now on Amazon, in paperback and on Kindle: [link]
>
> The code is open on GitHub: [link]
>
> If you read it, I'd really value an honest review. And if you're a student like me who wants to understand how
> AI systems actually make decisions, I wrote it for you.

## Later, if people ask

- **Black-and-white paperback** at $19.99–24.99: `print-bw/interior-bw.pdf` and `print-bw/cover-paperback-bw.pdf`,
  black and white ink, white paper. A cheaper option for students.
- **Hardcover**: premium colour, `print-color/interior-color.pdf` and `print-color/cover-hardcover-color.pdf`.
- **Your own ISBN** from isbn.gov.in, if you want to sell through other printers or bookshops.
