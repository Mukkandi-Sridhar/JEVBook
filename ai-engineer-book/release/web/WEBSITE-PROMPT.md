# Prompt for the website session

Copy everything below the line into the Claude session that works on your website repository. First copy these
files from `ai-engineer-book/release/web/` into that repository (for example into `public/books/ship-real-ai/`):
`book.json`, `cover-1200.jpg`, `cover-600.webp`, `og-image.jpg`, `ship-real-ai-sample.pdf`.

---

Add my new book, **Ship Real AI**, to this website: a book landing page that ranks well in search, and a premium
in-browser reader for the free sample. Read the existing site first and match its framework, styling and
navigation; do not restyle the rest of the site.

## The book

All facts are in `book.json` (title, subtitle, author, edition, pages, description, five parts, 17 modules with their
section titles). Use only those facts. Do not invent reviews, ratings, sales numbers, prices or an ISBN: the ISBN is
pending, so leave a clearly marked placeholder for it and for the store links (Amazon paperback, Kindle, India
paperback) that I will fill in later.

- Title: Ship Real AI
- Subtitle: The AI Engineer Bootcamp for LLMs, RAG, MCP, AI Agents and Evals, from First Principles to Production
  and Interviews
- Author: Sridhar Mukkandi. Publisher: Mukkandi Sridhar (self-published). First edition, 2026. 193 pages, colour.
- Tagline: "Anyone can build the demo. This book is about what comes after."
- Images: `cover-1200.jpg` (front cover), `cover-600.webp` (smaller), `og-image.jpg` (1200 x 630 share image).

## 1. The book page (`/books/ship-real-ai`)

Sections, in this order:

1. **Hero**: cover with a soft shadow, title, subtitle, tagline, two buttons: "Read the free sample" (opens the reader)
   and "Get the book" (store links; placeholders for now).
2. **Who it is for**: beginners with Python, software engineers adding AI, data scientists moving to agents.
3. **What you will build**: one support assistant for an imagined Indian marketplace, grown module by module from a
   single model call to a production service.
4. **What makes it different**: one real system end to end; real industry terms and structures; numbers measured,
   costs in rupees; every code listing run before printing.
5. **Contents**: the five parts, each expandable to its modules and section titles, from `book.json`.
6. **Sample**: a large preview card that opens the reader.
7. **About the author**: "Sridhar Mukkandi is an applied AI engineer who builds AI agents and the decision systems
   behind them." Also link my other book, *Decide, Don't Generate*, if the site already has a page for it.
8. **FAQ** (5–6 real questions: Who is it for? Do I need a GPU? Which language is the code in? Is there a sample?
   Which formats? Does it help with interviews?), answered from the facts above.

Design: premium and calm, matching the cover (cream `#F4EFE3`, indigo `#10163A`, saffron `#E8780A`), generous
whitespace, excellent typography, smooth subtle animations, fully responsive, dark-mode aware, and accessible
(contrast AA, alt text, keyboard navigation, visible focus).

## 2. The reader (`/books/ship-real-ai/read`)

A custom, Kindle-like reading experience for `ship-real-ai-sample.pdf` (cover, front matter, preface and all of
Module 1), built with PDF.js (pin an exact version) and rendered on the client:

- Single page on phones, two-page spread on wide screens, with page-turn by swipe, arrow keys, click zones and
  buttons; a smooth page-turn animation that respects "reduce motion".
- A side panel with the table of contents (from the PDF outline) and a page-thumbnail strip.
- Zoom (fit width, fit page, + / −), full-screen, a progress bar with "page N of M", and "jump to page".
- Reading themes: light, sepia and dark (dark mode inverts page background and text but not figures and the cover).
- Remember the last page and theme in localStorage, with try/catch so it never breaks.
- Text search inside the sample.
- Fast: lazy-render only nearby pages, show a skeleton while loading, preload the next spread.
- At the end of the sample, an elegant "Continue reading" panel with the store links (placeholders).
- **Do not** offer the full book for free or put the full PDF anywhere public. Only the sample PDF is served.

## 3. SEO, done properly

- Unique `<title>` ("Ship Real AI: The AI Engineer Bootcamp for LLMs, RAG, MCP, AI Agents and Evals | Sridhar
  Mukkandi") and a meta description of about 155 characters written from the description in `book.json`.
- Canonical URL, Open Graph and Twitter card tags using `og-image.jpg`, `og:type=book`, `book:author`,
  `book:release_date`, `book:tag`.
- JSON-LD structured data: a `Book` (name, alternateName = subtitle, author `Person`, publisher, inLanguage,
  numberOfPages, bookFormat, image, description, about = the subjects, workExample for paperback and ebook with
  the ISBN placeholder left out until it exists), a `BreadcrumbList`, and an `FAQPage` matching the visible FAQ.
  Validate it in the format Google's Rich Results Test accepts. No fake reviews or ratings in the markup.
- Semantic HTML: one `<h1>`, headings in order, the contents as real lists, descriptive link text.
- Add the pages to `sitemap.xml` and make sure `robots.txt` allows them; the reader page can be `noindex` (the book
  page is the one to rank), but the sample PDF should be linked from the book page so it can be indexed.
- Performance for Core Web Vitals: responsive images (`srcset`, WebP), explicit width and height, lazy loading
  below the fold, preload the hero cover, no layout shift, minimal JavaScript on the book page (load PDF.js only on
  the reader page).
- Internal links: from the home page, the author or about page, and the other book's page to this book.
- Natural keywords in the visible copy (AI engineer, AI engineering book, LLMs, RAG, AI agents, MCP, evals, LLMOps,
  system design interview), never stuffed.

## 4. Finish

Build the site, fix any warnings, check the pages on a phone-sized and a desktop viewport, run Lighthouse and aim
for 95+ in Performance, Accessibility, Best Practices and SEO, then show me screenshots and the scores. Tell me
exactly which placeholders I need to fill in (ISBN, store links, prices). After it is deployed, I will submit the
sitemap in Google Search Console and Bing Webmaster Tools.
