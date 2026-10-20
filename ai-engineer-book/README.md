# The Applied AI Engineer: From Probability to Production Agents

A separate book project from *Decide, Don't Generate*. It has its own build, style guide, figures and references,
and shares nothing with the JEV book's chapters.

- Plan: `../plans/Next book plan.md` (10 parts, 38 chapters). Research: `../reports/AI engineer book plan research.md`.
- Style rules (lessons from the JEV drafts): `STYLE.md`. Check every chapter against them.
- Claims to check before print: `VERIFY.md`, plus `[[VERIFY]]` markers in the text.

## Status

| Part | Chapters | State |
|---|---|---|
| I. The job and the foundations | 1–5 | First draft |
| II–X | 6–38 | Planned |

## Build

```bash
python3 tools/build_figures.py all          # figures/src/cNN.py -> figures/cNN/*.pdf
quarto render --to pdf                      # -> _book/The-Applied-AI-Engineer.pdf
BOOK_DRAFT=1 quarto render --to pdf         # same, with [[VERIFY]] markers shown
```

Fonts: IBM Plex Serif, Work Sans and IBM Plex Mono (in assets/fonts). Devanagari text falls back to the FreeSans font (`fonts-freefont-ttf`), shaped with HarfBuzz.
