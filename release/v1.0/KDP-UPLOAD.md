# KDP upload sheet: *Decide, Don't Generate*

What to enter on each KDP screen, for the colour paperback, the hardcover, the black-and-white paperback and the
Kindle ebook. Screen and field names
follow KDP's setup flow as documented in its help pages; the KDP site couldn't be opened from this build, so if a
label differs, choose the closest match. Prices, dates and your account details are yours to fill.

## 1. Details (the same for every edition)

| Field | Enter |
|---|---|
| Language | English |
| Book title | Decide, Don't Generate |
| Subtitle | Jev, System One Models, and the Decision Layer of Agentic AI |
| Series | leave empty |
| Edition number | 1 |
| Author | Sridhar Mukkandi |
| Contributors | none |
| Publishing rights | I own the copyright and hold the necessary publishing rights |
| Primary audience | Not sexually explicit; reading age: leave blank or 18+ |
| Low-content book / Large print | No / No |

**Description.** Paste this into KDP's description box. KDP accepts these simple HTML tags (bold, lists, line
breaks); the store shows them as formatting. Every claim in it is true of the book.

```html
<b>Most of what an AI agent does isn't writing. It's deciding.</b><br><br>
Is this alert real? Which team gets this ticket? Is this action safe? Most agents hand every one of those small decisions to a large language model, then dig the answer out of a paragraph. It's slow, it's expensive, and the model sounds just as sure when it's wrong.<br><br>
<b>This book teaches the missing piece: the decision layer.</b> You'll learn to get probabilities you can trust, turn them into actions with thresholds set by real costs, and build agents where a fast decision model decides and the LLM only writes.<br><br>
<b>What you'll learn</b>
<ul>
<li>Check whether a model's probabilities are calibrated, and fix them when they aren't</li>
<li>Set act, review and escalate thresholds from what each mistake costs, and from how many people you have</li>
<li>Compare six ways to make the same decision, from hand-written rules to LLMs to a System One model</li>
<li>Build a hybrid agent, a production decision service, and your own small System One model</li>
<li>Run new systems in shadow mode, monitor drift, and give every failure a safe meaning</li>
</ul>
<b>What's inside</b>
<ul>
<li>22 chapters, from probability basics to production, written for students and engineers alike</li>
<li>22 runnable labs in Python, around one realistic (synthetic) security team</li>
<li>A free mock of the API: no API key, no cost, every example runs</li>
<li>138 figures, 62 key ideas, and a revision list of all of them at the back</li>
</ul>
<b>Who it's for:</b> students learning machine learning, engineers building AI agents, and tech leads deciding what to build. Basic Python is enough.<br><br>
<i>An independent guide. Not affiliated with TypeSafe AI.</i>
```

The plain-text version used before (no formatting) is in the repository history if KDP rejects the HTML.

**Keywords** (seven boxes, up to 50 characters each). These are phrases buyers type into Amazon's search; they
don't repeat words already in the title or subtitle, which Amazon searches anyway.

1. agentic AI agents for engineers
2. LLM agent architecture design patterns
3. probability calibration machine learning
4. AI decision making systems in production
5. human in the loop review thresholds
6. hands on AI engineering Python projects
7. cybersecurity SOC alert triage machine learning

Don't use other companies' product names as keywords unless the book is about them; "TypeSafe" is left out for
that reason.

**Categories** (KDP lets you choose three). One broad category for visibility and two smaller ones, where a new book
can reach the top of the list sooner. Pick the closest names KDP's picker shows:

1. Computers & Technology › Computer Science › AI & Machine Learning › Machine Learning
2. Computers & Technology › Computer Science › AI & Machine Learning › Expert Systems
3. Computers & Technology › Security & Encryption (the case study is a security team)

The back-cover category line is "Artificial Intelligence / Machine Learning".

## 1b. Prices (US store)

KDP's printing cost for 270 pages (Amazon.com): **premium colour $18.55**, **standard colour $7.88**, **black and
white $4.24** (fixed $1.00 plus $0.065, $0.0255 or $0.012 a page). Paperback royalty is 60% of the price minus
that cost.

| Edition | Price | Your royalty per copy |
|---|---:|---:|
| Kindle ebook (KDP Select on) | $9.99 | about $5.70 (70%, minus about $1.80 delivery for the 12 MB file) |
| Black-and-white paperback | $24.99 | $10.75 |
| Colour paperback, premium colour | $39.99 | $5.44 |
| Colour paperback, standard colour (option) | $34.99 | $13.11 |

Premium colour is expensive to print: below $30.92 KDP won't accept the price at all. Standard colour prints the
same figures on thinner paper with slightly less vivid ink, costs far less, and has the same paper thickness as the
black-and-white edition, so `print-bw/cover-paperback-bw.pdf` (spine 0.608 in) fits it. Choose premium colour only
if you want the best print quality. Set prices for amazon.in in rupees separately; KDP suggests them from the US
price.

## 2. AI-generated content (asked on the Details screen)

KDP asks whether the book contains AI-generated text, images or translations. It counts content as AI-generated if
an AI tool created it, even if you then edited it substantially; content you wrote yourself and only refined with an
AI tool counts as AI-assisted and needn't be disclosed. On that definition, here is how this book was made and the
honest answers:

- **Text: Yes, AI-generated.** The chapters were drafted with an AI model working to the author's specification:
  the author set the subject, structure, voice rules and honesty rules, chose what to keep, and reviewed and
  directed revisions; the model wrote the prose and code. Select the option that describes the text as generated by
  AI with extensive human editing, if KDP offers that level of detail.
- **Images: Yes, AI-generated.** No image generator was used: every figure is a chart or diagram drawn by Python
  code, and the cover is typographic layout drawn by code. But that code was written by the same AI model, and the
  cover design choices were made by it under the author's direction, so "Yes" is the safe and honest answer.
- **Translations: No.**

KDP doesn't show these answers to readers. If you'd like readers to know too, add a sentence to the preface or the
copyright page; that is your call and isn't in this build.

## 3. Paperback content

| Setting | Choose |
|---|---|
| Manuscript | `print-color/interior-color.pdf` |
| ISBN | Get a free KDP ISBN |
| Publication date | as you choose |
| Print options: ink and paper | **Premium colour ink, white paper** |
| Trim size | **7 × 10 in (17.78 × 25.4 cm)** |
| Bleed settings | **No bleed** |
| Paperback cover finish | **Matte** |
| Reading direction | Left to right |
| Book cover | Upload a cover you already have: `print-color/cover-paperback-color.pdf` |
| Barcode | Leave KDP's option to add the barcode on (the empty area is bottom right of the back cover) |
| AI-generated content | as section 2 |

KDP's previewer should report 270 pages and a spine of about 0.634 in. If it reports a different page count, stop:
the cover's spine was built for 270.

## 4. Hardcover content

| Setting | Choose |
|---|---|
| Manuscript | `print-color/interior-color.pdf` (same file) |
| ISBN | Get a free KDP ISBN (the hardcover gets its own, different from the paperback's) |
| Print options: ink and paper | **Premium colour ink, white paper** (the only colour option for hardcovers) |
| Trim size | **7 × 10 in** |
| Bleed settings | **No bleed** |
| Cover finish | **Matte** (case laminate) |
| Book cover | `print-color/cover-hardcover-color.pdf` |

KDP should report 270 pages and a spine of about 0.823 in.

## 4b. Black-and-white paperback (optional, cheaper to print)

The same book printed in black and white: the interior is already converted to true greyscale, and every figure,
box and zone was checked to read without colour (see `RELEASE.md`, "v1.0.3"). Only the cover prints in colour, as
it does for every KDP paperback. It is a separate paperback with its own ISBN.

| Setting | Choose |
|---|---|
| Manuscript | `print-bw/interior-bw.pdf` |
| ISBN | Get a free KDP ISBN (its own, different from the colour paperback's and the hardcover's) |
| Print options: ink and paper | **Black & white ink, white paper** |
| Trim size | **7 × 10 in** |
| Bleed settings | **No bleed** |
| Paperback cover finish | **Matte** |
| Book cover | `print-bw/cover-paperback-bw.pdf` (its spine is narrower: black-and-white paper is thinner) |
| Barcode | Leave KDP's option to add the barcode on |

KDP should report 270 pages and a spine of about 0.608 in (270 × 0.002252 in). Use this cover only with black-and-white
paper: on premium colour paper the spine would be 0.634 in and the cover wouldn't fit.

Two paperbacks of the same title sit side by side in the store, so make the difference visible to buyers, for
example by adding "Black and White Edition" in the edition or subtitle field. KDP's help pages couldn't be opened
from this build; check its current rule on listing two paperbacks of one book before you publish both.

## 5. Kindle ebook

| Setting | Choose |
|---|---|
| Manuscript | `ebook/book.epub` |
| Kindle eBook cover | Upload your cover file: `ebook/ebook-cover.jpg` (1600 × 2560 px) |
| DRM | your choice |
| ISBN | not needed for Kindle |
| AI-generated content | as section 2 |

Open the Kindle previewer after upload and page through a chapter with code (Chapter 16) and one with a wide table
(Chapter 13) on the phone view.

## 6. Which file goes where

| KDP screen | Field | File |
|---|---|---|
| Paperback content | Manuscript | `print-color/interior-color.pdf` |
| Paperback content | Cover | `print-color/cover-paperback-color.pdf` |
| Hardcover content | Manuscript | `print-color/interior-color.pdf` |
| Hardcover content | Cover | `print-color/cover-hardcover-color.pdf` |
| Black-and-white paperback content | Manuscript | `print-bw/interior-bw.pdf` |
| Black-and-white paperback content | Cover | `print-bw/cover-paperback-bw.pdf` |
| Kindle eBook content | Manuscript | `ebook/book.epub` |
| Kindle eBook content | Cover | `ebook/ebook-cover.jpg` |

Don't upload anything from `print-color/guides/`, `print-bw/guides/`, `preview/`, `marketing/` or `checks/`.
